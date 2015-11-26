# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPanel.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from WordTools import ExecWord

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        # super(Ui_MainWindow, self).__init__()
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi(self)
        # aftersetupUi()函数补充设置Qt Designer无法实现的内容
        self.aftersetupUi()

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

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Enter or e.key() == QtCore.Qt.Key_Return:
            # 点击回车按键开始进行文档的搜索
            if self.comboBox.currentText():
                self.word = ExecWord.ExecWord(self.comboBox.currentText())
                if self.comboBox_2.currentText():
                    self.word.Exec(self.comboBox_2.currentText())
                else:
                    # 提示输入搜索内容
                    QtGui.QMessageBox.question(self,
                                               u'提示',
                                               u'请输入目录',
                                               QtGui.QMessageBox.Ok)
            else:
                # 提示输入搜索内容
                QtGui.QMessageBox.question(self,
                                           u'提示',
                                           u'请输入搜索内容',
                                           QtGui.QMessageBox.Ok)

    @QtCore.pyqtSlot()
    def OpenDirectory(self):
        options = QtGui.QFileDialog.DontResolveSymlinks | QtGui.QFileDialog.ShowDirsOnly
        directory = QtGui.QFileDialog.getExistingDirectory(self,
                "QFileDialog.getExistingDirectory()",
                self.comboBox_2.currentText(), options)
        if directory:
            self.comboBox_2.setText(directory)

    def aftersetupUi(self):
        # 手动补充设置
        # comboBox设置(暂时)
        self.comboBox.addItem('abc')
        self.comboBox_2.addItem('C:\\testDocs')
        # button2按钮映射处理
        self.connect(self.pushButton_2,
                     QtCore.SIGNAL('clicked()'),
                     self,
                     QtCore.SLOT('OpenDirectory()'))

        # 清理treeWidget
        self.treeWidget.clear()
        # 接下来开始初始化treeWidget的各项数据
        item = QtGui.QTreeWidgetItem(self.treeWidget)
        item.setText(0, u'这个地方放地址')
        parameterItem = QtGui.QTreeWidgetItem(item)
        parameterItem.setText(0, "Parameter")


    # 以下是通过Qt Designer自动生成的代码
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(701, 506)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 681, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(30, 30))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 681, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setMaximumSize(QtCore.QSize(30, 30))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtGui.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 100, 681, 371))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SearchInDocs", None))
        self.label.setText(_translate("MainWindow", "搜索:", None))
        self.pushButton.setText(_translate("MainWindow", "...", None))
        self.label_2.setText(_translate("MainWindow", "路径:", None))
        self.pushButton_2.setText(_translate("MainWindow", "...", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "搜索结果", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
