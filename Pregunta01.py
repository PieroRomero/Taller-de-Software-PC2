def crearMatrizCuadradaYVerficarParidadDeLaDiagonal(numLado):
    N = []

    for x in range(numLado):
        M = []
        for y in range(numLado):
            e = int(input("Ingrese un número: "))
            M.append(e)    
        N.append(M)
    
    print("La matriz N es igual a:", N)

    d = 0 
    for n in range(numLado):
        d = d + N[n][n]

    print("La suma de los números de la diagonal es:", d)

    if d % 2 == 0:
        print("La suma de los números de la diagonal es par")
    else:
        print("La suma de los números de la diagonal es impar")

crearMatrizCuadradaYVerficarParidadDeLaDiagonal(3)
crearMatrizCuadradaYVerficarParidadDeLaDiagonal(4)
crearMatrizCuadradaYVerficarParidadDeLaDiagonal(5)
