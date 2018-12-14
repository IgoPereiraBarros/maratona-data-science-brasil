# -*- coding: utf-8 -*-

import sys
import os
import string
import cgi
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

class Http(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith(".html"):
                f = open(DocumentRoot + self.path)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return

            if self.path.endswith(".esp"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('hey, today is the' + str(time.localtime()[7]))
                self.wfile.write(' day in the year' + str(time.localtime()[0]))
                return
        except IOError as e:
            self.send_error(404, 'File Not Found: {}'.format(self.path))

    def do_POST(self):
        global rootnode

        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multpart/form-data':
                query=cgi.parse_multipart(self.rfile, pdict)
            self.send_response(301)

            self.end_headers()
            upfilecontent = query.get('upfile')
            print('Filecontent', upfilecontent[0])
            self.wfile.write('<html>Post Ok. <br />');
            self.wfile.write(upfilecontent[0]);
            self.wfile.write('</html>')
        except:
            pass

def main(nameVirtualHost):

    try:
        virtualhost = str.split(nameVirtualHost, ':')
        if virtualhost[0] == '+':
            virtualhost[0] = ""

        server = HTTPServer((virtualhost[0], int(virtualhost[1])), Http)
        print('Start server HTTP in {}'.format(nameVirtualHost))
        server.serve_forever()
    except KeyboardInterrupt:
        print('Shutting down srver HTTP')
        server.socket.close()

if __name__ == '__main__':
    DocumentRoot = '{}/htdocs/'.format(os.path.realpath(os.path.dirname(__file__)))
    PORT = '8000'
    HOST = "localhost"

    try:
        main(sys.argv[1])
    except Exception as e:
        main('{}:{}'.format(HOST, PORT))