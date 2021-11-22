import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic

from random import randint


class CirclesApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.isDraw = False
        self.pushButton.clicked.connect(self.draw_circles)

    def draw_circles(self):
        self.isDraw = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        if self.isDraw:
            qp.begin(self)

            qp.setPen(QPen(Qt.yellow, 8))

            d1 = randint(100, 400)
            d2 = randint(100, 400)
            d3 = randint(100, 400)

            qp.drawEllipse(75, 40, d1 // 2, d1 // 2)
            qp.drawEllipse(10, 70, d2 // 2, d2 // 2)
            qp.drawEllipse(80, 50, d3 // 2, d3 // 2)

            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CirclesApp()
    ex.show()
    sys.exit(app.exec_())
