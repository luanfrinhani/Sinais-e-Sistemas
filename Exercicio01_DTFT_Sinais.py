# -*- coding: utf-8 -*-
"""ExercicioSinais01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K6hRMmU2Fmp97RGrtVJGCsvPV7cAmGdX
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, ifft, fftfreq, fftshift

#Letra A

#Criando a função 0.5^n*u(n)
L = 100
Ts = 1
t1 = np.arange(0,L,Ts)
x1 = 0.5**t1

#Calculando a DTFT da função x
X1 = fft(x1)

w1 = fftfreq(len(X1),d=1.0)*(2*pi)
wd1 = fftshift(w1/pi)

Xd1 = fftshift(X1)
modX1 = np.abs(Xd1)
phaseX1 = np.angle(Xd1)

phaseX1[modX1 < 0.00001] = 0

#Plotagem dos gráficos para cada uma das funções
fig1,ax1 = plt.subplots(3,1)
ax1[0].stem(t1,x1,use_line_collection = True)
ax1[0].set_xlabel("Amostras")
ax1[0].set_ylabel("Amplitude")
ax1[0].grid()
ax1[0].set_title("Letra A")

ax1[1].plot(wd1,modX1)
ax1[1].set_xlabel("Amplitude")
ax1[1].set_ylabel("w/pi")
ax1[1].grid()

ax1[2].plot(wd1,phaseX1)
ax1[2].set_xlabel("Amplitude")
ax1[2].set_ylabel("w/pi")
ax1[2].grid()
plt.show()

#Letra B
#Criando a função
def degrau():
  x = []
  L = 50
  Ts = 1
  t = np.arange(0,L,Ts)
  for i in range(len(t)):
    if (i>=20):
      x.append(1)
    else:
      x.append(0)
  return x
L = 50
Ts = 1
t2 = np.arange(0,L,Ts)
x2 = 2*(0.8)**(t2+2)*degrau()

X2 = fft(x2)

w2 = fftfreq(len(X2),d=1.0)*(2*pi)
wd2 = fftshift(w2/pi)

Xd2 = fftshift(X2)
modX2 = np.abs(Xd2)
phaseX2 = np.angle(Xd2)

phaseX2[modX2 < 0.00001] = 0



fig2, ax2 = plt.subplots(3,1)
ax2[0].stem(t2,x2,use_line_collection = True)
ax2[0].set_xlabel("Amostras")
ax2[0].set_ylabel("Amplitude")
ax2[0].grid()
ax2[0].set_xlim(0,15)
ax2[0].set_title("Letra B")

ax2[1].plot(wd2,modX2)
ax2[1].set_xlabel("Amplitude")
ax2[1].set_ylabel("w2/pi")
ax2[1].grid()

ax2[2].plot(wd2,phaseX2)
ax2[2].set_xlabel("Amplitude")
ax2[2].set_ylabel("w2/pi")
ax2[2].grid()
plt.show()

#Letra C
#Criando a função
L = 200
Ts = 1
t3 = np.arange(0,L,Ts)

x3 = 5*((-0.9)**t3)*np.cos(0.1*pi*t3)

#Calculando a DTFT da função x3

X3 = fft(x3)

w3 = fftfreq(len(X3),d=1.0)*(2*pi)
wd3 = fftshift(w3/pi)

Xd3 = fftshift(X3)
modX3 = np.abs(Xd3)
phaseX3 = np.angle(Xd3)

phaseX3[modX3 < 0.00001] = 0

# Plotando o gráfico da função x3 no tempo
fig3, ax3 = plt.subplots(3,1)
ax3[0].stem(t3,x3,use_line_collection = True)
ax3[0].set_xlabel("Amostras")
ax3[0].set_ylabel("Amplitude")
ax3[0].set_xlim(0,30)
ax3[0].set_title("Letra C")
ax3[0].grid()

# Plotando o gráfico da magnitude de X3 
ax3[1].plot(wd3,modX3)
ax3[1].set_xlabel("Amplitude")
ax3[1].set_ylabel("w2/pi")
ax3[1].grid()

# Plotando o gráfico da fase de X3
ax3[2].plot(wd3,phaseX3)
ax3[2].set_xlabel("Amplitude")
ax3[2].set_ylabel("w2/pi")
ax3[2].grid()
plt.show()

#Letra D
#Criando a função
L = 100
Ts = 1
t4 = np.arange(0,L,Ts)

x4 = (0.9*(np.exp(1.j*pi/3)))**t4

#Calculando a DTFT da função x4

X4 = fft(x4)

w4 = fftfreq(len(X4),d=1.0)*(2*pi)
wd4 = fftshift(w4/pi)

Xd4 = fftshift(X4)
modX4 = np.abs(Xd4)
phaseX4 = np.angle(Xd4)

phaseX4[modX4 < 0.00001] = 0

# Plotando o gráfico da função x4 no tempo
fig4, ax4 = plt.subplots(3,1)
ax4[0].stem(t4,x4,use_line_collection = True)
ax4[0].set_xlabel("Amostras")
ax4[0].set_ylabel("Amplitude")
ax4[0].set_xlim(0,30)
ax4[0].set_title("Letra D")
ax4[0].grid()

# Plotando o gráfico da magnitude de X4
ax4[1].plot(wd4,modX4)
ax4[1].set_xlabel("Amplitude")
ax4[1].set_ylabel("w2/pi")
ax4[1].grid()

# Plotando o gráfico da fase de X3
ax4[2].plot(wd4,phaseX4)
ax4[2].set_xlabel("Amplitude")
ax4[2].set_ylabel("w2/pi")
ax4[2].grid()
plt.show()

