import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from time import *

from Gui import *
from Text import *


class BL (Window):
    def __init__(self, parent=None):
        Window.__init__(self,parent=parent)

        self.gui = Window()

        self.get_sum.clicked.connect(self.on_clik)

    def on_clik(self):
        self.value = self.get_combobox_value()
        self.koef = self.get_koef(self.value)
        self.time = self.get_time(self.value)
        self.konki = self.get_konki(self.value)
        self.price = self.calculate(self.koef, self.time, self.konki)
        self.price_box.set(self.price)
        self.log = self.logging(self.price)

    def get_combobox_value(self):
        category_item = self.choice_category.currentText()
        time_item = self.choice_time.currentText()
        konki_item = self.choice_konki.currentText()
        list = []
        list.append(category_item)
        list.append(time_item)
        list.append(konki_item)
        return list

    def calculate(self, koef, time, konki):
        result = (350 + konki) * koef * time
        return result

    def get_koef(self, value):
        koef = 0
        if value[0] == choice_category_text[1]:
            koef = float(1)
        if value[0] == choice_category_text[2]:
            koef = float(0.75)
        if value[0] == choice_category_text[3]:
            koef = float(0.5)
        return koef

    def get_time(self, value):
        time = 0
        if value[1] == choice_time_text[1]:
            time = int(1)
        if value[1] == choice_time_text[2]:
            time = int(2)
        if value[1] == choice_time_text[3]:
            time = int(3)
        return time

    def get_konki(self, value):
        konki = 0
        if value[2] == choice_konki_text[1]:
            konki = int(250)
        if value[2] == choice_konki_text[2]:
            konki = int(0)
        return konki

    def logging(self, string):
        filename = '_log.txt'
        line = ""
        line += strftime("%d-%m-%Y; %H:%M:%S") #Date and time
        line += "; "
        line += ("Куплен билет на сумму - " + str(string) + " руб.")
        line += "; "
        line += "\n" #New line

        if str(string) == '0':
            pass
        else:
            try:
                with open(filename, "a", encoding = "utf8") as file:
                    file.write(line)
            except Exception:
                print ("Can't write string")
