import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class PriceBox (QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent=parent)
        self.resize(70,40)

        self.palette = QPalette()
        self.palette.setColor(QPalette.WindowText,QColor(0,255,0))

        self.indicator = QLabel(self)
        self.indicator.resize(self.width(),self.height())
        self.indicator.move(0,0)
        self.indicator.setFont(QFont("Sans Serif", 9, QFont.Bold))
        self.indicator.setAlignment(Qt.AlignCenter)
        self.indicator.setPalette(self.palette)
        
        self.set(None)

    def set(self,value):
        if value:
            self.indicator.setText(str(value))
            self.color = QColor (0,0,0)
        elif value == 0:
            self.indicator.setText(str(value))
            self.color = QColor (0,0,0)
        elif value == None:
            self.indicator.setText("")
            self.color = QColor (192,192,192)
            
    def paintEvent (self,Event):
        p = QPainter(self)
        p.setBrush(self.color)
        p.setPen(QPen(self.color,1))
        p.drawRect(0,0,self.width(),self.height())

    def text(self):
        return self.indicator.text()

class AbstractModule (QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent=parent)
        self.resize (350,350)

        self.category = QLabel(self)
        self.category.move(40, 50)
        self.category.resize(110,50)
        self.category.setAlignment(Qt.AlignCenter)

        self.time = QLabel(self)
        self.time.move(40, 90)
        self.time.resize(110,50)
        self.time.setAlignment(Qt.AlignCenter)

        self.konki = QLabel(self)
        self.konki.move(40, 130)
        self.konki.resize(110,50)
        self.konki.setAlignment(Qt.AlignCenter)

        self.choice_category = QComboBox(self)
        self.choice_category.move(200,65)
        self.choice_category.resize(100,20)

        self.choice_time = QComboBox(self)
        self.choice_time.move(200,102)
        self.choice_time.resize(100,20)

        self.choice_konki = QComboBox(self)
        self.choice_konki.move(200,142)
        self.choice_konki.resize(100,20)

        self.get_sum = QPushButton(self)
        self.get_sum.move(130,200)
        self.get_sum.resize(80,30)

        self.price = QLabel(self)
        self.price.move(70, 280)
        self.price.resize(110,30)
        self.price.setAlignment(Qt.AlignLeft)