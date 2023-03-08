from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtGui import QDoubleValidator

class Calculator(QWidget):
    def init(self):
        super().init()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Калькулятор')
        self.setGeometry(100, 100, 300, 200)

        self.label1 = QLabel('Число 1')
        self.lineedit1 = QLineEdit()
        self.lineedit1.setValidator(QDoubleValidator())

        self.label2 = QLabel('Число 2')
        self.lineedit2 = QLineEdit()
        self.lineedit2.setValidator(QDoubleValidator())

        self.label3 = QLabel('Результат')
        self.lineedit3 = QLineEdit()
        self.lineedit3.setReadOnly(True)

        self.button_add = QPushButton('Сложение')
        self.button_add.clicked.connect(self.add)

        self.button_subtract = QPushButton('Вычитание')
        self.button_subtract.clicked.connect(self.subtract)

        self.button_multiply = QPushButton('Умножение')
        self.button_multiply.clicked.connect(self.multiply)

        self.button_divide = QPushButton('Деление')
        self.button_divide.clicked.connect(self.divide)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.lineedit1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.lineedit2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.lineedit3)
        vbox.addWidget(self.button_add)
        vbox.addWidget(self.button_subtract)
        vbox.addWidget(self.button_multiply)
        vbox.addWidget(self.button_divide)

        self.setLayout(vbox)
        self.show()

    def add(self):
        num1 = float(self.lineedit1.text())
        num2 = float(self.lineedit2.text())
        result = num1 + num2
        self.lineedit3.setText(str(result))

    def subtract(self):
        num1 = float(self.lineedit1.text())
        num2 = float(self.lineedit2.text())
        result = num1 - num2
        self.lineedit3.setText(str(result))

    def multiply(self):
        num1 = float(self.lineedit1.text())
        num2 = float(self.lineedit2.text())
        result = num1 * num2
        self.lineedit3.setText(str(result))

    def divide(self):
        num1 = float(self.lineedit1.text())
        num2 = float(self.lineedit2.text())
        if num2 == 0:
            self.lineedit3.setText('Ошибка: деление на ноль')
        else:
            result = num1 / num2
            self.lineedit3.setText(str(result))

if __name__ == '__main__':
    app = QApplication([])
    calculator = Calculator()
    app.exec()
