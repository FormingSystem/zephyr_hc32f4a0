---
id: learning.zephyr-docs.kconfig-reference.page-178
title: "`drivers/uaol`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第178章\_`drivers/uaol`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/uaol` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_UAOL"></a>

## 178.1 `CONFIG_UAOL`

**提示（Prompt）**：USB 音频卸载链路（UAOL）驱动

**说明（Help）**

启用 USB 音频卸载链路（USB Audio Offload Link，UAOL）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/uaol/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/uaol/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_UAOL_INIT_PRIORITY"></a>

## 178.2 `CONFIG_UAOL_INIT_PRIORITY`

**提示（Prompt）**：UAOL 初始化优先级（Init Priority）

**说明（Help）**

UAOL 驱动设备的初始化优先级（Device Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UAOL
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEFAULT
```

**定义位置（Location）**：[`drivers/uaol/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/uaol/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 音频卸载链路（UAOL）驱动

**配置项引用（Symbol References）**：[`CONFIG_UAOL`](P178_drivers_uaol_配置项参考.md#CONFIG_UAOL)、[`CONFIG_KERNEL_INIT_PRIORITY_DEFAULT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEFAULT)。

<a id="CONFIG_UAOL_INTEL_ADSP"></a>

## 178.3 `CONFIG_UAOL_INTEL_ADSP`

**提示（Prompt）**：Intel ADSP UAOL 驱动。

**说明（Help）**

Intel ADSP UAOL 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_UAOL_ENABLED && CONFIG_PM_DEVICE_RUNTIME && CONFIG_UAOL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/uaol/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/uaol/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 音频卸载链路（UAOL）驱动

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)、[`CONFIG_UAOL`](P178_drivers_uaol_配置项参考.md#CONFIG_UAOL)。

<a id="CONFIG_UAOL_INTEL_ADSP_CLOCK_FREQUENCY"></a>

## 178.4 `CONFIG_UAOL_INTEL_ADSP_CLOCK_FREQUENCY`

**提示（Prompt）**：UAOL 时钟频率（Clock Frequency）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UAOL
```

**默认值（Defaults）**

```text
19200000
```

**定义位置（Location）**：[`drivers/uaol/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/uaol/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 音频卸载链路（UAOL）驱动

**配置项引用（Symbol References）**：[`CONFIG_UAOL`](P178_drivers_uaol_配置项参考.md#CONFIG_UAOL)。

<!-- kconfig-navigation -->

[上一章](P177_drivers_timeaware_gpio_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P179_drivers_usb_配置项参考_1.md)
