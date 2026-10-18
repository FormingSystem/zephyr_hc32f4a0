---
id: learning.zephyr-docs.api-file-audio-test-reference.page-8
title: zephyr__drivers__interrupt_controller__intc_mchp_eic_g1.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_mchp\_eic\_g1.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip eic g1外设的外部中断控制器（EIC）驱动头文件。

<a id="details"></a>

```c
#include <soc.h>
#include <zephyr/types.h>
#include <zephyr/drivers/gpio.h>
```

查看此文件的源码。

Microchip eic g1 外设的外部中断控制器驱动头文件（EIC Driver Header File）。可用它访问 EIC 驱动实现的 API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_eic_5Fconfig_5Fparams"></a>

```c
struct eic_config_params
```

相关声明：[eic_config_params](../platform_security_model_reference/P005_eic_config_params_结构体.md)。

为GPIO引脚配置Microchip外部中断控制器（EIC）线路的参数。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.2\_类型定义（Typedefs）

<a id="r_a710e45791e99d5f4e511923ea3d116fc"></a>

```c
typedef void(* mchp_eic_callback_t) (uint32_t pins, void *data)
```

相关声明：[mchp_eic_callback_t](#a710e45791e99d5f4e511923ea3d116fc)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

EIC 中断服务例程回调（ISR Callback），用于向 GPIO 层通知中断。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.3\_枚举（Enumerations）

<a id="r_a3a92a102ec5b77cf35016dae7cacf41f"></a>

```c
enum mchp_eic_trigger { MCHP_EIC_RISING = 1 , MCHP_EIC_FALLING , MCHP_EIC_BOTH , MCHP_EIC_HIGH , MCHP_EIC_LOW }
```

相关声明：[mchp_eic_trigger](#a3a92a102ec5b77cf35016dae7cacf41f)、[MCHP_EIC_RISING](#a3a92a102ec5b77cf35016dae7cacf41fa93d49c3438952c6d76d2cbb61477f496)、[MCHP_EIC_FALLING](#a3a92a102ec5b77cf35016dae7cacf41face8d3c3419e2ea54cd9b6ba9aa83bbf8)、[MCHP_EIC_BOTH](#a3a92a102ec5b77cf35016dae7cacf41fa76c21794771849ca27bfeae560393442)、[MCHP_EIC_HIGH](#a3a92a102ec5b77cf35016dae7cacf41fa0043919874fba56cfecf81b6af88c511)、[MCHP_EIC_LOW](#a3a92a102ec5b77cf35016dae7cacf41fa871bfb5c942a54250d8b03c0c5c9ed02)。

EIC 中断触发选择（Interrupt Trigger Selection）。

<a id="r_aec15300a23f1397ed93625d5418d3cc4"></a>

```c
enum mchp_gpio_port_id { MCHP_PORT_ID0 = 0 , MCHP_PORT_ID1 , MCHP_PORT_ID2 , MCHP_PORT_ID3 , MCHP_PORT_ID_MAX }
```

相关声明：[mchp_gpio_port_id](#aec15300a23f1397ed93625d5418d3cc4)、[MCHP_PORT_ID0](#aec15300a23f1397ed93625d5418d3cc4aab13ef018cd24524b971a61baacf25f3)、[MCHP_PORT_ID1](#aec15300a23f1397ed93625d5418d3cc4af49402c39ba9da1b0e0f7da49474c7a7)、[MCHP_PORT_ID2](#aec15300a23f1397ed93625d5418d3cc4aa7a9d95ee540de2dfbec299e0b7fddec)、[MCHP_PORT_ID3](#aec15300a23f1397ed93625d5418d3cc4abb7842e8dbb3a8a2e60d978172ca8fa8)、[MCHP_PORT_ID_MAX](#aec15300a23f1397ed93625d5418d3cc4a1053c0ce57a811b634c24e4f1342689f)。

Microchip GPIO 端口标识符（Port Identifiers）。

<a id="r_a43ecd6415e664dc6bda9c3374f86913f"></a>

```c
enum mchp_eic_line { EIC_LINE_0 = 0 , EIC_LINE_1 , EIC_LINE_2 , EIC_LINE_3 , EIC_LINE_4 , EIC_LINE_5 , EIC_LINE_6 , EIC_LINE_7 , EIC_LINE_8 , EIC_LINE_9 , EIC_LINE_10 , EIC_LINE_11 , EIC_LINE_12 , EIC_LINE_13 , EIC_LINE_14 , EIC_LINE_15 , EIC_LINE_MAX }
```

相关声明：[mchp_eic_line](#a43ecd6415e664dc6bda9c3374f86913f)、[EIC_LINE_0](#a43ecd6415e664dc6bda9c3374f86913fab0aa7cf6c7e4544caeed49f8f1370465)、[EIC_LINE_1](#a43ecd6415e664dc6bda9c3374f86913fa2a19ee62bd2238ed0b230128460eea0e)、[EIC_LINE_2](#a43ecd6415e664dc6bda9c3374f86913fa13a8e7a14cbb3eb0a29e4adb153fddf1)、[EIC_LINE_3](#a43ecd6415e664dc6bda9c3374f86913fa2480037d5320d82b51ef791602e86744)、[EIC_LINE_4](#a43ecd6415e664dc6bda9c3374f86913fab7107f342e53d5064cfcee8d791fbed8)、[EIC_LINE_5](#a43ecd6415e664dc6bda9c3374f86913fa3e3128f973a6b4e3c6c9ebff72214c27)、[EIC_LINE_6](#a43ecd6415e664dc6bda9c3374f86913fa478a0b1c6ea938e962c5b9847472dd51)、[EIC_LINE_7](#a43ecd6415e664dc6bda9c3374f86913fab447e3383e4b1bc48c53265c74b00d33)、[EIC_LINE_8](#a43ecd6415e664dc6bda9c3374f86913fab2da776e2843f1b4de58bb365e661baa)、[EIC_LINE_9](#a43ecd6415e664dc6bda9c3374f86913fab634c21298a333b2461b66f0169ec3bd)、[EIC_LINE_10](#a43ecd6415e664dc6bda9c3374f86913fa455d858d964458f84acd4710e0792f0b)、[EIC_LINE_11](#a43ecd6415e664dc6bda9c3374f86913fa4a4e98221146268888edd655465222c5)、[EIC_LINE_12](#a43ecd6415e664dc6bda9c3374f86913faa755a252e4d1b2c4aff1824dece02377)、[EIC_LINE_13](#a43ecd6415e664dc6bda9c3374f86913fadcef4e5bb50e89389a7a543bbab4c7fe)、[EIC_LINE_14](#a43ecd6415e664dc6bda9c3374f86913fa1b09c3dcf5e1e6bb4383d59d8d59139e)、[EIC_LINE_15](#a43ecd6415e664dc6bda9c3374f86913fa61d79f894d2a9099f0a1926d22e6dd29)、[EIC_LINE_MAX](#a43ecd6415e664dc6bda9c3374f86913fa9f26cc1a0ba03a5dc234704ca1009331)。

Microchip 外部中断控制器（External Interrupt Controller，EIC）线路标识符（Line Identifiers）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.4\_函数（Functions）

<a id="r_af05976a876021ebc3900a52209a49c00"></a>

```c
int eic_mchp_config_interrupt (struct eic_config_params *eic_pin_config)
```

相关声明：[eic_mchp_config_interrupt](#af05976a876021ebc3900a52209a49c00)、[eic_config_params](../platform_security_model_reference/P005_eic_config_params_结构体.md)。

为给定引脚配置并启用 EIC 中断（Interrupt）。

<a id="r_af2698011a2a1dfee017645dda7b72d0d"></a>

```c
uint32_t eic_mchp_interrupt_pending (uint8_t port_id)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[eic_mchp_interrupt_pending](#af2698011a2a1dfee017645dda7b72d0d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取给定端口的待处理中断（Pending EIC Interrupts）。

<a id="r_a9055a4d254b3d4c8cf2124b0459e8272"></a>

```c
int eic_mchp_disable_interrupt (struct eic_config_params *eic_pin_config)
```

相关声明：[eic_mchp_disable_interrupt](#a9055a4d254b3d4c8cf2124b0459e8272)、[eic_config_params](../platform_security_model_reference/P005_eic_config_params_结构体.md)。

禁用给定引脚配置对应的 EIC 中断（Interrupt）。

## 8.5\_详细说明（Detailed Documentation）

<a id="a710e45791e99d5f4e511923ea3d116fc"></a>

### `mchp_eic_callback_t`

```c
typedef void(* mchp_eic_callback_t) (uint32_t pins, void *data)
```

EIC 中断服务例程回调（ISR Callback），用于向 GPIO 层通知中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] pins` | 已触发 GPIO 引脚的位掩码（Bitmask），第 n 位对应引脚 n。 |
| `[in] data` | 与 GPIO 端口关联的用户／驱动上下文指针（Context Pointer）。 |

**说明（Note）**：注意（Note）：从中断上下文（Interrupt Context）调用。

<a id="a43ecd6415e664dc6bda9c3374f86913f"></a>

### `mchp_eic_line`

```c
enum mchp_eic_line
```

Microchip 外部中断控制器（External Interrupt Controller，EIC）线路标识符（Line Identifiers）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `EIC_LINE_0` | EIC 线路（Line）0。 |
| `EIC_LINE_1` | EIC 线路（Line）1。 |
| `EIC_LINE_2` | EIC 线路（Line）2。 |
| `EIC_LINE_3` | EIC 线路（Line）3。 |
| `EIC_LINE_4` | EIC 线路（Line）4。 |
| `EIC_LINE_5` | EIC 线路（Line）5。 |
| `EIC_LINE_6` | EIC 线路（Line）6。 |
| `EIC_LINE_7` | EIC 线路（Line）7。 |
| `EIC_LINE_8` | EIC 线路（Line）8。 |
| `EIC_LINE_9` | EIC 线路（Line）9。 |
| `EIC_LINE_10` | EIC 线路（Line）10。 |
| `EIC_LINE_11` | EIC 线路（Line）11。 |
| `EIC_LINE_12` | EIC 线路（Line）12。 |
| `EIC_LINE_13` | EIC 线路（Line）13。 |
| `EIC_LINE_14` | EIC 线路（Line）14。 |
| `EIC_LINE_15` | EIC 线路（Line）15。 |
| `EIC_LINE_MAX` | EIC 线路数量（Number of Lines），用作哨兵值（Sentinel）。 |

<a id="a3a92a102ec5b77cf35016dae7cacf41f"></a>

### `mchp_eic_trigger`

```c
enum mchp_eic_trigger
```

EIC 中断触发选择（Interrupt Trigger Selection）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MCHP_EIC_RISING` | 上升沿触发中断（Rising-edge Interrupt）。 |
| `MCHP_EIC_FALLING` | 下降沿触发中断（Falling-edge Interrupt）。 |
| `MCHP_EIC_BOTH` | 上升沿和下降沿均触发中断（Both-edge Interrupt）。 |
| `MCHP_EIC_HIGH` | 输入为高电平时触发中断（High-level Interrupt）。 |
| `MCHP_EIC_LOW` | 输入为低电平时触发中断（Low-level Interrupt）。 |

<a id="aec15300a23f1397ed93625d5418d3cc4"></a>

### `mchp_gpio_port_id`

```c
enum mchp_gpio_port_id
```

Microchip GPIO 端口标识符（Port Identifiers）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MCHP_PORT_ID0` | GPIO 端口（Port）0。 |
| `MCHP_PORT_ID1` | GPIO 端口（Port）1。 |
| `MCHP_PORT_ID2` | GPIO 端口（Port）2。 |
| `MCHP_PORT_ID3` | GPIO 端口（Port）3。 |
| `MCHP_PORT_ID_MAX` | 端口数量（Number of Ports），用作哨兵值（Sentinel）。 |

<a id="af05976a876021ebc3900a52209a49c00"></a>

### `eic_mchp_config_interrupt()`

```c
int eic_mchp_config_interrupt ( struct eic_config_params * eic_pin_config)
```

为给定引脚配置并启用 EIC 中断（Interrupt）。

此函数为指定引脚配置 EIC 中断，包括设置触发类型（Trigger Type）、启用输入、按需配置去抖（Debounce），并更新内部数据结构，以反映引脚到 EIC 线路的新分配关系。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `eic_pin_config` | 指向 EIC 引脚配置结构体（Pin Configuration Structure）的指针。 |

返回（Returns）：成功时为 0，失败时为负错误码；引脚没有可用 EIC 线路时为 -ENOTSUP，EIC 线路已在使用时为 -EBUSY。

<a id="a9055a4d254b3d4c8cf2124b0459e8272"></a>

### `eic_mchp_disable_interrupt()`

```c
int eic_mchp_disable_interrupt ( struct eic_config_params * eic_pin_config)
```

禁用给定引脚配置对应的 EIC 中断（Interrupt）。

此函数禁用与指定引脚配置关联的 EIC 中断。它检查引脚当前是否已分配到 EIC 线路；如果是，则禁用该中断线路，并更新内部数据结构，将线路标记为空闲（Free）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `eic_pin_config` | 指向 EIC 引脚配置结构体（Pin Configuration Structure）的指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="af2698011a2a1dfee017645dda7b72d0d"></a>

### `eic_mchp_interrupt_pending()`

```c
uint32_t eic_mchp_interrupt_pending ( uint8_t port_id)
```

获取给定端口的待处理中断（Pending EIC Interrupts）。

此函数检查指定端口中哪些引脚具有待处理的 EIC 中断（Pending Interrupts），返回位掩码，其中每个置位的位对应一个具有待处理中断的引脚。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port_id` | 要检查待处理中断（Pending Interrupts）的端口标识符。 |

返回（Returns）：表示端口中哪些引脚具有待处理中断的位掩码（Bitmask），返回值中每个置位的位都对应一个具有待处理中断的引脚编号。


## 8.6\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P396_intc_mchp_eic_g1.h_源码浏览.md)
- [eic_config_params](../platform_security_model_reference/P005_eic_config_params_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fab0aa7cf6c7e4544caeed49f8f1370465"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fa2a19ee62bd2238ed0b230128460eea0e"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fa13a8e7a14cbb3eb0a29e4adb153fddf1"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fa2480037d5320d82b51ef791602e86744"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fab7107f342e53d5064cfcee8d791fbed8"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fa3e3128f973a6b4e3c6c9ebff72214c27"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fa478a0b1c6ea938e962c5b9847472dd51"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fab447e3383e4b1bc48c53265c74b00d33"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fab2da776e2843f1b4de58bb365e661baa"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fab634c21298a333b2461b66f0169ec3bd"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fa455d858d964458f84acd4710e0792f0b"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fa4a4e98221146268888edd655465222c5"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913faa755a252e4d1b2c4aff1824dece02377"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fadcef4e5bb50e89389a7a543bbab4c7fe"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fa1b09c3dcf5e1e6bb4383d59d8d59139e"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fa61d79f894d2a9099f0a1926d22e6dd29"></a>
<a id="a43ecd6415e664dc6bda9c3374f86913fa9f26cc1a0ba03a5dc234704ca1009331"></a>
<a id="a3a92a102ec5b77cf35016dae7cacf41fa93d49c3438952c6d76d2cbb61477f496"></a>
<a id="a3a92a102ec5b77cf35016dae7cacf41face8d3c3419e2ea54cd9b6ba9aa83bbf8"></a>
<a id="a3a92a102ec5b77cf35016dae7cacf41fa76c21794771849ca27bfeae560393442"></a>
<a id="a3a92a102ec5b77cf35016dae7cacf41fa0043919874fba56cfecf81b6af88c511"></a>
<a id="a3a92a102ec5b77cf35016dae7cacf41fa871bfb5c942a54250d8b03c0c5c9ed02"></a>
<a id="aec15300a23f1397ed93625d5418d3cc4aab13ef018cd24524b971a61baacf25f3"></a>
<a id="aec15300a23f1397ed93625d5418d3cc4af49402c39ba9da1b0e0f7da49474c7a7"></a>
<a id="aec15300a23f1397ed93625d5418d3cc4aa7a9d95ee540de2dfbec299e0b7fddec"></a>
<a id="aec15300a23f1397ed93625d5418d3cc4abb7842e8dbb3a8a2e60d978172ca8fa8"></a>
<a id="aec15300a23f1397ed93625d5418d3cc4a1053c0ce57a811b634c24e4f1342689f"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_zephyr__net__ieee802154_radio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__dt-bindings__sensor__lis2dux12.h_文件参考.md)
