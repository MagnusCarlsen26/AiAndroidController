import os

# Clear the log file at the start of each run
if os.path.exists("agent_log.txt"):
    open("agent_log.txt", "w").close()

from pygui.utils.getScreenshot import getScreenshot
from agent.utils.addCoordinateGrid import addCoordinateGrid
from service.geminiApi import geminiApi
from .prompts.systemPrompt import SYSTEM_PROMPT
from .utils.parseLLMResponse import parseLLMResponse

from pygui.tools.click import click
from pygui.tools.abort import abort
from pygui.tools.getScreenshotTool import getScreenshotTool
from pygui.tools.pressBack import pressBack
from pygui.tools.pressHome import pressHome
from pygui.tools.pressRecentApps import pressRecentApps
from pygui.tools.scrollDown import scrollDown
from pygui.tools.scrollUp import scrollUp
from pygui.tools.wait import wait
from pygui.tools.types import types

import pprint
import time
import sys
import io
import json

TOOLS = [
    click,
    abort,
    getScreenshotTool,
    pressBack,
    pressHome,
    pressRecentApps,
    scrollDown,
    scrollUp,
    wait,
    types
]

chatHistory = []

TASK = """
Please order Mysore Masala Dosa for me. I am starving bro.
I will only eat from swiggy no other app.
"""
MODEL = "gemini-2.5-flash"

while True:

    screenshot = addCoordinateGrid(getScreenshot(), save=True)

    chat = geminiApi(
        TASK,
        SYSTEM_PROMPT,
        MODEL,
        imageData=screenshot["screenshot"],
        chatHistory=chatHistory
    )

    response = parseLLMResponse(chat[0])
    chatHistory = chat[1]

    old_stdout = sys.stdout
    redirected_output = io.StringIO()
    pprint.pprint(response) # Commented out pprint

    with open("agent_log.txt", "a") as f:
        f.write(json.dumps(response, indent=2) + "\n")

    for tool in TOOLS:
        if tool.__name__ == response["toolName"]:
            try:
                if 'payload' in response:

                    if tool.__name__ == "click":
                        addCoordinateGrid(getScreenshot(), marks=[(response["payload"]["horizantal"], response["payload"]["vertical"])], save=True)

                    response["payload"]["imageMeta"] = screenshot["imageMeta"]
                    tool(response["payload"])
                else:
                    tool()    
            except Exception as e:
                error_message = f"An error occurred while executing tool {response["toolName"]}: {e}. Your previous tool call was likely incorrect. Please try again by properly calling your tools."
                print(error_message)
                chatHistory.append({"role": "model", "parts": [{"text": json.dumps(response)}]})
                chatHistory.append({"role": "user", "parts": [{"text": error_message}]})
                break # Break out of the for loop to re-evaluate with the LLM

    time.sleep(1)