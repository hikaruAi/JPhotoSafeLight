####Build Resources

import os

if __name__=="__main__":
    os.system("pyrcc5 Resources/resources.qrc -o resources.py")
    os.system("pyuic5 UI/MainWindow.ui -o MainWindow.py -x")
    rf=open("MainWindow.py","rt")
    rs=rf.read().replace("resources_rc","resources")
    rs=rs.replace("(object)","(QtWidgets.QMainWindow)")
    rs=rs.replace("def setupUi","def __init__")
    #rs=rs.replace(,"QtWidgets.QMainWindow.__init__(self)")
    rs=rs.replace("MainWindow.","self.")
    rs=rs.replace(", MainWindow):","):")
    rs=rs.replace(" def retranslateUi(self):","")
    rs=rs.replace("Ui_MainWindow","MainWindow")
    rs=rs.replace("def __init__(self):","def __init__(self):\n        QtWidgets.QMainWindow.__init__(self)")
    rs=rs.replace("(MainWindow)","(self)")
    rs=rs.replace("self.retranslateUi(self)","")
    rf.close()
    rf=open("MainWindow.py","wt")
    rf.write(rs)
    rf.close()
    print ("Build resources succesfull!!")