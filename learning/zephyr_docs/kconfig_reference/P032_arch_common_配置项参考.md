---
id: learning.zephyr-docs.kconfig-reference.page-32
title: "`arch/common`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第32章\_`arch/common`配置项参考

本章翻译官方 Kconfig 数据库中 `arch/common` 的 26 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ACPI"></a>

## 32.1 `CONFIG_ACPI`

**提示（Prompt）**：高级配置与电源接口（ACPI）支持

**说明（Help）**

启用 ACPI 驱动（Driver）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_PCIE_MMIO_CFG
```

**定义位置（Location）**：[`arch/common/acpi/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/acpi/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_PCIE_MMIO_CFG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE_MMIO_CFG)。

<a id="CONFIG_ACPI_DEV_MAX"></a>

## 32.2 `CONFIG_ACPI_DEV_MAX`

**提示（Prompt）**：最大子设备数量（Maximum Child Devices）

**说明（Help）**

ACPI 子设备（Child Device）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ACPI
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`arch/common/acpi/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/acpi/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 高级配置与电源接口（ACPI）支持

**配置项引用（Symbol References）**：[`CONFIG_ACPI`](P032_arch_common_配置项参考.md#CONFIG_ACPI)。

<a id="CONFIG_ACPI_IRQ_VECTOR_MAX"></a>

## 32.3 `CONFIG_ACPI_IRQ_VECTOR_MAX`

**提示（Prompt）**：每个设备的中断向量数量（Interrupt Vectors per Device）

**说明（Help）**

每个设备允许的最大中断向量（Interrupt Vector）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ACPI
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`arch/common/acpi/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/acpi/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 高级配置与电源接口（ACPI）支持

**配置项引用（Symbol References）**：[`CONFIG_ACPI`](P032_arch_common_配置项参考.md#CONFIG_ACPI)。

<a id="CONFIG_ACPI_MAX_PRT_ENTRY"></a>

## 32.4 `CONFIG_ACPI_MAX_PRT_ENTRY`

**提示（Prompt）**：PRT 缓冲区大小（PRT Buffer Size）

**说明（Help）**

PRT 表缓冲区（PRT Table Buffer）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PCIE_PRT && CONFIG_ACPI
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`arch/common/acpi/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/acpi/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 高级配置与电源接口（ACPI）支持

**配置项引用（Symbol References）**：[`CONFIG_PCIE_PRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE_PRT)、[`CONFIG_ACPI`](P032_arch_common_配置项参考.md#CONFIG_ACPI)。

<a id="CONFIG_ACPI_MMIO_ENTRIES_MAX"></a>

## 32.5 `CONFIG_ACPI_MMIO_ENTRIES_MAX`

**提示（Prompt）**：每个设备的内存映射 I/O 条目数量（MMIO Entries per Device）

**说明（Help）**

每个设备允许的最大内存映射 I/O（MMIO）条目数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ACPI
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`arch/common/acpi/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/acpi/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 高级配置与电源接口（ACPI）支持

**配置项引用（Symbol References）**：[`CONFIG_ACPI`](P032_arch_common_配置项参考.md#CONFIG_ACPI)。

<a id="CONFIG_ACPI_POWEROFF"></a>

## 32.6 `CONFIG_ACPI_POWEROFF`

**提示（Prompt）**：通过将系统置于 S5 电源状态实现关机（Power Off）

**说明（Help）**

启用通过高级配置与电源接口（ACPI）关闭系统电源的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ACPI
```

**定义位置（Location）**：[`arch/common/acpi/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/acpi/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 高级配置与电源接口（ACPI）支持

**配置项引用（Symbol References）**：[`CONFIG_ACPI`](P032_arch_common_配置项参考.md#CONFIG_ACPI)。

<a id="CONFIG_ACPI_SHELL"></a>

## 32.7 `CONFIG_ACPI_SHELL`

**提示（Prompt）**：ACPI 命令行（Command Shell）

**说明（Help）**

启用内置命令行（Shell）中用于调试 ACPI 的命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_ACPI
```

**定义位置（Location）**：[`arch/common/acpi/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/acpi/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 高级配置与电源接口（ACPI）支持

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_ACPI`](P032_arch_common_配置项参考.md#CONFIG_ACPI)。

<a id="CONFIG_ARCH_HAS_WORD_GRANULAR_ACCESS_INSTR_MEM"></a>

## 32.8 `CONFIG_ARCH_HAS_WORD_GRANULAR_ACCESS_INSTR_MEM`

**提示（Prompt）**：按字粒度访问的指令存储器支持（Word Granular Access Instruction Memory）

**说明（Help）**

启用对按字节寻址（Byte Addressable）、按字粒度访问（Word Granular Access）的指令存储器的访问支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_WORD_GRANULAR_ACCESS
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_ESP32
CONFIG_SOC_SERIES_ESP32S2
CONFIG_SOC_SERIES_ESP32S3
```

**定义位置（Location）**：[`arch/common/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_WORD_GRANULAR_ACCESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WORD_GRANULAR_ACCESS)、[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)。

<a id="CONFIG_ARCH_SUPPORTS_ROM_OFFSET"></a>

## 32.9 `CONFIG_ARCH_SUPPORTS_ROM_OFFSET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于在链接器脚本（Linker Script）中启用只读存储器偏移（ROM Offset）支持的隐藏选项。它会在 ROM 区域起始位置放置一个大小为 `CONFIG_ROM_START_OFFSET`、内容为 `0x0` 的块。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARC
CONFIG_ARM
CONFIG_ARM64
CONFIG_X86
CONFIG_RISCV
```

**定义位置（Location）**：[`arch/common/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_ARM_BTI"></a>

## 32.10 `CONFIG_ARM_BTI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示已启用分支目标标识（Branch Target Identification，BTI）。

注意：BTI 要求使用 `-mbranch-protection` 编译 C 库，以包含 BTI 着陆点（Landing Pad）指令。工具链提供的 Newlib 缺少这项支持，因此 BTI 只能使用最小 C 库（Minimal libc），或通过 `PICOLIBC_USE_MODULE` 从源码构建的 picolibc。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MINIMAL_LIBC || CONFIG_PICOLIBC_USE_MODULE
```

**被选择（Selected by）**

```text
CONFIG_ARM_PACBTI_STANDARD
CONFIG_ARM_PACBTI_BTI
CONFIG_ARM_PACBTI_PACRET_BTI
CONFIG_ARM_PACBTI_PACRET_LEAF_BTI
```

**定义位置（Location）**：[`arch/common/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_MINIMAL_LIBC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MINIMAL_LIBC)、[`CONFIG_PICOLIBC_USE_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOLIBC_USE_MODULE)、[`CONFIG_ARM_PACBTI_STANDARD`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_STANDARD)、[`CONFIG_ARM_PACBTI_BTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_BTI)、[`CONFIG_ARM_PACBTI_PACRET_BTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_PACRET_BTI)、[`CONFIG_ARM_PACBTI_PACRET_LEAF_BTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_PACRET_LEAF_BTI)。

<a id="CONFIG_ARM_MPU"></a>

## 32.11 `CONFIG_ARM_MPU`

**提示（Prompt）**：ARM 内存保护单元支持（MPU Support）

**说明（Help）**

微控制器（MCU）实现了内存保护单元（Memory Protection Unit，MPU）。

注意：ARMv6-M、ARMv7-M 和 ARMv8-R MPU 架构要求 MPU 区域的基地址与大小按 2 的幂对齐（Power-of-Two Alignment）。NXP MPU 和 ARMv8-M MPU 不要求区域基地址与区域大小按 2 的幂对齐。

ARMv8-M 和 ARMv8-R MPU 要求有效 MPU 区域互不重叠。因此，当系统要求的特权访问策略（PRIV Access Policy）不同于 ARMv8-M 或 ARMv8-R 背景内存映射（Background Memory Map）的访问策略时，这两类 MPU 在配置动态内存区域时必须对内存映射进行完整分区（Full Partition）。动态区域例如特权栈保护区（PRIV Stack Guard）、用户线程栈（User Thread Stack）和应用内存域（Application Memory Domain）。

应用开发者可以启用 `MPU_GAP_FILLING` 选项，强制完整的特权／内核（PRIV / Kernel）内存分区。如果不强制完整分区，部分内核 SRAM 区域可能仅受 ARMv8-M 或 ARMv8-R 默认内存映射覆盖。这对用户模式（User Mode）没有问题，因为 ARM 背景映射完全不允许非特权（nPRIV）访问。

然而，背景映射策略允许特权代码取指（Instruction Fetch），因此强制关闭该 Kconfig 选项后，在就地执行（XIP）构建中意外尝试从 SRAM 执行代码时，系统无法直接触发内存管理异常（MemManage Exception）。由于这不会损害用户模式的保护，ARMv8-M 和 ARMv8-R MPU 驱动默认跳过完整分区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_MPU
```

**默认值（Defaults）**

```text
y if CONFIG_CPU_AARCH64_CORTEX_R
```

**主动选择（Selects）**

```text
CONFIG_MPU
CONFIG_SRAM_REGION_PERMISSIONS
CONFIG_THREAD_STACK_INFO
CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT if CONFIG_CPU_AARCH32_CORTEX_R || CONFIG_CPU_CORTEX_M
CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT if !(CONFIG_CPU_HAS_NXP_SYSMPU || CONFIG_ARMV8_M_BASELINE || CONFIG_ARMV8_M_MAINLINE || CONFIG_AARCH32_ARMV8_R)
CONFIG_MPU_REQUIRES_NON_OVERLAPPING_REGIONS if CONFIG_CPU_HAS_ARM_MPU && (CONFIG_ARMV8_M_BASELINE || CONFIG_ARMV8_M_MAINLINE || CONFIG_AARCH32_ARMV8_R)
CONFIG_MPU_GAP_FILLING if CONFIG_AARCH32_ARMV8_R
CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_ISOLATED_STACKS if CONFIG_CPU_AARCH32_CORTEX_R || CONFIG_CPU_CORTEX_M
CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API if CONFIG_USERSPACE && CONFIG_CPU_AARCH64_CORTEX_R
```

**被选择（Selected by）**

```text
CONFIG_SOC_R8A78000_R52
CONFIG_SOC_SR100
CONFIG_SOC_SERIES_RA8D1
CONFIG_SOC_SERIES_RA8D2
CONFIG_SOC_SERIES_RA8M1
CONFIG_SOC_SERIES_RA8M2
CONFIG_SOC_SERIES_RA8P1
CONFIG_SOC_SERIES_RA8T1
CONFIG_SOC_SERIES_RA8T2
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_SERIES_M333X
CONFIG_SOC_SERIES_M335X
CONFIG_SOC_SERIES_M55M1X
CONFIG_SOC_SERIES_AMEBAD
CONFIG_SOC_SERIES_AMEBADPLUS
CONFIG_SOC_SERIES_AMEBAG2
CONFIG_SOC_MIMX8ML8_M7
CONFIG_SOC_MIMX9352_M33
CONFIG_SOC_MIMX94398_M33
CONFIG_SOC_MIMX94398_M7_0
CONFIG_SOC_MIMX94398_M7_1
CONFIG_SOC_MIMX9596_M7
CONFIG_SOC_MIMX9529_M7
CONFIG_SOC_VERSAL_RPU
CONFIG_SOC_AMD_VERSALNET_RPU
CONFIG_SOC_AMD_VERSAL2_RPU
CONFIG_ETH_NXP_ENET
CONFIG_ETH_DWC_ETHER_QOS_CORE
CONFIG_ETH_DWC_ETHER_1000_CORE
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_XILINX_ZYNQMP_RPU
```

**定义位置（Location）**：[`arch/common/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_MPU`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU)、[`CONFIG_SRAM_REGION_PERMISSIONS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_REGION_PERMISSIONS)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT)、[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT)、[`CONFIG_CPU_HAS_NXP_SYSMPU`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_NXP_SYSMPU)、[`CONFIG_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_BASELINE)、[`CONFIG_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_MAINLINE)、[`CONFIG_AARCH32_ARMV8_R`](P029_arch_arm_配置项参考_1.md#CONFIG_AARCH32_ARMV8_R)、[`CONFIG_MPU_REQUIRES_NON_OVERLAPPING_REGIONS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU_REQUIRES_NON_OVERLAPPING_REGIONS)、[`CONFIG_CPU_HAS_ARM_MPU`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_ARM_MPU)、[`CONFIG_MPU_GAP_FILLING`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU_GAP_FILLING)、[`CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_ISOLATED_STACKS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_ISOLATED_STACKS)、[`CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API`](P001_kernel_配置项参考_1.md#CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_SOC_R8A78000_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A78000_R52)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_SERIES_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_SERIES_RA8D2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_SERIES_RA8M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_SERIES_RA8T2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_SERIES_M333X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M333X)、[`CONFIG_SOC_SERIES_M335X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M335X)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_SOC_SERIES_AMEBADPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBADPLUS)、[`CONFIG_SOC_SERIES_AMEBAG2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAG2)、[`CONFIG_SOC_MIMX8ML8_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_M7)、[`CONFIG_SOC_MIMX9352_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_M33)、[`CONFIG_SOC_MIMX94398_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M33)、[`CONFIG_SOC_MIMX94398_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_0)、[`CONFIG_SOC_MIMX94398_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_1)、[`CONFIG_SOC_MIMX9596_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596_M7)、[`CONFIG_SOC_MIMX9529_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529_M7)、[`CONFIG_SOC_VERSAL_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VERSAL_RPU)、[`CONFIG_SOC_AMD_VERSALNET_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_RPU)、[`CONFIG_SOC_AMD_VERSAL2_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_RPU)、[`CONFIG_ETH_NXP_ENET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_NXP_ENET)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_SOC_XILINX_ZYNQMP_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XILINX_ZYNQMP_RPU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT`、`CONFIG_SOC_SR100`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_SERIES_AMEBADPLUS`、`CONFIG_SOC_SERIES_AMEBAG2`。

<a id="CONFIG_ARM_PAC"></a>

## 32.12 `CONFIG_ARM_PAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示已启用指针认证码（Pointer Authentication Code，PAC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARM_PACBTI_STANDARD
CONFIG_ARM_PACBTI_PACRET
CONFIG_ARM_PACBTI_PACRET_LEAF
CONFIG_ARM_PACBTI_PACRET_BTI
CONFIG_ARM_PACBTI_PACRET_LEAF_BTI
```

**定义位置（Location）**：[`arch/common/Kconfig:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_PACBTI_STANDARD`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_STANDARD)、[`CONFIG_ARM_PACBTI_PACRET`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_PACRET)、[`CONFIG_ARM_PACBTI_PACRET_LEAF`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_PACRET_LEAF)、[`CONFIG_ARM_PACBTI_PACRET_BTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_PACRET_BTI)、[`CONFIG_ARM_PACBTI_PACRET_LEAF_BTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_PACRET_LEAF_BTI)。

<a id="CONFIG_ARM_PACBTI"></a>

## 32.13 `CONFIG_ARM_PACBTI`

**提示（Prompt）**：指针认证与分支目标标识（Pointer Authentication and Branch Target Identification，PACBTI）

**说明（Help）**

选择 PACBTI 配置，使编译器插入所需的指针认证与分支目标标识（Pointer Authentication and Branch Target Identification，PACBTI）指令。这还会设置必要的配置选项，以启用硬件中的 PACBTI 位。

对于 ARM32，PACBTI 在 ARMv8.1-M 主线（Mainline）处理器上可用。对于 ARM64，PAC 要求 ARMv8.3-A 或更新版本，BTI 要求 ARMv8.5-A 或更新版本。ARMv9-A 将这两者都列为必需特性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV8_1_M_MAINLINE || CONFIG_ARMV8_A || CONFIG_ARMV9_A
```

**默认值（Defaults）**

```text
CONFIG_ARM_PACBTI_NONE
```

**可选项（Choices）**

```text
CONFIG_ARM_PACBTI_STANDARD
CONFIG_ARM_PACBTI_PACRET
CONFIG_ARM_PACBTI_PACRET_LEAF
CONFIG_ARM_PACBTI_BTI
CONFIG_ARM_PACBTI_PACRET_BTI
CONFIG_ARM_PACBTI_PACRET_LEAF_BTI
CONFIG_ARM_PACBTI_NONE
```

**定义位置（Location）**：[`arch/common/Kconfig:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV8_1_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_1_M_MAINLINE)、[`CONFIG_ARMV8_A`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV8_A)、[`CONFIG_ARMV9_A`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV9_A)、[`CONFIG_ARM_PACBTI_NONE`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_NONE)、[`CONFIG_ARM_PACBTI_STANDARD`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_STANDARD)、[`CONFIG_ARM_PACBTI_PACRET`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_PACRET)、[`CONFIG_ARM_PACBTI_PACRET_LEAF`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_PACRET_LEAF)、[`CONFIG_ARM_PACBTI_BTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_BTI)、[`CONFIG_ARM_PACBTI_PACRET_BTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_PACRET_BTI)、[`CONFIG_ARM_PACBTI_PACRET_LEAF_BTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI_PACRET_LEAF_BTI)。

<a id="CONFIG_ARM_PACBTI_BTI"></a>

## 32.14 `CONFIG_ARM_PACBTI_BTI`

**提示（Prompt）**：仅分支目标标识（BTI Only）

**说明（Help）**

启用分支目标标识（Branch Target Identification，BTI），在有效的间接分支目标处插入专用着陆点（Landing Pad）指令。此选项不启用指针认证（Pointer Authentication，PAC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_PACBTI>
```

**主动选择（Selects）**

```text
CONFIG_ARM_BTI
```

**定义位置（Location）**：[`arch/common/Kconfig:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 指针认证与分支目标标识（Pointer Authentication and Branch Target Identification，PACBTI）

**配置项引用（Symbol References）**：[`CONFIG_ARM_PACBTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI)、[`CONFIG_ARM_BTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_BTI)。

<a id="CONFIG_ARM_PACBTI_NONE"></a>

## 32.15 `CONFIG_ARM_PACBTI_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**

指示编译器生成不使用分支保护（Branch Protection）或返回地址签名（Return Address Signing）的代码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_PACBTI>
```

**定义位置（Location）**：[`arch/common/Kconfig:208`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L208)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 指针认证与分支目标标识（Pointer Authentication and Branch Target Identification，PACBTI）

**配置项引用（Symbol References）**：[`CONFIG_ARM_PACBTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI)。

<a id="CONFIG_ARM_PACBTI_PACRET"></a>

## 32.16 `CONFIG_ARM_PACBTI_PACRET`

**提示（Prompt）**：仅返回地址指针认证（PACRET Only）

**说明（Help）**

指示编译器为所有将返回地址保存到内存的函数生成返回地址签名（Return Address Signing）代码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_PACBTI>
```

**主动选择（Selects）**

```text
CONFIG_ARM_PAC
```

**定义位置（Location）**：[`arch/common/Kconfig:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 指针认证与分支目标标识（Pointer Authentication and Branch Target Identification，PACBTI）

**配置项引用（Symbol References）**：[`CONFIG_ARM_PACBTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI)、[`CONFIG_ARM_PAC`](P032_arch_common_配置项参考.md#CONFIG_ARM_PAC)。

<a id="CONFIG_ARM_PACBTI_PACRET_BTI"></a>

## 32.17 `CONFIG_ARM_PACBTI_PACRET_BTI`

**提示（Prompt）**：返回地址指针认证与分支目标标识（PACRET + BTI）

**说明（Help）**

指示编译器为所有将返回地址保存到内存的函数生成返回地址签名（Return Address Signing）代码，并在允许的间接分支指令目标处添加着陆点（Landing Pad）指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_PACBTI>
```

**主动选择（Selects）**

```text
CONFIG_ARM_PAC
CONFIG_ARM_BTI
```

**定义位置（Location）**：[`arch/common/Kconfig:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 指针认证与分支目标标识（Pointer Authentication and Branch Target Identification，PACBTI）

**配置项引用（Symbol References）**：[`CONFIG_ARM_PACBTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI)、[`CONFIG_ARM_PAC`](P032_arch_common_配置项参考.md#CONFIG_ARM_PAC)、[`CONFIG_ARM_BTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_BTI)。

<a id="CONFIG_ARM_PACBTI_PACRET_LEAF"></a>

## 32.18 `CONFIG_ARM_PACBTI_PACRET_LEAF`

**提示（Prompt）**：返回地址指针认证与叶函数签名（PACRET + Leaf）

**说明（Help）**

指示编译器为所有将返回地址保存到内存的函数生成返回地址签名（Return Address Signing）代码，同时也为叶函数（Leaf Function）签名，即使叶函数不将返回地址写入内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_PACBTI>
```

**主动选择（Selects）**

```text
CONFIG_ARM_PAC
```

**定义位置（Location）**：[`arch/common/Kconfig:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 指针认证与分支目标标识（Pointer Authentication and Branch Target Identification，PACBTI）

**配置项引用（Symbol References）**：[`CONFIG_ARM_PACBTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI)、[`CONFIG_ARM_PAC`](P032_arch_common_配置项参考.md#CONFIG_ARM_PAC)。

<a id="CONFIG_ARM_PACBTI_PACRET_LEAF_BTI"></a>

## 32.19 `CONFIG_ARM_PACBTI_PACRET_LEAF_BTI`

**提示（Prompt）**：返回地址指针认证、叶函数签名与分支目标标识（PACRET + Leaf + BTI）

**说明（Help）**

指示编译器为所有将返回地址保存到内存的函数生成返回地址签名（Return Address Signing）代码；同时也为叶函数（Leaf Function）签名，即使叶函数不将返回地址写入内存；并在允许的间接分支指令目标处添加着陆点（Landing Pad）指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_PACBTI>
```

**主动选择（Selects）**

```text
CONFIG_ARM_PAC
CONFIG_ARM_BTI
```

**定义位置（Location）**：[`arch/common/Kconfig:198`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L198)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 指针认证与分支目标标识（Pointer Authentication and Branch Target Identification，PACBTI）

**配置项引用（Symbol References）**：[`CONFIG_ARM_PACBTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI)、[`CONFIG_ARM_PAC`](P032_arch_common_配置项参考.md#CONFIG_ARM_PAC)、[`CONFIG_ARM_BTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_BTI)。

<a id="CONFIG_ARM_PACBTI_STANDARD"></a>

## 32.20 `CONFIG_ARM_PACBTI_STANDARD`

**提示（Prompt）**：标准配置（Standard：PACRET + LEAF + BTI）

**说明（Help）**

指示编译器生成代码，并以标准级别启用所有分支保护（Branch Protection）特性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_PACBTI>
```

**主动选择（Selects）**

```text
CONFIG_ARM_PAC
CONFIG_ARM_BTI
```

**定义位置（Location）**：[`arch/common/Kconfig:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 指针认证与分支目标标识（Pointer Authentication and Branch Target Identification，PACBTI）

**配置项引用（Symbol References）**：[`CONFIG_ARM_PACBTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_PACBTI)、[`CONFIG_ARM_PAC`](P032_arch_common_配置项参考.md#CONFIG_ARM_PAC)、[`CONFIG_ARM_BTI`](P032_arch_common_配置项参考.md#CONFIG_ARM_BTI)。

<a id="CONFIG_ARM_PAC_PER_THREAD"></a>

## 32.21 `CONFIG_ARM_PAC_PER_THREAD`

**提示（Prompt）**：为每个线程设置密码学安全的 PAC 密钥（Cryptographically Secure PAC Key）

**说明（Help）**

选择此选项，为每个线程生成并使用独立密钥，以生成指针认证码（Pointer Authentication Code，PAC）。内部在 `arch_new_thread()` 中使用 `sys_csrand_get()` 生成密码学安全的随机密钥（Cryptographically Secure Random Key），将其保存在该线程的架构专用上下文（Architecture-Specific Context）中。随后进行上下文切换（Context Switch）时，在切换到该线程之前，将这些密钥加载到 PAC 密钥寄存器。

应用可以从 `RNG_GENERATOR_CHOICE` 选择适当的生成器，以使用基于硬件的随机密钥生成器；也可以选择 `TIMER_RANDOM_GENERATOR`，使用伪随机密钥进行测试。

注意：此选项要求 GCC 14.3 或更高版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_PAC
```

**主动选择（Selects）**

```text
CONFIG_CSPRNG_NEEDED
```

**弱选择（Implies）**

```text
CONFIG_TEST_RANDOM_GENERATOR if !CONFIG_CSPRNG_ENABLED
```

**定义位置（Location）**：[`arch/common/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_PAC`](P032_arch_common_配置项参考.md#CONFIG_ARM_PAC)、[`CONFIG_CSPRNG_NEEDED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CSPRNG_NEEDED)、[`CONFIG_TEST_RANDOM_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_RANDOM_GENERATOR)、[`CONFIG_CSPRNG_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CSPRNG_ENABLED)。

<a id="CONFIG_EXCEPTION_DUMP"></a>

## 32.22 `CONFIG_EXCEPTION_DUMP`

**提示（Prompt）**：异常信息转储（Exception Dump）

**说明（Help）**

打印架构故障处理程序（Architecture Fault Handler）收集的寄存器、故障原因（Fault Cause）和栈回溯（Stack Trace）信息。禁用后，镜像会移除转储调用点及其格式字符串。

这适用于引导加载程序（Bootloader）等体积受限的构建。否则，只要禁用 `LOG`，这些转储就会无条件编译进镜像，因为后备的 `printk` 本身不提供日志级别过滤（Level Filtering）。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/common/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

<a id="CONFIG_EXCEPTION_DUMP_HOOK"></a>

## 32.23 `CONFIG_EXCEPTION_DUMP_HOOK`

**提示（Prompt）**：异常打印钩子（Exception Printing Hooks）

**说明（Help）**

启用钩子（Hook），以配置另一种异常信息输出方式，其接口与 `printk` 或 `LOG` 类似。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EXCEPTION_DUMP
```

**定义位置（Location）**：[`arch/common/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 异常信息转储（Exception Dump）

**配置项引用（Symbol References）**：[`CONFIG_EXCEPTION_DUMP`](P032_arch_common_配置项参考.md#CONFIG_EXCEPTION_DUMP)。

<a id="CONFIG_EXCEPTION_DUMP_HOOK_ONLY"></a>

## 32.24 `CONFIG_EXCEPTION_DUMP_HOOK_ONLY`

**提示（Prompt）**：设置钩子时不向日志或 printk 输出异常信息（Exception Prints）

**说明（Help）**

如果设置了异常钩子（Exception Hook），则不向日志或 `printk` 输出异常信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EXCEPTION_DUMP_HOOK
```

**定义位置（Location）**：[`arch/common/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 异常信息转储（Exception Dump） → 异常打印钩子（Exception Printing Hooks）

**配置项引用（Symbol References）**：[`CONFIG_EXCEPTION_DUMP_HOOK`](P032_arch_common_配置项参考.md#CONFIG_EXCEPTION_DUMP_HOOK)。

<a id="CONFIG_ISR_TABLE_SHELL"></a>

## 32.25 `CONFIG_ISR_TABLE_SHELL`

**提示（Prompt）**：用于转储中断服务例程表的命令行命令（ISR Table Dump）

**说明（Help）**

启用一个用于转储中断服务例程表（ISR Table）的命令行（Shell）命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_SW_ISR_TABLE && CONFIG_SHELL
```

**定义位置（Location）**：[`arch/common/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_GEN_SW_ISR_TABLE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_SW_ISR_TABLE)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)。

<a id="CONFIG_SEMIHOST"></a>

## 32.26 `CONFIG_SEMIHOST`

**提示（Prompt）**：ARM、RISC-V 和 Xtensa 目标的半主机支持（Semihosting Support）

**说明（Help）**

半主机（Semihosting）是一种机制，使运行在 ARM、RISC-V 或 Xtensa 目标上的代码能够与运行调试器（Debugger）的主机通信，并使用主机的输入／输出（Input/Output，I/O）设施。更多信息见：

[ARM 半主机说明](https://developer.arm.com/documentation/dui0471/m/what-is-semihosting-)

[RISC-V 半主机规范](https://github.com/riscv-non-isa/riscv-semihosting/blob/main/riscv-semihosting.adoc)

此选项同时适用于硬件和 QEMU；调用 QEMU 时会自动使用 `-semihosting-config` 开关。

译注：此 ARM 外部引用目前只返回文档应用外壳，未取得可核验的半主机说明正文。保留官方 Kconfig 原始地址，不将该外部正文记为已验证；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_SEMIHOST
```

**定义位置（Location）**：[`arch/common/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/common/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_SEMIHOST`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_SEMIHOST)。

<!-- kconfig-navigation -->

[上一章](P031_arch_arm64_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P033_arch_posix_配置项参考.md)
