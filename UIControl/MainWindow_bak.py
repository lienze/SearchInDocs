__author__ = 'lienze'
# -*- coding: utf-8-*-
import sys
from PyQt4 import QtGui, QtCore


class MainPanel(QtGui.QMainWindow):
    def __init__(self, parent=None):
        # 初始化主界面
        QtGui.QMainWindow.__init__(self, parent)
        # widget = QtGui.QWidget()
        # widget.resize(250, 150)
        self.setGeometry(300, 300, 550, 300)
        self.setWindowTitle('SearchInDocs')
        # 主界面放置于屏幕中间
        self.center()
        # 初始化菜单栏
        # 初始化菜单栏 1.About按钮
        menu_file_about = QtGui.QAction(QtGui.QIcon('icons/exit.png'),
                                  'About',
                                  self)
        menu_file_about.setShortcut('Ctrl+A')
        menu_file_about.setStatusTip('About application')
        menu_file_about.connect(menu_file_about,
                               QtCore.SIGNAL('triggered()'),
                               QtGui.qApp,
                               QtCore.SLOT('quit()'))
        # 初始化菜单栏 2.Exit按钮
        menu_file_exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'),
                                  'Exit',
                                  self)
        menu_file_exit.setShortcut('Ctrl+Q')
        menu_file_exit.setStatusTip('Exit application')
        menu_file_exit.connect(menu_file_exit,
                               QtCore.SIGNAL('triggered()'),
                               QtGui.qApp,
                               QtCore.SLOT('quit()'))

        # self.statusBar()
        menubar = self.menuBar()
        menu_file = menubar.addMenu('&File')
        menu_file.addAction(menu_file_about)
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

        # 组件初始化
        Label_Addr = QtGui.QLabel(u"路径:")
        LineEdit_Addr = QtGui.QLineEdit()
        Button_OK = QtGui.QPushButton('OK')

        Label_Test = QtGui.QLabel(u'测试')

        # 初始化布局管理器
        mainWidget = QtGui.QWidget()
        self.setCentralWidget(mainWidget)

        '''hbox = QtGui.QHBoxLayout()
        # hbox.addStretch(1)
        hbox.addWidget(ok)
        hbox.addWidget(cancel)

        vbox = QtGui.QVBoxLayout()
        # vbox.addStretch(1)
        vbox.addLayout(hbox)
        mainWidget.setLayout(vbox)'''

        hbox_top = QtGui.QHBoxLayout()
        hbox_top.addWidget(Label_Addr)
        hbox_top.addWidget(LineEdit_Addr)
        hbox_top.addWidget(Button_OK)

        hbox_buttom = QtGui.QHBoxLayout()
        hbox_buttom.addWidget(Label_Test)

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox_top)
        # vbox.addStretch(1)
        vbox.addLayout(hbox_buttom)
        mainWidget.setLayout(vbox)

        '''label1 = QtGui.QLabel(self.tr("用户名:"))
        label2 = QtGui.QLabel(self.tr("姓名："))
        label3 = QtGui.QLabel(self.tr("性别:"))
        label4 = QtGui.QLabel(self.tr("部门:"))
        label5 = QtGui.QLabel(self.tr("年龄:"))
        otherLabel = QtGui.QLabel(self.tr("备注:"))
        otherLabel.setFrameStyle(QtGui.QFrame.Panel|QtGui.QFrame.Sunken)
        userLineEdit = QtGui.QLineEdit()
        nameLineEdit = QtGui.QLineEdit()
        sexComboBox = QtGui.QComboBox()
        sexComboBox.insertItem(0, self.tr("男"))
        sexComboBox.insertItem(1, self.tr("女"))
        departmentTextEdit = QtGui.QTextEdit()
        ageLineEdit = QtGui.QLineEdit()

        labelCol = 0
        contentCol = 1

        leftLayout = QtGui.QGridLayout()
        leftLayout.addWidget(label1, 0, labelCol)
        leftLayout.addWidget(userLineEdit, 0, contentCol)
        leftLayout.addWidget(label2, 1, labelCol)
        leftLayout.addWidget(nameLineEdit, 1, contentCol)
        leftLayout.addWidget(label3, 2, labelCol)
        leftLayout.addWidget(sexComboBox, 2, contentCol)
        leftLayout.addWidget(label4, 3, labelCol)
        leftLayout.addWidget(departmentTextEdit, 3, contentCol)
        leftLayout.addWidget(label5, 4, labelCol)
        leftLayout.addWidget(ageLineEdit, 4, contentCol)
        leftLayout.addWidget(otherLabel, 5, labelCol, 1, 2)
        leftLayout.setColumnStretch(0, 1)
        leftLayout.setColumnStretch(1, 3)

        label6 = QtGui.QLabel(self.tr("头像:"))
        iconLabel = QtGui.QLabel()
        icon = QtGui.QPixmap("image/2.jpg")
        iconLabel.setPixmap(icon)
        iconLabel.resize(icon.width(), icon.height())
        iconPushButton = QtGui.QPushButton(self.tr("改变"))
        hLayout = QtGui.QHBoxLayout()
        hLayout.setSpacing(20)
        hLayout.addWidget(label6)
        hLayout.addWidget(iconLabel)
        hLayout.addWidget(iconPushButton)

        label7 = QtGui.QLabel(self.tr("个人说明:"))
        descTextEdit = QtGui.QTextEdit()

        rightLayout = QtGui.QVBoxLayout()
        rightLayout.setMargin(10)
        rightLayout.addLayout(hLayout)
        rightLayout.addWidget(label7)
        rightLayout.addWidget(descTextEdit)

        OKPushButton = QtGui.QPushButton(self.tr("确定"))
        cancelPushButton = QtGui.QPushButton(self.tr("取消"))
        bottomLayout = QtGui.QHBoxLayout()
        bottomLayout.addStretch()
        bottomLayout.addWidget(OKPushButton)
        bottomLayout.addWidget(cancelPushButton)

        mainLayout = QtGui.QGridLayout(self)
        mainLayout.setMargin(15)
        mainLayout.setSpacing(10)
        mainLayout.addLayout(leftLayout, 0, 0)
        mainLayout.addLayout(rightLayout, 0, 1)
        mainLayout.addLayout(bottomLayout, 1, 0, 1, 2)
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)'''

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
