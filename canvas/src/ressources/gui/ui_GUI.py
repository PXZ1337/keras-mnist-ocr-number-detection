# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\DEV\ocr-number-detection\canvas\src\ressources\gui\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(1280, 720))
        Dialog.setMaximumSize(QtCore.QSize(1280, 720))
        self.DrawingFrame = QtWidgets.QStackedWidget(Dialog)
        self.DrawingFrame.setGeometry(QtCore.QRect(130, 160, 256, 256))
        self.DrawingFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.DrawingFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DrawingFrame.setObjectName("DrawingFrame")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.DrawingFrame.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.DrawingFrame.addWidget(self.page_2)
        self.Clear_Button = QtWidgets.QPushButton(Dialog)
        self.Clear_Button.setGeometry(QtCore.QRect(130, 520, 256, 50))
        self.Clear_Button.setObjectName("Clear_Button")
        self.PredictionFrame = QtWidgets.QStackedWidget(Dialog)
        self.PredictionFrame.setGeometry(QtCore.QRect(460, 160, 280, 280))
        self.PredictionFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.PredictionFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.PredictionFrame.setLineWidth(0)
        self.PredictionFrame.setObjectName("PredictionFrame")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.PredictionFrame.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.PredictionFrame.addWidget(self.page_4)
        self.Predict_Button = QtWidgets.QPushButton(Dialog)
        self.Predict_Button.setGeometry(QtCore.QRect(460, 520, 280, 50))
        self.Predict_Button.setObjectName("Predict_Button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "OCR Number Detection"))
        self.Clear_Button.setText(_translate("Dialog", "Clear"))
        self.Predict_Button.setText(_translate("Dialog", "Predict"))
