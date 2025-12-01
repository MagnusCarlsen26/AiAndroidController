TOOLS = """
[
  {
    "tool_name": "click",
    "tool_description": "You need to describe what you want to click and where you want to click. Send description of this as payload.",
    "payload" : {
      "description" : str,
      "horizontal" : int,
      "vertical" : int
    }
  },
  {
    "tool_name": "scrollUp",
    "tool_description": "scrolls in upward direction. Payload should be the coordinate where u want to keep your finger and scroll.",
    "payload" : {
      "horizontal" : int,
      "vertical" : int,
    }
  },
  {
    "tool_name": "scrollDown",
    "tool_description": "scrolls in downards direction. Payload should be the coordinate where u want to keep your finger and scroll.",
    "payload" : {
      "horizontal" : int,
      "vertical" : int,
    }
  },
  {
    "tool_name": "pressBack",
    "tool_description": "Presses back button"
  },
  {
    "tool_name": "pressHome",
    "tool_description": "Presses home button"
  },
  {
    "tool_name": "getScreenshot",
    "tool_description": "gets screenshot of current view of phone"
  },
  {
    "tool_name": "wait",
    "tool_description": "waits for some secs. may be used when something is loading",
    "payload" : {
      "sleep" : int // in secs
    }
  },
  {
    "tool_name": "types",
    "tool_description": "Types the given text using the keyboard.",
    "payload" : {
      "text" : str // The text to be typed
    }
  },

  {
    "tool_name": "unlockPhone",
    "tool_description": "if you think phone is locked, then use this tool to unlock."
  }
]
"""

  # {
  #   "tool_name": "abort",
  #   "tool_description": "something went wrong or task can't be done or you don't know how to do it or if the task is completed. Try 10 times if you are not able to do it"
  # },
  # {
  #   "tool_name": "pressRecentApps",
  #   "tool_description": "Presses recent apps button"
  # },
  # {
  #   "tool_name": "verifyCoordinates",
  #   "tool_description": "Takes a screenshot, marks the given coordinates, and saves the image. Returns the path to the marked screenshot. This tool MUST be called before any 'click' action to verify the coordinates. The returned screenshot will have a green marker at the specified coordinates. Review the screenshot and if the coordinates are correct, call the 'click' tool with the same coordinates. If the coordinates are incorrect, call this tool again with updated coordinates.",
  #   "payload" : {
  #     "horizantal" : int,
  #     "vertical" : int
  #   }
  # },