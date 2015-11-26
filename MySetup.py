from distutils.core import setup
import glob
import py2exe

py2exe_options = {
    "includes":["sip"],
    "packages":['PyQt4.QtGui','PyQt4.QtCore'],
    "bundle_files":1,
    "compressed":1,
}

setup(
    name='SearchInDocs',
    version='0.0.1',
    windows=["SearchInDocs.py"],
    options={'py2exe':py2exe_options},
    zipfile=None,
)
