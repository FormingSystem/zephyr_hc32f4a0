---
id: learning.zephyr-docs.api-source-supplement-reference.page-149
title: pstate.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pstate_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第149章\_pstate.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pstate_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../power/P029_性能状态头文件.md)。

## 149.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="foldopen00042"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="adevicetree_8h_html"></a>
<a id="agroup__devicetree-generic-foreach_html_gae907df926b94f1da52b1ab701392f3bd"></a>
<a id="agroup__devicetree-generic-id_html_ga015b4819473797982e83cae497697086"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="apstate_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructpstate_html"></a>
<a id="astructpstate_html_a323a2eadb17ea552b15468b1c59a4372"></a>
<a id="astructpstate_html_ac5c9e7d72a359e667ea84d0e75bfcda3"></a>

```c
/*
 * Copyright (c) 2025 Analog Devices, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_CPU_FREQ_PSTATE_H_
#define ZEPHYR_INCLUDE_CPU_FREQ_PSTATE_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/types.h>
#include <zephyr/devicetree.h>
#include <zephyr/cpu_freq/pstate.h>


#define PSTATE_DT_SYM(_node) _CONCAT(__pstate_, DT_DEP_ORD(_node))

#define PSTATE_DT_DEFINE(_node, _config)                                                           \
        const struct pstate PSTATE_DT_SYM(_node) = {                                               \
                .load_threshold = DT_PROP(_node, load_threshold),                                  \
                .config = _config,                                                                 \
        };

#define PSTATE_DT_GET(_node) &PSTATE_DT_SYM(_node)


struct pstate {
        uint8_t load_threshold;
        const void *config;
};

/* Define performance-states as extern to be picked up by CPU Freq policy */
#define Z_DECLARE_PSTATE_EXTERN(_node) \
        extern const struct pstate PSTATE_DT_SYM(_node);

DT_FOREACH_CHILD_STATUS_OKAY(DT_PATH(performance_states), Z_DECLARE_PSTATE_EXTERN)



#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_CPU_FREQ_PSTATE_H_ */
```

## 149.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Analog Devices, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 69 行

将性能状态（Performance-states）声明为 `extern`，以便 CPU 频率策略（CPU Freq policy）使用。

### 注释 3：原第 83 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_CPU_FREQ_PSTATE_H_`。

## 149.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../power/P029_性能状态头文件.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/cpu_freq/pstate.h](../power/P029_性能状态头文件.md)
- [pstate](../power/P026_性能状态结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [load_threshold](https://docs.zephyrproject.org/latest/doxygen/html/structpstate.html#ac5c9e7d72a359e667ea84d0e75bfcda3)
- [config](https://docs.zephyrproject.org/latest/doxygen/html/structpstate.html#a323a2eadb17ea552b15468b1c59a4372)
- [DT_FOREACH_CHILD_STATUS_OKAY](../dt_foreach_reference/P001_设备树遍历宏.md#gae907df926b94f1da52b1ab701392f3bd)
- [DT_PATH](../dt_identity_reference/P001_设备树节点标识宏.md#ga015b4819473797982e83cae497697086)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [pstate.h](../power/P029_性能状态头文件.md)
- [pstate::config](https://docs.zephyrproject.org/latest/doxygen/html/structpstate.html#a323a2eadb17ea552b15468b1c59a4372)
- [pstate::load_threshold](https://docs.zephyrproject.org/latest/doxygen/html/structpstate.html#ac5c9e7d72a359e667ea84d0e75bfcda3)

---

[上一章](P148_psci.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P150_ptp_clock.h_源码浏览.md)
