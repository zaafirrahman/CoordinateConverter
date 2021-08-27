# Polar to Cartesius

import numpy as np

r = float(input('Input radius : '))
t = float(input('Input theta : '))

x = r * np.cos(t*(np.pi/180))
y = r * np.sin(t*(np.pi/180))

print('\nCartesius :')
print(f'x = {x}')
print(f'y = {y}')
