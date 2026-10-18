---
id: learning.zephyr-docs.kconfig-reference.page-27
title: "`arch/Kconfig`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第27章\_`arch/Kconfig`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `arch/Kconfig` 的 38 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_KOBJECT_TEXT_AREA"></a>

## 27.1 `CONFIG_KOBJECT_TEXT_AREA`

**提示（Prompt）**：内核对象代码区大小（Kobject Text Area Size）

**说明（Help）**

内核对象代码区（Kernel Object Text Area）的大小，用于链接脚本（Linker Script）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE
```

**默认值（Defaults）**

```text
1024 if CONFIG_UBSAN
512 if CONFIG_COVERAGE_GCOV
512 if CONFIG_NO_OPTIMIZATIONS
512 if CONFIG_STACK_CANARIES_ALL
512 if CONFIG_STACK_CANARIES && CONFIG_RISCV
256
```

**定义位置（Location）**：[`arch/Kconfig:452`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L452)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_UBSAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UBSAN)、[`CONFIG_COVERAGE_GCOV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE_GCOV)、[`CONFIG_NO_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NO_OPTIMIZATIONS)、[`CONFIG_STACK_CANARIES_ALL`](P002_kernel_配置项参考_2.md#CONFIG_STACK_CANARIES_ALL)、[`CONFIG_STACK_CANARIES`](P002_kernel_配置项参考_2.md#CONFIG_STACK_CANARIES)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_MAX_THREAD_BYTES"></a>

## 27.2 `CONFIG_MAX_THREAD_BYTES`

**提示（Prompt）**：跟踪对象线程权限（Object Thread Permissions）使用的字节数

**说明（Help）**

每个内核对象（Kernel Object）都关联一个位域（Bitfield），用于保存该对象的线程权限（Thread Permissions）。此选项控制位域大小，以字节为单位，并限制系统可创建的线程数量。默认值随 CPU 数量增加，因为内核会为每个 CPU 创建一个空闲线程（Idle Thread）。应用程序若自行声明了大量线程，仍需进一步提高此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE
```

**默认值（Defaults）**

```text
5 if CONFIG_MP_MAX_NUM_CPUS > 4
4 if CONFIG_MP_MAX_NUM_CPUS > 2
3 if CONFIG_MP_MAX_NUM_CPUS > 1
2
```

**定义位置（Location）**：[`arch/Kconfig:511`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L511)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_MP_MAX_NUM_CPUS`](P001_kernel_配置项参考_1.md#CONFIG_MP_MAX_NUM_CPUS)。

<a id="CONFIG_MIPS"></a>

## 27.3 `CONFIG_MIPS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

MIPS 架构（Architecture）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_ARCH_IS_SET
CONFIG_ATOMIC_OPERATIONS_C
```

**被选择（Selected by）**

```text
CONFIG_SOC_QEMU_MALTA
```

**定义位置（Location）**：[`arch/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_IS_SET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_IS_SET)、[`CONFIG_ATOMIC_OPERATIONS_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_C)、[`CONFIG_SOC_QEMU_MALTA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_MALTA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_QEMU_MALTA`。

<a id="CONFIG_MPU"></a>

## 27.4 `CONFIG_MPU`

**提示（Prompt）**：内存保护单元功能（MPU Features）

**说明（Help）**

启用后，此选项向核心内核表明内存保护单元（MPU）已启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_MPU
```

**被选择（Selected by）**

```text
CONFIG_ARC_MPU
CONFIG_RISCV_PMP
CONFIG_XTENSA_MPU
CONFIG_ARM_MPU
```

**定义位置（Location）**：[`arch/Kconfig:1215`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1215)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARC_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_MPU)、[`CONFIG_RISCV_PMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_PMP)、[`CONFIG_XTENSA_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_MPU)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)。

<a id="CONFIG_MPU_GAP_FILLING"></a>

## 27.5 `CONFIG_MPU_GAP_FILLING`

**提示（Prompt）**：强制 MPU 填充背景内存区域（Background Memory Regions）

**说明（Help）**

此 Kconfig 选项要求 MPU 驱动在上下文切换（Context Switch）期间编程动态 MPU 区域，即用户线程栈、特权栈保护区（PRIV Stack Guard）和应用内存域时，强制完整划分内核 SRAM。允许将其配置为关闭，是为了给应用内存域编程留下更多可用 MPU 区域。

注意：只有构建启用用户空间（USERSPACE）支持时，才应需要更多 MPU 区域。因此，构建不支持 USERSPACE 时，应始终要求填充空隙（Gap Filling）。关闭此选项后，对于未被显式 MPU 区域覆盖的内存，依据架构特定机制限制为仅特权代码可访问。有关此选项的使用方式，参见架构专用文档。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPU_REQUIRES_NON_OVERLAPPING_REGIONS && CONFIG_MPU
```

**默认值（Defaults）**

```text
y if !CONFIG_USERSPACE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_STM32N6X
CONFIG_ARM_MPU
```

**定义位置（Location）**：[`arch/Kconfig:1239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1239)。

**菜单路径（Menu Path）**：顶层（Top） → 内存保护单元功能（MPU Features）

**配置项引用（Symbol References）**：[`CONFIG_MPU_REQUIRES_NON_OVERLAPPING_REGIONS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU_REQUIRES_NON_OVERLAPPING_REGIONS)、[`CONFIG_MPU`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32N6X`。

<a id="CONFIG_MPU_REQUIRES_NON_OVERLAPPING_REGIONS"></a>

## 27.6 `CONFIG_MPU_REQUIRES_NON_OVERLAPPING_REGIONS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 MPU 要求活动，即已启用的 MPU 区域（Region）彼此不能重叠，则启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPU
```

**被选择（Selected by）**

```text
CONFIG_ARC_MPU
CONFIG_ARM_MPU
```

**定义位置（Location）**：[`arch/Kconfig:1233`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1233)。

**菜单路径（Menu Path）**：顶层（Top） → 内存保护单元功能（MPU Features）

**配置项引用（Symbol References）**：[`CONFIG_MPU`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU)、[`CONFIG_ARC_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_MPU)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)。

<a id="CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT"></a>

## 27.7 `CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 MPU 要求区域（Region）的对齐和大小均为 2 的幂，则启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPU
```

**被选择（Selected by）**

```text
CONFIG_ARC_MPU
CONFIG_PMP_POWER_OF_TWO_ALIGNMENT
CONFIG_ARM_MPU
```

**定义位置（Location）**：[`arch/Kconfig:1227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1227)。

**菜单路径（Menu Path）**：顶层（Top） → 内存保护单元功能（MPU Features）

**配置项引用（Symbol References）**：[`CONFIG_MPU`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU)、[`CONFIG_ARC_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_MPU)、[`CONFIG_PMP_POWER_OF_TWO_ALIGNMENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PMP_POWER_OF_TWO_ALIGNMENT)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)。

<a id="CONFIG_NOCACHE_MEMORY"></a>

## 27.8 `CONFIG_NOCACHE_MEMORY`

**提示（Prompt）**：非缓存内存（Uncached Memory）支持

**说明（Help）**

添加名为 `nocache` 的读写内存段（Read-write Memory Section），配置为不经过缓存。当缓存一致性（Cache Coherence）问题无法通过理想方式处理，或不能通过缓存维护操作解决时，可用该段进行 DMA 传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
```

**被选择（Selected by）**

```text
CONFIG_CRYPTO_INFINEON_MXCRYPTO
CONFIG_CRYPTO_MCUX_DCP
CONFIG_RENESAS_RZ_LCDC
CONFIG_ENTROPY_MCUX_CAAM
CONFIG_ETH_MCHP_GMAC_G1
CONFIG_ETH_NXP_ENET
CONFIG_ETH_NXP_S32_GMAC
CONFIG_ETH_NXP_S32_NETC
CONFIG_ETH_RENESAS_RA
CONFIG_ETH_RENESAS_RA_RMAC
CONFIG_ETH_SAM_GMAC
CONFIG_ETH_STM32_HAL
CONFIG_ETH_XLNX_GEM
CONFIG_ETH_ESP32_DWC_ETHER_1000
CONFIG_ETH_NUMAKER_DWC_ETHER_1000
CONFIG_ETH_NXP_DWC_ETHER_QOS
CONFIG_ETH_STM32_DWC_ETHER_QOS
CONFIG_ETH_STM32_DWC_ETHER_1000
CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS
CONFIG_ETH_NXP_IMX_NETC
CONFIG_MDIO_NXP_S32_GMAC
CONFIG_MDIO_NXP_S32_NETC
CONFIG_GPIO_NXP_SIUL2
CONFIG_NXP_SIUL2_EIRQ
CONFIG_MBOX_NXP_S32_MRU
CONFIG_PWM_NXP_S32_EMIOS
CONFIG_IMX_USDHC_DMA_SUPPORT
CONFIG_UART_NXP_S32_LINFLEXD
CONFIG_NXP_S32_SPI
CONFIG_UDC_NXP_EHCI
CONFIG_UHC_NXP_EHCI
CONFIG_USB_DC_NXP_EHCI
CONFIG_WDT_NXP_S32
```

**被弱选择（Implied by）**

```text
CONFIG_DMA_MCUX_EDMA_V4
```

**定义位置（Location）**：[`arch/Kconfig:552`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L552)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_CRYPTO_INFINEON_MXCRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRYPTO_INFINEON_MXCRYPTO)、[`CONFIG_CRYPTO_MCUX_DCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRYPTO_MCUX_DCP)、[`CONFIG_RENESAS_RZ_LCDC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RENESAS_RZ_LCDC)、[`CONFIG_ENTROPY_MCUX_CAAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENTROPY_MCUX_CAAM)、[`CONFIG_ETH_MCHP_GMAC_G1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_MCHP_GMAC_G1)、[`CONFIG_ETH_NXP_ENET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_NXP_ENET)、[`CONFIG_ETH_NXP_S32_GMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_NXP_S32_GMAC)、[`CONFIG_ETH_NXP_S32_NETC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_ETH_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_RENESAS_RA)、[`CONFIG_ETH_RENESAS_RA_RMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_RENESAS_RA_RMAC)、[`CONFIG_ETH_SAM_GMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_SAM_GMAC)、[`CONFIG_ETH_STM32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_XLNX_GEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_XLNX_GEM)、[`CONFIG_ETH_ESP32_DWC_ETHER_1000`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_ESP32_DWC_ETHER_1000)、[`CONFIG_ETH_NUMAKER_DWC_ETHER_1000`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_NUMAKER_DWC_ETHER_1000)、[`CONFIG_ETH_NXP_DWC_ETHER_QOS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_NXP_DWC_ETHER_QOS)、[`CONFIG_ETH_STM32_DWC_ETHER_QOS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_STM32_DWC_ETHER_QOS)、[`CONFIG_ETH_STM32_DWC_ETHER_1000`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_STM32_DWC_ETHER_1000)、[`CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS)、[`CONFIG_ETH_NXP_IMX_NETC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_NXP_IMX_NETC)、[`CONFIG_MDIO_NXP_S32_GMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDIO_NXP_S32_GMAC)、[`CONFIG_MDIO_NXP_S32_NETC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDIO_NXP_S32_NETC)、[`CONFIG_GPIO_NXP_SIUL2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_NXP_SIUL2)、[`CONFIG_NXP_SIUL2_EIRQ`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_NXP_SIUL2_EIRQ)、[`CONFIG_MBOX_NXP_S32_MRU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBOX_NXP_S32_MRU)、[`CONFIG_PWM_NXP_S32_EMIOS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_NXP_S32_EMIOS)、[`CONFIG_IMX_USDHC_DMA_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IMX_USDHC_DMA_SUPPORT)、[`CONFIG_UART_NXP_S32_LINFLEXD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NXP_S32_LINFLEXD)、[`CONFIG_NXP_S32_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_S32_SPI)、[`CONFIG_UDC_NXP_EHCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_NXP_EHCI)、[`CONFIG_UHC_NXP_EHCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_NXP_EHCI)、[`CONFIG_USB_DC_NXP_EHCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DC_NXP_EHCI)、[`CONFIG_WDT_NXP_S32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NXP_S32)、[`CONFIG_DMA_MCUX_EDMA_V4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA_MCUX_EDMA_V4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_NOINIT_SNIPPET_FIRST"></a>

## 27.9 `CONFIG_NOINIT_SNIPPET_FIRST`

**提示（Prompt）**：优先放置未初始化链接脚本片段（No-init Linker Script Snippet）

**说明（Help）**

默认情况下，`include/zephyr/linker/common-noinit.ld` 在段末尾插入 `snippets-noinit.ld`。有时 `snippets-noinit.ld` 中的指令需要作用于本文件中的其他指令，此时包含 `snippets-noinit.ld` 的语句必须位于段开头。此配置选项允许这样安排。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_PSC3
```

**定义位置（Location）**：[`arch/Kconfig:430`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L430)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_PSC3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSC3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_PSC3`。

<a id="CONFIG_NO_UNUSED_STACK_INSPECTION"></a>

## 27.10 `CONFIG_NO_UNUSED_STACK_INSPECTION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果架构在检查未使用栈内存（Unused Stack Memory）时会产生故障，则选择此项。该区域指当前栈指针与当前栈区域最深可用地址之间的内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARC_STACK_CHECKING
```

**定义位置（Location）**：[`arch/Kconfig:503`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L503)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC_STACK_CHECKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_STACK_CHECKING)。

<a id="CONFIG_OPENRISC"></a>

## 27.11 `CONFIG_OPENRISC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

OpenRISC 架构（Architecture）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_ARCH_IS_SET
CONFIG_ATOMIC_OPERATIONS_BUILTIN
CONFIG_BIG_ENDIAN
CONFIG_USE_SWITCH
CONFIG_USE_SWITCH_SUPPORTED
CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE
CONFIG_ARCH_HAS_CODE_DATA_RELOCATION
```

**被选择（Selected by）**

```text
CONFIG_SOC_QEMU_OR1K
```

**定义位置（Location）**：[`arch/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_IS_SET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_IS_SET)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_BIG_ENDIAN`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_BIG_ENDIAN)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)、[`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE)、[`CONFIG_ARCH_HAS_CODE_DATA_RELOCATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CODE_DATA_RELOCATION)、[`CONFIG_SOC_QEMU_OR1K`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_OR1K)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`、`CONFIG_SOC_QEMU_OR1K`。

<a id="CONFIG_PRIVILEGED_STACK_SIZE"></a>

## 27.12 `CONFIG_PRIVILEGED_STACK_SIZE`

**提示（Prompt）**：特权栈大小（Privileged Stack Size）

**说明（Help）**

此选项设置用户模式线程栈之外额外使用的特权栈区域（Privileged Stack Region）大小。正常执行时，用户模式不能访问该区域；执行系统调用（System Call）期间，由系统调用使用此区域。该值必须为最小栈对齐值（Minimum Stack Alignment）的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE
```

**默认值（Defaults）**

```text
2048 if CONFIG_EMUL
1024
```

**定义位置（Location）**：[`arch/Kconfig:440`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L440)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)。

<a id="CONFIG_RISCV"></a>

## 27.13 `CONFIG_RISCV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RISC-V 架构（Architecture）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RISCV_ENABLED
```

**主动选择（Selects）**

```text
CONFIG_ARCH_IS_SET
CONFIG_ATOMIC_OPERATIONS_C if !CONFIG_RISCV_ISA_EXT_A && !CONFIG_ATOMIC_OPERATIONS_ARCH
CONFIG_ATOMIC_OPERATIONS_BUILTIN if CONFIG_RISCV_ISA_EXT_A
CONFIG_ARCH_SUPPORTS_COREDUMP
CONFIG_ARCH_SUPPORTS_COREDUMP_PRIV_STACKS
CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS if !CONFIG_SMP
CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR
CONFIG_ARCH_SUPPORTS_ROM_START if !CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
CONFIG_ARCH_SUPPORTS_EMPTY_IRQ_SPURIOUS
CONFIG_ARCH_HAS_CODE_DATA_RELOCATION
CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE
CONFIG_ARCH_HAS_SUSPEND_TO_RAM
CONFIG_USE_SWITCH_SUPPORTED
CONFIG_USE_SWITCH
CONFIG_SCHED_IPI_SUPPORTED if CONFIG_SMP
CONFIG_ARCH_HAS_DIRECTED_IPIS
CONFIG_BARRIER_OPERATIONS_BUILTIN if CONFIG_RISCV_ISA_BASE_FENCE
CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET if CONFIG_USERSPACE
CONFIG_ARCH_HAS_STACK_CANARIES_TLS
CONFIG_STACK_CANARIES_TLS_PREPEND if CONFIG_STACK_CANARIES_TLS
CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED
CONFIG_ARCH_HAS_SEMIHOST
CONFIG_ARCH_HAS_ISR_TABLES_LOCAL_DECLARATION
CONFIG_ARCH_SUPPORTS_ROM_OFFSET
CONFIG_ARCH_HAS_CPU_IDLE_HOOKS
CONFIG_ARCH_HAS_DIRECT_INTERRUPTS
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL616CL
CONFIG_SOC_SERIES_BL61X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_SERIES_BL808
CONFIG_SOC_NEORV32
CONFIG_SOC_RISCV_VIRTUAL_RENODE
CONFIG_SOC_FAMILY_CH32V
CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV
CONFIG_SOC_RP2350A_HAZARD3_0
CONFIG_SOC_RP2350B_HAZARD3_0
CONFIG_SOC_FAMILY_CDNS_SWERV
CONFIG_SOC_SERIES_ESP32C2
CONFIG_SOC_SERIES_ESP32C3
CONFIG_SOC_SERIES_ESP32C5
CONFIG_SOC_SERIES_ESP32C6
CONFIG_SOC_SERIES_ESP32C61
CONFIG_SOC_SERIES_ESP32H2
CONFIG_SOC_SERIES_ESP32P4
CONFIG_RISCV_CORE_NORDIC_VPR
CONFIG_SOC_OPENTITAN
CONFIG_SOC_LITEX_VEXIIRISCV
CONFIG_SOC_LITEX_VEXRISCV
CONFIG_SOC_SERIES_GD32VF103
CONFIG_SOC_SERIES_HYDROGEN
CONFIG_SOC_SERIES_NITROGEN
CONFIG_SOC_SERIES_AE350
CONFIG_SOC_IT51XXX
CONFIG_SOC_IT8XXX2
CONFIG_SOC_SERIES_TLSR951X
CONFIG_SOC_SERIES_NIOSV
CONFIG_SOC_OPENISA_RV32M1
CONFIG_SOC_SERIES_PIC64GX
CONFIG_SOC_SERIES_SY1XX
CONFIG_SOC_THEJAS32
CONFIG_SOC_GANGA
CONFIG_SOC_FAMILY_MAX32_RV32
CONFIG_SOC_SERIES_RHX
CONFIG_SOC_SERIES_RMX
CONFIG_SOC_EGIS_ET171
CONFIG_SOC_SERIES_STARFIVE_JH71XX
CONFIG_SOC_SERIES_MIV
CONFIG_SOC_SERIES_POLARFIRE
CONFIG_SOC_EFINIX_SAPPHIRE
CONFIG_SOC_CV32A6
CONFIG_SOC_CV64A6
CONFIG_SOC_SERIES_FE300
CONFIG_SOC_SERIES_FU500
CONFIG_SOC_SERIES_FU700
```

**定义位置（Location）**：[`arch/Kconfig:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L147)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_IS_SET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_IS_SET)、[`CONFIG_ATOMIC_OPERATIONS_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_C)、[`CONFIG_RISCV_ISA_EXT_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_ISA_EXT_A)、[`CONFIG_ATOMIC_OPERATIONS_ARCH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_ARCH)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_ARCH_SUPPORTS_COREDUMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP)、[`CONFIG_ARCH_SUPPORTS_COREDUMP_PRIV_STACKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP_PRIV_STACKS)、[`CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR)、[`CONFIG_ARCH_SUPPORTS_ROM_START`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_ROM_START)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ARCH_SUPPORTS_EMPTY_IRQ_SPURIOUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_EMPTY_IRQ_SPURIOUS)、[`CONFIG_ARCH_HAS_CODE_DATA_RELOCATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CODE_DATA_RELOCATION)、[`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE)、[`CONFIG_ARCH_HAS_SUSPEND_TO_RAM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_SUSPEND_TO_RAM)、[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_SCHED_IPI_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_IPI_SUPPORTED)、[`CONFIG_ARCH_HAS_DIRECTED_IPIS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DIRECTED_IPIS)、[`CONFIG_BARRIER_OPERATIONS_BUILTIN`](P001_kernel_配置项参考_1.md#CONFIG_BARRIER_OPERATIONS_BUILTIN)、[`CONFIG_RISCV_ISA_BASE_FENCE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_ISA_BASE_FENCE)、[`CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_ARCH_HAS_STACK_CANARIES_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACK_CANARIES_TLS)、[`CONFIG_STACK_CANARIES_TLS_PREPEND`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_STACK_CANARIES_TLS_PREPEND)、[`CONFIG_STACK_CANARIES_TLS`](P002_kernel_配置项参考_2.md#CONFIG_STACK_CANARIES_TLS)、[`CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED)、[`CONFIG_ARCH_HAS_SEMIHOST`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_SEMIHOST)、[`CONFIG_ARCH_HAS_ISR_TABLES_LOCAL_DECLARATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_ISR_TABLES_LOCAL_DECLARATION)、[`CONFIG_ARCH_SUPPORTS_ROM_OFFSET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_ROM_OFFSET)、[`CONFIG_ARCH_HAS_CPU_IDLE_HOOKS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CPU_IDLE_HOOKS)、[`CONFIG_ARCH_HAS_DIRECT_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DIRECT_INTERRUPTS)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL616CL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL616CL)、[`CONFIG_SOC_SERIES_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL61X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_SERIES_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL808)、[`CONFIG_SOC_NEORV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NEORV32)、[`CONFIG_SOC_RISCV_VIRTUAL_RENODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RISCV_VIRTUAL_RENODE)、[`CONFIG_SOC_FAMILY_CH32V`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_CH32V)、[`CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV)、[`CONFIG_SOC_RP2350A_HAZARD3_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A_HAZARD3_0)、[`CONFIG_SOC_RP2350B_HAZARD3_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B_HAZARD3_0)、[`CONFIG_SOC_FAMILY_CDNS_SWERV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_CDNS_SWERV)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_RISCV_CORE_NORDIC_VPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_CORE_NORDIC_VPR)、[`CONFIG_SOC_OPENTITAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENTITAN)、[`CONFIG_SOC_LITEX_VEXIIRISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LITEX_VEXIIRISCV)、[`CONFIG_SOC_LITEX_VEXRISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LITEX_VEXRISCV)、[`CONFIG_SOC_SERIES_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32VF103)、[`CONFIG_SOC_SERIES_HYDROGEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_HYDROGEN)、[`CONFIG_SOC_SERIES_NITROGEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NITROGEN)、[`CONFIG_SOC_SERIES_AE350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)、[`CONFIG_SOC_IT51XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51XXX)、[`CONFIG_SOC_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2)、[`CONFIG_SOC_SERIES_TLSR951X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TLSR951X)、[`CONFIG_SOC_SERIES_NIOSV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NIOSV)、[`CONFIG_SOC_OPENISA_RV32M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENISA_RV32M1)、[`CONFIG_SOC_SERIES_PIC64GX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PIC64GX)、[`CONFIG_SOC_SERIES_SY1XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SY1XX)、[`CONFIG_SOC_THEJAS32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_THEJAS32)、[`CONFIG_SOC_GANGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GANGA)、[`CONFIG_SOC_FAMILY_MAX32_RV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_RV32)、[`CONFIG_SOC_SERIES_RHX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RHX)、[`CONFIG_SOC_SERIES_RMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RMX)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)、[`CONFIG_SOC_SERIES_STARFIVE_JH71XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STARFIVE_JH71XX)、[`CONFIG_SOC_SERIES_MIV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MIV)、[`CONFIG_SOC_SERIES_POLARFIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_POLARFIRE)、[`CONFIG_SOC_EFINIX_SAPPHIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFINIX_SAPPHIRE)、[`CONFIG_SOC_CV32A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV32A6)、[`CONFIG_SOC_CV64A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV64A6)、[`CONFIG_SOC_SERIES_FE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FE300)、[`CONFIG_SOC_SERIES_FU500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU500)、[`CONFIG_SOC_SERIES_FU700`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU700)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_SUPPORTS_COREDUMP`、`CONFIG_ARCH_SUPPORTS_COREDUMP_PRIV_STACKS`、`CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS`、`CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR`、`CONFIG_ARCH_SUPPORTS_ROM_START`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`、`CONFIG_ARCH_SUPPORTS_EMPTY_IRQ_SPURIOUS`、`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`、`CONFIG_ARCH_HAS_STACK_CANARIES_TLS`、`CONFIG_SOC_FAMILY_CH32V`、`CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV`、`CONFIG_SOC_FAMILY_CDNS_SWERV`、`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_OPENTITAN`、`CONFIG_SOC_LITEX_VEXIIRISCV`、`CONFIG_SOC_LITEX_VEXRISCV`、`CONFIG_SOC_SERIES_HYDROGEN`、`CONFIG_SOC_SERIES_NITROGEN`、`CONFIG_SOC_IT51XXX`、`CONFIG_SOC_IT8XXX2`、`CONFIG_SOC_SERIES_SY1XX`、`CONFIG_SOC_GANGA`、`CONFIG_SOC_FAMILY_MAX32_RV32`、`CONFIG_SOC_SERIES_RHX`、`CONFIG_SOC_SERIES_RMX`、`CONFIG_SOC_SERIES_FE300`、`CONFIG_SOC_SERIES_FU500`、`CONFIG_SOC_SERIES_FU700`。

<a id="CONFIG_RX"></a>

## 27.14 `CONFIG_RX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Renesas RX 架构（Architecture）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_ARCH_IS_SET
CONFIG_ATOMIC_OPERATIONS_C
CONFIG_USE_SWITCH
CONFIG_USE_SWITCH_SUPPORTED
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RX130
CONFIG_SOC_SERIES_RX140
CONFIG_SOC_SERIES_RX14T
CONFIG_SOC_SERIES_RX261
CONFIG_SOC_SERIES_RX26T
CONFIG_SOC_SERIES_RX62N
CONFIG_SOC_SERIES_RX74M
CONFIG_SOC_SERIES_RX74N
```

**定义位置（Location）**：[`arch/Kconfig:243`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L243)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_IS_SET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_IS_SET)、[`CONFIG_ATOMIC_OPERATIONS_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_C)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)、[`CONFIG_SOC_SERIES_RX130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX130)、[`CONFIG_SOC_SERIES_RX140`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX140)、[`CONFIG_SOC_SERIES_RX14T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX14T)、[`CONFIG_SOC_SERIES_RX261`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX261)、[`CONFIG_SOC_SERIES_RX26T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX26T)、[`CONFIG_SOC_SERIES_RX62N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX62N)、[`CONFIG_SOC_SERIES_RX74M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74M)、[`CONFIG_SOC_SERIES_RX74N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74N)。

<a id="CONFIG_SHARED_INTERRUPTS"></a>

## 27.15 `CONFIG_SHARED_INTERRUPTS`

**提示（Prompt）**：启用共享中断（Shared Interrupts）支持［实验性］

**说明（Help）**

设置此项以启用共享中断（Shared Interrupts）支持。请谨慎使用，启用后会使镜像大小（Image Size）有不可忽略的增加。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_SW_ISR_TABLE
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_REALTEK_AMEBA_ZEPHYR_BT
CONFIG_REALTEK_AMEBA_ZEPHYR_BT
CONFIG_COMPARATOR_MSPM0
```

**定义位置（Location）**：[`arch/Kconfig:627`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L627)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

**配置项引用（Symbol References）**：[`CONFIG_GEN_SW_ISR_TABLE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_SW_ISR_TABLE)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_REALTEK_AMEBA_ZEPHYR_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_REALTEK_AMEBA_ZEPHYR_BT)、[`CONFIG_COMPARATOR_MSPM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COMPARATOR_MSPM0)。

<a id="CONFIG_SHARED_IRQ_MAX_NUM_CLIENTS"></a>

## 27.16 `CONFIG_SHARED_IRQ_MAX_NUM_CLIENTS`

**提示（Prompt）**：每个共享中断允许的最大客户端数（Maximum Clients per Shared Interrupt）

**说明（Help）**

此选项控制每个共享中断（Shared Interrupt）允许的最大客户端数量，请根据需要设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHARED_INTERRUPTS
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`arch/Kconfig:636`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L636)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration） → 启用共享中断（Shared Interrupts）支持［实验性］

**配置项引用（Symbol References）**：[`CONFIG_SHARED_INTERRUPTS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SHARED_INTERRUPTS)。

<a id="CONFIG_SIMPLIFIED_EXCEPTION_CODES"></a>

## 27.17 `CONFIG_SIMPLIFIED_EXCEPTION_CODES`

**提示（Prompt）**：将架构专用异常码（Architecture-specific Exception Codes）转换为 `K_ERR_CPU_EXCEPTION`

**说明（Help）**

同一段错误代码，例如 `NULL` 指针解引用，在 CPU 层面可能产生多种异常码（Exception Code），取决于地址是否存在、是否配置 MPU、CPU 的具体实现及其他原因。启用此选项后，将所有架构专用异常码统一为通用的 `K_ERR_CPU_EXCEPTION`，大幅提高测试代码的可移植性（Portability）。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y if CONFIG_ZTEST
```

**定义位置（Location）**：[`arch/Kconfig:809`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L809)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)。

<a id="CONFIG_SOC_CACHE"></a>

## 27.18 `CONFIG_SOC_CACHE`

**提示（Prompt）**：SoC 专用缓存控制器（SoC-specific Cache Controller）

**说明（Help）**

SoC 专用缓存控制器（Cache Controller），要求搜索路径中存在 `soc_cache.h` 文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_HAS_CACHE_FUNCTIONS && <choice CONFIG_CACHE_TYPE>
```

**定义位置（Location）**：[`arch/Kconfig:1481`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1481)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options） → 缓存类型（Cache Type）

**配置项引用（Symbol References）**：[`CONFIG_SOC_HAS_CACHE_FUNCTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_HAS_CACHE_FUNCTIONS)、[`CONFIG_CACHE_TYPE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_TYPE)。

<a id="CONFIG_SPARC"></a>

## 27.19 `CONFIG_SPARC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SPARC 架构（Architecture）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_ARCH_IS_SET
CONFIG_USE_SWITCH
CONFIG_USE_SWITCH_SUPPORTED
CONFIG_BIG_ENDIAN
CONFIG_ATOMIC_OPERATIONS_BUILTIN if CONFIG_SPARC_CASA
CONFIG_ATOMIC_OPERATIONS_C if !CONFIG_SPARC_CASA
CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE
CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO
```

**被选择（Selected by）**

```text
CONFIG_SOC_LEON3
CONFIG_SOC_GR716A
```

**定义位置（Location）**：[`arch/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_IS_SET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_IS_SET)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)、[`CONFIG_BIG_ENDIAN`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_BIG_ENDIAN)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_SPARC_CASA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPARC_CASA)、[`CONFIG_ATOMIC_OPERATIONS_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_C)、[`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE)、[`CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO)、[`CONFIG_SOC_LEON3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LEON3)、[`CONFIG_SOC_GR716A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GR716A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`、`CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO`、`CONFIG_SOC_LEON3`、`CONFIG_SOC_GR716A`。

<a id="CONFIG_SRAM_BASE_ADDRESS"></a>

## 27.20 `CONFIG_SRAM_BASE_ADDRESS`

**提示（Prompt）**：SRAM 基地址（Base Address）［已弃用］

**说明（Help）**

SRAM 基地址（Base Address），默认值来自设备树（Devicetree）的 `/chosen/zephyr,sram`。用户一般应避免通过 menuconfig 或配置文件修改。此选项现已弃用，必须改为引用设备树中 `zephyr,sram` 对应的 chosen 节点。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**默认值（Defaults）**

```text
0x0
```

**定义位置（Location）**：[`arch/Kconfig:317`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L317)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

<a id="CONFIG_SRAM_DEPRECATED_KCONFIG_SET"></a>

## 27.21 `CONFIG_SRAM_DEPRECATED_KCONFIG_SET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示手动设置了 `CONFIG_SRAM_SIZE` 或 `CONFIG_SRAM_BASE_ADDRESS`。这些 Kconfig 选项现已弃用，应改为引用设备树（Devicetree）中 `zephyr,sram` 对应的 chosen 节点。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y if CONFIG_SRAM_SIZE != 0
y if CONFIG_SRAM_BASE_ADDRESS != 0x0
n
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`arch/Kconfig:294`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L294)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_SRAM_SIZE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_SIZE)、[`CONFIG_SRAM_BASE_ADDRESS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_BASE_ADDRESS)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_SRAM_REGION_PERMISSIONS"></a>

## 27.22 `CONFIG_SRAM_REGION_PERMISSIONS`

**提示（Prompt）**：为 SRAM 中的内核区域分配适当权限（Permissions）

**说明（Help）**

此选项表示内存保护硬件（Memory Protection Hardware）存在且已启用，并在启动时为内核镜像中的内存范围配置了保护区域。启用后，内核镜像的特定区域会对所有线程，包括监管者线程（Supervisor Thread），应用以下访问策略：

1. 所有程序代码具有只读、可执行权限。
2. 所有只读数据具有只读权限；若硬件支持，则禁止执行。
3. 所有其他 RAM 地址具有读写权限；若硬件支持，则禁止执行。

`USERSPACE`、`HW_STACK_PROTECTION` 等选项还可能对内存映射施加额外策略，可作用于全局，也可仅作用于当前运行线程。为满足内存保护硬件的对齐约束，此选项可能消耗额外内存。

禁用后，整个内核使用默认内存访问权限，通常为读／写／执行。对于仅使用 MMU 实现按需分页（Demand Paging）、不需要内存保护且不希望为区域间对齐消耗 RAM 的系统，关闭此选项可能更合适。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MMU || CONFIG_MPU
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ARC_MPU
CONFIG_ARM_AARCH32_MMU
CONFIG_ARM_MMU
CONFIG_RISCV_PMP
CONFIG_XTENSA_MPU
CONFIG_ARM_MPU
```

**定义位置（Location）**：[`arch/Kconfig:1266`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1266)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_MPU`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU)、[`CONFIG_ARC_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_MPU)、[`CONFIG_ARM_AARCH32_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_AARCH32_MMU)、[`CONFIG_ARM_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MMU)、[`CONFIG_RISCV_PMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_PMP)、[`CONFIG_XTENSA_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_MPU)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)。

<a id="CONFIG_SRAM_SIZE"></a>

## 27.23 `CONFIG_SRAM_SIZE`

**提示（Prompt）**：SRAM 大小（Size，kB）［已弃用］

**说明（Help）**

SRAM 大小，以 kB 为单位，默认值来自设备树（Devicetree）的 `/chosen/zephyr,sram`。用户一般应避免通过 menuconfig 或配置文件修改。此选项现已弃用，必须改为引用设备树中 `zephyr,sram` 对应的 chosen 节点。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`arch/Kconfig:308`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L308)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

<a id="CONFIG_SRAM_SW_ISR_TABLE"></a>

## 27.24 `CONFIG_SRAM_SW_ISR_TABLE`

**提示（Prompt）**：将软件 ISR 表（Software ISR Table）放入 SRAM 而非 Flash

**说明（Help）**

此选项指定将软件中断向量表（Software Interrupts Vector Table）放在 SRAM 中，而非 Flash。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_DYNAMIC_INTERRUPTS
```

**定义位置（Location）**：[`arch/Kconfig:775`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L775)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

**配置项引用（Symbol References）**：[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)。

<a id="CONFIG_SRAM_VECTOR_TABLE"></a>

## 27.25 `CONFIG_SRAM_VECTOR_TABLE`

**提示（Prompt）**：将向量表（Vector Table）放入 SRAM 而非 Flash

**说明（Help）**

启用就地执行（XiP）时，此选项会将向量表（Vector Table）从 Flash 重定位到 SRAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_VECTOR_TABLE_RELOCATION && CONFIG_XIP && !CONFIG_ROMSTART_RELOCATION_ROM
```

**被选择（Selected by）**

```text
CONFIG_SILABS_SISDK_SLEEPTIMER
CONFIG_SILABS_SISDK_SLEEPTIMER
```

**定义位置（Location）**：[`arch/Kconfig:766`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L766)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_VECTOR_TABLE_RELOCATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_VECTOR_TABLE_RELOCATION)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)、[`CONFIG_ROMSTART_RELOCATION_ROM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ROMSTART_RELOCATION_ROM)、[`CONFIG_SILABS_SISDK_SLEEPTIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_SLEEPTIMER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_VECTOR_TABLE_RELOCATION`。

<a id="CONFIG_STACK_CANARIES_TLS_GUARD_OFFSET"></a>

## 27.26 `CONFIG_STACK_CANARIES_TLS_GUARD_OFFSET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

从线程局部存储（TLS）基址寄存器到栈金丝雀（Stack Canary）的字节偏移量。设置 `-mstack-protector-guard-offset=<offset>`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STACK_CANARIES_TLS_PREPEND
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`arch/Kconfig:1052`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1052)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_STACK_CANARIES_TLS_PREPEND`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_STACK_CANARIES_TLS_PREPEND)。

<a id="CONFIG_STACK_CANARIES_TLS_GUARD_REG"></a>

## 27.27 `CONFIG_STACK_CANARIES_TLS_GUARD_REG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

访问栈金丝雀（Stack Canary）时，用作线程局部存储（TLS）基址指针的寄存器。设置 `-mstack-protector-guard-reg=<reg>`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_STACK_CANARIES_TLS_PREPEND
```

**默认值（Defaults）**

```text
"tp" if CONFIG_RISCV
```

**定义位置（Location）**：[`arch/Kconfig:1044`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1044)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_STACK_CANARIES_TLS_PREPEND`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_STACK_CANARIES_TLS_PREPEND)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_STACK_CANARIES_TLS_PREPEND"></a>

## 27.28 `CONFIG_STACK_CANARIES_TLS_PREPEND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将栈金丝雀（Stack Canary）段 `.stack_chk.guard` 放在 TLS 块偏移 `0` 处，作为 `.tdata/.tbss` 之前的第一个段。对于编译器通过 TLS 基址指针加固定偏移访问金丝雀的架构，例如 RISC-V，这是必需的。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STACK_CANARIES_TLS
```

**被选择（Selected by）**

```text
CONFIG_RISCV
```

**定义位置（Location）**：[`arch/Kconfig:1035`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1035)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_STACK_CANARIES_TLS`](P002_kernel_配置项参考_2.md#CONFIG_STACK_CANARIES_TLS)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_STACK_GROWS_UP"></a>

## 27.29 `CONFIG_STACK_GROWS_UP`

**提示（Prompt）**：栈向更高内存地址增长（Stack Grows Upward）

**说明（Help）**

如果架构的线程栈向高地址增长（Upward-growing Thread Stack），选择此选项；这种情况并不常见。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`arch/Kconfig:497`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L497)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

<a id="CONFIG_TOOLCHAIN_HAS_BUILTIN_FFS"></a>

## 27.30 `CONFIG_TOOLCHAIN_HAS_BUILTIN_FFS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，用于表示工具链具有 `__builtin_ffs*()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y if !(CONFIG_64BIT && CONFIG_RISCV)
```

**定义位置（Location）**：[`arch/Kconfig:1513`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1513)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_TOOLCHAIN_SUPPORTS_ISR_TABLES_LOCAL_DECLARATION"></a>

## 27.31 `CONFIG_TOOLCHAIN_SUPPORTS_ISR_TABLES_LOCAL_DECLARATION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，用于表示工具链支持中断表的本地声明（Local Declaration of Interrupt Tables）。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`arch/Kconfig:585`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L585)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

<a id="CONFIG_TRICORE"></a>

## 27.32 `CONFIG_TRICORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

TriCore 架构（Architecture）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_ARCH_IS_SET
CONFIG_USE_SWITCH
CONFIG_USE_SWITCH_SUPPORTED
CONFIG_ATOMIC_OPERATIONS_BUILTIN if "zephyr" = "llvm"
CONFIG_ATOMIC_OPERATIONS_C if "zephyr" != "llvm"
CONFIG_ARCH_HAS_CODE_DATA_RELOCATION
CONFIG_ARCH_SUPPORTS_ROM_START
CONFIG_ARCH_HAS_THREAD_ABORT
CONFIG_BARRIER_OPERATIONS_BUILTIN if "zephyr" = "llvm"
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_TC3X
CONFIG_SOC_SERIES_TC4X
```

**弱选择（Implies）**

```text
CONFIG_XIP
```

**定义位置（Location）**：[`arch/Kconfig:198`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L198)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_IS_SET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_IS_SET)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_ATOMIC_OPERATIONS_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_C)、[`CONFIG_ARCH_HAS_CODE_DATA_RELOCATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CODE_DATA_RELOCATION)、[`CONFIG_ARCH_SUPPORTS_ROM_START`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_ROM_START)、[`CONFIG_ARCH_HAS_THREAD_ABORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_THREAD_ABORT)、[`CONFIG_BARRIER_OPERATIONS_BUILTIN`](P001_kernel_配置项参考_1.md#CONFIG_BARRIER_OPERATIONS_BUILTIN)、[`CONFIG_SOC_SERIES_TC3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TC3X)、[`CONFIG_SOC_SERIES_TC4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TC4X)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_SUPPORTS_ROM_START`、`CONFIG_ARCH_HAS_THREAD_ABORT`、`CONFIG_SOC_SERIES_TC3X`、`CONFIG_SOC_SERIES_TC4X`。

<a id="CONFIG_TRUSTED_EXECUTION_NONSECURE"></a>

## 27.33 `CONFIG_TRUSTED_EXECUTION_NONSECURE`

**提示（Prompt）**：可信执行（Trusted Execution）：非安全固件镜像（Non-Secure Firmware Image）

**说明（Help）**

选择此选项，为支持可信执行（Trusted Execution）的平台构建非安全固件镜像（Non-Secure Firmware Image）。非安全固件镜像在非安全，即普通状态（Non-Secure/Normal State）下执行，因此不得访问属于安全域（Secure Domain）的 CPU 资源，包括内存区域、外设、中断等。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_TRUSTED_EXECUTION_SECURE && CONFIG_ARCH_HAS_TRUSTED_EXECUTION
```

**定义位置（Location）**：[`arch/Kconfig:386`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L386)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_TRUSTED_EXECUTION_SECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_SECURE)、[`CONFIG_ARCH_HAS_TRUSTED_EXECUTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_TRUSTED_EXECUTION)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_TRUSTED_EXECUTION`。

<a id="CONFIG_TRUSTED_EXECUTION_SECURE"></a>

## 27.34 `CONFIG_TRUSTED_EXECUTION_SECURE`

**提示（Prompt）**：可信执行（Trusted Execution）：安全固件镜像（Secure Firmware Image）

**说明（Help）**

选择此选项，为支持可信执行（Trusted Execution）的平台构建安全固件镜像（Secure Firmware Image）。安全固件镜像在安全状态（Secure State）下执行，并可允许 CPU 在非安全，即普通状态（Non-Secure/Normal State）下执行。因此，安全固件镜像应能配置内存区域、外设、中断等 CPU 资源的安全属性（Security Attribution），并处理安全违规（Security Violation）相关故障。还可选择允许从非安全域调用某些函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_TRUSTED_EXECUTION
```

**定义位置（Location）**：[`arch/Kconfig:372`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L372)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_TRUSTED_EXECUTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_TRUSTED_EXECUTION)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_TRUSTED_EXECUTION`。

<a id="CONFIG_USERSPACE"></a>

## 27.35 `CONFIG_USERSPACE`

**提示（Prompt）**：用户模式线程（User Mode Threads）

**说明（Help）**

启用后，可以创建用户模式（User Mode）线程，或将线程降至用户模式。该模式的权限受到显著限制，必须通过系统调用（System Call）与内核交互；更多详情参见 Zephyr 文档。用户线程栈溢出（Stack Overflow）会被捕获，内核自身受到保护，不会因此受损。启用此选项不一定能捕获系统处于特权模式或正在处理系统调用时发生的栈溢出；若要确保始终捕获这些情况，请启用 `CONFIG_HW_STACK_PROTECTION`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_USERSPACE && CONFIG_SRAM_REGION_PERMISSIONS
```

**主动选择（Selects）**

```text
CONFIG_THREAD_STACK_INFO
CONFIG_LINKER_USE_NO_RELAX
```

**被选择（Selected by）**

```text
CONFIG_TEST_ENABLE_USERSPACE
```

**定义位置（Location）**：[`arch/Kconfig:412`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L412)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_USERSPACE)、[`CONFIG_SRAM_REGION_PERMISSIONS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_REGION_PERMISSIONS)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_LINKER_USE_NO_RELAX`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_USE_NO_RELAX)、[`CONFIG_TEST_ENABLE_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_ENABLE_USERSPACE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_USERSPACE`。

<a id="CONFIG_X86"></a>

## 27.36 `CONFIG_X86`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

x86 架构（Architecture）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_ARCH_IS_SET
CONFIG_ATOMIC_OPERATIONS_BUILTIN
CONFIG_ARCH_SUPPORTS_COREDUMP
CONFIG_ARCH_SUPPORTS_COREDUMP_PRIV_STACKS
CONFIG_ARCH_SUPPORTS_ROM_START if !CONFIG_X86_64
CONFIG_CPU_HAS_MMU
CONFIG_ARCH_MEM_DOMAIN_DATA if CONFIG_USERSPACE && !CONFIG_X86_COMMON_PAGE_TABLE
CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API if CONFIG_USERSPACE
CONFIG_ARCH_HAS_GDBSTUB if !CONFIG_X86_64
CONFIG_ARCH_HAS_TIMING_FUNCTIONS
CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE
CONFIG_ARCH_HAS_DEMAND_PAGING if !CONFIG_X86_64
CONFIG_ARCH_HAS_DEMAND_MAPPING if CONFIG_ARCH_HAS_DEMAND_PAGING
CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING if CONFIG_ARCH_HAS_DEMAND_PAGING && !CONFIG_X86_KPTI
CONFIG_EVICTION_TRACKING if CONFIG_DEMAND_PAGING && !CONFIG_X86_KPTI
CONFIG_NEED_LIBC_MEM_PARTITION if CONFIG_USERSPACE && CONFIG_TIMING_FUNCTIONS && !CONFIG_BOARD_HAS_TIMING_FUNCTIONS && !CONFIG_SOC_HAS_TIMING_FUNCTIONS
CONFIG_ARCH_HAS_STACK_CANARIES_TLS
CONFIG_ARCH_SUPPORTS_MEM_MAPPED_STACKS if CONFIG_X86_MMU && !CONFIG_DEMAND_PAGING
CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET if CONFIG_USERSPACE
CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED
CONFIG_ARCH_SUPPORTS_ROM_OFFSET
CONFIG_ARCH_HAS_CPU_IDLE_HOOKS if !CONFIG_X86_64
CONFIG_ARCH_HAS_DIRECT_INTERRUPTS if !CONFIG_X86_64
```

**被选择（Selected by）**

```text
CONFIG_SOC_ELKHART_LAKE
CONFIG_SOC_NOVA_LAKE
CONFIG_SOC_ATOM
CONFIG_SOC_WILDCAT_LAKE
CONFIG_SOC_FAMILY_INTEL_ISH
CONFIG_SOC_ALDER_LAKE
CONFIG_SOC_LAKEMONT
CONFIG_SOC_RAPTOR_LAKE
CONFIG_SOC_APOLLO_LAKE
CONFIG_SOC_PANTHER_LAKE
```

**定义位置（Location）**：[`arch/Kconfig:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L114)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_IS_SET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_IS_SET)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_ARCH_SUPPORTS_COREDUMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP)、[`CONFIG_ARCH_SUPPORTS_COREDUMP_PRIV_STACKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP_PRIV_STACKS)、[`CONFIG_ARCH_SUPPORTS_ROM_START`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_ROM_START)、[`CONFIG_X86_64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_64)、[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_ARCH_MEM_DOMAIN_DATA`](P001_kernel_配置项参考_1.md#CONFIG_ARCH_MEM_DOMAIN_DATA)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_X86_COMMON_PAGE_TABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_COMMON_PAGE_TABLE)、[`CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API`](P001_kernel_配置项参考_1.md#CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API)、[`CONFIG_ARCH_HAS_GDBSTUB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_GDBSTUB)、[`CONFIG_ARCH_HAS_TIMING_FUNCTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_TIMING_FUNCTIONS)、[`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE)、[`CONFIG_ARCH_HAS_DEMAND_PAGING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DEMAND_PAGING)、[`CONFIG_ARCH_HAS_DEMAND_MAPPING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DEMAND_MAPPING)、[`CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING)、[`CONFIG_X86_KPTI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_KPTI)、[`CONFIG_EVICTION_TRACKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EVICTION_TRACKING)、[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)、[`CONFIG_NEED_LIBC_MEM_PARTITION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NEED_LIBC_MEM_PARTITION)、[`CONFIG_TIMING_FUNCTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TIMING_FUNCTIONS)、[`CONFIG_BOARD_HAS_TIMING_FUNCTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_HAS_TIMING_FUNCTIONS)、[`CONFIG_SOC_HAS_TIMING_FUNCTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_HAS_TIMING_FUNCTIONS)、[`CONFIG_ARCH_HAS_STACK_CANARIES_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACK_CANARIES_TLS)、[`CONFIG_ARCH_SUPPORTS_MEM_MAPPED_STACKS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_SUPPORTS_MEM_MAPPED_STACKS)、[`CONFIG_X86_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_MMU)、[`CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET)、[`CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED)、[`CONFIG_ARCH_SUPPORTS_ROM_OFFSET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_ROM_OFFSET)、[`CONFIG_ARCH_HAS_CPU_IDLE_HOOKS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CPU_IDLE_HOOKS)、[`CONFIG_ARCH_HAS_DIRECT_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DIRECT_INTERRUPTS)、[`CONFIG_SOC_ELKHART_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ELKHART_LAKE)、[`CONFIG_SOC_NOVA_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NOVA_LAKE)、[`CONFIG_SOC_ATOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATOM)、[`CONFIG_SOC_WILDCAT_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_WILDCAT_LAKE)、[`CONFIG_SOC_FAMILY_INTEL_ISH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ISH)、[`CONFIG_SOC_ALDER_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ALDER_LAKE)、[`CONFIG_SOC_LAKEMONT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LAKEMONT)、[`CONFIG_SOC_RAPTOR_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RAPTOR_LAKE)、[`CONFIG_SOC_APOLLO_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_APOLLO_LAKE)、[`CONFIG_SOC_PANTHER_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PANTHER_LAKE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_SUPPORTS_COREDUMP`、`CONFIG_ARCH_SUPPORTS_COREDUMP_PRIV_STACKS`、`CONFIG_ARCH_SUPPORTS_ROM_START`、`CONFIG_ARCH_HAS_GDBSTUB`、`CONFIG_ARCH_HAS_TIMING_FUNCTIONS`、`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`、`CONFIG_ARCH_HAS_STACK_CANARIES_TLS`、`CONFIG_SOC_ELKHART_LAKE`、`CONFIG_SOC_NOVA_LAKE`、`CONFIG_SOC_ATOM`、`CONFIG_SOC_WILDCAT_LAKE`、`CONFIG_SOC_FAMILY_INTEL_ISH`、`CONFIG_SOC_ALDER_LAKE`、`CONFIG_SOC_LAKEMONT`、`CONFIG_SOC_RAPTOR_LAKE`、`CONFIG_SOC_APOLLO_LAKE`、`CONFIG_SOC_PANTHER_LAKE`。

<a id="CONFIG_XIP"></a>

## 27.37 `CONFIG_XIP`

**提示（Prompt）**：就地执行（Execute in Place）

**说明（Help）**

直接从 Flash/MRAM 等非易失存储器（Non-volatile Storage）执行应用代码，无需先复制到 RAM。并非所有目标都支持此选项，因此必须谨慎使用。启用后，链接器使代码段 `.text` 和只读数据段 `.rodata` 的加载内存地址（Load Memory Address，LMA）与虚拟内存地址（Virtual Memory Address，VMA）一致，使它们直接从存储位置读取。可修改的已初始化数据 `.data` 仍在早期启动阶段复制到 RAM。

这会减少 RAM 使用量，但执行速度慢于从 RAM 运行。运行前会重定位到 RAM 的应用，例如为 RAM 加载式引导加载程序模式构建的应用，应禁用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RA0E1
CONFIG_SOC_SERIES_RA2A1
CONFIG_SOC_SERIES_RA4C1
CONFIG_SOC_SERIES_RA4E1
CONFIG_SOC_SERIES_RA4E2
CONFIG_SOC_SERIES_RA4L1
CONFIG_SOC_SERIES_RA4M1
CONFIG_SOC_SERIES_RA4M2
CONFIG_SOC_SERIES_RA4M3
CONFIG_SOC_SERIES_RA4T1
CONFIG_SOC_SERIES_RA4W1
CONFIG_SOC_SERIES_RA6E1
CONFIG_SOC_SERIES_RA6E2
CONFIG_SOC_SERIES_RA6M1
CONFIG_SOC_SERIES_RA6M2
CONFIG_SOC_SERIES_RA6M3
CONFIG_SOC_SERIES_RA6M4
CONFIG_SOC_SERIES_RA6M5
CONFIG_SOC_SERIES_RA8D1
CONFIG_SOC_SERIES_RA8D2
CONFIG_SOC_SERIES_RA8E1
CONFIG_SOC_SERIES_RA8M1
CONFIG_SOC_SERIES_RA8M2
CONFIG_SOC_SERIES_RA8P1
CONFIG_SOC_SERIES_RA8T1
CONFIG_SOC_SERIES_RA8T2
CONFIG_FLASH_MCUX_FLEXSPI_XIP
CONFIG_FLASH_MCUX_FLEXSPI_XIP
CONFIG_FLASH_MCUX_XSPI_XIP
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
CONFIG_SOC_SERIES_GD32VF103
CONFIG_SOC_FAMILY_ENSEMBLE_RTSS
CONFIG_SOC_SERIES_RX130
CONFIG_SOC_SERIES_RX140
CONFIG_SOC_SERIES_RX14T
CONFIG_SOC_SERIES_RX261
CONFIG_SOC_SERIES_RX26T
CONFIG_SOC_SERIES_RX62N
CONFIG_SOC_SERIES_RX74M
CONFIG_SOC_SERIES_RX74N
CONFIG_SOC_OPENISA_RV32M1
CONFIG_SOC_SERIES_SAMX7X
CONFIG_SOC_SERIES_RTL87X2G
CONFIG_SOC_RTS5817
CONFIG_SOC_SERIES_STM32MP13X
CONFIG_FLASH_MCUX_FLEXSPI_XIP
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL616CL
CONFIG_SOC_SERIES_BL61X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_SERIES_BL808
CONFIG_SOC_NEORV32
CONFIG_SOC_RISCV_VIRTUAL_RENODE
CONFIG_SOC_FAMILY_CH32V
CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV
CONFIG_SOC_SERIES_RP2040
CONFIG_SOC_SERIES_RP2350
CONFIG_RISCV_CORE_NORDIC_VPR
CONFIG_SOC_SERIES_NRF51
CONFIG_SOC_SERIES_NRF52
CONFIG_SOC_SERIES_NRF53
CONFIG_SOC_SERIES_NRF91
CONFIG_SOC_OPENTITAN
CONFIG_SOC_SERIES_AE350
CONFIG_SOC_IT51XXX
CONFIG_SOC_IT8XXX2
CONFIG_SOC_SERIES_TLSR951X
CONFIG_SOC_FAMILY_ENSEMBLE_APSS
CONFIG_SOC_SERIES_B1
CONFIG_SOC_SERIES_NIOSV
CONFIG_SOC_SERIES_PIC64GX
CONFIG_SOC_FAMILY_MAX32_RV32
CONFIG_SOC_SERIES_RHX
CONFIG_SOC_SERIES_RMX
CONFIG_SOC_EGIS_ET171
CONFIG_SOC_SERIES_STARFIVE_JH71XX
CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1
CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3
CONFIG_SOC_SERIES_MIV
CONFIG_SOC_SERIES_POLARFIRE
CONFIG_SOC_EFINIX_SAPPHIRE
CONFIG_SOC_SERIES_FE300
CONFIG_SOC_SERIES_FU500
CONFIG_SOC_SERIES_FU700
CONFIG_CPU_CORTEX_M
CONFIG_ARC
CONFIG_TRICORE
```

**定义位置（Location）**：[`arch/Kconfig:326`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L326)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA0E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA0E1)、[`CONFIG_SOC_SERIES_RA2A1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2A1)、[`CONFIG_SOC_SERIES_RA4C1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4C1)、[`CONFIG_SOC_SERIES_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_SOC_SERIES_RA4E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E2)、[`CONFIG_SOC_SERIES_RA4L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4L1)、[`CONFIG_SOC_SERIES_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_SOC_SERIES_RA4M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M2)、[`CONFIG_SOC_SERIES_RA4M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M3)、[`CONFIG_SOC_SERIES_RA4T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4T1)、[`CONFIG_SOC_SERIES_RA4W1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4W1)、[`CONFIG_SOC_SERIES_RA6E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E1)、[`CONFIG_SOC_SERIES_RA6E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E2)、[`CONFIG_SOC_SERIES_RA6M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M1)、[`CONFIG_SOC_SERIES_RA6M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M2)、[`CONFIG_SOC_SERIES_RA6M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M3)、[`CONFIG_SOC_SERIES_RA6M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_SERIES_RA6M5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_SERIES_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_SERIES_RA8D2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_SERIES_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_SERIES_RA8M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_SERIES_RA8T2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_FLASH_MCUX_FLEXSPI_XIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MCUX_FLEXSPI_XIP)、[`CONFIG_FLASH_MCUX_XSPI_XIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MCUX_XSPI_XIP)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_SERIES_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32VF103)、[`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_RTSS)、[`CONFIG_SOC_SERIES_RX130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX130)、[`CONFIG_SOC_SERIES_RX140`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX140)、[`CONFIG_SOC_SERIES_RX14T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX14T)、[`CONFIG_SOC_SERIES_RX261`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX261)、[`CONFIG_SOC_SERIES_RX26T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX26T)、[`CONFIG_SOC_SERIES_RX62N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX62N)、[`CONFIG_SOC_SERIES_RX74M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74M)、[`CONFIG_SOC_SERIES_RX74N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74N)、[`CONFIG_SOC_OPENISA_RV32M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENISA_RV32M1)、[`CONFIG_SOC_SERIES_SAMX7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMX7X)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)、[`CONFIG_SOC_RTS5817`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTS5817)、[`CONFIG_SOC_SERIES_STM32MP13X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP13X)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL616CL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL616CL)、[`CONFIG_SOC_SERIES_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL61X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_SERIES_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL808)、[`CONFIG_SOC_NEORV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NEORV32)、[`CONFIG_SOC_RISCV_VIRTUAL_RENODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RISCV_VIRTUAL_RENODE)、[`CONFIG_SOC_FAMILY_CH32V`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_CH32V)、[`CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV)、[`CONFIG_SOC_SERIES_RP2040`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2040)、[`CONFIG_SOC_SERIES_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2350)、[`CONFIG_RISCV_CORE_NORDIC_VPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_CORE_NORDIC_VPR)、[`CONFIG_SOC_SERIES_NRF51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_SOC_SERIES_NRF52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_SERIES_NRF53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_SERIES_NRF91`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_OPENTITAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENTITAN)、[`CONFIG_SOC_SERIES_AE350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)、[`CONFIG_SOC_IT51XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51XXX)、[`CONFIG_SOC_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2)、[`CONFIG_SOC_SERIES_TLSR951X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TLSR951X)、[`CONFIG_SOC_FAMILY_ENSEMBLE_APSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_APSS)、[`CONFIG_SOC_SERIES_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_B1)、[`CONFIG_SOC_SERIES_NIOSV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NIOSV)、[`CONFIG_SOC_SERIES_PIC64GX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PIC64GX)、[`CONFIG_SOC_FAMILY_MAX32_RV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_RV32)、[`CONFIG_SOC_SERIES_RHX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RHX)、[`CONFIG_SOC_SERIES_RMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RMX)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)、[`CONFIG_SOC_SERIES_STARFIVE_JH71XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STARFIVE_JH71XX)、[`CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1)、[`CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3)、[`CONFIG_SOC_SERIES_MIV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MIV)、[`CONFIG_SOC_SERIES_POLARFIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_POLARFIRE)、[`CONFIG_SOC_EFINIX_SAPPHIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFINIX_SAPPHIRE)、[`CONFIG_SOC_SERIES_FE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FE300)、[`CONFIG_SOC_SERIES_FU500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU500)、[`CONFIG_SOC_SERIES_FU700`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU700)、[`CONFIG_CPU_CORTEX_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_TRICORE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRICORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`、`CONFIG_SOC_RTS5817`、`CONFIG_SOC_SERIES_STM32MP13X`、`CONFIG_SOC_FAMILY_CH32V`、`CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV`、`CONFIG_SOC_SERIES_RP2350`、`CONFIG_SOC_OPENTITAN`、`CONFIG_SOC_IT51XXX`、`CONFIG_SOC_IT8XXX2`、`CONFIG_SOC_FAMILY_ENSEMBLE_APSS`、`CONFIG_SOC_SERIES_B1`、`CONFIG_SOC_FAMILY_MAX32_RV32`、`CONFIG_SOC_SERIES_RHX`、`CONFIG_SOC_SERIES_RMX`、`CONFIG_SOC_SERIES_FE300`、`CONFIG_SOC_SERIES_FU500`、`CONFIG_SOC_SERIES_FU700`。

<a id="CONFIG_XTENSA"></a>

## 27.38 `CONFIG_XTENSA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Xtensa 架构（Architecture）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_ARCH_IS_SET
CONFIG_USE_SWITCH
CONFIG_USE_SWITCH_SUPPORTED
CONFIG_ARCH_HAS_CODE_DATA_RELOCATION
CONFIG_ARCH_HAS_TIMING_FUNCTIONS
CONFIG_ARCH_MEM_DOMAIN_DATA if CONFIG_USERSPACE
CONFIG_THREAD_STACK_INFO
CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET if CONFIG_USERSPACE
CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR if !CONFIG_SMP
CONFIG_ARCH_HAS_USERSPACE if CONFIG_XTENSA_MMU || CONFIG_XTENSA_MPU
CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED
CONFIG_ARCH_HAS_SEMIHOST
CONFIG_ARCH_HAS_CPU_IDLE_HOOKS
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_ESP32
CONFIG_SOC_SERIES_ESP32S2
CONFIG_SOC_SERIES_ESP32S3
CONFIG_SOC_MIMXRT595S_F1
CONFIG_SOC_MIMXRT685S_HIFI4
CONFIG_SOC_MIMXRT798S_HIFI1
CONFIG_SOC_MIMXRT758S_HIFI1
CONFIG_SOC_MIMXRT735S_HIFI1
CONFIG_SOC_MIMXRT798S_HIFI4
CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER
CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER32
CONFIG_SOC_MIMX8QM6_ADSP
CONFIG_SOC_MIMX8ML8_ADSP
CONFIG_SOC_MIMX8UD7_ADSP
CONFIG_SOC_MIMX8QX6_ADSP
CONFIG_SOC_ACP_7_X
CONFIG_SOC_SERIES_INTEL_ADSP_ACE
CONFIG_SOC_SERIES_INTEL_ADSP_CAVS
CONFIG_SOC_XTENSA_DC233C
CONFIG_SOC_ACP_7_0
CONFIG_SOC_ACP_6_0
CONFIG_SOC_MT8186_ADSP
CONFIG_SOC_MT8188_ADSP
CONFIG_SOC_MT8195_ADSP
CONFIG_SOC_MT8196_ADSP
CONFIG_SOC_MT8365_ADSP
```

**弱选择（Implies）**

```text
CONFIG_ARCH_HAS_RESERVED_PAGE_FRAMES if CONFIG_XTENSA_MMU
```

**定义位置（Location）**：[`arch/Kconfig:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L179)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_IS_SET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_IS_SET)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)、[`CONFIG_ARCH_HAS_CODE_DATA_RELOCATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CODE_DATA_RELOCATION)、[`CONFIG_ARCH_HAS_TIMING_FUNCTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_TIMING_FUNCTIONS)、[`CONFIG_ARCH_MEM_DOMAIN_DATA`](P001_kernel_配置项参考_1.md#CONFIG_ARCH_MEM_DOMAIN_DATA)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET)、[`CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_ARCH_HAS_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_USERSPACE)、[`CONFIG_XTENSA_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_MMU)、[`CONFIG_XTENSA_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_MPU)、[`CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED)、[`CONFIG_ARCH_HAS_SEMIHOST`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_SEMIHOST)、[`CONFIG_ARCH_HAS_CPU_IDLE_HOOKS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CPU_IDLE_HOOKS)、[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_MIMXRT595S_F1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_F1)、[`CONFIG_SOC_MIMXRT685S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_HIFI4)、[`CONFIG_SOC_MIMXRT798S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI1)、[`CONFIG_SOC_MIMXRT758S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_HIFI1)、[`CONFIG_SOC_MIMXRT735S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_HIFI1)、[`CONFIG_SOC_MIMXRT798S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI4)、[`CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER)、[`CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER32)、[`CONFIG_SOC_MIMX8QM6_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QM6_ADSP)、[`CONFIG_SOC_MIMX8ML8_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_ADSP)、[`CONFIG_SOC_MIMX8UD7_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8UD7_ADSP)、[`CONFIG_SOC_MIMX8QX6_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QX6_ADSP)、[`CONFIG_SOC_ACP_7_X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ACP_7_X)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)、[`CONFIG_SOC_SERIES_INTEL_ADSP_CAVS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_CAVS)、[`CONFIG_SOC_XTENSA_DC233C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XTENSA_DC233C)、[`CONFIG_SOC_ACP_7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ACP_7_0)、[`CONFIG_SOC_ACP_6_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ACP_6_0)、[`CONFIG_SOC_MT8186_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8186_ADSP)、[`CONFIG_SOC_MT8188_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8188_ADSP)、[`CONFIG_SOC_MT8195_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8195_ADSP)、[`CONFIG_SOC_MT8196_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8196_ADSP)、[`CONFIG_SOC_MT8365_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8365_ADSP)、[`CONFIG_ARCH_HAS_RESERVED_PAGE_FRAMES`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_RESERVED_PAGE_FRAMES)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_TIMING_FUNCTIONS`、`CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR`、`CONFIG_ARCH_HAS_USERSPACE`、`CONFIG_SOC_MIMXRT685S_HIFI4`、`CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER`、`CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER32`、`CONFIG_SOC_ACP_7_X`、`CONFIG_SOC_XTENSA_DC233C`、`CONFIG_SOC_ACP_7_0`、`CONFIG_SOC_ACP_6_0`。

<!-- kconfig-navigation -->

[上一章](P026_arch_Kconfig_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P028_arch_arc_配置项参考.md)
