---
id: learning.zephyr-docs.api-file-service-interface-reference.page-5
title: zephyr__dt-bindings__interrupt-controller__arm-gic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arm-gic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_dt-bindings\_\_interrupt-controller\_\_arm-gic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/arm-gic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Arm通用中断控制器（GIC）的设备树宏。

<a id="details"></a>

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

Arm通用中断控制器（GIC）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="r_ga296e915831223a614a6ea87dbe7735e7"></a>

```c
#define IRQ_TYPE_LEVEL BIT(1)
```

相关声明：[IRQ_TYPE_LEVEL](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#ga296e915831223a614a6ea87dbe7735e7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电平触发中断（Level-Triggered Interrupt）。

<a id="r_gaff68b0efbc719bc28f0d56c9ba8607bc"></a>

```c
#define IRQ_TYPE_EDGE BIT(2)
```

相关声明：[IRQ_TYPE_EDGE](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#gaff68b0efbc719bc28f0d56c9ba8607bc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

边沿触发中断（Edge-Triggered Interrupt）。

<a id="r_gab5dc7ac388a5501a92f0c26d3995217f"></a>

```c
#define GIC_SPI 0x0
```

相关声明：[GIC_SPI](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#gab5dc7ac388a5501a92f0c26d3995217f)。

共享外设中断（Shared Peripheral Interrupt，SPI）组。

<a id="r_ga25633bd9b6e14b0f6ded91b2fcfd614a"></a>

```c
#define GIC_PPI 0x1
```

相关声明：[GIC_PPI](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#ga25633bd9b6e14b0f6ded91b2fcfd614a)。

私有外设中断（Private Peripheral Interrupt，PPI）组。

<a id="r_ga2dbeaa0c017cdff0982b381cc96f0a6c"></a>

```c
#define IRQ_DEFAULT_PRIORITY 0xa0
```

相关声明：[IRQ_DEFAULT_PRIORITY](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#ga2dbeaa0c017cdff0982b381cc96f0a6c)。

默认中断优先级（Default Interrupt Priority）。

<a id="define-members-0"></a>

### CPU 中断编号（CPU Interrupt Numbers）

Arm CPU 接口的私有外设中断（Private Peripheral Interrupt，PPI）编号。

<a id="r_ga8688f8eec1ec9ecbacafbec20e32807e"></a>

```c
#define GIC_INT_VIRT_MAINT 25
```

相关声明：[GIC_INT_VIRT_MAINT](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#ga8688f8eec1ec9ecbacafbec20e32807e)。

虚拟维护中断（Virtual Maintenance Interrupt）。

<a id="r_ga88ef9b1e5027f1e6b1b13896d84ba7e9"></a>

```c
#define GIC_INT_HYP_TIMER 26
```

相关声明：[GIC_INT_HYP_TIMER](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#ga88ef9b1e5027f1e6b1b13896d84ba7e9)。

虚拟机监控器定时器中断（Hypervisor Timer Interrupt）。

<a id="r_ga3faa32072c74bcb2d79387085322f661"></a>

```c
#define GIC_INT_VIRT_TIMER 27
```

相关声明：[GIC_INT_VIRT_TIMER](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#ga3faa32072c74bcb2d79387085322f661)。

虚拟定时器中断（Virtual Timer Interrupt）。

<a id="r_gadfb3434e71e3da30646b94ecfd3d192f"></a>

```c
#define GIC_INT_LEGACY_FIQ 28
```

相关声明：[GIC_INT_LEGACY_FIQ](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#gadfb3434e71e3da30646b94ecfd3d192f)。

传统 nFIQ 信号（Legacy nFIQ Signal）。

<a id="r_ga9ae0a769a0e37b134971553a73865d55"></a>

```c
#define GIC_INT_PHYS_TIMER 29
```

相关声明：[GIC_INT_PHYS_TIMER](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#ga9ae0a769a0e37b134971553a73865d55)。

安全物理定时器中断（Secure Physical Timer Interrupt）。

<a id="r_gaf01b2804853035ed3f111ecf3d8778ad"></a>

```c
#define GIC_INT_NS_PHYS_TIMER 30
```

相关声明：[GIC_INT_NS_PHYS_TIMER](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#gaf01b2804853035ed3f111ecf3d8778ad)。

非安全物理定时器中断（Non-secure Physical Timer Interrupt），别名。

<a id="r_gabb56dd46d1d35f1137881b9dc0db2036"></a>

```c
#define GIC_INT_LEGACY_IRQ 31
```

相关声明：[GIC_INT_LEGACY_IRQ](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#gabb56dd46d1d35f1137881b9dc0db2036)。

传统 nIRQ 信号（Legacy nIRQ Signal）。


## 5.2\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P016_arm-gic.h_源码浏览.md)
- [IRQ_TYPE_LEVEL](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#ga296e915831223a614a6ea87dbe7735e7)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [IRQ_TYPE_EDGE](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#gaff68b0efbc719bc28f0d56c9ba8607bc)
- [GIC_SPI](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#gab5dc7ac388a5501a92f0c26d3995217f)
- [GIC_PPI](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#ga25633bd9b6e14b0f6ded91b2fcfd614a)
- [IRQ_DEFAULT_PRIORITY](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#ga2dbeaa0c017cdff0982b381cc96f0a6c)
- [GIC_INT_VIRT_MAINT](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#ga8688f8eec1ec9ecbacafbec20e32807e)
- [GIC_INT_HYP_TIMER](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#ga88ef9b1e5027f1e6b1b13896d84ba7e9)
- [GIC_INT_VIRT_TIMER](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#ga3faa32072c74bcb2d79387085322f661)
- [GIC_INT_LEGACY_FIQ](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#gadfb3434e71e3da30646b94ecfd3d192f)
- [GIC_INT_PHYS_TIMER](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#ga9ae0a769a0e37b134971553a73865d55)
- [GIC_INT_NS_PHYS_TIMER](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#gaf01b2804853035ed3f111ecf3d8778ad)
- [GIC_INT_LEGACY_IRQ](../api_vector_pipeline_topic_reference/P007_Arm通用中断控制器（GIC Interrupt Controller）.md#gabb56dd46d1d35f1137881b9dc0db2036)

<a id="header-details"></a>

---

[上一章](P004_zephyr__dt-bindings__sensor__adxl313.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__mgmt__ec_host_cmd__backend.h_文件参考.md)
