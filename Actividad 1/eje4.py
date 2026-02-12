# Ejercicio Propuesto N°14

import math
class cal:
    @staticmethod
    def cuadrado(n):
        return math.pow(n,2)
    @staticmethod
    def cubo(n):
        return math.pow(n,3)

n = int(input("Ingrese un numero: "))

print(f"El cuadrado de {n} es {cal.cuadrado(n):.0f} y el cubo es {cal.cubo(n):.0f}")
