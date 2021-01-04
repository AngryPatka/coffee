# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 300)
        MainWindow.setStyleSheet("QStatusBar {\n"
                                 "    color: #c96174;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.price = QtWidgets.QSpinBox(self.widget)
        self.price.setMinimum(1)
        self.price.setMaximum(1000000)
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.sortName = QtWidgets.QLineEdit(self.widget)
        self.sortName.setObjectName("sortName")
        self.gridLayout.addWidget(self.sortName, 0, 1, 1, 1)
        self.inGrainsOrGround = QtWidgets.QComboBox(self.widget)
        self.inGrainsOrGround.setObjectName("inGrainsOrGround")
        self.inGrainsOrGround.addItem("")
        self.inGrainsOrGround.addItem("")
        self.gridLayout.addWidget(self.inGrainsOrGround, 2, 1, 1, 1)
        self.flavorDescription = QtWidgets.QLineEdit(self.widget)
        self.flavorDescription.setObjectName("flavorDescription")
        self.gridLayout.addWidget(self.flavorDescription, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.volume = QtWidgets.QSpinBox(self.widget)
        self.volume.setMinimum(1)
        self.volume.setMaximum(1000000)
        self.volume.setObjectName("volume")
        self.gridLayout.addWidget(self.volume, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.degreeOfRoast = QtWidgets.QLineEdit(self.widget)
        self.degreeOfRoast.setObjectName("degreeOfRoast")
        self.gridLayout.addWidget(self.degreeOfRoast, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy)
        self.button.setText("")
        self.button.setObjectName("button")
        self.gridLayout.addWidget(self.button, 6, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Объем упаковки"))
        self.inGrainsOrGround.setItemText(0, _translate("MainWindow", "Молотый"))
        self.inGrainsOrGround.setItemText(1, _translate("MainWindow", "В зёрнах"))
        self.label.setText(_translate("MainWindow", "Название сорта"))
        self.label_4.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_5.setText(_translate("MainWindow", "Цена"))
        self.label_2.setText(_translate("MainWindow", "Степень обжарки"))
        self.label_3.setText(_translate("MainWindow", "Молотый/в зёрнах"))
