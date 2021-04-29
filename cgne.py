import pandas as pd
import pathlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col

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
png = plt.imsave('image.png', image, cmap='gray')

