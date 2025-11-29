from pygui.utils.getScreenshot import getScreenshot
from agent.utils.addCoordinateGrid import addCoordinateGrid
from service.geminiApi import geminiApi
from .prompts.systemPrompt import SYSTEM_PROMPT

print(geminiApi(
    "Tell me the coordiante i should click so that like button is triggered.",
    SYSTEM_PROMPT,
    "gemini-2.0-flash",
    imageData=addCoordinateGrid(getScreenshot())
))
