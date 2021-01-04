# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QStatusBar {\n"
                                 "    color: #c96174;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.changeBtn = QtWidgets.QPushButton(self.widget)
        self.changeBtn.setObjectName("changeBtn")
        self.gridLayout.addWidget(self.changeBtn, 1, 0, 1, 1)
        self.addBtn = QtWidgets.QPushButton(self.widget)
        self.addBtn.setObjectName("addBtn")
        self.gridLayout.addWidget(self.addBtn, 1, 1, 1, 1)
        self.coffeeTable = QtWidgets.QTableWidget(self.widget)
        self.coffeeTable.setObjectName("coffeeTable")
        self.coffeeTable.setColumnCount(0)
        self.coffeeTable.setRowCount(0)
        self.gridLayout.addWidget(self.coffeeTable, 0, 0, 1, 2)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кофе"))
        self.changeBtn.setText(_translate("MainWindow", "Изменить"))
        self.addBtn.setText(_translate("MainWindow", "Добавить"))
