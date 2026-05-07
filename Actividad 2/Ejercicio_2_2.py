
from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"


class Planeta:
    def __init__(self, nombre, can_satelites, masa, volumen, diametro, distancia_al_sol, tipo, es_observable):
        self.nombre = nombre
        self.can_satelites = can_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_al_sol = distancia_al_sol
        self.tipo = tipo
        self.es_observable = es_observable
    
    def imprimir(self):
        print(f"\n----------------Planeta----------------\n")
        print(f"Nombre del planeta: {self.nombre}")   
        print(f"Cantidad de satelites: {self.can_satelites}")   
        print(f"Masa del planta: {self.masa}")   
        print(f"Volumen del planeta: {self.volumen}")   
        print(f"Diámetro del planeta: {self.diametro}")
        print(f"Distancia al sol: {self.distancia_al_sol}")
        print(f"Tipo de planeta: {self.tipo.name}")
        print(f"Es observable: {self.es_observable}")
    
    def cal_densidad(self):
        return self.masa / self.volumen if self.volumen != 0 else 0
    
    def es_planta_esterior(self):
        limite = 149597870 * 3.4
        return self.distancia_al_sol > limite
    
def ingresar_planeta():
    nombre = input("\nIngrese el nombre del planeta: ")
    can_satelites = int(input("Ingrese cantidad de satélites: "))
    masa = float(input("Ingrese la masa: "))
    volumen = float(input("Ingrese el volumen: "))
    diametro = int(input("Ingrese el diámetro: "))
    distancia_al_sol=int(input("Ingrese la distancia al sol: "))
    
    return nombre, can_satelites, masa, volumen, diametro, distancia_al_sol


dt_p1 =ingresar_planeta()
planeta_1 = Planeta(*dt_p1, TipoPlaneta.TERRESTRE,True)

planeta_1.imprimir()
print(f"Es planeta exterior: {planeta_1.es_planta_esterior()}")
print(f"Densidad del planeta: {planeta_1.cal_densidad()}")
print(f"\n---------------------------------------\n")