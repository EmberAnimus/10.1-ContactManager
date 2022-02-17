# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 510)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 781, 491))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButtonSubmit = QPushButton(self.widget)
        self.pushButtonSubmit.setObjectName(u"pushButtonSubmit")

        self.gridLayout.addWidget(self.pushButtonSubmit, 1, 6, 1, 1)

        self.labelCity = QLabel(self.widget)
        self.labelCity.setObjectName(u"labelCity")

        self.gridLayout.addWidget(self.labelCity, 3, 2, 1, 1)

        self.labelFileDir = QLabel(self.widget)
        self.labelFileDir.setObjectName(u"labelFileDir")

        self.gridLayout.addWidget(self.labelFileDir, 0, 1, 1, 6)

        self.pushButtonClear = QPushButton(self.widget)
        self.pushButtonClear.setObjectName(u"pushButtonClear")

        self.gridLayout.addWidget(self.pushButtonClear, 3, 6, 1, 1)

        self.lineEditName = QLineEdit(self.widget)
        self.lineEditName.setObjectName(u"lineEditName")

        self.gridLayout.addWidget(self.lineEditName, 1, 1, 1, 1)

        self.labelCurFile = QLabel(self.widget)
        self.labelCurFile.setObjectName(u"labelCurFile")

        self.gridLayout.addWidget(self.labelCurFile, 0, 0, 1, 1)

        self.labelName = QLabel(self.widget)
        self.labelName.setObjectName(u"labelName")

        self.gridLayout.addWidget(self.labelName, 1, 0, 1, 1)

        self.labelStreet = QLabel(self.widget)
        self.labelStreet.setObjectName(u"labelStreet")

        self.gridLayout.addWidget(self.labelStreet, 1, 2, 1, 1)

        self.pushButtonChange = QPushButton(self.widget)
        self.pushButtonChange.setObjectName(u"pushButtonChange")

        self.gridLayout.addWidget(self.pushButtonChange, 0, 7, 1, 1)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 3, 1, 1)

        self.comboBoxCountry = QComboBox(self.widget)
        self.comboBoxCountry.setObjectName(u"comboBoxCountry")

        self.gridLayout.addWidget(self.comboBoxCountry, 3, 5, 1, 1)

        self.pushButtonDelete = QPushButton(self.widget)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")

        self.gridLayout.addWidget(self.pushButtonDelete, 1, 7, 1, 1)

        self.labelNum = QLabel(self.widget)
        self.labelNum.setObjectName(u"labelNum")

        self.gridLayout.addWidget(self.labelNum, 3, 0, 1, 1)

        self.labelState = QLabel(self.widget)
        self.labelState.setObjectName(u"labelState")

        self.gridLayout.addWidget(self.labelState, 1, 4, 1, 1)

        self.lineEditCity = QLineEdit(self.widget)
        self.lineEditCity.setObjectName(u"lineEditCity")

        self.gridLayout.addWidget(self.lineEditCity, 3, 3, 1, 1)

        self.labelCountry = QLabel(self.widget)
        self.labelCountry.setObjectName(u"labelCountry")

        self.gridLayout.addWidget(self.labelCountry, 3, 4, 1, 1)

        self.comboBoxState = QComboBox(self.widget)
        self.comboBoxState.setObjectName(u"comboBoxState")

        self.gridLayout.addWidget(self.comboBoxState, 1, 5, 1, 1)

        self.lineEditNum = QLineEdit(self.widget)
        self.lineEditNum.setObjectName(u"lineEditNum")

        self.gridLayout.addWidget(self.lineEditNum, 3, 1, 1, 1)

        self.pushButtonQuit = QPushButton(self.widget)
        self.pushButtonQuit.setObjectName(u"pushButtonQuit")

        self.gridLayout.addWidget(self.pushButtonQuit, 3, 7, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.tableViewContacts = QTableView(self.widget)
        self.tableViewContacts.setObjectName(u"tableViewContacts")
        self.tableViewContacts.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableViewContacts.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableViewContacts.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tableViewContacts)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButtonSubmit.setText(QCoreApplication.translate("Widget", u"Submit", None))
        self.labelCity.setText(QCoreApplication.translate("Widget", u"City:", None))
        self.labelFileDir.setText(QCoreApplication.translate("Widget", u"(Base File)", None))
        self.pushButtonClear.setText(QCoreApplication.translate("Widget", u"Clear", None))
        self.labelCurFile.setText(QCoreApplication.translate("Widget", u"Current File:", None))
        self.labelName.setText(QCoreApplication.translate("Widget", u"Name:", None))
        self.labelStreet.setText(QCoreApplication.translate("Widget", u"Street:", None))
        self.pushButtonChange.setText(QCoreApplication.translate("Widget", u"Change File", None))
        self.pushButtonDelete.setText(QCoreApplication.translate("Widget", u"Delete", None))
        self.labelNum.setText(QCoreApplication.translate("Widget", u"Phone Number:", None))
        self.labelState.setText(QCoreApplication.translate("Widget", u"Region:", None))
        self.labelCountry.setText(QCoreApplication.translate("Widget", u"Country:", None))
        self.lineEditNum.setInputMask(QCoreApplication.translate("Widget", u"(999)999-9999", None))
        self.pushButtonQuit.setText(QCoreApplication.translate("Widget", u"Save and Quit", None))
    # retranslateUi

