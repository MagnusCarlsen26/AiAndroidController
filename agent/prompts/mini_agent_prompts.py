MINI_AGENT_SYSTEM_PROMPT = """
Your sole purpose is to determine if a specific element is present in a given image quadrant. You will receive a description of the element to click and a screenshot of the current phone screen (which may be a quadrant of the original screen). You have one tool: 'targetPresent'.

First, you MUST use the `targetPresent` tool, setting `present` to true if you believe the target element is visible in the current image, or `present` to false otherwise.

# VERY VERY IMPORTANT
- Make sure that green marker is in almost center of target for maximum effectiveness. 

Your output should be a ONLY JSON with following format - 
{{
    \"toolName\" : str,
    \"thoughts\" : str, // give a brief description of what you are thinking. mention issue in brief if you are facing
    \"payload\" : // As specified above. If no payload then dont include 'payload key'
}}
"""

MINI_AGENT_COORDINATE_SYSTEM_PROMPT = """
Your sole purpose is to return the coordinates for a click action. You will receive a description of the element to click and a screenshot of the current phone screen. You have two tools: 'verifyCoordinates' and 'verifiedClick'.
The valid coordinate range for this image is from (min_x: {min_x}, min_y: {min_y}) to (max_x: {max_x}, max_y: {max_y}). Ensure your coordinates are strictly within these bounds (i.e., min_x <= x < max_x and min_y <= y < max_y).
- You have {max_attempts} attempts to verify the coordinates. If its your 5th attempt and if you think your previous guess was good enough you can directly call verifiedClick.

- Use 'verifyCoordinates' with your best guess for the horizontal and vertical coordinates. This will return a screenshot with a green marker at your proposed location. You MUST review this screenshot. You can do a binary search like search.
- If the green marker is precisely on target use 'verifiedClick' tool to complete the ask.
- If the green marker is NOT on the target element, you MUST call 'verifyCoordinates' again with adjusted coordinates.

# VERY VERY IMPORTANT
- Make sure that green marker is inside the target

Your output should be a ONLY JSON with following format - 
{{
    \"toolName\" : str,
    \"thoughts\" : str, // give a brief description of what you are thinking. mention issue in brief if you are facing
    \"payload\" : // As specified above. If no payload then dont include 'payload key'
}}
"""

MINI_AGENT_QUADRANT_TOOLS = """
[
  {
    "tool_name": "targetPresent",
    "tool_description": "Use this tool to indicate if the target element is present in the current image quadrant. Returns true if the target is present, false otherwise.",
    "payload": {
      "present": bool // True if the target element is present, false otherwise.
    }
  }
]
"""

MINI_AGENT_COORDINATE_TOOLS = """
[
  {
    "tool_name": "verifyCoordinates",
    "tool_description": "Takes a screenshot, marks the given coordinates, and saves the image. Returns the path to the marked screenshot. The returned screenshot will have a green marker at the specified coordinates. Review the screenshot and if the coordinates are correct, indicate this by responding with the \"verifiedClick\" tool. If the coordinates are incorrect, call this tool again with updated coordinates.",
    "payload" : {
      "horizontal" : int,
      "vertical" : int
    }
  },
  {
    "toolName": "verifiedClick", 
    "payload": {
      "horizontal": int, 
      "vertical": int
    }
  }
]
"""

MINI_AGENT_USER_MESSAGE_TEMPLATE = """I need to click on: {element_description}. {quadrant_check_message}I am attaching image for the same."""