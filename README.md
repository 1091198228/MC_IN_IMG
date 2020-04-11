# MC_IN_IMG
## 在我的世界里生成图片建筑

原图：
![原图](https://github.com/daichenglong/MC_IN_IMG/blob/master/4.png?raw=true)

效果：
![效果图](https://github.com/daichenglong/MC_IN_IMG/blob/master/%E6%95%88%E6%9E%9C/2020-04-11_17.59.19.png?raw=true)

原理：
+ 用cv2库把图片转换为二维数组
+ 循环遍历二维数组的像素值，判断每个像素值的大小，不同的值对应不同颜色的方块，然后把命令写入mcfunction文件。
+ 在我的世界执行函数。

## 什么是mcfunction文件？
我的世界1.12版本加入的有个 /function 命令 此命令可以让玩家调用外部函数，mcfunction文件里面写的有调用时执行的命令。

## 什么是数据包？
数据包（data pack）系统为玩家进一步定制其Minecraft体验提供了一种新方式。数据包可用于覆盖或添加新的进度、函数、战利品表和结构，而不进行任何代码修改。
[数据包参考链接](https://minecraft-zh.gamepedia.com/%E6%95%B0%E6%8D%AE%E5%8C%85#pack.mcmeta)

## 如果使用此脚本？

使用前需要做的
- 把```mytest.zip``` 压缩包，解压到到 ```世界存档名/datapacks/``` 下
- 修改```MC_IN_IMG.py```文件内的变量
 ```
#图片路径
imgdir="4.png"

#我的世界函数文件路径
mcfunction=r"世界存档的路径\test\datapacks\mytest\data\test\functions\test1.mcfunction"

#目标生成区域左上角坐标
xyz = [244,255,165]
```

在游戏生成图片建筑：，在游戏里面执行``` /function test:test1 ```命令

