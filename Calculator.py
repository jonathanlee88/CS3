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

    layout = QHBoxLayout(widget)
    layout.addWidget(button1)
    layout.addWidget(button2)
    layout.addWidget(button3)
    layout.addWidget(button4)
    layout.addWidget(button5)
    layout.addWidget(button6)
    layout.addWidget(button7)
    layout.addWidget(button8)
    layout.addWidget(button9)

    grid = QGridLayout(widget)
    grid.addWidget(button1, 0, 0)
    grid.addWidget(button2, 1, 1)
    grid.addWidget(button3, 2, 2)
    grid.addWidget(button4, 3, 3)
    grid.addWidget(button5, 4, 4)
    grid.addWidget(button6, 5, 5)
    grid.addWidget(button7, 6, 6)
    grid.addWidget(button8, 7, 7)
    grid.addWidget(button9, 8, 8)

    hbox = QHBoxLayout(widget)
    hbox.addWidget(button1)
    hbox.addWidget(button2)
    hbox.addWidget(button3)
    hbox.addWidget(button4)
    hbox.addWidget(button5)
    hbox.addWidget(button6)
    hbox.addWidget(button7)
    hbox.addWidget(button8)
    hbox.addWidget(button9)

    ##hbox.setLayout(hbox)
    ##widget.addLayout(hbox)

    widget.setFixedSize(800, 600)
    ##widget.setWindowTitle('Steven Payne')
    ##widget.setStyleSheet('background-color: #cca8a5;')

    widget.show()  # displays window
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
