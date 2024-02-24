from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.draw)
        self.coords = []

    def draw(self):
        self.size = random.randint(10, 100)
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            qp.setPen(QColor(r, g, b))
            qp.setBrush(QColor(r, g, b))
            qp.drawEllipse(random.randint(100, 680 - 100), random.randint(100, 480 - 100), self.size, self.size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())