---
id: learning.zephyr-docs.kconfig-reference.page-104
title: "`drivers/hwspinlock`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第104章\_`drivers/hwspinlock`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/hwspinlock` 的 5 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HWSPINLOCK"></a>

## 104.1 `CONFIG_HWSPINLOCK`

**提示（Prompt）**：硬件自旋锁驱动（Hardware Spinlock Drivers）

**说明（Help）**

包含硬件自旋锁（Hardware Spinlock）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/hwspinlock/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwspinlock/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_HWSPINLOCK_INIT_PRIORITY"></a>

## 104.2 `CONFIG_HWSPINLOCK_INIT_PRIORITY`

**提示（Prompt）**：硬件自旋锁初始化优先级（HW Spinlock Init Priority）

**说明（Help）**

硬件自旋锁（HW Spinlock）驱动设备的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HWSPINLOCK
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEFAULT
```

**定义位置（Location）**：[`drivers/hwspinlock/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwspinlock/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件自旋锁驱动（Hardware Spinlock Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWSPINLOCK`](P104_drivers_hwspinlock_配置项参考.md#CONFIG_HWSPINLOCK)、[`CONFIG_KERNEL_INIT_PRIORITY_DEFAULT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEFAULT)。

<a id="CONFIG_HWSPINLOCK_NXP_SEMA42"></a>

## 104.3 `CONFIG_HWSPINLOCK_NXP_SEMA42`

**提示（Prompt）**：NXP SEMA42 硬件自旋锁驱动（HW Spinlock Driver）

**说明（Help）**

此选项启用 SEMA42 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SEMA42_ENABLED && CONFIG_HWSPINLOCK
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/hwspinlock/Kconfig.nxp_sema42:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwspinlock/Kconfig.nxp_sema42#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件自旋锁驱动（Hardware Spinlock Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWSPINLOCK`](P104_drivers_hwspinlock_配置项参考.md#CONFIG_HWSPINLOCK)。

<a id="CONFIG_SQN_HWSPINLOCK"></a>

## 104.4 `CONFIG_SQN_HWSPINLOCK`

**提示（Prompt）**：Sequans 硬件自旋锁驱动（HW Spinlock Driver）

**说明（Help）**

为 SQN 启用硬件自旋锁（HW Spinlock）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SQN_HWSPINLOCK_ENABLED && CONFIG_HWSPINLOCK
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/hwspinlock/Kconfig.sqn:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwspinlock/Kconfig.sqn#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件自旋锁驱动（Hardware Spinlock Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWSPINLOCK`](P104_drivers_hwspinlock_配置项参考.md#CONFIG_HWSPINLOCK)。

<a id="CONFIG_SQN_HWSPINLOCK_RELAX_TIME"></a>

## 104.5 `CONFIG_SQN_HWSPINLOCK_RELAX_TIME`

**提示（Prompt）**：Sequans 硬件自旋锁放松时间（Relax Time）

**说明（Help）**

默认硬件自旋锁放松时间（Relax Time），以微秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SQN_HWSPINLOCK && CONFIG_HWSPINLOCK
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/hwspinlock/Kconfig.sqn:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwspinlock/Kconfig.sqn#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件自旋锁驱动（Hardware Spinlock Drivers） → Sequans 硬件自旋锁驱动（HW Spinlock Driver）

**配置项引用（Symbol References）**：[`CONFIG_SQN_HWSPINLOCK`](P104_drivers_hwspinlock_配置项参考.md#CONFIG_SQN_HWSPINLOCK)、[`CONFIG_HWSPINLOCK`](P104_drivers_hwspinlock_配置项参考.md#CONFIG_HWSPINLOCK)。

<!-- kconfig-navigation -->

[上一章](P103_drivers_hwinfo_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P105_drivers_i2c_配置项参考_1.md)
