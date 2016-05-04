# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/self.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setObjectName("MainWindow")
        self.resize(741, 365)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(900, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.mainImage = QtWidgets.QLabel(self.centralwidget)
        self.mainImage.setGeometry(QtCore.QRect(10, 10, 291, 291))
        self.mainImage.setText("")
        self.mainImage.setPixmap(QtGui.QPixmap(":/images/DefaultImage.jpg"))
        self.mainImage.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.mainImage.setObjectName("mainImage")
        self.comandText = QtWidgets.QTextEdit(self.centralwidget)
        self.comandText.setGeometry(QtCore.QRect(310, 40, 411, 251))
        self.comandText.setFrameShadow(QtWidgets.QFrame.Raised)
        self.comandText.setLineWidth(0)
        self.comandText.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.comandText.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.comandText.setObjectName("comandText")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionLoad_Image = QtWidgets.QAction(self)
        self.actionLoad_Image.setObjectName("actionLoad_Image")
        self.actionSave_Image = QtWidgets.QAction(self)
        self.actionSave_Image.setObjectName("actionSave_Image")
        self.actionExport_Filter = QtWidgets.QAction(self)
        self.actionExport_Filter.setObjectName("actionExport_Filter")
        self.actionCredits = QtWidgets.QAction(self)
        self.actionCredits.setObjectName("actionCredits")
        self.actionUndo = QtWidgets.QAction(self)
        self.actionUndo.setPriority(QtWidgets.QAction.HighPriority)
        self.actionUndo.setObjectName("actionUndo")
        self.menuFile.addAction(self.actionLoad_Image)
        self.menuFile.addAction(self.actionSave_Image)
        self.menuFile.addAction(self.actionExport_Filter)
        self.menuFile.addAction(self.actionUndo)
        self.menubar.addAction(self.menuFile.menuAction())

        
        QtCore.QMetaObject.connectSlotsByName(self)

   
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "J PhotoSafeLight - $fileName$"))
        self.comandText.setToolTip(_translate("MainWindow", "Writr your commands"))
        self.comandText.setWhatsThis(_translate("MainWindow", "Write your commands here and press  ENTER"))
        self.comandText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_Image.setText(_translate("MainWindow", "Load Image"))
        self.actionLoad_Image.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionSave_Image.setText(_translate("MainWindow", "Save Image"))
        self.actionSave_Image.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExport_Filter.setText(_translate("MainWindow", "Export Filter"))
        self.actionExport_Filter.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))

import resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(self)
    self.show()
    sys.exit(app.exec_())

