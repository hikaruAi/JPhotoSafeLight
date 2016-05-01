###Main Script####

import sys
from MainWindow import *
import os, shutil
from PIL import Image

class PhotoSafeLight(MainWindow):
    def __init__(self):
        MainWindow.__init__(self)
        self.browseLocation=QtCore.QStandardPaths.standardLocations(6)[0]
        self.tempDirectory=QtCore.QStandardPaths.standardLocations(7)[0]
        self.file=""
        self.workingImage=""
        self.lastWorkingImage=""
        self.PIL_image=None
        self.listOfCommands=[""]
        self.currentLineText=""
        self.moreSetup()
        self.show()

    def moreSetup(self):
        self.setTitle()
        self.setEventsHandlers()
        p=QtGui.QPixmap(":/images/emptyImage.png")
        p_scaled= p.scaled(self.mainImage.size(), QtCore.Qt.KeepAspectRatio,1)
        self.mainImage.setPixmap(p_scaled)
        self.comandText.insertPlainText(">>")

    def setTitle(self):
        s="J PhotoSafeLight - $fileName$"
        s=s.replace("$fileName$",self.file)
        self.setWindowTitle(s)

    def setEventsHandlers(self):
        ###MENU####
        self.actionLoad_Image.triggered.connect(self.On_Menu_LoadImage)
        self.comandText.textChanged.connect(self.CommandTextTextChanged)

    def CommandTextTextChanged(self):
        if self.comandText.toPlainText()[-1]==">":
            return
        currentText=self.comandText.toPlainText().replace(">>","")
        #print("Changed text:",currentText.replace("\n","#END#"))
        if (len(currentText)>0 and currentText[-1]=="\n"):
            currentCommand=currentText.split("\n")[-2]
            if currentCommand!="":
                self.listOfCommands.append(currentCommand)
                print("Current command", currentCommand)
            self.comandText.insertPlainText(">>")

    def SetInitialTempFiles(self):
        self.workingImage=self.tempDirectory+"WK_"+os.path.basename(self.file)
        self.lastWorkingImage=self.tempDirectory+"LWK_"+os.path.basename(self.file)
        shutil.copy2(self.file,self.workingImage)
        shutil.copy2(self.file,self.lastWorkingImage)
        print(self.workingImage)
        print(self.lastWorkingImage)

    def RefreshMainImageFromTemp(self):
        p=QtGui.QPixmap(self.workingImage)
        p_scaled= p.scaled(self.mainImage.size(), QtCore.Qt.KeepAspectRatio,1)
        self.mainImage.setPixmap(p_scaled)

    def LoadImageFromTempToPIL(self):
        self.PIL_image=Image.open(self.workingImage)
        print(self.PIL_image.format,"Size: ",self.PIL_image.size)

    def On_Menu_LoadImage(self):
        print("Load Image menu pressed")
        self.file = QtWidgets.QFileDialog.getOpenFileName(self,"Load Image",self.browseLocation,"Image Files (*.png *.jpg *.bmp)",None)[0]
        print("Selected:",self.file)
        self.browseLocation= os.path.dirname(self.file)
        print("Browse location: ",self.browseLocation)
        self.SetInitialTempFiles()
        self.RefreshMainImageFromTemp()
        self.LoadImageFromTempToPIL()

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=PhotoSafeLight()
    sys.exit(app.exec_())

