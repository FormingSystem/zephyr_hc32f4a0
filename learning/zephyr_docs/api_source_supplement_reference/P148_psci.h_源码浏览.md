---
id: learning.zephyr-docs.api-source-supplement-reference.page-148
title: psci.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/psci_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第148章\_psci.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/psci_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../power/P072_Arm电源状态协调接口头文件.md)。

## 148.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="adevice_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="apsci_8h_html_a1964266f31f19eb7e7e0acd4bb660f4c"></a>
<a id="apsci_8h_html_ac41b706f3b75f2c42689e5c57908903c"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>

```c
/*
 * Copyright 2020 Carlo Caione <ccaione@baylibre.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_PM_CPU_OPS_PSCI_H_
#define ZEPHYR_INCLUDE_DRIVERS_PM_CPU_OPS_PSCI_H_

#include <zephyr/types.h>
#include <zephyr/arch/arm64/arm-smccc.h>
#include <stddef.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

/* PSCI version decoding (independent of PSCI version) */

#define PSCI_VERSION_MAJOR_SHIFT                16
#define PSCI_VERSION_MINOR_MASK                 \
                ((1U << PSCI_VERSION_MAJOR_SHIFT) - 1)
#define PSCI_VERSION_MAJOR_MASK                 ~PSCI_VERSION_MINOR_MASK

#define PSCI_VERSION_MAJOR(ver)                 \
                (((ver) & PSCI_VERSION_MAJOR_MASK) >> PSCI_VERSION_MAJOR_SHIFT)

#define PSCI_VERSION_MINOR(ver)                 \
                ((ver) & PSCI_VERSION_MINOR_MASK)

uint32_t psci_version(void);


int psci_cpu_suspend(uint32_t state, uintptr_t entry_point);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_PM_CPU_OPS_PSCI_H_ */
```

## 148.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2020 Carlo Caione <ccaione@baylibre.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 25 行

电源状态协调接口（PSCI）的版本解码，与 PSCI 版本本身无关。

### 注释 3：原第 77 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PM_CPU_OPS_PSCI_H_`。

## 148.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../power/P072_Arm电源状态协调接口头文件.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [psci_version](https://docs.zephyrproject.org/latest/doxygen/html/psci_8h.html#a1964266f31f19eb7e7e0acd4bb660f4c)
- [psci_cpu_suspend](https://docs.zephyrproject.org/latest/doxygen/html/psci_8h.html#ac41b706f3b75f2c42689e5c57908903c)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)

---

[上一章](P147_pm_s2ram.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P149_pstate.h_源码浏览.md)
