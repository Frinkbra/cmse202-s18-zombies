import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as py
#define initial conditions
S0 = 999
I0 = 1
R0 = 0
#N = S0 + I0 + R0
y0 = [S0, I0, R0]
t = np.linspace(0,1,1000)

#define initial rates per day
B = 0.05
g = 0.001

#defining derivatives
def fun(y,t):
    Si = y[0]
    Ii = y[1]
    Ri = y[2]
    
    dS = -(B * Si * Ii)
    dI = (B * Si * Ii) - g * Ii
    dR = g * Ii
    
    return [dS, dI, dR]

 #running derivatives through odeint
sol = odeint(fun, y0, t)
plt.plot(sol[:,0])
plt.plot(sol[:,1])
plt.plot(sol[:,2])