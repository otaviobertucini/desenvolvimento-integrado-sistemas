import pandas as pd
import pathlib
import numpy as np

path = pathlib.Path(__file__).parent.absolute()

# dirty_lines = open(str(path) + '/data/real/g-1.txt', "r").read().split('\n')
# dirty_lines.pop()
# clean_lines = []
# for line in dirty_lines:
#     aux = line.replace(',', '')
#     clean_lines.append(float(aux))
# vector_lines = np.array(clean_lines)
# # vector = vector_lines.reshape(len(vector_lines), 1)
# vector = vector_lines.reshape(len(vector_lines), 1)
imported_vector = pd.read_csv(str(path) + '/data/real/g-1.txt', sep='.', header=None).to_numpy()
vector = []
for e in imported_vector:
    aux = e[0].replace(',', '')
    vector.append([float(aux)])
vector = np.matrix(vector)


first = np.zeros((3600, 1))
print(first.shape)

matrix_lines = pd.read_csv(str(path) + '/data/real/H-1.txt', sep=',', lineterminator='\n', header=None  )
matrix = np.matrix(matrix_lines.to_numpy())

# print(vector_lines.dot(first))
# print('shape: ' + str(matrix.shape))

# dot = np.nan_to_num(matrix.dot(first))
# dot = dot.reshape(dot.shape)    
# print('shape dot after: ' + str(dot.shape))
# dot = dot.reshape(dot.shape[0])

# sub = np.squeeze(np.asarray(np.nan_to_num(matrix.dot(first))))
# sub = np.array(sub[0])
# print('shape dot: ' + str(dot.shape))
print('shape matrix: ' + str(matrix.shape))
print('shape vector: ' + str(vector.shape))

# sub = vector - dot

print(vector - (matrix * first))
