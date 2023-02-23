import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QWidget,
)


class Add_Window(QWidget):
    def __init__(
        self, con: sqlite3.Connection, cur: sqlite3.Cursor, load_table
    ):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)

        self.con = con
        self.cur = cur
        self.load_table = load_table

        self.pushButton.clicked.connect(self.add)

    def add(self):
        self.cur.execute(
            f"""
            INSERT INTO coffee(id, variety_name, degree_of_roasting, is_ground, taste_description, price, packing_volume)
            VALUES({self.id_lb.text()}, '{self.variety_name_lb.text()}', '{self.degree_of_roasting_lb.text()}', {self.is_ground_lb.text()}, '{self.taste_description_lb.text()}', '{self.price_lb.text()}', '{self.packing_volume_lb.text()}') 
        """
        )

        self.con.commit()

        self.load_table()
        self.close()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()

        self.add_window = Add_Window(self.con, self.cur, self.load_table)

        self.load_table()

        self.pushButton.clicked.connect(self.add)

    def load_table(self):
        res = sorted(self.cur.execute('SELECT * FROM coffee').fetchall())
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(len(res[0]))

        self.tableWidget.setHorizontalHeaderLabels(
            [
                'ID',
                'Название сорта',
                'Степень обжарки',
                'Молотый/В зернах',
                'Описание вкуса',
                'Цена',
                'Объем упаковки',
            ]
        )

        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

        self.tableWidget.resizeColumnsToContents()

    def add(self):
        self.add_window.show()

    def closeEvent(self, a0) -> None:
        self.con.close()
        return super().closeEvent(a0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
