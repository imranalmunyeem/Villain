# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JARVISmain(object):
    def setupUi(self, JARVISmain):
        JARVISmain.setObjectName("JARVISmain")
        JARVISmain.resize(1080, 720)
        JARVISmain.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.kartisTechLabel = QtWidgets.QLabel(JARVISmain)
        self.kartisTechLabel.setGeometry(QtCore.QRect(240, 10, 640, 81))
        self.kartisTechLabel.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"\n"
"background-color: transparent;")
        self.kartisTechLabel.setText("")
        self.kartisTechLabel.setPixmap(QtGui.QPixmap("../../../gui_tools/KartisTechnology(white).png"))
        self.kartisTechLabel.setScaledContents(True)
        self.kartisTechLabel.setObjectName("kartisTechLabel")
        self.exitButton = QtWidgets.QPushButton(JARVISmain)
        self.exitButton.setGeometry(QtCore.QRect(946, 639, 131, 71))
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet("border-image: url(E:/CODING/Artificial_Intelligence/FacialRecogByJARVIS/with GUI/gui_tools/exit(with border).png);\n"
"background-color: transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 5px 5px 5px 5px;\n"
"")
        self.exitButton.setText("")
        self.exitButton.setFlat(False)
        self.exitButton.setObjectName("exitButton")
        self.listeningLabel = QtWidgets.QLabel(JARVISmain)
        self.listeningLabel.setGeometry(QtCore.QRect(-80, 150, 461, 321))
        self.listeningLabel.setStyleSheet("border-radius: 200px;\n"
"background: transparent;")
        self.listeningLabel.setText("")
        self.listeningLabel.setPixmap(QtGui.QPixmap("../../../gui_tools/listeningGIF.gif"))
        self.listeningLabel.setScaledContents(True)
        self.listeningLabel.setObjectName("listeningLabel")
        self.arcLabel = QtWidgets.QLabel(JARVISmain)
        self.arcLabel.setGeometry(QtCore.QRect(230, 110, 641, 361))
        self.arcLabel.setStyleSheet("border-radius: 200px;\n"
"background: transparent;")
        self.arcLabel.setText("")
        self.arcLabel.setPixmap(QtGui.QPixmap("../../../gui_tools/techcircle.gif"))
        self.arcLabel.setScaledContents(True)
        self.arcLabel.setObjectName("arcLabel")
        self.backgroundgifLabel = QtWidgets.QLabel(JARVISmain)
        self.backgroundgifLabel.setGeometry(QtCore.QRect(0, 450, 1091, 271))
        self.backgroundgifLabel.setStyleSheet("border-radius: 200px;\n"
"background: transparent;")
        self.backgroundgifLabel.setText("")
        self.backgroundgifLabel.setPixmap(QtGui.QPixmap("../../../gui_tools/background.gif"))
        self.backgroundgifLabel.setScaledContents(True)
        self.backgroundgifLabel.setObjectName("backgroundgifLabel")
        self.codingLabel = QtWidgets.QLabel(JARVISmain)
        self.codingLabel.setGeometry(QtCore.QRect(0, -20, 251, 211))
        self.codingLabel.setStyleSheet("border-radius: 200px;\n"
"background: transparent;")
        self.codingLabel.setText("")
        self.codingLabel.setPixmap(QtGui.QPixmap("../../../gui_tools/Code_Template.gif"))
        self.codingLabel.setScaledContents(False)
        self.codingLabel.setObjectName("codingLabel")
        self.ironmanHelmetLabel = QtWidgets.QLabel(JARVISmain)
        self.ironmanHelmetLabel.setGeometry(QtCore.QRect(780, 0, 461, 311))
        self.ironmanHelmetLabel.setStyleSheet("border-radius: 200px;\n"
"background: transparent;")
        self.ironmanHelmetLabel.setText("")
        self.ironmanHelmetLabel.setPixmap(QtGui.QPixmap("../../../gui_tools/Iron_Template.jpg"))
        self.ironmanHelmetLabel.setScaledContents(False)
        self.ironmanHelmetLabel.setObjectName("ironmanHelmetLabel")
        self.frame = QtWidgets.QFrame(JARVISmain)
        self.frame.setGeometry(QtCore.QRect(10, 480, 923, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.terminalOutputBox = QtWidgets.QLineEdit(self.frame)
        self.terminalOutputBox.setGeometry(QtCore.QRect(0, 0, 923, 200))
        self.terminalOutputBox.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"font:14pt \"Karisma\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 1px 1px 1px 1px;\n"
"padding-left:5px;")
        self.terminalOutputBox.setText("")
        self.terminalOutputBox.setReadOnly(True)
        self.terminalOutputBox.setObjectName("terminalOutputBox")
        self.terminalInputBox = QtWidgets.QLineEdit(self.frame)
        self.terminalInputBox.setGeometry(QtCore.QRect(0, 200, 923, 31))
        self.terminalInputBox.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"font: 16pt \"Karisma\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 3px 3px 3px 3px;\n"
"padding-left:5px;")
        self.terminalInputBox.setText("")
        self.terminalInputBox.setObjectName("terminalInputBox")
        self.enterButton = QtWidgets.QPushButton(self.frame)
        self.enterButton.setGeometry(QtCore.QRect(852, 200, 71, 31))
        self.enterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enterButton.setStyleSheet("border-image: url(E:/CODING/Artificial_Intelligence/FacialRecogByJARVIS/with GUI/gui_tools/enter.png);\n"
"background-color: transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-left: 5px;\n"
"")
        self.enterButton.setText("")
        self.enterButton.setFlat(False)
        self.enterButton.setObjectName("enterButton")
        self.jarvisSpeakingLabel = QtWidgets.QLabel(JARVISmain)
        self.jarvisSpeakingLabel.setEnabled(True)
        self.jarvisSpeakingLabel.setGeometry(QtCore.QRect(-80, 150, 461, 321))
        self.jarvisSpeakingLabel.setStyleSheet("border-radius: 200px;\n"
"background: transparent;")
        self.jarvisSpeakingLabel.setText("")
        self.jarvisSpeakingLabel.setPixmap(QtGui.QPixmap("../../../gui_tools/Ntuks.gif"))
        self.jarvisSpeakingLabel.setScaledContents(True)
        self.jarvisSpeakingLabel.setObjectName("jarvisSpeakingLabel")
        self.jarvisSpeakingLabel.raise_()
        self.arcLabel.raise_()
        self.ironmanHelmetLabel.raise_()
        self.backgroundgifLabel.raise_()
        self.kartisTechLabel.raise_()
        self.exitButton.raise_()
        self.listeningLabel.raise_()
        self.codingLabel.raise_()
        self.frame.raise_()

        self.retranslateUi(JARVISmain)
        QtCore.QMetaObject.connectSlotsByName(JARVISmain)

    def retranslateUi(self, JARVISmain):
        _translate = QtCore.QCoreApplication.translate
        JARVISmain.setWindowTitle(_translate("JARVISmain", "JARVIS Main Window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JARVISmain = QtWidgets.QWidget()
    ui = Ui_JARVISmain()
    ui.setupUi(JARVISmain)
    JARVISmain.show()
    sys.exit(app.exec_())
