---
id: learning.zephyr-docs.api-file-signal-device-reference.page-12
title: zephyr__drivers__interrupt_controller__intc_bcm283x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__bcm283x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_bcm283x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__bcm283x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BCM283x中断控制器（Interrupt Controller）的驱动API。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

BCM283x 中断控制器（Interrupt Controller）驱动 API。在 BCM2710（Pi 2、Pi 3、Pi Zero 2 W）上，两个物理控制器共同提供单一、平坦的 Zephyr 中断请求（IRQ）编号空间：IRQ 0..9 对应 BCM2836 ARM 本地中断控制器（ARM-local intc），包括每核定时器、邮箱、GPU 级联和性能监视单元（PMU）；驱动为 `drivers/interrupt_controller/intc_bcm2836_l1.c`。IRQ 32..127 对应 BCM2835 ARMC 外设汇聚控制器（Peripheral Aggregator），包括基本寄存器组、GPU 寄存器组 1 和 GPU 寄存器组 2，并级联在 L1 IRQ 8 下；驱动为 `drivers/interrupt_controller/intc_bcm2835_armctrl.c`。SoC 层 `soc/brcm/bcm2710/soc_irq.c` 在启用 `CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER` 时安装 `z_soc_irq_*` 架构钩子（Architecture Hooks），并根据调用方指定的 IRQ 范围分派给下面两组驱动函数。各驱动通过 `device_map()` 管理自己的内存映射输入输出（MMIO）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.1\_宏定义（Macros）

<a id="r_ga2677638c4dd01041425d25f25901302e"></a>

```c
#define BCM283X_ARMC_IRQ_BASE 32U
```

相关声明：[BCM283X_ARMC_IRQ_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga2677638c4dd01041425d25f25901302e)。

路由到 BCM2835 ARMC 外设汇聚控制器（Peripheral Aggregator）的第一个 Zephyr IRQ 编号。

<a id="r_ga70d77d4efbe9b3ee949345a3e06bb119"></a>

```c
#define BCM283X_ARMC_IRQ_LIMIT (BCM283X_ARMC_IRQ_BASE + 96U)
```

相关声明：[BCM283X_ARMC_IRQ_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga70d77d4efbe9b3ee949345a3e06bb119)、[BCM283X_ARMC_IRQ_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga2677638c4dd01041425d25f25901302e)。

Zephyr IRQ 空间中最后一个 ARMC IRQ 编号加一，即该范围的上界（不包含）。

<a id="r_ga1355c9269a0e920df0b82ee5b3c183e5"></a>

```c
#define BCM283X_IRQ_IS_L1(irq)
```

相关声明：[BCM283X_IRQ_IS_L1](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga1355c9269a0e920df0b82ee5b3c183e5)。

当 `irq` 位于 BCM2836 ARM 本地中断控制器（ARM-local intc）的范围 0..9 内时为真。

<a id="r_ga689c39201eb30edae3268b4a68bbedd6"></a>

```c
#define BCM283X_IRQ_IS_ARMC(irq)
```

相关声明：[BCM283X_IRQ_IS_ARMC](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga689c39201eb30edae3268b4a68bbedd6)。

当 `irq` 位于 BCM2835 ARMC 外设中断范围 32..127 内时为真。

<a id="r_ga27d1697bee1f6e81ae9bcebac38783a0"></a>

```c
#define BCM2836_L1_IRQ_GPU_BIT 8U
```

相关声明：[BCM2836_L1_IRQ_GPU_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga27d1697bee1f6e81ae9bcebac38783a0)。

GPU 级联（Cascade）在 L1 `IRQ_SOURCE` 中的位位置。

<a id="r_ga70edde5d34e0c9bb01f314fdc69f0cd7"></a>

```c
#define BCM2836_L1_IRQ_PMU_BIT 9U
```

相关声明：[BCM2836_L1_IRQ_PMU_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga70edde5d34e0c9bb01f314fdc69f0cd7)。

每核性能监视单元（PMU）IRQ 在 L1 `IRQ_SOURCE` 中的位位置。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.2\_函数（Functions）

<a id="r_gaea4d0829c483de09258ff7500d49973a"></a>

```c
void bcm2836_l1_intc_init (void)
```

相关声明：[bcm2836_l1_intc_init](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#gaea4d0829c483de09258ff7500d49973a)。

初始化 BCM2836 ARM 本地中断控制器（ARM-local Interrupt Controller）。

<a id="r_ga747b5793762f454f37f2aea5a0a98367"></a>

```c
void bcm2836_l1_intc_irq_enable (unsigned int irq)
```

相关声明：[bcm2836_l1_intc_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga747b5793762f454f37f2aea5a0a98367)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

使能一个 L1 中断源（IRQ Source）。

<a id="r_ga8172bde4064553565f1a2f004e7246a9"></a>

```c
void bcm2836_l1_intc_irq_disable (unsigned int irq)
```

相关声明：[bcm2836_l1_intc_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga8172bde4064553565f1a2f004e7246a9)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

禁用一个 L1 中断源（IRQ Source）。

<a id="r_ga2fe5a8b685d905243c05558a13212b3b"></a>

```c
int bcm2836_l1_intc_irq_is_enabled (unsigned int irq)
```

相关声明：[bcm2836_l1_intc_irq_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga2fe5a8b685d905243c05558a13212b3b)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

查询一个 L1 中断源（IRQ Source）当前是否已使能。

<a id="r_gacfe08085a3ca52ac0fb3123d0213359c"></a>

```c
unsigned int bcm2836_l1_intc_irq_get_active (void)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[bcm2836_l1_intc_irq_get_active](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#gacfe08085a3ca52ac0fb3123d0213359c)。

解析当前触发的 L1 中断请求（IRQ）。

<a id="r_ga53c43b0af32be13e55f15dfb4adaa5b0"></a>

```c
void bcm2835_armctrl_ic_init (void)
```

相关声明：[bcm2835_armctrl_ic_init](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga53c43b0af32be13e55f15dfb4adaa5b0)。

初始化 BCM2835 ARMC 外设中断控制器（Peripheral Interrupt Controller）。

<a id="r_gaa413beb6b63102a3f8fe61d7d1e96a8d"></a>

```c
void bcm2835_armctrl_ic_irq_enable (unsigned int irq)
```

相关声明：[bcm2835_armctrl_ic_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#gaa413beb6b63102a3f8fe61d7d1e96a8d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

使能一个 ARMC 外设中断源（IRQ Source）。

<a id="r_ga2c44c3f942a7cc764fadf1502b9ecc49"></a>

```c
void bcm2835_armctrl_ic_irq_disable (unsigned int irq)
```

相关声明：[bcm2835_armctrl_ic_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga2c44c3f942a7cc764fadf1502b9ecc49)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

禁用一个 ARMC 外设中断源（IRQ Source）。

<a id="r_ga75f8a727ac5a2f6a303031ca916c6552"></a>

```c
int bcm2835_armctrl_ic_irq_is_enabled (unsigned int irq)
```

相关声明：[bcm2835_armctrl_ic_irq_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga75f8a727ac5a2f6a303031ca916c6552)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

查询一个 ARMC 外设中断源（IRQ Source）是否已使能。

<a id="r_ga4ed816681fd685c63a9b602f5390da97"></a>

```c
unsigned int bcm2835_armctrl_ic_irq_get_active (void)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[bcm2835_armctrl_ic_irq_get_active](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga4ed816681fd685c63a9b602f5390da97)。

解析当前触发的 ARMC 外设中断请求（IRQ）。


## 12.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P392_intc_bcm283x.h_源码浏览.md)
- [BCM283X_ARMC_IRQ_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga2677638c4dd01041425d25f25901302e)
- [BCM283X_ARMC_IRQ_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga70d77d4efbe9b3ee949345a3e06bb119)
- [BCM283X_IRQ_IS_L1](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga1355c9269a0e920df0b82ee5b3c183e5)
- [BCM283X_IRQ_IS_ARMC](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga689c39201eb30edae3268b4a68bbedd6)
- [BCM2836_L1_IRQ_GPU_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga27d1697bee1f6e81ae9bcebac38783a0)
- [BCM2836_L1_IRQ_PMU_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga70edde5d34e0c9bb01f314fdc69f0cd7)
- [bcm2836_l1_intc_init](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#gaea4d0829c483de09258ff7500d49973a)
- [bcm2836_l1_intc_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga747b5793762f454f37f2aea5a0a98367)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [bcm2836_l1_intc_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga8172bde4064553565f1a2f004e7246a9)
- [bcm2836_l1_intc_irq_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga2fe5a8b685d905243c05558a13212b3b)
- [bcm2836_l1_intc_irq_get_active](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#gacfe08085a3ca52ac0fb3123d0213359c)
- [bcm2835_armctrl_ic_init](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga53c43b0af32be13e55f15dfb4adaa5b0)
- [bcm2835_armctrl_ic_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#gaa413beb6b63102a3f8fe61d7d1e96a8d)
- [bcm2835_armctrl_ic_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga2c44c3f942a7cc764fadf1502b9ecc49)
- [bcm2835_armctrl_ic_irq_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga75f8a727ac5a2f6a303031ca916c6552)
- [bcm2835_armctrl_ic_irq_get_active](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga4ed816681fd685c63a9b602f5390da97)
- [CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER)
- [device_map()](../device_reference/P011_设备MMIO管理概述.md#ga6b4a9841a5176104e1b63f7475d3d2a2)

<a id="header-details"></a>

---

[上一章](P011_zephyr__mgmt__mcumgr__grp__fs_mgmt__fs_mgmt_hash_checksum.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__drivers__interrupt_controller__intc_exti_stm32.h_文件参考.md)
