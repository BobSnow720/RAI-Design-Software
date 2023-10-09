import numpy as np
import math
import selfmadeformat as sf
def ptscof(poigin_pre):
    poigin = poigin_pre
    poigin = sf.MomsOrg(poigin)
    eig, fea = sf.DireCof(poigin)
    pos, val, vect = sf.Maxab(eig, fea)
    posvct = sf.PosiAx(vect, 2)
    apha = sf.RadAxxy(posvct, 0)
    thet = sf.RadAxz(posvct)
    poigin = sf.RotWhole(poigin, apha, 2)
    poigin = sf.RotWhole(poigin, -thet, 1)

    # zrange = sf.Getpts(poigin, 10000, -10000, 10000, -10000, 0.000, -0.003)
    zrange = sf.Getpts(poigin, 10000, -10000, 10000, -10000, 0.000, -3.0)
    pos, val, vect, rxy = sf.Judgbp(zrange, poigin)
    apha = sf.RadAxxy(vect, rxy)
    poigin = sf.RotWhole(poigin, apha, 2)

    poigin = sf.Zpostn(poigin)
    # zrange = sf.Getpts(poigin, 10000, -10000, 10000, -10000, 0, -0.0006)
    zrange = sf.Getpts(poigin, 10000, -10000, 10000, -10000, 0, -0.6)
    xmaxpt = sf.Maxcordnpt(zrange, 0)
    xminpt = sf.Mincordnpt(zrange, 0)
    # posxpts = sf.Getpts(poigin, 0.5 * xmaxpt[0] + 0.00025, \
    #                     0.5 * xmaxpt[0], 0.00025, -0.00025, 10000, 0)
    posxpts = sf.Getpts(poigin, 0.5 * xmaxpt[0] + 0.25, \
                        0.5 * xmaxpt[0], 0.25, -0.25, 10000, 0)
    # negxpts = sf.Getpts(poigin, 0.5 * xminpt[0], 0.5 * xminpt[0] - 0.00025, \
                        # 0.00025, -0.00025, 10000, 0)
    negxpts = sf.Getpts(poigin, 0.5 * xminpt[0], 0.5 * xminpt[0] - 0.25, \
                        0.25, -0.25, 10000, 0)
    # try :
    #     a = np.mean(negxpts[:, 2])
    # except Exception as e:
    #     print('error is :', e)

    if np.mean(posxpts[:, 2]) < np.mean(negxpts[:, 2]):
        poigin = sf.RotWhole(poigin, np.pi, 2)
    return poigin

def ptsshape(poigin_pre,ex,shr):
    if ex=='':
        ex = 0.5
    else:
        ex = float(ex)
    if shr=='':
        shr = 1
    else:
        shr = float(shr)
    poigin = poigin_pre
    # zrange = sf.Getpts(poigin, 10000, -10000, 10000, -10000, 0.0008, 0)
    zrange = sf.Getpts(poigin, 10000, -10000, 10000, -10000, 0.8, 0)
    dimax = np.max(zrange, axis=0)
    dimin = np.min(zrange, axis=0)
    # zyrange = sf.Getpts(poigin, 0.0005, -0.0005, 10000, -10000, 0.0005, -0.0005)
    zyrange = sf.Getpts(poigin, 0.5, -0.5, 10000, -10000, 0.5, -0.5)
    zymax = np.max(zyrange, axis=0)
    zymin = np.min(zyrange, axis=0)
    yl = zymax[1] - zymin[1]
    # ky = 2 * (ex / 1000) / yl
    ky = 2 * ex / yl
    # 找中间带距离YOZ面最远的点
    if abs(dimin[0]) >= dimax[0]:
        kyx = math.pi / abs(dimin[0])
    else:
        kyx = math.pi / dimax[0]
    e = math.e
    # kx = (shr/1000) / (dimax[0] * (e ** dimax[0] - e ** dimin[0]))
    kx = shr/ (dimax[0] * (e ** dimax[0] - e ** dimin[0]))
    bx = 1 + kx * e ** dimin[0]
    poigin = sf.Expand_Y(poigin, ky, kyx)
    poigin = sf.Shrink_X(poigin, kx, bx)
    return poigin
def ptsincirc(points):
    # points = sf.Getpts(points, 10000, -10000, 10000, -10000, 0, -0.0005)
    points = sf.Getpts(points, 10000, -10000, 10000, -10000, 0, -0.5)
    dimax = np.max(points, axis=0)
    dimin = np.min(points, axis=0)
    # aimpt = sf.MinLinePt(points, dimax[0], dimin[0], dimax[1], dimin[1], 0.001 / 10)
    aimpt = sf.MinLinePt(points, dimax[0], dimin[0], dimax[1], dimin[1], 1.0 / 10)
    xz = aimpt[0]
    yz = aimpt[1]
    # aimpt = sf.MinLinePt_Pro(points, dimax[0], dimin[0], dimax[1], dimin[1], \
    #                          0.001/100, xz + 0.0001, xz - 0.0001,yz + 0.0001, yz - 0.0001)
    aimpt = sf.MinLinePt_Pro(points, dimax[0], dimin[0], dimax[1], dimin[1], \
                             1.0/100, xz + 0.1, xz - 0.1,yz + 0.1, yz - 0.1)
    return aimpt











