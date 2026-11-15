---
id: learning.zephyr-docs.kconfig-reference.page-416
title: "`subsys/profiling`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第416章\_`subsys/profiling`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/profiling` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PROFILING"></a>

## 416.1 `CONFIG_PROFILING`

**提示（Prompt）**：性能分析工具（Profiling tools）

**说明（Help）**

启用 perf 等性能分析工具（Profiling tool）。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`subsys/profiling/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/profiling/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

<a id="CONFIG_PROFILING_PERF"></a>

## 416.2 `CONFIG_PROFILING_PERF`

**提示（Prompt）**：Perf 性能分析支持

**说明（Help）**

启用 `perf` 命令行命令（Shell command）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_PROFILING_PERF_HAS_BACKEND && CONFIG_PROFILING
```

**定义位置（Location）**：[`subsys/profiling/perf/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/profiling/perf/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 性能分析工具（Profiling tools）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_PROFILING_PERF_HAS_BACKEND`](P416_subsys_profiling_配置项参考.md#CONFIG_PROFILING_PERF_HAS_BACKEND)、[`CONFIG_PROFILING`](P416_subsys_profiling_配置项参考.md#CONFIG_PROFILING)。

<a id="CONFIG_PROFILING_PERF_BUFFER_SIZE"></a>

## 416.3 `CONFIG_PROFILING_PERF_BUFFER_SIZE`

**提示（Prompt）**：Perf 缓冲区大小（Buffer size）

**说明（Help）**

perf 用于保存栈回溯样本（Stack trace sample）的缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PROFILING_PERF && CONFIG_PROFILING
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/profiling/perf/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/profiling/perf/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 性能分析工具（Profiling tools） → Perf 性能分析支持

**配置项引用（Symbol References）**：[`CONFIG_PROFILING_PERF`](P416_subsys_profiling_配置项参考.md#CONFIG_PROFILING_PERF)、[`CONFIG_PROFILING`](P416_subsys_profiling_配置项参考.md#CONFIG_PROFILING)。

<a id="CONFIG_PROFILING_PERF_HAS_BACKEND"></a>

## 416.4 `CONFIG_PROFILING_PERF_HAS_BACKEND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

存在 `arch_perf_current_stack_trace()` 的实现时选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PROFILING
```

**被选择（Selected by）**

```text
CONFIG_PROFILING_PERF_BACKEND_RISCV
CONFIG_PROFILING_PERF_BACKEND_ARM_CORTEX_M
CONFIG_PROFILING_PERF_BACKEND_X86
CONFIG_PROFILING_PERF_BACKEND_X86_64
CONFIG_PROFILING_PERF_BACKEND_ARM64
```

**定义位置（Location）**：[`subsys/profiling/perf/backends/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/profiling/perf/backends/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 性能分析工具（Profiling tools）

**配置项引用（Symbol References）**：[`CONFIG_PROFILING`](P416_subsys_profiling_配置项参考.md#CONFIG_PROFILING)、[`CONFIG_PROFILING_PERF_BACKEND_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PROFILING_PERF_BACKEND_RISCV)、[`CONFIG_PROFILING_PERF_BACKEND_ARM_CORTEX_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PROFILING_PERF_BACKEND_ARM_CORTEX_M)、[`CONFIG_PROFILING_PERF_BACKEND_X86`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PROFILING_PERF_BACKEND_X86)、[`CONFIG_PROFILING_PERF_BACKEND_X86_64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PROFILING_PERF_BACKEND_X86_64)、[`CONFIG_PROFILING_PERF_BACKEND_ARM64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PROFILING_PERF_BACKEND_ARM64)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PROFILING_PERF_BACKEND_RISCV`、`CONFIG_PROFILING_PERF_BACKEND_ARM_CORTEX_M`、`CONFIG_PROFILING_PERF_BACKEND_X86`、`CONFIG_PROFILING_PERF_BACKEND_X86_64`、`CONFIG_PROFILING_PERF_BACKEND_ARM64`。

<!-- kconfig-navigation -->

[上一章](P415_subsys_precision_timing_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P417_subsys_random_配置项参考.md)
