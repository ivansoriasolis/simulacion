import random

iteraciones = 1000
personas = 25
ocurrencias = 0

for iter in range(iteraciones):
    cumples = [random.randint(1,365) for i in range(personas)]
    if len([i for i in cumples if cumples.count(i)>1])!=0:
        ocurrencias += 1

print(float(ocurrencias)/iteraciones)
    
