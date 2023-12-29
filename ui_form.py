# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextBrowser, QToolButton,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 371, 18))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 250, 271, 18))
        self.tape = QLineEdit(Widget)
        self.tape.setObjectName(u"tape")
        self.tape.setGeometry(QRect(390, 270, 341, 26))
        self.run = QPushButton(Widget)
        self.run.setObjectName(u"run")
        self.run.setGeometry(QRect(270, 240, 87, 26))
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 450, 71, 18))
        self.days = QLabel(Widget)
        self.days.setObjectName(u"days")
        self.days.setGeometry(QRect(100, 450, 71, 18))
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 480, 61, 18))
        self.license = QLabel(Widget)
        self.license.setObjectName(u"license")
        self.license.setGeometry(QRect(100, 480, 391, 18))
        self.states = QListWidget(Widget)
        self.states.setObjectName(u"states")
        self.states.setGeometry(QRect(580, 320, 211, 192))
        self.addState = QPushButton(Widget)
        self.addState.setObjectName(u"addState")
        self.addState.setGeometry(QRect(700, 520, 87, 26))
        self.newState = QLineEdit(Widget)
        self.newState.setObjectName(u"newState")
        self.newState.setGeometry(QRect(580, 520, 113, 26))
        self.transition_rules = QTableWidget(Widget)
        if (self.transition_rules.columnCount() < 6):
            self.transition_rules.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.transition_rules.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.transition_rules.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.transition_rules.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.transition_rules.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.transition_rules.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.transition_rules.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.transition_rules.setObjectName(u"transition_rules")
        self.transition_rules.setGeometry(QRect(10, 50, 621, 192))
        self.add_transition_rule_button = QToolButton(Widget)
        self.add_transition_rule_button.setObjectName(u"add_transition_rule_button")
        self.add_transition_rule_button.setGeometry(QRect(600, 50, 31, 25))
        icon = QIcon(QIcon.fromTheme(u"contact-new"))
        self.add_transition_rule_button.setIcon(icon)
        self.textBrowser = QTextBrowser(Widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(310, 380, 256, 91))
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(580, 300, 51, 18))
        self.renewLicense = QPushButton(Widget)
        self.renewLicense.setObjectName(u"renewLicense")
        self.renewLicense.setGeometry(QRect(50, 520, 87, 26))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"TuringMachine.pro", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Please enter the transition rules of the turing machine:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Please enter the tape you want to check:", None))
        self.run.setText(QCoreApplication.translate("Widget", u"Run", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Days Left: ", None))
        self.days.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"License:", None))
        self.license.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.addState.setText(QCoreApplication.translate("Widget", u"Add State", None))
        ___qtablewidgetitem = self.transition_rules.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"delete", None));
        ___qtablewidgetitem1 = self.transition_rules.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"Current State", None));
        ___qtablewidgetitem2 = self.transition_rules.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"Read", None));
        ___qtablewidgetitem3 = self.transition_rules.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Widget", u"Next State", None));
        ___qtablewidgetitem4 = self.transition_rules.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Widget", u"Write", None));
        ___qtablewidgetitem5 = self.transition_rules.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Widget", u"Move", None));
        self.add_transition_rule_button.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e01b24;\">Warning: Please ensure that 'accept' and 'discard' states are at the end, and the initial state is at the beginning.</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"States:", None))
        self.renewLicense.setText(QCoreApplication.translate("Widget", u"RENEW", None))
    # retranslateUi

