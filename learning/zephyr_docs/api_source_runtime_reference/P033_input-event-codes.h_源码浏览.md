---
id: learning.zephyr-docs.api-source-runtime-reference.page-33
title: input-event-codes.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input-event-codes_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_input-event-codes.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/input-event-codes_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/input-event-codes_8h.html)。

## 33.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00270"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00289"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00299"></a>
<a id="l00301"></a>
<a id="l00302"></a>

```c
/*
 * Copyright 2023 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * Input event codes, for codes available in Linux, use the same values as in
 * https://elixir.bootlin.com/linux/latest/source/include/uapi/linux/input-event-codes.h
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INPUT_INPUT_EVENT_CODES_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INPUT_INPUT_EVENT_CODES_H_



#define INPUT_EV_KEY 0x01
#define INPUT_EV_REL 0x02
#define INPUT_EV_ABS 0x03
#define INPUT_EV_MSC 0x04
#define INPUT_EV_DEVICE 0xef
#define INPUT_EV_VENDOR_START 0xf0
#define INPUT_EV_VENDOR_STOP 0xff

#define INPUT_KEY_RESERVED 0

/* zephyr-keep-sorted-start */
#define INPUT_KEY_0 11
#define INPUT_KEY_1 2
#define INPUT_KEY_2 3
#define INPUT_KEY_3 4
#define INPUT_KEY_4 5
#define INPUT_KEY_5 6
#define INPUT_KEY_6 7
#define INPUT_KEY_7 8
#define INPUT_KEY_8 9
#define INPUT_KEY_9 10
#define INPUT_KEY_A 30
#define INPUT_KEY_APOSTROPHE 40
#define INPUT_KEY_B 48
#define INPUT_KEY_BACK 158
#define INPUT_KEY_BACKSLASH 43
#define INPUT_KEY_BACKSPACE 14
#define INPUT_KEY_BLUETOOTH 237
#define INPUT_KEY_BRIGHTNESSDOWN 224
#define INPUT_KEY_BRIGHTNESSUP 225
#define INPUT_KEY_C 46
#define INPUT_KEY_CAPSLOCK 58
#define INPUT_KEY_CLOSECD 160
#define INPUT_KEY_COFFEE 152
#define INPUT_KEY_COMMA 51
#define INPUT_KEY_COMPOSE 127
#define INPUT_KEY_CONNECT 218
#define INPUT_KEY_D 32
#define INPUT_KEY_DELETE 111
#define INPUT_KEY_DOLLAR 0x1b2
#define INPUT_KEY_DOT 52
#define INPUT_KEY_DOWN 108
#define INPUT_KEY_E 18
#define INPUT_KEY_EJECTCD 161
#define INPUT_KEY_EJECTCLOSECD 162
#define INPUT_KEY_END 107
#define INPUT_KEY_ENTER 28
#define INPUT_KEY_EQUAL 13
#define INPUT_KEY_ESC 1
#define INPUT_KEY_EURO 0x1b3
#define INPUT_KEY_F 33
#define INPUT_KEY_F1 59
#define INPUT_KEY_F10 68
#define INPUT_KEY_F11 87
#define INPUT_KEY_F12 88
#define INPUT_KEY_F13 183
#define INPUT_KEY_F14 184
#define INPUT_KEY_F15 185
#define INPUT_KEY_F16 186
#define INPUT_KEY_F17 187
#define INPUT_KEY_F18 188
#define INPUT_KEY_F19 189
#define INPUT_KEY_F2 60
#define INPUT_KEY_F20 190
#define INPUT_KEY_F21 191
#define INPUT_KEY_F22 192
#define INPUT_KEY_F23 193
#define INPUT_KEY_F24 194
#define INPUT_KEY_F3 61
#define INPUT_KEY_F4 62
#define INPUT_KEY_F5 63
#define INPUT_KEY_F6 64
#define INPUT_KEY_F7 65
#define INPUT_KEY_F8 66
#define INPUT_KEY_F9 67
#define INPUT_KEY_FASTFORWARD 208
#define INPUT_KEY_FAVORITES 364
#define INPUT_KEY_FORWARD 159
#define INPUT_KEY_G 34
#define INPUT_KEY_GRAVE 41
#define INPUT_KEY_H 35
#define INPUT_KEY_HOME 102
#define INPUT_KEY_I 23
#define INPUT_KEY_INSERT 110
#define INPUT_KEY_J 36
#define INPUT_KEY_K 37
#define INPUT_KEY_KP0 82
#define INPUT_KEY_KP1 79
#define INPUT_KEY_KP2 80
#define INPUT_KEY_KP3 81
#define INPUT_KEY_KP4 75
#define INPUT_KEY_KP5 76
#define INPUT_KEY_KP6 77
#define INPUT_KEY_KP7 71
#define INPUT_KEY_KP8 72
#define INPUT_KEY_KP9 73
#define INPUT_KEY_KPASTERISK 55
#define INPUT_KEY_KPCOMMA 121
#define INPUT_KEY_KPDOT 83
#define INPUT_KEY_KPENTER 96
#define INPUT_KEY_KPEQUAL 117
#define INPUT_KEY_KPMINUS 74
#define INPUT_KEY_KPPLUS 78
#define INPUT_KEY_KPPLUSMINUS 118
#define INPUT_KEY_KPSLASH 98
#define INPUT_KEY_L 38
#define INPUT_KEY_LEFT 105
#define INPUT_KEY_LEFTALT 56
#define INPUT_KEY_LEFTBRACE 26
#define INPUT_KEY_LEFTCTRL 29
#define INPUT_KEY_LEFTMETA 125
#define INPUT_KEY_LEFTSHIFT 42
#define INPUT_KEY_M 50
#define INPUT_KEY_MENU 139
#define INPUT_KEY_MINUS 12
#define INPUT_KEY_MUTE 113
#define INPUT_KEY_N 49
#define INPUT_KEY_NEXTSONG 163
#define INPUT_KEY_NUMLOCK 69
#define INPUT_KEY_O 24
#define INPUT_KEY_P 25
#define INPUT_KEY_PAGEDOWN 109
#define INPUT_KEY_PAGEUP 104
#define INPUT_KEY_PAUSE 119
#define INPUT_KEY_PLAY 207
#define INPUT_KEY_PLAYPAUSE 164
#define INPUT_KEY_POWER 116
#define INPUT_KEY_PREVIOUSSONG 165
#define INPUT_KEY_PRINT 210
#define INPUT_KEY_Q 16
#define INPUT_KEY_R 19
#define INPUT_KEY_RECORD 167
#define INPUT_KEY_REWIND 168
#define INPUT_KEY_RIGHT 106
#define INPUT_KEY_RIGHTALT 100
#define INPUT_KEY_RIGHTBRACE 27
#define INPUT_KEY_RIGHTCTRL 97
#define INPUT_KEY_RIGHTMETA 126
#define INPUT_KEY_RIGHTSHIFT 54
#define INPUT_KEY_S 31
#define INPUT_KEY_SCALE 120
#define INPUT_KEY_SCROLLLOCK 70
#define INPUT_KEY_SEMICOLON 39
#define INPUT_KEY_SLASH 53
#define INPUT_KEY_SLEEP 142
#define INPUT_KEY_SPACE 57
#define INPUT_KEY_STOPCD 166
#define INPUT_KEY_SYSRQ 99
#define INPUT_KEY_T 20
#define INPUT_KEY_TAB 15
#define INPUT_KEY_U 22
#define INPUT_KEY_UP 103
#define INPUT_KEY_UWB 239
#define INPUT_KEY_V 47
#define INPUT_KEY_VOLUMEDOWN 114
#define INPUT_KEY_VOLUMEUP 115
#define INPUT_KEY_W 17
#define INPUT_KEY_WAKEUP 143
#define INPUT_KEY_WLAN 238
#define INPUT_KEY_X 45
#define INPUT_KEY_Y 21
#define INPUT_KEY_Z 44
/* zephyr-keep-sorted-stop */


/* zephyr-keep-sorted-start */
#define INPUT_BTN_0 0x100
#define INPUT_BTN_1 0x101
#define INPUT_BTN_2 0x102
#define INPUT_BTN_3 0x103
#define INPUT_BTN_4 0x104
#define INPUT_BTN_5 0x105
#define INPUT_BTN_6 0x106
#define INPUT_BTN_7 0x107
#define INPUT_BTN_8 0x108
#define INPUT_BTN_9 0x109
#define INPUT_BTN_A INPUT_BTN_SOUTH
#define INPUT_BTN_B INPUT_BTN_EAST
#define INPUT_BTN_BACK 0x116
#define INPUT_BTN_C 0x132
#define INPUT_BTN_DPAD_DOWN 0x221
#define INPUT_BTN_DPAD_LEFT 0x222
#define INPUT_BTN_DPAD_RIGHT 0x223
#define INPUT_BTN_DPAD_UP 0x220
#define INPUT_BTN_EAST 0x131
#define INPUT_BTN_EXTRA 0x114
#define INPUT_BTN_FORWARD 0x115
#define INPUT_BTN_GEAR_DOWN 0x150
#define INPUT_BTN_GEAR_UP 0x151
#define INPUT_BTN_LEFT 0x110
#define INPUT_BTN_MIDDLE 0x112
#define INPUT_BTN_MODE 0x13c
#define INPUT_BTN_NORTH 0x133
#define INPUT_BTN_RIGHT 0x111
#define INPUT_BTN_SELECT 0x13a
#define INPUT_BTN_SIDE 0x113
#define INPUT_BTN_SOUTH 0x130
#define INPUT_BTN_START 0x13b
#define INPUT_BTN_TASK 0x117
#define INPUT_BTN_THUMBL 0x13d
#define INPUT_BTN_THUMBR 0x13e
#define INPUT_BTN_TL 0x136
#define INPUT_BTN_TL2 0x138
#define INPUT_BTN_TOUCH 0x14a
#define INPUT_BTN_TR 0x137
#define INPUT_BTN_TR2 0x139
#define INPUT_BTN_WEST 0x134
#define INPUT_BTN_X INPUT_BTN_NORTH
#define INPUT_BTN_Y INPUT_BTN_WEST
#define INPUT_BTN_Z 0x135
/* zephyr-keep-sorted-stop */

/* zephyr-keep-sorted-start */
#define INPUT_ABS_BRAKE 0x0a
#define INPUT_ABS_GAS 0x09
#define INPUT_ABS_MT_SLOT 0x2f
#define INPUT_ABS_RUDDER 0x07
#define INPUT_ABS_RX 0x03
#define INPUT_ABS_RY 0x04
#define INPUT_ABS_RZ 0x05
#define INPUT_ABS_THROTTLE 0x06
#define INPUT_ABS_WHEEL 0x08
#define INPUT_ABS_X 0x00
#define INPUT_ABS_Y 0x01
#define INPUT_ABS_Z 0x02
/* zephyr-keep-sorted-stop */

/* zephyr-keep-sorted-start */
#define INPUT_REL_DIAL 0x07
#define INPUT_REL_HWHEEL 0x06
#define INPUT_REL_MISC 0x09
#define INPUT_REL_RX 0x03
#define INPUT_REL_RY 0x04
#define INPUT_REL_RZ 0x05
#define INPUT_REL_WHEEL 0x08
#define INPUT_REL_X 0x00
#define INPUT_REL_Y 0x01
#define INPUT_REL_Z 0x02
/* zephyr-keep-sorted-stop */

/* zephyr-keep-sorted-start */
#define INPUT_MSC_SCAN 0x04
/* zephyr-keep-sorted-stop */


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INPUT_INPUT_EVENT_CODES_H_ */
```

## 33.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

输入事件代码（Input event codes）：对于 Linux 中已有的代码，采用与[Linux input-event-codes.h](https://elixir.bootlin.com/linux/latest/source/include/uapi/linux/input-event-codes.h) 相同的值。

### 注释 2：原第 41 行

保持排序区域的起始标记：`zephyr-keep-sorted-start`。

### 注释 3：原第 193 行

保持排序区域的结束标记：`zephyr-keep-sorted-stop`。

### 注释 4：原第 202 行

保持排序区域的起始标记：`zephyr-keep-sorted-start`。

### 注释 5：原第 247 行

保持排序区域的结束标记：`zephyr-keep-sorted-stop`。

### 注释 6：原第 255 行

保持排序区域的起始标记：`zephyr-keep-sorted-start`。

### 注释 7：原第 268 行

保持排序区域的结束标记：`zephyr-keep-sorted-stop`。

### 注释 8：原第 276 行

保持排序区域的起始标记：`zephyr-keep-sorted-start`。

### 注释 9：原第 287 行

保持排序区域的结束标记：`zephyr-keep-sorted-stop`。

### 注释 10：原第 295 行

保持排序区域的起始标记：`zephyr-keep-sorted-start`。

### 注释 11：原第 297 行

保持排序区域的结束标记：`zephyr-keep-sorted-stop`。

### 注释 12：原第 302 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INPUT_INPUT_EVENT_CODES_H_`。

## 33.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/input-event-codes_8h.html)

---

[上一章](P032_ifx_clock_source_psoc4xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P034_intc_mchp_xec_ecia.h_源码浏览.md)
