---
id: learning.zephyr-docs.api-source-reference.page-531
title: mipi_display.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mipi__display_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第531章\_mipi\_display.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mipi__display_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mipi__display_8h.html)。

## 531.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00264"></a>
<a id="l00265"></a>

```c
/*
 * Copyright 2023 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DISPLAY_MIPI_DISPLAY_H_
#define ZEPHYR_INCLUDE_DISPLAY_MIPI_DISPLAY_H_


#ifdef __cplusplus
extern "C" {
#endif


#define MIPI_DCS_NOP                        0x00U
#define MIPI_DCS_SOFT_RESET                 0x01U
#define MIPI_DCS_GET_COMPRESSION_MODE       0x03U
#define MIPI_DCS_GET_DISPLAY_ID             0x04U
#define MIPI_DCS_GET_RED_CHANNEL            0x06U
#define MIPI_DCS_GET_GREEN_CHANNEL          0x07U
#define MIPI_DCS_GET_BLUE_CHANNEL           0x08U
#define MIPI_DCS_GET_DISPLAY_STATUS         0x09U
#define MIPI_DCS_GET_POWER_MODE             0x0AU
#define MIPI_DCS_GET_ADDRESS_MODE           0x0BU
#define MIPI_DCS_GET_PIXEL_FORMAT           0x0CU
#define MIPI_DCS_GET_DISPLAY_MODE           0x0DU
#define MIPI_DCS_GET_SIGNAL_MODE            0x0EU
#define MIPI_DCS_GET_DIAGNOSTIC_RESULT      0x0FU
#define MIPI_DCS_ENTER_SLEEP_MODE           0x10U
#define MIPI_DCS_EXIT_SLEEP_MODE            0x11U
#define MIPI_DCS_ENTER_PARTIAL_MODE         0x12U
#define MIPI_DCS_ENTER_NORMAL_MODE          0x13U
#define MIPI_DCS_EXIT_INVERT_MODE           0x20U
#define MIPI_DCS_ENTER_INVERT_MODE          0x21U
#define MIPI_DCS_SET_GAMMA_CURVE            0x26U
#define MIPI_DCS_SET_DISPLAY_OFF            0x28U
#define MIPI_DCS_SET_DISPLAY_ON             0x29U
#define MIPI_DCS_SET_COLUMN_ADDRESS         0x2AU
#define MIPI_DCS_SET_PAGE_ADDRESS           0x2BU
#define MIPI_DCS_WRITE_MEMORY_START         0x2CU
#define MIPI_DCS_WRITE_LUT                  0x2DU
#define MIPI_DCS_READ_MEMORY_START          0x2EU
#define MIPI_DCS_SET_PARTIAL_ROWS           0x30U
#define MIPI_DCS_SET_PARTIAL_COLUMNS        0x31U
#define MIPI_DCS_SET_SCROLL_AREA            0x33U
#define MIPI_DCS_SET_TEAR_OFF               0x34U
#define MIPI_DCS_SET_TEAR_ON                0x35U
#define MIPI_DCS_SET_ADDRESS_MODE           0x36U
#define MIPI_DCS_SET_SCROLL_START           0x37U
#define MIPI_DCS_EXIT_IDLE_MODE             0x38U
#define MIPI_DCS_ENTER_IDLE_MODE            0x39U
#define MIPI_DCS_SET_PIXEL_FORMAT           0x3AU
#define MIPI_DCS_WRITE_MEMORY_CONTINUE      0x3CU
#define MIPI_DCS_SET_3D_CONTROL             0x3DU
#define MIPI_DCS_READ_MEMORY_CONTINUE       0x3EU
#define MIPI_DCS_GET_3D_CONTROL             0x3FU
#define MIPI_DCS_SET_VSYNC_TIMING           0x40U
#define MIPI_DCS_SET_TEAR_SCANLINE          0x44U
#define MIPI_DCS_GET_SCANLINE               0x45U
#define MIPI_DCS_SET_DISPLAY_BRIGHTNESS     0x51U
#define MIPI_DCS_GET_DISPLAY_BRIGHTNESS     0x52U
#define MIPI_DCS_WRITE_CONTROL_DISPLAY      0x53U
#define MIPI_DCS_GET_CONTROL_DISPLAY        0x54U
#define MIPI_DCS_WRITE_POWER_SAVE           0x55U
#define MIPI_DCS_GET_POWER_SAVE             0x56U
#define MIPI_DCS_SET_CABC_MIN_BRIGHTNESS    0x5EU
#define MIPI_DCS_GET_CABC_MIN_BRIGHTNESS    0x5FU
#define MIPI_DCS_READ_DDB_START             0xA1U
#define MIPI_DCS_READ_DDB_CONTINUE          0xA8U

#define MIPI_DCS_PIXEL_FORMAT_24BIT         0x77
#define MIPI_DCS_PIXEL_FORMAT_18BIT         0x66
#define MIPI_DCS_PIXEL_FORMAT_16BIT         0x55
#define MIPI_DCS_PIXEL_FORMAT_12BIT         0x33
#define MIPI_DCS_PIXEL_FORMAT_8BIT          0x22
#define MIPI_DCS_PIXEL_FORMAT_3BIT          0x11



#define MIPI_DCS_ADDRESS_MODE_MIRROR_Y      BIT(7)
#define MIPI_DCS_ADDRESS_MODE_MIRROR_X      BIT(6)
#define MIPI_DCS_ADDRESS_MODE_SWAP_XY       BIT(5)
#define MIPI_DCS_ADDRESS_MODE_REFRESH_BT    BIT(4)
#define MIPI_DCS_ADDRESS_MODE_BGR           BIT(3)
#define MIPI_DCS_ADDRESS_MODE_LATCH_RL      BIT(2)
#define MIPI_DCS_ADDRESS_MODE_FLIP_X        BIT(1)
#define MIPI_DCS_ADDRESS_MODE_FLIP_Y        BIT(0)



#define MIPI_DSI_V_SYNC_START                           0x01U
#define MIPI_DSI_V_SYNC_END                             0x11U
#define MIPI_DSI_H_SYNC_START                           0x21U
#define MIPI_DSI_H_SYNC_END                             0x31U
#define MIPI_DSI_COLOR_MODE_OFF                         0x02U
#define MIPI_DSI_COLOR_MODE_ON                          0x12U
#define MIPI_DSI_SHUTDOWN_PERIPHERAL                    0x22U
#define MIPI_DSI_TURN_ON_PERIPHERAL                     0x32U
#define MIPI_DSI_GENERIC_SHORT_WRITE_0_PARAM            0x03U
#define MIPI_DSI_GENERIC_SHORT_WRITE_1_PARAM            0x13U
#define MIPI_DSI_GENERIC_SHORT_WRITE_2_PARAM            0x23U
#define MIPI_DSI_GENERIC_READ_REQUEST_0_PARAM           0x04U
#define MIPI_DSI_GENERIC_READ_REQUEST_1_PARAM           0x14U
#define MIPI_DSI_GENERIC_READ_REQUEST_2_PARAM           0x24U
#define MIPI_DSI_DCS_SHORT_WRITE                        0x05U
#define MIPI_DSI_DCS_SHORT_WRITE_PARAM                  0x15U
#define MIPI_DSI_DCS_READ                               0x06U
#define MIPI_DSI_SET_MAXIMUM_RETURN_PACKET_SIZE         0x37U
#define MIPI_DSI_END_OF_TRANSMISSION                    0x08U
#define MIPI_DSI_NULL_PACKET                            0x09U
#define MIPI_DSI_BLANKING_PACKET                        0x19U
#define MIPI_DSI_GENERIC_LONG_WRITE                     0x29U
#define MIPI_DSI_DCS_LONG_WRITE                         0x39U
#define MIPI_DSI_LOOSELY_PACKED_PIXEL_STREAM_YCBCR20    0x0CU
#define MIPI_DSI_PACKED_PIXEL_STREAM_YCBCR24            0x1CU
#define MIPI_DSI_PACKED_PIXEL_STREAM_YCBCR16            0x2CU
#define MIPI_DSI_PACKED_PIXEL_STREAM_30                 0x0DU
#define MIPI_DSI_PACKED_PIXEL_STREAM_36                 0x1DU
#define MIPI_DSI_PACKED_PIXEL_STREAM_YCBCR12            0x3DU
#define MIPI_DSI_PACKED_PIXEL_STREAM_16                 0x0EU
#define MIPI_DSI_PACKED_PIXEL_STREAM_18                 0x1EU
#define MIPI_DSI_PIXEL_STREAM_3BYTE_18                  0x2EU
#define MIPI_DSI_PACKED_PIXEL_STREAM_24                 0x3EU



#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DISPLAY_MIPI_DISPLAY_H_ */
```

## 531.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 265 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DISPLAY_MIPI_DISPLAY_H_`。

## 531.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mipi__display_8h.html)

---

[上一章](P530_mii.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P532_max2221x.h_源码浏览.md)
