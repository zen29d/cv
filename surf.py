import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2 as cv

def surf(image):
    '''
    plot an image suraface in grayscale
    surf(image)
    image: 2D array
    '''
    # todo:  option[default:gray]= color, gray
    # if type == 'color':
    #     clrtype = plt.cm.jet
    # else:
    #     clrtype = plt.cm.gray

    # Grayscaling 
    img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # Reduing size > big size take more time to generate 
    img = cv.resize(img, (64,64))

    # Generating X and Y
    x, y = np.mgrid[0:img.shape[0], 0:img.shape[1]]

    # Ploting
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(x, y, img ,rstride=1, cstride=1, cmap=plt.cm.gray)
    plt.show()

if __name__ == "__main__":
    pass