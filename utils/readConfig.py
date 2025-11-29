import json

def readConfig(filePath: str = "userConfig.json"):

    with open(filePath, 'r') as f:
        config = json.load(f)

    return config
