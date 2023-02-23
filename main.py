import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()

        self.load_table()

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

    def closeEvent(self, a0) -> None:
        self.con.close()
        return super().closeEvent(a0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
