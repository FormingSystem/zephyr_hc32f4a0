---
id: learning.zephyr-docs.device-power-control-model-reference.page-81
title: sam_sckc_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsam__sckc__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第81章\_sam\_sckc\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsam__sckc__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

慢时钟控制器（Slow Clock Controller，SCKC）的配置。

```c
#include <zephyr/drivers/clock_control/mchp_sam_pmc.h>
```

<a id="details"></a>

慢时钟控制器（Slow Clock Controller，SCKC）的配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 81.1\_数据成员（Data Fields）

<a id="r_a332b32859d73b961eb0f32f376390824"></a>

```c
uint32_t crystal_osc: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[crystal_osc](#a332b32859d73b961eb0f32f376390824)。

使用外部晶体振荡器代替 RC 振荡器。

<a id="r_a9a634b76cc127423dbfcb2b86435eb96"></a>

```c
uint32_t reserved: 31
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved](#a9a634b76cc127423dbfcb2b86435eb96)。

保留（Reserved）。

## 81.2\_详细说明（Detailed Documentation）

<a id="a332b32859d73b961eb0f32f376390824"></a>

### `crystal_osc`

```c
uint32_t sam_sckc_config::crystal_osc
```

使用外部晶体振荡器代替 RC 振荡器。

<a id="a9a634b76cc127423dbfcb2b86435eb96"></a>

### `reserved`

```c
uint32_t sam_sckc_config::reserved
```

保留（Reserved）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_sam_pmc.h`

## 81.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_sam_pmc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__pmc_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P080_sam_pmc_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P082_sbs_gauge_device_chemistry_结构体.md)
