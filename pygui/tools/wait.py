import time

def wait(payload: dict):
    sleep_duration = payload.get("sleep", 1)  # Default to 1 second if not provided
    time.sleep(sleep_duration)
