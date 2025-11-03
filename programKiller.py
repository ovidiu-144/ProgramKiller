import os, signal
import win32gui
#import win32con
import win32process
import time

# win32process.GetWindowThreadProcessId trimite pid-ul
def win32gui_proces_list(process_list):
    pids = []
    for title, pid in process_list:
        if pid not in pids:
            os.kill(pid, signal.SIGTERM)
            pids.append(pid)
        print(f"Am inchis procesul {pid}")

pid_list = []
def get_process_list(hwnd, extra):

    title = win32gui.GetWindowText(hwnd)
    if win32gui.IsWindowVisible(hwnd) and title:
        print(f"Window: {title}")
        if title.__contains__("Program Manager"):
            print("Not This")
        else:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            pid_list.append((title, pid))
            print(pid)


def main():
    #Enumerates all top-level windows on the screen by passing the handle to each window, in turn, to an application-defined callback function.
    win32gui.EnumWindows(get_process_list, pid_list)
    print(pid_list)

    time.sleep(1)
    win32gui_proces_list(pid_list)


if __name__=="__main__":
    main()

