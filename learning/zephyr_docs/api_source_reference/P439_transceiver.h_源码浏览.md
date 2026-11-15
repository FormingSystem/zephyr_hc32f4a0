---
id: learning.zephyr-docs.api-source-reference.page-439
title: transceiver.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lin_2transceiver_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第439章\_transceiver.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lin_2transceiver_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lin_2transceiver_8h.html)。

## 439.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00034"></a>
<a id="l00040"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__lin__transceiver_html_ga898972c2e62cd45e53a901801502b2f9"></a>
<a id="agroup__lin__transceiver_html_ga8a81eb11fe36f6a1a4db51015367ed36"></a>
<a id="alin_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2022 Vestas Wind Systems A/S
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_ZEPHYR_DRIVERS_LIN_TRANSCEIVER_H
#define ZEPHYR_INCLUDE_ZEPHYR_DRIVERS_LIN_TRANSCEIVER_H

#ifdef __cplusplus
extern "C" {
#endif


#include <zephyr/drivers/lin.h>
#include <zephyr/device.h>



typedef int (*lin_transceiver_enable_t)(const struct device *dev, uint8_t flags);

typedef int (*lin_transceiver_disable_t)(const struct device *dev);

__subsystem struct lin_transceiver_driver_api {
        lin_transceiver_enable_t enable;
        lin_transceiver_disable_t disable;
};


static inline int lin_transceiver_enable(const struct device *dev, uint8_t flags)
{
        return DEVICE_API_GET(lin_transceiver, dev)->enable(dev, flags);
}

static inline int lin_transceiver_disable(const struct device *dev)
{
        return DEVICE_API_GET(lin_transceiver, dev)->disable(dev);
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_ZEPHYR_DRIVERS_LIN_TRANSCEIVER_H */
```

## 439.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Vestas Wind Systems A/S。

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 114 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ZEPHYR_DRIVERS_LIN_TRANSCEIVER_H`。

## 439.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lin_2transceiver_8h.html)
- [zephyr/drivers/lin.h](../peripheral_bus_storage_header_reference/P007_zephyr__drivers__lin.h_头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [lin_transceiver_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__transceiver.html#ga8a81eb11fe36f6a1a4db51015367ed36)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [lin_transceiver_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__transceiver.html#ga898972c2e62cd45e53a901801502b2f9)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [lin.h](../peripheral_bus_storage_header_reference/P007_zephyr__drivers__lin.h_头文件参考.md)

---

[上一章](P438_led_fake.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P440_linear_range.h_源码浏览.md)
