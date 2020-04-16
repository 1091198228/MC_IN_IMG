# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:28:18 2020

@author: xiaolong
"""

#!/bin/python
import cv2
import math

#图片路径
imgdir="16.jpg"
#缩放倍数
bs=3
#我的世界函数文件路径
mcfunction=r"D:\GAME\MC\.minecraft\versions\1.15.2\saves\新的世界\datapacks\mytest\data\test\functions\test1.mcfunction"

#目标生成区域左上角坐标
xyz = [8,100,20]

def openimg(imgdir,bl):
    #传入图片路径和，图片缩放比例
    imge=cv2.imread(imgdir)
    imge=cv2.resize(imge,(int(imge.shape[1]/bl),int(imge.shape[0]/bl)),interpolation=cv2.INTER_AREA)
    return imge


def ColourDistance(rgb_1, rgb_2):
     #颜色对比函数
     R_1,G_1,B_1 = rgb_1
     R_2,G_2,B_2 = rgb_2
     rmean = (R_1 +R_2 ) / 2
     R = R_1 - R_2
     G = G_1 -G_2
     B = B_1 - B_2
     return math.sqrt((2+rmean/256)*(R**2)+4*(G**2)+(2+(255-rmean)/256)*(B**2))

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
        #石头minecraft:stone
        return("fill {} {} {} {} {} {} minecraft:stone\n".format(x+col,y-row,z,x+col,y-row,z))

"""
    方块名     方块英文名                   RGB
 白色羊毛	    minecraft:white_wool	    255 255 255
 橙色羊毛	    minecraft:orange_wool   	240	118	19
 品红色羊毛   minecraft:magenta_wool		255	0	255
 淡蓝色羊毛   minecraft:light_blue_wool   0	255	255
 黄色羊毛	    minecraft:yellow_wool		255	255	0
 黄绿色羊毛  	minecraft:lime_wool		    112	185	25
 粉红色羊毛	minecraft:pink_wool		    237	141	172
 灰色羊毛	    minecraft:gray_wool	        128	128	128
 淡灰色羊毛	minecraft:light_gray_wool	192	192	192
 青色羊毛	    minecraft:cyan_wool	        0	128	128
 紫色羊毛	    minecraft:purple_wool	   	128	0	128
 蓝色羊毛	    minecraft:blue_wool	        0	0	255
 棕色羊毛	    minecraft:brown_wool      	128	128	0
 绿色羊毛	    minecraft:green_wool      	0	128	0
 红色羊毛	    minecraft:red_wool        	255	0	0
 黑色羊毛	    minecraft:black_wool      	0	0	0

"""
white_wool=(255,255,255)
orange_wool=(240,118,19)
magenta_wool=(255,0,255)
light_blue_wool=(0,255,255)
yellow_wool=(255,255,0)
lime_wool=(112,185,25)
pink_wool=(237,141,172)
gray_wool=(128,128,128)
light_gray_wool=(192,192,192)
cyan_wool=(0,128,128)
purple_wool=(128,0,128)
blue_wool=(0,0,255)
brown_wool=(128,128,0)
green_wool=(0,128,0)
red_wool=(255,0,0)
black_wool=(0,0,0)


def echocode3(xyz,rgb,row,col):
    #传入坐标、像素值、y轴偏移、x轴偏移
    #根据传入的像素值来判断生成什么颜色的方块

    x=xyz[0]
    y=xyz[1]
    z=xyz[2]
    cols2=[]
    cols1=[]
    for i in (white_wool,orange_wool,magenta_wool,light_blue_wool,yellow_wool,lime_wool,pink_wool,gray_wool,light_gray_wool,cyan_wool,purple_wool,blue_wool,brown_wool,green_wool,red_wool,black_wool):
        cols1.append(ColourDistance(rgb, i))
    cols2=cols1[:]
    cols2.sort(reverse=False)
    c_id=cols1.index(cols2[0])
    if c_id==0:
        return("fill {} {} {} {} {} {} minecraft:white_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    elif c_id==1:
        return("fill {} {} {} {} {} {} minecraft:orange_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    elif c_id==2:
        return("fill {} {} {} {} {} {} minecraft:magenta_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    elif c_id==3:
        return("fill {} {} {} {} {} {} minecraft:light_blue_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    elif c_id==4:
        return("fill {} {} {} {} {} {} minecraft:yellow_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    elif c_id==5:
        return("fill {} {} {} {} {} {} minecraft:lime_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    elif c_id==6:
        return("fill {} {} {} {} {} {} minecraft:pink_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    elif c_id==7:
        return("fill {} {} {} {} {} {} minecraft:gray_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    elif c_id==8:
        return("fill {} {} {} {} {} {} minecraft:light_gray_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    elif c_id==9:
        return("fill {} {} {} {} {} {} minecraft:cyan_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    elif c_id==10:
        return("fill {} {} {} {} {} {} minecraft:purple_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    elif c_id==11:
        return("fill {} {} {} {} {} {} minecraft:blue_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    elif c_id==12:
        return("fill {} {} {} {} {} {} minecraft:brown_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    elif c_id==13:
        return("fill {} {} {} {} {} {} minecraft:green_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    elif c_id==14:
        return("fill {} {} {} {} {} {} minecraft:red_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    elif c_id==15:
        return("fill {} {} {} {} {} {} minecraft:black_wool\n".format(x+col,y,z+row,x+col,y,z+row))
    else:
        return("fill {} {} {} {} {} {} minecraft:glowstone\n".format(x+col,y,z+row,x+col,y,z+row))
    
    

def writetxt(mcfunction,xyz,imge):
    #传入我的世界函数文件路径、坐标、图片数组
    print(str(imge.shape[0]) + " " + str(imge.shape[1]))
    imge=imge[:,:,(2,1,0)]
    file = open(mcfunction,'w')
    for row in range(imge.shape[0]):  #行
        for col in range(imge.shape[1]): #列
            #print(imge[row][col])
            file.write(echocode3(xyz,imge[row][col], row, col))        
    file.close()




imge=openimg(imgdir,bs)
writetxt(mcfunction,xyz,imge)

#预览图片,但这不是在游戏里的效果图
cv2.namedWindow("Faces")
cv2.imshow("Faces", imge)
cv2.waitKey(0)        