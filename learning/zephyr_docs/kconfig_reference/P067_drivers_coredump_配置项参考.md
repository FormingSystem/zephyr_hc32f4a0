---
id: learning.zephyr-docs.kconfig-reference.page-67
title: "`drivers/coredump`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第67章\_`drivers/coredump`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/coredump` 的 2 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_COREDUMP_DEVICE"></a>

## 67.1 `CONFIG_COREDUMP_DEVICE`

**提示（Prompt）**：核心转储伪设备驱动（Coredump Pseudo-Device Drivers）

**说明（Help）**

启用伪设备（Pseudo-Device）支持，以帮助将所需数据收集到核心转储（Core Dump）中。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/coredump/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/coredump/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_COREDUMP_DEVICE_INIT_PRIORITY"></a>

## 67.2 `CONFIG_COREDUMP_DEVICE_INIT_PRIORITY`

**提示（Prompt）**：核心转储设备初始化优先级（Coredump Device Init Priority）

**说明（Help）**

核心转储伪设备（Coredump Pseudo-Device）驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COREDUMP_DEVICE
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/coredump/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/coredump/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 核心转储伪设备驱动（Coredump Pseudo-Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COREDUMP_DEVICE`](P067_drivers_coredump_配置项参考.md#CONFIG_COREDUMP_DEVICE)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<!-- kconfig-navigation -->

[上一章](P066_drivers_console_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P068_drivers_counter_配置项参考_1.md)
