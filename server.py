# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class Test(object):

    def __init__(self, count):
        self.count = 0

    def oneMore(self):
        time.sleep(5)
        self.count += 1
        return self.count

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        # print()
        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()
        self.wfile.write(bytes("mano jkkkkkk" + str(test.oneMore()), "utf-8"))

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