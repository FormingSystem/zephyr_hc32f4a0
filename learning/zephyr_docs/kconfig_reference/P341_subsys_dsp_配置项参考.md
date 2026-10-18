---
id: learning.zephyr-docs.kconfig-reference.page-341
title: "`subsys/dsp`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第341章\_`subsys/dsp`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/dsp` 的 9 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DSP"></a>

## 341.1 `CONFIG_DSP`

**提示（Prompt）**：数字信号处理子系统（DSP subsystem）

**说明（Help）**

将数字信号处理（Digital Signal Processing，DSP）子系统纳入 Zephyr 构建，使应用能够包含 `<zephyr/dsp/dsp.h>` 头文件并调用其中的接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`subsys/dsp/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dsp/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

<a id="CONFIG_DSP_BACKEND"></a>

## 341.2 `CONFIG_DSP_BACKEND`

**提示（Prompt）**：DSP 库后端选择（backend selection）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DSP
```

**默认值（Defaults）**

```text
CONFIG_DSP_BACKEND_POWERQUAD if DT_HAS_NXP_POWERQUAD_ENABLED && CONFIG_CMSIS_DSP
CONFIG_DSP_BACKEND_CMSIS if CONFIG_CMSIS_DSP
CONFIG_DSP_BACKEND_ARCMWDT if CONFIG_ARC && "zephyr" = "arcmwdt"
CONFIG_DSP_BACKEND_CUSTOM
```

**可选项（Choices）**

```text
CONFIG_DSP_BACKEND_CMSIS
CONFIG_DSP_BACKEND_POWERQUAD
CONFIG_DSP_BACKEND_CUSTOM
CONFIG_DSP_BACKEND_ARCMWDT
```

**定义位置（Location）**：[`subsys/dsp/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dsp/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 数字信号处理子系统（DSP subsystem）

**配置项引用（Symbol References）**：[`CONFIG_DSP`](P341_subsys_dsp_配置项参考.md#CONFIG_DSP)、[`CONFIG_DSP_BACKEND_POWERQUAD`](P341_subsys_dsp_配置项参考.md#CONFIG_DSP_BACKEND_POWERQUAD)、[`CONFIG_CMSIS_DSP`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP)、[`CONFIG_DSP_BACKEND_CMSIS`](P341_subsys_dsp_配置项参考.md#CONFIG_DSP_BACKEND_CMSIS)、[`CONFIG_DSP_BACKEND_ARCMWDT`](P341_subsys_dsp_配置项参考.md#CONFIG_DSP_BACKEND_ARCMWDT)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_DSP_BACKEND_CUSTOM`](P341_subsys_dsp_配置项参考.md#CONFIG_DSP_BACKEND_CUSTOM)。

<a id="CONFIG_DSP_BACKEND_ARCMWDT"></a>

## 341.3 `CONFIG_DSP_BACKEND_ARCMWDT`

**提示（Prompt）**：使用 mwdt 库作为数学运算后端（math backend）

**说明（Help）**

使用 MWDT-DSP 库实现 Zephyr 的各种 DSP 函数。此功能要求选择 MetaWare 工具链（toolchain）和 CMSIS 模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCMWDT_LIBC && CONFIG_CMSIS_DSP && <choice CONFIG_DSP_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_DSP_BACKEND_HAS_STATIC
CONFIG_DSP_BACKEND_HAS_AGU
CONFIG_DSP_BACKEND_HAS_XDATA_SECTION
```

**定义位置（Location）**：[`subsys/dsp/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dsp/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 数字信号处理子系统（DSP subsystem） → DSP 库后端选择（backend selection）

**配置项引用（Symbol References）**：[`CONFIG_ARCMWDT_LIBC`](P197_lib_配置项参考_1.md#CONFIG_ARCMWDT_LIBC)、[`CONFIG_CMSIS_DSP`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP)、[`CONFIG_DSP_BACKEND`](P341_subsys_dsp_配置项参考.md#CONFIG_DSP_BACKEND)、[`CONFIG_DSP_BACKEND_HAS_STATIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DSP_BACKEND_HAS_STATIC)、[`CONFIG_DSP_BACKEND_HAS_AGU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DSP_BACKEND_HAS_AGU)、[`CONFIG_DSP_BACKEND_HAS_XDATA_SECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DSP_BACKEND_HAS_XDATA_SECTION)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_DSP_BACKEND_HAS_STATIC`、`CONFIG_DSP_BACKEND_HAS_AGU`、`CONFIG_DSP_BACKEND_HAS_XDATA_SECTION`。

<a id="CONFIG_DSP_BACKEND_CMSIS"></a>

## 341.4 `CONFIG_DSP_BACKEND_CMSIS`

**提示（Prompt）**：使用 CMSIS-DSP 库作为数学运算后端

**说明（Help）**

使用 CMSIS-DSP 库实现 Zephyr 的各种 DSP 函数。此功能要求选择 CMSIS 模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_DSP && <choice CONFIG_DSP_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_DSP_BACKEND_HAS_STATIC
```

**定义位置（Location）**：[`subsys/dsp/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dsp/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 数字信号处理子系统（DSP subsystem） → DSP 库后端选择（backend selection）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_DSP`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP)、[`CONFIG_DSP_BACKEND`](P341_subsys_dsp_配置项参考.md#CONFIG_DSP_BACKEND)、[`CONFIG_DSP_BACKEND_HAS_STATIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DSP_BACKEND_HAS_STATIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_DSP_BACKEND_HAS_STATIC`。

<a id="CONFIG_DSP_BACKEND_CUSTOM"></a>

## 341.5 `CONFIG_DSP_BACKEND_CUSTOM`

**提示（Prompt）**：DSP 不使用任何 Zephyr 后端

**说明（Help）**

由应用提供自定义的 DSP 后端（backend）。应用或其模块之一应将实现添加到 `zdsp` 构建目标（build target）中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DSP_BACKEND>
```

**定义位置（Location）**：[`subsys/dsp/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dsp/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 数字信号处理子系统（DSP subsystem） → DSP 库后端选择（backend selection）

**配置项引用（Symbol References）**：[`CONFIG_DSP_BACKEND`](P341_subsys_dsp_配置项参考.md#CONFIG_DSP_BACKEND)。

<a id="CONFIG_DSP_BACKEND_POWERQUAD"></a>

## 341.6 `CONFIG_DSP_BACKEND_POWERQUAD`

**提示（Prompt）**：使用 NXP PowerQuad 硬件 DSP 加速器

**说明（Help）**

使用 NXP PowerQuad 硬件 DSP 协处理器（coprocessor）实现 Zephyr 的各种 DSP 函数，不受支持的运算回退到 CMSIS-DSP。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_DSP && DT_HAS_NXP_POWERQUAD_ENABLED && <choice CONFIG_DSP_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_DSP_BACKEND_HAS_STATIC
```

**定义位置（Location）**：[`subsys/dsp/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dsp/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 数字信号处理子系统（DSP subsystem） → DSP 库后端选择（backend selection）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_DSP`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP)、[`CONFIG_DSP_BACKEND`](P341_subsys_dsp_配置项参考.md#CONFIG_DSP_BACKEND)、[`CONFIG_DSP_BACKEND_HAS_STATIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DSP_BACKEND_HAS_STATIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_DSP_BACKEND_HAS_STATIC`。

<a id="CONFIG_DSP_BACKEND_POWERQUAD_SUPPORT_Q31"></a>

## 341.7 `CONFIG_DSP_BACKEND_POWERQUAD_SUPPORT_Q31`

**提示（Prompt）**：使用 PowerQuad 执行 Q31 定点运算（fixed-point operations）

**说明（Help）**

使用 PowerQuad 硬件加速器执行 Q31 定点运算。PowerQuad 内部以单精度浮点数（single-precision float）计算，其尾数（mantissa）只有 24 位，少于 Q31 的 31 位精度。可接受这种误差时才选择本项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DSP_BACKEND_POWERQUAD && CONFIG_DSP
```

**定义位置（Location）**：[`subsys/dsp/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dsp/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 数字信号处理子系统（DSP subsystem）

**配置项引用（Symbol References）**：[`CONFIG_DSP_BACKEND_POWERQUAD`](P341_subsys_dsp_配置项参考.md#CONFIG_DSP_BACKEND_POWERQUAD)、[`CONFIG_DSP`](P341_subsys_dsp_配置项参考.md#CONFIG_DSP)。

<a id="CONFIG_DSP_POWERQUAD_ADDR_REMAP"></a>

## 341.8 `CONFIG_DSP_POWERQUAD_ADDR_REMAP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由需要地址转换的片上系统（SoC）选择：在这些 SoC 上，PowerQuad 无法直接访问某些内存区域，例如 FlexSPI。SoC 必须在其 `soc.h` 中提供 `soc_powerquad_remap_addr()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DSP_BACKEND_POWERQUAD && CONFIG_DSP
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RW6XX
```

**定义位置（Location）**：[`subsys/dsp/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dsp/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 数字信号处理子系统（DSP subsystem）

**配置项引用（Symbol References）**：[`CONFIG_DSP_BACKEND_POWERQUAD`](P341_subsys_dsp_配置项参考.md#CONFIG_DSP_BACKEND_POWERQUAD)、[`CONFIG_DSP`](P341_subsys_dsp_配置项参考.md#CONFIG_DSP)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_DSP_POWERQUAD_TMP_BASE"></a>

## 341.9 `CONFIG_DSP_POWERQUAD_TMP_BASE`

**提示（Prompt）**：PowerQuad 临时内存基地址（base address）

**说明（Help）**

PowerQuad 用作临时工作内存的专用 RAM 的基地址。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_DSP_BACKEND_POWERQUAD && CONFIG_DSP
```

**默认值（Defaults）**

```text
0xE0000000
```

**定义位置（Location）**：[`subsys/dsp/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dsp/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 数字信号处理子系统（DSP subsystem）

**配置项引用（Symbol References）**：[`CONFIG_DSP_BACKEND_POWERQUAD`](P341_subsys_dsp_配置项参考.md#CONFIG_DSP_BACKEND_POWERQUAD)、[`CONFIG_DSP`](P341_subsys_dsp_配置项参考.md#CONFIG_DSP)。

<!-- kconfig-navigation -->

[上一章](P340_subsys_disk_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P342_subsys_emul_配置项参考.md)
