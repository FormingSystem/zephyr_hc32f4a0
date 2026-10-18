---
id: learning.zephyr-docs.driver-model-reference.page-15
title: Atmel_SAM电源管理时钟配置
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structatmel__sam__pmc__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_Atmel\_SAM电源管理时钟配置

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structatmel__sam__pmc__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

单个外设时钟的电源管理控制器（Power Management Controller，PMC）时钟配置。

```c
#include <zephyr/drivers/clock_control/atmel_sam_pmc.h>
```

<a id="details"></a>

单个外设时钟的电源管理控制器（Power Management Controller，PMC）时钟配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_a8e2bbec7dd455159da3f469c6fb45635"></a>

```c
uint32_t clock_type
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clock_type](#a8e2bbec7dd455159da3f469c6fb45635)。

时钟类型，参见 `atmel_sam_pmc.h` 设备树绑定（DT Bindings）。

<a id="r_aab47279eb62b0d9fb6e097a935f09edd"></a>

```c
uint32_t peripheral_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[peripheral_id](#aab47279eb62b0d9fb6e097a935f09edd)。

PMC 内的外设标识符。

## 15.2\_详细说明（Detailed Documentation）

<a id="a8e2bbec7dd455159da3f469c6fb45635"></a>

### `clock_type`

```c
uint32_t atmel_sam_pmc_config::clock_type
```

时钟类型，参见 `atmel_sam_pmc.h` 设备树绑定（DT Bindings）。

<a id="aab47279eb62b0d9fb6e097a935f09edd"></a>

### `peripheral_id`

```c
uint32_t atmel_sam_pmc_config::peripheral_id
```

PMC 内的外设标识符。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/atmel_sam_pmc.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/atmel_sam_pmc.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2clock__control_2atmel__sam__pmc_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_Arm时钟控制.md) · [返回大纲](大纲.md) · [下一章](P016_音频编解码器配置.md)
