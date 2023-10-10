from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 514)
        MainWindow.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(20, 0, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(31)
        self.outputLabel.setFont(font)
        self.outputLabel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.outputLabel.setStyleSheet("color:rgb(81, 81, 81)")
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.outputLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.percentButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.press_it('%'))
        self.percentButton.setGeometry(QtCore.QRect(10, 100, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.percentButton.setFont(font)
        self.percentButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.percentButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.percentButton.setAutoFillBackground(False)
        self.percentButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(218, 218, 218);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(204, 204, 204)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:rgb(218, 218, 218);\n"
"}")
        self.percentButton.setCheckable(False)
        self.percentButton.setAutoDefault(False)
        self.percentButton.setDefault(False)
        self.percentButton.setFlat(False)
        self.percentButton.setObjectName("percentButton")
        self.clearButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.press_it('c'))
        self.clearButton.setGeometry(QtCore.QRect(90, 100, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.clearButton.setFont(font)
        self.clearButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.clearButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.clearButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(218, 218, 218);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(204, 204, 204)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:rgb(218, 218, 218);\n"
"}")
        self.clearButton.setObjectName("clearButton")
        self.aeroButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.remove_it())
        self.aeroButton.setGeometry(QtCore.QRect(170, 100, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.aeroButton.setFont(font)
        self.aeroButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.aeroButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.aeroButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(218, 218, 218);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(204, 204, 204)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:rgb(218, 218, 218);\n"
"}")
        self.aeroButton.setObjectName("aeroButton")
        self.slashButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.press_it('/'))
        self.slashButton.setGeometry(QtCore.QRect(250, 100, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.slashButton.setFont(font)
        self.slashButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.slashButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.slashButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(218, 218, 218);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(204, 204, 204)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:rgb(218, 218, 218);\n"
"}")
        self.slashButton.setObjectName("slashButton")
        self.multiplyButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.press_it('*'))
        self.multiplyButton.setGeometry(QtCore.QRect(250, 180, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.multiplyButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.multiplyButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(218, 218, 218);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(204, 204, 204)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:rgb(218, 218, 218);\n"
"}")
        self.multiplyButton.setObjectName("multiplyButton")
        self.sevenButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.press_it('7'))
        self.sevenButton.setGeometry(QtCore.QRect(10, 180, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.sevenButton.setFont(font)
        self.sevenButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sevenButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.sevenButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(160, 160, 160);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(193, 193, 193)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:white;\n"
"}")
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.press_it('8'))
        self.eightButton.setGeometry(QtCore.QRect(90, 180, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.eightButton.setFont(font)
        self.eightButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.eightButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.eightButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(160, 160, 160);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(193, 193, 193)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:white;\n"
"}")
        self.eightButton.setObjectName("eightButton")
        self.nineButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.press_it('9'))
        self.nineButton.setGeometry(QtCore.QRect(170, 180, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.nineButton.setFont(font)
        self.nineButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.nineButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.nineButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(160, 160, 160);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(193, 193, 193)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:white;\n"
"}")
        self.nineButton.setObjectName("nineButton")
        self.sixButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.press_it('6'))
        self.sixButton.setGeometry(QtCore.QRect(170, 260, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.sixButton.setFont(font)
        self.sixButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sixButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.sixButton.setAcceptDrops(False)
        self.sixButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(160, 160, 160);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(193, 193, 193)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:white;\n"
"}")
        self.sixButton.setFlat(False)
        self.sixButton.setObjectName("sixButton")
        self.fourButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.press_it('4'))
        self.fourButton.setGeometry(QtCore.QRect(10, 260, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.fourButton.setFont(font)
        self.fourButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.fourButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.fourButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(160, 160, 160);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(193, 193, 193)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:white;\n"
"}")
        self.fourButton.setObjectName("fourButton")
        self.minusbutton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.press_it('-'))
        self.minusbutton.setGeometry(QtCore.QRect(250, 260, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.minusbutton.setFont(font)
        self.minusbutton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.minusbutton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.minusbutton.setStyleSheet("QPushButton{\n"
"background-color:rgb(218, 218, 218);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(204, 204, 204)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:rgb(218, 218, 218);\n"
"}")
        self.minusbutton.setObjectName("minusbutton")
        self.fiveButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.press_it('5'))
        self.fiveButton.setGeometry(QtCore.QRect(90, 260, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.fiveButton.setFont(font)
        self.fiveButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.fiveButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.fiveButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(160, 160, 160);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(193, 193, 193)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:white;\n"
"}")
        self.fiveButton.setObjectName("fiveButton")
        self.twoButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.press_it('2'))
        self.twoButton.setGeometry(QtCore.QRect(90, 340, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.twoButton.setFont(font)
        self.twoButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.twoButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.twoButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(160, 160, 160);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(193, 193, 193)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:white;\n"
"}")
        self.twoButton.setObjectName("twoButton")
        self.plusButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.press_it('+'))
        self.plusButton.setGeometry(QtCore.QRect(250, 340, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plusButton.setFont(font)
        self.plusButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.plusButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.plusButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(218, 218, 218);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(204, 204, 204)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:rgb(218, 218, 218);\n"
"}")
        self.plusButton.setObjectName("plusButton")
        self.oneButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.press_it('1'))
        self.oneButton.setGeometry(QtCore.QRect(10, 340, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.oneButton.setFont(font)
        self.oneButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.oneButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.oneButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(160, 160, 160);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(193, 193, 193)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:white;\n"
"}")
        self.oneButton.setObjectName("oneButton")
        self.threeButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.press_it('3'))
        self.threeButton.setGeometry(QtCore.QRect(170, 340, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.threeButton.setFont(font)
        self.threeButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.threeButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.threeButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(160, 160, 160);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(193, 193, 193)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:white;\n"
"}")
        self.threeButton.setObjectName("threeButton")
        self.dotButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.dot_it())
        self.dotButton.setGeometry(QtCore.QRect(170, 420, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.dotButton.setFont(font)
        self.dotButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.dotButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.dotButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(160, 160, 160);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(193, 193, 193)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:white;\n"
"}")
        self.dotButton.setObjectName("dotButton")
        self.plusminusButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.plusminus_it())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 420, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.plusminusButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.plusminusButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(218, 218, 218);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(204, 204, 204)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:rgb(218, 218, 218);\n"
"}")
        self.plusminusButton.setObjectName("plusminusButton")
        self.equalsButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.equals_it())
        self.equalsButton.setGeometry(QtCore.QRect(250, 420, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.equalsButton.setFont(font)
        self.equalsButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.equalsButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.equalsButton.setAutoFillBackground(False)
        self.equalsButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(227, 76, 0);\n"
"color:white;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(249, 83, 0)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:rgb(227, 76, 0);\n"
"}")
        self.equalsButton.setObjectName("equalsButton")
        self.zeroButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.press_it('0'))
        self.zeroButton.setGeometry(QtCore.QRect(90, 420, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.zeroButton.setFont(font)
        self.zeroButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.zeroButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.zeroButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(160, 160, 160);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(193, 193, 193)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:white;\n"
"}")
        self.zeroButton.setObjectName("zeroButton")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 80, 311, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #equals function
    def equals_it(self):
        screen = self.outputLabel.text()
        try:
            answer = eval(screen)
            self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText('ERROR')

    #dot function
    def dot_it(self):
        screen = self.outputLabel.text()
        if '.' in screen:
            pass
        else:
            self.outputLabel.setText(f'{screen}.')


    #plus and minus function
    def plusminus_it(self):
        screen = self.outputLabel.text()
        if screen[0] == '-':
            self.outputLabel.setText(screen[1:])
        else:
            self.outputLabel.setText(f'-{self.outputLabel.text()}')
        
    #backspace function
    def remove_it(self):
        screen = self.outputLabel.text()
        screen = screen[:-1]
        if screen == '':
            self.outputLabel.setText('0')
        else:
            self.outputLabel.setText(screen)

    #Main press function
    def press_it(self,pressed):
        if pressed == 'c':
             self.outputLabel.setText('0')
        else:
             if self.outputLabel.text() == '0':
                 self.outputLabel.setText('')
             self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.clearButton.setText(_translate("MainWindow", "C"))
        self.aeroButton.setText(_translate("MainWindow", "<<"))
        self.slashButton.setText(_translate("MainWindow", "/"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.minusbutton.setText(_translate("MainWindow", "-"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.dotButton.setText(_translate("MainWindow", "."))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.equalsButton.setText(_translate("MainWindow", "="))
        self.zeroButton.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
