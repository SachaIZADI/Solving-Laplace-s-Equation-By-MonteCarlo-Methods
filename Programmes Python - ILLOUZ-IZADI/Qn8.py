import matplotlib.pyplot as plt
import numpy.random as rd
from math import*

# Définition des paramètres
N=1000
global a
a=0
global b
b=0

# Definition de {h}
hmin=5*10**(-3)
hmax=0.5
nbH=100

H_liste = [hmin+(hmax-hmin)*k/nbH for k in range(nbH)]



# Simulation de N variables X_n partants de la position x (=0.5), pour nbH valeurs du pas h : en tout N*nbH simulations
def E(x,H_liste,N):
    # Definition de {E} l'espérance de T_x
    E=[]
    for h in H_liste :
        ST=0 # Somme des Temps d'atteinte
        for n in range (N+1):
            # Simulation des X_n
            X=x
            while X<1 and X>0 :
                ksi=rd.randint(0,2) # Loi de Bernoulli B(0.5) : X(Omega)={0,1}
                # transformation X(Omega)={0,1} --> ksi(Omega)={-1,1}
                if ksi==0:
                    ksi=-1
                X=X+ksi*h # Calcul de X_k
                ST+=1
        E+=[ST/N] # Espérance approchée par une moyenne
    return E


# Tracé du graphe E(T^x) en fonction de h
plt.clf()
plt.plot(H_liste,E(0.5,H_liste,N),'red')
plt.plot(H_liste,E(0.9,H_liste,N),'blue')
plt.plot(H_liste,E(0.1,H_liste,N),'green')
plt.legend(["$\ \mathbb{E}(T^{\ 0.5})=f(h) $","$\ \mathbb{E}(T^{\ 0.9})=f(h) $","$\ \mathbb{E}(T^{\ 0.1})=f(h) $"], loc="best")
plt.title("$\ Graphe\ de\ \mathbb{E}(T^x) $")
plt.xlabel("$\ h $")
plt.ylabel("$\ \mathbb{E}(T^x) $")
#plt.axis([hmin, hmax, 0, 0.1])
plt.yscale('log')
plt.xscale('log')
plt.grid(True,which="both")
plt.show()