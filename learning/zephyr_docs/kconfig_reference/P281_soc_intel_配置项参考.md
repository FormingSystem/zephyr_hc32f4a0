---
id: learning.zephyr-docs.kconfig-reference.page-281
title: "`soc/intel`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第281章\_`soc/intel`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/intel` 的 61 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ADSP_CLOCK"></a>

## 281.1 `CONFIG_ADSP_CLOCK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CAVS 时钟驱动（Clock Driver），允许选择时钟类型，从而选择频率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_CLOCK_CONTROL_ADSP`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_ADSP_IDLE_CLOCK_GATING"></a>

## 281.2 `CONFIG_ADSP_IDLE_CLOCK_GATING`

**提示（Prompt）**：空闲期间的 DSP 时钟门控（DSP clock gating in Idle）

**说明（Help）**

为真时，固件（FW）将在启用时钟门控（clock gating）的情况下运行。此选项会修改 DSP 的硬件配置。每当内核在空闲期间进入 WAITI 状态（等待中断，wait for interrupt），时钟就可以被门控关闭，但这不表示一定会发生。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L147)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_ADSP_IMR_CONTEXT_SAVE"></a>

## 281.3 `CONFIG_ADSP_IMR_CONTEXT_SAVE`

**提示（Prompt）**：关闭内核前将固件上下文保存到 IMR（Saves FW context into IMR）

**说明（Help）**

为真时，固件（FW）将在进入 D3 状态前，将其全部上下文（context）存入 IMR。以后主机再次为 DSP 上电时，可以使用这些上下文恢复固件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_ADSP_INIT_HPSRAM"></a>

## 281.4 `CONFIG_ADSP_INIT_HPSRAM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

需要初始化高性能 SRAM（HP SRAM）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_ADSP_NEED_POWER_ON_CACHE"></a>

## 281.5 `CONFIG_ADSP_NEED_POWER_ON_CACHE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

需要为缓存 SRAM 存储体（cache SRAM banks）上电。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_ADSP_POWER_DOWN_HPSRAM"></a>

## 281.6 `CONFIG_ADSP_POWER_DOWN_HPSRAM`

**提示（Prompt）**：掉电期间关闭高性能 SRAM（Switch off HP SRAM）

**说明（Help）**

掉电期间关闭高性能 SRAM（HP SRAM）。可由平台配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**默认值（Defaults）**

```text
n if CONFIG_ZTEST
y
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_ADSP_TRACE_SIMCALL"></a>

## 281.7 `CONFIG_ADSP_TRACE_SIMCALL`

**提示（Prompt）**：除窗口跟踪外，还输出 SIMCALL 数据（SIMCALL output）

**说明（Help）**

为真时，`trace_out` 层还会使用 SIMCALL 指令，将传入数据输出到承载该程序的模拟器进程的标准输出（standard output）。所有窗口内容保持相同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_HP_SRAM_RESERVE"></a>

## 281.8 `CONFIG_HP_SRAM_RESERVE`

**提示（Prompt）**：在高性能 SRAM 起始处预留的字节数（HP-SRAM reserved bytes）

**说明（Help）**

在高性能 SRAM（HP-SRAM）起始处预留的字节数。虽然主机窗口（host windows）的地址位于此处，Zephyr 不会在此放置任何符号（symbol）。SOF 应用也会直接使用此区域，因此修改此值时要格外谨慎。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**默认值（Defaults）**

```text
65536
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_INTEL_ADSP_CACHED_REGION"></a>

## 281.9 `CONFIG_INTEL_ADSP_CACHED_REGION`

**提示（Prompt）**：带缓存的区域保护选项映射（Cached RPO mapping）

**说明（Help）**

指定哪个 512M 区域包含带缓存映射（cached mapping）；区域编号为 0～7，由 Xtensa 区域保护选项（Region Protection Option，RPO）定义。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INTEL_ADSP_MEMORY_IS_MIRRORED && CONFIG_SOC_FAMILY_INTEL_ADSP
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_INTEL_ADSP_MEMORY_IS_MIRRORED`](P281_soc_intel_配置项参考.md#CONFIG_INTEL_ADSP_MEMORY_IS_MIRRORED)、[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_INTEL_ADSP_DEBUG_SLOT_MANAGER"></a>

## 281.10 `CONFIG_INTEL_ADSP_DEBUG_SLOT_MANAGER`

**提示（Prompt）**：调试槽位管理器（Debug slot manager）

**说明（Help）**

选择后，只能通过管理器 API 分配调试槽位（debug slot），禁止直接访问和修改调试窗口（debug window）。使用此 API 可动态分配槽位，替代静态且容易出错的槽位使用方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_INTEL_ADSP_FWREADY_MSG"></a>

## 281.11 `CONFIG_INTEL_ADSP_FWREADY_MSG`

**提示（Prompt）**：向主机发送固件就绪消息（firmware ready message）

**说明（Help）**

系统启动并运行后，向主机发送固件就绪消息（firmware ready message）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**默认值（Defaults）**

```text
y if CONFIG_INTEL_ADSP_SIM
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_INTEL_ADSP_SIM`](P281_soc_intel_配置项参考.md#CONFIG_INTEL_ADSP_SIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_INTEL_ADSP_IPC_OLD_INTERFACE"></a>

## 281.12 `CONFIG_INTEL_ADSP_IPC_OLD_INTERFACE`

**提示（Prompt）**：公开旧版进程间通信接口（old IPC interface）

**说明（Help）**

公开旧版 IPC 接口（`intel_adsp_ipc_*` 函数），以维持向后兼容性（backward compatibility）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_BACKEND_INTEL_ADSP_HOST_IPC && CONFIG_SOC_FAMILY_INTEL_ADSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_INTEL_ADSP_HOST_IPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPC_SERVICE_BACKEND_INTEL_ADSP_HOST_IPC)、[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_INTEL_ADSP_MEMORY_IS_MIRRORED"></a>

## 281.13 `CONFIG_INTEL_ADSP_MEMORY_IS_MIRRORED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为真时，表示某些物理内存区域在不同地址处具有镜像映射（mirrored mapping）。通过其中一组地址访问时经过 CPU 缓存，而通过另一组地址访问时直接访问内存。使用这种内存映射方式的 SoC 会选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_INTEL_ADSP_ACE15
CONFIG_SOC_SERIES_INTEL_ADSP_ACE20
CONFIG_SOC_SERIES_INTEL_ADSP_ACE30
CONFIG_SOC_SERIES_INTEL_ADSP_ACE40
CONFIG_SOC_SERIES_INTEL_ADSP_CAVS
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE15`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE15)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE20)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE30`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE30)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE40)、[`CONFIG_SOC_SERIES_INTEL_ADSP_CAVS`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_INTEL_ADSP_CAVS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`、`CONFIG_SOC_SERIES_INTEL_ADSP_ACE15`、`CONFIG_SOC_SERIES_INTEL_ADSP_ACE20`、`CONFIG_SOC_SERIES_INTEL_ADSP_ACE30`、`CONFIG_SOC_SERIES_INTEL_ADSP_ACE40`。

<a id="CONFIG_INTEL_ADSP_SIM"></a>

## 281.14 `CONFIG_INTEL_ADSP_SIM`

**提示（Prompt）**：Intel 音频 DSP 模拟器（ADSP Simulator）

**说明（Help）**

在模拟器（simulator）中运行此 SoC 家族。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**主动选择（Selects）**

```text
CONFIG_SIMULATOR_XTENSA
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_SIMULATOR_XTENSA`](P040_arch_xtensa_配置项参考.md#CONFIG_SIMULATOR_XTENSA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_INTEL_ADSP_UNCACHED_REGION"></a>

## 281.15 `CONFIG_INTEL_ADSP_UNCACHED_REGION`

**提示（Prompt）**：不带缓存的区域保护选项映射（Uncached RPO mapping）

**说明（Help）**

与 `INTEL_ADSP_CACHED_REGION` 类似，此项指定哪个 512M 区域（0～7）包含不带缓存映射（uncached mapping）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INTEL_ADSP_MEMORY_IS_MIRRORED && CONFIG_SOC_FAMILY_INTEL_ADSP
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:171`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L171)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_INTEL_ADSP_MEMORY_IS_MIRRORED`](P281_soc_intel_配置项参考.md#CONFIG_INTEL_ADSP_MEMORY_IS_MIRRORED)、[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_MEMORY_WIN_0_SIZE"></a>

## 281.16 `CONFIG_MEMORY_WIN_0_SIZE`

**提示（Prompt）**：内存窗口 0 的大小（Size of memory window 0）

**说明（Help）**

内存窗口 0（memory window 0）的大小。此窗口用于固件状态和发件箱／上行邮箱（outbox/uplink mbox）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_MEMORY_WIN_1_SIZE"></a>

## 281.17 `CONFIG_MEMORY_WIN_1_SIZE`

**提示（Prompt）**：内存窗口 1 的大小（Size of memory window 1）

**说明（Help）**

内存窗口 1（memory window 1）的大小。此窗口用于收件箱／下行邮箱（inbox/downlink mbox）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_MEMORY_WIN_2_SIZE"></a>

## 281.18 `CONFIG_MEMORY_WIN_2_SIZE`

**提示（Prompt）**：内存窗口 2 的大小（Size of memory window 2）

**说明（Help）**

内存窗口 2（memory window 2）的大小。此窗口用于调试（debug），默认大小为 12288 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**默认值（Defaults）**

```text
12288
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_MEMORY_WIN_3_SIZE"></a>

## 281.19 `CONFIG_MEMORY_WIN_3_SIZE`

**提示（Prompt）**：内存窗口 3 的大小（Size of memory window 3）

**说明（Help）**

内存窗口 3（memory window 3）的大小。此窗口用于跟踪（trace）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_SOC_ACE15_MTPM"></a>

## 281.20 `CONFIG_SOC_ACE15_MTPM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ACE 1.5 Meteor Lake PCH M 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_INTEL_ADSP_ACE
CONFIG_SOC_SERIES_INTEL_ADSP_ACE15
```

**被选择（Selected by）**

```text
CONFIG_BOARD_INTEL_ADSP
CONFIG_BOARD_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/ace/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/ace/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE15`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE15)、[`CONFIG_BOARD_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_INTEL_ADSP_ACE15`、`CONFIG_BOARD_INTEL_ADSP`。

<a id="CONFIG_SOC_ACE20_LNL"></a>

## 281.21 `CONFIG_SOC_ACE20_LNL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ACE 2.0 Lunar Lake PCH 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_INTEL_ADSP_ACE
CONFIG_SOC_SERIES_INTEL_ADSP_ACE20
```

**被选择（Selected by）**

```text
CONFIG_BOARD_INTEL_ADSP
CONFIG_BOARD_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/ace/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/ace/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE20)、[`CONFIG_BOARD_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_INTEL_ADSP_ACE20`、`CONFIG_BOARD_INTEL_ADSP`。

<a id="CONFIG_SOC_ACE30"></a>

## 281.22 `CONFIG_SOC_ACE30`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ACE 3.0 Panther Lake PCH 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_INTEL_ADSP_ACE
CONFIG_SOC_SERIES_INTEL_ADSP_ACE30
```

**被选择（Selected by）**

```text
CONFIG_BOARD_INTEL_ADSP
CONFIG_BOARD_INTEL_ADSP
CONFIG_BOARD_INTEL_ADSP
CONFIG_BOARD_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/ace/Kconfig.soc:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/ace/Kconfig.soc#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE30`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE30)、[`CONFIG_BOARD_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_INTEL_ADSP_ACE30`、`CONFIG_BOARD_INTEL_ADSP`。

<a id="CONFIG_SOC_ACE40"></a>

## 281.23 `CONFIG_SOC_ACE40`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ACE 4.0 Nova Lake PCH 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_INTEL_ADSP_ACE
CONFIG_SOC_SERIES_INTEL_ADSP_ACE40
```

**被选择（Selected by）**

```text
CONFIG_BOARD_INTEL_ADSP
CONFIG_BOARD_INTEL_ADSP
CONFIG_BOARD_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/ace/Kconfig.soc:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/ace/Kconfig.soc#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE40)、[`CONFIG_BOARD_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_INTEL_ADSP_ACE40`、`CONFIG_BOARD_INTEL_ADSP`。

<a id="CONFIG_SOC_AGILEX"></a>

## 281.24 `CONFIG_SOC_AGILEX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel Agilex 片上系统 FPGA（SoC FPGA）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_AGILEX
```

**被选择（Selected by）**

```text
CONFIG_BOARD_INTEL_SOCFPGA_AGILEX_SOCDK
```

**定义位置（Location）**：[`soc/intel/intel_socfpga/agilex/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_socfpga/agilex/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AGILEX`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_AGILEX)、[`CONFIG_BOARD_INTEL_SOCFPGA_AGILEX_SOCDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_INTEL_SOCFPGA_AGILEX_SOCDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_INTEL_SOCFPGA_AGILEX_SOCDK`。

<a id="CONFIG_SOC_AGILEX5"></a>

## 281.25 `CONFIG_SOC_AGILEX5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel Agilex5 片上系统 FPGA（SoC FPGA）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_AGILEX5
```

**被选择（Selected by）**

```text
CONFIG_BOARD_INTEL_SOCFPGA_AGILEX5_SOCDK
```

**定义位置（Location）**：[`soc/intel/intel_socfpga/agilex5/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_socfpga/agilex5/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AGILEX5`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_AGILEX5)、[`CONFIG_BOARD_INTEL_SOCFPGA_AGILEX5_SOCDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_INTEL_SOCFPGA_AGILEX5_SOCDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_INTEL_SOCFPGA_AGILEX5_SOCDK`。

<a id="CONFIG_SOC_CAVSV25"></a>

## 281.26 `CONFIG_SOC_CAVSV25`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel Tiger Lake 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_INTEL_ADSP_CAVS
```

**被选择（Selected by）**

```text
CONFIG_BOARD_INTEL_ADSP
CONFIG_BOARD_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/cavs/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/cavs/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_INTEL_ADSP_CAVS`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_INTEL_ADSP_CAVS)、[`CONFIG_BOARD_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_INTEL_ADSP`。

<a id="CONFIG_SOC_CYCLONEV"></a>

## 281.27 `CONFIG_SOC_CYCLONEV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel Cyclone V 片上系统 FPGA（SoC FPGA）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_CYCLONEV
```

**被选择（Selected by）**

```text
CONFIG_BOARD_CYCLONEV_SOCDK
```

**定义位置（Location）**：[`soc/intel/intel_socfpga_std/cyclonev/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_socfpga_std/cyclonev/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CYCLONEV`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_CYCLONEV)、[`CONFIG_BOARD_CYCLONEV_SOCDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CYCLONEV_SOCDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_CYCLONEV_SOCDK`。

<a id="CONFIG_SOC_FAMILY_INTEL_ADSP_TRIPLE_FAULT_BREADCRUMB"></a>

## 281.28 `CONFIG_SOC_FAMILY_INTEL_ADSP_TRIPLE_FAULT_BREADCRUMB`

**提示（Prompt）**：在高性能 SRAM 窗口 0 中记录三重故障线索（triple fault breadcrumbs）

**说明（Help）**

当双重异常（double exception）升级为逸出 CPU 的三重故障（triple fault）时，通过高性能 SRAM（HP-SRAM）窗口 0 的不带缓存别名（uncached alias），记录 EPC1、双重异常 EXCCAUSE 和 DEPC。这是一种轻量级跟踪辅助手段，可在生产构建中启用，用于诊断致命 CPU 锁死和双重故障（double faults）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_SOC_INTEL_COMM_WIDGET"></a>

## 281.29 `CONFIG_SOC_INTEL_COMM_WIDGET`

**提示（Prompt）**：Intel 通信组件驱动（Communication Widget driver）

**说明（Help）**

选择此项以启用 Intel 通信组件驱动（Communication Widget driver）。DSP 通信组件是用于通用边带消息（sideband message）发送和接收的设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_COMMUNICATION_WIDGET_ENABLED && CONFIG_SOC_FAMILY_INTEL_ADSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/intel/intel_adsp/ace/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/ace/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_SOC_NIOSV_G"></a>

## 281.30 `CONFIG_SOC_NIOSV_G`

原库同名定义共 2 条；本项为数据库第 17668 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel FPGA NIOSV 通用处理器（General Purpose Processor）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NIOSV
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NIOSV_G
```

**定义位置（Location）**：[`soc/intel/intel_niosv/niosv/Kconfig.soc:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_niosv/niosv/Kconfig.soc#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NIOSV`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_NIOSV)、[`CONFIG_BOARD_NIOSV_G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NIOSV_G)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NIOSV_G`。

<a id="CONFIG_SOC_NIOSV_G--record-17669"></a>

## 281.31 `CONFIG_SOC_NIOSV_G`

原库同名定义共 2 条；本项为数据库第 17669 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel FPGA NIOSV 通用处理器（General Purpose Processor）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_NIOSV
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NIOSV_G
```

**定义位置（Location）**：[`soc/intel/intel_niosv/niosv/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_niosv/niosv/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_NIOSV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_NIOSV)、[`CONFIG_BOARD_NIOSV_G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NIOSV_G)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_NIOSV`、`CONFIG_BOARD_NIOSV_G`。

<a id="CONFIG_SOC_NIOSV_M"></a>

## 281.32 `CONFIG_SOC_NIOSV_M`

原库同名定义共 2 条；本项为数据库第 17670 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel FPGA NIOSV 微控制器内核处理器（Microcontroller Core Processor）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NIOSV
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NIOSV_M
```

**定义位置（Location）**：[`soc/intel/intel_niosv/niosv/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_niosv/niosv/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NIOSV`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_NIOSV)、[`CONFIG_BOARD_NIOSV_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NIOSV_M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NIOSV_M`。

<a id="CONFIG_SOC_NIOSV_M--record-17671"></a>

## 281.33 `CONFIG_SOC_NIOSV_M`

原库同名定义共 2 条；本项为数据库第 17671 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel FPGA NIOSV 微控制器内核处理器（Microcontroller Core Processor）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_NIOSV
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NIOSV_M
```

**定义位置（Location）**：[`soc/intel/intel_niosv/niosv/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_niosv/niosv/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_NIOSV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_NIOSV)、[`CONFIG_BOARD_NIOSV_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NIOSV_M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_NIOSV`、`CONFIG_BOARD_NIOSV_M`。

<a id="CONFIG_SOC_SERIES_AGILEX"></a>

## 281.34 `CONFIG_SOC_SERIES_AGILEX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel Agilex 片上系统 FPGA 系列（SoC FPGA Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_INTEL_SOCFPGA
```

**被选择（Selected by）**

```text
CONFIG_SOC_AGILEX
```

**定义位置（Location）**：[`soc/intel/intel_socfpga/agilex/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_socfpga/agilex/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_SOCFPGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_SOCFPGA)、[`CONFIG_SOC_AGILEX`](P281_soc_intel_配置项参考.md#CONFIG_SOC_AGILEX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_SOCFPGA`。

<a id="CONFIG_SOC_SERIES_AGILEX5"></a>

## 281.35 `CONFIG_SOC_SERIES_AGILEX5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel Agilex5 片上系统 FPGA 系列（SoC FPGA Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_INTEL_SOCFPGA
```

**被选择（Selected by）**

```text
CONFIG_SOC_AGILEX5
```

**定义位置（Location）**：[`soc/intel/intel_socfpga/agilex5/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_socfpga/agilex5/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_SOCFPGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_SOCFPGA)、[`CONFIG_SOC_AGILEX5`](P281_soc_intel_配置项参考.md#CONFIG_SOC_AGILEX5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_SOCFPGA`。

<a id="CONFIG_SOC_SERIES_CYCLONEV"></a>

## 281.36 `CONFIG_SOC_SERIES_CYCLONEV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel Cyclone V 片上系统 FPGA 系列（SoC FPGA Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_INTEL_SOCFPGA_STD
```

**被选择（Selected by）**

```text
CONFIG_SOC_CYCLONEV
```

**定义位置（Location）**：[`soc/intel/intel_socfpga_std/cyclonev/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_socfpga_std/cyclonev/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_SOCFPGA_STD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_SOCFPGA_STD)、[`CONFIG_SOC_CYCLONEV`](P281_soc_intel_配置项参考.md#CONFIG_SOC_CYCLONEV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_SOCFPGA_STD`。

<a id="CONFIG_SOC_SERIES_INTEL_ADSP_ACE"></a>

## 281.37 `CONFIG_SOC_SERIES_INTEL_ADSP_ACE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel 音频 DSP ACE（Intel ADSP ACE）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**被选择（Selected by）**

```text
CONFIG_SOC_ACE15_MTPM
CONFIG_SOC_ACE20_LNL
CONFIG_SOC_ACE30
CONFIG_SOC_ACE40
```

**定义位置（Location）**：[`soc/intel/intel_adsp/ace/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/ace/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_SOC_ACE15_MTPM`](P281_soc_intel_配置项参考.md#CONFIG_SOC_ACE15_MTPM)、[`CONFIG_SOC_ACE20_LNL`](P281_soc_intel_配置项参考.md#CONFIG_SOC_ACE20_LNL)、[`CONFIG_SOC_ACE30`](P281_soc_intel_配置项参考.md#CONFIG_SOC_ACE30)、[`CONFIG_SOC_ACE40`](P281_soc_intel_配置项参考.md#CONFIG_SOC_ACE40)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_SOC_SERIES_INTEL_ADSP_ACE_CUSTOM_MORE_SPIN_RELAX_NOPS"></a>

## 281.38 `CONFIG_SOC_SERIES_INTEL_ADSP_ACE_CUSTOM_MORE_SPIN_RELAX_NOPS`

**提示（Prompt）**：使用带更多空操作的 Intel 音频 DSP 专用 arch_spin_relax()（more NOPs）

**说明（Help）**

获取自旋锁（spinlock）失败后，添加一些空操作指令（NOP）。这样会给总线额外时间，以在各 CPU 之间同步读－比较－写事务（RCW transaction）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_XTENSA_MORE_SPIN_RELAX_NOPS && CONFIG_SOC_FAMILY_INTEL_ADSP
```

**默认值（Defaults）**

```text
y if CONFIG_SMP && CONFIG_MP_MAX_NUM_CPUS > 1
```

**定义位置（Location）**：[`soc/intel/intel_adsp/ace/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/ace/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_MORE_SPIN_RELAX_NOPS`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MORE_SPIN_RELAX_NOPS)、[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_MP_MAX_NUM_CPUS`](P001_kernel_配置项参考_1.md#CONFIG_MP_MAX_NUM_CPUS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_SOC_SERIES_INTEL_ADSP_ACE_NUM_SPIN_RELAX_NOPS"></a>

## 281.39 `CONFIG_SOC_SERIES_INTEL_ADSP_ACE_NUM_SPIN_RELAX_NOPS`

**提示（Prompt）**：Intel 音频 DSP 专用 arch_spin_relax() 使用的空操作指令数量（number of NOPs）

**说明（Help）**

指定 Intel 音频 DSP 专用 `arch_spin_relax()` 中的空操作指令（NOP）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_INTEL_ADSP_ACE_CUSTOM_MORE_SPIN_RELAX_NOPS && CONFIG_SOC_FAMILY_INTEL_ADSP
```

**默认值（Defaults）**

```text
32 if CONFIG_MP_MAX_NUM_CPUS = 1
64 if CONFIG_MP_MAX_NUM_CPUS = 2
96 if CONFIG_MP_MAX_NUM_CPUS = 3
128 if CONFIG_MP_MAX_NUM_CPUS = 4
160 if CONFIG_MP_MAX_NUM_CPUS = 5
```

**定义位置（Location）**：[`soc/intel/intel_adsp/ace/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/ace/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 使用带更多空操作的 Intel 音频 DSP 专用 arch_spin_relax()（more NOPs）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE_CUSTOM_MORE_SPIN_RELAX_NOPS`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_INTEL_ADSP_ACE_CUSTOM_MORE_SPIN_RELAX_NOPS)、[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_MP_MAX_NUM_CPUS`](P001_kernel_配置项参考_1.md#CONFIG_MP_MAX_NUM_CPUS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_SOC_SERIES_INTEL_ADSP_ACE_NUM_SPIN_RELAX_NOPS_ADD_CPU_ID"></a>

## 281.40 `CONFIG_SOC_SERIES_INTEL_ADSP_ACE_NUM_SPIN_RELAX_NOPS_ADD_CPU_ID`

**提示（Prompt）**：添加 CPU 标识以错开空操作数量（Add CPU ID to offset NOPs）

**说明（Help）**

将 CPU 标识（CPU ID）加入 `arch_spin_relax()` 的空操作指令（NOP）数量中。这样可使各 CPU 的循环存在差异，进一步避免它们同时进行读－比较－写事务（RCW transactions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_INTEL_ADSP_ACE_CUSTOM_MORE_SPIN_RELAX_NOPS && CONFIG_SOC_FAMILY_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/ace/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/ace/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 使用带更多空操作的 Intel 音频 DSP 专用 arch_spin_relax()（more NOPs）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE_CUSTOM_MORE_SPIN_RELAX_NOPS`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_INTEL_ADSP_ACE_CUSTOM_MORE_SPIN_RELAX_NOPS)、[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_SOC_SERIES_INTEL_ADSP_CAVS"></a>

## 281.41 `CONFIG_SOC_SERIES_INTEL_ADSP_CAVS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel 音频 DSP CAVS（Intel ADSP CAVS）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**被选择（Selected by）**

```text
CONFIG_SOC_CAVSV25
```

**定义位置（Location）**：[`soc/intel/intel_adsp/cavs/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/cavs/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_SOC_CAVSV25`](P281_soc_intel_配置项参考.md#CONFIG_SOC_CAVSV25)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_SOC_SERIES_NIOSV"></a>

## 281.42 `CONFIG_SOC_SERIES_NIOSV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel FPGA NIOSV 处理器

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_INTEL_NIOSV
```

**被选择（Selected by）**

```text
CONFIG_SOC_NIOSV_M
CONFIG_SOC_NIOSV_G
```

**定义位置（Location）**：[`soc/intel/intel_niosv/niosv/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_niosv/niosv/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_NIOSV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_NIOSV)、[`CONFIG_SOC_NIOSV_M`](P281_soc_intel_配置项参考.md#CONFIG_SOC_NIOSV_M)、[`CONFIG_SOC_NIOSV_G`](P281_soc_intel_配置项参考.md#CONFIG_SOC_NIOSV_G)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_NIOSV`。

<a id="CONFIG_SRAM_RETENTION_MODE"></a>

## 281.43 `CONFIG_SRAM_RETENTION_MODE`

**提示（Prompt）**：初始化期间的 SRAM 保留模式（SRAM retention mode）

**说明（Help）**

启用此选项时，会在固件启动过程中激活 SRAM 保留模式（retention mode）；禁用时则不激活。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/intel/intel_adsp/ace/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/ace/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_XTENSA_CPU_IDLE_SPIN"></a>

## 281.44 `CONFIG_XTENSA_CPU_IDLE_SPIN`

**提示（Prompt）**：为 k_cpu_idle 使用忙循环（busy loop）

**说明（Help）**

CPU 空闲状态使用自旋循环（spin loop），替代 WAITI。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_XTENSA_WAITI_BUG"></a>

## 281.45 `CONFIG_XTENSA_WAITI_BUG`

**提示（Prompt）**：LX6 上 WAITI 缺陷的规避序列（workaround sequence）

**说明（Help）**

SOF 历来在其 ADSP 平台中包含此规避措施：在进入 WAITI 前，先执行 128 条空操作指令（NOP），随后执行 ISYNC 和 EXTW。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**被选择（Selected by）**

```text
CONFIG_SOC_CAVSV25
```

**定义位置（Location）**：[`soc/intel/intel_adsp/Kconfig:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/Kconfig#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_SOC_CAVSV25`](P281_soc_intel_配置项参考.md#CONFIG_SOC_CAVSV25)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="SB_CONFIG_SOC_ACE15_MTPM"></a>

## 281.46 `SB_CONFIG_SOC_ACE15_MTPM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ACE 1.5 Meteor Lake PCH M 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE
SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE15
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_INTEL_ADSP
SB_CONFIG_BOARD_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/ace/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/ace/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE)、[`SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE15`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE15)、[`SB_CONFIG_BOARD_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE15`、`SB_CONFIG_BOARD_INTEL_ADSP`。

<a id="SB_CONFIG_SOC_ACE20_LNL"></a>

## 281.47 `SB_CONFIG_SOC_ACE20_LNL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ACE 2.0 Lunar Lake PCH 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE
SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE20
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_INTEL_ADSP
SB_CONFIG_BOARD_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/ace/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/ace/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE)、[`SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE20`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE20)、[`SB_CONFIG_BOARD_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE20`、`SB_CONFIG_BOARD_INTEL_ADSP`。

<a id="SB_CONFIG_SOC_ACE30"></a>

## 281.48 `SB_CONFIG_SOC_ACE30`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ACE 3.0 Panther Lake PCH 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE
SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE30
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_INTEL_ADSP
SB_CONFIG_BOARD_INTEL_ADSP
SB_CONFIG_BOARD_INTEL_ADSP
SB_CONFIG_BOARD_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/ace/Kconfig.soc:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/ace/Kconfig.soc#L34)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE)、[`SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE30`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE30)、[`SB_CONFIG_BOARD_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE30`、`SB_CONFIG_BOARD_INTEL_ADSP`。

<a id="SB_CONFIG_SOC_ACE40"></a>

## 281.49 `SB_CONFIG_SOC_ACE40`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ACE 4.0 Nova Lake PCH 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE
SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE40
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_INTEL_ADSP
SB_CONFIG_BOARD_INTEL_ADSP
SB_CONFIG_BOARD_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/ace/Kconfig.soc:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/ace/Kconfig.soc#L44)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE)、[`SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE40`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE40)、[`SB_CONFIG_BOARD_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE40`、`SB_CONFIG_BOARD_INTEL_ADSP`。

<a id="SB_CONFIG_SOC_AGILEX"></a>

## 281.50 `SB_CONFIG_SOC_AGILEX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel Agilex 片上系统 FPGA（SoC FPGA）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_AGILEX
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_INTEL_SOCFPGA_AGILEX_SOCDK
```

**定义位置（Location）**：[`soc/intel/intel_socfpga/agilex/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_socfpga/agilex/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_AGILEX`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_SERIES_AGILEX)、[`SB_CONFIG_BOARD_INTEL_SOCFPGA_AGILEX_SOCDK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_INTEL_SOCFPGA_AGILEX_SOCDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_INTEL_SOCFPGA_AGILEX_SOCDK`。

<a id="SB_CONFIG_SOC_AGILEX5"></a>

## 281.51 `SB_CONFIG_SOC_AGILEX5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel Agilex5 片上系统 FPGA（SoC FPGA）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_AGILEX5
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_INTEL_SOCFPGA_AGILEX5_SOCDK
```

**定义位置（Location）**：[`soc/intel/intel_socfpga/agilex5/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_socfpga/agilex5/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_AGILEX5`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_SERIES_AGILEX5)、[`SB_CONFIG_BOARD_INTEL_SOCFPGA_AGILEX5_SOCDK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_INTEL_SOCFPGA_AGILEX5_SOCDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_INTEL_SOCFPGA_AGILEX5_SOCDK`。

<a id="SB_CONFIG_SOC_CAVSV25"></a>

## 281.52 `SB_CONFIG_SOC_CAVSV25`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel Tiger Lake 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_INTEL_ADSP_CAVS
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_INTEL_ADSP
SB_CONFIG_BOARD_INTEL_ADSP
```

**定义位置（Location）**：[`soc/intel/intel_adsp/cavs/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/cavs/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_INTEL_ADSP_CAVS`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_SERIES_INTEL_ADSP_CAVS)、[`SB_CONFIG_BOARD_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_INTEL_ADSP`。

<a id="SB_CONFIG_SOC_CYCLONEV"></a>

## 281.53 `SB_CONFIG_SOC_CYCLONEV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel Cyclone V 片上系统 FPGA（SoC FPGA）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_CYCLONEV
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_CYCLONEV_SOCDK
```

**定义位置（Location）**：[`soc/intel/intel_socfpga_std/cyclonev/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_socfpga_std/cyclonev/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CYCLONEV`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_SERIES_CYCLONEV)、[`SB_CONFIG_BOARD_CYCLONEV_SOCDK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CYCLONEV_SOCDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_CYCLONEV_SOCDK`。

<a id="SB_CONFIG_SOC_NIOSV_G"></a>

## 281.54 `SB_CONFIG_SOC_NIOSV_G`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel FPGA NIOSV 通用处理器（General Purpose Processor）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NIOSV
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NIOSV_G
```

**定义位置（Location）**：[`soc/intel/intel_niosv/niosv/Kconfig.soc:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_niosv/niosv/Kconfig.soc#L20)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NIOSV`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_SERIES_NIOSV)、[`SB_CONFIG_BOARD_NIOSV_G`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NIOSV_G)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NIOSV_G`。

<a id="SB_CONFIG_SOC_NIOSV_M"></a>

## 281.55 `SB_CONFIG_SOC_NIOSV_M`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel FPGA NIOSV 微控制器内核处理器（Microcontroller Core Processor）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NIOSV
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NIOSV_M
```

**定义位置（Location）**：[`soc/intel/intel_niosv/niosv/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_niosv/niosv/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NIOSV`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_SERIES_NIOSV)、[`SB_CONFIG_BOARD_NIOSV_M`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NIOSV_M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NIOSV_M`。

<a id="SB_CONFIG_SOC_SERIES_AGILEX"></a>

## 281.56 `SB_CONFIG_SOC_SERIES_AGILEX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel Agilex 片上系统 FPGA 系列（SoC FPGA Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_INTEL_SOCFPGA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AGILEX
```

**定义位置（Location）**：[`soc/intel/intel_socfpga/agilex/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_socfpga/agilex/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_INTEL_SOCFPGA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_INTEL_SOCFPGA)、[`SB_CONFIG_SOC_AGILEX`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_AGILEX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_INTEL_SOCFPGA`。

<a id="SB_CONFIG_SOC_SERIES_AGILEX5"></a>

## 281.57 `SB_CONFIG_SOC_SERIES_AGILEX5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel Agilex5 片上系统 FPGA 系列（SoC FPGA Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_INTEL_SOCFPGA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AGILEX5
```

**定义位置（Location）**：[`soc/intel/intel_socfpga/agilex5/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_socfpga/agilex5/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_INTEL_SOCFPGA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_INTEL_SOCFPGA)、[`SB_CONFIG_SOC_AGILEX5`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_AGILEX5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_INTEL_SOCFPGA`。

<a id="SB_CONFIG_SOC_SERIES_CYCLONEV"></a>

## 281.58 `SB_CONFIG_SOC_SERIES_CYCLONEV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel Cyclone V 片上系统 FPGA 系列（SoC FPGA Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_INTEL_SOCFPGA_STD
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_CYCLONEV
```

**定义位置（Location）**：[`soc/intel/intel_socfpga_std/cyclonev/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_socfpga_std/cyclonev/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_INTEL_SOCFPGA_STD`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_INTEL_SOCFPGA_STD)、[`SB_CONFIG_SOC_CYCLONEV`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_CYCLONEV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_INTEL_SOCFPGA_STD`。

<a id="SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE"></a>

## 281.59 `SB_CONFIG_SOC_SERIES_INTEL_ADSP_ACE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel 音频 DSP ACE（Intel ADSP ACE）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_INTEL_ADSP
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_ACE15_MTPM
SB_CONFIG_SOC_ACE20_LNL
SB_CONFIG_SOC_ACE30
SB_CONFIG_SOC_ACE40
```

**定义位置（Location）**：[`soc/intel/intel_adsp/ace/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/ace/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_INTEL_ADSP)、[`SB_CONFIG_SOC_ACE15_MTPM`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_ACE15_MTPM)、[`SB_CONFIG_SOC_ACE20_LNL`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_ACE20_LNL)、[`SB_CONFIG_SOC_ACE30`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_ACE30)、[`SB_CONFIG_SOC_ACE40`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_ACE40)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="SB_CONFIG_SOC_SERIES_INTEL_ADSP_CAVS"></a>

## 281.60 `SB_CONFIG_SOC_SERIES_INTEL_ADSP_CAVS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel 音频 DSP CAVS（Intel ADSP CAVS）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_INTEL_ADSP
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_CAVSV25
```

**定义位置（Location）**：[`soc/intel/intel_adsp/cavs/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/cavs/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_INTEL_ADSP)、[`SB_CONFIG_SOC_CAVSV25`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_CAVSV25)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="SB_CONFIG_SOC_SERIES_NIOSV"></a>

## 281.61 `SB_CONFIG_SOC_SERIES_NIOSV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel FPGA NIOSV 处理器

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_INTEL_NIOSV
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NIOSV_M
SB_CONFIG_SOC_NIOSV_G
```

**定义位置（Location）**：[`soc/intel/intel_niosv/niosv/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_niosv/niosv/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_INTEL_NIOSV`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_INTEL_NIOSV)、[`SB_CONFIG_SOC_NIOSV_M`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_NIOSV_M)、[`SB_CONFIG_SOC_NIOSV_G`](P281_soc_intel_配置项参考.md#SB_CONFIG_SOC_NIOSV_G)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_INTEL_NIOSV`。

<!-- kconfig-navigation -->

[上一章](P280_soc_infineon_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P282_soc_ite_配置项参考.md)
