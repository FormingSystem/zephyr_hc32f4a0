---
id: learning.zephyr-docs.kconfig-reference.page-338
title: "`subsys/debug`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第338章\_`subsys/debug`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/debug` 的 86 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ASAN"></a>

## 338.1 `CONFIG_ASAN`

**提示（Prompt）**：使用地址消毒器构建（Build with Address Sanitizer）

**说明（Help）**

启用地址消毒器（Address Sanitizer）来构建 Zephyr。所译快照中仅支持基于 POSIX 架构的开发板，需要较新的编译器支持 `-fsanitize=address` 命令行选项，并提供 `libasan` 库。

注意：使用 GCC 时，由于 `libasan` 存在潜在死锁风险，64 位开发板默认禁用退出时的内存泄漏检测。可在环境变量 `ASAN_OPTIONS` 中加入 `leak_check_at_exit=1` 更改此行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX
```

**定义位置（Location）**：[`subsys/debug/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)。

<a id="CONFIG_ASAN_NOP_DLCLOSE"></a>

## 338.2 `CONFIG_ASAN_NOP_DLCLOSE`

**提示（Prompt）**：以空操作覆盖主机操作系统的 dlclose()（Override host OS dlclose with a NOP）

**说明（Help）**

以空操作（NOP）覆盖主机操作系统的 `dlclose()`。这是针对泄漏消毒器（Leak Sanitizer，LSAN）已知限制的变通处理：若在泄漏检查之前调用 `dlclose`，检查时的栈跟踪会报告 `<unknown module>`，且无法抑制这些报告。详情见 [Sanitizers issue 89](https://github.com/google/sanitizers/issues/89)。

译注：原文中间一次将函数名拼为 `dlcose`；这里按标题中的 `dlclose()` 表示。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ASAN
```

**默认值（Defaults）**

```text
y if HAS_SDL
```

**定义位置（Location）**：[`subsys/debug/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 使用地址消毒器构建（Build with Address Sanitizer）

**配置项引用（Symbol References）**：[`CONFIG_ASAN`](P338_subsys_debug_配置项参考.md#CONFIG_ASAN)。

<a id="CONFIG_ASAN_RECOVER"></a>

## 338.3 `CONFIG_ASAN_RECOVER`

**提示（Prompt）**：消毒器报错后继续执行（Continue after sanitizer errors）

**说明（Help）**

编译器消毒器（compiler sanitizers）默认在第一次报错后退出。设为 `y` 可让代码继续执行，适用于代码库存在已知但未抑制错误的情况。运行时还必须在 `ASAN_OPTIONS` 环境变量中设置 `halt_on_error=0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ASAN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/debug/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 使用地址消毒器构建（Build with Address Sanitizer）

**配置项引用（Symbol References）**：[`CONFIG_ASAN`](P338_subsys_debug_配置项参考.md#CONFIG_ASAN)。

<a id="CONFIG_ASSERT"></a>

## 338.4 `CONFIG_ASSERT`

**提示（Prompt）**：运行时断言检查（Runtime assertion checking，ZASSERT）

**说明（Help）**

启用 ZASSERT 宏。禁用后，所有断言（assertions）都不生成编译代码，从而提高性能、减小系统占用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_FORCE_NO_ASSERT
```

**默认值（Defaults）**

```text
y if CONFIG_TEST
```

**弱选择（Implies）**

```text
CONFIG_PRINTK
```

**定义位置（Location）**：[`subsys/debug/zassert/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/zassert/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_FORCE_NO_ASSERT`](P338_subsys_debug_配置项参考.md#CONFIG_FORCE_NO_ASSERT)、[`CONFIG_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST)、[`CONFIG_PRINTK`](P338_subsys_debug_配置项参考.md#CONFIG_PRINTK)。

<a id="CONFIG_ASSERT_LEVEL"></a>

## 338.5 `CONFIG_ASSERT_LEVEL`

**提示（Prompt）**：__ASSERT() 级别（level）[已弃用，DEPRECATED]

**说明（Help）**

指定 `__ASSERT()` 宏使用的断言级别（assertion level），可设为以下三种值：

- 级别 `0`：关闭。
- 级别 `1`：开启，每个包含 `__assert.h` 的文件都产生警告。
- 级别 `2`：开启，不产生警告。

已弃用：请改为配置 DEFAULT ZASSERT 模块（`CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_OFF/ON/VERBOSE`）。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`subsys/debug/zassert/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/zassert/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

<a id="CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_NORMAL"></a>

## 338.6 `CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_NORMAL`

**提示（Prompt）**：普通级别，仅保留位置（Normal, location only）

**说明（Help）**

`ZASSERT_LEVEL_NORMAL`：检查断言并打印位置（location），但不编译消息及其参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/debug/zassert/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/zassert/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → DEFAULT 断言模块的断言级别（Assertion level for DEFAULT assert module）

<a id="CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_OFF"></a>

## 338.7 `CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

`ZASSERT_LEVEL_OFF`：DEFAULT 模块的断言在编译时移除（compiled out）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/debug/zassert/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/zassert/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → DEFAULT 断言模块的断言级别（Assertion level for DEFAULT assert module）

<a id="CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_TERSE"></a>

## 338.8 `CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_TERSE`

**提示（Prompt）**：简略级别，仅检查（Terse, only check）

**说明（Help）**

`ZASSERT_LEVEL_TERSE`：执行断言检查，但不编译位置、消息及其参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/debug/zassert/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/zassert/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → DEFAULT 断言模块的断言级别（Assertion level for DEFAULT assert module）

<a id="CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_VERBOSE"></a>

## 338.9 `CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_VERBOSE`

**提示（Prompt）**：详细级别，包含消息（Verbose, with message）

**说明（Help）**

`ZASSERT_LEVEL_VERBOSE`：执行断言检查，并将位置、消息及其参数编译进程序。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/debug/zassert/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/zassert/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → DEFAULT 断言模块的断言级别（Assertion level for DEFAULT assert module）

<a id="CONFIG_ASSERT_NO_COND_INFO"></a>

## 338.10 `CONFIG_ASSERT_NO_COND_INFO`

**提示（Prompt）**：禁用断言条件信息（Disable condition info for asserts）[已弃用，DEPRECATED]

**说明（Help）**

从打印的断言消息中移除断言条件（assert condition）。可节省目标代码空间，因此对资源很小的目标可能有必要。建议先禁用条件信息，再考虑禁用文件信息，因为可依据文件信息在源码中找到条件。

已弃用：此选项会将 DEFAULT ZASSERT 模块设为简略级别（Terse）；应改用 `CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_TERSE` 直接配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/debug/zassert/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/zassert/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_ASSERT_NO_FILE_INFO"></a>

## 338.11 `CONFIG_ASSERT_NO_FILE_INFO`

**提示（Prompt）**：禁用断言文件信息（Disable file info for asserts）[已弃用，DEPRECATED]

**说明（Help）**

移除发生断言的源文件名称和路径，可节省目标代码空间，因此对资源很小的目标可能有必要。

已弃用：此选项会将 DEFAULT ZASSERT 模块设为简略级别（Terse）；应改用 `CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_TERSE` 直接配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/debug/zassert/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/zassert/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_ASSERT_NO_MSG_INFO"></a>

## 338.12 `CONFIG_ASSERT_NO_MSG_INFO`

**提示（Prompt）**：禁用断言消息（Disable message for asserts）[已弃用，DEPRECATED]

**说明（Help）**

从打印的断言中移除附加消息（additional message）。可节省目标代码空间，因此对资源很小的目标可能有必要。建议先禁用消息，再考虑禁用文件信息，因为可依据文件信息在源码中找到消息。

已弃用：此选项会将 DEFAULT ZASSERT 模块设为简略级别（Terse）；应改用 `CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_TERSE` 直接配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/debug/zassert/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/zassert/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_ASSERT_TEST"></a>

## 338.13 `CONFIG_ASSERT_TEST`

**提示（Prompt）**：断言测试模式（Assert test mode）

**说明（Help）**

启用断言测试模式（assert test mode）：断言条件为假时，允许断言后置动作处理程序（assert post action handler）返回，而不是中止。验证断言功能的测试可选择此项，并实现自定义后置动作钩子（hook），使测试能够继续。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`subsys/debug/zassert/Kconfig:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/zassert/Kconfig#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

<a id="CONFIG_ASSERT_VERBOSE"></a>

## 338.14 `CONFIG_ASSERT_VERBOSE`

**提示（Prompt）**：详细断言（Verbose assertions）[已弃用，DEPRECATED]

**说明（Help）**

允许打印包含断言信息的消息，包括位置、条件表达式以及该断言的附加说明。

已弃用：此选项会将 DEFAULT ZASSERT 模块设为详细级别（Verbose）；应改用 `CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_VERBOSE` 直接配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/debug/zassert/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/zassert/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_CALLGRAPH_INFO"></a>

## 338.15 `CONFIG_CALLGRAPH_INFO`

**提示（Prompt）**：生成调用图信息（Generate call graph information）

**说明（Help）**

为每个编译单元（compilation unit）额外生成一个 `.ci` 文件，按函数列出 GCC 在编译时已知的全部调用（calls），采用 VCG 格式。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`subsys/debug/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

<a id="CONFIG_CS_TRACE_DEFMT"></a>

## 338.16 `CONFIG_CS_TRACE_DEFMT`

**提示（Prompt）**：CoreSight跟踪解格式器（Trace Deformatter）

**说明（Help）**

此模块解码使用 CoreSight 跟踪格式化器（Trace Formatter）格式化的数据，例如送入嵌入式跟踪路由器（Embedded Trace Router，ETR）的数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_DEBUG_NRF_ETR_DECODE
CONFIG_DEBUG_NRF_ETR_DEBUG
```

**定义位置（Location）**：[`subsys/debug/Kconfig:286`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L286)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_NRF_ETR_DECODE`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_DECODE)、[`CONFIG_DEBUG_NRF_ETR_DEBUG`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_DEBUG)。

<a id="CONFIG_DEBUG"></a>

## 338.17 `CONFIG_DEBUG`

**提示（Prompt）**：启用调试构建内核（Build kernel with debugging enabled）

**说明（Help）**

构建适合调试的内核。所译快照中，此选项仅禁用优化（optimization）；可从此处进一步选择其他调试变体，获得更多调试能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`subsys/debug/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

<a id="CONFIG_DEBUG_COREDUMP"></a>

## 338.18 `CONFIG_DEBUG_COREDUMP`

**提示（Prompt）**：核心转储（Core Dump）

**说明（Help）**

启用核心转储（core dump），以便用于离线调试（offline debugging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_SUPPORTS_COREDUMP
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_SUPPORTS_COREDUMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_SUPPORTS_COREDUMP`。

<a id="CONFIG_DEBUG_COREDUMP_BACKEND"></a>

## 338.19 `CONFIG_DEBUG_COREDUMP_BACKEND`

**提示（Prompt）**：核心转储后端（Coredump backend）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_COREDUMP
```

**默认值（Defaults）**

```text
CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING
```

**可选项（Choices）**

```text
CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING
CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP
CONFIG_DEBUG_COREDUMP_BACKEND_FLASH_PARTITION
CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY
CONFIG_DEBUG_COREDUMP_BACKEND_INTEL_ADSP_MEM_WINDOW
CONFIG_DEBUG_COREDUMP_BACKEND_AMD_ACP_PANIC_DUMP
CONFIG_DEBUG_COREDUMP_BACKEND_OTHER
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP)、[`CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING)、[`CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP)、[`CONFIG_DEBUG_COREDUMP_BACKEND_FLASH_PARTITION`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_FLASH_PARTITION)、[`CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY)、[`CONFIG_DEBUG_COREDUMP_BACKEND_INTEL_ADSP_MEM_WINDOW`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_INTEL_ADSP_MEM_WINDOW)、[`CONFIG_DEBUG_COREDUMP_BACKEND_AMD_ACP_PANIC_DUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_AMD_ACP_PANIC_DUMP)、[`CONFIG_DEBUG_COREDUMP_BACKEND_OTHER`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_OTHER)。

<a id="CONFIG_DEBUG_COREDUMP_BACKEND_AMD_ACP_PANIC_DUMP"></a>

## 338.20 `CONFIG_DEBUG_COREDUMP_BACKEND_AMD_ACP_PANIC_DUMP`

**提示（Prompt）**：AMD ACP 崩溃转储（AMD ACP Panic Dump）

**说明（Help）**

使用 AMD ACP 异常盒（exception box）作为核心转储后端。转储数据写入异常盒中的异常缓冲区（exception buffer），并通过中断通知主机。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_COREDUMP_BACKEND>
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储后端（Coredump backend）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_BACKEND`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND)。

<a id="CONFIG_DEBUG_COREDUMP_BACKEND_FLASH_PARTITION"></a>

## 338.21 `CONFIG_DEBUG_COREDUMP_BACKEND_FLASH_PARTITION`

**提示（Prompt）**：使用 Flash 分区保存核心转储（flash partition for coredump）

**说明（Help）**

核心转储（core dump）保存在 DTS 别名为 `coredump-partition` 的 Flash 分区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH && <choice CONFIG_DEBUG_COREDUMP_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_FLASH_MAP
CONFIG_STREAM_FLASH
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储后端（Coredump backend）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_DEBUG_COREDUMP_BACKEND`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND)、[`CONFIG_FLASH_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MAP)、[`CONFIG_STREAM_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STREAM_FLASH)。

<a id="CONFIG_DEBUG_COREDUMP_BACKEND_INTEL_ADSP_MEM_WINDOW"></a>

## 338.22 `CONFIG_DEBUG_COREDUMP_BACKEND_INTEL_ADSP_MEM_WINDOW`

**提示（Prompt）**：Intel ADSP 使用内存窗口保存核心转储（memory window for coredump）

**说明（Help）**

通过内存窗口槽位 `slot[1]` 执行核心转储。它是 Intel ADSP 与 Xtensa DSP 共享的内存区域。窗口 `2` 的槽位 `[1]` 为调试信息预留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_MEM_WINDOW_ENABLED && <choice CONFIG_DEBUG_COREDUMP_BACKEND>
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储后端（Coredump backend）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_BACKEND`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND)。

<a id="CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY"></a>

## 338.23 `CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY`

**提示（Prompt）**：使用内存保存核心转储（memory to store the coredump）

**说明（Help）**

将核心转储或其中一部分保存到专用内存区域，并在启动时保护该区域，使其可在热重启（warm reboot）后读取。发生完整硬件重启周期，例如断电再上电时，RAM 很可能丢失数据，因此该方案显然不适用。预留空间大小参见 `DEBUG_COREDUMP_BACKEND_IN_MEMORY_SIZE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_COREDUMP_BACKEND>
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储后端（Coredump backend）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_BACKEND`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND)。

<a id="CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY_SIZE"></a>

## 338.24 `CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY_SIZE`

**提示（Prompt）**：内存核心转储大小（In-memory coredump size）

**说明（Help）**

设置用于保存核心转储并在热重启后访问的专用内存区域。至少必须容纳 `arch_coredump_info_dump()` 输出的信息。若空间不足，额外内存区域会被静默忽略。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY && CONFIG_DEBUG_COREDUMP
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY)、[`CONFIG_DEBUG_COREDUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP)。

<a id="CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING"></a>

## 338.25 `CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING`

**提示（Prompt）**：使用日志子系统进行核心转储（Logging subsystem for coredump）

**说明（Help）**

通过日志子系统（logging subsystem）执行核心转储。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_COREDUMP_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_LOG
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储后端（Coredump backend）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_BACKEND`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)。

<a id="CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP"></a>

## 338.26 `CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP`

**提示（Prompt）**：原始 UDP 核心转储后端，支持 IPv4 与 IPv6（Raw UDP coredump backend）

**说明（Help）**

向由 `net_ipaddr_parse()` 解析的固定 UDP 对端发送原始核心转储帧（raw coredump frames）；可使用 IPv4 或 IPv6 地址，并可选择添加 `:port`。在主机上使用 `scripts/coredump/coredump_udp_receiver.py` 重组 `.bin` 文件，供 `scripts/coredump/coredump_gdbserver.py` 使用。还可通过日志子系统将相同数据镜像为以 ASCII `#CD:` 开头的十六进制行，参见 `DEBUG_COREDUMP_LOGGING_UDP_MIRROR_TO_LOG`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING && CONFIG_NET_SOCKETS && CONFIG_NET_UDP && (CONFIG_NET_IPV4 || CONFIG_NET_IPV6) && <choice CONFIG_DEBUG_COREDUMP_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_LOG if CONFIG_DEBUG_COREDUMP_LOGGING_UDP_MIRROR_TO_LOG
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储后端（Coredump backend）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_DEBUG_COREDUMP_BACKEND`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_DEBUG_COREDUMP_LOGGING_UDP_MIRROR_TO_LOG`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_LOGGING_UDP_MIRROR_TO_LOG)。

<a id="CONFIG_DEBUG_COREDUMP_BACKEND_OTHER"></a>

## 338.27 `CONFIG_DEBUG_COREDUMP_BACKEND_OTHER`

**提示（Prompt）**：树外定义的核心转储后端子系统（coredump backend defined out of tree）

**说明（Help）**

通过树外定义（out of tree）的自定义机制执行核心转储。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_COREDUMP_BACKEND>
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储后端（Coredump backend）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_BACKEND`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND)。

<a id="CONFIG_DEBUG_COREDUMP_DUMP_THREAD_PRIV_STACK"></a>

## 338.28 `CONFIG_DEBUG_COREDUMP_DUMP_THREAD_PRIV_STACK`

**提示（Prompt）**：转储用户线程的特权栈（Dump privilege stack of user threads）

**说明（Help）**

转储用户线程（user threads）的特权栈（privilege stack）。若要节省核心转储后端空间，或确定无需查看特权栈，则选择 `n`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_SUPPORTS_COREDUMP_PRIV_STACKS && CONFIG_USERSPACE && CONFIG_DEBUG_COREDUMP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_SUPPORTS_COREDUMP_PRIV_STACKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP_PRIV_STACKS)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_DEBUG_COREDUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_SUPPORTS_COREDUMP_PRIV_STACKS`。

<a id="CONFIG_DEBUG_COREDUMP_FATAL_UNLOCK_IRQS"></a>

## 338.29 `CONFIG_DEBUG_COREDUMP_FATAL_UNLOCK_IRQS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`z_fatal_error()` 在核心转储之前屏蔽中断。Socket 发送和以太网驱动需要中断请求（IRQ）交付才能完成数据报发送，因此仅在核心转储调用期间解除 IRQ 屏蔽，随后恢复原先的 DAIF／屏蔽状态。

在 ARM64 上，同步异常期间 `DAIF.I` 位通常仍然置位，因此 `arch_irq_unlock(arch_irq_lock())` 不够；转储窗口期间会显式清除 `DAIF.I`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP && <choice CONFIG_DEBUG_COREDUMP_BACKEND>
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储后端（Coredump backend） → 原始 UDP 核心转储后端，支持 IPv4 与 IPv6（Raw UDP coredump backend）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP)、[`CONFIG_DEBUG_COREDUMP_BACKEND`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND)。

<a id="CONFIG_DEBUG_COREDUMP_FLASH_CHUNK_SIZE"></a>

## 338.30 `CONFIG_DEBUG_COREDUMP_FLASH_CHUNK_SIZE`

**提示（Prompt）**：Flash 写入操作的分块大小（Chunk size for flash write operations）

**说明（Help）**

较大的值减少总写入操作次数，可加快写入，但会消耗更多内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_COREDUMP_BACKEND_FLASH_PARTITION && CONFIG_DEBUG_COREDUMP
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_BACKEND_FLASH_PARTITION`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_FLASH_PARTITION)、[`CONFIG_DEBUG_COREDUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP)。

<a id="CONFIG_DEBUG_COREDUMP_LOGGING_UDP_HOST"></a>

## 338.31 `CONFIG_DEBUG_COREDUMP_LOGGING_UDP_HOST`

**提示（Prompt）**：原始核心转储的 UDP 对端地址，IPv4／IPv6，可选端口（UDP peer address）

**说明（Help）**

传给 `net_ipaddr_parse()` 的目标主机字符串。示例：

```text
192.0.2.1
192.0.2.1:17777
[2001:db8::1]
[2001:db8::1]:17777
```

省略端口时，采用默认 UDP 端口 `17777`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP && <choice CONFIG_DEBUG_COREDUMP_BACKEND>
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储后端（Coredump backend） → 原始 UDP 核心转储后端，支持 IPv4 与 IPv6（Raw UDP coredump backend）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP)、[`CONFIG_DEBUG_COREDUMP_BACKEND`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND)。

<a id="CONFIG_DEBUG_COREDUMP_LOGGING_UDP_MIRROR_TO_LOG"></a>

## 338.32 `CONFIG_DEBUG_COREDUMP_LOGGING_UDP_MIRROR_TO_LOG`

**提示（Prompt）**：以 #CD: 十六进制形式将核心转储镜像到 UART 日志（Mirror coredump to log）

**说明（Help）**

禁用时，仅通过 UDP 将原始核心转储发送到 `DEBUG_COREDUMP_LOGGING_UDP_HOST`，采用生产式输出，不生成 Twister／UART 十六进制日志。在收集端计算机上使用 `scripts/coredump/coredump_udp_receiver.py`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP && <choice CONFIG_DEBUG_COREDUMP_BACKEND>
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储后端（Coredump backend） → 原始 UDP 核心转储后端，支持 IPv4 与 IPv6（Raw UDP coredump backend）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP)、[`CONFIG_DEBUG_COREDUMP_BACKEND`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND)。

<a id="CONFIG_DEBUG_COREDUMP_MEMORY_DUMP"></a>

## 338.33 `CONFIG_DEBUG_COREDUMP_MEMORY_DUMP`

**提示（Prompt）**：内存转储（Memory dump）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_COREDUMP
```

**默认值（Defaults）**

```text
CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_LINKER_RAM
```

**可选项（Choices）**

```text
CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN
CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS
CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_LINKER_RAM
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP)、[`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_LINKER_RAM`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_LINKER_RAM)、[`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN)、[`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS)。

<a id="CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_LINKER_RAM"></a>

## 338.34 `CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_LINKER_RAM`

**提示（Prompt）**：链接器段定义的 RAM（RAM defined by linker section）

**说明（Help）**

转储 `_image_ram_start[]` 与 `_image_ram_end[]` 之间的内存区域，至少包括数据段（data）、不初始化段（noinit）和 BSS 段。这是默认选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_COREDUMP_MEMORY_DUMP>
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 内存转储（Memory dump）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP)。

<a id="CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN"></a>

## 338.35 `CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN`

**提示（Prompt）**：最小转储（Minimal）

**说明（Help）**

只转储最基本的内存内容，例如发生异常的线程的线程结构体（thread struct）和栈（stack）。仅在确实需要尽可能小的核心转储（core dump）时使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_COREDUMP_MEMORY_DUMP>
```

**主动选择（Selects）**

```text
CONFIG_THREAD_STACK_INFO
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 内存转储（Memory dump）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)。

<a id="CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS"></a>

## 338.36 `CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS`

**提示（Prompt）**：线程（Threads）

**说明（Help）**

转储所有线程的线程结构体、栈和调试线程所需的全部数据。在对称多处理（SMP）系统中，还包含每个 CPU 的中断服务例程栈（ISR stack）。`DEBUG_THREAD_INFO` 提供内核结构体偏移量，使离线 GDB 能够在 SMP 和非 SMP 系统上枚举线程。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS && <choice CONFIG_DEBUG_COREDUMP_MEMORY_DUMP>
```

**主动选择（Selects）**

```text
CONFIG_THREAD_STACK_INFO
CONFIG_DEBUG_THREAD_INFO
CONFIG_DEBUG_COREDUMP_THREADS_METADATA
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 内存转储（Memory dump）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS)、[`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_DEBUG_THREAD_INFO`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_THREAD_INFO)、[`CONFIG_DEBUG_COREDUMP_THREADS_METADATA`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_THREADS_METADATA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS`。

<a id="CONFIG_DEBUG_COREDUMP_SHELL"></a>

## 338.37 `CONFIG_DEBUG_COREDUMP_SHELL`

**提示（Prompt）**：核心转储命令行（Coredump shell）

**说明（Help）**

此命令行接口（shell）提供对核心转储（coredump）及其后端（backend）的访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_DEBUG_COREDUMP
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_DEBUG_COREDUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP)。

<a id="CONFIG_DEBUG_COREDUMP_SMP_FREEZE_CPUS"></a>

## 338.38 `CONFIG_DEBUG_COREDUMP_SMP_FREEZE_CPUS`

**提示（Prompt）**：冻结其他 CPU 并捕获其当前寄存器（live registers）

**说明（Help）**

在对称多处理（SMP）系统中，发生致命错误（panic）时正在另一 CPU 上运行的线程，其 `callee_saved` 上下文已经过时：它只在上一次主动上下文切换时更新。因此，普通的逐线程转储无法捕获该线程真正的当前寄存器。此选项向其他每个 CPU 发送处理器间中断（IPI），捕获其当前寄存器状态并纳入核心转储（coredump），使 GDB 也能正确显示这些线程的回溯（backtrace）。

每个被冻结的 CPU 都在自己的中断处理函数中自旋，原先持有的资源保持原状，直到转储完成；随后通过正常的异常返回路径，从被中断的位置继续执行。若某个 CPU 未在有限超时时间内响应，例如它从未启动或卡在屏蔽中断的状态，则跳过该 CPU，继续完成其余转储。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SMP && CONFIG_ARCH_SUPPORTS_COREDUMP_SMP_FREEZE && CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS && CONFIG_DEBUG_COREDUMP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:191`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L191)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump）

**配置项引用（Symbol References）**：[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_ARCH_SUPPORTS_COREDUMP_SMP_FREEZE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_SUPPORTS_COREDUMP_SMP_FREEZE)、[`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS)、[`CONFIG_DEBUG_COREDUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP)。

<a id="CONFIG_DEBUG_COREDUMP_THREADS_METADATA"></a>

## 338.39 `CONFIG_DEBUG_COREDUMP_THREADS_METADATA`

**提示（Prompt）**：线程元数据（Threads metadata）

**说明（Help）**

核心转储（core dump）将包含线程元数据段，其中保存启用线程调试所需的数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS && CONFIG_DEBUG_COREDUMP
```

**主动选择（Selects）**

```text
CONFIG_DEBUG_THREAD_INFO
```

**被选择（Selected by）**

```text
CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS)、[`CONFIG_DEBUG_COREDUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP)、[`CONFIG_DEBUG_THREAD_INFO`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_THREAD_INFO)、[`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS`。

<a id="CONFIG_DEBUG_COREDUMP_THREAD_SNAPSHOT_MAX"></a>

## 338.40 `CONFIG_DEBUG_COREDUMP_THREAD_SNAPSHOT_MAX`

**提示（Prompt）**：每次 SMP 核心转储的线程快照数量上限

**说明（Help）**

在对称多处理（SMP）系统中，核心转储（coredump）短暂持有 `z_thread_monitor_lock`，为线程链表中的指针制作快照，然后在执行缓慢的逐线程转储 I/O 前释放锁，避免另一 CPU 上并发执行的 `k_thread_abort()` 被阻塞整个转储过程。本选项限制快照可容纳的线程数。若受监控线程数超过此值，则只转储前 N 个。线程较多的系统可增大此值以捕获全部线程；代价是在致命错误处理路径的栈上占用 N 个指针的空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SMP && CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS && CONFIG_DEBUG_COREDUMP
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump）

**配置项引用（Symbol References）**：[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS)、[`CONFIG_DEBUG_COREDUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP)。

<a id="CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP"></a>

## 338.41 `CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP`

**提示（Prompt）**：仅转储栈顶（top of stack）

**说明（Help）**

只转储每个线程栈的顶部，而非整个栈区域。这里的栈顶区域从栈指针（stack pointer）开始，终点取栈末尾与配置限制中较小者；当前线程使用 `DEBUG_COREDUMP_THREAD_STACK_TOP_LIMIT_FOR_CURRENT`，其余线程使用 `DEBUG_COREDUMP_THREAD_STACK_TOP_LIMIT`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN || CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS) && CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR && CONFIG_DEBUG_COREDUMP
```

**默认值（Defaults）**

```text
y if CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:237`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L237)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN)、[`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS)、[`CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR)、[`CONFIG_DEBUG_COREDUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR`。

<a id="CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP_LIMIT"></a>

## 338.42 `CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP_LIMIT`

**提示（Prompt）**：非当前线程的栈顶大小上限

**说明（Help）**

异常发生时未在运行的线程，其栈最多转储的字节数。负值表示不限制，即一直转储到该栈区域的末尾。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP && CONFIG_DEBUG_COREDUMP
```

**默认值（Defaults）**

```text
-1
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:262`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L262)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 仅转储栈顶（top of stack）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP)、[`CONFIG_DEBUG_COREDUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP)。

<a id="CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP_LIMIT_FOR_CURRENT"></a>

## 338.43 `CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP_LIMIT_FOR_CURRENT`

**提示（Prompt）**：当前线程的栈顶大小上限

**说明（Help）**

异常发生时正在运行的线程，其栈最多转储的字节数。负值表示不限制，即一直转储到该栈区域的末尾。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP && CONFIG_DEBUG_COREDUMP
```

**默认值（Defaults）**

```text
CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP_LIMIT
```

**定义位置（Location）**：[`subsys/debug/coredump/Kconfig:253`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/Kconfig#L253)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 仅转储栈顶（top of stack）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP)、[`CONFIG_DEBUG_COREDUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP)、[`CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP_LIMIT`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP_LIMIT)。

<a id="CONFIG_DEBUG_THREAD_INFO"></a>

## 338.44 `CONFIG_DEBUG_THREAD_INFO`

**提示（Prompt）**：线程感知支持（Thread awareness）

**说明（Help）**

此选项导出内核结构体偏移量数组，使调试器的实时操作系统（RTOS）插件能够确定运行中线程的状态。在对称多处理（SMP）系统中，`thread_info.c` 的 `K_CURR_THREAD` 偏移量本身只反映 `cpus[0].current`；同时导出的 `CPU_STRIDE` 和 `NUM_CPUS` 允许理解这些字段的调试器插件读取每个 CPU 的当前线程，计算关系如下：

```c
cpus[i].current = K_CURR_THREAD + i * CPU_STRIDE
```

不了解这些新增字段的插件仍然只能看到 `cpus[0]`，行为与以前一致。这两个条目属于新增内容，不改变任何既有条目的含义。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_THREAD_MONITOR
CONFIG_THREAD_NAME
```

**被选择（Selected by）**

```text
CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS
CONFIG_DEBUG_COREDUMP_THREADS_METADATA
```

**定义位置（Location）**：[`subsys/debug/Kconfig:250`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L250)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_THREAD_NAME`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_NAME)、[`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS)、[`CONFIG_DEBUG_COREDUMP_THREADS_METADATA`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_THREADS_METADATA)。

<a id="CONFIG_EARLY_CONSOLE"></a>

## 338.45 `CONFIG_EARLY_CONSOLE`

**提示（Prompt）**：尽早启用标准输出（stdout）

**说明（Help）**

为了调试，此选项尽早启用标准输出（stdout）。例如，设置 `STDOUT_CONSOLE` 后，将提前初始化相应驱动，使 stdout 尽早通过控制台（console）输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SERIAL_HAS_POST_KERNEL_INIT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/debug/Kconfig:171`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L171)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL_HAS_POST_KERNEL_INIT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_POST_KERNEL_INIT)。

<a id="CONFIG_EXCEPTION_STACK_TRACE"></a>

## 338.46 `CONFIG_EXCEPTION_STACK_TRACE`

**提示（Prompt）**：尝试在异常时打印栈回溯（stack traces）

**说明（Help）**

如果体系结构的致命错误处理代码支持，则在报告异常时尝试打印由函数内存地址组成的栈回溯（stack trace）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_STACKWALK
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/debug/Kconfig:238`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L238)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_STACKWALK`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_STACKWALK)。

<a id="CONFIG_FORCE_NO_ASSERT"></a>

## 338.47 `CONFIG_FORCE_NO_ASSERT`

**提示（Prompt）**：强制禁用断言（原文：Force-disable no assertions）【已弃用 DEPRECATED】

**说明（Help）**

此布尔选项禁用 Zephyr 断言测试（assertion testing），即使断言通过 `CFLAGS` 而非 Kconfig 启用，例如 twister 场景。它只用于为特定测试绕过编译器缺陷。

已弃用：使用 `CONFIG_ASSERT=n` 禁用所有 ZASSERT 模块。译注：原文标题含有 “no assertions” 的歧义措辞；本说明按原文正文保留其“禁用断言”的作用。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/debug/zassert/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/zassert/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_GDBSTUB"></a>

## 338.48 `CONFIG_GDBSTUB`

**提示（Prompt）**：GDB 远程串行协议支持（Remote Serial Protocol）【实验性 EXPERIMENTAL】

**说明（Help）**

启用通过 GDB 或其他支持 GDB 协议的应用访问目标（target）的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_GDBSTUB
```

**主动选择（Selects）**

```text
CONFIG_UART_USE_RUNTIME_CONFIGURE if CONFIG_SERIAL
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/debug/gdbstub/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/gdbstub/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_GDBSTUB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_GDBSTUB)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_USE_RUNTIME_CONFIGURE)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_GDBSTUB`。

<a id="CONFIG_GDBSTUB_BUF_SZ"></a>

## 338.49 `CONFIG_GDBSTUB_BUF_SZ`

**提示（Prompt）**：GDB 后端发送／接收缓冲区大小（字节）

**说明（Help）**

指定 GDB 后端发送／接收缓冲区的大小，单位为字节。缓冲区必须足够大，能够一次容纳一个完整的 GDB 数据包（packet）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GDBSTUB
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`subsys/debug/gdbstub/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/gdbstub/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → GDB 远程串行协议支持（Remote Serial Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_GDBSTUB`](P338_subsys_debug_配置项参考.md#CONFIG_GDBSTUB)。

<a id="CONFIG_GDBSTUB_CUSTOM_BACKEND"></a>

## 338.50 `CONFIG_GDBSTUB_CUSTOM_BACKEND`

**提示（Prompt）**：使用自定义后端（custom backend）

**说明（Help）**

为 GDB 使用自定义后端（backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/debug/gdbstub/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/gdbstub/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → GDB 远程串行协议支持（Remote Serial Protocol）【实验性 EXPERIMENTAL】 → GDB 后端（backend）

<a id="CONFIG_GDBSTUB_ENTER_IMMEDIATELY"></a>

## 338.51 `CONFIG_GDBSTUB_ENTER_IMMEDIATELY`

**提示（Prompt）**：启动时停止执行并进入 GDB 调试桩（stub）

**说明（Help）**

作用类似 QEMU 的 `-S`。启用后，启动过程会在用户代码开始执行前停止，GDB 调试桩（stub）等待连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GDBSTUB
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/debug/gdbstub/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/gdbstub/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → GDB 远程串行协议支持（Remote Serial Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_GDBSTUB`](P338_subsys_debug_配置项参考.md#CONFIG_GDBSTUB)。

<a id="CONFIG_GDBSTUB_SERIAL_BACKEND"></a>

## 338.52 `CONFIG_GDBSTUB_SERIAL_BACKEND`

**提示（Prompt）**：使用串行后端（serial backend）

**说明（Help）**

使用串行接口作为 GDB 的后端（backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL && <choice>
```

**定义位置（Location）**：[`subsys/debug/gdbstub/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/gdbstub/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → GDB 远程串行协议支持（Remote Serial Protocol）【实验性 EXPERIMENTAL】 → GDB 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_GDBSTUB_TRACE"></a>

## 338.53 `CONFIG_GDBSTUB_TRACE`

**提示（Prompt）**：GDB 后端附加日志（extra logging）

**说明（Help）**

为 GDB 后端启用附加调试日志，包括断点中断（breakpoint interrupts）及其收到的远程命令（remote commands）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GDBSTUB
```

**定义位置（Location）**：[`subsys/debug/gdbstub/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/gdbstub/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → GDB 远程串行协议支持（Remote Serial Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_GDBSTUB`](P338_subsys_debug_配置项参考.md#CONFIG_GDBSTUB)。

<a id="CONFIG_GPROF"></a>

## 338.54 `CONFIG_GPROF`

**提示（Prompt）**：生成性能分析信息（profiling information）

**说明（Help）**

为应用生成可使用 gprof 分析的调用图性能数据（call graph profile data）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX
```

**定义位置（Location）**：[`subsys/debug/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)。

<a id="CONFIG_MIPI_STP_DECODER"></a>

## 338.55 `CONFIG_MIPI_STP_DECODER`

**提示（Prompt）**：MIPI STPv2 解码器（decoder）

**说明（Help）**

此模块对 STPv2 数据流进行解码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_BIG_ENDIAN
```

**被选择（Selected by）**

```text
CONFIG_DEBUG_NRF_ETR_DECODE
CONFIG_DEBUG_NRF_ETR_DEBUG
```

**定义位置（Location）**：[`subsys/debug/Kconfig:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L280)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_BIG_ENDIAN`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_BIG_ENDIAN)、[`CONFIG_DEBUG_NRF_ETR_DECODE`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_DECODE)、[`CONFIG_DEBUG_NRF_ETR_DEBUG`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_DEBUG)。

<a id="CONFIG_MSAN"></a>

## 338.56 `CONFIG_MSAN`

**提示（Prompt）**：使用内存消毒器（MemorySanitizer）构建

**说明（Help）**

启用 LLVM MemorySanitizer 构建 Zephyr。所译快照中仅支持 POSIX 体系结构，且要求主机编译器足够新、支持此功能，目前仅支持 x86_64 上的 clang。受 clang 限制，不能与 `CONFIG_ASAN` 同时使用，必须二选一；需要时可以与 `CONFIG_UBSAN` 组合使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX
```

**定义位置（Location）**：[`subsys/debug/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)。

<a id="CONFIG_OMIT_FRAME_POINTER"></a>

## 338.57 `CONFIG_OMIT_FRAME_POINTER`

**提示（Prompt）**：省略帧指针（frame pointer）

**说明（Help）**

选择 Y 可获得最佳性能。在包括 x86 的某些体系结构上，这会优先考虑代码大小和性能，而不是可调试性（debuggability）。若希望保留帧指针（frame pointer），请选择 N。若应用使用运行时回溯（runtime backtracing）但不支持解析栈展开表（unwind tables），保留帧指针可能有用。不确定时，请禁用 `OVERRIDE_FRAME_POINTER_DEFAULT`，让编译器为体系结构采用合理的默认设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_FRAME_POINTER && CONFIG_OVERRIDE_FRAME_POINTER_DEFAULT
```

**定义位置（Location）**：[`subsys/debug/Kconfig:219`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L219)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 覆盖编译器对 -fomit-frame-pointer 的默认设置

**配置项引用（Symbol References）**：[`CONFIG_FRAME_POINTER`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FRAME_POINTER)、[`CONFIG_OVERRIDE_FRAME_POINTER_DEFAULT`](P338_subsys_debug_配置项参考.md#CONFIG_OVERRIDE_FRAME_POINTER_DEFAULT)。

<a id="CONFIG_OVERRIDE_FRAME_POINTER_DEFAULT"></a>

## 338.58 `CONFIG_OVERRIDE_FRAME_POINTER_DEFAULT`

**提示（Prompt）**：覆盖编译器对 -fomit-frame-pointer 的默认设置

**说明（Help）**

省略帧指针（frame pointer）会避免编译器将栈帧指针放入寄存器，可减少函数序言／尾声（prologue/epilogue）中的若干指令，并释放一个通用寄存器；在 x86 等寄存器紧张的体系结构上，可能明显改善性能。

在包括 x86 的某些体系结构上，省略帧指针会使局部变量更难定位，从而妨碍调试。使用 `-O1` 及更高优化等级时，GCC 会自动启用 `-fomit-frame-pointer`，但前提是该体系结构的有效调试不依赖帧指针。若要覆盖编译器默认的帧指针行为，选择 Y；否则选择 N。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_FRAME_POINTER
```

**定义位置（Location）**：[`subsys/debug/Kconfig:203`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L203)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_FRAME_POINTER`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FRAME_POINTER)。

<a id="CONFIG_PRINTK"></a>

## 338.59 `CONFIG_PRINTK`

**提示（Prompt）**：将 printk() 输出发送到控制台（console）

**说明（Help）**

此选项将 `printk()` 调试输出发送到受支持的控制台设备，而不是完全抑制 `printk()` 输出的生成。输出立即发送，不使用互斥（mutual exclusion）或缓冲（buffering）。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_BOOT_BANNER
CONFIG_LOG
CONFIG_LOG_MODE_MINIMAL
```

**被弱选择（Implied by）**

```text
CONFIG_ASSERT
```

**定义位置（Location）**：[`subsys/debug/Kconfig:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_BOOT_BANNER`](P197_lib_配置项参考_1.md#CONFIG_BOOT_BANNER)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_LOG_MODE_MINIMAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_ASSERT`](P338_subsys_debug_配置项参考.md#CONFIG_ASSERT)。

<a id="CONFIG_PRINTK_BUFFER_SIZE"></a>

## 338.60 `CONFIG_PRINTK_BUFFER_SIZE`

**提示（Prompt）**：printk() 缓冲区大小（buffer size）

**说明（Help）**

启用用户空间（userspace）后，会缓冲 `printk()` 调用的输出，以免每输出一个字符都进行一次系统调用（system call）。本项指定该缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PRINTK && CONFIG_USERSPACE
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/debug/Kconfig:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 将 printk() 输出发送到控制台（console）

**配置项引用（Symbol References）**：[`CONFIG_PRINTK`](P338_subsys_debug_配置项参考.md#CONFIG_PRINTK)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)。

<a id="CONFIG_SEGGER_DEBUGMON"></a>

## 338.61 `CONFIG_SEGGER_DEBUGMON`

**提示（Prompt）**：使用 SEGGER 的 J-Link 调试监控（debug monitor）实现

**说明（Help）**

启用 SEGGER 的调试监控中断（debug monitor interrupt）实现，覆盖默认的 `z_arm_debug_monitor` 符号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CORTEX_M_DEBUG_MONITOR_HOOK
```

**定义位置（Location）**：[`subsys/debug/Kconfig:272`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L272)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_CORTEX_M_DEBUG_MONITOR_HOOK`](P029_arch_arm_配置项参考_1.md#CONFIG_CORTEX_M_DEBUG_MONITOR_HOOK)。

<a id="CONFIG_SPIN_LOCK_TIME_LIMIT"></a>

## 338.62 `CONFIG_SPIN_LOCK_TIME_LIMIT`

**提示（Prompt）**：自旋锁持有时间上限（时钟周期）

**说明（Help）**

在解锁时通过断言（assert）检查：持锁经历的系统时钟周期数必须小于配置值。要求定时器驱动的 `sys_clock_get_cycles_32()` 无锁（lock free）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ASSERT && CONFIG_SPIN_VALIDATE && CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/debug/Kconfig:191`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L191)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 自旋锁验证（Spinlock validation）

**配置项引用（Symbol References）**：[`CONFIG_ASSERT`](P338_subsys_debug_配置项参考.md#CONFIG_ASSERT)、[`CONFIG_SPIN_VALIDATE`](P338_subsys_debug_配置项参考.md#CONFIG_SPIN_VALIDATE)、[`CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT)。

<a id="CONFIG_SPIN_VALIDATE"></a>

## 338.63 `CONFIG_SPIN_VALIDATE`

**提示（Prompt）**：自旋锁验证（Spinlock validation）

**说明（Help）**

启用断言（asserts）后，可使用自旋锁验证框架（spinlock validation framework）。它会明显增加内核代码大小，约为 3k，因此不要在已知资源较少的平台上使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ASSERT && CONFIG_MULTITHREADING && (CONFIG_MP_MAX_NUM_CPUS <= 4 || (CONFIG_64BIT && CONFIG_MP_MAX_NUM_CPUS <= 8))
```

**定义位置（Location）**：[`subsys/debug/Kconfig:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_ASSERT`](P338_subsys_debug_配置项参考.md#CONFIG_ASSERT)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_MP_MAX_NUM_CPUS`](P001_kernel_配置项参考_1.md#CONFIG_MP_MAX_NUM_CPUS)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)。

<a id="CONFIG_STACK_SENTINEL"></a>

## 338.64 `CONFIG_STACK_SENTINEL`

**提示（Prompt）**：栈哨兵（Stack sentinel）

**说明（Help）**

在线程栈最低地址处存储一个魔数（magic value），定期检查它是否仍然存在；若不存在，则以受控方式终止线程。当前在四处检查：

1. 每次上下文切换时，检查即将切出的线程。
2. 硬件中断未引发上下文切换时，检查被中断的线程。
3. 线程从其入口函数返回时。
4. 线程调用 `k_yield()` 但未发生上下文切换时。

此功能无法防止内存损坏，届时系统也可能已经不可用。不过，栈溢出（stack overflow）会导致异常难解的行为，能够确定发生了栈溢出仍然很有价值。本功能面向缺乏硬件栈溢出保护，或系统资源不足以使用该硬件保护的系统。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && !CONFIG_USERSPACE && !CONFIG_MPU_STACK_GUARD
```

**主动选择（Selects）**

```text
CONFIG_THREAD_STACK_INFO
```

**定义位置（Location）**：[`subsys/debug/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_MPU_STACK_GUARD`](P028_arch_arc_配置项参考.md#CONFIG_MPU_STACK_GUARD)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)。

<a id="CONFIG_STACK_USAGE"></a>

## 338.65 `CONFIG_STACK_USAGE`

**提示（Prompt）**：生成栈使用量信息（stack usage information）

**说明（Help）**

生成附加文件，逐函数列出其最大栈使用量。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`subsys/debug/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

<a id="CONFIG_SYMTAB"></a>

## 338.66 `CONFIG_SYMTAB`

**提示（Prompt）**：生成符号表（symbol table）

**说明（Help）**

生成包含每个函数偏移量和名称的符号表（symbol table）。包含 `<zephyr/debug/symtab.h>` 头文件即可访问此表。若不了解本项的用途，请选择 N。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`subsys/debug/symtab/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/symtab/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

<a id="CONFIG_SYMTAB_SHELL"></a>

## 338.67 `CONFIG_SYMTAB_SHELL`

**提示（Prompt）**：符号表命令行命令（Symbol table shell commands）

**说明（Help）**

用于访问符号表（symbol table）的命令行命令（shell commands）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_SYMTAB
```

**定义位置（Location）**：[`subsys/debug/symtab/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/symtab/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 生成符号表（symbol table）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SYMTAB`](P338_subsys_debug_配置项参考.md#CONFIG_SYMTAB)。

<a id="CONFIG_THREAD_ANALYZER"></a>

## 338.68 `CONFIG_THREAD_ANALYZER`

**提示（Prompt）**：线程分析器（Thread Analyzer）

**说明（Help）**

启用线程分析器（thread analyzer）及其所需的所有模块。可用它调试线程配置问题，例如检查栈大小配置以发现栈溢出（stack overflow），或找出可优化大小的栈。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ARCH_POSIX
```

**主动选择（Selects）**

```text
CONFIG_INIT_STACKS
CONFIG_THREAD_MONITOR
CONFIG_THREAD_STACK_INFO
```

**定义位置（Location）**：[`subsys/debug/thread_analyzer/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/thread_analyzer/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_INIT_STACKS`](P001_kernel_配置项参考_1.md#CONFIG_INIT_STACKS)、[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)。

<a id="CONFIG_THREAD_ANALYZER_AUTO"></a>

## 338.69 `CONFIG_THREAD_ANALYZER_AUTO`

**提示（Prompt）**：在线程中运行周期性线程分析

**说明（Help）**

自动运行线程分析器（thread analyzer），无需向应用添加代码；它将定期执行线程分析。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_ANALYZER
```

**定义位置（Location）**：[`subsys/debug/thread_analyzer/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/thread_analyzer/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER)。

<a id="CONFIG_THREAD_ANALYZER_AUTO_INTERVAL"></a>

## 338.70 `CONFIG_THREAD_ANALYZER_AUTO_INTERVAL`

**提示（Prompt）**：线程分析间隔（Thread analysis interval）

**说明（Help）**

调用线程分析器周期性打印函数的时间间隔，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_ANALYZER_AUTO && CONFIG_THREAD_ANALYZER
```

**默认值（Defaults）**

```text
60
```

**取值范围（Ranges）**

```text
[5, 3600]
```

**定义位置（Location）**：[`subsys/debug/thread_analyzer/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/thread_analyzer/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer） → 在线程中运行周期性线程分析

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER_AUTO`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER_AUTO)、[`CONFIG_THREAD_ANALYZER`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER)。

<a id="CONFIG_THREAD_ANALYZER_AUTO_SEPARATE_CORES"></a>

## 338.71 `CONFIG_THREAD_ANALYZER_AUTO_SEPARATE_CORES`

**提示（Prompt）**：在每个核心上分别运行线程分析器

**说明（Help）**

在每个核心上运行线程分析器的自动分析线程，并分别报告各核心的结果。运行在缓存不一致（cache-incoherent）体系结构上的平台需要此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SCHED_CPU_MASK && CONFIG_THREAD_ANALYZER_AUTO && CONFIG_THREAD_ANALYZER
```

**默认值（Defaults）**

```text
y if CONFIG_KERNEL_COHERENCE
```

**定义位置（Location）**：[`subsys/debug/thread_analyzer/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/thread_analyzer/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer） → 在线程中运行周期性线程分析

**配置项引用（Symbol References）**：[`CONFIG_SCHED_CPU_MASK`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_CPU_MASK)、[`CONFIG_THREAD_ANALYZER_AUTO`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER_AUTO)、[`CONFIG_THREAD_ANALYZER`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER)、[`CONFIG_KERNEL_COHERENCE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_COHERENCE)。

<a id="CONFIG_THREAD_ANALYZER_AUTO_STACK_SIZE"></a>

## 338.72 `CONFIG_THREAD_ANALYZER_AUTO_STACK_SIZE`

**提示（Prompt）**：周期性线程分析线程的栈大小（stack size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_ANALYZER_AUTO && CONFIG_THREAD_ANALYZER
```

**默认值（Defaults）**

```text
2048 if CONFIG_THREAD_ANALYZER_USE_LOG && CONFIG_LOG_MODE_IMMEDIATE && CONFIG_NO_OPTIMIZATIONS
1024
```

**定义位置（Location）**：[`subsys/debug/thread_analyzer/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/thread_analyzer/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer） → 在线程中运行周期性线程分析

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER_AUTO`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER_AUTO)、[`CONFIG_THREAD_ANALYZER`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER)、[`CONFIG_THREAD_ANALYZER_USE_LOG`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER_USE_LOG)、[`CONFIG_LOG_MODE_IMMEDIATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MODE_IMMEDIATE)、[`CONFIG_NO_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NO_OPTIMIZATIONS)。

<a id="CONFIG_THREAD_ANALYZER_AUTO_THREAD_PRIORITY"></a>

## 338.73 `CONFIG_THREAD_ANALYZER_AUTO_THREAD_PRIORITY`

**提示（Prompt）**：线程分析线程的优先级（priority）

**说明（Help）**

设置执行线程分析的线程优先级（thread priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_ANALYZER_AUTO_THREAD_PRIORITY_OVERRIDE && CONFIG_THREAD_ANALYZER_AUTO && CONFIG_THREAD_ANALYZER
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/debug/thread_analyzer/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/thread_analyzer/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer） → 在线程中运行周期性线程分析 → 覆盖默认的线程分析线程优先级

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER_AUTO_THREAD_PRIORITY_OVERRIDE`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER_AUTO_THREAD_PRIORITY_OVERRIDE)、[`CONFIG_THREAD_ANALYZER_AUTO`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER_AUTO)、[`CONFIG_THREAD_ANALYZER`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER)。

<a id="CONFIG_THREAD_ANALYZER_AUTO_THREAD_PRIORITY_OVERRIDE"></a>

## 338.74 `CONFIG_THREAD_ANALYZER_AUTO_THREAD_PRIORITY_OVERRIDE`

**提示（Prompt）**：覆盖默认的线程分析线程优先级

**说明（Help）**

允许更改线程分析线程的默认优先级（priority）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_ANALYZER_AUTO && CONFIG_THREAD_ANALYZER
```

**定义位置（Location）**：[`subsys/debug/thread_analyzer/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/thread_analyzer/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer） → 在线程中运行周期性线程分析

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER_AUTO`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER_AUTO)、[`CONFIG_THREAD_ANALYZER`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER)。

<a id="CONFIG_THREAD_ANALYZER_ISR_STACK_USAGE"></a>

## 338.75 `CONFIG_THREAD_ANALYZER_ISR_STACK_USAGE`

**提示（Prompt）**：分析中断栈（interrupt stacks）使用量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_ANALYZER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/debug/thread_analyzer/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/thread_analyzer/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER)。

<a id="CONFIG_THREAD_ANALYZER_LONG_FRAME_PER_INTERVAL"></a>

## 338.76 `CONFIG_THREAD_ANALYZER_LONG_FRAME_PER_INTERVAL`

**提示（Prompt）**：打印自上次线程分析间隔以来的最长栈帧（longest frame）

**说明（Help）**

打印后重置线程的最长栈帧（longest frame）字段，使下次打印显示该时间区间内的最长栈帧，从而能够观察线程初始启动后出现了哪些较长的栈帧。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SCHED_THREAD_USAGE_ANALYSIS && CONFIG_THREAD_ANALYZER
```

**定义位置（Location）**：[`subsys/debug/thread_analyzer/Kconfig:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/thread_analyzer/Kconfig#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer）

**配置项引用（Symbol References）**：[`CONFIG_SCHED_THREAD_USAGE_ANALYSIS`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_THREAD_USAGE_ANALYSIS)、[`CONFIG_THREAD_ANALYZER`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER)。

<a id="CONFIG_THREAD_ANALYZER_PRINT_THREAD_PRIORITY"></a>

## 338.77 `CONFIG_THREAD_ANALYZER_PRINT_THREAD_PRIORITY`

**提示（Prompt）**：打印每个线程的优先级（priority）

**说明（Help）**

在打印输出中包含每个线程的优先级（priority）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_ANALYZER
```

**定义位置（Location）**：[`subsys/debug/thread_analyzer/Kconfig:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/thread_analyzer/Kconfig#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER)。

<a id="CONFIG_THREAD_ANALYZER_PRIV_STACK_USAGE"></a>

## 338.78 `CONFIG_THREAD_ANALYZER_PRIV_STACK_USAGE`

**提示（Prompt）**：分析特权栈（privileged stacks）使用量

**说明（Help）**

打印用户线程（user threads）的特权栈（privileged stack）使用量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE && CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET && CONFIG_THREAD_ANALYZER
```

**定义位置（Location）**：[`subsys/debug/thread_analyzer/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/thread_analyzer/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET)、[`CONFIG_THREAD_ANALYZER`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER)。

<a id="CONFIG_THREAD_ANALYZER_RUN_UNLOCKED"></a>

## 338.79 `CONFIG_THREAD_ANALYZER_RUN_UNLOCKED`

**提示（Prompt）**：在不锁定中断的情况下运行分析

**说明（Help）**

线程分析耗时较长：对找到的每个线程，会逐字检查其栈，查找不匹配魔数（magic number）的内容。通常分析线程时使用 `k_thread_foreach`；从线程链表的角度看，这样是安全的，但可能长时间锁定中断，甚至导致蓝牙（Bluetooth）通信断开。

设置此标志后，线程分析器将改用 `k_thread_foreach_unlocked`，允许在线程分析期间处理中断。这种配置的限制请参阅 `k_thread_foreach` 文档。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_ANALYZER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/debug/thread_analyzer/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/thread_analyzer/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER)。

<a id="CONFIG_THREAD_ANALYZER_STACK_SAFETY"></a>

## 338.80 `CONFIG_THREAD_ANALYZER_STACK_SAFETY`

**提示（Prompt）**：在线程分析中加入线程运行时栈安全检查

**说明（Help）**

启用后，当某线程的未用栈空间低于其配置阈值（threshold）时，栈使用量分析会调用可自定义的处理函数（handler）。该处理函数可以记录警告、挂起线程，甚至中止线程。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_ANALYZER
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_THREAD_RUNTIME_STACK_SAFETY
```

**定义位置（Location）**：[`subsys/debug/thread_analyzer/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/thread_analyzer/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER)、[`CONFIG_THREAD_RUNTIME_STACK_SAFETY`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_RUNTIME_STACK_SAFETY)。

<a id="CONFIG_THREAD_ANALYZER_USE_LOG"></a>

## 338.81 `CONFIG_THREAD_ANALYZER_USE_LOG`

**提示（Prompt）**：使用日志输出（logger output）

**说明（Help）**

使用日志输出（logger output）打印线程信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_LOG
```

**定义位置（Location）**：[`subsys/debug/thread_analyzer/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/thread_analyzer/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer） → 线程分析打印模式（print mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)。

<a id="CONFIG_THREAD_ANALYZER_USE_PRINTK"></a>

## 338.82 `CONFIG_THREAD_ANALYZER_USE_PRINTK`

**提示（Prompt）**：使用 printk 函数

**说明（Help）**

使用内核 `printk` 函数打印线程信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/debug/thread_analyzer/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/thread_analyzer/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer） → 线程分析打印模式（print mode）

<a id="CONFIG_UBSAN"></a>

## 338.83 `CONFIG_UBSAN`

**提示（Prompt）**：使用未定义行为消毒器（Undefined Behavior Sanitizer）构建

**说明（Help）**

启用未定义行为消毒器（Undefined Behavior Sanitizer）构建 Zephyr。需要较新的编译器支持 `-fsanitize=undefined` 命令行选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`subsys/debug/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options）

<a id="CONFIG_UBSAN_LIBRARY"></a>

## 338.84 `CONFIG_UBSAN_LIBRARY`

**提示（Prompt）**：调用 ubsan 例程（routines）

**说明（Help）**

运行时检测到未定义行为（undefined behavior）时，调用 ubsan 库例程，提供错误条件、源文件名、行号，以及相关类型和值的信息。目前仅支持基于 POSIX 体系结构的开发板，或使用 picolibc 的构建。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ARCH_POSIX || CONFIG_PICOLIBC) && <choice CONFIG_UBSAN_MODE>
```

**定义位置（Location）**：[`subsys/debug/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 使用未定义行为消毒器（Undefined Behavior Sanitizer）构建 → 未定义行为消毒器模式（Undefined behavior sanitizer mode）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_PICOLIBC`](P198_lib_配置项参考_2.md#CONFIG_PICOLIBC)、[`CONFIG_UBSAN_MODE`](P338_subsys_debug_配置项参考.md#CONFIG_UBSAN_MODE)。

<a id="CONFIG_UBSAN_MODE"></a>

## 338.85 `CONFIG_UBSAN_MODE`

**提示（Prompt）**：未定义行为消毒器模式（Undefined behavior sanitizer mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UBSAN
```

**默认值（Defaults）**

```text
CONFIG_UBSAN_LIBRARY
```

**可选项（Choices）**

```text
CONFIG_UBSAN_LIBRARY
CONFIG_UBSAN_TRAP
```

**定义位置（Location）**：[`subsys/debug/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 使用未定义行为消毒器（Undefined Behavior Sanitizer）构建

**配置项引用（Symbol References）**：[`CONFIG_UBSAN`](P338_subsys_debug_配置项参考.md#CONFIG_UBSAN)、[`CONFIG_UBSAN_LIBRARY`](P338_subsys_debug_配置项参考.md#CONFIG_UBSAN_LIBRARY)、[`CONFIG_UBSAN_TRAP`](P338_subsys_debug_配置项参考.md#CONFIG_UBSAN_TRAP)。

<a id="CONFIG_UBSAN_TRAP"></a>

## 338.86 `CONFIG_UBSAN_TRAP`

**提示（Prompt）**：调用 __builtin_trap

**说明（Help）**

检测到未定义行为（undefined behavior）时，调用 `__builtin_trap` 引发异常。任何目标（target）都可使用此方式，但提供的信息较少，因此难以确定触发问题的代码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UBSAN_MODE>
```

**定义位置（Location）**：[`subsys/debug/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 使用未定义行为消毒器（Undefined Behavior Sanitizer）构建 → 未定义行为消毒器模式（Undefined behavior sanitizer mode）

**配置项引用（Symbol References）**：[`CONFIG_UBSAN_MODE`](P338_subsys_debug_配置项参考.md#CONFIG_UBSAN_MODE)。

<!-- kconfig-navigation -->

[上一章](P337_subsys_dap_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P339_subsys_dfu_配置项参考.md)
