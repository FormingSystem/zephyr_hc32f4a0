---
id: learning.zephyr-docs.api-source-reference.page-601
title: nrf_qspi_nor.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf__qspi__nor_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第601章\_nrf\_qspi\_nor.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nrf__qspi__nor_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nrf__qspi__nor_8h.html)。

## 601.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="anrf__qspi__nor_8h_html_abfe75f149d6a54c7fefe9d3a2ed21ea3"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_FLASH_NRF_QSPI_NOR_H_
#define ZEPHYR_INCLUDE_DRIVERS_FLASH_NRF_QSPI_NOR_H_

#ifdef __cplusplus
extern "C" {
#endif

__syscall void nrf_qspi_nor_xip_enable(const struct device *dev, bool enable);

#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/nrf_qspi_nor.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_FLASH_NRF_QSPI_NOR_H_ */
```

## 601.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 40 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FLASH_NRF_QSPI_NOR_H_`。

## 601.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nrf__qspi__nor_8h.html)
- [nrf_qspi_nor_xip_enable](https://docs.zephyrproject.org/latest/doxygen/html/nrf__qspi__nor_8h.html#abfe75f149d6a54c7fefe9d3a2ed21ea3)
- [device](../device_reference/P002_设备对象结构.md)

---

[上一章](P600_nrf_lpcomp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P602_numaker_m031x_clock.h_源码浏览.md)
