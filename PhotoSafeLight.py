#lint:disable
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
        if debug:
            self.file="DefaultImage.jpg"
            self.SetInitialTempFiles()
            self.LoadImageFromTempToPIL()
            self.RefreshMainImageFromTemp()
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

    def ExecuteLastCommand(self):
        initTime=time.time()
        image=self.PIL_image
        width=image.width
        height=image.height
        center_x=int(width/2)
        center_y=int(height/2)
        center=(center_x,center_y)
        listData=list(image.getdata())
        command, mode =self.getCommandMode()
        #command=command.replace("g","locals()['g']")
        print("Command:",command)
        commandAsFunc=eval("lambda: "+command)
        for i in range(len(listData)):
            px = i % ( width )
            py = math.trunc( i / width)
            x=px/width
            y=py/height
            pixel=listData[i]
            r=pixel[0]
            g=pixel[1]
            b=pixel[2]
            distance_center=sqrt(((px-center_x)**2)+((py-center_y)**2))
            if mode==CommandMode.red:
                r=int(commandAsFunc())
            elif mode==CommandMode.green:
                g=int(commandAsFunc())
            elif mode==CommandMode.blue:
                b=int(commandAsFunc())
            elif mode==CommandMode.pixel:
                pixel=eval(commandAsFunc())
            elif mode==CommandMode.none:
               break
            #r=int((r+g+b)/3)

            if mode==CommandMode.pixel:
                listData[i]=pixel
            else:
                listData[i]=(r,g,b)
        image.putdata(listData)
        image.save(self.workingImage)
        self.RefreshMainImageFromTemp()
        self.LoadImageFromTempToPIL()
        print("Execute command time:", time.time()-initTime)

    def getCommandMode(self):
        command=self.listOfCommands[-1]
        mode=CommandMode.none

        if "r=" in command:
                command=command.replace("r=","")
                mode=CommandMode.red
        elif "r =" in command:
            command=command.replace("r =","")
            mode=CommandMode.red

        elif "g=" in command:
            command=command.replace("g=","")
            mode=CommandMode.green
        elif "g =" in command:
            command=command.replace("g =","")
            mode=CommandMode.green

        elif "b=" in command:
            command=command.replace("b=","")
            mode=CommandMode.green
        elif "b =" in command:
            command=command.replace("b =","")
            mode=CommandMode.green

        elif "pixel=" in command:
            command=command.replace("pixel=","")
            mode=CommandMode.green
        elif "pixel =" in command:
            command=command.replace("pixel =","")
            mode=CommandMode.pixel
        return command, mode

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

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=PhotoSafeLight()
    sys.exit(app.exec_())

#lint:enable
