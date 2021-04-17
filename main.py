import sys  # sys нужен для передачи argv в QApplication
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
        self.start_button.clicked.connect(self.start)

    def method_selected(self):
        self.method = self.sender().number

    def start(self):
        x = linspace(0, self.length_input.value(), self.i_input.value())  # разбиение интервала длины
        t = linspace(0, self.time_input.value(), self.k_input.value())  # разбиение интервала времени
        alpha = self.alpha_input.value()
        c = self.c_input.value()
        d = self.d_input.value()
        time = self.time_input.value()
        length = self.length_input.value()
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
