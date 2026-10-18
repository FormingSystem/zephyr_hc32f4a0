---
id: learning.zephyr-docs.api-source-reference.page-719
title: riscv_plic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/riscv__plic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第719章\_riscv\_plic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/riscv__plic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/riscv__plic_8h.html)。

## 719.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="adevice_8h_html"></a>
<a id="ariscv__plic_8h_html_a1208afc18002e5c1d2539958a0331647"></a>
<a id="ariscv__plic_8h_html_a2fe43faade1720a6046550e1175d6351"></a>
<a id="ariscv__plic_8h_html_a69dafac67e153be3be5f209050bd27ad"></a>
<a id="ariscv__plic_8h_html_a94ba6fdef8d90dae8b184f902519d248"></a>
<a id="ariscv__plic_8h_html_aa2f97f63d37ae4fc381d79bdf78a274d"></a>
<a id="ariscv__plic_8h_html_aa6aaaff9f5af0f4acbbea187f13a5e6b"></a>
<a id="ariscv__plic_8h_html_aa73cba0daaafa6dc0d1b54abbbc5172a"></a>
<a id="ariscv__plic_8h_html_aedeb9961a5d9d85e7084250cd31ca99f"></a>
<a id="ariscv__plic_8h_html_af7070f20dd4c29eee03f69d7795cced2"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2022 Carlo Caione <ccaione@baylibre.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_PLIC_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_PLIC_H_

#include <zephyr/device.h>

void riscv_plic_irq_complete(uint32_t irq);

void riscv_plic_irq_enable(uint32_t irq);

void riscv_plic_irq_disable(uint32_t irq);

int riscv_plic_irq_is_enabled(uint32_t irq);

void riscv_plic_set_priority(uint32_t irq, uint32_t prio);

int riscv_plic_irq_set_affinity(uint32_t irq, uint32_t cpumask);

void riscv_plic_irq_set_pending(uint32_t irq);

unsigned int riscv_plic_get_irq(void);

const struct device *riscv_plic_get_dev(void);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_PLIC_H_ */
```

## 719.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Carlo Caione <ccaione@baylibre.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 89 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_PLIC_H_`。

## 719.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/riscv__plic_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [riscv_plic_irq_complete](https://docs.zephyrproject.org/latest/doxygen/html/riscv__plic_8h.html#af7070f20dd4c29eee03f69d7795cced2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [riscv_plic_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/riscv__plic_8h.html#aa2f97f63d37ae4fc381d79bdf78a274d)
- [riscv_plic_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/riscv__plic_8h.html#a69dafac67e153be3be5f209050bd27ad)
- [riscv_plic_irq_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/riscv__plic_8h.html#aa6aaaff9f5af0f4acbbea187f13a5e6b)
- [riscv_plic_set_priority](https://docs.zephyrproject.org/latest/doxygen/html/riscv__plic_8h.html#aa73cba0daaafa6dc0d1b54abbbc5172a)
- [riscv_plic_irq_set_affinity](https://docs.zephyrproject.org/latest/doxygen/html/riscv__plic_8h.html#a2fe43faade1720a6046550e1175d6351)
- [riscv_plic_irq_set_pending](https://docs.zephyrproject.org/latest/doxygen/html/riscv__plic_8h.html#aedeb9961a5d9d85e7084250cd31ca99f)
- [riscv_plic_get_irq](https://docs.zephyrproject.org/latest/doxygen/html/riscv__plic_8h.html#a1208afc18002e5c1d2539958a0331647)
- [device](../device_reference/P002_设备对象结构.md)
- [riscv_plic_get_dev](https://docs.zephyrproject.org/latest/doxygen/html/riscv__plic_8h.html#a94ba6fdef8d90dae8b184f902519d248)
- [device.h](../device_reference/P007_设备模型头文件参考.md)

---

[上一章](P718_riscv_clic.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P720_rm3100.h_源码浏览.md)
