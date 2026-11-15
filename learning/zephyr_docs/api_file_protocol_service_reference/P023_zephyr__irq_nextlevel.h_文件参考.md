---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-23
title: zephyr__irq_nextlevel.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/irq__nextlevel_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_irq\_nextlevel.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/irq__nextlevel_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

中断配置（Configuring Interrupts）的公共接口。

查看此文件的源码。

<a id="details"></a>

中断配置（Configuring Interrupts）的公共接口。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.1\_函数（Functions）

<a id="r_a335d42cf95c25ab8564475c4b4c3ead9"></a>

```c
static void irq_enable_next_level (const struct device *dev, uint32_t irq)
```

相关声明：[irq_enable_next_level](#a335d42cf95c25ab8564475c4b4c3ead9)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

启用下一级（Next Level）的 IRQ。

<a id="r_ad694fcad4c3fba0d2794cdc34ddcd1bb"></a>

```c
static void irq_disable_next_level (const struct device *dev, uint32_t irq)
```

相关声明：[irq_disable_next_level](#ad694fcad4c3fba0d2794cdc34ddcd1bb)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

禁用下一级（Next Level）的 IRQ。

<a id="r_aa7178acd1058940b83c7c7500217bc01"></a>

```c
static unsigned int irq_is_enabled_next_level (const struct device *dev)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[irq_is_enabled_next_level](#aa7178acd1058940b83c7c7500217bc01)、[device](../device_reference/P002_设备对象结构.md)。

取得 IRQ 的使能状态（Enable State）。

<a id="r_af41789f946ebb445f4a402009ed2e8bb"></a>

```c
static void irq_set_priority_next_level (const struct device *dev, uint32_t irq, uint32_t prio, uint32_t flags)
```

相关声明：[irq_set_priority_next_level](#af41789f946ebb445f4a402009ed2e8bb)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

设置 IRQ 优先级（Priority）。

<a id="r_a7e0e5fe59eae08878a8f243dd9301633"></a>

```c
static unsigned int irq_line_is_enabled_next_level (const struct device *dev, unsigned int irq)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[irq_line_is_enabled_next_level](#a7e0e5fe59eae08878a8f243dd9301633)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

获取 IRQ 线路（Line）的使能状态（Enable State）。

## 23.2\_详细说明（Detailed Documentation）

<a id="ad694fcad4c3fba0d2794cdc34ddcd1bb"></a>

### `irq_disable_next_level()`

```c
void irq_disable_next_level ( const struct device * dev, uint32_t irq )
```

声明属性：`inline`、`static`。

禁用下一级（Next Level）的 IRQ。

本例程禁用中断控制器（Interrupt Controller）中的中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `irq` | 要禁用的 IRQ。 |

<a id="a335d42cf95c25ab8564475c4b4c3ead9"></a>

### `irq_enable_next_level()`

```c
void irq_enable_next_level ( const struct device * dev, uint32_t irq )
```

声明属性：`inline`、`static`。

启用下一级（Next Level）的 IRQ。

本例程启用中断控制器（Interrupt Controller）中的中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `irq` | 要启用的 IRQ。 |

<a id="aa7178acd1058940b83c7c7500217bc01"></a>

### `irq_is_enabled_next_level()`

```c
unsigned int irq_is_enabled_next_level ( const struct device * dev)
```

声明属性：`inline`、`static`。

取得 IRQ 的使能状态（Enable State）。

本例程指示中断控制器（Interrupt Controller）中是否存在任何已启用的中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

返回（Returns）：中断使能状态，为 true 或 false。

<a id="a7e0e5fe59eae08878a8f243dd9301633"></a>

### `irq_line_is_enabled_next_level()`

```c
unsigned int irq_line_is_enabled_next_level ( const struct device * dev, unsigned int irq )
```

声明属性：`inline`、`static`。

获取 IRQ 线路（Line）的使能状态（Enable State）。

查询指定 IRQ 线路（Line）是否已启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `irq` | 要查询的 IRQ 线路（Line）。 |

返回（Returns）：中断使能状态，为 true 或 false。

<a id="af41789f946ebb445f4a402009ed2e8bb"></a>

### `irq_set_priority_next_level()`

```c
void irq_set_priority_next_level ( const struct device * dev, uint32_t irq, uint32_t prio, uint32_t flags )
```

声明属性：`inline`、`static`。

设置 IRQ 优先级（Priority）。

本例程指示中断控制器（Interrupt Controller）中是否存在任何已启用的中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `irq` | 要禁用的 IRQ。 |
| `prio` | 中断控制器（Interrupt Controller）中该 IRQ 的优先级（Priority）。 |
| `flags` | 控制器专用标志（Controller-specific Flags）。 |


## 23.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P411_irq_nextlevel.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P022_zephyr__drivers__interrupt_controller__intc_renesas_rx_grp_int.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__psa__key_ids.h_文件参考.md)
