---
id: learning.zephyr-docs.kconfig-reference.page-90
title: "`drivers/ethernet`配置项参考（4/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第90章\_`drivers/ethernet`配置项参考（4/4）

本章翻译官方 Kconfig 数据库中 `drivers/ethernet` 的 32 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PHY_MAXLINEAR_GPY111"></a>

## 90.1 `CONFIG_PHY_MAXLINEAR_GPY111`

**提示（Prompt）**：MaxLinear GPY111 物理层（PHY）驱动

**说明（Help）**

启用 MaxLinear GPY111 以太网物理层（Ethernet PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXLINEAR_GPY111_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_PHY_MICROCHIP_KSZ8081"></a>

## 90.2 `CONFIG_PHY_MICROCHIP_KSZ8081`

**提示（Prompt）**：Microchip KSZ8081 物理层（PHY）驱动

**说明（Help）**

启用 Microchip KSZ8081 以太网物理层（Ethernet PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_KSZ8081_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_PHY_MICROCHIP_KSZ9131"></a>

## 90.3 `CONFIG_PHY_MICROCHIP_KSZ9131`

**提示（Prompt）**：Microchip KSZ9131 物理层（PHY）驱动

**说明（Help）**

启用 Microchip KSZ9131 以太网物理层（Ethernet PHY）驱动。此驱动同时支持 KSZ9131 和 LAN8840 PHY 芯片。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_MICROCHIP_KSZ9131_ENABLED || DT_HAS_MICROCHIP_LAN8840_ENABLED) && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_PHY_MICROCHIP_LAN8742"></a>

## 90.4 `CONFIG_PHY_MICROCHIP_LAN8742`

**提示（Prompt）**：Microchip LAN8742 物理层（PHY）驱动

**说明（Help）**

启用 Microchip LAN8742 以太网物理层（Ethernet PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_LAN8742_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
CONFIG_GPIO if n
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_PHY_MICROCHIP_T1S"></a>

## 90.5 `CONFIG_PHY_MICROCHIP_T1S`

**提示（Prompt）**：Microchip 10BASE-T1S 以太网物理层（Ethernet PHY）驱动

**说明（Help）**

启用 Microchip LAN8650/1 Rev.B0/B1 内部物理层（Internal PHY）以及 LAN8670/1/2 Rev.C1/C2/D0 物理层（PHY）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_T1S_PHY_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
CONFIG_PHY_OA_TC14_PLCA_LIB
CONFIG_ETH_PHY_API_PLCA
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig.microchip_t1s:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig.microchip_t1s#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_PHY_OA_TC14_PLCA_LIB`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_OA_TC14_PLCA_LIB)、[`CONFIG_ETH_PHY_API_PLCA`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_API_PLCA)。

<a id="CONFIG_PHY_MICROCHIP_VSC8541"></a>

## 90.6 `CONFIG_PHY_MICROCHIP_VSC8541`

**提示（Prompt）**：Microchip VSC8541 物理层（PHY）驱动

**说明（Help）**

启用 Microchip VSC8541 以太网物理层（Ethernet PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_VSC8541_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_PHY_MONITOR_PERIOD"></a>

## 90.7 `CONFIG_PHY_MONITOR_PERIOD`

**提示（Prompt）**：监控任务执行周期（Monitor Task Execution Period）

**说明（Help）**

监控任务（Monitor Task）的执行周期，以毫秒为单位。该任务定期运行，用于检测 PHY 链路状态（Link Status）的变化，并将变化报告给操作系统（Operating System）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_PHY_MOTORCOMM_YT8521"></a>

## 90.8 `CONFIG_PHY_MOTORCOMM_YT8521`

**提示（Prompt）**：裕太微（Motorcomm）YT8521/YT8531 以太网物理层（Ethernet PHY）驱动

**说明（Help）**

启用裕太微（Motorcomm）YT8521/YT8531 以太网物理层（Ethernet PHY）驱动。此驱动同时支持 YT8521 和 YT8531 PHY 芯片。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_MOTORCOMM_YT8521_ENABLED || DT_HAS_MOTORCOMM_YT8531_ENABLED) && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:191`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L191)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_PHY_NXP_T1S"></a>

## 90.9 `CONFIG_PHY_NXP_T1S`

**提示（Prompt）**：NXP 10BASE-T1S 以太网物理层（Ethernet PHY）驱动

**说明（Help）**

启用 NXP 10BASE-T1S 物理层（PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_T1S_PHY_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ETH_PHY_API_PLCA
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig.nxp_t1s:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig.nxp_t1s#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_PHY_API_PLCA`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_API_PLCA)。

<a id="CONFIG_PHY_OA_TC14_PLCA_LIB"></a>

## 90.10 `CONFIG_PHY_OA_TC14_PLCA_LIB`

**提示（Prompt）**：OPEN Alliance TC14 PLCA 通用库（Generic Library）

**说明（Help）**

启用 OPEN Alliance TC14 物理层冲突避免（PLCA）通用库（Generic Library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_PHY_MICROCHIP_T1S
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PHY_MICROCHIP_T1S`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_MICROCHIP_T1S)。

<a id="CONFIG_PHY_QUALCOMM_AR8031"></a>

## 90.11 `CONFIG_PHY_QUALCOMM_AR8031`

**提示（Prompt）**：Qualcomm Atheros AR8031 以太网物理层（Ethernet PHY）驱动

**说明（Help）**

启用 Qualcomm Atheros AR8031 以太网物理层（Ethernet PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_QCA_AR8031_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L147)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_PHY_REALTEK_RTL8211F"></a>

## 90.12 `CONFIG_PHY_REALTEK_RTL8211F`

**提示（Prompt）**：Realtek RTL8211F 物理层（PHY）驱动

**说明（Help）**

启用瑞昱（Realtek）RTL8211F 以太网物理层（Ethernet PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTL8211F_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_PHY_TI_DP83825"></a>

## 90.13 `CONFIG_PHY_TI_DP83825`

**提示（Prompt）**：TI DP83825 物理层（PHY）驱动

**说明（Help）**

启用 TI DP83825 以太网物理层（Ethernet PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_DP83825_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_PHY_TI_DP83867"></a>

## 90.14 `CONFIG_PHY_TI_DP83867`

**提示（Prompt）**：TI DP83867 物理层（PHY）驱动

**说明（Help）**

启用 TI DP83867 以太网物理层（Ethernet PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_DP83867_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_PHY_TJA1103"></a>

## 90.15 `CONFIG_PHY_TJA1103`

**提示（Prompt）**：TJA1103 物理层（PHY）驱动

**说明（Help）**

启用 TJA1103 物理层（PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_TJA1103_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig.tja1103:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig.tja1103#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_PHY_TJA1103_IRQ_THREAD_PRIO"></a>

## 90.16 `CONFIG_PHY_TJA1103_IRQ_THREAD_PRIO`

**提示（Prompt）**：内部传入数据包处理线程（Incoming Packet Handler）的优先级

**说明（Help）**

负责 TJA1103 INT 中断请求（IRQ）处理的内部线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PHY_TJA1103 && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig.tja1103:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig.tja1103#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → TJA1103 物理层（PHY）驱动

**配置项引用（Symbol References）**：[`CONFIG_PHY_TJA1103`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_TJA1103)、[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_PHY_TJA1103_IRQ_THREAD_STACK_SIZE"></a>

## 90.17 `CONFIG_PHY_TJA1103_IRQ_THREAD_STACK_SIZE`

**提示（Prompt）**：处理 TJA1103 中断请求（IRQ）的线程栈大小（Stack Size）

**说明（Help）**

用于处理已触发的 INT 中断请求（IRQ）的内部线程所用的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PHY_TJA1103 && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig.tja1103:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig.tja1103#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → TJA1103 物理层（PHY）驱动

**配置项引用（Symbol References）**：[`CONFIG_PHY_TJA1103`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_TJA1103)、[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_PHY_TJA11XX"></a>

## 90.18 `CONFIG_PHY_TJA11XX`

**提示（Prompt）**：TJA11XX 物理层（PHY）驱动

**说明（Help）**

启用 TJA11xx 物理层（PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_TJA11XX_ENABLED && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig.tja11xx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig.tja11xx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_PHY_VERIFY_DEVICE_IDENTIFICATION"></a>

## 90.19 `CONFIG_PHY_VERIFY_DEVICE_IDENTIFICATION`

**提示（Prompt）**：验证所选 PHY 与实际报告的 PHY 芯片标识（Chip ID）是否匹配

**说明（Help）**

验证物理层芯片（PHY Chip）报告的组织唯一标识符（Organizationally Unique Identifier，OUI）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_PTP_CLOCK_DWC_MAC"></a>

## 90.20 `CONFIG_PTP_CLOCK_DWC_MAC`

**提示（Prompt）**：DWC MAC 精密时间协议时钟驱动支持（PTP Clock Driver Support）

**说明（Help）**

为 Synopsys DesignWare MAC 核（Core）启用精密时间协议（PTP）时钟支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK && DT_HAS_SNPS_DWMAC_PTP_CLOCK_ENABLED && (CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_PTP_TIMESTAMPING
CONFIG_PINCTRL if n
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig.ptp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig.ptp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_CLOCK)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_L2_PTP_TIMESTAMPING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP_TIMESTAMPING)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_PTP_CLOCK_DWC_MAC_DIGITAL_ROLLOVER"></a>

## 90.21 `CONFIG_PTP_CLOCK_DWC_MAC_DIGITAL_ROLLOVER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

让精密时间协议（PTP）系统时间以十进制回卷模式（Digital Rollover Mode）运行：不足一秒的字段（Sub-Second Field）按纳秒计数，在 `10^9` 处回卷；不采用二进制回卷模式（Binary Rollover Mode），后者以 `2^-31 s` 为单位计数，并在 `2^31` 处回卷。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_STM32F1X && CONFIG_PTP_CLOCK_DWC_MAC && (CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig.ptp:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig.ptp#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动 → DWC MAC 精密时间协议时钟驱动支持（PTP Clock Driver Support）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_PTP_CLOCK_DWC_MAC`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F1X`。

<a id="CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP"></a>

## 90.22 `CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP`

**提示（Prompt）**：需要记录时间戳的接收帧（Received Frames to Timestamp）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK_DWC_MAC && (CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP if CONFIG_PTP || CONFIG_NET_GPTP
CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_ALL
```

**可选项（Choices）**

```text
CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_ALL
CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig.ptp:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig.ptp#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动 → DWC MAC 精密时间协议时钟驱动支持（PTP Clock Driver Support）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK_DWC_MAC`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP)、[`CONFIG_PTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP)、[`CONFIG_NET_GPTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_GPTP)、[`CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_ALL`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_ALL)。

<a id="CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_ALL"></a>

## 90.23 `CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_ALL`

**提示（Prompt）**：所有帧（All Frames）

**说明（Help）**

为每个收到的帧记录时间戳（Timestamp）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP>
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig.ptp:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig.ptp#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动 → DWC MAC 精密时间协议时钟驱动支持（PTP Clock Driver Support） → 需要记录时间戳的接收帧（Received Frames to Timestamp）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP)。

<a id="CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_IPV4"></a>

## 90.24 `CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_IPV4`

**提示（Prompt）**：通过 UDP/IPv4 传输 PTP（PTP over UDP/IPv4）

**说明（Help）**

为通过 UDP/IPv4 承载的 PTP 帧记录时间戳（Timestamp）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP && CONFIG_PTP_CLOCK_DWC_MAC && (CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y if CONFIG_PTP_UDP_IPV4_PROTOCOL
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig.ptp:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig.ptp#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动 → DWC MAC 精密时间协议时钟驱动支持（PTP Clock Driver Support）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP)、[`CONFIG_PTP_CLOCK_DWC_MAC`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PTP_UDP_IPV4_PROTOCOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_UDP_IPV4_PROTOCOL)。

<a id="CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_IPV6"></a>

## 90.25 `CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_IPV6`

**提示（Prompt）**：通过 UDP/IPv6 传输 PTP（PTP over UDP/IPv6）

**说明（Help）**

为通过 UDP/IPv6 承载的 PTP 帧记录时间戳（Timestamp）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP && CONFIG_PTP_CLOCK_DWC_MAC && (CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y if CONFIG_PTP_UDP_IPV6_PROTOCOL
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig.ptp:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig.ptp#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动 → DWC MAC 精密时间协议时钟驱动支持（PTP Clock Driver Support）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP)、[`CONFIG_PTP_CLOCK_DWC_MAC`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PTP_UDP_IPV6_PROTOCOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_UDP_IPV6_PROTOCOL)。

<a id="CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_L2"></a>

## 90.26 `CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_L2`

**提示（Prompt）**：通过以太网传输 PTP（PTP over Ethernet）

**说明（Help）**

为直接通过以太网（Ethernet）承载的 PTP 帧记录时间戳（Timestamp）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP && CONFIG_PTP_CLOCK_DWC_MAC && (CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y if CONFIG_PTP_IEEE_802_3_PROTOCOL || CONFIG_NET_GPTP
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig.ptp:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig.ptp#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动 → DWC MAC 精密时间协议时钟驱动支持（PTP Clock Driver Support）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP)、[`CONFIG_PTP_CLOCK_DWC_MAC`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PTP_IEEE_802_3_PROTOCOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_IEEE_802_3_PROTOCOL)、[`CONFIG_NET_GPTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_GPTP)。

<a id="CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP"></a>

## 90.27 `CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP`

**提示（Prompt）**：仅 PTP 帧（PTP Frames Only）

**说明（Help）**

仅为收到的、属于已启用 PTP 版本和传输方式（Transport）的 PTP 事件消息（Event Message）记录时间戳。它涵盖端到端（End-to-End）和对等（Peer-to-Peer）延迟机制所需的消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP>
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig.ptp:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig.ptp#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动 → DWC MAC 精密时间协议时钟驱动支持（PTP Clock Driver Support） → 需要记录时间戳的接收帧（Received Frames to Timestamp）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP)。

<a id="CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTPV2"></a>

## 90.28 `CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTPV2`

**提示（Prompt）**：PTPv2 帧格式（Frame Format）

**说明（Help）**

按 IEEE 1588-2008（PTPv2）解析收到的 PTP 帧；否则按 IEEE 1588-2002（PTPv1）解析。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP && CONFIG_PTP_CLOCK_DWC_MAC && (CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig.ptp:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig.ptp#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动 → DWC MAC 精密时间协议时钟驱动支持（PTP Clock Driver Support）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC_RX_TIMESTAMP_PTP)、[`CONFIG_PTP_CLOCK_DWC_MAC`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_PTP_CLOCK_ESP32"></a>

## 90.29 `CONFIG_PTP_CLOCK_ESP32`

**提示（Prompt）**：ESP32 以太网精密时间协议时钟驱动（PTP Clock Driver）

**说明（Help）**

启用以太网 MAC 提供的 IEEE 1588 精密时间协议（PTP）时钟。MAC 在硬件中为发送帧和接收帧记录时间戳，并提供一个自由运行时钟（Free-Running Clock），可设置其时间、调整偏移（Offset）和速率（Rate）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK && DT_HAS_SNPS_DWMAC_PTP_CLOCK_ENABLED && CONFIG_ETH_ESP32 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.esp32:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.esp32#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ESP32 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_CLOCK)、[`CONFIG_ETH_ESP32`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ESP32)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_PTP_CLOCK_SAM_GMAC"></a>

## 90.30 `CONFIG_PTP_CLOCK_SAM_GMAC`

**提示（Prompt）**：SAM GMAC 精密时间协议时钟驱动支持（PTP Clock Driver Support）

**说明（Help）**

启用 SAM GMAC 精密时间协议（PTP）时钟支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK && CONFIG_ETH_SAM_GMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_PTP_TIMESTAMPING
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.sam_gmac:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.sam_gmac#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Atmel SAM 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_CLOCK)、[`CONFIG_ETH_SAM_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_SAM_GMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_L2_PTP_TIMESTAMPING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP_TIMESTAMPING)。

<a id="CONFIG_PTP_CLOCK_STM32_HAL"></a>

## 90.31 `CONFIG_PTP_CLOCK_STM32_HAL`

**提示（Prompt）**：STM32 HAL 精密时间协议时钟驱动支持（PTP Clock Driver Support）

**说明（Help）**

启用 STM32 精密时间协议（PTP）时钟支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK && DT_HAS_SNPS_DWMAC_PTP_CLOCK_ENABLED && CONFIG_ETH_STM32_HAL_API_V2 && (CONFIG_SOC_SERIES_STM32F7X || CONFIG_SOC_SERIES_STM32H5X || CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H7RSX || CONFIG_SOC_SERIES_STM32N6X) && CONFIG_ETH_STM32_HAL && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_PTP_TIMESTAMPING
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_CLOCK)、[`CONFIG_ETH_STM32_HAL_API_V2`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_STM32_HAL_API_V2)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_L2_PTP_TIMESTAMPING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP_TIMESTAMPING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_SERIES_STM32N6X`。

<a id="CONFIG_PTP_CLOCK_XMC4XXX"></a>

## 90.32 `CONFIG_PTP_CLOCK_XMC4XXX`

**提示（Prompt）**：XMC4XXX 精密时间协议时钟驱动支持（PTP Clock Driver Support）

**说明（Help）**

启用 XMC4XXX 精密时间协议（PTP）时钟支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK && DT_HAS_SNPS_DWMAC_PTP_CLOCK_ENABLED && CONFIG_ETH_XMC4XXX && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_PTP_TIMESTAMPING
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.xmc4xxx:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.xmc4xxx#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → XMC4XXX 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_CLOCK)、[`CONFIG_ETH_XMC4XXX`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XMC4XXX)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_L2_PTP_TIMESTAMPING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP_TIMESTAMPING)。

<!-- kconfig-navigation -->

[上一章](P089_drivers_ethernet_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P091_drivers_firmware_配置项参考.md)
