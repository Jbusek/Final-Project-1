# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 300)
        MainWindow.setMinimumSize(QtCore.QSize(350, 300))
        MainWindow.setMaximumSize(QtCore.QSize(350, 300))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 81, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 10, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.button_jane = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.button_jane.setGeometry(QtCore.QRect(140, 80, 100, 20))
        self.button_jane.setObjectName("button_jane")
        self.button_john = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.button_john.setGeometry(QtCore.QRect(140, 110, 100, 20))
        self.button_john.setObjectName("button_john")
        self.button_submit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_submit.setGeometry(QtCore.QRect(80, 150, 201, 32))
        self.button_submit.setMinimumSize(QtCore.QSize(0, 0))
        self.button_submit.setObjectName("button_submit")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 200, 141, 20))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 36))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voting Application"))
        self.label.setText(_translate("MainWindow", "Identification"))
        self.label_2.setText(_translate("MainWindow", "Candidates"))
        self.button_jane.setText(_translate("MainWindow", "Jane"))
        self.button_john.setText(_translate("MainWindow", "John"))
        self.button_submit.setText(_translate("MainWindow", "Submit"))
        self.label_3.setText(_translate("MainWindow", "Incorrect Identification"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
