# Cartesius to Polar

import numpy as np

x = float(input('Input x-axis : '))
y = float(input('Input y-axis : '))

r = np.sqrt(x**2 + y**2)
t = np.arctan(y/x)/(np.pi/180)

print('\nPolar :')
print('\nFirst Representation :')
print(f'radius = {r}')
print(f'theta = {t}')
print('\nSecond Representation :')
print(f'radius = {r}')
print(f'theta = {t + 2*np.pi}')
print('\nThird Representation :')
print(f'radius = {-r}')
print(f'theta = {t - np.pi}')
print('\nFourth Representation :')
print(f'radius = {-r}')
print(f'theta = {t + np.pi}')
