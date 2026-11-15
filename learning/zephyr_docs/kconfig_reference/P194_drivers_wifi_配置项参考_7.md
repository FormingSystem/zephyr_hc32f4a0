---
id: learning.zephyr-docs.kconfig-reference.page-194
title: "`drivers/wifi`配置项参考（7/7）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第194章\_`drivers/wifi`配置项参考（7/7）

本章翻译官方 Kconfig 数据库中 `drivers/wifi` 的 13 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_WIFI_WINC1500"></a>

## 194.1 `CONFIG_WIFI_WINC1500`

**提示（Prompt）**：WINC1500 驱动支持［已弃用，DEPRECATED］

**说明（Help）**

此卸载型 Wi-Fi 驱动（offloaded WiFi driver）已弃用，将在后续版本中移除。此官方快照计划在 Zephyr 4.6 中移除该驱动。弃用原因是该驱动已无人维护。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_WINC1500_ENABLED && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_ATMEL_WINC1500
CONFIG_WIFI_OFFLOAD
CONFIG_NET_L2_WIFI_MGMT
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/wifi/winc1500/Kconfig.winc1500:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/winc1500/Kconfig.winc1500#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_ATMEL_WINC1500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATMEL_WINC1500)、[`CONFIG_WIFI_OFFLOAD`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_OFFLOAD)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ATMEL_WINC1500`。

<a id="CONFIG_WIFI_WINC1500_BUF_CTR"></a>

## 194.2 `CONFIG_WIFI_WINC1500_BUF_CTR`

**提示（Prompt）**：每个缓冲区池中的缓冲区数量（buffers per pool）

**说明（Help）**

设置驱动在各缓冲区池（buffer pool）中可访问的缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_WINC1500 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/wifi/winc1500/Kconfig.winc1500:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/winc1500/Kconfig.winc1500#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → WINC1500 驱动支持［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_WINC1500`](P194_drivers_wifi_配置项参考_7.md#CONFIG_WIFI_WINC1500)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_WINC1500_MAX_PACKET_SIZE"></a>

## 194.3 `CONFIG_WIFI_WINC1500_MAX_PACKET_SIZE`

**提示（Prompt）**：数据包最大大小（Maximum size of a packet），单位为字节

**说明（Help）**

设置经过芯片的网络数据包的最大大小。这决定每个缓冲区池（buffer pool）中各缓冲区的大小。除非清楚修改的影响，否则不要更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_WINC1500 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`drivers/wifi/winc1500/Kconfig.winc1500:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/winc1500/Kconfig.winc1500#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → WINC1500 驱动支持［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_WINC1500`](P194_drivers_wifi_配置项参考_7.md#CONFIG_WIFI_WINC1500)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_WINC1500_NAME"></a>

## 194.4 `CONFIG_WIFI_WINC1500_NAME`

**提示（Prompt）**：驱动名称（Driver name）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_WINC1500 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
"WINC1500"
```

**定义位置（Location）**：[`drivers/wifi/winc1500/Kconfig.winc1500:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/winc1500/Kconfig.winc1500#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → WINC1500 驱动支持［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_WINC1500`](P194_drivers_wifi_配置项参考_7.md#CONFIG_WIFI_WINC1500)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_WINC1500_OFFLOAD_MAX_SOCKETS"></a>

## 194.5 `CONFIG_WIFI_WINC1500_OFFLOAD_MAX_SOCKETS`

**提示（Prompt）**：可管理的最大套接字数（sockets）

**说明（Help）**

设置可通过驱动和芯片管理的套接字（sockets）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_WINC1500 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/wifi/winc1500/Kconfig.winc1500:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/winc1500/Kconfig.winc1500#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → WINC1500 驱动支持［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_WINC1500`](P194_drivers_wifi_配置项参考_7.md#CONFIG_WIFI_WINC1500)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_WINC1500_REGION_ASIA"></a>

## 194.6 `CONFIG_WIFI_WINC1500_REGION_ASIA`

**提示（Prompt）**：亚洲地区（Region Asia）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/wifi/winc1500/Kconfig.winc1500:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/winc1500/Kconfig.winc1500#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → WINC1500 驱动支持［已弃用，DEPRECATED］ → 芯片在哪个地区（region）运行？

<a id="CONFIG_WIFI_WINC1500_REGION_EUROPE"></a>

## 194.7 `CONFIG_WIFI_WINC1500_REGION_EUROPE`

**提示（Prompt）**：欧洲地区（Region Europe）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/wifi/winc1500/Kconfig.winc1500:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/winc1500/Kconfig.winc1500#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → WINC1500 驱动支持［已弃用，DEPRECATED］ → 芯片在哪个地区（region）运行？

<a id="CONFIG_WIFI_WINC1500_REGION_NORTH_AMERICA"></a>

## 194.8 `CONFIG_WIFI_WINC1500_REGION_NORTH_AMERICA`

**提示（Prompt）**：北美地区（Region North America）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/wifi/winc1500/Kconfig.winc1500:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/winc1500/Kconfig.winc1500#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → WINC1500 驱动支持［已弃用，DEPRECATED］ → 芯片在哪个地区（region）运行？

<a id="CONFIG_WIFI_WINC1500_THREAD_PRIO"></a>

## 194.9 `CONFIG_WIFI_WINC1500_THREAD_PRIO`

**提示（Prompt）**：硬件抽象层回调处理线程（HAL callback handler thread）优先级

**说明（Help）**

设置处理 WINC1500 硬件抽象层回调（HAL callbacks）的线程优先级。除非清楚修改的影响，否则不要更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_WINC1500 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/wifi/winc1500/Kconfig.winc1500:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/winc1500/Kconfig.winc1500#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → WINC1500 驱动支持［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_WINC1500`](P194_drivers_wifi_配置项参考_7.md#CONFIG_WIFI_WINC1500)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_WINC1500_THREAD_STACK_SIZE"></a>

## 194.10 `CONFIG_WIFI_WINC1500_THREAD_STACK_SIZE`

**提示（Prompt）**：硬件抽象层回调处理线程（HAL callback handler thread）栈大小

**说明（Help）**

设置处理 WINC1500 硬件抽象层回调（HAL callbacks）的线程栈大小。除非清楚修改的影响，否则不要更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_WINC1500 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/wifi/winc1500/Kconfig.winc1500:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/winc1500/Kconfig.winc1500#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → WINC1500 驱动支持［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_WINC1500`](P194_drivers_wifi_配置项参考_7.md#CONFIG_WIFI_WINC1500)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WINC1500_DRV_USE_OLD_SPI_SW"></a>

## 194.11 `CONFIG_WINC1500_DRV_USE_OLD_SPI_SW`

**提示（Prompt）**：在厂商硬件抽象层（vendor HAL）中使用旧版 SPI 访问方式

**说明（Help）**

启用后，将 `USE_OLD_SPI_SW` 设置传递给厂商硬件抽象层（vendor HAL）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_WINC1500 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/winc1500/Kconfig.winc1500:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/winc1500/Kconfig.winc1500#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → WINC1500 驱动支持［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_WINC1500`](P194_drivers_wifi_配置项参考_7.md#CONFIG_WIFI_WINC1500)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WLAN_CALDATA_2ANT_HI_ISO"></a>

## 194.12 `CONFIG_WLAN_CALDATA_2ANT_HI_ISO`

**提示（Prompt）**：选择双天线高隔离度（2ANT HIGH ISOLATION）

**说明（Help）**

选择双天线高隔离度校准数据（2ANT High Isolation Caldata）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_IW61X && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:962`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L962)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WLAN_CALDATA_2ANT_LO_ISO"></a>

## 194.13 `CONFIG_WLAN_CALDATA_2ANT_LO_ISO`

**提示（Prompt）**：选择双天线低隔离度（2ANT LOW ISOLATION）

**说明（Help）**

选择双天线低隔离度校准数据（2ANT Low Isolation Caldata）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_IW61X && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:967`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L967)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<!-- kconfig-navigation -->

[上一章](P193_drivers_wifi_配置项参考_6.md) · [返回大纲](大纲.md) · [下一章](P195_drivers_wuc_配置项参考.md)
