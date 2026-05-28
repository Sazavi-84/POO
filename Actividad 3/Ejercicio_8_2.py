import sys
import math
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QMessageBox
)


class AnalisisNotas:

    def __init__(self, notas):
        self.notas = notas

    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()

        suma = 0
        for nota in self.notas:
            suma += (nota - promedio) ** 2

        return math.sqrt(suma / len(self.notas))

    def obtener_mayor(self):
        return max(self.notas)

    def obtener_menor(self):
        return min(self.notas)


class Ventana(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Sistema de Notas"
        )

        self.resize(420, 450)

        self.setStyleSheet("""
            QWidget {
                background-color: #0D0D0D;
                color: #00F5FF;
                font-size: 14px;
                font-family: Consolas;
            }

            QLabel {
                color: #FF00FF;
                font-size: 16px;
                font-weight: bold;
            }

            QLineEdit {
                background-color: #161616;
                color: #00F5FF;
                border: 2px solid #00F5FF;
                border-radius: 12px;
                padding: 10px;
                font-size: 14px;
            }

            QLineEdit:focus {
                border: 2px solid #FF00FF;
                background-color: #1E1E1E;
            }

            QPushButton {
                background-color: #7A00FF;
                color: white;
                border: 2px solid #FF00FF;
                border-radius: 12px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #A020F0;
                border: 2px solid #00F5FF;
            }

            QPushButton:pressed {
                background-color: #5500AA;
            }
        """)

        self.titulo = QLabel(
            "Sistema de Analisis de Notas"
        )

        self.nota1 = QLineEdit()
        self.nota1.setPlaceholderText(
            "Ingrese Nota 1"
        )

        self.nota2 = QLineEdit()
        self.nota2.setPlaceholderText(
            "Ingrese Nota 2"
        )

        self.nota3 = QLineEdit()
        self.nota3.setPlaceholderText(
            "Ingrese Nota 3"
        )

        self.nota4 = QLineEdit()
        self.nota4.setPlaceholderText(
            "Ingrese Nota 4"
        )

        self.nota5 = QLineEdit()
        self.nota5.setPlaceholderText(
            "Ingrese Nota 5"
        )

        self.boton_calcular = QPushButton(
            "Calcular"
        )

        self.boton_limpiar = QPushButton(
            "Limpiar"
        )

        self.boton_calcular.clicked.connect(
            self.calcular
        )

        self.boton_limpiar.clicked.connect(
            self.limpiar
        )

        self.resultado = QLabel("")

        layout = QVBoxLayout()

        layout.addWidget(
            self.titulo
        )

        layout.addWidget(
            self.nota1
        )

        layout.addWidget(
            self.nota2
        )

        layout.addWidget(
            self.nota3
        )

        layout.addWidget(
            self.nota4
        )

        layout.addWidget(
            self.nota5
        )

        layout.addWidget(
            self.boton_calcular
        )

        layout.addWidget(
            self.boton_limpiar
        )

        layout.addWidget(
            self.resultado
        )

        self.setLayout(layout)

    def mostrar_alerta(
            self, mensaje):

        alerta = QMessageBox()

        alerta.setWindowTitle(
            "Error"
        )

        alerta.setText(mensaje)

        alerta.setIcon(
            QMessageBox.Warning
        )

        alerta.exec()

    def obtener_notas(self):

        campos = [
            self.nota1,
            self.nota2,
            self.nota3,
            self.nota4,
            self.nota5
        ]

        notas = []

        for i, campo in enumerate(
                campos, start=1):

            texto = campo.text().strip()

            if texto == "":

                self.mostrar_alerta(
                    f"Debe ingresar "
                    f"la nota {i}"
                )

                return None

            try:
                nota = float(texto)

                if nota < 0 or nota > 5:

                    self.mostrar_alerta(
                        f"La nota {i} "
                        f"debe estar "
                        f"entre 0 y 5"
                    )

                    return None

                notas.append(nota)

            except ValueError:

                self.mostrar_alerta(
                    f"La nota {i} "
                    f"debe ser numerica"
                )

                return None

        return notas

    def calcular(self):

        notas = self.obtener_notas()

        if notas is None:
            return

        analisis = AnalisisNotas(
            notas
        )

        promedio = (
            analisis
            .calcular_promedio()
        )

        desviacion = (
            analisis
            .calcular_desviacion()
        )

        mayor = (
            analisis
            .obtener_mayor()
        )

        menor = (
            analisis
            .obtener_menor()
        )

        self.resultado.setText(
            f"Promedio: "
            f"{promedio:.2f}\n\n"

            f"Desviacion "
            f"estandar: "
            f"{desviacion:.2f}\n\n"

            f"Nota mayor: "
            f"{mayor}\n\n"

            f"Nota menor: "
            f"{menor}"
        )

    def limpiar(self):

        self.nota1.clear()
        self.nota2.clear()
        self.nota3.clear()
        self.nota4.clear()
        self.nota5.clear()

        self.resultado.setText("")

        self.nota1.setFocus()


app = QApplication(sys.argv)

ventana = Ventana()
ventana.show()

sys.exit(app.exec())