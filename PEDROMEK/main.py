import numpy
import matplotlib.pyplot as plt
import control
from scipy import signal

x0 = 0
t0 = 0;
tF = 10;
dt = 1E-3;
tl = 3
N = round((tF - t0) / dt) + 1
t = numpy.linspace(t0, tF, N)
td = numpy.linspace(t0, tl, round(tl / dt) + 1)
u1 = numpy.ones(len(t))  # Escalon unitario
u2 = 0.5 - 0.5 * signal.square(2 * numpy.pi * 0.5 * td)  # Impulso unitario
u3 = (numpy.linspace(t0, tF, N)) / tF  # Rampa
u4 = numpy.sin(1.5708 * t)  # Funcion sinusoidal

# Elementos del circuito RLC

R = 1E3  # 1 kOhm
L = 1E-6  # 1 uF
C = 1E-6  # 1 uH

# Funcion de trasnferencia

num = [C * L * R, C * R ** 2 + L, R]
den = [3 * C * L * R, 5 * C * R ** 2 + L, 2 * R]
sys = control.tf(num, den)
print(sys)

# Controlador I

Cr = 10E-9  # 10 nF
Re = 200E3  # 200 kOhms
numI = 1
denI = [Re * Cr, 0]
I = control.tf(numI, denI)

# Sistema con el controlador de lazo cerrado

X = control.series(sys, I)
sysI = control.feedback(X, 1, sign=-1)
print(sysI)

# Respuesta al escalon unitario

fig1 = plt.figure()
plt.plot(t, u1, '-', color=[0.93, 0.69, 0.13], label='$Ve(t)$')  # Escalon
ts, Vs = control.forced_response(sys, t, u1, x0)
plt.plot(t, Vs, '-', color=[0, 0.45, 0.74], label='$Vs(t)$')  # Lazo abierto
ts, i = control.forced_response(sysI, t, u1, x0)
plt.plot(t, i, ':', color=[0.47, 0.67, 0.19], label='$I$')  # Lazo cerrado
plt.grid(True)
plt.xlim(-0.5, 10)
plt.ylim(-0.1, 1.2)
plt.xlabel('$t$''$[segundos]$')
plt.ylabel('$V(t)$''$[volts]$')
plt.title('Respuesta al escalón')
plt.legend(loc='lower right')
fig1.set_size_inches(6, 4)
fig1.savefig('step.png', dpi=600)
plt.show()

# Respuesta al impulso unitario

fig2 = plt.figure()
plt.plot(td, u2, '-', color=[0.93, 0.69, 0.13], label='$Ve(t)$')  # Escalon
ts, Vs = control.forced_response(sys, td, u2, x0)
plt.plot(td, Vs, '-', color=[0, 0.45, 0.74], label='$Vs(t)$')  # Lazo abierto
ts, i = control.forced_response(sysI, td, u2, x0)
plt.plot(td, i, ':', color=[0.47, 0.67, 0.19], label='$I$')  # Lazo cerrado
plt.grid(True)
plt.xlim(0, 3)
plt.ylim(-0.2, 1.2)
plt.xlabel('$t$''$[segundos]$')
plt.ylabel('$V(t)$''$[volts]$')
plt.title('Respuesta al impulso')
plt.legend(loc='upper right')
fig2.set_size_inches(6, 4)
fig2.savefig('impulse.png', dpi=600)
plt.show()  # Lazo cerrado

# Respuesta a la rampa

fig3 = plt.figure()
plt.plot(t, u3, '-', color=[0.93, 0.69, 0.13], label='$Ve(t)$')  # Escalon
ts, Vs = control.forced_response(sys, t, u3, x0)
plt.plot(t, Vs, '-', color=[0, 0.45, 0.74], label='$Vs(t)$')  # Lazo abierto
ts, i = control.forced_response(sysI, t, u3, x0)
plt.plot(t, i, ':', color=[0.47, 0.67, 0.19], label='$I$')  # Lazo cerrado
plt.grid(True)
plt.xlim(-0.5, 10)
plt.ylim(-0.1, 1.2)
plt.xlabel('$t$''$[segundos]$')
plt.ylabel('$V(t)$''$[volts]$')
plt.title('Respuesta a la rampa')
plt.legend(loc='lower right')
fig3.set_size_inches(6, 4)
fig3.savefig('ramp.png', dpi=600)
plt.show()

# Respuesta a la funcion sinosuidal

fig4 = plt.figure()
plt.plot(t, u4, '-', color=[0.93, 0.69, 0.13], label='$Ve(t)$')  # Escalon
ts, Vs = control.forced_response(sys, t, u4, x0)
plt.plot(t, Vs, '-', color=[0, 0.45, 0.74], label='$Vs(t)$')  # Lazo abierto
ts, i = control.forced_response(sysI, t, u4, x0)
plt.plot(t, i, ':', color=[0.47, 0.67, 0.19], label='$I$')  # Lazo cerrado
plt.grid(True)
plt.xlim(-0.5, 10)
plt.ylim(-1.2, 1.2)
plt.xlabel('$t$''$[segundos]$')
plt.ylabel('$V(t)$''$[volts]$')
plt.title('Respuesta a la funcion sinosuidal')
plt.legend(loc='lower right')
fig4.set_size_inches(6, 4)
fig4.savefig('senoidal.png', dpi=600)
plt.show()
