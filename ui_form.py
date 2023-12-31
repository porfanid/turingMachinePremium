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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QTableWidget,
    QTableWidgetItem, QTextBrowser, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1484, 710)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setSizeIncrement(QSize(2, 2))
        self.scrollArea = QScrollArea(Widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-10, -10, 1491, 721))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1475, 705))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.gridLayoutWidget_2 = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 1461, 691))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.states = QListWidget(self.gridLayoutWidget_2)
        self.states.setObjectName(u"states")

        self.horizontalLayout_2.addWidget(self.states)

        self.horizontalSpacer_2 = QSpacerItem(293, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.newState = QLineEdit(self.gridLayoutWidget_2)
        self.newState.setObjectName(u"newState")

        self.horizontalLayout.addWidget(self.newState)

        self.addState = QPushButton(self.gridLayoutWidget_2)
        self.addState.setObjectName(u"addState")

        self.horizontalLayout.addWidget(self.addState)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.textBrowser = QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.monthsQuantity = QSpinBox(self.gridLayoutWidget_2)
        self.monthsQuantity.setObjectName(u"monthsQuantity")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.monthsQuantity.sizePolicy().hasHeightForWidth())
        self.monthsQuantity.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.monthsQuantity, 4, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.days = QLabel(self.gridLayoutWidget_2)
        self.days.setObjectName(u"days")
        sizePolicy.setHeightForWidth(self.days.sizePolicy().hasHeightForWidth())
        self.days.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.days, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 135, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.license = QLabel(self.gridLayoutWidget_2)
        self.license.setObjectName(u"license")
        sizePolicy.setHeightForWidth(self.license.sizePolicy().hasHeightForWidth())
        self.license.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.license, 3, 1, 1, 1)

        self.renewLicense = QPushButton(self.gridLayoutWidget_2)
        self.renewLicense.setObjectName(u"renewLicense")

        self.gridLayout.addWidget(self.renewLicense, 5, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.add_transition_rule_button = QToolButton(self.gridLayoutWidget_2)
        self.add_transition_rule_button.setObjectName(u"add_transition_rule_button")
        icon = QIcon(QIcon.fromTheme(u"contact-new"))
        self.add_transition_rule_button.setIcon(icon)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.add_transition_rule_button)

        self.transition_rules = QTableWidget(self.gridLayoutWidget_2)
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
        self.transition_rules.setAutoScroll(False)
        self.transition_rules.setAutoScrollMargin(0)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.transition_rules)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.tape = QLineEdit(self.gridLayoutWidget_2)
        self.tape.setObjectName(u"tape")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.tape)

        self.run = QPushButton(self.gridLayoutWidget_2)
        self.run.setObjectName(u"run")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.run)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(6, QFormLayout.LabelRole, self.verticalSpacer_2)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.formLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.result_box = QTextBrowser(self.gridLayoutWidget_2)
        self.result_box.setObjectName(u"result_box")

        self.verticalLayout_3.addWidget(self.result_box)


        self.formLayout_2.setLayout(3, QFormLayout.FieldRole, self.verticalLayout_3)


        self.horizontalLayout_3.addLayout(self.formLayout_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"TuringMachine.pro", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"States:", None))
        self.addState.setText(QCoreApplication.translate("Widget", u"Add State", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please make sure that you have at least 2 states and one of them is 'accept' or 'discard'(without the quotes).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><"
                        "span style=\" color:#e01b24;\">Warning: Please ensure that 'accept' and 'discard' states are at the end, and the initial state is at the beginning.</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"License:", None))
        self.days.setText(QCoreApplication.translate("Widget", u"Loading...", None))
        self.license.setText(QCoreApplication.translate("Widget", u"Loading...", None))
        self.renewLicense.setText(QCoreApplication.translate("Widget", u"RENEW", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Days Left: ", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"months", None))
        self.add_transition_rule_button.setText("")
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
        self.label.setText(QCoreApplication.translate("Widget", u"Please enter the transition rules of the turing machine:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Please enter the tape you want to check:", None))
        self.run.setText(QCoreApplication.translate("Widget", u"Run", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Result:", None))
    # retranslateUi

