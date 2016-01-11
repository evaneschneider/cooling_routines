;plot the results of the Creasey shock tube test

;read in the mpi outputs and concatenate
np = 1
nbx = 1
nby = 1
nbz = 1

;start loop over timesteps


set_plot, 'ps'
;pretty font
!p.font = 0
;thick lines
!p.thick = 3
!x.thick = 3
!y.thick = 3
!z.thick = 3


fileout = "cooling.eps"
device, filename=fileout, /encapsulated
device, xsize=4, ysize=4, /inches 
;white background
bkg = fltarr(100,100)
bkg(*,*) = 255
tv,bkg,0,0,xsize=1,ysize=1,/normal
plotsym, 8, 0.3


;plot the exact solution
gama = 5./3.
n = 1.0
mp = 1.672622e-24; //mass of hydrogen atom (g)
kb = 1.380658e-16; //Boltzmann constant (erg/K)
cool = 5.0e-24
time = findgen(101)/10.0

T_init = 1e4
;T = T_init - ((gama-1.0)/(n*kb)) * cool*time*3.15569e10 ;constant cooling
T0 = 1e3
T1 = 20*T0
A = -cool*(gama-1.0) / (n*kb*T0)
T = (T_init - T0)*exp(A*time*3.15569e10) + T0 ;cooling spike
;print, T

plot, time, T, linestyle=0, charsize=1.0, /noerase, position=[0.25,0.15,0.95,0.95], /normal,$
    xtitle="time (kyr)", xrange = [0.0, 10.0], /xstyle, $
    ytitle="temperature", yrange = [0,1e4], /ystyle

time = findgen(11)
T_num = fltarr(11)

for i=0, 10 do begin

;read in cooling solution 
outdir="binaries/"+strtrim(i,2)+".bin."
read_grid_mpi, np, nbx, nby, nbz, outdir, x, y, z, d, mx, my, mz, E

;calculate velocity, pressure, internal energy
d_c = 0.1*mp
p_c = 1.59922742e-9
n = d*d_c/mp
vx = mx / d
vy = my / d
vz = mz / d
p =  (E - 0.5*d*(vx*vx + vy*vy + vz*vz)) * (gama - 1.0) 
T = p*p_c / (n*kb)

T_num[i] = T[0]

endfor
print, T_num

oplot, time, T_num, psym=8

device, /close
set_plot, 'x'


end

