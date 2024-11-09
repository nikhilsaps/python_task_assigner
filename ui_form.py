
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.verticalLayoutWidget = QWidget(Widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 781, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(800, 40))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(300, 16777215))
        self.groupBox_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cap_csv_data = QLabel(self.groupBox_3)
        self.cap_csv_data.setObjectName(u"cap_csv_data")
        self.cap_csv_data.setGeometry(QRect(10, 30, 231, 141))
        self.cap_csv_data.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.cap_assign_csv = QLabel(self.groupBox_3)
        self.cap_assign_csv.setObjectName(u"cap_assign_csv")
        self.cap_assign_csv.setGeometry(QRect(10, 170, 231, 251))
        self.cap_assign_csv.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.load_cap_csv = QPushButton(self.groupBox_3)
        self.load_cap_csv.setObjectName(u"load_cap_csv")
        self.load_cap_csv.setGeometry(QRect(20, 480, 80, 24))
        self.assign_cap_csv = QPushButton(self.groupBox_3)
        self.assign_cap_csv.setObjectName(u"assign_cap_csv")
        self.assign_cap_csv.setGeometry(QRect(140, 480, 80, 24))

        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(300, 700))
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rma_csv_data = QLabel(self.groupBox_2)
        self.rma_csv_data.setObjectName(u"rma_csv_data")
        self.rma_csv_data.setGeometry(QRect(10, 30, 231, 141))
        self.rma_csv_data.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.rma_assign_csv = QLabel(self.groupBox_2)
        self.rma_assign_csv.setObjectName(u"rma_assign_csv")
        self.rma_assign_csv.setGeometry(QRect(10, 170, 231, 251))
        self.rma_assign_csv.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.load_rma_csv = QPushButton(self.groupBox_2)
        self.load_rma_csv.setObjectName(u"load_rma_csv")
        self.load_rma_csv.setGeometry(QRect(20, 480, 80, 24))
        self.assign_rma_csv = QPushButton(self.groupBox_2)
        self.assign_rma_csv.setObjectName(u"assign_rma_csv")
        self.assign_rma_csv.setGeometry(QRect(150, 480, 80, 24))

        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(300, 700))
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.almond_csv_data = QLabel(self.groupBox)
        self.almond_csv_data.setObjectName(u"almond_csv_data")
        self.almond_csv_data.setGeometry(QRect(10, 30, 231, 141))
        self.almond_csv_data.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.almond_assign_csv = QLabel(self.groupBox)
        self.almond_assign_csv.setObjectName(u"almond_assign_csv")
        self.almond_assign_csv.setGeometry(QRect(10, 170, 231, 251))
        self.almond_assign_csv.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.load_almond_csv = QPushButton(self.groupBox)
        self.load_almond_csv.setObjectName(u"load_almond_csv")
        self.load_almond_csv.setGeometry(QRect(30, 480, 80, 24))
        self.assign_almond_csv = QPushButton(self.groupBox)
        self.assign_almond_csv.setObjectName(u"assign_almond_csv")
        self.assign_almond_csv.setGeometry(QRect(139, 480, 91, 24))

        self.horizontalLayout.addWidget(self.groupBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"MOI", None))
        self.label.setText(QCoreApplication.translate("Widget", u"MOI  Automated Assigner", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"CAP", None))
        self.cap_csv_data.setText(QCoreApplication.translate("Widget", u"CAP File data", None))
        self.cap_assign_csv.setText(QCoreApplication.translate("Widget", u"CAP Assign Data ", None))
        self.load_cap_csv.setText(QCoreApplication.translate("Widget", u"Load CSV", None))
        self.assign_cap_csv.setText(QCoreApplication.translate("Widget", u"Assign CAP", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"RMA", None))
        self.rma_csv_data.setText(QCoreApplication.translate("Widget", u"RMA File Data", None))
        self.rma_assign_csv.setText(QCoreApplication.translate("Widget", u"RMA  Assign Data", None))
        self.load_rma_csv.setText(QCoreApplication.translate("Widget", u"Load CSV", None))
        self.assign_rma_csv.setText(QCoreApplication.translate("Widget", u"RMA Assign", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Almond", None))
        self.almond_csv_data.setText(QCoreApplication.translate("Widget", u"Almond File data", None))
        self.almond_assign_csv.setText(QCoreApplication.translate("Widget", u"Almond Assign Data", None))
        self.load_almond_csv.setText(QCoreApplication.translate("Widget", u"Load CSV", None))
        self.assign_almond_csv.setText(QCoreApplication.translate("Widget", u"Almond Assign", None))
    # retranslateUi

