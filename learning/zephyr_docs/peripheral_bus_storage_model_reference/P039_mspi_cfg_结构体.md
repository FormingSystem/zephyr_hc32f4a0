---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-39
title: mspi_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_mspi\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI控制器配置（Controller Configuration）。

```c
#include <zephyr/drivers/mspi.h>
```

<a id="details"></a>

MSPI控制器配置（Controller Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 39.1\_数据成员（Data Fields）

<a id="r_af54bbbfbe07d88325117131fefe265ef"></a>

```c
uint8_t channel_num
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_num](#af54bbbfbe07d88325117131fefe265ef)。

MSPI 通道编号。

<a id="r_ab33e45d7802cf777a595d87058e8bfb5"></a>

```c
enum mspi_op_mode op_mode
```

相关声明：[mspi_op_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga3f211cd81e05cb9ee073a2722f6b22d8)、[op_mode](#ab33e45d7802cf777a595d87058e8bfb5)。

配置工作模式（Operation mode）。

<a id="r_a449894e0e58f96b775b4cc1c1eb83e77"></a>

```c
enum mspi_duplex duplex
```

相关声明：[mspi_duplex](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga20e348d7a9f1f9b32078a3bf6c4e82b9)、[duplex](#a449894e0e58f96b775b4cc1c1eb83e77)。

配置双工模式（Duplex mode）。

<a id="r_a2cf6e063074f86973cf03324637d656a"></a>

```c
bool dqs_support
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[dqs_support](#a2cf6e063074f86973cf03324637d656a)。

数据选通信号（DQS）支持标志。

<a id="r_a1192af56f714a42aa667a40e369b185e"></a>

```c
bool sw_multi_periph
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[sw_multi_periph](#a1192af56f714a42aa667a40e369b185e)。

是否启用软件管理的多外设功能。

<a id="r_a4053a398f6390e45ef6da385756f14bf"></a>

```c
struct gpio_dt_spec * ce_group
```

相关声明：[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)、[ce_group](#a4053a398f6390e45ef6da385756f14bf)。

GPIO 片选线，可选。

<a id="r_a20f6e453165b6ac22a42906604a3258a"></a>

```c
uint32_t num_ce_gpios
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[num_ce_gpios](#a20f6e453165b6ac22a42906604a3258a)。

GPIO 片选线编号，可选。

<a id="r_a6d24969046f175f158a5dae05e9284b1"></a>

```c
uint32_t num_periph
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[num_periph](#a6d24969046f175f158a5dae05e9284b1)。

外设编号，范围从 0 到主机控制器的外设数量限制。

<a id="r_a9a76198688b4acac9101274a71bfbf9c"></a>

```c
uint32_t max_freq
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_freq](#a9a76198688b4acac9101274a71bfbf9c)。

支持的最高频率，单位为 MHz。

<a id="r_afef0fe6991e28a4496e51333963fd3d1"></a>

```c
bool re_init
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[re_init](#afef0fe6991e28a4496e51333963fd3d1)。

是否重新初始化控制器。

## 39.2\_详细说明（Detailed Documentation）

<a id="a4053a398f6390e45ef6da385756f14bf"></a>

### `ce_group`

```c
struct gpio_dt_spec* mspi_cfg::ce_group
```

GPIO 片选线，可选。

<a id="af54bbbfbe07d88325117131fefe265ef"></a>

### `channel_num`

```c
uint8_t mspi_cfg::channel_num
```

MSPI 通道编号。

<a id="a2cf6e063074f86973cf03324637d656a"></a>

### `dqs_support`

```c
bool mspi_cfg::dqs_support
```

数据选通信号（DQS）支持标志。

<a id="a449894e0e58f96b775b4cc1c1eb83e77"></a>

### `duplex`

```c
enum mspi_duplex mspi_cfg::duplex
```

配置双工模式（Duplex mode）。

<a id="a9a76198688b4acac9101274a71bfbf9c"></a>

### `max_freq`

```c
uint32_t mspi_cfg::max_freq
```

支持的最高频率，单位为 MHz。

<a id="a20f6e453165b6ac22a42906604a3258a"></a>

### `num_ce_gpios`

```c
uint32_t mspi_cfg::num_ce_gpios
```

GPIO 片选线编号，可选。

<a id="a6d24969046f175f158a5dae05e9284b1"></a>

### `num_periph`

```c
uint32_t mspi_cfg::num_periph
```

外设编号，范围从 0 到主机控制器的外设数量限制。

<a id="ab33e45d7802cf777a595d87058e8bfb5"></a>

### `op_mode`

```c
enum mspi_op_mode mspi_cfg::op_mode
```

配置工作模式（Operation mode）。

<a id="afef0fe6991e28a4496e51333963fd3d1"></a>

### `re_init`

```c
bool mspi_cfg::re_init
```

是否重新初始化控制器。

<a id="a1192af56f714a42aa667a40e369b185e"></a>

### `sw_multi_periph`

```c
bool mspi_cfg::sw_multi_periph
```

是否启用软件管理的多外设功能。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mspi.h`

## 39.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mspi_op_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga3f211cd81e05cb9ee073a2722f6b22d8)
- [mspi_duplex](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga20e348d7a9f1f9b32078a3bf6c4e82b9)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P038_mspi_ce_control_结构体.md) · [返回大纲](大纲.md) · [下一章](P040_mspi_dev_cfg_结构体.md)
