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


class PruebaExcepciones:


    def division(self, numerador, denominador):
        salida = ""

        try:
            salida += "Ingresando al primer try\n"

            numerador = float(numerador)
            denominador = float(denominador)

            resultado = numerador / denominador

            salida += f"Resultado de la división: {resultado}\n"

        except ZeroDivisionError:
            salida += "Error: División por cero\n"

        except ValueError:
            salida += "Error: Debe ingresar valores numéricos\n"

        finally:
            salida += "Ingresando al primer finally\n"

        return salida

    def objeto_nulo(self):
        salida = ""

        try:
            salida += "\nIngresando al segundo try\n"

            objeto = None
            objeto.upper() 

            salida += "Imprimiendo objeto\n"

        except ArithmeticError:
            salida += "Error aritmético\n"

        except Exception:
            salida += "Ocurrió una excepción\n"

        finally:
            salida += "Ingresando al segundo finally\n"

        return salida


class VentanaPrincipal(QWidget):

    def __init__(self):
        super().__init__()

        self.prueba = PruebaExcepciones()

        self.setWindowTitle("Ejercicio 6.4 - Excepciones")
        self.resize(500, 400)

        self.lbl_num = QLabel("Numerador:")
        self.lbl_den = QLabel("Denominador:")


        self.txt_num = QLineEdit()
        self.txt_den = QLineEdit()

        self.btn_ejecutar = QPushButton("Ejecutar")
        self.btn_limpiar = QPushButton("Limpiar")

  
        self.txt_resultado = QTextEdit()
        self.txt_resultado.setReadOnly(True)

      
        self.btn_ejecutar.clicked.connect(self.ejecutar)
        self.btn_limpiar.clicked.connect(self.limpiar)

       
        layout = QVBoxLayout()

        layout.addWidget(self.lbl_num)
        layout.addWidget(self.txt_num)

        layout.addWidget(self.lbl_den)
        layout.addWidget(self.txt_den)

        layout.addWidget(self.btn_ejecutar)
        layout.addWidget(self.btn_limpiar)

        layout.addWidget(self.txt_resultado)

        self.setLayout(layout)

    def ejecutar(self):
        numerador = self.txt_num.text()
        denominador = self.txt_den.text()

        if numerador == "" or denominador == "":
            QMessageBox.warning(
                self,
                "Advertencia",
                "Debe ingresar el numerador y el denominador."
            )
            return

        salida = ""

        salida += self.prueba.division(
            numerador,
            denominador
        )

        salida += self.prueba.objeto_nulo()

        self.txt_resultado.setText(salida)

    def limpiar(self):
        self.txt_num.clear()
        self.txt_den.clear()
        self.txt_resultado.clear()

        self.txt_num.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())