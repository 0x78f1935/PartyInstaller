# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headerFrame = QtWidgets.QFrame(self.centralwidget)
        self.headerFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.headerFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.Info = QtWidgets.QLabel(self.headerFrame)
        self.Info.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Info.setFont(font)
        self.Info.setAlignment(QtCore.Qt.AlignCenter)
        self.Info.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Info.setObjectName("Info")
        self.gridLayout.addWidget(self.Info, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.headerFrame)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ContentView = QtWidgets.QScrollArea(self.centralwidget)
        self.ContentView.setWidgetResizable(True)
        self.ContentView.setObjectName("ContentView")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 618, 358))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.layoutframe = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.layoutframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.layoutframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.layoutframe.setObjectName("layoutframe")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutframe)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(-1, 0, -1, -1)
        self.layout.setSpacing(6)
        self.layout.setObjectName("layout")
        self.verticalLayout_3.addLayout(self.layout)
        self.verticalLayout_4.addWidget(self.layoutframe)
        self.layoutversionsframe = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.layoutversionsframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.layoutversionsframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.layoutversionsframe.setObjectName("layoutversionsframe")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutversionsframe)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.layoutversions = QtWidgets.QVBoxLayout()
        self.layoutversions.setObjectName("layoutversions")
        self.verticalLayout_5.addLayout(self.layoutversions)
        self.verticalLayout_4.addWidget(self.layoutversionsframe)
        self.ContentView.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.ContentView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setToolTipDuration(0)
        self.menubar.setObjectName("menubar")
        self.menuConfigure = QtWidgets.QMenu(self.menubar)
        self.menuConfigure.setObjectName("menuConfigure")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.setFolder = QtWidgets.QAction(MainWindow)
        self.setFolder.setWhatsThis("")
        self.setFolder.setObjectName("setFolder")
        self.setCensorship = QtWidgets.QAction(MainWindow)
        self.setCensorship.setObjectName("setCensorship")
        self.menuConfigure.addAction(self.setFolder)
        self.menuConfigure.addSeparator()
        self.menuConfigure.addAction(self.setCensorship)
        self.menubar.addAction(self.menuConfigure.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Party Installer"))
        self.Info.setText(_translate("MainWindow", "TextLabel"))
        self.menuConfigure.setTitle(_translate("MainWindow", "Configure"))
        self.setFolder.setText(_translate("MainWindow", "Set Story Folder"))
        self.setFolder.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.setCensorship.setText(_translate("MainWindow", "Set Censorship"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
