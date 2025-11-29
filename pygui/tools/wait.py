import time

def wait(payload: dict):
    sleep_duration = max(5,payload.get("sleep", 1) ) # Default to 1 second if not provided
    time.sleep(sleep_duration)
