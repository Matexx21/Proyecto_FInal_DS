from PyQt5 import QtCore, QtGui

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QSpacerItem,
    QSizePolicy,
)

class Ui_MainWindow(object):

    def __init__(self) -> None:
        self.main_window = QMainWindow()
        self.centralwidget = QWidget(self.main_window)
        self.grid_layout = QGridLayout(self.centralwidget)
        self.title = QLabel(self.centralwidget)
        self.vertical_layout_1 = QVBoxLayout()
        self.vertical_layout_2 = QVBoxLayout()
        self.vertical_layout_3 = QVBoxLayout()
        self.vertical_layout_4 = QVBoxLayout()
        self.imagen_carta_1 = QLabel(self.centralwidget)
        self.imagen_carta_2 = QLabel(self.centralwidget)
        self.imagen_carta_3 = QLabel(self.centralwidget)
        self.imagen_carta_4 = QLabel(self.centralwidget)
        self.iniciar_boton = QPushButton(self.centralwidget)
        self.creditos_boton = QPushButton(self.centralwidget)

    def setup_ui(self):
        self.main_window.setObjectName("MainWindow")
        self.main_window.resize(700, 500)
        self.centralwidget.setObjectName("centralwidget")
        self.grid_layout.setObjectName("gridLayout")
        self.vertical_layout_3.setObjectName("verticalLayout_3")
        self.imagen_carta_2.setMinimumSize(QtCore.QSize(130, 170))
        self.imagen_carta_2.setMaximumSize(QtCore.QSize(130, 170))
        self.imagen_carta_2.setText("")
        self.imagen_carta_2.setPixmap(QtGui.QPixmap("resources/cartas/Seis de Treboles.png"))
        self.imagen_carta_2.setScaledContents(True)
        self.imagen_carta_2.setObjectName("label_3")
        self.vertical_layout_3.addWidget(self.imagen_carta_2)
        spacer_item = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )
        self.vertical_layout_3.addItem(spacer_item)
        self.imagen_carta_3.setMinimumSize(QtCore.QSize(130, 170))
        self.imagen_carta_3.setMaximumSize(QtCore.QSize(130, 170))
        self.imagen_carta_3.setText("")
        self.imagen_carta_3.setPixmap(QtGui.QPixmap("resources/cartas/Rey de Diamantes.png"))
        self.imagen_carta_3.setScaledContents(True)
        self.imagen_carta_3.setObjectName("label_4")
        self.vertical_layout_3.addWidget(self.imagen_carta_3)
        self.grid_layout.addLayout(self.vertical_layout_3, 0, 4, 1, 1)
        self.vertical_layout_2.setObjectName("verticalLayout_2")
        self.imagen_carta_1.setMinimumSize(QtCore.QSize(130, 170))
        self.imagen_carta_1.setMaximumSize(QtCore.QSize(130, 170))
        self.imagen_carta_1.setText("")
        self.imagen_carta_1.setPixmap(QtGui.QPixmap("resources/cartas/As de Corazones.png"))
        self.imagen_carta_1.setScaledContents(True)
        self.imagen_carta_1.setObjectName("label_2")
        self.vertical_layout_2.addWidget(self.imagen_carta_1)
        spacer_item_1 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )
        self.vertical_layout_2.addItem(spacer_item_1)
        self.imagen_carta_4.setMinimumSize(QtCore.QSize(130, 170))
        self.imagen_carta_4.setMaximumSize(QtCore.QSize(130, 170))
        self.imagen_carta_4.setText("")
        self.imagen_carta_4.setPixmap(QtGui.QPixmap("resources/cartas/Tres de Picas.png"))
        self.imagen_carta_4.setScaledContents(True)
        self.imagen_carta_4.setObjectName("label_5")
        self.vertical_layout_2.addWidget(self.imagen_carta_4)
        self.grid_layout.addLayout(self.vertical_layout_2, 0, 0, 1, 1)
        self.vertical_layout_4.setObjectName("verticalLayout_4")
        spacer_item_2 = QSpacerItem(
            20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred
        )
        self.vertical_layout_4.addItem(spacer_item_2)
        self.title.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("label")
        self.vertical_layout_4.addWidget(self.title)
        self.vertical_layout_1.setObjectName("verticalLayout")
        self.iniciar_boton.setMinimumSize(QtCore.QSize(0, 50))
        self.iniciar_boton.setObjectName("iniciar_boton")
        self.vertical_layout_1.addWidget(self.iniciar_boton)
        self.creditos_boton.setMinimumSize(QtCore.QSize(0, 50))
        self.creditos_boton.setObjectName("creditos_boton")
        self.vertical_layout_1.addWidget(self.creditos_boton)
        spacer_item_3 = QSpacerItem(
            20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding
        )
        self.vertical_layout_1.addItem(spacer_item_3)
        self.vertical_layout_4.addLayout(self.vertical_layout_1)
        self.grid_layout.addLayout(self.vertical_layout_4, 0, 2, 1, 1)
        spacer_item_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )
        self.grid_layout.addItem(spacer_item_4, 0, 1, 1, 1)
        spacer_item_5 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )
        self.grid_layout.addItem(spacer_item_5, 0, 3, 1, 1)
        self.main_window.setCentralWidget(self.centralwidget)
        self.retranslate_ui()

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.main_window.setWindowTitle(_translate("MainWindow", "Texas Hold'em"))
        self.title.setText(_translate("MainWindow", "Texas Hold'em"))
        self.iniciar_boton.setText(_translate("MainWindow", "Iniciar Juego"))
        self.creditos_boton.setText(_translate("MainWindow", "Créditos"))

    def show(self):
        self.main_window.show()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setup_ui()
    ui.show()
    sys.exit(app.exec_())
