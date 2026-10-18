---
id: learning.zephyr-docs.device-power-control-model-reference.page-6
title: dtc_transfer_status_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdtc__transfer__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_dtc\_transfer\_status\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdtc__transfer__status.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数据传输控制器（DTC）的传输状态。

```c
#include <zephyr/drivers/misc/renesas_rx_dtc/renesas_rx_dtc.h>
```

<a id="details"></a>

数据传输控制器（DTC）的传输状态。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_a2cc3ae3d23f9f5cfbfd5a1cebf4d1291"></a>

```c
uint8_t activation_irq
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[activation_irq](#a2cc3ae3d23f9f5cfbfd5a1cebf4d1291)。

激活 IRQ 编号。

<a id="r_ae755e9c68b612b78b52b55faaf49cd0c"></a>

```c
bool in_progress
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[in_progress](#ae755e9c68b612b78b52b55faaf49cd0c)。

传输进行中标志（Transfer in progress flag）。

## 6.2\_详细说明（Detailed Documentation）

<a id="a2cc3ae3d23f9f5cfbfd5a1cebf4d1291"></a>

### `activation_irq`

```c
uint8_t dtc_transfer_status::activation_irq
```

激活 IRQ 编号。

<a id="ae755e9c68b612b78b52b55faaf49cd0c"></a>

### `in_progress`

```c
bool dtc_transfer_status::in_progress
```

传输进行中标志（Transfer in progress flag）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/misc/renesas_rx_dtc/renesas_rx_dtc.h`

## 6.3\_原页交叉引用（Cross References）

- [zephyr/drivers/misc/renesas_rx_dtc/renesas_rx_dtc.h](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_comp_nrf_lpcomp_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P007_dummy_api_结构体.md)
