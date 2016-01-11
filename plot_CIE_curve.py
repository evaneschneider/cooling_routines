import matplotlib.pyplot as plt
import numpy as np
import h5py

f1 = open('z_collis.txt', 'r')
lines1 = f1.readlines()
f1.close()
T1 = []
L1 = []

for line in lines1:
  p = line.split()
  T1.append(float(p[0]))
  L1.append(float(p[1]))


f2 = open('schure_CIE_curve.txt', 'r')
lines = f2.readlines()
f2.close()

f = h5py.File('CoolingTables/z_0.000.hdf5','r')
T2 = np.array(f['Solar/Temperature_bins/'])
L2 = np.array(f['Solar/Net_cooling/'])
H2 = np.array(f['Solar/Hydrogen_density_bins/'])
f.close()

f3 = open('hazy_coolingcurve_n0.txt', 'r')
f3.readline()
lines3 = f3.readlines()
f3.close()

T3 = []
L3 = []

for line in lines3:
  p = line.split()
  T3.append(float(p[0]))
  L3.append(float(p[1]))

T3 = np.power(10, T3)
L3 = np.power(10, L3)


logT = []
logLn = []
logLhd = []

for line in lines:
  p = line.split()
  logT.append(float(p[0]))
  logLn.append(float(p[1]))
  logLhd.append(float(p[2]))


logT = np.array(logT)
logLn = np.array(logLn)
logLhd = np.array(logLhd)
T = np.power(10, logT)
Lhd = np.power(10, logLhd)
logTlow = logT[logT < 5.38]
Tlow = np.power(10, logTlow)
logThigh = logT[logT > 5.35]
Thigh = np.power(10, logThigh)
#Lfit = np.log10(3e-23 * np.power((np.power(10, Tv) / 1e7), -0.9))
Lfit = np.power(10, (0.38 * (logThigh -7.5) * (logThigh - 7.5) - 22.6))
#Lfit2 = np.log10(3e-24 * np.power((np.power(10, Tv) / 1e4), 3.3))
Lfit2 = np.power(10, (-2.5 * (logTlow - 5.1) * (logTlow - 5.1) - 20.7))

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(T, Lhd, color="Blue")
#ax1.plot(Tlow, Lfit2)
#ax1.plot(Thigh, Lfit)
ax1.plot(T2, L2[:,80], color="Green")
ax1.plot(T3, L3, color="Red")
ax1.text(1e6, 5e-21, 'CIE solar abundance (Schure 2009)', color="Blue")
ax1.text(1e6, 2e-21, 'CIE solar abundance (Cloudy 2016)', color="Red")
ax1.text(1e6, 1e-21, 'CIE solar abundance (Wiersma 2009)', color="Green")
plt.axis([1e3, 1e9, 1e-24, 1e-20])
plt.xscale('log')
plt.yscale('log')
plt.show()
