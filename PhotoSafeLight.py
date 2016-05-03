###Main Script####

import sys
from MainWindow import *
import os, shutil
from PIL import Image
import PIL
import colorsys, math
from enum import Enum
from math import *
import time

useNumpy=False
if useNumpy:
    processFile="op_numpy.py"
else:
    processFile="op.py"
debug=True

class CommandMode(Enum):
    none=0
    red=1
    green=2
    pixel=3

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
        f=open(processFile)
        self.opsString=f.read()
        f.close()
        if debug:
            self.file="DefaultImage.jpg"
            self.SetInitialTempFiles()
            self.LoadImageFromTempToPIL()
            self.RefreshMainImageFromTemp()
            self.setTitle()
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
        self.useNumpy.stateChanged.connect(self.OnUseNumpyChanged)

    def OnUseNumpyChanged(self,v):
        useNumpy=self.useNumpy.isChecked()
        if useNumpy:
            processFile="op_numpy.py"
        else:
            processFile="op.py"
        f=open(processFile)
        self.opsString=f.read()
        f.close()
        #print(self.opsString)
    def ExecuteLastCommand(self):
        initTime=time.time()
        f=self.opsString
        f=f.replace("#IMAGEPATH#",self.workingImage)
        f=f.replace("#command#",self.listOfCommands[-1])
        c=compile(f,"<string>","exec")
        exec(c)
        self.RefreshMainImageFromTemp()
        self.LoadImageFromTempToPIL()
        print("Execute command time:", time.time()-initTime)
    def CommandTextTextChanged(self):
        if self.comandText.toPlainText()[-1]==">":
            return
        currentText=self.comandText.toPlainText().replace(">>","")
        #print("Changed text:",currentText.replace("\n","#END#"))
        if (len(currentText)>0 and currentText[-1]=="\n"):
            currentCommand=currentText.split("\n")[-2]
            if currentCommand!="":
                self.listOfCommands.append(currentCommand)
                print(currentCommand)
                self.comandText.insertPlainText(">>")
                self.ExecuteLastCommand()

    def addColor(self,text,color):
        return "<color="+color+">"+text+"<color>"

    def SetInitialTempFiles(self):
        self.workingImage=self.tempDirectory+"WK_PhotoSafeLight."+self.file.split(".")[-1]
        self.lastWorkingImage=self.tempDirectory+"LWK_PhotoSafeLight."+self.file.split(".")[-1]
        shutil.copy2(self.file,self.workingImage)

        image=Image.open(self.workingImage)
        initSize=image.size
        labelSize=(self.mainImage.size().width(),self.mainImage.size().height())
        if initSize[0]>initSize[1]:
            factor=labelSize[0]/initSize[0]
        else:
            factor=labelSize[1]/initSize[1]
        finalSize=(int(initSize[0]*factor),int(initSize[1]*factor))
        print("Scale:",factor, "Final size:",finalSize)
        image=image.resize(finalSize,PIL.Image.LANCZOS)
        image.save(self.workingImage)
        shutil.copy2(self.workingImage,self.lastWorkingImage)
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
        self.setTitle()

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=PhotoSafeLight()
    sys.exit(app.exec_())

#lint:enable
