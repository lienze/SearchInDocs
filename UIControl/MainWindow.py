__author__ = 'lienze'
# coding=utf-8
import sys
from PyQt4 import QtGui, QtCore


class MainPanel(QtGui.QMainWindow):
    def __init__(self, parent=None):
        # 初始化主界面
        QtGui.QMainWindow.__init__(self, parent)
        # widget = QtGui.QWidget()
        # widget.resize(250, 150)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('simple')
        # 主界面放置于屏幕中间
        self.center()
        # 初始化菜单栏
        menu_file_exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'),
                                  'Exit',
                                  self)
        menu_file_exit.setShortcut('Ctrl+Q')
        menu_file_exit.setStatusTip('Exit application')
        menu_file_exit.connect(menu_file_exit,
                               QtCore.SIGNAL('triggered()'),
                               QtGui.qApp,
                               QtCore.SLOT('quit()'))
        self.statusBar()
        menubar = self.menuBar()
        menu_file = menubar.addMenu('&File')
        menu_file.addAction(menu_file_exit)
        # 初始化状态栏
        self.statusBar().showMessage('Ready')
        # 增加关闭按钮
        '''button_Quit = QtGui.QPushButton('Closed', self)
        button_Quit.setGeometry(10, 10, 60, 30)
        button_Quit.setToolTip('Clicked the button')
        button_Quit.show()  # 默认就是显示的，对应的是hide()方法
        self.connect(button_Quit,
                     QtCore.SIGNAL('clicked()'),
                     QtGui.qApp,
                     QtCore.SLOT('quit()'))'''

    def closeEvent(self, event):
        # 这是重写的关闭按钮的函数
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
        # 调整位置
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2,
                  (screen.height() - size.height())/2)
