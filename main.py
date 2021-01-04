import sys
import sqlite3

from main_ui import Ui_MainWindow as MainUi
from add_edit_coffee_form_ui import Ui_MainWindow as AddEditCoffeeForm

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class AddEditCoffeeWindow(QMainWindow, AddEditCoffeeForm):
    def __init__(self, main_window, coffee_info=None):
        super().__init__()
        self.setupUi(self)

        self.main_window = main_window
        self.coffee_info = coffee_info

        self.initUI()

    def initUI(self):
        if not self.coffee_info:  # форма открылась для добавления
            self.setWindowTitle('Добавить кофе')

            self.button.setText('Добавить')

            self.add = True
        else:  # форма открылась для редактирования
            self.setWindowTitle('Изменить кофе')

            self.sortName.setText(self.coffee_info[1])
            self.degreeOfRoast.setText(self.coffee_info[2])
            self.inGrainsOrGround.setCurrentIndex(['Молотый', 'В зёрнах'].index(self.coffee_info[3]))
            self.flavorDescription.setText(self.coffee_info[4])
            self.price.setValue(int(self.coffee_info[5]))
            self.volume.setValue(int(self.coffee_info[6]))

            self.button.setText('Изменить')

            self.add = False

        self.button.clicked.connect(self.add_or_edit)

    def add_or_edit(self):
        self.statusbar.showMessage('')
        sort_name = self.sortName.text()
        degree_of_roast = self.degreeOfRoast.text()
        in_grains_or_ground = self.inGrainsOrGround.currentText()
        fl_description = self.flavorDescription.text()
        price = self.price.value()
        volume = self.volume.value()

        if sort_name and degree_of_roast and in_grains_or_ground and fl_description and price and volume:
            if self.add:
                req = f"""
                INSERT INTO Coffee(SortName, DegreeOfRoast, InGrainsOrGround, FlavorDescription, Price, Volume)
                VALUES('{sort_name}', '{degree_of_roast}', '{in_grains_or_ground}', '{fl_description}', {price}, {volume})
                """
            else:
                req = f"""
                UPDATE Coffee
                SET SortName = '{sort_name}', DegreeOfRoast = '{degree_of_roast}',
                    InGrainsOrGround = '{in_grains_or_ground}', FlavorDescription = '{fl_description}',
                    Price = {price}, Volume = {volume}
                WHERE Id = {self.coffee_info[0]}
                """
            self.main_window.execute_query(req, False)
            self.main_window.show_table()

            self.close()
        else:
            self.statusbar.showMessage('Заполнены не все поля.')


class Window(QMainWindow, MainUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.initUI()

    def initUI(self):
        self.coffeeTable.setColumnCount(7)
        self.coffeeTable.setHorizontalHeaderLabels(['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
                                                    'Описание вкуса', 'Цена', 'Объем упаковки'])

        self.changeBtn.clicked.connect(self.change_coffee)
        self.addBtn.clicked.connect(self.add_coffee)

        self.show_table()

    def execute_query(self, query: str, get_result: bool):
        """Выполняет запрос

        :param query: SQL-запрос
        :param get_result: True - получение информации из БД, False - изменение БД
        """

        con = sqlite3.connect('data/coffee.sqlite')
        cur = con.cursor()

        if get_result:
            res = cur.execute(query).fetchall()
            cur.close()
            con.close()
            return res

        cur.execute(query)

        con.commit()
        cur.close()
        con.close()

    def show_table(self):
        req = "SELECT * FROM Coffee"
        coffees = self.execute_query(req, True)
        self.coffeeTable.setRowCount(0)

        for i, info in enumerate(coffees):
            self.coffeeTable.setRowCount(self.coffeeTable.rowCount() + 1)

            for j, elem in enumerate(info):
                item = QTableWidgetItem(str(elem))
                self.coffeeTable.setItem(i, j, item)

        self.coffeeTable.resizeColumnsToContents()

    def change_coffee(self):
        self.statusbar.showMessage('')

        table = self.coffeeTable
        rows = list(set(item.row() for item in table.selectedItems()))

        if not len(rows):
            self.statusbar.showMessage('Кофе для редактирования не выбран.')
        elif len(rows) == 1:
            row = rows[0]

            info = [table.item(row, i).text() for i in range(7)]

            self.add_edit_coffee_window = AddEditCoffeeWindow(self, info)
            self.add_edit_coffee_window.show()
        else:
            self.statusbar.showMessage('Пожалуйста, выберете только одно кофе для редактирования.')

    def add_coffee(self):
        self.statusbar.showMessage('')
        self.add_edit_coffee_window = AddEditCoffeeWindow(self)
        self.add_edit_coffee_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
