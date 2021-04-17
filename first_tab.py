# Form implementation generated from reading ui file 'first tab.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1200, 750))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.k_text = QtWidgets.QLabel(self.centralwidget)
        self.k_text.setObjectName("k_text")
        self.gridLayout.addWidget(self.k_text, 6, 0, 2, 1)
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stop_button.setFont(font)
        self.stop_button.setObjectName("stop_button")
        self.gridLayout.addWidget(self.stop_button, 10, 5, 2, 1)
        self.alpha_input = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.alpha_input.setMaximum(1.0)
        self.alpha_input.setSingleStep(0.01)
        self.alpha_input.setProperty("value", 0.24)
        self.alpha_input.setObjectName("alpha_input")
        self.gridLayout.addWidget(self.alpha_input, 13, 1, 1, 1)
        self.c_input = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.c_input.setMaximum(1.0)
        self.c_input.setSingleStep(0.01)
        self.c_input.setProperty("value", 0.8)
        self.c_input.setObjectName("c_input")
        self.gridLayout.addWidget(self.c_input, 14, 1, 1, 1)
        self.i_text = QtWidgets.QLabel(self.centralwidget)
        self.i_text.setObjectName("i_text")
        self.gridLayout.addWidget(self.i_text, 5, 0, 1, 1)
        self.k_input = QtWidgets.QSpinBox(self.centralwidget)
        self.k_input.setMaximum(1000000)
        self.k_input.setProperty("value", 100)
        self.k_input.setObjectName("k_input")
        self.gridLayout.addWidget(self.k_input, 6, 1, 2, 1)
        self.crank_nicholson_method_selector = QtWidgets.QRadioButton(self.centralwidget)
        self.crank_nicholson_method_selector.setObjectName("crank_nicholson_method_selector")
        self.gridLayout.addWidget(self.crank_nicholson_method_selector, 3, 0, 1, 1)
        self.add_t_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_t_button.setObjectName("add_t_button")
        self.gridLayout.addWidget(self.add_t_button, 19, 5, 1, 1)
        self.delete_t_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_t_button.setObjectName("delete_t_button")
        self.gridLayout.addWidget(self.delete_t_button, 18, 4, 1, 2)
        self.alpha_text = QtWidgets.QLabel(self.centralwidget)
        self.alpha_text.setObjectName("alpha_text")
        self.gridLayout.addWidget(self.alpha_text, 13, 0, 1, 1)
        self.t_input = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.t_input.setDecimals(2)
        self.t_input.setMaximum(1000.0)
        self.t_input.setSingleStep(0.01)
        self.t_input.setProperty("value", 75.0)
        self.t_input.setObjectName("t_input")
        self.gridLayout.addWidget(self.t_input, 19, 4, 1, 1)
        self.number_input = QtWidgets.QSpinBox(self.centralwidget)
        self.number_input.setMaximum(1000000)
        self.number_input.setProperty("value", 1000)
        self.number_input.setObjectName("number_input")
        self.gridLayout.addWidget(self.number_input, 8, 1, 2, 1)
        self.delete_x_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_x_button.setObjectName("delete_x_button")
        self.gridLayout.addWidget(self.delete_x_button, 8, 4, 1, 2)
        self.add_x_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_x_button.setObjectName("add_x_button")
        self.gridLayout.addWidget(self.add_x_button, 9, 5, 1, 1)
        self.d_text = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setKerning(True)
        self.d_text.setFont(font)
        self.d_text.setObjectName("d_text")
        self.gridLayout.addWidget(self.d_text, 15, 0, 1, 1)
        self.set_x_text = QtWidgets.QLabel(self.centralwidget)
        self.set_x_text.setAlignment(QtCore.Qt.Alignment.AlignRight|QtCore.Qt.Alignment.AlignTrailing|QtCore.Qt.Alignment.AlignVCenter)
        self.set_x_text.setObjectName("set_x_text")
        self.gridLayout.addWidget(self.set_x_text, 9, 3, 1, 1)
        self.set_t_text = QtWidgets.QLabel(self.centralwidget)
        self.set_t_text.setAlignment(QtCore.Qt.Alignment.AlignRight|QtCore.Qt.Alignment.AlignTrailing|QtCore.Qt.Alignment.AlignVCenter)
        self.set_t_text.setObjectName("set_t_text")
        self.gridLayout.addWidget(self.set_t_text, 19, 3, 1, 1)
        self.time_input = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.time_input.setDecimals(2)
        self.time_input.setMaximum(1000.0)
        self.time_input.setSingleStep(0.01)
        self.time_input.setProperty("value", 150.0)
        self.time_input.setObjectName("time_input")
        self.gridLayout.addWidget(self.time_input, 17, 1, 2, 1)
        self.list_t_text = QtWidgets.QLabel(self.centralwidget)
        self.list_t_text.setObjectName("list_t_text")
        self.gridLayout.addWidget(self.list_t_text, 12, 3, 1, 3)
        self.reset_t_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_t_button.setObjectName("reset_t_button")
        self.gridLayout.addWidget(self.reset_t_button, 17, 4, 1, 2)
        self.time_text = QtWidgets.QLabel(self.centralwidget)
        self.time_text.setObjectName("time_text")
        self.gridLayout.addWidget(self.time_text, 17, 0, 2, 1)
        self.length_text = QtWidgets.QLabel(self.centralwidget)
        self.length_text.setObjectName("length_text")
        self.gridLayout.addWidget(self.length_text, 16, 0, 1, 1)
        self.implicit_method_selector = QtWidgets.QRadioButton(self.centralwidget)
        self.implicit_method_selector.setCheckable(True)
        self.implicit_method_selector.setObjectName("implicit_method_selector")
        self.gridLayout.addWidget(self.implicit_method_selector, 2, 0, 1, 1)
        self.i_input = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.i_input.setFont(font)
        self.i_input.setMaximum(1000000)
        self.i_input.setProperty("value", 100)
        self.i_input.setDisplayIntegerBase(10)
        self.i_input.setObjectName("i_input")
        self.gridLayout.addWidget(self.i_input, 5, 1, 1, 1)
        self.explicit_method_selector = QtWidgets.QRadioButton(self.centralwidget)
        self.explicit_method_selector.setObjectName("explicit_method_selector")
        self.gridLayout.addWidget(self.explicit_method_selector, 1, 0, 1, 1)
        self.list_x_text = QtWidgets.QLabel(self.centralwidget)
        self.list_x_text.setObjectName("list_x_text")
        self.gridLayout.addWidget(self.list_x_text, 0, 3, 1, 3)
        self.Otu_plot = QtWidgets.QGraphicsView(self.centralwidget)
        self.Otu_plot.setMinimumSize(QtCore.QSize(551, 361))
        self.Otu_plot.setObjectName("Otu_plot")
        self.gridLayout.addWidget(self.Otu_plot, 0, 2, 11, 1)
        self.x_setted_list = QtWidgets.QListWidget(self.centralwidget)
        self.x_setted_list.setObjectName("x_setted_list")
        self.gridLayout.addWidget(self.x_setted_list, 1, 3, 6, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 2)
        self.Oxu_plot = QtWidgets.QGraphicsView(self.centralwidget)
        self.Oxu_plot.setMinimumSize(QtCore.QSize(551, 361))
        self.Oxu_plot.setObjectName("Oxu_plot")
        self.gridLayout.addWidget(self.Oxu_plot, 11, 2, 9, 1)
        self.reset_x_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_x_button.setObjectName("reset_x_button")
        self.gridLayout.addWidget(self.reset_x_button, 7, 4, 1, 2)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 10, 3, 2, 2)
        self.d_input = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setKerning(True)
        self.d_input.setFont(font)
        self.d_input.setDecimals(3)
        self.d_input.setMaximum(1.0)
        self.d_input.setSingleStep(0.001)
        self.d_input.setProperty("value", 0.002)
        self.d_input.setObjectName("d_input")
        self.gridLayout.addWidget(self.d_input, 15, 1, 1, 1)
        self.t_setted_list = QtWidgets.QListWidget(self.centralwidget)
        self.t_setted_list.setObjectName("t_setted_list")
        self.gridLayout.addWidget(self.t_setted_list, 13, 3, 4, 3)
        self.x_input = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.x_input.setDecimals(2)
        self.x_input.setMaximum(100.0)
        self.x_input.setSingleStep(0.01)
        self.x_input.setProperty("value", 15.0)
        self.x_input.setObjectName("x_input")
        self.gridLayout.addWidget(self.x_input, 9, 4, 1, 1)
        self.number_text = QtWidgets.QLabel(self.centralwidget)
        self.number_text.setObjectName("number_text")
        self.gridLayout.addWidget(self.number_text, 8, 0, 2, 1)
        self.length_input = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.length_input.setDecimals(2)
        self.length_input.setMaximum(100.0)
        self.length_input.setSingleStep(0.01)
        self.length_input.setProperty("value", 30.0)
        self.length_input.setObjectName("length_input")
        self.gridLayout.addWidget(self.length_input, 16, 1, 1, 1)
        self.c_text = QtWidgets.QLabel(self.centralwidget)
        self.c_text.setObjectName("c_text")
        self.gridLayout.addWidget(self.c_text, 14, 0, 1, 1)
        self.analytical_solution_selector = QtWidgets.QRadioButton(self.centralwidget)
        self.analytical_solution_selector.setObjectName("analytical_solution_selector")
        self.gridLayout.addWidget(self.analytical_solution_selector, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.k_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">K, кол-во разбиений по времени</p></body></html>"))
        self.stop_button.setText(_translate("MainWindow", "СТОП"))
        self.i_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">I, кол-во разбиений по длине</p></body></html>"))
        self.crank_nicholson_method_selector.setText(_translate("MainWindow", "Схема Кранка-Николсона"))
        self.add_t_button.setText(_translate("MainWindow", "Добавить"))
        self.delete_t_button.setText(_translate("MainWindow", "Удалить выделенное"))
        self.alpha_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'palatino linotype\',\'new athena unicode\',\'athena\',\'gentium\',\'code2000\',\'serif\';\">α</span>, коэффициент диффузии, см²/с</p></body></html>"))
        self.delete_x_button.setText(_translate("MainWindow", "Удалить выделенное"))
        self.add_x_button.setText(_translate("MainWindow", "Добавить"))
        self.d_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">D, коэффицент пропорциональности</p><p align=\"center\">концентрации растворённого вещества, 1/с</p></body></html>"))
        self.set_x_text.setText(_translate("MainWindow", "x = "))
        self.set_t_text.setText(_translate("MainWindow", "t = "))
        self.list_t_text.setText(_translate("MainWindow", "Список графиков по длине"))
        self.reset_t_button.setText(_translate("MainWindow", "Очистить список"))
        self.time_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">T, время наблюдения, с</p></body></html>"))
        self.length_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">l, длина трубки, см</p></body></html>"))
        self.implicit_method_selector.setText(_translate("MainWindow", "Неявная схема"))
        self.explicit_method_selector.setText(_translate("MainWindow", "Явная схема"))
        self.list_x_text.setText(_translate("MainWindow", "Список графиков по времени"))
        self.reset_x_button.setText(_translate("MainWindow", "Очистить список"))
        self.start_button.setText(_translate("MainWindow", "СТАРТ"))
        self.number_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">N, кол-во слагаемых в сумме Фурье</p><p align=\"center\">аналитического решения</p></body></html>"))
        self.c_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">c, коэффициент пористости</p></body></html>"))
        self.analytical_solution_selector.setText(_translate("MainWindow", "Аналитическое решение"))
