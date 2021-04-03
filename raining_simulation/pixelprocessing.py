from setup import *
import numpy as np

def renderer():
	pixObj =  pg.PixelArray(DISPSURFACE)
	pixMatrix = np.zeros(SCREENSIZE, float)
	for i in range(SCREENSIZE[0]):
		for i in range(SCREENSIZE[1]):
			colour = list(DISPSURFACE.get_at(i,j))
			pixMatrix[i][j] = sum(colour[0:3])/(255*3.0)  
	
	kernal = np.array([[1.0, 0.0, 0.0, 0.0]
						[0.0, 1.0, 0.0, 0.0]
						[0.0, 0.0, 1.0, 0.0]
						[0.0, 0.0, 0.0, 1.0]])
	pixMatrix = convolution2d(pixMatrix, kernel, 0.0)

	for i in range(SCREENSIZE[0]):
		for j in range(SCREENSIZE[1]):
			pixObj[i][j] = (int(255*pixMatrix[i][j]), int(255*pixMatrix[i][j]), int(255*pixMatrix[i][j]))


def convolution2d(image, kernel, bias):
    m, n = kernel.shape
    if (m == n):
        y, x = image.shape
        y = y - m + 1
        x = x - m + 1
        new_image = np.zeros((y,x))
        for i in range(y):
            for j in range(x):
                new_image[i][j] = np.sum(image[i:i+m, j:j+m]*kernel) + bias
return new_image		




