from .currMouseCoordinates import currMouseCoordinates
from pynput import mouse
import time

def getTargetCoordinates(
    targetName: str,
) -> tuple[int | None, int | None]:

    print(f"Move your mouse over {targetName}. Then press left click to register.")
    
    onTargetClick, isClicked = getOnTargetClick()
    listener = mouse.Listener(on_click=onTargetClick)
    listener.start()

    while not isClicked[0]:
        time.sleep(0.1)

    currMouseX, currMouseY = currMouseCoordinates()
    print(currMouseX, currMouseY)
    listener.stop()
    listener.join()
    
    return currMouseX, currMouseY

def getOnTargetClick():

    isClicked = [False]

    def onTargetClick(x, y, button, isPressed) -> None:

        isClicked[0] = True

    return onTargetClick, isClicked
