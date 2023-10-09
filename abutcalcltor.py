
import math
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs

from OCC.Core.gp import gp_Ax2, gp_Elips, gp_Pnt, gp_Dir, gp_Vec, gp_Circ, gp_Trsf
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCone, BRepPrimAPI_MakePrism
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, \
       BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace, BRepBuilderAPI_MakePolygon, \
       BRepBuilderAPI_Sewing, BRepBuilderAPI_Transform

from OCC.Core.BRepOffsetAPI import BRepOffsetAPI_ThruSections  # 放样
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Core.BRepAlgoAPI import  BRepAlgoAPI_Fuse  # 布尔操作

from OCC.Core.GeomAPI import GeomAPI_PointsToBSpline, GeomAPI_IntSS  # 样条曲线工具
from OCC.Core.TColgp import TColgp_Array1OfPnt  # 向量组工具
from OCC.Extend.TopologyUtils import TopologyExplorer  # 拓扑搜寻工具
from OCC.Core.TopExp import TopExp_Explorer  # 拓扑搜寻
from OCC.Core.TopAbs import TopAbs_FACE

from OCC.Core.BOPAlgo import BOPAlgo_Splitter  # 分割
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeFillet  # 倒角


global abc,efg


def abut_create(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16):
    # 圆锥建模
    # a4 = 1.6
    cir3 = a4 # 半径

    # a6 = 2
    height_cone1 = a6
    # a8 = 8
    alpha = a8
    cir2 = cir3 - height_cone1 * math.tan(alpha/180 * math.pi)

    cone1 = BRepPrimAPI_MakeCone(gp_Ax2 (gp_Pnt(0,0,0),gp_Dir (0,0,-1)),cir3,cir2,height_cone1).Shape()


    # 六角建模
    # a5 = 1.3
    cir_hex = a5
    # a7 = 1.3
    height_hex = a7
    rad = math.pi/3
    pts_hex = []
    for i in range(6):
           pts_hex.append(gp_Pnt(0,0,-height_cone1))
           x = cir_hex * math.cos(i*rad)
           pts_hex[i].SetX(x)
           y = cir_hex * math.sin(i*rad)
           pts_hex[i].SetY(y)
           #print(x,y)
    polygon = BRepBuilderAPI_MakePolygon()
    for pt in pts_hex:
        polygon.Add(pt)
    polygon.Close()
    fc_hex = BRepBuilderAPI_MakeFace(polygon.Wire()).Face()

    vect_hex = gp_Vec(0, 0, -height_hex)
    prism_hex = BRepPrimAPI_MakePrism(fc_hex, vect_hex).Shape()


    # 放样侧面
         # 椭圆面
    # a12 = 3.0
    r_max = a12
    # a11 = 2.2
    r_min = a11
    elip = gp_Elips(gp_Ax2(gp_Pnt(0.0, 0.0, 0.0), gp_Dir(0, 0.0, 1.0)), r_max, r_min)
    eg_elip = BRepBuilderAPI_MakeEdge(elip).Edge()
    Wr_elip = BRepBuilderAPI_MakeWire(eg_elip)
    wr_elip = Wr_elip.Wire()
    vect_elip = gp_Vec(0,0,6)
    prism_elip = BRepPrimAPI_MakePrism(Wr_elip.Shape(),vect_elip).Shape()

         # XOY向曲面
    # a9 = 4.0
    height_curvH = a9
    # a10 = 2.5
    height_curvL = a10
    miny_curv = -5
    pts_curv = []
    for i in range(5):
           pts_curv.append(gp_Pnt(0,0,0))
    pts_curv[0] = gp_Pnt(-2*r_max, miny_curv, height_curvL)
    pts_curv[1] = gp_Pnt(-r_max, miny_curv, height_curvL)
    pts_curv[2] = gp_Pnt(0, miny_curv, height_curvH)
    pts_curv[3] = gp_Pnt(r_max, miny_curv, height_curvL)
    pts_curv[4] = gp_Pnt(2*r_max, miny_curv, height_curvL)
    array = TColgp_Array1OfPnt(1, 5)
    for i in range(5):
           array.SetValue(i+1, pts_curv[i])
    curv = GeomAPI_PointsToBSpline(array).Curve()
    Eg_curv = BRepBuilderAPI_MakeEdge(curv)
    V1 = Eg_curv.Vertex1()
    V2 = Eg_curv.Vertex2()

    vect_Curve_elip = gp_Vec(0,10,0)
    prism_curve = BRepPrimAPI_MakePrism(Eg_curv.Shape(),vect_Curve_elip).Shape()

         # 分割操作
    fc_curv = TopoDS_Shape(prism_curve)
    fc_elip = TopoDS_Shape(prism_elip)
    print(fc_curv)
    splitter = BOPAlgo_Splitter()
    splitter.AddArgument(fc_elip)
    splitter.AddTool(fc_curv)
    splitter.Perform()
    fcs = []
    i = 0
    exp = TopExp_Explorer(splitter.Shape(), TopAbs_FACE)
    while exp.More():
        fcs.append(exp.Current())
        exp.Next()
        i += 1
    print(i)

    egs = []
    i = 0
    for e in TopologyExplorer(fcs[0]).edges():
           egs.append(e)
           if i == 5:
               None
           i += 1
    print("Number of edges in the face: ", len(egs))
         # 放样操作
    botcir = gp_Circ(gp_Ax2(gp_Pnt(0.0, 0.0, 0), gp_Dir(0.0, 0.0, 1.0)), cir3)
    eg_botcir = BRepBuilderAPI_MakeEdge(botcir)
    Wr_botcir = BRepBuilderAPI_MakeWire(eg_botcir.Edge())
    wr_botcir = Wr_botcir.Wire()
    wr_egs2 = BRepBuilderAPI_MakeWire(egs[2]).Wire()
              # 偏移曲线的绘制
    # a3 = 0.1
    height_ofst = a3
    cir_ofst = (cir3-cir2)/height_cone1 * height_ofst + cir3
    print(cir_ofst,botcir)
    Cir_ofst = gp_Circ(gp_Ax2(gp_Pnt(0.0, 0.0, height_ofst), gp_Dir(0.0, 0.0, 1.0)), cir_ofst)
    eg_ofst = BRepBuilderAPI_MakeEdge(Cir_ofst).Edge()
    Wr_ofst = BRepBuilderAPI_MakeWire(eg_ofst)
    wr_ofst = Wr_ofst.Wire()
    trsf = gp_Trsf()
    # a2 = 0.1
    height_ofst_cur = a2
    trsf.SetTranslation(gp_Vec(0.0, 0.0, -height_ofst_cur))
    Tran_wr_egs2_ofst = BRepBuilderAPI_Transform(wr_egs2,trsf)
    wr_egs2_ofst = BRepBuilderAPI_MakeWire(Tran_wr_egs2_ofst.Shape()).Wire()
    cursurf = BRepOffsetAPI_ThruSections(False, False)
    for wire in [wr_botcir, wr_ofst, wr_egs2_ofst, wr_egs2]:
        cursurf.AddWire(wire)
    cursurf.Build()

    # 肩台面
    fc_curvin = BRepBuilderAPI_MakeFace(wr_egs2).Face()
    # 上圆锥
    prism_curvin = BRepPrimAPI_MakePrism(fc_curvin,gp_Vec(0,0,-10)).Shape()

         # 上下圆的绘制
    # a13 = r_min-0.55
    cir4 = a13    # 确保肩台有1毫米左右空间
    # a14 = 4.0
    height_cirup = height_curvH + a14
    cirdw = gp_Circ(gp_Ax2(gp_Pnt(0.0, 0.0, 0), gp_Dir(0.0, 0.0, 1.0)), cir4)
    eg_cirdw = BRepBuilderAPI_MakeEdge(cirdw)
    Wr_cirdw = BRepBuilderAPI_MakeWire(eg_cirdw.Edge())
    wr_cirdw = Wr_cirdw.Wire()
    # a15 = 3
    beta = a15
    cir5 = cir4 - height_cirup * math.tan(beta/180 * math.pi)
    cirup = gp_Circ(gp_Ax2(gp_Pnt(0.0, 0.0, height_cirup), gp_Dir(0.0, 0.0, 1.0)), cir5)
    eg_cirup = BRepBuilderAPI_MakeEdge(cirup)
    Wr_cirup = BRepBuilderAPI_MakeWire(eg_cirup.Edge())
    wr_cirup = Wr_cirup.Wire()
        # 放样
    udsurf = BRepOffsetAPI_ThruSections(True, False)
    for wr in [wr_cirdw, wr_cirup]:
        udsurf.AddWire(wr)
    udsurf.Build()
    print(udsurf.Shape())


    # 上圆锥区域
         # 布林运算
    uczone = BRepAlgoAPI_Fuse(prism_curvin, udsurf.Shape()).Shape()

         # 倒角
    flt = BRepFilletAPI_MakeFillet(uczone)
    egs = []
    i = 1
    for e in TopologyExplorer(uczone).edges():
        if i == 4 :
            # a1 = 0.6
            flt.Add(a1, e)
        egs.append(e)
        i += 1
    print("循环运行次数：",i-1)
    flt.Build()
    rst = flt.Shape()

         # 寻找面
    fcs = []
    i = 0
    for f in TopologyExplorer(rst).faces():
        if i==0 or i==1 or i==3 or i==5:
            None
        fcs.append(f)
        i += 1
    print("循环运行次数：",i)

    # 内圆柱
    # a16 = 0.85
    cir1 = a16
    cir_Cy = gp_Circ(gp_Ax2(gp_Pnt(0.0, 0.0, -height_cone1-height_hex), gp_Dir(0.0, 0.0, 1.0)), cir1)
    eg_Cy = BRepBuilderAPI_MakeEdge(cir_Cy).Edge()
    Wr_Cy = BRepBuilderAPI_MakeWire(eg_Cy)
    wr_Cy = Wr_Cy.Wire()
    prism_Cy = BRepPrimAPI_MakePrism(wr_Cy,gp_Vec(0,0,height_hex+height_cone1+height_cirup)).Shape()


    # 关键元素整理
         # 上圆环
    splitter = BOPAlgo_Splitter()
    splitter.AddArgument(fcs[5])
    fc_Cy = TopoDS_Shape(prism_Cy)
    print("这个是Shell格式，也可以用来分割面",fc_Cy)
    splitter.AddTool(fc_Cy)
    splitter.Perform()
    fcs_1 = []
    i = 0
    exp_1 = TopExp_Explorer(splitter.Shape(), TopAbs_FACE)
    while exp_1.More():
        fcs_1.append(exp_1.Current())
        exp_1.Next()
        i += 1
    print("上圆环分割面数",i)

        # cone1侧面及下圆面
    fcs_2 = []
    i = 0
    exp_2 = TopExp_Explorer(cone1, TopAbs_FACE)
    while exp_2.More():
        fcs_2.append(exp_2.Current())
        exp_2.Next()
        i += 1
    print("cone1面数",i)


        # 棱柱侧面及下方六边形
    fcs_3 = []
    i = 0
    exp_3 = TopExp_Explorer(prism_hex, TopAbs_FACE)
    while exp_3.More():
        fcs_3.append(exp_3.Current())
        exp_3.Next()
        i += 1
    print("六棱柱面数",i)

        # cone1下方分割面
    fc_hex_Z = BRepPrimAPI_MakePrism(polygon.Wire(),gp_Vec(0,0,-height_hex)).Shape()

    splitter = BOPAlgo_Splitter()
    splitter.AddArgument(fcs_2[1])
    fc_Cy = TopoDS_Shape(fc_hex_Z)
    splitter.AddTool(fc_Cy)
    splitter.Perform()
    fcs_4 = []
    i = 0
    exp_4 = TopExp_Explorer(splitter.Shape(), TopAbs_FACE)
    while exp_4.More():
        fcs_4.append(exp_4.Current())
        exp_4.Next()
        i += 1
    print("cone1下方分割面数",i)

        # 六棱柱下方分割面
    splitter = BOPAlgo_Splitter()
    splitter.AddArgument(fcs_3[7])
    fc_Cy = TopoDS_Shape(prism_Cy)
    splitter.AddTool(fc_Cy)
    splitter.Perform()
    fcs_5 = []
    i = 0
    exp_5 = TopExp_Explorer(splitter.Shape(), TopAbs_FACE)
    while exp_5.More():
        fcs_5.append(exp_5.Current())
        exp_5.Next()
        i += 1
    print("六棱柱下方分割面数",i)


    sew = BRepBuilderAPI_Sewing()
    sew.Add(fcs_1[0])
    sew.Add(fcs[0])
    sew.Add(fcs[1])
    sew.Add(fcs[3])
    sew.Add(cursurf.Shape())
    sew.Add(fcs_2[0])
    sew.Add(fcs_4[0])
    sew.Add(fc_hex_Z)
    sew.Add(fcs_5[0])
    sew.Add(prism_Cy)
    sew.Perform()
    print("sew.SewedShape()--------------->",sew.SewedShape())
    sew_sha = TopoDS_Shape(sew.SewedShape())
    # abc = sew_sha


    # # Quilt，面包成实体
    # ful = BRepTools_Quilt()
    # fcs_1_0 = TopoDS_Shape(fcs_1[0])
    # ful.Add(fcs_1_0)
    # fcs_0 = TopoDS_Shape(fcs[0])
    # ful.Add(fcs_0 )
    # fcs_1 = TopoDS_Shape(fcs[1])
    # ful.Add(fcs_1)
    # fcs_3 = TopoDS_Shape(fcs[3])
    # ful.Add(fcs_3)
    # ful.Add(cursurf.Shape())
    # fcs_2_0 = TopoDS_Shape(fcs_2[0])
    # ful.Add(fcs_2_0)
    # fcs_4_0 = TopoDS_Shape(fcs_4[0])
    # ful.Add(fcs_4_0)
    # ful.Add(fc_hex_Z)
    # fcs_5_0 = TopoDS_Shape(fcs_5[0])
    # ful.Add(fcs_5_0)
    # ful.Add(prism_Cy)
    # fulpart = TopoDS_Shape(ful.Shells())
    # print("------------>",fulpart)
    #
    #
    # flt = BRepFilletAPI_MakeFillet(sew_sha)
    # egs = []
    # i = 1
    # for e in TopologyExplorer(sew_sha).edges():
    #     if i== 2 :
    #         # display.DisplayShape(e)
    #         flt.Add(0.1, e)
    #         None
    #     egs.append(e)
    #     i += 1
    # print("循环运行次数：",i-1)
    #
    # flt.Build()
    # rst = flt.Shape()
    # efg = rst


    # step_writer = STEPControl_Writer()
    # step_writer.Transfer(rst, STEPControl_AsIs)
    # status = step_writer.Write("abutment.stp")
    return sew_sha


def save_stp(rst, filnm):
    name = filnm
    step_writer = STEPControl_Writer()
    step_writer.Transfer(rst, STEPControl_AsIs)
    if name[len(name)-4:]!=".stp":
        step_writer.Write(name + ".stp")
    else:
        step_writer.Write(name)


# a1 = 0.6
# a2 = 0.1
# a3 = 0.1
# a4 = 1.6
# a5 = 1.3
# a6 = 2
# a7 = 1.3
# a8 = 8
# a9 = 4.0
# a10 = 2.5
# a11 = 2.2
# a12 = 3.0
# a13 = 1.65
# a14 = 4.0
# a15 = 3
# a16 = 0.85
# abc = abut_create(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16)
#
# save_stp(abc,"t6.stp")

