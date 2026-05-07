from enum import Enum


class TipoCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"


class CuentaBancaria:
    

    def __init__(self, nombres_titular: str, apellidos_titular: str,
                 numero_cuenta: int, tipo_cuenta: TipoCuenta):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo: float = 0.0  

    def imprimir(self):
      
        print("\n" + "=" * 45)
        print("         DATOS DE LA CUENTA BANCARIA")
        print("=" * 45)
        print(f"  Nombres del titular  : {self.nombres_titular}")
        print(f"  Apellidos del titular: {self.apellidos_titular}")
        print(f"  Número de cuenta     : {self.numero_cuenta}")
        print(f"  Tipo de cuenta       : {self.tipo_cuenta.value}")
        print(f"  Saldo                : ${self.saldo:,.2f}")
        print("=" * 45)

    def consultar_saldo(self):
        
        print(f"\n  Saldo actual: ${self.saldo:,.2f}")

    def consignar(self, valor: float) -> bool:
        
        if valor > 0:
            self.saldo += valor
            print(f"\n  Se han consignado ${valor:,.2f}.")
            print(f"     Nuevo saldo: ${self.saldo:,.2f}")
            return True
        else:
            print("\n  El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor: float) -> bool:

        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"\n  Se han retirado ${valor:,.2f}.")
            print(f"     Nuevo saldo: ${self.saldo:,.2f}")
            return True
        elif valor <= 0:
            print("\n  El valor a retirar debe ser mayor que cero.")
            return False
        else:
            print(f"\n  Fondos insuficientes. Saldo actual: ${self.saldo:,.2f}")
            return False



def leer_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Ingrese un número entero válido.")


def leer_float(mensaje: str) -> float:
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("  Ingrese un número válido.")


def seleccionar_tipo_cuenta() -> TipoCuenta:
    print("\n  Tipo de cuenta:")
    print("    1. Ahorros")
    print("    2. Corriente")
    while True:
        opcion = input("  Seleccione (1/2): ").strip()
        if opcion == "1":
            return TipoCuenta.AHORROS
        elif opcion == "2":
            return TipoCuenta.CORRIENTE
        else:
            print("  Opción inválida. Ingrese 1 o 2.")


def mostrar_menu() -> str:
    print("\n" + "-" * 45)
    print("             MENÚ DE OPERACIONES")
    print("-" * 45)
    print("  1. Ver datos de la cuenta")
    print("  2. Consultar saldo")
    print("  3. Consignar")
    print("  4. Retirar")
    print("  5. Salir")
    print("-" * 45)
    return input("  Seleccione una opción: ").strip()




def main():
    print("\n" + "=" * 45)
    print("       CREACIÓN DE CUENTA BANCARIA")
    print("=" * 45)

    nombres = input("  Nombres del titular    : ").strip()
    apellidos = input("  Apellidos del titular  : ").strip()
    numero = leer_entero("  Número de cuenta       : ")
    tipo = seleccionar_tipo_cuenta()

    cuenta = CuentaBancaria(nombres, apellidos, numero, tipo)
    print("\n  ¡Cuenta creada exitosamente con saldo inicial $0!")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            cuenta.imprimir()
        elif opcion == "2":
            cuenta.consultar_saldo()
        elif opcion == "3":
            valor = leer_float("  Valor a consignar: $")
            cuenta.consignar(valor)
        elif opcion == "4":
            valor = leer_float("  Valor a retirar: $")
            cuenta.retirar(valor)
        elif opcion == "5":
            print("\n  ¡Hasta luego!\n")
            break
        else:
            print("   Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()