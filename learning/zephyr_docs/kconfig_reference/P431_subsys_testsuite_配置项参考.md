---
id: learning.zephyr-docs.kconfig-reference.page-431
title: "`subsys/testsuite`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第431章\_`subsys/testsuite`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/testsuite` 的 66 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_COVERAGE"></a>

## 431.1 `CONFIG_COVERAGE`

**提示（Prompt）**：生成覆盖率数据（Coverage data）

**说明（Help）**

使用 `-coverage` 选项构建应用，生成可用于制作覆盖率报告（Coverage report）的数据。更多信息参见 [Zephyr 覆盖率文档](https://docs.zephyrproject.org/latest/develop/test/coverage.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_COVERAGE_SUPPORT
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig.coverage:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig.coverage#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 覆盖率（Coverage）

**配置项引用（Symbol References）**：[`CONFIG_HAS_COVERAGE_SUPPORT`](P431_subsys_testsuite_配置项参考.md#CONFIG_HAS_COVERAGE_SUPPORT)。

<a id="CONFIG_COVERAGE_DUMP"></a>

## 431.2 `CONFIG_COVERAGE_DUMP`

**提示（Prompt）**：退出时将覆盖率数据（Coverage data）转储到控制台

**说明（Help）**

退出时，将收集的覆盖率信息（Coverage information）转储到控制台。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COVERAGE_DUMP_METHOD>
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig.coverage:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig.coverage#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 覆盖率（Coverage） → 覆盖率数据转储方式（Dump method）

**配置项引用（Symbol References）**：[`CONFIG_COVERAGE_DUMP_METHOD`](P431_subsys_testsuite_配置项参考.md#CONFIG_COVERAGE_DUMP_METHOD)。

<a id="CONFIG_COVERAGE_DUMP_METHOD"></a>

## 431.3 `CONFIG_COVERAGE_DUMP_METHOD`

**提示（Prompt）**：覆盖率数据转储方式（Dump method）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COVERAGE_GCOV
```

**默认值（Defaults）**

```text
CONFIG_COVERAGE_DUMP
```

**可选项（Choices）**

```text
CONFIG_COVERAGE_DUMP
CONFIG_COVERAGE_SEMIHOST
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig.coverage:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig.coverage#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 覆盖率（Coverage）

**配置项引用（Symbol References）**：[`CONFIG_COVERAGE_GCOV`](P431_subsys_testsuite_配置项参考.md#CONFIG_COVERAGE_GCOV)、[`CONFIG_COVERAGE_DUMP`](P431_subsys_testsuite_配置项参考.md#CONFIG_COVERAGE_DUMP)、[`CONFIG_COVERAGE_SEMIHOST`](P431_subsys_testsuite_配置项参考.md#CONFIG_COVERAGE_SEMIHOST)。

<a id="CONFIG_COVERAGE_DUMP_PATH_EXCLUDE"></a>

## 431.4 `CONFIG_COVERAGE_DUMP_PATH_EXCLUDE`

**提示（Prompt）**：从覆盖率数据中排除匹配此模式（Pattern）的文件

**说明（Help）**

使用 POSIX 的 `fnmatch` 函数将文件名与模式（Pattern）匹配。文件名依据其在构建目录中的路径，而不是原始源码树中的路径。空字符串 `""` 禁用模式匹配。

**类型（Type）**：字符串（String），`string`。

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig.coverage:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig.coverage#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 覆盖率（Coverage）

<a id="CONFIG_COVERAGE_GCOV"></a>

## 431.5 `CONFIG_COVERAGE_GCOV`

**提示（Prompt）**：从硬件平台生成覆盖率数据（Coverage data）

**说明（Help）**

选择自定义 gcov 库，通过串口提供报告。可将串口转储交给 `gen_gcov_files.py`，生成所需的 `.gcda` 文件，再由 gcov 工具读取。更多信息参见原文所列的 `gcovr.com`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NATIVE_BUILD && <choice>
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig.coverage:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig.coverage#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 覆盖率（Coverage） → 生成覆盖率数据（Coverage data） → 覆盖率模式（Coverage mode）

**配置项引用（Symbol References）**：[`CONFIG_NATIVE_BUILD`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NATIVE_BUILD)。

<a id="CONFIG_COVERAGE_GCOV_HEAP_SIZE"></a>

## 431.6 `CONFIG_COVERAGE_GCOV_HEAP_SIZE`

**提示（Prompt）**：为 gcov 覆盖率数据转储分配的堆大小（Heap size）

**说明（Help）**

配置通过串口转储 gcov 覆盖率数据（Coverage data）所用的堆大小。设为 0 时不使用缓冲区，直接经串口转储数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COVERAGE_GCOV
```

**默认值（Defaults）**

```text
65536 if CONFIG_X86 || CONFIG_SOC_SERIES_MPS2
16384
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig.coverage:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig.coverage#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 覆盖率（Coverage）

**配置项引用（Symbol References）**：[`CONFIG_COVERAGE_GCOV`](P431_subsys_testsuite_配置项参考.md#CONFIG_COVERAGE_GCOV)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_SOC_SERIES_MPS2`](P263_soc_arm_配置项参考.md#CONFIG_SOC_SERIES_MPS2)。

<a id="CONFIG_COVERAGE_NATIVE_GCOV"></a>

## 431.7 `CONFIG_COVERAGE_NATIVE_GCOV`

**提示（Prompt）**：宿主编译器基于 gcov 的代码覆盖率（Code coverage）

**说明（Help）**

使用编译器标准 `--coverage` 选项进行原生构建，即采用兼容 gcov/GCC 的覆盖率（Coverage）方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NATIVE_BUILD && <choice>
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig.coverage:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig.coverage#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 覆盖率（Coverage） → 生成覆盖率数据（Coverage data） → 覆盖率模式（Coverage mode）

**配置项引用（Symbol References）**：[`CONFIG_NATIVE_BUILD`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NATIVE_BUILD)。

<a id="CONFIG_COVERAGE_NATIVE_SOURCE"></a>

## 431.8 `CONFIG_COVERAGE_NATIVE_SOURCE`

**提示（Prompt）**：宿主编译器基于源码的代码覆盖率（Source-based code coverage）

**说明（Help）**

使用编译器基于源码的覆盖率（Source-based coverage）选项进行原生构建。目前仅 LLVM 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NATIVE_BUILD && "" = "llvm" && <choice>
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig.coverage:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig.coverage#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 覆盖率（Coverage） → 生成覆盖率数据（Coverage data） → 覆盖率模式（Coverage mode）

**配置项引用（Symbol References）**：[`CONFIG_NATIVE_BUILD`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NATIVE_BUILD)。

<a id="CONFIG_COVERAGE_SEMIHOST"></a>

## 431.9 `CONFIG_COVERAGE_SEMIHOST`

**提示（Prompt）**：使用半主机（Semihosting）写出覆盖率数据

**说明（Help）**

使用半主机（Semihosting）将覆盖率数据写入宿主机文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SEMIHOST && <choice CONFIG_COVERAGE_DUMP_METHOD>
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig.coverage:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig.coverage#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 覆盖率（Coverage） → 覆盖率数据转储方式（Dump method）

**配置项引用（Symbol References）**：[`CONFIG_SEMIHOST`](P032_arch_common_配置项参考.md#CONFIG_SEMIHOST)、[`CONFIG_COVERAGE_DUMP_METHOD`](P431_subsys_testsuite_配置项参考.md#CONFIG_COVERAGE_DUMP_METHOD)。

<a id="CONFIG_FORCE_COVERAGE"></a>

## 431.10 `CONFIG_FORCE_COVERAGE`

**提示（Prompt）**：强制启用覆盖率（Force coverage）

**说明（Help）**

无论平台是否支持，都启用覆盖率数据（Coverage data）生成。如果平台默认不支持覆盖率，设置此项也不保证能够收集数据；应用可能无法装入可用内存，或在运行时崩溃。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_HAS_COVERAGE_SUPPORT
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig.coverage:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig.coverage#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 覆盖率（Coverage）

**配置项引用（Symbol References）**：[`CONFIG_HAS_COVERAGE_SUPPORT`](P431_subsys_testsuite_配置项参考.md#CONFIG_HAS_COVERAGE_SUPPORT)。

<a id="CONFIG_HAS_COVERAGE_SUPPORT"></a>

## 431.11 `CONFIG_HAS_COVERAGE_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

代码覆盖率报告（Code coverage report）生成功能仅适用于有足够空闲 RAM 缓冲覆盖率数据的开发板，或基于 POSIX 架构（POSIX ARCH）的开发板。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_INTEL_ISH
CONFIG_ARCH_POSIX
CONFIG_FORCE_COVERAGE
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig.coverage:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig.coverage#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 覆盖率（Coverage）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ISH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ISH)、[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_FORCE_COVERAGE`](P431_subsys_testsuite_配置项参考.md#CONFIG_FORCE_COVERAGE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ISH`。

<a id="CONFIG_TEST"></a>

## 431.12 `CONFIG_TEST`

**提示（Prompt）**：将项目标记为测试（Test）

**说明（Help）**

将项目或应用标记为测试（Test），以启用若干测试默认配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_THREAD_NAME
```

**被选择（Selected by）**

```text
CONFIG_ZTEST
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_NAME`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_NAME)、[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_TEST_ARM_CORTEX_M"></a>

## 431.13 `CONFIG_TEST_ARM_CORTEX_M`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

测试所需的 ARM Cortex-M 配置，用于选择栈大小并启用测试功能。构建安全 ARMv8-M 固件（Secure firmware）时，此选项还强制将 BusFault、HardFault 和不可屏蔽中断（NMI）异常路由到安全状态（Secure State），让测试套件能够在测试中使用它们。注意，默认情况下，以 `ARM_SECURE_FIRMWARE` 构建时，这些异常的目标状态设为非安全状态（Non-Secure state）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M && CONFIG_TEST
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ARM_SECURE_BUSFAULT_HARDFAULT_NMI if CONFIG_ARM_SECURE_FIRMWARE
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_TEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_TEST)、[`CONFIG_ARM_SECURE_BUSFAULT_HARDFAULT_NMI`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_SECURE_BUSFAULT_HARDFAULT_NMI)、[`CONFIG_ARM_SECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_SECURE_FIRMWARE)。

<a id="CONFIG_TEST_BUSY_SIM"></a>

## 431.14 `CONFIG_TEST_BUSY_SIM`

**提示（Prompt）**：忙碌模拟器（Busy simulator）

**说明（Help）**

使用计数器设备（Counter device）产生随机间隔的中断，并在中断中随机忙循环（Busy loop），以模拟 CPU 负载。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TEST
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_GENERATOR
CONFIG_COUNTER
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing）

**配置项引用（Symbol References）**：[`CONFIG_TEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_TEST)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_TEST_CAPTURE"></a>

## 431.15 `CONFIG_TEST_CAPTURE`

**提示（Prompt）**：测试输出捕获（Test output capture）

**说明（Help）**

启用 `tc_capture` 辅助功能（`zephyr/tc_capture.h`），将 `printk` 和日志输出记录到内存缓冲区，使测试能够对运行期间生成的文本进行断言（Assertion）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TEST
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing）

**配置项引用（Symbol References）**：[`CONFIG_TEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_TEST)。

<a id="CONFIG_TEST_CAPTURE_BUFFER_SIZE"></a>

## 431.16 `CONFIG_TEST_CAPTURE_BUFFER_SIZE`

**提示（Prompt）**：测试输出捕获缓冲区大小（Capture buffer size）

**说明（Help）**

用于保存捕获测试输出的缓冲区大小，单位为字节。超过此大小的输出会被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TEST_CAPTURE
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → 测试输出捕获（Test output capture）

**配置项引用（Symbol References）**：[`CONFIG_TEST_CAPTURE`](P431_subsys_testsuite_配置项参考.md#CONFIG_TEST_CAPTURE)。

<a id="CONFIG_TEST_ENABLE_USERSPACE"></a>

## 431.17 `CONFIG_TEST_ENABLE_USERSPACE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，实现 `TEST_USERSPACE` 逻辑。当设置 `CONFIG_ARCH_HAS_USERSPACE`，且测试用例通过 `CONFIG_TEST_USERSPACE` 表明要测试用户模式（User mode）时，启用 `USERSPACE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TEST_USERSPACE && CONFIG_ARCH_HAS_USERSPACE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USERSPACE
```

**弱选择（Implies）**

```text
CONFIG_DYNAMIC_OBJECTS
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing）

**配置项引用（Symbol References）**：[`CONFIG_TEST_USERSPACE`](P431_subsys_testsuite_配置项参考.md#CONFIG_TEST_USERSPACE)、[`CONFIG_ARCH_HAS_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_USERSPACE)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_DYNAMIC_OBJECTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_OBJECTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_USERSPACE`。

<a id="CONFIG_TEST_EXTRA_STACK_SIZE"></a>

## 431.18 `CONFIG_TEST_EXTRA_STACK_SIZE`

**提示（Prompt）**：测试函数的额外线程栈大小（Extra thread stack size）

**说明（Help）**

在某些默认栈大小不足的平台上，为测试提供额外栈空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TEST
```

**默认值（Defaults）**

```text
2048 if CONFIG_COVERAGE_GCOV
768 if CONFIG_XTENSA
128 if CONFIG_OPENRISC
0
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → 将项目标记为测试（Test）

**配置项引用（Symbol References）**：[`CONFIG_TEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_TEST)、[`CONFIG_COVERAGE_GCOV`](P431_subsys_testsuite_配置项参考.md#CONFIG_COVERAGE_GCOV)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_OPENRISC`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_OPENRISC)。

<a id="CONFIG_TEST_FLASH_DRIVERS"></a>

## 431.19 `CONFIG_TEST_FLASH_DRIVERS`

**提示（Prompt）**：测试闪存驱动（Flash drivers）

**说明（Help）**

辅助测试闪存驱动（Flash driver）。仅在使用 `qemu_x86` 时才应启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BOARD_QEMU_X86
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_QEMU_X86`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_QEMU_X86)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_QEMU_X86`。

<a id="CONFIG_TEST_HW_STACK_PROTECTION"></a>

## 431.20 `CONFIG_TEST_HW_STACK_PROTECTION`

**提示（Prompt）**：硬件可用时启用基于硬件的栈溢出检测（Stack overflow detection）

**说明（Help）**

硬件支持时，默认对全部测试用例启用基于硬件的栈保护（Hardware-based stack protection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_STACK_PROTECTION && CONFIG_TEST
```

**默认值（Defaults）**

```text
y if !CONFIG_TEST_USERSPACE_WITHOUT_HW_STACK_PROTECTION
```

**主动选择（Selects）**

```text
CONFIG_HW_STACK_PROTECTION
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACK_PROTECTION)、[`CONFIG_TEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_TEST)、[`CONFIG_TEST_USERSPACE_WITHOUT_HW_STACK_PROTECTION`](P431_subsys_testsuite_配置项参考.md#CONFIG_TEST_USERSPACE_WITHOUT_HW_STACK_PROTECTION)、[`CONFIG_HW_STACK_PROTECTION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_HW_STACK_PROTECTION)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_STACK_PROTECTION`。

<a id="CONFIG_TEST_LOGGING_DEFAULTS"></a>

## 431.21 `CONFIG_TEST_LOGGING_DEFAULTS`

**提示（Prompt）**：测试用例日志默认配置（Logging defaults）

**说明（Help）**

实现默认策略：为全部测试用例启用最小模式（Minimal mode）日志。需要其他日志配置或完全不需要日志的测试，应在项目级 `defconfig` 中禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TEST
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_LOG
CONFIG_LOG_DEFAULT_MINIMAL
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing）

**配置项引用（Symbol References）**：[`CONFIG_TEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_TEST)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_DEFAULT_MINIMAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_DEFAULT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LOG_DEFAULT_MINIMAL`。

<a id="CONFIG_TEST_LOGGING_FLUSH_AFTER_TEST"></a>

## 431.22 `CONFIG_TEST_LOGGING_FLUSH_AFTER_TEST`

**提示（Prompt）**：启用后，每个测试用例结束后刷新日志（Flush logs）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && CONFIG_ZTEST
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_TEST_USERSPACE"></a>

## 431.23 `CONFIG_TEST_USERSPACE`

**提示（Prompt）**：表明此测试使用用户模式（User mode）

**说明（Help）**

表示测试用例会使线程进入用户模式（User mode），如果平台支持，构建系统将覆盖相关设置并启用 `USERSPACE`。应针对各测试分别在 `.conf` 文件中设置，不应用于测试用例之外。使用此选项的测试还应在 `testcase.yaml` 中设置 `userspace` 过滤标签。未启用用户空间时，相关 API 是空操作（No-op），因此即便测试运行在不支持用户空间的平台，也可设置此项；测试仍应能运行，只是全部线程都处于监督者模式（Supervisor mode）。如果测试必须启用用户空间才能通过，则应在 `testcase.yaml` 中通过 `CONFIG_ARCH_HAS_USERSPACE` 过滤平台。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`subsys/testsuite/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing）

<a id="CONFIG_TEST_USERSPACE_WITHOUT_HW_STACK_PROTECTION"></a>

## 431.24 `CONFIG_TEST_USERSPACE_WITHOUT_HW_STACK_PROTECTION`

**提示（Prompt）**：运行用户模式测试时不额外启用栈保护（Stack protection）

**说明（Help）**

硬件平台的内存保护单元或内存管理单元（MPU/MMU）能力可能不足以在同时启用用户模式（User Mode）和硬件栈保护（HW Stack Protection）时运行全部测试。对于这些平台，执行用户模式相关测试时不启用硬件栈保护。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TEST_ENABLE_USERSPACE
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_KE1XF || CONFIG_SOC_SERIES_S32K1
```

**定义位置（Location）**：[`subsys/testsuite/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing）

**配置项引用（Symbol References）**：[`CONFIG_TEST_ENABLE_USERSPACE`](P431_subsys_testsuite_配置项参考.md#CONFIG_TEST_ENABLE_USERSPACE)、[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_SERIES_S32K1`。

<a id="CONFIG_ZTEST"></a>

## 431.25 `CONFIG_ZTEST`

**提示（Prompt）**：Zephyr 测试框架（Testing framework）

**说明（Help）**

启用 Zephyr 测试框架（Testing framework），仅在编写自动化测试时才应启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_TEST
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing）

**配置项引用（Symbol References）**：[`CONFIG_TEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_TEST)。

<a id="CONFIG_ZTEST_ASSERT_HOOK"></a>

## 431.26 `CONFIG_ZTEST_ASSERT_HOOK`

**提示（Prompt）**：使用预定义断言处理程序与钩子函数（Assert handler and hook）

**说明（Help）**

使用预定义的通用断言失败处理程序（Assert-fail handler）和后置钩子（Post hook）执行测试用例所需动作，常用于错误场景测试。通过 Twister 运行测试时，记得在 YAML 文件中添加 `ignore_fault` 标签。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_ASSERT_VERBOSE"></a>

## 431.27 `CONFIG_ZTEST_ASSERT_VERBOSE`

**提示（Prompt）**：断言详细程度（Assertion verbosity level）

**说明（Help）**

设置断言（Assertion）的输出详细程度：

- 0：失败断言只输出文件和行号。
- 1：失败断言输出文件、行号、函数和原因。
- 2：同时记录成功的断言。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_BENCHMARK"></a>

## 431.28 `CONFIG_ZTEST_BENCHMARK`

**提示（Prompt）**：Ztest 基准测试功能（Benchmarking features）［实验性，Experimental］

**说明（Help）**

启用基准测试（Benchmarking）所需的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_TIMING_FUNCTIONS
CONFIG_REQUIRES_FULL_LIBC
CONFIG_REQUIRES_FLOAT_PRINTF
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/testsuite/ztest/benchmark/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/benchmark/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → 基准测试选项（Benchmarking options）

**配置项引用（Symbol References）**：[`CONFIG_TIMING_FUNCTIONS`](P432_subsys_timing_配置项参考.md#CONFIG_TIMING_FUNCTIONS)、[`CONFIG_REQUIRES_FULL_LIBC`](P198_lib_配置项参考_2.md#CONFIG_REQUIRES_FULL_LIBC)、[`CONFIG_REQUIRES_FLOAT_PRINTF`](P198_lib_配置项参考_2.md#CONFIG_REQUIRES_FLOAT_PRINTF)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_ZTEST_BENCHMARK_MAX_SAMPLES"></a>

## 431.29 `CONFIG_ZTEST_BENCHMARK_MAX_SAMPLES`

**提示（Prompt）**：为百分位数（Percentile）保留的样本数量

**说明（Help）**

样本缓冲区的容量，以每个 8 字节的样本数表示。一次只运行一个基准测试（Benchmark），因此全部测试共用一个该大小的缓冲区。容量至少应覆盖最大基准测试的样本数：保留的是最先采集的样本，而不是整个运行过程的抽样；若只保留前缀，计算出的百分位数会漏掉缓冲区填满后发生的情况，而长尾往往就在后面。样本数超过缓冲区容量的基准测试不报告任何百分位数，并说明有多少样本未能容纳。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST_BENCHMARK_PERCENTILES && CONFIG_ZTEST_BENCHMARK
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/testsuite/ztest/benchmark/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/benchmark/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → 基准测试选项（Benchmarking options） → Ztest 基准测试功能（Benchmarking features）［实验性，Experimental］ → 报告延迟百分位数（Latency percentiles）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST_BENCHMARK_PERCENTILES`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_BENCHMARK_PERCENTILES)、[`CONFIG_ZTEST_BENCHMARK`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_BENCHMARK)。

<a id="CONFIG_ZTEST_BENCHMARK_OUTLIERS"></a>

## 431.30 `CONFIG_ZTEST_BENCHMARK_OUTLIERS`

**提示（Prompt）**：用离群样本数量（Outlier count）替代标准误差

**说明（Help）**

将报告中的标准误差（Standard error）一行替换为明显高于中位数（Median）的样本数，以及该数量占总样本的百分比。超过中位数多少才计入，由 `CONFIG_ZTEST_BENCHMARK_OUTLIER_MARGIN_DIV` 决定。标准误差描述对同一随机总体均值估计的精确程度；延迟分布通常不同，它大部分执行命中一个基准耗时，少数执行受到其他活动打断。原文举例：一万个耗时 760 周期的样本加一个 1240 周期的样本，标准误差为 0.048，看起来是在精确描述一个从未实际出现过的平均执行时间；而 `1 / 10000 (0.010%)` 更直接表明发生了什么。仅修改面向人的报告，CSV 输出仍保留标准误差列。

译注：例子中的样本数与比例表达式均按原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST_BENCHMARK_PERCENTILES && CONFIG_ZTEST_BENCHMARK
```

**定义位置（Location）**：[`subsys/testsuite/ztest/benchmark/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/benchmark/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → 基准测试选项（Benchmarking options） → Ztest 基准测试功能（Benchmarking features）［实验性，Experimental］ → 报告延迟百分位数（Latency percentiles）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST_BENCHMARK_PERCENTILES`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_BENCHMARK_PERCENTILES)、[`CONFIG_ZTEST_BENCHMARK`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_BENCHMARK)。

<a id="CONFIG_ZTEST_BENCHMARK_OUTLIER_MARGIN_DIV"></a>

## 431.31 `CONFIG_ZTEST_BENCHMARK_OUTLIER_MARGIN_DIV`

**提示（Prompt）**：以除数表示的中位数上方离群裕量（Outlier margin divisor）

**说明（Help）**

指定样本必须高于中位数（Median）多少才算离群值（Outlier），以中位数的除数表示。默认 16 表示裕量为中位数的十六分之一，因此基准值为 400 时，从 426 起计为离群值。裕量至少为两个计数，避免粗粒度定时器产生的相邻计数波动被计入。若没有裕量，任何高于中位数的样本都算离群值；但基准耗时并非严格单值，计时器分辨率会使其分散在几个计数上。当计数器相对待测操作较粗时，整个分布甚至可能只有两个值，导致约半数样本高于中位数，即便没有受到干扰也被报告为离群值。原文最后建议：减小此值以统计更小的干扰；平台固有基准噪声较大时增大此值。

译注：末尾调参建议与前述“除数越大、裕量越小”的定义方向相反。译文保留两处内容，并明确指出这一原文矛盾。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST_BENCHMARK_OUTLIERS && CONFIG_ZTEST_BENCHMARK
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 1000]
```

**定义位置（Location）**：[`subsys/testsuite/ztest/benchmark/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/benchmark/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → 基准测试选项（Benchmarking options） → Ztest 基准测试功能（Benchmarking features）［实验性，Experimental］ → 报告延迟百分位数（Latency percentiles） → 用离群样本数量（Outlier count）替代标准误差

**配置项引用（Symbol References）**：[`CONFIG_ZTEST_BENCHMARK_OUTLIERS`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_BENCHMARK_OUTLIERS)、[`CONFIG_ZTEST_BENCHMARK`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_BENCHMARK)。

<a id="CONFIG_ZTEST_BENCHMARK_OUTPUT_CSV"></a>

## 431.32 `CONFIG_ZTEST_BENCHMARK_OUTPUT_CSV`

**提示（Prompt）**：以 CSV 格式输出基准测试结果（Benchmark results）

**说明（Help）**

将基准测试（Benchmark）结果输出为逗号分隔值（Comma-Separated Values，CSV），供机器解析。每行以一个字母标识记录类型（Record type），决定测试类型和列布局。

使用 `ZTEST_BENCHMARK()` 或 `ZTEST_BENCHMARK_SETUP_TEARDOWN()` 创建的采样基准测试（Sampled benchmark），输出如下原始格式；原文将字段列表折成两行：

```text
  S, suite, name, samples, total_cycles, mean, stddev, std_error, min, min_sample, max,
  max_sample
```

全部周期值都根据对照测量（Control measurement）进行了噪声校正。字段含义：

- `suite`：测试套件名称（Test suite name）。
- `name`：基准测试名称。
- `samples`：迭代次数。
- `total_cycles`：累计周期数。
- `mean`：每次迭代的平均周期数。
- `stddev`：标准差（Standard deviation）。
- `std_error`：均值标准误差（Standard error of the mean）。
- `min` / `max`：周期数的最小值和最大值。
- `min_sample` / `max_sample`：各极值出现时的迭代编号。

每个至少运行一次的基准测试，还输出一条 `C` 记录，表示首次执行的冷启动开销（Cold cost）；该次执行不计入分布：

```text
  C, suite, name, warmup, cold
```

- `warmup`：开始采样前执行的迭代次数。
- `cold`：首次执行的周期数，已进行噪声校正。

通过 `ZTEST_BENCHMARK_MANUAL()` 创建的手动采样测试（Manually sampled benchmark）输出 `M` 记录，列布局与 `S` 相同；其中 `samples` 为实际记录了测量区间的迭代数。未记录样本时改为输出 `M, suite, name, INCONCLUSIVE`。

通过 `ZTEST_BENCHMARK_TIMED()` 或 `ZTEST_BENCHMARK_TIMED_SETUP_TEARDOWN()` 创建的定时基准测试（Timed benchmark），输出：

```text
  T, suite, name, iterations, total_cycles, net_cycles, ops_per_sec, cycles_per_op
```

- `suite`：测试套件名称。
- `name`：基准测试名称。
- `iterations`：完成的运行次数。
- `total_cycles`：总周期数，含开销。
- `net_cycles`：扣除循环开销后的周期数。
- `ops_per_sec`：吞吐量（Throughput），即每秒操作次数。
- `cycles_per_op`：每次操作的平均周期开销。

如果测得的开销超过总时间，该行以 `INCONCLUSIVE` 替代数值结果，例如 `T, my_suite, my_benchmark, INCONCLUSIVE`。

启用 `CONFIG_ZTEST_BENCHMARK_PERCENTILES` 后，每个采样测试和手动采样测试额外输出：

```text
  P, suite, name, samples, min, p50, p90, p99, p999, p9999, max
```

- `samples`：用于计算百分位数的保留样本数量。
- `min` / `max`：周期数的最小值和最大值。
- `p50` 至 `p9999`：最近秩法百分位数（Nearest-rank percentiles），其中 `p9999` 为第 99.99 百分位数。

全部值都根据对照测量进行了噪声校正。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZTEST_BENCHMARK_OUTPUT_FORMAT>
```

**定义位置（Location）**：[`subsys/testsuite/ztest/benchmark/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/benchmark/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → 基准测试选项（Benchmarking options） → Ztest 基准测试功能（Benchmarking features）［实验性，Experimental］ → Ztest 基准测试输出格式（Benchmark output format）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST_BENCHMARK_OUTPUT_FORMAT`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_BENCHMARK_OUTPUT_FORMAT)。

<a id="CONFIG_ZTEST_BENCHMARK_OUTPUT_FORMAT"></a>

## 431.33 `CONFIG_ZTEST_BENCHMARK_OUTPUT_FORMAT`

**提示（Prompt）**：Ztest 基准测试输出格式（Benchmark output format）

**说明（Help）**

选择基准测试结果（Benchmark results）的输出格式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST_BENCHMARK
```

**默认值（Defaults）**

```text
CONFIG_ZTEST_BENCHMARK_OUTPUT_VERBOSE
```

**可选项（Choices）**

```text
CONFIG_ZTEST_BENCHMARK_OUTPUT_VERBOSE
CONFIG_ZTEST_BENCHMARK_OUTPUT_CSV
```

**定义位置（Location）**：[`subsys/testsuite/ztest/benchmark/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/benchmark/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → 基准测试选项（Benchmarking options） → Ztest 基准测试功能（Benchmarking features）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_ZTEST_BENCHMARK`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_BENCHMARK)、[`CONFIG_ZTEST_BENCHMARK_OUTPUT_VERBOSE`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_BENCHMARK_OUTPUT_VERBOSE)、[`CONFIG_ZTEST_BENCHMARK_OUTPUT_CSV`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_BENCHMARK_OUTPUT_CSV)。

<a id="CONFIG_ZTEST_BENCHMARK_OUTPUT_VERBOSE"></a>

## 431.34 `CONFIG_ZTEST_BENCHMARK_OUTPUT_VERBOSE`

**提示（Prompt）**：输出详细基准测试结果（Verbose benchmark results）

**说明（Help）**

采用面向人阅读的输出格式，包含单位和说明。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZTEST_BENCHMARK_OUTPUT_FORMAT>
```

**定义位置（Location）**：[`subsys/testsuite/ztest/benchmark/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/benchmark/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → 基准测试选项（Benchmarking options） → Ztest 基准测试功能（Benchmarking features）［实验性，Experimental］ → Ztest 基准测试输出格式（Benchmark output format）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST_BENCHMARK_OUTPUT_FORMAT`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_BENCHMARK_OUTPUT_FORMAT)。

<a id="CONFIG_ZTEST_BENCHMARK_PERCENTILES"></a>

## 431.35 `CONFIG_ZTEST_BENCHMARK_PERCENTILES`

**提示（Prompt）**：报告延迟百分位数（Latency percentiles）

**说明（Help）**

保留各基准测试的独立样本，在常规统计之外报告最小值、p50、p90、p99、p99.9、p99.99 和最大值。均值与标准误差（Standard error）描述平均值估计的精确度，适合考察吞吐量，却不足以描述延迟：实时系统关注单次操作可能有多差，而这体现在分布尾部（Tail）。百分位数（Percentile）还为 `CONFIG_ZTEST_BENCHMARK_OUTLIERS` 提供明显高于中位数的样本计数。要分辨百分位数，必须有足够样本：p99 至少需要 100 个，p99.9 至少 1000 个，p99.99 至少 10000 个；低于这些数量时，报告值退化为最大值。保留每个样本占用 8 字节，因此应按基准测试运行的迭代次数配置缓冲区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST_BENCHMARK
```

**定义位置（Location）**：[`subsys/testsuite/ztest/benchmark/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/benchmark/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → 基准测试选项（Benchmarking options） → Ztest 基准测试功能（Benchmarking features）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_ZTEST_BENCHMARK`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_BENCHMARK)。

<a id="CONFIG_ZTEST_BENCHMARK_WARMUP"></a>

## 431.36 `CONFIG_ZTEST_BENCHMARK_WARMUP`

**提示（Prompt）**：开始采样前执行的迭代次数（Warmup iterations）

**说明（Help）**

每个基准测试开始记录前，完整执行的迭代次数，不计入报告的分布。无论此值如何设置，第一次执行始终属于预运行：缓存、分支预测器和地址转换后备缓冲器（TLB）均处于冷状态，可能比稳态慢一个数量级，因此单独报告为冷启动开销（Cold cost），不混入样本。若同时将其计入分布，一次冷启动就可能决定高百分位数，因为 10000 个样本下，最近秩法的 p99.99 是第二大的值。因此，默认值 0 表示除首次执行外不再排除额外迭代；首次执行实际是另行报告，并非丢弃。对于全部开销接近一次缓存未命中（Cache miss）的微基准测试，增加预运行会影响测量准确性。因此，仅当关注稳态，且测试足够大、缓存状态确实重要时才应增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST_BENCHMARK
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/testsuite/ztest/benchmark/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/benchmark/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → 基准测试选项（Benchmarking options） → Ztest 基准测试功能（Benchmarking features）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_ZTEST_BENCHMARK`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_BENCHMARK)。

<a id="CONFIG_ZTEST_COVERAGE_PER_TEST"></a>

## 431.37 `CONFIG_ZTEST_COVERAGE_PER_TEST`

**提示（Prompt）**：按独立测试用例转储代码覆盖率数据（Per-test coverage data）

**说明（Help）**

每个测试前重置 gcov 计数器，测试后分别转储带测试标签（Test tag）的覆盖率产物，从而建立测试到源代码的覆盖率矩阵（Coverage matrix）。转储采用已配置的控制台或半主机（Semihosting）传输方式；半主机模式下，各产物写入宿主机的 `<gcda-path>@@<suite>.<test>`，避免各测试的转储相互覆盖。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COVERAGE_GCOV && CONFIG_ZTEST
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L147)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_COVERAGE_GCOV`](P431_subsys_testsuite_配置项参考.md#CONFIG_COVERAGE_GCOV)、[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_COVERAGE_PER_TEST_TAG_SIZE"></a>

## 431.38 `CONFIG_ZTEST_COVERAGE_PER_TEST_TAG_SIZE`

**提示（Prompt）**：每测试覆盖率标签（Per-test coverage tag）的最大长度

**说明（Help）**

用于组合传给覆盖率转储的 `<suite>.<test>` 标签的栈缓冲区大小。测试套件和测试名称组合后的长度，包括末尾 NUL，超过此值时会被截断。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST_COVERAGE_PER_TEST && CONFIG_ZTEST
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework） → 按独立测试用例转储代码覆盖率数据（Per-test coverage data）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST_COVERAGE_PER_TEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_COVERAGE_PER_TEST)、[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_COVERAGE_RESET_BEFORE_TESTS"></a>

## 431.39 `CONFIG_ZTEST_COVERAGE_RESET_BEFORE_TESTS`

**提示（Prompt）**：重置覆盖率计数器（Coverage counters）

**说明（Help）**

运行测试前重置 gcov 计数器，确保覆盖率报告只统计测试本身触发的代码行，不计入开发板初始化和测试前引导代码。例如，待测代码在启动期间也会执行时，此功能很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COVERAGE_GCOV && CONFIG_ZTEST
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_COVERAGE_GCOV`](P431_subsys_testsuite_配置项参考.md#CONFIG_COVERAGE_GCOV)、[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_CPU_HOLD_TIME_MS"></a>

## 431.40 `CONFIG_ZTEST_CPU_HOLD_TIME_MS`

**提示（Prompt）**：单 CPU 类型测试期间保持其他 CPU 的最长时间（毫秒）

**说明（Help）**

指定单 CPU（1cpu）类型测试在多 CPU 系统中执行的最长时间，单位为毫秒。默认值应足够大多数此类测试使用；较慢的平台，包括部分模拟器，可能需要更大值。请注意，为长时间运行的测试增大此值可能使持续集成（CI）系统负载过重，应谨慎修改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_FAIL_FAST"></a>

## 431.41 `CONFIG_ZTEST_FAIL_FAST`

**提示（Prompt）**：首个测试失败后中止（Abort）

**说明（Help）**

遇到首个失败测试即停止并中止，不再执行队列中可能剩余的测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_FAIL_ON_ASSUME"></a>

## 431.42 `CONFIG_ZTEST_FAIL_ON_ASSUME`

**提示（Prompt）**：假设失败时将测试运行判为失败（Assumption failure）

**说明（Help）**

启用后，只要有假设（Assumption）失败，测试二进制最终结果就判为失败。即使失败的 `zassume` 调用仍将对应测试标为跳过（Skipped），最终结果也显示失败，以提高可见性。通过 `ZTEST_EXPECT_SKIP` 注解预期跳过的测试不在此列。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:213`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L213)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_FATAL_HOOK"></a>

## 431.43 `CONFIG_ZTEST_FATAL_HOOK`

**提示（Prompt）**：使用预定义致命错误处理程序与钩子函数（Fatal handler and hook）

**说明（Help）**

使用预定义的通用致命错误处理程序（Fatal error handler）和后置钩子（Post hook）执行测试用例所需动作，常用于错误场景测试。通过 Twister 运行测试时，记得在 YAML 文件中添加 `ignore_fault` 标签。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_MOCKING"></a>

## 431.44 `CONFIG_ZTEST_MOCKING`

**提示（Prompt）**：模拟支持函数（Mocking support functions）

**说明（Help）**

启用 Ztest 的模拟（Mocking）支持，让测试能够为函数设置返回值和预期参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:228`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L228)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing）

<a id="CONFIG_ZTEST_NO_YIELD"></a>

## 431.45 `CONFIG_ZTEST_NO_YIELD`

**提示（Prompt）**：测试完成后不让出执行权给空闲线程（Idle thread）

**说明（Help）**

测试完成后，不让出执行权给空闲线程（Idle thread），而是在循环中自旋（Spin）。适用于低功耗模式测试，因为空闲线程可能使开发板进入调试器无法连接的低功耗状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**默认值（Defaults）**

```text
n if CONFIG_COVERAGE_DUMP || CONFIG_COVERAGE_SEMIHOST
y if CONFIG_PM || CONFIG_PM_DEVICE || CONFIG_PM_DEVICE_RUNTIME
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)、[`CONFIG_COVERAGE_DUMP`](P431_subsys_testsuite_配置项参考.md#CONFIG_COVERAGE_DUMP)、[`CONFIG_COVERAGE_SEMIHOST`](P431_subsys_testsuite_配置项参考.md#CONFIG_COVERAGE_SEMIHOST)、[`CONFIG_PM`](P411_subsys_pm_配置项参考.md#CONFIG_PM)、[`CONFIG_PM_DEVICE`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE)、[`CONFIG_PM_DEVICE_RUNTIME`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME)。

<a id="CONFIG_ZTEST_PARAMETER_COUNT"></a>

## 431.46 `CONFIG_ZTEST_PARAMETER_COUNT`

**提示（Prompt）**：为参数或返回值（Parameter/return value）预留的数量

**说明（Help）**

可同时存在的返回值（Return value）或预期参数（Expected parameter）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST_MOCKING
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:234`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L234)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → 模拟支持函数（Mocking support functions）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST_MOCKING`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_MOCKING)。

<a id="CONFIG_ZTEST_REPEAT"></a>

## 431.47 `CONFIG_ZTEST_REPEAT`

**提示（Prompt）**：重复执行测试与测试套件（Test suite）

**说明（Help）**

此规则重复执行测试和测试套件（Test suite）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_RETEST_IF_PASSED"></a>

## 431.48 `CONFIG_ZTEST_RETEST_IF_PASSED`

**提示（Prompt）**：测试通过后重置开发板以再次测试

**说明（Help）**

测试通过后重置开发板，再次运行测试。尝试复现间歇性失败（Intermittent failure）时，可用此方式替代手动复位。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**主动选择（Selects）**

```text
CONFIG_REBOOT
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)、[`CONFIG_REBOOT`](P198_lib_配置项参考_2.md#CONFIG_REBOOT)。

<a id="CONFIG_ZTEST_RULE_1CPU"></a>

## 431.49 `CONFIG_ZTEST_RULE_1CPU`

**提示（Prompt）**：在单个 CPU 上运行全部测试

**说明（Help）**

此规则在每个单元测试前调用 `z_test_1cpu_start`，测试后调用 `ztest_1cpu_stop`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework） → Ztest 提供的规则（Rules）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_SHELL"></a>

## 431.50 `CONFIG_ZTEST_SHELL`

**提示（Prompt）**：带命令行支持的 Ztest（Shell support）

**说明（Help）**

启用命令行（Shell）来管理测试执行和测试选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**主动选择（Selects）**

```text
CONFIG_SHELL
CONFIG_SHELL_THREAD_PRIORITY_OVERRIDE
CONFIG_GETOPT_LONG
CONFIG_SHELL_GETOPT
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_THREAD_PRIORITY_OVERRIDE`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_THREAD_PRIORITY_OVERRIDE)、[`CONFIG_GETOPT_LONG`](P197_lib_配置项参考_1.md#CONFIG_GETOPT_LONG)、[`CONFIG_SHELL_GETOPT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_GETOPT)。

<a id="CONFIG_ZTEST_SHUFFLE"></a>

## 431.51 `CONFIG_ZTEST_SHUFFLE`

**提示（Prompt）**：打乱测试与测试套件的顺序（Shuffle order）

**说明（Help）**

此规则打乱测试和测试套件（Test suite）的执行顺序。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**主动选择（Selects）**

```text
CONFIG_TEST_RANDOM_GENERATOR if !CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)、[`CONFIG_TEST_RANDOM_GENERATOR`](P417_subsys_random_配置项参考.md#CONFIG_TEST_RANDOM_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ZTEST_STACK_SIZE"></a>

## 431.52 `CONFIG_ZTEST_STACK_SIZE`

**提示（Prompt）**：测试函数线程栈大小（Thread stack size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**默认值（Defaults）**

```text
2048 if CONFIG_COVERAGE_GCOV
2048 if CONFIG_X86
1024
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)、[`CONFIG_COVERAGE_GCOV`](P431_subsys_testsuite_配置项参考.md#CONFIG_COVERAGE_GCOV)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_ZTEST_SUITE_REPEAT_COUNT"></a>

## 431.53 `CONFIG_ZTEST_SUITE_REPEAT_COUNT`

**提示（Prompt）**：测试套件运行的迭代次数（Iterations）

**说明（Help）**

此规则执行一个测试套件（Test suite）N 次。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST_REPEAT && CONFIG_ZTEST
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework） → 重复执行测试与测试套件（Test suite）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST_REPEAT`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_REPEAT)、[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_SUMMARY"></a>

## 431.54 `CONFIG_ZTEST_SUMMARY`

**提示（Prompt）**：显示测试摘要（Test summary）

**说明（Help）**

控制是否输出测试摘要（Test summary）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_TC_UTIL_USER_OVERRIDE"></a>

## 431.55 `CONFIG_ZTEST_TC_UTIL_USER_OVERRIDE`

**提示（Prompt）**：覆盖 `tc_util.h`

**说明（Help）**

允许覆盖 `tc_util.h` 中的定义。启用后，用户应在 Zephyr 包含路径（Include path）中提供 `tc_util_user_override.h`，例如在项目的 `CMakeLists.txt` 中添加 `zephyr_include_directories(project PRIVATE my_folder)`。该覆盖头文件可使用 `#define` 定义 `tc_util.h` 中由 `#ifndef ... #endif` 包围的各个宏和字符串。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_TEST_DELAY_MS"></a>

## 431.56 `CONFIG_ZTEST_TEST_DELAY_MS`

**提示（Prompt）**：测试之间的延迟（Delay，毫秒）

**说明（Help）**

对于无法处理快速控制台输出的系统，在测试之间添加延迟，以控制输出速率。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_TEST_REPEAT_COUNT"></a>

## 431.57 `CONFIG_ZTEST_TEST_REPEAT_COUNT`

**提示（Prompt）**：测试运行的迭代次数（Iterations）

**说明（Help）**

此规则执行一个测试（Test）N 次。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST_REPEAT && CONFIG_ZTEST
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework） → 重复执行测试与测试套件（Test suite）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST_REPEAT`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST_REPEAT)、[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_THREAD_PRIORITY"></a>

## 431.58 `CONFIG_ZTEST_THREAD_PRIORITY`

**提示（Prompt）**：测试线程优先级（Testing thread priority）

**说明（Help）**

设置测试线程优先级，默认值为 -1，即协作式（Cooperative）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**默认值（Defaults）**

```text
-2 if !CONFIG_PREEMPT_ENABLED
-1
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)、[`CONFIG_PREEMPT_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PREEMPT_ENABLED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PREEMPT_ENABLED`。

<a id="CONFIG_ZTEST_VERBOSE_OUTPUT"></a>

## 431.59 `CONFIG_ZTEST_VERBOSE_OUTPUT`

**提示（Prompt）**：详细测试输出（Verbose test output）

**说明（Help）**

控制详细显示测试输出，还是完全不输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:199`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L199)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_VERBOSE_SUMMARY"></a>

## 431.60 `CONFIG_ZTEST_VERBOSE_SUMMARY`

**提示（Prompt）**：详细测试摘要（Verbose test summary）

**说明（Help）**

控制测试套件摘要（Suite summary）以详细形式显示，还是仅显示一行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L206)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_VERIFY_RUN_ALL"></a>

## 431.61 `CONFIG_ZTEST_VERIFY_RUN_ALL`

**提示（Prompt）**：验证全部已定义测试均已运行

**说明（Help）**

如果并非全部测试都已运行，此规则将项目结果判为失败。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)。

<a id="CONFIG_ZTEST_WARN_NO_OPTIMIZATIONS"></a>

## 431.62 `CONFIG_ZTEST_WARN_NO_OPTIMIZATIONS`

**提示（Prompt）**：使用 `CONFIG_NO_OPTIMIZATIONS` 运行测试时发出警告

**说明（Help）**

在不启用编译器优化（Compiler optimization）的情况下构建 Ztest 时，打印 CMake 警告。若测试未专门调整以适应此配置，请不要针对在该配置下运行的结果提交问题报告。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NO_OPTIMIZATIONS && CONFIG_ZTEST
```

**默认值（Defaults）**

```text
y if !(CONFIG_ARCH_POSIX || CONFIG_COVERAGE)
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → Zephyr 测试框架（Testing framework）

**配置项引用（Symbol References）**：[`CONFIG_NO_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NO_OPTIMIZATIONS)、[`CONFIG_ZTEST`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTEST)、[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_COVERAGE`](P431_subsys_testsuite_配置项参考.md#CONFIG_COVERAGE)。

<a id="CONFIG_ZTRESS"></a>

## 431.63 `CONFIG_ZTRESS`

**提示（Prompt）**：压力测试框架（Stress test framework）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_USERSPACE
```

**主动选择（Selects）**

```text
CONFIG_THREAD_RUNTIME_STATS
CONFIG_THREAD_MONITOR
CONFIG_TEST_RANDOM_GENERATOR if !CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:241`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L241)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_THREAD_RUNTIME_STATS`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_RUNTIME_STATS)、[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_TEST_RANDOM_GENERATOR`](P417_subsys_random_配置项参考.md#CONFIG_TEST_RANDOM_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ZTRESS_MAX_THREADS"></a>

## 431.64 `CONFIG_ZTRESS_MAX_THREADS`

**提示（Prompt）**：Ztress 框架的最大线程数（Maximum threads）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTRESS
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:250`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L250)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → 压力测试框架（Stress test framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTRESS`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTRESS)。

<a id="CONFIG_ZTRESS_REPORT_PROGRESS_MS"></a>

## 431.65 `CONFIG_ZTRESS_REPORT_PROGRESS_MS`

**提示（Prompt）**：进度报告间隔（Progress report interval，毫秒）

**说明（Help）**

设为 0 可禁用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTRESS
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:260`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L260)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → 压力测试框架（Stress test framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTRESS`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTRESS)。

<a id="CONFIG_ZTRESS_STACK_SIZE"></a>

## 431.66 `CONFIG_ZTRESS_STACK_SIZE`

**提示（Prompt）**：Ztress 线程栈大小（Thread stack size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTRESS
```

**默认值（Defaults）**

```text
4096 if CONFIG_NO_OPTIMIZATIONS
2048
```

**定义位置（Location）**：[`subsys/testsuite/ztest/Kconfig:255`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/ztest/Kconfig#L255)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 测试（Testing） → 压力测试框架（Stress test framework）

**配置项引用（Symbol References）**：[`CONFIG_ZTRESS`](P431_subsys_testsuite_配置项参考.md#CONFIG_ZTRESS)、[`CONFIG_NO_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NO_OPTIMIZATIONS)。

<!-- kconfig-navigation -->

[上一章](P430_subsys_task_wdt_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P432_subsys_timing_配置项参考.md)
