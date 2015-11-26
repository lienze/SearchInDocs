__author__ = 'lienze'
# coding=utf-8
from win32com.client import Dispatch, constants
import os
import fnmatch


class ExecWord:
    def __init__(self, filePath=None):
        self.word = Dispatch('word.application')
        self.word.DisplayAlerts = 0
        self.word.Visible = 0
        self.filePath = filePath

    def findString(self, findstr):
        print findstr
        # self.word.Selection.Find.Wrap = 1
        boo_res = self.word.Selection.Find.Execute(findstr)
        # print self.word.Selection.Find.Text
        return boo_res

    def Exec(self, findstr):
        try:
            for path, dirs, files in os.walk(self.filePath):
                for filename in files:
                    if not (fnmatch.fnmatch(filename, '*.docx') or fnmatch.fnmatch(filename, '*.doc')):
                        continue
                    doc = os.path.abspath(os.path.join(path,filename))
                    print 'processing %s...' % doc
                    self.word.Documents.Open(doc)
                    # docastext = doc[:-4] + 'txt'
                    # self.word.ActiveDocument.SaveAs(docastext, FileFormat=constants.wdFormatText)
                    if self.findString(findstr):
                        print u'找到了'
                    self.word.ActiveDocument.Close()
        finally:
            self.word.Quit()
            print 'end'

