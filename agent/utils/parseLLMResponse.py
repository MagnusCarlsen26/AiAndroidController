import json
import re

def parseLLMResponse(response: str):

    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", response, re.IGNORECASE)
    json_str = None
    if match:
        json_str = match.group(1)
    else:
        # Try to find the first valid JSON object if not in markdown
        match = re.search(r'({[\s\S]*})', response)
        if match:
            json_str = match.group(1)
        else:
            json_str = response  # Last resort

    try:
        return json.loads(json_str)
    except Exception as e:
        print("Error occured while parsing LLM response. LLM response -")
        print(response)
        return None
