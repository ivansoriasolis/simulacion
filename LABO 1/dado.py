import random
n= 100000000
conteo = { n:0 for n in range(1,7)}

for i in range(0,n):
    lanzamiento = random.randint(1,6)
    conteo[lanzamiento]+=1

for i in conteo:
    print("Probabilidad de que salga %d: %f"%(i,conteo[i]/n))
