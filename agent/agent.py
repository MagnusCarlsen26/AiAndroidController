from pygui.utils.getScreenshot import getScreenshot
from service.geminiApi import geminiApi
from prompts.systemPrompt import SYSTEM_PROMPT

print(geminiApi(
    "what do you see?",
    SYSTEM_PROMPT,
    imageData=getScreenshot()
))
