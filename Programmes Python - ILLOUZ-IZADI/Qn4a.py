import matplotlib.pyplot as plt
import numpy.random as rd
import math

# Définition des paramètres
h=3*10**(-2)
N=1000
global a
a=0.5
global b
b=1

# Définition de wh(x) : 
wh=[]*math.floor(1/h)

# Définition de I_h :
Ih=[h*i for i in range(math.floor(1/h)+1)]

# Solution exacte u(x)
def u(x):
    return((b-a)*x + a)
U=[u(x) for x in Ih]

# Simulation de N variables X_n partant d'une postion x de I_h : en tout N*h^(-1) simulations
# En moyenne il y a N*h^(-1)*E(E(T_x)) itérations

for x in Ih:
    # Définition de N0 et N1 : Ni = nombre de réalisation de [X_Tx = i]
    N0=0
    N1=0
    for n in range (N+1):
        # Simulation des X_n (reprise programme Qn3)
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
    # Calcul de wh(x) = a*P(X_Tx = 0) + b*P(X_Tx = 1) où l'on approxime P(X_Tx = i) = Ni/N = fi
    wh=wh+[a*N0/N+b*N1/N]


# Tracé du graphe y = wh(x)
plt.clf()
plt.plot(Ih,wh)
plt.plot(Ih,U,"--")
plt.title("$\ Comparaison\ entre\ w_{h}(x)\ et\ u(x)$")
plt.xlabel("$\ x $")
plt.ylabel("$\ y(x) $")
plt.legend(["$\ y=w_{h}(x) $","$\ y=u(x) $"], loc="best")
plt.axis([0, 1, 0, b])
plt.grid()
plt.show()



