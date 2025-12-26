import random
import math

radius = random.randint(3,10)
area = round(math.pi * (radius**2), 2) 

print(f"Raggio generato: {radius}")
print(f"L'area del cerchio è: {area}")
