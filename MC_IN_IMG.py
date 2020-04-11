# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:28:18 2020

@author: xiaolong
"""

#!/bin/python
import cv2

#图片路径
imgdir="4.png"

#我的世界函数文件路径
mcfunction=r"D:\GAME\MC\.minecraft\versions\1.15.2-forge-31.1.18\saves\test\datapacks\mytest\data\test\functions\test1.mcfunction"

#目标生成区域左上角坐标
xyz = [244,255,165]

def openimg(imgdir,bl):
    #传入图片路径和，图片缩放比例
    imge=cv2.imread(imgdir,0)
    imge=cv2.resize(imge,(int(imge.shape[1]/bl),int(imge.shape[0]/bl)),interpolation=cv2.INTER_AREA)
    return imge

#minecraft:glowstone    荧石
#minecraft:black_wool   黑色羊毛
#minecraft:stone        石头
#如果想显示更多颜色请添加命令生成规则

def echocode(xyz,vlue,row,col):
    #传入坐标、像素值、y轴偏移、x轴偏移
    #根据传入的像素值来判断生成什么颜色的方块
    x=xyz[0]
    y=xyz[1]
    z=xyz[2]
    if vlue > 200:
        #荧石
        return("fill {} {} {} {} {} {} minecraft:glowstone\n".format(x+col,y-row,z,x+col,y-row,z))
    elif vlue>20:
        #黑色羊毛
        return("fill {} {} {} {} {} {} minecraft:black_wool\n".format(x+col,y-row,z,x+col,y-row,z))
    else:
        #石头
        return("fill {} {} {} {} {} {} minecraft:stone\n".format(x+col,y-row,z,x+col,y-row,z))

def writetxt(mcfunction,xyz,imge):
    #传入我的世界函数文件路径、坐标、图片数组
    file = open(mcfunction,'w')
    for row in range(imge.shape[0]):  #行
        for col in range(imge.shape[1]): #列
            #print(imge[row][col])
            file.write(echocode(xyz,imge[row][col], row, col))        
    file.close()


imge=openimg(imgdir,3)
writetxt(mcfunction,xyz,imge)

#预览图片
cv2.namedWindow("Faces")
cv2.imshow("Faces", imge)
cv2.waitKey(0)        