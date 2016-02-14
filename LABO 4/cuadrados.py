import math

semilla = 4345
nsimo = 5

def cuadradosMedios(semilla, nsimo):
    X = semilla
    D = math.ceil(math.log10(semilla))
    for n in range(nsimo):
        Y = X**2
        longY = math.ceil(math.log10(Y))
        iniY = longY-((longY - D) // 2)
        finY = iniY - D
        X1 = (Y % (10**(iniY))) // 10**finY
        X = X1
    return X/10**D

print(cuadradosMedios(semilla,nsimo))


