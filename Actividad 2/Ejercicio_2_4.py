import math


class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
       
        return 2 * math.pi * self.radio

    def __str__(self):
        return (f"Círculo (radio={self.radio} cm)\n"
                f"  Área      : {self.calcular_area():.4f} cm²\n"
                f"  Perímetro : {self.calcular_perimetro():.4f} cm")


class Rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
       
        return self.base * self.altura

    def calcular_perimetro(self):
        
        return 2 * self.base + 2 * self.altura

    def __str__(self):
        return (f"Rectángulo (base={self.base} cm, altura={self.altura} cm)\n"
                f"  Área      : {self.calcular_area():.4f} cm²\n"
                f"  Perímetro : {self.calcular_perimetro():.4f} cm")


class Cuadrado:
    

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        
        return self.lado ** 2

    def calcular_perimetro(self):
        
        return 4 * self.lado

    def __str__(self):
        return (f"Cuadrado (lado={self.lado} cm)\n"
                f"  Área      : {self.calcular_area():.4f} cm²\n"
                f"  Perímetro : {self.calcular_perimetro():.4f} cm")


class TrianguloRectangulo:
    

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def calcular_perimetro(self):
        
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo(self):
        h = self.calcular_hipotenusa()
        lados = {round(self.base, 6), round(self.altura, 6), round(h, 6)}
        if len(lados) == 1:
            return "Equilátero (todos sus lados son iguales)"
        elif len(lados) == 2:
            return "Isósceles (tiene dos lados iguales)"
        else:
            return "Escaleno (todos sus lados son diferentes)"

    def __str__(self):
        return (f"Triángulo Rectángulo (base={self.base} cm, altura={self.altura} cm)\n"
                f"  Área        : {self.calcular_area():.4f} cm²\n"
                f"  Hipotenusa  : {self.calcular_hipotenusa():.4f} cm\n"
                f"  Perímetro   : {self.calcular_perimetro():.4f} cm\n"
                f"  Tipo        : {self.determinar_tipo()}")




def leer_numero(mensaje, positivo=True):
   
    while True:
        try:
            valor = float(input(mensaje))
            if positivo and valor <= 0:
                print("    El valor debe ser mayor que cero. Intente de nuevo.")
            else:
                return valor
        except ValueError:
            print("    Entrada inválida. Ingrese un número.")


def separador(titulo=""):
    ancho = 50
    if titulo:
        print(f"\n{'─' * 5} {titulo} {'─' * (ancho - len(titulo) - 7)}")
    else:
        print("─" * ancho)



def menu():
    opciones = {
        "1": "Círculo",
        "2": "Rectángulo",
        "3": "Cuadrado",
        "4": "Triángulo Rectángulo",
        "5": "Salir",
    }

    print("\n" + "═" * 50)
    print("    FIGURAS GEOMÉTRICAS")
    print("═" * 50)

    while True:
        separador("MENÚ")
        for k, v in opciones.items():
            print(f"  {k}. {v}")
        separador()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            separador("CÍRCULO")
            r = leer_numero("  Radio (cm): ")
            figura = Circulo(r)
            print()
            print(figura)

        elif opcion == "2":
            separador("RECTÁNGULO")
            b = leer_numero("  Base (cm)  : ")
            a = leer_numero("  Altura (cm): ")
            figura = Rectangulo(b, a)
            print()
            print(figura)

        elif opcion == "3":
            separador("CUADRADO")
            l = leer_numero("  Lado (cm): ")
            figura = Cuadrado(l)
            print()
            print(figura)

        elif opcion == "4":
            separador("TRIÁNGULO RECTÁNGULO")
            b = leer_numero("  Base (cm)  : ")
            a = leer_numero("  Altura (cm): ")
            figura = TrianguloRectangulo(b, a)
            print()
            print(figura)

        elif opcion == "5":
            print("\n  ¡Hasta luego!\n")
            break

        else:
            print("  Opción no válida. Elija entre 1 y 5.")

        input("\n  Presione Enter para continuar...")


if __name__ == "__main__":
    menu()