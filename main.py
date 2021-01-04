import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


def get_coffees():
    con = sqlite3.connect('coffee.sqlite')
    cur = con.cursor()

    res = cur.execute("SELECT * FROM Coffee").fetchall()

    cur.close()
    con.close()

    return res


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.initUI()

    def initUI(self):
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
                                              'Описание вкуса', 'Цена', 'Объем упаковки'])

        coffees = get_coffees()
        self.update_table(coffees)

    def update_table(self, coffees):
        self.table.setRowCount(0)

        for i, info in enumerate(coffees):
            self.table.setRowCount(self.table.rowCount() + 1)

            for j, elem in enumerate(info):
                item = QTableWidgetItem(str(elem))
                item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, j, item)

        self.table.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
