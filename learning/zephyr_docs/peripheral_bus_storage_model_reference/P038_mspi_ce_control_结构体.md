---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-38
title: mspi_ce_control_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__ce__control.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_mspi\_ce\_control\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__ce__control.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI片选（Chip Select）的控制结构。

```c
#include <zephyr/drivers/mspi.h>
```

<a id="details"></a>

MSPI 片选控制结构体（Chip Select control structure）。可通过 GPIO 引脚控制片选使能（CE）线，替代控制器内部的 CE 逻辑。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.1\_数据成员（Data Fields）

<a id="r_a1f1b6f5583abc08c8c7fae95e1a29a7a"></a>

```c
struct gpio_dt_spec gpio
```

相关声明：[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)、[gpio](#a1f1b6f5583abc08c8c7fae95e1a29a7a)。

CE GPIO 的 GPIO 设备树规格（Devicetree specification）。

<a id="r_abc3e35be0b7b3f5c118b0d16033125ba"></a>

```c
uint32_t delay
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[delay](#abc3e35be0b7b3f5c118b0d16033125ba)。

需要等待的延迟。

## 38.2\_详细说明（Detailed Documentation）

<a id="abc3e35be0b7b3f5c118b0d16033125ba"></a>

### `delay`

```c
uint32_t mspi_ce_control::delay
```

需要等待的延迟。

在开始传输前和释放 CE 线前等待的时间，单位为微秒。

<a id="a1f1b6f5583abc08c8c7fae95e1a29a7a"></a>

### `gpio`

```c
struct gpio_dt_spec mspi_ce_control::gpio
```

CE GPIO 的 GPIO 设备树规格（Devicetree specification）。

必要时可将设备指针设为 `NULL`，以完全禁止 CE 控制。GPIO 标志 `GPIO_ACTIVE_LOW`/`GPIO_ACTIVE_HIGH` 应与 MSPI 配置一致。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mspi.h`

## 38.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_mspi_callback_context_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_mspi_cfg_结构体.md)
