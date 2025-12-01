import os

# Clear the log file at the start of each run
if os.path.exists("agent_log.txt"):
    open("agent_log.txt", "w").close()

from pygui.utils.getScreenshot import getScreenshot
from agent.utils.addCoordinateGrid import addCoordinateGrid
from service.geminiApi import geminiApi
from .prompts.systemPrompt import SYSTEM_PROMPT
from .utils.parseLLMResponse import parseLLMResponse
from .utils.manage_image_history import manage_chat_history

from pygui.tools.click import click
from pygui.tools.getScreenshotTool import getScreenshotTool
from pygui.tools.pressBack import pressBack
from pygui.tools.pressHome import pressHome
from pygui.tools.pressRecentApps import pressRecentApps
from pygui.tools.scrollDown import scrollDown
from pygui.tools.scrollUp import scrollUp
from pygui.tools.wait import wait
from pygui.tools.types import types
from agent.mini_agent import run_mini_agent

import pprint
import time
import sys
import io
import json

TOOLS = [
    click,
    getScreenshotTool,
    pressBack,
    pressHome,
    pressRecentApps,
    scrollDown,
    scrollUp,
    wait,
    types,
]

chatHistory = []

TASK = """
Please order Mysore Masala Dosa for me. I am starving bro.
I will only eat from swiggy no other app.
"""
MODEL = "gemini-2.5-flash"
while True:

    print("Starting agent loop...")
    screenshot = addCoordinateGrid(getScreenshot(), save=True)
    print("Screenshot captured and grid added.")

    chat = geminiApi(
        TASK,
        SYSTEM_PROMPT,
        MODEL,
        imageData=screenshot["screenshot"],
        chatHistory=manage_chat_history(chatHistory)
    )

    response = parseLLMResponse(chat[0])
    chatHistory = chat[1]

    print(f"LLM Response: {response}")

    if response is None:
        error_message = "Error: LLM returned an unparseable response. Please ensure your response is a valid JSON."
        print(error_message)
        chatHistory.append({"role": "user", "parts": [{"text": error_message}]})
        continue

    old_stdout = sys.stdout
    redirected_output = io.StringIO()
    pprint.pprint(response) # Commented out pprint

    with open("agent_log.txt", "a") as f:
        f.write(json.dumps(response, indent=2) + "\n")

    for tool in TOOLS:
        if tool.__name__ == response["toolName"]:
            print(f"Executing tool: {response['toolName']}")
            try:
                if 'payload' in response:

                    if tool.__name__ == "click":
                        element_description = response["payload"]["description"]
                        print(f"Running mini-agent for element: {element_description}")
                        x, y = run_mini_agent(element_description)
                        print(f"Mini-agent returned coordinates: x={x}, y={y}")
                        # Now that coordinates are verified, perform the click
                        click({"horizontal": x, "vertical": y, "imageMeta": screenshot["imageMeta"]})
                        print(f"Click tool executed with coordinates: x={x}, y={y}")
                    else:
                        response["payload"]["imageMeta"] = screenshot["imageMeta"]
                        tool(response["payload"])
                        print(f"Tool {response['toolName']} executed with payload.")
                else:
                    tool()
                    print(f"Tool {response['toolName']} executed without payload.")
            except Exception as e:
                print(f"DEBUG: response['toolName'] type: {type(response['toolName'])}, value: {repr(response['toolName'])}")
                print(f"DEBUG: Exception type: {type(e)}, value: {repr(e)}")
                error_message = f"An error occurred while executing tool {repr(response['toolName'])}: {repr(e)}. Your previous tool call was likely incorrect. Please try again by properly calling your tools."
                print(error_message)
                chatHistory.append({"role": "model", "parts": [{"text": json.dumps(response)}]})
                chatHistory.append({"role": "user", "parts": [{"text": error_message}]})
                
                exit()

    time.sleep(1)