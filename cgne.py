import pandas as pd
import pathlib
import numpy as np

path = pathlib.Path(__file__).parent.absolute()

dirty_lines = open(str(path) + '/data/real/g-1.txt', "r").read().split('\n')
dirty_lines.pop()
clean_lines = []
for line in dirty_lines:
    aux = line.replace(',', '')
    clean_lines.append(float(aux))

vector_lines = np.array(clean_lines)

first = np.zeros((60))
# matrix = pd.read_csv(str(path) + '/data/test/M.csv')
# vector = pd.read_csv(str(path) + '/data/test/a.csv')

# test = vector_lines[:500]

# print(vector_lines.dot(first))

rand = np.random.randint(8, size=3600)
matrix = rand.reshape(60, 60)
print(vector_lines - matrix.dot(first))
