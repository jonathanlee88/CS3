import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    widget = QWidget()  # creates a window that is visible
    button1 = QPushButton("1")
    button2 = QPushButton("2")
    button3 = QPushButton("3")
    button4 = QPushButton("4")
    button5 = QPushButton("5")
    button6 = QPushButton("6")
    button7 = QPushButton("7")
    button8 = QPushButton("8")
    button9 = QPushButton("9")

    buttonAdd = QPushButton("+")
    buttonMinus = QPushButton("-")
    
    ##    layout = QHBoxLayout(widget)
    ##    layout.addWidget(button1)
    ##    layout.addWidget(button2)
    ##    layout.addWidget(button3)

    grid = QGridLayout(widget)
    grid.addWidget(button1, 0, 0)
    grid.addWidget(button2, 0, 1)
    grid.addWidget(button3, 0, 2)
    grid.addWidget(button4, 1, 0)
    grid.addWidget(button5, 1, 1)
    grid.addWidget(button6, 1, 2)
    grid.addWidget(button7, 2, 0)
    grid.addWidget(button8, 2, 1)
    grid.addWidget(button9, 2, 2)

    hbox = QHBoxLayout(widget)
    ##hbox.addWidget(button5)
    ##hbox.addWidget(button6)

##    widget.addLayout(hbox)

    widget.setFixedSize(800,600)
    ##    widget.setWindowTitle('Steven Payne')
    ##    widget.setStyleSheet(
    ##        'background-color: #cca8a5;'
    ##    )

    widget.show()  # displays window
    sys.exit(app.exec_())

def calculate():
    app = QApplication(sys.argv)

    sys.exit(app.exec_())

if __name__ == '__main__':
    window()