# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/popup.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(240, 320)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Name = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Name.setObjectName("Name")
        self.verticalLayout.addWidget(self.Name)
        self.installinfo = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.installinfo.setFont(font)
        self.installinfo.setAlignment(QtCore.Qt.AlignCenter)
        self.installinfo.setObjectName("installinfo")
        self.verticalLayout.addWidget(self.installinfo)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 220, 257))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.contentview = QtWidgets.QVBoxLayout()
        self.contentview.setObjectName("contentview")
        self.verticalLayout_3.addLayout(self.contentview)
        self.forumbutton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.forumbutton.setObjectName("forumbutton")
        self.verticalLayout_3.addWidget(self.forumbutton)
        self.backButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.backButton.setObjectName("backButton")
        self.verticalLayout_3.addWidget(self.backButton)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Choose Version"))
        self.Name.setText(_translate("Form", "TextLabel"))
        self.installinfo.setText(_translate("Form", "TextLabel"))
        self.forumbutton.setText(_translate("Form", "Forum"))
        self.backButton.setText(_translate("Form", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
