import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QTextEdit,
    QFileDialog,
    QVBoxLayout,
    QMessageBox
)


class LeerArchivo:
    def leer(self, ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()


class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.lector = LeerArchivo()

        self.setWindowTitle("Lectura de Archivos")
        self.resize(700, 500)

        self.lbl_archivo = QLabel("No se ha seleccionado ningún archivo")

        self.btn_seleccionar = QPushButton("Seleccionar Archivo")
        self.btn_leer = QPushButton("Leer Archivo")
        self.btn_limpiar = QPushButton("Limpiar")

        self.txt_contenido = QTextEdit()
        self.txt_contenido.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_archivo)
        layout.addWidget(self.btn_seleccionar)
        layout.addWidget(self.btn_leer)
        layout.addWidget(self.btn_limpiar)
        layout.addWidget(self.txt_contenido)

        self.setLayout(layout)

        self.ruta_archivo = ""

        self.btn_seleccionar.clicked.connect(self.seleccionar_archivo)
        self.btn_leer.clicked.connect(self.leer_archivo)
        self.btn_limpiar.clicked.connect(self.limpiar)

    def seleccionar_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo",
            "",
            "Archivos de texto (*.txt);;Todos los archivos (*)"
        )

        if ruta:
            self.ruta_archivo = ruta
            self.lbl_archivo.setText(f"Archivo: {ruta}")

    def leer_archivo(self):
        if not self.ruta_archivo:
            QMessageBox.warning(
                self,
                "Advertencia",
                "Debe seleccionar un archivo."
            )
            return

        try:
            contenido = self.lector.leer(self.ruta_archivo)
            self.txt_contenido.setPlainText(contenido)

        except Exception:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo leer el archivo."
            )

    def limpiar(self):
        self.lbl_archivo.setText("No se ha seleccionado ningún archivo")
        self.txt_contenido.clear()
        self.ruta_archivo = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = Ventana()
    ventana.show()

    sys.exit(app.exec())