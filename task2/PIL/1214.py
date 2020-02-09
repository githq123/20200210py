import numpy as np
from PIL import Image
im0=np.array(Image.open('1214.jpg'))
print(im0.shape,im0.dtype)
im=np.array(Image.open('1214.jpg').convert('L'))
im1=255-im
im2=(100/255)*im+150
im3=255*(im1/255)**2
pil_im=Image.fromarray(np.uint(im1))
pil_im.show()