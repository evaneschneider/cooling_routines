import matplotlib.pyplot as plt
import numpy as np


f1 = open('../cloudy_coolingcurve_nm3_HM05_zone3.txt', 'r')
f1.readline()
lines1 = f1.readlines()
f1.close()

f2 = open('../cloudy_coolingcurve_n0_HM05_zone3.txt', 'r')
f2.readline()
lines2 = f2.readlines()
f2.close()

f3 = open('../cloudy_coolingcurve_n3_HM05_zone3.txt', 'r')
f3.readline()
lines3 = f3.readlines()
f3.close()


T = []
C1 = []
C2 = []
C3 = []
H1 = []
H2 = []
H3 = []


for line in lines1:
  p = line.split()
  T.append(float(p[1]))
  C1.append(float(p[2]))
  H1.append(float(p[3]))

for line in lines2:
  p = line.split()
  C2.append(float(p[2]))
  H2.append(float(p[3]))

for line in lines3:
  p = line.split()
  C3.append(float(p[2]))
  H3.append(float(p[3]))


T = np.array(T)
C1 = np.array(C1)
C2 = np.array(C2)
C3 = np.array(C3)
H1 = np.array(H1)
H2 = np.array(H2)
H3 = np.array(H3)


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(T, C1, color='blue')
ax1.plot(T, C2, color='green')
ax1.plot(T, C3, color='purple')
ax1.plot(T, H1, color='blue', linestyle='--')
ax1.plot(T, H2, color='green', linestyle='--')
ax1.plot(T, H3, color='purple', linestyle='--')
plt.axis([1, 9, -30, -17])
plt.xlabel('log(T) [$\mathdefault{K}$]')
plt.ylabel('log($\Lambda / n_h^2$) [$\mathdefault{erg}\/ \mathdefault{cm}^{-3}\/ \mathdefault{s}^{-1}$]')
plt.text(1.2, -18, 'solar, log(n_h) = -3', color='blue')
plt.text(1.2, -19, 'solar, log(n_h) = 0', color='green')
plt.text(1.2, -20, 'solar, log(n_h) = 3', color='purple')
plt.show()
fig.savefig("coolingcurve_H&M_PIE.png")
