import sys
import math
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


class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        if valor <= 0:
            raise ArithmeticError(
                "El valor debe ser un número positivo para calcular el logaritmo"
            )
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        if valor < 0:
            raise ArithmeticError(
                "El valor debe ser un número positivo para calcular la raíz cuadrada"
            )
        return math.sqrt(valor)


class VentanaCalculos(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cálculos Numéricos")
        self.resize(400, 300)

        self.lbl_valor = QLabel("Valor numérico:")
        self.txt_valor = QLineEdit()

        self.btn_calcular = QPushButton("Calcular")
        self.btn_limpiar = QPushButton("Limpiar")

        self.resultado = QTextEdit()
        self.resultado.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_valor)
        layout.addWidget(self.txt_valor)
        layout.addWidget(self.btn_calcular)
        layout.addWidget(self.btn_limpiar)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

        self.btn_calcular.clicked.connect(self.calcular)
        self.btn_limpiar.clicked.connect(self.limpiar)

    def calcular(self):
        self.resultado.clear()

        try:
            valor = float(self.txt_valor.text())

            logaritmo = CalculosNumericos.calcular_logaritmo_neperiano(valor)
            raiz = CalculosNumericos.calcular_raiz_cuadrada(valor)

            self.resultado.append(f"Logaritmo neperiano: {logaritmo}")
            self.resultado.append(f"Raíz cuadrada: {raiz}")

        except ValueError:
            QMessageBox.warning(
                self,
                "Error",
                "El valor debe ser numérico."
            )

        except ArithmeticError as e:
            QMessageBox.warning(
                self,
                "Error aritmético",
                str(e)
            )

    def limpiar(self):
        self.txt_valor.clear()
        self.resultado.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaCalculos()
    ventana.show()
    sys.exit(app.exec())