---
id: learning.zephyr-docs.kconfig-reference.page-323
title: "`subsys/bluetooth`配置项参考（4/13）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第323章\_`subsys/bluetooth`配置项参考（4/13）

本章翻译官方 Kconfig 数据库中 `subsys/bluetooth` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_CTLR_EVENT_IFS_LOW_LAT_US"></a>

## 323.1 `CONFIG_BT_CTLR_EVENT_IFS_LOW_LAT_US`

**提示（Prompt）**：低延迟 tIFS 值，单位为微秒（Low latency tIFS value）

**说明（Help）**

设置低延迟帧间间隔（tIFS）值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
52 if CONFIG_BT_CTLR_CONN_INTERVAL_LOW_LATENCY
150
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1197`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1197)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 允许低延迟连接间隔（Allow low latency connection intervals）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_CONN_INTERVAL_LOW_LATENCY`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CONN_INTERVAL_LOW_LATENCY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_EVENT_OVERHEAD_RESERVE_MAX"></a>

## 323.2 `CONFIG_BT_CTLR_EVENT_OVERHEAD_RESERVE_MAX`

**提示（Prompt）**：在时间预留中计入最大事件开销（Reserve maximum event overhead in time reservations）

**说明（Help）**

计算事件时间预留量（event time reservations）时，使用无线电事件调度所需的 CPU 时间开销。如果禁用此选项，外设 ACL 和外设 ISO 角色（Peripheral ACL/ISO role）不计入 CPU 时间开销；其他角色仍会在事件时间预留量中计入 CPU 开销。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:861`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L861)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_EXTENDED_FEAT_SET"></a>

## 323.3 `CONFIG_BT_CTLR_EXTENDED_FEAT_SET`

**提示（Prompt）**：链路层扩展功能集支持（LL Extended Feature Set support）

**说明（Help）**

在控制器（Controller）中启用蓝牙 6.0 链路层扩展功能集（LL Extended Feature Set）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_EXTENDED_FEAT_SET_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_LE_EXTENDED_FEAT_SET
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1183`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1183)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_EXTENDED_FEAT_SET_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_EXTENDED_FEAT_SET_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_LE_EXTENDED_FEAT_SET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LE_EXTENDED_FEAT_SET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_EXTENDED_FEAT_SET_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_EXT_REJ_IND"></a>

## 323.4 `CONFIG_BT_CTLR_EXT_REJ_IND`

**提示（Prompt）**：扩展拒绝指示（Extended Reject Indication）

**说明（Help）**

在控制器（Controller）中启用蓝牙 v4.1 扩展拒绝指示（Extended Reject Indication）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT && CONFIG_BT_CONN && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_BT_CTLR_CONN_PARAM_REQ
CONFIG_BT_CTLR_PHY
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:579`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L579)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_CONN_PARAM_REQ`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CONN_PARAM_REQ)、[`CONFIG_BT_CTLR_PHY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT`、`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_PHY`。

<a id="CONFIG_BT_CTLR_EXT_SCAN_FP"></a>

## 323.5 `CONFIG_BT_CTLR_EXT_SCAN_FP`

**提示（Prompt）**：低功耗蓝牙扩展扫描器过滤策略（LE Extended Scanner Filter Policies）

**说明（Help）**

在控制器（Controller）中启用蓝牙 v4.2 低功耗蓝牙扩展扫描器过滤策略（LE Extended Scanner Filter Policies）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_CTLR_EXT_SCAN_FP_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:707`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L707)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_CTLR_EXT_SCAN_FP_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_EXT_SCAN_FP_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_EXT_SCAN_FP_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_FAL_SIZE"></a>

## 323.6 `CONFIG_BT_CTLR_FAL_SIZE`

**提示（Prompt）**：基于控制器的低功耗蓝牙隐私接纳列表大小（LE Controller-based Privacy Accept List size）

**说明（Help）**

设置基于控制器的低功耗蓝牙隐私（LE Controller-based Privacy）所用过滤接纳列表（Filter Accept List）的大小。基于 nRF5x 的控制器受硬件限制，最多支持 `8` 个设备；基于 OpenISA 的控制器也受硬件限制，最多支持 `8` 个设备。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_FILTER_ACCEPT_LIST && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 8] if CONFIG_SOC_COMPATIBLE_NRF || CONFIG_SOC_OPENISA_RV32M1
[1, 16] if !(CONFIG_SOC_COMPATIBLE_NRF || CONFIG_SOC_OPENISA_RV32M1)
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:685`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L685)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_FILTER_ACCEPT_LIST`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_FILTER_ACCEPT_LIST)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)、[`CONFIG_SOC_OPENISA_RV32M1`](P298_soc_openisa_配置项参考.md#CONFIG_SOC_OPENISA_RV32M1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_SOC_COMPATIBLE_NRF`。

<a id="CONFIG_BT_CTLR_FILTER_ACCEPT_LIST"></a>

## 323.7 `CONFIG_BT_CTLR_FILTER_ACCEPT_LIST`

**提示（Prompt）**：过滤接纳列表支持（Filter Accept List Support）

**说明（Help）**

启用控制器过滤接纳列表（Filter Accept List）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HCI_RAW || CONFIG_BT_FILTER_ACCEPT_LIST
```

**被选择（Selected by）**

```text
CONFIG_BT_CTLR_PRIVACY
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:668`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L668)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)、[`CONFIG_BT_FILTER_ACCEPT_LIST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_FILTER_ACCEPT_LIST)、[`CONFIG_BT_CTLR_PRIVACY`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_PRIVACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_FORCE_MD_AUTO"></a>

## 323.8 `CONFIG_BT_CTLR_FORCE_MD_AUTO`

**提示（Prompt）**：强制 MD 位的自动计算（Forced MD bit automatic calculation）

**说明（Help）**

根据运行时传入待发送数据的吞吐量（transmit data throughput），强制设置所发送 PDU 的 MD 位（More Data bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_THROUGHPUT && !CONFIG_BT_CTLR_LOW_LAT && CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1152)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_THROUGHPUT`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_THROUGHPUT)、[`CONFIG_BT_CTLR_LOW_LAT`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_LOW_LAT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_FORCE_MD_COUNT"></a>

## 323.9 `CONFIG_BT_CTLR_FORCE_MD_COUNT`

**提示（Prompt）**：强制设置 MD 位的次数（Forced MD bit count）

**说明（Help）**

成功发送非空 PDU 后，在发送 PDU（Tx PDU）中强制置位 MD 的次数。如果应用希望在同一连接事件（connection event）中继续发送数据，却不能及时提供新的发送数据，此设置可延长连接事件，避免其提前关闭。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_BT_CTLR_LOW_LAT && CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1 if CONFIG_BT_CTLR_FORCE_MD_AUTO
0
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1138)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_LOW_LAT`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_LOW_LAT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_FORCE_MD_AUTO`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_FORCE_MD_AUTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_FRAME_SPACE_UPDATE"></a>

## 323.10 `CONFIG_BT_CTLR_FRAME_SPACE_UPDATE`

**提示（Prompt）**：帧间隔更新（Frame Space Update）

**说明（Help）**

在控制器（Controller）中启用蓝牙 6.0 帧间隔更新（Frame Space Update）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_FRAME_SPACE_UPDATE_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_FRAME_SPACE_UPDATE
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1166)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_FRAME_SPACE_UPDATE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_FRAME_SPACE_UPDATE_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_FRAME_SPACE_UPDATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_FRAME_SPACE_UPDATE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_FRAME_SPACE_UPDATE_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_HCI"></a>

## 323.11 `CONFIG_BT_CTLR_HCI`

**提示（Prompt）**：主机控制器接口（Host Controller Interface，HCI）

**说明（Help）**

在控制器中启用主机控制器接口（Host Controller Interface，HCI）。除单元测试（unit testing）等少数特殊情况外，几乎都应启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_HCI_ADV_HANDLE_MAPPING"></a>

## 323.12 `CONFIG_BT_CTLR_HCI_ADV_HANDLE_MAPPING`

**提示（Prompt）**：HCI 与 LL 之间的广播集合句柄映射（Advertising set handle mapping）

**说明（Help）**

使用外部主机（external host）时，启用 HCI 与链路层（LL）之间的广播集合句柄（advertising set handles）映射。外部主机可以按核心规范规定使用任意数字作为集合句柄，而 LL 始终采用从零开始的编号。使用 Zephyr 主机时可以禁用此选项，去掉额外的映射逻辑。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HCI_RAW
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:200`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L200)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_HCI_CODEC_AND_DELAY_INFO"></a>

## 323.13 `CONFIG_BT_CTLR_HCI_CODEC_AND_DELAY_INFO`

**提示（Prompt）**：编解码器与控制器延迟信息命令（Codecs and controller delay information commands）

**说明（Help）**

启用用于读取受支持的编解码器（codecs）、编解码器能力（codec capabilities）及控制器延迟（controller delay）信息的 HCI 命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_HCI && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_CTLR_ISO_VENDOR_DATA_PATH
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1150)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_HCI`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_HCI)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_ISO_VENDOR_DATA_PATH`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_ISO_VENDOR_DATA_PATH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_HCI_VS_BUILD_INFO"></a>

## 323.14 `CONFIG_BT_CTLR_HCI_VS_BUILD_INFO`

**提示（Prompt）**：Zephyr HCI VS 构建信息字符串（Zephyr HCI VS Build Info string）

**说明（Help）**

用户定义的字符串，Zephyr 厂商专用读取构建信息命令（VS Read Build Information）会将其放在 Zephyr 版本和构建时间之后返回。若将其设置为非空字符串，必须在开头添加一个空格，与已有信息分隔。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_HCI && CONFIG_BT_HCI_VS && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:210`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L210)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_HCI`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_HCI)、[`CONFIG_BT_HCI_VS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_VS)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ISOAL_FRAMED_BIS_OFFSET_MARGIN"></a>

## 323.15 `CONFIG_BT_CTLR_ISOAL_FRAMED_BIS_OFFSET_MARGIN`

**提示（Prompt）**：BIS 成帧时间偏移使用的裕量，单位为微秒（framed time offset margin）

**说明（Help）**

可靠交付有效载荷（payloads）所需的裕量会有所不同，但通常应为 `EVENT_OVERHEAD_START_US` 加上用于覆盖等时适配层（ISOAL）处理开销的一小段裕量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_ADV_ISO || CONFIG_BT_CTLR_CONN_ISO) && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2000
```

**取值范围（Ranges）**

```text
[0, 10000]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:660`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L660)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ISOAL_FRAMED_CIS_OFFSET_MARGIN"></a>

## 323.16 `CONFIG_BT_CTLR_ISOAL_FRAMED_CIS_OFFSET_MARGIN`

**提示（Prompt）**：CIS 成帧时间偏移使用的裕量，单位为微秒（framed time offset margin）

**说明（Help）**

注意：连接等时流（CIS）通常不需要裕量；如果有效载荷（payload）未能及时赶上第一个子事件，可以使用空 PDU（null PDUs）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_ADV_ISO || CONFIG_BT_CTLR_CONN_ISO) && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10000]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:670`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L670)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ISOAL_LOG_DBG_VERBOSE"></a>

## 323.17 `CONFIG_BT_CTLR_ISOAL_LOG_DBG_VERBOSE`

**提示（Prompt）**：ISO-AL 详细调试日志（ISO-AL verbose debug logging）

**说明（Help）**

使用此选项启用等时适配层（ISO-AL）的详细调试日志（verbose debug logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ISOAL_LOG_LEVEL = 4 && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:291`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L291)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ISOAL_LOG_LEVEL)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ISOAL_PSN_IGNORE"></a>

## 323.18 `CONFIG_BT_CTLR_ISOAL_PSN_IGNORE`

**提示（Prompt）**：忽略发送 ISO 数据包序列号的使用（Ignore Tx ISO Data Packet Sequence Number use）

**说明（Help）**

忽略发送等时数据包序列号（Tx ISO Data Packet Sequence Number）的使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_ADV_ISO || CONFIG_BT_CTLR_CONN_ISO) && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:654`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L654)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ISOAL_SINKS"></a>

## 323.19 `CONFIG_BT_CTLR_ISOAL_SINKS`

**提示（Prompt）**：等时适配层接收端数量（Number of Isochronous Adaptation Layer sinks）

**说明（Help）**

设置等时适配层（ISO AL）支持的并发活动接收端（sinks）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_SYNC_ISO || CONFIG_BT_CTLR_CONN_ISO) && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:301`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L301)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_ISO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ISOAL_SN_STRICT"></a>

## 323.20 `CONFIG_BT_CTLR_ISOAL_SN_STRICT`

**提示（Prompt）**：严格使用发送 ISO 数据序列号（Enforce Strict Tx ISO Data Sequence Number use）

**说明（Help）**

根据发送服务数据单元（TX SDU）的数据包序列号（packet sequence number），严格确定释放有效载荷（released payloads）的顺序。在将 SDU 分片成非成帧 PDU（unframed PDUs）时生效。

启用后，如果 TX SDU 的数据包序列号没有按 SDU 间隔递增，且向 ISO-AL 交付 SDU 的时序也不严格遵循该间隔，SDU 可能被分配到已经过期的有效载荷编号，从而被丢弃。

禁用后，TX SDU 可能偏离其在流中的对齐位置，并被分片到较不容易被丢弃的有效载荷中。这能改善数据向接收器的交付情况，但代价是在接收到的 SDU 流中产生时序偏斜（skews）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_BT_CTLR_ISOAL_PSN_IGNORE && (CONFIG_BT_CTLR_ADV_ISO || CONFIG_BT_CTLR_CONN_ISO) && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:633`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L633)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ISOAL_PSN_IGNORE`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_ISOAL_PSN_IGNORE)、[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ISOAL_SOURCES"></a>

## 323.21 `CONFIG_BT_CTLR_ISOAL_SOURCES`

**提示（Prompt）**：等时适配层发送端数量（Number of Isochronous Adaptation Layer sources）

**说明（Help）**

设置等时适配层（ISO AL）支持的并发活动发送端（sources）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_ADV_ISO || CONFIG_BT_CTLR_CONN_ISO) && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:292`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L292)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ISO_RX_BUFFERS"></a>

## 323.22 `CONFIG_BT_CTLR_ISO_RX_BUFFERS`

**提示（Prompt）**：等时接收缓冲区数量（Number of Isochronous Rx buffers）

**说明（Help）**

设置控制器中可缓存的等时接收 PDU（Isochronous Rx PDUs）数量。最坏情况下，所需接收缓冲区数量等于为每个活动 ISO 组在一个 ISO 事件中准备的接收节点（RX nodes）总数。该数量取决于 ISO 组中的突发（bursts）数量和组数量，实际配置可能需要低于理论最大值。默认值 `8` 用于支持两个各含 4 个有效载荷的组，例如 `2` 个 CIG，每个 CIG 包含 `2` 个 `BN=2` 的 CIS。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_SYNC_ISO || CONFIG_BT_CTLR_CONN_ISO) && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 30]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:251`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L251)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_ISO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ISO_RX_SDU_BUFFERS"></a>

## 323.23 `CONFIG_BT_CTLR_ISO_RX_SDU_BUFFERS`

**提示（Prompt）**：ISO-AL 可缓存的 SDU 分片数量（Number of SDU fragments that the ISO-AL can buffer）

**说明（Help）**

设置等时适配层（ISO-AL）为每个接收端（sink）缓存的等时接收 SDU 分片（Isochronous Rx SDU fragments）数量。需要先缓存所有分片，以在逐个释放之前计算完整接收 SDU 的大小和状态。缓冲区数量与 SDU 分片最大大小共同限制了能够在 HCI ISO 数据头（Data header）中准确声明的 SDU 最大大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_SYNC_ISO || CONFIG_BT_CTLR_CONN_ISO) && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:310`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L310)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_ISO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ISO_TX_BUFFERS"></a>

## 323.24 `CONFIG_BT_CTLR_ISO_TX_BUFFERS`

**提示（Prompt）**：等时发送缓冲区数量（Number of Isochronous Tx buffers）

**说明（Help）**

设置控制器中可排队等待发送的等时发送 PDU（Isochronous Tx PDUs）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_ADV_ISO || CONFIG_BT_CTLR_CONN_ISO) && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ISO_TX_BUF_COUNT if CONFIG_BT_ISO
3
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L265)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_TX_BUF_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_TX_BUF_COUNT)、[`CONFIG_BT_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_ISO`。

<a id="CONFIG_BT_CTLR_ISO_TX_BUFFER_SIZE"></a>

## 323.25 `CONFIG_BT_CTLR_ISO_TX_BUFFER_SIZE`

**提示（Prompt）**：等时发送缓冲区大小（Isochronous Tx buffer size）

**说明（Help）**

等时发送缓冲区（Isochronous Tx buffers）的大小，也是 HCI `LE Read Buffer Size V2` 命令响应返回的值。它表示 HCI ISO 数据包的数据部分，对应 `Data_Total_Length` 字段。所译快照中 SDU 最大长度为 `4095` 字节，因此还需增加 `8` 字节的 HCI ISO 数据包开销，包括 `Packet_Sequence_Number`、`ISO_SDU_Length`、`Packet_Status_Flag` 字段，以及在提供时包含的可选 `Time_Stamp` 字段。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_ADV_ISO || CONFIG_BT_CTLR_CONN_ISO) && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
9 if CONFIG_BT_LL_SW_SPLIT
1
```

**取值范围（Ranges）**

```text
[9, 4103] if CONFIG_BT_LL_SW_SPLIT
[1, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:275`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L275)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ISO_TX_SDU_LEN_MAX"></a>

## 323.26 `CONFIG_BT_CTLR_ISO_TX_SDU_LEN_MAX`

**提示（Prompt）**：等时信道发送 SDU 最大长度（Maximum Isochronous Channel Transmit SDU Length）

**说明（Help）**

等时信道（Isochronous Channel）发送服务数据单元（Transmit SDU）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_ADV_ISO || CONFIG_BT_CTLR_CONN_ISO) && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 4095]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1097`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1097)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ISO_TX_SEG_PLAYLOAD_MIN"></a>

## 323.27 `CONFIG_BT_CTLR_ISO_TX_SEG_PLAYLOAD_MIN`

**提示（Prompt）**：新分段中的有效载荷数据最小字节数（Minimum payload data bytes in a new segment）

**说明（Help）**

使向 PDU 中插入一个新分段（segment）值得进行的最小有效载荷字节数（payload bytes）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_ADV_ISO || CONFIG_BT_CTLR_CONN_ISO) && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:298`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L298)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ISO_VENDOR_DATA_PATH"></a>

## 323.28 `CONFIG_BT_CTLR_ISO_VENDOR_DATA_PATH`

**提示（Prompt）**：厂商专用 ISO 数据路径（Vendor-specific ISO data path）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_SYNC_ISO || CONFIG_BT_CTLR_CONN_ISO) && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_HCI_CODEC_AND_DELAY_INFO
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:323`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L323)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_ISO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_HCI_CODEC_AND_DELAY_INFO`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_HCI_CODEC_AND_DELAY_INFO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_JIT_SCHEDULING"></a>

## 323.29 `CONFIG_BT_CTLR_JIT_SCHEDULING`

**提示（Prompt）**：即时调度（Just-in-Time Scheduling）

**说明（Help）**

此选项启用实验性的“下一代”（Next Generation）调度功能：移除 ticker 中的优先级和冲突解决（collision resolving），改为依靠链路层中的即时、惰性处理（just-in-time, lazy resolution）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TICKER_SLOT_AGNOSTIC && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1382`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1382)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_TICKER_SLOT_AGNOSTIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_SLOT_AGNOSTIC)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_LE_ENC"></a>

## 323.30 `CONFIG_BT_CTLR_LE_ENC`

**提示（Prompt）**：低功耗蓝牙加密（LE Encryption）

**说明（Help）**

在控制器（Controller）中启用蓝牙 v4.0 低功耗蓝牙加密（LE Encryption）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_LE_ENC_SUPPORT && CONFIG_BT_CONN && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:554`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L554)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_LE_ENC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_LE_ENC_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_LE_ENC_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_LE_PATH_LOSS_MONITORING"></a>

## 323.31 `CONFIG_BT_CTLR_LE_PATH_LOSS_MONITORING`

**提示（Prompt）**：低功耗蓝牙路径损耗监测功能（LE Path Loss Monitoring Feature）

**说明（Help）**

启用低功耗蓝牙路径损耗监测（LE Path Loss Monitoring）功能支持，其定义见蓝牙核心规范（Bluetooth Core specification）Version 5.4，Vol 6, Part B, Section 4.6.32。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_LE_PATH_LOSS_MONITORING_SUPPORT && CONFIG_BT_CONN && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_PATH_LOSS_MONITORING
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:658`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L658)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_LE_PATH_LOSS_MONITORING_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_LE_PATH_LOSS_MONITORING_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_PATH_LOSS_MONITORING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PATH_LOSS_MONITORING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_LE_PATH_LOSS_MONITORING_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_LE_PING"></a>

## 323.32 `CONFIG_BT_CTLR_LE_PING`

**提示（Prompt）**：低功耗蓝牙 Ping（LE Ping）

**说明（Help）**

在控制器（Controller）中启用蓝牙 v4.1 低功耗蓝牙 Ping（LE Ping）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_LE_ENC && CONFIG_BT_CONN && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:595`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L595)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_LE_ENC`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_LE_ENC)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_LE_POWER_CONTROL"></a>

## 323.33 `CONFIG_BT_CTLR_LE_POWER_CONTROL`

**提示（Prompt）**：低功耗蓝牙功率控制请求功能（LE Power Control Request Feature）

**说明（Help）**

启用低功耗蓝牙功率控制请求（LE Power Control Request）功能支持，其定义见蓝牙核心规范（Bluetooth Core specification）Version 5.4，Vol 6, Part B, Section 4.6.31。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_LE_POWER_CONTROL_SUPPORT && CONFIG_BT_CONN && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_TRANSMIT_POWER_CONTROL
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:650`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L650)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_LE_POWER_CONTROL_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_LE_POWER_CONTROL_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TRANSMIT_POWER_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TRANSMIT_POWER_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_LE_POWER_CONTROL_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_LLCP_COMMON_TX_CTRL_BUF_NUM"></a>

## 323.34 `CONFIG_BT_CTLR_LLCP_COMMON_TX_CTRL_BUF_NUM`

**提示（Prompt）**：所有连接共享的可用发送控制缓冲区数量（tx control buffers across all connections）

**说明（Help）**

设置可用于发送的控制缓冲区（control buffers）数量，即控制过程发送（control procedure TX）所用发送缓冲池的大小。该池由所有过程／连接共享，通过先进先出队列（FIFO queue）分配。配置范围为 `0` 到 `(4 - BT_CTLR_LLCP_PER_CONN_TX_CTRL_BUF_NUM) * BT_CTLR_LLCP_CONN`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1072`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1072)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_LLCP_CONN"></a>

## 323.35 `CONFIG_BT_CTLR_LLCP_CONN`

**提示（Prompt）**：最坏情况下过程重叠的连接数量（connections with worst-case overlapping procedures）

**说明（Help）**

设置必须满足链路层控制协议（LLCP）过程最坏缓冲需求的连接数量。如果同时在更多连接上执行 LLCP 过程，可能导致不稳定。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MAX_CONN
```

**取值范围（Ranges）**

```text
[1, CONFIG_BT_MAX_CONN]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1044`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1044)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MAX_CONN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAX_CONN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_LLCP_LOCAL_PROC_CTX_BUF_NUM"></a>

## 323.36 `CONFIG_BT_CTLR_LLCP_LOCAL_PROC_CTX_BUF_NUM`

**提示（Prompt）**：所有连接共享的本地控制过程上下文数量（local control procedure contexts）

**说明（Help）**

设置可用的控制过程上下文（control procedure contexts）数量，即用于处理本地发起控制过程（locally initiated control procedures）的上下文池大小。该池由所有连接共享，通过队列分配。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
6 if CONFIG_BT_AUTO_DATA_LEN_UPDATE = y && CONFIG_BT_CTLR_LLCP_CONN < 4
2 if CONFIG_BT_CTLR_LLCP_CONN = 1
CONFIG_BT_CTLR_LLCP_CONN if CONFIG_BT_CTLR_LLCP_CONN > 1
```

**取值范围（Ranges）**

```text
[2, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1083`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1083)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AUTO_DATA_LEN_UPDATE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUTO_DATA_LEN_UPDATE)、[`CONFIG_BT_CTLR_LLCP_CONN`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_LLCP_CONN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_LLCP_PER_CONN_TX_CTRL_BUF_NUM"></a>

## 323.37 `CONFIG_BT_CTLR_LLCP_PER_CONN_TX_CTRL_BUF_NUM`

**提示（Prompt）**：每条连接预留的发送控制缓冲区数量（tx control buffers reserved per connection）

**说明（Help）**

设置为每条连接预先分配的控制缓冲区（control buffers）数量，确定任意连接至少可用的缓冲区数量。设为非零可确保连接始终能够取得控制过程发送（control procedure TX）所需的缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CTLR_LLCP_TX_PER_CONN_TX_CTRL_BUF_NUM_MAX
```

**取值范围（Ranges）**

```text
[0, CONFIG_BT_CTLR_LLCP_TX_PER_CONN_TX_CTRL_BUF_NUM_MAX]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1062`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1062)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_LLCP_TX_PER_CONN_TX_CTRL_BUF_NUM_MAX`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_LLCP_TX_PER_CONN_TX_CTRL_BUF_NUM_MAX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_LLCP_REMOTE_PROC_CTX_BUF_NUM"></a>

## 323.38 `CONFIG_BT_CTLR_LLCP_REMOTE_PROC_CTX_BUF_NUM`

**提示（Prompt）**：所有连接共享的远端控制过程上下文数量（remote control procedure contexts）

**说明（Help）**

设置可用的控制过程上下文（control procedure contexts）数量，即用于处理远端发起控制过程（remotely initiated control procedures）的上下文池大小。该池由所有连接共享，通过队列分配。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CTLR_LLCP_CONN
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1095`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1095)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_LLCP_CONN`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_LLCP_CONN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_LLCP_TX_PER_CONN_TX_CTRL_BUF_NUM_MAX"></a>

## 323.39 `CONFIG_BT_CTLR_LLCP_TX_PER_CONN_TX_CTRL_BUF_NUM_MAX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

理论上，任意一条连接所需发送控制缓冲区（tx ctrl buffers）的最大数量为 `4`：活动加密过程（active encryption procedure）需要两个，拒绝远端请求需要一个，本地主动终止（local terminate）需要一个。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1054`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1054)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_LLID_DATA_START_EMPTY"></a>

## 323.40 `CONFIG_BT_CTLR_LLID_DATA_START_EMPTY`

**提示（Prompt）**：处理零长度 L2CAP 起始帧（Handle zero length L2CAP start frame）

**说明（Help）**

处理零长度的 L2CAP 起始帧（start frame）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HCI_RAW
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_LLL_PREPARE_AT_MARGIN"></a>

## 323.41 `CONFIG_BT_CTLR_LLL_PREPARE_AT_MARGIN`

**提示（Prompt）**：在准备裕量时刻执行 LLL 准备（LLL prepare at margin）

**说明（Help）**

在准备裕量时刻（prepare margin）执行下层链路层（LLL）准备回调，即使当前没有活动的重叠状态／角色也如此。这会使 CPU 在准备 tick（prepare tick）处首次唤醒之后，再额外唤醒一次。

LLL 准备回调在具有硬实时要求的无线电发送或接收时刻之前足够早地执行，因此，如果某项资源在准备 tick 时就设置好会提前消耗电流，则可将其设置推迟到准备裕量对应的时刻。

如果必须在硬实时无线电发送或接收时刻就绪的资源，可以在准备 tick 时设置，且在实际需要它们之前不会影响电流消耗，则禁用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_BT_CTLR_LOW_LAT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_COMPATIBLE_NRF54LX
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:907`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L907)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_LOW_LAT`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_LOW_LAT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_LLL_PRIO"></a>

## 323.42 `CONFIG_BT_CTLR_LLL_PRIO`

**提示（Prompt）**：下层链路层（无线电）IRQ 优先级（Lower Link Layer Radio IRQ priority）

**说明（Help）**

事件准备（event preparation）和无线电中断请求（radio IRQ）的中断优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 3] if CONFIG_SOC_SERIES_NRF51
[0, 6] if CONFIG_SOC_COMPATIBLE_NRF52X || CONFIG_SOC_COMPATIBLE_NRF53X
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:880`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L880)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_SOC_COMPATIBLE_NRF52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF52X)、[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_SOC_COMPATIBLE_NRF52X`、`CONFIG_SOC_COMPATIBLE_NRF53X`。

<a id="CONFIG_BT_CTLR_LOW_LAT"></a>

## 323.43 `CONFIG_BT_CTLR_LOW_LAT`

**提示（Prompt）**：低延迟非协商式事件抢占（Low latency non-negotiating event preemption）

**说明（Help）**

使用低延迟非协商式事件抢占（low latency non-negotiating event preemption），减少控制器事件调度框架造成的无线电中断服务例程（Radio ISR）延迟。但冗余的无线电状态切换也会降低空中无线电利用率（on-air radio utilization）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_LOW_LAT_ULL && CONFIG_BT_CTLR_LOW_LAT_ULL_DONE && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_NRF51
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:927`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L927)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_LOW_LAT_ULL`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_LOW_LAT_ULL)、[`CONFIG_BT_CTLR_LOW_LAT_ULL_DONE`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_LOW_LAT_ULL_DONE)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_LOW_LAT_ULL"></a>

## 323.44 `CONFIG_BT_CTLR_LOW_LAT_ULL`

**提示（Prompt）**：低延迟上层链路层（Low latency ULL）

**说明（Help）**

低延迟上层链路层（ULL）实现，使用尾链（tailchaining）代替 `while` 循环，对来自下层链路层（LLL）的接收消息进行分派（demux）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_NRF51
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:937`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L937)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_LOW_LAT_ULL_DONE"></a>

## 323.45 `CONFIG_BT_CTLR_LOW_LAT_ULL_DONE`

**提示（Prompt）**：低延迟 ULL 准备出队（Low latency ULL prepare dequeue）

**说明（Help）**

在上层链路层（ULL）上下文中处理完成事件（Done events）并使其出队。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_NRF51
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:944`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L944)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_MESH_SCAN_FILTERS"></a>

## 323.46 `CONFIG_BT_CTLR_MESH_SCAN_FILTERS`

**提示（Prompt）**：Mesh 扫描过滤器数量（Number of Mesh scan filters）

**说明（Help）**

设置 Intel Mesh 厂商专用扩展（Vendor Specific Extensions）可提供的不同 Mesh 扫描过滤器（Scan Filters）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_MESH_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 15]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_MESH_EXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_MESH_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_MESH_SF_PATTERNS"></a>

## 323.47 `CONFIG_BT_CTLR_MESH_SF_PATTERNS`

**提示（Prompt）**：Mesh 扫描过滤模式数量（Number of Mesh scan filter patterns）

**说明（Help）**

设置 Intel Mesh 厂商专用扩展（Vendor Specific Extensions）中，每个扫描过滤器（Scan Filter）可提供的不同 Mesh 扫描过滤模式（Scan Filter patterns）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_MESH_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
15
```

**取值范围（Ranges）**

```text
[1, 15]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:220`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L220)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_MESH_EXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_MESH_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_MIN_USED_CHAN"></a>

## 323.48 `CONFIG_BT_CTLR_MIN_USED_CHAN`

**提示（Prompt）**：最少使用信道数（Minimum Number of Used Channels）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.0 最少使用信道数过程（Minimum Number of Used Channels Procedure）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_MIN_USED_CHAN_SUPPORT && CONFIG_BT_CONN && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:627`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L627)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_MIN_USED_CHAN_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_MIN_USED_CHAN_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_MIN_USED_CHAN_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_NRF_GRTC"></a>

## 323.49 `CONFIG_BT_CTLR_NRF_GRTC`

**提示（Prompt）**：使用 nRF GRTC 外设（Use nRF GRTC peripheral）

**说明（Help）**

启用 nRF54Lx 的 `NRF_GRTC` 外设（peripheral）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TICKER_CNTR_FREE_RUNNING && CONFIG_SOC_COMPATIBLE_NRF54LX && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:961`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L961)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_TICKER_CNTR_FREE_RUNNING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_CNTR_FREE_RUNNING)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TICKER_CNTR_FREE_RUNNING`、`CONFIG_SOC_COMPATIBLE_NRF54LX`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_NRF_GRTC_AUTOEN_CPUACTIVE"></a>

## 323.50 `CONFIG_BT_CTLR_NRF_GRTC_AUTOEN_CPUACTIVE`

**提示（Prompt）**：CPU 活动时自动启用 nRF GRTC（Auto enable nRF GRTC on CPU active）

**说明（Help）**

在 CPU 处于活动状态（active）时自动启用 nRF GRTC。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_NRF_GRTC_START && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:980`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L980)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 使用 nRF GRTC 外设（Use nRF GRTC peripheral） → 启动 nRF GRTC 外设（Start nRF GRTC peripheral）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_NRF_GRTC_START`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_NRF_GRTC_START)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_NRF_GRTC_AUTOEN_DEFAULT"></a>

## 323.51 `CONFIG_BT_CTLR_NRF_GRTC_AUTOEN_DEFAULT`

**提示（Prompt）**：默认自动启用 nRF GRTC（Auto enable nRF GRTC by default）

**说明（Help）**

默认自动启用 nRF GRTC。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_NRF_GRTC_START && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:986`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L986)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 使用 nRF GRTC 外设（Use nRF GRTC peripheral） → 启动 nRF GRTC 外设（Start nRF GRTC peripheral）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_NRF_GRTC_START`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_NRF_GRTC_START)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_NRF_GRTC_KEEPRUNNING"></a>

## 323.52 `CONFIG_BT_CTLR_NRF_GRTC_KEEPRUNNING`

**提示（Prompt）**：保持 nRF GRTC 外设运行（Keep running nRF GRTC peripheral）

**说明（Help）**

保持 nRF GRTC 外设（peripheral）持续运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_NRF_GRTC_START && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:974`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L974)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 使用 nRF GRTC 外设（Use nRF GRTC peripheral） → 启动 nRF GRTC 外设（Start nRF GRTC peripheral）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_NRF_GRTC_START`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_NRF_GRTC_START)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_NRF_GRTC_START"></a>

## 323.53 `CONFIG_BT_CTLR_NRF_GRTC_START`

**提示（Prompt）**：启动 nRF GRTC 外设（Start nRF GRTC peripheral）

**说明（Help）**

允许显式启动（explicit start）nRF54Lx 的 `NRF_GRTC` 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_NRF_GRTC && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:968`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L968)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 使用 nRF GRTC 外设（Use nRF GRTC peripheral）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_NRF_GRTC`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_NRF_GRTC)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_OPTIMIZE_CHOICE"></a>

## 323.54 `CONFIG_BT_CTLR_OPTIMIZE_CHOICE`

原库同名定义共 2 条；本项为数据库第 1943 条记录，各定义分别保留。

**提示（Prompt）**：优化选项（Optimization options）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LTO && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CTLR_OPTIMIZE_FOR_SPEED
```

**可选项（Choices）**

```text
CONFIG_BT_CTLR_OPTIMIZE_FOR_APP_DEFAULT
CONFIG_BT_CTLR_OPTIMIZE_FOR_SIZE
CONFIG_BT_CTLR_OPTIMIZE_FOR_SPEED
CONFIG_BT_CTLR_OPTIMIZE_FOR_SPEED
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:699`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L699)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_LTO`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LTO)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_OPTIMIZE_FOR_SPEED`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_OPTIMIZE_FOR_SPEED)、[`CONFIG_BT_CTLR_OPTIMIZE_FOR_APP_DEFAULT`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_OPTIMIZE_FOR_APP_DEFAULT)、[`CONFIG_BT_CTLR_OPTIMIZE_FOR_SIZE`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_OPTIMIZE_FOR_SIZE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_OPTIMIZE_CHOICE--record-1944"></a>

## 323.55 `CONFIG_BT_CTLR_OPTIMIZE_CHOICE`

原库同名定义共 2 条；本项为数据库第 1944 条记录，各定义分别保留。

**提示（Prompt）**：优化选项（Optimization options）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LTO && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**可选项（Choices）**

```text
CONFIG_BT_CTLR_OPTIMIZE_FOR_APP_DEFAULT
CONFIG_BT_CTLR_OPTIMIZE_FOR_SIZE
CONFIG_BT_CTLR_OPTIMIZE_FOR_SPEED
CONFIG_BT_CTLR_OPTIMIZE_FOR_SPEED
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1449`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1449)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_LTO`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LTO)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_OPTIMIZE_FOR_APP_DEFAULT`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_OPTIMIZE_FOR_APP_DEFAULT)、[`CONFIG_BT_CTLR_OPTIMIZE_FOR_SIZE`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_OPTIMIZE_FOR_SIZE)、[`CONFIG_BT_CTLR_OPTIMIZE_FOR_SPEED`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_OPTIMIZE_FOR_SPEED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_OPTIMIZE_FOR_APP_DEFAULT"></a>

## 323.56 `CONFIG_BT_CTLR_OPTIMIZE_FOR_APP_DEFAULT`

**提示（Prompt）**：采用应用默认优化（Optimize for application defaults）

**说明（Help）**

按照应用默认设置（application defaults）优化控制器编译。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_OPTIMIZE_CHOICE>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:704`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L704)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 优化选项（Optimization options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_OPTIMIZE_CHOICE`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_OPTIMIZE_CHOICE)。

<a id="CONFIG_BT_CTLR_OPTIMIZE_FOR_SIZE"></a>

## 323.57 `CONFIG_BT_CTLR_OPTIMIZE_FOR_SIZE`

**提示（Prompt）**：优化空间占用（Optimize for space）

**说明（Help）**

以减小代码大小（code size）为目标优化控制器编译。这是 Zephyr 项目的默认优化方式，但编译控制器时会覆盖为速度优化（optimize for speed），以降低应用的中断服务例程（ISR）和线程延迟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_OPTIMIZE_CHOICE>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:709`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L709)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 优化选项（Optimization options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_OPTIMIZE_CHOICE`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_OPTIMIZE_CHOICE)。

<a id="CONFIG_BT_CTLR_OPTIMIZE_FOR_SPEED"></a>

## 323.58 `CONFIG_BT_CTLR_OPTIMIZE_FOR_SPEED`

原库同名定义共 2 条；本项为数据库第 1947 条记录，各定义分别保留。

**提示（Prompt）**：优化速度（Optimize for Speed）

**说明（Help）**

以提高执行速度（execution speed）为目标优化控制器编译。由于控制器的上层链路层（Upper Link Layer）和下层链路层（Lower Link Layer）均在 ISR 中执行，使用速度优化可降低应用的 ISR 和线程延迟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_OPTIMIZE_CHOICE>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:718`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L718)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 优化选项（Optimization options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_OPTIMIZE_CHOICE`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_OPTIMIZE_CHOICE)。

<a id="CONFIG_BT_CTLR_OPTIMIZE_FOR_SPEED--record-1948"></a>

## 323.59 `CONFIG_BT_CTLR_OPTIMIZE_FOR_SPEED`

原库同名定义共 2 条；本项为数据库第 1948 条记录，各定义分别保留。

**提示（Prompt）**：优化速度（Optimize for Speed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_OPTIMIZE_CHOICE>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1453`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1453)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 优化选项（Optimization options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_OPTIMIZE_CHOICE`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_OPTIMIZE_CHOICE)。

<a id="CONFIG_BT_CTLR_PARAM_CHECK"></a>

## 323.60 `CONFIG_BT_CTLR_PARAM_CHECK`

**提示（Prompt）**：HCI 命令参数检查（HCI Command Parameter checking）

**说明（Help）**

启用检查 HCI 命令参数（Command Parameters）的代码。主机与控制器合并构建（combined host plus controller builds）不需要此检查，省略它可节省部分代码空间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HCI_RAW
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1035`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1035)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_PERIPHERAL_ISO"></a>

## 323.61 `CONFIG_BT_CTLR_PERIPHERAL_ISO`

原库同名定义共 2 条；本项为数据库第 1950 条记录，各定义分别保留。

**提示（Prompt）**：低功耗蓝牙连接等时流外设（LE Connected Isochronous Stream Peripheral）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.2 低功耗蓝牙连接等时流外设角色（LE Connected Isochronous Stream Peripheral role）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT && CONFIG_BT_ISO_PERIPHERAL && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_ISO_PERIPHERAL
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1045`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1045)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT)、[`CONFIG_BT_ISO_PERIPHERAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_PERIPHERAL)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_PERIPHERAL_ISO--record-1951"></a>

## 323.62 `CONFIG_BT_CTLR_PERIPHERAL_ISO`

原库同名定义共 2 条；本项为数据库第 1951 条记录，各定义分别保留。

**提示（Prompt）**：低功耗蓝牙连接等时流外设，分离式链路层（Split Link Layer）[实验性，EXPERIMENTAL]

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT && CONFIG_BT_ISO_PERIPHERAL && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_ISO_PERIPHERAL
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_SET_HOST_FEATURE
CONFIG_EXPERIMENTAL if CONFIG_BT_LL_SW_SPLIT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1053`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1053)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT)、[`CONFIG_BT_ISO_PERIPHERAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_PERIPHERAL)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_SET_HOST_FEATURE`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_SET_HOST_FEATURE)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_PERIPHERAL_ISO_EARLY_CIG_START"></a>

## 323.63 `CONFIG_BT_CTLR_PERIPHERAL_ISO_EARLY_CIG_START`

**提示（Prompt）**：提前启动外设 CIG 事件（Early start of peripheral CIG event）

**说明（Help）**

提前一个事件开始调度外设等时连接组事件（Peripheral ISO CIG events），因此将 CIG 偏移（offset）与参考点（reference point）向前调整一个间隔。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_PERIPHERAL_ISO && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1391`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1391)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_PERIPHERAL_ISO`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_PERIPHERAL_ISO)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_PERIPHERAL_ISO_RESERVE_MAX"></a>

## 323.64 `CONFIG_BT_CTLR_PERIPHERAL_ISO_RESERVE_MAX`

**提示（Prompt）**：外设按最大数据 PDU 大小预留时间（maximum data PDU size time reservation for Peripheral）

**说明（Help）**

使用外设连接等时组（Peripheral CIG）事件的最大时间预留量。如果未启用这一最大时间预留，则仅预留发送或接收突发数量（burst number）个 CIS PDU 所需的时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_PERIPHERAL_ISO && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:850`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L850)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_PERIPHERAL_ISO`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_PERIPHERAL_ISO)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_PERIPHERAL_RESERVE_MAX"></a>

## 323.65 `CONFIG_BT_CTLR_PERIPHERAL_RESERVE_MAX`

**提示（Prompt）**：外设按最大数据 PDU 大小预留时间（maximum data PDU size time reservation for Peripheral）

**说明（Help）**

考虑到数据长度（Data length）可能从默认 `27` 字节更新为所支持的最大大小，按最大数据 PDU 大小预留时间。如果禁用最大时间预留，则采用发送空 PDU（empty PDU）所需的时间预留量。重叠的无线电事件（radio events）将使用 `is_abort_cb` 机制决定是否继续连接事件（connection event）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PERIPHERAL && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:837`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L837)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG"></a>

## 323.66 `CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG`

**提示（Prompt）**：外设发起的功能交换（Peripheral-initiated Features Exchange）

**说明（Help）**

在控制器（Controller）中启用蓝牙 v4.1 外设发起的功能交换（Peripheral-initiated Features Exchange）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG_SUPPORT && CONFIG_BT_CONN && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:587`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L587)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_PHY_2M"></a>

## 323.67 `CONFIG_BT_CTLR_PHY_2M`

**提示（Prompt）**：2Mbps 物理层支持（2Mbps PHY Support）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.0 的 2Mbps 物理层（PHY）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_PHY || CONFIG_BT_CTLR_ADV_EXT) && CONFIG_BT_CTLR_PHY_2M_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:715`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L715)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_PHY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_CTLR_PHY_2M_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_2M_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_PHY`、`CONFIG_BT_CTLR_PHY_2M_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_PHY_2M_NRF"></a>

## 323.68 `CONFIG_BT_CTLR_PHY_2M_NRF`

**提示（Prompt）**：Nordic Semiconductor 2Mbps 物理层支持，仅限明文（Cleartext only）

**说明（Help）**

在控制器中启用 Nordic Semiconductor 专有的 2Mbps 物理层（PHY）支持。不支持加密连接（encrypted connections）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF51 && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:393`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L393)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_PHY_CODED"></a>

## 323.69 `CONFIG_BT_CTLR_PHY_CODED`

**提示（Prompt）**：编码物理层支持（Coded PHY Support）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.0 编码物理层（Coded PHY）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_PHY || CONFIG_BT_CTLR_ADV_EXT) && CONFIG_BT_CTLR_PHY_CODED_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HCI_RAW
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:722`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L722)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_PHY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_CTLR_PHY_CODED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_CODED_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_PHY`、`CONFIG_BT_CTLR_PHY_CODED_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_PRIVACY"></a>

## 323.70 `CONFIG_BT_CTLR_PRIVACY`

**提示（Prompt）**：基于控制器的低功耗蓝牙隐私（LE Controller-based Privacy）

**说明（Help）**

在控制器（Controller）中启用蓝牙 v4.2 基于控制器的低功耗蓝牙隐私（LE Controller-based Privacy）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_PRIVACY_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HCI_RAW || CONFIG_BT_SMP
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_FILTER_ACCEPT_LIST if CONFIG_BT_LL_SW_SPLIT
CONFIG_BT_RPA
CONFIG_BT_SYSTEM_WORKQUEUE_COOP if CONFIG_BT_LL_SW_SPLIT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:674`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L674)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_PRIVACY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PRIVACY_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CTLR_FILTER_ACCEPT_LIST`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_FILTER_ACCEPT_LIST)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_RPA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_RPA)、[`CONFIG_BT_SYSTEM_WORKQUEUE_COOP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SYSTEM_WORKQUEUE_COOP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_PRIVACY_SUPPORT`、`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_RPA`。

<a id="CONFIG_BT_CTLR_PROFILE_ISR"></a>

## 323.71 `CONFIG_BT_CTLR_PROFILE_ISR`

**提示（Prompt）**：分析无线电 ISR 性能（Profile radio ISR）

**说明（Help）**

启用无线电 ISR 延迟和 CPU 使用量测量，并生成包含这些性能分析数据（profiling data）的控制器事件（controller event）。事件包含当前、最小和最大 ISR 入口延迟，以及当前、最小和最大 ISR CPU 使用时间，单位为微秒。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1462`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1462)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_RADIO_ENABLE_FAST"></a>

## 323.72 `CONFIG_BT_CTLR_RADIO_ENABLE_FAST`

**提示（Prompt）**：使用 tTXEN/RXEN,FAST 快速爬升（ramp-up）

**说明（Help）**

启用无线电快速爬升模式（fast radio ramp-up mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_COMPATIBLE_NRF52X || CONFIG_SOC_COMPATIBLE_NRF53X || CONFIG_SOC_COMPATIBLE_NRF54LX) && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:992`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L992)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF52X)、[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF52X`、`CONFIG_SOC_COMPATIBLE_NRF53X`、`CONFIG_SOC_COMPATIBLE_NRF54LX`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_RADIO_TIMER_ISR"></a>

## 323.73 `CONFIG_BT_CTLR_RADIO_TIMER_ISR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

允许使用定时器中断服务例程回调（timer ISR callback）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_COMPATIBLE_NRF52X || CONFIG_SOC_COMPATIBLE_NRF53X) && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1001`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1001)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF52X)、[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF52X`、`CONFIG_SOC_COMPATIBLE_NRF53X`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_READ_ISO_LINK_QUALITY"></a>

## 323.74 `CONFIG_BT_CTLR_READ_ISO_LINK_QUALITY`

**提示（Prompt）**：低功耗蓝牙读取 ISO 链路质量（LE Read ISO Link Quality）

**说明（Help）**

启用 `LE Read ISO Link Quality`（读取等时链路质量）命令支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_READ_ISO_LINK_QUALITY_SUPPORT && (CONFIG_BT_CTLR_SYNC_ISO || CONFIG_BT_CTLR_CONN_ISO) && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1125)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_READ_ISO_LINK_QUALITY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_READ_ISO_LINK_QUALITY_SUPPORT)、[`CONFIG_BT_CTLR_SYNC_ISO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_READ_ISO_LINK_QUALITY_SUPPORT`、`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_RL_SIZE"></a>

## 323.75 `CONFIG_BT_CTLR_RL_SIZE`

**提示（Prompt）**：基于控制器的低功耗蓝牙隐私解析列表大小（LE Controller-based Privacy Resolving List size）

**说明（Help）**

设置基于控制器的低功耗蓝牙隐私（LE Controller-based Privacy）所用解析列表（Resolving List）的大小。基于 nRF5x 的控制器受硬件限制，最多支持 `8` 个设备；基于 OpenISA 的控制器也受硬件限制，最多支持 `8` 个设备。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_PRIVACY && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 8] if CONFIG_SOC_COMPATIBLE_NRF
[1, 8] if CONFIG_SOC_OPENISA_RV32M1
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:696`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L696)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_PRIVACY`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_PRIVACY)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)、[`CONFIG_SOC_OPENISA_RV32M1`](P298_soc_openisa_配置项参考.md#CONFIG_SOC_OPENISA_RV32M1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_SOC_COMPATIBLE_NRF`。

<a id="CONFIG_BT_CTLR_RPA_CACHE_SIZE"></a>

## 323.76 `CONFIG_BT_CTLR_RPA_CACHE_SIZE`

**提示（Prompt）**：基于控制器的低功耗蓝牙软件隐私解析列表大小（Software Privacy Resolving List size）

**说明（Help）**

设置基于控制器、采用软件延后处理的低功耗蓝牙隐私（LE Controller-based Software deferred Privacy）所用“已知未知”解析列表（Known Unknown Resolving List）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SW_DEFERRED_PRIVACY && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:366`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L366)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 基于控制器的低功耗蓝牙软件隐私（LE Controller-based Software Privacy）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SW_DEFERRED_PRIVACY`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SW_DEFERRED_PRIVACY)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_RX_BUFFERS"></a>

## 323.77 `CONFIG_BT_CTLR_RX_BUFFERS`

**提示（Prompt）**：接收缓冲区数量（Number of Rx buffers）

**说明（Help）**

设置控制器中可缓存的接收 PDU（Rx PDUs）数量。在 `7.5ms` 连接间隔、2M PHY 条件下，最多可接收 `18` 个 L2CAP 有效载荷大小为 `1` 字节的数据包。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
6 if CONFIG_BT_HCI_RAW
1
```

**取值范围（Ranges）**

```text
[1, 18]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:240`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L240)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_RX_PDU_META"></a>

## 323.78 `CONFIG_BT_CTLR_RX_PDU_META`

**提示（Prompt）**：接收 PDU 元数据（RX PDU meta data）

**说明（Help）**

启用厂商专用接收 PDU 元数据（vendor specific Rx PDU meta data），将其作为接收对象（Rx object）的一部分。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:956`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L956)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_RX_PRIO_STACK_SIZE"></a>

## 323.79 `CONFIG_BT_CTLR_RX_PRIO_STACK_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

控制器的协作式高优先级接收线程（Co-Operative high priority Rx thread）栈大小。在主机与控制器合并构建中，如果已入队的 ACL 和 ISO 数据在普通接收线程中因等待空闲发送缓冲区而阻塞，则使用高优先级接收线程，优先向主机传递已完成数据包数量事件（Number of Completed Packets event）与断开事件（Disconnect Event）。在仅控制器构建中，该高优先级接收线程是多余的。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_BT_HCI_RAW && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
448
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SCAN_AUX_CHAIN_COUNT"></a>

## 323.80 `CONFIG_BT_CTLR_SCAN_AUX_CHAIN_COUNT`

**提示（Prompt）**：低功耗蓝牙扩展扫描辅助链（LE Extended Scanning Auxiliary Chains）

**说明（Help）**

可以同时跟随的扩展／周期性广播链（extended/periodic advertising chains）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_CTLR_ADV_EXT && CONFIG_BT_CTLR_SCAN_AUX_USE_CHAINS && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:559`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L559)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_CTLR_SCAN_AUX_USE_CHAINS`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_SCAN_AUX_USE_CHAINS)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SCAN_AUX_SET"></a>

## 323.81 `CONFIG_BT_CTLR_SCAN_AUX_SET`

**提示（Prompt）**：低功耗蓝牙扩展扫描辅助集合（LE Extended Scanning Auxiliary Sets）

**说明（Help）**

支持的辅助信道扫描集合（auxiliary channel scan sets）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_CTLR_ADV_EXT && !CONFIG_BT_CTLR_SCAN_AUX_USE_CHAINS && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:551`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L551)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_CTLR_SCAN_AUX_USE_CHAINS`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_SCAN_AUX_USE_CHAINS)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SCAN_AUX_SYNC_RESERVE_MIN"></a>

## 323.82 `CONFIG_BT_CTLR_SCAN_AUX_SYNC_RESERVE_MIN`

**提示（Prompt）**：为扫描辅助 PDU 和周期性同步 PDU 使用最小时间预留（minimal time reservation）

**说明（Help）**

为辅助 PDU（Auxiliary PDU）和周期性同步 PDU（Periodic Sync PDU）的接收使用最小时间预留量。对端设备可能在短时间内调度多个采用小 PDU 的广播集合，因此使用最小预留量可避免漏掉时间安排紧密的多个辅助或周期性同步 PDU 接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
((CONFIG_BT_OBSERVER && CONFIG_BT_CTLR_ADV_EXT) || CONFIG_BT_CTLR_SYNC_PERIODIC) && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:568`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L568)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_CTLR_SYNC_PERIODIC`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_PERIODIC)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SCAN_AUX_USE_CHAINS"></a>

## 323.83 `CONFIG_BT_CTLR_SCAN_AUX_USE_CHAINS`

**提示（Prompt）**：使用基于链的新实现跟随广播链（new chains based implementation）

**说明（Help）**

使用基于链（chains）的新实现来跟随广播链，代替旧的基于集合（sets）的实现。新实现的资源占用小得多，因为它将每条广播链的分配量限制在最低必要水平，并且只使用一个 ticker。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_CTLR_ADV_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:542`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L542)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SCAN_DATA_LEN_MAX"></a>

## 323.84 `CONFIG_BT_CTLR_SCAN_DATA_LEN_MAX`

**提示（Prompt）**：扩展扫描数据最大长度（Maximum Extended Scanning Data Length）

**说明（Help）**

扩展扫描数据（Extended Scanning Data）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_CTLR_ADV_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**取值范围（Ranges）**

```text
[31, 1650]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:245`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L245)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SCAN_ENABLE_STRICT"></a>

## 323.85 `CONFIG_BT_CTLR_SCAN_ENABLE_STRICT`

**提示（Prompt）**：严格执行扫描启用／禁用规则（Enforce Strict Scan Enable/Disable）

**说明（Help）**

在启用已启用的扫描或禁用已禁用的扫描时，强制返回 HCI 命令不允许错误（Command Disallowed）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:616`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L616)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SCAN_INDICATION"></a>

## 323.86 `CONFIG_BT_CTLR_SCAN_INDICATION`

**提示（Prompt）**：扫描器指示（Scanner indications）

**说明（Help）**

生成用于指示空中扫描器活动（on air scanner events）的事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1225`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1225)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SCAN_REQ_NOTIFY"></a>

## 323.87 `CONFIG_BT_CTLR_SCAN_REQ_NOTIFY`

**提示（Prompt）**：扫描请求通知（Scan Request Notifications）

**说明（Help）**

生成事件，通知已通过空中接口接收到的扫描请求（scan requests）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BROADCASTER && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_CTLR_ADV_EXT
CONFIG_BT_CTLR_VS_SCAN_REQ_RX
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1213`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1213)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_CTLR_VS_SCAN_REQ_RX`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_VS_SCAN_REQ_RX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SCAN_REQ_RSSI"></a>

## 323.88 `CONFIG_BT_CTLR_SCAN_REQ_RSSI`

**提示（Prompt）**：测量扫描请求 RSSI（Measure Scan Request RSSI）

**说明（Help）**

测量通过空中接口接收到的扫描请求的接收信号强度指示（RSSI）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SCAN_REQ_NOTIFY && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1219`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1219)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 扫描请求通知（Scan Request Notifications）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SCAN_REQ_NOTIFY`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_SCAN_REQ_NOTIFY)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SCAN_SYNC_ISO_SET"></a>

## 323.89 `CONFIG_BT_CTLR_SCAN_SYNC_ISO_SET`

**提示（Prompt）**：低功耗蓝牙广播等时组同步集合（LE ISO Broadcast Isochronous Groups Sync Sets）

**说明（Help）**

支持的广播等时组（broadcast isochronous groups，BIGs）同步集合（sync sets）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SYNC_ISO && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ISO_MAX_BIG
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:985`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L985)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_ISO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_MAX_BIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_MAX_BIG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SCAN_UNRESERVED"></a>

## 323.90 `CONFIG_BT_CTLR_SCAN_UNRESERVED`

**提示（Prompt）**：不预留的扫描窗口（Unreserved scan window）

**说明（Help）**

在连续扫描模式（continuous scan mode）下，扫描器不为扫描窗口（scan window）预留时间空间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && !CONFIG_BT_CTLR_LOW_LAT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_MESH
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1231`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1231)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_CTLR_LOW_LAT`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_LOW_LAT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SCA_UPDATE"></a>

## 323.91 `CONFIG_BT_CTLR_SCA_UPDATE`

**提示（Prompt）**：睡眠时钟精度更新过程（Sleep Clock Accuracy Update procedure）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.1 睡眠时钟精度更新过程（Sleep Clock Accuracy Update procedure）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SCA_UPDATE && CONFIG_BT_CTLR_SCA_UPDATE_SUPPORT && CONFIG_BT_CONN && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_CONN_ISO
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:635`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L635)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_SCA_UPDATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SCA_UPDATE)、[`CONFIG_BT_CTLR_SCA_UPDATE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SCA_UPDATE_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_SCA_UPDATE_SUPPORT`、`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_CONN_ISO`。

<a id="CONFIG_BT_CTLR_SCHED_ADVANCED"></a>

## 323.92 `CONFIG_BT_CTLR_SCHED_ADVANCED`

**提示（Prompt）**：高级调度（Advanced scheduling）

**说明（Help）**

允许观察者（observer）、发起者（initiator）和中心设备（central）角色在时间空间中以不重叠方式安排。使用连接更新中的窗口偏移（window offset），并在外设角色（peripheral role）中通过连接参数请求（connection parameter request），协商与活动中心设备角色互不重叠的安排，避免外设角色漂移到本地控制器中活动中心设备角色的时间区间。

当本地控制器中还存在其他活动的观察者、发起者、中心设备或外设角色时，此功能能最大限度提高同时活动的中心设备与外设连接之间的平均数据传输量。禁用此功能会导致角色在时间空间中重叠，从而使活动角色跳过某些事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SCHED_ADVANCED_SUPPORT && (CONFIG_BT_CONN || (CONFIG_BT_CTLR_ADV_EXT && CONFIG_BT_CTLR_ADV_AUX_SET > 0) || CONFIG_BT_CTLR_ADV_ISO) && CONFIG_BT_TICKER_NEXT_SLOT_GET && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CENTRAL || (CONFIG_BT_BROADCASTER && CONFIG_BT_CTLR_ADV_EXT) || CONFIG_BT_CTLR_ADV_ISO
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:759`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L759)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SCHED_ADVANCED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SCHED_ADVANCED_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_CTLR_ADV_AUX_SET`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_AUX_SET)、[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_TICKER_NEXT_SLOT_GET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_NEXT_SLOT_GET)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_SCHED_ADVANCED_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SETTINGS"></a>

## 323.93 `CONFIG_BT_CTLR_SETTINGS`

**提示（Prompt）**：设置系统（Settings System）

**说明（Help）**

允许控制器使用设置系统（settings system）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SET_HOST_FEATURE"></a>

## 323.94 `CONFIG_BT_CTLR_SET_HOST_FEATURE`

原库同名定义共 2 条；本项为数据库第 1984 条记录，各定义分别保留。

**提示（Prompt）**：LE Set Host Feature 命令（设置主机功能）

**说明（Help）**

启用可选的 `LE Set Host Feature`（设置主机功能）命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_CTLR_ADV_EXT_CODING_SELECTION
CONFIG_BT_CTLR_ADV_ISO
CONFIG_BT_CTLR_SYNC_ISO
CONFIG_BT_CTLR_CENTRAL_ISO
CONFIG_BT_CTLR_PERIPHERAL_ISO
CONFIG_BT_CTLR_SUBRATING
CONFIG_BT_CTLR_CHANNEL_SOUNDING
CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1021`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1021)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_ADV_EXT_CODING_SELECTION`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT_CODING_SELECTION)、[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_SYNC_ISO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_CTLR_CENTRAL_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CENTRAL_ISO)、[`CONFIG_BT_CTLR_PERIPHERAL_ISO`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_PERIPHERAL_ISO)、[`CONFIG_BT_CTLR_SUBRATING`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SUBRATING)、[`CONFIG_BT_CTLR_CHANNEL_SOUNDING`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CHANNEL_SOUNDING)、[`CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SET_HOST_FEATURE--record-1985"></a>

## 323.95 `CONFIG_BT_CTLR_SET_HOST_FEATURE`

原库同名定义共 2 条；本项为数据库第 1985 条记录，各定义分别保留。

**提示（Prompt）**：LE Set Host Feature 命令，分离式链路层（Split Link Layer）[实验性，EXPERIMENTAL]

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL if CONFIG_BT_LL_SW_SPLIT
```

**被选择（Selected by）**

```text
CONFIG_BT_CTLR_ADV_EXT_CODING_SELECTION
CONFIG_BT_CTLR_ADV_ISO
CONFIG_BT_CTLR_SYNC_ISO
CONFIG_BT_CTLR_CENTRAL_ISO
CONFIG_BT_CTLR_PERIPHERAL_ISO
CONFIG_BT_CTLR_SUBRATING
CONFIG_BT_CTLR_CHANNEL_SOUNDING
CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1026`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1026)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_ADV_EXT_CODING_SELECTION`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT_CODING_SELECTION)、[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_SYNC_ISO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_CTLR_CENTRAL_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CENTRAL_ISO)、[`CONFIG_BT_CTLR_PERIPHERAL_ISO`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_PERIPHERAL_ISO)、[`CONFIG_BT_CTLR_SUBRATING`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SUBRATING)、[`CONFIG_BT_CTLR_CHANNEL_SOUNDING`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CHANNEL_SOUNDING)、[`CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS"></a>

## 323.96 `CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS`

**提示（Prompt）**：更短的连接间隔（Shorter Connection Intervals）

**说明（Help）**

在控制器中启用蓝牙 6.2 更短连接间隔（Shorter Connection Intervals）支持。

译注：版本号按所译 Zephyr 官方快照保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS_SUPPORT && CONFIG_BT_CTLR_EXTENDED_FEAT_SET && CONFIG_BT_CTLR_SUBRATING && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_SHORTER_CONNECTION_INTERVALS
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_SET_HOST_FEATURE
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1191`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1191)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 链路层扩展功能集支持（LL Extended Feature Set support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS_SUPPORT)、[`CONFIG_BT_CTLR_EXTENDED_FEAT_SET`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_EXTENDED_FEAT_SET)、[`CONFIG_BT_CTLR_SUBRATING`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SUBRATING)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SHORTER_CONNECTION_INTERVALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SHORTER_CONNECTION_INTERVALS)、[`CONFIG_BT_CTLR_SET_HOST_FEATURE`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_SET_HOST_FEATURE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SLOT_RESERVATION_UPDATE"></a>

## 323.97 `CONFIG_BT_CTLR_SLOT_RESERVATION_UPDATE`

**提示（Prompt）**：PHY 或 DLE 更新后调整事件时长预留（Update event length reservation）

**说明（Help）**

数据长度更新（Data Length Update）和／或物理层更新（PHY Update）过程完成后，更新事件时长预留量（event length reservation），避免无线电事件（radio events）重叠。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_DATA_LENGTH || CONFIG_BT_CTLR_PHY) && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:872`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L872)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DATA_LENGTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DATA_LENGTH)、[`CONFIG_BT_CTLR_PHY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_DATA_LENGTH`、`CONFIG_BT_CTLR_PHY`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SMI_RX"></a>

## 323.98 `CONFIG_BT_CTLR_SMI_RX`

**提示（Prompt）**：稳定调制指数：接收器（Stable modulation index - Receiver）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.0 稳定调制指数接收（SMI RX）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SMI_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SMI_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SMI_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_SMI_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SMI_TX"></a>

## 323.99 `CONFIG_BT_CTLR_SMI_TX`

**提示（Prompt）**：稳定调制指数：发送器（Stable modulation index - Transmitter）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.0 稳定调制指数发送（SMI TX）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SMI_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1138)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SMI_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SMI_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_SMI_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SMI_TX_SETTING"></a>

## 323.100 `CONFIG_BT_CTLR_SMI_TX_SETTING`

**提示（Prompt）**：通过设置启用稳定调制指数发送器（Stable modulation index - Transmitter as setting）

**说明（Help）**

允许通过系统设置（system setting）启用蓝牙 5.0 稳定调制指数发送（SMI TX）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SMI_TX && CONFIG_BT_CTLR_SETTINGS && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1144)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 稳定调制指数：发送器（Stable modulation index - Transmitter）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SMI_TX`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_SMI_TX)、[`CONFIG_BT_CTLR_SETTINGS`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_SETTINGS)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<!-- kconfig-navigation -->

[上一章](P322_subsys_bluetooth_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P324_subsys_bluetooth_配置项参考_5.md)
