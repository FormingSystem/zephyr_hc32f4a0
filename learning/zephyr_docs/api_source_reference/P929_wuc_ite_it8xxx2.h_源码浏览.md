---
id: learning.zephyr-docs.api-source-reference.page-929
title: wuc_ite_it8xxx2.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wuc__ite__it8xxx2_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第929章\_wuc\_ite\_it8xxx2.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/wuc__ite__it8xxx2_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/wuc__ite__it8xxx2_8h.html)。

## 929.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="adevice_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="awuc__ite__it8xxx2_8h_html_a12abd49530eee59cb3d9670c35c307b1"></a>
<a id="awuc__ite__it8xxx2_8h_html_ab589f992436176f288056e219ead7972"></a>
<a id="awuc__ite__it8xxx2_8h_html_ad48382e2c3fd0d12c3a1334d863a9065"></a>
<a id="awuc__ite__it8xxx2_8h_html_af707d0b461010aea4fcfbfbeb82d0b2b"></a>

```c
/*
 * Copyright (c) 2022 ITE Corporation. All Rights Reserved
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_WUC_ITE_IT8XXX2_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_WUC_ITE_IT8XXX2_H_

#include <zephyr/device.h>
#include <stdint.h>

void it8xxx2_wuc_enable(const struct device *dev, uint8_t mask);

void it8xxx2_wuc_disable(const struct device *dev, uint8_t mask);

void it8xxx2_wuc_clear_status(const struct device *dev, uint8_t mask);

void it8xxx2_wuc_set_polarity(const struct device *dev, uint8_t mask,
                              uint32_t flags);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_WUC_ITE_IT8XXX2_H_ */
```

## 929.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 ITE Corporation. All Rights Reserved。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 50 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_WUC_ITE_IT8XXX2_H_`。

## 929.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/wuc__ite__it8xxx2_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [it8xxx2_wuc_enable](https://docs.zephyrproject.org/latest/doxygen/html/wuc__ite__it8xxx2_8h.html#a12abd49530eee59cb3d9670c35c307b1)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [it8xxx2_wuc_disable](https://docs.zephyrproject.org/latest/doxygen/html/wuc__ite__it8xxx2_8h.html#af707d0b461010aea4fcfbfbeb82d0b2b)
- [it8xxx2_wuc_clear_status](https://docs.zephyrproject.org/latest/doxygen/html/wuc__ite__it8xxx2_8h.html#ad48382e2c3fd0d12c3a1334d863a9065)
- [it8xxx2_wuc_set_polarity](https://docs.zephyrproject.org/latest/doxygen/html/wuc__ite__it8xxx2_8h.html#ab589f992436176f288056e219ead7972)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [device.h](../device_reference/P007_设备模型头文件参考.md)

---

[上一章](P928_wuc_ite_it51xxx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P930_wuc_nxp_llwu.h_源码浏览.md)
