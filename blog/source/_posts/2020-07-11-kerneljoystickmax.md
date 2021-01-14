---
title: Linux Kernel joystick max button number limitation is 80
tags:
  - 插件
categories: []
toc: false
date: 2020-07-11 07:08:39
---

{% asset_img linux_joystick_maxbutton.jpg x-plane 11 %}


Today latest Linux kernel stable version is 5.7.8.


we found Linux kernel has max joystick buttons up to 80, no more


We are selling USB joystick device QMCP737C for flight simulator, which is nothing but common USB HID joystick. it has physical 104 buttons


Product link
https://x-plane.vip/quickmade/qmcp737c/



it works good on Windows, Mac, but not on Linux. 
Linux kernel exposes /dev/input/js0 max to 80 button, but we have 104 buttons.


I did a lots of google search, but nothing I got. then I have to look at Kernel source, to find out where this number max 80 comes from


Eventually I found the final limitation


#define BTN_JOYSTICK 0x120

#define BTN_DEAD 0x12f

#define BTN_TRIGGER_HAPPY 0x2c0

#define KEY_MAX 0x2ff

include/uapi/linux/input-event-codes.h

according to function hidinput_configure_usage() in file drivers/hid/hid-input.c

the joystick button mapping is not a continues space, general speak the mapping space is from

BTN_JOYSTICK~BTN_DEAD 
BTN_TRIGGER_HAPPY~KEY_MAX

and finally I got the max limitation is 80.

my question is why KEY_MAX is 0x2ff?  
this number 0x2ff looks like not align with char? integer? the answer is no
 
so may I ask to expand KEY_MAX to such as 0x4ff?

I did a quick test on Ubuntu, all 104 buttons are showing up

{% asset_img after_linux_joystick_patch.jpg x-plane 11 %}

then a patch is submitted to kernel driver input group
https://patchwork.kernel.org/patch/11657985/