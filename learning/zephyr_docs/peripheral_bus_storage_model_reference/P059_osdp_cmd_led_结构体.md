---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-59
title: osdp_cmd_led_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd__led.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_osdp\_cmd\_led\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd__led.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

由控制面板（CP）发送至外设（PD），用于控制其板载LED的行为。

```c
#include <zephyr/mgmt/osdp.h>
```

<a id="details"></a>

由控制面板（CP）发送至外设（PD），用于控制其板载LED的行为。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 59.1\_数据成员（Data Fields）

<a id="r_afe5e061d91fda9f008b5f8e5441df467"></a>

```c
uint8_t reader
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reader](#afe5e061d91fda9f008b5f8e5441df467)。

读卡器编号（Reader number）。

<a id="r_ae4ff10389198d00047ffa2a7ec7d15ac"></a>

```c
uint8_t led_number
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[led_number](#ae4ff10389198d00047ffa2a7ec7d15ac)。

LED 编号。

<a id="r_a2130237d1b79ee36c5f5087cdec7acfb"></a>

```c
struct osdp_cmd_led_params temporary
```

相关声明：[osdp_cmd_led_params](P060_osdp_cmd_led_params_结构体.md)、[temporary](#a2130237d1b79ee36c5f5087cdec7acfb)。

临时 LED 状态描述符（Ephemeral status descriptor）。

<a id="r_a033fd34a88b03d22a088bd7d2676efb5"></a>

```c
struct osdp_cmd_led_params permanent
```

相关声明：[osdp_cmd_led_params](P060_osdp_cmd_led_params_结构体.md)、[permanent](#a033fd34a88b03d22a088bd7d2676efb5)。

永久 LED 状态描述符（Permanent status descriptor）。

## 59.2\_详细说明（Detailed Documentation）

<a id="ae4ff10389198d00047ffa2a7ec7d15ac"></a>

### `led_number`

```c
uint8_t osdp_cmd_led::led_number
```

LED 编号。

`0` 表示第一个 LED，`1` 表示第二个 LED，依此类推。

<a id="a033fd34a88b03d22a088bd7d2676efb5"></a>

### `permanent`

```c
struct osdp_cmd_led_params osdp_cmd_led::permanent
```

永久 LED 状态描述符（Permanent status descriptor）。

<a id="afe5e061d91fda9f008b5f8e5441df467"></a>

### `reader`

```c
uint8_t osdp_cmd_led::reader
```

读卡器编号（Reader number）。

`0` 表示第一个读卡器，`1` 表示第二个读卡器，依此类推。

<a id="a2130237d1b79ee36c5f5087cdec7acfb"></a>

### `temporary`

```c
struct osdp_cmd_led_params osdp_cmd_led::temporary
```

临时 LED 状态描述符（Ephemeral status descriptor）。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/osdp.h`

## 59.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/osdp.h](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [osdp_cmd_led_params](P060_osdp_cmd_led_params_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P058_osdp_cmd_keyset_结构体.md) · [返回大纲](大纲.md) · [下一章](P060_osdp_cmd_led_params_结构体.md)
