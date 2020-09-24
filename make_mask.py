from PIL import Image
import numpy as np

w, h = 256, 256
data = np.zeros((h, w, 3), dtype=np.uint8)
data[0:128, 0:128] = [0, 0, 0]  # red patch in upper left
data[128:256, 0:256] = [255, 255, 255]  # red patch in upper left
img = Image.fromarray(data, 'RGB')
img.save('mask.png')
# img.show()
