# openphoton

https://pypi.org/project/openphoton/

Step-By-Step Tutorial:
https://youtu.be/bz9cDEuyxx0

This README.md file is under construction. But the steps presented below is sufficient for you to simulate light propagation from a laser, passing through lens, and passing through your test object. More features will be added soon.

### FEATURES:
 - Light propagation using Rayleigh-Sommerfeld Diffraction Integral
 - Includes Fresnel Approximation and Fraunhofer Approximation
 - Simulation of converging lens and diverging Lens
 - Simulation of amplitude-based test object using SLM


## Examples of How To Use (Alpha Version)

Add openphoton to your operating system or python virtual environment

```python
pip install openphoton
```

Create a laser beam
```python
import openphoton as op

# side length (m)
# aperture radius (m)
u0 = op.devices.laser_beam(
    side_length=0.06,
    aperture_radius=0.026)
```

In order to forward propagate the wave field, you must choose between fresnel (near-field) approximation and
fraunhoffer (far-field) approximation. To determine which approximation is best for your system, you have to calculate
the Fresnel number F_N. If F_N = [1, +infinity], then use fresnel approximation. Otherwise, use fraunhoffer approximation.
```python
# uo = wave field to propagate
# L = source plane side length (m)
# wavelength = wavelength of light (m)
# z = propagation distance (m)
# u1 = resulting wave field after propagation
u1 = op.rayleigh_sommerfeld.fresnel_approx(
    u0, L, wavelength, z)
```

Apply converging lens or diverging lens on the laser beam
```python
import numpy as np

# u1 = wave field before the lens
# L = u1 side length (m)
# wavelength of light (m)
# f_length = lens focal length (m)
# u2 = wave field after the lens
u2 = np.multiply(u1, op.lenses.converging_lens(u1,L,wavelength,f_length))
```

Apply SLM or test object on the laser beam
```python
import numpy as np

# filename = image of test object file name
filename : str = "USAF_1951_1024p.png"

# SLM_amplitude() converts RGB image into numpy array
# pixel_size = number of pixels of image, ideally this must be the same with u1
test_object = op.devices.SLM_amplitude(filename, pixel_size)

# u1 = wave field before the test object
# L = u1 side length (m)
# wavelength of light (m)
# u2 = wave field after the test object
u2 = np.multiply(u1, test_object)
```

### References:
 - Shen, Fabin, and Anbo Wang. "Fast-Fourier-transform based numerical integration method for the Rayleigh-Sommerfeld diffraction formula." Applied optics 45, no. 6 (2006): 1102-1110.
 - Schmidt, Jason D. "Numerical simulation of optical wave propagation with examples in MATLAB." SPIE (2010).
 - Voelz, David G., and Michael C. Roggemann. "Digital simulation of scalar optical diffraction: revisiting chirp function sampling criteria and consequences." Applied optics 48, no. 32 (2009): 6132-6142.
