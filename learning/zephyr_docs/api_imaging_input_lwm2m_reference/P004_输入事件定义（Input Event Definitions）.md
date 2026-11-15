---
id: learning.zephyr-docs.api-imaging-input-lwm2m-reference.page-4
title: 输入事件定义（Input Event Definitions）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_输入事件定义（Input Event Definitions）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-member-group"></a>
<a id="member-group"></a>

## 4.1\_输入事件类型（Input event types.）



<a id="r_ga4a517c31bdbdd1bd82ba456d256ef1f1"></a>

```c
#define INPUT_EV_KEY 0x01
```

相关声明：[INPUT_EV_KEY](#ga4a517c31bdbdd1bd82ba456d256ef1f1)。

按键事件（Key event）。

<a id="r_ga02de6c85efab3d21eb81e88e54d58e03"></a>

```c
#define INPUT_EV_REL 0x02
```

相关声明：[INPUT_EV_REL](#ga02de6c85efab3d21eb81e88e54d58e03)。

相对坐标事件（Relative coordinate event）。

<a id="r_gaa6bcd6755fbdb3eb103f03a72759ce4f"></a>

```c
#define INPUT_EV_ABS 0x03
```

相关声明：[INPUT_EV_ABS](#gaa6bcd6755fbdb3eb103f03a72759ce4f)。

绝对坐标事件（Absolute coordinate event）。

<a id="r_ga40ab1faa2e28e32c30016ad854afa6cf"></a>

```c
#define INPUT_EV_MSC 0x04
```

相关声明：[INPUT_EV_MSC](#ga40ab1faa2e28e32c30016ad854afa6cf)。

其他事件（Miscellaneous event）。

<a id="r_ga3ebe8a83ea38c4c87cda6bc9e18f2e61"></a>

```c
#define INPUT_EV_DEVICE 0xef
```

相关声明：[INPUT_EV_DEVICE](#ga3ebe8a83ea38c4c87cda6bc9e18f2e61)。

设备专用输入事件（Device specific input event）。

<a id="r_ga7037a9ea2e0a63c40a5d206e507e5f42"></a>

```c
#define INPUT_EV_VENDOR_START 0xf0
```

相关声明：[INPUT_EV_VENDOR_START](#ga7037a9ea2e0a63c40a5d206e507e5f42)。

厂商专用事件范围起点（Vendor specific event start）。

<a id="r_gaa19a341e18ff5c43e1b8ddf58c7b9676"></a>

```c
#define INPUT_EV_VENDOR_STOP 0xff
```

相关声明：[INPUT_EV_VENDOR_STOP](#gaa19a341e18ff5c43e1b8ddf58c7b9676)。

厂商专用事件范围终点（Vendor specific event stop）。

## 4.2\_输入事件的按键编码（Input event KEY codes.）



<a id="r_ga94e5a0d74dad76e57679b97af90ecb65"></a>

```c
#define INPUT_KEY_RESERVED 0
```

相关声明：[INPUT_KEY_RESERVED](#ga94e5a0d74dad76e57679b97af90ecb65)。

保留，不要使用（Reserved, do not use）。

<a id="r_gab41cb2f1768b0a0667ab6509b6d3af21"></a>

```c
#define INPUT_KEY_0 11
```

相关声明：[INPUT_KEY_0](#gab41cb2f1768b0a0667ab6509b6d3af21)。

0键（0 Key）。

<a id="r_gad62520853a15b74d68c1bab5a3119eaa"></a>

```c
#define INPUT_KEY_1 2
```

相关声明：[INPUT_KEY_1](#gad62520853a15b74d68c1bab5a3119eaa)。

1键（1 Key）。

<a id="r_gadb02e289d07d4d4457c88b1ada7e2534"></a>

```c
#define INPUT_KEY_2 3
```

相关声明：[INPUT_KEY_2](#gadb02e289d07d4d4457c88b1ada7e2534)。

2键（2 Key）。

<a id="r_ga95a246cefcaafd26d15c1c124bdf2ca4"></a>

```c
#define INPUT_KEY_3 4
```

相关声明：[INPUT_KEY_3](#ga95a246cefcaafd26d15c1c124bdf2ca4)。

3键（3 Key）。

<a id="r_ga0c16c2e62a65eab0fe8952a4cf60254d"></a>

```c
#define INPUT_KEY_4 5
```

相关声明：[INPUT_KEY_4](#ga0c16c2e62a65eab0fe8952a4cf60254d)。

4键（4 Key）。

<a id="r_ga386e2c69d5e5a9549668b1a2a2d297e1"></a>

```c
#define INPUT_KEY_5 6
```

相关声明：[INPUT_KEY_5](#ga386e2c69d5e5a9549668b1a2a2d297e1)。

5键（5 Key）。

<a id="r_ga87e0cea90040710253718ce29c407f3e"></a>

```c
#define INPUT_KEY_6 7
```

相关声明：[INPUT_KEY_6](#ga87e0cea90040710253718ce29c407f3e)。

6键（6 Key）。

<a id="r_ga090686eaaacddb8c2f58b31b4b9801b8"></a>

```c
#define INPUT_KEY_7 8
```

相关声明：[INPUT_KEY_7](#ga090686eaaacddb8c2f58b31b4b9801b8)。

7键（7 Key）。

<a id="r_ga6f2b66c0eea17b044778a326ffcd3f57"></a>

```c
#define INPUT_KEY_8 9
```

相关声明：[INPUT_KEY_8](#ga6f2b66c0eea17b044778a326ffcd3f57)。

8键（8 Key）。

<a id="r_ga91473de481c47f3f9e40caf42e49250f"></a>

```c
#define INPUT_KEY_9 10
```

相关声明：[INPUT_KEY_9](#ga91473de481c47f3f9e40caf42e49250f)。

9键（9 Key）。

<a id="r_ga553b457efaafb3cdc41e7b1e953cd6fe"></a>

```c
#define INPUT_KEY_A 30
```

相关声明：[INPUT_KEY_A](#ga553b457efaafb3cdc41e7b1e953cd6fe)。

A键（A Key）。

<a id="r_gaa528a10eb85fa9dc46198e08962fab3a"></a>

```c
#define INPUT_KEY_APOSTROPHE 40
```

相关声明：[INPUT_KEY_APOSTROPHE](#gaa528a10eb85fa9dc46198e08962fab3a)。

单引号键（Apostrophe Key）。

<a id="r_gaaae2c60e8907c14c094e5c1c4e3dae3b"></a>

```c
#define INPUT_KEY_B 48
```

相关声明：[INPUT_KEY_B](#gaaae2c60e8907c14c094e5c1c4e3dae3b)。

B键（B Key）。

<a id="r_gab5ad87c6e97f6b09f9dc1a1570a9c299"></a>

```c
#define INPUT_KEY_BACK 158
```

相关声明：[INPUT_KEY_BACK](#gab5ad87c6e97f6b09f9dc1a1570a9c299)。

后退键（Back Key）。

<a id="r_ga180fcae595fbc580bfe1a94414a4b02b"></a>

```c
#define INPUT_KEY_BACKSLASH 43
```

相关声明：[INPUT_KEY_BACKSLASH](#ga180fcae595fbc580bfe1a94414a4b02b)。

反斜杠键（Backslash Key）。

<a id="r_ga654ffbdc8f2fef696ee0237704cebc34"></a>

```c
#define INPUT_KEY_BACKSPACE 14
```

相关声明：[INPUT_KEY_BACKSPACE](#ga654ffbdc8f2fef696ee0237704cebc34)。

退格键（Backspace Key）。

<a id="r_ga26f6330d7631bdae0f2bb34f623a85ae"></a>

```c
#define INPUT_KEY_BLUETOOTH 237
```

相关声明：[INPUT_KEY_BLUETOOTH](#ga26f6330d7631bdae0f2bb34f623a85ae)。

蓝牙键（Bluetooth Key）。

<a id="r_gac4afc3e97b18a1f22e3d59730177e27f"></a>

```c
#define INPUT_KEY_BRIGHTNESSDOWN 224
```

相关声明：[INPUT_KEY_BRIGHTNESSDOWN](#gac4afc3e97b18a1f22e3d59730177e27f)。

降低亮度键（Brightness Down Key）。

<a id="r_gaff59e776a3e3a0fe4d32caeb41a32c53"></a>

```c
#define INPUT_KEY_BRIGHTNESSUP 225
```

相关声明：[INPUT_KEY_BRIGHTNESSUP](#gaff59e776a3e3a0fe4d32caeb41a32c53)。

提高亮度键（Brightness Up Key）。

<a id="r_ga1b88afc2eacfbbd778785398baebd287"></a>

```c
#define INPUT_KEY_C 46
```

相关声明：[INPUT_KEY_C](#ga1b88afc2eacfbbd778785398baebd287)。

C键（C Key）。

<a id="r_ga8dfa14142766962272afc77538f8a909"></a>

```c
#define INPUT_KEY_CAPSLOCK 58
```

相关声明：[INPUT_KEY_CAPSLOCK](#ga8dfa14142766962272afc77538f8a909)。

大写锁定键（Caps Lock Key）。

<a id="r_gaee0312912b4c067c60d77b26e56cd905"></a>

```c
#define INPUT_KEY_CLOSECD 160
```

相关声明：[INPUT_KEY_CLOSECD](#gaee0312912b4c067c60d77b26e56cd905)。

关闭光驱托盘键（Close CD Key）。

<a id="r_ga345dc788101108c27f488cfa0fc885c8"></a>

```c
#define INPUT_KEY_COFFEE 152
```

相关声明：[INPUT_KEY_COFFEE](#ga345dc788101108c27f488cfa0fc885c8)。

屏幕保护键（Screen Saver Key）。

<a id="r_ga1220a9e90676992fcd3c308a7f1038f7"></a>

```c
#define INPUT_KEY_COMMA 51
```

相关声明：[INPUT_KEY_COMMA](#ga1220a9e90676992fcd3c308a7f1038f7)。

逗号键（Comma Key）。

<a id="r_ga52882fff91dc0c288cf0b60baa60be65"></a>

```c
#define INPUT_KEY_COMPOSE 127
```

相关声明：[INPUT_KEY_COMPOSE](#ga52882fff91dc0c288cf0b60baa60be65)。

组合字符键（Compose Key）。

<a id="r_gaedf1f55d35163e56ca03f4409ea6b7d0"></a>

```c
#define INPUT_KEY_CONNECT 218
```

相关声明：[INPUT_KEY_CONNECT](#gaedf1f55d35163e56ca03f4409ea6b7d0)。

连接键（Connect Key）。

<a id="r_ga206eda236c1ce08e3ad6eef192ac303e"></a>

```c
#define INPUT_KEY_D 32
```

相关声明：[INPUT_KEY_D](#ga206eda236c1ce08e3ad6eef192ac303e)。

D键（D Key）。

<a id="r_ga2abef21124d504927c675959331a4c3b"></a>

```c
#define INPUT_KEY_DELETE 111
```

相关声明：[INPUT_KEY_DELETE](#ga2abef21124d504927c675959331a4c3b)。

删除键（Delete Key）。

<a id="r_gacd0cb4c35c9463bf61dcb247fc4bd546"></a>

```c
#define INPUT_KEY_DOLLAR 0x1b2
```

相关声明：[INPUT_KEY_DOLLAR](#gacd0cb4c35c9463bf61dcb247fc4bd546)。

美元符号键（Dollar Key）。

<a id="r_gacbd30145c479c472d105a0c5251c0e4d"></a>

```c
#define INPUT_KEY_DOT 52
```

相关声明：[INPUT_KEY_DOT](#gacbd30145c479c472d105a0c5251c0e4d)。

句点键（Dot Key）。

<a id="r_gad80b82e35e50f775a091b8f5031d2c9b"></a>

```c
#define INPUT_KEY_DOWN 108
```

相关声明：[INPUT_KEY_DOWN](#gad80b82e35e50f775a091b8f5031d2c9b)。

向下键（Down Key）。

<a id="r_ga4c1a1f169d8159ed36b194ae3d0aa0e7"></a>

```c
#define INPUT_KEY_E 18
```

相关声明：[INPUT_KEY_E](#ga4c1a1f169d8159ed36b194ae3d0aa0e7)。

E键（E Key）。

<a id="r_ga14280fdec597834c206d6ceed0db00fb"></a>

```c
#define INPUT_KEY_EJECTCD 161
```

相关声明：[INPUT_KEY_EJECTCD](#ga14280fdec597834c206d6ceed0db00fb)。

弹出光驱托盘键（Eject CD Key）。

<a id="r_gafbcaf9650bd513e187caf37186119924"></a>

```c
#define INPUT_KEY_EJECTCLOSECD 162
```

相关声明：[INPUT_KEY_EJECTCLOSECD](#gafbcaf9650bd513e187caf37186119924)。

弹出／关闭光驱托盘切换键（Eject/Close CD Toggle Key）。

<a id="r_gaff91435e45612b50955523d029dfd1e4"></a>

```c
#define INPUT_KEY_END 107
```

相关声明：[INPUT_KEY_END](#gaff91435e45612b50955523d029dfd1e4)。

行尾键（End Key）。

<a id="r_ga8e4e6c4072fd5595a80a4e4ff1ae1c32"></a>

```c
#define INPUT_KEY_ENTER 28
```

相关声明：[INPUT_KEY_ENTER](#ga8e4e6c4072fd5595a80a4e4ff1ae1c32)。

回车键（Enter Key）。

<a id="r_ga0775ec23155f396f368425fb4dc35e54"></a>

```c
#define INPUT_KEY_EQUAL 13
```

相关声明：[INPUT_KEY_EQUAL](#ga0775ec23155f396f368425fb4dc35e54)。

等号键（Equal Key）。

<a id="r_ga2026ab8608c7013781cdcf1e546e4d93"></a>

```c
#define INPUT_KEY_ESC 1
```

相关声明：[INPUT_KEY_ESC](#ga2026ab8608c7013781cdcf1e546e4d93)。

退出键（Escape Key）。

<a id="r_ga76aa5878ae736d2d9afea7b3f917eddb"></a>

```c
#define INPUT_KEY_EURO 0x1b3
```

相关声明：[INPUT_KEY_EURO](#ga76aa5878ae736d2d9afea7b3f917eddb)。

欧元符号键（Euro Key）。

<a id="r_gaed15f4e46a5e80bd9d8508f2f0317386"></a>

```c
#define INPUT_KEY_F 33
```

相关声明：[INPUT_KEY_F](#gaed15f4e46a5e80bd9d8508f2f0317386)。

F键（F Key）。

<a id="r_ga06374b0c4c42d708874d799afac87f54"></a>

```c
#define INPUT_KEY_F1 59
```

相关声明：[INPUT_KEY_F1](#ga06374b0c4c42d708874d799afac87f54)。

F1键（F1 Key）。

<a id="r_ga925bd568cbef2c8241a8bc38cd1fc0ee"></a>

```c
#define INPUT_KEY_F10 68
```

相关声明：[INPUT_KEY_F10](#ga925bd568cbef2c8241a8bc38cd1fc0ee)。

F10键（F10 Key）。

<a id="r_gaf8db5439ca4244843ddea6c78e235227"></a>

```c
#define INPUT_KEY_F11 87
```

相关声明：[INPUT_KEY_F11](#gaf8db5439ca4244843ddea6c78e235227)。

F11键（F11 Key）。

<a id="r_gac206e26c278998da99fc7907f2d68d90"></a>

```c
#define INPUT_KEY_F12 88
```

相关声明：[INPUT_KEY_F12](#gac206e26c278998da99fc7907f2d68d90)。

F12键（F12 Key）。

<a id="r_gafe37c9d54407b3401974a400831d9200"></a>

```c
#define INPUT_KEY_F13 183
```

相关声明：[INPUT_KEY_F13](#gafe37c9d54407b3401974a400831d9200)。

F13键（F13 Key）。

<a id="r_ga57112c273fb46a4f748047953355e430"></a>

```c
#define INPUT_KEY_F14 184
```

相关声明：[INPUT_KEY_F14](#ga57112c273fb46a4f748047953355e430)。

F14键（F14 Key）。

<a id="r_ga379756870b1a1d808f97f60cf2d3ecc5"></a>

```c
#define INPUT_KEY_F15 185
```

相关声明：[INPUT_KEY_F15](#ga379756870b1a1d808f97f60cf2d3ecc5)。

F15键（F15 Key）。

<a id="r_ga0336cf1cdcaa5ee62c1a4a7d7b5f94b0"></a>

```c
#define INPUT_KEY_F16 186
```

相关声明：[INPUT_KEY_F16](#ga0336cf1cdcaa5ee62c1a4a7d7b5f94b0)。

F16键（F16 Key）。

<a id="r_ga15ae8eaffd7978c3d91fe05bfedaec0d"></a>

```c
#define INPUT_KEY_F17 187
```

相关声明：[INPUT_KEY_F17](#ga15ae8eaffd7978c3d91fe05bfedaec0d)。

F17键（F17 Key）。

<a id="r_gaf58e8117aadc979c00e99e5d2944e572"></a>

```c
#define INPUT_KEY_F18 188
```

相关声明：[INPUT_KEY_F18](#gaf58e8117aadc979c00e99e5d2944e572)。

F18键（F18 Key）。

<a id="r_ga45127f8182970453761bea5703e164ca"></a>

```c
#define INPUT_KEY_F19 189
```

相关声明：[INPUT_KEY_F19](#ga45127f8182970453761bea5703e164ca)。

F19键（F19 Key）。

<a id="r_gae7ea4afc3ee03cba0820e1230a1bc844"></a>

```c
#define INPUT_KEY_F2 60
```

相关声明：[INPUT_KEY_F2](#gae7ea4afc3ee03cba0820e1230a1bc844)。

F2键（F2 Key）。

<a id="r_gaa0d8d5c8f17f26a6571bd50acd7e7c56"></a>

```c
#define INPUT_KEY_F20 190
```

相关声明：[INPUT_KEY_F20](#gaa0d8d5c8f17f26a6571bd50acd7e7c56)。

F20键（F20 Key）。

<a id="r_ga958fc836aa61bd04731563b97b3f2c3b"></a>

```c
#define INPUT_KEY_F21 191
```

相关声明：[INPUT_KEY_F21](#ga958fc836aa61bd04731563b97b3f2c3b)。

F21键（F21 Key）。

<a id="r_ga9f865f6f67f7ad3e747450cbe7bd001b"></a>

```c
#define INPUT_KEY_F22 192
```

相关声明：[INPUT_KEY_F22](#ga9f865f6f67f7ad3e747450cbe7bd001b)。

F22键（F22 Key）。

<a id="r_ga201402a9046f510fcc818fc281acdd74"></a>

```c
#define INPUT_KEY_F23 193
```

相关声明：[INPUT_KEY_F23](#ga201402a9046f510fcc818fc281acdd74)。

F23键（F23 Key）。

<a id="r_gade48ffdee4f9fc816467f61444e388d4"></a>

```c
#define INPUT_KEY_F24 194
```

相关声明：[INPUT_KEY_F24](#gade48ffdee4f9fc816467f61444e388d4)。

F24键（F24 Key）。

<a id="r_gaa186203f9efabb0868348938e5eabcfd"></a>

```c
#define INPUT_KEY_F3 61
```

相关声明：[INPUT_KEY_F3](#gaa186203f9efabb0868348938e5eabcfd)。

F3键（F3 Key）。

<a id="r_gace5db941d06022b3b33dd9e72a799b68"></a>

```c
#define INPUT_KEY_F4 62
```

相关声明：[INPUT_KEY_F4](#gace5db941d06022b3b33dd9e72a799b68)。

F4键（F4 Key）。

<a id="r_ga5ab64f326303e6b097eac8f9a1827feb"></a>

```c
#define INPUT_KEY_F5 63
```

相关声明：[INPUT_KEY_F5](#ga5ab64f326303e6b097eac8f9a1827feb)。

F5键（F5 Key）。

<a id="r_ga3f8d3788cd179ffb9d68de85e23ee1b0"></a>

```c
#define INPUT_KEY_F6 64
```

相关声明：[INPUT_KEY_F6](#ga3f8d3788cd179ffb9d68de85e23ee1b0)。

F6键（F6 Key）。

<a id="r_ga647c9e3d15d4866c3ae486b09f6182fa"></a>

```c
#define INPUT_KEY_F7 65
```

相关声明：[INPUT_KEY_F7](#ga647c9e3d15d4866c3ae486b09f6182fa)。

F7键（F7 Key）。

<a id="r_ga6a1be4c1720c9bbd18950ba7d9b91042"></a>

```c
#define INPUT_KEY_F8 66
```

相关声明：[INPUT_KEY_F8](#ga6a1be4c1720c9bbd18950ba7d9b91042)。

F8键（F8 Key）。

<a id="r_ga16baac9275d3b860e117705aba632681"></a>

```c
#define INPUT_KEY_F9 67
```

相关声明：[INPUT_KEY_F9](#ga16baac9275d3b860e117705aba632681)。

F9键（F9 Key）。

<a id="r_ga6c9a01c0a070b213af72cb8088e75876"></a>

```c
#define INPUT_KEY_FASTFORWARD 208
```

相关声明：[INPUT_KEY_FASTFORWARD](#ga6c9a01c0a070b213af72cb8088e75876)。

快进键（Fast Forward Key）。

<a id="r_ga72c6ae0ec2266f37256900458a031414"></a>

```c
#define INPUT_KEY_FAVORITES 364
```

相关声明：[INPUT_KEY_FAVORITES](#ga72c6ae0ec2266f37256900458a031414)。

收藏键（Favorites Key）。

<a id="r_gad64d70c2ccc65f5189666efa0847ca7a"></a>

```c
#define INPUT_KEY_FORWARD 159
```

相关声明：[INPUT_KEY_FORWARD](#gad64d70c2ccc65f5189666efa0847ca7a)。

前进键（Forward Key）。

<a id="r_ga5480ba49acaa553a194984a98b92f552"></a>

```c
#define INPUT_KEY_G 34
```

相关声明：[INPUT_KEY_G](#ga5480ba49acaa553a194984a98b92f552)。

G键（G Key）。

<a id="r_ga1aaa62276091bde62d4e5aa872902559"></a>

```c
#define INPUT_KEY_GRAVE 41
```

相关声明：[INPUT_KEY_GRAVE](#ga1aaa62276091bde62d4e5aa872902559)。

重音符／反引号键（Grave (backtick) Key）。

<a id="r_ga3014cf5abad3b71a0ae45b5b7c713f38"></a>

```c
#define INPUT_KEY_H 35
```

相关声明：[INPUT_KEY_H](#ga3014cf5abad3b71a0ae45b5b7c713f38)。

H键（H Key）。

<a id="r_gaa8314d1e4f4ca225922f039791b36d42"></a>

```c
#define INPUT_KEY_HOME 102
```

相关声明：[INPUT_KEY_HOME](#gaa8314d1e4f4ca225922f039791b36d42)。

行首键（Home Key）。

<a id="r_ga6c987aa5736663b7f309f2b2fb9423c5"></a>

```c
#define INPUT_KEY_I 23
```

相关声明：[INPUT_KEY_I](#ga6c987aa5736663b7f309f2b2fb9423c5)。

I键（I Key）。

<a id="r_gabfa379fe24dd23461e435de41c23864d"></a>

```c
#define INPUT_KEY_INSERT 110
```

相关声明：[INPUT_KEY_INSERT](#gabfa379fe24dd23461e435de41c23864d)。

插入键（Insert Key）。

<a id="r_ga7d5c3e334909eb4b2c76217b69a61260"></a>

```c
#define INPUT_KEY_J 36
```

相关声明：[INPUT_KEY_J](#ga7d5c3e334909eb4b2c76217b69a61260)。

J键（J Key）。

<a id="r_ga8cb73e35923639e77e861631565134df"></a>

```c
#define INPUT_KEY_K 37
```

相关声明：[INPUT_KEY_K](#ga8cb73e35923639e77e861631565134df)。

K键（K Key）。

<a id="r_ga8e5438fce6c7a717da4322de2982a2ed"></a>

```c
#define INPUT_KEY_KP0 82
```

相关声明：[INPUT_KEY_KP0](#ga8e5438fce6c7a717da4322de2982a2ed)。

数字小键盘0键（Keypad 0 Key）。

<a id="r_gaa5b65c8ff4b94208ff434f3ed8c9f1f1"></a>

```c
#define INPUT_KEY_KP1 79
```

相关声明：[INPUT_KEY_KP1](#gaa5b65c8ff4b94208ff434f3ed8c9f1f1)。

数字小键盘1键（Keypad 1 Key）。

<a id="r_gad50d9044613b97c6d6292afe15cceb06"></a>

```c
#define INPUT_KEY_KP2 80
```

相关声明：[INPUT_KEY_KP2](#gad50d9044613b97c6d6292afe15cceb06)。

数字小键盘2键（Keypad 2 Key）。

<a id="r_ga8a084e91c2906b1f8dd43939293d4812"></a>

```c
#define INPUT_KEY_KP3 81
```

相关声明：[INPUT_KEY_KP3](#ga8a084e91c2906b1f8dd43939293d4812)。

数字小键盘3键（Keypad 3 Key）。

<a id="r_ga1a9ca528816497bf32bee4e524d2977c"></a>

```c
#define INPUT_KEY_KP4 75
```

相关声明：[INPUT_KEY_KP4](#ga1a9ca528816497bf32bee4e524d2977c)。

数字小键盘4键（Keypad 4 Key）。

<a id="r_ga83e04456cf68db301973d09af1a19641"></a>

```c
#define INPUT_KEY_KP5 76
```

相关声明：[INPUT_KEY_KP5](#ga83e04456cf68db301973d09af1a19641)。

数字小键盘5键（Keypad 5 Key）。

<a id="r_gabd7a6dc0d9440de1ffef2a3643583966"></a>

```c
#define INPUT_KEY_KP6 77
```

相关声明：[INPUT_KEY_KP6](#gabd7a6dc0d9440de1ffef2a3643583966)。

数字小键盘6键（Keypad 6 Key）。

<a id="r_ga58709627a1190549d0e0004e4b5bcd74"></a>

```c
#define INPUT_KEY_KP7 71
```

相关声明：[INPUT_KEY_KP7](#ga58709627a1190549d0e0004e4b5bcd74)。

数字小键盘7键（Keypad 7 Key）。

<a id="r_ga94e64bbd09dda7434d8a9f086daca1a7"></a>

```c
#define INPUT_KEY_KP8 72
```

相关声明：[INPUT_KEY_KP8](#ga94e64bbd09dda7434d8a9f086daca1a7)。

数字小键盘8键（Keypad 8 Key）。

<a id="r_ga7dda283e4603e0ce4d14a9a87ea74c4f"></a>

```c
#define INPUT_KEY_KP9 73
```

相关声明：[INPUT_KEY_KP9](#ga7dda283e4603e0ce4d14a9a87ea74c4f)。

数字小键盘9键（Keypad 9 Key）。

<a id="r_gaa0c33b6ba975617f93230aa75a49fef5"></a>

```c
#define INPUT_KEY_KPASTERISK 55
```

相关声明：[INPUT_KEY_KPASTERISK](#gaa0c33b6ba975617f93230aa75a49fef5)。

数字小键盘星号键（Keypad Asterisk Key）。

<a id="r_gabb3767d06adbe20b3fb580e8816f916f"></a>

```c
#define INPUT_KEY_KPCOMMA 121
```

相关声明：[INPUT_KEY_KPCOMMA](#gabb3767d06adbe20b3fb580e8816f916f)。

数字小键盘逗号键（Keypad Comma Key）。

<a id="r_gac6c07467b6202089166c56c498fd4b27"></a>

```c
#define INPUT_KEY_KPDOT 83
```

相关声明：[INPUT_KEY_KPDOT](#gac6c07467b6202089166c56c498fd4b27)。

数字小键盘句点键（Keypad Dot Key）。

<a id="r_gae8fd841f81d29788d5d0b602538bbd0e"></a>

```c
#define INPUT_KEY_KPENTER 96
```

相关声明：[INPUT_KEY_KPENTER](#gae8fd841f81d29788d5d0b602538bbd0e)。

数字小键盘回车键（Keypad Enter Key）。

<a id="r_gaefdae376c1daf752b698efaf89a07b18"></a>

```c
#define INPUT_KEY_KPEQUAL 117
```

相关声明：[INPUT_KEY_KPEQUAL](#gaefdae376c1daf752b698efaf89a07b18)。

数字小键盘等号键（Keypad Equal Key）。

<a id="r_gad4f23f54ec4f2252864c507e09ad9cea"></a>

```c
#define INPUT_KEY_KPMINUS 74
```

相关声明：[INPUT_KEY_KPMINUS](#gad4f23f54ec4f2252864c507e09ad9cea)。

数字小键盘减号键（Keypad Minus Key）。

<a id="r_ga3d6307d0237d8f34a3d448dc9e40528f"></a>

```c
#define INPUT_KEY_KPPLUS 78
```

相关声明：[INPUT_KEY_KPPLUS](#ga3d6307d0237d8f34a3d448dc9e40528f)。

数字小键盘加号键（Keypad Plus Key）。

<a id="r_ga21a77384e45feb96ecc322032dc7231e"></a>

```c
#define INPUT_KEY_KPPLUSMINUS 118
```

相关声明：[INPUT_KEY_KPPLUSMINUS](#ga21a77384e45feb96ecc322032dc7231e)。

数字小键盘加号键（Keypad Plus Key）。

<a id="r_gab3f0ce8548cef85df2672d09d021fe39"></a>

```c
#define INPUT_KEY_KPSLASH 98
```

相关声明：[INPUT_KEY_KPSLASH](#gab3f0ce8548cef85df2672d09d021fe39)。

数字小键盘斜杠键（Keypad Slash Key）。

<a id="r_gad79329b4b6c3eaad43aabac8c3538622"></a>

```c
#define INPUT_KEY_L 38
```

相关声明：[INPUT_KEY_L](#gad79329b4b6c3eaad43aabac8c3538622)。

L键（L Key）。

<a id="r_gae8c0a4811cd2056d0b6885239d635492"></a>

```c
#define INPUT_KEY_LEFT 105
```

相关声明：[INPUT_KEY_LEFT](#gae8c0a4811cd2056d0b6885239d635492)。

向左键（Left Key）。

<a id="r_ga8d384257be19e2eb0d807d35f2656f16"></a>

```c
#define INPUT_KEY_LEFTALT 56
```

相关声明：[INPUT_KEY_LEFTALT](#ga8d384257be19e2eb0d807d35f2656f16)。

左 Alt键（Left Alt Key）。

<a id="r_gaecdffb7aff0fee1e078319a23a97e10e"></a>

```c
#define INPUT_KEY_LEFTBRACE 26
```

相关声明：[INPUT_KEY_LEFTBRACE](#gaecdffb7aff0fee1e078319a23a97e10e)。

左括号键（Left Brace Key）。

<a id="r_ga1bc52bc876c50da66cc292f250603db7"></a>

```c
#define INPUT_KEY_LEFTCTRL 29
```

相关声明：[INPUT_KEY_LEFTCTRL](#ga1bc52bc876c50da66cc292f250603db7)。

左 Ctrl键（Left Ctrl Key）。

<a id="r_gad18b505a7f718887f932a5b7fedfecd3"></a>

```c
#define INPUT_KEY_LEFTMETA 125
```

相关声明：[INPUT_KEY_LEFTMETA](#gad18b505a7f718887f932a5b7fedfecd3)。

左 Meta键（Left Meta Key）。

<a id="r_gacaf73383130558303396a7add94bdafd"></a>

```c
#define INPUT_KEY_LEFTSHIFT 42
```

相关声明：[INPUT_KEY_LEFTSHIFT](#gacaf73383130558303396a7add94bdafd)。

左 Shift键（Left Shift Key）。

<a id="r_ga7c8f628eb719d1d4b428805914c376a7"></a>

```c
#define INPUT_KEY_M 50
```

相关声明：[INPUT_KEY_M](#ga7c8f628eb719d1d4b428805914c376a7)。

M键（M Key）。

<a id="r_gab159cae18818e930e4d928ebcc206651"></a>

```c
#define INPUT_KEY_MENU 139
```

相关声明：[INPUT_KEY_MENU](#gab159cae18818e930e4d928ebcc206651)。

菜单键（Menu Key）。

<a id="r_gae9779c5f21b9e14e5cbe1db8c5073819"></a>

```c
#define INPUT_KEY_MINUS 12
```

相关声明：[INPUT_KEY_MINUS](#gae9779c5f21b9e14e5cbe1db8c5073819)。

减号键（Minus Key）。

<a id="r_ga8554adab31fc9c20c9de01bcb2aff839"></a>

```c
#define INPUT_KEY_MUTE 113
```

相关声明：[INPUT_KEY_MUTE](#ga8554adab31fc9c20c9de01bcb2aff839)。

静音键（Mute Key）。

<a id="r_ga09c0c860ee76803bb317dbac1072cd1d"></a>

```c
#define INPUT_KEY_N 49
```

相关声明：[INPUT_KEY_N](#ga09c0c860ee76803bb317dbac1072cd1d)。

N键（N Key）。

<a id="r_ga456a105c367fa61a1c041c6b9fd7a6fe"></a>

```c
#define INPUT_KEY_NEXTSONG 163
```

相关声明：[INPUT_KEY_NEXTSONG](#ga456a105c367fa61a1c041c6b9fd7a6fe)。

下一曲键（Next Song Key）。

<a id="r_ga93e220e43b3d33ffa985445f6dbf9c3c"></a>

```c
#define INPUT_KEY_NUMLOCK 69
```

相关声明：[INPUT_KEY_NUMLOCK](#ga93e220e43b3d33ffa985445f6dbf9c3c)。

数字锁定键（Num Lock Key）。

<a id="r_gae964cb377e0bcd958dad6da9626d298c"></a>

```c
#define INPUT_KEY_O 24
```

相关声明：[INPUT_KEY_O](#gae964cb377e0bcd958dad6da9626d298c)。

O键（O Key）。

<a id="r_ga396def37642dee65c74c48ff72aaa53d"></a>

```c
#define INPUT_KEY_P 25
```

相关声明：[INPUT_KEY_P](#ga396def37642dee65c74c48ff72aaa53d)。

P键（P Key）。

<a id="r_gaf6bc999ac2a136235fe95803c6df73c1"></a>

```c
#define INPUT_KEY_PAGEDOWN 109
```

相关声明：[INPUT_KEY_PAGEDOWN](#gaf6bc999ac2a136235fe95803c6df73c1)。

向下翻页键（Page Down Key）。

<a id="r_gaebb169acd4c3ce873353fd595364b374"></a>

```c
#define INPUT_KEY_PAGEUP 104
```

相关声明：[INPUT_KEY_PAGEUP](#gaebb169acd4c3ce873353fd595364b374)。

向上翻页键（Page UpKey）。

<a id="r_ga08319efd258cd774ff8bc964c5a402dd"></a>

```c
#define INPUT_KEY_PAUSE 119
```

相关声明：[INPUT_KEY_PAUSE](#ga08319efd258cd774ff8bc964c5a402dd)。

暂停键（Pause Key）。

<a id="r_ga1a377fdb1967aeff84e96d47c71bcf41"></a>

```c
#define INPUT_KEY_PLAY 207
```

相关声明：[INPUT_KEY_PLAY](#ga1a377fdb1967aeff84e96d47c71bcf41)。

播放键（Play Key）。

<a id="r_ga210c431786b1a1b9af29b4a9516ca063"></a>

```c
#define INPUT_KEY_PLAYPAUSE 164
```

相关声明：[INPUT_KEY_PLAYPAUSE](#ga210c431786b1a1b9af29b4a9516ca063)。

播放／暂停切换键（Play/Pause Toggle Key）。

<a id="r_ga2b05b5429ef1b0dc37698b82201d257d"></a>

```c
#define INPUT_KEY_POWER 116
```

相关声明：[INPUT_KEY_POWER](#ga2b05b5429ef1b0dc37698b82201d257d)。

电源键（Power Key）。

<a id="r_ga71b9c93b94d21c672bff26f9f1c6a7d4"></a>

```c
#define INPUT_KEY_PREVIOUSSONG 165
```

相关声明：[INPUT_KEY_PREVIOUSSONG](#ga71b9c93b94d21c672bff26f9f1c6a7d4)。

上一曲键（Previous Song Key）。

<a id="r_ga4927612cf9f69324b15d8d9e46ab3326"></a>

```c
#define INPUT_KEY_PRINT 210
```

相关声明：[INPUT_KEY_PRINT](#ga4927612cf9f69324b15d8d9e46ab3326)。

打印键（Print Key）。

<a id="r_ga9ee8d6012d74e489ee8072f71497a36e"></a>

```c
#define INPUT_KEY_Q 16
```

相关声明：[INPUT_KEY_Q](#ga9ee8d6012d74e489ee8072f71497a36e)。

Q键（Q Key）。

<a id="r_ga421f14c501d86ed907ed4249f93a9e7e"></a>

```c
#define INPUT_KEY_R 19
```

相关声明：[INPUT_KEY_R](#ga421f14c501d86ed907ed4249f93a9e7e)。

R键（R Key）。

<a id="r_ga26409cb68bb098c1a18181cd737c82d6"></a>

```c
#define INPUT_KEY_RECORD 167
```

相关声明：[INPUT_KEY_RECORD](#ga26409cb68bb098c1a18181cd737c82d6)。

录制键（Record Key）。

<a id="r_gaeaf9b701a99b0d9d0210a472312d294d"></a>

```c
#define INPUT_KEY_REWIND 168
```

相关声明：[INPUT_KEY_REWIND](#gaeaf9b701a99b0d9d0210a472312d294d)。

快退键（Rewind Key）。

<a id="r_ga1bf6f292c1ab3ca25001b4ef4ca2626b"></a>

```c
#define INPUT_KEY_RIGHT 106
```

相关声明：[INPUT_KEY_RIGHT](#ga1bf6f292c1ab3ca25001b4ef4ca2626b)。

向右键（Right Key）。

<a id="r_gac02b6a2133d5ddf8847e1ce94250536f"></a>

```c
#define INPUT_KEY_RIGHTALT 100
```

相关声明：[INPUT_KEY_RIGHTALT](#gac02b6a2133d5ddf8847e1ce94250536f)。

右 Alt键（Right Alt Key）。

<a id="r_gaa0802d3471f6c774d37a8827e632d7fb"></a>

```c
#define INPUT_KEY_RIGHTBRACE 27
```

相关声明：[INPUT_KEY_RIGHTBRACE](#gaa0802d3471f6c774d37a8827e632d7fb)。

右括号键（Right Brace Key）。

<a id="r_gabb2e15ee9c30a649c92e82c42f513a35"></a>

```c
#define INPUT_KEY_RIGHTCTRL 97
```

相关声明：[INPUT_KEY_RIGHTCTRL](#gabb2e15ee9c30a649c92e82c42f513a35)。

右 Ctrl键（Right Ctrl Key）。

<a id="r_ga23ebc28da84872b585c9dcfeb057bfc9"></a>

```c
#define INPUT_KEY_RIGHTMETA 126
```

相关声明：[INPUT_KEY_RIGHTMETA](#ga23ebc28da84872b585c9dcfeb057bfc9)。

右 Meta键（Right Meta Key）。

<a id="r_ga4fce26a4ffc693507043c1cfe95d279d"></a>

```c
#define INPUT_KEY_RIGHTSHIFT 54
```

相关声明：[INPUT_KEY_RIGHTSHIFT](#ga4fce26a4ffc693507043c1cfe95d279d)。

右 Shift键（Right Shift Key）。

<a id="r_gadefb5566a41148a0df4dd95cb2c5e2d2"></a>

```c
#define INPUT_KEY_S 31
```

相关声明：[INPUT_KEY_S](#gadefb5566a41148a0df4dd95cb2c5e2d2)。

S键（S Key）。

<a id="r_ga32491acdefb2e9f0eab5e7fc5755d2bc"></a>

```c
#define INPUT_KEY_SCALE 120
```

相关声明：[INPUT_KEY_SCALE](#ga32491acdefb2e9f0eab5e7fc5755d2bc)。

缩放键（Scale Key）。

<a id="r_ga1d0958d93ddb7f3ff662e84a06c95a7c"></a>

```c
#define INPUT_KEY_SCROLLLOCK 70
```

相关声明：[INPUT_KEY_SCROLLLOCK](#ga1d0958d93ddb7f3ff662e84a06c95a7c)。

滚动锁定键（Scroll Lock Key）。

<a id="r_ga7d45c7e2399dc6b20b6e470cb35d1dd6"></a>

```c
#define INPUT_KEY_SEMICOLON 39
```

相关声明：[INPUT_KEY_SEMICOLON](#ga7d45c7e2399dc6b20b6e470cb35d1dd6)。

分号键（Semicolon Key）。

<a id="r_gab17a459ab34d1353809c1a7360db3818"></a>

```c
#define INPUT_KEY_SLASH 53
```

相关声明：[INPUT_KEY_SLASH](#gab17a459ab34d1353809c1a7360db3818)。

斜杠键（Slash Key）。

<a id="r_gaf826720ad8af092655351c0527b849df"></a>

```c
#define INPUT_KEY_SLEEP 142
```

相关声明：[INPUT_KEY_SLEEP](#gaf826720ad8af092655351c0527b849df)。

系统睡眠键（System Sleep Key）。

<a id="r_ga4d6d5af48ea84fbea0df2fcb38ac7812"></a>

```c
#define INPUT_KEY_SPACE 57
```

相关声明：[INPUT_KEY_SPACE](#ga4d6d5af48ea84fbea0df2fcb38ac7812)。

空格键（Space Key）。

<a id="r_ga99f104293221f3a3e5ff054fa259658f"></a>

```c
#define INPUT_KEY_STOPCD 166
```

相关声明：[INPUT_KEY_STOPCD](#ga99f104293221f3a3e5ff054fa259658f)。

停止光盘播放键（Stop CD Key）。

<a id="r_ga41b7f92a09624c06eee3a3650ac36139"></a>

```c
#define INPUT_KEY_SYSRQ 99
```

相关声明：[INPUT_KEY_SYSRQ](#ga41b7f92a09624c06eee3a3650ac36139)。

系统请求键（SysReq Key）。

<a id="r_gadc43d9d7846b0e87dc217dcab831e4fe"></a>

```c
#define INPUT_KEY_T 20
```

相关声明：[INPUT_KEY_T](#gadc43d9d7846b0e87dc217dcab831e4fe)。

T键（T Key）。

<a id="r_gac38db99311ad987f019f16e601a6911d"></a>

```c
#define INPUT_KEY_TAB 15
```

相关声明：[INPUT_KEY_TAB](#gac38db99311ad987f019f16e601a6911d)。

制表键（Tab Key）。

<a id="r_gab6403be2f0b9b60f626a57e5c9ed2666"></a>

```c
#define INPUT_KEY_U 22
```

相关声明：[INPUT_KEY_U](#gab6403be2f0b9b60f626a57e5c9ed2666)。

U键（U Key）。

<a id="r_ga01e7f6a6aee5972612536c70a84db848"></a>

```c
#define INPUT_KEY_UP 103
```

相关声明：[INPUT_KEY_UP](#ga01e7f6a6aee5972612536c70a84db848)。

向上键（Up Key）。

<a id="r_ga74c693d33698eac543ee6ad4943c2d81"></a>

```c
#define INPUT_KEY_UWB 239
```

相关声明：[INPUT_KEY_UWB](#ga74c693d33698eac543ee6ad4943c2d81)。

超宽带键（Ultra-Wideband Key）。

<a id="r_ga9f37deb8d631a8705cc0506d9b46b42c"></a>

```c
#define INPUT_KEY_V 47
```

相关声明：[INPUT_KEY_V](#ga9f37deb8d631a8705cc0506d9b46b42c)。

V键（V Key）。

<a id="r_ga36b4c1340f9d7c5374e4fbe82244d492"></a>

```c
#define INPUT_KEY_VOLUMEDOWN 114
```

相关声明：[INPUT_KEY_VOLUMEDOWN](#ga36b4c1340f9d7c5374e4fbe82244d492)。

降低音量键（Volume Down Key）。

<a id="r_gaa876076df525fa996dbced370c1be2e3"></a>

```c
#define INPUT_KEY_VOLUMEUP 115
```

相关声明：[INPUT_KEY_VOLUMEUP](#gaa876076df525fa996dbced370c1be2e3)。

提高音量键（Volume Up Key）。

<a id="r_gaafc7f5b6c9d8f7ef13527ce60c08d36d"></a>

```c
#define INPUT_KEY_W 17
```

相关声明：[INPUT_KEY_W](#gaafc7f5b6c9d8f7ef13527ce60c08d36d)。

W键（W Key）。

<a id="r_gaeba4b122e3850b8c96e803353ac7bd35"></a>

```c
#define INPUT_KEY_WAKEUP 143
```

相关声明：[INPUT_KEY_WAKEUP](#gaeba4b122e3850b8c96e803353ac7bd35)。

唤醒系统键（System Wake Up Key）。

<a id="r_gae008f06aa7ca74912fe8ebbcd3dda45f"></a>

```c
#define INPUT_KEY_WLAN 238
```

相关声明：[INPUT_KEY_WLAN](#gae008f06aa7ca74912fe8ebbcd3dda45f)。

无线局域网键（Wireless LAN Key）。

<a id="r_ga8665fe56c47f02bd98793674dbc145b9"></a>

```c
#define INPUT_KEY_X 45
```

相关声明：[INPUT_KEY_X](#ga8665fe56c47f02bd98793674dbc145b9)。

X键（X Key）。

<a id="r_gae86058bcd4e4a5393b35253176dc498f"></a>

```c
#define INPUT_KEY_Y 21
```

相关声明：[INPUT_KEY_Y](#gae86058bcd4e4a5393b35253176dc498f)。

Y键（Y Key）。

<a id="r_ga32a1603a3c0127e6ebe059af32314273"></a>

```c
#define INPUT_KEY_Z 44
```

相关声明：[INPUT_KEY_Z](#ga32a1603a3c0127e6ebe059af32314273)。

Z键（Z Key）。

## 4.3\_输入事件的按钮编码（Input event BTN codes.）



<a id="r_ga30976f1bb4418fccbae30a56f714bea1"></a>

```c
#define INPUT_BTN_0 0x100
```

相关声明：[INPUT_BTN_0](#ga30976f1bb4418fccbae30a56f714bea1)。

0按钮（0 button）。

<a id="r_ga1f76026fc79560722aaf95aee0985705"></a>

```c
#define INPUT_BTN_1 0x101
```

相关声明：[INPUT_BTN_1](#ga1f76026fc79560722aaf95aee0985705)。

1按钮（1 button）。

<a id="r_ga73129f8a7a6216f629f3d3b3433c4430"></a>

```c
#define INPUT_BTN_2 0x102
```

相关声明：[INPUT_BTN_2](#ga73129f8a7a6216f629f3d3b3433c4430)。

2按钮（2 button）。

<a id="r_gae8651f9708cb6def0e64094542018b6e"></a>

```c
#define INPUT_BTN_3 0x103
```

相关声明：[INPUT_BTN_3](#gae8651f9708cb6def0e64094542018b6e)。

3按钮（3 button）。

<a id="r_ga11b176175bd1ff1d062d2dfc111c80f3"></a>

```c
#define INPUT_BTN_4 0x104
```

相关声明：[INPUT_BTN_4](#ga11b176175bd1ff1d062d2dfc111c80f3)。

4按钮（4 button）。

<a id="r_ga9ea411071196ca3e90df6bbfbb48cf57"></a>

```c
#define INPUT_BTN_5 0x105
```

相关声明：[INPUT_BTN_5](#ga9ea411071196ca3e90df6bbfbb48cf57)。

5按钮（5 button）。

<a id="r_ga66d852c7078d65fcb2e34cee8a5fcd61"></a>

```c
#define INPUT_BTN_6 0x106
```

相关声明：[INPUT_BTN_6](#ga66d852c7078d65fcb2e34cee8a5fcd61)。

6按钮（6 button）。

<a id="r_ga55330f8419dacc72404607f4abd2ac3e"></a>

```c
#define INPUT_BTN_7 0x107
```

相关声明：[INPUT_BTN_7](#ga55330f8419dacc72404607f4abd2ac3e)。

7按钮（7 button）。

<a id="r_gab92962cc2fd0784c1afbf0ed036a92a4"></a>

```c
#define INPUT_BTN_8 0x108
```

相关声明：[INPUT_BTN_8](#gab92962cc2fd0784c1afbf0ed036a92a4)。

8按钮（8 button）。

<a id="r_ga790321e6da41ee0dfe7550b03166f514"></a>

```c
#define INPUT_BTN_9 0x109
```

相关声明：[INPUT_BTN_9](#ga790321e6da41ee0dfe7550b03166f514)。

9按钮（9 button）。

<a id="r_ga1e7a8c57c7a0a33cd3311ee141a0836c"></a>

```c
#define INPUT_BTN_A INPUT_BTN_SOUTH
```

相关声明：[INPUT_BTN_A](#ga1e7a8c57c7a0a33cd3311ee141a0836c)、[INPUT_BTN_SOUTH](#ga5bbd97c212dbd08288cbdf1dc1a64cb5)。

A按钮（A button）。

<a id="r_gae4355ae2a831823486b28388a78dd964"></a>

```c
#define INPUT_BTN_B INPUT_BTN_EAST
```

相关声明：[INPUT_BTN_B](#gae4355ae2a831823486b28388a78dd964)、[INPUT_BTN_EAST](#gae57dc96a45c1a29169a6df702bb70cb7)。

B按钮（B button）。

<a id="r_ga1aae01791507acfc119387d7600e8e6a"></a>

```c
#define INPUT_BTN_BACK 0x116
```

相关声明：[INPUT_BTN_BACK](#ga1aae01791507acfc119387d7600e8e6a)。

后退按钮（Back button）。

<a id="r_ga0e20c12420205d110a4e20c3a798cd8f"></a>

```c
#define INPUT_BTN_C 0x132
```

相关声明：[INPUT_BTN_C](#ga0e20c12420205d110a4e20c3a798cd8f)。

C按钮（C button）。

<a id="r_ga912a826581f671fbc3f04b9bb2582432"></a>

```c
#define INPUT_BTN_DPAD_DOWN 0x221
```

相关声明：[INPUT_BTN_DPAD_DOWN](#ga912a826581f671fbc3f04b9bb2582432)。

方向键向下（Directional pad Down）。

<a id="r_ga7360624be8436db1e33ecc62e4e74b14"></a>

```c
#define INPUT_BTN_DPAD_LEFT 0x222
```

相关声明：[INPUT_BTN_DPAD_LEFT](#ga7360624be8436db1e33ecc62e4e74b14)。

方向键向左（Directional pad Left）。

<a id="r_gabcf0e865e8c374ec77ef8bd3abf23117"></a>

```c
#define INPUT_BTN_DPAD_RIGHT 0x223
```

相关声明：[INPUT_BTN_DPAD_RIGHT](#gabcf0e865e8c374ec77ef8bd3abf23117)。

方向键向右（Directional pad Right）。

<a id="r_ga3b2879d72a2e4a4292442cee04f6a5c6"></a>

```c
#define INPUT_BTN_DPAD_UP 0x220
```

相关声明：[INPUT_BTN_DPAD_UP](#ga3b2879d72a2e4a4292442cee04f6a5c6)。

方向键向上（Directional pad Up）。

<a id="r_gae57dc96a45c1a29169a6df702bb70cb7"></a>

```c
#define INPUT_BTN_EAST 0x131
```

相关声明：[INPUT_BTN_EAST](#gae57dc96a45c1a29169a6df702bb70cb7)。

东侧按钮（East button）。

<a id="r_ga296364e72a76c9d03729b35ff64a3ea3"></a>

```c
#define INPUT_BTN_EXTRA 0x114
```

相关声明：[INPUT_BTN_EXTRA](#ga296364e72a76c9d03729b35ff64a3ea3)。

附加按钮（Extra button）。

<a id="r_ga1483e1ef939172b42b98be83961d3668"></a>

```c
#define INPUT_BTN_FORWARD 0x115
```

相关声明：[INPUT_BTN_FORWARD](#ga1483e1ef939172b42b98be83961d3668)。

前进按钮（Forward button）。

<a id="r_gac1810029daec295ab8df9c2463c3b12d"></a>

```c
#define INPUT_BTN_GEAR_DOWN 0x150
```

相关声明：[INPUT_BTN_GEAR_DOWN](#gac1810029daec295ab8df9c2463c3b12d)。

降挡按钮（Gear Down button）。

<a id="r_ga5f84880e2febbd344348a235cba670d1"></a>

```c
#define INPUT_BTN_GEAR_UP 0x151
```

相关声明：[INPUT_BTN_GEAR_UP](#ga5f84880e2febbd344348a235cba670d1)。

升挡按钮（Gear Up button）。

<a id="r_ga391066a02e4297af7c214031037aeb3e"></a>

```c
#define INPUT_BTN_LEFT 0x110
```

相关声明：[INPUT_BTN_LEFT](#ga391066a02e4297af7c214031037aeb3e)。

左按钮（Left button）。

<a id="r_ga86b7c6fbd3e37e21bd6b0fb379c89b44"></a>

```c
#define INPUT_BTN_MIDDLE 0x112
```

相关声明：[INPUT_BTN_MIDDLE](#ga86b7c6fbd3e37e21bd6b0fb379c89b44)。

中间按钮（Middle button）。

<a id="r_ga0b1db382e01c7d8f88dd531625f4b759"></a>

```c
#define INPUT_BTN_MODE 0x13c
```

相关声明：[INPUT_BTN_MODE](#ga0b1db382e01c7d8f88dd531625f4b759)。

模式按钮（Mode button）。

<a id="r_gab1378ad64c11487f0f607d039db61d82"></a>

```c
#define INPUT_BTN_NORTH 0x133
```

相关声明：[INPUT_BTN_NORTH](#gab1378ad64c11487f0f607d039db61d82)。

北侧按钮（North button）。

<a id="r_ga300d9d3924d22f27180272908f6ad8db"></a>

```c
#define INPUT_BTN_RIGHT 0x111
```

相关声明：[INPUT_BTN_RIGHT](#ga300d9d3924d22f27180272908f6ad8db)。

右按钮（Right button）。

<a id="r_gaad0c944797cd368eca5f6753326fe28a"></a>

```c
#define INPUT_BTN_SELECT 0x13a
```

相关声明：[INPUT_BTN_SELECT](#gaad0c944797cd368eca5f6753326fe28a)。

选择按钮（Select button）。

<a id="r_gaf34f37dd3c5ef85af7805c1a307bdcc4"></a>

```c
#define INPUT_BTN_SIDE 0x113
```

相关声明：[INPUT_BTN_SIDE](#gaf34f37dd3c5ef85af7805c1a307bdcc4)。

侧面按钮（Side button）。

<a id="r_ga5bbd97c212dbd08288cbdf1dc1a64cb5"></a>

```c
#define INPUT_BTN_SOUTH 0x130
```

相关声明：[INPUT_BTN_SOUTH](#ga5bbd97c212dbd08288cbdf1dc1a64cb5)。

南侧按钮（South button）。

<a id="r_ga874350c63269e66869d3424d108bf891"></a>

```c
#define INPUT_BTN_START 0x13b
```

相关声明：[INPUT_BTN_START](#ga874350c63269e66869d3424d108bf891)。

开始按钮（Start button）。

<a id="r_ga14273a631fbaec99bf96c7929034cb2d"></a>

```c
#define INPUT_BTN_TASK 0x117
```

相关声明：[INPUT_BTN_TASK](#ga14273a631fbaec99bf96c7929034cb2d)。

任务按钮（Task button）。

<a id="r_ga5809e3b7e5f922904b5177f551880ceb"></a>

```c
#define INPUT_BTN_THUMBL 0x13d
```

相关声明：[INPUT_BTN_THUMBL](#ga5809e3b7e5f922904b5177f551880ceb)。

左摇杆按钮（Left thumbstick button）。

<a id="r_ga83061a701ecd88a543a1ff9850cfd070"></a>

```c
#define INPUT_BTN_THUMBR 0x13e
```

相关声明：[INPUT_BTN_THUMBR](#ga83061a701ecd88a543a1ff9850cfd070)。

右摇杆按钮（Right thumbstick button）。

<a id="r_ga3c5f6d03b079c2771d5b5a0dbed75cad"></a>

```c
#define INPUT_BTN_TL 0x136
```

相关声明：[INPUT_BTN_TL](#ga3c5f6d03b079c2771d5b5a0dbed75cad)。

左扳机 L1（Left trigger (L1)）。

<a id="r_ga59b1954abc7d0f4d05e025a570439155"></a>

```c
#define INPUT_BTN_TL2 0x138
```

相关声明：[INPUT_BTN_TL2](#ga59b1954abc7d0f4d05e025a570439155)。

左扳机 2，即 L2（Left trigger 2 (L2)）。

<a id="r_ga80661f579f180f02e05fa3c1175728c4"></a>

```c
#define INPUT_BTN_TOUCH 0x14a
```

相关声明：[INPUT_BTN_TOUCH](#ga80661f579f180f02e05fa3c1175728c4)。

触摸屏触摸（Touchscreen touch）。

<a id="r_gacc3e39f0e70af828684efe126931b5ff"></a>

```c
#define INPUT_BTN_TR 0x137
```

相关声明：[INPUT_BTN_TR](#gacc3e39f0e70af828684efe126931b5ff)。

右扳机 R1（Right trigger (R1)）。

<a id="r_ga7401c1c0ec2b6d20ab4ca0bfa87b06bd"></a>

```c
#define INPUT_BTN_TR2 0x139
```

相关声明：[INPUT_BTN_TR2](#ga7401c1c0ec2b6d20ab4ca0bfa87b06bd)。

右扳机 2，即 R2（Right trigger 2 (R2)）。

<a id="r_ga0913edaa3f7176c942c6708090719d48"></a>

```c
#define INPUT_BTN_WEST 0x134
```

相关声明：[INPUT_BTN_WEST](#ga0913edaa3f7176c942c6708090719d48)。

西侧按钮（West button）。

<a id="r_gad205e660b5cc9e148db7b0acd22c4560"></a>

```c
#define INPUT_BTN_X INPUT_BTN_NORTH
```

相关声明：[INPUT_BTN_X](#gad205e660b5cc9e148db7b0acd22c4560)、[INPUT_BTN_NORTH](#gab1378ad64c11487f0f607d039db61d82)。

X按钮（X button）。

<a id="r_ga4a11b785ae5dab8922f481217e01fd08"></a>

```c
#define INPUT_BTN_Y INPUT_BTN_WEST
```

相关声明：[INPUT_BTN_Y](#ga4a11b785ae5dab8922f481217e01fd08)、[INPUT_BTN_WEST](#ga0913edaa3f7176c942c6708090719d48)。

Y按钮（Y button）。

<a id="r_ga09f473104f9c92f40e2f481b1e02a28f"></a>

```c
#define INPUT_BTN_Z 0x135
```

相关声明：[INPUT_BTN_Z](#ga09f473104f9c92f40e2f481b1e02a28f)。

Z按钮（Z button）。

## 4.4\_输入事件的绝对轴编码（Input event ABS codes.）



<a id="r_ga79930c9f3260ca7ae2026e85280b9808"></a>

```c
#define INPUT_ABS_BRAKE 0x0a
```

相关声明：[INPUT_ABS_BRAKE](#ga79930c9f3260ca7ae2026e85280b9808)。

刹车绝对位置（Absolute brake position）。

<a id="r_ga77831126c364a12132db3e51af8002e3"></a>

```c
#define INPUT_ABS_GAS 0x09
```

相关声明：[INPUT_ABS_GAS](#ga77831126c364a12132db3e51af8002e3)。

油门踏板绝对位置（Absolute gas position）。

<a id="r_ga7dbd7e0140f5d13c7b92243568dba95b"></a>

```c
#define INPUT_ABS_MT_SLOT 0x2f
```

相关声明：[INPUT_ABS_MT_SLOT](#ga7dbd7e0140f5d13c7b92243568dba95b)。

绝对坐标多点触控槽标识符（Absolute multitouch slot identifier）。

<a id="r_ga5c9daa51741ad28757bfb4e7538bf2c7"></a>

```c
#define INPUT_ABS_RUDDER 0x07
```

相关声明：[INPUT_ABS_RUDDER](#ga5c9daa51741ad28757bfb4e7538bf2c7)。

方向舵绝对位置（Absolute rudder position）。

<a id="r_ga2564b261dc72e0d48776bfd80282baf4"></a>

```c
#define INPUT_ABS_RX 0x03
```

相关声明：[INPUT_ABS_RX](#ga2564b261dc72e0d48776bfd80282baf4)。

绕 X 轴的绝对旋转量（Absolute rotation around X axis）。

<a id="r_ga69109075f91f270b43de41f7e558f894"></a>

```c
#define INPUT_ABS_RY 0x04
```

相关声明：[INPUT_ABS_RY](#ga69109075f91f270b43de41f7e558f894)。

绕 Y 轴的绝对旋转量（Absolute rotation around Y axis）。

<a id="r_gad4f9589ef67776adc52a2cee72bb1634"></a>

```c
#define INPUT_ABS_RZ 0x05
```

相关声明：[INPUT_ABS_RZ](#gad4f9589ef67776adc52a2cee72bb1634)。

绕 Z 轴的绝对旋转量（Absolute rotation around Z axis）。

<a id="r_ga44d3e48d42006c73e011d9ee8d5656c3"></a>

```c
#define INPUT_ABS_THROTTLE 0x06
```

相关声明：[INPUT_ABS_THROTTLE](#ga44d3e48d42006c73e011d9ee8d5656c3)。

节流阀绝对位置（Absolute throttle position）。

<a id="r_ga5fde78f9e113ac35ebb4f1735a08d3e3"></a>

```c
#define INPUT_ABS_WHEEL 0x08
```

相关声明：[INPUT_ABS_WHEEL](#ga5fde78f9e113ac35ebb4f1735a08d3e3)。

方向盘绝对位置（Absolute wheel position）。

<a id="r_ga6bb2cf3decdbbeac354f66db7239f8c1"></a>

```c
#define INPUT_ABS_X 0x00
```

相关声明：[INPUT_ABS_X](#ga6bb2cf3decdbbeac354f66db7239f8c1)。

绝对 X 坐标（Absolute X coordinate）。

<a id="r_gad2f731397644733e4b3d9f8f96d4f87a"></a>

```c
#define INPUT_ABS_Y 0x01
```

相关声明：[INPUT_ABS_Y](#gad2f731397644733e4b3d9f8f96d4f87a)。

绝对 Y 坐标（Absolute Y coordinate）。

<a id="r_gae007afd99bf586fdc4c6b1a5ae1a3859"></a>

```c
#define INPUT_ABS_Z 0x02
```

相关声明：[INPUT_ABS_Z](#gae007afd99bf586fdc4c6b1a5ae1a3859)。

绝对 Z 坐标（Absolute Z coordinate）。

## 4.5\_输入事件的相对轴编码（Input event REL codes.）



<a id="r_gab8aeb81a612ec63d687cbe1d9becb823"></a>

```c
#define INPUT_REL_DIAL 0x07
```

相关声明：[INPUT_REL_DIAL](#gab8aeb81a612ec63d687cbe1d9becb823)。

拨盘相对坐标（Relative dial coordinate）。

<a id="r_ga5b9989321b8e8f883bd338c1a37d50c2"></a>

```c
#define INPUT_REL_HWHEEL 0x06
```

相关声明：[INPUT_REL_HWHEEL](#ga5b9989321b8e8f883bd338c1a37d50c2)。

水平滚轮相对坐标（Relative horizontal wheel coordinate）。

<a id="r_gaf2a08d3d5a0aa60b8f56ff7e2110a54e"></a>

```c
#define INPUT_REL_MISC 0x09
```

相关声明：[INPUT_REL_MISC](#gaf2a08d3d5a0aa60b8f56ff7e2110a54e)。

其他相对坐标（Relative misc coordinate）。

<a id="r_ga5727f75f795b31982dc8681a0eed3378"></a>

```c
#define INPUT_REL_RX 0x03
```

相关声明：[INPUT_REL_RX](#ga5727f75f795b31982dc8681a0eed3378)。

绕 X 轴的相对旋转量（Relative rotation around X axis）。

<a id="r_ga85cde1de349dffef0c7dd5757e94cb4a"></a>

```c
#define INPUT_REL_RY 0x04
```

相关声明：[INPUT_REL_RY](#ga85cde1de349dffef0c7dd5757e94cb4a)。

绕 Y 轴的相对旋转量（Relative rotation around Y axis）。

<a id="r_ga1f1ed1ce01e943906e5cecf071c0bf96"></a>

```c
#define INPUT_REL_RZ 0x05
```

相关声明：[INPUT_REL_RZ](#ga1f1ed1ce01e943906e5cecf071c0bf96)。

绕 Z 轴的相对旋转量（Relative rotation around Z axis）。

<a id="r_ga3884c7bbfb3b23e9cbc054f327b4344c"></a>

```c
#define INPUT_REL_WHEEL 0x08
```

相关声明：[INPUT_REL_WHEEL](#ga3884c7bbfb3b23e9cbc054f327b4344c)。

滚轮相对坐标（Relative wheel coordinate）。

<a id="r_ga6afab29530dfffbb81b191b90548ffd2"></a>

```c
#define INPUT_REL_X 0x00
```

相关声明：[INPUT_REL_X](#ga6afab29530dfffbb81b191b90548ffd2)。

相对 X 坐标（Relative X coordinate）。

<a id="r_ga5fbdf5c33ac1e5330c3f30b37ee8f51d"></a>

```c
#define INPUT_REL_Y 0x01
```

相关声明：[INPUT_REL_Y](#ga5fbdf5c33ac1e5330c3f30b37ee8f51d)。

相对 Y 坐标（Relative Y coordinate）。

<a id="r_gae5626b188d77b39a79df4bb7790cd316"></a>

```c
#define INPUT_REL_Z 0x02
```

相关声明：[INPUT_REL_Z](#gae5626b188d77b39a79df4bb7790cd316)。

相对 Z 坐标（Relative Z coordinate）。

## 4.6\_输入事件的其他类型编码（Input event MSC codes.）



<a id="r_ga62a5a51f0beb512236dfa276211e1f43"></a>

```c
#define INPUT_MSC_SCAN 0x04
```

相关声明：[INPUT_MSC_SCAN](#ga62a5a51f0beb512236dfa276211e1f43)。

扫描码（Scan code）。

## 4.7\_详细说明（Detailed Documentation）

<a id="ga79930c9f3260ca7ae2026e85280b9808"></a>

### `INPUT_ABS_BRAKE`

```c
#define INPUT_ABS_BRAKE 0x0a
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

刹车绝对位置（Absolute brake position）。

<a id="ga77831126c364a12132db3e51af8002e3"></a>

### `INPUT_ABS_GAS`

```c
#define INPUT_ABS_GAS 0x09
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

油门踏板绝对位置（Absolute gas position）。

<a id="ga7dbd7e0140f5d13c7b92243568dba95b"></a>

### `INPUT_ABS_MT_SLOT`

```c
#define INPUT_ABS_MT_SLOT 0x2f
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

绝对坐标多点触控槽标识符（Absolute multitouch slot identifier）。

<a id="ga5c9daa51741ad28757bfb4e7538bf2c7"></a>

### `INPUT_ABS_RUDDER`

```c
#define INPUT_ABS_RUDDER 0x07
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

方向舵绝对位置（Absolute rudder position）。

<a id="ga2564b261dc72e0d48776bfd80282baf4"></a>

### `INPUT_ABS_RX`

```c
#define INPUT_ABS_RX 0x03
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

绕 X 轴的绝对旋转量（Absolute rotation around X axis）。

<a id="ga69109075f91f270b43de41f7e558f894"></a>

### `INPUT_ABS_RY`

```c
#define INPUT_ABS_RY 0x04
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

绕 Y 轴的绝对旋转量（Absolute rotation around Y axis）。

<a id="gad4f9589ef67776adc52a2cee72bb1634"></a>

### `INPUT_ABS_RZ`

```c
#define INPUT_ABS_RZ 0x05
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

绕 Z 轴的绝对旋转量（Absolute rotation around Z axis）。

<a id="ga44d3e48d42006c73e011d9ee8d5656c3"></a>

### `INPUT_ABS_THROTTLE`

```c
#define INPUT_ABS_THROTTLE 0x06
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

节流阀绝对位置（Absolute throttle position）。

<a id="ga5fde78f9e113ac35ebb4f1735a08d3e3"></a>

### `INPUT_ABS_WHEEL`

```c
#define INPUT_ABS_WHEEL 0x08
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

方向盘绝对位置（Absolute wheel position）。

<a id="ga6bb2cf3decdbbeac354f66db7239f8c1"></a>

### `INPUT_ABS_X`

```c
#define INPUT_ABS_X 0x00
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

绝对 X 坐标（Absolute X coordinate）。

<a id="gad2f731397644733e4b3d9f8f96d4f87a"></a>

### `INPUT_ABS_Y`

```c
#define INPUT_ABS_Y 0x01
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

绝对 Y 坐标（Absolute Y coordinate）。

<a id="gae007afd99bf586fdc4c6b1a5ae1a3859"></a>

### `INPUT_ABS_Z`

```c
#define INPUT_ABS_Z 0x02
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

绝对 Z 坐标（Absolute Z coordinate）。

<a id="ga30976f1bb4418fccbae30a56f714bea1"></a>

### `INPUT_BTN_0`

```c
#define INPUT_BTN_0 0x100
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

0按钮（0 button）。

<a id="ga1f76026fc79560722aaf95aee0985705"></a>

### `INPUT_BTN_1`

```c
#define INPUT_BTN_1 0x101
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

1按钮（1 button）。

<a id="ga73129f8a7a6216f629f3d3b3433c4430"></a>

### `INPUT_BTN_2`

```c
#define INPUT_BTN_2 0x102
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

2按钮（2 button）。

<a id="gae8651f9708cb6def0e64094542018b6e"></a>

### `INPUT_BTN_3`

```c
#define INPUT_BTN_3 0x103
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

3按钮（3 button）。

<a id="ga11b176175bd1ff1d062d2dfc111c80f3"></a>

### `INPUT_BTN_4`

```c
#define INPUT_BTN_4 0x104
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

4按钮（4 button）。

<a id="ga9ea411071196ca3e90df6bbfbb48cf57"></a>

### `INPUT_BTN_5`

```c
#define INPUT_BTN_5 0x105
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

5按钮（5 button）。

<a id="ga66d852c7078d65fcb2e34cee8a5fcd61"></a>

### `INPUT_BTN_6`

```c
#define INPUT_BTN_6 0x106
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

6按钮（6 button）。

<a id="ga55330f8419dacc72404607f4abd2ac3e"></a>

### `INPUT_BTN_7`

```c
#define INPUT_BTN_7 0x107
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

7按钮（7 button）。

<a id="gab92962cc2fd0784c1afbf0ed036a92a4"></a>

### `INPUT_BTN_8`

```c
#define INPUT_BTN_8 0x108
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

8按钮（8 button）。

<a id="ga790321e6da41ee0dfe7550b03166f514"></a>

### `INPUT_BTN_9`

```c
#define INPUT_BTN_9 0x109
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

9按钮（9 button）。

<a id="ga1e7a8c57c7a0a33cd3311ee141a0836c"></a>

### `INPUT_BTN_A`

```c
#define INPUT_BTN_A INPUT_BTN_SOUTH
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

A按钮（A button）。

<a id="gae4355ae2a831823486b28388a78dd964"></a>

### `INPUT_BTN_B`

```c
#define INPUT_BTN_B INPUT_BTN_EAST
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

B按钮（B button）。

<a id="ga1aae01791507acfc119387d7600e8e6a"></a>

### `INPUT_BTN_BACK`

```c
#define INPUT_BTN_BACK 0x116
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

后退按钮（Back button）。

<a id="ga0e20c12420205d110a4e20c3a798cd8f"></a>

### `INPUT_BTN_C`

```c
#define INPUT_BTN_C 0x132
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

C按钮（C button）。

<a id="ga912a826581f671fbc3f04b9bb2582432"></a>

### `INPUT_BTN_DPAD_DOWN`

```c
#define INPUT_BTN_DPAD_DOWN 0x221
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

方向键向下（Directional pad Down）。

<a id="ga7360624be8436db1e33ecc62e4e74b14"></a>

### `INPUT_BTN_DPAD_LEFT`

```c
#define INPUT_BTN_DPAD_LEFT 0x222
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

方向键向左（Directional pad Left）。

<a id="gabcf0e865e8c374ec77ef8bd3abf23117"></a>

### `INPUT_BTN_DPAD_RIGHT`

```c
#define INPUT_BTN_DPAD_RIGHT 0x223
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

方向键向右（Directional pad Right）。

<a id="ga3b2879d72a2e4a4292442cee04f6a5c6"></a>

### `INPUT_BTN_DPAD_UP`

```c
#define INPUT_BTN_DPAD_UP 0x220
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

方向键向上（Directional pad Up）。

<a id="gae57dc96a45c1a29169a6df702bb70cb7"></a>

### `INPUT_BTN_EAST`

```c
#define INPUT_BTN_EAST 0x131
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

东侧按钮（East button）。

<a id="ga296364e72a76c9d03729b35ff64a3ea3"></a>

### `INPUT_BTN_EXTRA`

```c
#define INPUT_BTN_EXTRA 0x114
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

附加按钮（Extra button）。

<a id="ga1483e1ef939172b42b98be83961d3668"></a>

### `INPUT_BTN_FORWARD`

```c
#define INPUT_BTN_FORWARD 0x115
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

前进按钮（Forward button）。

<a id="gac1810029daec295ab8df9c2463c3b12d"></a>

### `INPUT_BTN_GEAR_DOWN`

```c
#define INPUT_BTN_GEAR_DOWN 0x150
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

降挡按钮（Gear Down button）。

<a id="ga5f84880e2febbd344348a235cba670d1"></a>

### `INPUT_BTN_GEAR_UP`

```c
#define INPUT_BTN_GEAR_UP 0x151
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

升挡按钮（Gear Up button）。

<a id="ga391066a02e4297af7c214031037aeb3e"></a>

### `INPUT_BTN_LEFT`

```c
#define INPUT_BTN_LEFT 0x110
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

左按钮（Left button）。

<a id="ga86b7c6fbd3e37e21bd6b0fb379c89b44"></a>

### `INPUT_BTN_MIDDLE`

```c
#define INPUT_BTN_MIDDLE 0x112
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

中间按钮（Middle button）。

<a id="ga0b1db382e01c7d8f88dd531625f4b759"></a>

### `INPUT_BTN_MODE`

```c
#define INPUT_BTN_MODE 0x13c
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

模式按钮（Mode button）。

<a id="gab1378ad64c11487f0f607d039db61d82"></a>

### `INPUT_BTN_NORTH`

```c
#define INPUT_BTN_NORTH 0x133
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

北侧按钮（North button）。

<a id="ga300d9d3924d22f27180272908f6ad8db"></a>

### `INPUT_BTN_RIGHT`

```c
#define INPUT_BTN_RIGHT 0x111
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

右按钮（Right button）。

<a id="gaad0c944797cd368eca5f6753326fe28a"></a>

### `INPUT_BTN_SELECT`

```c
#define INPUT_BTN_SELECT 0x13a
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

选择按钮（Select button）。

<a id="gaf34f37dd3c5ef85af7805c1a307bdcc4"></a>

### `INPUT_BTN_SIDE`

```c
#define INPUT_BTN_SIDE 0x113
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

侧面按钮（Side button）。

<a id="ga5bbd97c212dbd08288cbdf1dc1a64cb5"></a>

### `INPUT_BTN_SOUTH`

```c
#define INPUT_BTN_SOUTH 0x130
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

南侧按钮（South button）。

<a id="ga874350c63269e66869d3424d108bf891"></a>

### `INPUT_BTN_START`

```c
#define INPUT_BTN_START 0x13b
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

开始按钮（Start button）。

<a id="ga14273a631fbaec99bf96c7929034cb2d"></a>

### `INPUT_BTN_TASK`

```c
#define INPUT_BTN_TASK 0x117
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

任务按钮（Task button）。

<a id="ga5809e3b7e5f922904b5177f551880ceb"></a>

### `INPUT_BTN_THUMBL`

```c
#define INPUT_BTN_THUMBL 0x13d
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

左摇杆按钮（Left thumbstick button）。

<a id="ga83061a701ecd88a543a1ff9850cfd070"></a>

### `INPUT_BTN_THUMBR`

```c
#define INPUT_BTN_THUMBR 0x13e
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

右摇杆按钮（Right thumbstick button）。

<a id="ga3c5f6d03b079c2771d5b5a0dbed75cad"></a>

### `INPUT_BTN_TL`

```c
#define INPUT_BTN_TL 0x136
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

左扳机 L1（Left trigger (L1)）。

<a id="ga59b1954abc7d0f4d05e025a570439155"></a>

### `INPUT_BTN_TL2`

```c
#define INPUT_BTN_TL2 0x138
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

左扳机 2，即 L2（Left trigger 2 (L2)）。

<a id="ga80661f579f180f02e05fa3c1175728c4"></a>

### `INPUT_BTN_TOUCH`

```c
#define INPUT_BTN_TOUCH 0x14a
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

触摸屏触摸（Touchscreen touch）。

<a id="gacc3e39f0e70af828684efe126931b5ff"></a>

### `INPUT_BTN_TR`

```c
#define INPUT_BTN_TR 0x137
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

右扳机 R1（Right trigger (R1)）。

<a id="ga7401c1c0ec2b6d20ab4ca0bfa87b06bd"></a>

### `INPUT_BTN_TR2`

```c
#define INPUT_BTN_TR2 0x139
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

右扳机 2，即 R2（Right trigger 2 (R2)）。

<a id="ga0913edaa3f7176c942c6708090719d48"></a>

### `INPUT_BTN_WEST`

```c
#define INPUT_BTN_WEST 0x134
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

西侧按钮（West button）。

<a id="gad205e660b5cc9e148db7b0acd22c4560"></a>

### `INPUT_BTN_X`

```c
#define INPUT_BTN_X INPUT_BTN_NORTH
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

X按钮（X button）。

<a id="ga4a11b785ae5dab8922f481217e01fd08"></a>

### `INPUT_BTN_Y`

```c
#define INPUT_BTN_Y INPUT_BTN_WEST
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

Y按钮（Y button）。

<a id="ga09f473104f9c92f40e2f481b1e02a28f"></a>

### `INPUT_BTN_Z`

```c
#define INPUT_BTN_Z 0x135
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

Z按钮（Z button）。

<a id="gaa6bcd6755fbdb3eb103f03a72759ce4f"></a>

### `INPUT_EV_ABS`

```c
#define INPUT_EV_ABS 0x03
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

绝对坐标事件（Absolute coordinate event）。

<a id="ga3ebe8a83ea38c4c87cda6bc9e18f2e61"></a>

### `INPUT_EV_DEVICE`

```c
#define INPUT_EV_DEVICE 0xef
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

设备专用输入事件（Device specific input event）。

<a id="ga4a517c31bdbdd1bd82ba456d256ef1f1"></a>

### `INPUT_EV_KEY`

```c
#define INPUT_EV_KEY 0x01
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

按键事件（Key event）。

<a id="ga40ab1faa2e28e32c30016ad854afa6cf"></a>

### `INPUT_EV_MSC`

```c
#define INPUT_EV_MSC 0x04
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

其他事件（Miscellaneous event）。

<a id="ga02de6c85efab3d21eb81e88e54d58e03"></a>

### `INPUT_EV_REL`

```c
#define INPUT_EV_REL 0x02
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

相对坐标事件（Relative coordinate event）。

<a id="ga7037a9ea2e0a63c40a5d206e507e5f42"></a>

### `INPUT_EV_VENDOR_START`

```c
#define INPUT_EV_VENDOR_START 0xf0
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

厂商专用事件范围起点（Vendor specific event start）。

<a id="gaa19a341e18ff5c43e1b8ddf58c7b9676"></a>

### `INPUT_EV_VENDOR_STOP`

```c
#define INPUT_EV_VENDOR_STOP 0xff
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

厂商专用事件范围终点（Vendor specific event stop）。

<a id="gab41cb2f1768b0a0667ab6509b6d3af21"></a>

### `INPUT_KEY_0`

```c
#define INPUT_KEY_0 11
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

0键（0 Key）。

<a id="gad62520853a15b74d68c1bab5a3119eaa"></a>

### `INPUT_KEY_1`

```c
#define INPUT_KEY_1 2
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

1键（1 Key）。

<a id="gadb02e289d07d4d4457c88b1ada7e2534"></a>

### `INPUT_KEY_2`

```c
#define INPUT_KEY_2 3
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

2键（2 Key）。

<a id="ga95a246cefcaafd26d15c1c124bdf2ca4"></a>

### `INPUT_KEY_3`

```c
#define INPUT_KEY_3 4
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

3键（3 Key）。

<a id="ga0c16c2e62a65eab0fe8952a4cf60254d"></a>

### `INPUT_KEY_4`

```c
#define INPUT_KEY_4 5
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

4键（4 Key）。

<a id="ga386e2c69d5e5a9549668b1a2a2d297e1"></a>

### `INPUT_KEY_5`

```c
#define INPUT_KEY_5 6
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

5键（5 Key）。

<a id="ga87e0cea90040710253718ce29c407f3e"></a>

### `INPUT_KEY_6`

```c
#define INPUT_KEY_6 7
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

6键（6 Key）。

<a id="ga090686eaaacddb8c2f58b31b4b9801b8"></a>

### `INPUT_KEY_7`

```c
#define INPUT_KEY_7 8
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

7键（7 Key）。

<a id="ga6f2b66c0eea17b044778a326ffcd3f57"></a>

### `INPUT_KEY_8`

```c
#define INPUT_KEY_8 9
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

8键（8 Key）。

<a id="ga91473de481c47f3f9e40caf42e49250f"></a>

### `INPUT_KEY_9`

```c
#define INPUT_KEY_9 10
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

9键（9 Key）。

<a id="ga553b457efaafb3cdc41e7b1e953cd6fe"></a>

### `INPUT_KEY_A`

```c
#define INPUT_KEY_A 30
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

A键（A Key）。

<a id="gaa528a10eb85fa9dc46198e08962fab3a"></a>

### `INPUT_KEY_APOSTROPHE`

```c
#define INPUT_KEY_APOSTROPHE 40
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

单引号键（Apostrophe Key）。

<a id="gaaae2c60e8907c14c094e5c1c4e3dae3b"></a>

### `INPUT_KEY_B`

```c
#define INPUT_KEY_B 48
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

B键（B Key）。

<a id="gab5ad87c6e97f6b09f9dc1a1570a9c299"></a>

### `INPUT_KEY_BACK`

```c
#define INPUT_KEY_BACK 158
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

后退键（Back Key）。

<a id="ga180fcae595fbc580bfe1a94414a4b02b"></a>

### `INPUT_KEY_BACKSLASH`

```c
#define INPUT_KEY_BACKSLASH 43
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

反斜杠键（Backslash Key）。

<a id="ga654ffbdc8f2fef696ee0237704cebc34"></a>

### `INPUT_KEY_BACKSPACE`

```c
#define INPUT_KEY_BACKSPACE 14
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

退格键（Backspace Key）。

<a id="ga26f6330d7631bdae0f2bb34f623a85ae"></a>

### `INPUT_KEY_BLUETOOTH`

```c
#define INPUT_KEY_BLUETOOTH 237
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

蓝牙键（Bluetooth Key）。

<a id="gac4afc3e97b18a1f22e3d59730177e27f"></a>

### `INPUT_KEY_BRIGHTNESSDOWN`

```c
#define INPUT_KEY_BRIGHTNESSDOWN 224
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

降低亮度键（Brightness Down Key）。

<a id="gaff59e776a3e3a0fe4d32caeb41a32c53"></a>

### `INPUT_KEY_BRIGHTNESSUP`

```c
#define INPUT_KEY_BRIGHTNESSUP 225
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

提高亮度键（Brightness Up Key）。

<a id="ga1b88afc2eacfbbd778785398baebd287"></a>

### `INPUT_KEY_C`

```c
#define INPUT_KEY_C 46
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

C键（C Key）。

<a id="ga8dfa14142766962272afc77538f8a909"></a>

### `INPUT_KEY_CAPSLOCK`

```c
#define INPUT_KEY_CAPSLOCK 58
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

大写锁定键（Caps Lock Key）。

<a id="gaee0312912b4c067c60d77b26e56cd905"></a>

### `INPUT_KEY_CLOSECD`

```c
#define INPUT_KEY_CLOSECD 160
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

关闭光驱托盘键（Close CD Key）。

<a id="ga345dc788101108c27f488cfa0fc885c8"></a>

### `INPUT_KEY_COFFEE`

```c
#define INPUT_KEY_COFFEE 152
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

屏幕保护键（Screen Saver Key）。

<a id="ga1220a9e90676992fcd3c308a7f1038f7"></a>

### `INPUT_KEY_COMMA`

```c
#define INPUT_KEY_COMMA 51
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

逗号键（Comma Key）。

<a id="ga52882fff91dc0c288cf0b60baa60be65"></a>

### `INPUT_KEY_COMPOSE`

```c
#define INPUT_KEY_COMPOSE 127
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

组合字符键（Compose Key）。

<a id="gaedf1f55d35163e56ca03f4409ea6b7d0"></a>

### `INPUT_KEY_CONNECT`

```c
#define INPUT_KEY_CONNECT 218
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

连接键（Connect Key）。

<a id="ga206eda236c1ce08e3ad6eef192ac303e"></a>

### `INPUT_KEY_D`

```c
#define INPUT_KEY_D 32
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

D键（D Key）。

<a id="ga2abef21124d504927c675959331a4c3b"></a>

### `INPUT_KEY_DELETE`

```c
#define INPUT_KEY_DELETE 111
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

删除键（Delete Key）。

<a id="gacd0cb4c35c9463bf61dcb247fc4bd546"></a>

### `INPUT_KEY_DOLLAR`

```c
#define INPUT_KEY_DOLLAR 0x1b2
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

美元符号键（Dollar Key）。

<a id="gacbd30145c479c472d105a0c5251c0e4d"></a>

### `INPUT_KEY_DOT`

```c
#define INPUT_KEY_DOT 52
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

句点键（Dot Key）。

<a id="gad80b82e35e50f775a091b8f5031d2c9b"></a>

### `INPUT_KEY_DOWN`

```c
#define INPUT_KEY_DOWN 108
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

向下键（Down Key）。

<a id="ga4c1a1f169d8159ed36b194ae3d0aa0e7"></a>

### `INPUT_KEY_E`

```c
#define INPUT_KEY_E 18
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

E键（E Key）。

<a id="ga14280fdec597834c206d6ceed0db00fb"></a>

### `INPUT_KEY_EJECTCD`

```c
#define INPUT_KEY_EJECTCD 161
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

弹出光驱托盘键（Eject CD Key）。

<a id="gafbcaf9650bd513e187caf37186119924"></a>

### `INPUT_KEY_EJECTCLOSECD`

```c
#define INPUT_KEY_EJECTCLOSECD 162
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

弹出／关闭光驱托盘切换键（Eject/Close CD Toggle Key）。

<a id="gaff91435e45612b50955523d029dfd1e4"></a>

### `INPUT_KEY_END`

```c
#define INPUT_KEY_END 107
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

行尾键（End Key）。

<a id="ga8e4e6c4072fd5595a80a4e4ff1ae1c32"></a>

### `INPUT_KEY_ENTER`

```c
#define INPUT_KEY_ENTER 28
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

回车键（Enter Key）。

<a id="ga0775ec23155f396f368425fb4dc35e54"></a>

### `INPUT_KEY_EQUAL`

```c
#define INPUT_KEY_EQUAL 13
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

等号键（Equal Key）。

<a id="ga2026ab8608c7013781cdcf1e546e4d93"></a>

### `INPUT_KEY_ESC`

```c
#define INPUT_KEY_ESC 1
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

退出键（Escape Key）。

<a id="ga76aa5878ae736d2d9afea7b3f917eddb"></a>

### `INPUT_KEY_EURO`

```c
#define INPUT_KEY_EURO 0x1b3
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

欧元符号键（Euro Key）。

<a id="gaed15f4e46a5e80bd9d8508f2f0317386"></a>

### `INPUT_KEY_F`

```c
#define INPUT_KEY_F 33
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F键（F Key）。

<a id="ga06374b0c4c42d708874d799afac87f54"></a>

### `INPUT_KEY_F1`

```c
#define INPUT_KEY_F1 59
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F1键（F1 Key）。

<a id="ga925bd568cbef2c8241a8bc38cd1fc0ee"></a>

### `INPUT_KEY_F10`

```c
#define INPUT_KEY_F10 68
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F10键（F10 Key）。

<a id="gaf8db5439ca4244843ddea6c78e235227"></a>

### `INPUT_KEY_F11`

```c
#define INPUT_KEY_F11 87
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F11键（F11 Key）。

<a id="gac206e26c278998da99fc7907f2d68d90"></a>

### `INPUT_KEY_F12`

```c
#define INPUT_KEY_F12 88
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F12键（F12 Key）。

<a id="gafe37c9d54407b3401974a400831d9200"></a>

### `INPUT_KEY_F13`

```c
#define INPUT_KEY_F13 183
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F13键（F13 Key）。

<a id="ga57112c273fb46a4f748047953355e430"></a>

### `INPUT_KEY_F14`

```c
#define INPUT_KEY_F14 184
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F14键（F14 Key）。

<a id="ga379756870b1a1d808f97f60cf2d3ecc5"></a>

### `INPUT_KEY_F15`

```c
#define INPUT_KEY_F15 185
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F15键（F15 Key）。

<a id="ga0336cf1cdcaa5ee62c1a4a7d7b5f94b0"></a>

### `INPUT_KEY_F16`

```c
#define INPUT_KEY_F16 186
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F16键（F16 Key）。

<a id="ga15ae8eaffd7978c3d91fe05bfedaec0d"></a>

### `INPUT_KEY_F17`

```c
#define INPUT_KEY_F17 187
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F17键（F17 Key）。

<a id="gaf58e8117aadc979c00e99e5d2944e572"></a>

### `INPUT_KEY_F18`

```c
#define INPUT_KEY_F18 188
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F18键（F18 Key）。

<a id="ga45127f8182970453761bea5703e164ca"></a>

### `INPUT_KEY_F19`

```c
#define INPUT_KEY_F19 189
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F19键（F19 Key）。

<a id="gae7ea4afc3ee03cba0820e1230a1bc844"></a>

### `INPUT_KEY_F2`

```c
#define INPUT_KEY_F2 60
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F2键（F2 Key）。

<a id="gaa0d8d5c8f17f26a6571bd50acd7e7c56"></a>

### `INPUT_KEY_F20`

```c
#define INPUT_KEY_F20 190
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F20键（F20 Key）。

<a id="ga958fc836aa61bd04731563b97b3f2c3b"></a>

### `INPUT_KEY_F21`

```c
#define INPUT_KEY_F21 191
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F21键（F21 Key）。

<a id="ga9f865f6f67f7ad3e747450cbe7bd001b"></a>

### `INPUT_KEY_F22`

```c
#define INPUT_KEY_F22 192
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F22键（F22 Key）。

<a id="ga201402a9046f510fcc818fc281acdd74"></a>

### `INPUT_KEY_F23`

```c
#define INPUT_KEY_F23 193
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F23键（F23 Key）。

<a id="gade48ffdee4f9fc816467f61444e388d4"></a>

### `INPUT_KEY_F24`

```c
#define INPUT_KEY_F24 194
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F24键（F24 Key）。

<a id="gaa186203f9efabb0868348938e5eabcfd"></a>

### `INPUT_KEY_F3`

```c
#define INPUT_KEY_F3 61
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F3键（F3 Key）。

<a id="gace5db941d06022b3b33dd9e72a799b68"></a>

### `INPUT_KEY_F4`

```c
#define INPUT_KEY_F4 62
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F4键（F4 Key）。

<a id="ga5ab64f326303e6b097eac8f9a1827feb"></a>

### `INPUT_KEY_F5`

```c
#define INPUT_KEY_F5 63
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F5键（F5 Key）。

<a id="ga3f8d3788cd179ffb9d68de85e23ee1b0"></a>

### `INPUT_KEY_F6`

```c
#define INPUT_KEY_F6 64
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F6键（F6 Key）。

<a id="ga647c9e3d15d4866c3ae486b09f6182fa"></a>

### `INPUT_KEY_F7`

```c
#define INPUT_KEY_F7 65
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F7键（F7 Key）。

<a id="ga6a1be4c1720c9bbd18950ba7d9b91042"></a>

### `INPUT_KEY_F8`

```c
#define INPUT_KEY_F8 66
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F8键（F8 Key）。

<a id="ga16baac9275d3b860e117705aba632681"></a>

### `INPUT_KEY_F9`

```c
#define INPUT_KEY_F9 67
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

F9键（F9 Key）。

<a id="ga6c9a01c0a070b213af72cb8088e75876"></a>

### `INPUT_KEY_FASTFORWARD`

```c
#define INPUT_KEY_FASTFORWARD 208
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

快进键（Fast Forward Key）。

<a id="ga72c6ae0ec2266f37256900458a031414"></a>

### `INPUT_KEY_FAVORITES`

```c
#define INPUT_KEY_FAVORITES 364
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

收藏键（Favorites Key）。

<a id="gad64d70c2ccc65f5189666efa0847ca7a"></a>

### `INPUT_KEY_FORWARD`

```c
#define INPUT_KEY_FORWARD 159
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

前进键（Forward Key）。

<a id="ga5480ba49acaa553a194984a98b92f552"></a>

### `INPUT_KEY_G`

```c
#define INPUT_KEY_G 34
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

G键（G Key）。

<a id="ga1aaa62276091bde62d4e5aa872902559"></a>

### `INPUT_KEY_GRAVE`

```c
#define INPUT_KEY_GRAVE 41
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

重音符／反引号键（Grave (backtick) Key）。

<a id="ga3014cf5abad3b71a0ae45b5b7c713f38"></a>

### `INPUT_KEY_H`

```c
#define INPUT_KEY_H 35
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

H键（H Key）。

<a id="gaa8314d1e4f4ca225922f039791b36d42"></a>

### `INPUT_KEY_HOME`

```c
#define INPUT_KEY_HOME 102
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

行首键（Home Key）。

<a id="ga6c987aa5736663b7f309f2b2fb9423c5"></a>

### `INPUT_KEY_I`

```c
#define INPUT_KEY_I 23
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

I键（I Key）。

<a id="gabfa379fe24dd23461e435de41c23864d"></a>

### `INPUT_KEY_INSERT`

```c
#define INPUT_KEY_INSERT 110
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

插入键（Insert Key）。

<a id="ga7d5c3e334909eb4b2c76217b69a61260"></a>

### `INPUT_KEY_J`

```c
#define INPUT_KEY_J 36
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

J键（J Key）。

<a id="ga8cb73e35923639e77e861631565134df"></a>

### `INPUT_KEY_K`

```c
#define INPUT_KEY_K 37
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

K键（K Key）。

<a id="ga8e5438fce6c7a717da4322de2982a2ed"></a>

### `INPUT_KEY_KP0`

```c
#define INPUT_KEY_KP0 82
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘0键（Keypad 0 Key）。

<a id="gaa5b65c8ff4b94208ff434f3ed8c9f1f1"></a>

### `INPUT_KEY_KP1`

```c
#define INPUT_KEY_KP1 79
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘1键（Keypad 1 Key）。

<a id="gad50d9044613b97c6d6292afe15cceb06"></a>

### `INPUT_KEY_KP2`

```c
#define INPUT_KEY_KP2 80
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘2键（Keypad 2 Key）。

<a id="ga8a084e91c2906b1f8dd43939293d4812"></a>

### `INPUT_KEY_KP3`

```c
#define INPUT_KEY_KP3 81
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘3键（Keypad 3 Key）。

<a id="ga1a9ca528816497bf32bee4e524d2977c"></a>

### `INPUT_KEY_KP4`

```c
#define INPUT_KEY_KP4 75
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘4键（Keypad 4 Key）。

<a id="ga83e04456cf68db301973d09af1a19641"></a>

### `INPUT_KEY_KP5`

```c
#define INPUT_KEY_KP5 76
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘5键（Keypad 5 Key）。

<a id="gabd7a6dc0d9440de1ffef2a3643583966"></a>

### `INPUT_KEY_KP6`

```c
#define INPUT_KEY_KP6 77
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘6键（Keypad 6 Key）。

<a id="ga58709627a1190549d0e0004e4b5bcd74"></a>

### `INPUT_KEY_KP7`

```c
#define INPUT_KEY_KP7 71
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘7键（Keypad 7 Key）。

<a id="ga94e64bbd09dda7434d8a9f086daca1a7"></a>

### `INPUT_KEY_KP8`

```c
#define INPUT_KEY_KP8 72
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘8键（Keypad 8 Key）。

<a id="ga7dda283e4603e0ce4d14a9a87ea74c4f"></a>

### `INPUT_KEY_KP9`

```c
#define INPUT_KEY_KP9 73
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘9键（Keypad 9 Key）。

<a id="gaa0c33b6ba975617f93230aa75a49fef5"></a>

### `INPUT_KEY_KPASTERISK`

```c
#define INPUT_KEY_KPASTERISK 55
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘星号键（Keypad Asterisk Key）。

<a id="gabb3767d06adbe20b3fb580e8816f916f"></a>

### `INPUT_KEY_KPCOMMA`

```c
#define INPUT_KEY_KPCOMMA 121
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘逗号键（Keypad Comma Key）。

<a id="gac6c07467b6202089166c56c498fd4b27"></a>

### `INPUT_KEY_KPDOT`

```c
#define INPUT_KEY_KPDOT 83
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘句点键（Keypad Dot Key）。

<a id="gae8fd841f81d29788d5d0b602538bbd0e"></a>

### `INPUT_KEY_KPENTER`

```c
#define INPUT_KEY_KPENTER 96
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘回车键（Keypad Enter Key）。

<a id="gaefdae376c1daf752b698efaf89a07b18"></a>

### `INPUT_KEY_KPEQUAL`

```c
#define INPUT_KEY_KPEQUAL 117
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘等号键（Keypad Equal Key）。

<a id="gad4f23f54ec4f2252864c507e09ad9cea"></a>

### `INPUT_KEY_KPMINUS`

```c
#define INPUT_KEY_KPMINUS 74
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘减号键（Keypad Minus Key）。

<a id="ga3d6307d0237d8f34a3d448dc9e40528f"></a>

### `INPUT_KEY_KPPLUS`

```c
#define INPUT_KEY_KPPLUS 78
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘加号键（Keypad Plus Key）。

<a id="ga21a77384e45feb96ecc322032dc7231e"></a>

### `INPUT_KEY_KPPLUSMINUS`

```c
#define INPUT_KEY_KPPLUSMINUS 118
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘加号键（Keypad Plus Key）。

<a id="gab3f0ce8548cef85df2672d09d021fe39"></a>

### `INPUT_KEY_KPSLASH`

```c
#define INPUT_KEY_KPSLASH 98
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字小键盘斜杠键（Keypad Slash Key）。

<a id="gad79329b4b6c3eaad43aabac8c3538622"></a>

### `INPUT_KEY_L`

```c
#define INPUT_KEY_L 38
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

L键（L Key）。

<a id="gae8c0a4811cd2056d0b6885239d635492"></a>

### `INPUT_KEY_LEFT`

```c
#define INPUT_KEY_LEFT 105
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

向左键（Left Key）。

<a id="ga8d384257be19e2eb0d807d35f2656f16"></a>

### `INPUT_KEY_LEFTALT`

```c
#define INPUT_KEY_LEFTALT 56
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

左 Alt键（Left Alt Key）。

<a id="gaecdffb7aff0fee1e078319a23a97e10e"></a>

### `INPUT_KEY_LEFTBRACE`

```c
#define INPUT_KEY_LEFTBRACE 26
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

左括号键（Left Brace Key）。

<a id="ga1bc52bc876c50da66cc292f250603db7"></a>

### `INPUT_KEY_LEFTCTRL`

```c
#define INPUT_KEY_LEFTCTRL 29
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

左 Ctrl键（Left Ctrl Key）。

<a id="gad18b505a7f718887f932a5b7fedfecd3"></a>

### `INPUT_KEY_LEFTMETA`

```c
#define INPUT_KEY_LEFTMETA 125
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

左 Meta键（Left Meta Key）。

<a id="gacaf73383130558303396a7add94bdafd"></a>

### `INPUT_KEY_LEFTSHIFT`

```c
#define INPUT_KEY_LEFTSHIFT 42
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

左 Shift键（Left Shift Key）。

<a id="ga7c8f628eb719d1d4b428805914c376a7"></a>

### `INPUT_KEY_M`

```c
#define INPUT_KEY_M 50
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

M键（M Key）。

<a id="gab159cae18818e930e4d928ebcc206651"></a>

### `INPUT_KEY_MENU`

```c
#define INPUT_KEY_MENU 139
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

菜单键（Menu Key）。

<a id="gae9779c5f21b9e14e5cbe1db8c5073819"></a>

### `INPUT_KEY_MINUS`

```c
#define INPUT_KEY_MINUS 12
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

减号键（Minus Key）。

<a id="ga8554adab31fc9c20c9de01bcb2aff839"></a>

### `INPUT_KEY_MUTE`

```c
#define INPUT_KEY_MUTE 113
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

静音键（Mute Key）。

<a id="ga09c0c860ee76803bb317dbac1072cd1d"></a>

### `INPUT_KEY_N`

```c
#define INPUT_KEY_N 49
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

N键（N Key）。

<a id="ga456a105c367fa61a1c041c6b9fd7a6fe"></a>

### `INPUT_KEY_NEXTSONG`

```c
#define INPUT_KEY_NEXTSONG 163
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

下一曲键（Next Song Key）。

<a id="ga93e220e43b3d33ffa985445f6dbf9c3c"></a>

### `INPUT_KEY_NUMLOCK`

```c
#define INPUT_KEY_NUMLOCK 69
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

数字锁定键（Num Lock Key）。

<a id="gae964cb377e0bcd958dad6da9626d298c"></a>

### `INPUT_KEY_O`

```c
#define INPUT_KEY_O 24
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

O键（O Key）。

<a id="ga396def37642dee65c74c48ff72aaa53d"></a>

### `INPUT_KEY_P`

```c
#define INPUT_KEY_P 25
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

P键（P Key）。

<a id="gaf6bc999ac2a136235fe95803c6df73c1"></a>

### `INPUT_KEY_PAGEDOWN`

```c
#define INPUT_KEY_PAGEDOWN 109
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

向下翻页键（Page Down Key）。

<a id="gaebb169acd4c3ce873353fd595364b374"></a>

### `INPUT_KEY_PAGEUP`

```c
#define INPUT_KEY_PAGEUP 104
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

向上翻页键（Page UpKey）。

<a id="ga08319efd258cd774ff8bc964c5a402dd"></a>

### `INPUT_KEY_PAUSE`

```c
#define INPUT_KEY_PAUSE 119
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

暂停键（Pause Key）。

<a id="ga1a377fdb1967aeff84e96d47c71bcf41"></a>

### `INPUT_KEY_PLAY`

```c
#define INPUT_KEY_PLAY 207
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

播放键（Play Key）。

<a id="ga210c431786b1a1b9af29b4a9516ca063"></a>

### `INPUT_KEY_PLAYPAUSE`

```c
#define INPUT_KEY_PLAYPAUSE 164
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

播放／暂停切换键（Play/Pause Toggle Key）。

<a id="ga2b05b5429ef1b0dc37698b82201d257d"></a>

### `INPUT_KEY_POWER`

```c
#define INPUT_KEY_POWER 116
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

电源键（Power Key）。

<a id="ga71b9c93b94d21c672bff26f9f1c6a7d4"></a>

### `INPUT_KEY_PREVIOUSSONG`

```c
#define INPUT_KEY_PREVIOUSSONG 165
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

上一曲键（Previous Song Key）。

<a id="ga4927612cf9f69324b15d8d9e46ab3326"></a>

### `INPUT_KEY_PRINT`

```c
#define INPUT_KEY_PRINT 210
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

打印键（Print Key）。

<a id="ga9ee8d6012d74e489ee8072f71497a36e"></a>

### `INPUT_KEY_Q`

```c
#define INPUT_KEY_Q 16
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

Q键（Q Key）。

<a id="ga421f14c501d86ed907ed4249f93a9e7e"></a>

### `INPUT_KEY_R`

```c
#define INPUT_KEY_R 19
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

R键（R Key）。

<a id="ga26409cb68bb098c1a18181cd737c82d6"></a>

### `INPUT_KEY_RECORD`

```c
#define INPUT_KEY_RECORD 167
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

录制键（Record Key）。

<a id="ga94e5a0d74dad76e57679b97af90ecb65"></a>

### `INPUT_KEY_RESERVED`

```c
#define INPUT_KEY_RESERVED 0
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

保留，不要使用（Reserved, do not use）。

<a id="gaeaf9b701a99b0d9d0210a472312d294d"></a>

### `INPUT_KEY_REWIND`

```c
#define INPUT_KEY_REWIND 168
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

快退键（Rewind Key）。

<a id="ga1bf6f292c1ab3ca25001b4ef4ca2626b"></a>

### `INPUT_KEY_RIGHT`

```c
#define INPUT_KEY_RIGHT 106
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

向右键（Right Key）。

<a id="gac02b6a2133d5ddf8847e1ce94250536f"></a>

### `INPUT_KEY_RIGHTALT`

```c
#define INPUT_KEY_RIGHTALT 100
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

右 Alt键（Right Alt Key）。

<a id="gaa0802d3471f6c774d37a8827e632d7fb"></a>

### `INPUT_KEY_RIGHTBRACE`

```c
#define INPUT_KEY_RIGHTBRACE 27
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

右括号键（Right Brace Key）。

<a id="gabb2e15ee9c30a649c92e82c42f513a35"></a>

### `INPUT_KEY_RIGHTCTRL`

```c
#define INPUT_KEY_RIGHTCTRL 97
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

右 Ctrl键（Right Ctrl Key）。

<a id="ga23ebc28da84872b585c9dcfeb057bfc9"></a>

### `INPUT_KEY_RIGHTMETA`

```c
#define INPUT_KEY_RIGHTMETA 126
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

右 Meta键（Right Meta Key）。

<a id="ga4fce26a4ffc693507043c1cfe95d279d"></a>

### `INPUT_KEY_RIGHTSHIFT`

```c
#define INPUT_KEY_RIGHTSHIFT 54
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

右 Shift键（Right Shift Key）。

<a id="gadefb5566a41148a0df4dd95cb2c5e2d2"></a>

### `INPUT_KEY_S`

```c
#define INPUT_KEY_S 31
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

S键（S Key）。

<a id="ga32491acdefb2e9f0eab5e7fc5755d2bc"></a>

### `INPUT_KEY_SCALE`

```c
#define INPUT_KEY_SCALE 120
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

缩放键（Scale Key）。

<a id="ga1d0958d93ddb7f3ff662e84a06c95a7c"></a>

### `INPUT_KEY_SCROLLLOCK`

```c
#define INPUT_KEY_SCROLLLOCK 70
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

滚动锁定键（Scroll Lock Key）。

<a id="ga7d45c7e2399dc6b20b6e470cb35d1dd6"></a>

### `INPUT_KEY_SEMICOLON`

```c
#define INPUT_KEY_SEMICOLON 39
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

分号键（Semicolon Key）。

<a id="gab17a459ab34d1353809c1a7360db3818"></a>

### `INPUT_KEY_SLASH`

```c
#define INPUT_KEY_SLASH 53
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

斜杠键（Slash Key）。

<a id="gaf826720ad8af092655351c0527b849df"></a>

### `INPUT_KEY_SLEEP`

```c
#define INPUT_KEY_SLEEP 142
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

系统睡眠键（System Sleep Key）。

<a id="ga4d6d5af48ea84fbea0df2fcb38ac7812"></a>

### `INPUT_KEY_SPACE`

```c
#define INPUT_KEY_SPACE 57
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

空格键（Space Key）。

<a id="ga99f104293221f3a3e5ff054fa259658f"></a>

### `INPUT_KEY_STOPCD`

```c
#define INPUT_KEY_STOPCD 166
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

停止光盘播放键（Stop CD Key）。

<a id="ga41b7f92a09624c06eee3a3650ac36139"></a>

### `INPUT_KEY_SYSRQ`

```c
#define INPUT_KEY_SYSRQ 99
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

系统请求键（SysReq Key）。

<a id="gadc43d9d7846b0e87dc217dcab831e4fe"></a>

### `INPUT_KEY_T`

```c
#define INPUT_KEY_T 20
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

T键（T Key）。

<a id="gac38db99311ad987f019f16e601a6911d"></a>

### `INPUT_KEY_TAB`

```c
#define INPUT_KEY_TAB 15
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

制表键（Tab Key）。

<a id="gab6403be2f0b9b60f626a57e5c9ed2666"></a>

### `INPUT_KEY_U`

```c
#define INPUT_KEY_U 22
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

U键（U Key）。

<a id="ga01e7f6a6aee5972612536c70a84db848"></a>

### `INPUT_KEY_UP`

```c
#define INPUT_KEY_UP 103
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

向上键（Up Key）。

<a id="ga74c693d33698eac543ee6ad4943c2d81"></a>

### `INPUT_KEY_UWB`

```c
#define INPUT_KEY_UWB 239
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

超宽带键（Ultra-Wideband Key）。

<a id="ga9f37deb8d631a8705cc0506d9b46b42c"></a>

### `INPUT_KEY_V`

```c
#define INPUT_KEY_V 47
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

V键（V Key）。

<a id="ga36b4c1340f9d7c5374e4fbe82244d492"></a>

### `INPUT_KEY_VOLUMEDOWN`

```c
#define INPUT_KEY_VOLUMEDOWN 114
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

降低音量键（Volume Down Key）。

<a id="gaa876076df525fa996dbced370c1be2e3"></a>

### `INPUT_KEY_VOLUMEUP`

```c
#define INPUT_KEY_VOLUMEUP 115
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

提高音量键（Volume Up Key）。

<a id="gaafc7f5b6c9d8f7ef13527ce60c08d36d"></a>

### `INPUT_KEY_W`

```c
#define INPUT_KEY_W 17
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

W键（W Key）。

<a id="gaeba4b122e3850b8c96e803353ac7bd35"></a>

### `INPUT_KEY_WAKEUP`

```c
#define INPUT_KEY_WAKEUP 143
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

唤醒系统键（System Wake Up Key）。

<a id="gae008f06aa7ca74912fe8ebbcd3dda45f"></a>

### `INPUT_KEY_WLAN`

```c
#define INPUT_KEY_WLAN 238
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

无线局域网键（Wireless LAN Key）。

<a id="ga8665fe56c47f02bd98793674dbc145b9"></a>

### `INPUT_KEY_X`

```c
#define INPUT_KEY_X 45
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

X键（X Key）。

<a id="gae86058bcd4e4a5393b35253176dc498f"></a>

### `INPUT_KEY_Y`

```c
#define INPUT_KEY_Y 21
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

Y键（Y Key）。

<a id="ga32a1603a3c0127e6ebe059af32314273"></a>

### `INPUT_KEY_Z`

```c
#define INPUT_KEY_Z 44
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

Z键（Z Key）。

<a id="ga62a5a51f0beb512236dfa276211e1f43"></a>

### `INPUT_MSC_SCAN`

```c
#define INPUT_MSC_SCAN 0x04
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

扫描码（Scan code）。

<a id="gab8aeb81a612ec63d687cbe1d9becb823"></a>

### `INPUT_REL_DIAL`

```c
#define INPUT_REL_DIAL 0x07
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

拨盘相对坐标（Relative dial coordinate）。

<a id="ga5b9989321b8e8f883bd338c1a37d50c2"></a>

### `INPUT_REL_HWHEEL`

```c
#define INPUT_REL_HWHEEL 0x06
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

水平滚轮相对坐标（Relative horizontal wheel coordinate）。

<a id="gaf2a08d3d5a0aa60b8f56ff7e2110a54e"></a>

### `INPUT_REL_MISC`

```c
#define INPUT_REL_MISC 0x09
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

其他相对坐标（Relative misc coordinate）。

<a id="ga5727f75f795b31982dc8681a0eed3378"></a>

### `INPUT_REL_RX`

```c
#define INPUT_REL_RX 0x03
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

绕 X 轴的相对旋转量（Relative rotation around X axis）。

<a id="ga85cde1de349dffef0c7dd5757e94cb4a"></a>

### `INPUT_REL_RY`

```c
#define INPUT_REL_RY 0x04
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

绕 Y 轴的相对旋转量（Relative rotation around Y axis）。

<a id="ga1f1ed1ce01e943906e5cecf071c0bf96"></a>

### `INPUT_REL_RZ`

```c
#define INPUT_REL_RZ 0x05
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

绕 Z 轴的相对旋转量（Relative rotation around Z axis）。

<a id="ga3884c7bbfb3b23e9cbc054f327b4344c"></a>

### `INPUT_REL_WHEEL`

```c
#define INPUT_REL_WHEEL 0x08
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

滚轮相对坐标（Relative wheel coordinate）。

<a id="ga6afab29530dfffbb81b191b90548ffd2"></a>

### `INPUT_REL_X`

```c
#define INPUT_REL_X 0x00
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

相对 X 坐标（Relative X coordinate）。

<a id="ga5fbdf5c33ac1e5330c3f30b37ee8f51d"></a>

### `INPUT_REL_Y`

```c
#define INPUT_REL_Y 0x01
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

相对 Y 坐标（Relative Y coordinate）。

<a id="gae5626b188d77b39a79df4bb7790cd316"></a>

### `INPUT_REL_Z`

```c
#define INPUT_REL_Z 0x02
```

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
```

相对 Z 坐标（Relative Z coordinate）。


## 4.8\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/input/input-event-codes.h](../api_file_input_wake_protocol_reference/P003_zephyr__dt-bindings__input__input-event-codes.h_文件参考.md)

<a id="INPUT_EV_CODES"></a>
<a id="INPUT_KEY_CODES"></a>
<a id="INPUT_BTN_CODES"></a>
<a id="INPUT_ABS_CODES"></a>
<a id="INPUT_REL_CODES"></a>
<a id="INPUT_MSC_CODES"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P003_服务发现协议（Service Discovery Protocol，SDP）.md) · [返回大纲](大纲.md) · [下一章](P005_轻量级M2M（LwM2M）的高层API。.md)
