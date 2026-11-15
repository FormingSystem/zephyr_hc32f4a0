---
id: learning.zephyr-docs.device-power-control-model-reference.page-14
title: gpio_ra_callback_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgpio__ra__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_gpio\_ra\_callback\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__ra__callback.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

外部RA GPIO中断（Interrupt）的回调配置。

```c
#include <zephyr/drivers/misc/renesas_ra_external_interrupt/renesas_ra_external_interrupt.h>
```

<a id="details"></a>

外部RA GPIO中断（Interrupt）的回调配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_ae2a5801c1a3f38dbb1c7b83fcf6373d5"></a>

```c
struct device * port
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[port](#ae2a5801c1a3f38dbb1c7b83fcf6373d5)。

GPIO 端口设备。

<a id="r_acb33518d1af46916fbbe0acd666b1bbc"></a>

```c
uint8_t port_num
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[port_num](#acb33518d1af46916fbbe0acd666b1bbc)。

端口索引编号。

<a id="r_a5e89aec076339fb4debe3a6b2041cf34"></a>

```c
uint8_t pin
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pin](#a5e89aec076339fb4debe3a6b2041cf34)。

引脚编号。

<a id="r_a78fde66020bebe07d34c63ade045d269"></a>

```c
enum gpio_int_trig trigger
```

相关声明：[gpio_int_trig](../hardware/P271_GPIO驱动后端.md#ga4ea6fd78423e6e3004702b599bc7b12d)、[trigger](#a78fde66020bebe07d34c63ade045d269)。

触发条件（Trigger condition）。

<a id="r_a5c89f78aba384aa8fcbef25ae48c3bcd"></a>

```c
enum gpio_int_mode mode
```

相关声明：[gpio_int_mode](../hardware/P271_GPIO驱动后端.md#ga82f0562c44cf0f76cc7e16d606a975db)、[mode](#a5c89f78aba384aa8fcbef25ae48c3bcd)。

中断模式配置。

<a id="r_afe6c9d43bf51368103f8210e13b6c550"></a>

```c
void(* isr )(const struct device *dev, gpio_pin_t pin)
```

相关声明：[isr](#afe6c9d43bf51368103f8210e13b6c550)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)、[pin](#a5e89aec076339fb4debe3a6b2041cf34)。

中断服务例程（ISR）处理函数。

## 14.2\_详细说明（Detailed Documentation）

<a id="afe6c9d43bf51368103f8210e13b6c550"></a>

### `isr`

```c
void(* gpio_ra_callback::isr) (const struct device *dev, gpio_pin_t pin)
```

中断服务例程（ISR）处理函数。

<a id="a5c89f78aba384aa8fcbef25ae48c3bcd"></a>

### `mode`

```c
enum gpio_int_mode gpio_ra_callback::mode
```

中断模式配置。

<a id="a5e89aec076339fb4debe3a6b2041cf34"></a>

### `pin`

```c
uint8_t gpio_ra_callback::pin
```

引脚编号。

<a id="ae2a5801c1a3f38dbb1c7b83fcf6373d5"></a>

### `port`

```c
struct device* gpio_ra_callback::port
```

GPIO 端口设备。

<a id="acb33518d1af46916fbbe0acd666b1bbc"></a>

### `port_num`

```c
uint8_t gpio_ra_callback::port_num
```

端口索引编号。

<a id="a78fde66020bebe07d34c63ade045d269"></a>

### `trigger`

```c
enum gpio_int_trig gpio_ra_callback::trigger
```

触发条件（Trigger condition）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/misc/renesas_ra_external_interrupt/renesas_ra_external_interrupt.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/drivers/misc/renesas_ra_external_interrupt/renesas_ra_external_interrupt.h](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__external__interrupt_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [gpio_int_trig](../hardware/P271_GPIO驱动后端.md#ga4ea6fd78423e6e3004702b599bc7b12d)
- [gpio_int_mode](../hardware/P271_GPIO驱动后端.md#ga82f0562c44cf0f76cc7e16d606a975db)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_gpio_cmsdk_ahb_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_gpio_rx_callback_结构体.md)
