# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\dcm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 704)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.EGRAMLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.EGRAMLabel.setFont(font)
        self.EGRAMLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EGRAMLabel.setObjectName("EGRAMLabel")
        self.horizontalLayout.addWidget(self.EGRAMLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.atrialPlots = PlotWidget(self.centralwidget)
        self.atrialPlots.setObjectName("atrialPlots")
        self.verticalLayout_2.addWidget(self.atrialPlots)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.ventricularPlots = PlotWidget(self.centralwidget)
        self.ventricularPlots.setObjectName("ventricularPlots")
        self.verticalLayout_2.addWidget(self.ventricularPlots)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 3, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 63, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem)
        self.pace_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pace_btn.sizePolicy().hasHeightForWidth())
        self.pace_btn.setSizePolicy(sizePolicy)
        self.pace_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.pace_btn.setMaximumSize(QtCore.QSize(500, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pace_btn.setFont(font)
        self.pace_btn.setObjectName("pace_btn")
        self.verticalLayout_5.addWidget(self.pace_btn)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.aoo_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.aoo_btn.setChecked(True)
        self.aoo_btn.setObjectName("aoo_btn")
        self.pacing_mode_group = QtWidgets.QButtonGroup(MainWindow)
        self.pacing_mode_group.setObjectName("pacing_mode_group")
        self.pacing_mode_group.addButton(self.aoo_btn)
        self.gridLayout.addWidget(self.aoo_btn, 0, 0, 1, 1)
        self.aai_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.aai_btn.setChecked(False)
        self.aai_btn.setObjectName("aai_btn")
        self.pacing_mode_group.addButton(self.aai_btn)
        self.gridLayout.addWidget(self.aai_btn, 1, 0, 1, 1)
        self.vvi_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.vvi_btn.setChecked(False)
        self.vvi_btn.setObjectName("vvi_btn")
        self.pacing_mode_group.addButton(self.vvi_btn)
        self.gridLayout.addWidget(self.vvi_btn, 1, 1, 1, 1)
        self.voo_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.voo_btn.setObjectName("voo_btn")
        self.pacing_mode_group.addButton(self.voo_btn)
        self.gridLayout.addWidget(self.voo_btn, 0, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.reports_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reports_btn.sizePolicy().hasHeightForWidth())
        self.reports_btn.setSizePolicy(sizePolicy)
        self.reports_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.reports_btn.setMaximumSize(QtCore.QSize(500, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reports_btn.setFont(font)
        self.reports_btn.setObjectName("reports_btn")
        self.verticalLayout.addWidget(self.reports_btn)
        self.parameters_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameters_btn.sizePolicy().hasHeightForWidth())
        self.parameters_btn.setSizePolicy(sizePolicy)
        self.parameters_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.parameters_btn.setMaximumSize(QtCore.QSize(500, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parameters_btn.setFont(font)
        self.parameters_btn.setObjectName("parameters_btn")
        self.verticalLayout.addWidget(self.parameters_btn)
        self.about_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_btn.sizePolicy().hasHeightForWidth())
        self.about_btn.setSizePolicy(sizePolicy)
        self.about_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.about_btn.setMaximumSize(QtCore.QSize(500, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.about_btn.setFont(font)
        self.about_btn.setObjectName("about_btn")
        self.verticalLayout.addWidget(self.about_btn)
        self.set_clock_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_clock_btn.sizePolicy().hasHeightForWidth())
        self.set_clock_btn.setSizePolicy(sizePolicy)
        self.set_clock_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.set_clock_btn.setMaximumSize(QtCore.QSize(500, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_clock_btn.setFont(font)
        self.set_clock_btn.setObjectName("set_clock_btn")
        self.verticalLayout.addWidget(self.set_clock_btn)
        self.new_patient_btn = QtWidgets.QPushButton(self.centralwidget)
        self.new_patient_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_patient_btn.sizePolicy().hasHeightForWidth())
        self.new_patient_btn.setSizePolicy(sizePolicy)
        self.new_patient_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.new_patient_btn.setMaximumSize(QtCore.QSize(500, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_patient_btn.setFont(font)
        self.new_patient_btn.setObjectName("new_patient_btn")
        self.verticalLayout.addWidget(self.new_patient_btn)
        self.quit_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quit_btn.sizePolicy().hasHeightForWidth())
        self.quit_btn.setSizePolicy(sizePolicy)
        self.quit_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.quit_btn.setMaximumSize(QtCore.QSize(500, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        self.verticalLayout.addWidget(self.quit_btn)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionReview = QtWidgets.QAction(MainWindow)
        self.actionReview.setObjectName("actionReview")
        self.actionModify = QtWidgets.QAction(MainWindow)
        self.actionModify.setObjectName("actionModify")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DCM"))
        self.EGRAMLabel.setText(_translate("MainWindow", "ELECTROGRAM"))
        self.label.setText(_translate("MainWindow", "Atrial"))
        self.label_2.setText(_translate("MainWindow", "Ventricular"))
        self.pace_btn.setText(_translate("MainWindow", "Pace Now"))
        self.aoo_btn.setText(_translate("MainWindow", "AOO"))
        self.aai_btn.setText(_translate("MainWindow", "AAI"))
        self.vvi_btn.setText(_translate("MainWindow", "VVI"))
        self.voo_btn.setText(_translate("MainWindow", "VOO"))
        self.reports_btn.setText(_translate("MainWindow", "Reports"))
        self.parameters_btn.setText(_translate("MainWindow", "Parameters"))
        self.about_btn.setText(_translate("MainWindow", "About"))
        self.set_clock_btn.setText(_translate("MainWindow", "Set Clock"))
        self.new_patient_btn.setText(_translate("MainWindow", "New Patient"))
        self.quit_btn.setText(_translate("MainWindow", "Quit"))
        self.actionReview.setText(_translate("MainWindow", "Review"))
        self.actionModify.setText(_translate("MainWindow", "Modify"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
