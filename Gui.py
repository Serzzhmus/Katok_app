import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Abstract import *
from Text import *


class Window (AbstractModule):
    def __init__(self, parent=None):
        AbstractModule.__init__(self,parent=parent)

        self.category.setText(category_text)
        self.category.setFont(QFont("Sans Serif", 8, QFont.Bold))

        self.time.setText(time_text)
        self.time.setFont(QFont("Sans Serif", 8, QFont.Bold))

        self.konki.setText(konki_text)
        self.konki.setFont(QFont("Sans Serif", 8, QFont.Bold))

        self.choice_category.addItems(choice_category_text)
        self.choice_category.setFont(QFont("Sans Serif", 8, QFont.Bold))

        self.choice_time.addItems(choice_time_text)
        self.choice_time.setFont(QFont("Sans Serif", 8, QFont.Bold))

        self.choice_konki.addItems(choice_konki_text)
        self.choice_konki.setFont(QFont("Sans Serif", 8, QFont.Bold))

        self.get_sum.setText(button_text)

        self.price.setText(price_text)
        self.price.setFont(QFont("Sans Serif", 9, QFont.Bold))

        self.price_box = PriceBox(self)
        self.price_box.move(160,265)


