---
id: learning.zephyr-docs.kconfig-reference.page-125
title: "`drivers/modem`配置项参考（1/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第125章\_`drivers/modem`配置项参考（1/4）

本章翻译官方 Kconfig 数据库中 `drivers/modem` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BC66X_INIT_DELAY"></a>

## 125.1 `CONFIG_BC66X_INIT_DELAY`

**提示（Prompt）**：驱动初始化延迟（Initialization Delay，毫秒）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1200
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_BC66X_INIT_RETRIES"></a>

## 125.2 `CONFIG_BC66X_INIT_RETRIES`

**提示（Prompt）**：初始化重试次数（Initialization Retries）

**说明（Help）**

重试调制解调器初始化的次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_BC66X_INIT_TIMEOUT"></a>

## 125.3 `CONFIG_BC66X_INIT_TIMEOUT`

**提示（Prompt）**：驱动初始化超时（Initialization Timeout，秒）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_BC66X_WAIT_FOR_HW_DELAY"></a>

## 125.4 `CONFIG_BC66X_WAIT_FOR_HW_DELAY`

**提示（Prompt）**：等待硬件的延迟（Hardware Delay，毫秒）

**说明（Help）**

开始通信前，等待调制解调器硬件完成上电的延迟时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2500
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/quectel/bc66x/Kconfig.quectel-bc66x#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_AT_MONITOR"></a>

## 125.5 `CONFIG_HL78XX_AT_MONITOR`

**提示（Prompt）**：HL78XX 已解析 AT 监视器（Parsed AT Monitor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/hl78xx_at_monitor/Kconfig.hl78xx_at_monitor:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/hl78xx_at_monitor/Kconfig.hl78xx_at_monitor#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_AT_MONITOR_HEAP_SIZE"></a>

## 125.6 `CONFIG_HL78XX_AT_MONITOR_HEAP_SIZE`

**提示（Prompt）**：延后处理的 AT 通知堆大小（Deferred AT Notification Heap Size）

**说明（Help）**

复制并排队已解析的主动 AT 通知（Unsolicited AT Notification）所用堆大小，用于在系统工作队列中延后分发给监视器。运行时监视器快照分发（Runtime Monitor Snapshot Dispatch）不使用此堆。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_AT_MONITOR && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
512
```

**取值范围（Ranges）**

```text
[64, 4096]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/hl78xx_at_monitor/Kconfig.hl78xx_at_monitor:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/hl78xx_at_monitor/Kconfig.hl78xx_at_monitor#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX 已解析 AT 监视器（Parsed AT Monitor）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_AT_MONITOR`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_AT_MONITOR)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_AT_MONITOR_MAX_INSTANCE_MONITORS"></a>

## 125.7 `CONFIG_HL78XX_AT_MONITOR_MAX_INSTANCE_MONITORS`

**提示（Prompt）**：运行时 HL78xx AT 监视器最大数量

**说明（Help）**

可注册的运行时 AT 监视器最大数量。此上限使 AT 监视器分发能够在不分配内存的情况下，对运行时监视器生成快照。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_AT_MONITOR && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/hl78xx_at_monitor/Kconfig.hl78xx_at_monitor:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/hl78xx_at_monitor/Kconfig.hl78xx_at_monitor#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX 已解析 AT 监视器（Parsed AT Monitor）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_AT_MONITOR`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_AT_MONITOR)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_EVT_MONITOR"></a>

## 125.8 `CONFIG_HL78XX_EVT_MONITOR`

**提示（Prompt）**：HL78XX AT 通知监视器（AT Notification Monitor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/hl78xx_evt_monitor/Kconfig.hl78xx_evt_monitor:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/hl78xx_evt_monitor/Kconfig.hl78xx_evt_monitor#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_EVT_MONITOR_APP_INIT_PRIORITY"></a>

## 125.9 `CONFIG_HL78XX_EVT_MONITOR_APP_INIT_PRIORITY`

**提示（Prompt）**：Sierra Wireless HL78XX 事件监视器应用初始化优先级

**说明（Help）**

Sierra Wireless HL78XX 事件监视器应用的初始化优先级。除非清楚其影响，否则不要随意更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_EVT_MONITOR && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/hl78xx_evt_monitor/Kconfig.hl78xx_evt_monitor:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/hl78xx_evt_monitor/Kconfig.hl78xx_evt_monitor#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX AT 通知监视器（AT Notification Monitor）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_EVT_MONITOR`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_EVT_MONITOR)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_EVT_MONITOR_HEAP_SIZE"></a>

## 125.10 `CONFIG_HL78XX_EVT_MONITOR_HEAP_SIZE`

**提示（Prompt）**：通知堆大小（Notification Heap Size）

**说明（Help）**

复制并排队 HL78xx 事件通知所用堆大小，用于在系统工作队列中延后分发给监视器。直接运行时监视器分发不使用此堆。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_EVT_MONITOR && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[64, 4096]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/hl78xx_evt_monitor/Kconfig.hl78xx_evt_monitor:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/hl78xx_evt_monitor/Kconfig.hl78xx_evt_monitor#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX AT 通知监视器（AT Notification Monitor）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_EVT_MONITOR`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_EVT_MONITOR)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_EVT_MONITOR_MAX_INSTANCE_MONITORS"></a>

## 125.11 `CONFIG_HL78XX_EVT_MONITOR_MAX_INSTANCE_MONITORS`

**提示（Prompt）**：运行时 HL78xx 事件监视器最大数量

**说明（Help）**

可注册的运行时事件监视器最大数量。此上限使事件监视器分发能够在不分配内存的情况下，对运行时监视器生成快照，包括从中断服务例程（ISR）上下文调用分发的情况。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_EVT_MONITOR && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/hl78xx_evt_monitor/Kconfig.hl78xx_evt_monitor:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/hl78xx_evt_monitor/Kconfig.hl78xx_evt_monitor#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX AT 通知监视器（AT Notification Monitor）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_EVT_MONITOR`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_EVT_MONITOR)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_GNSS"></a>

## 125.12 `CONFIG_HL78XX_GNSS`

**提示（Prompt）**：HL78xx 全球导航卫星系统（GNSS）驱动

**说明（Help）**

启用 HL78xx 调制解调器的全球导航卫星系统（Global Navigation Satellite System，GNSS）支持。此驱动使用 `AT+KGPS*` 命令提供独立 GNSS 功能，支持 GPS、GLONASS、Galileo 和北斗（BeiDou）卫星系统。NMEA 语句以主动结果码（URC）形式接收，由 GNSS 子系统处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_GNSS
CONFIG_GNSS_NMEA0183
CONFIG_GNSS_NMEA0183_MATCH
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:244`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L244)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_NMEA0183`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA0183)、[`CONFIG_GNSS_NMEA0183_MATCH`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA0183_MATCH)。

<a id="CONFIG_HL78XX_GNSS_ADVANCED_NMEA_CONFIG"></a>

## 125.13 `CONFIG_HL78XX_GNSS_ADVANCED_NMEA_CONFIG`

**提示（Prompt）**：高级 NMEA 语句配置（Sentence Configuration）

**说明（Help）**

启用手动配置额外 NMEA 语句，超出最低必需语句（GGA、GST、RMC）和补充语句的范围。大多数用户无需此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**被选择（Selected by）**

```text
CONFIG_HL78XX_GNSS_AUX_DATA_PARSER
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:291`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L291)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_HL78XX_GNSS_AUX_DATA_PARSER`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_AUX_DATA_PARSER)。

<a id="CONFIG_HL78XX_GNSS_AUX_DATA_PARSER"></a>

## 125.14 `CONFIG_HL78XX_GNSS_AUX_DATA_PARSER`

**提示（Prompt）**：补充 NMEA0183 解析器（Supplementary Parsers）

**说明（Help）**

启用补充 NMEA0183 语句解析，提供基本位置与时间之外的 GNSS 信息：

- GSA：GNSS 精度因子（DOP）与活动卫星，包含精度因子及定位类型。
- GST：GNSS 伪距误差统计（Pseudorange Error Statistics），即位置误差估计。
- PEPU：HL78XX 专有 EPE 语句，提供 HL78xx 特定的位置误差。

基本导航不必需这些语句，但它们可提供更丰富的精度和质量指标。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_HL78XX_GNSS_ADVANCED_NMEA_CONFIG
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:298`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L298)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_HL78XX_GNSS_ADVANCED_NMEA_CONFIG`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_ADVANCED_NMEA_CONFIG)。

<a id="CONFIG_HL78XX_GNSS_CONSTELLATIONS"></a>

## 125.15 `CONFIG_HL78XX_GNSS_CONSTELLATIONS`

**提示（Prompt）**：GNSS 卫星星座（Satellite Constellations）

**说明（Help）**

选择启用哪些卫星星座。HL78xx 调制解调器通过 `AT+GNSSCONF=10,<value>` 支持 GPS 和 GLONASS。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_HL78XX_GNSS_CONSTELLATIONS_GPS_GLONASS
```

**可选项（Choices）**

```text
CONFIG_HL78XX_GNSS_CONSTELLATIONS_GPS_ONLY
CONFIG_HL78XX_GNSS_CONSTELLATIONS_GPS_GLONASS
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:476`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L476)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_HL78XX_GNSS_CONSTELLATIONS_GPS_GLONASS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_CONSTELLATIONS_GPS_GLONASS)、[`CONFIG_HL78XX_GNSS_CONSTELLATIONS_GPS_ONLY`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_CONSTELLATIONS_GPS_ONLY)。

<a id="CONFIG_HL78XX_GNSS_CONSTELLATIONS_GPS_GLONASS"></a>

## 125.16 `CONFIG_HL78XX_GNSS_CONSTELLATIONS_GPS_GLONASS`

**提示（Prompt）**：GPS + GLONASS

**说明（Help）**

同时启用 GPS 和 GLONASS 星座，以改善精度和可用性（Availability）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_GNSS_CONSTELLATIONS>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:488`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L488)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → GNSS 卫星星座（Satellite Constellations）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_CONSTELLATIONS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_CONSTELLATIONS)。

<a id="CONFIG_HL78XX_GNSS_CONSTELLATIONS_GPS_ONLY"></a>

## 125.17 `CONFIG_HL78XX_GNSS_CONSTELLATIONS_GPS_ONLY`

**提示（Prompt）**：仅 GPS（GPS Only）

**说明（Help）**

仅启用 GPS 星座。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_GNSS_CONSTELLATIONS>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:483`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L483)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → GNSS 卫星星座（Satellite Constellations）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_CONSTELLATIONS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_CONSTELLATIONS)。

<a id="CONFIG_HL78XX_GNSS_NMEA_DTM"></a>

## 125.18 `CONFIG_HL78XX_GNSS_NMEA_DTM`

**提示（Prompt）**：DTM 语句（Sentence）

**说明（Help）**

启用 DTM（基准参考，Datum Reference）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_AUX_DATA_PARSER && CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:379`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L379)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → NMEA 语句选择（Sentence Selection）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_AUX_DATA_PARSER`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_AUX_DATA_PARSER)、[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_GNSS_NMEA_GGA"></a>

## 125.19 `CONFIG_HL78XX_GNSS_NMEA_GGA`

**提示（Prompt）**：GGA 语句（Sentence）

**说明（Help）**

启用 GGA（全球定位系统定位数据，Global Positioning System Fix Data）。GNSS 主动结果码（URC）和 `+GNSSLOC?` 响应需要此语句。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:312`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L312)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → NMEA 语句选择（Sentence Selection）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_GNSS_NMEA_GLL"></a>

## 125.20 `CONFIG_HL78XX_GNSS_NMEA_GLL`

**提示（Prompt）**：GLL 语句（Sentence）

**说明（Help）**

启用 GLL（地理位置——纬度／经度，Geographic Position – Latitude/Longitude）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_AUX_DATA_PARSER && CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:359`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L359)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → NMEA 语句选择（Sentence Selection）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_AUX_DATA_PARSER`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_AUX_DATA_PARSER)、[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_GNSS_NMEA_GNS"></a>

## 125.21 `CONFIG_HL78XX_GNSS_NMEA_GNS`

**提示（Prompt）**：GNS 语句（Sentence）

**说明（Help）**

启用 GNS（GNSS 定位数据，GNSS Fix Data）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_AUX_DATA_PARSER && CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:353`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L353)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → NMEA 语句选择（Sentence Selection）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_AUX_DATA_PARSER`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_AUX_DATA_PARSER)、[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_GNSS_NMEA_GSA"></a>

## 125.22 `CONFIG_HL78XX_GNSS_NMEA_GSA`

**提示（Prompt）**：GSA 语句（Sentence）

**说明（Help）**

启用 GSA（GNSS 精度因子与活动卫星，GNSS DOP and Active Satellites）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_AUX_DATA_PARSER && CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y if CONFIG_HL78XX_GNSS_AUX_DATA_PARSER
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:342`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L342)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → NMEA 语句选择（Sentence Selection）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_AUX_DATA_PARSER`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_AUX_DATA_PARSER)、[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_GNSS_NMEA_GST"></a>

## 125.23 `CONFIG_HL78XX_GNSS_NMEA_GST`

**提示（Prompt）**：GST 语句（Sentence）

**说明（Help）**

启用 GST（GNSS 伪距误差统计，GNSS Pseudorange Error Statistics）。GNSS 主动结果码（URC）和 `+GNSSLOC?` 响应需要此语句。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:319`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L319)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → NMEA 语句选择（Sentence Selection）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_GNSS_NMEA_GST_DUP"></a>

## 125.24 `CONFIG_HL78XX_GNSS_NMEA_GST_DUP`

**提示（Prompt）**：GST（重复位 10，Duplicate Bit 10）

**说明（Help）**

再次启用 GST（位 10）。请确认它是否与位 6 不同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_AUX_DATA_PARSER && CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:374`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L374)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → NMEA 语句选择（Sentence Selection）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_AUX_DATA_PARSER`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_AUX_DATA_PARSER)、[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_GNSS_NMEA_GSV"></a>

## 125.25 `CONFIG_HL78XX_GNSS_NMEA_GSV`

**提示（Prompt）**：GSV 语句（Sentence）

**说明（Help）**

启用 GSV（可见 GNSS 卫星，GNSS Satellites in View）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y if CONFIG_HL78XX_GNSS_AUX_DATA_PARSER
y if CONFIG_GNSS_SATELLITES
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:333`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L333)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → NMEA 语句选择（Sentence Selection）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_HL78XX_GNSS_AUX_DATA_PARSER`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_AUX_DATA_PARSER)、[`CONFIG_GNSS_SATELLITES`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_SATELLITES)。

<a id="CONFIG_HL78XX_GNSS_NMEA_OUTPUT_PORT"></a>

## 125.26 `CONFIG_HL78XX_GNSS_NMEA_OUTPUT_PORT`

**提示（Prompt）**：NMEA 输出端口配置。

**说明（Help）**

指定用于输出 NMEA 帧的端口：

- 0：不输出 NMEA 帧。
- 1：通过 USB 专用 NMEA 端口输出。
- 3：通过 UART1 输出。
- 4：通过同一端口输出（URC 模式），原文推荐此项。
- 5：通过 CMUX DLC1 输出。
- 6：通过 CMUX DLC2 输出。
- 7：通过 CMUX DLC3 输出。
- 8：通过 CMUX DLC4 输出。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[0, 8]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:495`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L495)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_GNSS_NMEA_PEPU"></a>

## 125.27 `CONFIG_HL78XX_GNSS_NMEA_PEPU`

**提示（Prompt）**：PEPU 语句（Sentence）

**说明（Help）**

启用专有 PEPU（位置与速度不确定度，Position and Velocity Uncertainty）语句，提供 HL78xx 特定的位置和速度精度信息。对应 NMEA 掩码中的位 12（`0x1000`）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_12 && CONFIG_HL78XX_GNSS_AUX_DATA_PARSER && CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y if CONFIG_HL78XX_GNSS_AUX_DATA_PARSER
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:384`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L384)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → NMEA 语句选择（Sentence Selection）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_12)、[`CONFIG_HL78XX_GNSS_AUX_DATA_PARSER`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_AUX_DATA_PARSER)、[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_GNSS_NMEA_PIDX"></a>

## 125.28 `CONFIG_HL78XX_GNSS_NMEA_PIDX`

**提示（Prompt）**：PIDX 语句（Sentence）

**说明（Help）**

启用 PIDX（专有索引，Proprietary Index）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_AUX_DATA_PARSER && CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:369`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L369)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → NMEA 语句选择（Sentence Selection）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_AUX_DATA_PARSER`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_AUX_DATA_PARSER)、[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_GNSS_NMEA_RMC"></a>

## 125.29 `CONFIG_HL78XX_GNSS_NMEA_RMC`

**提示（Prompt）**：RMC 语句（Sentence）

**说明（Help）**

启用 RMC（推荐的最少专用 GNSS 数据，Recommended Minimum Specific GNSS Data）。GNSS 主动结果码（URC）和 `+GNSSLOC?` 响应需要此语句。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:326`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L326)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → NMEA 语句选择（Sentence Selection）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_GNSS_NMEA_VTG"></a>

## 125.30 `CONFIG_HL78XX_GNSS_NMEA_VTG`

**提示（Prompt）**：VTG 语句（Sentence）

**说明（Help）**

启用 VTG（对地航向与地面速度，Course Over Ground and Ground Speed）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_AUX_DATA_PARSER && CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:348`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L348)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → NMEA 语句选择（Sentence Selection）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_AUX_DATA_PARSER`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_AUX_DATA_PARSER)、[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_GNSS_NMEA_ZDA"></a>

## 125.31 `CONFIG_HL78XX_GNSS_NMEA_ZDA`

**提示（Prompt）**：ZDA 语句（Sentence）

**说明（Help）**

启用 ZDA（时间与日期，Time & Date）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_AUX_DATA_PARSER && CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:364`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L364)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → NMEA 语句选择（Sentence Selection）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_AUX_DATA_PARSER`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_AUX_DATA_PARSER)、[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_GNSS_PROCESS_POST_PSM"></a>

## 125.32 `CONFIG_HL78XX_GNSS_PROCESS_POST_PSM`

**提示（Prompt）**：退出睡眠后处理 GNSS 请求（Post-PSM）

**说明（Help）**

此模式下，调制解调器自然退出省电模式（PSM）睡眠后，即 GPIO6 置为有效、唤醒引脚触发时，会在 LTE 连接重新建立之前立即处理 GNSS 请求。驱动截获唤醒序列，设置 `CFUN=4`（飞行模式，Airplane Mode），防止 LTE 重新占用共享射频路径，使 GNSS 得以运行。GNSS 完成后，调制解调器恢复全部功能，继续 LTE 注册。需要在每个唤醒周期开始时、执行 LTE 操作前取得 GNSS 数据时，可使用此模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_GNSS_REQUEST_PROCESSING_MODE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:449`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L449)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → GNSS 请求处理模式（Request Processing Mode）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_REQUEST_PROCESSING_MODE`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_REQUEST_PROCESSING_MODE)。

<a id="CONFIG_HL78XX_GNSS_PROCESS_PRE_PSM"></a>

## 125.33 `CONFIG_HL78XX_GNSS_PROCESS_PRE_PSM`

**提示（Prompt）**：进入睡眠时处理 GNSS 请求（Pre-PSM）

**说明（Help）**

此模式下，调制解调器一进入 PSM 睡眠，就处理 GNSS 请求。驱动立即唤醒调制解调器，并在 LTE 调制解调器仍休眠时启动 GNSS，因此共享射频接收路径已经空闲，无需设置飞行模式。希望 GNSS 捕获（Acquisition）在 PSM 睡眠窗口中运行、尽量延长卫星定位可用时间时，可使用此模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_GNSS_REQUEST_PROCESSING_MODE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:464`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L464)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → GNSS 请求处理模式（Request Processing Mode）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_REQUEST_PROCESSING_MODE`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_REQUEST_PROCESSING_MODE)。

<a id="CONFIG_HL78XX_GNSS_REQUEST_PROCESSING_MODE"></a>

## 125.34 `CONFIG_HL78XX_GNSS_REQUEST_PROCESSING_MODE`

**提示（Prompt）**：GNSS 请求处理模式（Request Processing Mode）

**说明（Help）**

选择排队的 GNSS 请求相对于调制解调器省电模式（Power Save Mode，PSM）睡眠周期的处理方式。

- POST-PSM：调制解调器自然从 PSM 唤醒后、LTE 重新建立前运行 GNSS。驱动设置 `CFUN=4`（飞行模式），在 LTE 注册前为 GNSS 占用共享射频路径。
- PRE-PSM：调制解调器一进入 PSM 睡眠就运行 GNSS。驱动立即唤醒调制解调器，在 LTE 仍休眠时启动 GNSS，无需设置飞行模式。

注意：此选项只影响排队／待处理的 GNSS 请求。调制解调器已经睡眠时，显式调用 `hl78xx_enter_gnss_mode()` 总会立即唤醒它，不受此设置影响。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_PSM && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_HL78XX_GNSS_PROCESS_POST_PSM
```

**可选项（Choices）**

```text
CONFIG_HL78XX_GNSS_PROCESS_POST_PSM
CONFIG_HL78XX_GNSS_PROCESS_PRE_PSM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:429`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L429)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_PSM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_PSM)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_HL78XX_GNSS_PROCESS_POST_PSM`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_PROCESS_POST_PSM)、[`CONFIG_HL78XX_GNSS_PROCESS_PRE_PSM`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_PROCESS_PRE_PSM)。

<a id="CONFIG_HL78XX_GNSS_SATELLITES_COUNT"></a>

## 125.35 `CONFIG_HL78XX_GNSS_SATELLITES_COUNT`

**提示（Prompt）**：卫星跟踪槽位数量（Satellite Tracking Slots）

**说明（Help）**

可同时跟踪的最大卫星数量。这会影响内存用量，每个卫星槽位约需 32 字节 RAM。默认值为 24，足以满足大多数使用场景。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS_SOURCE_NMEA && CONFIG_HL78XX_GNSS_NMEA_GSV && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
24
```

**取值范围（Ranges）**

```text
[12, 32]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:511`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L511)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS_NMEA_GSV`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_NMEA_GSV)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_HL78XX_GNSS_SOURCE"></a>

## 125.36 `CONFIG_HL78XX_GNSS_SOURCE`

**提示（Prompt）**：GNSS 来源选择（Source Selection）

**说明（Help）**

选择从 HL78XX 模块取得 GNSS 数据的方法。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_HL78XX_GNSS_SOURCE_NMEA
```

**可选项（Choices）**

```text
CONFIG_HL78XX_GNSS_SOURCE_NMEA
CONFIG_HL78XX_GNSS_SOURCE_LOC
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L265)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_HL78XX_GNSS_SOURCE_NMEA`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_NMEA)、[`CONFIG_HL78XX_GNSS_SOURCE_LOC`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE_LOC)。

<a id="CONFIG_HL78XX_GNSS_SOURCE_LOC"></a>

## 125.37 `CONFIG_HL78XX_GNSS_SOURCE_LOC`

**提示（Prompt）**：来源：最近已知定位结果（Latest Known Position Fix）

**说明（Help）**

使用 `AT+GNSSLOC?` 命令获取最近的 GNSS 定位结果。

- 完全在命令模式（Command Mode）下运行，无需切换到数据模式。
- 直接返回经过解析的结构化位置数据。
- 适用于需要快速取得位置数据、不希望解析原始 NMEA 字符串的应用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_GNSS_SOURCE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:279`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L279)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → GNSS 来源选择（Source Selection）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_SOURCE`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE)。

<a id="CONFIG_HL78XX_GNSS_SOURCE_NMEA"></a>

## 125.38 `CONFIG_HL78XX_GNSS_SOURCE_NMEA`

**提示（Prompt）**：来源：NMEA（需手动解析，Manual Parsing）

**说明（Help）**

在接收 `+GNSSNMEA` 命令的同一端口上启用原始 NMEA 帧输出。

- 需要将模块切换到数据模式（Data Mode）。
- 必须手动解析原始 NMEA 字符串，提取位置数据。
- 适用于需要完整 GNSS 语句数据的应用，例如 `$GPGGA`、`$GPRMC` 等。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_GNSS_SOURCE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:271`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L271)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → GNSS 来源选择（Source Selection）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_SOURCE`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_SOURCE)。

<a id="CONFIG_HL78XX_GNSS_START_MODE"></a>

## 125.39 `CONFIG_HL78XX_GNSS_START_MODE`

**提示（Prompt）**：GNSS 启动模式（Start Mode）

**说明（Help）**

选择 `AT+GNSSSTART` 命令使用的 GNSS 启动模式。正常运行时，原文推荐 AUTO 模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_HL78XX_GNSS_START_MODE_AUTO
```

**可选项（Choices）**

```text
CONFIG_HL78XX_GNSS_START_MODE_AUTO
CONFIG_HL78XX_GNSS_START_MODE_WARM
CONFIG_HL78XX_GNSS_START_MODE_COLD
CONFIG_HL78XX_GNSS_START_MODE_FACTORY
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:399`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L399)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_HL78XX_GNSS_START_MODE_AUTO`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_START_MODE_AUTO)、[`CONFIG_HL78XX_GNSS_START_MODE_WARM`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_START_MODE_WARM)、[`CONFIG_HL78XX_GNSS_START_MODE_COLD`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_START_MODE_COLD)、[`CONFIG_HL78XX_GNSS_START_MODE_FACTORY`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_START_MODE_FACTORY)。

<a id="CONFIG_HL78XX_GNSS_START_MODE_AUTO"></a>

## 125.40 `CONFIG_HL78XX_GNSS_START_MODE_AUTO`

**提示（Prompt）**：AUTO——正常运行（Normal Operations）

**说明（Help）**

使用先前保存的全部数据，用于正常运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_GNSS_START_MODE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:406`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L406)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → GNSS 启动模式（Start Mode）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_START_MODE`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_START_MODE)。

<a id="CONFIG_HL78XX_GNSS_START_MODE_COLD"></a>

## 125.41 `CONFIG_HL78XX_GNSS_START_MODE_COLD`

**提示（Prompt）**：COLD——测试模式（Test Mode）

**说明（Help）**

仅用于测试。除历书（Almanac）和扩展星历（Extended Ephemeris）外，不使用任何先前保存的数据。时间与上次位置均未知。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_GNSS_START_MODE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:416`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L416)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → GNSS 启动模式（Start Mode）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_START_MODE`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_START_MODE)。

<a id="CONFIG_HL78XX_GNSS_START_MODE_FACTORY"></a>

## 125.42 `CONFIG_HL78XX_GNSS_START_MODE_FACTORY`

**提示（Prompt）**：FACTORY——测试模式（Test Mode）

**说明（Help）**

仅用于测试。不使用任何先前保存的数据，使用出厂默认数据（Factory Default Data）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_GNSS_START_MODE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:422`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L422)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → GNSS 启动模式（Start Mode）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_START_MODE`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_START_MODE)。

<a id="CONFIG_HL78XX_GNSS_START_MODE_WARM"></a>

## 125.43 `CONFIG_HL78XX_GNSS_START_MODE_WARM`

**提示（Prompt）**：WARM——测试模式（Test Mode）

**说明（Help）**

仅用于测试。使用除星历（Ephemeris）之外的所有先前保存数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_GNSS_START_MODE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:411`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L411)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动 → GNSS 启动模式（Start Mode）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_GNSS_START_MODE`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS_START_MODE)。

<a id="CONFIG_HL78XX_GNSS_SUPPORT_ASSISTED_MODE"></a>

## 125.44 `CONFIG_HL78XX_GNSS_SUPPORT_ASSISTED_MODE`

**提示（Prompt）**：辅助 GNSS（Assisted GNSS，A-GNSS）模式支持

**说明（Help）**

启用通过 `AT+GNSSAD` 命令使用辅助 GNSS（A-GNSS）模式的支持。A-GNSS 利用蜂窝网络辅助数据，可缩短首次定位时间（Time-to-first-fix）并提高精度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_12 && CONFIG_HL78XX_GNSS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:257`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L257)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78xx 全球导航卫星系统（GNSS）驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_12)、[`CONFIG_HL78XX_GNSS`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_GNSS)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM"></a>

## 125.45 `CONFIG_MODEM`

**提示（Prompt）**：调制解调器驱动（Modem Drivers）

**说明（Help）**

启用调制解调器驱动的配置选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_WIFI_ESP_AT
CONFIG_WIFI_ST67W611M1
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/sparkfun_sara_r4/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/sparkfun_sara_r4/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/st87mxx/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st87mxx/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/wnc_m14a2a/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/wnc_m14a2a/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/modem/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI_ST67W611M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ST67W611M1)。

<a id="CONFIG_MODEM_AT_SHELL"></a>

## 125.46 `CONFIG_MODEM_AT_SHELL`

**提示（Prompt）**：基于调制解调器模块的 AT 命令 Shell

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_SHELL && !CONFIG_SHELL_WILDCARD && CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_MODEM_MODULES
CONFIG_MODEM_AT_USER_PIPE
```

**定义位置（Location）**：[`drivers/modem/Kconfig.at_shell:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.at_shell#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_SHELL)、[`CONFIG_SHELL_WILDCARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_WILDCARD)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_MODULES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_AT_USER_PIPE`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_AT_USER_PIPE)。

<a id="CONFIG_MODEM_AT_SHELL_CHAT_RECEIVE_BUF_SIZE"></a>

## 125.47 `CONFIG_MODEM_AT_SHELL_CHAT_RECEIVE_BUF_SIZE`

**提示（Prompt）**：调制解调器会话（Modem Chat）接收缓冲区大小，单位为字节

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_AT_SHELL && CONFIG_MODEM
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/modem/Kconfig.at_shell:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.at_shell#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 基于调制解调器模块的 AT 命令 Shell

**配置项引用（Symbol References）**：[`CONFIG_MODEM_AT_SHELL`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_AT_SHELL)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_AT_SHELL_COMMAND_MAX_SIZE"></a>

## 125.48 `CONFIG_MODEM_AT_SHELL_COMMAND_MAX_SIZE`

原库同名定义共 2 条；本项为数据库第 11781 条记录，各定义分别保留。

**提示（Prompt）**：AT 命令最大大小（Maximum Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_AT_SHELL && CONFIG_MODEM
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/modem/Kconfig.at_shell:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.at_shell#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 基于调制解调器模块的 AT 命令 Shell

**配置项引用（Symbol References）**：[`CONFIG_MODEM_AT_SHELL`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_AT_SHELL)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_AT_SHELL_COMMAND_MAX_SIZE--record-11782"></a>

## 125.49 `CONFIG_MODEM_AT_SHELL_COMMAND_MAX_SIZE`

原库同名定义共 2 条；本项为数据库第 11782 条记录，各定义分别保留。

**提示（Prompt）**：AT 命令最大大小（Maximum Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AT_SHELL && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → AT 命令行（AT Command Shell）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AT_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_AT_SHELL)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_AT_SHELL_RESPONSE_MAX_SIZE"></a>

## 125.50 `CONFIG_MODEM_AT_SHELL_RESPONSE_MAX_SIZE`

原库同名定义共 2 条；本项为数据库第 11783 条记录，各定义分别保留。

**提示（Prompt）**：AT 响应最大大小（Maximum Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_AT_SHELL && CONFIG_MODEM
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`drivers/modem/Kconfig.at_shell:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.at_shell#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 基于调制解调器模块的 AT 命令 Shell

**配置项引用（Symbol References）**：[`CONFIG_MODEM_AT_SHELL`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_AT_SHELL)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_AT_SHELL_RESPONSE_MAX_SIZE--record-11784"></a>

## 125.51 `CONFIG_MODEM_AT_SHELL_RESPONSE_MAX_SIZE`

原库同名定义共 2 条；本项为数据库第 11784 条记录，各定义分别保留。

**提示（Prompt）**：AT 响应最大大小（Maximum Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AT_SHELL && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → AT 命令行（AT Command Shell）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AT_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_AT_SHELL)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_AT_SHELL_RESPONSE_TIMEOUT_MS"></a>

## 125.52 `CONFIG_MODEM_AT_SHELL_RESPONSE_TIMEOUT_MS`

**提示（Prompt）**：等待 AT 命令响应的超时时间，单位为毫秒

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AT_SHELL && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → AT 命令行（AT Command Shell）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AT_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_AT_SHELL)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_AT_SHELL_RESPONSE_TIMEOUT_S"></a>

## 125.53 `CONFIG_MODEM_AT_SHELL_RESPONSE_TIMEOUT_S`

**提示（Prompt）**：等待 AT 命令响应的超时时间，单位为秒

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_AT_SHELL && CONFIG_MODEM
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/modem/Kconfig.at_shell:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.at_shell#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 基于调制解调器模块的 AT 命令 Shell

**配置项引用（Symbol References）**：[`CONFIG_MODEM_AT_SHELL`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_AT_SHELL)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_AT_USER_PIPE"></a>

## 125.54 `CONFIG_MODEM_AT_USER_PIPE`

**提示（Prompt）**：调制解调器 AT 命令用户管道辅助函数（User Pipe Helpers）

**说明（Help）**

管理用于任意 AT 命令的用户管道访问的实用函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_MODEM_CHAT
CONFIG_MODEM_PIPE
CONFIG_MODEM_PIPELINK
```

**被选择（Selected by）**

```text
CONFIG_MODEM_AT_SHELL
```

**定义位置（Location）**：[`drivers/modem/Kconfig.at_shell:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.at_shell#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CHAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CHAT)、[`CONFIG_MODEM_PIPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_PIPE)、[`CONFIG_MODEM_PIPELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_PIPELINK)、[`CONFIG_MODEM_AT_SHELL`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_AT_SHELL)。

<a id="CONFIG_MODEM_AT_USER_PIPE_IDX"></a>

## 125.55 `CONFIG_MODEM_AT_USER_PIPE_IDX`

**提示（Prompt）**：要使用的用户管道编号（User Pipe Number）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_AT_USER_PIPE && CONFIG_MODEM
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/modem/Kconfig.at_shell:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.at_shell#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器 AT 命令用户管道辅助函数（User Pipe Helpers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_AT_USER_PIPE`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_AT_USER_PIPE)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR"></a>

## 125.56 `CONFIG_MODEM_CELLULAR`

**提示（Prompt）**：通用蜂窝调制解调器（Generic Cellular Modem）支持

**说明（Help）**

此驱动使用通用 3GPP AT 命令，以及标准 CMUX 和点对点协议（PPP），配置蜂窝调制解调器以建立点对点网络连接。它是为 u-blox、Quectel 及其他调制解调器定制驱动的模板；定制驱动可包含电源管理和更复杂的设备专用功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_MODEM_MODULES
CONFIG_MODEM_PPP
CONFIG_MODEM_CMUX
CONFIG_MODEM_CHAT
CONFIG_MODEM_PIPE
CONFIG_MODEM_PIPELINK
CONFIG_MODEM_BACKEND_UART
CONFIG_UART_USE_RUNTIME_CONFIGURE
CONFIG_PM_DEVICE_DRIVER_NEEDS_DEDICATED_WQ if CONFIG_PM_DEVICE_RUNTIME
CONFIG_NET_L2_PPP_OPTION_MRU
CONFIG_NET_L2_PPP_PAP
CONFIG_NET_L2_PPP_MGMT
CONFIG_MODEM_CMUX_DEFAULT_MTU_127 if DT_HAS_QUECTEL_BG95_ENABLED || DT_HAS_QUECTEL_BG96_ENABLED || DT_HAS_QUECTEL_EG21_G_ENABLED || DT_HAS_QUECTEL_EG25_G_ENABLED || DT_HAS_SIMCOM_SIM7080_ENABLED || DT_HAS_U_BLOX_SARA_R4_ENABLED || DT_HAS_U_BLOX_SARA_R5_ENABLED || DT_HAS_SWIR_HL7800_ENABLED || DT_HAS_TELIT_ME910G1_ENABLED || DT_HAS_TELIT_ME310G1_ENABLED || DT_HAS_TELIT_LE910C1TX_ENABLED || DT_HAS_TELIT_LEX10Q1_ENABLED || DT_HAS_SQN_GM02S_ENABLED || DT_HAS_QUECTEL_EG800Q_ENABLED || DT_HAS_SIMCOM_A76XX_ENABLED || DT_HAS_FIBOCOM_LE250_ENABLED || DT_HAS_TRASNA_LEXI_R10_ENABLED || DT_HAS_QUECTEL_EG915U_ENABLED || DT_HAS_NORDIC_NRF93M1_ENABLED || DT_HAS_NORDIC_NRF91_SM_V2_ENABLED || DT_HAS_QUECTEL_BG770_ENABLED
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MODEM_MODULES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_PPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_PPP)、[`CONFIG_MODEM_CMUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CMUX)、[`CONFIG_MODEM_CHAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CHAT)、[`CONFIG_MODEM_PIPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_PIPE)、[`CONFIG_MODEM_PIPELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_PIPELINK)、[`CONFIG_MODEM_BACKEND_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_USE_RUNTIME_CONFIGURE)、[`CONFIG_PM_DEVICE_DRIVER_NEEDS_DEDICATED_WQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_DRIVER_NEEDS_DEDICATED_WQ)、[`CONFIG_PM_DEVICE_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)、[`CONFIG_NET_L2_PPP_OPTION_MRU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PPP_OPTION_MRU)、[`CONFIG_NET_L2_PPP_PAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PPP_PAP)、[`CONFIG_NET_L2_PPP_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PPP_MGMT)、[`CONFIG_MODEM_CMUX_DEFAULT_MTU_127`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CMUX_DEFAULT_MTU_127)。

<a id="CONFIG_MODEM_CELLULAR_APN"></a>

## 125.57 `CONFIG_MODEM_CELLULAR_APN`

**提示（Prompt）**：静态接入点名称（Static APN）

**说明（Help）**

留空时，驱动会等待应用调用 `cellular_set_apn()`，之后才进入拨号阶段（Dial Phase）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"internet"
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_CHAT_BUFFER_SIZE"></a>

## 125.58 `CONFIG_MODEM_CELLULAR_CHAT_BUFFER_SIZE`

**提示（Prompt）**：会话脚本（Chat Script）使用的缓冲区大小，单位为字节。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_CLEAR_FORBIDDEN"></a>

## 125.59 `CONFIG_MODEM_CELLULAR_CLEAR_FORBIDDEN`

**提示（Prompt）**：启动时清除 SIM 卡中的禁止网络列表（Forbidden Networks）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_U_BLOX_LARA_R6_ENABLED && CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L207)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_INIT_PRIORITY"></a>

## 125.60 `CONFIG_MODEM_CELLULAR_INIT_PRIORITY`

**提示（Prompt）**：蜂窝调制解调器驱动初始化优先级

**说明（Help）**

蜂窝调制解调器驱动的初始化优先级。默认小于 `GNSS_INIT_PRIORITY`，因为 LTE 调制解调器常集成 GNSS 调制解调器。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
91
```

**取值范围（Ranges）**

```text
[0, 99]
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_MAX_RECOVERIES"></a>

## 125.61 `CONFIG_MODEM_CELLULAR_MAX_RECOVERIES`

**提示（Prompt）**：挂起前允许的最大连续恢复尝试次数（Recovery Attempts）

**说明（Help）**

在服务未恢复的情况下，连续执行此次数的初始化或 CMUX 连接恢复尝试后，驱动会挂起到空闲状态，而非无限复位调制解调器。CMUX 一旦重新连接，计数器便复位。设为 0 表示不限次数地重试。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_MAX_SCRIPT_FAILURES"></a>

## 125.62 `CONFIG_MODEM_CELLULAR_MAX_SCRIPT_FAILURES`

**提示（Prompt）**：挂起前允许的最大连续脚本失败次数（Script Failures）

**说明（Help）**

驱动放弃当前尝试并挂起到空闲状态之前，允许的连续会话脚本失败次数。值为 0 时，第一次失败即放弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_NEW_BAUDRATE"></a>

## 125.63 `CONFIG_MODEM_CELLULAR_NEW_BAUDRATE`

**提示（Prompt）**：若支持，要为调制解调器配置的新波特率（Baud Rate）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
3000000 if DT_HAS_U_BLOX_LARA_R6_ENABLED
115200
```

**取值范围（Ranges）**

```text
[9600, 4000000]
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_NEW_BAUDRATE_DELAY"></a>

## 125.64 `CONFIG_MODEM_CELLULAR_NEW_BAUDRATE_DELAY`

**提示（Prompt）**：调制解调器更改波特率所需时间，单位为毫秒

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
100 if DT_HAS_U_BLOX_LARA_R6_ENABLED
1000 if DT_HAS_QUECTEL_EG21_G_ENABLED
1000 if DT_HAS_QUECTEL_EG25_G_ENABLED
300
```

**取值范围（Ranges）**

```text
[0, 1000]
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_ON_DEMAND_CONNECT"></a>

## 125.65 `CONFIG_MODEM_CELLULAR_ON_DEMAND_CONNECT`

**提示（Prompt）**：按需拨打数据呼叫（Data Call，随 net_if 管理状态启停）

**说明（Help）**

按需拨打 PPP 数据呼叫，而非在上电时拨打。调制解调器启动后停留在休息状态，仅当使用方通过 `net_if_up()` 启用 PPP 接口时拨号，并在 `net_if_down()` 时挂断，使连接层能够将连接／断开映射为实际拨号／挂断，并在断开后重新拨号。此选项选择 `MODEM_DEDICATED_WORKQUEUE`，因为挂断路径需要它，原因见 `modem_cellular.c`。仅适用于厂商配置未提供网络会话脚本（Network Chat Script）的调制解调器；对于提供此类脚本的设备，启用后会导致驱动初始化失败（`-ENOTSUP`），因为这类调制解调器无论 PPP 接口的管理状态如何，都会在注册时拨号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_MODEM_DEDICATED_WORKQUEUE
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_DEDICATED_WORKQUEUE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_DEDICATED_WORKQUEUE)。

<a id="CONFIG_MODEM_CELLULAR_PDP_CONTEXT_ID"></a>

## 125.66 `CONFIG_MODEM_CELLULAR_PDP_CONTEXT_ID`

**提示（Prompt）**：数据呼叫使用的 PDP 上下文标识符（Context Identifier）

**说明（Help）**

驱动定义、去激活和拨号所用分组数据协议（PDP）上下文的标识符。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 24]
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_PERIODIC_SCRIPT_MS"></a>

## 125.67 `CONFIG_MODEM_CELLULAR_PERIODIC_SCRIPT_MS`

**提示（Prompt）**：周期性脚本间隔（Periodic Script Interval），单位为毫秒

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
30000 if DT_HAS_NORDIC_NRF93M1_ENABLED
2000
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_RAT"></a>

## 125.68 `CONFIG_MODEM_CELLULAR_RAT`

**提示（Prompt）**：要使用的无线接入技术（Radio Access Technology）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_U_BLOX_LARA_R6_ENABLED && CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_CELLULAR_RAT_4G
```

**可选项（Choices）**

```text
CONFIG_MODEM_CELLULAR_RAT_4G
CONFIG_MODEM_CELLULAR_RAT_4G_3G
CONFIG_MODEM_CELLULAR_RAT_4G_3G_2G
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_CELLULAR_RAT_4G`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR_RAT_4G)、[`CONFIG_MODEM_CELLULAR_RAT_4G_3G`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR_RAT_4G_3G)、[`CONFIG_MODEM_CELLULAR_RAT_4G_3G_2G`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR_RAT_4G_3G_2G)。

<a id="CONFIG_MODEM_CELLULAR_RAT_4G"></a>

## 125.69 `CONFIG_MODEM_CELLULAR_RAT_4G`

**提示（Prompt）**：仅使用 4G

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_CELLULAR_RAT>
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:196`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L196)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持 → 要使用的无线接入技术（Radio Access Technology）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR_RAT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR_RAT)。

<a id="CONFIG_MODEM_CELLULAR_RAT_4G_3G"></a>

## 125.70 `CONFIG_MODEM_CELLULAR_RAT_4G_3G`

**提示（Prompt）**：使用 4G 和 3G

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_CELLULAR_RAT>
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:199`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L199)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持 → 要使用的无线接入技术（Radio Access Technology）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR_RAT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR_RAT)。

<a id="CONFIG_MODEM_CELLULAR_RAT_4G_3G_2G"></a>

## 125.71 `CONFIG_MODEM_CELLULAR_RAT_4G_3G_2G`

**提示（Prompt）**：使用 4G、3G 和 2G

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_CELLULAR_RAT>
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持 → 要使用的无线接入技术（Radio Access Technology）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR_RAT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR_RAT)。

<a id="CONFIG_MODEM_CELLULAR_RECOVERY_BACKOFF_MAX_MS"></a>

## 125.72 `CONFIG_MODEM_CELLULAR_RECOVERY_BACKOFF_MAX_MS`

**提示（Prompt）**：最大恢复退避时间（Recovery Backoff），单位为毫秒

**说明（Help）**

每次恢复尝试退避时间的上限，避免较大的尝试次数预算导致复位前的延迟无界增长。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
60000
```

**取值范围（Ranges）**

```text
[0, 3600000]
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_RECOVERY_BACKOFF_MS"></a>

## 125.73 `CONFIG_MODEM_CELLULAR_RECOVERY_BACKOFF_MS`

**提示（Prompt）**：恢复退避步长（Recovery Backoff Step），单位为毫秒

**说明（Help）**

每次恢复复位前的延迟，乘以尝试次数，使反复失败时逐渐退避，而非连续不断地复位调制解调器。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2000
```

**取值范围（Ranges）**

```text
[0, 3600000]
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_RESET_POWER_ON_DELAY_MS"></a>

## 125.74 `CONFIG_MODEM_CELLULAR_RESET_POWER_ON_DELAY_MS`

**提示（Prompt）**：解除复位引脚有效状态与向电源引脚发送脉冲之间的延迟

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_SERIAL_NUMBER_MAX_SIZE"></a>

## 125.75 `CONFIG_MODEM_CELLULAR_SERIAL_NUMBER_MAX_SIZE`

**提示（Prompt）**：调制解调器序列号字符串的最大长度，不含空字符（NUL）

**说明（Help）**

3GPP TS 27.007 中 `+CGSN` 的文档规定，序列号文本不得超过 2048 个字符。多数调制解调器将国际移动设备识别码（IMEI）作为序列号输出，因此 16 个字符足够。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[16, 2048]
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_SHELL"></a>

## 125.76 `CONFIG_MODEM_CELLULAR_SHELL`

**提示（Prompt）**：蜂窝调制解调器驱动 Shell 命令

**说明（Help）**

启用 `cellular_modem` 驱动的 Shell 命令，通过 `cellular` 命令在运行时提供 `cellular_modem_pause_periodic_script()` / `cellular_modem_resume_periodic_script()` 功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_SHELL && CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_SHELL
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_SHELL)、[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)。

<a id="CONFIG_MODEM_CELLULAR_STATS"></a>

## 125.77 `CONFIG_MODEM_CELLULAR_STATS`

**提示（Prompt）**：运行统计（Operational Statistics）

**说明（Help）**

维护累计运行计数，例如服务中断时长、注册丢失、命令失败和恢复次数，并通过 `cellular_get_stats()` 提供访问。每个实例增加少量 RAM 占用，并在既有代码路径中增加少量计数递增操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_UART_BUFFER_SIZES"></a>

## 125.78 `CONFIG_MODEM_CELLULAR_UART_BUFFER_SIZES`

**提示（Prompt）**：UART 接收和发送缓冲区大小，单位为字节。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELLULAR_USER_PIPE_BUFFER_SIZES"></a>

## 125.79 `CONFIG_MODEM_CELLULAR_USER_PIPE_BUFFER_SIZES`

**提示（Prompt）**：每个用户管道（User Pipe）使用的缓冲区大小，单位为字节。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/modem/Kconfig.cellular:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig.cellular#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 通用蜂窝调制解调器（Generic Cellular Modem）支持

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CELL_INFO"></a>

## 125.80 `CONFIG_MODEM_CELL_INFO`

**提示（Prompt）**：查询运营商与小区信息（Operator and Cell Info）

**说明（Help）**

查询数字运营商标识（Operator ID）、位置区码（Location Area Code）和小区标识（Cell ID）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/Kconfig:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L184)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CMD_HANDLER"></a>

## 125.81 `CONFIG_MODEM_CMD_HANDLER`

**提示（Prompt）**：通用调制解调器命令处理程序（Generic Modem Command Handler）

**说明（Help）**

此通用命令处理程序使用调制解调器接口处理输入数据，并通过针对以下情况定义的回调，将数据交还调制解调器驱动：

- 调制解调器响应（Modem Response）。
- 主动消息（Unsolicited Message）。
- 为当前操作指定的处理程序。

要配置并使用此层，应创建 `modem_cmd_handler_data` 对象，将其引用与 `modem_context` 对象中的 `modem_cmd_handler` 引用一起传给 `modem_cmd_handler_init()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CONTEXT && CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_NET_BUF
```

**被选择（Selected by）**

```text
CONFIG_MODEM_QUECTEL_BG9X
CONFIG_MODEM_SIM7080
CONFIG_MODEM_ST87MXX
CONFIG_MODEM_UBLOX_SARA
CONFIG_WIFI_ESP_AT
CONFIG_WIFI_ST67W611M1
```

**定义位置（Location）**：[`drivers/modem/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器上下文辅助驱动（Modem Context Helper）【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_NET_BUF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_BUF)、[`CONFIG_MODEM_QUECTEL_BG9X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_QUECTEL_BG9X)、[`CONFIG_MODEM_SIM7080`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM_ST87MXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_ST87MXX)、[`CONFIG_MODEM_UBLOX_SARA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_WIFI_ESP_AT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI_ST67W611M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ST67W611M1)。

<a id="CONFIG_MODEM_CMD_HANDLER_MAX_PARAM_COUNT"></a>

## 125.82 `CONFIG_MODEM_CMD_HANDLER_MAX_PARAM_COUNT`

**提示（Prompt）**：每条命令解析的最大参数数量（Maximum Parameters）

**说明（Help）**

此选项设置命令处理程序可解析的最大参数数量。该数量也受 `match_buf` 字段长度 `match_buf_len` 限制，因为此缓冲区必须足以保存以 `/r` 结尾的一整行数据。译注：行结束标记在原文中写作 `/r`，此处保留其拼写。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CMD_HANDLER && CONFIG_MODEM_CONTEXT && CONFIG_MODEM
```

**默认值（Defaults）**

```text
14 if CONFIG_MODEM_SIM7080
6
```

**定义位置（Location）**：[`drivers/modem/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器上下文辅助驱动（Modem Context Helper）【实验性】 → 通用调制解调器命令处理程序（Generic Modem Command Handler）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CMD_HANDLER`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CMD_HANDLER)、[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_SIM7080`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_SIM7080)。

<a id="CONFIG_MODEM_CONTEXT"></a>

## 125.83 `CONFIG_MODEM_CONTEXT`

**提示（Prompt）**：调制解调器上下文辅助驱动（Modem Context Helper）【实验性】

**说明（Help）**

此驱动允许调制解调器驱动使用自定义协议与接口通信。它不检查接收数据，收到的协议数据的所有处理都由应用提供的工作方法（Work Method）负责。此驱动组合了调制解调器接口、命令处理程序、引脚配置和套接字处理的抽象，每一项都需要配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_MODEM_HL78XX
CONFIG_MODEM_QUECTEL_BG9X
CONFIG_MODEM_SIM7080
CONFIG_MODEM_ST87MXX
CONFIG_MODEM_UBLOX_SARA
CONFIG_WIFI_ESP_AT
CONFIG_WIFI_ST67W611M1
```

**定义位置（Location）**：[`drivers/modem/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM_QUECTEL_BG9X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_QUECTEL_BG9X)、[`CONFIG_MODEM_SIM7080`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM_ST87MXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_ST87MXX)、[`CONFIG_MODEM_UBLOX_SARA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_WIFI_ESP_AT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI_ST67W611M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ST67W611M1)。

<a id="CONFIG_MODEM_CONTEXT_MAX_NUM"></a>

## 125.84 `CONFIG_MODEM_CONTEXT_MAX_NUM`

**提示（Prompt）**：调制解调器上下文最大数量（Maximum Contexts）

**说明（Help）**

要处理的调制解调器上下文最大数量。多数情况下应保持为 1。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CONTEXT && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/modem/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器上下文辅助驱动（Modem Context Helper）【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_CONTEXT_VERBOSE_DEBUG"></a>

## 125.85 `CONFIG_MODEM_CONTEXT_VERBOSE_DEBUG`

**提示（Prompt）**：调制解调器上下文的详细调试输出（Verbose Debug Output）

**说明（Help）**

启用后，调制解调器上下文辅助模块会产生极其大量的调试输出。生产环境中不得保持开启。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CONTEXT && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器上下文辅助驱动（Modem Context Helper）【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_DEFAULT_SLEEP_LEVEL"></a>

## 125.86 `CONFIG_MODEM_DEFAULT_SLEEP_LEVEL`

**提示（Prompt）**：默认睡眠级别（Default Sleep Level）

**说明（Help）**

应用可以覆盖此设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_POWER_DOWN && CONFIG_MODEM_HL78XX_LOW_POWER_MODE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_HL78XX_SLEEP_LEVEL_HIBERNATE
```

**可选项（Choices）**

```text
CONFIG_MODEM_HL78XX_SLEEP_LEVEL_HIBERNATE
CONFIG_MODEM_HL78XX_SLEEP_LEVEL_LITE_HIBERNATE
CONFIG_MODEM_HL78XX_SLEEP_LEVEL_SLEEP
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1295`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1295)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_POWER_DOWN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_POWER_DOWN)、[`CONFIG_MODEM_HL78XX_LOW_POWER_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_LOW_POWER_MODE)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_SLEEP_LEVEL_HIBERNATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_SLEEP_LEVEL_HIBERNATE)、[`CONFIG_MODEM_HL78XX_SLEEP_LEVEL_LITE_HIBERNATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_SLEEP_LEVEL_LITE_HIBERNATE)、[`CONFIG_MODEM_HL78XX_SLEEP_LEVEL_SLEEP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_SLEEP_LEVEL_SLEEP)。

<a id="CONFIG_MODEM_HL7800"></a>

## 125.87 `CONFIG_MODEM_HL7800`

**提示（Prompt）**：Sierra Wireless HL7800 调制解调器驱动

**说明（Help）**

选择此设置以启用 Sierra Wireless HL7800 LTE-M/NB-IoT 调制解调器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_MODEM_RECEIVER
CONFIG_NET_OFFLOAD
```

**弱选择（Implies）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_RECEIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_RECEIVER)、[`CONFIG_NET_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_OFFLOAD)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_MODEM_HL7800_ADDRESS_FAMILY_IPV4"></a>

## 125.88 `CONFIG_MODEM_HL7800_ADDRESS_FAMILY_IPV4`

**提示（Prompt）**：IPv4（互联网协议第 4 版）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:343`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L343)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → IP 地址族（Address Family）

<a id="CONFIG_MODEM_HL7800_ADDRESS_FAMILY_IPV4V6"></a>

## 125.89 `CONFIG_MODEM_HL7800_ADDRESS_FAMILY_IPV4V6`

**提示（Prompt）**：IPv4v6（IPv4／IPv6 双栈）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:349`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L349)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → IP 地址族（Address Family）

<a id="CONFIG_MODEM_HL7800_ADDRESS_FAMILY_IPV6"></a>

## 125.90 `CONFIG_MODEM_HL7800_ADDRESS_FAMILY_IPV6`

**提示（Prompt）**：IPv6（互联网协议第 6 版）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:346`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L346)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → IP 地址族（Address Family）

<a id="CONFIG_MODEM_HL7800_ALLOW_SLEEP_DELAY_MS"></a>

## 125.91 `CONFIG_MODEM_HL7800_ALLOW_SLEEP_DELAY_MS`

**提示（Prompt）**：允许调制解调器睡眠前的延迟，单位为毫秒

**说明（Help）**

此值应大于网络延迟（Network Latency），否则调制解调器可能尚未有机会接收套接字数据就进入睡眠。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
5000
```

**取值范围（Ranges）**

```text
[5000, 3600000]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:354`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L354)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_APN_NAME"></a>

## 125.92 `CONFIG_MODEM_HL7800_APN_NAME`

**提示（Prompt）**：用于建立网络连接的接入点名称（APN）

**说明（Help）**

此设置用于 `AT+CGDCONT` 命令，设置 PDP 上下文的 APN 名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_SET_APN_NAME_ON_STARTUP && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 在驱动初始化期间设置 APN 名称

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_SET_APN_NAME_ON_STARTUP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL7800_SET_APN_NAME_ON_STARTUP)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_1"></a>

## 125.93 `CONFIG_MODEM_HL7800_BAND_1`

**提示（Prompt）**：频段（Band）1：2000 MHz

**说明（Help）**

启用频段 1：2000 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_10"></a>

## 125.94 `CONFIG_MODEM_HL7800_BAND_10`

**提示（Prompt）**：频段 10：2100 MHz

**说明（Help）**

启用频段 10：2100 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_12"></a>

## 125.95 `CONFIG_MODEM_HL7800_BAND_12`

**提示（Prompt）**：频段 12：700 MHz

**说明（Help）**

启用频段 12：700 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_13"></a>

## 125.96 `CONFIG_MODEM_HL7800_BAND_13`

**提示（Prompt）**：频段 13：700 MHz

**说明（Help）**

启用频段 13：700 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_14"></a>

## 125.97 `CONFIG_MODEM_HL7800_BAND_14`

**提示（Prompt）**：频段 14：700 MHz

**说明（Help）**

启用频段 14：700 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_17"></a>

## 125.98 `CONFIG_MODEM_HL7800_BAND_17`

**提示（Prompt）**：频段 17：700 MHz

**说明（Help）**

启用频段 17：700 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_18"></a>

## 125.99 `CONFIG_MODEM_HL7800_BAND_18`

**提示（Prompt）**：频段 18：800 MHz

**说明（Help）**

启用频段 18：800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_19"></a>

## 125.100 `CONFIG_MODEM_HL7800_BAND_19`

**提示（Prompt）**：频段 19：800 MHz

**说明（Help）**

启用频段 19：800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<!-- kconfig-navigation -->

[上一章](P124_drivers_mm_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P126_drivers_modem_配置项参考_2.md)
