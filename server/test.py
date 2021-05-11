import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as col
import pathlib
from datetime import datetime

start = datetime.now()

path = str(pathlib.Path(__file__).parent.absolute()) + '/../images/'
print('path: ' + path)

image = pd.read_csv('./image.csv').to_numpy()
image = np.flipud(np.rot90(image))

image = (image - np.min(image))/np.ptp(image)
png = plt.imsave(path + 'image.png', image, cmap='gray')

attributes = {
    "username": 'otavio',
    "algorithm": "CGNE",
    "start": str(start),
    "end": str(datetime.now()),
}

print(attributes)

# plt.imsave('image.png', png)

