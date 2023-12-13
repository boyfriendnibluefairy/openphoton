import numpy as np
#from aperture_functions import circ
from . import aperture_functions as af

def converging_lens(u1, L, wavelength, focal_length):
    """function for simulating lens with positive focal length"""
    # u1 = source field to be multiplied with lens transmittance
    # L = side length of source field u1
    # wavelength = wavelength of source field

    # determine size of X and Y of u1
    M, N = np.shape(u1)
    # calculate sample interval
    dx = L / M
    # calculate wave number
    k = 2 * np.pi / wavelength
    # lens radius
    lens_r = L/2

    # source spatial coordinates
    x = np.linspace(start=-L / 2, stop=(L / 2) - dx, num=M)
    y = x
    X, Y = np.meshgrid(x, y)

    # lens pupil
    pupil = af.circ(np.sqrt(np.square(X)+np.square(Y))/lens_r)

    # lens phase matrix
    phase = np.exp(-1j*(k/(2*focal_length))*(np.square(X)+np.square(Y)))

    # lens transmittance
    t_lens = np.multiply(pupil, phase)

    return t_lens

def diverging_lens(u1, L, wavelength, focal_length):
    """function for simulating lens with negative focal length"""
    # u1 = source field to be multiplied with lens transmittance
    # L = side length of source field u1
    # wavelength = wavelength of source field

    # determine size of X and Y of u1
    M, N = np.shape(u1)
    # calculate sample interval
    dx = L / M
    # calculate wave number
    k = 2 * np.pi / wavelength
    # lens radius
    lens_r = L/2

    # source spatial coordinates
    x = np.linspace(start=-L / 2, stop=(L / 2) - dx, num=M)
    y = x
    X, Y = np.meshgrid(x, y)

    # lens pupil
    pupil = af.circ(np.sqrt(np.square(X)+np.square(Y))/lens_r)

    # lens phase matrix
    phase = np.exp(1j*(k/(2*focal_length))*(np.square(X) + np.square(Y)))

    # lens transmittance
    t_lens = np.multiply(pupil, phase)

    return t_lens