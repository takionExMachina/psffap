from subprocess import Popen, PIPE
import os

os.chdir("C:\Windows\System32\drivers\etc")
command = "echo 127.0.0.1 google.com >> hosts"
CMD = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)

# 'uac_info':"requireAdministrator"

