# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import pandas as pd
import pathlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col

hostName = "localhost"
serverPort = 8001

class CGNE(object):

    def generate_image(self, name):

        path = pathlib.Path(__file__).parent.absolute()

        imported_vector = pd.read_csv(str(path) + '/data/real/g-3.txt', sep='.', header=None).to_numpy()
        vector = []
        for e in imported_vector:
            aux = e[0].replace(',', '')
            vector.append([float(aux)])
        vector = np.matrix(vector)


        image = np.zeros((3600, 1))

        print('matrix imported started')
        matrix_lines = pd.read_csv(str(path) + '/data/real/H-1.txt', sep=',', lineterminator='\n', header=None)
        print('matrix imported as df')
        matrix = np.matrix(matrix_lines.to_numpy())
        print('natrix converted: ' + str(matrix.dtype))

        r = vector - (matrix * image)
        p = matrix.T * r

        error = 0

        count = 0
        # while count < 5:
        while error < float('1e-4'):

            print('i = ' + str(count))

            alpha = ((r.T * r) / (p.T * p)).item((0, 0))

            print('alpha: ' + str(alpha))

            next_image = image + (alpha * p)
            next_r = r - (alpha * (matrix * p))

            beta = ((next_r.T * next_r) / (r.T * r)).item((0, 0))

            p = matrix.T * next_r + beta * p
            image = next_image
            error = np.linalg.norm(next_r, 2) - np.linalg.norm(r, 2)
            print('error: ', error)
            r = next_r 

            count += 1

        image = image.reshape(60, 60)

        image = (image - np.min(image))/np.ptp(image)
        png = plt.imsave(str(name) + '.png', image, cmap='gray')

class MyServer(BaseHTTPRequestHandler):

    def do_POST(self):
        print('i delete all my girls numbers on the phone for u')
        data = json.loads(self.rfile.read(int(self.headers['Content-Length'])))

        cgne.generate_image(data['name'])

        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()
        self.wfile.write(bytes("mano jkkkkkk", "utf-8"))

if __name__ == "__main__":
    cgne = CGNE()
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")