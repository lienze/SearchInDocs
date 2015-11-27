__author__ = 'lienze'
# coding=utf-8
import sys
from PyQt4 import QtGui
from UIControl import MainWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    # 捕获所有异常并打印消息
    try:
        mp = MainWindow.Ui_MainWindow()
        mp.show()
    except Exception, e:
        print e.message
    sys.exit(app.exec_())

else:
    pass
