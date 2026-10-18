---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-29
title: zephyr__drivers__interrupt_controller__riscv_aplic_direct.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic__direct_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_riscv\_aplic\_direct.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic__direct_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RISC-V APLIC直接投递模式（Direct Delivery Mode）的驱动API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/types.h>
#include <zephyr/arch/riscv/csr.h>
```

查看此文件的源码。

RISC-V 高级平台级中断控制器（Advanced Platform-Level Interrupt Controller，APLIC）的直接递送模式（Direct Delivery Mode）驱动 API。本头文件为以该模式运行的 APLIC 提供 API。在直接模式下，中断直接递送到硬件线程（Hart）的 MEXT 中断线，而不经过消息信号中断（MSI）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 29.1\_函数（Functions）

<a id="r_a375cb46c74f6b57288f745afa111a215"></a>

```c
void riscv_aplic_direct_mode_enable (const struct device *dev, bool enable)
```

相关声明：[riscv_aplic_direct_mode_enable](#a375cb46c74f6b57288f745afa111a215)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 APLIC 递送模式（Delivery Mode）。

<a id="r_aa2ccdb76d1801ab2a21f07ff00f7dabe"></a>

```c
int riscv_aplic_is_enabled (uint32_t local_irq)
```

相关声明：[riscv_aplic_is_enabled](#aa2ccdb76d1801ab2a21f07ff00f7dabe)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查指定的 RISC-V APLIC 中断线（Interrupt Line）是否已启用。

<a id="r_a767ca44582fa377331d124db4412c9af"></a>

```c
void riscv_aplic_set_priority (const struct device *dev, uint32_t local_irq, uint32_t prio)
```

相关声明：[riscv_aplic_set_priority](#a767ca44582fa377331d124db4412c9af)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在启用直接递送模式（Direct Delivery Mode）的域（Domain）中，为指定中断源配置优先级（Priority）。

<a id="r_a6f17dc3326d12fcebc0bd0e5dcfbd3e6"></a>

```c
unsigned int riscv_aplic_get_saved_irq (void)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[riscv_aplic_get_saved_irq](#a6f17dc3326d12fcebc0bd0e5dcfbd3e6)。

获取活动中断 ID（Active Interrupt ID）。

<a id="r_a49a32a14d9da6d14e109ae0261d12e95"></a>

```c
const struct device * riscv_aplic_get_saved_dev (void)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[riscv_aplic_get_saved_dev](#a49a32a14d9da6d14e109ae0261d12e95)。

获取活动中断控制器设备（Active Interrupt Controller Device）。

<a id="r_a089864486c6968eda8a0dd702b77c464"></a>

```c
void aplic_irq_handler (const struct device *dev)
```

相关声明：[aplic_irq_handler](#a089864486c6968eda8a0dd702b77c464)、[device](../device_reference/P002_设备对象结构.md)。

APLIC 直接模式中断（Direct-mode Interrupts）的 IRQ 处理程序。

<a id="r_a9fb92561a3507bace0e644f1cad25548"></a>

```c
int aplic_direct_init (const struct device *dev)
```

相关声明：[aplic_direct_init](#a9fb92561a3507bace0e644f1cad25548)、[device](../device_reference/P002_设备对象结构.md)。

在启用直接递送模式（Direct Delivery Mode）的情况下初始化 APLIC。

## 29.2\_详细说明（Detailed Documentation）

<a id="a9fb92561a3507bace0e644f1cad25548"></a>

### `aplic_direct_init()`

```c
int aplic_direct_init ( const struct device * dev)
```

在启用直接递送模式（Direct Delivery Mode）的情况下初始化 APLIC。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 高级平台级中断控制器（APLIC）设备。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="a089864486c6968eda8a0dd702b77c464"></a>

### `aplic_irq_handler()`

```c
void aplic_irq_handler ( const struct device * dev)
```

APLIC 直接模式中断（Direct-mode Interrupts）的 IRQ 处理程序。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 高级平台级中断控制器（APLIC）设备。 |

<a id="a375cb46c74f6b57288f745afa111a215"></a>

### `riscv_aplic_direct_mode_enable()`

```c
void riscv_aplic_direct_mode_enable ( const struct device * dev, bool enable )
```

启用或禁用 APLIC 递送模式（Delivery Mode）。

控制域配置寄存器（Domain Configuration Register）中的递送模式位（Delivery Mode Bit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 高级平台级中断控制器（APLIC）设备。 |
| `enable` | `true` 启用直接递送模式（Direct Delivery Mode），`false` 禁用。 |

<a id="a49a32a14d9da6d14e109ae0261d12e95"></a>

### `riscv_aplic_get_saved_dev()`

```c
const struct device * riscv_aplic_get_saved_dev ( void )
```

获取活动中断控制器设备（Active Interrupt Controller Device）。

**说明（Note）**：**注意（Note）：**应在中断已锁定（Interrupt Locked）的情况下调用。

**返回（Returns）**：**返回值（Returns）：**活动中断设备（Active Interrupt Device）的设备指针。

<a id="a6f17dc3326d12fcebc0bd0e5dcfbd3e6"></a>

### `riscv_aplic_get_saved_irq()`

```c
unsigned int riscv_aplic_get_saved_irq ( void )
```

获取活动中断 ID（Active Interrupt ID）。

**说明（Note）**：**注意（Note）：**应在中断已锁定（Interrupt Locked）的情况下调用。

**返回（Returns）**：**返回值（Returns）：**活动中断（Active Interrupt）的 ID。

<a id="aa2ccdb76d1801ab2a21f07ff00f7dabe"></a>

### `riscv_aplic_is_enabled()`

```c
int riscv_aplic_is_enabled ( uint32_t local_irq)
```

检查指定的 RISC-V APLIC 中断线（Interrupt Line）是否已启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `local_irq` | 要检查的本地 IRQ 编号（Local IRQ Number）。 |

**返回（Returns）**：**返回值（Returns）：**已启用返回 `1`，否则返回 `0`。

<a id="a767ca44582fa377331d124db4412c9af"></a>

### `riscv_aplic_set_priority()`

```c
void riscv_aplic_set_priority ( const struct device * dev, uint32_t local_irq, uint32_t prio )
```

在启用直接递送模式（Direct Delivery Mode）的域（Domain）中，为指定中断源配置优先级（Priority）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 高级平台级中断控制器（APLIC）设备。 |
| `local_irq` | 将要配置目标寄存器（Target Register）的本地 IRQ。 |
| `prio` | 要设置的优先级值（Priority Value）。 |


## 29.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P717_riscv_aplic_direct.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P028_zephyr__dt-bindings__gpio__renesas-rztn-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P030_zephyr__drivers__interrupt_controller__sam0_eic.h_文件参考.md)
