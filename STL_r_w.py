import numpy as np
np.set_printoptions(precision=16)
import struct

def stlGetFormat(fileName):
    fid = open(fileName,'rb')
    fid.seek(0,2)                # Go to the end of the file
    fidSIZE = fid.tell()         # Check the size of the file
    if (fidSIZE-84)%50 > 0:
        stlFORMAT = 'ascii'
    else:
        fid.seek(0,0)            # go to the beginning of the file
        header  = fid.read(80).decode()
        isSolid = header[0:5]=='solid'
        fid.seek(-80,2)          # go to the end of the file minus 80 characters
        tail       = fid.read(80)
        isEndSolid = tail.find(b'endsolid')+1

        if isSolid & isEndSolid:
            stlFORMAT = 'ascii'
        else:
            stlFORMAT = 'binary'
    fid.close()
    return stlFORMAT


def READ_stlbinary(stlFILENAME):
    # Open the binary STL file
    fidIN = open(stlFILENAME, 'rb')
    # Read the header
    fidIN.seek(80, 0)  # Move to the last 4 bytes of the header
    facetcount = struct.unpack('I', fidIN.read(4))[0]  # Read the number of facets (uint32:'I',4 bytes)

    # Initialise arrays into which the STL data will be loaded:
    coordNORMALS = np.zeros((facetcount, 3))
    coordVERTICES = np.zeros((facetcount, 3, 3))
    # Read the data for each facet:
    for loopF in np.arange(0, facetcount):
        tempIN = struct.unpack(12 * 'f', fidIN.read(4 * 12))  # Read the data of each facet (float:'f',4 bytes)
        coordNORMALS[loopF, :] = tempIN[0:3]  # x,y,z components of the facet's normal vector
        coordVERTICES[loopF, :, 0] = tempIN[3:6]  # x,y,z coordinates of vertex 1
        coordVERTICES[loopF, :, 1] = tempIN[6:9]  # x,y,z coordinates of vertex 2
        coordVERTICES[loopF, :, 2] = tempIN[9:12]  # x,y,z coordinates of vertex 3
        fidIN.read(2);  # Move to the start of the next facet.  Using file.read is much quicker than using seek
    fidIN.close()

    for i in range(len(coordVERTICES)):
        coordVERTICES[i] = coordVERTICES[i].T

    return [coordVERTICES, coordNORMALS]


def READ_stlascii(stlFILENAME):
    # Read the ascii STL file
    fidIN = open(stlFILENAME,'r')
    fidCONTENTlist = [line.strip() for line in fidIN.readlines() if line.strip()]     #Read all the lines and Remove all blank lines
    fidCONTENT = np.array(fidCONTENTlist)
    fidIN.close()

    # Read the STL name
    line1 = fidCONTENT[0]
    if (len(line1) >= 7):
        stlNAME = line1[6:]
    else:
        stlNAME = 'unnamed_object';

    # Read the vector normals
    stringNORMALS = fidCONTENT[np.char.find(fidCONTENT,'facet normal')+1 > 0]
    coordNORMALS  = np.array(np.char.split(stringNORMALS).tolist())[:,2:].astype(float)

    # Read the vertex coordinates
    facetTOTAL       = stringNORMALS.size
    stringVERTICES   = fidCONTENT[np.char.find(fidCONTENT,'vertex')+1 > 0]
    coordVERTICESall = np.array(np.char.split(stringVERTICES).tolist())[:,1:].astype(float)
    cotemp           = coordVERTICESall.reshape((3,facetTOTAL,3),order='F')
    coordVERTICES    = cotemp.transpose(1,2,0)

    for i in range(len(coordVERTICES)):
        coordVERTICES[i] = coordVERTICES[i].T

    return [coordVERTICES,coordNORMALS,stlNAME]


def Read_stl(stlFILENAME):
    stlFORMAT = stlGetFormat(stlFILENAME)

    if stlFORMAT=='ascii':
        [coordVERTICES,coordNORMALS,stlNAME] = READ_stlascii(stlFILENAME)
    elif stlFORMAT=='binary':
        [coordVERTICES,coordNORMALS] = READ_stlbinary(stlFILENAME)
        stlNAME = 'unnamed_object'
    return [coordVERTICES,coordNORMALS,stlNAME]

# stl = Read_stl('0911_STL_selfmade_binary.stl')
# # for i in range(len(stl[0])):
# #     stl[0][i] = stl[0][i].T
# stl_2 = stl[0].reshape(-1, 3)
# print(stl_2, '\n')


# def stl_read(filnm):
#     with open(filnm, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#         pts = list()
#         for line in lines:
#             str_line = line.strip()  # 使用strip()方法去除每行末尾的换行符
#             if str_line[:6] == 'vertex':
#                 unit = str_line[7:].split(' ')
#                 pts.append(list(map(float, unit)))
#     pts = np.array(pts)
#     return pts

# print(stl_read('0911_STL_selfmade_ascll.stl'))


def stl_faces(pts: np.ndarray):
    trians = np.empty((0, 3), dtype=int)
    for i in range(len(pts) // 3):
        array = np.array([i * 3, i * 3 + 1, i * 3 + 2])
        trians = np.r_[trians, [array]]
    return trians


def fanorm_calculator(pts: np.ndarray):
    fanorms = np.empty((0, 3))
    for i in range(len(pts) // 3):
        array1 = pts[i * 3 + 1] - pts[i * 3]
        array2 = pts[i * 3 + 2] - pts[i * 3 + 1]
        fanorm = np.cross(array1, array2)
        fanorm = fanorm / np.linalg.norm(fanorm)
        fanorms = np.r_[fanorms, [fanorm]]
    return fanorms

def stl_save(pts: np.ndarray, fanorms: np.ndarray, filnm):
    if filnm[-4:] != '.stl':
        filnm = filnm + '.stl'
    with open(filnm, 'w', encoding='utf-8') as file:
        fanorms = fanorms.tolist()
        pts = pts.tolist()
        file.write('solid WRAP' + '\n')
        for i in range(len(fanorms)):
            cnt = 0
            while cnt < 6:
                if cnt == 0:
                    file.write('facet normal' + ' ' + str(fanorms[i][0]) + ' ' + str(fanorms[i][1]) + ' '
                               + str(fanorms[i][2]) + '\n')
                elif cnt == 1:
                    file.write('outer loop' + '\n')
                elif 2 <= cnt <= 4:
                    file.write('vertex' + ' ' + str(pts[i * 3 + cnt - 2][0]) + ' '
                               + str(pts[i * 3 + cnt - 2][1]) + ' ' + str(pts[i * 3 + cnt - 2][2]) + '\n')
                else:
                    file.write('endloop' + '\n' + 'endfacet' + '\n')
                cnt += 1
        file.write('endsolid WRAP' + '\n')

