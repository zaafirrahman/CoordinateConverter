import numpy as np

def pc(r,t):
    a = (r*np.cos(t*(np.pi/180)), r*np.sin(t*(np.pi/180)))
    return a

def cp1(x,y):
    a = (np.sqrt(x**2+y**2), np.arctan(y/x)/(np.pi/180))
    return a

def cp2(x,y):
    a = (np.sqrt(x**2+y**2), np.arctan(y/x)/(np.pi/180)+2*np.pi)
    return a  

def cp3(x,y):
    a = (-(np.sqrt(x**2+y**2)), np.arctan(y/x)/(np.pi/180)-np.pi)
    return a

def cp4(x,y):
    a = (-(np.sqrt(x**2+y**2)), np.arctan(y/x)/(np.pi/180)+np.pi)
    return a

def cp(x,y):
    return cp1(x,y), cp2(x,y), cp3(x,y), cp4(x,y)
