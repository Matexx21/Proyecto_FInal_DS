# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/xeland314/workspace/python/poker/ui/mesa.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mesa(object):
    def __init__(self) -> None:
        self.__resources_folder = os.path.join("resources", "cartas")
        self.__carta_reverso_path = os.path.join(self.__resources_folder, "Carta.png")
        self.__mesa_path = os.path.join(self.__resources_folder, "mesa.png")

    def setup_ui(self, Form):
        Form.setObjectName("Form")
        Form.resize(617, 499)
        Form.setMaximumSize(QtCore.QSize(625, 500))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.carta_8 = QtWidgets.QLabel(self.groupBox_2)
        self.carta_8.setMinimumSize(QtCore.QSize(80, 110))
        self.carta_8.setMaximumSize(QtCore.QSize(80, 110))
        self.carta_8.setText("")
        self.carta_8.setPixmap(QtGui.QPixmap(self.__carta_reverso_path))
        self.carta_8.setScaledContents(True)
        self.carta_8.setObjectName("carta_8")
        self.horizontalLayout_3.addWidget(self.carta_8)
        self.carta_7 = QtWidgets.QLabel(self.groupBox_2)
        self.carta_7.setMinimumSize(QtCore.QSize(80, 110))
        self.carta_7.setMaximumSize(QtCore.QSize(80, 110))
        self.carta_7.setText("")
        self.carta_7.setPixmap(QtGui.QPixmap(self.__carta_reverso_path))
        self.carta_7.setScaledContents(True)
        self.carta_7.setObjectName("carta_7")
        self.horizontalLayout_3.addWidget(self.carta_7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.retirarse_boton = QtWidgets.QPushButton(self.groupBox_2)
        self.retirarse_boton.setObjectName("retirarse_boton")
        self.verticalLayout.addWidget(self.retirarse_boton)
        self.pasar_boton = QtWidgets.QPushButton(self.groupBox_2)
        self.pasar_boton.setObjectName("pasar_boton")
        self.verticalLayout.addWidget(self.pasar_boton)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.apostar_boton = QtWidgets.QPushButton(self.groupBox_2)
        self.apostar_boton.setObjectName("apostar_boton")
        self.horizontalLayout_4.addWidget(self.apostar_boton)
        self.input_apuesta = QtWidgets.QSpinBox(self.groupBox_2)
        self.input_apuesta.setMinimum(1)
        self.input_apuesta.setMaximum(1000)
        self.input_apuesta.setObjectName("input_apuesta")
        self.horizontalLayout_4.addWidget(self.input_apuesta)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 2, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(525, 325))
        self.widget.setObjectName("widget")
        self.mesa = QtWidgets.QLabel(self.widget)
        self.mesa.setGeometry(QtCore.QRect(10, 10, 575, 305))
        self.mesa.setMinimumSize(QtCore.QSize(575, 305))
        self.mesa.setMaximumSize(QtCore.QSize(575, 305))
        self.mesa.setText("")
        self.mesa.setPixmap(QtGui.QPixmap(self.__mesa_path))
        self.mesa.setScaledContents(True)
        self.mesa.setObjectName("mesa")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(120, 170, 341, 112))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem)
        self.carta_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.carta_4.setMinimumSize(QtCore.QSize(80, 110))
        self.carta_4.setMaximumSize(QtCore.QSize(80, 110))
        self.carta_4.setText("")
        self.carta_4.setPixmap(QtGui.QPixmap(self.__carta_reverso_path))
        self.carta_4.setScaledContents(True)
        self.carta_4.setObjectName("carta_4")
        self.horizontalLayout_2.addWidget(self.carta_4)
        self.carta_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.carta_5.setMinimumSize(QtCore.QSize(80, 110))
        self.carta_5.setMaximumSize(QtCore.QSize(80, 110))
        self.carta_5.setText("")
        self.carta_5.setPixmap(QtGui.QPixmap(self.__carta_reverso_path))
        self.carta_5.setScaledContents(True)
        self.carta_5.setObjectName("carta_5")
        self.horizontalLayout_2.addWidget(self.carta_5)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 50, 341, 112))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem2)
        self.carta_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.carta_1.setMinimumSize(QtCore.QSize(80, 110))
        self.carta_1.setMaximumSize(QtCore.QSize(80, 110))
        self.carta_1.setText("")
        self.carta_1.setPixmap(QtGui.QPixmap(self.__carta_reverso_path))
        self.carta_1.setScaledContents(True)
        self.carta_1.setObjectName("carta_1")
        self.horizontalLayout.addWidget(self.carta_1)
        self.carta_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.carta_2.setMinimumSize(QtCore.QSize(80, 110))
        self.carta_2.setMaximumSize(QtCore.QSize(80, 110))
        self.carta_2.setText("")
        self.carta_2.setPixmap(QtGui.QPixmap(self.__carta_reverso_path))
        self.carta_2.setScaledContents(True)
        self.carta_2.setObjectName("carta_2")
        self.horizontalLayout.addWidget(self.carta_2)
        self.carta_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.carta_3.setMinimumSize(QtCore.QSize(80, 110))
        self.carta_3.setMaximumSize(QtCore.QSize(80, 110))
        self.carta_3.setText("")
        self.carta_3.setPixmap(QtGui.QPixmap(self.__carta_reverso_path))
        self.carta_3.setScaledContents(True)
        self.carta_3.setObjectName("carta_3")
        self.horizontalLayout.addWidget(self.carta_3)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dinero_actual = QtWidgets.QLabel(self.groupBox_2)
        self.dinero_actual.setObjectName("label_6")
        self.verticalLayout.addWidget(self.dinero_actual)
        self.ronda_label = QtWidgets.QLabel(self.groupBox_3)
        self.ronda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ronda_label.setObjectName("ronda_label")
        self.verticalLayout_3.addWidget(self.ronda_label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.mi_apuesta = QtWidgets.QLabel(self.groupBox_3)
        self.mi_apuesta.setText("")
        self.mi_apuesta.setObjectName("mi_apuesta")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mi_apuesta)
        self.apuesta_1 = QtWidgets.QLabel(self.groupBox_3)
        self.apuesta_1.setText("")
        self.apuesta_1.setObjectName("apuesta_1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.apuesta_1)
        self.apuesta_2 = QtWidgets.QLabel(self.groupBox_3)
        self.apuesta_2.setText("")
        self.apuesta_2.setObjectName("apuesta_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.apuesta_2)
        self.apuesta_3 = QtWidgets.QLabel(self.groupBox_3)
        self.apuesta_3.setText("")
        self.apuesta_3.setObjectName("apuesta_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.apuesta_3)
        self.verticalLayout_3.addLayout(self.formLayout)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_3.addItem(spacerItem4)
        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Texas Holdem"))
        self.retirarse_boton.setText(_translate("Form", "Retirarse"))
        self.pasar_boton.setText(_translate("Form", "Pasar"))
        self.apostar_boton.setText(_translate("Form", "Apostar"))
        self.ronda_label.setText(_translate("Form", "Ronda"))
        self.label_2.setText(_translate("Form", "Yo:"))
        self.label_3.setText(_translate("Form", "Jugador 1:"))
        self.label_4.setText(_translate("Form", "Jugador 2:"))
        self.label_5.setText(_translate("Form", "Jugador 3:"))
        self.dinero_actual.setText(_translate("Form", "Dinero: 1000"))
        self.label.setText(_translate("Form", "Apuestas"))
