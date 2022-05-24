import psutil
import time
import os
import ctypes


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

def main():
    print('Stop the Server tool with STRG+C')
    ctypes.windll.kernel32.SetConsoleTitleW("VRisingServerTool by Boolty")
    time.sleep(3)
    while True:
        if checkIfProcessRunning('VRisingServer'):
            print('is runnuning...')
            time.sleep(1)
        else:
            print('VRisingServer will not run...')
            print('Starting VRisingServer...')
            os.system('VRisingServer.exe')
            time.sleep(20)


if __name__ == '__main__':
    main()