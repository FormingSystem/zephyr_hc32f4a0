---
id: learning.zephyr-docs.kconfig-reference.page-9
title: "`<module:cmsis-dsp>/zephyr`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第9章\_`<module:cmsis-dsp>/zephyr`配置项参考

本章翻译官方 Kconfig 数据库中 `<module:cmsis-dsp>/zephyr` 的 11 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CMSIS_DSP"></a>

## 9.1 `CONFIG_CMSIS_DSP`

原库同名定义共 2 条；本项为数据库第 3946 条记录，各定义分别保留。

**提示（Prompt）**：CMSIS-DSP 库支持（Library Support）

**说明（Help）**

此选项启用 CMSIS-DSP 库（Library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CMSIS_NN
CONFIG_CMSIS_NN
```

**定义位置（Location）**：`<module:cmsis-dsp>/zephyr/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `cmsis-dsp`（CMSIS-DSP 模块；工作区相对路径 `modules/lib/cmsis-dsp`）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_NN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CMSIS_NN)。

<a id="CONFIG_CMSIS_DSP_AUTOVECTORIZE"></a>

## 9.2 `CONFIG_CMSIS_DSP_AUTOVECTORIZE`

**提示（Prompt）**：自动向量化（Auto Vectorize）

**说明（Help）**

此选项使 DSP 函数优先采用可自动向量化（Autovectorizable）的代码，而非使用 C 内建函数（Intrinsics）的代码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_DSP
```

**定义位置（Location）**：`<module:cmsis-dsp>/zephyr/Kconfig:56`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `cmsis-dsp`（CMSIS-DSP 模块；工作区相对路径 `modules/lib/cmsis-dsp`） → CMSIS-DSP 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_DSP`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP)。

<a id="CONFIG_CMSIS_DSP_CUSTOM_CONFIG"></a>

## 9.3 `CONFIG_CMSIS_DSP_CUSTOM_CONFIG`

**提示（Prompt）**：自定义配置头文件（Custom Configuration Header）

**说明（Help）**

此选项启用包含头文件 `arm_dsp_config.h`。可在该头文件中定义 `ARM_DSP_ATTRIBUTE` 和 `ARM_DSP_TABLE_ATTRIBUTE`。`ARM_DSP_ATTRIBUTE` 可用于将所有函数定义为弱符号（Weak），或将它们放入特定内存段（Memory Section）；`ARM_DSP_TABLE_ATTRIBUTE` 可用于将 CMSIS DSP 表放入特定内存段。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_DSP
```

**定义位置（Location）**：`<module:cmsis-dsp>/zephyr/Kconfig:39`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `cmsis-dsp`（CMSIS-DSP 模块；工作区相对路径 `modules/lib/cmsis-dsp`） → CMSIS-DSP 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_DSP`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP)。

<a id="CONFIG_CMSIS_DSP_FLOAT16"></a>

## 9.4 `CONFIG_CMSIS_DSP_FLOAT16`

**提示（Prompt）**：半精度（16 位浮点，Half-Precision）支持

**说明（Help）**

此选项启用半精度（16 位）浮点运算（Half-precision Floating-point Operations）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FP16_ARITHMETIC && CONFIG_CMSIS_DSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:cmsis-dsp>/zephyr/Kconfig:62`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `cmsis-dsp`（CMSIS-DSP 模块；工作区相对路径 `modules/lib/cmsis-dsp`） → CMSIS-DSP 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_FP16_ARITHMETIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FP16_ARITHMETIC)、[`CONFIG_CMSIS_DSP`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP)。

<a id="CONFIG_CMSIS_DSP_LAX_VECTOR_CONVERSIONS"></a>

## 9.5 `CONFIG_CMSIS_DSP_LAX_VECTOR_CONVERSIONS`

**提示（Prompt）**：宽松向量转换（Lax Vector Conversions）

**说明（Help）**

此选项启用宽松向量转换（Lax Vector Conversions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ARMV8_1_M_MVEI || CONFIG_ARMV8_1_M_MVEF || CONFIG_CMSIS_DSP_NEON || CONFIG_CMSIS_DSP_NEON_EXPERIMENTAL) && CONFIG_CMSIS_DSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:cmsis-dsp>/zephyr/Kconfig:76`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `cmsis-dsp`（CMSIS-DSP 模块；工作区相对路径 `modules/lib/cmsis-dsp`） → CMSIS-DSP 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_ARMV8_1_M_MVEI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARMV8_1_M_MVEI)、[`CONFIG_ARMV8_1_M_MVEF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARMV8_1_M_MVEF)、[`CONFIG_CMSIS_DSP_NEON`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP_NEON)、[`CONFIG_CMSIS_DSP_NEON_EXPERIMENTAL`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP_NEON_EXPERIMENTAL)、[`CONFIG_CMSIS_DSP`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP)。

<a id="CONFIG_CMSIS_DSP_LOOPUNROLL"></a>

## 9.6 `CONFIG_CMSIS_DSP_LOOPUNROLL`

**提示（Prompt）**：循环展开（Loop Unrolling）

**说明（Help）**

此选项启用 DSP 函数中的手动循环展开（Manual Loop Unrolling）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_DSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:cmsis-dsp>/zephyr/Kconfig:28`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `cmsis-dsp`（CMSIS-DSP 模块；工作区相对路径 `modules/lib/cmsis-dsp`） → CMSIS-DSP 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_DSP`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP)。

<a id="CONFIG_CMSIS_DSP_MATRIXCHECK"></a>

## 9.7 `CONFIG_CMSIS_DSP_MATRIXCHECK`

**提示（Prompt）**：矩阵检查（Matrix Check）

**说明（Help）**

此选项启用对矩阵输入和输出尺寸（Matrix Input and Output Sizes）的验证。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_DSP
```

**定义位置（Location）**：`<module:cmsis-dsp>/zephyr/Kconfig:50`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `cmsis-dsp`（CMSIS-DSP 模块；工作区相对路径 `modules/lib/cmsis-dsp`） → CMSIS-DSP 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_DSP`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP)。

<a id="CONFIG_CMSIS_DSP_NE10_DSP_RIFFT_SCALING"></a>

## 9.8 `CONFIG_CMSIS_DSP_NE10_DSP_RIFFT_SCALING`

**提示（Prompt）**：使用 Neon 对 RIFFT 进行缩放（Scaling）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_CMSIS_DSP_NEON || CONFIG_CMSIS_DSP_NEON_EXPERIMENTAL) && CONFIG_CMSIS_DSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:cmsis-dsp>/zephyr/Kconfig:70`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `cmsis-dsp`（CMSIS-DSP 模块；工作区相对路径 `modules/lib/cmsis-dsp`） → CMSIS-DSP 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_DSP_NEON`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP_NEON)、[`CONFIG_CMSIS_DSP_NEON_EXPERIMENTAL`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP_NEON_EXPERIMENTAL)、[`CONFIG_CMSIS_DSP`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP)。

<a id="CONFIG_CMSIS_DSP_NEON"></a>

## 9.9 `CONFIG_CMSIS_DSP_NEON`

**提示（Prompt）**：Neon 指令集（Instruction Set）

**说明（Help）**

此选项启用 NEON 高级 SIMD 指令集（Advanced SIMD Instruction Set），大多数 Cortex-A 及部分 Cortex-R 处理器提供此指令集。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_A && CONFIG_CMSIS_DSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:cmsis-dsp>/zephyr/Kconfig:11`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `cmsis-dsp`（CMSIS-DSP 模块；工作区相对路径 `modules/lib/cmsis-dsp`） → CMSIS-DSP 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A)、[`CONFIG_CMSIS_DSP`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP)。

<a id="CONFIG_CMSIS_DSP_NEON_EXPERIMENTAL"></a>

## 9.10 `CONFIG_CMSIS_DSP_NEON_EXPERIMENTAL`

**提示（Prompt）**：Neon 指令集（Instruction Set）

**说明（Help）**

此选项启用 NEON 高级 SIMD 指令集（Advanced SIMD Instruction Set），大多数 Cortex-A 及部分 Cortex-R 处理器提供此指令集。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_A && CONFIG_CMSIS_DSP
```

**定义位置（Location）**：`<module:cmsis-dsp>/zephyr/Kconfig:19`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `cmsis-dsp`（CMSIS-DSP 模块；工作区相对路径 `modules/lib/cmsis-dsp`） → CMSIS-DSP 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A)、[`CONFIG_CMSIS_DSP`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP)。

<a id="CONFIG_CMSIS_DSP_ROUNDING"></a>

## 9.11 `CONFIG_CMSIS_DSP_ROUNDING`

**提示（Prompt）**：舍入（Rounding）

**说明（Help）**

此选项启用支持函数（Support Functions）中的舍入（Rounding）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_DSP
```

**定义位置（Location）**：`<module:cmsis-dsp>/zephyr/Kconfig:34`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `cmsis-dsp`（CMSIS-DSP 模块；工作区相对路径 `modules/lib/cmsis-dsp`） → CMSIS-DSP 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_DSP`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP)。

<!-- kconfig-navigation -->

[上一章](P008_drivers_timer_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P010_module_hal_espressif_zephyr_配置项参考.md)
