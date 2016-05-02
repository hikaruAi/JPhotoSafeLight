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
        self.resize(900, 381)
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
        self.mainImage.setGeometry(QtCore.QRect(10, 10, 431, 331))
        self.mainImage.setText("")
        self.mainImage.setPixmap(QtGui.QPixmap(":/images/emptyImage.png"))
        self.mainImage.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.mainImage.setObjectName("mainImage")
        self.comandText = QtWidgets.QTextEdit(self.centralwidget)
        self.comandText.setGeometry(QtCore.QRect(480, 60, 411, 281))
        self.comandText.setObjectName("comandText")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
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
        self.menuFile.addAction(self.actionLoad_Image)
        self.menuFile.addAction(self.actionSave_Image)
        self.menuFile.addAction(self.actionExport_Filter)
        self.menuAbout.addAction(self.actionCredits)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        
        QtCore.QMetaObject.connectSlotsByName(self)

   
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "J PhotoSafeLight - $fileName$"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionLoad_Image.setText(_translate("MainWindow", "Load Image"))
        self.actionLoad_Image.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionSave_Image.setText(_translate("MainWindow", "Save Image"))
        self.actionExport_Filter.setText(_translate("MainWindow", "Export Filter"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))

import resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(self)
    self.show()
    sys.exit(app.exec_())

