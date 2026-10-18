---
id: learning.zephyr-docs.kconfig-reference.page-124
title: "`drivers/mm`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第124章\_`drivers/mm`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/mm` 的 8 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_EXTERNAL_ADDRESS_TRANSLATION"></a>

## 124.1 `CONFIG_EXTERNAL_ADDRESS_TRANSLATION`

**提示（Prompt）**：外部地址转换模块（External Address Translation Module）支持

**说明（Help）**

此配置用于支持 SoC 可能需要的外部地址转换模块，使用 `system_mm` API 的 `sys_mm_drv_page_phys_get()` 函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MMU && CONFIG_MM_DRV
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AM62X_M4
CONFIG_SOC_SERIES_AM64X_M4
```

**定义位置（Location）**：[`drivers/mm/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mm/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 内存管理（Memory Management）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_MM_DRV`](P124_drivers_mm_配置项参考.md#CONFIG_MM_DRV)、[`CONFIG_SOC_SERIES_AM62X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X_M4)、[`CONFIG_SOC_SERIES_AM64X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_M4)。

<a id="CONFIG_MM_DRV"></a>

## 124.2 `CONFIG_MM_DRV`

**提示（Prompt）**：内存管理（Memory Management）驱动【实验性（EXPERIMENTAL）】

**说明（Help）**

在系统配置中纳入内存管理（Memory Management）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_KERNEL_VM_SUPPORT
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AM62X_M4
CONFIG_SOC_SERIES_AM64X_M4
```

**定义位置（Location）**：[`drivers/mm/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mm/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_KERNEL_VM_SUPPORT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_VM_SUPPORT)、[`CONFIG_SOC_SERIES_AM62X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X_M4)、[`CONFIG_SOC_SERIES_AM64X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_M4)。

<a id="CONFIG_MM_DRV_INTEL_ADSP_MTL_TLB"></a>

## 124.3 `CONFIG_MM_DRV_INTEL_ADSP_MTL_TLB`

**提示（Prompt）**：用于 Meteor Lake 的 Intel 音频 DSP TLB 驱动

**说明（Help）**

Intel 音频数字信号处理器（DSP）硬件（Meteor Lake）上地址转换查找缓冲器（TLB）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_MTL_TLB_ENABLED && CONFIG_MM_DRV
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_SYS_MEM_BLOCKS
```

**定义位置（Location）**：[`drivers/mm/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mm/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 内存管理（Memory Management）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MM_DRV`](P124_drivers_mm_配置项参考.md#CONFIG_MM_DRV)、[`CONFIG_SYS_MEM_BLOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_MEM_BLOCKS)。

<a id="CONFIG_MM_DRV_INTEL_ADSP_TLB"></a>

## 124.4 `CONFIG_MM_DRV_INTEL_ADSP_TLB`

**提示（Prompt）**：Intel 音频 DSP TLB 驱动

**说明（Help）**

Intel 音频数字信号处理器（DSP）硬件上地址转换查找缓冲器（TLB）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_TLB_ENABLED && CONFIG_MM_DRV
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mm/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mm/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 内存管理（Memory Management）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MM_DRV`](P124_drivers_mm_配置项参考.md#CONFIG_MM_DRV)。

<a id="CONFIG_MM_DRV_INTEL_ADSP_TLB_REMAP_UNUSED_RAM"></a>

## 124.5 `CONFIG_MM_DRV_INTEL_ADSP_TLB_REMAP_UNUSED_RAM`

**提示（Prompt）**：关闭未使用 RAM 的电源（Power Off Unused RAM）

**说明（Help）**

允许 TLB 驱动重映射未使用的 RAM。这里的“未使用”指从链接脚本定义的 `unused_l2_sram_start_marke` 到 RAM 末尾的内存。注意，未使用内存默认会断电。如果动态管理内存，例如使用堆分配器（Heap Allocator），应禁用此选项。译注：符号拼写 `unused_l2_sram_start_marke` 按官方帮助原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MM_DRV
```

**定义位置（Location）**：[`drivers/mm/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mm/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 内存管理（Memory Management）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MM_DRV`](P124_drivers_mm_配置项参考.md#CONFIG_MM_DRV)。

<a id="CONFIG_MM_DRV_INTEL_VIRTUAL_REGION_COUNT"></a>

## 124.6 `CONFIG_MM_DRV_INTEL_VIRTUAL_REGION_COUNT`

**提示（Prompt）**：虚拟内存中定义的最大区域数量（Maximum Regions）

**说明（Help）**

此选项定义保存所有虚拟内存区域（Virtual Memory Region）的表的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MM_DRV_INTEL_ADSP_MTL_TLB && CONFIG_MM_DRV
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/mm/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mm/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 内存管理（Memory Management）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MM_DRV_INTEL_ADSP_MTL_TLB`](P124_drivers_mm_配置项参考.md#CONFIG_MM_DRV_INTEL_ADSP_MTL_TLB)、[`CONFIG_MM_DRV`](P124_drivers_mm_配置项参考.md#CONFIG_MM_DRV)。

<a id="CONFIG_MM_DRV_PAGE_SIZE"></a>

## 124.7 `CONFIG_MM_DRV_PAGE_SIZE`

**提示（Prompt）**：内存页大小（Memory Page Size）

**说明（Help）**

内存页的大小。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_MM_DRV
```

**默认值（Defaults）**

```text
0x1000
```

**定义位置（Location）**：[`drivers/mm/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mm/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 内存管理（Memory Management）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MM_DRV`](P124_drivers_mm_配置项参考.md#CONFIG_MM_DRV)。

<a id="CONFIG_MM_TI_RAT"></a>

## 124.8 `CONFIG_MM_TI_RAT`

**提示（Prompt）**：Texas Instruments 区域地址转换（RAT）模块

**说明（Help）**

启用 TI SoC 专用的基于区域的地址转换（Region-based Address Translation）支持函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EXTERNAL_ADDRESS_TRANSLATION && CONFIG_EXTERNAL_ADDRESS_TRANSLATION && CONFIG_MM_DRV
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AM62X_M4
CONFIG_SOC_SERIES_AM64X_M4
```

**定义位置（Location）**：[`drivers/mm/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mm/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 内存管理（Memory Management）驱动【实验性（EXPERIMENTAL）】 → 外部地址转换模块（External Address Translation Module）支持

**配置项引用（Symbol References）**：[`CONFIG_EXTERNAL_ADDRESS_TRANSLATION`](P124_drivers_mm_配置项参考.md#CONFIG_EXTERNAL_ADDRESS_TRANSLATION)、[`CONFIG_MM_DRV`](P124_drivers_mm_配置项参考.md#CONFIG_MM_DRV)、[`CONFIG_SOC_SERIES_AM62X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X_M4)、[`CONFIG_SOC_SERIES_AM64X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_M4)。

<!-- kconfig-navigation -->

[上一章](P123_drivers_misc_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P125_drivers_modem_配置项参考_1.md)
