import matplotlib.pyplot as plt
import numpy.random as rd
from math import*

# Définition des paramètres
x=0.5
h=5*10**(-3)
global a
a=0
global b
b=0

# Definition de {N}
Nmax=10**3
N_liste=[k for k in range(1,Nmax+1)]

# Définition de l'erreur :
err=[]

#Définition de la fonction f : 
def f(x):
    return math.sin(2*math.pi*x)
    
# Solution exacte u(x)
def u(x):
    return(-1/(4*(math.pi)**2)*f(x))
U =u(x)

# Simulation de Nmax variables X_n partants de la position x (=0.5), pour h=5.10**(-3)
# A chaque itération N -- N+1, on calcule l'erreur |wh(x)-u(x)|_N

S=0
for N in N_liste:
    # Simulation des X_n
    X=x
    while X<1 and X>0 :
        ksi=rd.randint(0,2) # Loi de Bernoulli B(0.5) : X(Omega)={0,1}
        # transformation X(Omega)={0,1} --> ksi(Omega)={-1,1}
        if ksi==0:
            ksi=-1
        X=X+ksi*h # Calcul de X_k
        S+=f(X) #Calcul de la somme des f(X_k)
    #Approximation de l'espérance par une moyenne (Loi des grands nombres)et Calcul de |wh(x)-u(x)|_
    wh=-h**2*(S/N)/2
    err=err+[abs(wh-U)]


# Tracé du graphe err=|wh(x)-u(x)| en fonction de h
plt.clf()
plt.plot(N_liste,err)
plt.title("$\ Graphe\ de\ err=|w_{h}(x)-u(x)| $")
plt.xlabel("$\ N $")
plt.ylabel("$\ err $")
#plt.axis([hmin, hmax, 0, 0.1])
plt.yscale('log')
plt.xscale('log')
plt.grid(True,which="both")
plt.show()