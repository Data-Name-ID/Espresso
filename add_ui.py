# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\DataN\Desktop\Espresso\UI\addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(406, 243)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.taste_description_lb = QtWidgets.QLineEdit(Form)
        self.taste_description_lb.setObjectName("taste_description_lb")
        self.gridLayout_2.addWidget(self.taste_description_lb, 4, 1, 1, 1)
        self.id_lb = QtWidgets.QLineEdit(Form)
        self.id_lb.setObjectName("id_lb")
        self.gridLayout_2.addWidget(self.id_lb, 0, 1, 1, 1)
        self.variety_name_lb = QtWidgets.QLineEdit(Form)
        self.variety_name_lb.setObjectName("variety_name_lb")
        self.gridLayout_2.addWidget(self.variety_name_lb, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.price_lb = QtWidgets.QLineEdit(Form)
        self.price_lb.setObjectName("price_lb")
        self.gridLayout_2.addWidget(self.price_lb, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.degree_of_roasting_lb = QtWidgets.QLineEdit(Form)
        self.degree_of_roasting_lb.setObjectName("degree_of_roasting_lb")
        self.gridLayout_2.addWidget(self.degree_of_roasting_lb, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.is_ground_lb = QtWidgets.QLineEdit(Form)
        self.is_ground_lb.setObjectName("is_ground_lb")
        self.gridLayout_2.addWidget(self.is_ground_lb, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.packing_volume_lb = QtWidgets.QLineEdit(Form)
        self.packing_volume_lb.setObjectName("packing_volume_lb")
        self.gridLayout_2.addWidget(self.packing_volume_lb, 6, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.info = QtWidgets.QLabel(Form)
        self.info.setText("")
        self.info.setObjectName("info")
        self.horizontalLayout_5.addWidget(self.info)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить сорт кофе"))
        self.label_6.setText(_translate("Form", "Цена"))
        self.label.setText(_translate("Form", "ID"))
        self.label_5.setText(_translate("Form", "Описание вкуса"))
        self.label_3.setText(_translate("Form", "Название сорта"))
        self.label_2.setText(_translate("Form", "Степень обжарки"))
        self.label_4.setText(_translate("Form", "Молотый/В зернах"))
        self.label_7.setText(_translate("Form", "Объем упаковки"))
        self.pushButton.setText(_translate("Form", "Добавить"))