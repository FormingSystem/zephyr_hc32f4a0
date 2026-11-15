---
id: learning.zephyr-docs.kconfig-reference.page-191
title: "`drivers/wifi`配置项参考（4/7）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第191章\_`drivers/wifi`配置项参考（4/7）

本章翻译官方 Kconfig 数据库中 `drivers/wifi` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NXP_WIFI_11V"></a>

## 191.1 `CONFIG_NXP_WIFI_11V`

**提示（Prompt）**：802.11v 支持

**说明（Help）**

启用 802.11v 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:652`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L652)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_5GHz_SUPPORT"></a>

## 191.2 `CONFIG_NXP_WIFI_5GHz_SUPPORT`

**提示（Prompt）**：5 GHz 支持（A 频段，Band A）

**说明（Help）**

启用 5 GHz 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NXP_88W8801 && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:835`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L835)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8801`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8801)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_AMPDU_DEBUG"></a>

## 191.3 `CONFIG_NXP_WIFI_AMPDU_DEBUG`

**提示（Prompt）**：聚合 MAC 协议数据单元（A-MPDU）调试

**说明（Help）**

启用后，可监测聚合 MAC 协议数据单元接收（A-MPDU RX）包的处理情况。注意，此驱动不支持 A-MPDU 发送（TX）。若要观察乱序包（Out-of-order Packets）处理期间的定时器活动，还需单独启用定时器调试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1414`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1414)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_ANT_DETECT"></a>

## 191.4 `CONFIG_NXP_WIFI_ANT_DETECT`

**提示（Prompt）**：天线自动检测（Antenna Automatic Detection）

**说明（Help）**

自动检测存在的两根天线，然后向固件配置对应的评估模式 Mode-X（原文：evaluate Mode-X），并启用天线分集（Antenna Diversity）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_RW610 && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1034`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1034)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_AUTO_INIT"></a>

## 191.5 `CONFIG_NXP_WIFI_AUTO_INIT`

**提示（Prompt）**：自动初始化 NXP Wi-Fi

**说明（Help）**

自动初始化 NXP Wi-Fi 驱动和固件（FW）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_AUTO_NULL_TX"></a>

## 191.6 `CONFIG_NXP_WIFI_AUTO_NULL_TX`

**提示（Prompt）**：自动发送空帧（Null Frame）

**说明（Help）**

支持为信道状态信息（CSI）周期性发送空帧（Null Frame）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NXP_RW610 || CONFIG_NXP_IW610
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:981`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L981)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)。

<a id="CONFIG_NXP_WIFI_AUTO_POWER_SAVE"></a>

## 191.7 `CONFIG_NXP_WIFI_AUTO_POWER_SAVE`

**提示（Prompt）**：自动启动节能支持（Power Save）

**说明（Help）**

Wi-Fi 驱动初始化时自动启动节能（Power Save）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:562`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L562)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_CCK_DESENSE_CFG"></a>

## 191.8 `CONFIG_NXP_WIFI_CCK_DESENSE_CFG`

**提示（Prompt）**：补码键控降敏模式（CCK Desense Mode）支持

**说明（Help）**

在 Wi-Fi 驱动中启用补码键控降敏模式（CCK Desense Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NXP_RW610 || CONFIG_NXP_IW610
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1013`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1013)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)。

<a id="CONFIG_NXP_WIFI_CHANNEL_LOAD"></a>

## 191.9 `CONFIG_NXP_WIFI_CHANNEL_LOAD`

**提示（Prompt）**：信道负载（Channel Load）设置支持

**说明（Help）**

启用信道负载（Channel Load）设置支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:671`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L671)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_CLOCKSYNC"></a>

## 191.10 `CONFIG_NXP_WIFI_CLOCKSYNC`

**提示（Prompt）**：使用时间同步功能锁存（TSF Latch）进行时钟同步

**说明（Help）**

启用时间同步功能锁存（TSF Latch）的时钟同步。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NXP_RW610 || CONFIG_NXP_IW61X || CONFIG_NXP_IW610 || CONFIG_NXP_IW416) && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1116)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_NXP_IW416`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_CLOUD_KEEP_ALIVE"></a>

## 191.11 `CONFIG_NXP_WIFI_CLOUD_KEEP_ALIVE`

**提示（Prompt）**：云端保活（Cloud Keep Alive）

**说明（Help）**

在 Wi-Fi 驱动中启用云端保活（Cloud Keep Alive）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:641`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L641)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_CMD_RESP_DEBUG"></a>

## 191.12 `CONFIG_NXP_WIFI_CMD_RESP_DEBUG`

**提示（Prompt）**：转储命令码和响应码（Command and Response Codes）

**说明（Help）**

分别转储发送给固件的命令码，以及从固件接收的响应码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1353`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1353)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_COEX_DUTY_CYCLE"></a>

## 191.13 `CONFIG_NXP_WIFI_COEX_DUTY_CYCLE`

**提示（Prompt）**：设置占空比（Duty Cycle）

**说明（Help）**

在 Wi-Fi 驱动中设置占空比（Duty Cycle）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NXP_RW610 || CONFIG_NXP_IW610
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1019`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1019)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)。

<a id="CONFIG_NXP_WIFI_COMPRESS_RU_TX_PWTBL"></a>

## 191.14 `CONFIG_NXP_WIFI_COMPRESS_RU_TX_PWTBL`

**提示（Prompt）**：压缩资源单元发射功率表（Compress RU TX Power Table）支持

**说明（Help）**

启用压缩资源单元发射功率表（Compress RU TX Power Table）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NXP_IW416 && (CONFIG_NXP_RW610 || CONFIG_NXP_IW61X || CONFIG_NXP_IW610 || CONFIG_NXP_IW416) && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1128)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_IW416`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_COMPRESS_TX_PWTBL"></a>

## 191.15 `CONFIG_NXP_WIFI_COMPRESS_TX_PWTBL`

**提示（Prompt）**：压缩发射功率表（Compress TX Power Table）支持

**说明（Help）**

启用压缩发射功率表（Compress TX Power Table）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NXP_RW610 || CONFIG_NXP_IW61X || CONFIG_NXP_IW610 || CONFIG_NXP_IW416) && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1122)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_NXP_IW416`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_CORE_TASK_STACK_SIZE"></a>

## 191.16 `CONFIG_NXP_WIFI_CORE_TASK_STACK_SIZE`

**提示（Prompt）**：Wi-Fi 核心任务栈大小

**说明（Help）**

指定 Wi-Fi 核心任务（Core Task）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:459`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L459)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 驱动栈配置（Stack Configurations）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_CSI"></a>

## 191.17 `CONFIG_NXP_WIFI_CSI`

**提示（Prompt）**：信道状态信息（CSI）支持

**说明（Help）**

启用／禁用信道状态信息（Channel State Information，CSI）采集。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if !CONFIG_NXP_WIFI_SLIM
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:862`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L862)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_SLIM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SLIM)。

<a id="CONFIG_NXP_WIFI_CSI_AMI"></a>

## 191.18 `CONFIG_NXP_WIFI_CSI_AMI`

**提示（Prompt）**：CSI 环境运动指数（AMI）支持

**说明（Help）**

启用／禁用使用信道状态信息（CSI）计算环境运动指数（Ambient Motion Index，AMI）的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_CSI && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_FPU
CONFIG_NXP_LIBCSI_CM33 if CONFIG_NXP_RW610
CONFIG_NXP_LIBCSI_CM7_20M if CONFIG_NXP_IW610
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:880`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L880)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_CSI`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_CSI)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_NXP_LIBCSI_CM33`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_LIBCSI_CM33)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_LIBCSI_CM7_20M`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_LIBCSI_CM7_20M)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)。

<a id="CONFIG_NXP_WIFI_CUSTOM"></a>

## 191.19 `CONFIG_NXP_WIFI_CUSTOM`

**提示（Prompt）**：自定义 NXP Wi-Fi 器件

**说明（Help）**

自定义 NXP Wi-Fi 芯片支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_CUSTOM_CALDATA"></a>

## 191.20 `CONFIG_NXP_WIFI_CUSTOM_CALDATA`

**提示（Prompt）**：由驱动设置校准数据（Caldata）

**说明（Help）**

强制使用自定义校准数据（Calibration Data）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1182)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_CUSTOM_HOST"></a>

## 191.21 `CONFIG_NXP_WIFI_CUSTOM_HOST`

**提示（Prompt）**：NXP Wi-Fi 的自定义主机平台

**说明（Help）**

为 NXP Wi-Fi 自定义主机平台，例如采用非 NXP 主机平台。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NXP_RW610 && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_BOARD_NATIVE_SIM
y if !CONFIG_HAS_MCUX && !CONFIG_HAS_IMX_HAL && !CONFIG_HAS_NXP_S32_HAL
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_BOARD_NATIVE_SIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NATIVE_SIM)、[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_HAS_IMX_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_IMX_HAL)、[`CONFIG_HAS_NXP_S32_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NXP_S32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NATIVE_SIM`、`CONFIG_HAS_MCUX`、`CONFIG_HAS_IMX_HAL`、`CONFIG_HAS_NXP_S32_HAL`。

<a id="CONFIG_NXP_WIFI_DRIVER_TASK_PRIO"></a>

## 191.22 `CONFIG_NXP_WIFI_DRIVER_TASK_PRIO`

**提示（Prompt）**：Wi-Fi 驱动任务优先级

**说明（Help）**

指定 Wi-Fi 驱动任务的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:504`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L504)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 线程优先级配置

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_DRIVER_TASK_STACK_SIZE"></a>

## 191.23 `CONFIG_NXP_WIFI_DRIVER_TASK_STACK_SIZE`

**提示（Prompt）**：Wi-Fi 驱动任务栈大小

**说明（Help）**

指定 Wi-Fi 驱动任务使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:453`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L453)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 驱动栈配置（Stack Configurations）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_DTIM_PERIOD"></a>

## 191.24 `CONFIG_NXP_WIFI_DTIM_PERIOD`

**提示（Prompt）**：Wi-Fi 投递流量指示消息（DTIM）周期

**说明（Help）**

设置 Wi-Fi 驱动中的投递流量指示消息（DTIM）周期。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1079`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1079)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_ECSA"></a>

## 191.25 `CONFIG_NXP_WIFI_ECSA`

**提示（Prompt）**：扩展信道切换公告（ECSA）

**说明（Help）**

按照规范执行信道切换（Channel Switch）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_SOFTAP_SUPPORT && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:913`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L913)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_SOFTAP_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_WIFI_SOFTAP_SUPPORT)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_ENABLE_ERROR_LOGS"></a>

## 191.26 `CONFIG_NXP_WIFI_ENABLE_ERROR_LOGS`

**提示（Prompt）**：Wi-Fi 驱动错误日志控制

**说明（Help）**

启用时，发生错误会打印错误消息，因而增加镜像大小。强烈建议开发期间保持启用，以便快速定位问题。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if (CONFIG_WIFI_LOG_LEVEL_ERR || CONFIG_WIFI_LOG_LEVEL_DBG) && !CONFIG_NXP_WIFI_SLIM_DISABLE_DEBUG
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1289`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1289)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_WIFI_LOG_LEVEL_ERR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_LOG_LEVEL_ERR)、[`CONFIG_WIFI_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_LOG_LEVEL_DBG)、[`CONFIG_NXP_WIFI_SLIM_DISABLE_DEBUG`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SLIM_DISABLE_DEBUG)。

<a id="CONFIG_NXP_WIFI_ENABLE_WARNING_LOGS"></a>

## 191.27 `CONFIG_NXP_WIFI_ENABLE_WARNING_LOGS`

**提示（Prompt）**：Wi-Fi 驱动警告日志控制

**说明（Help）**

启用时，发生错误会打印错误消息，因而增加镜像大小。强烈建议开发期间保持启用，以便快速定位问题。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if (CONFIG_WIFI_LOG_LEVEL_WRN || CONFIG_WIFI_LOG_LEVEL_DBG) && !CONFIG_NXP_WIFI_SLIM_DISABLE_DEBUG
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1298`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1298)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_WIFI_LOG_LEVEL_WRN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_LOG_LEVEL_WRN)、[`CONFIG_WIFI_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_LOG_LEVEL_DBG)、[`CONFIG_NXP_WIFI_SLIM_DISABLE_DEBUG`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SLIM_DISABLE_DEBUG)。

<a id="CONFIG_NXP_WIFI_EU_CRYPTO"></a>

## 191.28 `CONFIG_NXP_WIFI_EU_CRYPTO`

**提示（Prompt）**：Wi-Fi EU Crypto

**说明（Help）**

在 Wi-Fi 驱动中启用 EU Crypto 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NXP_88W8801 && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if !CONFIG_NXP_WIFI_SLIM
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1137)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8801`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8801)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_SLIM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SLIM)。

<a id="CONFIG_NXP_WIFI_EVENTS_DEBUG"></a>

## 191.29 `CONFIG_NXP_WIFI_EVENTS_DEBUG`

**提示（Prompt）**：转储事件信息（Event Information）

**说明（Help）**

转储从固件收到的事件码（Event Code），帮助开发者查看固件事件及其时间戳（Timestamp）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1344`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1344)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_EXTERNAL_COEX_PTA"></a>

## 191.30 `CONFIG_NXP_WIFI_EXTERNAL_COEX_PTA`

**提示（Prompt）**：外部共存分组流量仲裁（External COEX PTA）支持

**说明（Help）**

启用外部共存分组流量仲裁（External Coexistence Packet Traffic Arbitration，PTA）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:814`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L814)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_EXTRA_DEBUG"></a>

## 191.31 `CONFIG_NXP_WIFI_EXTRA_DEBUG`

**提示（Prompt）**：Wi-Fi 驱动额外调试控制

**说明（Help）**

此宏用于取得 Wi-Fi 驱动的额外调试信息，例如发生关联失败（Association Failure）时提供更详细的原因。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_LOG_LEVEL_DBG && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1325`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1325)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_LOG_LEVEL_DBG)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_EXTRA_TX_HEADROOM"></a>

## 191.32 `CONFIG_NXP_WIFI_EXTRA_TX_HEADROOM`

**提示（Prompt）**：802.3 以太网头部之前额外预留的头部空间（Headroom）

**说明（Help）**

在 802.3 以太网头部之前额外预留空间。为满足 DMA 访问要求，此值加上以太网头部预留大小后，必须按 4 字节对齐。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
26 if CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM
0
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1278`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1278)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM)。

<a id="CONFIG_NXP_WIFI_EXT_ANT_GAIN"></a>

## 191.33 `CONFIG_NXP_WIFI_EXT_ANT_GAIN`

**提示（Prompt）**：外部天线增益配置（External Antenna Gain Configuration）

**说明（Help）**

允许通过主机命令，在运行时按子频段配置净天线增益（Net Antenna Gain）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_RW610 && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1041`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1041)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_EXT_SCAN_SUPPORT"></a>

## 191.34 `CONFIG_NXP_WIFI_EXT_SCAN_SUPPORT`

**提示（Prompt）**：扩展扫描（Extended Scan）支持

**说明（Help）**

启用扩展扫描（Extended Scan）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NXP_88W8801 && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:570`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L570)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持 → Wi-Fi 扫描支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8801`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8801)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_FIPS"></a>

## 191.35 `CONFIG_NXP_WIFI_FIPS`

**提示（Prompt）**：联邦信息处理标准（FIPS）

**说明（Help）**

在 Wi-Fi 驱动中启用联邦信息处理标准（FIPS）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1164)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_FORCE_RTS"></a>

## 191.36 `CONFIG_NXP_WIFI_FORCE_RTS`

**提示（Prompt）**：强制请求发送（RTS）支持

**说明（Help）**

启用强制请求发送（RTS）设置支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if !CONFIG_NXP_WIFI_SLIM
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:802`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L802)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_SLIM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SLIM)。

<a id="CONFIG_NXP_WIFI_FRAG_THRESHOLD"></a>

## 191.37 `CONFIG_NXP_WIFI_FRAG_THRESHOLD`

**提示（Prompt）**：分片阈值（Fragment Threshold）设置支持

**说明（Help）**

启用分片阈值（Fragment Threshold）设置支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if !CONFIG_NXP_WIFI_SLIM
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:796`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L796)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_SLIM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SLIM)。

<a id="CONFIG_NXP_WIFI_FWDNLD_IO_DEBUG"></a>

## 191.38 `CONFIG_NXP_WIFI_FWDNLD_IO_DEBUG`

**提示（Prompt）**：固件下载调试（FW Download Debug）

**说明（Help）**

启用后，监测固件（FW）下载调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1443`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1443)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_FW_AUTO_RECONNECT"></a>

## 191.39 `CONFIG_NXP_WIFI_FW_AUTO_RECONNECT`

**提示（Prompt）**：固件自动重连（Firmware Auto Reconnect）

**说明（Help）**

启用固件自动重连（Firmware Auto Reconnect）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NXP_88W8987 || CONFIG_NXP_IW416 || CONFIG_NXP_IW610 || CONFIG_NXP_IW61X) && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1189)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8987`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8987)、[`CONFIG_NXP_IW416`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_FW_DEBUG"></a>

## 191.40 `CONFIG_NXP_WIFI_FW_DEBUG`

**提示（Prompt）**：固件调试（FW Debug）

**说明（Help）**

启用后，监测来自固件（FW）的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1448`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1448)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_FW_VDLLV2"></a>

## 191.41 `CONFIG_NXP_WIFI_FW_VDLLV2`

**提示（Prompt）**：固件虚拟动态链接库第 2 版（Virtual Dynamic Link Library v2）

**说明（Help）**

用于在运行时加载部分固件功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_RW610 && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:974`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L974)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_FW_VDLL_DEBUG"></a>

## 191.42 `CONFIG_NXP_WIFI_FW_VDLL_DEBUG`

**提示（Prompt）**：虚拟动态链接库（VDLL）调试

**说明（Help）**

启用后，监测虚拟动态链接库（VDLL）的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1468`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1468)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_GET_LOG"></a>

## 191.43 `CONFIG_NXP_WIFI_GET_LOG`

**提示（Prompt）**：取得 802.11 日志

**说明（Help）**

在 Wi-Fi 驱动中取得 802.11 日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:851`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L851)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_HOST_SLEEP"></a>

## 191.44 `CONFIG_NXP_WIFI_HOST_SLEEP`

**提示（Prompt）**：主机睡眠（Host Sleep）

**说明（Help）**

为微控制器（MCU）启用主机睡眠（Host Sleep）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_PM
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1144)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)。

<a id="CONFIG_NXP_WIFI_HOST_TXRX_MGMT_FRAME"></a>

## 191.45 `CONFIG_NXP_WIFI_HOST_TXRX_MGMT_FRAME`

**提示（Prompt）**：主机在监听模式（Monitor Mode）下发送管理帧和数据帧

**说明（Help）**

用于在监听模式（Monitor Mode）下发送管理帧和数据帧。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NXP_RW610 || CONFIG_NXP_IW610) && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:941`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L941)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_IMD3_CFG"></a>

## 191.46 `CONFIG_NXP_WIFI_IMD3_CFG`

**提示（Prompt）**：设置互调失真（IMD）验证参数

**说明（Help）**

用于设置 Wi-Fi、低功耗蓝牙（BLE）共存模式及天线隔离调试的三阶互调（IM3）配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NXP_RW610 || CONFIG_NXP_IW610
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1025`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1025)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)。

<a id="CONFIG_NXP_WIFI_INACTIVITY_TIMEOUT_EXT"></a>

## 191.47 `CONFIG_NXP_WIFI_INACTIVITY_TIMEOUT_EXT`

**提示（Prompt）**：不活动超时扩展（Inactivity Timeout Ext）支持

**说明（Help）**

启用不活动超时扩展（Inactivity Timeout Ext）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:677`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L677)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_IND_DNLD"></a>

## 191.48 `CONFIG_NXP_WIFI_IND_DNLD`

**提示（Prompt）**：并行固件下载（Parallel Firmware Download）

**说明（Help）**

启用并行固件下载（Parallel Firmware Download）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NXP_88W8987 || CONFIG_NXP_IW416 || CONFIG_NXP_IW610 || CONFIG_NXP_IW61X) && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**被弱选择（Implied by）**

```text
CONFIG_NXP_WIFI_RESET
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1195`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1195)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8987`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8987)、[`CONFIG_NXP_IW416`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_RESET`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_RESET)。

<a id="CONFIG_NXP_WIFI_IND_OOB_RESET"></a>

## 191.49 `CONFIG_NXP_WIFI_IND_OOB_RESET`

**提示（Prompt）**：Wi-Fi 独立带外复位（Independent Out-of-band Reset）

**说明（Help）**

增加通过外部 GPIO 执行 Wi-Fi 独立复位的选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_IND_RESET && CONFIG_NXP_WIFI_IND_DNLD && (CONFIG_NXP_88W8987 || CONFIG_NXP_IW416 || CONFIG_NXP_IW610 || CONFIG_NXP_IW61X) && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**被弱选择（Implied by）**

```text
CONFIG_NXP_WIFI_RESET
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1205`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1205)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 独立复位（Independent Reset）

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_IND_RESET`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_IND_RESET)、[`CONFIG_NXP_WIFI_IND_DNLD`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_IND_DNLD)、[`CONFIG_NXP_88W8987`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8987)、[`CONFIG_NXP_IW416`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_RESET`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_RESET)。

<a id="CONFIG_NXP_WIFI_IND_RESET"></a>

## 191.50 `CONFIG_NXP_WIFI_IND_RESET`

**提示（Prompt）**：Wi-Fi 独立复位（Independent Reset）

**说明（Help）**

启用 Wi-Fi 独立复位（Independent Reset）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NXP_88W8987 || CONFIG_NXP_IW416 || CONFIG_NXP_IW610 || CONFIG_NXP_IW61X) && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**被弱选择（Implied by）**

```text
CONFIG_NXP_WIFI_RESET
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1200`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1200)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_88W8987`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8987)、[`CONFIG_NXP_IW416`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_RESET`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_RESET)。

<a id="CONFIG_NXP_WIFI_IO_DEBUG"></a>

## 191.51 `CONFIG_NXP_WIFI_IO_DEBUG`

**提示（Prompt）**：输入／输出调试（Input-Output Debug，高级）

**说明（Help）**

启用 Wi-Fi 驱动的输入／输出（I/O）调试，以观察驱动如何与 SDIO 总线交互。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1390`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1390)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_IO_DUMP"></a>

## 191.52 `CONFIG_NXP_WIFI_IO_DUMP`

**提示（Prompt）**：数据包十六进制转储（Hex Dump Packets）

**说明（Help）**

启用 Wi-Fi 驱动的输入／输出（I/O）调试，以查看从 SDIO 总线接收和发送到总线的所有数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1398`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1398)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_IO_INFO_DUMP"></a>

## 191.53 `CONFIG_NXP_WIFI_IO_INFO_DUMP`

**提示（Prompt）**：输入／输出调试（Input-Output Debug，基础）

**说明（Help）**

转储输入／输出数据包信息，包括包大小、目标接口等。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1382`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1382)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_IPS"></a>

## 191.54 `CONFIG_NXP_WIFI_IPS`

**提示（Prompt）**：IPS

**说明（Help）**

启用／禁用 Wi-Fi 驱动中的 IPS 配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NXP_RW610 || CONFIG_NXP_IW610
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:993`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L993)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)。

<a id="CONFIG_NXP_WIFI_IPV6"></a>

## 191.55 `CONFIG_NXP_WIFI_IPV6`

**提示（Prompt）**：IPv6 支持

**说明（Help）**

启用 IPv6 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6 && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:828`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L828)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_MAX_AP_ENTRIES"></a>

## 191.56 `CONFIG_NXP_WIFI_MAX_AP_ENTRIES`

**提示（Prompt）**：最大扫描条目数量

**说明（Help）**

Wi-Fi 驱动所保存的 AP 列表中的最大条目数量。每个条目约占 400 字节 RAM。应根据最终用户环境中预期存在的 AP 数量选择此值。注意，驱动自动仅保留信号最强的 AP。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
5 if CONFIG_NXP_WIFI_SLIM
10
```

**取值范围（Ranges）**

```text
[1, 30]
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:583`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L583)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持 → Wi-Fi 扫描支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_SLIM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SLIM)。

<a id="CONFIG_NXP_WIFI_MAX_CSI_LOCAL_BUF"></a>

## 191.57 `CONFIG_NXP_WIFI_MAX_CSI_LOCAL_BUF`

**提示（Prompt）**：CSI 本地缓冲区最大条目数量

**说明（Help）**

设置信道状态信息（CSI）本地缓冲区的最大条目数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_CSI && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:897`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L897)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_CSI`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_CSI)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_MAX_PRIO"></a>

## 191.58 `CONFIG_NXP_WIFI_MAX_PRIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设置 Wi-Fi 驱动中的 Wi-Fi 最大优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:685`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L685)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_MAX_RECONNECT_LIMIT"></a>

## 191.59 `CONFIG_NXP_WIFI_MAX_RECONNECT_LIMIT`

**提示（Prompt）**：最大重连次数限制

**说明（Help）**

设置最大重连次数限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:556`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L556)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_MAX_RESCAN_LIMIT"></a>

## 191.60 `CONFIG_NXP_WIFI_MAX_RESCAN_LIMIT`

**提示（Prompt）**：最大扫描次数限制

**说明（Help）**

设置最大扫描次数限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:603`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L603)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持 → Wi-Fi 扫描支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_MEF_CFG"></a>

## 191.61 `CONFIG_NXP_WIFI_MEF_CFG`

**提示（Prompt）**：内存高效过滤（Memory Efficient Filtering）

**说明（Help）**

在 Wi-Fi 驱动中启用内存高效过滤（Memory Efficient Filtering）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_PM
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1158)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)。

<a id="CONFIG_NXP_WIFI_MEM_ACCESS"></a>

## 191.62 `CONFIG_NXP_WIFI_MEM_ACCESS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在 Wi-Fi 驱动中启用内存访问命令（Memory Access Command）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1085`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1085)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_MEM_DEBUG"></a>

## 191.63 `CONFIG_NXP_WIFI_MEM_DEBUG`

**提示（Prompt）**：内存分配调试（Allocations Debug）

**说明（Help）**

监测 Wi-Fi 驱动执行的内存分配与释放，以评估和／或调试驱动使用的堆内存（Heap Memory）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1406`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1406)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_MMSF"></a>

## 191.64 `CONFIG_NXP_WIFI_MMSF`

**提示（Prompt）**：802.11ax 密度配置（Density Config）

**说明（Help）**

指定／获取 Wi-Fi 驱动中的 802.11ax 密度配置（Density Config）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NXP_RW610 || CONFIG_NXP_IW610) && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:947`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L947)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_MON_TASK_PRIO"></a>

## 191.65 `CONFIG_NXP_WIFI_MON_TASK_PRIO`

**提示（Prompt）**：Mon 任务优先级

**说明（Help）**

指定 Mon 任务的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_NXP_RW610 || CONFIG_NXP_IW610 || CONFIG_NXP_IW61X || CONFIG_NXP_IW416) && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:475`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L475)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 线程优先级配置

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_NXP_IW416`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_MON_TASK_STACK_SIZE"></a>

## 191.66 `CONFIG_NXP_WIFI_MON_TASK_STACK_SIZE`

**提示（Prompt）**：Mon 线程栈大小

**说明（Help）**

指定 Mon 任务使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_NXP_RW610 || CONFIG_NXP_IW610 || CONFIG_NXP_IW61X || CONFIG_NXP_IW416) && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
5120 if CONFIG_NXP_WIFI_RECOVERY
3072
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:426`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L426)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 驱动栈配置（Stack Configurations）

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_NXP_IW416`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_RECOVERY`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_RECOVERY)。

<a id="CONFIG_NXP_WIFI_MULTI_BSSID_SUPPORT"></a>

## 191.67 `CONFIG_NXP_WIFI_MULTI_BSSID_SUPPORT`

**提示（Prompt）**：多基本服务集标识符（Multiple BSSID）支持

**说明（Help）**

启用多基本服务集标识符（Multiple BSSID）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_11AX && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:789`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L789)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_11AX`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_WIFI_11AX)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_NET_DEBUG"></a>

## 191.68 `CONFIG_NXP_WIFI_NET_DEBUG`

**提示（Prompt）**：网络（NET）调试

**说明（Help）**

启用网络驱动抽象 API（Network Driver Abstraction API）的调试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1307)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_NET_MONITOR"></a>

## 191.69 `CONFIG_NXP_WIFI_NET_MONITOR`

**提示（Prompt）**：网络监测（Networking Monitor）

**说明（Help）**

设置／获取网络监测（Network Monitor）配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NXP_RW610 || CONFIG_NXP_IW610) && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if !CONFIG_NXP_WIFI_SLIM
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:935`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L935)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_SLIM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SLIM)。

<a id="CONFIG_NXP_WIFI_OWE"></a>

## 191.70 `CONFIG_NXP_WIFI_OWE`

**提示（Prompt）**：机会式无线加密（Opportunistic Wireless Encryption）

**说明（Help）**

在 Wi-Fi 驱动中启用机会式无线加密（Opportunistic Wireless Encryption，OWE）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1169)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_PART"></a>

## 191.71 `CONFIG_NXP_WIFI_PART`

**提示（Prompt）**：选择 NXP Wi-Fi 器件

**说明（Help）**

选择 NXP Wi-Fi 芯片支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NXP_WIFI_CUSTOM && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**可选项（Choices）**

```text
CONFIG_NXP_RW610
CONFIG_NXP_88W8987
CONFIG_NXP_IW416
CONFIG_NXP_IW61X
CONFIG_NXP_88W8801
CONFIG_NXP_IW610
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
CONFIG_NXP_IW416
```

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
CONFIG_NXP_IW61X
```

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
CONFIG_NXP_IW610
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_CUSTOM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_CUSTOM)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_88W8987`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8987)、[`CONFIG_NXP_IW416`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_NXP_88W8801`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8801)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)。

<a id="CONFIG_NXP_WIFI_PKT_DEBUG"></a>

## 191.72 `CONFIG_NXP_WIFI_PKT_DEBUG`

**提示（Prompt）**：数据包调试（Packet Debug）

**说明（Help）**

启用数据包发送／接收（TX/RX）代码日志，帮助开发者定位 WLAN 数据通路问题，例如发送或接收失败。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1375`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1375)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_PKT_FWD"></a>

## 191.73 `CONFIG_NXP_WIFI_PKT_FWD`

**提示（Prompt）**：Wi-Fi 数据包转发（Packet Forward）

**说明（Help）**

在软件接入点（SoftAP）上启用 Wi-Fi 数据包转发。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_SOFTAP_SUPPORT && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NXP_RW610 || CONFIG_NXP_IW610
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1072`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1072)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_SOFTAP_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_WIFI_SOFTAP_SUPPORT)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)。

<a id="CONFIG_NXP_WIFI_POWERSAVE_TASK_PRIO"></a>

## 191.74 `CONFIG_NXP_WIFI_POWERSAVE_TASK_PRIO`

**提示（Prompt）**：Wi-Fi 节能任务优先级

**说明（Help）**

指定 Wi-Fi 节能（Power Save）任务的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:488`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L488)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 线程优先级配置

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_POWERSAVE_TASK_STACK_SIZE"></a>

## 191.75 `CONFIG_NXP_WIFI_POWERSAVE_TASK_STACK_SIZE`

**提示（Prompt）**：Wi-Fi 节能任务栈大小

**说明（Help）**

指定 Wi-Fi 节能（Power Save）任务使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:440`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L440)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 驱动栈配置（Stack Configurations）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_PS_DEBUG"></a>

## 191.76 `CONFIG_NXP_WIFI_PS_DEBUG`

**提示（Prompt）**：节能调试（Power Save Debug）

**说明（Help）**

对节能命令，分别转储发送给固件的命令码及从固件收到的响应码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1360`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1360)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_RECOVERY"></a>

## 191.77 `CONFIG_NXP_WIFI_RECOVERY`

**提示（Prompt）**：恢复（Recovery）

**说明（Help）**

启用 Wi-Fi 恢复（Recovery）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NXP_RW610 || CONFIG_NXP_IW610 || CONFIG_NXP_IW61X || CONFIG_NXP_IW416) && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:927`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L927)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_NXP_IW416`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_REG_ACCESS"></a>

## 191.78 `CONFIG_NXP_WIFI_REG_ACCESS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在 Wi-Fi 驱动中启用寄存器访问命令（Register Access Command）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1090`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1090)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_RESET"></a>

## 191.79 `CONFIG_NXP_WIFI_RESET`

**提示（Prompt）**：Wi-Fi 复位（Reset）

**说明（Help）**

用于启用、禁用或复位 Wi-Fi。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_NXP_WIFI_IND_DNLD if CONFIG_NXP_IW610 || CONFIG_NXP_IW61X || CONFIG_NXP_IW416
CONFIG_NXP_WIFI_IND_RESET if CONFIG_NXP_IW610 || CONFIG_NXP_IW61X || CONFIG_NXP_IW416
CONFIG_NXP_WIFI_IND_OOB_RESET if (CONFIG_NXP_IW610 || CONFIG_NXP_IW61X || CONFIG_NXP_IW416) && !CONFIG_NXP_WIFI_CUSTOM_HOST
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:904`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L904)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_IND_DNLD`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_IND_DNLD)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_NXP_IW416`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416)、[`CONFIG_NXP_WIFI_IND_RESET`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_IND_RESET)、[`CONFIG_NXP_WIFI_IND_OOB_RESET`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_IND_OOB_RESET)、[`CONFIG_NXP_WIFI_CUSTOM_HOST`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_CUSTOM_HOST)。

<a id="CONFIG_NXP_WIFI_RF_TEST_MODE"></a>

## 191.80 `CONFIG_NXP_WIFI_RF_TEST_MODE`

**提示（Prompt）**：无线局域网射频测试模式（WLAN RF Test Mode）

**说明（Help）**

启用无线局域网（WLAN）测试模式命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NXP_RW610 || CONFIG_NXP_IW610 || CONFIG_NXP_IW61X || CONFIG_NXP_IW416
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1108)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_NXP_IW416`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW416)。

<a id="CONFIG_NXP_WIFI_ROAMING"></a>

## 191.81 `CONFIG_NXP_WIFI_ROAMING`

**提示（Prompt）**：Wi-Fi 软件漫游（Soft Roaming）

**说明（Help）**

在 Wi-Fi 驱动中启用软件漫游（Soft Roaming）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if !CONFIG_NXP_WIFI_SLIM
```

**主动选择（Selects）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_ROAMING if CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT_SKIP_DHCP_ON_ROAMING if CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:633`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L633)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_SLIM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SLIM)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_ROAMING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_ROAMING)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_SKIP_DHCP_ON_ROAMING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_SKIP_DHCP_ON_ROAMING)。

<a id="CONFIG_NXP_WIFI_RTS_THRESHOLD"></a>

## 191.82 `CONFIG_NXP_WIFI_RTS_THRESHOLD`

**提示（Prompt）**：请求发送（RTS）阈值设置支持

**说明（Help）**

启用请求发送（RTS）阈值设置支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:665`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L665)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_RX_ABORT_CFG"></a>

## 191.83 `CONFIG_NXP_WIFI_RX_ABORT_CFG`

**提示（Prompt）**：接收中止（RX Abort）支持

**说明（Help）**

在 Wi-Fi 驱动中启用使用静态接收信号强度指示（RSSI）阈值的接收中止（RX Abort）配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NXP_RW610 || CONFIG_NXP_IW610
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:999`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L999)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)。

<a id="CONFIG_NXP_WIFI_RX_ABORT_CFG_EXT"></a>

## 191.84 `CONFIG_NXP_WIFI_RX_ABORT_CFG_EXT`

**提示（Prompt）**：接收中止扩展（RX Abort Extension）支持

**说明（Help）**

在 Wi-Fi 驱动中启用使用动态接收信号强度指示（RSSI）阈值的接收中止扩展（RX Abort Extension）配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NXP_RW610 || CONFIG_NXP_IW610
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1006`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1006)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)。

<a id="CONFIG_NXP_WIFI_SCAN_CHANNEL_GAP"></a>

## 191.85 `CONFIG_NXP_WIFI_SCAN_CHANNEL_GAP`

**提示（Prompt）**：启用扫描信道间隔（Scan Channel Gap）

**说明（Help）**

启用扫描信道间隔（Scan Channel Gap）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if !CONFIG_NXP_WIFI_SLIM
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:597`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L597)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持 → Wi-Fi 扫描支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_SLIM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SLIM)。

<a id="CONFIG_NXP_WIFI_SCAN_DEBUG"></a>

## 191.86 `CONFIG_NXP_WIFI_SCAN_DEBUG`

**提示（Prompt）**：扫描调试（Scan Debug）

**说明（Help）**

启用扫描代码日志，帮助开发者定位 WLAN 扫描相关问题，例如分段扫描（Split Scan）、信道选择等。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1367`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1367)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SCAN_TASK_PRIO"></a>

## 191.87 `CONFIG_NXP_WIFI_SCAN_TASK_PRIO`

**提示（Prompt）**：Wi-Fi 扫描任务优先级

**说明（Help）**

指定 Wi-Fi 扫描任务的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:510`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L510)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 线程优先级配置

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SCAN_TASK_STACK_SIZE"></a>

## 191.88 `CONFIG_NXP_WIFI_SCAN_TASK_STACK_SIZE`

**提示（Prompt）**：Wi-Fi 扫描任务栈大小

**说明（Help）**

指定 Wi-Fi 扫描任务使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:465`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L465)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 驱动栈配置（Stack Configurations）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SCAN_WITH_RSSIFILTER"></a>

## 191.89 `CONFIG_NXP_WIFI_SCAN_WITH_RSSIFILTER`

**提示（Prompt）**：使用 RSSI 过滤进行扫描

**说明（Help）**

在 Wi-Fi 驱动中启用接收信号强度指示（RSSI）阈值支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:577`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L577)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持 → Wi-Fi 扫描支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SCHED_SCAN_DEFAULT_ITERATION"></a>

## 191.90 `CONFIG_NXP_WIFI_SCHED_SCAN_DEFAULT_ITERATION`

**提示（Prompt）**：计划迭代次数为 0 时的调度扫描默认迭代次数

**说明（Help）**

当 `sched_scan` 计划的迭代次数为 0 时，改用有限迭代次数。`sched_scan` 停止后，`hostap` 会重新触发一次 `sched_scan`，以避免某些边界情况下意外无限扫描。此选项设为 0 时，使用无限扫描。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
6
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:609`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L609)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持 → Wi-Fi 扫描支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SCHED_SCAN_MIN_INTERVAL"></a>

## 191.91 `CONFIG_NXP_WIFI_SCHED_SCAN_MIN_INTERVAL`

**提示（Prompt）**：调度扫描（Scheduled Scan）每次扫描的最小间隔

**说明（Help）**

`sched_scan` 计划的最小间隔，单位为秒，用于在部分场景下节省功耗。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:618`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L618)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持 → Wi-Fi 扫描支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SDIO_DEBUG"></a>

## 191.92 `CONFIG_NXP_WIFI_SDIO_DEBUG`

**提示（Prompt）**：SDIO 调试

**说明（Help）**

启用后，监测 SDIO 初始化和反初始化错误。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1432`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1432)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SDIO_IO_DEBUG"></a>

## 191.93 `CONFIG_NXP_WIFI_SDIO_IO_DEBUG`

**提示（Prompt）**：SDIO 输入／输出（I/O）调试

**说明（Help）**

启用后，监测 SDIO 驱动在数据与命令操作中的读写错误。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1437`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1437)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SDIO_MULTI_PORT_RX_AGGR"></a>

## 191.94 `CONFIG_NXP_WIFI_SDIO_MULTI_PORT_RX_AGGR`

**提示（Prompt）**：SDIO 多端口接收聚合（Multiport RX Aggregation）

**说明（Help）**

在 Wi-Fi 驱动中启用 SDIO 多端口接收聚合（Multiport RX Aggregation）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if !CONFIG_SOC_SERIES_RW6XX
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:744`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L744)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi SDIO 多端口聚合（Multi Port Aggregation）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_NXP_WIFI_SDIO_MULTI_PORT_TX_AGGR"></a>

## 191.95 `CONFIG_NXP_WIFI_SDIO_MULTI_PORT_TX_AGGR`

**提示（Prompt）**：SDIO 多端口发送聚合（Multiport TX Aggregation）

**说明（Help）**

在 Wi-Fi 驱动中启用 SDIO 多端口接收聚合（Multiport RX Aggregation）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_WMM && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if !CONFIG_SOC_SERIES_RW6XX
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:750`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L750)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi SDIO 多端口聚合（Multi Port Aggregation）

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_WMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_WIFI_WMM)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_NXP_WIFI_SET_SU"></a>

## 191.96 `CONFIG_NXP_WIFI_SET_SU`

**提示（Prompt）**：单用户（Single User）支持

**说明（Help）**

启用单用户（Single User）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_11AX && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:782`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L782)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_11AX`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_WIFI_11AX)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SHELL"></a>

## 191.97 `CONFIG_NXP_WIFI_SHELL`

**提示（Prompt）**：NXP Wi-Fi 命令行（Shell）

**说明（Help）**

NXP Wi-Fi 命令行命令（Shell Commands）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_SHELL
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:418`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L418)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)。

<a id="CONFIG_NXP_WIFI_SIGMA_AGENT"></a>

## 191.98 `CONFIG_NXP_WIFI_SIGMA_AGENT`

**提示（Prompt）**：Wi-Fi Alliance Sigma Agent 支持

**说明（Help）**

在 Wi-Fi 驱动中启用 Wi-Fi Alliance Sigma Agent 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_SMOKE_TESTS && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_POSIX_API
CONFIG_POSIX_THREADS
CONFIG_PTHREAD_CREATE_BARRIER
CONFIG_POSIX_TIMERS
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1235`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1235)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 冒烟测试（Smoke Tests）

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_SMOKE_TESTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_WIFI_SMOKE_TESTS)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_POSIX_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_API)、[`CONFIG_POSIX_THREADS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREADS)、[`CONFIG_PTHREAD_CREATE_BARRIER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTHREAD_CREATE_BARRIER)、[`CONFIG_POSIX_TIMERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_TIMERS)。

<a id="CONFIG_NXP_WIFI_SLIM"></a>

## 191.99 `CONFIG_NXP_WIFI_SLIM`

**提示（Prompt）**：Wi-Fi 精简（SLIM）功能

**说明（Help）**

为资源受限平台启用精简（SLIM）功能，禁用部分高级 Wi-Fi 功能以减小内存和代码大小。启用后，原本采用 `default y` 的功能会改为默认禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1212`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1212)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SLIM_DISABLE_DEBUG"></a>

## 191.100 `CONFIG_NXP_WIFI_SLIM_DISABLE_DEBUG`

**提示（Prompt）**：Wi-Fi SLIM 禁用调试日志

**说明（Help）**

禁用 Wi-Fi 调试日志，包括错误和警告日志，以减小内存和代码大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1219`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1219)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<!-- kconfig-navigation -->

[上一章](P190_drivers_wifi_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P192_drivers_wifi_配置项参考_5.md)
