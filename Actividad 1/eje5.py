# Ejercicio Propuesto N°17

import math
class circulo:
    @staticmethod  
    def area(radio):
        return math.pi * math.pow(radio,2)
    @staticmethod
    def perimetro(radio):
        return 2 * math.pi * radio

r = float(input("Ingrese el radio del circulo: "))
print(f"El area es {circulo.area(r):.3f}\nLa longitud de la circunferencia es: {circulo.perimetro(r):.3f}")