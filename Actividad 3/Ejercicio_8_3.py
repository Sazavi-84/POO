import sys
import math
import os
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QGridLayout,
    QLineEdit,
    QMessageBox
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class VentanaFigura(QWidget):
    def __init__(self, titulo):
        super().__init__()

        self.setWindowTitle(titulo)
        self.setGeometry(300, 200, 420, 550)

        self.setStyleSheet("""
            QWidget {
                background-color: #F5EFE6;
                font-family: Segoe UI;
                font-size: 14px;
                color: #5C4033;
            }

            QLabel {
                color: #4B3832;
                font-size: 16px;
                font-weight: bold;
            }

            QLineEdit {
                background-color: #FFF8F0;
                border: 2px solid #D6C6B8;
                border-radius: 15px;
                padding: 10px;
                font-size: 14px;
                color: #4B3832;
            }

            QLineEdit:focus {
                border: 2px solid #A67B5B;
                background-color: white;
            }

            QPushButton {
                background-color: #C8A27A;
                border: none;
                border-radius: 18px;
                padding: 12px;
                font-size: 15px;
                font-weight: bold;
                color: white;
            }

            QPushButton:hover {
                background-color: #B08968;
            }

            QPushButton:pressed {
                background-color: #8D6E63;
            }
        """)

        self.layout = QVBoxLayout()

        self.titulo = QLabel(titulo)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #6F4E37;
            margin-bottom: 10px;
        """)

        self.layout.addWidget(
            self.titulo,
            alignment=Qt.AlignCenter
        )

        imagenes = {
            "Cilindro": os.path.join(
                BASE_DIR,
                "img",
                "cilindro.png"
            ),

            "Esfera": os.path.join(
                BASE_DIR,
                "img",
                "esfera.png"
            ),

            "Pirámide": os.path.join(
                BASE_DIR,
                "img",
                "piramide.png"
            ),

            "Cubo": os.path.join(
                BASE_DIR,
                "img",
                "cubo.png"
            ),

            "Prisma": os.path.join(
                BASE_DIR,
                "img",
                "prisma.png"
            )
        }

        self.imagen = QLabel()
        self.imagen.setFixedSize(220, 220)
        self.imagen.setAlignment(Qt.AlignCenter)

        ruta = imagenes[titulo]
        pixmap = QPixmap(ruta)

        if pixmap.isNull():
            self.imagen.setText(
                "Imagen no encontrada"
            )
        else:
            pixmap = pixmap.scaled(
                180,
                180,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            self.imagen.setPixmap(
                pixmap
            )

        self.layout.addWidget(
            self.imagen,
            alignment=Qt.AlignCenter
        )

        self.campos = {}

        self.crear_campos(titulo)

        self.boton_calcular = QPushButton(
            "Calcular"
        )
        self.boton_calcular.setMinimumHeight(
            45
        )

        self.boton_calcular.clicked.connect(
            self.calcular
        )

        self.resultado = QLabel("")
        self.resultado.setAlignment(
            Qt.AlignCenter
        )

        self.resultado.setStyleSheet("""
            font-size: 16px;
            color: #5C4033;
            margin-top: 15px;
        """)

        self.layout.addWidget(
            self.boton_calcular
        )

        self.layout.addWidget(
            self.resultado,
            alignment=Qt.AlignCenter
        )

        self.setLayout(self.layout)

    def crear_input(self, texto):
        entrada = QLineEdit()

        entrada.setPlaceholderText(
            texto
        )

        entrada.setMinimumHeight(
            40
        )

        self.layout.addWidget(
            entrada
        )

        return entrada

    def crear_campos(self, figura):

        if figura == "Cilindro":
            self.campos["radio"] = (
                self.crear_input(
                    "Radio"
                )
            )

            self.campos["altura"] = (
                self.crear_input(
                    "Altura"
                )
            )

        elif figura == "Esfera":
            self.campos["radio"] = (
                self.crear_input(
                    "Radio"
                )
            )

        elif figura == "Pirámide":
            self.campos["lado"] = (
                self.crear_input(
                    "Lado de la base"
                )
            )

            self.campos["altura"] = (
                self.crear_input(
                    "Altura"
                )
            )

            self.campos["apotema"] = (
                self.crear_input(
                    "Apotema"
                )
            )

        elif figura == "Cubo":
            self.campos["lado"] = (
                self.crear_input(
                    "Lado"
                )
            )

        elif figura == "Prisma":
            self.campos["largo"] = (
                self.crear_input(
                    "Largo"
                )
            )

            self.campos["ancho"] = (
                self.crear_input(
                    "Ancho"
                )
            )

            self.campos["altura"] = (
                self.crear_input(
                    "Altura"
                )
            )

    def calcular(self):
        try:
            figura = self.windowTitle()

            if figura == "Cilindro":
                radio = float(
                    self.campos[
                        "radio"
                    ].text()
                )

                altura = float(
                    self.campos[
                        "altura"
                    ].text()
                )

                volumen = (
                    math.pi *
                    radio ** 2 *
                    altura
                )

                superficie = (
                    2 *
                    math.pi *
                    radio *
                    (radio + altura)
                )

            elif figura == "Esfera":
                radio = float(
                    self.campos[
                        "radio"
                    ].text()
                )

                volumen = (
                    (4 / 3) *
                    math.pi *
                    radio ** 3
                )

                superficie = (
                    4 *
                    math.pi *
                    radio ** 2
                )

            elif figura == "Pirámide":
                lado = float(
                    self.campos[
                        "lado"
                    ].text()
                )

                altura = float(
                    self.campos[
                        "altura"
                    ].text()
                )

                apotema = float(
                    self.campos[
                        "apotema"
                    ].text()
                )

                volumen = (
                    lado ** 2 *
                    altura
                ) / 3

                superficie = (
                    lado ** 2 +
                    (2 *
                     lado *
                     apotema)
                )

            elif figura == "Cubo":
                lado = float(
                    self.campos[
                        "lado"
                    ].text()
                )

                volumen = (
                    lado ** 3
                )

                superficie = (
                    6 *
                    lado ** 2
                )

            elif figura == "Prisma":
                largo = float(
                    self.campos[
                        "largo"
                    ].text()
                )

                ancho = float(
                    self.campos[
                        "ancho"
                    ].text()
                )

                altura = float(
                    self.campos[
                        "altura"
                    ].text()
                )

                volumen = (
                    largo *
                    ancho *
                    altura
                )

                superficie = 2 * (
                    (largo * ancho) +
                    (largo * altura) +
                    (ancho * altura)
                )

            self.resultado.setText(
                f"Volumen: {volumen:.2f}\n"
                f"Superficie: {superficie:.2f}"
            )

        except ValueError:
            QMessageBox.warning(
                self,
                "Error",
                "Ingrese valores numéricos válidos"
            )


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Figuras Geométricas"
        )

        self.setGeometry(
            200,
            100,
            500,
            350
        )

        self.setStyleSheet("""
            QWidget {
                background-color: #F5EFE6;
                font-family: Segoe UI;
                color: #5C4033;
            }

            QPushButton {
                background-color: #C8A27A;
                border: none;
                border-radius: 20px;
                padding: 15px;
                font-size: 15px;
                font-weight: bold;
                color: white;
            }

            QPushButton:hover {
                background-color: #B08968;
            }

            QPushButton:pressed {
                background-color: #8D6E63;
            }
        """)

        self.ventanas = []

        layout = QVBoxLayout()

        titulo = QLabel(
            "Figuras Geométricas"
        )

        titulo.setAlignment(
            Qt.AlignCenter
        )

        titulo.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: #6F4E37;
            margin-bottom: 20px;
        """)

        subtitulo = QLabel(
            "Selecciona una figura"
        )

        subtitulo.setAlignment(
            Qt.AlignCenter
        )

        subtitulo.setStyleSheet("""
            font-size: 15px;
            color: #8B6F5A;
            margin-bottom: 15px;
        """)

        layout.addWidget(
            titulo
        )

        layout.addWidget(
            subtitulo
        )

        grid = QGridLayout()
        grid.setSpacing(15)

        figuras = [
            "Cilindro",
            "Esfera",
            "Pirámide",
            "Cubo",
            "Prisma"
        ]

        posiciones = [
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 1),
            (2, 0)
        ]

        for figura, (
            fila,
            columna
        ) in zip(
            figuras,
            posiciones
        ):

            boton = QPushButton(
                figura
            )

            boton.setMinimumHeight(
                55
            )

            boton.clicked.connect(
                lambda checked,
                f=figura:
                self.abrir_ventana(f)
            )

            grid.addWidget(
                boton,
                fila,
                columna
            )

        layout.addLayout(
            grid
        )

        self.setLayout(
            layout
        )

    def abrir_ventana(
        self,
        figura
    ):
        ventana = (
            VentanaFigura(
                figura
            )
        )

        self.ventanas.append(
            ventana
        )

        ventana.show()


app = QApplication(sys.argv)

ventana = VentanaPrincipal()
ventana.show()

sys.exit(app.exec())