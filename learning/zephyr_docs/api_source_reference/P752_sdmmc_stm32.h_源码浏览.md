---
id: learning.zephyr-docs.api-source-reference.page-752
title: sdmmc_stm32.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sdmmc__stm32_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第752章\_sdmmc\_stm32.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sdmmc__stm32_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sdmmc__stm32_8h.html)。

## 752.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00025"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__stm32__sdmmc__disk__interface_html_ga391e478b31cbe349faea2f531a0c1935"></a>
<a id="agroup__stm32__sdmmc__disk__interface_html_gadfccc3613153a85f5b14d3b600220e42"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2025 The Zephyr Contributors.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_DISK_SDMMC_STM32_H_
#define ZEPHYR_INCLUDE_DRIVERS_DISK_SDMMC_STM32_H_

#include <zephyr/device.h>
#include <stdint.h>


void stm32_sdmmc_get_card_cid(const struct device *dev, uint32_t cid[4]);

void stm32_sdmmc_get_card_csd(const struct device *dev, uint32_t csd[4]);


#endif /* ZEPHYR_INCLUDE_DRIVERS_DISK_SDMMC_STM32_H_ */
```

## 752.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 The Zephyr Contributors.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 64 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_DISK_SDMMC_STM32_H_`。

## 752.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sdmmc__stm32_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [stm32_sdmmc_get_card_cid](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__sdmmc__disk__interface.html#gadfccc3613153a85f5b14d3b600220e42)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [stm32_sdmmc_get_card_csd](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__sdmmc__disk__interface.html#ga391e478b31cbe349faea2f531a0c1935)
- [device.h](../device_reference/P007_设备模型头文件参考.md)

---

[上一章](P751_sdmmc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P753_select.h_源码浏览.md)
