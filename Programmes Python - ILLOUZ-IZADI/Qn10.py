import matplotlib.pyplot as plt
import numpy.random as rd
import math as math

# Définition des paramètres
M=20
h=1/M
N=100


#Définition de la fonction g : 
def g(x,y):
    return (math.exp(math.pi*y))*math.sin(math.pi*x)

# Définition de wh(x) et U(x,y) : 
wh=[[0 for i in range(M)] for j in range(M)]
U=[[g(x*h,y*h) for x in range(M)] for y in range(M)]

# Définition de D_h :
Dh=[h*i for i in range(M)]



# Simulation de N variables X_n partant d'une postion (x,y)
for x in range(M):
    for y in range(M):
        # tableau afin de compter les fréquences des arrivées sur les 4 bords
        # en rotation dans le sens trigonométrique
        Nc=[0 for k in range(4*M+1)]
        for n in range (N+1):
            # Simulation des X_n (reprise programme Qn3)
            # où X a maintenant deux coordonnées
            X=[x*h,y*h]
            while X[0]<1 and X[0]>0 and X[1]<1 and X[1]>0 :
                ksi=rd.randint(0,4) # Loi uniforme sur X(Omega)={0,1,2,3}
                if ksi==0:
                    X[0]=X[0]+h
                if ksi==1:
                    X[0]=X[0]-h
                if ksi==2:
                    X[1]=X[1]+h
                if ksi==3:
                    X[1]=X[1]-h
            # Incrémentation  compteur de fréquences d'arrivées sur les bords
            if X[1]<=0: # en bas
                Nc[math.floor(X[0]*M)] += 1/(N)
            elif X[0]>=1 : # à droite
                Nc[M+math.floor(X[1]*M)] += 1/(N)
            elif X[1]>=1: # en haut
                Nc[3*M-math.floor(X[1]*M)] += 1/(N)
            elif X[0]<=0: # à gauche
                Nc[4*M-math.floor(X[1]*M)] += 1/(N)
        # Calcul de wh    
        for k in range(M+1):
            wh[x][y]+=g(k*h,0)*Nc[k]+g(1,k*h)*Nc[M+k]+g(k*h,1)*Nc[2*M-k]+g(0,k*h)*Nc[4*M-k]
   

# Tracé du graphe z = wh(x,y)
from pylab import *
#imshow(wh)
#imshow(U)


import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1,2,1, projection='3d')

x = y = np.arange(0, 1.0, h)
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, wh, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_xlabel("$\ x $")
ax.set_ylabel("$\ y $")
ax.set_zlabel("$\ Courbe\ de\ V_h(x) $")
                       
ax = fig.add_subplot(1,2,2, projection='3d')
ax.plot_surface(X, Y, U, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
                                        

ax.set_xlabel("$\ x $")
ax.set_ylabel("$\ y $")
ax.set_zlabel("$\ Courbe\ de\ U(x) $")

plt.show()