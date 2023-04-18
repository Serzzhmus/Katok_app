import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from time import *

from Gui import *
from Text import *
from BL import *


class Katok_app (BL):
    def __init__(self, parent=None):
        BL.__init__(self,parent=parent)

        self.bl = BL()

        self.bl.get_sum.clicked.connect(self.bl.on_clik)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Katok_app()
    w.show()
    w.setWindowTitle('Общественный каток')
    cleanup = app.exec() 
    sys.exit(cleanup)