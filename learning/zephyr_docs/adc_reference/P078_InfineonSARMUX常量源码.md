---
id: learning.zephyr-docs.adc_reference.adcheaderremaining-78
title: InfineonSARMUX常量源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-sar_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第78章\_InfineonSARMUX常量源码

原文：[infineon-sar_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/infineon-sar_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览页的全部可见代码、注释与版权许可。仅去掉网页行号和行尾空白；网页折叠或未显示的文档注释不在可见源码中补造。接口中文说明见[对应参考页](P077_InfineonSARMUX常量参考.md)。

## 78.1\_完整可见源码

以下代码保持原标识符和法律声明，便于与官方文件逐项对照。

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ADC_INFINEON_SAR_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ADC_INFINEON_SAR_H_

/*
 * SARMUX Hardware Addresses
 * Used for zephyr,input-positive and zephyr,input-negative
 * SARMUX dedicated port (typically Port 2)
 */

#define CY_SAR_ADDR_SARMUX_0 0x0
#define CY_SAR_ADDR_SARMUX_1 0x1
#define CY_SAR_ADDR_SARMUX_2 0x2
#define CY_SAR_ADDR_SARMUX_3 0x3
#define CY_SAR_ADDR_SARMUX_4 0x4
#define CY_SAR_ADDR_SARMUX_5 0x5
#define CY_SAR_ADDR_SARMUX_6 0x6
#define CY_SAR_ADDR_SARMUX_7 0x7

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ADC_INFINEON_SAR_H_ */
```

## 78.2\_注释与阅读说明

原注释译文：SARMUX硬件地址（Hardware Address），用于 `zephyr,input-positive` 与 `zephyr,input-negative`；SARMUX专用端口（Dedicated Port）通常为端口2。八个宏的值从 `0x0` 到 `0x7`，宏名与值均保持原样。

---

[上一章：InfineonSARMUX常量参考](P077_InfineonSARMUX常量参考.md) · [返回大纲](大纲.md)
