---
id: learning.zephyr-docs.kconfig-reference.page-432
title: "`subsys/timing`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第432章\_`subsys/timing`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/timing` 的 2 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_TIMING_FUNCTIONS"></a>

## 432.1 `CONFIG_TIMING_FUNCTIONS`

**提示（Prompt）**：计时函数（Timing Functions）

**说明（Help）**

启用后，编译计时相关函数（Timing functions），用于测量代码执行时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_FLASH_SHELL_TEST_COMMANDS
CONFIG_INSTRUMENTATION_MODE_CALLGRAPH
CONFIG_INSTRUMENTATION_MODE_STATISTICAL
CONFIG_ZTEST_BENCHMARK
CONFIG_TIMING_FUNCTIONS_NEED_AT_BOOT
CONFIG_TRACING_CTF_TIMESTAMP
```

**定义位置（Location）**：[`subsys/timing/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/timing/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_SHELL_TEST_COMMANDS`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SHELL_TEST_COMMANDS)、[`CONFIG_INSTRUMENTATION_MODE_CALLGRAPH`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION_MODE_CALLGRAPH)、[`CONFIG_INSTRUMENTATION_MODE_STATISTICAL`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION_MODE_STATISTICAL)、[`CONFIG_ZTEST_BENCHMARK`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_BENCHMARK)、[`CONFIG_TIMING_FUNCTIONS_NEED_AT_BOOT`](P432_subsys_timing_配置项参考.md#CONFIG_TIMING_FUNCTIONS_NEED_AT_BOOT)、[`CONFIG_TRACING_CTF_TIMESTAMP`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_CTF_TIMESTAMP)。

<a id="CONFIG_TIMING_FUNCTIONS_NEED_AT_BOOT"></a>

## 432.2 `CONFIG_TIMING_FUNCTIONS_NEED_AT_BOOT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，表明计时函数（Timing functions）需要在启动时初始化。由需要使用这些函数的内核或其他子系统选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_TIMING_FUNCTIONS
```

**被选择（Selected by）**

```text
CONFIG_THREAD_RUNTIME_STATS_USE_TIMING_FUNCTIONS
CONFIG_DEMAND_PAGING_STATS_USING_TIMING_FUNCTIONS
```

**定义位置（Location）**：[`subsys/timing/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/timing/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_TIMING_FUNCTIONS`](P432_subsys_timing_配置项参考.md#CONFIG_TIMING_FUNCTIONS)、[`CONFIG_THREAD_RUNTIME_STATS_USE_TIMING_FUNCTIONS`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_RUNTIME_STATS_USE_TIMING_FUNCTIONS)、[`CONFIG_DEMAND_PAGING_STATS_USING_TIMING_FUNCTIONS`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING_STATS_USING_TIMING_FUNCTIONS)。

<!-- kconfig-navigation -->

[上一章](P431_subsys_testsuite_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P433_subsys_tracing_配置项参考.md)
