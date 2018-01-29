import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from scipy.integrate import odeint

P = 0       # birth rate
d = 0.1  # natural death percent (per day)
B = 0.0095  # transmission percent  (per day)
i = 1  # inmunity rate
N = 1000


def func(y, t):
    Sucepi = y[0]
    Zombi = y[1]
    Deadi = y[2]
    Recovi = y[3]
    #Infi = y[4]

    dSucep = -B*Sucepi*Zombi - d*Zombi - i*Recovi
    dZomb = B*Sucepi*Zombi - d*Zombi
    dDead = 2*d*Zombi
    dRecov = i*Recovi
    #dinf = -B*Sucepi*Zombi

    return [dSucep, dZomb, dDead, dRecov]


Sucep0 = 1000.              # initial population
Zomb0 = 100                # initial zombie population
Dead0 = 1  # initial death population
Recov0 = 10  # inmune poputalation

y0 = [Sucep0, Zomb0, Dead0, Recov0]
t = np.linspace(0, 1, 1000)


solution = odeint(func, y0, t)

plt.figure(figsize=(12, 6))
plt.plot(solution[:, 0], label="Suceptible")
plt.plot(solution[:, 1], label="Zombies")
plt.plot(solution[:, 2], label="Dead")
plt.plot(solution[:, 3], label="Inmune")
plt.legend()
solution[-1, 0]+solution[-1, 1]+solution[-1, 2]+solution[-1, 3]
