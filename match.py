from PIL import Image
import numpy as np
from scipy.ndimage.interpolation import rotate
from scipy.misc import imsave
Lo = Image.open('/Users/vruiz/Pictures/2017_05_20/IMG_5038.CR2.jpg')
Ro = Image.open('/Users/vruiz/Pictures/2017_05_20/IMG_5039.CR2.jpg')
L = np.array(Lo, dtype=np.float32)
R = np.array(Ro, dtype=np.float32)
while True:
    x_offset = int(input("X offset: "))
    y_offset = int(input("Y_offset: "))
    angle = float(input("angle: "))
    if (x_offset==0) & (y_offset==0):
        imsave("/tmp/1.jpg", Rr)
        break
    Rr = np.roll(R, y_offset, axis=0) # See scipy.ndimage.interpolation.shift
    Rr = np.roll(Rr, x_offset, axis=1)
    if angle != 0:
        Rr = rotate(Rr, angle, reshape=False)
    O = (L+Rr)/2.0
    P = np.array(np.round(O), dtype=np.uint8)
    av = Image.fromarray(P, 'RGB')
    av.show()
