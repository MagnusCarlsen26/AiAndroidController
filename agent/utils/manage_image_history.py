def manage_chat_history(chat_history):
    image_messages = []
    for i, message in enumerate(chat_history):
        # Check if the message is a dictionary or a Content object
        if isinstance(message, dict):
            parts = message.get("parts", [])
        else:  # Assume it's a Content object if not a dict
            parts = getattr(message, "parts", [])

        if any(isinstance(part, dict) and "image_data" in part for part in parts):
            image_messages.append((i, message))

    if len(image_messages) > 2:
        for i in range(len(image_messages) - 2):
            idx, msg_obj = image_messages[i]
            # Access parts based on whether msg_obj is a dict or Content object
            if isinstance(msg_obj, dict):
                target_parts = msg_obj.get("parts", [])
            else:
                target_parts = getattr(msg_obj, "parts", [])

            for part in target_parts:
                if isinstance(part, dict) and "image_data" in part:
                    part["image_data"] = {}

    return chat_history
