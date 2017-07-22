---
title: XPlane地景的目录和文件结构
date: 2016-03-22 04:53:28
---


![cpuwolf](/images/data/attachment/201603/22/124840cwbm9wwjtl4ow3lw.jpg)

X-Plane 10 地景由4种文件组成：


* 地景片文件.DSF，如上图，描述一个经纬度片的信息
* 美工类文件.OBJ, .PNG, DDS等
* 机场数据文件apt.dat
* 库文件列表library.txt


其中.DSF文件时重中之重：
它的命名和目录有规定

My Super Scenery       Earth nav data      
    +40-080         
      +42-072.dsf         
      +42-071.dsf

.dsf文件是按经纬度命名的，每1度一个文件。然而目录+40-080，可以最多放100个.dsf文件。


