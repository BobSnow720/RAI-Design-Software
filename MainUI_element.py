
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 整体窗口的设置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 640)
        MainWindow.setMinimumSize(1070,640)
        MainWindow.setMaximumSize(1070,640)
        MainWindow.setStyleSheet("background-color: rgb(242, 255, 254);")
        # 添加整体控件
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 添加tabWidget控件(调度)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(200, 10, 850, 600))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")

        # -----------------------------左侧按钮--------------------------------------
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(30, 40, 131, 31))
        self.btn_1.setStyleSheet("font: 10pt \"楷体\";selection-background-color: rgb(189, 255, 191);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(30, 120, 131, 31))
        self.btn_2.setStyleSheet("font: 10pt \"楷体\";selection-background-color: rgb(189, 255, 191);")
        self.btn_2.setObjectName("btn_2")
        self.btn_2_pa = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_pa.setGeometry(QtCore.QRect(165, 120, 15, 31))
        self.btn_2_pa.setStyleSheet("font: 10pt \"楷体\";selection-background-color: rgb(189, 255, 191);")
        self.btn_2_pa.setObjectName("btn_2_pa")

        # ----------------------------tab1：Shaper---------------------------------
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setEnabled(True)
        self.tab_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab_1.setObjectName("tab_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        # 调色按钮
        self.back_color = QtWidgets.QPushButton(self.tab_1)
        self.back_color.setGeometry(QtCore.QRect(10, 560, 91, 31))
        self.back_color.setObjectName("back_color")
        self.net_color = QtWidgets.QPushButton(self.tab_1)
        self.net_color.setGeometry(QtCore.QRect(150, 560, 91, 31))
        self.net_color.setObjectName("net_color")
        self.pts_color = QtWidgets.QPushButton(self.tab_1)
        self.pts_color.setGeometry(QtCore.QRect(290, 560, 91, 31))
        self.pts_color.setObjectName("pts_color")
        # 主控按钮
        self.Read = QtWidgets.QPushButton(self.tab_1)
        self.Read.setGeometry(QtCore.QRect(450, 10, 121, 31))
        self.Read.setObjectName("Read")
        self.Clear = QtWidgets.QPushButton(self.tab_1)
        self.Clear.setGeometry(QtCore.QRect(590, 10, 121, 31))
        self.Clear.setObjectName("Clear")
        self.Putoo = QtWidgets.QPushButton(self.tab_1)
        self.Putoo.setGeometry(QtCore.QRect(450, 70, 261, 31))
        self.Putoo.setObjectName("Putoo")
        self.Reshape = QtWidgets.QPushButton(self.tab_1)
        self.Reshape.setGeometry(QtCore.QRect(450, 335, 261, 31))
        self.Reshape.setObjectName("Reshape")
        # 位姿按钮
        self.Move = QtWidgets.QPushButton(self.tab_1)
        self.Move.setGeometry(QtCore.QRect(450, 110, 91, 31))
        self.Move.setObjectName("Move")
        self.Rotate = QtWidgets.QPushButton(self.tab_1)
        self.Rotate.setGeometry(QtCore.QRect(620, 110, 91, 31))
        self.Rotate.setObjectName("Rotate")
        self.xmov = QtWidgets.QLineEdit(self.tab_1)
        self.xmov.setGeometry(QtCore.QRect(470, 160, 71, 21))
        self.xmov.setObjectName("xmov")
        self.ymov = QtWidgets.QLineEdit(self.tab_1)
        self.ymov.setGeometry(QtCore.QRect(470, 200, 71, 21))
        self.ymov.setObjectName("ymov")
        self.zmov = QtWidgets.QLineEdit(self.tab_1)
        self.zmov.setGeometry(QtCore.QRect(470, 240, 71, 21))
        self.zmov.setObjectName("zmov")
        self.yrott = QtWidgets.QLineEdit(self.tab_1)
        self.yrott.setGeometry(QtCore.QRect(620, 200, 91, 21))
        self.yrott.setObjectName("yrott")
        self.zrott = QtWidgets.QLineEdit(self.tab_1)
        self.zrott.setGeometry(QtCore.QRect(620, 240, 91, 21))
        self.zrott.setObjectName("zrott")
        self.xrott = QtWidgets.QLineEdit(self.tab_1)
        self.xrott.setGeometry(QtCore.QRect(620, 160, 91, 21))
        self.xrott.setObjectName("xrott")
        self.Ydirct = QtWidgets.QPushButton(self.tab_1)
        self.Ydirct.setGeometry(QtCore.QRect(450, 270, 31, 31))
        self.Ydirct.setObjectName("Ydirct")
        self.ZLP = QtWidgets.QPushButton(self.tab_1)
        self.ZLP.setGeometry(QtCore.QRect(490, 270, 31, 31))
        self.ZLP.setObjectName("ZLP")
        self.ZLN = QtWidgets.QPushButton(self.tab_1)
        self.ZLN.setGeometry(QtCore.QRect(530, 270, 31, 31))
        self.ZLN.setObjectName("ZLN")
        self.ZMP = QtWidgets.QPushButton(self.tab_1)
        self.ZMP.setGeometry(QtCore.QRect(570, 270, 31, 31))
        self.ZMP.setObjectName("ZMP")
        self.ZMN = QtWidgets.QPushButton(self.tab_1)
        self.ZMN.setGeometry(QtCore.QRect(610, 270, 31, 31))
        self.ZMN.setObjectName("ZMN")
        self.ZSP = QtWidgets.QPushButton(self.tab_1)
        self.ZSP.setGeometry(QtCore.QRect(650, 270, 31, 31))
        self.ZSP.setObjectName("ZSP")
        self.ZSN = QtWidgets.QPushButton(self.tab_1)
        self.ZSN.setGeometry(QtCore.QRect(690, 270, 31, 31))
        self.ZSN.setObjectName("ZSN")
        # 变径参数
        self.expand = QtWidgets.QLineEdit(self.tab_1)
        self.expand.setGeometry(QtCore.QRect(450, 400, 91, 21))
        self.expand.setObjectName("expand")
        self.shrink = QtWidgets.QLineEdit(self.tab_1)
        self.shrink.setGeometry(QtCore.QRect(620, 400, 91, 21))
        self.shrink.setObjectName("shrink")
        # 最大圆
        self.BiggestCircle = QtWidgets.QPushButton(self.tab_1)
        self.BiggestCircle.setGeometry(QtCore.QRect(450, 460, 100, 41))
        self.BiggestCircle.setObjectName("BiggestCircle")
        self.label_cir = QtWidgets.QLabel(self.tab_1)
        self.label_cir.setGeometry(QtCore.QRect(560, 460, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_cir.setFont(font)
        self.label_cir.setObjectName("label_cir")
        # 存储
        self.SavePCD = QtWidgets.QPushButton(self.tab_1)
        self.SavePCD.setGeometry(QtCore.QRect(450, 520, 261, 41))
        self.SavePCD.setObjectName("SavePCD")
        # 界面内注释内容
        self.label_x = QtWidgets.QLabel(self.tab_1)
        self.label_x.setGeometry(QtCore.QRect(450, 160, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_x.setFont(font)
        self.label_x.setObjectName("label_x")
        self.label_y = QtWidgets.QLabel(self.tab_1)
        self.label_y.setGeometry(QtCore.QRect(450, 200, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_y.setFont(font)
        self.label_y.setObjectName("label_y")
        self.label_z = QtWidgets.QLabel(self.tab_1)
        self.label_z.setGeometry(QtCore.QRect(450, 240, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_z.setFont(font)
        self.label_z.setObjectName("label_z")
        self.label_ev = QtWidgets.QLabel(self.tab_1)
        self.label_ev.setGeometry(QtCore.QRect(450, 370, 101, 21))
        self.label_ev.setObjectName("label_ev")
        self.label_sv = QtWidgets.QLabel(self.tab_1)
        self.label_sv.setGeometry(QtCore.QRect(620, 370, 101, 21))
        self.label_sv.setObjectName("label_sv")
        ### 添加tab1
        self.tabWidget.addTab(self.tab_1, "")    # 把tab_2加到tabWidget中


        # -------------------------------tab2：Abutment--------------------------------------
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_22")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 541))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 注释和数值输入
        self.label_filt = QtWidgets.QLabel(self.tab_2)
        self.label_filt.setGeometry(QtCore.QRect(420, 20, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_filt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_filt.setFont(font)
        self.label_filt.setObjectName("label_filt")
        self.Value_filt = QtWidgets.QLineEdit(self.tab_2)
        self.Value_filt.setGeometry(QtCore.QRect(500, 20, 71, 21))
        self.Value_filt.setObjectName("Value_filt")

        self.label_end = QtWidgets.QLabel(self.tab_2)
        self.label_end.setGeometry(QtCore.QRect(620, 20, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_end.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_end.setFont(font)
        self.label_end.setObjectName("label_end")
        self.Value_end = QtWidgets.QLineEdit(self.tab_2)
        self.Value_end.setGeometry(QtCore.QRect(700, 20, 71, 21))
        self.Value_end.setObjectName("Value_end")

        self.label_begn = QtWidgets.QLabel(self.tab_2)
        self.label_begn.setGeometry(QtCore.QRect(420, 60, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_begn.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_begn.setFont(font)
        self.label_begn.setObjectName("label_begn")
        self.Value_begn = QtWidgets.QLineEdit(self.tab_2)
        self.Value_begn.setGeometry(QtCore.QRect(500, 60, 71, 21))
        self.Value_begn.setObjectName("Value_begn")

        self.label_cir3 = QtWidgets.QLabel(self.tab_2)
        self.label_cir3.setGeometry(QtCore.QRect(620, 60, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_cir3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_cir3.setFont(font)
        self.label_cir3.setObjectName("label_cir3")
        self.Value_cir3 = QtWidgets.QLineEdit(self.tab_2)
        self.Value_cir3.setGeometry(QtCore.QRect(700, 60, 71, 21))
        self.Value_cir3.setObjectName("Value_cir3")

        self.label_c_H = QtWidgets.QLabel(self.tab_2)
        self.label_c_H.setGeometry(QtCore.QRect(420, 100, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_c_H.setFont(font)
        self.label_c_H.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_c_H.setObjectName("label_c_H")
        self.Value_c_H = QtWidgets.QLineEdit(self.tab_2)
        self.Value_c_H.setGeometry(QtCore.QRect(500, 100, 71, 21))
        self.Value_c_H.setObjectName("Value_c_H")
        self.label_c_Hr = QtWidgets.QLabel(self.tab_2)
        self.label_c_Hr.setGeometry(QtCore.QRect(580, 100, 50, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_c_Hr.setFont(font)
        self.label_c_Hr.setObjectName("label_c_Hr")

        self.label_h2 = QtWidgets.QLabel(self.tab_2)
        self.label_h2.setGeometry(QtCore.QRect(620, 100, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_h2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_h2.setFont(font)
        self.label_h2.setObjectName("label_h2")
        self.Value_h2 = QtWidgets.QLineEdit(self.tab_2)
        self.Value_h2.setGeometry(QtCore.QRect(700, 100, 71, 21))
        self.Value_h2.setObjectName("Value_h2")

        self.label_h1 = QtWidgets.QLabel(self.tab_2)
        self.label_h1.setGeometry(QtCore.QRect(420, 140, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_h1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_h1.setFont(font)
        self.label_h1.setObjectName("label_h1")
        self.Value_h1 = QtWidgets.QLineEdit(self.tab_2)
        self.Value_h1.setGeometry(QtCore.QRect(500, 140, 71, 21))
        self.Value_h1.setObjectName("Value_h1")

        self.label_alph = QtWidgets.QLabel(self.tab_2)
        self.label_alph.setGeometry(QtCore.QRect(620, 140, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_alph.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_alph.setFont(font)
        self.label_alph.setObjectName("label_alph")
        self.Value_alph = QtWidgets.QLineEdit(self.tab_2)
        self.Value_alph.setGeometry(QtCore.QRect(700, 140, 71, 21))
        self.Value_alph.setObjectName("Value_alph")

        self.label_h_H = QtWidgets.QLabel(self.tab_2)
        self.label_h_H.setGeometry(QtCore.QRect(420, 180, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_h_H.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_h_H.setFont(font)
        self.label_h_H.setObjectName("label_h_H")
        self.Value_h_H = QtWidgets.QLineEdit(self.tab_2)
        self.Value_h_H.setGeometry(QtCore.QRect(500, 180, 71, 21))
        self.Value_h_H.setObjectName("Value_h_H")

        self.label_h_L = QtWidgets.QLabel(self.tab_2)
        self.label_h_L.setGeometry(QtCore.QRect(620, 180, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_h_L.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_h_L.setFont(font)
        self.label_h_L.setObjectName("label_h_L")
        self.Value_h_L = QtWidgets.QLineEdit(self.tab_2)
        self.Value_h_L.setGeometry(QtCore.QRect(700, 180, 71, 21))
        self.Value_h_L.setObjectName("Value_h_L")

        self.label_a = QtWidgets.QLabel(self.tab_2)
        self.label_a.setGeometry(QtCore.QRect(420, 220, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_a.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_a.setFont(font)
        self.label_a.setObjectName("label_a")
        self.Value_a = QtWidgets.QLineEdit(self.tab_2)
        self.Value_a.setGeometry(QtCore.QRect(500, 220, 71, 21))
        self.Value_a.setObjectName("Value_a")

        self.label_b = QtWidgets.QLabel(self.tab_2)
        self.label_b.setGeometry(QtCore.QRect(620, 220, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_b.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_b.setFont(font)
        self.label_b.setObjectName("label_b")
        self.Value_b = QtWidgets.QLineEdit(self.tab_2)
        self.Value_b.setGeometry(QtCore.QRect(700, 220, 71, 21))
        self.Value_b.setObjectName("Value_b")

        self.label_dwci = QtWidgets.QLabel(self.tab_2)
        self.label_dwci.setGeometry(QtCore.QRect(420, 260, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_dwci.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_dwci.setFont(font)
        self.label_dwci.setObjectName("label_dwci")
        self.Value_dwci = QtWidgets.QLineEdit(self.tab_2)
        self.Value_dwci.setGeometry(QtCore.QRect(500, 260, 71, 21))
        self.Value_dwci.setObjectName("Value_dwci")
        self.label_dwcir = QtWidgets.QLabel(self.tab_2)
        self.label_dwcir.setGeometry(QtCore.QRect(580, 260, 50, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_dwcir.setFont(font)
        self.label_dwcir.setObjectName("label_dwcir")

        self.label_h3 = QtWidgets.QLabel(self.tab_2)
        self.label_h3.setGeometry(QtCore.QRect(620, 260, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_h3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_h3.setFont(font)
        self.label_h3.setObjectName("label_h3")
        self.Value_h3 = QtWidgets.QLineEdit(self.tab_2)
        self.Value_h3.setGeometry(QtCore.QRect(700, 260, 71, 21))
        self.Value_h3.setObjectName("Value_h3")

        self.label_beta = QtWidgets.QLabel(self.tab_2)
        self.label_beta.setGeometry(QtCore.QRect(420, 300, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_beta.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_beta.setFont(font)
        self.label_beta.setObjectName("label_beta")
        self.Value_beta = QtWidgets.QLineEdit(self.tab_2)
        self.Value_beta.setGeometry(QtCore.QRect(500, 300, 71, 21))
        self.Value_beta.setObjectName("Value_beta")

        self.label_cir1 = QtWidgets.QLabel(self.tab_2)
        self.label_cir1.setGeometry(QtCore.QRect(620, 300, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_cir1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_cir1.setFont(font)
        self.label_cir1.setObjectName("label_cir1")
        self.Value_cir1 = QtWidgets.QLineEdit(self.tab_2)
        self.Value_cir1.setGeometry(QtCore.QRect(700, 300, 71, 21))
        self.Value_cir1.setObjectName("Value_cir1")
#################################################################################################

        # 按钮
        self.parmtrclear = QtWidgets.QPushButton(self.tab_2)
        self.parmtrclear.setGeometry(QtCore.QRect(450, 440, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.parmtrclear.setFont(font)
        self.parmtrclear.setObjectName("parmtrclear")

        self.recomn = QtWidgets.QPushButton(self.tab_2)
        self.recomn.setGeometry(QtCore.QRect(630, 440, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recomn.setFont(font)
        self.recomn.setObjectName("recomn")

        self.create = QtWidgets.QPushButton(self.tab_2)
        self.create.setGeometry(QtCore.QRect(450, 520, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.create.setFont(font)
        self.create.setObjectName("create")

        self.save = QtWidgets.QPushButton(self.tab_2)
        self.save.setGeometry(QtCore.QRect(630, 520, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save.setFont(font)
        self.save.setObjectName("save")

        ### 插入tab_2
        self.tabWidget.addTab(self.tab_2, "")

             # ------------------------------- Abut-help -------------------------------------
        self.tab_2_pa = QtWidgets.QWidget()
        self.tab_2_pa.setObjectName("tab_22")
        self.horizontalLayoutWidget_pa = QtWidgets.QWidget(self.tab_2_pa)
        self.horizontalLayoutWidget_pa.setGeometry(QtCore.QRect(10, 10, 824, 576))
        self.horizontalLayoutWidget_pa.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_pa = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_pa)
        self.horizontalLayout_pa.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_pa.setObjectName("horizontalLayout_pa")
        # QtCore, QtGui, QtWidgets
        self.image_pa = QtGui.QPixmap("image/Abutment Parameters.png")
        self.QLabel_pa = QtWidgets.QLabel(self.tab_2_pa)
        self.QLabel_pa.setGeometry(QtCore.QRect(0, 0, 830, 580))
        self.QLabel_pa.setPixmap(self.image_pa)
        self.QLabel_pa.setScaledContents(True)
        self.tabWidget.addTab(self.tab_2_pa, "")


        # --------------------------------------结尾-------------------------------------
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # tab
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Tab_1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab_2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2_pa), _translate("MainWindow", "Tab_3"))
        # 左侧按钮
        self.btn_1.setText(_translate("MainWindow", "Implant:Ajuster"))
        self.btn_2.setText(_translate("MainWindow", "Abutment:Designer"))
        self.btn_2_pa.setText(_translate("MainWindow", "!"))

        #---------------------------二级控件：Shaper----------------------------------
        # 调色按钮
        self.back_color.setText(_translate("Mainwindow", "back_color"))
        self.net_color.setText(_translate("Mainwindow", "net_color"))
        self.pts_color.setText(_translate("Mainwindow", "pts_color"))
        # 主控按钮
        self.Read.setText(_translate("Mainwindow", "Read"))
        self.Clear.setText(_translate("Mainwindow", "Clear"))
        self.Putoo.setText(_translate("Mainwindow", "Putoo"))
        self.Reshape.setText(_translate("Mainwindow", "Reshape"))
        # 位姿按钮
        self.Move.setText(_translate("Mainwindow", "Move"))
        self.Rotate.setText(_translate("Mainwindow", "Rotate"))
        self.Ydirct.setText(_translate("Mainwindow", "Y+"))
        self.ZLP.setText(_translate("Mainwindow", "1+"))
        self.ZLN.setText(_translate("Mainwindow", "1-"))
        self.ZMP.setText(_translate("Mainwindow", ".1+"))
        self.ZMN.setText(_translate("Mainwindow", ".1-"))
        self.ZSP.setText(_translate("Mainwindow", ".01+"))
        self.ZSN.setText(_translate("Mainwindow", ".01-"))
        # 最大圆
        self.BiggestCircle.setText(_translate("Mainwindow", "BiggestCircle"))
        self.label_cir.setText(_translate("Mainwindow", "CircleRadius"))
        # 存储
        self.SavePCD.setText(_translate("Mainwindow", "SavePCD"))
        # 界面内注释内容
        self.label_x.setText(_translate("Mainwindow", "x"))
        self.label_y.setText(_translate("Mainwindow", "y"))
        self.label_z.setText(_translate("Mainwindow", "z"))
        self.label_ev.setText(_translate("Mainwindow", "Expansion Value"))
        self.label_sv.setText(_translate("Mainwindow", "Shrinkage Value"))


        #-------------------------二级控件：Abutment------------------------------------
        self.label_filt.setText(_translate("Mainwindow", "r_Filt"))
        self.Value_filt.setPlaceholderText("     1")
        # self.Value_filt.setFocus()

        self.label_end.setText(_translate("Mainwindow", "l_T_Tag"))
        self.Value_end.setPlaceholderText("     2")

        self.label_begn.setText(_translate("Mainwindow", "l_D_Tag"))
        self.Value_begn.setPlaceholderText("     3")
        self.label_cir3.setText(_translate("Mainwindow", "rT_DCon"))
        self.Value_cir3.setPlaceholderText("     4")

        self.label_c_H.setText(_translate("Mainwindow", "r_Hex"))
        self.Value_c_H.setPlaceholderText("     5")
        self.label_c_Hr.setText(_translate("Mainwindow", "RecVal"))
        self.label_h2.setText(_translate("Mainwindow", "h_DCon"))
        self.Value_h2.setPlaceholderText("     6")

        self.label_h1.setText(_translate("Mainwindow", "h_Hex"))
        self.Value_h1.setPlaceholderText("     7")
        self.label_alph.setText(_translate("Mainwindow", "alph_D"))
        self.Value_alph.setPlaceholderText("     8")

        self.label_h_H.setText(_translate("Mainwindow", "h_T_Cur"))
        self.Value_h_H.setPlaceholderText("     9")
        self.label_h_L.setText(_translate("Mainwindow", "h_D_Cur"))
        self.Value_h_L.setPlaceholderText("     10")

        self.label_a.setText(_translate("Mainwindow", "rs_Elip"))
        self.Value_a.setPlaceholderText("     11")
        self.label_b.setText(_translate("Mainwindow", "rl_Elip"))
        self.Value_b.setPlaceholderText("     12")

        self.label_dwci.setText(_translate("Mainwindow", "rD_TCon"))
        self.Value_dwci.setPlaceholderText("     13")
        self.label_dwcir.setText(_translate("Mainwindow", "RecVal"))
        self.label_h3.setText(_translate("Mainwindow", "h_TCon"))
        self.Value_h3.setPlaceholderText("     14")

        self.label_beta.setText(_translate("Mainwindow", "beta_T"))
        self.Value_beta.setPlaceholderText("     15")
        self.label_cir1.setText(_translate("Mainwindow", "r_Cylin"))
        self.Value_cir1.setPlaceholderText("     16")

        self.parmtrclear.setText(_translate("Mainwindow", "clear"))
        self.recomn.setText(_translate("Mainwindow", "Recomn"))
        self.create.setText(_translate("Mainwindow", "Create"))
        self.save.setText(_translate("Mainwindow", "Save"))





