import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
%matplotlib inline

def agent_derivs(current_state, time_array):

    S_pop = current_state[0]
    I_pop = current_state[1]
    Z_pop = current_state[2]
    R_pop = current_state[3]
    D_pop = current_state[4]

    ### DIFFERENTIAL EQUATIONS ###
    d_S = -(S_pop * nat_d) - (S_pop * Z_pop * inf_r)
    d_I = (Z_pop * S_pop * inf_r) - (I_pop * rec_r) - (I_pop * inf_d) - (I_pop * turn_r)
    d_Z = (I_pop * turn_r) - (Z_pop * kill_r) - (Z_pop * z_nat_d)
    d_R = (I_pop * rec_r) - (R_pop * nat_d)
    #d_D = (S_pop * nat_d) + (R_pop * nat_d) + (I_pop * inf_d) + (Z_pop * S_pop * kill_r)
    d_D = (S_pop * nat_d) + (I_pop * inf_d) + (Z_pop * kill_r) + (Z_pop * z_nat_d) + (R_pop * nat_d)


    return [d_S, d_I, d_Z, d_R, d_D]

### PARAMETERS ###
nat_d = 1 # Natural death rate
inf_r = 2 # Infection rate
inf_d = 2 # Infected (natural) death rate (must be larger than nat_d)
rec_r = 1 # Recovery rate
kill_r = 3 # Kill rate (rate at which humans kill zombies)
z_nat_d = 1 # Zombie natural death rate
turn_r = 2 # Infected-to-Zombie turn rate

### INITIAL CONDITIONS ###
init_cond = [1000, 1, 0, 0, 0]
time_array = np.linspace(0, 1, 1000)

### DISPLAY INITIAL POPULATIONS ###
total_init = init_cond[0] + init_cond[1] + init_cond[2] + init_cond[3] + init_cond[4]
print('Initital S:', init_cond[0])
print('Initital I:', init_cond[1])
print('Initital Z:', init_cond[2])
print('Initital R:', init_cond[3])
print('Initital D:', init_cond[4])
print('TOTAL PEOPLE (initial):', total_init)

### Obtain results from odeint ###
results = odeint(agent_derivs, init_cond, time_array)

### Unpack the results for each compartment ###
Susceptible = results[:,0]
Infected = results[:,1]
Zombies = results[:,2]
Recovered = results[:,3]
Dead = results[:,4]

### Plot the results ###
plt.plot(time_array, Susceptible, label='Susceptible')
plt.plot(time_array, Infected, label='Infected')
plt.plot(time_array, Zombies, label='Zombies')
plt.plot(time_array, Recovered, label='Recovered')
plt.plot(time_array, Dead, label='Dead')
plt.grid()
plt.legend()
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('SIZRD Model')

### Display Final Populations ###
total_final = Susceptible[-1] + Infected[-1] + Zombies[-1] + Recovered[-1] + Dead[-1]
print('')
print('Final S:', Susceptible[-1])
print('Final I:', Infected[-1])
print('Final Z:', Zombies[-1])
print('Final R:', Recovered[-1])
print('Final D:', Dead[-1])
print('TOTAL PEOPLE:', total_final)
