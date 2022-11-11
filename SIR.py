import matplotlib.pyplot as plt
import numpy as np
import sys


font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }

ndays_1 = 366
ndays_2 = 30
dt = 1
beta = (1.0/3.0)
gamma = (1.0/4.0)
S= np.zeros(ndays_1)  # Susceptible
I= np.zeros(ndays_1)  # Infected
R= np.zeros(ndays_1)  # Recovered
t= np.arange(ndays_1)*dt # Time
I[0]= 0.03
S[0]= 1. - I[0]
R[0]= 0.

for i in range(ndays_1-1):
  S[i+1]=S[i] - (beta*S[i]*I[i])*dt
  I[i+1]=I[i] + (beta*S[i]*I[i] - gamma*I[i])*dt
  R[i+1]=R[i] + gamma*I[i]*dt

A= np.zeros(ndays_2)  # Susceptible
B= np.zeros(ndays_2)  # Infected
C= np.zeros(ndays_2)  # Recovered
B[0]= 0.03
A[0]= 1. - I[0]
C[0]= 0.
t_2= np.arange(ndays_2)*dt
for n in range(ndays_2-1):
  A[n+1]=A[n] - (beta*A[n]*B[n])*dt
  B[n+1]=B[n] + (beta*A[n]*B[n] - gamma*B[n])*dt
  C[n+1]=C[n] + gamma*B[n]*dt

ndays_3=14
a= np.zeros(ndays_3)  # Susceptible
b= np.zeros(ndays_3)  # Infected
c= np.zeros(ndays_3)  # Recovered
b[0]= 0.03
a[0]= 1. - I[0]
c[0]= 0.
t_3= np.arange(ndays_3)*dt

for j in range(ndays_3-1):
  a[j+1]=a[j] - (beta*a[j]*b[j])*dt
  b[j+1]=b[j] + (beta*a[j]*b[j] - gamma*b[j])*dt
  c[j+1]=c[j] + gamma*b[j]*dt

ndays_4=7
a_1= np.zeros(ndays_4)  # Susceptible
b_1= np.zeros(ndays_4)  # Infected
c_1= np.zeros(ndays_4)  # Recovered
b_1[0]= 0.03
a_1[0]= 1. - I[0]
c_1[0]= 0.
t_4= np.arange(ndays_4)*dt

for k in range(ndays_4-1):
  a_1[k+1]=a_1[k] - (beta*a_1[k]*b_1[k])*dt
  b_1[k+1]=b_1[k] + (beta*a_1[k]*b_1[k] - gamma*b_1[k])*dt
  c_1[k+1]=c_1[k] + gamma*b_1[k]*dt
figure, axis = plt.subplots(2, 2)
axis[0, 0].plot(t,S, 'b', lw=.7, label='Susceptible')
axis[0, 0].plot(t,I, 'r', lw=.7, label='Infected')
axis[0, 0].plot(t,R, 'g', lw=.7, label='Recovered')
axis[0, 0].set_title("SIR Model For Year case")

axis[0, 1].plot(t_2,A, 'b', lw=.7, label='Susceptible')
axis[0, 1].plot(t_2,B, 'r', lw=.7, label='Infected')
axis[0, 1].plot(t_2,C, 'g', lw=.7, label='Recovered')
axis[0, 1].set_title("SIR Model For Month case")

axis[1, 0].plot(t_3,a, 'b', lw=.7, label='Susceptible')
axis[1, 0].plot(t_3,b, 'r', lw=.7, label='Infected')
axis[1, 0].plot(t_3,c, 'g', lw=.7, label='Recovered')

axis[1, 1].plot(t_4,a_1, 'b', lw=.7, label='Susceptible')
axis[1, 1].plot(t_4,b_1, 'r', lw=.7, label='Infected')
axis[1, 1].plot(t_4,c_1, 'g', lw=.7, label='Recovered')

plt.show()
