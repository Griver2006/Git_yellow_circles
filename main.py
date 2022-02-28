import sys
from random import randrange

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        uic.loadUi('UI.ui', self)
        self.initUi()

    def initUi(self):
        self.btn_draw.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(200, 200, 0))
        radius = randrange(5, 200)
        qp.drawEllipse(randrange(0, 500), randrange(0, 450), radius, radius)
        qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec())