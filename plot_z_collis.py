import matplotlib.pyplot as plt
import numpy as np

f2 = open('z_collis.txt', 'r')
lines = f2.readlines()
f2.close()

lines2 = lines[35:387]
T = []
L = []

for line in lines2:
  p = line.split()
  T.append(float(p[0]))
  L.append(float(p[1]))


Tv = np.array(T)
Lv = np.array(L)


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(Tv, Lv)
plt.axis([1e4, 1e9, 1e-24, 1e-21])
plt.xscale('log')
plt.yscale('log')
plt.show()
