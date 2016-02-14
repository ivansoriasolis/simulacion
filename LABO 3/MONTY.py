import random
iteraciones = 1000
ganacambio = 0
cubos = 4
for n in range(iteraciones):
    balde = [None]*cubos
    balde[random.randrange(cubos)]="Premio"
    eleccion = random.randrange(cubos)
    mostrado = random.choice([i for i in range(cubos) if balde[i]!="Premio" and i != eleccion])
    cambio = random.choice([i for i in range(cubos) if i != mostrado and i != eleccion])
    if balde[cambio]=="Premio":
        ganacambio+=1
print(ganacambio/iteraciones)
