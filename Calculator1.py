from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

class Calculator(QWidget):
    def init(self):
        super().init()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Калькулятор')
        self.setGeometry(100, 100, 250, 250)

        self.lineedit = QLineEdit(self)
        self.lineedit.setReadOnly(True)
        self.lineedit.setAlignment(Qt.AlignmentFlag.AlignRight)

        grid = QGridLayout()
        self.setLayout(grid)

        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            '0', '.', '=', '/'
        ]

        positions = [(i, j) for i in range(4) for j in range(4)]

        for position, button in zip(positions, buttons):
            if button == '':
                continue
            button = QPushButton(button)
            button.clicked.connect(self.buttonClicked)
            grid.addWidget(button, *position)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lineedit)
        vbox.addLayout(grid)

        self.setLayout(vbox)
        self.show()

    def buttonClicked(self):
        button = self.sender()
        digit = button.text()

        if digit == '=':
            try:
                result = str(eval(self.lineedit.text()))
            except:
                result = 'Ошибка'
            self.lineedit.setText(result)
        elif digit == 'C':
            self.lineedit.setText('')
        else:
            self.lineedit.setText(self.lineedit.text() + digit)

if __name__ == '__main__':
    app = QApplication([])
    calculator = Calculator()
    app.exec()
