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
    "tool_description": "scrolls in upward direction"
  },
  {
    "tool_name": "scrollDown",
    "tool_description": "scrolls in downards direction"
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
    "tool_name": "pressRecentApps",
    "tool_description": "Presses recent apps button"
  },
  {
    "tool_name": "getScreenshot",
    "tool_description": "gets screenshot of current view of phone"
  },
  {
    "tool_name": "wait",
    "tool_description": "waits for 1s. may be used when something is loading"
  },
  {
    "tool_name": "abort",
    "tool_description": "something went wrong or task can't be done or you don't know how to do it or if the task is completed."
  }
]
"""
