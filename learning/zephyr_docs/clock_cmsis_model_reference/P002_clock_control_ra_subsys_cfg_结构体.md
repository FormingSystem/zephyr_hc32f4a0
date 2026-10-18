---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-2
title: clock_control_ra_subsys_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__control__ra__subsys__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_clock\_control\_ra\_subsys\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__control__ra__subsys__cfg.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

子系统时钟控制配置（Subsystem Clock Control Configuration）。

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

<a id="details"></a>

子系统时钟控制配置（Subsystem Clock Control Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

<a id="r_accdec304bb04737be3f75f0df3a29023"></a>

```c
uint32_t mstp
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mstp](#accdec304bb04737be3f75f0df3a29023)。

模块停止（MSTP）寄存器索引。

<a id="r_ad2dd15542bd355b716407bf9d9992f15"></a>

```c
uint32_t stop_bit
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[stop_bit](#ad2dd15542bd355b716407bf9d9992f15)。

时钟停止位（Clock Stop Bit）。

## 2.2\_详细说明（Detailed Documentation）

<a id="accdec304bb04737be3f75f0df3a29023"></a>

### `mstp`

```c
uint32_t clock_control_ra_subsys_cfg::mstp
```

模块停止（MSTP）寄存器索引。

<a id="ad2dd15542bd355b716407bf9d9992f15"></a>

### `stop_bit`

```c
uint32_t clock_control_ra_subsys_cfg::stop_bit
```

时钟停止位（Clock Stop Bit）。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/renesas_ra_cgc.h`

## 2.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/renesas_ra_cgc.h](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__cgc_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_clock_control_ra_pclk_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P003_clock_control_rx_pclk_cfg_结构体.md)
