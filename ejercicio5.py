# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x=0
z=0
y=2.0
t=0

listax=[]
listay=[]
listaz=[]
delta=0.5

while t<5:
    x=x+(delta*10.0*(y-x))  #Escogo variar primero x porque depende solo de x y de y, por tanto cambiando yo ya queda
    z=z+(delta*(xy-2.67*z)) #Escojo variar segundo z porque ya tenemos x y y
    y=y*(delta*(28.0*x-y-xz))
    listax.append(x)
    listay.append(y)
    listaz.append(z)
    t=t+delta








