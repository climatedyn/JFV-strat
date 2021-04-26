import numpy as np

def GaussianHeating(lat,pres,constamp,ycenter,ywidth,sigcenter,sigwidth):
    sig = pres/1e3
    return constamp*np.exp(-0.5*( (lat-ycenter)/ywidth )**2)*np.exp( -0.5*( (sig-sigcenter)/sigwidth )**2)

