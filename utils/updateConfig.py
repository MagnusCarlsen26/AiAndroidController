from .readConfig import readConfig
import json

def updateConfig(
    newKey: dict, 
    filePath: str = "userConfig.json"
):

    config = readConfig()
    config.update(newKey)

    with open(filePath, 'w') as f:
        json.dump(config, f, indent=4)
