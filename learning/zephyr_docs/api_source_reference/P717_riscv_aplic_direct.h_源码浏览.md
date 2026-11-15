---
id: learning.zephyr-docs.api-source-reference.page-717
title: riscv_aplic_direct.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic__direct_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第717章\_riscv\_aplic\_direct.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic__direct_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic__direct_8h.html)。

## 717.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="adevice_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="ariscv__aplic__direct_8h_html_a089864486c6968eda8a0dd702b77c464"></a>
<a id="ariscv__aplic__direct_8h_html_a375cb46c74f6b57288f745afa111a215"></a>
<a id="ariscv__aplic__direct_8h_html_a49a32a14d9da6d14e109ae0261d12e95"></a>
<a id="ariscv__aplic__direct_8h_html_a6f17dc3326d12fcebc0bd0e5dcfbd3e6"></a>
<a id="ariscv__aplic__direct_8h_html_a767ca44582fa377331d124db4412c9af"></a>
<a id="ariscv__aplic__direct_8h_html_a9fb92561a3507bace0e644f1cad25548"></a>
<a id="ariscv__aplic__direct_8h_html_aa2ccdb76d1801ab2a21f07ff00f7dabe"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_APLIC_DIRECT_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_APLIC_DIRECT_H_

#include <zephyr/device.h>
#include <zephyr/types.h>
#include <zephyr/arch/riscv/csr.h>

void riscv_aplic_direct_mode_enable(const struct device *dev, bool enable);

int riscv_aplic_is_enabled(uint32_t local_irq);

void riscv_aplic_set_priority(const struct device *dev, uint32_t local_irq, uint32_t prio);

#if defined(CONFIG_RISCV_APLIC_DIRECT_IRQ_AFFINITY)
void riscv_aplic_irq_set_affinity(const struct device *dev, uint32_t irq, uint32_t hart_id);
#endif

unsigned int riscv_aplic_get_saved_irq(void);

const struct device *riscv_aplic_get_saved_dev(void);

void aplic_irq_handler(const struct device *dev);

int aplic_direct_init(const struct device *dev);

#endif /* ZEPHYR_DRIVERS_INTERRUPT_CONTROLLER_INTC_RISCV_APLIC_DIRECT_H_ */
```

## 717.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© Qualcomm Technologies, Inc. and/or its subsidiaries.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 98 行

头文件保护宏（Header guard）标记：`ZEPHYR_DRIVERS_INTERRUPT_CONTROLLER_INTC_RISCV_APLIC_DIRECT_H_`。

## 717.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic__direct_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [riscv_aplic_direct_mode_enable](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic__direct_8h.html#a375cb46c74f6b57288f745afa111a215)
- [device](../device_reference/P002_设备对象结构.md)
- [riscv_aplic_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic__direct_8h.html#aa2ccdb76d1801ab2a21f07ff00f7dabe)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [riscv_aplic_set_priority](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic__direct_8h.html#a767ca44582fa377331d124db4412c9af)
- [riscv_aplic_get_saved_irq](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic__direct_8h.html#a6f17dc3326d12fcebc0bd0e5dcfbd3e6)
- [riscv_aplic_get_saved_dev](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic__direct_8h.html#a49a32a14d9da6d14e109ae0261d12e95)
- [aplic_irq_handler](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic__direct_8h.html#a089864486c6968eda8a0dd702b77c464)
- [aplic_direct_init](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic__direct_8h.html#a9fb92561a3507bace0e644f1cad25548)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)

---

[上一章](P716_riscv_aplic.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P718_riscv_clic.h_源码浏览.md)
