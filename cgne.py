import pandas as pd
import pathlib
import numpy as np

path = pathlib.Path(__file__).parent.absolute()

imported_vector = pd.read_csv(str(path) + '/data/real/g-1.txt', sep='.', header=None).to_numpy()
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

count = 0
while count < 5:

    print('i = ' + str(count))

    alpha = ((r.T * r) / (p.T * p))[0][0]

    print('alpha: ' + str(alpha[0][0]))

    next_image = image + (alpha * p)
    next_r = r - (alpha * (H * p))

    beta = ((next_r.T * next_r) / (r.T * r))[0][0]

    p = matrix.T * next_r + beta * p
    image = next_image
    r = next_r 

    count += 1
