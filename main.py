import sys  # sys нужен для передачи argv в QApplication

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from common_functions import *
from PyQt6 import QtWidgets
import gui


# noinspection DuplicatedCode
class App(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    methods = {0: analytical_solution, 1: explicit_solve, 2: implicit_solve, 3: crank_nicholson_solve}

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #  Функционал первой вкладки (основной)
        self.method = 0
        self.method_2 = 1
        self.method_3 = 1
        self.analytical_solution_selector.setChecked(True)
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
        self.start_button.clicked.connect(self.start_dynamics_calculate)
        #  Функционал второй вкладки (сходимость решений)
        self.explicit_method_selector_2.setChecked(True)
        self.explicit_method_selector_2.number = 1
        self.explicit_method_selector_2.toggled.connect(self.method_selected)
        self.implicit_method_selector_2.number = 2
        self.implicit_method_selector_2.toggled.connect(self.method_selected)
        self.crank_nicholson_method_selector_2.number = 3
        self.crank_nicholson_method_selector_2.toggled.connect(self.method_selected)
        self.tableWidget_by_t.cellChanged.connect(self.add_table_value)
        self.tableWidget_by_x.cellChanged.connect(self.add_table_value)
        self.tableWidget_error_rates.cellChanged.connect(self.add_table_value)
        self.add_x_button_2.clicked.connect(self.add_by_t_value)
        self.delete_x_button_2.clicked.connect(self.delete_by_t_value)
        self.reset_x_button_2.clicked.connect(self.reset_table_t_values)
        self.add_t_button_2.clicked.connect(self.add_by_x_value)
        self.delete_t_button_2.clicked.connect(self.delete_by_x_value)
        self.reset_t_button_2.clicked.connect(self.reset_table_x_values)
        self.start_button_2.clicked.connect(self.start_convergences_calculate)
        #  Функционал третьей вкладки
        self.explicit_method_selector_3.setChecked(True)
        self.explicit_method_selector_3.number = 1
        self.explicit_method_selector_3.toggled.connect(self.method_selected)
        self.implicit_method_selector_3.number = 2
        self.implicit_method_selector_3.toggled.connect(self.method_selected)
        self.crank_nicholson_method_selector_3.number = 3
        self.crank_nicholson_method_selector_3.toggled.connect(self.method_selected)
        self.add_button.clicked.connect(self.add_table_error_row)
        self.delete_button_3.clicked.connect(self.delete_table_error_row)
        self.reset_button_3.clicked.connect(self.reset_table_error)
        self.start_button_3.clicked.connect(self.start_errors_calculate)

    @staticmethod
    def add_value(given_list, value, max_value):
        if value <= max_value:
            if given_list.findItems(str("%.2f" % value), Qt.MatchFlags.MatchExactly):
                pass
            elif given_list.count():
                for i in range(given_list.count()):
                    if value < float(given_list.item(i).text()):
                        given_list.insertItem(i, str("%.2f" % value))
                        break
                    elif i == (given_list.count() - 1):
                        given_list.insertItem(i + 1, str("%.2f" % value))
            else:
                given_list.addItem(str("%.2f" % value))
            return True
        else:
            return False

    def add_x_value(self):
        if self.add_value(self.x_setted_list, self.x_input.value(), self.length_input.value()) is False:
            QMessageBox.critical(self, "Ошибка! ", "Выберите x меньше или равным длине трубки")

    def delete_x_value(self):
        self.x_setted_list.takeItem(self.x_setted_list.currentRow())

    def reset_x_values(self):
        self.x_setted_list.clear()

    def add_t_value(self):
        if self.add_value(self.t_setted_list, self.t_input.value(), self.time_input.value()) is False:
            QMessageBox.critical(self, "Ошибка! ", "Выберите t меньше или равным времени наблюдения")

    def delete_t_value(self):
        self.t_setted_list.takeItem(self.t_setted_list.currentRow())

    def reset_t_values(self):
        self.t_setted_list.clear()

    def method_selected(self):
        name = self.sender().objectName()
        if name[-1] == "2":
            self.method_2 = self.sender().number
        elif name[-1] == "3":
            self.method_3 = self.sender().number
            if 1 <= self.method_3 <= 2:
                text = "ε(ht/4, hx/2)"
            else:
                text = "ε(ht/2, hx/2)"
            self.tableWidget_error_rates.horizontalHeaderItem(3).setText(text)
        else:
            self.method = self.sender().number

    @staticmethod
    def get_functions_for_plot(x, field, given_list, label):
        x_values = np.array([])
        for i in range(given_list.count()):
            if float(given_list.item(i).text()) <= x[len(x) - 1]:
                index, = np.where(x >= float(given_list.item(i).text()))
                x_values = np.append(x_values, x[index[0]])
        x_values = np.unique(x_values)
        functions = np.zeros((len(x_values), len(field[0])))
        labels = np.array([])
        given_list.clear()
        for i in range(len(x_values)):
            App.add_value(given_list, x_values[i], x[len(x) - 1])
            index, = np.where(x >= x_values[i])
            functions[i] = field[index[0]]
            labels = np.append(labels, label + " = " + str("%.2f" % x[index[0]]))
        return functions, labels

    def start_dynamics_calculate(self):
        self.waiting_text.setText("Команда выполняется…")
        self.repaint()
        x = linspace(0, self.length_input.value(), self.i_input.value())  # разбиение интервала длины
        t = linspace(0, self.time_input.value(), self.k_input.value())  # разбиение интервала времени
        alpha = self.alpha_input.value()
        c = self.c_input.value()
        d = self.d_input.value()
        number = self.number_input.value()
        field = self.methods[self.method](x, t, alpha, c, d, number)
        x_functions, x_labels = self.get_functions_for_plot(x, field, self.x_setted_list, "x")
        t_functions, t_labels = self.get_functions_for_plot(t, field.T, self.t_setted_list, "t")
        t_array = np.array([t for _ in range(len(x_functions))])
        x_array = np.array([x for _ in range(len(t_functions))])
        plot(t_array, x_functions, x_labels, "t, с", "Изменение решения u(x,t) по времени")
        plot(x_array, t_functions, t_labels, "x, см", "Изменение решения u(x,t) по координате")
        self.waiting_text.setText("Ожидание команды…")

    def add_table_value(self):
        item = self.sender().item(self.sender().currentRow(), self.sender().currentColumn()).text()
        if 0 <= self.sender().currentColumn() <= 1:
            if not item.isdigit() or int(item) == 0:
                self.sender().blockSignals(True)
                self.sender().setItem(self.sender().currentRow(), self.sender().currentColumn(),
                                      QTableWidgetItem(str(100)))
                self.sender().blockSignals(False)
        else:
            self.sender().blockSignals(True)
            self.sender().setItem(self.sender().currentRow(), self.sender().currentColumn(), QTableWidgetItem(""))
            self.sender().blockSignals(False)

    def add_by_t_value(self):
        self.tableWidget_by_t.insertRow(self.tableWidget_by_t.rowCount())

    def reset_table_t_values(self):
        self.tableWidget_by_t.clearContents()
        self.tableWidget_by_t.setRowCount(0)

    def delete_by_t_value(self):
        self.tableWidget_by_t.removeRow(self.tableWidget_by_t.currentRow())

    def add_by_x_value(self):
        self.tableWidget_by_x.insertRow(self.tableWidget_by_x.rowCount())

    def reset_table_x_values(self):
        self.tableWidget_by_x.clearContents()
        self.tableWidget_by_x.setRowCount(0)

    def delete_by_x_value(self):
        self.tableWidget_by_x.removeRow(self.tableWidget_by_x.currentRow())

    def start_convergences_calculate(self):
        self.waiting_text_2.setText("Команда выполняется…")
        self.repaint()
        alpha = self.alpha_input.value()
        c = self.c_input.value()
        d = self.d_input.value()
        number = self.number_input_2.value()
        x_input = self.x_input_2.value()
        t_input = self.t_input_2.value()
        x = linspace(0, self.length_input.value(), self.i_input_2.value())  # разбиение интервала длины
        t = linspace(0, self.time_input.value(), self.k_input_2.value())  # разбиение интервала времени
        field = analytical_solution(x, t, alpha, c, d, number)
        index, = np.where(x >= x_input)
        x_array = np.empty((self.tableWidget_by_t.rowCount() + 1), dtype=object)
        x_array[0] = t
        x_functions = np.empty((self.tableWidget_by_t.rowCount() + 1), dtype=object)
        x_functions[0] = field[index[0]]
        x_labels = "Аналит. решение"
        index, = np.where(t >= t_input)
        t_array = np.empty((self.tableWidget_by_x.rowCount() + 1), dtype=object)
        t_array[0] = x
        t_functions = np.empty((self.tableWidget_by_x.rowCount() + 1), dtype=object)
        t_functions[0] = field.T[index[0]]
        t_labels = "Аналит. решение"
        for i in range(self.tableWidget_by_t.rowCount()):
            if not self.tableWidget_by_t.item(i, 0) or not self.tableWidget_by_t.item(0, 1):
                break
            x = linspace(0, self.length_input.value(), int(self.tableWidget_by_t.item(i, 0).text()))
            t = linspace(0, self.time_input.value(), int(self.tableWidget_by_t.item(i, 1).text()))
            field = self.methods[self.method_2](x, t, alpha, c, d, number)
            index, = np.where(x >= x_input)
            x_array[i + 1] = t
            x_functions[i + 1] = field[index[0]]
            x_labels = np.append(x_labels, "I=" + self.tableWidget_by_t.item(i, 0).text() + " K=" +
                                 self.tableWidget_by_t.item(i, 1).text())
        for i in range(self.tableWidget_by_x.rowCount()):
            if not self.tableWidget_by_x.item(i, 0) or not self.tableWidget_by_x.item(0, 1):
                break
            x = linspace(0, self.length_input.value(), int(self.tableWidget_by_x.item(i, 0).text()))
            t = linspace(0, self.time_input.value(), int(self.tableWidget_by_x.item(i, 1).text()))
            field = self.methods[self.method_2](x, t, alpha, c, d, number)
            index, = np.where(t >= t_input)
            t_array[i + 1] = x
            t_functions[i + 1] = field.T[index[0]]
            t_labels = np.append(t_labels, "I=" + self.tableWidget_by_x.item(i, 0).text() + " K=" +
                                 self.tableWidget_by_x.item(i, 1).text())
        plot(x_array, x_functions, x_labels, "t, с", "Сходимость решения u(x,t) к точному, x = " + str(x_input))
        plot(t_array, t_functions, t_labels, "x, см", "Сходимость решения u(x, t) к точному, t = " + str(t_input))
        self.waiting_text_2.setText("Ожидание команды…")

    def add_table_error_row(self):
        self.tableWidget_error_rates.insertRow(self.tableWidget_error_rates.rowCount())

    def reset_table_error(self):
        self.tableWidget_error_rates.clearContents()
        self.tableWidget_error_rates.setRowCount(0)

    def delete_table_error_row(self):
        self.tableWidget_error_rates.removeRow(self.tableWidget_error_rates.currentRow())

    def start_errors_calculate(self):
        self.waiting_text_3.setText("Команда выполняется…")
        self.repaint()
        alpha = self.alpha_input.value()
        c = self.c_input.value()
        d = self.d_input.value()
        time = self.time_input.value()
        length = self.length_input.value()
        number = self.number_input_2.value()
        if 1 <= self.method_3 <= 2:
            hx_rate, ht_rate = 4, 2
        else:
            hx_rate, ht_rate = 2, 2
        norm_error = uniform_norm_error
        for j in range(self.tableWidget_error_rates.rowCount()):
            if not self.tableWidget_error_rates.item(j, 0) or not self.tableWidget_error_rates.item(j, 1):
                break
            i = int(self.tableWidget_error_rates.item(j, 0).text())
            k = int(self.tableWidget_error_rates.item(j, 1).text())
            results = get_numerical_experiments(
                i, k, alpha, c, d, time, length, number, hx_rate, ht_rate, self.methods[self.method_3], norm_error)
            self.tableWidget_error_rates.setItem(j, 0, QTableWidgetItem(str(int(results[0]))))
            self.tableWidget_error_rates.setItem(j, 1, QTableWidgetItem(str(int(results[1]))))
            self.tableWidget_error_rates.setItem(j, 2, QTableWidgetItem(str("%.6f" % results[2])))
            self.tableWidget_error_rates.setItem(j, 3, QTableWidgetItem(str("%.6f" % results[3])))
            self.tableWidget_error_rates.setItem(j, 4, QTableWidgetItem(str("%.6f" % results[4])))
            self.repaint()
        self.waiting_text_3.setText("Ожидание команды…")


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = App()  # Создаём объект класса App
    window.setWindowTitle('ЧММФ — курсовая работа (1 вариант)')
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
