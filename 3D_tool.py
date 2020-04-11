# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 02:51:08 2020

@author: admin
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
ax = Axes3D(fig)
abc=np.zeros((10,10,10),dtype=int)
x1=[]
y1=[]
z1=[]

x2=[]
y2=[]
z2=[]
m='s'


def showimg():
    for x in range(abc.shape[0]):
        for y in range(abc.shape[1]):
            for z in range(abc.shape[2]):
                if abc[x][y][z]>20:
                    #print(abc[x][y][z])
                    x1.append(x)
                    y1.append(y)
                    z1.append(z)
                else:
                    x2.append(x)
                    y2.append(y)
                    z2.append(z)
    ax.scatter(z1, x1, y1, c='r', marker=m)
    ax.scatter(z2, x2, y2, c='#FFFFFF', marker=m)

ax.set_xlabel('Z Label')
ax.set_ylabel('X Label')
ax.set_zlabel('Y Label')



xyz=[0,0,0]
x=0
y=0
z=0
e=1
while(e):
    abc[x][y][z]=255    
    showimg()
    #plt.show()
    print("请输入指令")
    n=input()
    if n=='e':
        e=0
        #break
    elif n=='a':
        z=z-1
    elif n=='d':
        z=z+1
    elif n=='w':
        x=x+1
    elif n=='s':
        x=x-1
    else:
        print(0)

plt.show()
        

    