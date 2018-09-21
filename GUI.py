# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 50, 681, 431))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.wifi_entry = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.wifi_entry.setObjectName("wifi_entry")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.wifi_entry)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.wifi_password_entry = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.wifi_password_entry.setObjectName("wifi_password_entry")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.wifi_password_entry)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.dhcp_select = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.dhcp_select.setObjectName("dhcp_select")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dhcp_select)
        self.static_select = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.static_select.setObjectName("static_select")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.static_select)
        self.label_ip_address = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_ip_address.setObjectName("label_ip_address")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_ip_address)
        self.ip_entry = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ip_entry.setObjectName("ip_entry")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.ip_entry)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FPP Updater"))
        self.label_2.setText(_translate("MainWindow", "WiFi SSID:"))
        self.label_3.setText(_translate("MainWindow", "WiFi Password:"))
        self.label_4.setText(_translate("MainWindow", "IP Address"))
        self.dhcp_select.setText(_translate("MainWindow", " DHCP"))
        self.static_select.setText(_translate("MainWindow", "Static"))
        self.label_ip_address.setText(_translate("MainWindow", "IP Address:"))
        self.pushButton.setText(_translate("MainWindow", "Save"))

