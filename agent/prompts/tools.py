TOOLS = """
[
  {
    "tool_name": "click",
    "tool_description": "Clicks at current cursor position",
    "payload" : {
      "horizantal" : int,
      "vertical" : int
    }
  },
  {
    "tool_name": "scrollUp",
    "tool_description": "scrolls in upward direction. Payload should be the coordinate where u want to keep your finger and scroll.",
    "payload" : {
      "horizantal" : int,
      "vertical" : int,
    }
  },
  {
    "tool_name": "scrollDown",
    "tool_description": "scrolls in downards direction. Payload should be the coordinate where u want to keep your finger and scroll.",
    "payload" : {
      "horizantal" : int,
      "vertical" : int,
    }
  },
  {
    "tool_name": "pressBack",
    "tool_description": "Presses back button"
  {
    "tool_name": "pressHome",
    "tool_description": "Presses home button"
  },
  {
    "tool_name": "pressRecentApps",
    "tool_description": "Presses recent apps button"
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