---
id: learning.zephyr-docs.kconfig-reference.page-418
title: "`subsys/retention`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第418章\_`subsys/retention`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/retention` 的 10 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_RETENTION"></a>

## 418.1 `CONFIG_RETENTION`

**提示（Prompt）**：保留存储支持（Retention support）

**说明（Help）**

启用保留系统（Retention system）支持，使用保留内存驱动（Retained memory driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RETAINED_MEM && DT_HAS_ZEPHYR_RETENTION_ENABLED
```

**被选择（Selected by）**

```text
CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER
```

**弱选择（Implies）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`subsys/retention/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/retention/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM)、[`CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_RETENTION_BOOTLOADER_INFO"></a>

## 418.2 `CONFIG_RETENTION_BOOTLOADER_INFO`

**提示（Prompt）**：引导加载程序信息（Bootloader info）

**说明（Help）**

添加引导加载程序信息共享系统（Bootloader information sharing system），在启用数据共享时，可从引导加载程序获取数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RETENTION
```

**定义位置（Location）**：[`subsys/retention/Kconfig.blinfo:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/retention/Kconfig.blinfo#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support） → 保留模块（Retention modules）

**配置项引用（Symbol References）**：[`CONFIG_RETENTION`](P418_subsys_retention_配置项参考.md#CONFIG_RETENTION)。

<a id="CONFIG_RETENTION_BOOTLOADER_INFO_INIT_PRIORITY"></a>

## 418.3 `CONFIG_RETENTION_BOOTLOADER_INFO_INIT_PRIORITY`

**提示（Prompt）**：引导加载程序信息初始化优先级（Bootloader info init priority）

**说明（Help）**

引导加载程序信息（Bootloader info）的初始化优先级，原文要求高于保留子系统（Retention subsystem）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RETENTION_BOOTLOADER_INFO && CONFIG_RETENTION
```

**默认值（Defaults）**

```text
87
```

**定义位置（Location）**：[`subsys/retention/Kconfig.blinfo:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/retention/Kconfig.blinfo#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support） → 保留模块（Retention modules） → 引导加载程序信息（Bootloader info）

**配置项引用（Symbol References）**：[`CONFIG_RETENTION_BOOTLOADER_INFO`](P418_subsys_retention_配置项参考.md#CONFIG_RETENTION_BOOTLOADER_INFO)、[`CONFIG_RETENTION`](P418_subsys_retention_配置项参考.md#CONFIG_RETENTION)。

<a id="CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_FUNCTION"></a>

## 418.4 `CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_FUNCTION`

**提示（Prompt）**：函数（Function）

**说明（Help）**

允许通过调用函数获取引导加载程序（Bootloader）设置；该函数使用请求的数据更新缓冲区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RETENTION_BOOTLOADER_INFO && CONFIG_RETENTION
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/retention/Kconfig.blinfo:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/retention/Kconfig.blinfo#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support） → 保留模块（Retention modules） → 引导加载程序信息（Bootloader info）

**配置项引用（Symbol References）**：[`CONFIG_RETENTION_BOOTLOADER_INFO`](P418_subsys_retention_配置项参考.md#CONFIG_RETENTION_BOOTLOADER_INFO)、[`CONFIG_RETENTION`](P418_subsys_retention_配置项参考.md#CONFIG_RETENTION)。

<a id="CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_SETTINGS"></a>

## 418.5 `CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_SETTINGS`

**提示（Prompt）**：设置（Settings）。

**说明（Help）**

允许通过前缀为 `blinfo` 的设置项（Settings）获取引导加载程序（Bootloader）设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS && CONFIG_RETENTION_BOOTLOADER_INFO && CONFIG_RETENTION
```

**定义位置（Location）**：[`subsys/retention/Kconfig.blinfo:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/retention/Kconfig.blinfo#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support） → 保留模块（Retention modules） → 引导加载程序信息（Bootloader info）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)、[`CONFIG_RETENTION_BOOTLOADER_INFO`](P418_subsys_retention_配置项参考.md#CONFIG_RETENTION_BOOTLOADER_INFO)、[`CONFIG_RETENTION`](P418_subsys_retention_配置项参考.md#CONFIG_RETENTION)。

<a id="CONFIG_RETENTION_BOOTLOADER_INFO_TYPE_MCUBOOT"></a>

## 418.6 `CONFIG_RETENTION_BOOTLOADER_INFO_TYPE_MCUBOOT`

**提示（Prompt）**：MCUboot 引导加载程序（MCUboot bootloader）

**说明（Help）**

为 MCUboot 与应用添加引导信息共享系统，使应用能够读取 MCUboot 配置及当前运行映像（Image）的配置。例如，应用可据此了解如何处理固件更新，以及应将固件放入哪个槽位（Slot）。使用时必须创建保留区（Retention area），并在设备树中将其设置为 `zephyr,bootloader-info` chosen 节点；MCUboot 构建时必须使用同一个 `zephyr,bootloader-info` DTS 节点，并启用 `CONFIG_BOOT_SHARE_DATA`、`CONFIG_BOOT_SHARE_DATA_BOOTINFO` 和 `CONFIG_BOOT_SHARE_BACKEND_RETENTION`，否则无法访问共享信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_MCUBOOT_BOOTUTIL_LIB
```

**定义位置（Location）**：[`subsys/retention/Kconfig.blinfo:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/retention/Kconfig.blinfo#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support） → 保留模块（Retention modules） → 引导加载程序信息（Bootloader info）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTUTIL_LIB`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTUTIL_LIB)。

<a id="CONFIG_RETENTION_BOOT_MODE"></a>

## 418.7 `CONFIG_RETENTION_BOOT_MODE`

**提示（Prompt）**：启动模式（Boot mode）

**说明（Help）**

添加启动模式（Boot mode）系统，根据启动模式参数的值改变执行流程。例如，可从应用进入引导加载程序（Bootloader）的串口恢复模式，而无需按键。使用时必须创建至少包含 1 个可供用户使用字节的保留区（Retention area），并在设备树中将其设置为 `zephyr,boot-mode` chosen 节点。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RETENTION
```

**定义位置（Location）**：[`subsys/retention/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/retention/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support） → 保留模块（Retention modules）

**配置项引用（Symbol References）**：[`CONFIG_RETENTION`](P418_subsys_retention_配置项参考.md#CONFIG_RETENTION)。

<a id="CONFIG_RETENTION_BUFFER_SIZE"></a>

## 418.8 `CONFIG_RETENTION_BUFFER_SIZE`

**提示（Prompt）**：保留系统栈缓冲区大小（Retention stack buffer size）

**说明（Help）**

从保留设备（Retention device）读取数据或向其写入数据时，使用的基于栈的缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RETENTION
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 4096]
```

**定义位置（Location）**：[`subsys/retention/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/retention/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support）

**配置项引用（Symbol References）**：[`CONFIG_RETENTION`](P418_subsys_retention_配置项参考.md#CONFIG_RETENTION)。

<a id="CONFIG_RETENTION_INIT_PRIORITY"></a>

## 418.9 `CONFIG_RETENTION_INIT_PRIORITY`

**提示（Prompt）**：保留设备初始化优先级（Retention device init priority）

**说明（Help）**

保留设备（Retention device）的初始化优先级，原文要求高于保留内存驱动（Retained memory driver）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RETENTION
```

**默认值（Defaults）**

```text
86
```

**定义位置（Location）**：[`subsys/retention/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/retention/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support）

**配置项引用（Symbol References）**：[`CONFIG_RETENTION`](P418_subsys_retention_配置项参考.md#CONFIG_RETENTION)。

<a id="CONFIG_RETENTION_MUTEX_FORCE_DISABLE"></a>

## 418.10 `CONFIG_RETENTION_MUTEX_FORCE_DISABLE`

**提示（Prompt）**：禁用保留系统的互斥锁（Retention mutex）支持

**说明（Help）**

禁用用于避免并发访问保留设备（Retention device）问题的互斥锁（Mutex）。仅在中断服务程序（ISR）中需要访问保留设备，或其他特殊场景下才应启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && CONFIG_RETENTION
```

**被选择（Selected by）**

```text
CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER
```

**定义位置（Location）**：[`subsys/retention/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/retention/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_RETENTION`](P418_subsys_retention_配置项参考.md#CONFIG_RETENTION)、[`CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER)。

<!-- kconfig-navigation -->

[上一章](P417_subsys_random_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P419_subsys_rtio_配置项参考.md)
