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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headerFrame = QtWidgets.QFrame(self.centralwidget)
        self.headerFrame.setMinimumSize(QtCore.QSize(0, 30))
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.headerFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.Info = QtWidgets.QLabel(self.headerFrame)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 618, 369))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(-1, 0, -1, -1)
        self.layout.setSpacing(6)
        self.layout.setObjectName("layout")
        self.verticalLayout_4.addLayout(self.layout)
        self.ContentView.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.ContentView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Party Installer"))
        self.Info.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
