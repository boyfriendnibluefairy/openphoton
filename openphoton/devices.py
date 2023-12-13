import numpy as np
#from aperture_functions import circ
from . import aperture_functions as af
# for SLM
from PIL import Image

def laser_beam(side_length, aperture_radius, pixels=1024):
    """ A function that simulates a laser beam with Gaussian profile."""

    L = side_length           # side length of the laser
    laser_r = aperture_radius # radius of laser aperture
    M = pixels                # number of cells or samples
    dx = L/M                  # pixel pitch

    # source spatial coordinates
    x1 = np.linspace(start=-L / 2, stop=(L / 2) - dx, num=M)
    y1 = x1

    # create input or source wave field
    X1, Y1 = np.meshgrid(x1, y1)

    # aperture of laser
    pupil = af.circ(np.sqrt(np.square(X1) + np.square(Y1)) / laser_r)

    # Gaussian Laser Mode
    gaussian = np.exp(-1 * (np.square(X1) + np.square(Y1)) / (((laser_r) ** 2) / 2))

    laser_output = np.multiply(pupil, gaussian)
    return laser_output

def SLM_amplitude(filename, pixel_size):
    """ Artificial Spatial Light Modulator.
     This function converts image into
     numpy array of amplitude values"""

    # open rgb image and save it to a variable
    img_rgb = Image.open(filename)

    # resize the image to your desired value
    img_rgb = img_rgb.resize(size=(pixel_size, pixel_size))

    # convert RGB to grayscale
    # each pixel has value [0, 255]
    img_gray = img_rgb.convert('L')

    # PIL images into NumPy arrays
    np_img = np.asarray(img_gray)

    # convert pixel values [0,1]
    np_img = np_img / 255

    return np_img


