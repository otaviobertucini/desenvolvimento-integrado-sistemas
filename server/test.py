import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as col
import pathlib

path = str(pathlib.Path(__file__).parent.absolute()) + '/../images/'
print('path: ' + path)

image = pd.read_csv('./image.csv').to_numpy()
image = np.flipud(np.rot90(image))

image = (image - np.min(image))/np.ptp(image)
png = plt.imsave(path + 'image.png', image, cmap='gray')

# plt.imsave('image.png', png)

