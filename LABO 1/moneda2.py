import random

ncaras = 0
nsellos = 0

n = 1000

for i in range(0,n):
    lanzamiento = random.randint(0,1)
    if lanzamiento == 1:
        ncaras +=1
    else:
        nsellos +=1

print("caras: ",ncaras)
print("sellos:",nsellos)


