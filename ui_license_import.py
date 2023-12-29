# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'license_import.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_EnterLicense(object):
    def setupUi(self, EnterLicense):
        if not EnterLicense.objectName():
            EnterLicense.setObjectName(u"EnterLicense")
        EnterLicense.resize(400, 300)
        self.buttonBox = QDialogButtonBox(EnterLicense)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(200, 240, 171, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(EnterLicense)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 70, 51, 18))
        self.license_input = QLineEdit(EnterLicense)
        self.license_input.setObjectName(u"license_input")
        self.license_input.setGeometry(QRect(90, 70, 241, 26))
        self.buy = QPushButton(EnterLicense)
        self.buy.setObjectName(u"buy")
        self.buy.setGeometry(QRect(30, 240, 87, 26))

        self.retranslateUi(EnterLicense)
        self.buttonBox.accepted.connect(EnterLicense.accept)
        self.buttonBox.rejected.connect(EnterLicense.reject)

        QMetaObject.connectSlotsByName(EnterLicense)
    # setupUi

    def retranslateUi(self, EnterLicense):
        EnterLicense.setWindowTitle(QCoreApplication.translate("EnterLicense", u"Enter License", None))
        self.label.setText(QCoreApplication.translate("EnterLicense", u"license: ", None))
        self.buy.setText(QCoreApplication.translate("EnterLicense", u"Buy Now", None))
    # retranslateUi

