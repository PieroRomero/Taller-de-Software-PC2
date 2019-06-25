import random

def RandomSinRepetir(min, max, numElem):
    N = list(range(min, max + 1))
    random.shuffle(N)
    
    C = []
    for i in range(numElem):
        e = N[0]
        N.remove(e)
        C.append(e)

    return N

print("Por favor, ingrese 6 números distintos del 1 al 10")

C = RandomSinRepetir(1, 10, 6)

acert = 0

U = []
while len(U) < 6:
    n = int(input("Ingrese un número: "))
    if 1 <= n <= 10:
        if U.count(n) > 1:
            print("no debe repetir de número")
        else:
            U.append(n)
            acert = acert + 1 
    else:
        print("Debe ingresar un número entre 1 y 10. Intente de nuevo")

if acert == 6:
    print("Ha ganado 6 millones de soles")
elif acert == 5:
    print("Ha ganado 100 mil soles")
else:
    print("Siga intentado")