---
id: learning.zephyr-docs.kconfig-reference.page-324
title: "`subsys/bluetooth`配置项参考（5/13）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第324章\_`subsys/bluetooth`配置项参考（5/13）

本章翻译官方 Kconfig 数据库中 `subsys/bluetooth` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_CTLR_SUBRATING"></a>

## 324.1 `CONFIG_BT_CTLR_SUBRATING`

**提示（Prompt）**：低功耗蓝牙连接子速率（LE Connection Subrating）

**说明（Help）**

在控制器（Controller）中启用蓝牙 v5.3 低功耗蓝牙连接子速率（LE Connection Subrating）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SUBRATING_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_SUBRATING
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_SET_HOST_FEATURE
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1157)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SUBRATING_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SUBRATING_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SUBRATING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SUBRATING)、[`CONFIG_BT_CTLR_SET_HOST_FEATURE`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_SET_HOST_FEATURE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_SUBRATING_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SUBVERSION_NUMBER"></a>

## 324.2 `CONFIG_BT_CTLR_SUBVERSION_NUMBER`

**提示（Prompt）**：子版本号（Subversion Number）

**说明（Help）**

设置将在 `VERSION_IND` PDU 中使用的子版本号（Subversion Number）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0xFFFF
```

**取值范围（Ranges）**

```text
[0x0000, 0xFFFF]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L182)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SW_DEFERRED_PRIVACY"></a>

## 324.3 `CONFIG_BT_CTLR_SW_DEFERRED_PRIVACY`

**提示（Prompt）**：基于控制器的低功耗蓝牙软件隐私（LE Controller-based Software Privacy）

**说明（Help）**

启用基于软件的延后隐私计算（software based deferred privacy calculations）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_PRIVACY && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:360`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L360)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_PRIVACY`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_PRIVACY)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SW_SWITCH_SINGLE_TIMER"></a>

## 324.4 `CONFIG_BT_CTLR_SW_SWITCH_SINGLE_TIMER`

**提示（Prompt）**：使用单个 TIMER 的 tIFS 收发软件切换（Single TIMER tIFS Trx SW switching）

**说明（Help）**

使用蓝牙事件计时所用的同一个 TIMER 实例，实现 tIFS 收发软件切换（Trx SW switch）。要求已启用软件切换（SW switching）。

使用单个 TIMER 的影响：

- 优点：释放一个 TIMER 实例。
- 优点：消除硬件关闭超时（HCTO）实现的抖动（jitter）。
- 缺点：在蓝牙事件内部引入绝对时间漂移（absolute time drift），漂移量随该事件中交换的数据包数量线性增加。
- 缺点：控制器无法使用大多数预编程的可编程外设互连（PPI）信道，导致可供其他用途使用的信道减少 `4` 个。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_RADIO_ENABLE_FAST && (CONFIG_SOC_COMPATIBLE_NRF52X || CONFIG_SOC_COMPATIBLE_NRF53X || CONFIG_SOC_COMPATIBLE_NRF54LX) && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_COMPATIBLE_NRF54LX
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1015`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1015)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_RADIO_ENABLE_FAST`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_RADIO_ENABLE_FAST)、[`CONFIG_SOC_COMPATIBLE_NRF52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF52X)、[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF52X`、`CONFIG_SOC_COMPATIBLE_NRF53X`、`CONFIG_SOC_COMPATIBLE_NRF54LX`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_ISO"></a>

## 324.5 `CONFIG_BT_CTLR_SYNC_ISO`

原库同名定义共 2 条；本项为数据库第 1995 条记录，各定义分别保留。

**提示（Prompt）**：低功耗蓝牙广播等时信道广播同步（LE Broadcast Isochronous Channel advertising sync）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.2 低功耗蓝牙等时广播同步（LE Isochronous Advertising sync）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ISO_SYNC_RECEIVER && CONFIG_BT_CTLR_SYNC_ISO_SUPPORT && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_ISO_SYNC_RECEIVER
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_SYNC_PERIODIC
CONFIG_BT_CTLR_SET_HOST_FEATURE
CONFIG_BT_CTLR_SYNC_ISO_SEQUENTIAL if !CONFIG_BT_CTLR_SYNC_ISO_INTERLEAVED
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:918`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L918)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO_SYNC_RECEIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_SYNC_RECEIVER)、[`CONFIG_BT_CTLR_SYNC_ISO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_ISO_SUPPORT)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_SYNC_PERIODIC`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_PERIODIC)、[`CONFIG_BT_CTLR_SET_HOST_FEATURE`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_SET_HOST_FEATURE)、[`CONFIG_BT_CTLR_SYNC_ISO_SEQUENTIAL`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO_SEQUENTIAL)、[`CONFIG_BT_CTLR_SYNC_ISO_INTERLEAVED`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO_INTERLEAVED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_SYNC_ISO_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_ISO--record-1996"></a>

## 324.6 `CONFIG_BT_CTLR_SYNC_ISO`

原库同名定义共 2 条；本项为数据库第 1996 条记录，各定义分别保留。

**提示（Prompt）**：低功耗蓝牙广播等时信道广播同步，分离式链路层（Split Link Layer）[实验性，EXPERIMENTAL]

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL if CONFIG_BT_LL_SW_SPLIT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:929`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L929)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_ISO_INTERLEAVED"></a>

## 324.7 `CONFIG_BT_CTLR_SYNC_ISO_INTERLEAVED`

**提示（Prompt）**：低功耗蓝牙广播等时信道广播同步的交错打包（interleaved packing）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SYNC_ISO && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:938`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L938)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions） → 低功耗蓝牙广播等时信道广播同步，分离式链路层（Split Link Layer）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_ISO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_ISO_PDU_LEN_MAX"></a>

## 324.8 `CONFIG_BT_CTLR_SYNC_ISO_PDU_LEN_MAX`

**提示（Prompt）**：同步等时信道 PDU 最大长度（Maximum Synchronized Isochronous Channel PDU Length）

**说明（Help）**

同步接收器等时信道（Synchronized Receiver Isochronous Channel）协议数据单元（PDU）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SYNC_ISO && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
251
```

**取值范围（Ranges）**

```text
[251, 251] if CONFIG_BT_HCI_RAW
[1, 251]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1010`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1010)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_ISO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_ISO_RESERVE_MAX"></a>

## 324.9 `CONFIG_BT_CTLR_SYNC_ISO_RESERVE_MAX`

**提示（Prompt）**：使用最大的 ISO 同步接收器事件时间预留量（maximum ISO Synchronized Receiver event time reservation）

**说明（Help）**

使用最大的等时同步接收器（ISO Synchronized Receiver）事件时间预留量。禁用时，预留时间不包含预发送（pre-transmissions），也不包含任何控制子事件（Control subevents）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SYNC_ISO && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:600`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L600)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_ISO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_ISO_SEQUENTIAL"></a>

## 324.10 `CONFIG_BT_CTLR_SYNC_ISO_SEQUENTIAL`

**提示（Prompt）**：低功耗蓝牙广播等时信道广播同步的顺序打包（sequential packing）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SYNC_ISO && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_BT_CTLR_SYNC_ISO
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:933`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L933)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions） → 低功耗蓝牙广播等时信道广播同步，分离式链路层（Split Link Layer）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_ISO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_ISO_STREAM_COUNT"></a>

## 324.11 `CONFIG_BT_CTLR_SYNC_ISO_STREAM_COUNT`

**提示（Prompt）**：最大 ISO 同步接收流数量（Maximum ISO Synchronized Receiver Streams）

**说明（Help）**

控制器在所有广播等时组（Broadcast ISO groups）范围内支持的等时同步接收流（ISO Synchronized Receiver Streams）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SYNC_ISO && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ISO_MAX_CHAN
```

**取值范围（Ranges）**

```text
[CONFIG_BT_CTLR_SYNC_ISO_STREAM_MAX, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1001`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1001)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_ISO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_MAX_CHAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_MAX_CHAN)、[`CONFIG_BT_CTLR_SYNC_ISO_STREAM_MAX`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO_STREAM_MAX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_ISO_STREAM_MAX"></a>

## 324.12 `CONFIG_BT_CTLR_SYNC_ISO_STREAM_MAX`

**提示（Prompt）**：每个广播 ISO 组支持的最大 ISO 同步接收流数量（ISO Synchronized Receiver Streams per Broadcast ISO group）

**说明（Help）**

每个广播等时组（Broadcast ISO group）支持的等时同步接收流（ISO Synchronized Receiver Streams）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SYNC_ISO && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**取值范围（Ranges）**

```text
[1, 31]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:993`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L993)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_ISO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_PERIODIC"></a>

## 324.13 `CONFIG_BT_CTLR_SYNC_PERIODIC`

**提示（Prompt）**：同步状态下的低功耗蓝牙周期性广播（LE Periodic Advertising in Synchronization State）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.0 同步状态（Synchronization state）下的低功耗蓝牙周期性广播（LE Periodic Advertising）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_PER_ADV_SYNC
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_CHAN_SEL_2
```

**被选择（Selected by）**

```text
CONFIG_BT_CTLR_SYNC_ISO
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:825`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L825)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_PER_ADV_SYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC)、[`CONFIG_BT_CTLR_CHAN_SEL_2`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CHAN_SEL_2)、[`CONFIG_BT_CTLR_SYNC_ISO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_ISO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_PERIODIC_ADI_SUPPORT"></a>

## 324.14 `CONFIG_BT_CTLR_SYNC_PERIODIC_ADI_SUPPORT`

**提示（Prompt）**：带 ADI 支持的周期性广播同步，即重复过滤（Periodic Advertising Sync with ADI support）

**说明（Help）**

允许使用周期性广播 PDU（Periodic Advertising PDUs）中的 `AdvDataInfo` 执行重复过滤（duplicate filtering）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SYNC_PERIODIC && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:860`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L860)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_PERIODIC`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_PERIODIC)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_PERIODIC_ADV_LIST"></a>

## 324.15 `CONFIG_BT_CTLR_SYNC_PERIODIC_ADV_LIST`

**提示（Prompt）**：低功耗蓝牙周期性广播者列表支持（LE Periodic Advertiser List support）

**说明（Help）**

启用低功耗蓝牙周期性广播者列表（LE Periodic Advertiser List）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SYNC_PERIODIC && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:845`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L845)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_PERIODIC`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_PERIODIC)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_PERIODIC_ADV_LIST_SIZE"></a>

## 324.16 `CONFIG_BT_CTLR_SYNC_PERIODIC_ADV_LIST_SIZE`

**提示（Prompt）**：低功耗蓝牙周期性广播者列表大小（LE Periodic Advertiser List size）

**说明（Help）**

设置周期性广播者列表（Periodic Advertiser List）的大小；HCI `LE Read Periodic Advertiser List` 命令会返回此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SYNC_PERIODIC_ADV_LIST && CONFIG_BT_CTLR_SYNC_PERIODIC && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:851`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L851)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions） → 低功耗蓝牙周期性广播者列表支持（LE Periodic Advertiser List support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_PERIODIC_ADV_LIST`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_PERIODIC_ADV_LIST)、[`CONFIG_BT_CTLR_SYNC_PERIODIC`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_PERIODIC)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_PERIODIC_CTE_TYPE_FILTERING"></a>

## 324.17 `CONFIG_BT_CTLR_SYNC_PERIODIC_CTE_TYPE_FILTERING`

**提示（Prompt）**：按 CTE 类型过滤低功耗蓝牙周期性广播者（LE Periodic Advertiser filtering by CTE type）

**说明（Help）**

允许依据恒定音调扩展（Constant Tone Extension，CTE）类型过滤周期性广播（periodic advertisements）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SYNC_PERIODIC && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:867`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L867)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_PERIODIC`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_PERIODIC)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_PERIODIC_RSP"></a>

## 324.18 `CONFIG_BT_CTLR_SYNC_PERIODIC_RSP`

**提示（Prompt）**：同步状态下的低功耗蓝牙带响应周期性广播（LE Periodic Advertising with Responses in Synchronization State）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.4 同步状态（Synchronization state）下的低功耗蓝牙带响应周期性广播（LE Periodic Advertising with Responses）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_CTLR_SYNC_PERIODIC_RSP_SUPPORT && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_PER_ADV_SYNC_RSP
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_CHAN_SEL_2
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:834`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L834)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_CTLR_SYNC_PERIODIC_RSP_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_PERIODIC_RSP_SUPPORT)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_PER_ADV_SYNC_RSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC_RSP)、[`CONFIG_BT_CTLR_CHAN_SEL_2`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CHAN_SEL_2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_SYNC_PERIODIC_RSP_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_PERIODIC_SKIP_ON_SCAN_AUX"></a>

## 324.19 `CONFIG_BT_CTLR_SYNC_PERIODIC_SKIP_ON_SCAN_AUX`

**提示（Prompt）**：与扩展扫描事件重叠时跳过周期性同步事件（Skip Periodic Sync event on overlap with Extended Scan Event）

**说明（Help）**

当 `AUX_ADV_IND` 或 `AUX_CHAIN_IND` 辅助信道 PDU 的扫描无线电事件，在未预留的时间空间中与周期性同步无线电事件（Periodic Sync radio event）重叠时，允许中止周期性同步事件，以接收该辅助信道 PDU 并生成扩展广播报告（Extended Advertising Reports）。

默认情况下，为避免漏掉周期性广播报告的生成，希望周期性广播同步事件（Periodic Advertising Sync Events）优先于所有与其重叠的扩展广播主信道或辅助信道 PDU 接收。

但是，同时支持多个周期性广播同步且广播间隔较小时，会出现大量周期性同步事件重叠。此时，允许通过轮转调度（round robin scheduling）接收扩展广播辅助 PDU，并跳过重叠的周期性同步事件，会更合适；这样才能发现新的周期性广播对端设备（peers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SYNC_PERIODIC && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:579`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L579)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_PERIODIC`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_PERIODIC)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER"></a>

## 324.20 `CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER`

**提示（Prompt）**：周期性广播同步传输接收方（Periodic Advertising Sync Transfer receiver）

**说明（Help）**

作为 `LL_PERIODIC_SYNC_IND` 的接收方，启用周期性广播同步传输控制过程（Periodic Advertising Sync Transfer control procedure）支持。参见 Core_v5.3, Vol 6, Part B, Section 5.1.13。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT && CONFIG_BT_CTLR_SYNC_PERIODIC && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:874`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L874)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT)、[`CONFIG_BT_CTLR_SYNC_PERIODIC`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_PERIODIC)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER"></a>

## 324.21 `CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER`

**提示（Prompt）**：周期性广播同步传输发送方（Periodic Advertising Sync Transfer sender）

**说明（Help）**

作为 `LL_PERIODIC_SYNC_IND` 的发送方，启用周期性广播同步传输控制过程（Periodic Advertising Sync Transfer control procedure）支持。参见 Core_v5.3, Vol 6, Part B, Section 5.1.13。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER
```

**主动选择（Selects）**

```text
CONFIG_BT_TICKER_LAZY_GET if CONFIG_BT_LL_SW_SPLIT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:885`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L885)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER)、[`CONFIG_BT_TICKER_LAZY_GET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_LAZY_GET)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_TEST"></a>

## 324.22 `CONFIG_BT_CTLR_TEST`

**提示（Prompt）**：运行系统内单元测试（Run in-system unit tests）

**说明（Help）**

运行系统内单元测试（Run in-system unit tests）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:347`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L347)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_THROUGHPUT"></a>

## 324.23 `CONFIG_BT_CTLR_THROUGHPUT`

**提示（Prompt）**：测量传入待发送数据的吞吐量（Measure incoming Tx throughput）

**说明（Help）**

测量传入待发送数据的吞吐量（incoming Tx throughput），并记录结果。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HCI_RAW
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_TIFS_HW"></a>

## 324.24 `CONFIG_BT_CTLR_TIFS_HW`

**提示（Prompt）**：硬件加速的 tIFS 收发切换（H/w Accelerated tIFS Trx switching）

**说明（Help）**

允许使用硬件加速的 tIFS 收发切换（hardware accelerated tIFS Trx switching）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_TIFS_HW_SUPPORT && !CONFIG_BT_CTLR_RADIO_ENABLE_FAST && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1008`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1008)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_TIFS_HW_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_TIFS_HW_SUPPORT)、[`CONFIG_BT_CTLR_RADIO_ENABLE_FAST`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_RADIO_ENABLE_FAST)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_TIFS_HW_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_TRPA_CACHE_SIZE"></a>

## 324.25 `CONFIG_BT_CTLR_TRPA_CACHE_SIZE`

**提示（Prompt）**：基于控制器的低功耗蓝牙软件隐私目标 RPA 缓存大小（target RPA cache size）

**说明（Help）**

设置基于控制器、采用软件延后处理的低功耗蓝牙隐私（LE Controller-based Software deferred Privacy）所用“已知未知目标 RPA”解析列表（Known Unknown Target RPA Resolving List）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SW_DEFERRED_PRIVACY && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:375`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L375)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 基于控制器的低功耗蓝牙软件隐私（LE Controller-based Software Privacy）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SW_DEFERRED_PRIVACY`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SW_DEFERRED_PRIVACY)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_TX_DEFER"></a>

## 324.26 `CONFIG_BT_CTLR_TX_DEFER`

**提示（Prompt）**：延后设置 ACL 发送数据包传输（Deferred ACL Tx packet transmission setup）

**说明（Help）**

允许无线电延后设置 ACL 发送数据包传输（ACL Tx packet transmission），使上层入队的 ACL 数据包能够以尽可能短的延迟发出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_RADIO_TIMER_ISR && CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1124)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_RADIO_TIMER_ISR`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_RADIO_TIMER_ISR)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_TX_PWR"></a>

## 324.27 `CONFIG_BT_CTLR_TX_PWR`

**提示（Prompt）**：发射功率（Tx Power）

**说明（Help）**

选择受支持的低功耗蓝牙无线电发射功率级别（Bluetooth LE Radio transmit power level），单位为 dBm。仅可选择 SoC 原生支持的值。此处设置的值表示实际馈入天线的默认功率级别。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_TX_PWR_ANTENNA = 0 || CONFIG_BT_LL_SW_SPLIT) && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CTLR_TX_PWR_0
```

**可选项（Choices）**

```text
CONFIG_BT_CTLR_TX_PWR_PLUS_21
CONFIG_BT_CTLR_TX_PWR_PLUS_18
CONFIG_BT_CTLR_TX_PWR_PLUS_15
CONFIG_BT_CTLR_TX_PWR_PLUS_12
CONFIG_BT_CTLR_TX_PWR_PLUS_10
CONFIG_BT_CTLR_TX_PWR_PLUS_9
CONFIG_BT_CTLR_TX_PWR_PLUS_8
CONFIG_BT_CTLR_TX_PWR_PLUS_7
CONFIG_BT_CTLR_TX_PWR_PLUS_6
CONFIG_BT_CTLR_TX_PWR_PLUS_5
CONFIG_BT_CTLR_TX_PWR_PLUS_4
CONFIG_BT_CTLR_TX_PWR_PLUS_3
CONFIG_BT_CTLR_TX_PWR_PLUS_2
CONFIG_BT_CTLR_TX_PWR_PLUS_1
CONFIG_BT_CTLR_TX_PWR_0
CONFIG_BT_CTLR_TX_PWR_MINUS_1
CONFIG_BT_CTLR_TX_PWR_MINUS_2
CONFIG_BT_CTLR_TX_PWR_MINUS_3
CONFIG_BT_CTLR_TX_PWR_MINUS_4
CONFIG_BT_CTLR_TX_PWR_MINUS_5
CONFIG_BT_CTLR_TX_PWR_MINUS_6
CONFIG_BT_CTLR_TX_PWR_MINUS_7
CONFIG_BT_CTLR_TX_PWR_MINUS_8
CONFIG_BT_CTLR_TX_PWR_MINUS_9
CONFIG_BT_CTLR_TX_PWR_MINUS_10
CONFIG_BT_CTLR_TX_PWR_MINUS_12
CONFIG_BT_CTLR_TX_PWR_MINUS_14
CONFIG_BT_CTLR_TX_PWR_MINUS_15
CONFIG_BT_CTLR_TX_PWR_MINUS_16
CONFIG_BT_CTLR_TX_PWR_MINUS_18
CONFIG_BT_CTLR_TX_PWR_MINUS_20
CONFIG_BT_CTLR_TX_PWR_MINUS_21
CONFIG_BT_CTLR_TX_PWR_MINUS_24
CONFIG_BT_CTLR_TX_PWR_MINUS_26
CONFIG_BT_CTLR_TX_PWR_MINUS_30
CONFIG_BT_CTLR_TX_PWR_MINUS_40
CONFIG_BT_CTLR_TX_PWR_MINUS_46
CONFIG_BT_CTLR_TX_PWR_MINUS_70
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:328`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L328)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_TX_PWR_ANTENNA`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_ANTENNA)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_TX_PWR_0`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_0)、[`CONFIG_BT_CTLR_TX_PWR_PLUS_21`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_PLUS_21)、[`CONFIG_BT_CTLR_TX_PWR_PLUS_18`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_PLUS_18)、[`CONFIG_BT_CTLR_TX_PWR_PLUS_15`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_PLUS_15)、[`CONFIG_BT_CTLR_TX_PWR_PLUS_12`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_PLUS_12)、[`CONFIG_BT_CTLR_TX_PWR_PLUS_10`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_PLUS_10)、[`CONFIG_BT_CTLR_TX_PWR_PLUS_9`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_PLUS_9)、[`CONFIG_BT_CTLR_TX_PWR_PLUS_8`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_PLUS_8)、[`CONFIG_BT_CTLR_TX_PWR_PLUS_7`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_PLUS_7)、[`CONFIG_BT_CTLR_TX_PWR_PLUS_6`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_PLUS_6)、[`CONFIG_BT_CTLR_TX_PWR_PLUS_5`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_PLUS_5)、[`CONFIG_BT_CTLR_TX_PWR_PLUS_4`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_PLUS_4)、[`CONFIG_BT_CTLR_TX_PWR_PLUS_3`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_PLUS_3)、[`CONFIG_BT_CTLR_TX_PWR_PLUS_2`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_PLUS_2)、[`CONFIG_BT_CTLR_TX_PWR_PLUS_1`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_PLUS_1)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_1`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_1)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_2`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_2)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_3`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_3)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_4`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_4)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_5`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_5)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_6`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_6)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_7`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_7)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_8`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_8)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_9`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_9)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_10`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_10)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_12`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_12)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_14`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_14)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_15`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_15)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_16`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_16)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_18`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_18)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_20`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_20)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_21`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_21)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_24`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_24)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_26`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_26)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_30`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_30)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_40`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_40)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_46`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_46)、[`CONFIG_BT_CTLR_TX_PWR_MINUS_70`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR_MINUS_70)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_TX_PWR_0"></a>

## 324.28 `CONFIG_BT_CTLR_TX_PWR_0`

**提示（Prompt）**：0 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:394`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L394)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

<a id="CONFIG_BT_CTLR_TX_PWR_ANTENNA"></a>

## 324.29 `CONFIG_BT_CTLR_TX_PWR_ANTENNA`

**提示（Prompt）**：设置发射功率，单位为 dBm（Set TX power）

**说明（Help）**

请求一个以 dBm 表示的发射功率（TX power）。根据所用硬件支持的值，实际设置的功率级别会等于或小于请求值。对于超出支持范围的值，会设为最接近的受支持值。此处设置的值表示实际馈入天线的功率级别。使用前端模块（Front-End Module，FEM）时，会自动计算 SoC 和 FEM 的增益值，以使射频输出（RF output）尽可能接近用户请求的值。

译注：原文同时给出“不大于请求值”与“超出范围取最近值”两条规则，此处均保留；低于硬件最小值时应结合后者理解。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[-127, 127]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:527`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L527)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_TX_PWR_DYNAMIC_CONTROL"></a>

## 324.30 `CONFIG_BT_CTLR_TX_PWR_DYNAMIC_CONTROL`

**提示（Prompt）**：发射功率动态控制（Tx Power Dynamic Control）

**说明（Help）**

启用按角色／连接动态控制发射功率（Tx power）的功能。提供 HCI 厂商专用命令（VS commands），可按单个角色／连接设置和获取当前发射功率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_VS && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:542`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L542)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_VS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_VS)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_1"></a>

## 324.31 `CONFIG_BT_CTLR_TX_PWR_MINUS_1`

**提示（Prompt）**：-1 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_COMPATIBLE_NRF53X || CONFIG_SOC_SERIES_NRF54H || CONFIG_SOC_COMPATIBLE_NRF54LX) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:397`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L397)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)、[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF53X`、`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_10"></a>

## 324.32 `CONFIG_BT_CTLR_TX_PWR_MINUS_10`

**提示（Prompt）**：-10 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_COMPATIBLE_NRF54LX && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:431`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L431)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_12"></a>

## 324.33 `CONFIG_BT_CTLR_TX_PWR_MINUS_12`

**提示（Prompt）**：-12 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:435`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L435)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_14"></a>

## 324.34 `CONFIG_BT_CTLR_TX_PWR_MINUS_14`

**提示（Prompt）**：-14 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_COMPATIBLE_NRF54LX && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:438`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L438)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_15"></a>

## 324.35 `CONFIG_BT_CTLR_TX_PWR_MINUS_15`

**提示（Prompt）**：-15 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:442`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L442)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_16"></a>

## 324.36 `CONFIG_BT_CTLR_TX_PWR_MINUS_16`

**提示（Prompt）**：-16 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:446`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L446)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_18"></a>

## 324.37 `CONFIG_BT_CTLR_TX_PWR_MINUS_18`

**提示（Prompt）**：-18 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:449`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L449)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_2"></a>

## 324.38 `CONFIG_BT_CTLR_TX_PWR_MINUS_2`

**提示（Prompt）**：-2 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_COMPATIBLE_NRF53X || CONFIG_SOC_SERIES_NRF54H || CONFIG_SOC_COMPATIBLE_NRF54LX) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:401`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L401)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)、[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF53X`、`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_20"></a>

## 324.39 `CONFIG_BT_CTLR_TX_PWR_MINUS_20`

**提示（Prompt）**：-20 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:453`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L453)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_21"></a>

## 324.40 `CONFIG_BT_CTLR_TX_PWR_MINUS_21`

**提示（Prompt）**：-21 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:456`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L456)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_24"></a>

## 324.41 `CONFIG_BT_CTLR_TX_PWR_MINUS_24`

**提示（Prompt）**：-24 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:460`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L460)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_26"></a>

## 324.42 `CONFIG_BT_CTLR_TX_PWR_MINUS_26`

**提示（Prompt）**：-26 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_COMPATIBLE_NRF54LX && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:464`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L464)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_3"></a>

## 324.43 `CONFIG_BT_CTLR_TX_PWR_MINUS_3`

**提示（Prompt）**：-3 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_COMPATIBLE_NRF53X || CONFIG_SOC_COMPATIBLE_NRF54LX || CONFIG_SOC_FAMILY_ESPRESSIF_ESP32) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:405`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L405)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF53X`、`CONFIG_SOC_COMPATIBLE_NRF54LX`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_30"></a>

## 324.44 `CONFIG_BT_CTLR_TX_PWR_MINUS_30`

**提示（Prompt）**：-30 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_NRF51 || CONFIG_SOC_SERIES_NRF54H) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:468`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L468)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_4"></a>

## 324.45 `CONFIG_BT_CTLR_TX_PWR_MINUS_4`

**提示（Prompt）**：-4 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:409`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L409)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_40"></a>

## 324.46 `CONFIG_BT_CTLR_TX_PWR_MINUS_40`

**提示（Prompt）**：-40 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_COMPATIBLE_NRF52X || CONFIG_SOC_COMPATIBLE_NRF53X || CONFIG_SOC_SERIES_NRF54H || CONFIG_SOC_COMPATIBLE_NRF54LX) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:472`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L472)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF52X)、[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)、[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF52X`、`CONFIG_SOC_COMPATIBLE_NRF53X`、`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_46"></a>

## 324.47 `CONFIG_BT_CTLR_TX_PWR_MINUS_46`

**提示（Prompt）**：-46 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_COMPATIBLE_NRF54LX && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:476`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L476)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_5"></a>

## 324.48 `CONFIG_BT_CTLR_TX_PWR_MINUS_5`

**提示（Prompt）**：-5 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_COMPATIBLE_NRF53X || CONFIG_SOC_COMPATIBLE_NRF54LX) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:412`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L412)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF53X`、`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_6"></a>

## 324.49 `CONFIG_BT_CTLR_TX_PWR_MINUS_6`

**提示（Prompt）**：-6 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_COMPATIBLE_NRF53X || CONFIG_SOC_COMPATIBLE_NRF54LX || CONFIG_SOC_FAMILY_ESPRESSIF_ESP32) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:416`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L416)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF53X`、`CONFIG_SOC_COMPATIBLE_NRF54LX`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_7"></a>

## 324.50 `CONFIG_BT_CTLR_TX_PWR_MINUS_7`

**提示（Prompt）**：-7 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_COMPATIBLE_NRF53X || CONFIG_SOC_COMPATIBLE_NRF54LX) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:420`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L420)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF53X`、`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_70"></a>

## 324.51 `CONFIG_BT_CTLR_TX_PWR_MINUS_70`

**提示（Prompt）**：-70 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF54H && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:480`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L480)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_8"></a>

## 324.52 `CONFIG_BT_CTLR_TX_PWR_MINUS_8`

**提示（Prompt）**：-8 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:424`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L424)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

<a id="CONFIG_BT_CTLR_TX_PWR_MINUS_9"></a>

## 324.53 `CONFIG_BT_CTLR_TX_PWR_MINUS_9`

**提示（Prompt）**：-9 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_COMPATIBLE_NRF54LX || CONFIG_SOC_FAMILY_ESPRESSIF_ESP32) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:427`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L427)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF54LX`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BT_CTLR_TX_PWR_PLUS_1"></a>

## 324.54 `CONFIG_BT_CTLR_TX_PWR_PLUS_1`

**提示（Prompt）**：+1 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_COMPATIBLE_NRF53X || CONFIG_SOC_SERIES_NRF54H || CONFIG_SOC_COMPATIBLE_NRF54LX) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:390`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L390)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)、[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF53X`、`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_TX_PWR_PLUS_10"></a>

## 324.55 `CONFIG_BT_CTLR_TX_PWR_PLUS_10`

**提示（Prompt）**：+10 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF54H && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:354`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L354)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

<a id="CONFIG_BT_CTLR_TX_PWR_PLUS_12"></a>

## 324.56 `CONFIG_BT_CTLR_TX_PWR_PLUS_12`

**提示（Prompt）**：+12 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:350`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L350)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BT_CTLR_TX_PWR_PLUS_15"></a>

## 324.57 `CONFIG_BT_CTLR_TX_PWR_PLUS_15`

**提示（Prompt）**：+15 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:346`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L346)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BT_CTLR_TX_PWR_PLUS_18"></a>

## 324.58 `CONFIG_BT_CTLR_TX_PWR_PLUS_18`

**提示（Prompt）**：+18 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:342`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L342)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BT_CTLR_TX_PWR_PLUS_2"></a>

## 324.59 `CONFIG_BT_CTLR_TX_PWR_PLUS_2`

**提示（Prompt）**：+2 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH || CONFIG_SOC_COMPATIBLE_NRF53X || CONFIG_SOC_SERIES_NRF54H || CONFIG_SOC_COMPATIBLE_NRF54LX) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:386`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L386)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH)、[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)、[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH`、`CONFIG_SOC_COMPATIBLE_NRF53X`、`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_TX_PWR_PLUS_21"></a>

## 324.60 `CONFIG_BT_CTLR_TX_PWR_PLUS_21`

**提示（Prompt）**：+21 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:338`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L338)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BT_CTLR_TX_PWR_PLUS_3"></a>

## 324.61 `CONFIG_BT_CTLR_TX_PWR_PLUS_3`

**提示（Prompt）**：+3 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_COMPATIBLE_NRF52X || CONFIG_SOC_COMPATIBLE_NRF53X || CONFIG_SOC_SERIES_NRF54H || CONFIG_SOC_COMPATIBLE_NRF54LX || CONFIG_SOC_FAMILY_ESPRESSIF_ESP32) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:382`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L382)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF52X)、[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)、[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF52X`、`CONFIG_SOC_COMPATIBLE_NRF53X`、`CONFIG_SOC_COMPATIBLE_NRF54LX`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BT_CTLR_TX_PWR_PLUS_4"></a>

## 324.62 `CONFIG_BT_CTLR_TX_PWR_PLUS_4`

**提示（Prompt）**：+4 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_NRF51 || CONFIG_SOC_COMPATIBLE_NRF52X || CONFIG_SOC_SERIES_NRF54H || CONFIG_SOC_COMPATIBLE_NRF54LX) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:378`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L378)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_SOC_COMPATIBLE_NRF52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF52X)、[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF52X`、`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_TX_PWR_PLUS_5"></a>

## 324.63 `CONFIG_BT_CTLR_TX_PWR_PLUS_5`

**提示（Prompt）**：+5 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH || CONFIG_SOC_SERIES_NRF54H || CONFIG_SOC_COMPATIBLE_NRF54LX) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:374`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L374)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH)、[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH`、`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_TX_PWR_PLUS_6"></a>

## 324.64 `CONFIG_BT_CTLR_TX_PWR_PLUS_6`

**提示（Prompt）**：+6 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH || CONFIG_SOC_SERIES_NRF54H || CONFIG_SOC_COMPATIBLE_NRF54LX || CONFIG_SOC_FAMILY_ESPRESSIF_ESP32) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:370`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L370)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH)、[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH`、`CONFIG_SOC_COMPATIBLE_NRF54LX`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BT_CTLR_TX_PWR_PLUS_7"></a>

## 324.65 `CONFIG_BT_CTLR_TX_PWR_PLUS_7`

**提示（Prompt）**：+7 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH || CONFIG_SOC_SERIES_NRF54H || CONFIG_SOC_COMPATIBLE_NRF54LX) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:366`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L366)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH)、[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH`、`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_TX_PWR_PLUS_8"></a>

## 324.66 `CONFIG_BT_CTLR_TX_PWR_PLUS_8`

**提示（Prompt）**：+8 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH || CONFIG_SOC_SERIES_NRF54H || CONFIG_SOC_COMPATIBLE_NRF54LX) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:362`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L362)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH)、[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_RADIO_TX_PWR_HIGH`、`CONFIG_SOC_COMPATIBLE_NRF54LX`。

<a id="CONFIG_BT_CTLR_TX_PWR_PLUS_9"></a>

## 324.67 `CONFIG_BT_CTLR_TX_PWR_PLUS_9`

**提示（Prompt）**：+9 dBm 发射功率（Tx power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_NRF54H || CONFIG_SOC_FAMILY_ESPRESSIF_ESP32) && <choice CONFIG_BT_CTLR_TX_PWR>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:358`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L358)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发射功率（Tx Power）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BT_CTLR_TX_PWR`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_TX_PWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BT_CTLR_TX_RETRY_DISABLE"></a>

## 324.68 `CONFIG_BT_CTLR_TX_RETRY_DISABLE`

**提示（Prompt）**：禁用发送重试（Disable Tx Retry）

**说明（Help）**

如果对端在当前连接事件（connection event）中对某次发送返回否定应答（NACK），则避免重传该 PDU，直接结束连接事件，以减少重试消耗的电流，适用于对端没有缓冲区接收新 PDU 的情况。启用后可降低功耗，但发送延迟会增加一个连接间隔（connection interval）：下一次发送尝试会在下一个连接事件中进行，而不是在当前事件中反复重试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1111)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ULL_HIGH_PRIO"></a>

## 324.69 `CONFIG_BT_CTLR_ULL_HIGH_PRIO`

**提示（Prompt）**：上层链路层高优先级 IRQ 优先级（Upper Link Layer High IRQ priority）

**说明（Help）**

Ticker 的 Worker IRQ 及上层链路层（Upper Link Layer）高优先级功能所用的中断优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CTLR_LLL_PRIO if !CONFIG_BT_CTLR_ULL_LLL_PRIO_SUPPORT || CONFIG_BT_CTLR_ZLI || CONFIG_BT_CTLR_LOW_LAT
1
```

**取值范围（Ranges）**

```text
[CONFIG_BT_CTLR_LLL_PRIO, 3] if CONFIG_SOC_SERIES_NRF51
[CONFIG_BT_CTLR_LLL_PRIO, 6] if CONFIG_SOC_COMPATIBLE_NRF52X || CONFIG_SOC_COMPATIBLE_NRF53X
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:888`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L888)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_LLL_PRIO`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_LLL_PRIO)、[`CONFIG_BT_CTLR_ULL_LLL_PRIO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ULL_LLL_PRIO_SUPPORT)、[`CONFIG_BT_CTLR_ZLI`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_ZLI)、[`CONFIG_BT_CTLR_LOW_LAT`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_LOW_LAT)、[`CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_SOC_COMPATIBLE_NRF52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF52X)、[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_ULL_LLL_PRIO_SUPPORT`、`CONFIG_SOC_COMPATIBLE_NRF52X`、`CONFIG_SOC_COMPATIBLE_NRF53X`。

<a id="CONFIG_BT_CTLR_ULL_LOW_PRIO"></a>

## 324.70 `CONFIG_BT_CTLR_ULL_LOW_PRIO`

**提示（Prompt）**：上层链路层低优先级 IRQ 优先级（Upper Link Layer Low IRQ priority）

**说明（Help）**

Ticker 的 Job IRQ 及上层链路层（Upper Link Layer）低优先级功能所用的中断优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CTLR_ULL_HIGH_PRIO
```

**取值范围（Ranges）**

```text
[CONFIG_BT_CTLR_ULL_HIGH_PRIO, 3] if CONFIG_SOC_SERIES_NRF51
[CONFIG_BT_CTLR_ULL_HIGH_PRIO, 6] if CONFIG_SOC_COMPATIBLE_NRF52X || CONFIG_SOC_COMPATIBLE_NRF53X
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:898`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L898)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_ULL_HIGH_PRIO`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_ULL_HIGH_PRIO)、[`CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_SOC_COMPATIBLE_NRF52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF52X)、[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_SOC_COMPATIBLE_NRF52X`、`CONFIG_SOC_COMPATIBLE_NRF53X`。

<a id="CONFIG_BT_CTLR_USER_CPR_ANCHOR_POINT_MOVE"></a>

## 324.71 `CONFIG_BT_CTLR_USER_CPR_ANCHOR_POINT_MOVE`

**提示（Prompt）**：锚点移动的专有处理（Proprietary handling of anchor point movement）

**说明（Help）**

启用后，对于只涉及锚点移动（anchor point movement）的连接参数请求（Connection Parameter Request），将接受／拒绝决定交给专有逻辑（proprietary logic）处理。仅适用于外设（peripheral）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_USER_EXT && CONFIG_BT_CTLR_CONN_PARAM_REQ && CONFIG_BT_PERIPHERAL && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1438`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1438)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 控制器中的专有扩展（Proprietary extensions in Controller）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_USER_EXT`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_USER_EXT)、[`CONFIG_BT_CTLR_CONN_PARAM_REQ`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CONN_PARAM_REQ)、[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_USER_CPR_INTERVAL_MIN"></a>

## 324.72 `CONFIG_BT_CTLR_USER_CPR_INTERVAL_MIN`

**提示（Prompt）**：专有连接参数请求最小间隔（Proprietary Connection Parameter Request minimum interval）

**说明（Help）**

启用后，控制器可接受低至专有最小值（proprietary minimum value）的连接参数请求间隔（Connection Parameter Request intervals）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_USER_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1431`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1431)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 控制器中的专有扩展（Proprietary extensions in Controller）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_USER_EXT`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_USER_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_USER_EVT_RANGE"></a>

## 324.73 `CONFIG_BT_CTLR_USER_EVT_RANGE`

**提示（Prompt）**：为专有事件类型预留的事件常量范围（event constants reserved for proprietary event types）

**说明（Help）**

为专有用途预留的事件类型（event types）数量。通常在使用 `BT_CTLR_USER_EXT` 时使用该范围。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_USER_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1403`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1403)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 控制器中的专有扩展（Proprietary extensions in Controller）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_USER_EXT`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_USER_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_USER_EXT"></a>

## 324.74 `CONFIG_BT_CTLR_USER_EXT`

**提示（Prompt）**：控制器中的专有扩展（Proprietary extensions in Controller）

**说明（Help）**

用于统一启用控制器行为中专有事件类型（proprietary event types）的总开关。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1398`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1398)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_USER_TICKER_ID_RANGE"></a>

## 324.75 `CONFIG_BT_CTLR_USER_TICKER_ID_RANGE`

**提示（Prompt）**：为专有 ticker 节点预留的 ticker ID 常量范围（ticker id constants）

**说明（Help）**

为专有用途预留的 ticker ID 数量。通常在使用 `BT_CTLR_USER_EXT` 时使用该范围。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_USER_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1412`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1412)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 控制器中的专有扩展（Proprietary extensions in Controller）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_USER_EXT`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_USER_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_VERSION_SETTINGS"></a>

## 324.76 `CONFIG_BT_CTLR_VERSION_SETTINGS`

**提示（Prompt）**：版本设置（Version Settings）

**说明（Help）**

允许通过设置系统（settings system）配置控制器的公司标识符（Company Id）和子版本号（Subversion Number）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SETTINGS && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 设置系统（Settings System）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SETTINGS`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_SETTINGS)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_VS_SCAN_REQ_RX"></a>

## 324.77 `CONFIG_BT_CTLR_VS_SCAN_REQ_RX`

**提示（Prompt）**：使用扫描请求报告（Use scan request reporting）

**说明（Help）**

允许使用厂商专用扫描请求报告命令（VS Scan Request Reports Command）及扫描请求接收事件（Scan Request Received Event）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_VS && !CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_SCAN_REQ_NOTIFY
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1242`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1242)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_VS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_VS)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_SCAN_REQ_NOTIFY`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_SCAN_REQ_NOTIFY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_XTAL_ADVANCED"></a>

## 324.78 `CONFIG_BT_CTLR_XTAL_ADVANCED`

**提示（Prompt）**：高级事件准备（Advanced event preparation）

**说明（Help）**

启用高级事件准备功能，在无线电发送／接收（tx/rx）之前确定准备偏移量（preparation offset），并考虑事件准备阶段的预测处理时间需求，例如控制过程处理和 CPU 执行速度。对于间距较近的连续无线电事件，会保持晶体振荡器（crystal oscillator）运行，以减少晶体稳定过程的总次数及其电流消耗。

当角色事件的时间片（timeslice）安排紧密时，此功能通过减小准备阶段与无线电事件之间的偏移，最大限度提高平均时间片内的无线电利用率。禁用后，控制器在准备阶段与无线电事件之间使用固定偏移量，并在相邻且间距较近的无线电事件之间关闭再开启晶体振荡器；晶体稳定过程次数增加，平均电流也随之增大。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_XTAL_ADVANCED_SUPPORT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:728`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L728)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_XTAL_ADVANCED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_XTAL_ADVANCED_SUPPORT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_XTAL_ADVANCED_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_XTAL_THRESHOLD"></a>

## 324.79 `CONFIG_BT_CTLR_XTAL_THRESHOLD`

**提示（Prompt）**：晶体关闭阈值，单位为微秒（Crystal shutdown threshold in uS）

**说明（Help）**

配置两个连续无线电事件之间、从前一个事件结束到下一个事件准备之间的最优时间差，单位为微秒。低于该值时，会保持活动时钟晶体（active clock crystal）运行。此值取决于开发板（board）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_XTAL_ADVANCED && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:750`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L750)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 高级事件准备（Advanced event preparation）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_XTAL_ADVANCED`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_XTAL_ADVANCED)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ZLI"></a>

## 324.80 `CONFIG_BT_CTLR_ZLI`

**提示（Prompt）**：使用零延迟 IRQ（Use Zero Latency IRQs）

**说明（Help）**

启用零延迟中断请求（Zero Latency IRQ）功能支持。注意：选择此选项后，应用自身不得再使用零延迟 IRQ，否则会影响控制器稳定性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZERO_LATENCY_IRQS && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:679`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L679)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_ZERO_LATENCY_IRQS`](P030_arch_arm_配置项参考_2.md#CONFIG_ZERO_LATENCY_IRQS)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTS"></a>

## 324.81 `CONFIG_BT_CTS`

**提示（Prompt）**：GATT 当前时间服务（GATT Current Time service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.cts:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.cts#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CTS_HELPER_API"></a>

## 324.82 `CONFIG_BT_CTS_HELPER_API`

**提示（Prompt）**：用于编码和解码当前时间服务（CTS）格式时间的辅助 API（Helper APIs）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.cts:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.cts#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 当前时间服务（GATT Current Time service）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTS`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CUSTOM"></a>

## 324.83 `CONFIG_BT_CUSTOM`

**提示（Prompt）**：自定义（Custom）[已弃用，DEPRECATED]

**说明（Help）**

选择不基于 HCI 的自定义协议栈（custom, non-HCI based stack）。已弃用：此选项源自曾可在 Zephyr 蓝牙 API 后面卸载整个蓝牙主机（Bluetooth Host）的时期；当前源码树中没有任何选项选择它，而 HCI 传输已经是普通设备驱动。树外协议栈（out-of-tree stacks）应在此选择项（choice）中增加自己的条目。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_STACK_SELECTION>
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙协议栈选择（Bluetooth Stack Selection）

**配置项引用（Symbol References）**：[`CONFIG_BT_STACK_SELECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_STACK_SELECTION)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_BT_DATA_LEN_UPDATE"></a>

## 324.84 `CONFIG_BT_DATA_LEN_UPDATE`

**提示（Prompt）**：数据长度更新（Data Length Update）

**说明（Help）**

启用蓝牙 v4.2 低功耗蓝牙数据长度更新过程（LE Data Length Update procedure）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT) && CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_BUF_ACL_TX_SIZE > 27 || CONFIG_BT_BUF_ACL_RX_SIZE > 27
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L182)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BUF_ACL_TX_SIZE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BUF_ACL_TX_SIZE)、[`CONFIG_BT_BUF_ACL_RX_SIZE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BUF_ACL_RX_SIZE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT`。

<a id="CONFIG_BT_DEBUG_ISO_DATA"></a>

## 324.85 `CONFIG_BT_DEBUG_ISO_DATA`

**提示（Prompt）**：ISO 信道数据调试（ISO channel data debug）

**说明（Help）**

为蓝牙音频功能启用等时信道数据调试日志（ISO channels data debug logs），记录所有接收与发送的 ISO 数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ISO_LOG_LEVEL_DBG && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1107)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_LOG_LEVEL_DBG)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_DEBUG_MONITOR_RTT"></a>

## 324.86 `CONFIG_BT_DEBUG_MONITOR_RTT`

**提示（Prompt）**：基于 RTT 的监视协议（Monitor protocol over RTT）

**说明（Help）**

通过 RTT 缓冲区使用自定义日志协议（custom logging protocol），代替纯文本输出。需要主机端有能够解码该协议的专用应用。所译快照指出，BlueZ 的 `btmon` 工具能够执行此操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SEGGER_RTT && CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS >= 2 && <choice CONFIG_BT_DEBUG_TYPE>
```

**主动选择（Selects）**

```text
CONFIG_LOG
CONFIG_CONSOLE_HAS_DRIVER
CONFIG_BT_MONITOR
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:360`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L360)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙调试类型（Bluetooth debug type）

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)、[`CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS)、[`CONFIG_BT_DEBUG_TYPE`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_TYPE)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_CONSOLE_HAS_DRIVER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HAS_DRIVER)、[`CONFIG_BT_MONITOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MONITOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MONITOR`。

<a id="CONFIG_BT_DEBUG_MONITOR_RTT_BUFFER"></a>

## 324.87 `CONFIG_BT_DEBUG_MONITOR_RTT_BUFFER`

**提示（Prompt）**：自定义日志输出使用的缓冲区编号（Buffer number for custom logger output）

**说明（Help）**

选择日志输出所用上行缓冲区（up-buffer）的索引。确保该缓冲区编号未被其他日志后端使用，例如 `LOG_BACKEND_RTT_BUFFER` 中指定的后端，否则缓冲区内容会被覆盖。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DEBUG_MONITOR_RTT && <choice CONFIG_BT_DEBUG_TYPE>
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS]
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:375`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L375)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙调试类型（Bluetooth debug type） → 基于 RTT 的监视协议（Monitor protocol over RTT）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEBUG_MONITOR_RTT`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_MONITOR_RTT)、[`CONFIG_BT_DEBUG_TYPE`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_TYPE)、[`CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS)。

<a id="CONFIG_BT_DEBUG_MONITOR_RTT_BUFFER_NAME"></a>

## 324.88 `CONFIG_BT_DEBUG_MONITOR_RTT_BUFFER_NAME`

**提示（Prompt）**：自定义日志输出使用的缓冲区名称（Buffer name for custom logger output）

**说明（Help）**

选择日志输出使用的上行缓冲区（up-buffer）索引。

译注：原帮助文本写的是“索引（index）”；用于缓冲区名称配置时，它与该配置的提示文本不一致，此处保留原文表述。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DEBUG_MONITOR_RTT && <choice CONFIG_BT_DEBUG_TYPE>
```

**默认值（Defaults）**

```text
"btmonitor"
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:385`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L385)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙调试类型（Bluetooth debug type） → 基于 RTT 的监视协议（Monitor protocol over RTT）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEBUG_MONITOR_RTT`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_MONITOR_RTT)、[`CONFIG_BT_DEBUG_TYPE`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_TYPE)。

<a id="CONFIG_BT_DEBUG_MONITOR_RTT_BUFFER_SIZE"></a>

## 324.89 `CONFIG_BT_DEBUG_MONITOR_RTT_BUFFER_SIZE`

**提示（Prompt）**：为自定义日志输出预留的上行缓冲区大小（Size of reserved up-buffer）

**说明（Help）**

指定自定义日志输出（custom logger output）所用上行缓冲区（up-buffer）的预留大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DEBUG_MONITOR_RTT && <choice CONFIG_BT_DEBUG_TYPE>
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:391`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L391)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙调试类型（Bluetooth debug type） → 基于 RTT 的监视协议（Monitor protocol over RTT）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEBUG_MONITOR_RTT`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_MONITOR_RTT)、[`CONFIG_BT_DEBUG_TYPE`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_TYPE)。

<a id="CONFIG_BT_DEBUG_MONITOR_UART"></a>

## 324.90 `CONFIG_BT_DEBUG_MONITOR_UART`

**提示（Prompt）**：基于 UART 的监视协议（Monitor protocol over UART）

**说明（Help）**

通过控制台 UART 使用自定义日志协议（custom logging protocol），代替纯文本输出。需要主机端有能够解码该协议的专用应用；所译快照指出，BlueZ 的 `btmon` 工具能够执行此操作。

如果目标开发板有两个或更多外部 UART，可以同时使用 `UART_CONSOLE` 和此选项。如果只有一个外部 UART，则需要禁用 `UART_CONSOLE`；此时 `printk`／`printf` 输出会被编码进监视协议（monitor protocol）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_DEBUG_TYPE>
```

**主动选择（Selects）**

```text
CONFIG_LOG
CONFIG_CONSOLE_HAS_DRIVER
CONFIG_BT_MONITOR
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:313`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L313)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙调试类型（Bluetooth debug type）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEBUG_TYPE`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_TYPE)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_CONSOLE_HAS_DRIVER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HAS_DRIVER)、[`CONFIG_BT_MONITOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MONITOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MONITOR`。

<a id="CONFIG_BT_DEBUG_MONITOR_UART_BUFFER_SIZE"></a>

## 324.91 `CONFIG_BT_DEBUG_MONITOR_UART_BUFFER_SIZE`

**提示（Prompt）**：UART 监视发送缓冲区大小（UART monitor transmit buffer size）

**说明（Help）**

中断驱动监视输出（interrupt-driven monitor output）所用环形缓冲区（ring buffer）的大小，单位为字节。大于缓冲区的记录永远无法发送，总会被丢弃，因此应确保缓冲区能容纳最大的监视记录（monitor record）：最大 HCI 数据包加上最多 `25` 字节的监视头（monitor header）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DEBUG_MONITOR_UART_INTERRUPT_DRIVEN && CONFIG_BT_DEBUG_MONITOR_UART && <choice CONFIG_BT_DEBUG_TYPE>
```

**默认值（Defaults）**

```text
1024
```

**取值范围（Ranges）**

```text
[64, 32767]
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:345`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L345)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙调试类型（Bluetooth debug type） → 基于 UART 的监视协议（Monitor protocol over UART） → 中断驱动的 UART 监视输出（Interrupt-driven UART monitor output）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEBUG_MONITOR_UART_INTERRUPT_DRIVEN`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_MONITOR_UART_INTERRUPT_DRIVEN)、[`CONFIG_BT_DEBUG_MONITOR_UART`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_MONITOR_UART)、[`CONFIG_BT_DEBUG_TYPE`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_TYPE)。

<a id="CONFIG_BT_DEBUG_MONITOR_UART_INTERRUPT_DRIVEN"></a>

## 324.92 `CONFIG_BT_DEBUG_MONITOR_UART_INTERRUPT_DRIVEN`

**提示（Prompt）**：中断驱动的 UART 监视输出（Interrupt-driven UART monitor output）

**说明（Help）**

缓存完整的监视记录（monitor records），并从 UART 中断处理程序（interrupt handler）中发送，以避免蓝牙主机在等待逐字节发送时阻塞。无法放入缓冲区的记录会被丢弃，并在下一条监视记录中报告。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL_SUPPORT_INTERRUPT && !CONFIG_LOG_MODE_MINIMAL && CONFIG_BT_DEBUG_MONITOR_UART && <choice CONFIG_BT_DEBUG_TYPE>
```

**主动选择（Selects）**

```text
CONFIG_UART_INTERRUPT_DRIVEN
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:332`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L332)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙调试类型（Bluetooth debug type） → 基于 UART 的监视协议（Monitor protocol over UART）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_LOG_MODE_MINIMAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_BT_DEBUG_MONITOR_UART`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_MONITOR_UART)、[`CONFIG_BT_DEBUG_TYPE`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_TYPE)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)。

<a id="CONFIG_BT_DEBUG_NONE"></a>

## 324.93 `CONFIG_BT_DEBUG_NONE`

**提示（Prompt）**：无调试日志（No debug log）

**说明（Help）**

选择此项以禁用所有蓝牙调试日志（Bluetooth debug logs）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_DEBUG_TYPE>
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:308`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L308)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙调试类型（Bluetooth debug type）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEBUG_TYPE`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_TYPE)。

<a id="CONFIG_BT_DEBUG_TYPE"></a>

## 324.94 `CONFIG_BT_DEBUG_TYPE`

**提示（Prompt）**：蓝牙调试类型（Bluetooth debug type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_DEBUG_NONE
```

**可选项（Choices）**

```text
CONFIG_BT_DEBUG_NONE
CONFIG_BT_DEBUG_MONITOR_UART
CONFIG_BT_DEBUG_MONITOR_RTT
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:304`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L304)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_DEBUG_NONE`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_NONE)、[`CONFIG_BT_DEBUG_MONITOR_UART`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_MONITOR_UART)、[`CONFIG_BT_DEBUG_MONITOR_RTT`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_MONITOR_RTT)。

<a id="CONFIG_BT_DEFAULT_ROLE_SWITCH_ENABLE"></a>

## 324.95 `CONFIG_BT_DEFAULT_ROLE_SWITCH_ENABLE`

**提示（Prompt）**：蓝牙角色切换默认启用／禁用状态（Default Bluetooth Role Switch Enable/Disable State）

**说明（Help）**

此选项设置控制器默认链路策略（default link policy），决定是否启用角色切换（role switch）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:692`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L692)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_DEVICE_APPEARANCE"></a>

## 324.96 `CONFIG_BT_DEVICE_APPEARANCE`

**提示（Prompt）**：蓝牙设备外观（Bluetooth device appearance）

**说明（Help）**

蓝牙设备外观（Bluetooth device appearance）。可用值列表请参阅 [Bluetooth 分配编号（Assigned Numbers）](https://www.bluetooth.com/specifications/assigned-numbers)。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:964`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L964)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DEVICE_APPEARANCE_DYNAMIC"></a>

## 324.97 `CONFIG_BT_DEVICE_APPEARANCE_DYNAMIC`

**提示（Prompt）**：运行时修改蓝牙外观（Runtime Bluetooth Appearance changing）

**说明（Help）**

允许使用 `bt_set_appearance`。如果设置了 `CONFIG_BT_SETTINGS`，外观值（appearance）会持久化存储。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:958`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L958)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE"></a>

## 324.98 `CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE`

**提示（Prompt）**：允许远端 GATT 客户端写入 GAP 外观（GAP Appearance）

**说明（Help）**

启用后，远端 GATT 客户端（clients）可以写入设备外观 GAP 特征（device appearance GAP characteristic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DEVICE_APPEARANCE_DYNAMIC && CONFIG_BT_GAP_SVC && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.gap_svc:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.gap_svc#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 通用访问服务（GATT Generic Access Service）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEVICE_APPEARANCE_DYNAMIC`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEVICE_APPEARANCE_DYNAMIC)、[`CONFIG_BT_GAP_SVC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GAP_SVC)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN"></a>

## 324.99 `CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN`

**提示（Prompt）**：要求加密与身份认证（Encryption and authentication required）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_SECURITY>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.gap_svc:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.gap_svc#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 通用访问服务（GATT Generic Access Service） → 允许远端 GATT 客户端写入 GAP 外观（GAP Appearance） → 安全要求（Security requirements）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_SECURITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_SECURITY)。

<a id="CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_ENCRYPT"></a>

## 324.100 `CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_ENCRYPT`

**提示（Prompt）**：要求加密（Encryption required）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_SECURITY>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.gap_svc:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.gap_svc#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 通用访问服务（GATT Generic Access Service） → 允许远端 GATT 客户端写入 GAP 外观（GAP Appearance） → 安全要求（Security requirements）

**配置项引用（Symbol References）**：[`CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_SECURITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_SECURITY)。

<!-- kconfig-navigation -->

[上一章](P323_subsys_bluetooth_配置项参考_4.md) · [返回大纲](大纲.md) · [下一章](P325_subsys_bluetooth_配置项参考_6.md)
