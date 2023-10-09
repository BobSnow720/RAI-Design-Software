
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QColorDialog

import math

import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.opengl import GLViewWidget, GLAxisItem, GLGridItem

from OCC.Display.backend import load_backend
load_backend("qt-pyqt5")
import OCC.Display.qtDisplay as OCC_qtDisplay
from OCC.Core.Quantity import (
    Quantity_Color,
    Quantity_TOC_RGB
)

import selfmadeformat as sf
import ptsconfg
import abutcalcltor as abcal
import STL_r_w

from MainUI_element import Ui_MainWindow


class MainCode(QMainWindow, Ui_MainWindow):  # MainUi为qt designer生成的主界面设计文件的.py文件
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.status = self.statusBar()
        # self.setWindowTitle("Dental Assistant v1.0")
        self.setWindowTitle("3D打印种植牙根辅助设计软件")
        self.setWindowIcon(QIcon('example/pythongui/images/tubiao.png'))  # 设置窗体标题图标
        self.tabWidget.tabBar().hide()
        self.tabWidget.setCurrentIndex(0)
        # ------------------------------ 按钮触发函数 -----------------------------------
        self.btn_1.clicked.connect(self.menu_open1_clicked)  # 连接f1函数
        self.btn_2.clicked.connect(self.menu_open2_clicked)  # 连接f1函数
        self.btn_2_pa.clicked.connect(self.menu_open3_clicked)  # 连接f1函数

        # 连接到信号槽
        self.connect_signals()


        # ------------------------------ 二级控制：Shaper -----------------------------------
        self.graphicsView = GLViewWidget(self)
        self.pcr = (0.45, 0.35, 0.21)  # 定义颜色参数
        self.gridcr = (0, 200, 255)
          # 初始化
        self.mid_background_well()
        self.graphicsView.setCameraPosition(distance=20, elevation=12, azimuth=45)
        self.graphicsView.setBackgroundColor(0, 50, 50)
        self.gridLayout.addWidget(self.graphicsView, 0, 0)




        # ------------------------------ 二级控制：Abutment -----------------------------------
          # 画布内容
        self.canvas = OCC_qtDisplay.qtViewer3d(self)
        self.horizontalLayout.addWidget(self.canvas)
        self.canvas.resize(371, 611)
        self.canvas.InitDriver()
        self.display = self.canvas._display
          # 背景颜色设置
        self.color = Quantity_Color(0,10/255,10/255,Quantity_TOC_RGB)
        self.display.View.SetBackgroundColor(self.color)
        # self.display.Repaint()
          # 自动跳转输入
        self.AbutParaInput()
        # ------------------------------ 二级控制：Abut-help -----------------------------------
        self.horizontalLayout_pa.addWidget(self.QLabel_pa)



    # ---------------------------------- 一级控制 -------------------------------------------
    def menu_open1_clicked(self):
        self.tabWidget.setCurrentIndex(0)
    def menu_open2_clicked(self):
        self.tabWidget.setCurrentIndex(1)
        self.Value_filt.setFocus()  # 实现跳转到页面后可以直接开始输入
    def menu_open3_clicked(self):
        self.tabWidget.setCurrentIndex(2)

    def AbutParaInput(self):
        self.Value_filt.returnPressed.connect(self.Value_end.setFocus)
        self.Value_end.returnPressed.connect(self.Value_begn.setFocus)
        self.Value_begn.returnPressed.connect(self.Value_cir3.setFocus)
        self.Value_cir3.returnPressed.connect(self.Value_c_H.setFocus)
        self.Value_c_H.returnPressed.connect(self.Value_h2.setFocus)
        self.Value_h2.returnPressed.connect(self.Value_h1.setFocus)
        self.Value_h1.returnPressed.connect(self.Value_alph.setFocus)
        self.Value_alph.returnPressed.connect(self.Value_h_H.setFocus)
        self.Value_h_H.returnPressed.connect(self.Value_h_L.setFocus)
        self.Value_h_L.returnPressed.connect(self.Value_a.setFocus)
        self.Value_a.returnPressed.connect(self.Value_b.setFocus)
        self.Value_b.returnPressed.connect(self.Value_dwci.setFocus)
        self.Value_dwci.returnPressed.connect(self.Value_h3.setFocus)
        self.Value_h3.returnPressed.connect(self.Value_beta.setFocus)
        self.Value_beta.returnPressed.connect(self.Value_cir1.setFocus)


    def connect_signals(self):
        # Shaper部分
        self.Read.clicked.connect(self.Read_clicked)
        self.Clear.clicked.connect(self.Clear_clicked)
        self.Putoo.clicked.connect(self.Putoo_clicked)
        self.Reshape.clicked.connect(self.Reshape_clicked)
        self.SavePCD.clicked.connect(self.SavePCD_clicked)
        self.Move.clicked.connect(self.Move_clicked)
        self.Rotate.clicked.connect(self.Rotate_clicked)
        self.BiggestCircle.clicked.connect(self.BiggestCircle_clicked)
        self.Ydirct.clicked.connect(self.Ydirct_clicked)
        self.ZLP.clicked.connect(self.ZLP_clicked)
        self.ZLN.clicked.connect(self.ZLN_clicked)
        self.ZMP.clicked.connect(self.ZMP_clicked)
        self.ZMN.clicked.connect(self.ZMN_clicked)
        self.ZSP.clicked.connect(self.ZSP_clicked)
        self.ZSN.clicked.connect(self.ZSN_clicked)
        self.back_color.clicked.connect(self.back_color_clicked)
        self.net_color.clicked.connect(self.net_color_clicked)
        self.pts_color.clicked.connect(self.pts_color_clicked)
        # Abutment部分
        self.parmtrclear.clicked.connect(self.parmtrclear_clicked)
        self.recomn.clicked.connect(self.recomn_clicked)
        self.create.clicked.connect(self.create_clicked)
        self.save.clicked.connect(self.save_clicked)


    # --------------------------------- 二级函数：Shaper ------------------------------------
    def pts_color_clicked(self):
        color = QColorDialog.getColor()
        if color.isValid():
            print("所选颜色为：", color.name())
            hex_color = color.name()
            rgb_color = sf.hex_to_rgb(hex_color)
            self.pcr = sf.rgb_to_decimal(rgb_color)
            print("---:",self.pcr)
            # self.graphicsView.removeItem(self.plot)
            self.graphicsView.removeItem(self.mesh)
            # self.plot.setData(pos=self.np_points, color=(self.pcr[0], self.pcr[1], self.pcr[2], 1), size=0.00005, pxMode=False)
            # self.graphicsView.addItem(self.plot)
            self.mesh = gl.GLMeshItem(vertexes=self.np_points, drawEdges=True, faces=self.faces, smooth=False,
                                      edgeColor=(0.2, 0.2, 0.1, 1.0), color=(self.pcr[0], self.pcr[1], self.pcr[2], 1))
            self.graphicsView.addItem(self.mesh)
        else:
            print("没有选择颜色。")
            return
    def net_color_clicked(self):
        color = QColorDialog.getColor()
        if color.isValid():
            print("所选颜色为：", color.name())
            hex_color = color.name()
            self.gridcr = sf.hex_to_rgb(hex_color)
            self.graphicsView.removeItem(self.grid)
            self.grid = GLGridItem(color=(self.gridcr[0], self.gridcr[1], self.gridcr[2], 100))
            self.grid.setSize(20, 20, 1)
            self.grid.setSpacing(1, 1, 1)
            self.graphicsView.addItem(self.grid)
        else:
            print("没有选择颜色。")
            return
    def back_color_clicked(self):
        color = QColorDialog.getColor()
        if color.isValid():
            print("所选颜色为：", color.name())
            hex_color = color.name()
            rgb_color = sf.hex_to_rgb(hex_color)
            print(rgb_color)
            self.graphicsView.setBackgroundColor(rgb_color[0], rgb_color[1], rgb_color[2])
        else:
            print("没有选择颜色。")
            return
    # 按钮对应函数
    def BiggestCircle_clicked(self):
        self.graphicsView.clear()
        self.mid_background_well()
        aimpt = ptsconfg.ptsincirc(self.np_points)
        # aimpt[2] = 1000 * aimpt[2]
        self.label_cir.setText("R = %.3f mm" % aimpt[2])
        mov = aimpt[:]
        mov[2] = 0
        self.np_points = self.np_points - mov
        # self.plot.setData(pos=self.np_points, color=(self.pcr[0], self.pcr[1], self.pcr[2], 1), size=0.00005, pxMode=False)
        # self.graphicsView.addItem(self.plot)
        self.mesh = gl.GLMeshItem(vertexes=self.np_points, drawEdges=True, faces=self.faces, smooth=False,
                                  edgeColor=(0.2, 0.2, 0.1, 1.0), color=(self.pcr[0], self.pcr[1], self.pcr[2], 1))
        self.graphicsView.addItem(self.mesh)
    def Move_clicked(self):
        self.graphicsView.clear()
        self.mid_background_well()
        dir = ['','','']
        dir[0] = self.xmov.text()
        dir[1] = self.ymov.text()
        dir[2] = self.zmov.text()
        for i in range(3):
            self.MoAction(dir[i], i)
        # self.plot.setData(pos=self.np_points, color=(self.pcr[0], self.pcr[1], self.pcr[2], 1), size=0.00005, pxMode=False)
        # self.graphicsView.addItem(self.plot)
        self.mesh = gl.GLMeshItem(vertexes=self.np_points, drawEdges=True, faces=self.faces, smooth=False,
                                  edgeColor=(0.2, 0.2, 0.1, 1.0), color=(self.pcr[0], self.pcr[1], self.pcr[2], 1))
        self.graphicsView.addItem(self.mesh)
    def Rotate_clicked(self):
        self.graphicsView.clear()
        self.mid_background_well()
        dir = ['', '', '']
        dir[0] = self.xrott.text()
        dir[1] = self.yrott.text()
        dir[2] = self.zrott.text()
        for i in range(3):
            self.RoAction(dir[i], i)
        # self.plot.setData(pos=self.np_points, color=(self.pcr[0], self.pcr[1], self.pcr[2], 1), size=0.00005, pxMode=False)
        # self.graphicsView.addItem(self.plot)
        self.mesh = gl.GLMeshItem(vertexes=self.np_points, drawEdges=True, faces=self.faces, smooth=False,
                                  edgeColor=(0.2, 0.2, 0.1, 1.0), color=(self.pcr[0], self.pcr[1], self.pcr[2], 1))
        self.graphicsView.addItem(self.mesh)
    def Read_clicked(self):
        fileName, filetype = QFileDialog.getOpenFileName\
            (self, "Please Select Point Cloud File：", '.', "All Files(*);;")
        if fileName != '':
            # self.pcd = o3d.io.read_point_cloud(fileName)
            # self.np_points = np.asarray(self.pcd.points)
            self.pts = STL_r_w.Read_stl(fileName)
            self.np_points = self.pts[0].reshape(-1, 3)
            # self.plot = gl.GLScatterPlotItem()
            # self.plot.setData(pos=self.np_points, color=(self.pcr[0], self.pcr[1], self.pcr[2], 1), size=0.00005, pxMode=False)
            # self.graphicsView.addItem(self.plot)
            self.faces = STL_r_w.stl_faces(self.np_points)
            self.mesh = gl.GLMeshItem(vertexes=self.np_points, drawEdges=True, faces=self.faces, smooth=False,
                                      edgeColor=(0.2, 0.2, 0.1, 1.0), color=(self.pcr[0], self.pcr[1], self.pcr[2], 1))
            self.graphicsView.addItem(self.mesh)
    def Clear_clicked(self):
        self.graphicsView.clear()  # 这个clear，不会清除”graphicsView“的背景颜色、相机视角和距离信息
        self.mid_background_well()
    def Putoo_clicked(self):
        self.graphicsView.clear()
        self.mid_background_well()
        self.np_points = ptsconfg.ptscof(self.np_points)
        # self.plot.setData(pos=self.np_points, color=(self.pcr[0], self.pcr[1], self.pcr[2], 1), size=0.00005, pxMode=False)
        # self.graphicsView.addItem(self.plot)
        # self.faces = STL_r_w.stl_faces(self.np_points)
        self.mesh = gl.GLMeshItem(vertexes=self.np_points, drawEdges=True, faces=self.faces, smooth=False,
                                  edgeColor=(0.2, 0.2, 0.1, 1.0), color=(self.pcr[0], self.pcr[1], self.pcr[2], 1))
        self.graphicsView.addItem(self.mesh)
    def Reshape_clicked(self):
        self.graphicsView.clear()
        self.mid_background_well()
        self.np_points = ptsconfg.ptsshape(self.np_points,self.expand.text(),self.shrink.text())
        # self.plot.setData(pos=self.np_points, color=(self.pcr[0], self.pcr[1], self.pcr[2], 1), size=0.00005, pxMode=False)
        # self.graphicsView.addItem(self.plot)
        self.mesh = gl.GLMeshItem(vertexes=self.np_points, drawEdges=True, faces=self.faces, smooth=False,
                                  edgeColor=(0.2, 0.2, 0.1, 1.0), color=(self.pcr[0], self.pcr[1], self.pcr[2], 1))
        self.graphicsView.addItem(self.mesh)
    def SavePCD_clicked(self):
        fileName,fileType = QFileDialog.getSaveFileName\
            (self,"Save As：",'',"STL Files(*.stl);;PCD Files(*.pcd);;PLY Files(*.ply);;All Files(*)")
        print(fileType)
        if fileName != '':
            if fileType == "STL Files(*.stl)":
                self.fanorms = STL_r_w.fanorm_calculator(self.np_points)
                STL_r_w.stl_save(self.np_points, self.fanorms, fileName)
            # if fileType =="PCD Files(*.pcd)":
            #     sf.PriPCD(self.np_points,fileName)
            # if fileType == "PLY Files(*.ply)":
            #     sf.PriPLY(self.np_points,fileName)

    def mid_background_well(self):
        # 坐标轴
        axis = GLAxisItem(size=pg.Vector(12, 12, 15))
        self.graphicsView.addItem(axis)
        # XOY平面的网格
        self.grid = GLGridItem(color=(self.gridcr[0], self.gridcr[1], self.gridcr[2], 100))
        self.grid.setSize(20, 20, 1)
        self.grid.setSpacing(1, 1, 1)
        self.graphicsView.addItem(self.grid)

    def MoAction(self,text,ax):
        if text != "":
            cha = [0,0,0]
            text_num = float(text)
            cha[ax] = text_num
            self.np_points = self.np_points + cha
    def RoAction(self,text,ax):
        if text != "":
            text_num = float(text)
            rad = math.radians(text_num)
            self.np_points = sf.RotWhole(self.np_points, rad, ax)

    # 微调函数
    def Ydirct_clicked(self):
        try:
            # self.graphicsView.clear()
            # self.mid_background_well()
            self.graphicsView.setCameraPosition(distance=20, elevation=0, azimuth=90)
            # self.plot.setData(pos=self.np_points, color=(self.pcr[0], self.pcr[1], self.pcr[2], 1), size=0.00005,pxMode=False)
            # self.graphicsView.addItem(self.plot)
            # self.mesh = gl.GLMeshItem(vertexes=self.np_points, drawEdges=True, faces=self.faces, smooth=False)
            # self.graphicsView.addItem(self.mesh)
        except Exception as e:
            print("Warning：", str(e))

    def ZLP_clicked(self):
        self.graphicsView.clear()
        self.mid_background_well()
        self.np_points = self.np_points + [0, 0, 1.0]
        # self.plot.setData(pos=self.np_points, color=(self.pcr[0], self.pcr[1], self.pcr[2], 1), size=0.00005, pxMode=False)
        # self.graphicsView.addItem(self.plot)
        self.mesh = gl.GLMeshItem(vertexes=self.np_points, drawEdges=True, faces=self.faces, smooth=False,
                                  edgeColor=(0.2, 0.2, 0.1, 1.0), color=(self.pcr[0], self.pcr[1], self.pcr[2], 1))
        self.graphicsView.addItem(self.mesh)
    def ZLN_clicked(self):
        self.graphicsView.clear()
        self.mid_background_well()
        self.np_points = self.np_points + [0, 0, -1.0]
        # self.plot.setData(pos=self.np_points, color=(self.pcr[0], self.pcr[1], self.pcr[2], 1), size=0.00005, pxMode=False)
        # self.graphicsView.addItem(self.plot)
        self.mesh = gl.GLMeshItem(vertexes=self.np_points, drawEdges=True, faces=self.faces, smooth=False,
                                  edgeColor=(0.2, 0.2, 0.1, 1.0), color=(self.pcr[0], self.pcr[1], self.pcr[2], 1))
        self.graphicsView.addItem(self.mesh)
    def ZMP_clicked(self):
        self.graphicsView.clear()
        self.mid_background_well()
        self.np_points = self.np_points + [0, 0, 0.1]
        # self.plot.setData(pos=self.np_points, color=(self.pcr[0], self.pcr[1], self.pcr[2], 1), size=0.00005, pxMode=False)
        # self.graphicsView.addItem(self.plot)
        self.mesh = gl.GLMeshItem(vertexes=self.np_points, drawEdges=True, faces=self.faces, smooth=False,
                                  edgeColor=(0.2, 0.2, 0.1, 1.0), color=(self.pcr[0], self.pcr[1], self.pcr[2], 1))
        self.graphicsView.addItem(self.mesh)
    def ZMN_clicked(self):
        self.graphicsView.clear()
        self.mid_background_well()
        self.np_points = self.np_points + [0, 0, -0.1]
        # self.plot.setData(pos=self.np_points, color=(self.pcr[0], self.pcr[1], self.pcr[2], 1), size=0.00005, pxMode=False)
        # self.graphicsView.addItem(self.plot)
        self.mesh = gl.GLMeshItem(vertexes=self.np_points, drawEdges=True, faces=self.faces, smooth=False,
                                  edgeColor=(0.2, 0.2, 0.1, 1.0), color=(self.pcr[0], self.pcr[1], self.pcr[2], 1))
        self.graphicsView.addItem(self.mesh)
    def ZSP_clicked(self):
        self.graphicsView.clear()
        self.mid_background_well()
        self.np_points = self.np_points + [0, 0, 0.01]
        # self.plot.setData(pos=self.np_points, color=(self.pcr[0], self.pcr[1], self.pcr[2], 1), size=0.00005, pxMode=False)
        # self.graphicsView.addItem(self.plot)
        self.mesh = gl.GLMeshItem(vertexes=self.np_points, drawEdges=True, faces=self.faces, smooth=False,
                                  edgeColor=(0.2, 0.2, 0.1, 1.0), color=(self.pcr[0], self.pcr[1], self.pcr[2], 1))
        self.graphicsView.addItem(self.mesh)
    def ZSN_clicked(self):
        self.graphicsView.clear()
        self.mid_background_well()
        self.np_points = self.np_points + [0, 0, -0.01]
        # self.plot.setData(pos=self.np_points, color=(self.pcr[0], self.pcr[1], self.pcr[2], 1), size=0.00005, pxMode=False)
        # self.graphicsView.addItem(self.plot)
        self.mesh = gl.GLMeshItem(vertexes=self.np_points, drawEdges=True, faces=self.faces, smooth=False,
                                  edgeColor=(0.2, 0.2, 0.1, 1.0), color=(self.pcr[0], self.pcr[1], self.pcr[2], 1))
        self.graphicsView.addItem(self.mesh)


    # --------------------------------- 二级函数：Abutment ------------------------------------
    def save_clicked(self):
        fileName, fileType = QFileDialog.getSaveFileName \
            (self, "Save As：", '', "STP Files(*.stp);;All Files(*)")
        print("filename is :",fileName)
        if fileName != '':
            abcal.save_stp(self.model, fileName)

    def create_clicked(self):
        self.getparameters()
        try:
            self.model = abcal.abut_create(self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8,
                                           self.a9, self.a10, self.a11, self.a12, self.a13, self.a14, self.a15,
                                           self.a16)
            # self.model = abcal.abc
            self.display.EraseAll()
            self.display.DisplayShape(self.model, update=True)
            self.display.FitAll()
        except Exception as e:
            print("发生了一个未知的错误:", str(e))

    def recomn_clicked(self):
        self.getparameters()
        try :
            ra5 = self.a4 - self.a6 * math.tan(self.a8 / 180 * math.pi)
            self.label_c_Hr.setText("<%.3f " % ra5)
            ra13 = self.a11 - 0.55
            self.label_dwcir.setText("%.3f " % ra13)
        except Exception as e:
            print("发生了一个未知的错误:", str(e))

    def getparameters(self):
        if self.Value_filt.text() != '':
            self.a1 = float(self.Value_filt.text())
        if self.Value_end.text() != '':
            self.a2 = float(self.Value_end.text())
        if self.Value_begn.text() != '':
            self.a3 = float(self.Value_begn.text())
        if self.Value_cir3.text() != '':
            self.a4 = float(self.Value_cir3.text())
        if self.Value_c_H.text() != '':
            self.a5 = float(self.Value_c_H.text())
        if self.Value_h2.text() != '':
            self.a6 = float(self.Value_h2.text())
        if self.Value_h1.text() != '':
            self.a7 = float(self.Value_h1.text())
        if self.Value_alph.text() != '':
            self.a8 = float(self.Value_alph.text())
        if self.Value_h_H.text() != '':
            self.a9 = float(self.Value_h_H.text())
        if self.Value_h_L.text() != '':
            self.a10 = float(self.Value_h_L.text())
        if self.Value_a.text() != '':
            self.a11 = float(self.Value_a.text())
        if self.Value_b.text() != '':
            self.a12 = float(self.Value_b.text())
        if self.Value_dwci.text() != '':
            self.a13 = float(self.Value_dwci.text())
        if self.Value_h3.text() != '':
            self.a14 = float(self.Value_h3.text())
        if self.Value_beta.text() != '':
            self.a15 = float(self.Value_beta.text())
        if self.Value_cir1.text() != '':
            self.a16 = float(self.Value_cir1.text())

    def parmtrclear_clicked(self):
        self.Value_filt.clear()
        self.Value_end.clear()
        self.Value_begn.clear()
        self.Value_cir3.clear()
        self.Value_c_H.clear()
        self.Value_h2.clear()
        self.Value_h1.clear()
        self.Value_alph.clear()
        self.Value_h_H.clear()
        self.Value_h_L.clear()
        self.Value_a.clear()
        self.Value_b.clear()
        self.Value_dwci.clear()
        self.Value_h3.clear()
        self.Value_beta.clear()
        self.Value_cir1.clear()






