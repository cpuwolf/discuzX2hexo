---
title: X-Plane 11虚拟局域网联网飞行
tags:
  - 多人游戏
  - 连飞
  - 局域网
date: 2017-09-13 07:10:23
---

闲话少说，先看看连飞能不能吸引你。

{% asset_img taxing.jpg x-plane 11 %}

{% asset_img chase.jpg x-plane 11 %}

{% asset_img bridge.jpg x-plane 11 %}

{% asset_img mountain.jpg x-plane 11 %}

{% asset_img water.jpg x-plane 11 %}

X-Plane 11局域网连飞的飞机是会参与气动运算的。也就是说前面的飞机有尾流。这是其他飞行模拟器没有的。

我要谈的是局域网联网。而不是一般说的连飞，一般的连飞，自己可以上各种飞行论坛，他们都有连飞服务器，这个不在这篇文章的范围内。

局域网联网是没有中心服务器的概念，每个小伙伴都是对等的。可是除了上大学时，宿舍里的同学可以局域网，在家怎么和小伙伴局域网？有个概念，就这样诞生了，叫虚拟局域网

<embed src="https://vswf.douyucdn.cn/share/vshare.swf?vid=p2V0JMV85j4vRY5k" allowFullScreen="true" quality="high" width="400" height="300" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash"></embed>

## 虚拟局域网 ##

经过一段学习，找到一个国外的网站提供虚拟局域网的服务。先注册账号，每个小伙伴都需要注册，就是邮箱和密码

https://accounts.logme.in/registration.aspx

注册完之后，需要到你的邮箱点击一个网站发给你的确认链接。

然后在我们群里有个叫hamachi的软件，需要安装，这个程序会为你的计算机安装驱动和后台服务，以后每次启动，默认都会加入虚拟局域网

{% asset_img hamachi.jpg x-plane 11 %}

重要：安装过程中，windows会提示你是否选择为工作网络，一定要选是。

如果一切顺利，程序启动后，会提示你输入注册的用户名和密码。

如果登陆也一切顺利，程序会提示你选择新建网络，还是加入现有网络。本群里有已有的虚拟局域网络，所以选加入已有的。

输入网络ID，群里已经公布

如果审核通过，你就正式加入了虚拟局域网，你的局域网IP地址就显示在hamachi这个软件上。我的IP是25.21.94.206

## X-plane 11 ##

XP的设置里面有多人游戏设置，如图

{% asset_img setting.jpg x-plane 11 %}

这里的逻辑是，把除你之外的其他所有小伙伴的IP，都要加进来。

## Hamachi安装错误 ##

如果hamachi.msi安装错误，那么导入下面的注册表，到你的系统。

{% asset_link msi_runas_admin.reg %}

之后，右键点击hamachi.msi文件，会多一个"Run as administrator“菜单，点击运行即可

