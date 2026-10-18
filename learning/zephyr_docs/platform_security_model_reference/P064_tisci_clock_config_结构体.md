---
id: learning.zephyr-docs.platform-security-model-reference.page-64
title: tisci_clock_config_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtisci__clock__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_tisci\_clock\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtisci__clock__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

时钟配置结构（Clock Configuration Structure）。

```c
#include <zephyr/drivers/clock_control/tisci_clock_control.h>
```

<a id="details"></a>

时钟配置结构体（Clock configuration structure）。定义时钟配置，包括设备 ID 和时钟 ID。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 64.1\_数据成员（Data Fields）

<a id="r_a7c461d913c53bc5275419c250b0cb1b8"></a>

```c
uint32_t dev_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dev_id](#a7c461d913c53bc5275419c250b0cb1b8)。

与时钟关联的设备 ID。

<a id="r_a7746abef7a9d44b950aa8167a97e0e4b"></a>

```c
uint32_t clk_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_id](#a7746abef7a9d44b950aa8167a97e0e4b)。

设备内部的时钟 ID。

## 64.2\_详细说明（Detailed Documentation）

<a id="a7746abef7a9d44b950aa8167a97e0e4b"></a>

### `clk_id`

```c
uint32_t tisci_clock_config::clk_id
```

设备内部的时钟 ID。

<a id="a7c461d913c53bc5275419c250b0cb1b8"></a>

### `dev_id`

```c
uint32_t tisci_clock_config::dev_id
```

与时钟关联的设备 ID。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/tisci_clock_control.h`

## 64.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/tisci_clock_control.h](https://docs.zephyrproject.org/latest/doxygen/html/tisci__clock__control_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P063_tee_version_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P065_tisci_irq_release_req_结构体.md)
