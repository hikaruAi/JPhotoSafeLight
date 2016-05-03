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
        #self.useNumpy.stateChanged.connect(self.OnUseNumpyChanged)
        self.actionExport_Filter.triggered.connect(self.On_Menu_ExportFilter)
        self.actionSave_Image.triggered.connect(self.On_Menu_SaveImage)

    def On_Menu_SaveImage(self):
        ext=self.workingImage.split(".")[-1]
        f=QtWidgets.QFileDialog.getSaveFileName(self,"Export Image",self.browseLocation,"Image (*."+ext+")",None)[0]
        self.On_Menu_ExportFilter(self.tempDirectory+"_temp_.py")
        sf=open(self.tempDirectory+"_temp_.py")
        s=sf.read()
        sf.close()
        s=s.replace("    if len(sys.argv)>1:","")
        s=s.replace("        execute","    execute")
        s=s.replace("else","#else")
        s=s.replace("sys.argv[1]","'"+self.file+"'")
        s=s.replace("image.save(file)","image.save('"+f+"')")
        c=compile(s,"<string>","exec")
        exec(c)

    def On_Menu_ExportFilter(self,optionalFile=None):
        if optionalFile == None:
            f=QtWidgets.QFileDialog.getSaveFileName(self,"Export Filter",self.browseLocation,"Python File (*.py *.pyw)",None)[0]
        else:
            f=optionalFile
        s="#Your code here"
        for l in self.listOfCommands:
            s=s+"       "+l+"\n"
        fh=open(f,"wt")
        ns=self.opsString.replace("#command#",s)
        ns=ns.replace("#IMAGEPATH#",'sys.argv[1]')
        ns=ns.replace("#sys#","import sys")
        ns=ns.replace("#if","if")
        ns=ns.replace("#else","else")
        ns=ns.replace("#TAB#","    ")
        fh.write(ns)
        fh.close()

    def ExecuteLastCommand(self):
        initTime=time.time()
        f=self.opsString
        f=f.replace("#IMAGEPATH#","'"+self.workingImage+"'")
        f=f.replace("#command#",self.listOfCommands[-1])
        f=f.replace("def execute(fileName):","")
        f=f.replace("#TAB#","")
        f=f.replace("fileName","'"+self.workingImage+"'")
        f=f.replace("if __name__","#if __name__")
        f=f.replace("execute","#execute")
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

