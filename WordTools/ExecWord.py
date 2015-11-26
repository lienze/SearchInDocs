__author__ = 'lienze'
# coding=utf-8
from win32com.client import Dispatch, constants
import os
import fnmatch
from PyQt4 import QtCore, QtGui


class ExecWord:
    def __init__(self, filePath=None):
        self.word = Dispatch('word.application')
        self.word.DisplayAlerts = 0
        self.word.Visible = 0
        self.filePath = filePath
        self.delegate = None

    def findString(self, findstr):
        # self.word.Selection.Find.Wrap = 1
        boo_res = self.word.Selection.Find.Execute(findstr)
        # print self.word.Selection.Find.Text
        return boo_res

    def Exec(self, findstr):

        # 查找之前首先进行搜索结果列表清理
        self.delegate.treeWidget.clear()
        try:
            for path, dirs, files in os.walk(self.filePath):
                for filename in files:
                    if not (fnmatch.fnmatch(filename, '*.docx') or fnmatch.fnmatch(filename, '*.doc')):
                        continue
                    doc = os.path.abspath(os.path.join(path, filename))
                    # 状态栏显示相应进度
                    self.delegate.statusBar().showMessage(doc)
                    # print 'processing %s...' % doc
                    self.word.Documents.Open(doc)
                    # docastext = doc[:-4] + 'txt'
                    # self.word.ActiveDocument.SaveAs(docastext, FileFormat=constants.wdFormatText)
                    if self.findString(findstr):
                        # print u'找到了'
                        item = QtGui.QTreeWidgetItem(self.delegate.treeWidget)
                        item.setText(0, doc)
                        parameterItem = QtGui.QTreeWidgetItem(item)
                        parameterItem.setText(0, "Parameter")
                    self.word.ActiveDocument.Close()
        finally:
            self.word.Quit()
            print 'end'

