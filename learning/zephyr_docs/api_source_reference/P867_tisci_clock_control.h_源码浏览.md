---
id: learning.zephyr-docs.api-source-reference.page-867
title: tisci_clock_control.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tisci__clock__control_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第867章\_tisci\_clock\_control.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/tisci__clock__control_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/tisci__clock__control_8h.html)。

## 867.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructtisci__clock__config_html"></a>
<a id="astructtisci__clock__config_html_a7746abef7a9d44b950aa8167a97e0e4b"></a>
<a id="astructtisci__clock__config_html_a7c461d913c53bc5275419c250b0cb1b8"></a>

```c
/*
 * Copyright (c) 2025 Texas Instruments
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_TISCI_CLOCK_CONTROL_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_TISCI_CLOCK_CONTROL_H_

#include <stdint.h>


struct tisci_clock_config {
        uint32_t dev_id;
        uint32_t clk_id;
};

#define TISCI_GET_CLOCK(node_id) DEVICE_DT_GET(DT_PHANDLE(node_id, clocks))

#define TISCI_GET_CLOCK_DETAILS(node_id)        \
        {       \
                .dev_id = DT_CLOCKS_CELL(node_id, devid),       \
                .clk_id = DT_CLOCKS_CELL(node_id, clkid)        \
        }

#define TISCI_GET_CLOCK_BY_INST(inst) TISCI_GET_CLOCK(DT_DRV_INST(inst))

#define TISCI_GET_CLOCK_DETAILS_BY_INST(inst) TISCI_GET_CLOCK_DETAILS(DT_DRV_INST(inst))


#endif
```

## 867.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Texas Instruments。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 867.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/tisci__clock__control_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [tisci_clock_config](../platform_security_model_reference/P064_tisci_clock_config_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [dev_id](../platform_security_model_reference/P064_tisci_clock_config_结构体.md#a7c461d913c53bc5275419c250b0cb1b8)
- [clk_id](../platform_security_model_reference/P064_tisci_clock_config_结构体.md#a7746abef7a9d44b950aa8167a97e0e4b)
- [tisci_clock_config::clk_id](../platform_security_model_reference/P064_tisci_clock_config_结构体.md#a7746abef7a9d44b950aa8167a97e0e4b)
- [tisci_clock_config::dev_id](../platform_security_model_reference/P064_tisci_clock_config_结构体.md#a7c461d913c53bc5275419c250b0cb1b8)

---

[上一章](P866_ti_tps6287x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P868_tla2528.h_源码浏览.md)
