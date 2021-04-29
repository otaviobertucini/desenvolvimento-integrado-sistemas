import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as col

image = pd.read_csv('./image.csv').to_numpy()

image = (image - np.min(image))/np.ptp(image)
png = plt.imsave('image.png', image, cmap='gray')

# plt.imsave('image.png', png)

