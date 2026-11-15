---
id: learning.zephyr-docs.kconfig-reference.page-409
title: "`subsys/net`配置项参考（19/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第409章\_`subsys/net`配置项参考（19/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 61 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_WIFI_LOG_LEVEL_DBG"></a>

## 409.1 `CONFIG_WIFI_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Wi-Fi 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_LOG_LEVEL_DEFAULT"></a>

## 409.2 `CONFIG_WIFI_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Wi-Fi 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_LOG_LEVEL_ERR"></a>

## 409.3 `CONFIG_WIFI_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Wi-Fi 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_LOG_LEVEL_INF"></a>

## 409.4 `CONFIG_WIFI_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Wi-Fi 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_LOG_LEVEL_OFF"></a>

## 409.5 `CONFIG_WIFI_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Wi-Fi 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_LOG_LEVEL_WRN"></a>

## 409.6 `CONFIG_WIFI_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Wi-Fi 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_MGMT_AP_MAX_NUM_STA"></a>

## 409.7 `CONFIG_WIFI_MGMT_AP_MAX_NUM_STA`

**提示（Prompt）**：站点表（Station table）允许的最大站点数

**说明（Help）**

站点表（Station table）允许的最大站点数。表满后拒绝新站点（Station）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 2007]
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
8 if CONFIG_NXP_WIFI_SOFTAP_SUPPORT
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NXP_WIFI_SOFTAP_SUPPORT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SOFTAP_SUPPORT)。

<a id="CONFIG_WIFI_MGMT_AP_STA_INACTIVITY_TIMEOUT"></a>

## 409.8 `CONFIG_WIFI_MGMT_AP_STA_INACTIVITY_TIMEOUT`

**提示（Prompt）**：站点不活动超时（Station inactivity timeout，秒）

**说明（Help）**

站点不活动超时（Station inactivity timeout）指某个客户端没有流量时，接入点（AP）仍可保持其关联状态（Associated state）的时间。设置非零值后，AP 可以在超时后解除该客户端的关联。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
300
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_MGMT_AP_STA_SKIP_INACTIVITY_POLL"></a>

## 409.9 `CONFIG_WIFI_MGMT_AP_STA_SKIP_INACTIVITY_POLL`

**提示（Prompt）**：站点不活动超时后跳过不活动轮询（Inactivity poll）

**说明（Help）**

站点不活动超时后跳过不活动轮询（Inactivity poll），阻止接入点（AP）在超时后向站点发送空数据帧（Null data frame）。这样即使空闲站点仍在 AP 覆盖范围内，也可将其断开。注意，此参数只能在构建时配置，不支持运行时配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_MGMT_BSS_MAX_IDLE_TIME"></a>

## 409.10 `CONFIG_WIFI_MGMT_BSS_MAX_IDLE_TIME`

**提示（Prompt）**：基本服务集（BSS）最大空闲超时，单位为秒

**说明（Help）**

依据 IEEE 802.11-2020 第 11.21.13 节的基本服务集（BSS）最大空闲期管理：如果 `dot11WirelessManagementImplemented` 为 true、`dot11BSSMaxIdlePeriod` 非零，且 `dot11BSSMaxIdlePeriodIndicationByNonAPSTA` 为 true，则非 S1G、非接入点的站点（non-AP STA）必须在关联或重新关联请求帧（(Re)Association Request）中包含 BSS 最大空闲期元素（BSS Max Idle Period element）。如果 `dot11BSSMaxIdlePeriodIndicationByNonAPSTA` 为 true 的非 S1G 接入点（AP）收到的该请求帧包含此元素，则 AP 可以采用该非 AP 站点首选的最大空闲期。非 S1G AP 在关联或重新关联响应帧（(Re)Association Response）中，将选定值告知非 S1G 站点。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
300
```

**取值范围（Ranges）**

```text
[0, 64000]
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_MGMT_FORCED_PASSIVE_SCAN"></a>

## 409.11 `CONFIG_WIFI_MGMT_FORCED_PASSIVE_SCAN`

**提示（Prompt）**：强制被动 Wi-Fi 扫描（Passive scanning）

**说明（Help）**

无论用户提供何种参数，始终请求被动扫描（Passive scan）。通常用于底层硬件尚未通过射频（RF）发射认证的情况。但这不保证实际采用被动扫描，仍取决于底层芯片实现是否支持并遵从所请求的扫描类型。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS"></a>

## 409.12 `CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS`

**提示（Prompt）**：原始扫描结果（Raw scan results）

**说明（Help）**

启用原始扫描结果（Raw scan results），向应用提供原始信标（Beacon）或探测响应（Probe response）。此配置会显著增大 `net_mgmt` 事件的大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS_ONLY"></a>

## 409.13 `CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS_ONLY`

**提示（Prompt）**：仅提供原始扫描结果（Raw scan results only）

**说明（Help）**

仅启用原始扫描结果（Raw scan results）。向应用提供原始信标（Beacon）或探测响应（Probe response），不进行解析，由应用负责解析；不会另外向应用提供普通扫描结果。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS && CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → 原始扫描结果（Raw scan results）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS)、[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_MGMT_RAW_SCAN_RESULT_LENGTH"></a>

## 409.14 `CONFIG_WIFI_MGMT_RAW_SCAN_RESULT_LENGTH`

**提示（Prompt）**：原始扫描结果（Raw scan result）的最大长度

**说明（Help）**

定义原始扫描结果（Raw scan result）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS && CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → 原始扫描结果（Raw scan results）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS)、[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_MGMT_SCAN_CHAN_MAX_MANUAL"></a>

## 409.15 `CONFIG_WIFI_MGMT_SCAN_CHAN_MAX_MANUAL`

**提示（Prompt）**：可手动指定的信道（Channel）最大数量

**说明（Help）**

三个受支持频段（Band）合计约分配了 100 个信道。默认值 3 允许指定最常用的三个信道，即 2.4 GHz 频段的 1、6、11。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 110]
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_MGMT_SCAN_SSID_FILT_MAX"></a>

## 409.16 `CONFIG_WIFI_MGMT_SCAN_SSID_FILT_MAX`

**提示（Prompt）**：用于 SSID 过滤的服务集标识符（SSID）最大数量

**说明（Help）**

指定 SSID 过滤（SSID filtering）中最多可提供多少个 SSID，可根据底层芯片组的限制设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 4]
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_MGMT_TWT_CHECK_IP"></a>

## 409.17 `CONFIG_WIFI_MGMT_TWT_CHECK_IP`

**提示（Prompt）**：建立目标唤醒时间（TWT）前检查 IP 地址分配

**说明（Help）**

在建立目标唤醒时间（Target Wake Time，TWT）安排前，检查是否已获得有效 IP 地址。如果在连接初期触发 TWT，设备可能尚未获得有效 IP 地址就进入深度睡眠（Deep sleep），导致设备在 IP 层不可达，或即使处于唤醒时段也无法接收下行流量。在大多数场景中，可能需要在 Wi-Fi 接口获得有效 IP 地址前拒绝建立 TWT 安排。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_NM"></a>

## 409.18 `CONFIG_WIFI_NM`

**提示（Prompt）**：Wi-Fi 网络管理器（Network manager）支持

**说明（Help）**

允许使用 Wi-Fi 网络管理器（Network manager），例如 `wpa_supplicant`，管理 Wi-Fi 网络接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_AMEBA
CONFIG_WIFI_ESP_HOSTED
CONFIG_WIFI_ESP_HOSTED_MCU
CONFIG_WIFI_NXP
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_AMEBA`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_AMEBA)、[`CONFIG_WIFI_ESP_HOSTED`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED)、[`CONFIG_WIFI_ESP_HOSTED_MCU`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED_MCU)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)。

<a id="CONFIG_WIFI_NM_LOG_LEVEL_CHOICE"></a>

## 409.19 `CONFIG_WIFI_NM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Wi-Fi 网络管理器模块（Network manager module）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_WIFI_NM && CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_WIFI_NM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_WIFI_NM_LOG_LEVEL_OFF
CONFIG_WIFI_NM_LOG_LEVEL_ERR
CONFIG_WIFI_NM_LOG_LEVEL_WRN
CONFIG_WIFI_NM_LOG_LEVEL_INF
CONFIG_WIFI_NM_LOG_LEVEL_DBG
CONFIG_WIFI_NM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → Wi-Fi 网络管理器（Network manager）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_WIFI_NM`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_NM)、[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WIFI_NM_LOG_LEVEL_DEFAULT`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_NM_LOG_LEVEL_DEFAULT)、[`CONFIG_WIFI_NM_LOG_LEVEL_OFF`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_NM_LOG_LEVEL_OFF)、[`CONFIG_WIFI_NM_LOG_LEVEL_ERR`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_NM_LOG_LEVEL_ERR)、[`CONFIG_WIFI_NM_LOG_LEVEL_WRN`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_NM_LOG_LEVEL_WRN)、[`CONFIG_WIFI_NM_LOG_LEVEL_INF`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_NM_LOG_LEVEL_INF)、[`CONFIG_WIFI_NM_LOG_LEVEL_DBG`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_NM_LOG_LEVEL_DBG)。

<a id="CONFIG_WIFI_NM_LOG_LEVEL_DBG"></a>

## 409.20 `CONFIG_WIFI_NM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → Wi-Fi 网络管理器（Network manager）支持 → Wi-Fi 网络管理器模块（Network manager module）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_LOG_LEVEL_CHOICE`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_NM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NM_LOG_LEVEL_DEFAULT"></a>

## 409.21 `CONFIG_WIFI_NM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → Wi-Fi 网络管理器（Network manager）支持 → Wi-Fi 网络管理器模块（Network manager module）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_LOG_LEVEL_CHOICE`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_NM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NM_LOG_LEVEL_ERR"></a>

## 409.22 `CONFIG_WIFI_NM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → Wi-Fi 网络管理器（Network manager）支持 → Wi-Fi 网络管理器模块（Network manager module）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_LOG_LEVEL_CHOICE`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_NM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NM_LOG_LEVEL_INF"></a>

## 409.23 `CONFIG_WIFI_NM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → Wi-Fi 网络管理器（Network manager）支持 → Wi-Fi 网络管理器模块（Network manager module）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_LOG_LEVEL_CHOICE`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_NM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NM_LOG_LEVEL_OFF"></a>

## 409.24 `CONFIG_WIFI_NM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → Wi-Fi 网络管理器（Network manager）支持 → Wi-Fi 网络管理器模块（Network manager module）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_LOG_LEVEL_CHOICE`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_NM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NM_LOG_LEVEL_WRN"></a>

## 409.25 `CONFIG_WIFI_NM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → Wi-Fi 网络管理器（Network manager）支持 → Wi-Fi 网络管理器模块（Network manager module）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_LOG_LEVEL_CHOICE`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_NM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NM_MAX_MANAGED_INTERFACES"></a>

## 409.26 `CONFIG_WIFI_NM_MAX_MANAGED_INTERFACES`

**提示（Prompt）**：每个 Wi-Fi 网络管理器可管理的接口最大数量

**说明（Help）**

定义每个 Wi-Fi 网络管理器实例（Network manager instance）可同时管理的接口最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM && CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2 if CONFIG_WIFI_USAGE_MODE_STA_AP
1
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → Wi-Fi 网络管理器（Network manager）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_NM)、[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WIFI_USAGE_MODE_STA_AP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE_STA_AP)。

<a id="CONFIG_WIFI_P2P_MAX_PEERS"></a>

## 409.27 `CONFIG_WIFI_P2P_MAX_PEERS`

**提示（Prompt）**：单次查询可返回的点对点对端（P2P peer）最大数量

**说明（Help）**

定义单次查询操作可返回的点对点对端（P2P peer）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P && CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P)、[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_SHELL_MAX_AP_STA"></a>

## 409.28 `CONFIG_WIFI_SHELL_MAX_AP_STA`

**提示（Prompt）**：Wi-Fi 命令行（Shell）可管理的接入点（AP）与站点（STA）最大数量

**说明（Help）**

定义 Wi-Fi 命令行（Shell）可管理的接入点（AP）与站点（STA）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES"></a>

## 409.29 `CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES`

**提示（Prompt）**：在运行时提供 Wi-Fi 企业级安全证书

**说明（Help）**

允许在运行时提供 Wi-Fi 企业安全证书（Enterprise security certificate），使用 TLS 凭据子系统（TLS credentials subsystem）存储和管理证书。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_SHELL && CONFIG_WIFI_CERTIFICATE_LIB && CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_TLS_CREDENTIALS
CONFIG_TLS_CREDENTIALS_SHELL
CONFIG_BASE64
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_SHELL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_SHELL)、[`CONFIG_WIFI_CERTIFICATE_LIB`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CERTIFICATE_LIB)、[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_TLS_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS)、[`CONFIG_TLS_CREDENTIALS_SHELL`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS_SHELL)、[`CONFIG_BASE64`](P197_lib_配置项参考_1.md#CONFIG_BASE64)。

<a id="CONFIG_WIFI_STA_AUTO_DHCPV4"></a>

## 409.30 `CONFIG_WIFI_STA_AUTO_DHCPV4`

**提示（Prompt）**：站点（STA）连接后自动启动 DHCPv4

**说明（Help）**

启用后，站点（STA）连接建立时，Wi-Fi 驱动或认证客户端（Supplicant）自动启动 DHCPv4 客户端。禁用后，应用层负责手动启动 DHCPv4 客户端，或配置静态 IPv4 地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4 && CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIREGUARD"></a>

## 409.31 `CONFIG_WIREGUARD`

**提示（Prompt）**：WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］

**说明（Help）**

如需启用 WireGuard 虚拟专用网络（VPN）服务，请选择 `y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_VPN
CONFIG_NET_IPV4_MAPPING_TO_IPV6 if CONFIG_NET_IPV4 && CONFIG_NET_IPV6
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
CONFIG_NET_MGMT_EVENT_INFO
CONFIG_NET_L2_DUMMY
CONFIG_NET_L2_VIRTUAL
CONFIG_NET_L2_VIRTUAL_MGMT
CONFIG_NET_IP_DSCP_ECN
CONFIG_BASE64
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/lib/wireguard/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_VPN`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_VPN)、[`CONFIG_NET_IPV4_MAPPING_TO_IPV6`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_MAPPING_TO_IPV6)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_MGMT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NET_MGMT_EVENT_INFO`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_INFO)、[`CONFIG_NET_L2_DUMMY`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_DUMMY)、[`CONFIG_NET_L2_VIRTUAL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL)、[`CONFIG_NET_L2_VIRTUAL_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL_MGMT)、[`CONFIG_NET_IP_DSCP_ECN`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IP_DSCP_ECN)、[`CONFIG_BASE64`](P197_lib_配置项参考_1.md#CONFIG_BASE64)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_WIREGUARD_BUF_COUNT"></a>

## 409.32 `CONFIG_WIREGUARD_BUF_COUNT`

**提示（Prompt）**：内部临时网络缓冲区（Temporary network buffer）数量

**说明（Help）**

为临时使用分配的网络缓冲区数量。每个缓冲区占用 `WIREGUARD_BUF_LEN` 字节，总字节数为 `WIREGUARD_BUF_COUNT * WIREGUARD_BUF_LEN`。这些临时缓冲区用于接收（RX）时解密数据，以及发送（TX）时加密数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIREGUARD && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`subsys/net/lib/wireguard/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_WIREGUARD`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIREGUARD_BUF_LEN"></a>

## 409.33 `CONFIG_WIREGUARD_BUF_LEN`

**提示（Prompt）**：内部临时网络缓冲区长度（Temporary network buffer length）

**说明（Help）**

单个网络缓冲区的长度，范围从 IPv6 最小最大传输单元（MTU）长度，到以太网 MTU 减去 WireGuard 报头长度 16 字节、认证标签（Authentication tag）长度 16 字节，以及额外填充（Padding）16 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIREGUARD && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1500
```

**取值范围（Ranges）**

```text
[1328, 1500]
```

**定义位置（Location）**：[`subsys/net/lib/wireguard/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_WIREGUARD`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIREGUARD_CRYPTO"></a>

## 409.34 `CONFIG_WIREGUARD_CRYPTO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在可用的情况下，使用 PSA Crypto API 执行密码运算（Cryptographic operation），使支持的平台可利用硬件加速（Hardware acceleration）。注意，PSA 尚未提供 BLAKE2s 和 XChaCha20-Poly1305，因此仍使用参考实现。PSA 1.2 已有 XChaCha20，但原文所述 Zephyr 实现尚未具备。启用后，下列操作使用 PSA：

- X25519 密钥交换（Key exchange）。
- ChaCha20-Poly1305 带关联数据的认证加密（AEAD）与解密。
- 随机数生成（Random number generation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIREGUARD && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ECC_MONTGOMERY_255
CONFIG_PSA_WANT_ALG_HMAC
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_KEY_TYPE_CHACHA20
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_DERIVE
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
```

**定义位置（Location）**：[`subsys/net/lib/wireguard/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_WIREGUARD`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305)、[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ECC_MONTGOMERY_255`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_MONTGOMERY_255)、[`CONFIG_PSA_WANT_ALG_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HMAC)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_KEY_TYPE_CHACHA20`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_CHACHA20)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_DERIVE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_DERIVE)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)。

<a id="CONFIG_WIREGUARD_INTERFACE"></a>

## 409.35 `CONFIG_WIREGUARD_INTERFACE`

**提示（Prompt）**：使用的网络接口（Network interface）

**说明（Help）**

若希望 VPN 连接可使用全部网络接口，请留空。若指定接口，则全部 VPN 流量都经此接口路由。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIREGUARD && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/wireguard/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_WIREGUARD`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIREGUARD_LOG_LEVEL_CHOICE"></a>

## 409.36 `CONFIG_WIREGUARD_LOG_LEVEL_CHOICE`

**提示（Prompt）**：WireGuard VPN 服务日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_WIREGUARD && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_WIREGUARD_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_WIREGUARD_LOG_LEVEL_OFF
CONFIG_WIREGUARD_LOG_LEVEL_ERR
CONFIG_WIREGUARD_LOG_LEVEL_WRN
CONFIG_WIREGUARD_LOG_LEVEL_INF
CONFIG_WIREGUARD_LOG_LEVEL_DBG
CONFIG_WIREGUARD_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_WIREGUARD`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WIREGUARD_LOG_LEVEL_DEFAULT`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD_LOG_LEVEL_DEFAULT)、[`CONFIG_WIREGUARD_LOG_LEVEL_OFF`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD_LOG_LEVEL_OFF)、[`CONFIG_WIREGUARD_LOG_LEVEL_ERR`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD_LOG_LEVEL_ERR)、[`CONFIG_WIREGUARD_LOG_LEVEL_WRN`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD_LOG_LEVEL_WRN)、[`CONFIG_WIREGUARD_LOG_LEVEL_INF`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD_LOG_LEVEL_INF)、[`CONFIG_WIREGUARD_LOG_LEVEL_DBG`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD_LOG_LEVEL_DBG)。

<a id="CONFIG_WIREGUARD_LOG_LEVEL_DBG"></a>

## 409.37 `CONFIG_WIREGUARD_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIREGUARD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］ → WireGuard VPN 服务日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIREGUARD_LOG_LEVEL_CHOICE`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIREGUARD_LOG_LEVEL_DEFAULT"></a>

## 409.38 `CONFIG_WIREGUARD_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIREGUARD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］ → WireGuard VPN 服务日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIREGUARD_LOG_LEVEL_CHOICE`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIREGUARD_LOG_LEVEL_ERR"></a>

## 409.39 `CONFIG_WIREGUARD_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIREGUARD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］ → WireGuard VPN 服务日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIREGUARD_LOG_LEVEL_CHOICE`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIREGUARD_LOG_LEVEL_INF"></a>

## 409.40 `CONFIG_WIREGUARD_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIREGUARD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］ → WireGuard VPN 服务日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIREGUARD_LOG_LEVEL_CHOICE`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIREGUARD_LOG_LEVEL_OFF"></a>

## 409.41 `CONFIG_WIREGUARD_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIREGUARD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］ → WireGuard VPN 服务日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIREGUARD_LOG_LEVEL_CHOICE`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIREGUARD_LOG_LEVEL_WRN"></a>

## 409.42 `CONFIG_WIREGUARD_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIREGUARD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］ → WireGuard VPN 服务日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_WIREGUARD_LOG_LEVEL_CHOICE`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIREGUARD_MAX_PEER"></a>

## 409.43 `CONFIG_WIREGUARD_MAX_PEER`

**提示（Prompt）**：对端连接（Peer connection）的最大数量

**说明（Help）**

允许的 WireGuard VPN 连接数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIREGUARD && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`subsys/net/lib/wireguard/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_WIREGUARD`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIREGUARD_MAX_SRC_IPS"></a>

## 409.44 `CONFIG_WIREGUARD_MAX_SRC_IPS`

**提示（Prompt）**：对端源 IP 地址（Peer source IP address）的最大数量

**说明（Help）**

每个对端（Peer）允许的 IP 地址数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIREGUARD && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`subsys/net/lib/wireguard/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_WIREGUARD`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIREGUARD_PORT"></a>

## 409.45 `CONFIG_WIREGUARD_PORT`

**提示（Prompt）**：使用的 UDP 端口（Port）

**说明（Help）**

服务器角色监听连接或连接其他主机时使用的 UDP 端口。设为 0 时，由 WireGuard 代码选择端口。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIREGUARD && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
51820
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：[`subsys/net/lib/wireguard/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_WIREGUARD`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIREGUARD_TXRX_DEBUG"></a>

## 409.46 `CONFIG_WIREGUARD_TXRX_DEBUG`

**提示（Prompt）**：调试虚拟接口接收和发送的数据包（Virtual interface packet）

**说明（Help）**

启用接收和发送网络数据包的打印，可能产生大量输出，因此默认禁用。打印发生在虚拟接口 `wg0` 层。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIREGUARD_LOG_LEVEL_DBG && CONFIG_WIREGUARD && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/wireguard/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → WireGuard 虚拟专用网络（VPN）服务［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_WIREGUARD_LOG_LEVEL_DBG`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD_LOG_LEVEL_DBG)、[`CONFIG_WIREGUARD`](P409_subsys_net_配置项参考_19.md#CONFIG_WIREGUARD)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_ZPERF_SESSION_PER_THREAD"></a>

## 409.47 `CONFIG_ZPERF_SESSION_PER_THREAD`

**提示（Prompt）**：为每个会话运行独立线程（Separate thread）

**说明（Help）**

每个会话（Session）在自己的线程中启动。多个线程需要各自的栈空间，会使用更多内存，因此默认禁用。用户也可分别设置线程优先级；启动会话时未指定优先级，则使用 `ZPERF_WORK_Q_THREAD_PRIORITY` 作为默认值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ZPERF_IPERF2 && CONFIG_NET_ZPERF && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF_IPERF2`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_IPERF2)、[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_ZPERF_WORK_Q_STACK_SIZE"></a>

## 409.48 `CONFIG_ZPERF_WORK_Q_STACK_SIZE`

**提示（Prompt）**：zperf 工作队列线程栈大小（Work queue thread stack size）

**说明（Help）**

处理 zperf 工作队列（Work queue）的线程所用栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ZPERF && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_ZPERF_WORK_Q_THREAD_PRIORITY"></a>

## 409.49 `CONFIG_ZPERF_WORK_Q_THREAD_PRIORITY`

**提示（Prompt）**：zperf 工作队列线程优先级（Work queue thread priority）

**说明（Help）**

处理 zperf 工作队列（Work queue）的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ZPERF && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NUM_PREEMPT_PRIORITIES
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NUM_PREEMPT_PRIORITIES`](P001_kernel_配置项参考_1.md#CONFIG_NUM_PREEMPT_PRIORITIES)。

<a id="CONFIG_ZVFS_EVENTFD_ADD_SIZE_COAP_CLIENT"></a>

## 409.50 `CONFIG_ZVFS_EVENTFD_ADD_SIZE_COAP_CLIENT`

**提示（Prompt）**：CoAP 客户端需要的事件文件描述符（eventfd）数量

**说明（Help）**

CoAP 客户端分配一个 zvfs 事件文件描述符（eventfd），用于唤醒轮询循环（Poll loop）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_CLIENT && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 客户端支持（client support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_CLIENT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_CLIENT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_ZVFS_EVENTFD_ADD_SIZE_COAP_SERVER"></a>

## 409.51 `CONFIG_ZVFS_EVENTFD_ADD_SIZE_COAP_SERVER`

**提示（Prompt）**：CoAP 服务器需要的事件文件描述符（eventfd）数量

**说明（Help）**

CoAP 服务器分配一个 zvfs 事件文件描述符（eventfd），用于唤醒轮询循环（Poll loop）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_SERVER && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:250`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L250)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 服务器支持（server support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_SERVER`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_ZVFS_EVENTFD_ADD_SIZE_HTTP_SERVER"></a>

## 409.52 `CONFIG_ZVFS_EVENTFD_ADD_SIZE_HTTP_SERVER`

**提示（Prompt）**：HTTP 服务器需要的事件文件描述符（eventfd）数量

**说明（Help）**

HTTP 服务器分配一个常驻 zvfs 事件文件描述符（eventfd），用于唤醒轮询循环（Poll loop）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_ZVFS_EVENTFD_ADD_SIZE_LWM2M"></a>

## 409.53 `CONFIG_ZVFS_EVENTFD_ADD_SIZE_LWM2M`

**提示（Prompt）**：LwM2M 引擎需要的事件文件描述符（eventfd）数量

**说明（Help）**

在无周期时钟节拍（Tickless）模式下，LwM2M 引擎分配一个 zvfs 事件文件描述符（eventfd），用于唤醒轮询循环（Poll loop）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_TICKLESS && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:176`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L176)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_TICKLESS`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_TICKLESS)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_ZVFS_EVENTFD_ADD_SIZE_PTP"></a>

## 409.54 `CONFIG_ZVFS_EVENTFD_ADD_SIZE_PTP`

**提示（Prompt）**：PTP 协议栈需要的事件文件描述符（eventfd）数量

**说明（Help）**

PTP 协议栈分配一个 zvfs 事件文件描述符（eventfd），用于唤醒轮询循环（Poll loop）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_ZVFS_EVENTFD_ADD_SIZE_SOCKETS_SERVICE"></a>

## 409.55 `CONFIG_ZVFS_EVENTFD_ADD_SIZE_SOCKETS_SERVICE`

**提示（Prompt）**：套接字服务（Socket service）需要的事件文件描述符（eventfd）数量

**说明（Help）**

套接字服务分派器（Socket service dispatcher）分配一个常驻 `zvfs_eventfd`，用于在轮询（Polling）期间触发事件。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SERVICE && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SERVICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SERVICE)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_ZVFS_EVENTFD_ADD_SIZE_SSH_CLIENT"></a>

## 409.56 `CONFIG_ZVFS_EVENTFD_ADD_SIZE_SSH_CLIENT`

**提示（Prompt）**：SSH 客户端需要的事件文件描述符（eventfd）数量

**说明（Help）**

每个 SSH 客户端实例分配一个 zvfs 事件文件描述符（eventfd），用于唤醒轮询循环（Poll loop）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH_CLIENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_SSH_CLIENT_MAX_CLIENTS
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH_CLIENT`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_CLIENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SSH_CLIENT_MAX_CLIENTS`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_CLIENT_MAX_CLIENTS)。

<a id="CONFIG_ZVFS_EVENTFD_ADD_SIZE_SSH_SERVER"></a>

## 409.57 `CONFIG_ZVFS_EVENTFD_ADD_SIZE_SSH_SERVER`

**提示（Prompt）**：SSH 服务器需要的事件文件描述符（eventfd）数量

**说明（Help）**

每个 SSH 服务器实例分配一个 zvfs 事件文件描述符（eventfd），用于唤醒轮询循环（Poll loop）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_SSH_SERVER_MAX_SERVERS
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH_SERVER`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SSH_SERVER_MAX_SERVERS`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_SERVER_MAX_SERVERS)。

<a id="CONFIG_ZVFS_OPEN_ADD_SIZE_NET"></a>

## 409.58 `CONFIG_ZVFS_OPEN_ADD_SIZE_NET`

**提示（Prompt）**：要分配的网络套接字（Network socket）数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_MAX_CONTEXTS if CONFIG_NET_NATIVE && CONFIG_NET_SOCKETS
0
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:567`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L567)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MAX_CONTEXTS`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MAX_CONTEXTS)、[`CONFIG_NET_NATIVE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_NATIVE)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)。

<a id="CONFIG_ZVFS_OPEN_ADD_SIZE_QUIC_ENDPOINTS"></a>

## 409.59 `CONFIG_ZVFS_OPEN_ADD_SIZE_QUIC_ENDPOINTS`

**提示（Prompt）**：端点套接字描述符（Endpoint socket descriptor）的数量需求

**说明（Help）**

每个端点（Endpoint）需要一个 UDP 套接字，因此应增加 ZVFS 描述符（Descriptor）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_QUIC_MAX_ENDPOINTS
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:360`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L360)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC_MAX_ENDPOINTS`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_MAX_ENDPOINTS)。

<a id="CONFIG_ZVFS_OPEN_ADD_SIZE_SOCKETS_SERVICE"></a>

## 409.60 `CONFIG_ZVFS_OPEN_ADD_SIZE_SOCKETS_SERVICE`

**提示（Prompt）**：套接字服务（Socket service）的文件描述符需求

**说明（Help）**

套接字服务会打开一个常驻 `zvfs_eventfd`，占用一个文件描述符（File descriptor）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_ZVFS_OPEN_ADD_SIZE_TLS"></a>

## 409.61 `CONFIG_ZVFS_OPEN_ADD_SIZE_TLS`

**提示（Prompt）**：要分配的 TLS 网络套接字（Network socket）数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_SOCKETS_TLS_MAX_CONTEXTS if CONFIG_NET_SOCKETS_SOCKOPT_TLS
0
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:238`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L238)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS_TLS_MAX_CONTEXTS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_TLS_MAX_CONTEXTS)、[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS)。

<!-- kconfig-navigation -->

[上一章](P408_subsys_net_配置项参考_18.md) · [返回大纲](大纲.md) · [下一章](P410_subsys_nvmem_配置项参考.md)
