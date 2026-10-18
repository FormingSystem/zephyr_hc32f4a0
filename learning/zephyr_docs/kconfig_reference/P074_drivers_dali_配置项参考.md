---
id: learning.zephyr-docs.kconfig-reference.page-74
title: "`drivers/dali`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第74章\_`drivers/dali`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/dali` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DALI"></a>

## 74.1 `CONFIG_DALI`

**提示（Prompt）**：数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）驱动【实验性】

**说明（Help）**

启用对 DALI 总线（IEC 62386）的通用支持。此功能为实验性（Experimental），可能不稳定。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/dali/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dali/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_DALI_PWM"></a>

## 74.2 `CONFIG_DALI_PWM`

**提示（Prompt）**：通用 PWM DALI 驱动

**说明（Help）**

为具有通用脉宽调制（Pulse Width Modulation，PWM）功能的微控制器（MCU）启用 DALI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_DALI_PWM_ENABLED && CONFIG_DALI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PWM
CONFIG_COUNTER
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/dali/Kconfig.pwm:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dali/Kconfig.pwm#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_DALI`](P074_drivers_dali_配置项参考.md#CONFIG_DALI)、[`CONFIG_PWM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_DALI_PWM_PRIORITY"></a>

## 74.3 `CONFIG_DALI_PWM_PRIORITY`

**提示（Prompt）**：DALI 工作队列（Workqueue）优先级

**说明（Help）**

DALI 驱动所用工作队列（Workqueue）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DALI_PWM && CONFIG_DALI
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/dali/Kconfig.pwm:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dali/Kconfig.pwm#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）驱动【实验性】 → 通用 PWM DALI 驱动

**配置项引用（Symbol References）**：[`CONFIG_DALI_PWM`](P074_drivers_dali_配置项参考.md#CONFIG_DALI_PWM)、[`CONFIG_DALI`](P074_drivers_dali_配置项参考.md#CONFIG_DALI)。

<a id="CONFIG_DALI_PWM_STACK_SIZE"></a>

## 74.4 `CONFIG_DALI_PWM_STACK_SIZE`

**提示（Prompt）**：DALI 驱动工作队列线程栈（Workqueue Thread Stack）大小

**说明（Help）**

线程栈（Thread Stack）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DALI_PWM && CONFIG_DALI
```

**默认值（Defaults）**

```text
1120
```

**定义位置（Location）**：[`drivers/dali/Kconfig.pwm:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dali/Kconfig.pwm#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）驱动【实验性】 → 通用 PWM DALI 驱动

**配置项引用（Symbol References）**：[`CONFIG_DALI_PWM`](P074_drivers_dali_配置项参考.md#CONFIG_DALI_PWM)、[`CONFIG_DALI`](P074_drivers_dali_配置项参考.md#CONFIG_DALI)。

<!-- kconfig-navigation -->

[上一章](P073_drivers_dai_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P075_drivers_debug_配置项参考.md)
