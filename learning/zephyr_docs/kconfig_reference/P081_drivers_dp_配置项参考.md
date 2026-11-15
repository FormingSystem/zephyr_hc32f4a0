---
id: learning.zephyr-docs.kconfig-reference.page-81
title: "`drivers/dp`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第81章\_`drivers/dp`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/dp` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DP_DRIVER"></a>

## 81.1 `CONFIG_DP_DRIVER`

**提示（Prompt）**：调试端口（Debug Port，DP）驱动【实验性】

**说明（Help）**

启用调试端口（Debug Port）接口驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_DAP
```

**定义位置（Location）**：[`drivers/dp/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dp/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_DAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DAP)。

<a id="CONFIG_DP_DRIVER_INIT_PRIO"></a>

## 81.2 `CONFIG_DP_DRIVER_INIT_PRIO`

**提示（Prompt）**：调试端口驱动的初始化优先级（Initialization Priority）

**说明（Help）**

设置初始化优先级（Initialization Priority）数值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DP_DRIVER
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/dp/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dp/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试端口（Debug Port，DP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_DP_DRIVER`](P081_drivers_dp_配置项参考.md#CONFIG_DP_DRIVER)。

<a id="CONFIG_SWDP_BITBANG_DRIVER"></a>

## 81.3 `CONFIG_SWDP_BITBANG_DRIVER`

**提示（Prompt）**：串行线调试端口位模拟驱动（Serial Wire Debug Port Bit-Bang Driver）

**说明（Help）**

串行线调试端口（Serial Wire Debug Port）的位模拟驱动（Bit-Bang Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_SWDP_GPIO_ENABLED && CONFIG_GPIO && CONFIG_DP_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dp/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dp/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试端口（Debug Port，DP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_DP_DRIVER`](P081_drivers_dp_配置项参考.md#CONFIG_DP_DRIVER)。

<a id="CONFIG_SWDP_BITBANG_NO_DISCONNECT"></a>

## 81.4 `CONFIG_SWDP_BITBANG_NO_DISCONNECT`

**提示（Prompt）**：使用 `GPIO_INPUT` 代替 `GPIO_DISCONNECTED`

**说明（Help）**

停用调试端口（Debug Port）时，使用 `GPIO_INPUT` 代替 `GPIO_DISCONNECTED`。当底层 GPIO 驱动不支持 `GPIO_DISCONNECTED` 状态时，使用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SWDP_BITBANG_DRIVER && CONFIG_DP_DRIVER
```

**默认值（Defaults）**

```text
y if CONFIG_GPIO_STM32
```

**定义位置（Location）**：[`drivers/dp/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dp/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试端口（Debug Port，DP）驱动【实验性】 → 串行线调试端口位模拟驱动（Serial Wire Debug Port Bit-Bang Driver）

**配置项引用（Symbol References）**：[`CONFIG_SWDP_BITBANG_DRIVER`](P081_drivers_dp_配置项参考.md#CONFIG_SWDP_BITBANG_DRIVER)、[`CONFIG_DP_DRIVER`](P081_drivers_dp_配置项参考.md#CONFIG_DP_DRIVER)、[`CONFIG_GPIO_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_STM32)。

<!-- kconfig-navigation -->

[上一章](P080_drivers_dma_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P082_drivers_edac_配置项参考.md)
