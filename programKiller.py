import win32gui
import win32con
import time

def close_window(hwnd, extra):
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        if title and "task manager" not in title.lower():
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
            time.sleep(0.1)

win32gui.EnumWindows(close_window, None)
