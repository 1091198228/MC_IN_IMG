# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:42:27 2020

@author: admin
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

import cv2

#图片路径
imgdir="huaweilogo.jpg"
#我的世界函数文件路径
mcfunction=r"D:\GAME\MC\.minecraft\versions\1.15.2-forge-31.1.18\saves\test\datapacks\mytest\data\test\functions\test1.mcfunction"
mcfunction2=r"D:\GAME\MC\.minecraft\versions\1.15.2-forge-31.1.18\saves\test\datapacks\mytest\data\test\functions\air.mcfunction"
#目标生成区域左上角坐标
xyz = [243,73,70]
bl=4
imge=cv2.imread(imgdir,0)
imge=cv2.resize(imge,(int(imge.shape[1]/bl),int(imge.shape[0]/bl)),interpolation=cv2.INTER_AREA)
   
 
fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
ax = Axes3D(fig)
#m='.'
# xs=[]
# ys=[]
# zs=[]
# x1=[]
# y1=[]
# z1=[]
# for row in range(imge.shape[0]):  #行
#         for col in range(imge.shape[1]):
#             if imge[row][col]>200:
#                 xs.append(col)
#                 ys.append(-row)
#                 zs.append(1)
#             else:
#                 x1.append(col)
#                 y1.append(-row)
#                 z1.append(1)


# ax.scatter(zs, xs, ys, c='r', marker=m)
# ax.scatter(z1, x1, y1, c='k', marker=m)

def echocode(xyz,vlue,x,y,z):
    #传入坐标、像素值、x轴偏移、y轴偏移、z轴偏移
    #根据传入的像素值来判断生成什么颜色的方块
    if vlue > 200:
        #荧石
        return("fill {} {} {} {} {} {} minecraft:glowstone\n".format(xyz[0]+x,xyz[1]-y,xyz[2]+z,xyz[0]+x,xyz[1]-y,xyz[2]+z))
    elif vlue>20:
        #黑色羊毛
        return("fill {} {} {} {} {} {} minecraft:black_wool\n".format(xyz[0]+x,xyz[1]-y,xyz[2]+z,xyz[0]+x,xyz[1]-y,xyz[2]+z))
    else:
        #石头minecraft:stone
        #空气minecraft:air
        return("fill {} {} {} {} {} {} minecraft:air\n".format(xyz[0]+x,xyz[1]-y,xyz[2]+z,xyz[0]+x,xyz[1]-y,xyz[2]+z))



abc=np.zeros((10,10,10),dtype=int)
x1=[]
y1=[]
z1=[]

x2=[]
y2=[]
z2=[]

abc[0][0][1]=255
abc[0][0][2]=255
abc[0][0][3]=255
abc[0][0][4]=255
abc[0][0][5]=255
abc[0][0][6]=255
abc[0][0][7]=255
abc[0][1][3]=255
abc[0][2][3]=255
abc[0][3][3]=255
abc[0][4][3]=255


abc[9][9][9]=255

file = open(mcfunction,'w')
for x in range(abc.shape[0]):
    for y in range(abc.shape[1]):
        for z in range(abc.shape[2]):
            if abc[x][y][z]>20:
                print(abc[x][y][z])
                x1.append(x)
                y1.append(-y)
                z1.append(z)
                file.write(echocode(xyz, abc[x][y][z],x,y,z))
            else:
                x2.append(x)
                y2.append(-y)
                z2.append(z)
                file.write(echocode(xyz, abc[x][y][z],x,y,z))
file.close()


m='s'

ax.scatter(z1, x1, y1, c='r', marker=m)
#ax.scatter(z2, x2, y2, c='#FFFFFF', marker=m)

#清空函数
file = open(mcfunction2,'w')
for x in range(abc.shape[0]):
    for y in range(abc.shape[1]):
        for z in range(abc.shape[2]):
            file.write("fill {} {} {} {} {} {} minecraft:air\n".format(xyz[0]+x,xyz[1]-y,xyz[2]+z,xyz[0]+x,xyz[1]-y,xyz[2]+z))
file.close()

ax.set_xlabel('Z Label')
ax.set_ylabel('X Label')
ax.set_zlabel('Y Label')
 
plt.show()