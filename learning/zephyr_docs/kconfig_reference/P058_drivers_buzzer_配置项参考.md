---
id: learning.zephyr-docs.kconfig-reference.page-58
title: "`drivers/buzzer`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第58章\_`drivers/buzzer`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/buzzer` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BUZZER"></a>

## 58.1 `CONFIG_BUZZER`

**提示（Prompt）**：蜂鸣器驱动（Buzzer Drivers）［实验性，EXPERIMENTAL］

**说明（Help）**

在系统配置中包含蜂鸣器（Buzzer）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/buzzer/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/buzzer/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_BUZZER_GPIO"></a>

## 58.2 `CONFIG_BUZZER_GPIO`

**提示（Prompt）**：GPIO 驱动的有源蜂鸣器（Active Buzzer）

**说明（Help）**

为带有内置振荡器（Built-In Oscillator）的有源蜂鸣器启用 GPIO 后端（Backend）。驱动只控制开启／关闭，蜂鸣器的谐振频率（Resonance Frequency）由硬件固定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GPIO_BUZZER_ENABLED && CONFIG_BUZZER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/buzzer/Kconfig.gpio:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/buzzer/Kconfig.gpio#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蜂鸣器驱动（Buzzer Drivers）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_BUZZER`](P058_drivers_buzzer_配置项参考.md#CONFIG_BUZZER)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_BUZZER_INIT_PRIORITY"></a>

## 58.3 `CONFIG_BUZZER_INIT_PRIORITY`

**提示（Prompt）**：蜂鸣器初始化优先级（Initialization Priority）

**说明（Help）**

蜂鸣器（Buzzer）驱动的系统初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BUZZER
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/buzzer/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/buzzer/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蜂鸣器驱动（Buzzer Drivers）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_BUZZER`](P058_drivers_buzzer_配置项参考.md#CONFIG_BUZZER)。

<a id="CONFIG_BUZZER_PWM"></a>

## 58.4 `CONFIG_BUZZER_PWM`

**提示（Prompt）**：PWM 驱动的无源压电蜂鸣器（Passive Piezo Buzzer）

**说明（Help）**

为无源压电蜂鸣器（Passive Piezo Buzzer）启用脉宽调制（PWM）后端。PWM 通道周期决定声音频率，占空比（Duty Cycle）决定音量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PWM_BUZZER_ENABLED && CONFIG_BUZZER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PWM
```

**定义位置（Location）**：[`drivers/buzzer/Kconfig.pwm:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/buzzer/Kconfig.pwm#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蜂鸣器驱动（Buzzer Drivers）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_BUZZER`](P058_drivers_buzzer_配置项参考.md#CONFIG_BUZZER)、[`CONFIG_PWM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM)。

<!-- kconfig-navigation -->

[上一章](P057_drivers_bluetooth_配置项参考_4.md) · [返回大纲](大纲.md) · [下一章](P059_drivers_cache_配置项参考.md)
