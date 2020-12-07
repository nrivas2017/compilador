import gramatica as g
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from mydesign import Ui_MainWindow
import sys

class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.b_lexico.clicked.connect(self.ev_lexico)
        self.ui.b_sintactico.clicked.connect(self.ev_sintactico)
        self.ui.b_cargar.clicked.connect(self.ev_cargar)
        self.ui.b_limpiar.clicked.connect(self.ev_limpiar)
        self.ui.b_limpiar_sintactico.clicked.connect(self.ev_limpiar_sintactico)
        self.ui.b_limpiar_lexico.clicked.connect(self.ev_limpiar_lexico)
    def ev_lexico(self):
        self.ui.text_lexico.setText('')
        datos = self.ui.text_codigo.toPlainText().strip()
        resultado_lexico = g.prueba(datos)
        cadena= ''
        for lex in resultado_lexico:
            cadena += lex + "\n"
        self.ui.text_lexico.setText(cadena)
        self.ui.b_lexico.setEnabled(False)
    def ev_sintactico(self):
        self.ui.text_sintactico.setText('')
        datos = self.ui.text_codigo.toPlainText().strip()
        resultado_sintactico = g.prueba_sintactica(datos)
        cadena = ''
        for item in resultado_sintactico:
            cadena += item + "\n"
        self.ui.text_sintactico.setText( cadena )
        self.ui.b_sintactico.setEnabled(False)
    def ev_cargar(self):
        dlg = QFileDialog()
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')
            with f:
                data = f.read().strip()
                if data:
                    self.ui.text_codigo.setText(data+"\n")
    def ev_limpiar(self):
        self.ui.text_codigo.setText('')
        self.ui.text_lexico.setText('')
        self.ui.text_sintactico.setText('')
        self.ui.b_lexico.setEnabled(True)
        self.ui.b_sintactico.setEnabled(True)
    def ev_limpiar_lexico(self):
        self.ui.text_lexico.setText('')
        g.resultado_lexema.clear()
        self.ui.b_lexico.setEnabled(True)
    def ev_limpiar_sintactico(self):
        self.ui.text_sintactico.setText('')
        g.resultado_gramatica.clear()
        self.ui.b_sintactico.setEnabled(True)
def window():
    app = QApplication(sys.argv)
    win = mywindow()
    win.show()
    sys.exit(app.exec())
window()