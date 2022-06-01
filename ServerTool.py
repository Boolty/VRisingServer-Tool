import psutil
import time
import os
import ctypes
import threading
from datetime import datetime


PROCNAME = 'VRisingServer.exe'

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
    print('Version: 1.4')
    global PROCNAME
    os.system(PROCNAME)
    time.sleep(20)
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.nice(psutil.REALTIME_PRIORITY_CLASS)

def up():
    global PROCNAME
    while True:
        time.sleep(60)
        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
                proc.nice(psutil.REALTIME_PRIORITY_CLASS)

def main():
    global PROCNAME
    print('Stop the Server tool with STRG+C')
    ctypes.windll.kernel32.SetConsoleTitleW("VRisingServerTool by Boolty")
    off = True
    time.sleep(3)
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
            time.sleep(40)
        else:
            print('VRisingServer will not run...')
            print('Starting VRisingServer...')      
            threading.Thread(target=launch).start()  
            if off == True:
                threading.Thread(target=up).start()  
                off = False 
            time.sleep(10)


if __name__ == '__main__':
    main()
