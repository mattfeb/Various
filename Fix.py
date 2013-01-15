import sys
import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *

class Fix(QtGui.QWidget):

    def __init__(self):
        super(Fix, self).__init__()
        self.count = 1
        self.initUI()
        self.recentFileListLocation = ""

    def initUI(self):
        #Labels
        title = QtGui.QLabel("Title")
        episode = QtGui.QLabel("Episode")
        status = QtGui.QLabel("Status: ")

        #Line Edits
        self.titleEdit = QtGui.QLineEdit()
        self.episodeEdit = QtGui.QLineEdit()

        #Buttons
        addButton = QtGui.QPushButton("+")
        fixButton = QtGui.QPushButton("Fix")
        clearButton = QtGui.QPushButton("Clear")

        self.recentList = QtGui.QListWidget()
        
        listGroupBox = QtGui.QGroupBox()
        listGroupBox.setTitle("Recent/Saved Titles")

        #Layouts
        self.fileVBox = QtGui.QVBoxLayout()
        self.fileVBox.addWidget(fileAdder(self.count))


        grid = QtGui.QGridLayout()
        grid.addWidget(title, 1, 1)
        grid.addWidget(self.titleEdit, 1, 2)
        grid.addWidget(episode, 2, 1)
        grid.addWidget(self.episodeEdit, 2, 2)

        self.buttonHBox = QtGui.QHBoxLayout()
        self.buttonHBox.setSpacing(1)
        self.buttonHBox.addWidget(fixButton)
        self.buttonHBox.addWidget(clearButton)

        listHBox = QtGui.QHBoxLayout()
        listHBox.addWidget(self.recentList)

        listGroupBox.setLayout(listHBox)

        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(addButton, 0, QtCore.Qt.AlignLeft)
        self.vbox.addLayout(self.fileVBox)
        self.vbox.addLayout(grid)
        self.vbox.addLayout(self.buttonHBox)
        self.vbox.addWidget(fixButton, 0, QtCore.Qt.AlignCenter)
        self.vbox.addWidget(listGroupBox)
        self.vbox.addWidget(status)

        QtCore.QObject.connect(fixButton, QtCore.SIGNAL('clicked()'), self.fixFile)
        QtCore.QObject.connect(addButton, QtCore.SIGNAL('clicked()'), self.addFileEntry)
        QtCore.QObject.connect(clearButton, QtCore.SIGNAL('clicked()'), self.clearInput)

        self.fillRecentList()

        #Window
        self.setLayout(self.vbox)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Fix")
        self.show()

    def fixFile(self):
        items = (self.fileVBox.itemAt(i) for i in range(self.fileVBox.count()))
        for w in items:
            #w.widget().close()
            print(w.widget().selectedFile)
        #for i in range(self.fileVBox.count()):
        #    print(i)
        #    self.fileVBox.itemAt(i).widget().children().selectedFile

    def addFileEntry(self):
        self.count += 1
        f1 = fileAdder(self.count)
        self.fileVBox.addWidget(f1)

    def clearInput(self):
        self.titleEdit.setText("")
        self.episodeEdit.setText("")

    def fillRecentList(self):
        recentFiles = []#open("").readlines()

        for i in range(len(recentFiles)):
            if recentFiles[i] != "":
                print(recentFiles[i])
                self.recentList.addItem(recentFiles[i])


class fileAdder(QtGui.QWidget):

    def __init__(self, count):
        super(fileAdder, self).__init__()
        self.count = count 
        self.selectedFile = ""
        self.initUI()

    def initUI(self):
        self.n = QtGui.QLabel(str(self.count) + ".")
        self.filename = QtGui.QLabel("Filename")
        self.filenameEdit = QtGui.QLineEdit()
        self.browseButton = QtGui.QPushButton("browse...")

        QtCore.QObject.connect(self.browseButton, QtCore.SIGNAL('clicked()'), self.browse)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.n)
        hbox.addWidget(self.filename)
        hbox.addWidget(self.filenameEdit)
        hbox.addWidget(self.browseButton)
        self.setLayout(hbox)

    def browse(self):
        self.selectedFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        self.filenameEdit.setText(self.selectedFile)

def main():
    
    app = QtGui.QApplication(sys.argv)
    f = Fix()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
