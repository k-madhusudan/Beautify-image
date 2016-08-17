from skimage import data
import skimage
import os
from skimage import io
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import img_as_float
from skimage import color
# Saffron : 255, 153, 51
#cam = data.camera()
#print type(cam)
#print cam.shape

filename = os.path.join(input(),input())
#filename = os.path.join (input(),input())
lena = io.imread(filename)


#rgblena = rgb2gray(lena)
#lenaimg = img_as_float(lena)
print lena.shape

#print lenaimg[int(lenaimg.shape[0])-1][0]
maxx =[0,0,0]
minn = [255,255,255]
for i in range(0,lena.shape[0]):
	for j in range(0,lena.shape[1]):
		if  (lena[i,j][0] > maxx[0]):
			maxx[0] = lena[i,j][0]
		if (lena[i,j][1] > maxx[1]):
			maxx[1] = lena[i,j][1]
		if (lena[i,j][2] > maxx[2]):
			maxx[2] = lena[i,j][2]
		if (lena[i,j][0] < minn[0]):
			minn[0] = lena[i,j][0]
		if (lena[i,j][1] < minn[1]):
			minn[1] = lena[i,j][1]
		if (lena[i,j][2] < minn[2]):
			minn[2] = lena[i,j][2]

print maxx
print minn

for i in range(1,379):
	for j in range(1,379):
		if lena[i,j][0] > 159 & lena[i,j][0]< 192 &  lena[i,j][1] > 156 & lena[i,j][1]< 250 & lena[i,j][2] > 145 & lena[i,j][2]< 249  :
			lena[i,j] = lena[i-1,j-1]
#

io.imshow(lena, plugin=None)
io.show()
#print rgblena.min(), rgblena.max()
#plt.imshow(lena)
#plt.show()