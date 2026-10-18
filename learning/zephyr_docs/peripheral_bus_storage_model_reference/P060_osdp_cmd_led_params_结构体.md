---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-60
title: osdp_cmd_led_params_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd__led__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_osdp\_cmd\_led\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd__led__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LED参数子结构（Parameters Sub-Structure）。

```c
#include <zephyr/mgmt/osdp.h>
```

<a id="details"></a>

LED 参数子结构体（Parameters sub-structure），属于 LED 命令的一部分。参见 `osdp_cmd_led`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 60.1\_数据成员（Data Fields）

<a id="r_ae95e3b87bbccd7d9897fef329001ce39"></a>

```c
uint8_t control_code
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[control_code](#ae95e3b87bbccd7d9897fef329001ce39)。

控制码（Control code）。

<a id="r_adde9dfdd167d9dfc122b56cf5e47b10f"></a>

```c
uint8_t on_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[on_count](#adde9dfdd167d9dfc122b56cf5e47b10f)。

闪烁过程中点亮（ON）的持续时间，以 100 ms 为单位。

<a id="r_a278ff380c2ab7d9c83b55aa49b3137cb"></a>

```c
uint8_t off_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[off_count](#a278ff380c2ab7d9c83b55aa49b3137cb)。

闪烁过程中熄灭（OFF）的持续时间，以 100 ms 为单位。

<a id="r_a80b47a4c55494d7062c4a83fd81b0910"></a>

```c
uint8_t on_color
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[on_color](#a80b47a4c55494d7062c4a83fd81b0910)。

点亮计时阶段设置的颜色，参见 `osdp_led_color_e`。

<a id="r_ac6f1c1269697fcab96b6f68d62381ded"></a>

```c
uint8_t off_color
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[off_color](#ac6f1c1269697fcab96b6f68d62381ded)。

熄灭计时阶段设置的颜色，参见 `osdp_led_color_e`。

<a id="r_a002de25cd5070cb96e90ccd0d2091216"></a>

```c
uint16_t timer_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timer_count](#a002de25cd5070cb96e90ccd0d2091216)。

时间，以 100 ms 为单位，仅适用于临时模式（Temporary mode）。

## 60.2\_详细说明（Detailed Documentation）

<a id="ae95e3b87bbccd7d9897fef329001ce39"></a>

### `control_code`

```c
uint8_t osdp_cmd_led_params::control_code
```

控制码（Control code）。

临时控制码（Temporary Control Code）：

- `0`：无操作（NOP），不改变此 LED 的临时设置。
- `1`：取消任何临时操作，立即显示此 LED 的永久状态。
- `2`：按给定值设置临时状态，并立即启动计时器。

永久控制码（Permanent Control Code）：

- `0`：无操作（NOP），不改变此 LED 的永久设置。
- `1`：按给定值设置永久状态。

<a id="ac6f1c1269697fcab96b6f68d62381ded"></a>

### `off_color`

```c
uint8_t osdp_cmd_led_params::off_color
```

熄灭计时阶段设置的颜色，参见 `osdp_led_color_e`。

<a id="a278ff380c2ab7d9c83b55aa49b3137cb"></a>

### `off_count`

```c
uint8_t osdp_cmd_led_params::off_count
```

闪烁过程中熄灭（OFF）的持续时间，以 100 ms 为单位。

<a id="a80b47a4c55494d7062c4a83fd81b0910"></a>

### `on_color`

```c
uint8_t osdp_cmd_led_params::on_color
```

点亮计时阶段设置的颜色，参见 `osdp_led_color_e`。

<a id="adde9dfdd167d9dfc122b56cf5e47b10f"></a>

### `on_count`

```c
uint8_t osdp_cmd_led_params::on_count
```

闪烁过程中点亮（ON）的持续时间，以 100 ms 为单位。

<a id="a002de25cd5070cb96e90ccd0d2091216"></a>

### `timer_count`

```c
uint16_t osdp_cmd_led_params::timer_count
```

时间，以 100 ms 为单位，仅适用于临时模式（Temporary mode）。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/osdp.h`

## 60.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/osdp.h](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [osdp_led_color_e](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h.html#a97ee0d8eb19e4e37ac89b2b6d338b84e)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [osdp_cmd_led](P059_osdp_cmd_led_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P059_osdp_cmd_led_结构体.md) · [返回大纲](大纲.md) · [下一章](P061_osdp_cmd_output_结构体.md)
