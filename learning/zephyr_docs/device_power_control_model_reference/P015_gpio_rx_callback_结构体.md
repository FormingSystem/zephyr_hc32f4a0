---
id: learning.zephyr-docs.device-power-control-model-reference.page-15
title: gpio_rx_callback_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgpio__rx__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_gpio\_rx\_callback\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__rx__callback.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

外部RX GPIO中断（Interrupt）的回调配置。

```c
#include <zephyr/drivers/misc/renesas_rx_external_interrupt/renesas_rx_external_interrupt.h>
```

<a id="details"></a>

外部RX GPIO中断（Interrupt）的回调配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_a3d57065fd5dca68a35e33a1d8c195939"></a>

```c
struct device * port
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[port](#a3d57065fd5dca68a35e33a1d8c195939)。

GPIO 端口设备。

<a id="r_a46b0d0b6c5a088c8f142f222c1044327"></a>

```c
uint8_t port_num
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[port_num](#a46b0d0b6c5a088c8f142f222c1044327)。

端口索引编号。

<a id="r_ad2e07a69f97532116b893554b6841d52"></a>

```c
uint8_t pin
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pin](#ad2e07a69f97532116b893554b6841d52)。

引脚编号。

<a id="r_a7bbf270c50f0ac44dbf5a1a41773ad77"></a>

```c
enum gpio_int_trig trigger
```

相关声明：[gpio_int_trig](../hardware/P271_GPIO驱动后端.md#ga4ea6fd78423e6e3004702b599bc7b12d)、[trigger](#a7bbf270c50f0ac44dbf5a1a41773ad77)。

触发条件（Trigger condition）。

<a id="r_a325319906ec519a836a1025831d3ca9b"></a>

```c
enum gpio_int_mode mode
```

相关声明：[gpio_int_mode](../hardware/P271_GPIO驱动后端.md#ga82f0562c44cf0f76cc7e16d606a975db)、[mode](#a325319906ec519a836a1025831d3ca9b)。

中断模式配置。

<a id="r_aa15600e26b37674069c6d3c66aa60d4d"></a>

```c
void(* isr )(const struct device *dev, gpio_pin_t pin)
```

相关声明：[isr](#aa15600e26b37674069c6d3c66aa60d4d)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)、[pin](#ad2e07a69f97532116b893554b6841d52)。

中断服务例程（ISR）处理函数。

## 15.2\_详细说明（Detailed Documentation）

<a id="aa15600e26b37674069c6d3c66aa60d4d"></a>

### `isr`

```c
void(* gpio_rx_callback::isr) (const struct device *dev, gpio_pin_t pin)
```

中断服务例程（ISR）处理函数。

<a id="a325319906ec519a836a1025831d3ca9b"></a>

### `mode`

```c
enum gpio_int_mode gpio_rx_callback::mode
```

中断模式配置。

<a id="ad2e07a69f97532116b893554b6841d52"></a>

### `pin`

```c
uint8_t gpio_rx_callback::pin
```

引脚编号。

<a id="a3d57065fd5dca68a35e33a1d8c195939"></a>

### `port`

```c
struct device* gpio_rx_callback::port
```

GPIO 端口设备。

<a id="a46b0d0b6c5a088c8f142f222c1044327"></a>

### `port_num`

```c
uint8_t gpio_rx_callback::port_num
```

端口索引编号。

<a id="a7bbf270c50f0ac44dbf5a1a41773ad77"></a>

### `trigger`

```c
enum gpio_int_trig gpio_rx_callback::trigger
```

触发条件（Trigger condition）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/misc/renesas_rx_external_interrupt/renesas_rx_external_interrupt.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/drivers/misc/renesas_rx_external_interrupt/renesas_rx_external_interrupt.h](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__external__interrupt_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [gpio_int_trig](../hardware/P271_GPIO驱动后端.md#ga4ea6fd78423e6e3004702b599bc7b12d)
- [gpio_int_mode](../hardware/P271_GPIO驱动后端.md#ga82f0562c44cf0f76cc7e16d606a975db)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_gpio_ra_callback_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_gpio_tle9104_channel_diagnostics_结构体.md)
