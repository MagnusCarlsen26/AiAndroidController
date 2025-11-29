import json

def parseLLMResponse(response: str):

    try:
        return json.loads(response.strip("```").strip("json"))
    except Exception as e:
        print("Error occured while parsing LLM repsonse. LLM repsonse -")
        print(response)
        return None
