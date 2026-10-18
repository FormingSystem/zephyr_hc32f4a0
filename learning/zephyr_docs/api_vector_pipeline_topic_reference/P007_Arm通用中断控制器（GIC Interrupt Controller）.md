---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-7
title: Arm通用中断控制器（GIC Interrupt Controller）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__arm__gic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_Arm通用中断控制器（GIC Interrupt Controller）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__arm__gic.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Arm 通用中断控制器（Generic Interrupt Controller，GIC）的设备树宏。

<a id="details"></a>

Arm 通用中断控制器（Generic Interrupt Controller，GIC）的设备树（Devicetree）宏，用于为兼容标识为 `arm,gic` 和 `arm,gic-v3` 的中断控制器编码中断单元（Interrupt Cells）。中断由三个单元描述：中断组（`GIC_SPI` 或 `GIC_PPI`）、该组内的中断编号，以及触发类型（`IRQ_TYPE_LEVEL` 或 `IRQ_TYPE_EDGE`）。下列原始示例展示了其写法。

```c
&i2c0 {
        interrupts = <GIC_SPI 25 IRQ_TYPE_LEVEL>;
};
```

<a id="header-files"></a>
<a id="files"></a>

## 7.1\_文件（Files）

<a id="r_arm-gic_2Eh"></a>

```c
file arm-gic.h
```

相关声明：[arm-gic.h](https://docs.zephyrproject.org/latest/doxygen/html/arm-gic_8h.html)。

Arm通用中断控制器（GIC）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_ga296e915831223a614a6ea87dbe7735e7"></a>

```c
#define IRQ_TYPE_LEVEL BIT(1)
```

相关声明：[IRQ_TYPE_LEVEL](#ga296e915831223a614a6ea87dbe7735e7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电平触发中断（Level-Triggered Interrupt）。

<a id="r_gaff68b0efbc719bc28f0d56c9ba8607bc"></a>

```c
#define IRQ_TYPE_EDGE BIT(2)
```

相关声明：[IRQ_TYPE_EDGE](#gaff68b0efbc719bc28f0d56c9ba8607bc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

边沿触发中断（Edge-Triggered Interrupt）。

<a id="r_gab5dc7ac388a5501a92f0c26d3995217f"></a>

```c
#define GIC_SPI 0x0
```

相关声明：[GIC_SPI](#gab5dc7ac388a5501a92f0c26d3995217f)。

共享外设中断（Shared Peripheral Interrupt，SPI）组。

<a id="r_ga25633bd9b6e14b0f6ded91b2fcfd614a"></a>

```c
#define GIC_PPI 0x1
```

相关声明：[GIC_PPI](#ga25633bd9b6e14b0f6ded91b2fcfd614a)。

私有外设中断（Private Peripheral Interrupt，PPI）组。

<a id="r_ga2dbeaa0c017cdff0982b381cc96f0a6c"></a>

```c
#define IRQ_DEFAULT_PRIORITY 0xa0
```

相关声明：[IRQ_DEFAULT_PRIORITY](#ga2dbeaa0c017cdff0982b381cc96f0a6c)。

默认中断优先级（Default Interrupt Priority）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 7.3\_CPU 中断编号（CPU Interrupt Numbers）

Arm CPU 接口的私有外设中断（Private Peripheral Interrupt，PPI）编号。

<a id="r_ga8688f8eec1ec9ecbacafbec20e32807e"></a>

```c
#define GIC_INT_VIRT_MAINT 25
```

相关声明：[GIC_INT_VIRT_MAINT](#ga8688f8eec1ec9ecbacafbec20e32807e)。

虚拟维护中断（Virtual Maintenance Interrupt）。

<a id="r_ga88ef9b1e5027f1e6b1b13896d84ba7e9"></a>

```c
#define GIC_INT_HYP_TIMER 26
```

相关声明：[GIC_INT_HYP_TIMER](#ga88ef9b1e5027f1e6b1b13896d84ba7e9)。

虚拟机监控器定时器中断（Hypervisor Timer Interrupt）。

<a id="r_ga3faa32072c74bcb2d79387085322f661"></a>

```c
#define GIC_INT_VIRT_TIMER 27
```

相关声明：[GIC_INT_VIRT_TIMER](#ga3faa32072c74bcb2d79387085322f661)。

虚拟定时器中断（Virtual Timer Interrupt）。

<a id="r_gadfb3434e71e3da30646b94ecfd3d192f"></a>

```c
#define GIC_INT_LEGACY_FIQ 28
```

相关声明：[GIC_INT_LEGACY_FIQ](#gadfb3434e71e3da30646b94ecfd3d192f)。

传统 nFIQ 信号（Legacy nFIQ Signal）。

<a id="r_ga9ae0a769a0e37b134971553a73865d55"></a>

```c
#define GIC_INT_PHYS_TIMER 29
```

相关声明：[GIC_INT_PHYS_TIMER](#ga9ae0a769a0e37b134971553a73865d55)。

安全物理定时器中断（Secure Physical Timer Interrupt）。

<a id="r_gaf01b2804853035ed3f111ecf3d8778ad"></a>

```c
#define GIC_INT_NS_PHYS_TIMER 30
```

相关声明：[GIC_INT_NS_PHYS_TIMER](#gaf01b2804853035ed3f111ecf3d8778ad)。

非安全物理定时器中断（Non-secure Physical Timer Interrupt），别名。

<a id="r_gabb56dd46d1d35f1137881b9dc0db2036"></a>

```c
#define GIC_INT_LEGACY_IRQ 31
```

相关声明：[GIC_INT_LEGACY_IRQ](#gabb56dd46d1d35f1137881b9dc0db2036)。

传统 nIRQ 信号（Legacy nIRQ Signal）。

## 7.4\_详细说明（Detailed Documentation）

<a id="ga88ef9b1e5027f1e6b1b13896d84ba7e9"></a>

### `GIC_INT_HYP_TIMER`

```c
#define GIC_INT_HYP_TIMER 26
```

```c
#include <zephyr/dt-bindings/interrupt-controller/arm-gic.h>
```

虚拟机监控器定时器中断（Hypervisor Timer Interrupt）。

<a id="gadfb3434e71e3da30646b94ecfd3d192f"></a>

### `GIC_INT_LEGACY_FIQ`

```c
#define GIC_INT_LEGACY_FIQ 28
```

```c
#include <zephyr/dt-bindings/interrupt-controller/arm-gic.h>
```

传统 nFIQ 信号（Legacy nFIQ Signal）。

<a id="gabb56dd46d1d35f1137881b9dc0db2036"></a>

### `GIC_INT_LEGACY_IRQ`

```c
#define GIC_INT_LEGACY_IRQ 31
```

```c
#include <zephyr/dt-bindings/interrupt-controller/arm-gic.h>
```

传统 nIRQ 信号（Legacy nIRQ Signal）。

<a id="gaf01b2804853035ed3f111ecf3d8778ad"></a>

### `GIC_INT_NS_PHYS_TIMER`

```c
#define GIC_INT_NS_PHYS_TIMER 30
```

```c
#include <zephyr/dt-bindings/interrupt-controller/arm-gic.h>
```

非安全物理定时器中断（Non-secure Physical Timer Interrupt），别名。

<a id="ga9ae0a769a0e37b134971553a73865d55"></a>

### `GIC_INT_PHYS_TIMER`

```c
#define GIC_INT_PHYS_TIMER 29
```

```c
#include <zephyr/dt-bindings/interrupt-controller/arm-gic.h>
```

安全物理定时器中断（Secure Physical Timer Interrupt）。

<a id="ga8688f8eec1ec9ecbacafbec20e32807e"></a>

### `GIC_INT_VIRT_MAINT`

```c
#define GIC_INT_VIRT_MAINT 25
```

```c
#include <zephyr/dt-bindings/interrupt-controller/arm-gic.h>
```

虚拟维护中断（Virtual Maintenance Interrupt）。

<a id="ga3faa32072c74bcb2d79387085322f661"></a>

### `GIC_INT_VIRT_TIMER`

```c
#define GIC_INT_VIRT_TIMER 27
```

```c
#include <zephyr/dt-bindings/interrupt-controller/arm-gic.h>
```

虚拟定时器中断（Virtual Timer Interrupt）。

<a id="ga25633bd9b6e14b0f6ded91b2fcfd614a"></a>

### `GIC_PPI`

```c
#define GIC_PPI 0x1
```

```c
#include <zephyr/dt-bindings/interrupt-controller/arm-gic.h>
```

私有外设中断（Private Peripheral Interrupt，PPI）组。

<a id="gab5dc7ac388a5501a92f0c26d3995217f"></a>

### `GIC_SPI`

```c
#define GIC_SPI 0x0
```

```c
#include <zephyr/dt-bindings/interrupt-controller/arm-gic.h>
```

共享外设中断（Shared Peripheral Interrupt，SPI）组。

<a id="ga2dbeaa0c017cdff0982b381cc96f0a6c"></a>

### `IRQ_DEFAULT_PRIORITY`

```c
#define IRQ_DEFAULT_PRIORITY 0xa0
```

```c
#include <zephyr/dt-bindings/interrupt-controller/arm-gic.h>
```

默认中断优先级（Default Interrupt Priority）。

<a id="gaff68b0efbc719bc28f0d56c9ba8607bc"></a>

### `IRQ_TYPE_EDGE`

```c
#define IRQ_TYPE_EDGE BIT(2)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/arm-gic.h>
```

边沿触发中断（Edge-Triggered Interrupt）。

<a id="ga296e915831223a614a6ea87dbe7735e7"></a>

### `IRQ_TYPE_LEVEL`

```c
#define IRQ_TYPE_LEVEL BIT(1)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/arm-gic.h>
```

电平触发中断（Level-Triggered Interrupt）。


## 7.5\_原页交叉引用（Cross References）

- [arm-gic.h](https://docs.zephyrproject.org/latest/doxygen/html/arm-gic_8h.html)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md) · [返回大纲](大纲.md) · [下一章](P008_ARITHRSTCR 复位控制（Reset Control）.md)
