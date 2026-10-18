---
id: learning.zephyr-docs.api-source-reference.page-733
title: rtk.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtk_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第733章\_rtk.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rtk_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rtk_8h.html)。

## 733.1\_原始可见代码（Source Code）

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
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="foldopen00019"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="foldopen00027"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
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
<a id="artk_8h_html_a3fdf2f1d4f0414cc99c926a6fa06acf2"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructgnss__rtk__data__callback_html"></a>
<a id="astructgnss__rtk__data__callback_html_a63231a7df0b5e6346a61c28334dc6c71"></a>
<a id="astructgnss__rtk__data__callback_html_ab418432aeca49fdc7a8b26ffc3b0f443"></a>
<a id="astructgnss__rtk__data_html"></a>
<a id="astructgnss__rtk__data_html_a6843951f83ac4ea1624980cbe4d2f4f2"></a>
<a id="astructgnss__rtk__data_html_a9af2907041a16931c1f0e4119b9e3479"></a>

```c
/*
 * Copyright (c) 2023 Trackunit Corporation
 * Copyright (c) 2025 Croxel Inc.
 * Copyright (c) 2025 CogniPilot Foundation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_GNSS_RTK_RTK_H_
#define ZEPHYR_INCLUDE_GNSS_RTK_RTK_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>
#include <stddef.h>

struct gnss_rtk_data {
        const uint8_t *data;
        size_t len;
};

typedef void (*gnss_rtk_data_callback_t)(const struct device *dev,
                                         const struct gnss_rtk_data *data);

struct gnss_rtk_data_callback {
        const struct device *dev;
        gnss_rtk_data_callback_t callback;
};

#if CONFIG_GNSS_RTK
#define GNSS_RTK_DATA_CALLBACK_DEFINE(_dev, _callback)                                             \
        static const STRUCT_SECTION_ITERABLE(gnss_rtk_data_callback,                               \
                                             _gnss_rtk_data_callback__##_callback) = {             \
                .dev = _dev,                                                                       \
                .callback = _callback,                                                             \
        }

#define GNSS_DT_RTK_DATA_CALLBACK_DEFINE(_node_id, _callback)                                      \
        static const STRUCT_SECTION_ITERABLE(                                                      \
                gnss_rtk_data_callback,                                                            \
                CONCAT(_gnss_rtk_data_callback_, DT_DEP_ORD(_node_id), _, _callback)) = {          \
                .dev = DEVICE_DT_GET(_node_id),                                                    \
                .callback = _callback,                                                             \
        }
#else
#define GNSS_RTK_DATA_CALLBACK_DEFINE(_dev, _callback)
#define GNSS_DT_RTK_DATA_CALLBACK_DEFINE(_node_id, _callback)
#endif

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_GNSS_RTK_RTK_H_ */
```

## 733.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Trackunit Corporation。

版权（Copyright）：© 2025 Croxel Inc.。

版权（Copyright）：© 2025 CogniPilot Foundation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 56 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_GNSS_RTK_RTK_H_`。

## 733.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rtk_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [gnss_rtk_data](../sensor_navigation_model_reference/P013_gnss_rtk_data_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../sensor_navigation_model_reference/P013_gnss_rtk_data_结构体.md#a9af2907041a16931c1f0e4119b9e3479)
- [len](../sensor_navigation_model_reference/P013_gnss_rtk_data_结构体.md#a6843951f83ac4ea1624980cbe4d2f4f2)
- [gnss_rtk_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/rtk_8h.html#a3fdf2f1d4f0414cc99c926a6fa06acf2)
- [device](../device_reference/P002_设备对象结构.md)
- [gnss_rtk_data_callback](../sensor_navigation_model_reference/P014_gnss_rtk_data_callback_结构体.md)
- [dev](../sensor_navigation_model_reference/P014_gnss_rtk_data_callback_结构体.md#ab418432aeca49fdc7a8b26ffc3b0f443)
- [callback](../sensor_navigation_model_reference/P014_gnss_rtk_data_callback_结构体.md#a63231a7df0b5e6346a61c28334dc6c71)
- [gnss_rtk_data_callback::callback](../sensor_navigation_model_reference/P014_gnss_rtk_data_callback_结构体.md#a63231a7df0b5e6346a61c28334dc6c71)
- [gnss_rtk_data_callback::dev](../sensor_navigation_model_reference/P014_gnss_rtk_data_callback_结构体.md#ab418432aeca49fdc7a8b26ffc3b0f443)
- [gnss_rtk_data::len](../sensor_navigation_model_reference/P013_gnss_rtk_data_结构体.md#a6843951f83ac4ea1624980cbe4d2f4f2)
- [gnss_rtk_data::data](../sensor_navigation_model_reference/P013_gnss_rtk_data_结构体.md#a9af2907041a16931c1f0e4119b9e3479)

---

[上一章](P732_rpr_srv.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P734_rtl8752h-clocks.h_源码浏览.md)
