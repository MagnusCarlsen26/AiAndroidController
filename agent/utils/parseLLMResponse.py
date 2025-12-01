import json
import re
import ast

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
    except json.JSONDecodeError:
        try:
            # Clean up the string by removing extra quotes around keys
            cleaned_json_str = re.sub(r"\'(\w+)\':", r"\"\\1\":", json_str) # Replace single quoted keys with double quoted keys for json.loads
            return json.loads(cleaned_json_str)
        except json.JSONDecodeError:
            try:
                # Attempt to parse as a Python literal (dictionary string representation)
                parsed_dict = ast.literal_eval(json_str)
                return parsed_dict
            except (ValueError, SyntaxError) as e:
                print(f"Error occured while parsing LLM response with ast.literal_eval. Error: {e}")
                print("LLM response -")
                print(response)
                return None
    except Exception as e:
        print(f"Error occured while parsing LLM response. Error: {e}")
        print("LLM response -")
        print(response)
        return None
