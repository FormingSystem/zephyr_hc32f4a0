---
id: learning.zephyr-docs.api-file-service-reference.page-46
title: zephyr__drivers__misc__renesas_rx_external_interrupt__renesas_rx_external_interrupt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__external__interrupt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_zephyr\_\_drivers\_\_misc\_\_renesas\_rx\_external\_interrupt\_\_renesas\_rx\_external\_interrupt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__external__interrupt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RX外部中断（External Interrupt）的接口。

<a id="details"></a>

```c
#include <zephyr/drivers/gpio.h>
```

查看此文件的源码。

Renesas RX外部中断（External Interrupt）的接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 46.1\_数据结构（Data Structures）

<a id="r_gpio_5Frx_5Fcallback"></a>

```c
struct gpio_rx_callback
```

相关声明：[gpio_rx_callback](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md)。

外部RX GPIO中断（Interrupt）的回调配置。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 46.2\_函数（Functions）

<a id="func-members-0"></a>

<a id="r_aaee6debb5a530f1202bf04f05be3ba98"></a>

```c
int gpio_rx_interrupt_set (const struct device *dev, struct gpio_rx_callback *callback)
```

相关声明：[gpio_rx_interrupt_set](#aaee6debb5a530f1202bf04f05be3ba98)、[device](../device_reference/P002_设备对象结构.md)、[gpio_rx_callback](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md)。

配置并启用 RX 外部中断（External Interrupt）。

<a id="r_aa4e8687d852850bd1ace1fafba911bce"></a>

```c
void gpio_rx_interrupt_unset (const struct device *dev, uint8_t port_num, uint8_t pin)
```

相关声明：[gpio_rx_interrupt_unset](#aa4e8687d852850bd1ace1fafba911bce)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

禁用 RX 外部中断（External Interrupt）。

## 46.3\_详细说明（Detailed Documentation）

<a id="aaee6debb5a530f1202bf04f05be3ba98"></a>

### `gpio_rx_interrupt_set()`

```c
int gpio_rx_interrupt_set ( const struct device * dev, struct gpio_rx_callback * callback )
```

配置并启用 RX 外部中断（External Interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | RX 外部中断设备实例（External Interrupt Device Instance）。 |
| `callback` | 指向回调配置（Callback Configuration）的指针（Pointer）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="aa4e8687d852850bd1ace1fafba911bce"></a>

### `gpio_rx_interrupt_unset()`

```c
void gpio_rx_interrupt_unset ( const struct device * dev, uint8_t port_num, uint8_t pin )
```

禁用 RX 外部中断（External Interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | RX 外部中断设备实例（External Interrupt Device Instance）。 |
| `port_num` | 端口索引。 |
| `pin` | 引脚编号。 |


## 46.4\_原页交叉引用（Cross References）

- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P712_renesas_rx_external_interrupt.h_源码浏览.md)
- [gpio_rx_callback](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P045_zephyr__drivers__misc__renesas_ra_external_interrupt__renesas_ra_external_interrupt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P047_zephyr__dt-bindings__pinctrl__rv32m1-pinctrl.h_文件参考.md)
