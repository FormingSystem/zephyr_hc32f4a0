---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-94
title: swdp_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structswdp__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第94章\_swdp\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structswdp__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

串行线调试端口（Serial Wire Debug Port，SWDP）的驱动API。

```c
#include <zephyr/drivers/swdp.h>
```

<a id="details"></a>

串行线调试端口（Serial Wire Debug Port，SWDP）驱动 API。这是每个 SWDP 驱动都必须提供的 API。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 94.1\_数据成员（Data Fields）

<a id="r_a4a4e268bc2e80b0fa3af76c8fb6d70c7"></a>

```c
int(* swdp_output_sequence )(const struct device *dev, uint32_t count, const uint8_t *data)
```

相关声明：[swdp_output_sequence](#a4a4e268bc2e80b0fa3af76c8fb6d70c7)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 `data` 中的 `count` 位写入 SWDIO，最低有效位优先（LSB first）。

<a id="r_a0480ec7f5479382457ac2e9c264e46f4"></a>

```c
int(* swdp_input_sequence )(const struct device *dev, uint32_t count, uint8_t *data)
```

相关声明：[swdp_input_sequence](#a0480ec7f5479382457ac2e9c264e46f4)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 SWDIO 读取 `count` 位到 `data`，最低有效位优先（LSB first）。

<a id="r_a3b2a89ee837aae3731ba0d2ba8c1c323"></a>

```c
int(* swdp_transfer )(const struct device *dev, uint8_t request, uint32_t *data, uint8_t idle_cycles, uint8_t *response)
```

相关声明：[swdp_transfer](#a3b2a89ee837aae3731ba0d2ba8c1c323)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SWDP 传输并存储响应。

<a id="r_af83ae99fb199d5506256c13aec92f1a7"></a>

```c
int(* swdp_set_pins )(const struct device *dev, uint8_t pins, uint8_t value)
```

相关声明：[swdp_set_pins](#af83ae99fb199d5506256c13aec92f1a7)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 `SWCLK`、`SWDPIO` 和 `nRESET` 引脚状态。

<a id="r_ac0e08f227a18d087fa98894caa277282"></a>

```c
int(* swdp_get_pins )(const struct device *dev, uint8_t *state)
```

相关声明：[swdp_get_pins](#ac0e08f227a18d087fa98894caa277282)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

获取 `SWCLK`、`SWDPIO` 和 `nRESET` 引脚状态。

<a id="r_aba201f47bb6037334b3da19d17ea7349"></a>

```c
int(* swdp_set_clock )(const struct device *dev, uint32_t clock)
```

相关声明：[swdp_set_clock](#aba201f47bb6037334b3da19d17ea7349)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

设置 SWDP 时钟频率。

<a id="r_a62b5b2285bdec6d9e6069f1671ad1bc3"></a>

```c
int(* swdp_configure )(const struct device *dev, uint8_t turnaround, bool data_phase)
```

相关声明：[swdp_configure](#a62b5b2285bdec6d9e6069f1671ad1bc3)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

配置 SWDP 接口。

<a id="r_a642cd297ace3437669be092ca4061911"></a>

```c
int(* swdp_port_on )(const struct device *dev)
```

相关声明：[swdp_port_on](#a642cd297ace3437669be092ca4061911)、[device](../device_reference/P002_设备对象结构.md)。

启用接口，并将引脚设置为默认状态。

<a id="r_aa7e408b542b1bd9134b86f2a257cf004"></a>

```c
int(* swdp_port_off )(const struct device *dev)
```

相关声明：[swdp_port_off](#aa7e408b542b1bd9134b86f2a257cf004)、[device](../device_reference/P002_设备对象结构.md)。

禁用接口，并将引脚设置为高阻态（High-Z）。

## 94.2\_详细说明（Detailed Documentation）

<a id="a62b5b2285bdec6d9e6069f1671ad1bc3"></a>

### `swdp_configure`

```c
int(* swdp_api::swdp_configure) (const struct device *dev, uint8_t turnaround, bool data_phase)
```

配置 SWDP 接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |
| `turnaround` | 线路方向切换周期数（Line turnaround cycles）。 |
| `data_phase` | 始终生成数据阶段（Data Phase），包括收到 `WAIT`/`FAULT` 时。 |

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="ac0e08f227a18d087fa98894caa277282"></a>

### `swdp_get_pins`

```c
int(* swdp_api::swdp_get_pins) (const struct device *dev, uint8_t *state)
```

获取 `SWCLK`、`SWDPIO` 和 `nRESET` 引脚状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |
| `state` | 用于存储引脚状态的位置。 |

**说明（Note）**：注意：位位置由 `SWDP_*_PIN` 宏定义。

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="a0480ec7f5479382457ac2e9c264e46f4"></a>

### `swdp_input_sequence`

```c
int(* swdp_api::swdp_input_sequence) (const struct device *dev, uint32_t count, uint8_t *data)
```

从 SWDIO 读取 `count` 位到 `data`，最低有效位优先（LSB first）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |
| `count` | 要读取的位数。 |
| `data` | 存储已读位的缓冲区。 |

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="a4a4e268bc2e80b0fa3af76c8fb6d70c7"></a>

### `swdp_output_sequence`

```c
int(* swdp_api::swdp_output_sequence) (const struct device *dev, uint32_t count, const uint8_t *data)
```

将 `data` 中的 `count` 位写入 SWDIO，最低有效位优先（LSB first）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |
| `count` | 要写入的位数。 |
| `data` | 要写入的位。 |

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="aa7e408b542b1bd9134b86f2a257cf004"></a>

### `swdp_port_off`

```c
int(* swdp_api::swdp_port_off) (const struct device *dev)
```

禁用接口，并将引脚设置为高阻态（High-Z）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="a642cd297ace3437669be092ca4061911"></a>

### `swdp_port_on`

```c
int(* swdp_api::swdp_port_on) (const struct device *dev)
```

启用接口，并将引脚设置为默认状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |

**说明（Note）**：注意：将 `SWDPIO` 设为输出模式，将 `SWCLK` 和 `nRESET` 设为高电平。

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="aba201f47bb6037334b3da19d17ea7349"></a>

### `swdp_set_clock`

```c
int(* swdp_api::swdp_set_clock) (const struct device *dev, uint32_t clock)
```

设置 SWDP 时钟频率。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |
| `clock` | 时钟频率，单位为 Hz。 |

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="af83ae99fb199d5506256c13aec92f1a7"></a>

### `swdp_set_pins`

```c
int(* swdp_api::swdp_set_pins) (const struct device *dev, uint8_t pins, uint8_t value)
```

设置 `SWCLK`、`SWDPIO` 和 `nRESET` 引脚状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |
| `pins` | 待设置引脚的位掩码（Bitmask）。 |
| `value` | 要将引脚设置为的值。 |

**说明（Note）**：注意：位位置由 `SWDP_*_PIN` 宏定义。

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="a3b2a89ee837aae3731ba0d2ba8c1c323"></a>

### `swdp_transfer`

```c
int(* swdp_api::swdp_transfer) (const struct device *dev, uint8_t request, uint32_t *data, uint8_t idle_cycles, uint8_t *response)
```

执行 SWDP 传输并存储响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |
| `request` | SWDP 请求位（Request bits）。 |
| `data` | 与请求一同传输的数据。 |
| `idle_cycles` | 请求与响应之间的空闲周期数（Idle cycles）。 |
| `response` | 用于存储响应（`ACK`/`WAIT`/`FAULT`）的缓冲区。 |

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

本数据类型文档由以下文件生成：

- `zephyr/drivers/swdp.h`

## 94.3\_原页交叉引用（Cross References）

- [zephyr/drivers/swdp.h](https://docs.zephyrproject.org/latest/doxygen/html/swdp_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P093_smbus_dt_spec_结构体.md) · [返回大纲](大纲.md) · [下一章](P095_w1_driver_api_结构体.md)
