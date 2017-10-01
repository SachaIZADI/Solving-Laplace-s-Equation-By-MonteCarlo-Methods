import matplotlib.pyplot as plt
import numpy.random as rd
from math import*

# Définition des paramètres
x=0.5
N=1000
global a
a=0.5
global b
b=1

# Definition de {h}
hmin=5*10**(-3)
hmax=0.5
nbH=100

H_liste = [hmin+(hmax-hmin)*k/nbH for k in range(nbH)]

# Définition de l'erreur :
err=[]

# Solution exacte u(x) et calcul de la valeur attendue U=u(x_0)
def u(x):
    return((b-a)*x + a)
U=u(x)

# Simulation de N variables X_n partants de la position x (=0.5), pour nbH valeurs du pas h : en tout N*nbH simulations

for h in H_liste :
    # Définition de N0 et N1 : Ni = nombre de réalisation de [X_Tx = i]
    N0=0
    N1=0
    for n in range (N+1):
        # Simulation des X_n
        X=x
        while X<1 and X>0 :
            ksi=rd.randint(0,2) # Loi de Bernoulli B(0.5) : X(Omega)={0,1}
            # transformation X(Omega)={0,1} --> ksi(Omega)={-1,1}
            if ksi==0:
                ksi=-1
            X=X+ksi*h # Calcul de X_k
        if X>=1:
            N1=N1+1
        else :
            N0=N0+1
    # Calcul de |wh(x)-u(x)| où wh(x) = a*P(X_Tx = 0) + b*P(X_Tx = 1) 
    # et où l'on approxime P(X_Tx = i) = Ni/N = fi
    wh=a*N0/N+b*N1/N
    err=err+[abs(wh-U)]


# Tracé du graphe err=|wh(x)-u(x)| en fonction de h
plt.clf()
plt.plot(H_liste,err)
plt.title("$\ Graphe\ de\ err=|w_{h}(x)-u(x)| $")
plt.xlabel("$\ h $")
plt.ylabel("$\ err $")
#plt.axis([hmin, hmax, 0, 0.1])
plt.yscale('log')
plt.xscale('log')
plt.grid(True,which="both")
plt.show()