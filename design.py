

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 589)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setMovable(False)
        self.teb_connecting = QWidget()
        self.teb_connecting.setObjectName(u"teb_connecting")
        self.horizontalLayout_2 = QHBoxLayout(self.teb_connecting)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.table_sessions = QTableWidget(self.teb_connecting)
        if (self.table_sessions.columnCount() < 9):
            self.table_sessions.setColumnCount(9)
        self.table_sessions.setObjectName(u"table_sessions")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_sessions.sizePolicy().hasHeightForWidth())
        self.table_sessions.setSizePolicy(sizePolicy)
        self.table_sessions.setSortingEnabled(False)
        self.table_sessions.setRowCount(0)
        self.table_sessions.setColumnCount(9)
        self.table_sessions.horizontalHeader().setVisible(True)
        self.table_sessions.horizontalHeader().setDefaultSectionSize(65)
        self.table_sessions.horizontalHeader().setHighlightSections(False)
        self.table_sessions.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_sessions.horizontalHeader().setStretchLastSection(False)
        self.table_sessions.verticalHeader().setVisible(True)

        self.horizontalLayout_2.addWidget(self.table_sessions)

        self.settings = QGroupBox(self.teb_connecting)
        self.settings.setObjectName(u"settings")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.settings)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_connect = QPushButton(self.settings)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_connect.sizePolicy().hasHeightForWidth())
        self.btn_connect.setSizePolicy(sizePolicy2)
        self.btn_connect.setMinimumSize(QSize(0, 40))
        self.btn_connect.setBaseSize(QSize(20, 0))

        self.verticalLayout_3.addWidget(self.btn_connect)

        self.toolBox = QToolBox(self.settings)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setEnabled(True)
        self.toolBox.setAutoFillBackground(True)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 456, 360))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.drop_sessions = QWidget(self.page)
        self.drop_sessions.setObjectName(u"drop_sessions")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.drop_sessions.sizePolicy().hasHeightForWidth())
        self.drop_sessions.setSizePolicy(sizePolicy3)

        self.verticalLayout_4.addWidget(self.drop_sessions)

        self.toolBox.addItem(self.page, u"\u0421\u0435\u0439\u0441\u0441\u0438\u0438")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 456, 360))
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.drop_proxy = QWidget(self.page_2)
        self.drop_proxy.setObjectName(u"drop_proxy")
        sizePolicy3.setHeightForWidth(self.drop_proxy.sizePolicy().hasHeightForWidth())
        self.drop_proxy.setSizePolicy(sizePolicy3)
        self.drop_proxy.setAcceptDrops(True)

        self.verticalLayout_2.addWidget(self.drop_proxy)

        self.toolBox.addItem(self.page_2, u"\u041f\u0440\u043e\u043a\u0441\u0438")

        self.verticalLayout_3.addWidget(self.toolBox)

        self.out_concole = QLabel(self.settings)
        self.out_concole.setObjectName(u"out_concole")
        font = QFont()
        font.setBold(True)
        self.out_concole.setFont(font)
        self.out_concole.setAutoFillBackground(False)
        self.out_concole.setStyleSheet(u"background-color:  rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255)")

        self.verticalLayout_3.addWidget(self.out_concole)


        self.horizontalLayout_2.addWidget(self.settings)

        self.tabWidget.addTab(self.teb_connecting, "")
        self.tab_mail = QWidget()
        self.tab_mail.setObjectName(u"tab_mail")
        self.horizontalLayout = QHBoxLayout(self.tab_mail)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget.addTab(self.tab_mail, "")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.tabWidget.addTab(self.widget, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0433\u0440\u0430\u043c\u043c\u0435\u0440", None))
        self.settings.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043a\u043e\u043d\u043d\u0435\u043a\u0442\u0438\u0442\u044c", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0439\u0441\u0441\u0438\u0438", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043a\u0441\u0438", None))
        self.out_concole.setText(QCoreApplication.translate("MainWindow", u"lol", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.teb_connecting), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mail), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0447\u0442\u0435\u0440", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0442\u0435\u0440", None))
    # retranslateUi

