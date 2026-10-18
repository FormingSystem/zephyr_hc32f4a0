---
id: learning.zephyr-docs.kconfig-reference.page-196
title: "`drivers/xen`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第196章\_`drivers/xen`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/xen` 的 9 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NR_GRANT_FRAMES"></a>

## 196.1 `CONFIG_NR_GRANT_FRAMES`

**提示（Prompt）**：映射到 Zephyr 的授权帧数量（grant frames）

**说明（Help）**

配置 Zephyr 授权表驱动（grant table driver）在运行时支持的授权帧（grant frames）数量。此值应小于或等于 Xen 虚拟机监控器（hypervisor）为相应域（domain）配置的 `max_grant_frames`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN_GRANT_TABLE && CONFIG_XEN
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/xen/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/xen/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Xen 驱动 → Xen 授权表驱动（grant table driver）

**配置项引用（Symbol References）**：[`CONFIG_XEN_GRANT_TABLE`](P196_drivers_xen_配置项参考.md#CONFIG_XEN_GRANT_TABLE)、[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)。

<a id="CONFIG_XEN_DMOP"></a>

## 196.2 `CONFIG_XEN_DMOP`

**提示（Prompt）**：Xen dmop 超级调用包装函数（hypercall wrappers）

**说明（Help）**

启用 Xen 设备后端（device backends）所使用的 Xen `dm_op` 超级调用（hypercalls）的轻量包装函数。禁用后，从构建中移除 `dmop.c`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**定义位置（Location）**：[`drivers/xen/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/xen/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Xen 驱动

**配置项引用（Symbol References）**：[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)。

<a id="CONFIG_XEN_EVENTS"></a>

## 196.3 `CONFIG_XEN_EVENTS`

**提示（Prompt）**：Xen 事件驱动（events driver）

**说明（Help）**

Xen 事件通道驱动（event channels driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_UART_XEN_HVC
```

**定义位置（Location）**：[`drivers/xen/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/xen/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Xen 驱动

**配置项引用（Symbol References）**：[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)、[`CONFIG_UART_XEN_HVC`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_XEN_HVC)。

<a id="CONFIG_XEN_FDT"></a>

## 196.4 `CONFIG_XEN_FDT`

**提示（Prompt）**：Xen 启动扁平设备树（boot FDT）支持

**说明（Help）**

在早期启动（early boot）期间，将第一个固件参数提供的 Xen 启动设备树二进制块（boot device tree blob）复制到 Zephyr 自有内存中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BOARD_XENVM && CONFIG_XEN
```

**主动选择（Selects）**

```text
CONFIG_BOOT_FDT
CONFIG_FWARGS_HANDLER_HOOK
```

**定义位置（Location）**：[`drivers/xen/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/xen/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Xen 驱动

**配置项引用（Symbol References）**：[`CONFIG_BOARD_XENVM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XENVM)、[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)、[`CONFIG_BOOT_FDT`](P197_lib_配置项参考_1.md#CONFIG_BOOT_FDT)、[`CONFIG_FWARGS_HANDLER_HOOK`](P001_kernel_配置项参考_1.md#CONFIG_FWARGS_HANDLER_HOOK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_XENVM`。

<a id="CONFIG_XEN_FDT_MAX_SIZE"></a>

## 196.5 `CONFIG_XEN_FDT_MAX_SIZE`

**提示（Prompt）**：Xen 启动扁平设备树（boot FDT）的最大大小

**说明（Help）**

为复制的 Xen 启动设备树二进制块（boot device tree blob）保留的最大字节数。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN_FDT && CONFIG_XEN
```

**默认值（Defaults）**

```text
0x8000
```

**定义位置（Location）**：[`drivers/xen/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/xen/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Xen 驱动 → Xen 启动扁平设备树（boot FDT）支持

**配置项引用（Symbol References）**：[`CONFIG_XEN_FDT`](P196_drivers_xen_配置项参考.md#CONFIG_XEN_FDT)、[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)。

<a id="CONFIG_XEN_FLASK"></a>

## 196.6 `CONFIG_XEN_FLASK`

**提示（Prompt）**：XSM FLASK 驱动

**说明（Help）**

支持 XSM FLASK 超级调用接口（hypercall interface），可操作 Xen 安全策略（security policy），并为域（domains）分配安全标签（security labels）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**定义位置（Location）**：[`drivers/xen/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/xen/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Xen 驱动

**配置项引用（Symbol References）**：[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)。

<a id="CONFIG_XEN_GRANT_TABLE"></a>

## 196.7 `CONFIG_XEN_GRANT_TABLE`

**提示（Prompt）**：Xen 授权表驱动（grant table driver）

**说明（Help）**

Xen 授权表驱动（grant table driver）。注意：驱动使用 `k_malloc()` 动态分配内存，因此原文要求 `CONFIG_HEAP_MEM_POOL_SIZE` 大于或等于要分配并授权的页（pages）数量，或要映射的外部帧（foreign frames）数量。

译注：原文直接将堆大小与页／帧数量作比较，未给出页大小换算或额外管理开销；此处保留原文关系，不将它视为按字节计算的完整内存容量公式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_HEAP_MEM_POOL_SIZE > 0 || CONFIG_XEN_REGIONS) && CONFIG_XEN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/xen/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/xen/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Xen 驱动

**配置项引用（Symbol References）**：[`CONFIG_HEAP_MEM_POOL_SIZE`](P001_kernel_配置项参考_1.md#CONFIG_HEAP_MEM_POOL_SIZE)、[`CONFIG_XEN_REGIONS`](P196_drivers_xen_配置项参考.md#CONFIG_XEN_REGIONS)、[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)。

<a id="CONFIG_XEN_GRANT_TABLE_INIT_PRIORITY"></a>

## 196.8 `CONFIG_XEN_GRANT_TABLE_INIT_PRIORITY`

**提示（Prompt）**：授权表驱动初始化优先级（Grant table driver init priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN_GRANT_TABLE && CONFIG_XEN
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/xen/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/xen/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Xen 驱动 → Xen 授权表驱动（grant table driver）

**配置项引用（Symbol References）**：[`CONFIG_XEN_GRANT_TABLE`](P196_drivers_xen_配置项参考.md#CONFIG_XEN_GRANT_TABLE)、[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)。

<a id="CONFIG_XEN_REGIONS"></a>

## 196.9 `CONFIG_XEN_REGIONS`

**提示（Prompt）**：Xen 扩展区域驱动（extended regions driver）

**说明（Help）**

Xen 扩展区域驱动（extended regions driver），允许使用 Xen 虚拟机监控器（hypervisor）提供给 Zephyr 的扩展区域。借助该内存，可使用第二阶段地址转换（Stage 2 translation）层的空闲未映射空间，避免从 Zephyr 堆内存中分配。要求 hypervisor 节点中至少存在一个扩展区域（extended region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MMU && CONFIG_XEN
```

**主动选择（Selects）**

```text
CONFIG_SYS_MEM_BLOCKS
CONFIG_KERNEL_DIRECT_MAP
```

**定义位置（Location）**：[`drivers/xen/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/xen/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Xen 驱动

**配置项引用（Symbol References）**：[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)、[`CONFIG_SYS_MEM_BLOCKS`](P199_lib_配置项参考_3.md#CONFIG_SYS_MEM_BLOCKS)、[`CONFIG_KERNEL_DIRECT_MAP`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_DIRECT_MAP)。

<!-- kconfig-navigation -->

[上一章](P195_drivers_wuc_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P197_lib_配置项参考_1.md)
