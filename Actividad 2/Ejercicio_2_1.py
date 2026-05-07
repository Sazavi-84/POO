class Persona:
    def __init__(self, nombre, apellido, num_doc, a_nac):
        self.nombre = nombre
        self.apellido = apellido
        self.num_doc = num_doc
        self.a_nac = a_nac

    def mostrar_persona(self):
        print("\n----------------------------------\n")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Numero de documento de identidad: {self.num_doc}")
        print(f"Año de nacimoento: {self.a_nac}")
        print("\n----------------------------------")

def ingresar_persona():
    nombre = input("Ingresa el nombre: ")
    apellido = input("Ingresa el apellido: ")
    num_doc = input("Ingrese el número de documento: ")
    a_nac = int(input("Ingrese el año de nacimiemto: "))
    return nombre, apellido, num_doc, a_nac

print("\nPersona 1:")
dt_persona_1= ingresar_persona()
persona_1 = Persona(*dt_persona_1)

print("\nPersona 2: ")
dt_persona_2= ingresar_persona()
persona_2 = Persona(*dt_persona_2)

persona_1.mostrar_persona()
persona_2.mostrar_persona()

