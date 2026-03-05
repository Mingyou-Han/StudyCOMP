import numpy as np
from matplotlib import pyplot as plt
#import cv2

# Exercises related to section 1

def greyscale_rowscolumns(greyscaleimage):
    """Return the image resolution (rows, columns) of a greyscale image
    >>> img = np.array([[   0, 255,   0],  \
                        [ 110, 127, 140]])
    >>> greyscale_rowscolumns(img)
    (2, 3)
    """
    return greyscaleimage.shape

def greyscale_invert(greyscaleimage):
    """Return a greyscale image with inverted luminosity
    >>> img = np.array([[   0, 255,   0],  \
                        [  50, 200,  50],  \
                        [ 110, 127, 140]])
    >>> greyscale_invert(img)
    array([[255,   0, 255],
           [205,  55, 205],
           [145, 128, 115]])
    """
    inverseArray = []
    for x in range(greyscaleimage.shape[0]): #here, every x in [3,3] x moves 3 units
        for y in range(greyscaleimage[1]): #a nested loop to go through each unit then
            inverseArray[x][y]= abs(y-255) #absolute value 25 - 255 = 230 hence we inversed it using absolute values. 

    return inverseArray
        

def greyscale_highest_luminosity(greyscaleimage):
    """Return the highest luminosity
    >>> img = np.array([[   0, 250,   0],  \
                        [  50, 200,  50],  \
                        [ 110, 127, 140]])
    >>> greyscale_highest_luminosity(img)
    250
    """
    return None

def greyscale_blackout(greyscaleimage, threshold):
    """Black out pixels equal or brighter than a set threshold
    >>> img = np.array([[   0, 255,   0],  \
                        [  50, 200,  50],  \
                        [ 110, 127, 140]])
    >>> greyscale_blackout(img, 200)
    array([[  0,   0,   0],
           [ 50,   0,  50],
           [110, 127, 140]])
    """
    return None

# Exercises related to section 2

def colour_rowscolumns(colourimage):
    """Return the image resolution (rows, columns)
    >>> img = np.array([[[255,   0,   0], [  0, 255,   0], [  0,   0, 255]], \
                        [[  0,   0,   0], [255, 255, 255], [127, 127, 127]]])
    >>> colour_rowscolumns(img)
    (2, 3)
    """            
    return None

def remove_red(colourimage):
    """Remove information from the red channel
    >>> img = np.array([[[255,   0,   0], [  0, 255,   0], [  0,   0, 255]], \
                        [[  0,   0,   0], [255, 255, 255], [127, 127, 127]]])
    >>> remove_red(img)
    array([[[  0,   0,   0],
            [  0, 255,   0],
            [  0,   0, 255]],
    <BLANKLINE>
           [[  0,   0,   0],
            [  0, 255, 255],
            [  0, 127, 127]]])
    """
    return None

def to_greyscale(colourimage):
    """Convert from colour to greyscale.
    >>> img = np.array([[[255,   0,   0], [  0, 255,   0], [  0,   0, 255]], \
                        [[  0,   0,   0], [255, 255, 255], [127, 127, 127]]])
    >>> to_greyscale(img)
    array([[ 85.,  85.,  85.],
           [  0., 255., 127.]])
    """
    return None

# Exercise related to section 3


def capture_image(filename, webcam_id=0):
    None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
