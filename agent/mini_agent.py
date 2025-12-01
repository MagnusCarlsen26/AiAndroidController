import os
import sys
import io
import json
import pprint

from service.chatgptAPI import chatgptApi
from agent.utils.parseLLMResponse import parseLLMResponse
from pygui.tools.verify_coordinate import verify_coordinate
from pygui.tools.abort import abort
from agent.utils.addCoordinateGrid import addCoordinateGrid
from pygui.utils.getScreenshot import getScreenshot
from agent.utils.manage_image_history import manage_chat_history
from agent.prompts.mini_agent_prompts import MINI_AGENT_SYSTEM_PROMPT, MINI_AGENT_TOOLS, MINI_AGENT_USER_MESSAGE_TEMPLATE

MODEL = "gpt-5-mini"
MAX_ATTEMPTS = 20

def run_mini_agent(element_description: str):
    print(f"[Mini-Agxxent] Starting for element: {element_description}")
    mini_agent_chat_history = []
    attempts = 0

    while attempts < MAX_ATTEMPTS:

        user_message = MINI_AGENT_USER_MESSAGE_TEMPLATE.format(element_description=element_description)
        
        chat = chatgptApi(
            user_message,
            MINI_AGENT_SYSTEM_PROMPT + MINI_AGENT_TOOLS,
            model=MODEL,
            imageData=addCoordinateGrid(getScreenshot(), save=True)["screenshot"],
            chatHistory=manage_chat_history(mini_agent_chat_history)
        )

        response = parseLLMResponse(chat[0])
        mini_agent_chat_history = chat[1]

        with open("agent_log.txt", "a") as f:
            f.write(json.dumps(response, indent=2) + "\n")

        tool_name = response['toolName']
        payload = response.get("payload", {})

        if tool_name == "verifyCoordinates":
            print(f"[Mini-Agent] Calling verify_coordinate with horizontal={payload["horizontal"]}, vertical={payload["vertical"]}")
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
