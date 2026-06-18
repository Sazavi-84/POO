import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QMessageBox
)


class Vendedor:
    def __init__(self, nombre, apellidos):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = 0

    def verificar_edad(self, edad):
        if edad < 0 or edad > 120:
            raise ValueError(
                "La edad no puede ser negativa ni mayor a 120 años."
            )

        if edad < 18:
            raise ValueError(
                "El vendedor debe ser mayor de 18 años."
            )

        self.__edad = edad

    def imprimir(self):
        return (
            f"Nombre del vendedor: {self.__nombre}\n"
            f"Apellidos del vendedor: {self.__apellidos}\n"
            f"Edad del vendedor: {self.__edad}"
        )


class VentanaVendedor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registro de Vendedor")
        self.resize(400, 350)

        self.lbl_nombre = QLabel("Nombre:")
        self.txt_nombre = QLineEdit()

        self.lbl_apellidos = QLabel("Apellidos:")
        self.txt_apellidos = QLineEdit()

        self.lbl_edad = QLabel("Edad:")
        self.txt_edad = QLineEdit()

        self.btn_registrar = QPushButton("Registrar vendedor")
        self.btn_registrar.clicked.connect(self.registrar_vendedor)

        self.btn_limpiar = QPushButton("Limpiar")
        self.btn_limpiar.clicked.connect(self.limpiar_campos)

        self.txt_salida = QTextEdit()
        self.txt_salida.setReadOnly(True)

        layout = QVBoxLayout()

        layout.addWidget(self.lbl_nombre)
        layout.addWidget(self.txt_nombre)

        layout.addWidget(self.lbl_apellidos)
        layout.addWidget(self.txt_apellidos)

        layout.addWidget(self.lbl_edad)
        layout.addWidget(self.txt_edad)

        layout.addWidget(self.btn_registrar)
        layout.addWidget(self.btn_limpiar)
        layout.addWidget(self.txt_salida)

        self.setLayout(layout)

    def registrar_vendedor(self):
        try:
            nombre = self.txt_nombre.text().strip()
            apellidos = self.txt_apellidos.text().strip()

            if nombre == "" or apellidos == "":
                raise ValueError(
                    "Debe ingresar nombre y apellidos."
                )

            edad = int(self.txt_edad.text())

            vendedor = Vendedor(nombre, apellidos)
            vendedor.verificar_edad(edad)

            self.txt_salida.setText(vendedor.imprimir())

            QMessageBox.information(
                self,
                "Éxito",
                "Vendedor registrado correctamente."
            )

        except ValueError as e:
            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

    def limpiar_campos(self):
        self.txt_nombre.clear()
        self.txt_apellidos.clear()
        self.txt_edad.clear()
        self.txt_salida.clear()
        self.txt_nombre.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaVendedor()
    ventana.show()

    sys.exit(app.exec())