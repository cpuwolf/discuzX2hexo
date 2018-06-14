---
title: X-Plane 11.30我们可以期待
tags:
  - 主程序
date: 2018-06-14 09:45:34
---

2018年刚刚在美国拉斯维加斯举行的模拟飞行博览会，LR也给出了他们的一些更新消息

# 新廊桥

11.25已经拥有645个机场集成了最新的真实廊桥

# 地景库升级

11.30 地景库增加了更多的可用素材，包括铁栅栏，厂房


{% asset_img libupdate_fans.jpg x-plane 11 %}

{% asset_img libupdate_lib.jpg x-plane 11 %}

{% asset_img libupdate_lib2.jpg x-plane 11 %}


# 实验性气动更新

螺旋桨会使空气加速，这会被加入空气动力运算中

{% asset_img air_prop.jpg x-plane 11 %}

downwash会在一定程度减小升力，当飞机主轮着地后，你不需要动水平尾翼，机头会自动回落，X-Plane一直有这个效应，但是austin发现这个效应有点过在现在的版本中。

{% asset_img air_downwash.jpg x-plane 11 %}

机身升力

以前X-Plane对机身产生的气动影响不是最正确，但是11.30不再如此。风洞设备太贵，只能简单测试

{% asset_img air_fuse.jpg x-plane 11 %}

{% asset_img air_force.jpg x-plane 11 %}

research mode

考虑到新气动对老飞机的影响，LR决定增加一个开关，来启动实验性气动模式。

{% asset_img air_research.jpg x-plane 11 %}


# 增压系统

X-Plane一直以来都支持缺氧黑视效果。11.30开始，飞机插件开发商可以设置氧气量，以及机上有几个人再用氧气，它会自动计算氧气能持续时间。飞利浦前段时间拿到了高空驾驶执照，我相信这套系统将非常接近现实

# 防冰系统

X-Plane一直已来支持飞机结冰，然后直接失控。11.30开始，不再如此简单粗暴，会支持电子防冰，压缩空气加热防冰，化学试剂防冰，充气放冰等类型

# 可变桨距螺旋桨控制器

11.30再次更新其中的逻辑接近现实

# CWS(control wheel steering)

这是自动驾驶模式，半人工参与自动驾驶。737MCP上就有CWS按钮，但是X-Plane以前一直没有实现，然而11.30将自带

# 飞利浦自动驾驶系统

15节侧风737自动降落实验已经成功演示了自动驾驶系统是如何成功工作的。飞利浦从X-Plane 10 就为很多知名的插件飞机做飞行系统，比如CRJ-200，FF777等。所以他是最有资格，和经验懂得插件机是如何实现自己的飞行系统的。而现在11.30，这套系统不再需要插件机单独开发，因为他已经成为了X-Plane 11.30的一部分。所以对于没有太强的开发能力的飞机插件团队，可以直接用11.30以后的自带系统完美实现自动驾驶。

# Vulkan

airfoilmaker已经移植到vulkan。这是一个标志，Vulkan移植到X-Plane 11可行性证明了。同时openGL会一直保持一定的兼容。

{% asset_img vulkan_airmaker.jpg x-plane 11 %}

# 粒子系统

11.30粒子是最值得期待部分。引擎排出的烟，热量视觉浑浊，引擎吸入的水汽，飞机在湿跑道起飞机轮带起的水雾，引擎着火，都可以用新粒子系统更真实虚拟出来。

{% asset_img partical_engsuck.jpg x-plane 11 %}

{% asset_img partical_wheel.jpg x-plane 11 %}

{% asset_img partical_fire.jpg x-plane 11 %}

{% asset_img partical_ext.jpg x-plane 11 %}

同时易用的粒子系统编辑器也会提供。

{% asset_img partical_smoke.jpg x-plane 11 %}

# 时间表

11.25 beta现在正在进行时

11.30 夏天结束或者秋天开始

Vulkan 可能2018年底beta，或者2019年

{% asset_img xxx.jpg x-plane 11 %}