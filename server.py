# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

hostName = "localhost"
serverPort = 8001

class Test(object):

    def __init__(self, count):
        self.count = 0

    def oneMore(self):
        time.sleep(1)
        self.count += 1
        return self.count

class MyServer(BaseHTTPRequestHandler):

    def do_POST(self):
        # print()
        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()
        data = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        print(len(data['vector']))
        # self.wfile.write(bytes("mano jkkkkkk" + str(test.oneMore()), "utf-8"))
        self.wfile.write(bytes("mano jkkkkkk", "utf-8"))

if __name__ == "__main__":     
    test = Test(0)   
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")