---
id: learning.zephyr-docs.kconfig-reference.page-4
title: "`Kconfig.zephyr`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第4章\_`Kconfig.zephyr`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `Kconfig.zephyr` 的 22 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_OUTPUT_STAT"></a>

## 4.1 `CONFIG_OUTPUT_STAT`

**提示（Prompt）**：创建统计文件（Statistics File）。

**说明（Help）**

使用 `readelf -e <elf>` 创建统计文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`Kconfig.zephyr:695`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L695)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_OUTPUT_SYMBOLS"></a>

## 4.2 `CONFIG_OUTPUT_SYMBOLS`

**提示（Prompt）**：创建符号文件（Symbol File）。

**说明（Help）**

使用 `nm <elf>` 创建符号文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:701`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L701)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_REQUIRES_STD_C17"></a>

## 4.3 `CONFIG_REQUIRES_STD_C17`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，选择支持 C17 或更高版本标准的编译器能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_REQUIRES_STD_C23
```

**定义位置（Location）**：[`Kconfig.zephyr:370`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L370)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

**配置项引用（Symbol References）**：[`CONFIG_REQUIRES_STD_C23`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_REQUIRES_STD_C23)。

<a id="CONFIG_REQUIRES_STD_C23"></a>

## 4.4 `CONFIG_REQUIRES_STD_C23`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，选择支持 C23 或更高版本标准的编译器能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_REQUIRES_STD_C17
```

**定义位置（Location）**：[`Kconfig.zephyr:375`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L375)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

**配置项引用（Symbol References）**：[`CONFIG_REQUIRES_STD_C17`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_REQUIRES_STD_C17)。

<a id="CONFIG_ROM_END_OFFSET"></a>

## 4.5 `CONFIG_ROM_END_OFFSET`

**提示（Prompt）**：ROM 末尾偏移（ROM End Offset）。

**说明（Help）**

非零时，减少允许 Zephyr 镜像占用的最大空间，为其他系统（例如引导加载程序）创建和使用的附加镜像数据预留存储空间。对 MCUboot 而言，这包括镜像末尾的镜像交换字段及类型－长度－值（TLV）存储。若不确定，保持默认值 0。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`Kconfig.zephyr:183`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L183)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。

<a id="CONFIG_ROM_START_OFFSET"></a>

## 4.6 `CONFIG_ROM_START_OFFSET`

原库同名定义共 2 条；本项为数据库第 16260 条记录，各定义分别保留。

**提示（Prompt）**：ROM 起始偏移（ROM Start Offset）。

**说明（Help）**

如果应用由引导加载程序进行链式加载（Chain-loading），必须设置本变量，在镜像起点与第一个节起点之间预留足够空间，保存镜像头（Image Header）或其他元数据。对于 MCUboot，这既为镜像头保留足够空间，也满足 Cortex-M 目标的向量表对齐要求。向量表偏移寄存器（VTOR）的偏移必须按 `4 * (16 + NUM_IRQS)` 字节向上取整到 2 的幂后对齐，因此默认值随中断数量增加。存在额外要求的目标，例如镜像之前还需附加元数据，仍必须覆盖此值。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**默认值（Defaults）**

```text
0x1000 if CONFIG_BOOTLOADER_MCUBOOT && CONFIG_CPU_CORTEX_M && CONFIG_NUM_IRQS > 496
0x800 if CONFIG_BOOTLOADER_MCUBOOT && CONFIG_CPU_CORTEX_M && CONFIG_NUM_IRQS > 240
0x400 if CONFIG_BOOTLOADER_MCUBOOT && CONFIG_CPU_CORTEX_M && CONFIG_NUM_IRQS > 112
0x200 if CONFIG_BOOTLOADER_MCUBOOT
0
```

**定义位置（Location）**：[`Kconfig.zephyr:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_MCUBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOOTLOADER_MCUBOOT)、[`CONFIG_CPU_CORTEX_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M)、[`CONFIG_NUM_IRQS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NUM_IRQS)。

<a id="CONFIG_RUNTIME_ERROR_CHECKS"></a>

## 4.7 `CONFIG_RUNTIME_ERROR_CHECKS`

**提示（Prompt）**：运行时错误检查（Runtime Error Checks）。

**说明（Help）**

始终执行 `CHECKIF()` 宏覆盖的运行时检查。本项为默认选项，也是测试期间唯一使用的选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`Kconfig.zephyr:679`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L679)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → `CHECK` 宏的错误检查行为（Error Checking Behavior）。

<a id="CONFIG_SCOPE_CLEANUP_HELPERS"></a>

## 4.8 `CONFIG_SCOPE_CLEANUP_HELPERS`

**提示（Prompt）**：基于作用域的清理辅助工具（Scope-based Cleanup Helpers）。

**说明（Help）**

启用基于作用域的清理辅助宏，利用变量清理函数属性（Variable Cleanup Function Attribute）实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TOOLCHAIN_SUPPORTS_VARIABLE_CLEANUP_ATTRIBUTE
```

**定义位置（Location）**：[`Kconfig.zephyr:625`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L625)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

**配置项引用（Symbol References）**：[`CONFIG_TOOLCHAIN_SUPPORTS_VARIABLE_CLEANUP_ATTRIBUTE`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_TOOLCHAIN_SUPPORTS_VARIABLE_CLEANUP_ATTRIBUTE)。

<a id="CONFIG_SIZE_OPTIMIZATIONS"></a>

## 4.9 `CONFIG_SIZE_OPTIMIZATIONS`

**提示（Prompt）**：优化体积（Optimize for Size）。

**说明（Help）**

独立于其他选项，将编译器优化设为 `-Os`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPILER_OPTIMIZATIONS>
```

**定义位置（Location）**：[`Kconfig.zephyr:469`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L469)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。 → 优化级别（Optimization Level）。

**配置项引用（Symbol References）**：[`CONFIG_COMPILER_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_COMPILER_OPTIMIZATIONS)。

<a id="CONFIG_SIZE_OPTIMIZATIONS_AGGRESSIVE"></a>

## 4.10 `CONFIG_SIZE_OPTIMIZATIONS_AGGRESSIVE`

**提示（Prompt）**：激进优化体积（Aggressively Optimize for Size）。

**说明（Help）**

独立于其他选项，将编译器优化设为 `-Oz`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPILER_OPTIMIZATIONS>
```

**定义位置（Location）**：[`Kconfig.zephyr:475`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L475)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。 → 优化级别（Optimization Level）。

**配置项引用（Symbol References）**：[`CONFIG_COMPILER_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_COMPILER_OPTIMIZATIONS)。

<a id="CONFIG_SPEED_OPTIMIZATIONS"></a>

## 4.11 `CONFIG_SPEED_OPTIMIZATIONS`

**提示（Prompt）**：优化速度（Optimize for Speed）。

**说明（Help）**

独立于其他选项，将编译器优化设为 `-O2`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPILER_OPTIMIZATIONS>
```

**定义位置（Location）**：[`Kconfig.zephyr:481`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L481)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。 → 优化级别（Optimization Level）。

**配置项引用（Symbol References）**：[`CONFIG_COMPILER_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_COMPILER_OPTIMIZATIONS)。

<a id="CONFIG_SRAM_OFFSET"></a>

## 4.12 `CONFIG_SRAM_OFFSET`

原库同名定义共 2 条；本项为数据库第 18407 条记录，各定义分别保留。

**提示（Prompt）**：内核 SRAM 偏移（Kernel SRAM Offset）。

**说明（Help）**

指定内核起点相对于 SRAM 起点的字节偏移。将其从零改为其他值会影响 Zephyr 镜像链接，并减少应用代码可用的总 SRAM 量。若不确定，保持默认值 0。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`Kconfig.zephyr:261`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L261)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。

<a id="CONFIG_STD_C"></a>

## 4.13 `CONFIG_STD_C`

**提示（Prompt）**：C 语言标准（C Standard）。

**说明（Help）**

C 语言标准（C Standards）。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
CONFIG_STD_C23 if CONFIG_REQUIRES_STD_C23
CONFIG_STD_C17
```

**可选项（Choices）**

```text
CONFIG_STD_C17
CONFIG_STD_C23
```

**定义位置（Location）**：[`Kconfig.zephyr:381`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L381)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

**配置项引用（Symbol References）**：[`CONFIG_STD_C23`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_STD_C23)、[`CONFIG_REQUIRES_STD_C23`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_REQUIRES_STD_C23)、[`CONFIG_STD_C17`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_STD_C17)。

<a id="CONFIG_STD_C17"></a>

## 4.14 `CONFIG_STD_C17`

**提示（Prompt）**：C17。

**说明（Help）**

2017 年 C 语言标准，修复 C11 的缺陷，不引入新的语言特性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_REQUIRES_STD_C23 && <choice CONFIG_STD_C>
```

**定义位置（Location）**：[`Kconfig.zephyr:388`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L388)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。 → C 语言标准（C Standard）。

**配置项引用（Symbol References）**：[`CONFIG_REQUIRES_STD_C23`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_REQUIRES_STD_C23)、[`CONFIG_STD_C`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_STD_C)。

<a id="CONFIG_STD_C23"></a>

## 4.15 `CONFIG_STD_C23`

**提示（Prompt）**：C23 标准分支。

**说明（Help）**

2023 年 C 语言标准。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STD_C>
```

**定义位置（Location）**：[`Kconfig.zephyr:395`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L395)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。 → C 语言标准（C Standard）。

**配置项引用（Symbol References）**：[`CONFIG_STD_C`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_STD_C)。

<a id="CONFIG_TAINT"></a>

## 4.16 `CONFIG_TAINT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 Zephyr 构建被认定为受污染（Tainted），相关特性或模块必须选择此符号。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_TAINT_BLOBS
```

**定义位置（Location）**：[`Kconfig.zephyr:1061`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1061)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。

**配置项引用（Symbol References）**：[`CONFIG_TAINT_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TAINT_BLOBS)。

<a id="CONFIG_TOOLCHAIN_SUPPORTS_GNU_EXTENSIONS"></a>

## 4.17 `CONFIG_TOOLCHAIN_SUPPORTS_GNU_EXTENSIONS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，表示工具链支持 GNU 扩展（GNU Extensions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y if "zephyr" = "zephyr"
```

**定义位置（Location）**：[`Kconfig.zephyr:402`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L402)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

<a id="CONFIG_TOOLCHAIN_SUPPORTS_VARIABLE_CLEANUP_ATTRIBUTE"></a>

## 4.18 `CONFIG_TOOLCHAIN_SUPPORTS_VARIABLE_CLEANUP_ATTRIBUTE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，表示工具链支持变量的 `__cleanup(function)` 属性。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`Kconfig.zephyr:618`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L618)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

<a id="CONFIG_TOOLCHAIN_SUPPORTS_VLA_IN_STATEMENTS"></a>

## 4.19 `CONFIG_TOOLCHAIN_SUPPORTS_VLA_IN_STATEMENTS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏符号，表示工具链是否能在语句中处理变长数组（Variable-length Array，VLA）。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`Kconfig.zephyr:611`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L611)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

<a id="CONFIG_USE_DT_CODE_PARTITION"></a>

## 4.20 `CONFIG_USE_DT_CODE_PARTITION`

**提示（Prompt）**：将应用链接到设备树中的 `/chosen/zephyr,code-partition`。

**说明（Help）**

启用后，将应用链接到设备树 `/chosen` 中 `zephyr,code-partition` 属性选中的闪存分区。禁用后，可在下方手动设置闪存加载偏移和大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_FLASH_LOAD_OFFSET || n
```

**被选择（Selected by）**

```text
CONFIG_BOOTLOADER_MCUBOOT
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL616CL
CONFIG_SOC_SERIES_BL61X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_SERIES_BL808
CONFIG_SOC_SERIES_S32K3
CONFIG_BOOTLOADER_BOSSA
```

**定义位置（Location）**：[`Kconfig.zephyr:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。

**配置项引用（Symbol References）**：[`CONFIG_HAS_FLASH_LOAD_OFFSET`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAS_FLASH_LOAD_OFFSET)、[`CONFIG_BOOTLOADER_MCUBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOOTLOADER_MCUBOOT)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL616CL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL616CL)、[`CONFIG_SOC_SERIES_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL61X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_SERIES_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL808)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_BOOTLOADER_BOSSA`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BOOTLOADER_BOSSA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32K3`。

<a id="CONFIG_WARN_DEPRECATED"></a>

## 4.21 `CONFIG_WARN_DEPRECATED`

**提示（Prompt）**：对已弃用功能的使用发出警告（Deprecated Usage）。

**说明（Help）**

解析 Kconfig 树时，若启用了任何已弃用特性，则打印警告；编译时使用已弃用宏或符号，也打印警告。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_DEPRECATION_TEST
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`Kconfig.zephyr:1033`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1033)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。

**配置项引用（Symbol References）**：[`CONFIG_DEPRECATION_TEST`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATION_TEST)。

<a id="CONFIG_WARN_EXPERIMENTAL"></a>

## 4.22 `CONFIG_WARN_EXPERIMENTAL`

**提示（Prompt）**：对实验性功能的使用发出警告（Experimental Usage）。

**说明（Help）**

解析 Kconfig 树时，若启用了任何实验性特性，则打印警告。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:1048`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1048)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。

<!-- kconfig-navigation -->

[上一章](P003_Kconfig.zephyr_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P005_drivers_interrupt_controller_配置项参考_1.md)
