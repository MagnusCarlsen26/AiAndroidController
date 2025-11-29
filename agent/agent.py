from pygui.utils.getScreenshot import getScreenshot
from agent.utils.addCoordinateGrid import addCoordinateGrid
from service.geminiApi import geminiApi
from .prompts.systemPrompt import SYSTEM_PROMPT
from .utils.parseLLMResponse import parseLLMResponse

from pygui.tools.click import click

TOOLS = [
    click
]

while True:

    screenshot = addCoordinateGrid(getScreenshot(), save=True)

    chat = geminiApi(
        "Like this video",
        SYSTEM_PROMPT,
        "gemini-2.0-flash",
        imageData=screenshot["screenshot"]
    )

    response = parseLLMResponse(chat[0])
    print(response)
    for tool in TOOLS:
        if tool.__name__ == response["toolName"]:
            if 'payload' in response:
                response["payload"]["imageMeta"] = screenshot["imageMeta"]
                tool(response["payload"])
            else:
                tool()    
    # For now break immediately
    break