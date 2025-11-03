import os, signal

import win32gui
import win32con
import win32process
import psutil
import time
# creare mic gui in care aleg 1 sau 2



# win32process.GetWindowThreadProcessId trimite pid-ul
def kill_proces_list(process_list):
    pids = []
    for title, pid in process_list:
        if pid not in pids:
            os.kill(pid, signal.SIGTERM)
            pids.append(pid)
        print(f"Am inchis procesul {pid}")



pid_list = []
def get_process_list(hwnd, extra):
    SYSTEM_PROCESSES = [
                "taskmgr.exe", "explorer.exe", "wininit.exe", "winlogon.exe", "services.exe", "lsass.exe", "csrss.exe", "smss.exe"
            ]
    title = win32gui.GetWindowText(hwnd)
    if win32gui.IsWindowVisible(hwnd) and title:

        #   or title.__contains__("Edge")
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        proc = psutil.Process(pid)
        process_name = proc.name().lower()

        print(f"Window: {title} {process_name}")
        if process_name in SYSTEM_PROCESSES:
            print(f"Not This -> {process_name} and {pid}")
        else:
            #win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

            pid_list.append((title, pid))
            print(pid)


def main():
    #Enumerates all top-level windows on the screen by passing the handle to each window, in turn, to an application-defined callback function.
    win32gui.EnumWindows(get_process_list, pid_list)
    print(pid_list)

    time.sleep(2)
    kill_proces_list(pid_list)


if __name__=="__main__":
    main()
