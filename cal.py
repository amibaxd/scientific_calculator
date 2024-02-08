# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import math


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1152, 813)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 20pt \"Segoe UI\";")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.push_pi = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_pi.sizePolicy().hasHeightForWidth())
        self.push_pi.setSizePolicy(sizePolicy)
        self.push_pi.setObjectName("push_pi")
        self.gridLayout.addWidget(self.push_pi, 7, 4, 1, 1)
        self.push_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_1.sizePolicy().hasHeightForWidth())
        self.push_1.setSizePolicy(sizePolicy)
        self.push_1.setObjectName("push_1")
        self.gridLayout.addWidget(self.push_1, 6, 0, 1, 1)
        self.push_power = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_power.sizePolicy().hasHeightForWidth())
        self.push_power.setSizePolicy(sizePolicy)
        self.push_power.setObjectName("push_power")
        self.gridLayout.addWidget(self.push_power, 4, 4, 1, 1)
        self.push_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_3.sizePolicy().hasHeightForWidth())
        self.push_3.setSizePolicy(sizePolicy)
        self.push_3.setObjectName("push_3")
        self.gridLayout.addWidget(self.push_3, 6, 3, 1, 1)
        self.push_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_7.sizePolicy().hasHeightForWidth())
        self.push_7.setSizePolicy(sizePolicy)
        self.push_7.setObjectName("push_7")
        self.gridLayout.addWidget(self.push_7, 4, 0, 1, 1)
        self.push_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_2.sizePolicy().hasHeightForWidth())
        self.push_2.setSizePolicy(sizePolicy)
        self.push_2.setObjectName("push_2")
        self.gridLayout.addWidget(self.push_2, 6, 1, 1, 1)
        self.push_equalto = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_equalto.sizePolicy().hasHeightForWidth())
        self.push_equalto.setSizePolicy(sizePolicy)
        self.push_equalto.setObjectName("push_equalto")
        self.gridLayout.addWidget(self.push_equalto, 7, 3, 1, 1)
        self.push_cosx = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_cosx.sizePolicy().hasHeightForWidth())
        self.push_cosx.setSizePolicy(sizePolicy)
        self.push_cosx.setObjectName("push_cosx")
        self.gridLayout.addWidget(self.push_cosx, 1, 1, 1, 1)
        self.push_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_plus.sizePolicy().hasHeightForWidth())
        self.push_plus.setSizePolicy(sizePolicy)
        self.push_plus.setObjectName("push_plus")
        self.gridLayout.addWidget(self.push_plus, 6, 5, 1, 1)
        self.push_tanx = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_tanx.sizePolicy().hasHeightForWidth())
        self.push_tanx.setSizePolicy(sizePolicy)
        self.push_tanx.setObjectName("push_tanx")
        self.gridLayout.addWidget(self.push_tanx, 1, 3, 1, 1)
        self.push_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_div.sizePolicy().hasHeightForWidth())
        self.push_div.setSizePolicy(sizePolicy)
        self.push_div.setObjectName("push_div")
        self.gridLayout.addWidget(self.push_div, 5, 6, 1, 1)
        self.push_epowerx = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_epowerx.sizePolicy().hasHeightForWidth())
        self.push_epowerx.setSizePolicy(sizePolicy)
        self.push_epowerx.setObjectName("push_epowerx")
        self.gridLayout.addWidget(self.push_epowerx, 3, 3, 1, 1)
        self.push_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_8.sizePolicy().hasHeightForWidth())
        self.push_8.setSizePolicy(sizePolicy)
        self.push_8.setObjectName("push_8")
        self.gridLayout.addWidget(self.push_8, 4, 1, 1, 1)
        self.push_right = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_right.sizePolicy().hasHeightForWidth())
        self.push_right.setSizePolicy(sizePolicy)
        self.push_right.setObjectName("push_right")
        self.gridLayout.addWidget(self.push_right, 4, 6, 1, 1)
        self.push_dot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_dot.sizePolicy().hasHeightForWidth())
        self.push_dot.setSizePolicy(sizePolicy)
        self.push_dot.setObjectName("push_dot")
        self.gridLayout.addWidget(self.push_dot, 7, 1, 1, 1)
        self.push_greater = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_greater.sizePolicy().hasHeightForWidth())
        self.push_greater.setSizePolicy(sizePolicy)
        self.push_greater.setObjectName("push_greater")
        self.gridLayout.addWidget(self.push_greater, 3, 4, 1, 1)
        self.push_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_6.sizePolicy().hasHeightForWidth())
        self.push_6.setSizePolicy(sizePolicy)
        self.push_6.setObjectName("push_6")
        self.gridLayout.addWidget(self.push_6, 5, 3, 1, 1)
        self.push_equal = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_equal.sizePolicy().hasHeightForWidth())
        self.push_equal.setSizePolicy(sizePolicy)
        self.push_equal.setObjectName("push_equal")
        self.gridLayout.addWidget(self.push_equal, 7, 6, 1, 1)
        self.push_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_minus.sizePolicy().hasHeightForWidth())
        self.push_minus.setSizePolicy(sizePolicy)
        self.push_minus.setObjectName("push_minus")
        self.gridLayout.addWidget(self.push_minus, 6, 6, 1, 1)
        self.push_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_9.sizePolicy().hasHeightForWidth())
        self.push_9.setSizePolicy(sizePolicy)
        self.push_9.setObjectName("push_9")
        self.gridLayout.addWidget(self.push_9, 4, 3, 1, 1)
        self.push_lnx = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_lnx.sizePolicy().hasHeightForWidth())
        self.push_lnx.setSizePolicy(sizePolicy)
        self.push_lnx.setObjectName("push_lnx")
        self.gridLayout.addWidget(self.push_lnx, 3, 6, 1, 1)
        self.push_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_0.sizePolicy().hasHeightForWidth())
        self.push_0.setSizePolicy(sizePolicy)
        self.push_0.setObjectName("push_0")
        self.gridLayout.addWidget(self.push_0, 7, 0, 1, 1)
        self.push_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_5.sizePolicy().hasHeightForWidth())
        self.push_5.setSizePolicy(sizePolicy)
        self.push_5.setObjectName("push_5")
        self.gridLayout.addWidget(self.push_5, 5, 1, 1, 1)
        self.push_sinx = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_sinx.sizePolicy().hasHeightForWidth())
        self.push_sinx.setSizePolicy(sizePolicy)
        self.push_sinx.setObjectName("push_sinx")
        self.gridLayout.addWidget(self.push_sinx, 1, 0, 1, 1)
        self.push_logx = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_logx.sizePolicy().hasHeightForWidth())
        self.push_logx.setSizePolicy(sizePolicy)
        self.push_logx.setObjectName("push_logx")
        self.gridLayout.addWidget(self.push_logx, 3, 5, 1, 1)
        self.push_mult = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_mult.sizePolicy().hasHeightForWidth())
        self.push_mult.setSizePolicy(sizePolicy)
        self.push_mult.setObjectName("push_mult")
        self.gridLayout.addWidget(self.push_mult, 5, 5, 1, 1)
        self.push_root = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_root.sizePolicy().hasHeightForWidth())
        self.push_root.setSizePolicy(sizePolicy)
        self.push_root.setObjectName("push_root")
        self.gridLayout.addWidget(self.push_root, 3, 0, 1, 1)
        self.push_ans = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_ans.sizePolicy().hasHeightForWidth())
        self.push_ans.setSizePolicy(sizePolicy)
        self.push_ans.setObjectName("push_ans")
        self.gridLayout.addWidget(self.push_ans, 7, 5, 1, 1)
        self.push_e = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_e.sizePolicy().hasHeightForWidth())
        self.push_e.setSizePolicy(sizePolicy)
        self.push_e.setObjectName("push_e")
        self.gridLayout.addWidget(self.push_e, 6, 4, 1, 1)
        self.push_percent = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_percent.sizePolicy().hasHeightForWidth())
        self.push_percent.setSizePolicy(sizePolicy)
        self.push_percent.setObjectName("push_percent")
        self.gridLayout.addWidget(self.push_percent, 5, 4, 1, 1)
        self.push_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_4.sizePolicy().hasHeightForWidth())
        self.push_4.setSizePolicy(sizePolicy)
        self.push_4.setObjectName("push_4")
        self.gridLayout.addWidget(self.push_4, 5, 0, 1, 1)
        self.push_left = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_left.sizePolicy().hasHeightForWidth())
        self.push_left.setSizePolicy(sizePolicy)
        self.push_left.setObjectName("push_left")
        self.gridLayout.addWidget(self.push_left, 4, 5, 1, 1)
        self.push_xinverse = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_xinverse.sizePolicy().hasHeightForWidth())
        self.push_xinverse.setSizePolicy(sizePolicy)
        self.push_xinverse.setObjectName("push_xinverse")
        self.gridLayout.addWidget(self.push_xinverse, 3, 1, 1, 1)
        self.push_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_clear.sizePolicy().hasHeightForWidth())
        self.push_clear.setSizePolicy(sizePolicy)
        self.push_clear.setObjectName("push_clear")
        self.gridLayout.addWidget(self.push_clear, 2, 6, 1, 1)
        self.push_del = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_del.sizePolicy().hasHeightForWidth())
        self.push_del.setSizePolicy(sizePolicy)
        self.push_del.setObjectName("push_del")
        self.gridLayout.addWidget(self.push_del, 2, 5, 1, 1)
        self.push_lesser = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_lesser.sizePolicy().hasHeightForWidth())
        self.push_lesser.setSizePolicy(sizePolicy)
        self.push_lesser.setObjectName("push_lesser")
        self.gridLayout.addWidget(self.push_lesser, 2, 4, 1, 1)
        self.push_a = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_a.sizePolicy().hasHeightForWidth())
        self.push_a.setSizePolicy(sizePolicy)
        self.push_a.setObjectName("push_a")
        self.gridLayout.addWidget(self.push_a, 2, 0, 1, 1)
        self.push_b = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_b.sizePolicy().hasHeightForWidth())
        self.push_b.setSizePolicy(sizePolicy)
        self.push_b.setObjectName("push_b")
        self.gridLayout.addWidget(self.push_b, 2, 1, 1, 1)
        self.push_c = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_c.sizePolicy().hasHeightForWidth())
        self.push_c.setSizePolicy(sizePolicy)
        self.push_c.setObjectName("push_c")
        self.gridLayout.addWidget(self.push_c, 2, 3, 1, 1)
        self.push_asinx = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_asinx.sizePolicy().hasHeightForWidth())
        self.push_asinx.setSizePolicy(sizePolicy)
        self.push_asinx.setObjectName("push_asinx")
        self.gridLayout.addWidget(self.push_asinx, 1, 4, 1, 1)
        self.push_acosx = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_acosx.sizePolicy().hasHeightForWidth())
        self.push_acosx.setSizePolicy(sizePolicy)
        self.push_acosx.setObjectName("push_acosx")
        self.gridLayout.addWidget(self.push_acosx, 1, 5, 1, 1)
        self.push_atanx = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.push_atanx.sizePolicy().hasHeightForWidth())
        self.push_atanx.setSizePolicy(sizePolicy)
        self.push_atanx.setObjectName("push_atanx")
        self.gridLayout.addWidget(self.push_atanx, 1, 6, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1152, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.push_1.clicked.connect(self.method_1)
        self.push_2.clicked.connect(self.method_2)
        self.push_3.clicked.connect(self.method_3)
        self.push_4.clicked.connect(self.method_4)
        self.push_5.clicked.connect(self.method_5)
        self.push_6.clicked.connect(self.method_6)
        self.push_7.clicked.connect(self.method_7)
        self.push_8.clicked.connect(self.method_8)
        self.push_9.clicked.connect(self.method_9)
        self.push_0.clicked.connect(self.method_0)
        self.push_dot.clicked.connect(self.method_dot)
        self.push_equal.clicked.connect(self.method_equal)
        self.push_plus.clicked.connect(self.method_plus)
        self.push_minus.clicked.connect(self.method_minus)
        self.push_mult.clicked.connect(self.method_mult)
        self.push_div.clicked.connect(self.method_div)
        self.push_left.clicked.connect(self.method_left)
        self.push_right.clicked.connect(self.method_right)
        self.push_del.clicked.connect(self.method_del)
        self.push_clear.clicked.connect(self.method_clear)
        self.push_greater.clicked.connect(self.method_greater)
        self.push_lesser.clicked.connect(self.method_lesser)
        self.push_equalto.clicked.connect(self.method_equalto)
        
        self.push_logx.clicked.connect(self.method_logx)
        self.push_lnx.clicked.connect(self.method_lnx)
        
        self.push_pi.clicked.connect(self.method_pi)
        self.push_e.clicked.connect(self.method_e)
        self.push_power.clicked.connect(self.method_power)
        
        self.push_epowerx.clicked.connect(self.method_epowerx)
        self.push_xinverse.clicked.connect(self.method_xinverse)
        self.push_root.clicked.connect(self.method_root)

        self.push_sinx.clicked.connect(self.method_sinx)
        self.push_cosx.clicked.connect(self.method_cosx)
        self.push_tanx.clicked.connect(self.method_tanx)

        self.push_asinx.clicked.connect(self.method_asinx)
        self.push_acosx.clicked.connect(self.method_acosx)
        self.push_atanx.clicked.connect(self.method_atanx)
        
        

        
        

    def method_1(self):
        text = self.label.text()
        self.label.setText(text+"1")

    def method_2(self):
        text = self.label.text()
        self.label.setText(text+"2")

    def method_3(self):
        text = self.label.text()
        self.label.setText(text+"3")

    def method_4(self):
        text = self.label.text()
        self.label.setText(text+"4")

    def method_5(self):
        text = self.label.text()
        self.label.setText(text+"5")

    def method_6(self):
        text = self.label.text()
        self.label.setText(text+"6")

    def method_7(self):
        text = self.label.text()
        self.label.setText(text+"7")

    def method_8(self):
        text = self.label.text()
        self.label.setText(text+"8")

    def method_9(self):
        text = self.label.text()
        self.label.setText(text+"9")

    def method_0(self):
        text = self.label.text()
        self.label.setText(text+"0")

    def method_dot(self):
        text = self.label.text()
        self.label.setText(text+".")

    def method_plus(self):
        text = self.label.text()
        self.label.setText(text+"+")

    def method_minus(self):
        text = self.label.text()
        self.label.setText(text+"-")

    def method_mult(self):
        text = self.label.text()
        self.label.setText(text+"*")

    def method_div(self):
        text = self.label.text()
        self.label.setText(text+"/")

    def method_clear(self):
        self.label.setText("")

    def method_del(self):
        text = self.label.text()
        self.label.setText(text[:len(text)-1])

    def method_equal(self):
        text = self.label.text()

        try:
            ans = eval(text)
            self.label.setText(str(ans))
        except:
            self.label.setText("Wrong answer")

    def method_left(self):
        text = self.label.text()
        self.label.setText(text+"(")

    def method_right(self):
        text = self.label.text()
        self.label.setText(text+")")

    def method_greater(self):
        text = self.label.text()
        self.label.setText(text+">")

    def method_lesser(self):
        text = self.label.text()
        self.label.setText(text+"<")

    def method_equalto(self):
        text = self.label.text()
        self.label.setText(text+"==")

    def method_logx(self):
        text = self.label.text()
        self.label.setText(str(eval(f"math.log10({text})")))

    def method_lnx(self):
        text = self.label.text()
        self.label.setText(str(eval(f"math.log({text})")))

    
    def method_pi(self):
        text = self.label.text()
        self.label.setText(text+str(math.pi))

    def method_e(self):
        text = self.label.text()
        self.label.setText(text+str(math.e))

    def method_power(self):
        text = self.label.text()
        self.label.setText(text+"**")

    def method_epowerx(self):
        text = self.label.text()
        self.label.setText(str(eval(f"pow({math.e},{text})")))
                           
    def method_xinverse(self):
        text = self.label.text()
        self.label.setText(str(eval(f"1/{text}")))

    def method_root(self):
        text = self.label.text()
        self.label.setText(str(eval(f"pow({text},0.5)")))

    def method_sinx(self):
        text = self.label.text()
        self.label.setText(str(eval(f"math.sin({text})")))

    def method_cosx(self):
        text = self.label.text()
        self.label.setText(str(eval(f"math.cos({text})")))

    def method_tanx(self):
        text = self.label.text()
        self.label.setText(str(eval(f"math.tan({text})")))

    def method_asinx(self):
        text = self.label.text()
        self.label.setText(str(eval(f"math.asin({text})")))

    def method_acosx(self):
        text = self.label.text()
        self.label.setText(str(eval(f"math.acos({text})")))

    def method_atanx(self):
        text = self.label.text()
        self.label.setText(str(eval(f"math.atan({text})")))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scientific Calculator"))
        self.push_pi.setText(_translate("MainWindow", "pi"))
        self.push_1.setText(_translate("MainWindow", "1"))
        self.push_power.setText(_translate("MainWindow", "^"))
        self.push_3.setText(_translate("MainWindow", "3"))
        self.push_7.setText(_translate("MainWindow", "7"))
        self.push_2.setText(_translate("MainWindow", "2"))
        self.push_equalto.setText(_translate("MainWindow", "=="))
        self.push_cosx.setText(_translate("MainWindow", "cos(x)"))
        self.push_plus.setText(_translate("MainWindow", "+"))
        self.push_plus.setShortcut(_translate("MainWindow", "+"))
        self.push_tanx.setText(_translate("MainWindow", "tan(x)"))
        self.push_div.setText(_translate("MainWindow", "÷"))
        self.push_div.setShortcut(_translate("MainWindow", "/"))
        self.push_epowerx.setText(_translate("MainWindow", "e^x"))
        self.push_8.setText(_translate("MainWindow", "8"))
        self.push_right.setText(_translate("MainWindow", ")"))
        self.push_right.setShortcut(_translate("MainWindow", ")"))
        self.push_dot.setText(_translate("MainWindow", "."))
        self.push_greater.setText(_translate("MainWindow", ">"))
        self.push_6.setText(_translate("MainWindow", "6"))
        self.push_equal.setText(_translate("MainWindow", "="))
        self.push_minus.setText(_translate("MainWindow", "-"))
        self.push_minus.setShortcut(_translate("MainWindow", "-"))
        self.push_9.setText(_translate("MainWindow", "9"))
        self.push_lnx.setText(_translate("MainWindow", "lnx"))
        self.push_0.setText(_translate("MainWindow", "0"))
        self.push_5.setText(_translate("MainWindow", "5"))
        self.push_sinx.setText(_translate("MainWindow", "sin(x)"))
        self.push_logx.setText(_translate("MainWindow", "log(x)"))
        self.push_mult.setText(_translate("MainWindow", "x"))
        self.push_mult.setShortcut(_translate("MainWindow", "*"))
        self.push_root.setText(_translate("MainWindow", "Root"))
        self.push_ans.setText(_translate("MainWindow", "Ans"))
        self.push_e.setText(_translate("MainWindow", "e"))
        self.push_percent.setText(_translate("MainWindow", "%"))
        self.push_4.setText(_translate("MainWindow", "4"))
        self.push_left.setText(_translate("MainWindow", "("))
        self.push_left.setShortcut(_translate("MainWindow", "("))
        self.push_xinverse.setText(_translate("MainWindow", "x^-1"))
        self.push_clear.setText(_translate("MainWindow", "Clear"))
        self.push_del.setText(_translate("MainWindow", "Del"))
        self.push_del.setShortcut(_translate("MainWindow", "Backspace"))
        self.push_lesser.setText(_translate("MainWindow", "<"))
        self.push_a.setText(_translate("MainWindow", "a"))
        self.push_b.setText(_translate("MainWindow", "b"))
        self.push_c.setText(_translate("MainWindow", "c"))
        self.push_asinx.setText(_translate("MainWindow", "sin^-1(x)"))
        self.push_acosx.setText(_translate("MainWindow", "cos^-1(x)"))
        self.push_atanx.setText(_translate("MainWindow", "tan^-1(x)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
