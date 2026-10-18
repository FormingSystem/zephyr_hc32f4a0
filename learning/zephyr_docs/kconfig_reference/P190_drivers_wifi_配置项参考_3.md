---
id: learning.zephyr-docs.kconfig-reference.page-190
title: "`drivers/wifi`配置项参考（3/7）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第190章\_`drivers/wifi`配置项参考（3/7）

本章翻译官方 Kconfig 数据库中 `drivers/wifi` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NRF70_TX_DONE_WQ_PRIORITY"></a>

## 190.1 `CONFIG_NRF70_TX_DONE_WQ_PRIORITY`

**提示（Prompt）**：处理发送完成（TX Done）的工作队列优先级

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_TX_DONE_WQ_ENABLED && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:536`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L536)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF70_TX_DONE_WQ_ENABLED`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_TX_DONE_WQ_ENABLED)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_TX_DONE_WQ_STACK_SIZE"></a>

## 190.2 `CONFIG_NRF70_TX_DONE_WQ_STACK_SIZE`

**提示（Prompt）**：处理发送完成（TX Done）的工作队列栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_TX_DONE_WQ_ENABLED && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:540`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L540)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF70_TX_DONE_WQ_ENABLED`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_TX_DONE_WQ_ENABLED)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_TX_MAX_DATA_SIZE"></a>

## 190.3 `CONFIG_NRF70_TX_MAX_DATA_SIZE`

**提示（Prompt）**：发送（TX）数据最大大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1600
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:499`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L499)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_UTIL"></a>

## 190.4 `CONFIG_NRF70_UTIL`

**提示（Prompt）**：nRF70 驱动实用命令行（Utility Shell）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:284`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L284)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_WORKQ_MAX_ITEMS"></a>

## 190.5 `CONFIG_NRF70_WORKQ_MAX_ITEMS`

**提示（Prompt）**：所有工作队列的工作项（Work Items）最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:276`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L276)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_WORKQ_STACK_SIZE"></a>

## 190.6 `CONFIG_NRF70_WORKQ_STACK_SIZE`

**提示（Prompt）**：工作队列栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:272`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L272)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_2G_BAND"></a>

## 190.7 `CONFIG_NRF_WIFI_2G_BAND`

**提示（Prompt）**：将工作频段设为 2.4 GHz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_WIFI_OP_BAND>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:716`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L716)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → nRF Wi-Fi 工作频段（Operation Bands）

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_OP_BAND`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_OP_BAND)。

<a id="CONFIG_NRF_WIFI_5G_BAND"></a>

## 190.8 `CONFIG_NRF_WIFI_5G_BAND`

**提示（Prompt）**：将工作频段设为 5 GHz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_WIFI_OP_BAND>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:719`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L719)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → nRF Wi-Fi 工作频段（Operation Bands）

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_OP_BAND`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_OP_BAND)。

<a id="CONFIG_NRF_WIFI_ALL_BAND"></a>

## 190.9 `CONFIG_NRF_WIFI_ALL_BAND`

**提示（Prompt）**：将工作频段设为所有支持的频段

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_WIFI_OP_BAND>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:713`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L713)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → nRF Wi-Fi 工作频段（Operation Bands）

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_OP_BAND`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_OP_BAND)。

<a id="CONFIG_NRF_WIFI_AP_DEAD_DETECT_TIMEOUT"></a>

## 190.10 `CONFIG_NRF_WIFI_AP_DEAD_DETECT_TIMEOUT`

**提示（Prompt）**：接入点失效检测超时（AP Dead Detection Timeout），单位为秒

**说明（Help）**

未收到 AP 信标时，经过多少秒将 AP 判定为失效。用于检测 AP 无通知地停止工作，例如断电。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[1, 30]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:749`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L749)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_BEAMFORMING"></a>

## 190.11 `CONFIG_NRF_WIFI_BEAMFORMING`

**提示（Prompt）**：Wi-Fi 波束成形（Beamforming）。启用可略微改善性能；对于网络活动较少的应用，禁用可获得更好的节能效果。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:700`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L700)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_COEX_DISABLE_PRIORITY_WINDOW_FOR_SCAN"></a>

## 190.12 `CONFIG_NRF_WIFI_COEX_DISABLE_PRIORITY_WINDOW_FOR_SCAN`

**提示（Prompt）**：与短距无线（Short Range Radio）共存时强制禁用扫描优先窗口

**说明（Help）**

与短距无线（Short Range Radio）共存时，禁用扫描优先窗口（Priority Window）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:956`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L956)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_CTRL_HEAP_SIZE"></a>

## 190.13 `CONFIG_NRF_WIFI_CTRL_HEAP_SIZE`

**提示（Prompt）**：控制平面（Control Plane）专用内存池

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_NRF_WIFI_GLOBAL_HEAP && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
20000
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:637`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L637)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_GLOBAL_HEAP`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_GLOBAL_HEAP)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_DATA_HEAP_SIZE"></a>

## 190.14 `CONFIG_NRF_WIFI_DATA_HEAP_SIZE`

**提示（Prompt）**：数据平面（Data Plane）专用内存池

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_NRF_WIFI_GLOBAL_HEAP && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0 if CONFIG_NRF70_RADIO_TEST || CONFIG_NRF70_OFFLOADED_RAW_TX
8000 if CONFIG_NRF70_SCAN_ONLY
110000 if !CONFIG_SOC_FAMILY_NORDIC_NRF
65536
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:641`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L641)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_GLOBAL_HEAP`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_GLOBAL_HEAP)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NRF70_RADIO_TEST`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_RADIO_TEST)、[`CONFIG_NRF70_OFFLOADED_RAW_TX`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_OFFLOADED_RAW_TX)、[`CONFIG_NRF70_SCAN_ONLY`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SCAN_ONLY)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_WIFI_DISPLAY_SCAN_ABORT_ON_BSS_LIMIT"></a>

## 190.15 `CONFIG_NRF_WIFI_DISPLAY_SCAN_ABORT_ON_BSS_LIMIT`

**提示（Prompt）**：达到显示扫描的 BSS 数量上限时中止扫描

**说明（Help）**

启用后，达到基本服务集（BSS）数量上限时，中止用于显示的扫描（Display Scan）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:962`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L962)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_DISPLAY_SCAN_BSS_LIMIT"></a>

## 190.16 `CONFIG_NRF_WIFI_DISPLAY_SCAN_BSS_LIMIT`

**提示（Prompt）**：显示扫描的基本服务集（BSS）数量上限

**说明（Help）**

扫描结果中的基本服务集（BSS）条目数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
250 if CONFIG_NRF70_SCAN_ONLY
150
```

**取值范围（Ranges）**

```text
[1, 450] if CONFIG_NRF70_SCAN_ONLY
[1, 160]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:945`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L945)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NRF70_SCAN_ONLY`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SCAN_ONLY)。

<a id="CONFIG_NRF_WIFI_DYNAMIC_BANDWIDTH_SIGNALLING"></a>

## 190.17 `CONFIG_NRF_WIFI_DYNAMIC_BANDWIDTH_SIGNALLING`

**提示（Prompt）**：Wi-Fi 动态带宽信令（Dynamic Bandwidth Signalling）

**说明（Help）**

启用动态带宽信令（Dynamic Bandwidth Signalling）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:1000`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L1000)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_DYNAMIC_ED"></a>

## 190.18 `CONFIG_NRF_WIFI_DYNAMIC_ED`

**提示（Prompt）**：动态能量检测（Dynamic ED）

**说明（Help）**

启用专有算法（Proprietary Algorithm）支持，以改善高流量信道中的性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:1005`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L1005)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_FEAT_KEEPALIVE"></a>

## 190.19 `CONFIG_NRF_WIFI_FEAT_KEEPALIVE`

**提示（Prompt）**：用于连接维护的 Wi-Fi 保活（Keepalive）功能

**说明（Help）**

启用 Wi-Fi 保活（Keepalive）功能，通过向 AP 发送保活包维持连接。主要用于与不进行显式检查就断开空闲客户端的 AP 互操作，会略微增加功耗。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_STA_MODE && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:898`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L898)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF70_STA_MODE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_STA_MODE)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_FEAT_WMM"></a>

## 190.20 `CONFIG_NRF_WIFI_FEAT_WMM`

**提示（Prompt）**：无线多媒体／服务质量（WMM/QoS）支持

**说明（Help）**

控制无线多媒体（Wireless Multi-Media，WMM）功能的启用或禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:834`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L834)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_FW_BLOB_HANDLING"></a>

## 190.21 `CONFIG_NRF_WIFI_FW_BLOB_HANDLING`

**提示（Prompt）**：nRF70 固件二进制（Firmware Blob）处理

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_BUILD_ONLY_NO_BLOBS && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_NRF_WIFI_PATCHES_BUILTIN
```

**可选项（Choices）**

```text
CONFIG_NRF_WIFI_PATCHES_BUILTIN
CONFIG_NRF_WIFI_PATCHES_EXTERNAL
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_BUILD_ONLY_NO_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_ONLY_NO_BLOBS)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NRF_WIFI_PATCHES_BUILTIN`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_PATCHES_BUILTIN)、[`CONFIG_NRF_WIFI_PATCHES_EXTERNAL`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_PATCHES_EXTERNAL)。

<a id="CONFIG_NRF_WIFI_GLOBAL_HEAP"></a>

## 190.22 `CONFIG_NRF_WIFI_GLOBAL_HEAP`

**提示（Prompt）**：Wi-Fi 驱动使用 Zephyr 内核堆（Kernel Heap）

**说明（Help）**

启用后，Wi-Fi 驱动使用 `K_HEAP` 分配内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_KERNEL_MEM_POOL && (CONFIG_HEAP_MEM_POOL_SIZE > 0 || CONFIG_HEAP_MEM_POOL_IGNORE_MIN) && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:622`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L622)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_KERNEL_MEM_POOL`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_MEM_POOL)、[`CONFIG_HEAP_MEM_POOL_SIZE`](P001_kernel_配置项参考_1.md#CONFIG_HEAP_MEM_POOL_SIZE)、[`CONFIG_HEAP_MEM_POOL_IGNORE_MIN`](P001_kernel_配置项参考_1.md#CONFIG_HEAP_MEM_POOL_IGNORE_MIN)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_IFACE_MTU"></a>

## 190.23 `CONFIG_NRF_WIFI_IFACE_MTU`

**提示（Prompt）**：Wi-Fi 接口的最大传输单元（MTU）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1500
```

**取值范围（Ranges）**

```text
[576, 2304] if CONFIG_NET_IPV4
[1280, 2304] if CONFIG_NET_IPV6
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:724`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L724)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)。

<a id="CONFIG_NRF_WIFI_IF_AUTO_START"></a>

## 190.24 `CONFIG_NRF_WIFI_IF_AUTO_START`

**提示（Prompt）**：启动时自动启用 Wi-Fi 接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_KEEPALIVE_PERIOD_S"></a>

## 190.25 `CONFIG_NRF_WIFI_KEEPALIVE_PERIOD_S`

**提示（Prompt）**：保活周期（Keepalive Period），单位为秒

**说明（Help）**

向 AP 发送保活包（Keepalive Packet）的周期，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_WIFI_FEAT_KEEPALIVE && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[30, 3600]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:909`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L909)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → 用于连接维护的 Wi-Fi 保活（Keepalive）功能

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_FEAT_KEEPALIVE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_FEAT_KEEPALIVE)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_LOW_POWER"></a>

## 190.26 `CONFIG_NRF_WIFI_LOW_POWER`

**提示（Prompt）**：nRF Wi-Fi 芯片组低功耗模式（Low Power Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NRF70_RADIO_TEST && !CONFIG_NRF70_AP_MODE && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:199`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L199)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF70_RADIO_TEST`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_RADIO_TEST)、[`CONFIG_NRF70_AP_MODE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_AP_MODE)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_MAX_PS_POLL_FAIL_CNT"></a>

## 190.27 `CONFIG_NRF_WIFI_MAX_PS_POLL_FAIL_CNT`

**提示（Prompt）**：节能轮询（PS-Poll）失败的最大次数

**说明（Help）**

进入基于 QoS 空帧（QoS Null）的节能模式前，允许节能轮询（PS-Poll）失败的最大次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[10, 4294967295]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:986`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L986)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_MGMT_BUFF_OFFLOAD"></a>

## 190.28 `CONFIG_NRF_WIFI_MGMT_BUFF_OFFLOAD`

**提示（Prompt）**：管理缓冲区卸载（Management Buffer Offload）

**说明（Help）**

将管理缓冲区的补充操作卸载到上层媒体访问控制（UMAC），使主机无需为每个管理包交换命令和事件，即使该包由 UMAC 自身消费。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:888`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L888)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_OP_BAND"></a>

## 190.29 `CONFIG_NRF_WIFI_OP_BAND`

**提示（Prompt）**：nRF Wi-Fi 工作频段（Operation Bands）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_NRF_WIFI_2G_BAND if CONFIG_NRF70_2_4G_ONLY
CONFIG_NRF_WIFI_ALL_BAND
```

**可选项（Choices）**

```text
CONFIG_NRF_WIFI_ALL_BAND
CONFIG_NRF_WIFI_2G_BAND
CONFIG_NRF_WIFI_5G_BAND
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:708`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L708)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NRF_WIFI_2G_BAND`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_2G_BAND)、[`CONFIG_NRF70_2_4G_ONLY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF70_2_4G_ONLY)、[`CONFIG_NRF_WIFI_ALL_BAND`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_ALL_BAND)、[`CONFIG_NRF_WIFI_5G_BAND`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_5G_BAND)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRF70_2_4G_ONLY`。

<a id="CONFIG_NRF_WIFI_PATCHES_BUILTIN"></a>

## 190.30 `CONFIG_NRF_WIFI_PATCHES_BUILTIN`

**提示（Prompt）**：将 nRF70 固件补丁存储为驱动的一部分

**说明（Help）**

将 nRF70 固件（FW）补丁存储为驱动的一部分。此选项会影响驱动的代码存储占用（Code Memory Footprint）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_WIFI_FW_BLOB_HANDLING>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → nRF70 固件二进制（Firmware Blob）处理

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_FW_BLOB_HANDLING`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_FW_BLOB_HANDLING)。

<a id="CONFIG_NRF_WIFI_PATCHES_EXTERNAL"></a>

## 190.31 `CONFIG_NRF_WIFI_PATCHES_EXTERNAL`

**提示（Prompt）**：从外部二进制文件加载 nRF70 固件补丁

**说明（Help）**

通过外部工具加载 nRF70 固件（FW）补丁。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_WIFI_FW_BLOB_HANDLING>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → nRF70 固件二进制（Firmware Blob）处理

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_FW_BLOB_HANDLING`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_FW_BLOB_HANDLING)。

<a id="CONFIG_NRF_WIFI_PS_DATA_RETRIEVAL_MECHANISM"></a>

## 190.32 `CONFIG_NRF_WIFI_PS_DATA_RETRIEVAL_MECHANISM`

**提示（Prompt）**：节能数据获取机制（Power Save Data Retrieval Mechanism）

**说明（Help）**

选择从 AP 获取已缓冲数据的机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_NRF_WIFI_PS_POLL_BASED_RETRIEVAL
```

**可选项（Choices）**

```text
CONFIG_NRF_WIFI_PS_POLL_BASED_RETRIEVAL
CONFIG_NRF_WIFI_QOS_NULL_BASED_RETRIEVAL
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:866`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L866)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NRF_WIFI_PS_POLL_BASED_RETRIEVAL`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_PS_POLL_BASED_RETRIEVAL)、[`CONFIG_NRF_WIFI_QOS_NULL_BASED_RETRIEVAL`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_QOS_NULL_BASED_RETRIEVAL)。

<a id="CONFIG_NRF_WIFI_PS_EXIT_EVERY_TIM"></a>

## 190.33 `CONFIG_NRF_WIFI_PS_EXIT_EVERY_TIM`

**提示（Prompt）**：每次退出节能模式以取得 AP 缓冲的数据

**说明（Help）**

每次都退出节能模式（Power Save），以取得 AP 缓冲的数据。重新进入节能模式可能消耗一定时间和电能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_WIFI_PS_EXIT_STRATEGY>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:923`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L923)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → 节能退出策略（Power Save Exit Strategy）

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_PS_EXIT_STRATEGY`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_PS_EXIT_STRATEGY)。

<a id="CONFIG_NRF_WIFI_PS_EXIT_STRATEGY"></a>

## 190.34 `CONFIG_NRF_WIFI_PS_EXIT_STRATEGY`

**提示（Prompt）**：节能退出策略（Power Save Exit Strategy）

**说明（Help）**

选择退出节能模式（Power Save）以取得 AP 缓冲数据的策略。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_NRF_WIFI_PS_INT_PS
```

**可选项（Choices）**

```text
CONFIG_NRF_WIFI_PS_EXIT_EVERY_TIM
CONFIG_NRF_WIFI_PS_INT_PS
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:917`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L917)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NRF_WIFI_PS_INT_PS`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_PS_INT_PS)、[`CONFIG_NRF_WIFI_PS_EXIT_EVERY_TIM`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_PS_EXIT_EVERY_TIM)。

<a id="CONFIG_NRF_WIFI_PS_INT_PS"></a>

## 190.35 `CONFIG_NRF_WIFI_PS_INT_PS`

**提示（Prompt）**：根据智能算法退出节能模式

**说明（Help）**

根据智能算法退出节能模式（Power Save），以取得 AP 缓冲的数据。算法跟踪 AP 的缓冲数据量，动态决定在数据较少时保持节能状态（PS），或在数据较多时退出节能状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_WIFI_PS_EXIT_STRATEGY>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:929`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L929)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → 节能退出策略（Power Save Exit Strategy）

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_PS_EXIT_STRATEGY`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_PS_EXIT_STRATEGY)。

<a id="CONFIG_NRF_WIFI_PS_POLL_BASED_RETRIEVAL"></a>

## 190.36 `CONFIG_NRF_WIFI_PS_POLL_BASED_RETRIEVAL`

**提示（Prompt）**：基于 PS-Poll 帧获取 AP 缓冲数据的机制

**说明（Help）**

AP 通知存在已缓冲数据时，站点（STA）保持节能状态，并逐帧取回数据。这种方式更省电，但会增加流量延迟，适合帧数量很少的场景。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_WIFI_PS_DATA_RETRIEVAL_MECHANISM>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:872`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L872)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → 节能数据获取机制（Power Save Data Retrieval Mechanism）

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_PS_DATA_RETRIEVAL_MECHANISM`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_PS_DATA_RETRIEVAL_MECHANISM)。

<a id="CONFIG_NRF_WIFI_QOS_NOACK_POLICY"></a>

## 190.37 `CONFIG_NRF_WIFI_QOS_NOACK_POLICY`

**提示（Prompt）**：发送包的服务质量无确认策略（QoS No-ACK Policy）

**说明（Help）**

为指定流量标识符（TID）的发送包设置无确认策略（No-ACK Policy）。启用后，该 TID 的所有发送帧都带有 No-ACK 标志，表示接收方不应为这些包发送确认帧（ACK）。

应谨慎使用：对尽力而为（Best Effort，BE）或后台（Background，BK）类别启用 No-ACK，可能因不进行重试而导致 ARP/IP 等链路问题。理想用途是视频（Video，VI）或语音（Voice，VO）访问类别。应用必须通过服务类型（TOS）正确编码 TID，才能激活此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:840`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L840)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_QOS_NOACK_POLICY_TID"></a>

## 190.38 `CONFIG_NRF_WIFI_QOS_NOACK_POLICY_TID`

**提示（Prompt）**：无确认策略的流量标识符（Traffic Identifier，TID）

**说明（Help）**

指定应用无确认策略（No-ACK Policy）的流量标识符（TID）。TID 范围为 0 至 7，对应不同服务质量（QoS）优先级。具有此 TID 的所有发送帧都会标记 No-ACK 策略。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_WIFI_QOS_NOACK_POLICY && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:856`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L856)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → 发送包的服务质量无确认策略（QoS No-ACK Policy）

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_QOS_NOACK_POLICY`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_QOS_NOACK_POLICY)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_QOS_NULL_BASED_RETRIEVAL"></a>

## 190.39 `CONFIG_NRF_WIFI_QOS_NULL_BASED_RETRIEVAL`

**提示（Prompt）**：基于 QoS 空帧获取 AP 缓冲数据的机制

**说明（Help）**

AP 通知存在已缓冲数据时，站点（STA）退出节能模式，随后 AP 可发送所有已缓冲帧，无需额外开销或延迟。不过，站点要经过一段延迟才重新进入节能模式，因此会消耗更多电能，具体取决于延迟长度。适合缓冲流量较大的场景。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_WIFI_PS_DATA_RETRIEVAL_MECHANISM>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:879`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L879)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → 节能数据获取机制（Power Save Data Retrieval Mechanism）

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_PS_DATA_RETRIEVAL_MECHANISM`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_PS_DATA_RETRIEVAL_MECHANISM)。

<a id="CONFIG_NRF_WIFI_RPU_MIN_TIME_TO_ENTER_SLEEP_MS"></a>

## 190.40 `CONFIG_NRF_WIFI_RPU_MIN_TIME_TO_ENTER_SLEEP_MS`

**提示（Prompt）**：进入睡眠前的最短空闲时间，单位为毫秒

**说明（Help）**

假定没有活动，主机撤销 `WAKEUP_NOW` 并允许无线处理单元（RPU）进入睡眠模式之前的最短空闲时间。注意，较大的值可能增加功耗。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_WIFI_RPU_RECOVERY && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
5000
```

**取值范围（Ranges）**

```text
[100, 40000]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:791`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L791)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → 无线处理单元（RPU）恢复机制

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_RPU_RECOVERY`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_RPU_RECOVERY)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_RPU_RECOVERY"></a>

## 190.41 `CONFIG_NRF_WIFI_RPU_RECOVERY`

**提示（Prompt）**：无线处理单元（RPU）恢复机制

**说明（Help）**

启用无线处理单元（RPU）恢复机制，以从 RPU（nRF70）挂起状态恢复。此功能通过关闭再开启接口来复位接口，触发 RPU 冷启动（Cold Boot）。恢复期间，应用的网络连接会丢失，应用负责重新建立连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_WIFI_LOW_POWER && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:757`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L757)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_LOW_POWER`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_LOW_POWER)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_RPU_RECOVERY_DEBUG"></a>

## 190.42 `CONFIG_NRF_WIFI_RPU_RECOVERY_DEBUG`

**提示（Prompt）**：RPU 恢复调试日志

**说明（Help）**

启用 RPU 恢复调试日志，以帮助调试 RPU 恢复机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_WIFI_RPU_RECOVERY && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:800`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L800)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → 无线处理单元（RPU）恢复机制

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_RPU_RECOVERY`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_RPU_RECOVERY)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_RPU_RECOVERY_MAX_RETRIES"></a>

## 190.43 `CONFIG_NRF_WIFI_RPU_RECOVERY_MAX_RETRIES`

**提示（Prompt）**：连续 RPU 恢复重试的最大次数，0 表示禁用（原文表述）

**说明（Help）**

放弃恢复并复位系统之前，允许连续进行 RPU 恢复重试的最大次数。设为 0 时无限重试。

译注：标题原文写作“0 to disable”，帮助明确写作“0 to keep retrying indefinitely”。此处保留差异；帮助中的 0 表示不限制重试次数，而不是禁用恢复机制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_WIFI_RPU_RECOVERY && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:812`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L812)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → 无线处理单元（RPU）恢复机制

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_RPU_RECOVERY`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_RPU_RECOVERY)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_RPU_RECOVERY_PROPAGATION_DELAY_MS"></a>

## 190.44 `CONFIG_NRF_WIFI_RPU_RECOVERY_PROPAGATION_DELAY_MS`

**提示（Prompt）**：RPU 恢复传播延迟（Propagation Delay），单位为毫秒

**说明（Help）**

RPU 下电后、重新上电前等待的传播延迟（Propagation Delay），单位为毫秒。需要此延迟，以确保恢复事件传播到所有应用和协议栈，并为清理资源留出足够时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_WIFI_RPU_RECOVERY && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2000
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:770`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L770)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → 无线处理单元（RPU）恢复机制

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_RPU_RECOVERY`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_RPU_RECOVERY)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_RPU_RECOVERY_PS_ACTIVE_TIMEOUT_MS"></a>

## 190.45 `CONFIG_NRF_WIFI_RPU_RECOVERY_PS_ACTIVE_TIMEOUT_MS`

**提示（Prompt）**：RPU 恢复的节能活动超时，单位为毫秒

**说明（Help）**

节能活动超时（Power Save Active Timeout），单位为毫秒，超过后触发 RPU 恢复机制。用于确保没有活动时，RPU 会尝试进入节能模式。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_WIFI_RPU_RECOVERY && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
50000
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:783`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L783)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → 无线处理单元（RPU）恢复机制

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_RPU_RECOVERY`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_RPU_RECOVERY)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_RPU_RECOVERY_PS_STATE_DEBUG"></a>

## 190.46 `CONFIG_NRF_WIFI_RPU_RECOVERY_PS_STATE_DEBUG`

**提示（Prompt）**：RPU 恢复的节能状态调试日志

**说明（Help）**

启用 RPU 恢复的节能状态调试日志，以帮助调试 RPU 恢复机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_WIFI_RPU_RECOVERY && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:828`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L828)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → 无线处理单元（RPU）恢复机制

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_RPU_RECOVERY`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_RPU_RECOVERY)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_RPU_RECOVERY_QUIET_PERIOD_MS"></a>

## 190.47 `CONFIG_NRF_WIFI_RPU_RECOVERY_QUIET_PERIOD_MS`

**提示（Prompt）**：RPU 恢复静默期（Quiet Period），单位为毫秒

**说明（Help）**

触发 RPU 恢复后的静默期（Quiet Period），单位为毫秒。此期间不会触发新的 RPU 恢复。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_WIFI_RPU_RECOVERY && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:805`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L805)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → 无线处理单元（RPU）恢复机制

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_RPU_RECOVERY`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_RPU_RECOVERY)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_RPU_RECOVERY_RETRY_WINDOW_S"></a>

## 190.48 `CONFIG_NRF_WIFI_RPU_RECOVERY_RETRY_WINDOW_S`

**提示（Prompt）**：RPU 恢复重试窗口，单位为秒

**说明（Help）**

统计连续 RPU 恢复重试次数的时间窗口，单位为秒。若窗口内连续恢复重试次数超过 `NRF_WIFI_RPU_RECOVERY_MAX_RETRIES`，则复位系统。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_WIFI_RPU_RECOVERY && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
900
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:819`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L819)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → 无线处理单元（RPU）恢复机制

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_RPU_RECOVERY`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_RPU_RECOVERY)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_RX_STBC_HT"></a>

## 190.49 `CONFIG_NRF_WIFI_RX_STBC_HT`

**提示（Prompt）**：在高吞吐量（HT，Wi-Fi 4）模式下接收空时分组编码（STBC）数据包

**说明（Help）**

在高吞吐量（HT，Wi-Fi 4）模式下，接收使用空时分组编码（Space-Time Block Coding，STBC）的数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:993`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L993)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_SCAN_MAX_BSS_CNT"></a>

## 190.50 `CONFIG_NRF_WIFI_SCAN_MAX_BSS_CNT`

**提示（Prompt）**：返回的扫描结果最大数量

**说明（Help）**

返回的扫描结果最大数量。0 表示不限制基本服务集（BSS）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:693`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L693)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_TWT_SETUP_TIMEOUT_MS"></a>

## 190.51 `CONFIG_NRF_WIFI_TWT_SETUP_TIMEOUT_MS`

**提示（Prompt）**：目标唤醒时间（TWT）建立超时（ms）

**说明（Help）**

目标唤醒时间（TWT）建立流程的超时时长，单位为毫秒。站点（STA）每隔 100 ms 发送一次 TWT 建立请求，持续到达到此超时值。如果超时前未收到响应，则认为 TWT 建立失败。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
250
```

**取值范围（Ranges）**

```text
[100, 10000]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:1011`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L1011)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_USE_VARIABLE_NET_BUFS"></a>

## 190.52 `CONFIG_NRF_WIFI_USE_VARIABLE_NET_BUFS`

**提示（Prompt）**：使用可变网络缓冲区（Variable Network Buffers）

**说明（Help）**

在 nRF70 驱动中启用可变网络缓冲区（Variable Network Buffers），按数据大小分配不同尺寸的缓冲区，以优化 RAM 用量。此选项默认启用以节省 RAM；示例和应用可覆盖此设置，以获得更高性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:665`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L665)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF_WIFI_ZERO_COPY_TX"></a>

## 190.53 `CONFIG_NRF_WIFI_ZERO_COPY_TX`

**提示（Prompt）**：零拷贝发送通路（Zero-copy Transmit Path）

**说明（Help）**

启用零拷贝发送通路（Zero-copy Transmit Path）。驱动直接使用网络缓冲区发送，不再将数据复制到驱动缓冲区，可减少驱动堆内存用量，对性能影响不大。

应用应配置网络缓冲区，使整个数据包能够放进单个缓冲区。否则，驱动退回普通拷贝通路，但内存配置仍按零拷贝通路匹配，对普通拷贝通路而言可能并不理想。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_NRF54L
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:968`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L968)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_SOC_SERIES_NRF54L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM)。

<a id="CONFIG_NXP_88W8801"></a>

## 190.54 `CONFIG_NXP_88W8801`

**提示（Prompt）**：NXP 88W8801［实验性，EXPERIMENTAL］

**说明（Help）**

启用 NXP 88W8801 Wi-Fi 连接功能。器件详情请参阅 [NXP 88W8801 官方页面](https://www.nxp.com/products/wireless-connectivity/wi-fi-plus-bluetooth-plus-802-15-4/2-4-ghz-single-band-1x1-wi-fi-4-802-11n-solution:88W8801)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_WIFI_PART>
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP Wi-Fi 器件

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_PART`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_PART)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_NXP_88W8801_AW_NM191MA_M2"></a>

## 190.55 `CONFIG_NXP_88W8801_AW_NM191MA_M2`

**提示（Prompt）**：NXP AW-NM191MA-M2

**说明（Help）**

AzureWave Type NM191MA 是基于 NXP 88W8801 芯片组的小型高性能模块，集成印制电路板（PCB）天线，支持 Wi-Fi 802.11b/g/n，物理层（PHY）数据速率最高为 72.2 Mbps。详情请参阅 [AzureWave NXP 无线模块页面](https://www.azurewave.com/wireless-modules-nxp.html)。

译注：原文介绍模块时写作 AzureWave，介绍详情链接时却写作“Murata Type AW NM191MA”；链接仍指向 AzureWave，此处保留来源差异说明。

译注（引用状态）：AzureWave 原始引用在本次核验中返回 HTTP 404，未取得该外部页面正文。保留 Zephyr 原始链接；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_88W8801_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:355`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L355)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP 88W8801 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8801_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8801_MODULE)。

<a id="CONFIG_NXP_88W8801_AW_NM191_USD"></a>

## 190.56 `CONFIG_NXP_88W8801_AW_NM191_USD`

**提示（Prompt）**：NXP AW-NM191-USD

**说明（Help）**

AzureWave Type NM191 是基于 NXP 88W8801 芯片组的小型高性能模块，集成印制电路板（PCB）天线，支持 Wi-Fi 802.11b/g/n，物理层（PHY）数据速率最高为 72.2 Mbps。详情请参阅 [AzureWave NXP 无线模块页面](https://www.azurewave.com/wireless-modules-nxp.html)。

译注：原文介绍模块时写作 AzureWave，介绍详情链接时却写作“Murata Type AW NM191”；链接仍指向 AzureWave，此处保留来源差异说明。

译注（引用状态）：AzureWave 原始引用在本次核验中返回 HTTP 404，未取得该外部页面正文。保留 Zephyr 原始链接；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_88W8801_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:345`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L345)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP 88W8801 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8801_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8801_MODULE)。

<a id="CONFIG_NXP_88W8801_MODULE"></a>

## 190.57 `CONFIG_NXP_88W8801_MODULE`

**提示（Prompt）**：选择 NXP 88W8801 模块

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_88W8801 && !CONFIG_NXP_WIFI_CUSTOM && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**可选项（Choices）**

```text
CONFIG_NXP_88W8801_AW_NM191_USD
CONFIG_NXP_88W8801_AW_NM191MA_M2
CONFIG_NXP_88W8801_MURATA_2DS_USD
CONFIG_NXP_88W8801_MURATA_2DS_M2
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:341`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L341)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8801`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8801)、[`CONFIG_NXP_WIFI_CUSTOM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_CUSTOM)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_88W8801_AW_NM191_USD`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8801_AW_NM191_USD)、[`CONFIG_NXP_88W8801_AW_NM191MA_M2`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8801_AW_NM191MA_M2)、[`CONFIG_NXP_88W8801_MURATA_2DS_USD`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8801_MURATA_2DS_USD)、[`CONFIG_NXP_88W8801_MURATA_2DS_M2`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8801_MURATA_2DS_M2)。

<a id="CONFIG_NXP_88W8801_MURATA_2DS_M2"></a>

## 190.58 `CONFIG_NXP_88W8801_MURATA_2DS_M2`

**提示（Prompt）**：NXP MURATA-2DS-M2

**说明（Help）**

Murata Type 2DS 是基于 NXP 88W8801 芯片组的小型高性能模块，集成印制电路板（PCB）天线，支持 Wi-Fi 802.11b/g/n，物理层（PHY）数据速率最高为 72.2 Mbps。详情请参阅 [Murata Type 2DS 官方页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type2ds)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_88W8801_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:376`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L376)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP 88W8801 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8801_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8801_MODULE)。

<a id="CONFIG_NXP_88W8801_MURATA_2DS_USD"></a>

## 190.59 `CONFIG_NXP_88W8801_MURATA_2DS_USD`

**提示（Prompt）**：NXP MURATA-2DS-USD

**说明（Help）**

Murata Type 2DS 是基于 NXP 88W8801 芯片组的小型高性能模块，集成印制电路板（PCB）天线，支持 Wi-Fi 802.11b/g/n，物理层（PHY）数据速率最高为 72.2 Mbps。详情请参阅 [Murata Type 2DS 官方页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type2ds)和 [uSD-M.2 适配器页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/usd-m2-adapter)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_88W8801_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:365`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L365)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP 88W8801 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8801_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8801_MODULE)。

<a id="CONFIG_NXP_88W8987"></a>

## 190.60 `CONFIG_NXP_88W8987`

**提示（Prompt）**：NXP 88W8987［实验性，EXPERIMENTAL］

**说明（Help）**

启用 NXP 88W8987 Wi-Fi 连接功能。器件详情请参阅 [NXP 88W8987 官方页面](https://www.nxp.com/products/wireless-connectivity/wi-fi-plus-bluetooth-plus-802-15-4/2-4-5-ghz-dual-band-1x1-wi-fi-5-802-11ac-plus-bluetooth-5-2-solution:88W8987)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_WIFI_PART>
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP Wi-Fi 器件

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_PART`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_PART)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_NXP_88W8987_AW_CM358MA_M2"></a>

## 190.61 `CONFIG_NXP_88W8987_AW_CM358MA_M2`

**提示（Prompt）**：NXP AW-CM358MA-M2

**说明（Help）**

AzureWave Type CM358MA 模块基于 NXP 88W8987 组合 LGA 芯片组，支持 Wi-Fi 802.11a/b/g/n/ac 和蓝牙 5.1 BR/EDR/LE。Wi-Fi 物理层（PHY）数据速率最高为 433 Mbps，蓝牙最高为 3 Mbps。详情请参阅 [AzureWave NXP 无线模块页面](https://www.azurewave.com/wireless-modules-nxp.html)。

译注：原文介绍模块时写作 AzureWave，介绍详情链接时却写作“Murata Type AW CM358MA”；此处保留来源差异说明。

译注（引用状态）：AzureWave 原始引用在本次核验中返回 HTTP 404，未取得该外部页面正文。保留 Zephyr 原始链接；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_88W8987_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP 88W8987 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8987_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8987_MODULE)。

<a id="CONFIG_NXP_88W8987_AW_CM358_USD"></a>

## 190.62 `CONFIG_NXP_88W8987_AW_CM358_USD`

**提示（Prompt）**：NXP AW-CM358-USD

**说明（Help）**

AzureWave Type CM358 模块基于 NXP 88W8987 组合 LGA 芯片组，支持 Wi-Fi 802.11a/b/g/n/ac 和蓝牙 5.1 BR/EDR/LE。Wi-Fi 物理层（PHY）数据速率最高为 433 Mbps，蓝牙最高为 3 Mbps。详情请参阅 [AzureWave NXP 无线模块页面](https://www.azurewave.com/wireless-modules-nxp.html)。

译注（引用状态）：AzureWave 原始引用在本次核验中返回 HTTP 404，未取得该外部页面正文。保留 Zephyr 原始链接；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_88W8987_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP 88W8987 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8987_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8987_MODULE)。

<a id="CONFIG_NXP_88W8987_MODULE"></a>

## 190.63 `CONFIG_NXP_88W8987_MODULE`

**提示（Prompt）**：选择 NXP 88W8987 模块

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_88W8987 && !CONFIG_NXP_WIFI_CUSTOM && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**可选项（Choices）**

```text
CONFIG_NXP_88W8987_AW_CM358_USD
CONFIG_NXP_88W8987_AW_CM358MA_M2
CONFIG_NXP_88W8987_MURATA_1ZM_USD
CONFIG_NXP_88W8987_MURATA_1ZM_M2
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L114)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8987`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8987)、[`CONFIG_NXP_WIFI_CUSTOM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_CUSTOM)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_88W8987_AW_CM358_USD`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8987_AW_CM358_USD)、[`CONFIG_NXP_88W8987_AW_CM358MA_M2`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8987_AW_CM358MA_M2)、[`CONFIG_NXP_88W8987_MURATA_1ZM_USD`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8987_MURATA_1ZM_USD)、[`CONFIG_NXP_88W8987_MURATA_1ZM_M2`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8987_MURATA_1ZM_M2)。

<a id="CONFIG_NXP_88W8987_MURATA_1ZM_M2"></a>

## 190.64 `CONFIG_NXP_88W8987_MURATA_1ZM_M2`

**提示（Prompt）**：NXP MURATA-1ZM-M2

**说明（Help）**

Murata Type 1ZM 是基于 NXP 88W8987 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n/ac 和蓝牙 5.1 BR/EDR/LE。Wi-Fi 物理层（PHY）数据速率最高为 433 Mbps，蓝牙最高为 3 Mbps。详情请参阅 [Murata Type 1ZM 官方页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type1zm)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_88W8987_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP 88W8987 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8987_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8987_MODULE)。

<a id="CONFIG_NXP_88W8987_MURATA_1ZM_USD"></a>

## 190.65 `CONFIG_NXP_88W8987_MURATA_1ZM_USD`

**提示（Prompt）**：NXP MURATA-1ZM-USD

**说明（Help）**

Murata Type 1ZM 是基于 NXP 88W8987 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n/ac 和蓝牙 5.1 BR/EDR/LE。Wi-Fi 物理层（PHY）数据速率最高为 433 Mbps，蓝牙最高为 3 Mbps。详情请参阅 [Murata Type 1ZM 官方页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type1zm)和 [uSD-M.2 适配器页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/usd-m2-adapter)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_88W8987_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP 88W8987 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8987_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8987_MODULE)。

<a id="CONFIG_NXP_AW611_UBX_JODY_W5_M2"></a>

## 190.66 `CONFIG_NXP_AW611_UBX_JODY_W5_M2`

**提示（Prompt）**：NXP IW611-UBX-JODY-W5-M2

**说明（Help）**

u-blox JODY-W5 是小型高性能模块，原文称其基于 NXP AW611 组合芯片组，支持 Wi-Fi 802.11a/b/g/n/ac/ax 和蓝牙 5.3 BR/EDR/LE。系列详情请参阅 [u-blox JODY-W5 官方页面](https://www.u-blox.com/en/product/jody-w5-series)。

译注：此帮助使用 AW611；对应配置中还出现 IW611。型号拼写按原文保留。

译注（来源版本）：本条 Zephyr 官方快照记载蓝牙 5.3；本次打开所引厂商产品页时，该页已写为蓝牙 5.4。正文保留 Zephyr 快照的版本信息，不将当前产品页内容回填为原文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW61X_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:319`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L319)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW61X 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW61X_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X_MODULE)。

<a id="CONFIG_NXP_FW_DUMP_FLASH_ERASE_LENGTH"></a>

## 190.67 `CONFIG_NXP_FW_DUMP_FLASH_ERASE_LENGTH`

**提示（Prompt）**：用于存储固件转储的闪存擦除长度

**说明（Help）**

启用后，定义闪存区域中用于存储固件转储（FW Dump）的擦除长度。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_FW_DEBUG && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0x200000
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1460`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1460)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项 → 固件调试（FW Debug）

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_FW_DEBUG`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_FW_DEBUG)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_FW_DUMP_FLASH_START_ADDR"></a>

## 190.68 `CONFIG_NXP_FW_DUMP_FLASH_START_ADDR`

**提示（Prompt）**：存储固件转储的闪存起始地址

**说明（Help）**

启用后，定义闪存区域中用于存储固件转储（FW Dump）的起始地址。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_FW_DEBUG && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1453`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1453)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项 → 固件调试（FW Debug）

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_FW_DEBUG`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_FW_DEBUG)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_IW416"></a>

## 190.69 `CONFIG_NXP_IW416`

**提示（Prompt）**：NXP IW416［实验性，EXPERIMENTAL］

**说明（Help）**

启用 NXP IW416 Wi-Fi 连接功能。器件详情请参阅 [NXP IW416 官方页面](https://www.nxp.com/products/wireless-connectivity/wi-fi-plus-bluetooth-plus-802-15-4/2-4-5-ghz-dual-band-1x1-wi-fi-4-802-11n-plus-bluetooth-5-2-solution:IW416)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_WIFI_PART>
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP Wi-Fi 器件

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_PART`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_PART)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_NXP_IW416_AW_AM457MA_M2"></a>

## 190.70 `CONFIG_NXP_IW416_AW_AM457MA_M2`

**提示（Prompt）**：NXP IW416-AW-AM457MA-M2

**说明（Help）**

AzureWave Type AM457MA 是基于 NXP IW416 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n 和蓝牙 5.2 BR/EDR/LE。Wi-Fi 物理层（PHY）数据速率最高为 150 Mbps，蓝牙最高为 3 Mbps。详情请参阅 [AzureWave NXP 无线模块页面](https://www.azurewave.com/wireless-modules-nxp.html)。

译注（引用状态）：AzureWave 原始引用在本次核验中返回 HTTP 404，未取得该外部页面正文。保留 Zephyr 原始链接；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW416_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW416 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW416_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416_MODULE)。

<a id="CONFIG_NXP_IW416_AW_AM457_USD"></a>

## 190.71 `CONFIG_NXP_IW416_AW_AM457_USD`

**提示（Prompt）**：NXP IW416-AW-AM457-USD

**说明（Help）**

AzureWave Type AM457 是基于 NXP IW416 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n 和蓝牙 5.2 BR/EDR/LE。Wi-Fi 物理层（PHY）数据速率最高为 150 Mbps，蓝牙最高为 3 Mbps。详情请参阅 [AzureWave NXP 无线模块页面](https://www.azurewave.com/wireless-modules-nxp.html)。

译注（引用状态）：AzureWave 原始引用在本次核验中返回 HTTP 404，未取得该外部页面正文。保留 Zephyr 原始链接；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW416_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW416 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW416_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416_MODULE)。

<a id="CONFIG_NXP_IW416_AW_AM510MA_M2"></a>

## 190.72 `CONFIG_NXP_IW416_AW_AM510MA_M2`

**提示（Prompt）**：NXP IW416-AW-AM510MA-M2

**说明（Help）**

AzureWave Type AM510MA 是基于 NXP IW416 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n 和蓝牙 5.2 BR/EDR/LE。Wi-Fi 物理层（PHY）数据速率最高为 150 Mbps，蓝牙最高为 3 Mbps。详情请参阅 [AzureWave NXP 无线模块页面](https://www.azurewave.com/wireless-modules-nxp.html)。

译注（引用状态）：AzureWave 原始引用在本次核验中返回 HTTP 404，未取得该外部页面正文。保留 Zephyr 原始链接；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW416_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW416 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW416_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416_MODULE)。

<a id="CONFIG_NXP_IW416_AW_AM510_USD"></a>

## 190.73 `CONFIG_NXP_IW416_AW_AM510_USD`

**提示（Prompt）**：NXP IW416-AW-AM510-USD

**说明（Help）**

AzureWave Type AM510 是基于 NXP IW416 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n 和蓝牙 5.2 BR/EDR/LE。Wi-Fi 物理层（PHY）数据速率最高为 150 Mbps，蓝牙最高为 3 Mbps。详情请参阅 [AzureWave NXP 无线模块页面](https://www.azurewave.com/wireless-modules-nxp.html)。

译注（引用状态）：AzureWave 原始引用在本次核验中返回 HTTP 404，未取得该外部页面正文。保留 Zephyr 原始链接；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW416_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:191`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L191)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW416 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW416_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416_MODULE)。

<a id="CONFIG_NXP_IW416_MODULE"></a>

## 190.74 `CONFIG_NXP_IW416_MODULE`

**提示（Prompt）**：选择 NXP IW416 模块

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_IW416 && !CONFIG_NXP_WIFI_CUSTOM && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**可选项（Choices）**

```text
CONFIG_NXP_IW416_AW_AM457_USD
CONFIG_NXP_IW416_AW_AM457MA_M2
CONFIG_NXP_IW416_AW_AM510_USD
CONFIG_NXP_IW416_AW_AM510MA_M2
CONFIG_NXP_IW416_MURATA_1XK_USD
CONFIG_NXP_IW416_MURATA_1XK_M2
CONFIG_NXP_IW416_UBX_MAYA_W1_USD
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
CONFIG_NXP_IW416_MURATA_1XK_M2
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:165`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L165)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW416`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416)、[`CONFIG_NXP_WIFI_CUSTOM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_CUSTOM)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_IW416_AW_AM457_USD`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416_AW_AM457_USD)、[`CONFIG_NXP_IW416_AW_AM457MA_M2`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416_AW_AM457MA_M2)、[`CONFIG_NXP_IW416_AW_AM510_USD`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416_AW_AM510_USD)、[`CONFIG_NXP_IW416_AW_AM510MA_M2`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416_AW_AM510MA_M2)、[`CONFIG_NXP_IW416_MURATA_1XK_USD`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416_MURATA_1XK_USD)、[`CONFIG_NXP_IW416_MURATA_1XK_M2`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416_MURATA_1XK_M2)、[`CONFIG_NXP_IW416_UBX_MAYA_W1_USD`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416_UBX_MAYA_W1_USD)。

<a id="CONFIG_NXP_IW416_MURATA_1XK_M2"></a>

## 190.75 `CONFIG_NXP_IW416_MURATA_1XK_M2`

**提示（Prompt）**：NXP IW416-MURATA-1XK-M2

**说明（Help）**

Murata Type 1XK 是基于 NXP IW416 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n 和蓝牙 5.2 BR/EDR/LE。Wi-Fi 物理层（PHY）数据速率最高为 150 Mbps，蓝牙最高为 3 Mbps。详情请参阅 [Murata Type 1XK 官方页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type1xk)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW416_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:225`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L225)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW416 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW416_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416_MODULE)。

<a id="CONFIG_NXP_IW416_MURATA_1XK_USD"></a>

## 190.76 `CONFIG_NXP_IW416_MURATA_1XK_USD`

**提示（Prompt）**：NXP IW416-MURATA-1XK-USD

**说明（Help）**

Murata Type 1XK 是基于 NXP IW416 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n 和蓝牙 5.2 BR/EDR/LE。Wi-Fi 物理层（PHY）数据速率最高为 150 Mbps，蓝牙最高为 3 Mbps。详情请参阅 [Murata Type 1XK 官方页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type1xk)和 [uSD-M.2 适配器页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/usd-m2-adapter)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW416_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:213`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L213)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW416 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW416_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416_MODULE)。

<a id="CONFIG_NXP_IW416_UBX_MAYA_W1_USD"></a>

## 190.77 `CONFIG_NXP_IW416_UBX_MAYA_W1_USD`

**提示（Prompt）**：NXP IW416-UBX-MAYA-W1-USD

**说明（Help）**

u-blox MAYA-W1 系列是基于 NXP IW416 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n 和蓝牙 5.2 BR/EDR/LE。Wi-Fi 物理层（PHY）数据速率最高为 150 Mbps，蓝牙最高为 3 Mbps。EVK-MAYA-W1 详情请参阅 [u-blox MAYA-W1 系列页面](https://www.u-blox.com/en/product/maya-w1-series)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW416_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:236`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L236)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW416 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW416_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416_MODULE)。

<a id="CONFIG_NXP_IW610"></a>

## 190.78 `CONFIG_NXP_IW610`

**提示（Prompt）**：NXP IW610

**说明（Help）**

启用 NXP IW610 Wi-Fi 连接功能。器件详情请参阅 [NXP IW610 官方页面](https://www.nxp.com/products/wireless-connectivity/wi-fi-plus-bluetooth-plus-802-15-4/2-4-5ghz-dual-band-1x1-wi-fi-6-plus-bluetooth-low-energy-5-4-plus-802-15-4-tri-radio-solution:IW610)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_WIFI_PART>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP Wi-Fi 器件

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_PART`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_PART)。

<a id="CONFIG_NXP_IW610_MODULE"></a>

## 190.79 `CONFIG_NXP_IW610_MODULE`

**提示（Prompt）**：选择 NXP IW610 模块

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_IW610 && !CONFIG_NXP_WIFI_CUSTOM && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**可选项（Choices）**

```text
CONFIG_NXP_IW610_MURATA_2LL_M2
CONFIG_NXP_IW610_RD_USD
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
CONFIG_NXP_IW610_MURATA_2LL_M2
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:388`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L388)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_NXP_WIFI_CUSTOM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_CUSTOM)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_IW610_MURATA_2LL_M2`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610_MURATA_2LL_M2)、[`CONFIG_NXP_IW610_RD_USD`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610_RD_USD)。

<a id="CONFIG_NXP_IW610_MURATA_2LL_M2"></a>

## 190.80 `CONFIG_NXP_IW610_MURATA_2LL_M2`

**提示（Prompt）**：NXP IW610-MURATA-2LL-M2

**说明（Help）**

Murata Type 2LL 是基于 NXP IW610G 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n/ac/ax HE20、蓝牙 5.4 低功耗（Bluetooth Low Energy）和 802.15.4。Wi-Fi 物理层（PHY）数据速率最高为 114.7 Mbps，低功耗蓝牙最高为 2 Mbps。详情请参阅 [Murata Type 2LL 官方页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type2ll)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW610_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:392`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L392)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW610 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW610_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610_MODULE)。

<a id="CONFIG_NXP_IW610_RD_USD"></a>

## 190.81 `CONFIG_NXP_IW610_RD_USD`

**提示（Prompt）**：NXP IW610-RD-USD［实验性，EXPERIMENTAL］

**说明（Help）**

IW610 系列具有 1×1 双频（2.4 GHz／5 GHz）Wi-Fi 6 无线子系统。相比先前 Wi-Fi 标准，可提高网络效率、降低延迟并扩展覆盖范围。其低功耗蓝牙（Bluetooth LE）无线电支持 2 Mbit/s 高速数据率，以及用于网络配置（Network Commissioning）和传感器汇聚（Sensor Aggregation）的远距离通信和扩展广播（Extended Advertising）。Type RD USD 模块详情请参阅 [NXP IW610CHN 官方页面](https://www.nxp.com/part/IW610CHN)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW610_MODULE>
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:403`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L403)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW610 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW610_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610_MODULE)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_NXP_IW611_MURATA_2DL_M2"></a>

## 190.82 `CONFIG_NXP_IW611_MURATA_2DL_M2`

**提示（Prompt）**：NXP IW611-MURATA-2DL-M2

**说明（Help）**

Murata Type 2DL 是基于 NXP IW611 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n/ac/ax 和蓝牙 5.3 BR/EDR/LE。Wi-Fi 物理层（PHY）数据速率最高为 601 Mbps，蓝牙最高为 2 Mbps。详情请参阅 [Murata Type 2DL 官方页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type2dl)。

译注（来源版本）：本条 Zephyr 官方快照记载蓝牙 5.3；本次打开所引厂商产品页时，该页已写为蓝牙 5.4。正文保留 Zephyr 快照的版本信息，不将当前产品页内容回填为原文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW61X_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:288`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L288)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW61X 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW61X_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X_MODULE)。

<a id="CONFIG_NXP_IW611_MURATA_2DL_USD"></a>

## 190.83 `CONFIG_NXP_IW611_MURATA_2DL_USD`

**提示（Prompt）**：NXP IW611-MURATA-2DL-USD

**说明（Help）**

Murata Type 2DL 是基于 NXP IW611 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n/ac/ax 和蓝牙 5.3 BR/EDR/LE。Wi-Fi 物理层（PHY）数据速率最高为 601 Mbps，蓝牙最高为 2 Mbps。详情请参阅 [Murata Type 2DL 官方页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type2dl)和 [uSD-M.2 适配器页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/usd-m2-adapter)。

译注（来源版本）：本条 Zephyr 官方快照记载蓝牙 5.3；本次打开所引厂商产品页时，该页已写为蓝牙 5.4。正文保留 Zephyr 快照的版本信息，不将当前产品页内容回填为原文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW61X_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:276`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L276)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW61X 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW61X_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X_MODULE)。

<a id="CONFIG_NXP_IW611_UBX_JODY_W5_USD"></a>

## 190.84 `CONFIG_NXP_IW611_UBX_JODY_W5_USD`

**提示（Prompt）**：NXP AW611-UBX-JODY-W5-USD

**说明（Help）**

u-blox JODY-W5 是小型高性能模块，原文称其基于 NXP AW611 组合芯片组，支持 Wi-Fi 802.11a/b/g/n/ac/ax 和蓝牙 5.3 BR/EDR/LE。系列详情请参阅 [u-blox JODY-W5 官方页面](https://www.u-blox.com/en/product/jody-w5-series)。

译注：此帮助使用 AW611；对应配置中还出现 IW611。型号拼写按原文保留。

译注（来源版本）：本条 Zephyr 官方快照记载蓝牙 5.3；本次打开所引厂商产品页时，该页已写为蓝牙 5.4。正文保留 Zephyr 快照的版本信息，不将当前产品页内容回填为原文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW61X_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:309`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L309)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW61X 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW61X_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X_MODULE)。

<a id="CONFIG_NXP_IW612_MURATA_2EL_M2"></a>

## 190.85 `CONFIG_NXP_IW612_MURATA_2EL_M2`

**提示（Prompt）**：NXP IW612-MURATA-2EL-M2

**说明（Help）**

Murata Type 2EL 是基于 NXP IW612 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n/ac/ax、蓝牙 5.3 BR/EDR/LE 和 802.15.4。Wi-Fi 物理层（PHY）数据速率最高为 601 Mbps，蓝牙最高为 2 Mbps。详情请参阅 [Murata Type 2EL 官方页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type2el)。

译注（来源版本）：本条 Zephyr 官方快照记载蓝牙 5.3；本次打开所引厂商产品页时，该页已写为蓝牙 5.4。正文保留 Zephyr 快照的版本信息，不将当前产品页内容回填为原文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW61X_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L265)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW61X 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW61X_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X_MODULE)。

<a id="CONFIG_NXP_IW612_MURATA_2EL_USD"></a>

## 190.86 `CONFIG_NXP_IW612_MURATA_2EL_USD`

**提示（Prompt）**：NXP IW612-MURATA-2EL-USD

**说明（Help）**

Murata Type 2EL 是基于 NXP IW612 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n/ac/ax、蓝牙 5.3 BR/EDR/LE 和 802.15.4。Wi-Fi 物理层（PHY）数据速率最高为 601 Mbps，蓝牙最高为 2 Mbps。详情请参阅 [Murata Type 2EL 官方页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type2el)和 [uSD-M.2 适配器页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/usd-m2-adapter)。

译注（来源版本）：本条 Zephyr 官方快照记载蓝牙 5.3；本次打开所引厂商产品页时，该页已写为蓝牙 5.4。正文保留 Zephyr 快照的版本信息，不将当前产品页内容回填为原文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW61X_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:253`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L253)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW61X 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW61X_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X_MODULE)。

<a id="CONFIG_NXP_IW612_QUECTEL_FGS060N_USD"></a>

## 190.87 `CONFIG_NXP_IW612_QUECTEL_FGS060N_USD`

**提示（Prompt）**：NXP IW612-QUECTEL-FGS060N

**说明（Help）**

Quectel FGS060N 是基于 NXP IW612 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n/ac/ax、蓝牙 5.3 BR/EDR/LE 和 802.15.4。详情请参阅 [Quectel FGS060N 官方页面](https://www.quectel.com/product/wifi-bt-fgs060n)。

译注（引用状态）：Quectel 原始引用在本次直接请求中返回 HTTP 404，网页工具也未能取得正文。保留 Zephyr 原始链接；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW61X_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:329`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L329)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW61X 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW61X_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X_MODULE)。

<a id="CONFIG_NXP_IW612_UBX_MAYA_W276_M2"></a>

## 190.88 `CONFIG_NXP_IW612_UBX_MAYA_W276_M2`

**提示（Prompt）**：NXP IW612-UBX-MAYA-W276-M2

**说明（Help）**

u-blox MAYA-W276 是基于 NXP IW612 组合芯片组的小型高性能模块，支持 Wi-Fi 802.11a/b/g/n/ac/ax、蓝牙 5.3 BR/EDR/LE 和 802.15.4。系列详情请参阅 [u-blox MAYA-W2 官方页面](https://www.u-blox.com/en/product/maya-w2-series)。

译注（来源版本）：本条 Zephyr 官方快照记载蓝牙 5.3；本次打开所引厂商产品页时，该页已写为蓝牙 5.4。正文保留 Zephyr 快照的版本信息，不将当前产品页内容回填为原文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_IW61X_MODULE>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:299`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L299)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP IW61X 模块

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW61X_MODULE`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X_MODULE)。

<a id="CONFIG_NXP_IW61X"></a>

## 190.89 `CONFIG_NXP_IW61X`

**提示（Prompt）**：NXP IW61X［实验性，EXPERIMENTAL］

**说明（Help）**

启用 NXP IW61X Wi-Fi 连接功能。器件详情请参阅 [NXP IW611 官方页面](https://www.nxp.com/products/wireless-connectivity/wi-fi-plus-bluetooth-plus-802-15-4/2-4-5ghz-dual-band-1x1-wi-fi-6-802-11ax-plus-bluetooth-5-2-solution:IW611)和 [NXP IW612 官方页面](https://www.nxp.com/products/wireless-connectivity/wi-fi-plus-bluetooth-plus-802-15-4/2-4-5-ghz-dual-band-1x1-wi-fi-6-802-11ax-plus-bluetooth-5-2-plus-802-15-4-tri-radio-solution:IW612)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_WIFI_PART>
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP Wi-Fi 器件

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_PART`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_PART)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_NXP_IW61X_MODULE"></a>

## 190.90 `CONFIG_NXP_IW61X_MODULE`

**提示（Prompt）**：选择 NXP IW61X 模块

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_IW61X && !CONFIG_NXP_WIFI_CUSTOM && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**可选项（Choices）**

```text
CONFIG_NXP_IW612_MURATA_2EL_USD
CONFIG_NXP_IW612_MURATA_2EL_M2
CONFIG_NXP_IW611_MURATA_2DL_USD
CONFIG_NXP_IW611_MURATA_2DL_M2
CONFIG_NXP_IW612_UBX_MAYA_W276_M2
CONFIG_NXP_IW611_UBX_JODY_W5_USD
CONFIG_NXP_AW611_UBX_JODY_W5_M2
CONFIG_NXP_IW612_QUECTEL_FGS060N_USD
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
CONFIG_NXP_IW612_MURATA_2EL_M2
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:249`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L249)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_NXP_WIFI_CUSTOM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_CUSTOM)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_IW612_MURATA_2EL_USD`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW612_MURATA_2EL_USD)、[`CONFIG_NXP_IW612_MURATA_2EL_M2`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW612_MURATA_2EL_M2)、[`CONFIG_NXP_IW611_MURATA_2DL_USD`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW611_MURATA_2DL_USD)、[`CONFIG_NXP_IW611_MURATA_2DL_M2`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW611_MURATA_2DL_M2)、[`CONFIG_NXP_IW612_UBX_MAYA_W276_M2`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW612_UBX_MAYA_W276_M2)、[`CONFIG_NXP_IW611_UBX_JODY_W5_USD`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW611_UBX_JODY_W5_USD)、[`CONFIG_NXP_AW611_UBX_JODY_W5_M2`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_AW611_UBX_JODY_W5_M2)、[`CONFIG_NXP_IW612_QUECTEL_FGS060N_USD`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW612_QUECTEL_FGS060N_USD)。

<a id="CONFIG_NXP_LIBCSI_CM33"></a>

## 190.91 `CONFIG_NXP_LIBCSI_CM33`

**提示（Prompt）**：CSI 库支持 CM33

**说明（Help）**

构建包含 CM33 CSI 库支持的镜像。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_CSI_AMI && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**被选择（Selected by）**

```text
CONFIG_NXP_WIFI_CSI_AMI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:868`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L868)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_CSI_AMI`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_CSI_AMI)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_LIBCSI_CM7_20M"></a>

## 190.92 `CONFIG_NXP_LIBCSI_CM7_20M`

**提示（Prompt）**：CSI 库支持 CM7、20M 带宽

**说明（Help）**

构建包含 CM7 CSI 库支持、带宽为 20M 的镜像；带宽写法按原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_CSI_AMI && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**被选择（Selected by）**

```text
CONFIG_NXP_WIFI_CSI_AMI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:874`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L874)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_CSI_AMI`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_CSI_AMI)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_MONOLITHIC_WIFI"></a>

## 190.93 `CONFIG_NXP_MONOLITHIC_WIFI`

**提示（Prompt）**：Wi-Fi 固件整体构建（Monolithic Build）

**说明（Help）**

启用后，设备使用的 Wi-Fi 固件直接与应用链接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NXP_WIFI_CUSTOM && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_CUSTOM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_CUSTOM)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_OVERRIDE_CALIBRATION_DATA"></a>

## 190.94 `CONFIG_NXP_OVERRIDE_CALIBRATION_DATA`

**提示（Prompt）**：覆盖默认校准数据（Calibration Data）

**说明（Help）**

此选项用于覆盖默认校准数据（Calibration Data）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:955`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L955)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_RW610"></a>

## 190.95 `CONFIG_NXP_RW610`

**提示（Prompt）**：基于 NXP RW610 的芯片组

**说明（Help）**

使用基于 NXP RW610 的无线芯片时，选择此选项。它将启用基于 NXP RW610 的系列开发板支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RW6XX && <choice CONFIG_NXP_WIFI_PART>
```

**主动选择（Selects）**

```text
CONFIG_NXP_FW_LOADER
CONFIG_NXP_RF_IMU
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 选择 NXP Wi-Fi 器件

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_NXP_WIFI_PART`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_PART)、[`CONFIG_NXP_FW_LOADER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_FW_LOADER)、[`CONFIG_NXP_RF_IMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_RF_IMU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_NXP_WIFI_11AC"></a>

## 190.96 `CONFIG_NXP_WIFI_11AC`

**提示（Prompt）**：802.11ac 支持

**说明（Help）**

启用 802.11ac 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NXP_RW610 || CONFIG_NXP_IW61X || CONFIG_NXP_88W8987 || CONFIG_NXP_IW610 || CONFIG_NXP_WIFI_CUSTOM) && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NXP_WIFI_WMM
```

**被选择（Selected by）**

```text
CONFIG_NXP_WIFI_11AX
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:768`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L768)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_NXP_88W8987`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8987)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_NXP_WIFI_CUSTOM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_CUSTOM)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_WMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_WIFI_WMM)、[`CONFIG_NXP_WIFI_11AX`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_WIFI_11AX)。

<a id="CONFIG_NXP_WIFI_11AX"></a>

## 190.97 `CONFIG_NXP_WIFI_11AX`

**提示（Prompt）**：802.11ax 支持

**说明（Help）**

启用 802.11ax 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NXP_RW610 || CONFIG_NXP_IW61X || CONFIG_NXP_IW610 || CONFIG_NXP_WIFI_CUSTOM) && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NXP_WIFI_11AC
CONFIG_NXP_WIFI_WMM
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:759`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L759)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_NXP_WIFI_CUSTOM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_CUSTOM)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_11AC`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_WIFI_11AC)、[`CONFIG_NXP_WIFI_WMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_WIFI_WMM)。

<a id="CONFIG_NXP_WIFI_11AX_TWT"></a>

## 190.98 `CONFIG_NXP_WIFI_11AX_TWT`

**提示（Prompt）**：802.11ax 目标唤醒时间（TWT）支持

**说明（Help）**

在 Wi-Fi 驱动中启用 802.11ax 目标唤醒时间（TWT）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_11AX && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1065`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1065)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_11AX`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_WIFI_11AX)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_11K"></a>

## 190.99 `CONFIG_NXP_WIFI_11K`

**提示（Prompt）**：802.11k 支持

**说明（Help）**

启用 802.11k 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:646`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L646)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_11R"></a>

## 190.100 `CONFIG_NXP_WIFI_11R`

**提示（Prompt）**：802.11r 支持

**说明（Help）**

启用 802.11r 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if !CONFIG_NXP_WIFI_SLIM
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:658`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L658)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_SLIM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SLIM)。

<!-- kconfig-navigation -->

[上一章](P189_drivers_wifi_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P191_drivers_wifi_配置项参考_4.md)
