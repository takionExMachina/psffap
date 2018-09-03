
debug = Debug(MyEventHandler())
try:
    for (process, name) in debug.system.find_process_by_filename("firefox.exe"):
        print '[+] Found Firefox PID ' + str(process.get_pid())
        debug.attach(process.get_pid())
        debug.loop()

class MyEventHandler(EventHandler):
    def load_dll(self,event):
        module = event.get_module()
        if module.match_name("nss3.dll"):
            pid = event.get_pid()
            address = module.resolve("PR_Write")
            print '[+] Found PR_Write at addr ' + str(address)
            event.debug.hook_function(pid, address, preCB=PR_Write, postCB=None, paramCount=3, signature=None)

    def PR_Write(event, ra, arg1, arg2, arg3):
        print process.read(arg2, 1024)

