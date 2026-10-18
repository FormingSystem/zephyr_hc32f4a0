---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-36
title: mspi_cadence_timing_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__cadence__timing__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_mspi\_cadence\_timing\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__cadence__timing__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TI K3 MSPI外设的时序配置（Timing Configuration）。

```c
#include <zephyr/drivers/mspi/mspi_cadence.h>
```

<a id="details"></a>

TI K3 MSPI外设的时序配置（Timing Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 36.1\_数据成员（Data Fields）

<a id="r_af0f7347dcd065484df7e9b2f079f61e4"></a>

```c
uint8_t rd_delay
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rd_delay](#af0f7347dcd065484df7e9b2f079f61e4)。

应用于内部数据捕获电路的读取数据捕获周期数（Read data capture cycles）。

## 36.2\_详细说明（Detailed Documentation）

<a id="af0f7347dcd065484df7e9b2f079f61e4"></a>

### `rd_delay`

```c
uint8_t mspi_cadence_timing_cfg::rd_delay
```

应用于内部数据捕获电路的读取数据捕获周期数（Read data capture cycles）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mspi/mspi_cadence.h`

## 36.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi/mspi_cadence.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi__cadence_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P035_mmc_ext_csd_结构体.md) · [返回大纲](大纲.md) · [下一章](P037_mspi_callback_context_结构体.md)
