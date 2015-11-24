__author__ = 'lienze'
# coding=utf-8
import sys
from PyQt4 import QtGui, QtCore


class MainPanel(QtGui.QWidget):
    def __init__(self, parent=None):
        # 初始化主界面
        QtGui.QWidget.__init__(self, parent)
        # widget = QtGui.QWidget()
        # widget.resize(250, 150)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('simple')
        # 主界面放置于屏幕中间
        self.center()
        # 增加关闭按钮
        button_Quit = QtGui.QPushButton('Closed', self)
        button_Quit.setGeometry(10, 10, 60, 30)
        button_Quit.setToolTip('Clicked the button')
        button_Quit.show()  # 默认就是显示的，对应的是hide()方法
        self.connect(button_Quit,
                     QtCore.SIGNAL('clicked()'),
                     QtGui.qApp,
                     QtCore.SLOT('quit()'))
        #

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self,
                                           'Message',
                                           'Are you sure to quit?',
                                           QtGui.QMessageBox.Yes,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2,
                  (screen.height() - size.height())/2)