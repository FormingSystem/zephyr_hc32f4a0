---
id: learning.zephyr-docs.kconfig-reference.page-33
title: "`arch/posix`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第33章\_`arch/posix`配置项参考

本章翻译官方 Kconfig 数据库中 `arch/posix` 的 6 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ARCH_POSIX_LIBFUZZER"></a>

## 33.1 `CONFIG_ARCH_POSIX_LIBFUZZER`

**提示（Prompt）**：构建模糊测试目标（Fuzz Test Target）

**说明（Help）**

构建为 LLVM libFuzzer 目标（Target）。这需要工具链（Toolchain）支持：目前只有 Clang 可用，且仅支持 `native_sim[//64]`。通常应配合 `CONFIG_ASAN`、`UBSAN`、`MSAN` 中的一部分进行验证。应用必须实现入口点（Entry Point）`LLVMFuzzerTestOneInput()`；该入口在操作系统“外部”的主机环境（Host Environment）中运行。更多信息请参阅 Zephyr 文档、示例以及 [LLVM libFuzzer 官方文档](https://llvm.org/docs/LibFuzzer.html) 。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX
```

**定义位置（Location）**：[`arch/posix/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/posix/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 原生（POSIX）架构选项（Native Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)。

<a id="CONFIG_ARCH_POSIX_RECOMMENDED_STACK_SIZE"></a>

## 33.2 `CONFIG_ARCH_POSIX_RECOMMENDED_STACK_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

仅面向 POSIX 架构的 Zephyr 线程栈大小（Thread Stack Size），单位为字节。在此架构中，只有一部分线程状态保存在 Zephyr 线程栈中，实际的栈是底层原生 pthread 栈，因此分配的 Zephyr 栈可限制为此大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX
```

**默认值（Defaults）**

```text
60 if CONFIG_64BIT && CONFIG_ARCH_POSIX_UPDATE_STACK_INFO && CONFIG_STACK_SENTINEL
56 if CONFIG_64BIT && CONFIG_ARCH_POSIX_UPDATE_STACK_INFO
44 if CONFIG_64BIT && CONFIG_STACK_SENTINEL
40 if CONFIG_64BIT
36 if CONFIG_ARCH_POSIX_UPDATE_STACK_INFO && CONFIG_STACK_SENTINEL
32 if CONFIG_ARCH_POSIX_UPDATE_STACK_INFO
28 if CONFIG_STACK_SENTINEL
24
```

**定义位置（Location）**：[`arch/posix/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/posix/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 原生（POSIX）架构选项（Native Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)、[`CONFIG_ARCH_POSIX_UPDATE_STACK_INFO`](P033_arch_posix_配置项参考.md#CONFIG_ARCH_POSIX_UPDATE_STACK_INFO)、[`CONFIG_STACK_SENTINEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STACK_SENTINEL)。

<a id="CONFIG_ARCH_POSIX_TRAP_ON_FATAL"></a>

## 33.3 `CONFIG_ARCH_POSIX_TRAP_ON_FATAL`

**提示（Prompt）**：发生致命错误时触发 SIGTRAP（Fatal Error）

**说明（Help）**

发生致命错误（Fatal Error）时，在退出前触发 `SIGTRAP` 信号。如果已连接调试器（Debugger），这会自动暂停目标。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX
```

**定义位置（Location）**：[`arch/posix/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/posix/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 原生（POSIX）架构选项（Native Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)。

<a id="CONFIG_ARCH_POSIX_UPDATE_STACK_INFO"></a>

## 33.4 `CONFIG_ARCH_POSIX_UPDATE_STACK_INFO`

**提示（Prompt）**：使用实际 pthread 栈边界更新线程栈信息（Thread Stack Information）

**说明（Help）**

启用后，POSIX 架构会更新各线程的 `stack_info`，使其反映实际 pthread 栈，而不是 Zephyr 分配的栈。对于根据实际栈边界（Stack Bounds）自行检查栈溢出（Stack Overflow）的应用，这很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_STACK_INFO && CONFIG_ARCH_POSIX
```

**定义位置（Location）**：[`arch/posix/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/posix/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 原生（POSIX）架构选项（Native Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)。

<a id="CONFIG_NATIVE_USE_NSI_ERRNO"></a>

## 33.5 `CONFIG_NATIVE_USE_NSI_ERRNO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将原生模拟器（Native Simulator）的 `nsi_errno` 组件与 Zephyr 嵌入式代码一起构建。此组件允许在嵌入式 C 库（Embedded libc）与主机 C 库（Host libc）之间双向转换 `errno` 值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX
```

**被选择（Selected by）**

```text
CONFIG_AUDIO_DMIC_NATIVE_SIM
CONFIG_BT_USERCHAN
CONFIG_I2S_NATIVE_SIM
CONFIG_NATIVE_LINUX_LEDS
CONFIG_NET_NATIVE_OFFLOADED_SOCKETS
CONFIG_PTP_CLOCK_NATIVE
CONFIG_UART_NATIVE_TTY
CONFIG_VIDEO_NATIVE_SIM_FIFO
CONFIG_FUSE_FS_ACCESS
CONFIG_FILE_SYSTEM_NATIVE_MOUNT
```

**定义位置（Location）**：[`arch/posix/Kconfig.natsim_optional:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/posix/Kconfig.natsim_optional#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 原生（POSIX）架构选项（Native Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_AUDIO_DMIC_NATIVE_SIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AUDIO_DMIC_NATIVE_SIM)、[`CONFIG_BT_USERCHAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_USERCHAN)、[`CONFIG_I2S_NATIVE_SIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_NATIVE_SIM)、[`CONFIG_NATIVE_LINUX_LEDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NATIVE_LINUX_LEDS)、[`CONFIG_NET_NATIVE_OFFLOADED_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_OFFLOADED_SOCKETS)、[`CONFIG_PTP_CLOCK_NATIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_CLOCK_NATIVE)、[`CONFIG_UART_NATIVE_TTY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NATIVE_TTY)、[`CONFIG_VIDEO_NATIVE_SIM_FIFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_NATIVE_SIM_FIFO)、[`CONFIG_FUSE_FS_ACCESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FUSE_FS_ACCESS)、[`CONFIG_FILE_SYSTEM_NATIVE_MOUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FILE_SYSTEM_NATIVE_MOUNT)。

<a id="CONFIG_NATIVE_USE_NSI_FCNTL"></a>

## 33.6 `CONFIG_NATIVE_USE_NSI_FCNTL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将原生模拟器（Native Simulator）的 `nsi_fcntl` 组件与 Zephyr 嵌入式代码一起构建。此组件允许在嵌入式代码与主机 C 库（Host libc）之间双向转换 Zephyr ZVFS 中类似 `fcntl` 的标志，例如 `zvfs_open()` 的标志。

当 Zephyr 启用 POSIX 兼容层（Compatibility Layer）时，嵌入式 `fcntl.h` 中的常量与 Zephyr 虚拟文件系统（VFS）中的对应常量一致，因此也可以通过此组件转换。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX
```

**被选择（Selected by）**

```text
CONFIG_NET_NATIVE_OFFLOADED_SOCKETS
CONFIG_FILE_SYSTEM_NATIVE_MOUNT
```

**定义位置（Location）**：[`arch/posix/Kconfig.natsim_optional:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/posix/Kconfig.natsim_optional#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 原生（POSIX）架构选项（Native Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_NET_NATIVE_OFFLOADED_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_OFFLOADED_SOCKETS)、[`CONFIG_FILE_SYSTEM_NATIVE_MOUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FILE_SYSTEM_NATIVE_MOUNT)。

<!-- kconfig-navigation -->

[上一章](P032_arch_common_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P034_arch_riscv_配置项参考_1.md)
