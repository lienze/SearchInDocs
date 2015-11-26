__author__ = 'lienze'
import sys
from PyQt4 import QtGui
from UIControl import MainWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    mp = MainWindow.Ui_MainWindow()
    mp.show()

    sys.exit(app.exec_())
else:
    pass
