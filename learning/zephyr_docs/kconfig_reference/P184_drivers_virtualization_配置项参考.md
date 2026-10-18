---
id: learning.zephyr-docs.kconfig-reference.page-184
title: "`drivers/virtualization`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第184章\_`drivers/virtualization`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/virtualization` 的 8 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_IVSHMEM"></a>

## 184.1 `CONFIG_IVSHMEM`

**提示（Prompt）**：虚拟机间共享内存设备（Inter-VM Shared Memory，ivshmem）

**说明（Help）**

启用 QEMU 的 ivshmem 设备支持。ACRN 虚拟机监控器（Hypervisor）也提供该设备，使虚拟机（VM）能够彼此共享内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PCIE && CONFIG_VIRTUALIZATION
```

**被选择（Selected by）**

```text
CONFIG_IVSHMEM_V2
```

**定义位置（Location）**：[`drivers/virtualization/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/virtualization/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 虚拟化客户机驱动（Virtualization Guest Drivers）

**配置项引用（Symbol References）**：[`CONFIG_PCIE`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE)、[`CONFIG_VIRTUALIZATION`](P184_drivers_virtualization_配置项参考.md#CONFIG_VIRTUALIZATION)、[`CONFIG_IVSHMEM_V2`](P184_drivers_virtualization_配置项参考.md#CONFIG_IVSHMEM_V2)。

<a id="CONFIG_IVSHMEM_DOORBELL"></a>

## 184.2 `CONFIG_IVSHMEM_DOORBELL`

**提示（Prompt）**：支持基于中断的 ivshmem（门铃版本，Doorbell Version）

**说明（Help）**

启用 `ivshmem-doorbell`，即基于中断的 ivshmem 支持。对于 `ivshmem-v2`，也支持 INTx 中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IVSHMEM && CONFIG_VIRTUALIZATION
```

**被选择（Selected by）**

```text
CONFIG_ETH_IVSHMEM
```

**定义位置（Location）**：[`drivers/virtualization/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/virtualization/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 虚拟化客户机驱动（Virtualization Guest Drivers） → 虚拟机间共享内存设备（Inter-VM Shared Memory，ivshmem）

**配置项引用（Symbol References）**：[`CONFIG_IVSHMEM`](P184_drivers_virtualization_配置项参考.md#CONFIG_IVSHMEM)、[`CONFIG_VIRTUALIZATION`](P184_drivers_virtualization_配置项参考.md#CONFIG_VIRTUALIZATION)、[`CONFIG_ETH_IVSHMEM`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_IVSHMEM)。

<a id="CONFIG_IVSHMEM_INT_PRIORITY"></a>

## 184.3 `CONFIG_IVSHMEM_INT_PRIORITY`

**提示（Prompt）**：MSI-X 中断优先级（Interrupt Priority）

**说明（Help）**

MSI-X 所产生中断使用的优先级。INTx 中断优先级在设备树（Device Tree）中配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IVSHMEM_DOORBELL && CONFIG_IVSHMEM && CONFIG_VIRTUALIZATION
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/virtualization/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/virtualization/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 虚拟化客户机驱动（Virtualization Guest Drivers） → 虚拟机间共享内存设备（Inter-VM Shared Memory，ivshmem） → 支持基于中断的 ivshmem（门铃版本，Doorbell Version）

**配置项引用（Symbol References）**：[`CONFIG_IVSHMEM_DOORBELL`](P184_drivers_virtualization_配置项参考.md#CONFIG_IVSHMEM_DOORBELL)、[`CONFIG_IVSHMEM`](P184_drivers_virtualization_配置项参考.md#CONFIG_IVSHMEM)、[`CONFIG_VIRTUALIZATION`](P184_drivers_virtualization_配置项参考.md#CONFIG_VIRTUALIZATION)。

<a id="CONFIG_IVSHMEM_MSI_X_VECTORS"></a>

## 184.4 `CONFIG_IVSHMEM_MSI_X_VECTORS`

**提示（Prompt）**：预分配的通知向量（Notification Vector）数量

**说明（Help）**

必须预先分配 MSI-X 向量存储对象（Vector Holders）。预分配数量可多于或少于实际需要，取决于相互连接的虚拟机（VM）数量。这些向量在 ivshmem 中称为通知向量（Notification Vectors）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IVSHMEM_DOORBELL && CONFIG_IVSHMEM && CONFIG_VIRTUALIZATION
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/virtualization/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/virtualization/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 虚拟化客户机驱动（Virtualization Guest Drivers） → 虚拟机间共享内存设备（Inter-VM Shared Memory，ivshmem） → 支持基于中断的 ivshmem（门铃版本，Doorbell Version）

**配置项引用（Symbol References）**：[`CONFIG_IVSHMEM_DOORBELL`](P184_drivers_virtualization_配置项参考.md#CONFIG_IVSHMEM_DOORBELL)、[`CONFIG_IVSHMEM`](P184_drivers_virtualization_配置项参考.md#CONFIG_IVSHMEM)、[`CONFIG_VIRTUALIZATION`](P184_drivers_virtualization_配置项参考.md#CONFIG_VIRTUALIZATION)。

<a id="CONFIG_IVSHMEM_SHELL"></a>

## 184.5 `CONFIG_IVSHMEM_SHELL`

**提示（Prompt）**：IVshmem 命令行模块（Shell Module）

**说明（Help）**

此模块主要用于获取 ivshmem 信息，以及／或者从另一台虚拟机（VM）快速测试 ivshmem 客户端应用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_IVSHMEM && CONFIG_VIRTUALIZATION
```

**定义位置（Location）**：[`drivers/virtualization/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/virtualization/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 虚拟化客户机驱动（Virtualization Guest Drivers） → 虚拟机间共享内存设备（Inter-VM Shared Memory，ivshmem）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_IVSHMEM`](P184_drivers_virtualization_配置项参考.md#CONFIG_IVSHMEM)、[`CONFIG_VIRTUALIZATION`](P184_drivers_virtualization_配置项参考.md#CONFIG_VIRTUALIZATION)。

<a id="CONFIG_IVSHMEM_V2"></a>

## 184.6 `CONFIG_IVSHMEM_V2`

**提示（Prompt）**：虚拟机间共享内存 v2（Inter-VM Shared Memory v2，ivshmem-v2）

**说明（Help）**

启用 `ivshmem-v2` 支持。它主要用于 Jailhouse 虚拟机监控器（Hypervisor）中的进程间通信（IPC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_VIRTUALIZATION
```

**主动选择（Selects）**

```text
CONFIG_IVSHMEM
```

**被选择（Selected by）**

```text
CONFIG_ETH_IVSHMEM
```

**定义位置（Location）**：[`drivers/virtualization/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/virtualization/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 虚拟化客户机驱动（Virtualization Guest Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIRTUALIZATION`](P184_drivers_virtualization_配置项参考.md#CONFIG_VIRTUALIZATION)、[`CONFIG_IVSHMEM`](P184_drivers_virtualization_配置项参考.md#CONFIG_IVSHMEM)、[`CONFIG_ETH_IVSHMEM`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_IVSHMEM)。

<a id="CONFIG_IVSHMEM_V2_MAX_PEERS"></a>

## 184.7 `CONFIG_IVSHMEM_V2_MAX_PEERS`

**提示（Prompt）**：ivshmem-v2 对端（Peer）的最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IVSHMEM_V2 && CONFIG_VIRTUALIZATION
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[2, 65536]
```

**定义位置（Location）**：[`drivers/virtualization/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/virtualization/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 虚拟化客户机驱动（Virtualization Guest Drivers） → 虚拟机间共享内存 v2（Inter-VM Shared Memory v2，ivshmem-v2）

**配置项引用（Symbol References）**：[`CONFIG_IVSHMEM_V2`](P184_drivers_virtualization_配置项参考.md#CONFIG_IVSHMEM_V2)、[`CONFIG_VIRTUALIZATION`](P184_drivers_virtualization_配置项参考.md#CONFIG_VIRTUALIZATION)。

<a id="CONFIG_VIRTUALIZATION"></a>

## 184.8 `CONFIG_VIRTUALIZATION`

**提示（Prompt）**：虚拟化客户机驱动（Virtualization Guest Drivers）

**说明（Help）**

包含多种驱动，用于 Zephyr 作为客户机（Guest）在虚拟化或仿真环境中运行时，支持并提供相应功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ETH_IVSHMEM
```

**定义位置（Location）**：[`drivers/virtualization/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/virtualization/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_IVSHMEM`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_IVSHMEM)。

<!-- kconfig-navigation -->

[上一章](P183_drivers_virtio_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P185_drivers_w1_配置项参考.md)
