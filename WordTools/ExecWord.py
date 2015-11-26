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
        self.bFirstFindStr = False

    def findString(self, findstr):
        # self.word.Selection.Find.Wrap = 1
        boo_res = self.word.Selection.Find.Execute(findstr)
        # print self.word.Selection.Find.Text
        return boo_res

    def openWordFile(self, wordPath=None):
        # print wordPath
        self.word = Dispatch('word.application')
        self.word.Visible = 1
        self.word.Documents.Open(wordPath)

    def Exec(self, findstr):

        # 查找之前首先进行搜索结果列表清理
        self.delegate.treeWidget.clear()
        try:
            for path, dirs, files in os.walk(self.filePath):
                self.bFirstFindStr = True
                for filename in files:
                    if not (fnmatch.fnmatch(filename, '*.docx') or fnmatch.fnmatch(filename, '*.doc')):
                        continue
                    doc = os.path.abspath(os.path.join(path, filename))
                    # print 'processing %s...' % doc
                    if type(doc).__name__ == 'str':
                        doc = doc.decode('GBK')
                    # 状态栏显示相应进度
                    self.delegate.statusBar().showMessage(doc)
                    # print doc
                    self.word.Documents.Open(doc)
                    # docastext = doc[:-4] + 'txt'
                    # self.word.ActiveDocument.SaveAs(docastext, FileFormat=constants.wdFormatText)
                    # print findstr
                    if self.findString(findstr):
                        # print u'找到了'
                        if self.bFirstFindStr:
                            item = QtGui.QTreeWidgetItem(self.delegate.treeWidget)
                            item.setText(0, path)
                            self.bFirstFindStr = False
                        parameterItem = QtGui.QTreeWidgetItem(item)
                        if type(filename).__name__ == 'str':
                            filenameshow = filename.decode('gbk')
                        parameterItem.setText(0, filenameshow)
                    self.word.ActiveDocument.Close()
        finally:
            # self.word.Quit()
            self.delegate.statusBar().showMessage(u'搜索完毕')
            # 更新搜索记录
            self.delegate.configini.RecordHistoryList()
            print u'搜索完毕'

