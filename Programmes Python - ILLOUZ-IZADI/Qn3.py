import matplotlib.pyplot as plt
import numpy.random as rd


# Définition des paramètres
x=0.5
h=5*10**(-2)

# Liste de liste : stockage des 5 simulations
X_liste=[]

for j in range(5):

    X=[x]
    
    k=0
    
    while X[k]<1 and X[k]>0 :
        ksi=rd.randint(0,2) # Loi de Bernoulli B(0.5) : X(Omega)={0,1}
        # transformation X(Omega)={0,1} --> ksi(Omega)={-1,1}
        if ksi==0:
            ksi=-1
        X=X+[X[k]+ksi*h] # Calcul et Stockage de X_k
        k+=1
    
    print("la trajectoire s'arrête en x =",X[k],"et le temps d'attente T_x =",k)
    X_liste+=[X] # Stockage de la simulation



# Tracé des graphes X_n = f(n)
for j in range(5):
    N_liste=range(len(X_liste[j]))
    plt.plot(N_liste,X_liste[j])
plt.title("$\ Simulations\ de\ X_{n}\ pour\ n\in[0;T^{x}] $")
plt.xlabel("$\ n $")
plt.ylabel("$\ X_{n} $")
plt.grid()
plt.show()

