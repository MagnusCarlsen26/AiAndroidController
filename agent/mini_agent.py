import json

from service.chatgptAPI import chatgptApi
from agent.utils.parseLLMResponse import parseLLMResponse
from pygui.tools.verify_coordinate import verify_coordinate
from pygui.tools.abort import abort
from agent.utils.addCoordinateGrid import addCoordinateGrid
from pygui.utils.getScreenshot import getScreenshot
from agent.utils.manage_image_history import manage_chat_history
from agent.prompts.mini_agent_prompts import (
    MINI_AGENT_SYSTEM_PROMPT,
    MINI_AGENT_COORDINATE_SYSTEM_PROMPT,
    MINI_AGENT_QUADRANT_TOOLS,
    MINI_AGENT_COORDINATE_TOOLS,
    MINI_AGENT_USER_MESSAGE_TEMPLATE
)
from agent.utils.splitImage import split_image_into_quadrants

MODEL = "gpt-5-mini"
MAX_ATTEMPTS = 5

def search_target_in_quadrants(
    element_description: str,
    image,
    offset_x: int,
    offset_y: int,
    depth: int,
    mini_agent_chat_history
):
    print(offset_x, offset_y)
    if depth >= 2:
        # If max depth is reached, proceed with the original mini-agent logic
        return find_coordinates_in_image(
            element_description, 
            image, 
            offset_x, 
            offset_y
        )

    quadrants = split_image_into_quadrants(image)
    
    for q_name, q_image in quadrants.items():
        print(f"[Mini-Agent] Checking {q_name} at depth {depth}")
        
        # Determine new offset for the quadrant
        new_offset_x, new_offset_y = offset_x, offset_y
        if q_name == "quadrant2":
            new_offset_x += image.size[0] // 2
        elif q_name == "quadrant3":
            new_offset_y += image.size[1] // 2
        elif q_name == "quadrant4":
            new_offset_x += image.size[0] // 2
            new_offset_y += image.size[1] // 2

        # Query LLM to check if target is present in this quadrant
        user_message = MINI_AGENT_USER_MESSAGE_TEMPLATE.format(element_description=element_description, quadrant_check_message="Is it present in this quadrant? ")
        chat = chatgptApi(
            user_message,
            MINI_AGENT_SYSTEM_PROMPT + MINI_AGENT_QUADRANT_TOOLS,
            model=MODEL,
            imageData=addCoordinateGrid(q_image, save=True, x_offset=new_offset_x, y_offset=new_offset_y)["screenshot"],
            chatHistory=manage_chat_history(mini_agent_chat_history)
        )
        response = parseLLMResponse(chat[0])
        print(response)
        mini_agent_chat_history = chat[1]

        if response['toolName'] == "targetPresent":
            if response['payload']['present']:
                print(f"[Mini-Agent] Target found in {q_name}. Recursing...")
                result = search_target_in_quadrants(
                    element_description, 
                    q_image, 
                    new_offset_x, 
                    new_offset_y, 
                    depth + 1, 
                    mini_agent_chat_history
                )
                if result:
                    return result
                break
            else:
                print(f"[Mini-Agent] Target not present in {q_name}. Continuing search...")
        elif response['toolName'] == "abort":
            print(f"[Mini-Agent] LLM aborted for {q_name}. Continuing search...")
            continue # Continue to next quadrant
        else:
            print(f"[Mini-Agent] Unexpected tool call from LLM: {response['toolName']}. Aborting search in this branch.")
            # This can happen if the LLM tries to verify coordinates when it should be checking for presence.
            # For now, we'll just continue, but this might need more robust error handling.
            continue

    return None # Target not found in any quadrant at this depth

def find_coordinates_in_image(
    element_description: str,
    image,
    offset_x: int,
    offset_y: int,
):
    attempts = 0
    
    while attempts < MAX_ATTEMPTS:
        # Calculate absolute bounds for the current image/quadrant
        min_x, min_y = offset_x, offset_y
        max_x, max_y = offset_x + image.size[0], offset_y + image.size[1]
        print(f"[Mini-Agent] Current image bounds: min_x={min_x}, min_y={min_y}, max_x={max_x}, max_y={max_y}")
        
        formatted_coordinate_system_prompt = MINI_AGENT_COORDINATE_SYSTEM_PROMPT.format(
            min_x=min_x, min_y=min_y, max_x=max_x, max_y=max_y, max_attempts=MAX_ATTEMPTS
        )
        user_message = MINI_AGENT_USER_MESSAGE_TEMPLATE.format(element_description=element_description, quadrant_check_message="")
        chat = chatgptApi(
            user_message,
            formatted_coordinate_system_prompt + MINI_AGENT_COORDINATE_TOOLS,
            model=MODEL,
            imageData=addCoordinateGrid(image, save=True, x_offset=offset_x, y_offset=offset_y)["screenshot"],
        )
        response = parseLLMResponse(chat[0])

        tool_name = response['toolName']
        payload = response.get("payload", {})

        if tool_name == "verifyCoordinates":
            print(f"[Mini-Agent] Calling verify_coordinate with x={payload["horizontal"]}, y={payload["vertical"]}")
            result = verify_coordinate(payload["horizontal"], payload["vertical"])
            print(f"[Mini-Agent] verify_coordinate returned. Result: {result}")
            attempts += 1
        elif tool_name == "verifiedClick":
            print(f"[Mini-Agent] Verified click. Returning coordinates: horizontal={payload["horizontal"]}, vertical={payload["vertical"]}")
            return payload["horizontal"], payload["vertical"]
        elif tool_name == "abort":
            abort(payload.get("message", "Mini-agent aborted due to unspecified reason."))
            break
        else:
            error_message = f"Mini-agent called an unexpected tool: {tool_name}. Aborting."
            abort(error_message)
            break
    
    abort(f"Mini-agent failed to verify coordinates after {MAX_ATTEMPTS} attempts for: {element_description}.")

def run_mini_agent(element_description: str):
    print(f"[Mini-Agent] Starting for element: {element_description}")
    mini_agent_chat_history = []
    initial_screenshot = getScreenshot()
    
    result = search_target_in_quadrants(element_description, initial_screenshot, 0, 0, 0, mini_agent_chat_history)

    if result:
        log_entry = {
            "stage": "final_result",
            "element_description": element_description,
            "coordinates": result,
            "message": "Successfully found coordinates after recursive search."
        }
        with open("agent_log.txt", "a") as f:
            f.write(json.dumps(log_entry, indent=2) + "\n")
        return result
    else:
        log_entry = {
            "stage": "final_abort",
            "element_description": element_description,
            "message": f"Mini-agent failed to find element: {element_description} after recursive search."
        }
        with open("agent_log.txt", "a") as f:
            f.write(json.dumps(log_entry, indent=2) + "\n")
        abort(f"Mini-agent failed to find element: {element_description} after recursive search.")
