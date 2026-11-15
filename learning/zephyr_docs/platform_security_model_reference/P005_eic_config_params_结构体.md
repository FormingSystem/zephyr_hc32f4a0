---
id: learning.zephyr-docs.platform-security-model-reference.page-5
title: eic_config_params_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structeic__config__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_eic\_config\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structeic__config__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

为GPIO引脚配置Microchip外部中断控制器（EIC）线路的参数。

```c
#include <zephyr/drivers/interrupt_controller/intc_mchp_eic_g1.h>
```

<a id="details"></a>

为GPIO引脚配置Microchip外部中断控制器（EIC）线路的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_add7f563e55292364350b66cbb47f1f21"></a>

```c
enum mchp_eic_trigger trig_type
```

相关声明：[mchp_eic_trigger](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a3a92a102ec5b77cf35016dae7cacf41f)、[trig_type](#add7f563e55292364350b66cbb47f1f21)。

外部中断控制器（EIC）线路的触发类型：边沿或电平（edge/level）。

<a id="r_a44492d0b42ea6ccd0545726467ca82aa"></a>

```c
uint8_t pin_num
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pin_num](#a44492d0b42ea6ccd0545726467ca82aa)。

GPIO 引脚在端口内的编号。

<a id="r_a29d70eaee32a2835f5514e7ce168ec14"></a>

```c
uint8_t port_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[port_id](#a29d70eaee32a2835f5514e7ce168ec14)。

GPIO 端口标识符。

<a id="r_a9de61236e03ae6fff8a111dcd1a30497"></a>

```c
bool debounce
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[debounce](#a9de61236e03ae6fff8a111dcd1a30497)。

启用或禁用此线路的输入去抖（debouncing）。

<a id="r_ab7422775ca216017cbb74444bd1df6a4"></a>

```c
void * gpio_data
```

相关声明：[gpio_data](#ab7422775ca216017cbb74444bd1df6a4)。

指向 GPIO 驱动或用户上下文的指针，会通过回调传回。

<a id="r_a9f5b10cb7dc39d11c263e7e88e583ac6"></a>

```c
port_group_registers_t * port_addr
```

相关声明：[port_addr](#a9f5b10cb7dc39d11c263e7e88e583ac6)。

GPIO 端口寄存器的基地址。

<a id="r_a95858dedfde317eb8f70d15567a75ee6"></a>

```c
mchp_eic_callback_t eic_line_callback
```

相关声明：[mchp_eic_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a710e45791e99d5f4e511923ea3d116fc)、[eic_line_callback](#a95858dedfde317eb8f70d15567a75ee6)。

从 EIC 中断服务例程（ISR）调用的回调，用于通知 GPIO 层。

## 5.2\_详细说明（Detailed Documentation）

<a id="a9de61236e03ae6fff8a111dcd1a30497"></a>

### `debounce`

```c
bool eic_config_params::debounce
```

启用或禁用此线路的输入去抖（debouncing）。

<a id="a95858dedfde317eb8f70d15567a75ee6"></a>

### `eic_line_callback`

```c
mchp_eic_callback_t eic_config_params::eic_line_callback
```

从 EIC 中断服务例程（ISR）调用的回调，用于通知 GPIO 层。

<a id="ab7422775ca216017cbb74444bd1df6a4"></a>

### `gpio_data`

```c
void* eic_config_params::gpio_data
```

指向 GPIO 驱动或用户上下文的指针，会通过回调传回。

<a id="a44492d0b42ea6ccd0545726467ca82aa"></a>

### `pin_num`

```c
uint8_t eic_config_params::pin_num
```

GPIO 引脚在端口内的编号。

<a id="a9f5b10cb7dc39d11c263e7e88e583ac6"></a>

### `port_addr`

```c
port_group_registers_t* eic_config_params::port_addr
```

GPIO 端口寄存器的基地址。

<a id="a29d70eaee32a2835f5514e7ce168ec14"></a>

### `port_id`

```c
uint8_t eic_config_params::port_id
```

GPIO 端口标识符。

<a id="add7f563e55292364350b66cbb47f1f21"></a>

### `trig_type`

```c
enum mchp_eic_trigger eic_config_params::trig_type
```

外部中断控制器（EIC）线路的触发类型：边沿或电平（edge/level）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/interrupt_controller/intc_mchp_eic_g1.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/drivers/interrupt_controller/intc_mchp_eic_g1.h](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h_source.html)
- [mchp_eic_trigger](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a3a92a102ec5b77cf35016dae7cacf41f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [mchp_eic_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a710e45791e99d5f4e511923ea3d116fc)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_edac_synopsys_callback_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_fido2_attestation_result_结构体.md)
