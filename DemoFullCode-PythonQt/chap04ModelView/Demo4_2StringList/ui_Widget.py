# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(549, 348)
        font = QtGui.QFont()
        font.setPointSize(10)
        Widget.setFont(font)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtWidgets.QSplitter(Widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btnList_Reset = QtWidgets.QPushButton(self.groupBox)
        self.btnList_Reset.setObjectName("btnList_Reset")
        self.gridLayout.addWidget(self.btnList_Reset, 0, 0, 1, 1)
        self.btnList_Append = QtWidgets.QPushButton(self.groupBox)
        self.btnList_Append.setObjectName("btnList_Append")
        self.gridLayout.addWidget(self.btnList_Append, 1, 0, 1, 1)
        self.btnList_Insert = QtWidgets.QPushButton(self.groupBox)
        self.btnList_Insert.setObjectName("btnList_Insert")
        self.gridLayout.addWidget(self.btnList_Insert, 1, 1, 1, 1)
        self.btnList_Delete = QtWidgets.QPushButton(self.groupBox)
        self.btnList_Delete.setObjectName("btnList_Delete")
        self.gridLayout.addWidget(self.btnList_Delete, 2, 0, 1, 1)
        self.btnList_Clear = QtWidgets.QPushButton(self.groupBox)
        self.btnList_Clear.setObjectName("btnList_Clear")
        self.gridLayout.addWidget(self.btnList_Clear, 2, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setObjectName("listView")
        self.verticalLayout_3.addWidget(self.listView)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnText_Clear = QtWidgets.QPushButton(self.groupBox_2)
        self.btnText_Clear.setObjectName("btnText_Clear")
        self.verticalLayout.addWidget(self.btnText_Clear)
        self.btnText_Display = QtWidgets.QPushButton(self.groupBox_2)
        self.btnText_Display.setObjectName("btnText_Display")
        self.verticalLayout.addWidget(self.btnText_Display)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.verticalLayout_4.addWidget(self.splitter)
        self.groupBox_3 = QtWidgets.QGroupBox(Widget)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LabInfo = QtWidgets.QLabel(self.groupBox_3)
        self.LabInfo.setObjectName("LabInfo")
        self.horizontalLayout.addWidget(self.LabInfo)
        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Demo4_2, QListView的使用"))
        self.groupBox.setTitle(_translate("Widget", "QListView"))
        self.btnList_Reset.setText(_translate("Widget", "恢复列表"))
        self.btnList_Append.setText(_translate("Widget", "添加项"))
        self.btnList_Insert.setText(_translate("Widget", "插入项"))
        self.btnList_Delete.setText(_translate("Widget", "删除当前项"))
        self.btnList_Clear.setText(_translate("Widget", "清空列表"))
        self.groupBox_2.setTitle(_translate("Widget", "QPlainTextEdit"))
        self.btnText_Clear.setText(_translate("Widget", "清空文本"))
        self.btnText_Display.setText(_translate("Widget", "显示数据模型的StringList"))
        self.LabInfo.setText(_translate("Widget", "当前项的ModelIndex"))

