
TIPOS_COMBUSTIBLE = ["GASOLINA", "BIOETANOL", "DIESEL", "BIODIESEL", "GAS_NATURAL"]
TIPOS_AUTOMOVIL   = ["CIUDAD", "SUBCOMPACTO", "COMPACTO", "FAMILIAR", "EJECUTIVO", "SUV"]
TIPOS_COLOR       = ["BLANCO", "NEGRO", "ROJO", "NARANJA", "AMARILLO", "VERDE", "AZUL", "VIOLETA"]


class Automovil:


    def __init__(self, marca, modelo, motor, tipo_combustible,
                 tipo_automovil, numero_puertas, cantidad_asientos,
                 velocidad_maxima, color):
        self.__marca             = marca
        self.__modelo            = modelo
        self.__motor             = motor
        self.__tipo_combustible  = tipo_combustible
        self.__tipo_automovil    = tipo_automovil
        self.__numero_puertas    = numero_puertas
        self.__cantidad_asientos = cantidad_asientos
        self.__velocidad_maxima  = velocidad_maxima
        self.__color             = color
        self.__velocidad_actual  = 0         

   
    def get_marca(self):             return self.__marca
    def get_modelo(self):            return self.__modelo
    def get_motor(self):             return self.__motor
    def get_tipo_combustible(self):  return self.__tipo_combustible
    def get_tipo_automovil(self):    return self.__tipo_automovil
    def get_numero_puertas(self):    return self.__numero_puertas
    def get_cantidad_asientos(self): return self.__cantidad_asientos
    def get_velocidad_maxima(self):  return self.__velocidad_maxima
    def get_color(self):             return self.__color
    def get_velocidad_actual(self):  return self.__velocidad_actual

   
    def set_marca(self, marca):                         self.__marca             = marca
    def set_modelo(self, modelo):                       self.__modelo            = modelo
    def set_motor(self, motor):                         self.__motor             = motor
    def set_tipo_combustible(self, tipo_combustible):   self.__tipo_combustible  = tipo_combustible
    def set_tipo_automovil(self, tipo_automovil):       self.__tipo_automovil    = tipo_automovil
    def set_numero_puertas(self, numero_puertas):       self.__numero_puertas    = numero_puertas
    def set_cantidad_asientos(self, cantidad_asientos): self.__cantidad_asientos = cantidad_asientos
    def set_velocidad_maxima(self, velocidad_maxima):   self.__velocidad_maxima  = velocidad_maxima
    def set_color(self, color):                         self.__color             = color
    def set_velocidad_actual(self, velocidad_actual):   self.__velocidad_actual  = velocidad_actual

    
    def acelerar(self, incremento):

        if self.__velocidad_actual + incremento <= self.__velocidad_maxima:
            self.__velocidad_actual += incremento
        else:
            print("No se puede incrementar a una velocidad superior "
                  "a la máxima del automóvil.")

    def desacelerar(self, decremento):
      
        if self.__velocidad_actual - decremento >= 0:
            self.__velocidad_actual -= decremento
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self):
        
        self.__velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia_km):
        
        if self.__velocidad_actual == 0:
            print("El automóvil está detenido. No se puede calcular el tiempo.")
            return None
        return distancia_km / self.__velocidad_actual

    def imprimir(self):
        
        print("\n" + "─" * 40)
        print("       DATOS DEL AUTOMÓVIL")
        print("─" * 40)
        print(f"  Marca              : {self.__marca}")
        print(f"  Modelo             : {self.__modelo}")
        print(f"  Motor              : {self.__motor} L")
        print(f"  Tipo combustible   : {self.__tipo_combustible}")
        print(f"  Tipo automóvil     : {self.__tipo_automovil}")
        print(f"  Número de puertas  : {self.__numero_puertas}")
        print(f"  Cantidad asientos  : {self.__cantidad_asientos}")
        print(f"  Velocidad máxima   : {self.__velocidad_maxima} km/h")
        print(f"  Color              : {self.__color}")
        print(f"  Velocidad actual   : {self.__velocidad_actual} km/h")
        print("─" * 40 + "\n")



def leer_opcion(mensaje, opciones):

    print(mensaje)
    for i, op in enumerate(opciones, 1):
        print(f"  {i}. {op}")
    while True:
        try:
            idx = int(input("  Ingrese el número de opción: "))
            if 1 <= idx <= len(opciones):
                return opciones[idx - 1]
            print(f"  Por favor ingrese un número entre 1 y {len(opciones)}.")
        except ValueError:
            print("  Entrada inválida. Ingrese un número entero.")

def leer_entero(mensaje, minimo=None, maximo=None):
    
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"  El valor mínimo permitido es {minimo}.")
            elif maximo is not None and valor > maximo:
                print(f"  El valor máximo permitido es {maximo}.")
            else:
                return valor
        except ValueError:
            print("  Entrada inválida. Ingrese un número entero.")

def leer_flotante(mensaje, minimo=0.0):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < minimo:
                print(f"  El valor mínimo permitido es {minimo}.")
            else:
                return valor
        except ValueError:
            print("  Entrada inválida. Ingrese un número.")



def menu(auto):
    opciones_menu = [
        "Ver datos del automóvil",
        "Establecer velocidad actual",
        "Acelerar",
        "Desacelerar",
        "Frenar",
        "Calcular tiempo estimado de llegada",
        "Salir",
    ]

    while True:
        print("\n╔══════════════════════════════╗")
        print("║       MENÚ AUTOMÓVIL         ║")
        print("╚══════════════════════════════╝")
        for i, op in enumerate(opciones_menu, 1):
            print(f"  {i}. {op}")

        opcion = leer_entero("  Seleccione una opción: ", 1, len(opciones_menu))

        if opcion == 1:
            auto.imprimir()

        elif opcion == 2:
            vel = leer_entero(
                f"  Ingrese la velocidad actual (0 - {auto.get_velocidad_maxima()} km/h): ",
                0, auto.get_velocidad_maxima()
            )
            auto.set_velocidad_actual(vel)
            print(f"  Velocidad actual establecida en {auto.get_velocidad_actual()} km/h")

        elif opcion == 3:
            inc = leer_entero("  Ingrese el incremento de velocidad (km/h): ", 1)
            auto.acelerar(inc)
            print(f"  Velocidad actual = {auto.get_velocidad_actual()} km/h")

        elif opcion == 4:
            dec = leer_entero("  Ingrese el decremento de velocidad (km/h): ", 1)
            auto.desacelerar(dec)
            print(f"  Velocidad actual = {auto.get_velocidad_actual()} km/h")

        elif opcion == 5:
            auto.frenar()
            print(f"  Frenado. Velocidad actual = {auto.get_velocidad_actual()} km/h")

        elif opcion == 6:
            distancia = leer_flotante("  Ingrese la distancia a recorrer (km): ", 0.1)
            tiempo = auto.calcular_tiempo_llegada(distancia)
            if tiempo is not None:
                horas   = int(tiempo)
                minutos = int((tiempo - horas) * 60)
                print(f"  Tiempo estimado: {tiempo:.4f} h  →  {horas}h {minutos}min")

        elif opcion == 7:
            print("\n  ¡Hasta pronto!\n")
            break



def ingresar_automovil():
    print("\n" + "═" * 42)
    print("   REGISTRO DE NUEVO AUTOMÓVIL")
    print("═" * 42)

    marca    = input("  Marca: ").strip()
    modelo   = leer_entero("  Modelo (año de fabricación): ", 1900, 2100)
    motor    = leer_flotante("  Motor (litros de cilindraje): ", 0.1)
    combustible  = leer_opcion("\n  Tipo de combustible:", TIPOS_COMBUSTIBLE)
    tipo_auto    = leer_opcion("\n  Tipo de automóvil:",   TIPOS_AUTOMOVIL)
    puertas      = leer_entero("  Número de puertas: ",   2, 6)
    asientos     = leer_entero("  Cantidad de asientos: ", 1, 20)
    vel_max      = leer_entero("  Velocidad máxima (km/h): ", 1, 500)
    color        = leer_opcion("\n  Color:", TIPOS_COLOR)

    return Automovil(marca, modelo, motor, combustible,
                     tipo_auto, puertas, asientos, vel_max, color)



if __name__ == "__main__":

    auto1 = ingresar_automovil()
    menu(auto1)