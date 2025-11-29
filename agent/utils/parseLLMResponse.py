import json

def parseLLMResponse(response: str):

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return None
