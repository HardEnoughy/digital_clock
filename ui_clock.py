# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clock.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(461, 314)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.h_layout = QHBoxLayout()
        self.h_layout.setObjectName(u"h_layout")
        self.hours_label = QLabel(self.central_widget)
        self.hours_label.setObjectName(u"hours_label")
        self.hours_label.setTextFormat(Qt.MarkdownText)
        self.hours_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.h_layout.addWidget(self.hours_label)

        self.dots_label = QLabel(self.central_widget)
        self.dots_label.setObjectName(u"dots_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dots_label.sizePolicy().hasHeightForWidth())
        self.dots_label.setSizePolicy(sizePolicy1)
        self.dots_label.setAlignment(Qt.AlignCenter)

        self.h_layout.addWidget(self.dots_label)

        self.minutes_label = QLabel(self.central_widget)
        self.minutes_label.setObjectName(u"minutes_label")
        self.minutes_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.h_layout.addWidget(self.minutes_label)


        self.verticalLayout.addLayout(self.h_layout)

        MainWindow.setCentralWidget(self.central_widget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.hours_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.dots_label.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.minutes_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

