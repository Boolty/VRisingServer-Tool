import psutil
import time
import os
import ctypes
import threading
from datetime import datetime


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def launch():
    print('Starting VRisingServer...')
    print('Version: 1.3')
    os.system('VRisingServer.exe')
    time.sleep(20)

def main():
    print('Stop the Server tool with STRG+C')
    ctypes.windll.kernel32.SetConsoleTitleW("VRisingServerTool by Boolty")
    time.sleep(3)
    PROCNAME = 'VRisingServer.exe'
    restart = '03:00'
    while True:
        if checkIfProcessRunning(PROCNAME):
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            print("Server Time:", current_time, ' | Server is running...')
            if current_time == restart:
                print('Process was killed...')
                for proc in psutil.process_iter():
                    if proc.name() == PROCNAME:
                        proc.kill()
            time.sleep(20)
        else:
            print('VRisingServer will not run...')
            print('Starting VRisingServer...')      
            threading.Thread(target=launch).start()  
            time.sleep(10)


if __name__ == '__main__':
    main()
