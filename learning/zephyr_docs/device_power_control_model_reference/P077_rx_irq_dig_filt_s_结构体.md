---
id: learning.zephyr-docs.device-power-control-model-reference.page-77
title: rx_irq_dig_filt_s_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrx__irq__dig__filt__s.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第77章\_rx\_irq\_dig\_filt\_s\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrx__irq__dig__filt__s.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/interrupt_controller/intc_rx_icu.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 77.1\_数据成员（Data Fields）

<a id="r_a97fcdaa2ec47cb1714c48e5f67e4b069"></a>

```c
uint8_t filt_clk_div
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filt_clk_div](#a97fcdaa2ec47cb1714c48e5f67e4b069)。

<a id="r_a9338cdaf9596b591bc6ddd27a3a8cb97"></a>

```c
uint8_t filt_enable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filt_enable](#a9338cdaf9596b591bc6ddd27a3a8cb97)。

## 77.2\_详细说明（Detailed Documentation）

<a id="a97fcdaa2ec47cb1714c48e5f67e4b069"></a>

### `filt_clk_div`

```c
uint8_t rx_irq_dig_filt_s::filt_clk_div
```

<a id="a9338cdaf9596b591bc6ddd27a3a8cb97"></a>

### `filt_enable`

```c
uint8_t rx_irq_dig_filt_s::filt_enable
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/interrupt_controller/intc_rx_icu.h`

## 77.3\_原页交叉引用（Cross References）

- [zephyr/drivers/interrupt_controller/intc_rx_icu.h](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P076_rts5912_sccon_subsys_结构体.md) · [返回大纲](大纲.md) · [下一章](P078_sam_clk_cfg_结构体.md)
