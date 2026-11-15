---
id: learning.zephyr-docs.kconfig-reference.page-177
title: "`drivers/timeaware_gpio`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第177章\_`drivers/timeaware_gpio`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/timeaware_gpio` 的 3 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_TIMEAWARE_GPIO"></a>

## 177.1 `CONFIG_TIMEAWARE_GPIO`

**提示（Prompt）**：时间感知 GPIO（Time-aware GPIO）驱动

**说明（Help）**

启用时间感知 GPIO（Time-aware GPIO）驱动的配置选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/timeaware_gpio/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timeaware_gpio/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_TIMEAWARE_GPIO_INIT_PRIORITY"></a>

## 177.2 `CONFIG_TIMEAWARE_GPIO_INIT_PRIORITY`

**提示（Prompt）**：时间感知 GPIO 初始化优先级

**说明（Help）**

时间感知 GPIO（Time-aware GPIO）驱动的系统初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TIMEAWARE_GPIO
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/timeaware_gpio/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timeaware_gpio/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时间感知 GPIO（Time-aware GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_TIMEAWARE_GPIO`](P177_drivers_timeaware_gpio_配置项参考.md#CONFIG_TIMEAWARE_GPIO)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_TIMEAWARE_GPIO_INTEL"></a>

## 177.3 `CONFIG_TIMEAWARE_GPIO_INTEL`

**提示（Prompt）**：Intel 时间感知 GPIO（Time-aware GPIO）驱动

**说明（Help）**

Intel PCH 子系统中的 Intel 时间感知 GPIO（Time-aware GPIO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_TIMEAWARE_GPIO_ENABLED && CONFIG_TIMEAWARE_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/timeaware_gpio/Kconfig.intel:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timeaware_gpio/Kconfig.intel#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时间感知 GPIO（Time-aware GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_TIMEAWARE_GPIO`](P177_drivers_timeaware_gpio_配置项参考.md#CONFIG_TIMEAWARE_GPIO)。

<!-- kconfig-navigation -->

[上一章](P176_drivers_tee_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P178_drivers_uaol_配置项参考.md)
