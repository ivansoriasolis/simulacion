import random

def lanzarMoneda():
    return random.choice(["cara","sello"])

tiradas = 1000
caras = 0
sellos = 0

for i in range(tiradas):
    resultado = lanzarMoneda()
    if resultado == "cara":
        caras += 1
    else:
        sellos += 1
#asdfasfasf
    
print("%d caras: %f"%(caras,caras/tiradas))
print("%d caras: %f"%(sellos,sellos/tiradas))
