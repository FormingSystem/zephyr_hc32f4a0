---
id: learning.zephyr-docs.api-source-reference.page-385
title: input_pmw3610.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__pmw3610_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第385章\_input\_pmw3610.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/input__pmw3610_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/input__pmw3610_8h.html)。

## 385.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="agroup__pmw3610__interface_html_ga7c20acd4c9ed5b1e16ebc2e093119e0b"></a>
<a id="agroup__pmw3610__interface_html_gaa70dd183377503db716ec6277dade83a"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright 2024 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_INPUT_INPUT_PMW3610_H_
#define ZEPHYR_INCLUDE_INPUT_INPUT_PMW3610_H_


int pmw3610_set_resolution(const struct device *dev, uint16_t res_cpi);

int pmw3610_force_awake(const struct device *dev, bool enable);


#endif /* ZEPHYR_INCLUDE_INPUT_INPUT_PMW3610_H_ */
```

## 385.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 47 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_INPUT_INPUT_PMW3610_H_`。

## 385.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/input__pmw3610_8h.html)
- [pmw3610_set_resolution](https://docs.zephyrproject.org/latest/doxygen/html/group__pmw3610__interface.html#ga7c20acd4c9ed5b1e16ebc2e093119e0b)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [pmw3610_force_awake](https://docs.zephyrproject.org/latest/doxygen/html/group__pmw3610__interface.html#gaa70dd183377503db716ec6277dade83a)

---

[上一章](P384_input_paw32xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P386_input_renesas_ra_ctsu.h_源码浏览.md)
