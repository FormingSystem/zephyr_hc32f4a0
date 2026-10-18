---
id: learning.zephyr-docs.audio-video-model-reference.page-49
title: uaol_config_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuaol__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_uaol\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structuaol__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB音频卸载链路（UAOL）的流配置数据。

```c
#include <zephyr/drivers/uaol.h>
```

<a id="details"></a>

USB音频卸载链路（UAOL）的流配置数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 49.1\_数据成员（Data Fields）

<a id="r_ab4e1601f84eb1d2a2e741b99dd157dc4"></a>

```c
uint8_t xhci_bus
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[xhci_bus](#ab4e1601f84eb1d2a2e741b99dd157dc4)。

xHCI 控制器的总线（bus）编号。

<a id="r_abf3c127ea505f9d8e877fc5e6adc320a"></a>

```c
uint8_t xhci_device
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[xhci_device](#abf3c127ea505f9d8e877fc5e6adc320a)。

xHCI 控制器的设备（device）编号。

<a id="r_aaacde851401667b86919604e592ac417"></a>

```c
uint8_t xhci_function
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[xhci_function](#aaacde851401667b86919604e592ac417)。

xHCI 控制器的功能（function）编号。

<a id="r_a1339eb8254650486eaef38d6723555fb"></a>

```c
uint16_t art_divider_m
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[art_divider_m](#a1339eb8254650486eaef38d6723555fb)。

USB ART 分频器的乘数值。

<a id="r_ab85e93022ffde5f65b30c67d2ff0c082"></a>

```c
uint16_t art_divider_n
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[art_divider_n](#ab85e93022ffde5f65b30c67d2ff0c082)。

USB ART 分频器的除数值。

<a id="r_a46bb8d4d8abb45c5a0880a7c54a20570"></a>

```c
uint32_t sample_rate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[sample_rate](#a46bb8d4d8abb45c5a0880a7c54a20570)。

音频采样率，单位为帧/秒。

<a id="r_a9e0b745c13341828e542710bacb7b0d9"></a>

```c
uint32_t channels
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[channels](#a9e0b745c13341828e542710bacb7b0d9)。

音频通道数量。

<a id="r_ae08eb150aef59a2fc373021e2b5c79f6"></a>

```c
uint32_t sample_bits
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[sample_bits](#ae08eb150aef59a2fc373021e2b5c79f6)。

音频采样容器（sample container）的大小，单位为位。

<a id="r_af9d87bfb5f1ba99b1ad59f19fa0edc90"></a>

```c
uint32_t service_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[service_interval](#af9d87bfb5f1ba99b1ad59f19fa0edc90)。

PCM 流操作的服务间隔（service interval），单位为微秒。

<a id="r_a7be4b2a7f215424a2a7fe19f7242c6ef"></a>

```c
uint32_t sio_credit_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[sio_credit_size](#a7be4b2a7f215424a2a7fe19f7242c6ef)。

SIO 信用包（credit packet）大小，单位为字节。

<a id="r_a766781a2e8d45094ec12431ddbc89870"></a>

```c
uint16_t fifo_start_offset
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[fifo_start_offset](#a766781a2e8d45094ec12431ddbc89870)。

UAOL FIFO 起始地址偏移量。

<a id="r_ae7d46d04d57ad186ddb5875f336037b3"></a>

```c
uint16_t channel_map
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[channel_map](#ae7d46d04d57ad186ddb5875f336037b3)。

UAOL FIFO 的 HDA 链路流与通道映射。

<a id="r_a32f0a6ea54d32ffd51b4bfacb0cbcd4b"></a>

```c
enum uaol_direction direction
```

相关声明：[uaol_direction](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h.html#afeaa6e0eee46713a5161fd2873ed58be)、[direction](#a32f0a6ea54d32ffd51b4bfacb0cbcd4b)。

USB 流或端点的方向。

## 49.2\_详细说明（Detailed Documentation）

<a id="a1339eb8254650486eaef38d6723555fb"></a>

### `art_divider_m`

```c
uint16_t uaol_config::art_divider_m
```

USB ART 分频器的乘数值。

<a id="ab85e93022ffde5f65b30c67d2ff0c082"></a>

### `art_divider_n`

```c
uint16_t uaol_config::art_divider_n
```

USB ART 分频器的除数值。

<a id="ae7d46d04d57ad186ddb5875f336037b3"></a>

### `channel_map`

```c
uint16_t uaol_config::channel_map
```

UAOL FIFO 的 HDA 链路流与通道映射。

<a id="a9e0b745c13341828e542710bacb7b0d9"></a>

### `channels`

```c
uint32_t uaol_config::channels
```

音频通道数量。

<a id="a32f0a6ea54d32ffd51b4bfacb0cbcd4b"></a>

### `direction`

```c
enum uaol_direction uaol_config::direction
```

USB 流或端点的方向。

<a id="a766781a2e8d45094ec12431ddbc89870"></a>

### `fifo_start_offset`

```c
uint16_t uaol_config::fifo_start_offset
```

UAOL FIFO 起始地址偏移量。

<a id="ae08eb150aef59a2fc373021e2b5c79f6"></a>

### `sample_bits`

```c
uint32_t uaol_config::sample_bits
```

音频采样容器（sample container）的大小，单位为位。

<a id="a46bb8d4d8abb45c5a0880a7c54a20570"></a>

### `sample_rate`

```c
uint32_t uaol_config::sample_rate
```

音频采样率，单位为帧/秒。

<a id="af9d87bfb5f1ba99b1ad59f19fa0edc90"></a>

### `service_interval`

```c
uint32_t uaol_config::service_interval
```

PCM 流操作的服务间隔（service interval），单位为微秒。

<a id="a7be4b2a7f215424a2a7fe19f7242c6ef"></a>

### `sio_credit_size`

```c
uint32_t uaol_config::sio_credit_size
```

SIO 信用包（credit packet）大小，单位为字节。

<a id="ab4e1601f84eb1d2a2e741b99dd157dc4"></a>

### `xhci_bus`

```c
uint8_t uaol_config::xhci_bus
```

xHCI 控制器的总线（bus）编号。

<a id="abf3c127ea505f9d8e877fc5e6adc320a"></a>

### `xhci_device`

```c
uint8_t uaol_config::xhci_device
```

xHCI 控制器的设备（device）编号。

<a id="aaacde851401667b86919604e592ac417"></a>

### `xhci_function`

```c
uint8_t uaol_config::xhci_function
```

xHCI 控制器的功能（function）编号。

本数据类型文档由以下文件生成：

- `zephyr/drivers/uaol.h`

## 49.3\_原页交叉引用（Cross References）

- [zephyr/drivers/uaol.h](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uaol_direction](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h.html#afeaa6e0eee46713a5161fd2873ed58be)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P048_uaol_capabilities_结构体.md) · [返回大纲](大纲.md) · [下一章](P050_uaol_ep_table_entry_结构体.md)
