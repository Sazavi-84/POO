import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QTextEdit, QVBoxLayout,
    QGridLayout, QMessageBox
)


class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores = []

    def esta_lleno(self):
        return len(self.programadores) >= 3

    def esta_completo(self):
        return 2 <= len(self.programadores) <= 3

    def agregar_programador(self, programador):
        if self.esta_lleno():
            raise Exception(
                "El equipo está completo. No se puede agregar más programadores."
            )
        self.programadores.append(programador)

    @staticmethod
    def validar_campo(campo):
        if not campo.strip():
            raise Exception("El campo no puede estar vacío.")

        if len(campo) > 20:
            raise Exception(
                "La longitud no debe ser superior a 20 caracteres."
            )

        for caracter in campo:
            if caracter.isdigit():
                raise Exception(
                    "El nombre o apellido no puede contener dígitos."
                )


class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Equipo Maratón de Programación")
        self.resize(700, 500)

        self.equipo = None

        layout = QVBoxLayout()

        grid = QGridLayout()

        self.txtEquipo = QLineEdit()
        self.txtUniversidad = QLineEdit()
        self.txtLenguaje = QLineEdit()

        self.txtNombre = QLineEdit()
        self.txtApellido = QLineEdit()

        grid.addWidget(QLabel("Nombre del equipo:"), 0, 0)
        grid.addWidget(self.txtEquipo, 0, 1)

        grid.addWidget(QLabel("Universidad:"), 1, 0)
        grid.addWidget(self.txtUniversidad, 1, 1)

        grid.addWidget(QLabel("Lenguaje de programación:"), 2, 0)
        grid.addWidget(self.txtLenguaje, 2, 1)

        grid.addWidget(QLabel("Nombre del programador:"), 3, 0)
        grid.addWidget(self.txtNombre, 3, 1)

        grid.addWidget(QLabel("Apellidos del programador:"), 4, 0)
        grid.addWidget(self.txtApellido, 4, 1)

        layout.addLayout(grid)

        self.btnAgregar = QPushButton("Agregar Programador")
        self.btnMostrar = QPushButton("Mostrar Equipo")
        self.btnLimpiar = QPushButton("Limpiar")

        layout.addWidget(self.btnAgregar)
        layout.addWidget(self.btnMostrar)
        layout.addWidget(self.btnLimpiar)

        self.salida = QTextEdit()
        self.salida.setReadOnly(True)

        layout.addWidget(self.salida)

        self.setLayout(layout)

        self.btnAgregar.clicked.connect(self.agregar_programador)
        self.btnMostrar.clicked.connect(self.mostrar_equipo)
        self.btnLimpiar.clicked.connect(self.limpiar)

    def crear_equipo(self):
        if self.equipo is None:
            nombre_equipo = self.txtEquipo.text().strip()
            universidad = self.txtUniversidad.text().strip()
            lenguaje = self.txtLenguaje.text().strip()

            if not nombre_equipo or not universidad or not lenguaje:
                raise Exception(
                    "Debe ingresar los datos del equipo."
                )

            self.equipo = EquipoMaratonProgramacion(
                nombre_equipo,
                universidad,
                lenguaje
            )

    def agregar_programador(self):
        try:
            self.crear_equipo()

            nombre = self.txtNombre.text().strip()
            apellido = self.txtApellido.text().strip()

            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellido)

            programador = Programador(nombre, apellido)

            self.equipo.agregar_programador(programador)

            QMessageBox.information(
                self,
                "Éxito",
                "Programador agregado correctamente."
            )

            self.txtNombre.clear()
            self.txtApellido.clear()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def mostrar_equipo(self):
        try:
            if self.equipo is None:
                raise Exception("No se ha creado ningún equipo.")

            texto = (
                f"Equipo: {self.equipo.nombre_equipo}\n"
                f"Universidad: {self.equipo.universidad}\n"
                f"Lenguaje: {self.equipo.lenguaje_programacion}\n\n"
                f"Integrantes ({len(self.equipo.programadores)}):\n"
            )

            for i, p in enumerate(self.equipo.programadores, start=1):
                texto += f"{i}. {p.nombre} {p.apellidos}\n"

            texto += (
                "\nEstado: Completo"
                if self.equipo.esta_completo()
                else "\nEstado: Incompleto"
            )

            self.salida.setPlainText(texto)

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def limpiar(self):
        self.txtEquipo.clear()
        self.txtUniversidad.clear()
        self.txtLenguaje.clear()
        self.txtNombre.clear()
        self.txtApellido.clear()
        self.salida.clear()
        self.equipo = None


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = Ventana()
    ventana.show()

    sys.exit(app.exec())