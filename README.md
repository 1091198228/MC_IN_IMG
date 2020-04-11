# MC_IN_IMG
在我的世界里生成图片建筑

原图：
![img](https://github.com/daichenglong/MC_IN_IMG/blob/master/4.png?raw=true)

效果：
![img](https://github.com/daichenglong/MC_IN_IMG/blob/master/%E6%95%88%E6%9E%9C/2020-04-11_17.59.19.png?raw=true)

原理：
1.用cv2库把图片转换为二维数组
2.循环遍历二维数组的像素值，判断每个像素值的大小，不同的值对应不同颜色的方块，然后把命令写入mcfunction文件。
3.在我的世界执行函数。
