---
id: learning.zephyr-docs.usb.api-50
title: HID报告描述符构造宏
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usb__hid__mk__report__desc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_HID报告描述符构造宏

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__hid__mk__report__desc.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 50.1\_阅读说明与来源

译注：本页属于[HID通用说明](P040_HID通用说明.md)及其设备接口参考，说明报告描述符、设备回调和报告传输。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第40至50章的全部字段参考。

## 50.2\_宏定义（Macros）

<a id="r_ga3696f0782268d504b0c8bb540236779f"></a>

```c
#define HID_MOUSE_REPORT_DESC(bcnt)
```

用于 n 个按钮鼠标的简单 HID 鼠标报告描述符。

相关声明：[HID_MOUSE_REPORT_DESC](P050_HID报告描述符构造宏.md#ga3696f0782268d504b0c8bb540236779f)。

<a id="r_gaea973ffbe1612187c90614133956cfd6"></a>

```c
#define HID_KEYBOARD_REPORT_DESC()
```

简单 HID 键盘报告描述符。

相关声明：[HID_KEYBOARD_REPORT_DESC](P050_HID报告描述符构造宏.md#gaea973ffbe1612187c90614133956cfd6)。

## 50.3\_枚举（Enumerations）

<a id="r_ga4f2bb15109c64695f852afd6bd99e3bf"></a>

```c
enum hid_kbd_code {
    HID_KEY_A = 4,
    HID_KEY_B = 5,
    HID_KEY_C = 6,
    HID_KEY_D = 7,
    HID_KEY_E = 8,
    HID_KEY_F = 9,
    HID_KEY_G = 10,
    HID_KEY_H = 11,
    HID_KEY_I = 12,
    HID_KEY_J = 13,
    HID_KEY_K = 14,
    HID_KEY_L = 15,
    HID_KEY_M = 16,
    HID_KEY_N = 17,
    HID_KEY_O = 18,
    HID_KEY_P = 19,
    HID_KEY_Q = 20,
    HID_KEY_R = 21,
    HID_KEY_S = 22,
    HID_KEY_T = 23,
    HID_KEY_U = 24,
    HID_KEY_V = 25,
    HID_KEY_W = 26,
    HID_KEY_X = 27,
    HID_KEY_Y = 28,
    HID_KEY_Z = 29,
    HID_KEY_1 = 30,
    HID_KEY_2 = 31,
    HID_KEY_3 = 32,
    HID_KEY_4 = 33,
    HID_KEY_5 = 34,
    HID_KEY_6 = 35,
    HID_KEY_7 = 36,
    HID_KEY_8 = 37,
    HID_KEY_9 = 38,
    HID_KEY_0 = 39,
    HID_KEY_ENTER = 40,
    HID_KEY_ESC = 41,
    HID_KEY_BACKSPACE = 42,
    HID_KEY_TAB = 43,
    HID_KEY_SPACE = 44,
    HID_KEY_MINUS = 45,
    HID_KEY_EQUAL = 46,
    HID_KEY_LEFTBRACE = 47,
    HID_KEY_RIGHTBRACE = 48,
    HID_KEY_BACKSLASH = 49,
    HID_KEY_HASH = 50,
    HID_KEY_SEMICOLON = 51,
    HID_KEY_APOSTROPHE = 52,
    HID_KEY_GRAVE = 53,
    HID_KEY_COMMA = 54,
    HID_KEY_DOT = 55,
    HID_KEY_SLASH = 56,
    HID_KEY_CAPSLOCK = 57,
    HID_KEY_F1 = 58,
    HID_KEY_F2 = 59,
    HID_KEY_F3 = 60,
    HID_KEY_F4 = 61,
    HID_KEY_F5 = 62,
    HID_KEY_F6 = 63,
    HID_KEY_F7 = 64,
    HID_KEY_F8 = 65,
    HID_KEY_F9 = 66,
    HID_KEY_F10 = 67,
    HID_KEY_F11 = 68,
    HID_KEY_F12 = 69,
    HID_KEY_SYSRQ = 70,
    HID_KEY_SCROLLLOCK = 71,
    HID_KEY_PAUSE = 72,
    HID_KEY_INSERT = 73,
    HID_KEY_HOME = 74,
    HID_KEY_PAGEUP = 75,
    HID_KEY_DELETE = 76,
    HID_KEY_END = 77,
    HID_KEY_PAGEDOWN = 78,
    HID_KEY_RIGHT = 79,
    HID_KEY_LEFT = 80,
    HID_KEY_DOWN = 81,
    HID_KEY_UP = 82,
    HID_KEY_NUMLOCK = 83,
    HID_KEY_KPSLASH = 84,
    HID_KEY_KPASTERISK = 85,
    HID_KEY_KPMINUS = 86,
    HID_KEY_KPPLUS = 87,
    HID_KEY_KPENTER = 88,
    HID_KEY_KP_1 = 89,
    HID_KEY_KP_2 = 90,
    HID_KEY_KP_3 = 91,
    HID_KEY_KP_4 = 92,
    HID_KEY_KP_5 = 93,
    HID_KEY_KP_6 = 94,
    HID_KEY_KP_7 = 95,
    HID_KEY_KP_8 = 96,
    HID_KEY_KP_9 = 97,
    HID_KEY_KP_0 = 98,
    HID_KEY_KPDOT = 99,
    HID_KEY_MENU = 101
}
```

HID 键盘按键代码（Keyboard Button Codes）。

相关声明：[hid_kbd_code](P050_HID报告描述符构造宏.md#ga4f2bb15109c64695f852afd6bd99e3bf)、[HID_KEY_A](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5413afa6a28a21dd52f07db101f2d139)、[HID_KEY_B](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfabb0b25fe8c201dc75b72c7b078f745d6)、[HID_KEY_C](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa932c610512cc99157654c3997bc2b922)、[HID_KEY_D](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfabc172093417a4c40a7443eee551e9700)、[HID_KEY_E](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaff7192b9ddd4228e02c44b6fb2d7bf85)、[HID_KEY_F](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfacc002ca9f0f3bdc01b4de42d00e5560b)、[HID_KEY_G](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1eadd56346bbd64b1c33fa5393f65bda)、[HID_KEY_H](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4bfc341fccde664ec9267af6e705ba0c)、[HID_KEY_I](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfafcd25dc5bba218f7097698f8f49fdc45)、[HID_KEY_J](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa2a78196208c634941d63429cd1e1df7a)、[HID_KEY_K](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ceddaaaa90d84f0afb3e1ee9a35a976)、[HID_KEY_L](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5de66adc9eb2aa183eab1e23f977894)、[HID_KEY_M](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4f8174feca1eb72901576c4e24c8f8a9)、[HID_KEY_N](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab4d202043e8b0b7a8c2d4c519fd1eb07)、[HID_KEY_O](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfad8884ef7e77722099e6bd61265f6564c)、[HID_KEY_P](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaca0480331288d15eccec9f072f123817)、[HID_KEY_Q](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa05fb920f8129f57dd350036f17fbe519)、[HID_KEY_R](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa037de00c763ae6b270895b7a5f0f57a7)、[HID_KEY_S](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae6a84e8474b6c3e8f9f7d344408cfa0b)、[HID_KEY_T](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa893799f48b30c438349335556a0e15b6)、[HID_KEY_U](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab3c7c9f3a73e83623c651cdfddddeb05)、[HID_KEY_V](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa02f14e6303b4d2e4e46747324d649dda)、[HID_KEY_W](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfadf81a88f3f92f15e2abec83911bf3732)、[HID_KEY_X](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9f3b8bb63f6628db9a1678b72ec12b6d)、[HID_KEY_Y](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ca2ebe26c09f2400a8ebc0aa445ce89)、[HID_KEY_Z](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa5cd01ad23ede98de1ae176920b8fc8f)、[HID_KEY_1](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa039ced168420140b97e2d0676e1bb12a)、[HID_KEY_2](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae98dd71460def5e66fcf32e9783b96ea)、[HID_KEY_3](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf58d848786f8d2dfac702f7fae178311)、[HID_KEY_4](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa17019d72e84302486f72f7d8101baca5)、[HID_KEY_5](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf32ab36da2e30066c9ed2816596011c8)、[HID_KEY_6](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae16b76c1bf9f7aa58a1b1c556a6b6022)、[HID_KEY_7](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5887a1854f7d0787121bd75034cdd726)、[HID_KEY_8](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1761228849d7dc2b84d0565d3337b2e2)、[HID_KEY_9](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa758aec2540a6a2153702d6905c44ce52)、[HID_KEY_0](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa856ca663233681e789ef4aa94c44ebaf)、[HID_KEY_ENTER](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaeeab6ddad27c449cbc44ca2458912a75)、[HID_KEY_ESC](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa763b39fe76a92c4cc1fc32f47d2a760a)、[HID_KEY_BACKSPACE](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfafd6cf6a44966d518b173df4ed57ae720)、[HID_KEY_TAB](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a6c79e8ea85f6593c06d19098d69a03)、[HID_KEY_SPACE](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf4fc3d7b4b86f9f095cec624d190ebec)、[HID_KEY_MINUS](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa59864204064d3e8fac5271b69a7da23)、[HID_KEY_EQUAL](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfac8d82858905175ba79c24b0be1b1b1a8)、[HID_KEY_LEFTBRACE](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfac232473666b21ca772c84b68be6c1f3d)、[HID_KEY_RIGHTBRACE](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaef692bd882621d292255cb99d4697513)、[HID_KEY_BACKSLASH](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa25ba5457bc128593b1624d95ec536182)、[HID_KEY_HASH](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa0d57ce7c99d06ee9b15fef880af075eb)、[HID_KEY_SEMICOLON](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa3743f920856a12e726e1be05932c7411)、[HID_KEY_APOSTROPHE](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa7325a5bd52e9dc0cc38a85609b1c55ab)、[HID_KEY_GRAVE](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa8b84c64da5b8c5f5d99b86c1cfe09ffc)、[HID_KEY_COMMA](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa81aa5b3424f02fdf02295de47b11b19)、[HID_KEY_DOT](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa403fe927ebb0014e2c1b3dc25e1d9779)、[HID_KEY_SLASH](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa24c2c93a1c895745828311affc011dea)、[HID_KEY_CAPSLOCK](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4d40549a59fdcfdd0b2d592a6675bc89)、[HID_KEY_F1](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9642163abbbad8aa5c7088c8529aadd7)、[HID_KEY_F2](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9ce331f5f41ba3e3e05f485bc2d4138e)、[HID_KEY_F3](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa76adde1d9295cf62e7efb35e27911a1e)、[HID_KEY_F4](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa9956a2b95afe1a05fda65db5cc66467)、[HID_KEY_F5](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bface9e8d409d981f193f69fc5b29f38ca7)、[HID_KEY_F6](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfabc92147e725c8108c18f4e03005afbdc)、[HID_KEY_F7](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e2eabf8b9fa6cbfea613696b2c4122a)、[HID_KEY_F8](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5092add2863231d273ba60cd583ebe33)、[HID_KEY_F9](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a09deabde1a3a44378b7de44dad27b6)、[HID_KEY_F10](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfac2c4a3aec85b4d8171de4429ccabbe19)、[HID_KEY_F11](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa76bb35a0f71733b0a0f1bd7e3837064c)、[HID_KEY_F12](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab44ba4426c1574f4b296794b7bfe2172)、[HID_KEY_SYSRQ](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae5405b62cb20962cb5864ba6e90a4ab2)、[HID_KEY_SCROLLLOCK](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae16bd57629c7aba96a554d0446e83d98)、[HID_KEY_PAUSE](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1905733a0fe81f78e0752e3b0bb99c69)、[HID_KEY_INSERT](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e1c320cea0644c3dc38da06c865837b)、[HID_KEY_HOME](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5fc1127fe9014018f4831cbf272c883b)、[HID_KEY_PAGEUP](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa2468ac3b37d38b6158cd989ed54bcd8c)、[HID_KEY_DELETE](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae8f5051cb476c3e9253b008094c431fc)、[HID_KEY_END](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa8f933f0f6e5a1a3c3cdc1819ffcdce63)、[HID_KEY_PAGEDOWN](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7615ff4f608d64ae20a61540d939065)、[HID_KEY_RIGHT](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4c203feb452e3212089e8246b8d75f6c)、[HID_KEY_LEFT](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7d3c678a8ac31916068a0c5aff54d4b)、[HID_KEY_DOWN](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9e2597c2a109abda1c63c8d5ca5376b3)、[HID_KEY_UP](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5fe431b55adf16d82604e0fc2239090)、[HID_KEY_NUMLOCK](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfafec8c71efd5ee9decd156f0d33739fbe)、[HID_KEY_KPSLASH](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa44e83040efab214dcfe462ac0d338e0c)、[HID_KEY_KPASTERISK](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaff47eb8157a7118183573e3aefb7df08)、[HID_KEY_KPMINUS](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa6fb35c78b12ae434cb7a7280501886e9)、[HID_KEY_KPPLUS](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa2cb7852467d2ebd785e2f7556383a883)、[HID_KEY_KPENTER](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab5b923992d0bdc176f716cd8ace3a66e)、[HID_KEY_KP_1](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa7eea75b0eb4b4f0306daa3e6fccf09e4)、[HID_KEY_KP_2](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa68db65e7002e7cc599394a7eea116e3c)、[HID_KEY_KP_3](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4210f9a5ae469c8b863b28b9b2d8189d)、[HID_KEY_KP_4](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa48eefeeb48a942eaaa0726bd4a2df01d)、[HID_KEY_KP_5](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1b8d299d56a0289ae15cbf8c67e36a7c)、[HID_KEY_KP_6](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa90f2c51ad42e335a474061c4d5e4e5a9)、[HID_KEY_KP_7](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e191017084fadf830a7394de0e1cc05)、[HID_KEY_KP_8](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfadd7c795e2c9c212a4adeaba904bda447)、[HID_KEY_KP_9](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bface8d41615c6afd45724f4b6d16238c36)、[HID_KEY_KP_0](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ae4af2b06f6f2585a598353bfef9af7)、[HID_KEY_KPDOT](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9f26dd9d2aaa5d328481715764dbb1b9)、[HID_KEY_MENU](P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4b07b1bbe7695f2f67ce9df298c1d3c7)。

<a id="r_ga12f11556b697518b00fa86eb040f9eb8"></a>

```c
enum hid_kbd_modifier {
    HID_KBD_MODIFIER_NONE = 0x00,
    HID_KBD_MODIFIER_LEFT_CTRL = 0x01,
    HID_KBD_MODIFIER_LEFT_SHIFT = 0x02,
    HID_KBD_MODIFIER_LEFT_ALT = 0x04,
    HID_KBD_MODIFIER_LEFT_UI = 0x08,
    HID_KBD_MODIFIER_RIGHT_CTRL = 0x10,
    HID_KBD_MODIFIER_RIGHT_SHIFT = 0x20,
    HID_KBD_MODIFIER_RIGHT_ALT = 0x40,
    HID_KBD_MODIFIER_RIGHT_UI = 0x80
}
```

HID 键盘修饰键（Keyboard Modifiers）。

相关声明：[hid_kbd_modifier](P050_HID报告描述符构造宏.md#ga12f11556b697518b00fa86eb040f9eb8)、[HID_KBD_MODIFIER_NONE](P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a79b0eb4f485bedb745180f1b8798c603)、[HID_KBD_MODIFIER_LEFT_CTRL](P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a4df663509a05599fd66657cfc90a37c7)、[HID_KBD_MODIFIER_LEFT_SHIFT](P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8aba69ca183306d3d1427b66666803e57f)、[HID_KBD_MODIFIER_LEFT_ALT](P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a829d884291b546c0e276afa4ad92ac18)、[HID_KBD_MODIFIER_LEFT_UI](P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a718c92a2d0ca9dd6603825b97a99fc77)、[HID_KBD_MODIFIER_RIGHT_CTRL](P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a8e346c0e9c7d5b58e4b8748380423a92)、[HID_KBD_MODIFIER_RIGHT_SHIFT](P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8affdba298e8860b000a0916be7495c2dc)、[HID_KBD_MODIFIER_RIGHT_ALT](P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a85ce29a6ab9feef68350deca92001db2)、[HID_KBD_MODIFIER_RIGHT_UI](P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a1b4b75cd0364824cbfc80dfc68e294dd)。

<a id="r_ga8cef56ba216d0a01c6cc89f723d1740b"></a>

```c
enum hid_kbd_led {
    HID_KBD_LED_NUM_LOCK = 0x01,
    HID_KBD_LED_CAPS_LOCK = 0x02,
    HID_KBD_LED_SCROLL_LOCK = 0x04,
    HID_KBD_LED_COMPOSE = 0x08,
    HID_KBD_LED_KANA = 0x10
}
```

HID 键盘 LED。

相关声明：[hid_kbd_led](P050_HID报告描述符构造宏.md#ga8cef56ba216d0a01c6cc89f723d1740b)、[HID_KBD_LED_NUM_LOCK](P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740ba6cb2e1acb52cc5bab8dd3aa6ef6ac01b)、[HID_KBD_LED_CAPS_LOCK](P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740baa17e5130bd8c45eb21661d8783517266)、[HID_KBD_LED_SCROLL_LOCK](P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740ba6ea943f59b98680aefd0d5be4ef22e36)、[HID_KBD_LED_COMPOSE](P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740bad62692e71ae45351311c8bf2ce13e3c9)、[HID_KBD_LED_KANA](P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740bafd5d599c1955bdb1c62c7b17286b37f1)。

## 50.4\_详细说明（Detailed Documentation）

<a id="gaea973ffbe1612187c90614133956cfd6"></a>

### `HID_KEYBOARD_REPORT_DESC`

```c
#define HID_KEYBOARD_REPORT_DESC ( )
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
        {                               \
        HID_USAGE_PAGE(HID_USAGE_GEN_DESKTOP),                  \
        HID_USAGE(HID_USAGE_GEN_DESKTOP_KEYBOARD),              \
        HID_COLLECTION(HID_COLLECTION_APPLICATION),             \
                HID_USAGE_PAGE(HID_USAGE_GEN_DESKTOP_KEYPAD),   \
                /* HID_USAGE_MINIMUM(Keyboard LeftControl) */   \
                HID_USAGE_MIN8(0xE0),                           \
                /* HID_USAGE_MAXIMUM(Keyboard Right GUI) */     \
                HID_USAGE_MAX8(0xE7),                           \
                HID_LOGICAL_MIN8(0),                            \
                HID_LOGICAL_MAX8(1),                            \
                HID_REPORT_SIZE(1),                             \
                HID_REPORT_COUNT(8),                            \
                /* HID_INPUT(Data,Var,Abs) */                   \
                HID_INPUT(0x02),                                \
                HID_REPORT_SIZE(8),                             \
                HID_REPORT_COUNT(1),                            \
                /* HID_INPUT(Cnst,Var,Abs) */                   \
                HID_INPUT(0x03),                                \
                HID_REPORT_SIZE(1),                             \
                HID_REPORT_COUNT(5),                            \
                HID_USAGE_PAGE(HID_USAGE_GEN_LEDS),             \
                /* HID_USAGE_MINIMUM(Num Lock) */               \
                HID_USAGE_MIN8(1),                              \
                /* HID_USAGE_MAXIMUM(Kana) */                   \
                HID_USAGE_MAX8(5),                              \
                /* HID_OUTPUT(Data,Var,Abs) */                  \
                HID_OUTPUT(0x02),                               \
                HID_REPORT_SIZE(3),                             \
                HID_REPORT_COUNT(1),                            \
                /* HID_OUTPUT(Cnst,Var,Abs) */                  \
                HID_OUTPUT(0x03),                               \
                HID_REPORT_SIZE(8),                             \
                HID_REPORT_COUNT(6),                            \
                HID_LOGICAL_MIN8(0),                            \
                HID_LOGICAL_MAX8(101),                          \
                HID_USAGE_PAGE(HID_USAGE_GEN_DESKTOP_KEYPAD),   \
                /* HID_USAGE_MIN8(Reserved) */                  \
                HID_USAGE_MIN8(0),                              \
                /* HID_USAGE_MAX8(Keyboard Application) */      \
                HID_USAGE_MAX8(101),                            \
                /* HID_INPUT (Data,Ary,Abs) */                  \
                HID_INPUT(0x00),                                \
        HID_END_COLLECTION,                                     \
}
```

简单 HID 键盘报告描述符。

> 译注（源码核对）：当前预定义键盘报告包含8位修饰键、8位保留区、6个8位按键代码，并定义5个LED输出位及3位填充；不含报告ID。报告布局由这些项目共同决定，不能把按键用途码误当ASCII字符。

<a id="ga3696f0782268d504b0c8bb540236779f"></a>

### `HID_MOUSE_REPORT_DESC`

```c
#define HID_MOUSE_REPORT_DESC ( bcnt)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
        {                               \
        HID_USAGE_PAGE(HID_USAGE_GEN_DESKTOP),                  \
        HID_USAGE(HID_USAGE_GEN_DESKTOP_MOUSE),                 \
        HID_COLLECTION(HID_COLLECTION_APPLICATION),             \
                HID_USAGE(HID_USAGE_GEN_DESKTOP_POINTER),       \
                HID_COLLECTION(HID_COLLECTION_PHYSICAL),        \
                        /* Bits used for button signalling */   \
                        HID_USAGE_PAGE(HID_USAGE_GEN_BUTTON),   \
                        HID_USAGE_MIN8(1),                      \
                        HID_USAGE_MAX8(bcnt),                   \
                        HID_LOGICAL_MIN8(0),                    \
                        HID_LOGICAL_MAX8(1),                    \
                        HID_REPORT_SIZE(1),                     \
                        HID_REPORT_COUNT(bcnt),                 \
                        /* HID_INPUT (Data,Var,Abs) */          \
                        HID_INPUT(0x02),                        \
                        /* Unused bits */                       \
                        HID_REPORT_SIZE(8 - bcnt),              \
                        HID_REPORT_COUNT(1),                    \
                        /* HID_INPUT (Cnst,Ary,Abs) */          \
                        HID_INPUT(1),                           \
                        /* X and Y axis, scroll */              \
                        HID_USAGE_PAGE(HID_USAGE_GEN_DESKTOP),  \
                        HID_USAGE(HID_USAGE_GEN_DESKTOP_X),     \
                        HID_USAGE(HID_USAGE_GEN_DESKTOP_Y),     \
                        HID_USAGE(HID_USAGE_GEN_DESKTOP_WHEEL), \
                        HID_LOGICAL_MIN8(-127),                 \
                        HID_LOGICAL_MAX8(127),                  \
                        HID_REPORT_SIZE(8),                     \
                        HID_REPORT_COUNT(3),                    \
                        /* HID_INPUT (Data,Var,Rel) */          \
                        HID_INPUT(0x06),                        \
                HID_END_COLLECTION,                             \
        HID_END_COLLECTION,                                     \
}
```

用于 n 个按钮鼠标的简单 HID 鼠标报告描述符。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bcnt` | 按钮数量，允许范围为1至8。 |

> 译注（源码核对）：当前预定义鼠标描述符包含按钮位、补齐位以及X、Y和滚轮三个8位相对量；按钮数必须在1至8范围内。宏不为任意自定义报告自动增添字段，也不表示应用已经完成采样或USB发送。

<a id="ga4f2bb15109c64695f852afd6bd99e3bf"></a>

### `hid_kbd_code`

```c
enum hid_kbd_code
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 键盘按键代码（Keyboard Button Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HID_KEY_A` |  |
| `HID_KEY_B` |  |
| `HID_KEY_C` |  |
| `HID_KEY_D` |  |
| `HID_KEY_E` |  |
| `HID_KEY_F` |  |
| `HID_KEY_G` |  |
| `HID_KEY_H` |  |
| `HID_KEY_I` |  |
| `HID_KEY_J` |  |
| `HID_KEY_K` |  |
| `HID_KEY_L` |  |
| `HID_KEY_M` |  |
| `HID_KEY_N` |  |
| `HID_KEY_O` |  |
| `HID_KEY_P` |  |
| `HID_KEY_Q` |  |
| `HID_KEY_R` |  |
| `HID_KEY_S` |  |
| `HID_KEY_T` |  |
| `HID_KEY_U` |  |
| `HID_KEY_V` |  |
| `HID_KEY_W` |  |
| `HID_KEY_X` |  |
| `HID_KEY_Y` |  |
| `HID_KEY_Z` |  |
| `HID_KEY_1` |  |
| `HID_KEY_2` |  |
| `HID_KEY_3` |  |
| `HID_KEY_4` |  |
| `HID_KEY_5` |  |
| `HID_KEY_6` |  |
| `HID_KEY_7` |  |
| `HID_KEY_8` |  |
| `HID_KEY_9` |  |
| `HID_KEY_0` |  |
| `HID_KEY_ENTER` |  |
| `HID_KEY_ESC` |  |
| `HID_KEY_BACKSPACE` |  |
| `HID_KEY_TAB` |  |
| `HID_KEY_SPACE` |  |
| `HID_KEY_MINUS` |  |
| `HID_KEY_EQUAL` |  |
| `HID_KEY_LEFTBRACE` |  |
| `HID_KEY_RIGHTBRACE` |  |
| `HID_KEY_BACKSLASH` |  |
| `HID_KEY_HASH` |  |
| `HID_KEY_SEMICOLON` |  |
| `HID_KEY_APOSTROPHE` |  |
| `HID_KEY_GRAVE` |  |
| `HID_KEY_COMMA` |  |
| `HID_KEY_DOT` |  |
| `HID_KEY_SLASH` |  |
| `HID_KEY_CAPSLOCK` |  |
| `HID_KEY_F1` |  |
| `HID_KEY_F2` |  |
| `HID_KEY_F3` |  |
| `HID_KEY_F4` |  |
| `HID_KEY_F5` |  |
| `HID_KEY_F6` |  |
| `HID_KEY_F7` |  |
| `HID_KEY_F8` |  |
| `HID_KEY_F9` |  |
| `HID_KEY_F10` |  |
| `HID_KEY_F11` |  |
| `HID_KEY_F12` |  |
| `HID_KEY_SYSRQ` |  |
| `HID_KEY_SCROLLLOCK` |  |
| `HID_KEY_PAUSE` |  |
| `HID_KEY_INSERT` |  |
| `HID_KEY_HOME` |  |
| `HID_KEY_PAGEUP` |  |
| `HID_KEY_DELETE` |  |
| `HID_KEY_END` |  |
| `HID_KEY_PAGEDOWN` |  |
| `HID_KEY_RIGHT` |  |
| `HID_KEY_LEFT` |  |
| `HID_KEY_DOWN` |  |
| `HID_KEY_UP` |  |
| `HID_KEY_NUMLOCK` |  |
| `HID_KEY_KPSLASH` |  |
| `HID_KEY_KPASTERISK` |  |
| `HID_KEY_KPMINUS` |  |
| `HID_KEY_KPPLUS` |  |
| `HID_KEY_KPENTER` |  |
| `HID_KEY_KP_1` |  |
| `HID_KEY_KP_2` |  |
| `HID_KEY_KP_3` |  |
| `HID_KEY_KP_4` |  |
| `HID_KEY_KP_5` |  |
| `HID_KEY_KP_6` |  |
| `HID_KEY_KP_7` |  |
| `HID_KEY_KP_8` |  |
| `HID_KEY_KP_9` |  |
| `HID_KEY_KP_0` |  |
| `HID_KEY_KPDOT` |  |
| `HID_KEY_MENU` |  |

<a id="ga8cef56ba216d0a01c6cc89f723d1740b"></a>

### `hid_kbd_led`

```c
enum hid_kbd_led
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 键盘 LED。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HID_KBD_LED_NUM_LOCK` |  |
| `HID_KBD_LED_CAPS_LOCK` |  |
| `HID_KBD_LED_SCROLL_LOCK` |  |
| `HID_KBD_LED_COMPOSE` |  |
| `HID_KBD_LED_KANA` |  |

<a id="ga12f11556b697518b00fa86eb040f9eb8"></a>

### `hid_kbd_modifier`

```c
enum hid_kbd_modifier
```

```c
#include <zephyr/usb/class/hid.h>
```

HID 键盘修饰键（Keyboard Modifiers）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HID_KBD_MODIFIER_NONE` |  |
| `HID_KBD_MODIFIER_LEFT_CTRL` |  |
| `HID_KBD_MODIFIER_LEFT_SHIFT` |  |
| `HID_KBD_MODIFIER_LEFT_ALT` |  |
| `HID_KBD_MODIFIER_LEFT_UI` |  |
| `HID_KBD_MODIFIER_RIGHT_CTRL` |  |
| `HID_KBD_MODIFIER_RIGHT_SHIFT` |  |
| `HID_KBD_MODIFIER_RIGHT_ALT` |  |
| `HID_KBD_MODIFIER_RIGHT_UI` |  |

## 50.5\_源码跟踪与使用边界

通用项目及描述符见[hid.h](../../../include/zephyr/usb/class/hid.h)，新版接口见[usbd_hid.h](../../../include/zephyr/usb/class/usbd_hid.h)和[新版实现](../../../subsys/usb/device_next/class/usbd_hid.c)，旧接口见[usb_hid.h](../../../include/zephyr/usb/class/usb_hid.h)、[旧版实现](../../../subsys/usb/device/class/hid/core.c)及[新版兼容包装](../../../subsys/usb/device_next/class/usbd_hid_api.c)。本仓库版本可能与官方 latest 不同；译注依据保存的[官方通用头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/hid.h)、[新版头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_hid.h)、[新版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_hid.c)、[兼容包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_hid_api.c)和[旧版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/hid/core.c)，摘要见[来源记录](../SOURCES.md)。本批未编译、运行或操作USB硬件。

<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__usb__hid__definitions_html_ga0bdaa3d23c79204a1064cb53b279bd77"></a>
<a id="agroup__usb__hid__definitions_html_ga2e5e5ad0919fbaea0e6f8e5d86f4c2fd"></a>
<a id="agroup__usb__hid__definitions_html_ga69f8e44306828b3f44d3a7704ff07807"></a>
<a id="agroup__usb__hid__definitions_html_gacb3fc5b0f838dfa5eb95e9e1bf52b589"></a>
<a id="agroup__usb__hid__definitions_html_gae632e9a37203506c051c3cacfdf0c2c7"></a>
<a id="agroup__usb__hid__items_html_ga6cd6affb9d52e0bf98c7a5c83d03a764"></a>
<a id="agroup__usb__hid__definitions_html_ga13401731a0ead5448a0823d0f6142404"></a>
<a id="agroup__usb__hid__definitions_html_ga77a7162980a77efa1e2e7b21942bb7dd"></a>
<a id="agroup__usb__hid__definitions_html_ga983274dd50058de26e0e86d10d50e81a"></a>
<a id="agroup__usb__hid__definitions_html_gaa8c772d412ac1ac7a36739c52f04c0a9"></a>
<a id="agroup__usb__hid__definitions_html_gaca1e227f9241c217b8b1aeae6c4bd672"></a>
<a id="agroup__usb__hid__definitions_html_gad1ab1f8f9c8a4a80bfc8e3a327e3b2fb"></a>
<a id="agroup__usb__hid__definitions_html_gae283a3558ba536e163140a3b6cdbb273"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa5413afa6a28a21dd52f07db101f2d139"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfabb0b25fe8c201dc75b72c7b078f745d6"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa932c610512cc99157654c3997bc2b922"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfabc172093417a4c40a7443eee551e9700"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaff7192b9ddd4228e02c44b6fb2d7bf85"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfacc002ca9f0f3bdc01b4de42d00e5560b"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa1eadd56346bbd64b1c33fa5393f65bda"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa4bfc341fccde664ec9267af6e705ba0c"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfafcd25dc5bba218f7097698f8f49fdc45"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa2a78196208c634941d63429cd1e1df7a"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa4ceddaaaa90d84f0afb3e1ee9a35a976"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaf5de66adc9eb2aa183eab1e23f977894"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa4f8174feca1eb72901576c4e24c8f8a9"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfab4d202043e8b0b7a8c2d4c519fd1eb07"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfad8884ef7e77722099e6bd61265f6564c"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaca0480331288d15eccec9f072f123817"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa05fb920f8129f57dd350036f17fbe519"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa037de00c763ae6b270895b7a5f0f57a7"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfae6a84e8474b6c3e8f9f7d344408cfa0b"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa893799f48b30c438349335556a0e15b6"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfab3c7c9f3a73e83623c651cdfddddeb05"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa02f14e6303b4d2e4e46747324d649dda"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfadf81a88f3f92f15e2abec83911bf3732"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa9f3b8bb63f6628db9a1678b72ec12b6d"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa4ca2ebe26c09f2400a8ebc0aa445ce89"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaa5cd01ad23ede98de1ae176920b8fc8f"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa039ced168420140b97e2d0676e1bb12a"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfae98dd71460def5e66fcf32e9783b96ea"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaf58d848786f8d2dfac702f7fae178311"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa17019d72e84302486f72f7d8101baca5"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaf32ab36da2e30066c9ed2816596011c8"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfae16b76c1bf9f7aa58a1b1c556a6b6022"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa5887a1854f7d0787121bd75034cdd726"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa1761228849d7dc2b84d0565d3337b2e2"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa758aec2540a6a2153702d6905c44ce52"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa856ca663233681e789ef4aa94c44ebaf"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaeeab6ddad27c449cbc44ca2458912a75"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa763b39fe76a92c4cc1fc32f47d2a760a"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfafd6cf6a44966d518b173df4ed57ae720"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa5a6c79e8ea85f6593c06d19098d69a03"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaf4fc3d7b4b86f9f095cec624d190ebec"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaa59864204064d3e8fac5271b69a7da23"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfac8d82858905175ba79c24b0be1b1b1a8"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfac232473666b21ca772c84b68be6c1f3d"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaef692bd882621d292255cb99d4697513"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa25ba5457bc128593b1624d95ec536182"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa0d57ce7c99d06ee9b15fef880af075eb"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa3743f920856a12e726e1be05932c7411"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa7325a5bd52e9dc0cc38a85609b1c55ab"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa8b84c64da5b8c5f5d99b86c1cfe09ffc"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaa81aa5b3424f02fdf02295de47b11b19"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa403fe927ebb0014e2c1b3dc25e1d9779"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa24c2c93a1c895745828311affc011dea"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa4d40549a59fdcfdd0b2d592a6675bc89"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa9642163abbbad8aa5c7088c8529aadd7"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa9ce331f5f41ba3e3e05f485bc2d4138e"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa76adde1d9295cf62e7efb35e27911a1e"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaa9956a2b95afe1a05fda65db5cc66467"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bface9e8d409d981f193f69fc5b29f38ca7"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfabc92147e725c8108c18f4e03005afbdc"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa1e2eabf8b9fa6cbfea613696b2c4122a"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa5092add2863231d273ba60cd583ebe33"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa5a09deabde1a3a44378b7de44dad27b6"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfac2c4a3aec85b4d8171de4429ccabbe19"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa76bb35a0f71733b0a0f1bd7e3837064c"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfab44ba4426c1574f4b296794b7bfe2172"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfae5405b62cb20962cb5864ba6e90a4ab2"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfae16bd57629c7aba96a554d0446e83d98"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa1905733a0fe81f78e0752e3b0bb99c69"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa1e1c320cea0644c3dc38da06c865837b"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa5fc1127fe9014018f4831cbf272c883b"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa2468ac3b37d38b6158cd989ed54bcd8c"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfae8f5051cb476c3e9253b008094c431fc"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa8f933f0f6e5a1a3c3cdc1819ffcdce63"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaf7615ff4f608d64ae20a61540d939065"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa4c203feb452e3212089e8246b8d75f6c"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaf7d3c678a8ac31916068a0c5aff54d4b"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa9e2597c2a109abda1c63c8d5ca5376b3"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaf5fe431b55adf16d82604e0fc2239090"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfafec8c71efd5ee9decd156f0d33739fbe"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa44e83040efab214dcfe462ac0d338e0c"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfaff47eb8157a7118183573e3aefb7df08"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa6fb35c78b12ae434cb7a7280501886e9"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa2cb7852467d2ebd785e2f7556383a883"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfab5b923992d0bdc176f716cd8ace3a66e"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa7eea75b0eb4b4f0306daa3e6fccf09e4"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa68db65e7002e7cc599394a7eea116e3c"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa4210f9a5ae469c8b863b28b9b2d8189d"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa48eefeeb48a942eaaa0726bd4a2df01d"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa1b8d299d56a0289ae15cbf8c67e36a7c"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa90f2c51ad42e335a474061c4d5e4e5a9"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa1e191017084fadf830a7394de0e1cc05"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfadd7c795e2c9c212a4adeaba904bda447"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bface8d41615c6afd45724f4b6d16238c36"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa4ae4af2b06f6f2585a598353bfef9af7"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa9f26dd9d2aaa5d328481715764dbb1b9"></a>
<a id="gga4f2bb15109c64695f852afd6bd99e3bfa4b07b1bbe7695f2f67ce9df298c1d3c7"></a>
<a id="gga8cef56ba216d0a01c6cc89f723d1740ba6cb2e1acb52cc5bab8dd3aa6ef6ac01b"></a>
<a id="gga8cef56ba216d0a01c6cc89f723d1740baa17e5130bd8c45eb21661d8783517266"></a>
<a id="gga8cef56ba216d0a01c6cc89f723d1740ba6ea943f59b98680aefd0d5be4ef22e36"></a>
<a id="gga8cef56ba216d0a01c6cc89f723d1740bad62692e71ae45351311c8bf2ce13e3c9"></a>
<a id="gga8cef56ba216d0a01c6cc89f723d1740bafd5d599c1955bdb1c62c7b17286b37f1"></a>
<a id="gga12f11556b697518b00fa86eb040f9eb8a79b0eb4f485bedb745180f1b8798c603"></a>
<a id="gga12f11556b697518b00fa86eb040f9eb8a4df663509a05599fd66657cfc90a37c7"></a>
<a id="gga12f11556b697518b00fa86eb040f9eb8aba69ca183306d3d1427b66666803e57f"></a>
<a id="gga12f11556b697518b00fa86eb040f9eb8a829d884291b546c0e276afa4ad92ac18"></a>
<a id="gga12f11556b697518b00fa86eb040f9eb8a718c92a2d0ca9dd6603825b97a99fc77"></a>
<a id="gga12f11556b697518b00fa86eb040f9eb8a8e346c0e9c7d5b58e4b8748380423a92"></a>
<a id="gga12f11556b697518b00fa86eb040f9eb8affdba298e8860b000a0916be7495c2dc"></a>
<a id="gga12f11556b697518b00fa86eb040f9eb8a85ce29a6ab9feef68350deca92001db2"></a>
<a id="gga12f11556b697518b00fa86eb040f9eb8a1b4b75cd0364824cbfc80dfc68e294dd"></a>

[上一章](P049_HID报告项目定义.md) · [返回大纲](大纲.md) · [下一章](P051_HID键盘示例.md)
