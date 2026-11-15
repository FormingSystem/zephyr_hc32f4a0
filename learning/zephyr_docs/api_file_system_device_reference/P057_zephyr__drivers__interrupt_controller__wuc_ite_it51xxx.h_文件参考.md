---
id: learning.zephyr-docs.api-file-system-device-reference.page-57
title: zephyr__drivers__interrupt_controller__wuc_ite_it51xxx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wuc__ite__it51xxx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_wuc\_ite\_it51xxx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/wuc__ite__it51xxx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 57.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 唤醒控制器标志（Wakeup Controller Flags）

<a id="r_a679ab1940f920cfe6c0fa1d5ed14a468"></a>

```c
#define WUC_TYPE_EDGE_RISING BIT(0)
```

相关声明：[WUC_TYPE_EDGE_RISING](#a679ab1940f920cfe6c0fa1d5ed14a468)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

唤醒控制器上升沿触发模式（WUC Rising Edge Trigger Mode）。

<a id="r_a21b4240f97f62e69f23ea614de699955"></a>

```c
#define WUC_TYPE_EDGE_FALLING BIT(1)
```

相关声明：[WUC_TYPE_EDGE_FALLING](#a21b4240f97f62e69f23ea614de699955)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

唤醒控制器下降沿触发模式（WUC Falling Edge Trigger Mode）。

<a id="r_a824c451f35efc9b287cd694a0c674095"></a>

```c
#define WUC_TYPE_EDGE_BOTH (WUC_TYPE_EDGE_RISING | WUC_TYPE_EDGE_FALLING)
```

相关声明：[WUC_TYPE_EDGE_BOTH](#a824c451f35efc9b287cd694a0c674095)、[WUC_TYPE_EDGE_RISING](#a679ab1940f920cfe6c0fa1d5ed14a468)、[WUC_TYPE_EDGE_FALLING](#a21b4240f97f62e69f23ea614de699955)。

唤醒控制器双边沿触发模式（WUC Both Edge Trigger Mode）。

<a id="r_ad8761c64e6c8463e679673269f719511"></a>

```c
#define WUC_TYPE_LEVEL_TRIG BIT(2)
```

相关声明：[WUC_TYPE_LEVEL_TRIG](#ad8761c64e6c8463e679673269f719511)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aca8e63896387e7119a4a3a021c920367"></a>

```c
#define WUC_TYPE_LEVEL_HIGH BIT(3)
```

相关声明：[WUC_TYPE_LEVEL_HIGH](#aca8e63896387e7119a4a3a021c920367)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

唤醒控制器（WUC）高电平触发模式。

<a id="r_a8f46aef09381a08af4bc4e88aff0fab3"></a>

```c
#define WUC_TYPE_LEVEL_LOW BIT(4)
```

相关声明：[WUC_TYPE_LEVEL_LOW](#a8f46aef09381a08af4bc4e88aff0fab3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

唤醒控制器（WUC）低电平触发模式。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 57.2\_函数（Functions）

<a id="r_a5bea830b4eda87d1eca9a110cf4de495"></a>

```c
void it51xxx_wuc_enable (const struct device *dev, uint8_t mask)
```

相关声明：[it51xxx_wuc_enable](#a5bea830b4eda87d1eca9a110cf4de495)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

对应输入上的触发条件（trigger condition）向嵌入式控制器（EC）的电源管理控制模块产生唤醒信号（wake-up signal）。

<a id="r_ab5e2a83d651b94b9e6dd376bc78c1781"></a>

```c
void it51xxx_wuc_disable (const struct device *dev, uint8_t mask)
```

相关声明：[it51xxx_wuc_disable](#ab5e2a83d651b94b9e6dd376bc78c1781)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

对应输入上的触发条件不会置位唤醒信号，信号已取消而非处于挂起状态（canceled, not pending）。

<a id="r_aac15ac209632efaf52b39dd7e95b364d"></a>

```c
void it51xxx_wuc_clear_status (const struct device *dev, uint8_t mask)
```

相关声明：[it51xxx_wuc_clear_status](#aac15ac209632efaf52b39dd7e95b364d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过写 1 清零（write-1-clear）清除对应输入上出现的触发条件。

<a id="r_a2a493db8a468803196e2eb64430527df"></a>

```c
void it51xxx_wuc_set_polarity (const struct device *dev, uint8_t mask, uint32_t flags)
```

相关声明：[it51xxx_wuc_set_polarity](#a2a493db8a468803196e2eb64430527df)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

选择对应输入的触发边沿模式（trigger edge mode）。

## 57.3\_详细说明（Detailed Documentation）

<a id="a824c451f35efc9b287cd694a0c674095"></a>

### `WUC_TYPE_EDGE_BOTH`

```c
#define WUC_TYPE_EDGE_BOTH (WUC_TYPE_EDGE_RISING | WUC_TYPE_EDGE_FALLING)
```

唤醒控制器双边沿触发模式（WUC Both Edge Trigger Mode）。

<a id="a21b4240f97f62e69f23ea614de699955"></a>

### `WUC_TYPE_EDGE_FALLING`

```c
#define WUC_TYPE_EDGE_FALLING BIT(1)
```

唤醒控制器下降沿触发模式（WUC Falling Edge Trigger Mode）。

<a id="a679ab1940f920cfe6c0fa1d5ed14a468"></a>

### `WUC_TYPE_EDGE_RISING`

```c
#define WUC_TYPE_EDGE_RISING BIT(0)
```

唤醒控制器上升沿触发模式（WUC Rising Edge Trigger Mode）。

<a id="aca8e63896387e7119a4a3a021c920367"></a>

### `WUC_TYPE_LEVEL_HIGH`

```c
#define WUC_TYPE_LEVEL_HIGH BIT(3)
```

唤醒控制器（WUC）高电平触发模式。

<a id="a8f46aef09381a08af4bc4e88aff0fab3"></a>

### `WUC_TYPE_LEVEL_LOW`

```c
#define WUC_TYPE_LEVEL_LOW BIT(4)
```

唤醒控制器（WUC）低电平触发模式。

<a id="ad8761c64e6c8463e679673269f719511"></a>

### `WUC_TYPE_LEVEL_TRIG`

```c
#define WUC_TYPE_LEVEL_TRIG BIT(2)
```

<a id="aac15ac209632efaf52b39dd7e95b364d"></a>

### `it51xxx_wuc_clear_status()`

```c
void it51xxx_wuc_clear_status ( const struct device * dev, uint8_t mask )
```

通过写 1 清零（write-1-clear）清除对应输入上出现的触发条件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `mask` | 唤醒控制器（WUC）组的引脚掩码（pin mask）。 |

<a id="ab5e2a83d651b94b9e6dd376bc78c1781"></a>

### `it51xxx_wuc_disable()`

```c
void it51xxx_wuc_disable ( const struct device * dev, uint8_t mask )
```

对应输入上的触发条件不会置位唤醒信号，信号已取消而非处于挂起状态（canceled, not pending）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `mask` | 唤醒控制器（WUC）组的引脚掩码（pin mask）。 |

<a id="a5bea830b4eda87d1eca9a110cf4de495"></a>

### `it51xxx_wuc_enable()`

```c
void it51xxx_wuc_enable ( const struct device * dev, uint8_t mask )
```

对应输入上的触发条件（trigger condition）向嵌入式控制器（EC）的电源管理控制模块产生唤醒信号（wake-up signal）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `mask` | 唤醒控制器（WUC）组的引脚掩码（pin mask）。 |

<a id="a2a493db8a468803196e2eb64430527df"></a>

### `it51xxx_wuc_set_polarity()`

```c
void it51xxx_wuc_set_polarity ( const struct device * dev, uint8_t mask, uint32_t flags )
```

选择对应输入的触发边沿模式（trigger edge mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `mask` | 唤醒控制器（WUC）组的引脚掩码（pin mask）。 |
| `flags` | 选择触发边沿模式。 |


## 57.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P928_wuc_ite_it51xxx.h_源码浏览.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P056_zephyr__dt-bindings__pwm__wisblock-pwm.h_文件参考.md) · [返回大纲](大纲.md)
