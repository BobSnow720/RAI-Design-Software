
import numpy as np
import math
# def PriPCD(points,filnm):
#     name = filnm
#     pcd = o3d.geometry.PointCloud()
#     pcd.points = o3d.utility.Vector3dVector(points)
#     if name[len(name)-4:]!=".pcd":
#         o3d.io.write_point_cloud(name + ".pcd", pcd)
#     else:
#         o3d.io.write_point_cloud(name, pcd)
def MomsOrg(points):
    msctr = np.mean(points, axis=0)
    points = points - msctr
    return points
def DireCof(points):
    covpts = np.cov(points,rowvar=False) #######可操作
    eig,fea = np.linalg.eig(covpts)   #######可操作
    return eig,fea
def Maxab(eig,fea):
    a = 0
    b = eig[0]
    for n in range(2):
        if b <= eig[n + 1]:
            b = eig[n + 1]
            a = n + 1
    c = fea[:,a]
    return a,b,c
def Minab(eig,fea):
    a = 0
    b = eig[0]
    for n in range(2):
        if b >= eig[n + 1]:
            b = eig[n + 1]
            a = n + 1
    c = fea[:,a]
    return a,b,c
def Midab(eig,fea):
    a1,b1,c1 = Maxab(eig,fea)
    a2,b2,c2 = Minab(eig,fea)
    a3 = 3-a1-a2
    b3 = eig[a3]
    c3 = fea[:,a3]
    return a3,b3,c3
def PosiAx(feaclm,ax):
    if feaclm[ax]<0:
        feaclm = -1*feaclm
    return feaclm
def RadAxxy(fea,ax):
    lxy = (fea[0] ** 2 + fea[1] ** 2) ** 0.5
    kk = math.sin(fea[1-ax]) / lxy
    kxy1 = abs(kk) / kk
    kxy2 = (-1)**ax
    apha = -1 * kxy1 * kxy2 * math.acos(fea[ax] / lxy)
    return apha
def RadAxz(fea):
    lxy = (fea[0] ** 2 + fea[1] ** 2) ** 0.5
    thet = 0.5 * math.pi - math.atan(fea[2] / lxy)
    return thet
def rotate_X(x, y, z, alpha):
    x_r = x
    y_r = np.cos(alpha)*y - np.sin(alpha)*z
    z_r = np.sin(alpha)*y + np.cos(alpha)*z
    return x_r, y_r, z_r
def rotate_Y(x, y, z, beta):
    x_r = np.cos(beta)*x + np.sin(beta)*z
    y_r = y
    z_r = -np.sin(beta)*x + np.cos(beta)*z
    return x_r, y_r, z_r
def rotate_Z(x, y, z,  gamma):
    x_r = np.cos(gamma)*x - np.sin(gamma)*y
    y_r = np.sin(gamma)*x + np.cos(gamma)*y
    z_r = z
    return x_r, y_r, z_r
def RotWhole(points,rad,ax):
    if ax==0:
        for n in range(len(points)):
            points[n, 0], points[n, 1], points[n, 2] = \
                rotate_X(points[n, 0], points[n, 1], points[n, 2], rad)
    elif ax==1:
        for n in range(len(points)):
            points[n, 0], points[n, 1], points[n, 2] = \
                rotate_Y(points[n, 0], points[n, 1], points[n, 2], rad)
    elif ax==2:
        for n in range(len(points)):
            points[n, 0], points[n, 1], points[n, 2] = \
                rotate_Z(points[n, 0], points[n, 1], points[n, 2], rad)
    return points
def Getpts(points,xsup,xinf,ysup,yinf,zsup,zinf):
    zrange = []
    i = 0
    for n in range(len(points)):
        if  xinf<=points[n,0]<=xsup and yinf<=points[n,1]<=ysup and zinf<=points[n,2]<=zsup:
            zrange.insert(i, points[n])
            i = i + 1
    zrange = np.array(zrange)
    return zrange
def Maxcordnpt(points,ax):
    pgmax = np.max(points,axis=0)
    for n in range(len(points)):
        if points[n, ax] == pgmax[ax]:
            znum = n
            break
    aimpt = points[znum]
    return aimpt
def Mincordnpt(points,ax):
    pgmin = np.min(points,axis=0)
    for n in range(len(points)):
        if points[n, ax] == pgmin[ax]:
            znum = n
            break
    aimpt = points[znum]
    return aimpt
def Zpostn(points):
    aimpt = Maxcordnpt(points,1)
    if aimpt[2] < 0:
        RotWhole(points, np.pi, 1)
    return points
def Judgbp(belt,points):
    beig, bfea = DireCof(belt)
    bpos1, bval1, bvect1 = Maxab(beig, bfea)
    bpos2, bval2, bvect2 = Midab(beig, bfea)
    peig, pfea = DireCof(points)
    ppos1, pval1, pvect1 = Midab(peig, pfea)
    ppos2, pval2, pvect2 = Minab(peig, pfea)
    if bval1/bval2 > pval1/pval2:
        pos, val, vect = bpos1, bval1, bvect1
        rxy = 0
    else:
        pos, val, vect = ppos1, pval1, pvect1
        rxy = 1
    return pos, val, vect, rxy
def Expand_Y(points,ky,kyx):
    for n in range(len(points)):
        t = 1 + 0.5 * (1 + math.cos(kyx * points[n, 0])) * ky
        points[n, 1] = points[n, 1] * t
    return points
def Shrink_X(points,kx,bx):
    e = math.e
    for n in range(len(points)):
        t = (-kx * e ** points[n, 0] + bx)
        points[n, 0] = points[n, 0] * t
    return points
# def PriPLY(points,filnm):
#     name = filnm
#     pcd2 = o3d.geometry.PointCloud()
#     pcd2.points = o3d.utility.Vector3dVector(points)
#     distances = pcd2.compute_nearest_neighbor_distance()
#     avg_dist = np.mean(distances)
#     radius = 3 * avg_dist
#     pcd2.estimate_normals()
#     bpa_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting\
#                (pcd2, o3d.utility.DoubleVector([radius, radius * 2]))
#     dec_mesh = bpa_mesh.simplify_quadric_decimation(100000)
#     if name[len(name)-4:]!=".ply":
#         o3d.io.write_triangle_mesh(name + ".ply", bpa_mesh)
#     else:
#         o3d.io.write_triangle_mesh(name, bpa_mesh)
def MinLinePt(points,xsup,xinf,ysup,yinf,st):
    aimpt = [0., 0., 0.]
    p = 0
    q = 0
    ix = xinf
    while ix <= xsup:
        jy = yinf
        while jy <= ysup:
            count = [0, 0, 0, 0]
            for n in range(len(points)):
                if (xinf < points[n, 0] < ix) and (yinf < points[n, 1] < jy):
                    count[0] = 1
                if (ix < points[n, 0] < xsup) and (yinf < points[n, 1] < jy):
                    count[1] = 1
                if (ix < points[n, 0] < xsup) and (jy < points[n, 1] < ysup):
                    count[2] = 1
                if (xinf < points[n, 0] < ix) and (jy < points[n, 1] < ysup):
                    count[3] = 1
            if count == [1, 1, 1, 1]:
                l0 = 100
                for n in range(len(points)):
                    l1 = ((ix - points[n, 0]) ** 2 + (jy - points[n, 1]) ** 2) ** 0.5
                    if l0 >= l1:
                        l0 = l1
                if aimpt[2] < l0:
                    aimpt = [ix, jy, l0]
            jy += st
            p += 1
        ix += st
        q += 1
    return aimpt
def MinLinePt_Pro(points,xsup,xinf,ysup,yinf,st,bxsup,bxinf,bysup,byinf):
    aimpt = [0., 0., 0.]
    p = 0
    q = 0
    ix = bxinf
    while ix <= bxsup:
        jy = byinf
        while jy <= bysup:
            count = [0, 0, 0, 0]
            for n in range(len(points)):
                if (xinf < points[n, 0] < ix) and (yinf < points[n, 1] < jy):
                    count[0] = 1
                if (ix < points[n, 0] < xsup) and (yinf < points[n, 1] < jy):
                    count[1] = 1
                if (ix < points[n, 0] < xsup) and (jy < points[n, 1] < ysup):
                    count[2] = 1
                if (xinf < points[n, 0] < ix) and (jy < points[n, 1] < ysup):
                    count[3] = 1
            if count == [1, 1, 1, 1]:
                l0 = 100
                for n in range(len(points)):
                    l1 = ((ix - points[n, 0]) ** 2 + (jy - points[n, 1]) ** 2) ** 0.5
                    if l0 >= l1:
                        l0 = l1
                if aimpt[2] < l0:
                    aimpt = [ix, jy, l0]
            jy += st
            p += 1
        ix += st
        q += 1
    return aimpt
def nmultiply(x):
    value = 1
    if isinstance(x, int):
        for i in range(x):
            value *= i + 1
    else:
        print("NaN, please input int")
        value = None
    return value
def mysin(x):
    n = 10
    pi = 3.1415926
    x = x * pi / 180
    result = 0
    sign = 1
    for i in range(1, n+1):
        term = sign * (x**(2*i-1) / nmultiply(2*i-1))
        result += term
        sign *= -1
    return result
def mycos(x):
    n = 10
    pi = 3.1415926
    x = x * pi / 180
    result = 1
    sign = -1
    for i in range(1, n+1):
        term = sign * (x**(2*i) / nmultiply(2*i))
        result += term
        sign *= -1
    return result
def myacos(a):
    pi = 3.1415926
    x0 = 1.0
    x0 = x0 *180 /pi
    error = 1e-10
    while True:
        fx = mycos(x0) - a
        if abs(fx) < error:
            break
        dfx = -mysin(x0)
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < error:
            break
        x0 = x1
    return x0
def myatan(a):
    pi = 3.1415926
    n = 12
    result = 0
    sign = 1
    for i in range(n):
        term = sign * a**(2*i+1) / (2*i+1)
        result += term
        sign *=-1
    result = result *180 / pi
    return result
def myasin(a):
    if a > 1 or a < -1:
        return float('NaN')
    elif a == 1:
        return 90
    elif a == -1:
        return -90
    else:
        low = -90
        high = 90
        mid = (low + high) / 2
        while abs(high - low) > 1e-15:
            if mysin(mid) < a:
                low = mid
            else:
                high = mid
            mid = (low + high) / 2
    return mid
def d3covtrix(points):
    cov = np.zeros(shape=[3,3])
    ave = [0,0,0]
    n = len(points)
    for i in range(0,3):
        for j in range(n):
            ave[i] += points[j, i] / n
    for i in range(0,3):
        for j in range(0,3):
            for k in range(n):
                temp = (points[k, i] - ave[i]) * (points[k, j] - ave[j]) / (n - 1)
                cov[i, j] += temp
    return cov
def myeigvalue(cov):
    eigval = [0.,0.,0.]
    fa = np.array([0.,0.,0.,0.])
    fa[0] = -1
    fa[1] = cov[0,0]+cov[1,1]+cov[2,2]
    fa[2] = (cov[0,1]*cov[1,0]+cov[1,2]*cov[2,1]+cov[0,2]*cov[2,0])-\
            (cov[0,0]*cov[1,1]+cov[0,0]*cov[2,2]+cov[1,1]*cov[2,2])
    fa[3] = cov[0,0]*cov[1,1]*cov[2,2]+cov[0,1]*cov[1,2]*cov[2,0]+cov[0,2]*cov[1,0]*cov[2,1]- \
            (cov[0,0]*cov[1,2]*cov[2,1]+cov[0,1]*cov[1,0]*cov[2,2]+cov[0,2]*cov[1,1]*cov[2,0])
    der = [0.,0.,0.]
    der[0] = 3*fa[0]
    der[1] = 2*fa[1]
    der[2] = fa[2]
    edge = [0.,0.]
    edge[0] = (-der[1]-(der[1]**2-4*der[0]*der[2])**0.5)/(2*der[0])
    edge[1] = (-der[1]+(der[1]**2-4*der[0]*der[2])**0.5)/(2*der[0])
    if edge[0] > edge[1]:
        b = edge[0]
        edge[0] = edge[1]
        edge[1] = b
    mid = (edge[0]+edge[1])/2
    error = 1e-10
    inf = fa[0] * edge[0] ** 3 + fa[1] * edge[0] ** 2 + fa[2] * edge[0] + fa[3]
    if inf > 0:
        sign = 1
    else:
        sign = -1
    while True:
        if (edge[1]-edge[0])<error:
            break
        inf = fa[0]*edge[0]**3+fa[1]*edge[0]**2+fa[2]*edge[0]+fa[3]
        sup = fa[0]*edge[1]**3+fa[1]*edge[1]**2+fa[2]*edge[1]+fa[3]
        midvl = fa[0]*mid**3+fa[1]*mid**2+fa[2]*mid+fa[3]
        if inf*midvl >= 0:
            edge[0] = mid
        else:
            edge[1] = mid
        mid = (edge[0] + edge[1]) / 2
    eigval[1] = mid

    step = 1
    i = 0
    while True:
        rig = fa[0] * (eigval[1] + step) ** 3 + fa[1] * (eigval[1] + step) ** 2 + fa[2] * (eigval[1] + step) + fa[3]
        if rig*sign>0:
            break
        i += 1
        step = 10**i
    edge[0] = eigval[1]
    edge[1] = eigval[1]+step
    mid = (edge[0] + edge[1]) / 2
    while True:
        if (edge[1]-edge[0])<error:
            break
        inf = fa[0]*edge[0]**3+fa[1]*edge[0]**2+fa[2]*edge[0]+fa[3]
        sup = fa[0]*edge[1]**3+fa[1]*edge[1]**2+fa[2]*edge[1]+fa[3]
        midvl = fa[0]*mid**3+fa[1]*mid**2+fa[2]*mid+fa[3]
        if sup*midvl >= 0:
            edge[1] = mid
        else:
            edge[0] = mid
        mid = (edge[0] + edge[1]) / 2
    eigval[2] = mid
    step = -1
    i = 0
    while True:
        lef = fa[0] * (eigval[1] + step) ** 3 + fa[1] * (eigval[1] + step) ** 2 + fa[2] * (eigval[1] + step) + fa[3]
        if lef*sign<0:
            break
        i += 1
        step = -1*10**i
    edge[0] = eigval[1]+step
    edge[1] = eigval[1]
    mid = (edge[0] + edge[1]) / 2
    while True:
        if (edge[1]-edge[0])<error:
            break
        inf = fa[0]*edge[0]**3+fa[1]*edge[0]**2+fa[2]*edge[0]+fa[3]
        sup = fa[0]*edge[1]**3+fa[1]*edge[1]**2+fa[2]*edge[1]+fa[3]
        midvl = fa[0]*mid**3+fa[1]*mid**2+fa[2]*mid+fa[3]
        if inf*midvl >= 0:
            edge[0] = mid
        else:
            edge[1] = mid
        mid = (edge[0] + edge[1]) / 2
    eigval[0] = mid
    for i in range(2):
        for j in range(1, 3 - i):
            if abs(eigval[i]) < abs(eigval[i + j]):
                eigval[i], eigval[i + j] = eigval[i + j], eigval[i]
    return eigval
def power_iteration(cov, eps=1e-10, max_iter=1000):
    n = cov.shape[0]
    x = np.ones(n)
    for i in range(max_iter):
        x_new = np.dot(cov, x)
        x_new /= np.linalg.norm(x_new)
        if np.abs(np.dot(x, x_new)-1) < eps:
            return x_new
        x = x_new
    raise Exception(f"无法收敛于指定精度eps={eps}")
def eigenvectors(cov, eps=1e-10, max_iter=1000):
    n = cov.shape[0]
    eigenvecs = []
    for i in range(n):
        v = power_iteration(cov, eps=eps, max_iter=max_iter)
        eigenvecs.append(v)
        cov -= np.outer(np.dot(cov, v),v)
    return np.array(eigenvecs).T
def myeig(cov):
    eigval = myeigvalue(cov)
    eigvect = eigenvectors(cov)
    return eigval,eigvect
def findmaxpt(points,pos):
    a = 0
    b = points[0,pos]
    for n in range(len(points)):
        if b <= points[n+1,pos]:
            b = points[n+1,pos]
            a = n + 1
    return b
def findminpt(points,pos):
    a = 0
    b = points[0,pos]
    for n in range(len(points)):
        if b >= points[n+1,pos]:
            b = points[n+1,pos]
            a = n + 1
    return b
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
def rgb_to_decimal(rgb_color):
    r, g, b = rgb_color
    return (r/255, g/255, b/255)