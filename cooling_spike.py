#plot the results of the Creasey shock tube test

import matplotlib.pyplot as plt
import numpy as np
import h5py

fileout = "cooling.png"

#plot the exact solution
gamma = 5./3.
n = 1.0
mp = 1.672622e-24 # //mass of hydrogen atom (g)
kb = 1.380658e-16 # //Boltzmann constant (erg/K)
p_c = 1.599227e-08 # //characteristic pressure
cool = 5.0e-24
time = np.linspace(0.0, 30.0, 101)

T_init = 1e4
#T = T_init - ((gama-1.0)/(n*kb)) * cool*time*3.15569e10 #constant cooling
T0 = 1e3
T1 = 20*T0
A = -cool*(gamma-1.0) / (n*kb*T0)
T = (T_init - T0)*np.exp(A*time*3.15569e10) + T0 #cooling spike

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(time, T)
plt.axis([0.0, 10.0, 0, 1e4])
plt.xlabel('time [kyr]')
plt.ylabel('temperature [K]')

time = np.linspace(0, 10, 11)
T_num = np.empty(11) 

for i in range(0,11):

  f = h5py.File('../output/cooling/'+str(i)+'.h5', 'r')
  head = f.attrs
  gamma = head['gamma'][0]
  d  = f['density']
  mx = f['momentum_x']
  my = f['momentum_y']
  mz = f['momentum_z']
  E  = f['Energy']
#  e  = f['GasEnergy']
  d  = np.array(d)
  mx = np.array(mx)
  my = np.array(my)
  mz = np.array(mz)
  E  = np.array(E)
#  e  = np.array(e)
  vx = mx/d
  vy = my/d
  vz = mz/d
  p  = (E - 0.5*d*(vx*vx + vy*vy + vz*vz)) * (gamma - 1.0)
  e  = p/d/(gamma - 1.0)
#  e  = e/d

  T = p*p_c / (n*kb)

  T_num[i] = T[0]

ax1.plot(time, T_num, 'ro')
plt.show()

