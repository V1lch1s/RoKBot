import pyautogui
import time
import win32api, win32con #pywin32


def rightClick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.001) #This pauses the script for 0.001 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

    
def leftClick(x,y):
    try:
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.001)  # This pauses the script for 0.001 seconds
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    except pywintypes.error:
        time.sleep(1)
