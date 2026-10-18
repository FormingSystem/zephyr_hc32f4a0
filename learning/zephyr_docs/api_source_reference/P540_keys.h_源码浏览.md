---
id: learning.zephyr-docs.api-source-reference.page-540
title: keys.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第540章\_keys.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html)。

## 540.1\_原始可见代码（Source Code）

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
<a id="foldopen00011"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00050"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="amodem_2ubx_2keys_8h_html_a3870935799d095c3f26f9518100cc0f7"></a>
<a id="amodem_2ubx_2keys_8h_html_a3870935799d095c3f26f9518100cc0f7a6a11f27393f7b111fb9891e0c4eba446"></a>
<a id="amodem_2ubx_2keys_8h_html_a3f60a56d68ce91595cba9bc8376edc28"></a>
<a id="amodem_2ubx_2keys_8h_html_a3f60a56d68ce91595cba9bc8376edc28a06e98d1b22ac527f9e5d47b9bb4704df"></a>
<a id="amodem_2ubx_2keys_8h_html_a3f60a56d68ce91595cba9bc8376edc28a08920384c5e1455caf614ec19910e048"></a>
<a id="amodem_2ubx_2keys_8h_html_a3f60a56d68ce91595cba9bc8376edc28a0ff489b47a8115f63474ef085da6372a"></a>
<a id="amodem_2ubx_2keys_8h_html_a3f60a56d68ce91595cba9bc8376edc28a495b45cb8dd0100b5d434b123967f66e"></a>
<a id="amodem_2ubx_2keys_8h_html_a3f60a56d68ce91595cba9bc8376edc28ae0eb15b61ee6ff0a20056c070975325c"></a>
<a id="amodem_2ubx_2keys_8h_html_a581a2003a265c9c8105fa5f0df74f5b2"></a>
<a id="amodem_2ubx_2keys_8h_html_a581a2003a265c9c8105fa5f0df74f5b2a42d94a342b5ccebb9f567a607ca10df5"></a>
<a id="amodem_2ubx_2keys_8h_html_a581a2003a265c9c8105fa5f0df74f5b2a779c6c882b5d77d721372354e3f663d7"></a>
<a id="amodem_2ubx_2keys_8h_html_a6b1ef40333aa59c241513cf28c6c803f"></a>
<a id="amodem_2ubx_2keys_8h_html_a6b1ef40333aa59c241513cf28c6c803fa044cfa915e52970eb7ce70d0bf888645"></a>
<a id="amodem_2ubx_2keys_8h_html_a6b1ef40333aa59c241513cf28c6c803fa20755f35c6d802dc6e1950ab863d7bdc"></a>
<a id="amodem_2ubx_2keys_8h_html_a6b1ef40333aa59c241513cf28c6c803fa214ddebd75edb172e7cc98ab1ce5d52b"></a>
<a id="amodem_2ubx_2keys_8h_html_a6b1ef40333aa59c241513cf28c6c803fa292ec3e8ce4ae953718144bb4c73f7b7"></a>
<a id="amodem_2ubx_2keys_8h_html_a6b1ef40333aa59c241513cf28c6c803fa2c77f2c5511f7aca8837a0c8277cee34"></a>
<a id="amodem_2ubx_2keys_8h_html_a6b1ef40333aa59c241513cf28c6c803fa4cb76102f8174a0a34af81f04c5598ed"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78a0037d074be499163225d38bde68f8284"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78a0538bba8ebfdbe1392c9efec0ccb1e71"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78a192177b57cc58ed258f39794ef1abc32"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78a2d160c79ca993743606b777a8198e16d"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78a336a72a618136c1ee1b4608525ec1d13"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78a65d2e8ce96656bbc9cbd611dc553d9da"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78a7dd5de001be05acf6d4a47c4b649159b"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78a7ffb40fb28aaaa57b2fd965ce0c053e4"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78a9eb4f86da492bdab944b46699dc99488"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78ab4b47920933c4cb459f4b156c5d4066d"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78ab5fe1c71c3f8b1ccd69e705668862fb5"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78ab9796954694436bd8c1417acd8121a05"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78ac988266ee549c2824ff121f3c9471344"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78aee92e43d1c84b3cd729173b81f3a2f5d"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78aefbae40d03e2976f8de982a4d58ca787"></a>
<a id="amodem_2ubx_2keys_8h_html_aa9a0c17a62bdac457f3d7e960da9be78aff548ffd79eaffb73532efb820431f73"></a>
<a id="amodem_2ubx_2keys_8h_html_ad806f9ced89f2f3338e5d14116cdb2df"></a>
<a id="amodem_2ubx_2keys_8h_html_ad806f9ced89f2f3338e5d14116cdb2dfa0adf8300b051ffd90e13d04087f95ccf"></a>
<a id="amodem_2ubx_2keys_8h_html_ad806f9ced89f2f3338e5d14116cdb2dfa584a0b3c407fd7f8c8100ebeb4b12566"></a>

```c
/*
 * Copyright (c) 2025 Croxel Inc.
 * Copyright (c) 2025 CogniPilot Foundation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_MODEM_UBX_KEYS_H_
#define ZEPHYR_INCLUDE_MODEM_UBX_KEYS_H_

enum ubx_keys_msg_out {
        UBX_KEY_MSG_OUT_NMEA_GGA_UART1 = 0x209100bb,
        UBX_KEY_MSG_OUT_NMEA_RMC_UART1 = 0x209100ac,
        UBX_KEY_MSG_OUT_NMEA_GSV_UART1 = 0x209100c5,
        UBX_KEY_MSG_OUT_NMEA_DTM_UART1 = 0x209100a7,
        UBX_KEY_MSG_OUT_NMEA_GBS_UART1 = 0x209100de,
        UBX_KEY_MSG_OUT_NMEA_GLL_UART1 = 0x209100ca,
        UBX_KEY_MSG_OUT_NMEA_GNS_UART1 = 0x209100b6,
        UBX_KEY_MSG_OUT_NMEA_GRS_UART1 = 0x209100cf,
        UBX_KEY_MSG_OUT_NMEA_GSA_UART1 = 0x209100c0,
        UBX_KEY_MSG_OUT_NMEA_GST_UART1 = 0x209100d4,
        UBX_KEY_MSG_OUT_NMEA_VTG_UART1 = 0x209100b1,
        UBX_KEY_MSG_OUT_NMEA_VLW_UART1 = 0x209100e8,
        UBX_KEY_MSG_OUT_NMEA_ZDA_UART1 = 0x209100d9,
        UBX_KEY_MSG_OUT_UBX_NAV_PVT_UART1 = 0x20910007,
        UBX_KEY_MSG_OUT_UBX_NAV_SAT_UART1 = 0x20910016,
        UBX_KEY_MSG_OUT_UBX_RXM_RTCM_UART1 = 0x20910269,
};

enum ubx_keys_rate {
        UBX_KEY_RATE_MEAS = 0x30210001,
        UBX_KEY_RATE_NAV = 0x30210002,
};

enum ubx_keys_nav_cfg {
        UBX_KEY_NAV_CFG_FIX_MODE = 0x20110011,
        UBX_KEY_NAV_CFG_DYN_MODEL = 0x20110021,
};

enum ubx_keys_uart1_proto {
        UBX_KEY_UART1_PROTO_IN_UBX = 0x10730001,
        UBX_KEY_UART1_PROTO_IN_NMEA = 0x10730002,
        UBX_KEY_UART1_PROTO_IN_RTCM3X = 0x10730004,
        UBX_KEY_UART1_PROTO_OUT_UBX = 0x10740001,
        UBX_KEY_UART1_PROTO_OUT_NMEA = 0x10740002,
        UBX_KEY_UART1_PROTO_OUT_RTCM3X = 0x10740004,
};

enum ubx_keys_uart1_cfg {
        UBX_KEY_CFG_UART1_BAUDRATE = 0x40520001,
        UBX_KEY_CFG_UART1_STOPBITS = 0x20520002,
        UBX_KEY_CFG_UART1_DATABITS = 0x20520003,
        UBX_KEY_CFG_UART1_PARITY = 0x20520004,
        UBX_KEY_CFG_UART1_ENABLED = 0x10520005,
};

enum ubx_keys_nav_hp_cfg {
        UBX_KEY_NAV_HP_CFG_GNSS_MODE = 0x20140011,
};

#endif /* ZEPHYR_INCLUDE_MODEM_UBX_KEYS_H_ */
```

## 540.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Croxel Inc.。

版权（Copyright）：© 2025 CogniPilot Foundation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 62 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MODEM_UBX_KEYS_H_`。

## 540.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html)
- [ubx_keys_msg_out](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78)
- [UBX_KEY_MSG_OUT_NMEA_GGA_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78a7ffb40fb28aaaa57b2fd965ce0c053e4)
- [UBX_KEY_MSG_OUT_NMEA_RMC_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78ab4b47920933c4cb459f4b156c5d4066d)
- [UBX_KEY_MSG_OUT_NMEA_GSV_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78a336a72a618136c1ee1b4608525ec1d13)
- [UBX_KEY_MSG_OUT_NMEA_DTM_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78ab5fe1c71c3f8b1ccd69e705668862fb5)
- [UBX_KEY_MSG_OUT_NMEA_GBS_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78a65d2e8ce96656bbc9cbd611dc553d9da)
- [UBX_KEY_MSG_OUT_NMEA_GLL_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78a7dd5de001be05acf6d4a47c4b649159b)
- [UBX_KEY_MSG_OUT_NMEA_GNS_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78a2d160c79ca993743606b777a8198e16d)
- [UBX_KEY_MSG_OUT_NMEA_GRS_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78a9eb4f86da492bdab944b46699dc99488)
- [UBX_KEY_MSG_OUT_NMEA_GSA_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78aff548ffd79eaffb73532efb820431f73)
- [UBX_KEY_MSG_OUT_NMEA_GST_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78a0538bba8ebfdbe1392c9efec0ccb1e71)
- [UBX_KEY_MSG_OUT_NMEA_VTG_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78a192177b57cc58ed258f39794ef1abc32)
- [UBX_KEY_MSG_OUT_NMEA_VLW_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78aee92e43d1c84b3cd729173b81f3a2f5d)
- [UBX_KEY_MSG_OUT_NMEA_ZDA_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78aefbae40d03e2976f8de982a4d58ca787)
- [UBX_KEY_MSG_OUT_UBX_NAV_PVT_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78a0037d074be499163225d38bde68f8284)
- [UBX_KEY_MSG_OUT_UBX_NAV_SAT_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78ac988266ee549c2824ff121f3c9471344)
- [UBX_KEY_MSG_OUT_UBX_RXM_RTCM_UART1](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#aa9a0c17a62bdac457f3d7e960da9be78ab9796954694436bd8c1417acd8121a05)
- [ubx_keys_rate](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a581a2003a265c9c8105fa5f0df74f5b2)
- [UBX_KEY_RATE_MEAS](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a581a2003a265c9c8105fa5f0df74f5b2a779c6c882b5d77d721372354e3f663d7)
- [UBX_KEY_RATE_NAV](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a581a2003a265c9c8105fa5f0df74f5b2a42d94a342b5ccebb9f567a607ca10df5)
- [ubx_keys_nav_cfg](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#ad806f9ced89f2f3338e5d14116cdb2df)
- [UBX_KEY_NAV_CFG_FIX_MODE](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#ad806f9ced89f2f3338e5d14116cdb2dfa584a0b3c407fd7f8c8100ebeb4b12566)
- [UBX_KEY_NAV_CFG_DYN_MODEL](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#ad806f9ced89f2f3338e5d14116cdb2dfa0adf8300b051ffd90e13d04087f95ccf)
- [ubx_keys_uart1_proto](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a6b1ef40333aa59c241513cf28c6c803f)
- [UBX_KEY_UART1_PROTO_IN_UBX](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a6b1ef40333aa59c241513cf28c6c803fa4cb76102f8174a0a34af81f04c5598ed)
- [UBX_KEY_UART1_PROTO_IN_NMEA](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a6b1ef40333aa59c241513cf28c6c803fa292ec3e8ce4ae953718144bb4c73f7b7)
- [UBX_KEY_UART1_PROTO_IN_RTCM3X](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a6b1ef40333aa59c241513cf28c6c803fa044cfa915e52970eb7ce70d0bf888645)
- [UBX_KEY_UART1_PROTO_OUT_UBX](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a6b1ef40333aa59c241513cf28c6c803fa214ddebd75edb172e7cc98ab1ce5d52b)
- [UBX_KEY_UART1_PROTO_OUT_NMEA](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a6b1ef40333aa59c241513cf28c6c803fa20755f35c6d802dc6e1950ab863d7bdc)
- [UBX_KEY_UART1_PROTO_OUT_RTCM3X](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a6b1ef40333aa59c241513cf28c6c803fa2c77f2c5511f7aca8837a0c8277cee34)
- [ubx_keys_uart1_cfg](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a3f60a56d68ce91595cba9bc8376edc28)
- [UBX_KEY_CFG_UART1_BAUDRATE](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a3f60a56d68ce91595cba9bc8376edc28a0ff489b47a8115f63474ef085da6372a)
- [UBX_KEY_CFG_UART1_STOPBITS](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a3f60a56d68ce91595cba9bc8376edc28a08920384c5e1455caf614ec19910e048)
- [UBX_KEY_CFG_UART1_DATABITS](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a3f60a56d68ce91595cba9bc8376edc28ae0eb15b61ee6ff0a20056c070975325c)
- [UBX_KEY_CFG_UART1_PARITY](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a3f60a56d68ce91595cba9bc8376edc28a06e98d1b22ac527f9e5d47b9bb4704df)
- [UBX_KEY_CFG_UART1_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a3f60a56d68ce91595cba9bc8376edc28a495b45cb8dd0100b5d434b123967f66e)
- [ubx_keys_nav_hp_cfg](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a3870935799d095c3f26f9518100cc0f7)
- [UBX_KEY_NAV_HP_CFG_GNSS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2keys_8h.html#a3870935799d095c3f26f9518100cc0f7a6a11f27393f7b111fb9891e0c4eba446)

---

[上一章](P539_stats.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P541_openthread.h_源码浏览.md)
