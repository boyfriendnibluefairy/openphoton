import numpy as np
from scipy.fft import fft2, ifft2

## In python, the symbol j denotes imaginary number.
## It also requires a coefficient, ex "1j".

def fresnel_approx(u1, L, wavelength, z):
    """ Fresnel Approximation of
     Rayleigh-Sommerfeld Diffraction Solution I

     u2 = inverseFT{ FT{u1} * transfer_function } """

    # Assumptions:
    # 1. x and y side lengths are equal
    # 2. uniform sampling
    # 3. u1 = source plane field
    # 4. L = source plane side length
    # 5. L = observation plane side length
    # 6. z = propagation distance
    # 7. u2 = observation plane field
    # 8. H = Fresnel Approximation Transfer Function

    # determine size of X and Y of u1
    M, N = np.shape(u1)
    # calculate sample interval
    dx = L/M
    # calculate wave number
    k = 2*np.pi/wavelength

    # frequency coordinates
    fx = np.linspace(start=-1 / (2 * dx), stop=1 / (2 * dx) - (1 / L), num=M)
    FX, FY = np.meshgrid(fx, fx)

    # Fresnel Approximation Transfer Function
    FX_squared = np.square(FX)
    FY_squared = np.square(FY)
    H = np.exp(-1j*np.pi*wavelength*z*(FX_squared + FY_squared))

    # Perform wave propagation
    H = np.fft.fftshift(H)
    U1 = fft2(np.fft.fftshift(u1))
    U2 = np.multiply(U1, H)
    u2 = np.fft.ifftshift(ifft2(U2))
    return u2

def fraunhoffer_approx(u1, L1, wavelength, z):
    """ Fraunhoffer Approximation of
     Rayleigh-Sommerfeld Diffraction Solution I

     u2 = { exp()/(j*lambda*z) }*{ inverseFT{ FT{u1} }"""

    # In general, the source plane and observation plane
    # sizes are different for Fraunhoffer approximation
    # unless critical sampling is implemented.
    #
    # Assumptions:
    # 1. x and y side lengths are equal
    # 2. uniform sampling
    # 3. u1 = source plane field
    # 4. u2 = observation plane field
    # 5. L1 = source plane side length
    # 6. L2 = observation plane side length
    # 7. z = propagation distance

    # determine L_x and L_y of u1
    M, N = np.shape(u1)
    # calculate sample interval
    dx1 = L1 / M
    # calculate wave number
    k = 2 * np.pi / wavelength

    # observation plane side length
    L2 = (wavelength*z)/dx1
    # observation plane sample interval
    dx2 = (wavelength*z)/L1
    # observation plane coordinates
    x2 = np.linspace(start=-L2 / 2, stop=(L2/2)-dx2, num=M)

    X2, Y2 = np.meshgrid(x2, x2)
    X2_squared = np.square(X2)
    Y2_squared = np.square(Y2)
    A = np.exp(1j*k*(X2_squared + Y2_squared)/(2*z)) / (1j*wavelength*z)
    diff_integral = np.fft.ifftshift(fft2(np.fft.fftshift(u1)))*dx1*dx1
    u2 = np.multiply(A, diff_integral)

    return u2, L2