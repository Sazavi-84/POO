import sys
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QTextEdit, QVBoxLayout, QHBoxLayout, QMessageBox,
    QTableWidget, QTableWidgetItem, QHeaderView
)
from PySide6.QtCore import Qt


class AgendaTelefonica:
    def __init__(self, archivo="agenda.txt"):
        self.archivo = archivo

        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", encoding="utf-8") as f:
                pass

    def leer_contactos(self):
        contactos = {}

        with open(self.archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    partes = linea.split(",", 1)
                    if len(partes) == 2:
                        nombre = partes[0].strip()
                        telefono = partes[1].strip()
                        contactos[nombre] = telefono

        return contactos

    def guardar_contactos(self, contactos):
        with open(self.archivo, "w", encoding="utf-8") as f:
            for nombre, telefono in sorted(contactos.items(), key=lambda x: x[0].lower()):
                f.write(f"{nombre},{telefono}\n")

    def buscar_nombre_real(self, nombre_buscar):
        contactos = self.leer_contactos()
        for nombre in contactos:
            if nombre.lower() == nombre_buscar.lower():
                return nombre
        return None

    def crear_contacto(self, nombre, telefono):
        contactos = self.leer_contactos()

        nombre_existente = self.buscar_nombre_real(nombre)
        if nombre_existente is not None:
            return False, "Ya existe un contacto con ese nombre."

        contactos[nombre] = telefono
        self.guardar_contactos(contactos)
        return True, "Contacto creado correctamente."

    def actualizar_contacto(self, nombre, nuevo_telefono):
        contactos = self.leer_contactos()

        nombre_real = self.buscar_nombre_real(nombre)
        if nombre_real is None:
            return False, "El contacto no existe."

        contactos[nombre_real] = nuevo_telefono
        self.guardar_contactos(contactos)
        return True, "Contacto actualizado correctamente."

    def eliminar_contacto(self, nombre):
        contactos = self.leer_contactos()

        nombre_real = self.buscar_nombre_real(nombre)
        if nombre_real is None:
            return False, "El contacto no existe."

        del contactos[nombre_real]
        self.guardar_contactos(contactos)
        return True, "Contacto eliminado correctamente."

    def buscar_contacto(self, nombre_buscar):
        contactos = self.leer_contactos()

        for nombre, telefono in contactos.items():
            if nombre.lower() == nombre_buscar.lower():
                return nombre, telefono

        return None

    def obtener_contactos_ordenados(self):
        contactos = self.leer_contactos()
        return sorted(contactos.items(), key=lambda x: x[0].lower())

    def obtener_contactos_texto(self):
        contactos = self.leer_contactos()

        if not contactos:
            return "No hay contactos guardados."

        texto = "AGENDA TELEFÓNICA\n"
        texto += "=" * 40 + "\n"
        for nombre, telefono in sorted(contactos.items(), key=lambda x: x[0].lower()):
            texto += f"Nombre: {nombre}\nTeléfono: {telefono}\n"
            texto += "-" * 40 + "\n"

        return texto

    def limpiar_agenda(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            pass
        return True, "La agenda fue limpiada correctamente."


class VentanaAgenda(QWidget):
    def __init__(self):
        super().__init__()

        self.agenda = AgendaTelefonica("agenda.txt")
        self.setWindowTitle("Agenda Telefónica")
        self.setGeometry(150, 100, 1000, 600)

        self.inicializar_ui()
        self.aplicar_estilo()
        self.cargar_tabla_contactos()

    def inicializar_ui(self):
        # Etiquetas
        self.lbl_titulo = QLabel("AGENDA TELEFÓNICA")
        self.lbl_titulo.setAlignment(Qt.AlignCenter)

        self.lbl_nombre = QLabel("Nombre:")
        self.lbl_telefono = QLabel("Teléfono:")
        self.lbl_buscar = QLabel("Buscar:")

        self.txt_nombre = QLineEdit()
        self.txt_telefono = QLineEdit()
        self.txt_buscar = QLineEdit()

        
        self.btn_crear = QPushButton("Crear")
        self.btn_actualizar = QPushButton("Actualizar")
        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_ver = QPushButton("Ver contactos")
        self.btn_limpiar = QPushButton("Limpiar agenda")
        self.btn_borrar_campos = QPushButton("Limpiar campos")
        self.btn_buscar = QPushButton("Buscar")

        self.tabla_contactos = QTableWidget()
        self.tabla_contactos.setColumnCount(2)
        self.tabla_contactos.setHorizontalHeaderLabels(["Nombre", "Teléfono"])
        self.tabla_contactos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_contactos.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabla_contactos.setEditTriggers(QTableWidget.NoEditTriggers)

        
        self.area_texto = QTextEdit()
        self.area_texto.setReadOnly(True)

        
        layout_izquierdo = QVBoxLayout()

        fila_nombre = QHBoxLayout()
        fila_nombre.addWidget(self.lbl_nombre)
        fila_nombre.addWidget(self.txt_nombre)

        fila_telefono = QHBoxLayout()
        fila_telefono.addWidget(self.lbl_telefono)
        fila_telefono.addWidget(self.txt_telefono)

        fila_buscar = QHBoxLayout()
        fila_buscar.addWidget(self.lbl_buscar)
        fila_buscar.addWidget(self.txt_buscar)
        fila_buscar.addWidget(self.btn_buscar)

        fila_botones1 = QHBoxLayout()
        fila_botones1.addWidget(self.btn_crear)
        fila_botones1.addWidget(self.btn_actualizar)
        fila_botones1.addWidget(self.btn_eliminar)

        fila_botones2 = QHBoxLayout()
        fila_botones2.addWidget(self.btn_ver)
        fila_botones2.addWidget(self.btn_limpiar)
        fila_botones2.addWidget(self.btn_borrar_campos)

        layout_izquierdo.addWidget(self.lbl_titulo)
        layout_izquierdo.addLayout(fila_nombre)
        layout_izquierdo.addLayout(fila_telefono)
        layout_izquierdo.addLayout(fila_buscar)
        layout_izquierdo.addLayout(fila_botones1)
        layout_izquierdo.addLayout(fila_botones2)
        layout_izquierdo.addWidget(QLabel("Notas / información"))
        layout_izquierdo.addWidget(self.area_texto)

        
        layout_derecho = QVBoxLayout()
        layout_derecho.addWidget(QLabel("Contactos guardados"))
        layout_derecho.addWidget(self.tabla_contactos)

       
        layout_principal = QHBoxLayout()
        layout_principal.addLayout(layout_izquierdo, 2)
        layout_principal.addLayout(layout_derecho, 2)

        self.setLayout(layout_principal)

       
        self.btn_crear.clicked.connect(self.crear_contacto)
        self.btn_actualizar.clicked.connect(self.actualizar_contacto)
        self.btn_eliminar.clicked.connect(self.eliminar_contacto)
        self.btn_ver.clicked.connect(self.ver_contactos)
        self.btn_limpiar.clicked.connect(self.limpiar_agenda)
        self.btn_borrar_campos.clicked.connect(self.limpiar_campos)
        self.btn_buscar.clicked.connect(self.buscar_contacto)
        self.tabla_contactos.cellClicked.connect(self.seleccionar_contacto)

    def aplicar_estilo(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f5ecd7;
                color: #3e2f1c;
                font-family: 'Georgia';
                font-size: 14px;
            }

            QLabel {
                font-weight: bold;
                color: #4a3520;
            }

            QLabel#titulo {
                font-size: 26px;
                font-weight: bold;
            }

            QLineEdit {
                background-color: #fffaf0;
                border: 2px solid #8b6f47;
                border-radius: 8px;
                padding: 6px;
                color: #3e2f1c;
                selection-background-color: #b08d57;
            }

            QTextEdit {
                background-color: #fffaf0;
                border: 2px solid #8b6f47;
                border-radius: 10px;
                padding: 8px;
                font-family: 'Courier New';
                font-size: 13px;
                color: #3b2c1b;
            }

            QPushButton {
                background-color: #8b6f47;
                color: #fff8e7;
                border: 2px solid #5f4728;
                border-radius: 10px;
                padding: 8px 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #a27c4f;
            }

            QPushButton:pressed {
                background-color: #6e5435;
            }

            QTableWidget {
                background-color: #fffaf0;
                border: 2px solid #8b6f47;
                gridline-color: #bfa37a;
                color: #3e2f1c;
                font-size: 13px;
                selection-background-color: #d9c3a3;
                selection-color: #2d1f12;
            }

            QHeaderView::section {
                background-color: #8b6f47;
                color: #fff8e7;
                padding: 6px;
                border: 1px solid #5f4728;
                font-weight: bold;
            }

            QMessageBox {
                background-color: #f5ecd7;
            }
        """)

        
        self.lbl_titulo.setObjectName("titulo")

    def validar_telefono(self, telefono):
        return telefono.isdigit() 

    def crear_contacto(self):
        nombre = self.txt_nombre.text().strip()
        telefono = self.txt_telefono.text().strip()

        if not nombre or not telefono:
            QMessageBox.warning(self, "Error", "Debes ingresar nombre y teléfono.")
            return

        if not self.validar_telefono(telefono):
            QMessageBox.warning(
                self,
                "Error",
                "El teléfono debe contener exactamente 10 dígitos numéricos."
            )
            return

        exito, mensaje = self.agenda.crear_contacto(nombre, telefono)

        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.ver_contactos()
            self.cargar_tabla_contactos()
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Aviso", mensaje)

    def actualizar_contacto(self):
        nombre = self.txt_nombre.text().strip()
        telefono = self.txt_telefono.text().strip()

        if not nombre or not telefono:
            QMessageBox.warning(self, "Error", "Debes ingresar nombre y teléfono.")
            return

        if not self.validar_telefono(telefono):
            QMessageBox.warning(
                self,
                "Error",
                "El teléfono debe contener exactamente 10 dígitos numéricos."
            )
            return

        exito, mensaje = self.agenda.actualizar_contacto(nombre, telefono)

        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.ver_contactos()
            self.cargar_tabla_contactos()
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Aviso", mensaje)

    def eliminar_contacto(self):
        nombre = self.txt_nombre.text().strip()

        if not nombre:
            QMessageBox.warning(self, "Error", "Debes ingresar o seleccionar un contacto.")
            return

        exito, mensaje = self.agenda.eliminar_contacto(nombre)

        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.ver_contactos()
            self.cargar_tabla_contactos()
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Aviso", mensaje)

    def buscar_contacto(self):
        nombre_buscar = self.txt_buscar.text().strip()

        if not nombre_buscar:
            QMessageBox.warning(self, "Error", "Ingresa un nombre para buscar.")
            return

        resultado = self.agenda.buscar_contacto(nombre_buscar)

        if resultado:
            nombre, telefono = resultado
            self.txt_nombre.setText(nombre)
            self.txt_telefono.setText(telefono)
            self.area_texto.setPlainText(
                f"Contacto encontrado:\n\nNombre: {nombre}\nTeléfono: {telefono}"
            )
        else:
            self.area_texto.setPlainText("No se encontró el contacto.")
            QMessageBox.information(self, "Buscar", "No se encontró el contacto.")

    def seleccionar_contacto(self, fila, columna):
        nombre_item = self.tabla_contactos.item(fila, 0)
        telefono_item = self.tabla_contactos.item(fila, 1)

        if nombre_item and telefono_item:
            nombre = nombre_item.text()
            telefono = telefono_item.text()

            self.txt_nombre.setText(nombre)
            self.txt_telefono.setText(telefono)

            self.area_texto.setPlainText(
                f"Contacto seleccionado:\n\nNombre: {nombre}\nTeléfono: {telefono}"
            )

    def cargar_tabla_contactos(self):
        contactos = self.agenda.obtener_contactos_ordenados()
        self.tabla_contactos.setRowCount(len(contactos))

        for fila, (nombre, telefono) in enumerate(contactos):
            self.tabla_contactos.setItem(fila, 0, QTableWidgetItem(nombre))
            self.tabla_contactos.setItem(fila, 1, QTableWidgetItem(telefono))

    def ver_contactos(self):
        texto = self.agenda.obtener_contactos_texto()
        self.area_texto.setPlainText(texto)

    def limpiar_agenda(self):
        respuesta = QMessageBox.question(
            self,
            "Confirmar",
            "¿Seguro que deseas borrar toda la agenda?",
            QMessageBox.Yes | QMessageBox.No
        )

        if respuesta == QMessageBox.Yes:
            exito, mensaje = self.agenda.limpiar_agenda()
            if exito:
                QMessageBox.information(self, "Éxito", mensaje)
                self.ver_contactos()
                self.cargar_tabla_contactos()
                self.limpiar_campos()

    def limpiar_campos(self):
        self.txt_nombre.clear()
        self.txt_telefono.clear()
        self.txt_buscar.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaAgenda()
    ventana.show()
    sys.exit(app.exec())