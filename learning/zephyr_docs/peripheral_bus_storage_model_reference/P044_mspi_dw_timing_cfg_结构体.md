---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-44
title: mspi_dw_timing_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__dw__timing__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_mspi\_dw\_timing\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__dw__timing__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Designware MSPI配置结构；调用mspi_timing_config时应将其传递给MSPI驱动。

```c
#include <zephyr/drivers/mspi/mspi_dw.h>
```

<a id="details"></a>

Designware MSPI配置结构；调用mspi_timing_config时应将其传递给MSPI驱动。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 44.1\_数据成员（Data Fields）

<a id="r_a2614dad76fd70ee93e0442b0f45a72ee"></a>

```c
uint32_t rx_sample_dly
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rx_sample_dly](#a2614dad76fd70ee93e0442b0f45a72ee)。

## 44.2\_详细说明（Detailed Documentation）

<a id="a2614dad76fd70ee93e0442b0f45a72ee"></a>

### `rx_sample_dly`

```c
uint32_t mspi_dw_timing_cfg::rx_sample_dly
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/mspi/mspi_dw.h`

## 44.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi/mspi_dw.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi__dw_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P043_mspi_dt_spec_结构体.md) · [返回大纲](大纲.md) · [下一章](P045_mspi_event_结构体.md)
