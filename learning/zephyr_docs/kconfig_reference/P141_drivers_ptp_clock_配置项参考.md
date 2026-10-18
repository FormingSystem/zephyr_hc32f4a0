---
id: learning.zephyr-docs.kconfig-reference.page-141
title: "`drivers/ptp_clock`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第141章\_`drivers/ptp_clock`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/ptp_clock` 的 7 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PTP_CLOCK"></a>

## 141.1 `CONFIG_PTP_CLOCK`

**提示（Prompt）**：精确时间协议（Precision Time Protocol，PTP）时钟驱动

**说明（Help）**

启用精确时间协议时钟驱动的选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_NET_GPTP
CONFIG_NET_L2_PTP
CONFIG_PTP
```

**定义位置（Location）**：[`drivers/ptp_clock/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ptp_clock/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_PTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP)、[`CONFIG_PTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP)。

<a id="CONFIG_PTP_CLOCK_INIT_PRIORITY"></a>

## 141.2 `CONFIG_PTP_CLOCK_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

PTP 时钟设备驱动初始化优先级

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK
```

**默认值（Defaults）**

```text
CONFIG_ETH_INIT_PRIORITY if CONFIG_ETH_DRIVER
75
```

**定义位置（Location）**：[`drivers/ptp_clock/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ptp_clock/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 精确时间协议（Precision Time Protocol，PTP）时钟驱动

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK)、[`CONFIG_ETH_INIT_PRIORITY`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_INIT_PRIORITY)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_PTP_CLOCK_NATIVE"></a>

## 141.3 `CONFIG_PTP_CLOCK_NATIVE`

**提示（Prompt）**：native_sim 的 PTP 时钟驱动

**说明（Help）**

启用 native_sim 的 PTP 时钟驱动，以支持以太网时间戳（Timestamping）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_NATIVE_PTP_CLOCK_ENABLED && CONFIG_ARCH_POSIX && CONFIG_PTP_CLOCK
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_PTP_TIMESTAMPING
CONFIG_NATIVE_USE_NSI_ERRNO
```

**定义位置（Location）**：[`drivers/ptp_clock/Kconfig.native:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ptp_clock/Kconfig.native#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 精确时间协议（Precision Time Protocol，PTP）时钟驱动

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_PTP_CLOCK`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK)、[`CONFIG_NET_L2_PTP_TIMESTAMPING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP_TIMESTAMPING)、[`CONFIG_NATIVE_USE_NSI_ERRNO`](P033_arch_posix_配置项参考.md#CONFIG_NATIVE_USE_NSI_ERRNO)。

<a id="CONFIG_PTP_CLOCK_NXP_ENET"></a>

## 141.4 `CONFIG_PTP_CLOCK_NXP_ENET`

**提示（Prompt）**：NXP ENET PTP 时钟驱动

**说明（Help）**

启用 NXP ENET PTP 时钟，以支持以太网时间戳。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_ENET_PTP_CLOCK_ENABLED && CONFIG_ETH_NXP_ENET && CONFIG_PTP_CLOCK
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_PTP_TIMESTAMPING
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/ptp_clock/Kconfig.nxp_enet:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ptp_clock/Kconfig.nxp_enet#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 精确时间协议（Precision Time Protocol，PTP）时钟驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET)、[`CONFIG_PTP_CLOCK`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK)、[`CONFIG_NET_L2_PTP_TIMESTAMPING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP_TIMESTAMPING)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PTP_CLOCK_NXP_ENET_QOS"></a>

## 141.5 `CONFIG_PTP_CLOCK_NXP_ENET_QOS`

**提示（Prompt）**：NXP ENET QoS PTP 时钟驱动

**说明（Help）**

启用 NXP ENET QoS PTP 时钟，以支持以太网时间戳。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DWMAC_PTP_CLOCK_ENABLED && CONFIG_ETH_NXP_ENET_QOS && CONFIG_PTP_CLOCK
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_PTP_TIMESTAMPING
```

**定义位置（Location）**：[`drivers/ptp_clock/Kconfig.nxp_enet_qos:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ptp_clock/Kconfig.nxp_enet_qos#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 精确时间协议（Precision Time Protocol，PTP）时钟驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET_QOS)、[`CONFIG_PTP_CLOCK`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK)、[`CONFIG_NET_L2_PTP_TIMESTAMPING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP_TIMESTAMPING)。

<a id="CONFIG_PTP_CLOCK_NXP_NETC"></a>

## 141.6 `CONFIG_PTP_CLOCK_NXP_NETC`

**提示（Prompt）**：NXP NETC PTP 时钟驱动

**说明（Help）**

启用 NXP NETC PTP 时钟，以支持以太网时间戳。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_NETC_PTP_CLOCK_ENABLED && CONFIG_ETH_NXP_IMX_NETC && CONFIG_PTP_CLOCK
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_PTP_TIMESTAMPING
```

**定义位置（Location）**：[`drivers/ptp_clock/Kconfig.nxp_netc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ptp_clock/Kconfig.nxp_netc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 精确时间协议（Precision Time Protocol，PTP）时钟驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_IMX_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_IMX_NETC)、[`CONFIG_PTP_CLOCK`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK)、[`CONFIG_NET_L2_PTP_TIMESTAMPING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP_TIMESTAMPING)。

<a id="CONFIG_PTP_CLOCK_SHELL"></a>

## 141.7 `CONFIG_PTP_CLOCK_SHELL`

**提示（Prompt）**：PTP 时钟命令行（Shell）

**说明（Help）**

启用 PTP 时钟 Shell。所用快照中的 PTP 时钟 Shell 支持时钟操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_PTP_CLOCK
```

**被选择（Selected by）**

```text
CONFIG_NET_SHELL_QBV_SUPPORTED
```

**定义位置（Location）**：[`drivers/ptp_clock/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ptp_clock/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 精确时间协议（Precision Time Protocol，PTP）时钟驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_PTP_CLOCK`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK)、[`CONFIG_NET_SHELL_QBV_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SHELL_QBV_SUPPORTED)。

<!-- kconfig-navigation -->

[上一章](P140_drivers_psi5_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P142_drivers_pulse_io_配置项参考.md)
