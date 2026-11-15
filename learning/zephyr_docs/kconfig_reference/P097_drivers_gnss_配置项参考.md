---
id: learning.zephyr-docs.kconfig-reference.page-97
title: "`drivers/gnss`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第97章\_`drivers/gnss`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/gnss` 的 47 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_GNSS"></a>

## 97.1 `CONFIG_GNSS`

**提示（Prompt）**：全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**说明（Help）**

启用 GNSS 驱动及配置（Configuration）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_HL78XX_GNSS
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/x_nucleo_gnss1a1/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_gnss1a1/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/gnss/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_HL78XX_GNSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HL78XX_GNSS)。

<a id="CONFIG_GNSS_DUMP"></a>

## 97.2 `CONFIG_GNSS_DUMP`

**提示（Prompt）**：GNSS 转储支持（Dump Support）

**说明（Help）**

启用 GNSS 转储库（Dump Library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_GNSS
```

**被选择（Selected by）**

```text
CONFIG_GNSS_DUMP_TO_LOG
```

**定义位置（Location）**：[`drivers/gnss/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_DUMP_TO_LOG`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_DUMP_TO_LOG)。

<a id="CONFIG_GNSS_DUMP_TO_LOG"></a>

## 97.3 `CONFIG_GNSS_DUMP_TO_LOG`

**提示（Prompt）**：将 GNSS 事件转储到日志（Dump Events to Log）

**说明（Help）**

启用将 GNSS 信息转储到日志（Dump to Log）的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS
```

**主动选择（Selects）**

```text
CONFIG_GNSS_DUMP
```

**定义位置（Location）**：[`drivers/gnss/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_DUMP`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_DUMP)。

<a id="CONFIG_GNSS_DUMP_TO_LOG_BUF_SIZE"></a>

## 97.4 `CONFIG_GNSS_DUMP_TO_LOG_BUF_SIZE`

**提示（Prompt）**：GNSS 日志转储缓冲区大小（Log Dump Buffer Size）

**说明（Help）**

GNSS 日志转储缓冲区（Log Dump Buffer）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_DUMP_TO_LOG && CONFIG_GNSS
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/gnss/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → 将 GNSS 事件转储到日志（Dump Events to Log）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_DUMP_TO_LOG`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_DUMP_TO_LOG)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)。

<a id="CONFIG_GNSS_EMUL"></a>

## 97.5 `CONFIG_GNSS_EMUL`

**提示（Prompt）**：仿真 GNSS 驱动（Emulated GNSS Driver）

**说明（Help）**

启用仿真 GNSS 驱动（Emulated GNSS Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_GNSS_EMUL_ENABLED && CONFIG_GNSS_REFERENCE_FRAME_WGS84 && CONFIG_GNSS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TIMEOUT_64BIT
```

**定义位置（Location）**：[`drivers/gnss/Kconfig.emul:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig.emul#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS_REFERENCE_FRAME_WGS84`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_REFERENCE_FRAME_WGS84)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_TIMEOUT_64BIT`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_64BIT)。

<a id="CONFIG_GNSS_EMUL_MANUAL_UPDATE"></a>

## 97.6 `CONFIG_GNSS_EMUL_MANUAL_UPDATE`

**提示（Prompt）**：通过 `gnss_emul_set_data` 手动更新内部状态（Internal State）

**说明（Help）**

GNSS 仿真器（Emulator）的内部状态，例如位置、时间等，必须通过 `gnss_emul_set_data` 更新，而不再在写死的时刻自动转换到写死的状态。一旦设置了当前时间，发布的时间就会自动递增。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_EMUL && CONFIG_GNSS
```

**定义位置（Location）**：[`drivers/gnss/Kconfig.emul:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig.emul#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → 仿真 GNSS 驱动（Emulated GNSS Driver）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_EMUL`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_EMUL)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)。

<a id="CONFIG_GNSS_ERICSSON_F5521GW"></a>

## 97.7 `CONFIG_GNSS_ERICSSON_F5521GW`

**提示（Prompt）**：Ericsson F5521gw GNSS 驱动

**说明（Help）**

爱立信（Ericsson）F5521gw（HP HS2340）无线广域网（WWAN）模块的 GNSS 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS && DT_HAS_ERICSSON_F5521GW_ENABLED && CONFIG_GNSS_REFERENCE_FRAME_WGS84 && CONFIG_GNSS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MODEM_MODULES
CONFIG_MODEM_BACKEND_UART
CONFIG_MODEM_CHAT
CONFIG_GNSS_PARSE
CONFIG_GNSS_NMEA0183
CONFIG_GNSS_NMEA0183_MATCH
```

**定义位置（Location）**：[`drivers/gnss/Kconfig.ericsson_f5521gw:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig.ericsson_f5521gw#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_REFERENCE_FRAME_WGS84`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_REFERENCE_FRAME_WGS84)、[`CONFIG_MODEM_MODULES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_BACKEND_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_MODEM_CHAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CHAT)、[`CONFIG_GNSS_PARSE`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_PARSE)、[`CONFIG_GNSS_NMEA0183`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA0183)、[`CONFIG_GNSS_NMEA0183_MATCH`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA0183_MATCH)。

<a id="CONFIG_GNSS_ERICSSON_F5521GW_SATELLITES_COUNT"></a>

## 97.8 `CONFIG_GNSS_ERICSSON_F5521GW_SATELLITES_COUNT`

**提示（Prompt）**：最大卫星数量（Maximum Satellite Count）

**说明（Help）**

驱动可从 GNSS 设备解码的最大卫星数量（Maximum Satellite Count）。这不影响设备实际跟踪的卫星数量，只限制卫星回调（Satellites Callback）中能够报告其中多少颗。

> 译注：原文描述实际跟踪数量时写为 `devices`（设备），本条上下文讨论的是卫星数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_SATELLITES && CONFIG_GNSS_ERICSSON_F5521GW && CONFIG_GNSS
```

**默认值（Defaults）**

```text
24
```

**定义位置（Location）**：[`drivers/gnss/Kconfig.ericsson_f5521gw:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig.ericsson_f5521gw#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → Ericsson F5521gw GNSS 驱动

**配置项引用（Symbol References）**：[`CONFIG_GNSS_SATELLITES`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_SATELLITES)、[`CONFIG_GNSS_ERICSSON_F5521GW`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_ERICSSON_F5521GW)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)。

<a id="CONFIG_GNSS_GLOBALTOP_PA6H"></a>

## 97.9 `CONFIG_GNSS_GLOBALTOP_PA6H`

**提示（Prompt）**：GlobalTop PA6H GNSS 设备

**说明（Help）**

启用 GlobalTop PA6H GNSS 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS && DT_HAS_GLOBALTOP_PA6H_ENABLED && CONFIG_GNSS_REFERENCE_FRAME_WGS84 && CONFIG_GNSS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MODEM_MODULES
CONFIG_MODEM_BACKEND_UART
CONFIG_MODEM_CHAT
CONFIG_GNSS_PARSE
CONFIG_GNSS_NMEA0183
CONFIG_GNSS_NMEA0183_MATCH
```

**定义位置（Location）**：[`drivers/gnss/Kconfig.globaltop_pa6h:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig.globaltop_pa6h#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_REFERENCE_FRAME_WGS84`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_REFERENCE_FRAME_WGS84)、[`CONFIG_MODEM_MODULES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_BACKEND_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_MODEM_CHAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CHAT)、[`CONFIG_GNSS_PARSE`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_PARSE)、[`CONFIG_GNSS_NMEA0183`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA0183)、[`CONFIG_GNSS_NMEA0183_MATCH`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA0183_MATCH)。

<a id="CONFIG_GNSS_GLOBALTOP_PA6H_SATELLITES_COUNT"></a>

## 97.10 `CONFIG_GNSS_GLOBALTOP_PA6H_SATELLITES_COUNT`

**提示（Prompt）**：最大卫星数量（Maximum Satellite Count）

**说明（Help）**

可从 GNSS 设备解码的最大卫星数量（Maximum Satellite Count）。这不影响设备实际跟踪的卫星数量，只限制卫星回调（Satellites Callback）中能够报告其中多少颗。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_SATELLITES && CONFIG_GNSS_SATELLITES && CONFIG_GNSS_GLOBALTOP_PA6H && CONFIG_GNSS
```

**默认值（Defaults）**

```text
22
```

**定义位置（Location）**：[`drivers/gnss/Kconfig.globaltop_pa6h:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig.globaltop_pa6h#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → GlobalTop PA6H GNSS 设备

**配置项引用（Symbol References）**：[`CONFIG_GNSS_SATELLITES`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_SATELLITES)、[`CONFIG_GNSS_GLOBALTOP_PA6H`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_GLOBALTOP_PA6H)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)。

<a id="CONFIG_GNSS_INIT_PRIORITY"></a>

## 97.11 `CONFIG_GNSS_INIT_PRIORITY`

**提示（Prompt）**：GNSS 驱动初始化优先级（Initialization Priority）

**说明（Help）**

GNSS 驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS
```

**默认值（Defaults）**

```text
80
```

**取值范围（Ranges）**

```text
[0, 99]
```

**定义位置（Location）**：[`drivers/gnss/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)。

<a id="CONFIG_GNSS_LUATOS_AIR530Z"></a>

## 97.12 `CONFIG_GNSS_LUATOS_AIR530Z`

**提示（Prompt）**：Luatos Air530z GNSS 设备

**说明（Help）**

启用 Luatos Air530z GNSS 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS && DT_HAS_LUATOS_AIR530Z_ENABLED && CONFIG_GNSS_REFERENCE_FRAME_WGS84 && CONFIG_GNSS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MODEM_MODULES
CONFIG_MODEM_BACKEND_UART
CONFIG_MODEM_CHAT
CONFIG_GNSS_PARSE
CONFIG_GNSS_NMEA0183
CONFIG_GNSS_NMEA0183_MATCH
```

**定义位置（Location）**：[`drivers/gnss/Kconfig.luatos_air530z:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig.luatos_air530z#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_REFERENCE_FRAME_WGS84`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_REFERENCE_FRAME_WGS84)、[`CONFIG_MODEM_MODULES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_BACKEND_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_MODEM_CHAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CHAT)、[`CONFIG_GNSS_PARSE`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_PARSE)、[`CONFIG_GNSS_NMEA0183`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA0183)、[`CONFIG_GNSS_NMEA0183_MATCH`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA0183_MATCH)。

<a id="CONFIG_GNSS_LUATOS_AIR530Z_SATELLITES_COUNT"></a>

## 97.13 `CONFIG_GNSS_LUATOS_AIR530Z_SATELLITES_COUNT`

**提示（Prompt）**：最大卫星数量（Maximum Satellite Count）

**说明（Help）**

可从 GNSS 设备解码的最大卫星数量（Maximum Satellite Count）。这不影响设备实际跟踪的卫星数量，只限制卫星回调（Satellites Callback）中能够报告其中多少颗。

> 译注：原文描述实际跟踪数量时写为 `devices`（设备），本条上下文讨论的是卫星数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_SATELLITES && CONFIG_GNSS_LUATOS_AIR530Z && CONFIG_GNSS
```

**默认值（Defaults）**

```text
24
```

**定义位置（Location）**：[`drivers/gnss/Kconfig.luatos_air530z:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig.luatos_air530z#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → Luatos Air530z GNSS 设备

**配置项引用（Symbol References）**：[`CONFIG_GNSS_SATELLITES`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_SATELLITES)、[`CONFIG_GNSS_LUATOS_AIR530Z`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_LUATOS_AIR530Z)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)。

<a id="CONFIG_GNSS_NMEA0183"></a>

## 97.14 `CONFIG_GNSS_NMEA0183`

**提示（Prompt）**：NMEA 0183 解析工具（Parsing Utilities）

**说明（Help）**

启用 NMEA 0183 解析工具（Parsing Utilities）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS
```

**主动选择（Selects）**

```text
CONFIG_GNSS_PARSE
```

**被选择（Selected by）**

```text
CONFIG_GNSS_NMEA0183_MATCH
CONFIG_GNSS_ERICSSON_F5521GW
CONFIG_GNSS_NMEA_GENERIC
CONFIG_GNSS_GLOBALTOP_PA6H
CONFIG_GNSS_LUATOS_AIR530Z
CONFIG_GNSS_QUECTEL_LCX6G
CONFIG_HL78XX_GNSS
```

**定义位置（Location）**：[`drivers/gnss/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_PARSE`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_PARSE)、[`CONFIG_GNSS_NMEA0183_MATCH`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA0183_MATCH)、[`CONFIG_GNSS_ERICSSON_F5521GW`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_ERICSSON_F5521GW)、[`CONFIG_GNSS_NMEA_GENERIC`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA_GENERIC)、[`CONFIG_GNSS_GLOBALTOP_PA6H`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_GLOBALTOP_PA6H)、[`CONFIG_GNSS_LUATOS_AIR530Z`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_LUATOS_AIR530Z)、[`CONFIG_GNSS_QUECTEL_LCX6G`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_QUECTEL_LCX6G)、[`CONFIG_HL78XX_GNSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HL78XX_GNSS)。

<a id="CONFIG_GNSS_NMEA0183_MATCH"></a>

## 97.15 `CONFIG_GNSS_NMEA0183_MATCH`

**提示（Prompt）**：GNSS NMEA 0183 匹配工具（Match Utilities）

**说明（Help）**

启用 NMEA 0183 匹配工具（Match Utilities）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS
```

**主动选择（Selects）**

```text
CONFIG_GNSS_NMEA0183
```

**被选择（Selected by）**

```text
CONFIG_GNSS_ERICSSON_F5521GW
CONFIG_GNSS_NMEA_GENERIC
CONFIG_GNSS_GLOBALTOP_PA6H
CONFIG_GNSS_LUATOS_AIR530Z
CONFIG_GNSS_QUECTEL_LCX6G
CONFIG_HL78XX_GNSS
```

**定义位置（Location）**：[`drivers/gnss/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_NMEA0183`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA0183)、[`CONFIG_GNSS_ERICSSON_F5521GW`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_ERICSSON_F5521GW)、[`CONFIG_GNSS_NMEA_GENERIC`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA_GENERIC)、[`CONFIG_GNSS_GLOBALTOP_PA6H`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_GLOBALTOP_PA6H)、[`CONFIG_GNSS_LUATOS_AIR530Z`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_LUATOS_AIR530Z)、[`CONFIG_GNSS_QUECTEL_LCX6G`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_QUECTEL_LCX6G)、[`CONFIG_HL78XX_GNSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HL78XX_GNSS)。

<a id="CONFIG_GNSS_NMEA_GENERIC"></a>

## 97.16 `CONFIG_GNSS_NMEA_GENERIC`

**提示（Prompt）**：通用 GNSS NMEA 设备（Generic Device）

**说明（Help）**

基于 NMEA 的通用 GNSS 设备（Generic GNSS Device）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS && DT_HAS_GNSS_NMEA_GENERIC_ENABLED && CONFIG_GNSS_REFERENCE_FRAME_WGS84 && CONFIG_GNSS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MODEM_MODULES
CONFIG_MODEM_BACKEND_UART
CONFIG_MODEM_CHAT
CONFIG_GNSS_PARSE
CONFIG_GNSS_NMEA0183
CONFIG_GNSS_NMEA0183_MATCH
```

**定义位置（Location）**：[`drivers/gnss/Kconfig.generic:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig.generic#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_REFERENCE_FRAME_WGS84`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_REFERENCE_FRAME_WGS84)、[`CONFIG_MODEM_MODULES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_BACKEND_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_MODEM_CHAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CHAT)、[`CONFIG_GNSS_PARSE`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_PARSE)、[`CONFIG_GNSS_NMEA0183`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA0183)、[`CONFIG_GNSS_NMEA0183_MATCH`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA0183_MATCH)。

<a id="CONFIG_GNSS_NMEA_GENERIC_SATELLITES_COUNT"></a>

## 97.17 `CONFIG_GNSS_NMEA_GENERIC_SATELLITES_COUNT`

**提示（Prompt）**：最大卫星数量（Maximum Satellite Count）

**说明（Help）**

驱动可从 GNSS 设备解码的最大卫星数量（Maximum Satellite Count）。这不影响设备实际跟踪的卫星数量，只限制卫星回调（Satellites Callback）中能够报告其中多少颗。

> 译注：原文描述实际跟踪数量时写为 `devices`（设备），本条上下文讨论的是卫星数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_SATELLITES && CONFIG_GNSS_NMEA_GENERIC && CONFIG_GNSS
```

**默认值（Defaults）**

```text
24
```

**定义位置（Location）**：[`drivers/gnss/Kconfig.generic:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig.generic#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → 通用 GNSS NMEA 设备（Generic Device）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_SATELLITES`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_SATELLITES)、[`CONFIG_GNSS_NMEA_GENERIC`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA_GENERIC)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)。

<a id="CONFIG_GNSS_PARSE"></a>

## 97.18 `CONFIG_GNSS_PARSE`

**提示（Prompt）**：GNSS 解析工具（Parsing Utilities）

**说明（Help）**

启用 GNSS 解析工具（Parsing Utilities）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS
```

**被选择（Selected by）**

```text
CONFIG_GNSS_NMEA0183
CONFIG_GNSS_ERICSSON_F5521GW
CONFIG_GNSS_NMEA_GENERIC
CONFIG_GNSS_GLOBALTOP_PA6H
CONFIG_GNSS_LUATOS_AIR530Z
CONFIG_GNSS_QUECTEL_LCX6G
CONFIG_GNSS_U_BLOX_M10
CONFIG_GNSS_U_BLOX_M8
```

**定义位置（Location）**：[`drivers/gnss/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_NMEA0183`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA0183)、[`CONFIG_GNSS_ERICSSON_F5521GW`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_ERICSSON_F5521GW)、[`CONFIG_GNSS_NMEA_GENERIC`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA_GENERIC)、[`CONFIG_GNSS_GLOBALTOP_PA6H`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_GLOBALTOP_PA6H)、[`CONFIG_GNSS_LUATOS_AIR530Z`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_LUATOS_AIR530Z)、[`CONFIG_GNSS_QUECTEL_LCX6G`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_QUECTEL_LCX6G)、[`CONFIG_GNSS_U_BLOX_M10`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10)、[`CONFIG_GNSS_U_BLOX_M8`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M8)。

<a id="CONFIG_GNSS_QUECTEL_LCX6G"></a>

## 97.19 `CONFIG_GNSS_QUECTEL_LCX6G`

**提示（Prompt）**：移远（Quectel）LCX6G GNSS 调制解调器驱动（Modem Driver）

**说明（Help）**

启用移远（Quectel）LCX6G 系列 GNSS 调制解调器驱动（Modem Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS && (DT_HAS_QUECTEL_LC26G_ENABLED || DT_HAS_QUECTEL_LC76G_ENABLED || DT_HAS_QUECTEL_LC86G_ENABLED) && CONFIG_GNSS_REFERENCE_FRAME_WGS84 && CONFIG_GNSS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MODEM_MODULES
CONFIG_MODEM_BACKEND_UART
CONFIG_MODEM_CHAT
CONFIG_GNSS_PARSE
CONFIG_GNSS_NMEA0183
CONFIG_GNSS_NMEA0183_MATCH
```

**定义位置（Location）**：[`drivers/gnss/Kconfig.quectel_lcx6g:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig.quectel_lcx6g#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_REFERENCE_FRAME_WGS84`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_REFERENCE_FRAME_WGS84)、[`CONFIG_MODEM_MODULES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_BACKEND_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_MODEM_CHAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CHAT)、[`CONFIG_GNSS_PARSE`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_PARSE)、[`CONFIG_GNSS_NMEA0183`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA0183)、[`CONFIG_GNSS_NMEA0183_MATCH`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA0183_MATCH)。

<a id="CONFIG_GNSS_QUECTEL_LCX6G_SAT_ARRAY_SIZE"></a>

## 97.20 `CONFIG_GNSS_QUECTEL_LCX6G_SAT_ARRAY_SIZE`

**提示（Prompt）**：GNSS 卫星数组大小（Satellites Array Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_SATELLITES && CONFIG_GNSS_QUECTEL_LCX6G && CONFIG_GNSS
```

**默认值（Defaults）**

```text
24
```

**定义位置（Location）**：[`drivers/gnss/Kconfig.quectel_lcx6g:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig.quectel_lcx6g#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → 移远（Quectel）LCX6G GNSS 调制解调器驱动（Modem Driver）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_SATELLITES`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_SATELLITES)、[`CONFIG_GNSS_QUECTEL_LCX6G`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_QUECTEL_LCX6G)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)。

<a id="CONFIG_GNSS_QUECTEL_LCX6G_UART_RX_BUF_SIZE"></a>

## 97.21 `CONFIG_GNSS_QUECTEL_LCX6G_UART_RX_BUF_SIZE`

**提示（Prompt）**：UART 后端接收缓冲区大小（Backend Receive Buffer Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_QUECTEL_LCX6G && CONFIG_GNSS
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/gnss/Kconfig.quectel_lcx6g:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig.quectel_lcx6g#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → 移远（Quectel）LCX6G GNSS 调制解调器驱动（Modem Driver）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_QUECTEL_LCX6G`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_QUECTEL_LCX6G)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)。

<a id="CONFIG_GNSS_QUECTEL_LCX6G_UART_TX_BUF_SIZE"></a>

## 97.22 `CONFIG_GNSS_QUECTEL_LCX6G_UART_TX_BUF_SIZE`

**提示（Prompt）**：UART 后端发送缓冲区大小（Backend Transmit Buffer Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_QUECTEL_LCX6G && CONFIG_GNSS
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`drivers/gnss/Kconfig.quectel_lcx6g:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig.quectel_lcx6g#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → 移远（Quectel）LCX6G GNSS 调制解调器驱动（Modem Driver）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_QUECTEL_LCX6G`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_QUECTEL_LCX6G)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)。

<a id="CONFIG_GNSS_REFERENCE_FRAME"></a>

## 97.23 `CONFIG_GNSS_REFERENCE_FRAME`

**提示（Prompt）**：GNSS 参考框架基准（Reference Frame Datum）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS
```

**默认值（Defaults）**

```text
CONFIG_GNSS_REFERENCE_FRAME_WGS84
```

**可选项（Choices）**

```text
CONFIG_GNSS_REFERENCE_FRAME_WGS84
```

**定义位置（Location）**：[`drivers/gnss/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_REFERENCE_FRAME_WGS84`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_REFERENCE_FRAME_WGS84)。

<a id="CONFIG_GNSS_REFERENCE_FRAME_WGS84"></a>

## 97.24 `CONFIG_GNSS_REFERENCE_FRAME_WGS84`

**提示（Prompt）**：使用 WGS84 椭球体（Ellipsoid）作为参考框架基准（Reference Frame Datum）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_REFERENCE_FRAME>
```

**定义位置（Location）**：[`drivers/gnss/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → GNSS 参考框架基准（Reference Frame Datum）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_REFERENCE_FRAME`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_REFERENCE_FRAME)。

<a id="CONFIG_GNSS_SATELLITES"></a>

## 97.25 `CONFIG_GNSS_SATELLITES`

**提示（Prompt）**：GNSS 卫星支持（Satellites Support）

**说明（Help）**

启用 GNSS 卫星回调（Satellites Callback）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS
```

**定义位置（Location）**：[`drivers/gnss/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)。

<a id="CONFIG_GNSS_U_BLOX"></a>

## 97.26 `CONFIG_GNSS_U_BLOX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项（Hidden Option），用于启用 GNSS u-blox 通用配置（Common Configuration）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS
```

**被选择（Selected by）**

```text
CONFIG_GNSS_U_BLOX_F9P
CONFIG_GNSS_U_BLOX_M10
CONFIG_GNSS_U_BLOX_M8
```

**定义位置（Location）**：[`drivers/gnss/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_U_BLOX_F9P`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P)、[`CONFIG_GNSS_U_BLOX_M10`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10)、[`CONFIG_GNSS_U_BLOX_M8`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M8)。

<a id="CONFIG_GNSS_U_BLOX_F9P"></a>

## 97.27 `CONFIG_GNSS_U_BLOX_F9P`

**提示（Prompt）**：u-blox F9P 高精度 GNSS 模块（High-Precision GNSS Module）

**说明（Help）**

启用 u-blox F9P 高精度 GNSS 调制解调器驱动（Modem Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS && DT_HAS_U_BLOX_F9P_ENABLED && CONFIG_GNSS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MODEM_MODULES
CONFIG_MODEM_BACKEND_UART
CONFIG_GNSS_U_BLOX
CONFIG_GNSS_U_BLOX_PROTOCOL
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_f9p:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_f9p#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_MODEM_MODULES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_BACKEND_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_GNSS_U_BLOX`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX)、[`CONFIG_GNSS_U_BLOX_PROTOCOL`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_PROTOCOL)。

<a id="CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN"></a>

## 97.28 `CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN`

**提示（Prompt）**：高动态模式设置（High Dynamics Mode Setting）

**说明（Help）**

根据应用场景选择高动态导航模式（High Dynamics Navigation Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_U_BLOX_F9P && CONFIG_GNSS
```

**默认值（Defaults）**

```text
CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_2G
```

**可选项（Choices）**

```text
CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_1G
CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_2G
CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_4G
CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AUTOMOTIVE
CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_SEA
CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_BIKE
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_f9p:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_f9p#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → u-blox F9P 高精度 GNSS 模块（High-Precision GNSS Module）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_U_BLOX_F9P`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_2G`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_2G)、[`CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_1G`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_1G)、[`CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_4G`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_4G)、[`CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AUTOMOTIVE`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AUTOMOTIVE)、[`CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_SEA`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_SEA)、[`CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_BIKE`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_BIKE)。

<a id="CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_1G"></a>

## 97.29 `CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_1G`

**提示（Prompt）**：将高动态模式设为 1G 航空模式（1G Airborne）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN>
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_f9p:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_f9p#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → u-blox F9P 高精度 GNSS 模块（High-Precision GNSS Module） → 高动态模式设置（High Dynamics Mode Setting）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN)。

<a id="CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_2G"></a>

## 97.30 `CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_2G`

**提示（Prompt）**：将高动态模式设为 2G 航空模式（2G Airborne）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN>
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_f9p:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_f9p#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → u-blox F9P 高精度 GNSS 模块（High-Precision GNSS Module） → 高动态模式设置（High Dynamics Mode Setting）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN)。

<a id="CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_4G"></a>

## 97.31 `CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AIRBORNE_4G`

**提示（Prompt）**：将高动态模式设为 4G 航空模式（4G Airborne）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN>
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_f9p:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_f9p#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → u-blox F9P 高精度 GNSS 模块（High-Precision GNSS Module） → 高动态模式设置（High Dynamics Mode Setting）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN)。

<a id="CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AUTOMOTIVE"></a>

## 97.32 `CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_AUTOMOTIVE`

**提示（Prompt）**：将高动态模式设为汽车模式（Automotive Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN>
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_f9p:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_f9p#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → u-blox F9P 高精度 GNSS 模块（High-Precision GNSS Module） → 高动态模式设置（High Dynamics Mode Setting）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN)。

<a id="CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_BIKE"></a>

## 97.33 `CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_BIKE`

**提示（Prompt）**：将高动态模式设为骑行模式（Bike Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN>
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_f9p:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_f9p#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → u-blox F9P 高精度 GNSS 模块（High-Precision GNSS Module） → 高动态模式设置（High Dynamics Mode Setting）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN)。

<a id="CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_SEA"></a>

## 97.34 `CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN_SEA`

**提示（Prompt）**：将高动态模式设为海上模式（Sea Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN>
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_f9p:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_f9p#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → u-blox F9P 高精度 GNSS 模块（High-Precision GNSS Module） → 高动态模式设置（High Dynamics Mode Setting）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P_NAV_MODE_HIGH_DYN)。

<a id="CONFIG_GNSS_U_BLOX_F9P_RTK"></a>

## 97.35 `CONFIG_GNSS_U_BLOX_F9P_RTK`

**提示（Prompt）**：使用实时动态定位（RTK）提高定位精度（Fix Accuracy）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_RTK_PROTOCOL_RTCM3 && CONFIG_GNSS_RTK && CONFIG_GNSS_U_BLOX_F9P && CONFIG_GNSS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_f9p:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_f9p#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → u-blox F9P 高精度 GNSS 模块（High-Precision GNSS Module）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_RTK_PROTOCOL_RTCM3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GNSS_RTK_PROTOCOL_RTCM3)、[`CONFIG_GNSS_RTK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GNSS_RTK)、[`CONFIG_GNSS_U_BLOX_F9P`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)。

<a id="CONFIG_GNSS_U_BLOX_M10"></a>

## 97.36 `CONFIG_GNSS_U_BLOX_M10`

**提示（Prompt）**：u-blox M10 GNSS 模块（Module）

**说明（Help）**

启用 u-blox M10 GNSS 调制解调器驱动（Modem Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS && DT_HAS_U_BLOX_M10_ENABLED && CONFIG_GNSS_REFERENCE_FRAME_WGS84 && CONFIG_GNSS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MODEM_MODULES
CONFIG_MODEM_BACKEND_UART
CONFIG_GNSS_PARSE
CONFIG_GNSS_U_BLOX
CONFIG_GNSS_U_BLOX_PROTOCOL
CONFIG_UART_USE_RUNTIME_CONFIGURE
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_m10:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_m10#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_REFERENCE_FRAME_WGS84`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_REFERENCE_FRAME_WGS84)、[`CONFIG_MODEM_MODULES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_BACKEND_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_GNSS_PARSE`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_PARSE)、[`CONFIG_GNSS_U_BLOX`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX)、[`CONFIG_GNSS_U_BLOX_PROTOCOL`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_PROTOCOL)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_USE_RUNTIME_CONFIGURE)。

<a id="CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN"></a>

## 97.37 `CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN`

**提示（Prompt）**：高动态模式设置（High Dynamics Mode Setting）

**说明（Help）**

根据应用场景选择高动态导航模式（High Dynamics Navigation Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_U_BLOX_M10 && CONFIG_GNSS
```

**默认值（Defaults）**

```text
CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_2G
```

**可选项（Choices）**

```text
CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_1G
CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_2G
CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_4G
CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AUTOMOTIVE
CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_SEA
CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_BIKE
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_m10:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_m10#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → u-blox M10 GNSS 模块（Module）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_U_BLOX_M10`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_2G`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_2G)、[`CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_1G`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_1G)、[`CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_4G`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_4G)、[`CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AUTOMOTIVE`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AUTOMOTIVE)、[`CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_SEA`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_SEA)、[`CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_BIKE`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_BIKE)。

<a id="CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_1G"></a>

## 97.38 `CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_1G`

**提示（Prompt）**：将高动态模式设为 1G 航空模式（1G Airborne）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN>
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_m10:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_m10#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → u-blox M10 GNSS 模块（Module） → 高动态模式设置（High Dynamics Mode Setting）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN)。

<a id="CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_2G"></a>

## 97.39 `CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_2G`

**提示（Prompt）**：将高动态模式设为 2G 航空模式（2G Airborne）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN>
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_m10:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_m10#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → u-blox M10 GNSS 模块（Module） → 高动态模式设置（High Dynamics Mode Setting）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN)。

<a id="CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_4G"></a>

## 97.40 `CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AIRBORNE_4G`

**提示（Prompt）**：将高动态模式设为 4G 航空模式（4G Airborne）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN>
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_m10:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_m10#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → u-blox M10 GNSS 模块（Module） → 高动态模式设置（High Dynamics Mode Setting）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN)。

<a id="CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AUTOMOTIVE"></a>

## 97.41 `CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_AUTOMOTIVE`

**提示（Prompt）**：将高动态模式设为汽车模式（Automotive Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN>
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_m10:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_m10#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → u-blox M10 GNSS 模块（Module） → 高动态模式设置（High Dynamics Mode Setting）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN)。

<a id="CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_BIKE"></a>

## 97.42 `CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_BIKE`

**提示（Prompt）**：将高动态模式设为骑行模式（Bike Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN>
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_m10:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_m10#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → u-blox M10 GNSS 模块（Module） → 高动态模式设置（High Dynamics Mode Setting）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN)。

<a id="CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_SEA"></a>

## 97.43 `CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN_SEA`

**提示（Prompt）**：将高动态模式设为海上模式（Sea Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN>
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_m10:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_m10#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → u-blox M10 GNSS 模块（Module） → 高动态模式设置（High Dynamics Mode Setting）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10_NAV_MODE_HIGH_DYN)。

<a id="CONFIG_GNSS_U_BLOX_M8"></a>

## 97.44 `CONFIG_GNSS_U_BLOX_M8`

**提示（Prompt）**：u-blox M8 GNSS 模块（Module）

**说明（Help）**

启用 u-blox M8 GNSS 调制解调器驱动（Modem Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS && DT_HAS_U_BLOX_M8_ENABLED && CONFIG_GNSS_REFERENCE_FRAME_WGS84 && CONFIG_GNSS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MODEM_MODULES
CONFIG_MODEM_BACKEND_UART
CONFIG_GNSS_PARSE
CONFIG_GNSS_U_BLOX
CONFIG_GNSS_U_BLOX_PROTOCOL
CONFIG_UART_USE_RUNTIME_CONFIGURE
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_m8:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_m8#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_REFERENCE_FRAME_WGS84`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_REFERENCE_FRAME_WGS84)、[`CONFIG_MODEM_MODULES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_BACKEND_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_GNSS_PARSE`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_PARSE)、[`CONFIG_GNSS_U_BLOX`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX)、[`CONFIG_GNSS_U_BLOX_PROTOCOL`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_PROTOCOL)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_USE_RUNTIME_CONFIGURE)。

<a id="CONFIG_GNSS_U_BLOX_PROTOCOL"></a>

## 97.45 `CONFIG_GNSS_U_BLOX_PROTOCOL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项（Hidden Option），用于启用 GNSS u-blox 协议（Protocol）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS
```

**主动选择（Selects）**

```text
CONFIG_MODEM_UBX
```

**被选择（Selected by）**

```text
CONFIG_GNSS_U_BLOX_F9P
CONFIG_GNSS_U_BLOX_M10
CONFIG_GNSS_U_BLOX_M8
```

**定义位置（Location）**：[`drivers/gnss/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_MODEM_UBX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_UBX)、[`CONFIG_GNSS_U_BLOX_F9P`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P)、[`CONFIG_GNSS_U_BLOX_M10`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10)、[`CONFIG_GNSS_U_BLOX_M8`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M8)。

<a id="CONFIG_GNSS_U_BLOX_RESET_ON_INIT"></a>

## 97.46 `CONFIG_GNSS_U_BLOX_RESET_ON_INIT`

**提示（Prompt）**：初始化时使用复位引脚（Reset Pin）复位 GNSS

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_U_BLOX && CONFIG_GNSS
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_common:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_common#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS_U_BLOX`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)。

<a id="CONFIG_GNSS_U_BLOX_SATELLITES_COUNT"></a>

## 97.47 `CONFIG_GNSS_U_BLOX_SATELLITES_COUNT`

**提示（Prompt）**：u-blox 最大卫星数量（Maximum Satellite Count）

**说明（Help）**

u-blox 驱动能够解码的最大卫星数量（Maximum Satellite Count）。这不影响设备实际跟踪的卫星数量，只限制卫星回调（Satellites Callback）中报告的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_SATELLITES && CONFIG_GNSS_U_BLOX && CONFIG_GNSS
```

**默认值（Defaults）**

```text
24
```

**定义位置（Location）**：[`drivers/gnss/u_blox/Kconfig.u_blox_common:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gnss/u_blox/Kconfig.u_blox_common#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_GNSS_SATELLITES`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_SATELLITES)、[`CONFIG_GNSS_U_BLOX`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)。

<!-- kconfig-navigation -->

[上一章](P096_drivers_fuel_gauge_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P098_drivers_gpio_配置项参考_1.md)
