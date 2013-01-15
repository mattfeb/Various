import sys
import os
import random  
from PyQt4 import QtGui, QtCore 
from PyQt4.QtCore import *

validFileTypes = ["avi", "mkv", "mp4"]

class RandUI(QtGui.QWidget):

    def __init__(self):
        super(RandUI, self).__init__()
        self.initUI()
        self.fName = ""
        self.defaultDirectory = "C:/"

    def initUI(self):
        self.selectedPath = QtGui.QLabel()
        watchButton = QtGui.QPushButton("Watch")
        openButton = QtGui.QPushButton("Open...")
        pathInput = QtGui.QLineEdit()

        QtCore.QObject.connect(openButton, QtCore.SIGNAL('clicked()'), self.showOpenDialog)
        QtCore.QObject.connect(watchButton, QtCore.SIGNAL('clicked()'), self.watch)

        grid = QtGui.QGridLayout()
        grid.addWidget(openButton, 1, 1, 2, 1, QtCore.Qt.AlignCenter)
        grid.addWidget(watchButton, 3, 1, 1, 1, QtCore.Qt.AlignCenter)
        grid.addWidget(self.selectedPath, 4, 1)
        
        self.setLayout(grid)
        self.setGeometry(200, 200, 250, 200) 
        self.setWindowTitle("Watch Random File")
        self.show()

    def showOpenDialog(self):
        self.fName = QtGui.QFileDialog.getExistingDirectory(self, 'Open Directory', self.defaultDirectory)
        self.selectedPath.setText("Selected: " + self.fName)

    def watch(self):
        if self.fName == "":
            self.selectedPath.setText("No Directory Selected.")
            return
        rand = RandEpisode(self.fName)
        os.startfile(rand.getFile(self.fName))


class RandEpisode:

    def __init__(self, path):
        self.path = path

    def isMediaFile(self, fileName):
        fileType = ""

        #Check if its a folder
        if os.path.exists(fileName + "/"):
           return False

        try:
            fileType = fileName[fileName.rindex(".")+1:len(fileName)]
        except:
            return False

        #Check the extension to see if it's a media file as defined in validFileTypes
        for i in range(len(validFileTypes)):
            if fileType == validFileTypes[i]:
                return True
        return False

    #Get the file path, by randomly selecting a folder recursively 
    def getFile(self, path):
        print(path)
        if self.isMediaFile(path):
            return path
        else:
            dirList = os.listdir(path)
            n = random.randrange(len(dirList))
            return self.getFile(path + "/" + dirList[n])

def main():
    app = QtGui.QApplication(sys.argv)
    ex = RandUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

