import os, signal

import win32gui
import win32con
import win32process

import time
# creare mic gui in care aleg 1 sau 2



# win32process.GetWindowThreadProcessId trimite pid-ul
def win32gui_proces_list(process_list):
    pids = []
    for title, pid in process_list:
        if pid not in pids:
            os.win32gui(pid, signal.SIGTERM)
            pids.append(pid)
        print(f"Am inchis procesul {pid}")


pid_list = []
def get_process_list(hwnd, extra):

    title = win32gui.GetWindowText(hwnd)
    if win32gui.IsWindowVisible(hwnd) and title:
        print(f"Window: {title}")
        #  or title.__contains__("win32guier") or title.__contains__("Edge")
        if title.__contains__("Program Manager"):
            print("Not This")
        else:
            #win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
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

    #
    # def win32gui_process ():
    #     SYSTEM_PROCESSES = [
    #         "explorer.exe", "wininit.exe", "winlogon.exe", "services.exe", "lsass.exe", "csrss.exe", "smss.exe", "System", "Idle"
    #     ]
    #     f = wmi.WMI()
    #
    #     # Printing the header for the later columns
    #     print("pid   Process name")
    #
    #     # Iterating through all the running processes
    #     for process in f.Win32_Process():
    #         # Displaying the P_ID and P_Name of the process
    #         print(f"{process.ProcessId:<10} {process.Name}")
    #         if process.Name not in SYSTEM_PROCESSES:
    #             os.win32gui(process.ProcessId, signal.SIGwin32gui)

    # def close_windows (hwnd, extra):
    #     title = win32gui.GetWindowText(hwnd)
    #     if win32gui.IsWindowVisible(hwnd) and title:
    #         print (f"Window: {title}")
    #         if title.__contains__("Program Manager") or title.__contains__("win32guier") or title.__contains__("Edge"):
    #             print("nu inchidem astea")
    #         else:
    #             win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
    # win32gui_process()