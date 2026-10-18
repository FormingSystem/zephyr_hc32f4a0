---
id: learning.zephyr-docs.api-bridge-paging-topic-reference.page-8
title: BCM283x 中断控制器（Interrupt controllers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_BCM283x 中断控制器（Interrupt controllers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.1\_宏定义（Macros）

<a id="r_ga2677638c4dd01041425d25f25901302e"></a>

```c
#define BCM283X_ARMC_IRQ_BASE 32U
```

相关声明：[BCM283X_ARMC_IRQ_BASE](#ga2677638c4dd01041425d25f25901302e)。

路由到 BCM2835 ARMC 外设汇聚控制器（Peripheral Aggregator）的第一个 Zephyr IRQ 编号。

<a id="r_ga70d77d4efbe9b3ee949345a3e06bb119"></a>

```c
#define BCM283X_ARMC_IRQ_LIMIT (BCM283X_ARMC_IRQ_BASE + 96U)
```

相关声明：[BCM283X_ARMC_IRQ_LIMIT](#ga70d77d4efbe9b3ee949345a3e06bb119)、[BCM283X_ARMC_IRQ_BASE](#ga2677638c4dd01041425d25f25901302e)。

Zephyr IRQ 空间中最后一个 ARMC IRQ 编号加一，即该范围的上界（不包含）。

<a id="r_ga1355c9269a0e920df0b82ee5b3c183e5"></a>

```c
#define BCM283X_IRQ_IS_L1(irq)
```

相关声明：[BCM283X_IRQ_IS_L1](#ga1355c9269a0e920df0b82ee5b3c183e5)。

当 `irq` 位于 BCM2836 ARM 本地中断控制器（ARM-local intc）的范围 0..9 内时为真。

<a id="r_ga689c39201eb30edae3268b4a68bbedd6"></a>

```c
#define BCM283X_IRQ_IS_ARMC(irq)
```

相关声明：[BCM283X_IRQ_IS_ARMC](#ga689c39201eb30edae3268b4a68bbedd6)。

当 `irq` 位于 BCM2835 ARMC 外设中断范围 32..127 内时为真。

<a id="r_ga27d1697bee1f6e81ae9bcebac38783a0"></a>

```c
#define BCM2836_L1_IRQ_GPU_BIT 8U
```

相关声明：[BCM2836_L1_IRQ_GPU_BIT](#ga27d1697bee1f6e81ae9bcebac38783a0)。

GPU 级联（Cascade）在 L1 `IRQ_SOURCE` 中的位位置。

<a id="r_ga70edde5d34e0c9bb01f314fdc69f0cd7"></a>

```c
#define BCM2836_L1_IRQ_PMU_BIT 9U
```

相关声明：[BCM2836_L1_IRQ_PMU_BIT](#ga70edde5d34e0c9bb01f314fdc69f0cd7)。

每核性能监视单元（PMU）IRQ 在 L1 `IRQ_SOURCE` 中的位位置。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.2\_函数（Functions）

<a id="r_gaea4d0829c483de09258ff7500d49973a"></a>

```c
void bcm2836_l1_intc_init (void)
```

相关声明：[bcm2836_l1_intc_init](#gaea4d0829c483de09258ff7500d49973a)。

初始化 BCM2836 ARM 本地中断控制器（ARM-local Interrupt Controller）。

<a id="r_ga747b5793762f454f37f2aea5a0a98367"></a>

```c
void bcm2836_l1_intc_irq_enable (unsigned int irq)
```

相关声明：[bcm2836_l1_intc_irq_enable](#ga747b5793762f454f37f2aea5a0a98367)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

使能一个 L1 中断源（IRQ Source）。

<a id="r_ga8172bde4064553565f1a2f004e7246a9"></a>

```c
void bcm2836_l1_intc_irq_disable (unsigned int irq)
```

相关声明：[bcm2836_l1_intc_irq_disable](#ga8172bde4064553565f1a2f004e7246a9)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

禁用一个 L1 中断源（IRQ Source）。

<a id="r_ga2fe5a8b685d905243c05558a13212b3b"></a>

```c
int bcm2836_l1_intc_irq_is_enabled (unsigned int irq)
```

相关声明：[bcm2836_l1_intc_irq_is_enabled](#ga2fe5a8b685d905243c05558a13212b3b)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

查询一个 L1 中断源（IRQ Source）当前是否已使能。

<a id="r_gacfe08085a3ca52ac0fb3123d0213359c"></a>

```c
unsigned int bcm2836_l1_intc_irq_get_active (void)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[bcm2836_l1_intc_irq_get_active](#gacfe08085a3ca52ac0fb3123d0213359c)。

解析当前触发的 L1 中断请求（IRQ）。

<a id="r_ga53c43b0af32be13e55f15dfb4adaa5b0"></a>

```c
void bcm2835_armctrl_ic_init (void)
```

相关声明：[bcm2835_armctrl_ic_init](#ga53c43b0af32be13e55f15dfb4adaa5b0)。

初始化 BCM2835 ARMC 外设中断控制器（Peripheral Interrupt Controller）。

<a id="r_gaa413beb6b63102a3f8fe61d7d1e96a8d"></a>

```c
void bcm2835_armctrl_ic_irq_enable (unsigned int irq)
```

相关声明：[bcm2835_armctrl_ic_irq_enable](#gaa413beb6b63102a3f8fe61d7d1e96a8d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

使能一个 ARMC 外设中断源（IRQ Source）。

<a id="r_ga2c44c3f942a7cc764fadf1502b9ecc49"></a>

```c
void bcm2835_armctrl_ic_irq_disable (unsigned int irq)
```

相关声明：[bcm2835_armctrl_ic_irq_disable](#ga2c44c3f942a7cc764fadf1502b9ecc49)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

禁用一个 ARMC 外设中断源（IRQ Source）。

<a id="r_ga75f8a727ac5a2f6a303031ca916c6552"></a>

```c
int bcm2835_armctrl_ic_irq_is_enabled (unsigned int irq)
```

相关声明：[bcm2835_armctrl_ic_irq_is_enabled](#ga75f8a727ac5a2f6a303031ca916c6552)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

查询一个 ARMC 外设中断源（IRQ Source）是否已使能。

<a id="r_ga4ed816681fd685c63a9b602f5390da97"></a>

```c
unsigned int bcm2835_armctrl_ic_irq_get_active (void)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[bcm2835_armctrl_ic_irq_get_active](#ga4ed816681fd685c63a9b602f5390da97)。

解析当前触发的 ARMC 外设中断请求（IRQ）。

## 8.3\_详细说明（Detailed Documentation）

<a id="ga27d1697bee1f6e81ae9bcebac38783a0"></a>

### `BCM2836_L1_IRQ_GPU_BIT`

```c
#define BCM2836_L1_IRQ_GPU_BIT 8U
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

GPU 级联（Cascade）在 L1 `IRQ_SOURCE` 中的位位置。

这也是级联入口（Cascade Entry）的 Zephyr IRQ 编号。中断服务例程（ISR）从不注册到该索引；当 L1 中断控制器报告此 IRQ 时，SoC 分派程序会透明地进入 ARMC 控制器，查找实际触发中断的外设 IRQ。

<a id="ga70edde5d34e0c9bb01f314fdc69f0cd7"></a>

### `BCM2836_L1_IRQ_PMU_BIT`

```c
#define BCM2836_L1_IRQ_PMU_BIT 9U
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

每核性能监视单元（PMU）IRQ 在 L1 `IRQ_SOURCE` 中的位位置。

这也是性能监视单元（PMU）的 Zephyr IRQ 编号。

<a id="ga2677638c4dd01041425d25f25901302e"></a>

### `BCM283X_ARMC_IRQ_BASE`

```c
#define BCM283X_ARMC_IRQ_BASE 32U
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

路由到 BCM2835 ARMC 外设汇聚控制器（Peripheral Aggregator）的第一个 Zephyr IRQ 编号。

<a id="ga70d77d4efbe9b3ee949345a3e06bb119"></a>

### `BCM283X_ARMC_IRQ_LIMIT`

```c
#define BCM283X_ARMC_IRQ_LIMIT (BCM283X_ARMC_IRQ_BASE + 96U)
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

Zephyr IRQ 空间中最后一个 ARMC IRQ 编号加一，即该范围的上界（不包含）。

<a id="ga689c39201eb30edae3268b4a68bbedd6"></a>

### `BCM283X_IRQ_IS_ARMC`

```c
#define BCM283X_IRQ_IS_ARMC ( irq)
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

展开值（Value）：

```c
((irq) >= BCM283X_ARMC_IRQ_BASE && \
(irq) < BCM283X_ARMC_IRQ_LIMIT)
```

当 `irq` 位于 BCM2835 ARMC 外设中断范围 32..127 内时为真。

<a id="ga1355c9269a0e920df0b82ee5b3c183e5"></a>

### `BCM283X_IRQ_IS_L1`

```c
#define BCM283X_IRQ_IS_L1 ( irq)
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

展开值（Value）：

```c
((irq) < BCM283X_ARMC_IRQ_BASE)
```

当 `irq` 位于 BCM2836 ARM 本地中断控制器（ARM-local intc）的范围 0..9 内时为真。

<a id="ga53c43b0af32be13e55f15dfb4adaa5b0"></a>

### `bcm2835_armctrl_ic_init()`

```c
void bcm2835_armctrl_ic_init ( void )
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

初始化 BCM2835 ARMC 外设中断控制器（Peripheral Interrupt Controller）。

通过 `device_map()` 映射内存映射输入输出（MMIO）寄存器组，并禁用 bank-0、PEND1 和 PEND2 的全部中断源。由 SoC 的 `z_soc_irq_init()` 在架构启动期间调用，早于所有 `SYS_INIT` 优先级的初始化。

<a id="ga2c44c3f942a7cc764fadf1502b9ecc49"></a>

### `bcm2835_armctrl_ic_irq_disable()`

```c
void bcm2835_armctrl_ic_irq_disable ( unsigned int irq)
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

禁用一个 ARMC 外设中断源（IRQ Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | ARMC 范围内的 Zephyr IRQ 编号。对范围外编号的调用会被静默忽略。 |

<a id="gaa413beb6b63102a3f8fe61d7d1e96a8d"></a>

### `bcm2835_armctrl_ic_irq_enable()`

```c
void bcm2835_armctrl_ic_irq_enable ( unsigned int irq)
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

使能一个 ARMC 外设中断源（IRQ Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | ARMC 范围内的 Zephyr IRQ 编号，即 `BCM283X_ARMC_IRQ_BASE .. BCM283X_ARMC_IRQ_LIMIT - 1`。范围外的调用会被静默忽略。 |

<a id="ga4ed816681fd685c63a9b602f5390da97"></a>

### `bcm2835_armctrl_ic_irq_get_active()`

```c
unsigned int bcm2835_armctrl_ic_irq_get_active ( void )
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

解析当前触发的 ARMC 外设中断请求（IRQ）。

封装 bank-0 快捷位（Shortcut-bit）解析逻辑，即 BCM2835 ARM Peripherals 数据手册第 7 章中的 Quirk 1。仅在未置位任何快捷位时，才继续遍历 PEND1／PEND2。

**返回（Returns）**：返回值：触发中断的外设对应的 Zephyr IRQ 编号；若没有 ARMC 中断源被置为有效，则返回 `CONFIG_NUM_IRQS`。

<a id="ga75f8a727ac5a2f6a303031ca916c6552"></a>

### `bcm2835_armctrl_ic_irq_is_enabled()`

```c
int bcm2835_armctrl_ic_irq_is_enabled ( unsigned int irq)
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

查询一个 ARMC 外设中断源（IRQ Source）是否已使能。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | ARMC 范围内的 Zephyr IRQ 编号。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `1` | 已使能（Enabled）时。 |
| `0` | 已禁用（Disabled），或者 `irq` 位于 ARMC 范围之外时。 |

<a id="gaea4d0829c483de09258ff7500d49973a"></a>

### `bcm2836_l1_intc_init()`

```c
void bcm2836_l1_intc_init ( void )
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

初始化 BCM2836 ARM 本地中断控制器（ARM-local Interrupt Controller）。

通过 `device_map()` 映射内存映射输入输出（MMIO）寄存器组，并屏蔽所有本地路由到核心 0 的中断源。由 SoC 的 `z_soc_irq_init()` 在架构启动期间调用，早于所有 `SYS_INIT` 优先级的初始化。

<a id="ga8172bde4064553565f1a2f004e7246a9"></a>

### `bcm2836_l1_intc_irq_disable()`

```c
void bcm2836_l1_intc_irq_disable ( unsigned int irq)
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

禁用一个 L1 中断源（IRQ Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | L1 范围 0..9 内的 Zephyr IRQ 编号。 |

<a id="ga747b5793762f454f37f2aea5a0a98367"></a>

### `bcm2836_l1_intc_irq_enable()`

```c
void bcm2836_l1_intc_irq_enable ( unsigned int irq)
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

使能一个 L1 中断源（IRQ Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | L1 范围 0..9 内的 Zephyr IRQ 编号。IRQ 8，即 GPU 级联（Cascade），是隐式的，没有独立的 IRQ 使能位。 |

<a id="gacfe08085a3ca52ac0fb3123d0213359c"></a>

### `bcm2836_l1_intc_irq_get_active()`

```c
unsigned int bcm2836_l1_intc_irq_get_active ( void )
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

解析当前触发的 L1 中断请求（IRQ）。

**返回（Returns）**：返回值：触发中断的中断源对应的 Zephyr IRQ 编号；若没有 L1 中断源被置为有效，则返回 `CONFIG_NUM_IRQS`。GPU 级联位触发时，调用方接下来应进入 `bcm2835_armctrl_ic_irq_get_active()`。

<a id="ga2fe5a8b685d905243c05558a13212b3b"></a>

### `bcm2836_l1_intc_irq_is_enabled()`

```c
int bcm2836_l1_intc_irq_is_enabled ( unsigned int irq)
```

```c
#include <zephyr/drivers/interrupt_controller/intc_bcm283x.h>
```

查询一个 L1 中断源（IRQ Source）当前是否已使能。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | L1 范围内的 Zephyr IRQ 编号。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `1` | 已使能（Enabled）时。 |
| `0` | 已禁用时，或对于没有回读路径（Readback Path）的性能监视单元（PMU）。 |


## 8.4\_原页交叉引用（Cross References）

- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [zephyr/drivers/interrupt_controller/intc_bcm283x.h](../api_file_signal_device_reference/P012_zephyr__drivers__interrupt_controller__intc_bcm283x.h_文件参考.md)
- [device_map()](../device_reference/P011_设备MMIO管理概述.md#ga6b4a9841a5176104e1b63f7475d3d2a2)
- [CONFIG_NUM_IRQS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NUM_IRQS)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__intc__bcm283x_html_ga2677638c4dd01041425d25f25901302e"></a>
<a id="agroup__intc__bcm283x_html_ga70d77d4efbe9b3ee949345a3e06bb119"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_INA226 API主题.md) · [返回大纲](大纲.md) · [下一章](P009_链路层发现协议（Link Layer Discovery Protocol）的定义与辅助工具。.md)
