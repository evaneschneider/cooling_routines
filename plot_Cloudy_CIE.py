import matplotlib.pyplot as plt
import numpy as np


f1 = open('hazy_coolingcurve_ISM_n1.txt', 'r')
f1.readline()
lines1 = f1.readlines()
f1.close()

f2 = open('hazy_coolingcurve_solar_n0.txt', 'r')
f2.readline()
lines2 = f2.readlines()
f2.close()

f3 = open('hazy_coolingcurve_ISM_n2.txt', 'r')
f3.readline()
lines3 = f3.readlines()
f3.close()

T = []
L1 = []
L2 = []
L3 = []

for line in lines1:
  p = line.split()
  T.append(float(p[0]))
  L1.append(float(p[1]))

for line in lines2:
  p = line.split()
  L2.append(float(p[1]))

for line in lines3:
  p = line.split()
  L3.append(float(p[1]))

Tv = np.array(T)
Lv1 = np.array(L1)
Lv2 = np.array(L2)
Lv3 = np.array(L3)

Lv10 = np.log10(2e-26 * (1e7 * np.exp(-114800/(np.power(10,Tv) + 1000)) + 14 * np.sqrt(np.power(10,Tv)) * np.exp(-92 / np.power(10,Tv))))

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(Tv, Lv1, color='blue')
ax1.plot(Tv, Lv2, color='green')
ax1.plot(Tv, Lv3, color='purple')
ax1.plot(Tv, Lv10, color='red')
plt.axis([1, 9, -30, -17])
plt.xlabel('log(T)')
plt.ylabel('log(lambda / n_h^2)')
#plt.xscale('log')
#plt.yscale('log')
plt.text(1.2, -18, 'solar, log(n_h) = 1', color='green')
plt.text(1.2, -19, 'ISM, log(n_h) = 1', color='blue')
plt.text(1.2, -20, 'ISM, log(n_h) = 2', color='purple')
plt.text(3.5, -18, 'KI', color='red')
plt.show()
