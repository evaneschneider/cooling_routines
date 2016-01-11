#plot constant cooling using the Cloudy table 

import matplotlib.pyplot as plt
import numpy as np
import h5py

fileout = "cooling_nm3.png"

mp = 1.672622e-24 # //mass of hydrogen atom (g)
kb = 1.380658e-16 # //Boltzmann constant (erg/K)
p_c = 1.599227e-08 # //characteristic pressure
N = 100

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
plt.axis([0.0, 50000.0, 1e3, 1e6])
ax1.set_yscale('log')
plt.xlabel('time [kyr]')
plt.ylabel('temperature [K]')

time = np.linspace(0, 1000*N, N+1)
T_num = np.empty(N+1) 

for i in range(0,N+1):

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

  n = d[0]
  T = p*p_c / (n*kb)

  T_num[i] = T[0]

ax1.plot(time, T_num, "ro")
plt.show()
fig.savefig(fileout)

