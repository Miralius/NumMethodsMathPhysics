import sys  # sys нужен для передачи argv в QApplication

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from common_functions import *
from PyQt6 import QtWidgets
import first_tab  # Это наш конвертированный файл дизайна


class App(QtWidgets.QMainWindow, first_tab.Ui_MainWindow):
    method = 0
    methods = {0: analytical_solution, 1: explicit_solve, 2: implicit_solve, 3: crank_nicholson_solve}

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.analytical_solution_selector.number = 0
        self.analytical_solution_selector.toggled.connect(self.method_selected)
        self.explicit_method_selector.number = 1
        self.explicit_method_selector.toggled.connect(self.method_selected)
        self.implicit_method_selector.number = 2
        self.implicit_method_selector.toggled.connect(self.method_selected)
        self.crank_nicholson_method_selector.number = 3
        self.crank_nicholson_method_selector.toggled.connect(self.method_selected)
        self.add_x_button.clicked.connect(self.add_x_value)
        self.delete_x_button.clicked.connect(self.delete_x_value)
        self.reset_x_button.clicked.connect(self.reset_x_values)
        self.add_t_button.clicked.connect(self.add_t_value)
        self.delete_t_button.clicked.connect(self.delete_t_value)
        self.reset_t_button.clicked.connect(self.reset_t_values)
        self.start_button.clicked.connect(self.start)

    def add_x_value(self):
        if self.x_setted_list.findItems(str("%.2f" % self.x_input.value()), Qt.MatchFlags.MatchExactly):
            pass
        elif self.x_input.value() <= self.length_input.value():
            self.x_setted_list.addItem(str("%.2f" % self.x_input.value()))
        else:
            QMessageBox.critical(self, "Ошибка! ", "Выберите x меньше или равным длине трубки")
        self.x_setted_list.sortItems()

    def delete_x_value(self):
        self.x_setted_list.takeItem(self.x_setted_list.currentRow())

    def reset_x_values(self):
        self.x_setted_list.clear()

    def add_t_value(self):
        if self.t_setted_list.findItems(str("%.2f" % self.t_input.value()), Qt.MatchFlags.MatchExactly):
            pass
        elif self.t_input.value() <= self.time_input.value():
            self.t_setted_list.addItem(str("%.2f" % self.t_input.value()))
        else:
            QMessageBox.critical(self, "Ошибка! ", "Выберите t меньше или равным времени наблюдения")
        self.t_setted_list.sortItems()

    def delete_t_value(self):
        self.t_setted_list.takeItem(self.t_setted_list.currentRow())

    def reset_t_values(self):
        self.t_setted_list.clear()

    def method_selected(self):
        self.method = self.sender().number

    def start(self):
        x = linspace(0, self.length_input.value(), self.i_input.value())  # разбиение интервала длины
        t = linspace(0, self.time_input.value(), self.k_input.value())  # разбиение интервала времени
        alpha = self.alpha_input.value()
        c = self.c_input.value()
        d = self.d_input.value()
        number = self.number_input.value()
        field = self.methods[self.method](x, t, alpha, c, d, number)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = App()  # Создаём объект класса App
    window.setWindowTitle('ЧММФ — курсовая работа (1 вариант)')
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
