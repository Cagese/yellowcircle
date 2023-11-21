import sys
from random import randint

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from Ui import Ui_MainWindow


class Suprematism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qp = QPainter()
        self.flag = False
        self.status = None
        self.yellowmagic.clicked.connect(self.drawf)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.status)
            self.qp.end()

    def draw(self, status):
        self.coords_ = [400,300]
        R = randint(20, 300)
        self.qp.setBrush(QColor(randint(1,255),randint(1,255),randint(1,255)))
        self.qp.drawEllipse(int(self.coords_[0] - R / 2),
                            int(self.coords_[1] - R / 2), R, R)




    def mousePressEvent(self, event):
        self.coords_ = [event.x(), event.y()]
        if (event.button() == Qt.LeftButton):
            self.status = 1
        elif (event.button() == Qt.RightButton):
            self.status = 2
        self.drawf()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec_())
