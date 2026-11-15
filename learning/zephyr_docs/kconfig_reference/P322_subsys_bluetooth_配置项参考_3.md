---
id: learning.zephyr-docs.kconfig-reference.page-322
title: "`subsys/bluetooth`配置项参考（3/13）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第322章\_`subsys/bluetooth`配置项参考（3/13）

本章翻译官方 Kconfig 数据库中 `subsys/bluetooth` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_CTLR_ADV_INTERVAL_MAX"></a>

## 322.1 `CONFIG_BT_CTLR_ADV_INTERVAL_MAX`

**提示（Prompt）**：主广播间隔最大值（Primary Advertising Interval Maximum）

**说明（Help）**

支持的主广播间隔（Primary Advertising Interval）最大值。蓝牙核心规范 v5.3（Bluetooth Core Specification v5.3）允许的范围为 `0x000020` 到 `0xFFFFFF`，以 `0.625 ms` 为单位。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BROADCASTER && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x004000 if CONFIG_BT_LL_SW_SPLIT
0xFFFFFF
```

**取值范围（Ranges）**

```text
[0x000020, 0x004000] if CONFIG_BT_LL_SW_SPLIT
[0x000020, 0xFFFFFF]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:757`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L757)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_ISO"></a>

## 322.2 `CONFIG_BT_CTLR_ADV_ISO`

原库同名定义共 2 条；本项为数据库第 1783 条记录，各定义分别保留。

**提示（Prompt）**：低功耗蓝牙广播等时信道广播（LE Broadcast Isochronous Channel advertising）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.2 低功耗蓝牙等时广播（LE Isochronous Advertising）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ISO_BROADCASTER && CONFIG_BT_CTLR_ADV_ISO_SUPPORT && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_ISO_BROADCASTER
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_ADV_PERIODIC
CONFIG_BT_CTLR_SET_HOST_FEATURE
CONFIG_BT_CTLR_ADV_ISO_SEQUENTIAL if !CONFIG_BT_CTLR_ADV_ISO_INTERLEAVED
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:895`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L895)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO_BROADCASTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_BROADCASTER)、[`CONFIG_BT_CTLR_ADV_ISO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_ISO_SUPPORT)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_ADV_PERIODIC`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_PERIODIC)、[`CONFIG_BT_CTLR_SET_HOST_FEATURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SET_HOST_FEATURE)、[`CONFIG_BT_CTLR_ADV_ISO_SEQUENTIAL`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO_SEQUENTIAL)、[`CONFIG_BT_CTLR_ADV_ISO_INTERLEAVED`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO_INTERLEAVED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_ADV_ISO_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_ISO--record-1784"></a>

## 322.3 `CONFIG_BT_CTLR_ADV_ISO`

原库同名定义共 2 条；本项为数据库第 1784 条记录，各定义分别保留。

**提示（Prompt）**：低功耗蓝牙广播等时信道广播，分离式链路层（Split Link Layer）[实验性，EXPERIMENTAL]

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

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:906`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L906)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_ISO_INTERLEAVED"></a>

## 322.4 `CONFIG_BT_CTLR_ADV_ISO_INTERLEAVED`

**提示（Prompt）**：低功耗蓝牙广播等时信道广播的交错打包（interleaved packing）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_ISO && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:914`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L914)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions） → 低功耗蓝牙广播等时信道广播，分离式链路层（Split Link Layer）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_ISO_PDU_LEN_MAX"></a>

## 322.5 `CONFIG_BT_CTLR_ADV_ISO_PDU_LEN_MAX`

**提示（Prompt）**：广播等时信道 PDU 最大长度（Maximum Broadcast Isochronous Channel PDU Length）

**说明（Help）**

广播等时信道（Broadcast Isochronous Channel）协议数据单元（PDU）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_ISO && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
251
```

**取值范围（Ranges）**

```text
[1, 251]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:977`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L977)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_ISO_RESERVE_MAX"></a>

## 322.6 `CONFIG_BT_CTLR_ADV_ISO_RESERVE_MAX`

**提示（Prompt）**：使用最大的广播 ISO 事件时间预留量（maximum Broadcast ISO event time reservation）

**说明（Help）**

使用最大的广播等时（Broadcast ISO）事件时间预留量。禁用时，预留时间不包含最后一个广播等时流（BIS）的预发送（pre-transmissions），也不包含任何控制子事件（Control subevents）。这样允许扩展广播或周期性广播事件抢占广播等时组（BIG）事件；当 BIG 事件不与扩展广播或周期性广播重叠时，也允许更大的 BIG 事件，从而提高无线电利用率（radio utilization）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_ISO && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:492`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L492)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_ISO_SEQUENTIAL"></a>

## 322.7 `CONFIG_BT_CTLR_ADV_ISO_SEQUENTIAL`

**提示（Prompt）**：低功耗蓝牙广播等时信道广播的顺序打包（sequential packing）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_ISO && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_CTLR_ADV_ISO
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:910`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L910)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions） → 低功耗蓝牙广播等时信道广播，分离式链路层（Split Link Layer）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_ISO_SET"></a>

## 322.8 `CONFIG_BT_CTLR_ADV_ISO_SET`

**提示（Prompt）**：低功耗蓝牙等时信道广播集合（LE Isochronous Channel advertising sets）

**说明（Help）**

支持的广播集合（advertising sets）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_ISO && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ISO_MAX_BIG
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:953`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L953)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_MAX_BIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_MAX_BIG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_ISO_STREAM_COUNT"></a>

## 322.9 `CONFIG_BT_CTLR_ADV_ISO_STREAM_COUNT`

**提示（Prompt）**：最大广播 ISO 流数量（Maximum Broadcast ISO Streams）

**说明（Help）**

控制器（Controller）在所有广播等时组（Broadcast ISO groups）范围内支持的广播等时流（Broadcast ISO Streams）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_ISO && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ISO_MAX_CHAN
```

**取值范围（Ranges）**

```text
[CONFIG_BT_CTLR_ADV_ISO_STREAM_MAX, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:968`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L968)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_MAX_CHAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_MAX_CHAN)、[`CONFIG_BT_CTLR_ADV_ISO_STREAM_MAX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO_STREAM_MAX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_ISO_STREAM_MAX"></a>

## 322.10 `CONFIG_BT_CTLR_ADV_ISO_STREAM_MAX`

**提示（Prompt）**：每个广播 ISO 组支持的最大广播 ISO 流数量（Broadcast ISO Streams per Broadcast ISO group）

**说明（Help）**

每个广播等时组（Broadcast ISO group）支持的广播等时流（Broadcast ISO Streams）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_ISO && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**取值范围（Ranges）**

```text
[1, 31]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:961`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L961)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_PERIODIC"></a>

## 322.11 `CONFIG_BT_CTLR_ADV_PERIODIC`

**提示（Prompt）**：广播状态下的低功耗蓝牙周期性广播（LE Periodic Advertising in Advertising State）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.0 低功耗蓝牙周期性广播（LE Periodic Advertising）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BROADCASTER && CONFIG_BT_CTLR_ADV_PERIODIC_SUPPORT && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_PER_ADV
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_CHAN_SEL_2
```

**被选择（Selected by）**

```text
CONFIG_BT_CTLR_ADV_ISO
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:777`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L777)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_CTLR_ADV_PERIODIC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_PERIODIC_SUPPORT)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_PER_ADV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV)、[`CONFIG_BT_CTLR_CHAN_SEL_2`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CHAN_SEL_2)、[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_ADV_PERIODIC_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_PERIODIC_ADI_SUPPORT"></a>

## 322.12 `CONFIG_BT_CTLR_ADV_PERIODIC_ADI_SUPPORT`

**提示（Prompt）**：周期性广播 ADI 支持（Periodic Advertising ADI support）

**说明（Help）**

允许在周期性广播协议数据单元（Periodic Advertising PDUs）中添加 `AdvDataInfo`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_PERIODIC && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:806`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L806)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_PERIODIC`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_PERIODIC)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_PERIODIC_INTERVAL_MAX"></a>

## 322.13 `CONFIG_BT_CTLR_ADV_PERIODIC_INTERVAL_MAX`

**提示（Prompt）**：周期性广播间隔最大值（Periodic Advertising Interval Maximum）

**说明（Help）**

支持的周期性广播间隔（Periodic Advertising Interval）最大值。蓝牙核心规范 v5.3（Bluetooth Core Specification v5.3）允许的范围为 `0x0006` 到 `0xFFFF`，以 `1.25 ms` 为单位。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_PERIODIC && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x2000 if CONFIG_BT_LL_SW_SPLIT
0xFFFF
```

**取值范围（Ranges）**

```text
[0x0006, 0x2000] if CONFIG_BT_LL_SW_SPLIT
[0x0006, 0xFFFF]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:812`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L812)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_PERIODIC`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_PERIODIC)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_PERIODIC_RSP"></a>

## 322.14 `CONFIG_BT_CTLR_ADV_PERIODIC_RSP`

**提示（Prompt）**：广播状态下的低功耗蓝牙带响应周期性广播（LE Periodic Advertising with Responses in Advertising State）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.4 低功耗蓝牙带响应周期性广播（LE Periodic Advertising with Responses）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BROADCASTER && CONFIG_BT_CTLR_ADV_PERIODIC_RSP_SUPPORT && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_PER_ADV_RSP
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_CHAN_SEL_2
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:786`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L786)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_CTLR_ADV_PERIODIC_RSP_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_PERIODIC_RSP_SUPPORT)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_PER_ADV_RSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_RSP)、[`CONFIG_BT_CTLR_CHAN_SEL_2`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CHAN_SEL_2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_ADV_PERIODIC_RSP_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_RESERVE_MAX"></a>

## 322.15 `CONFIG_BT_CTLR_ADV_RESERVE_MAX`

**提示（Prompt）**：按最大广播 PDU 大小预留时间（maximum Advertising PDU size time reservation）

**说明（Help）**

考虑到广播数据（Advertising Data）可能从零增长到所支持的最大大小，按最大的广播协议数据单元（PDU）大小预留时间。如果禁用最大时间预留（maximum time reservation），则使用启动／启用广播时实际存在的广播数据所对应的时间预留量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BROADCASTER && CONFIG_BT_CTLR_ADV_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:470`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L470)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_SET"></a>

## 322.16 `CONFIG_BT_CTLR_ADV_SET`

**提示（Prompt）**：低功耗蓝牙广播扩展集合（LE Advertising Extensions Sets）

**说明（Help）**

支持的广播集合（advertising sets）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BROADCASTER && CONFIG_BT_CTLR_ADV_EXT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_EXT_ADV_MAX_ADV_SET if CONFIG_BT_EXT_ADV
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:749`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L749)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙广播扩展（LE Advertising Extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_EXT_ADV_MAX_ADV_SET`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV_MAX_ADV_SET)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_SYNC_PDU_BACK2BACK"></a>

## 322.17 `CONFIG_BT_CTLR_ADV_SYNC_PDU_BACK2BACK`

**提示（Prompt）**：周期性广播序列的背靠背发送（Back-to-back transmission of periodic advertising trains）

**说明（Help）**

允许在周期性广播序列（periodic advertising train）中发送 `AUX_CHAIN_IND`，各 `AUX_CHAIN_IND` 依次背靠背（back-to-back）发送。注意，连续的 `AUX_CHAIN_IND` 数据包不单独调度，而是按固定偏移尽力发送（best effort）。这意味着广播序列随时可能被其他事件抢占（preempted）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CTLR_ADV_PERIODIC && CONFIG_BT_CTLR_ADV_DATA_CHAIN
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_ADV_SYNC_PDU_LINK
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:450`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L450)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_ADV_PERIODIC`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_PERIODIC)、[`CONFIG_BT_CTLR_ADV_DATA_CHAIN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_DATA_CHAIN)、[`CONFIG_BT_CTLR_ADV_SYNC_PDU_LINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_SYNC_PDU_LINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_ADV_SYNC_PDU_LINK`。

<a id="CONFIG_BT_CTLR_ADV_SYNC_PDU_BACK2BACK_AFS"></a>

## 322.18 `CONFIG_BT_CTLR_ADV_SYNC_PDU_BACK2BACK_AFS`

**提示（Prompt）**：周期性广播序列背靠背发送的辅助帧间隔（AUX Frame Space）

**说明（Help）**

指定周期性广播序列（periodic advertising trains）背靠背发送所用的辅助帧间隔（AUX Frame Space），时间单位为微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_SYNC_PDU_BACK2BACK && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
300
```

**取值范围（Ranges）**

```text
[300, 1000]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:461`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L461)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 周期性广播序列的背靠背发送（Back-to-back transmission of periodic advertising trains）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_SYNC_PDU_BACK2BACK`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_SYNC_PDU_BACK2BACK)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ADV_SYNC_SET"></a>

## 322.19 `CONFIG_BT_CTLR_ADV_SYNC_SET`

**提示（Prompt）**：低功耗蓝牙周期性广播集合（LE Periodic Advertising Sets）

**说明（Help）**

支持的周期性广播集合（periodic advertising sets）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ADV_PERIODIC && CONFIG_BT_CTLR_ADV_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, CONFIG_BT_CTLR_ADV_AUX_SET]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:266`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L266)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_PERIODIC`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_PERIODIC)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_ADV_AUX_SET`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_AUX_SET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_AD_DATA_BACKUP"></a>

## 322.20 `CONFIG_BT_CTLR_AD_DATA_BACKUP`

**提示（Prompt）**：传统广播数据备份（Legacy AD Data backup）

**说明（Help）**

切换到传统定向广播（Legacy Directed Advertising）或扩展广播（Extended Advertising）模式时，备份传统广播数据（Legacy Advertising Data）；切回传统非定向广播（Legacy Non-Directed Advertising）模式时恢复这些数据。如果应用不使用定向广播，也不在传统与扩展广播之间切换，可以禁用此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_PERIPHERAL || CONFIG_BT_CTLR_ADV_EXT) && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ALLOW_SAME_PEER_CONN"></a>

## 322.21 `CONFIG_BT_CTLR_ALLOW_SAME_PEER_CONN`

**提示（Prompt）**：允许来自同一对端的连接请求（Allow connection requests from same peer）

**说明（Help）**

允许来自同一对端（peer）的连接请求。蓝牙规范不允许与同一对端建立多个连接，但在调试多连接时，允许此行为具有实用价值。警告：此选项启用的行为违反蓝牙规范（Bluetooth specification）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MAX_CONN > 1 && CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1180)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_MAX_CONN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAX_CONN)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ASSERT_DEBUG"></a>

## 322.22 `CONFIG_BT_CTLR_ASSERT_DEBUG`

**提示（Prompt）**：开发断言（Development asserts）

**说明（Help）**

此选项启用用于代码覆盖（code coverage）的开发断言（development asserts）。禁用这些断言检查后，控制器仍可运行，不会因此发生内存泄漏或内存破坏。例如，运行时未对齐内存访问（mis-aligned memory access）等情况，在开发测试中原本也会隐式触发 CPU 故障（fault）。不过，这类断言对于开发周期中的调试、代码覆盖和单元测试覆盖非常必要。

译注：以上是原帮助文本对这些开发检查的说明，不表示任意控制器故障均可安全忽略。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1209`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1209)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ASSERT_HANDLER"></a>

## 322.23 `CONFIG_BT_CTLR_ASSERT_HANDLER`

**提示（Prompt）**：应用定义的断言处理程序（Application Defined Assertion Handler）

**说明（Help）**

此选项为控制器断言机制（controller assertion mechanism）启用由应用定义的处理入口。应用代码必须定义 `void bt_ctlr_assert_handle(char *, int)`；控制器代码遇到不可恢复错误（unrecoverable error）时调用它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1221)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ASSERT_OPTIMIZE_FOR_SIZE"></a>

## 322.24 `CONFIG_BT_CTLR_ASSERT_OPTIMIZE_FOR_SIZE`

**提示（Prompt）**：按代码大小优化的断言（Assertions optimized for code size）

**说明（Help）**

针对代码大小优化控制器断言检查（Controller assertion check）。例如，通过未定义指令异常（undefined instruction exception）减小 ARM Cortex-M CPU 上的断言检查代码大小。可使用命令行工具 `arm-none-eabi-addr2line`，根据程序计数器（program counter）值得到源文件和行号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ASSERT_OPTIMIZE_FOR_SIZE_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1230`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1230)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ASSERT_OPTIMIZE_FOR_SIZE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ASSERT_OPTIMIZE_FOR_SIZE_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_ASSERT_OPTIMIZE_FOR_SIZE_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ASSERT_OVERHEAD_START"></a>

## 322.25 `CONFIG_BT_CTLR_ASSERT_OVERHEAD_START`

**提示（Prompt）**：对准备延迟进行断言（Assert on Prepare Latency）

**说明（Help）**

当控制器实现中的 CPU 使用开销导致无线电事件准备回调（Radio Event Prepare callback）延迟增大时触发断言。禁用后，控制器可平稳跳过因 CPU 使用延迟而晚到的无线电事件（radio events），但前提是不能每一个连续无线电事件间隔都被跳过；否则会导致远端监督超时（supervision timeout），并可能丢失本地断开事件（disconnect events）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:781`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L781)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ASSERT_VENDOR"></a>

## 322.26 `CONFIG_BT_CTLR_ASSERT_VENDOR`

**提示（Prompt）**：厂商定义的断言信息处理程序（Vendor Defined Assertion Information Handler）

**说明（Help）**

此选项为控制器断言机制启用厂商专用处理入口，并向其提供参数信息（parameter information）。厂商调试 HAL 接口必须将其定义为 `BT_ASSERT_VND(cond, param1, param2)`；控制器代码遇到带参数信息的不可恢复错误时调用它。实现中应包含等同于 `BT_ASSERT_DIE` 的操作，以停止内核（halt the kernel）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:794`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L794)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CENTRAL_ISO"></a>

## 322.27 `CONFIG_BT_CTLR_CENTRAL_ISO`

原库同名定义共 2 条；本项为数据库第 1808 条记录，各定义分别保留。

**提示（Prompt）**：低功耗蓝牙连接等时流中心设备（LE Connected Isochronous Stream Central）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.2 低功耗蓝牙连接等时流中心设备角色（LE Connected Isochronous Stream Central role）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT && CONFIG_BT_ISO_CENTRAL && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_ISO_CENTRAL
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1030`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1030)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT)、[`CONFIG_BT_ISO_CENTRAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_CENTRAL)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CENTRAL_ISO--record-1809"></a>

## 322.28 `CONFIG_BT_CTLR_CENTRAL_ISO`

原库同名定义共 2 条；本项为数据库第 1809 条记录，各定义分别保留。

**提示（Prompt）**：低功耗蓝牙连接等时流中心设备，分离式链路层（Split Link Layer）[实验性，EXPERIMENTAL]

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT && CONFIG_BT_ISO_CENTRAL && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_ISO_CENTRAL
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_SET_HOST_FEATURE
CONFIG_EXPERIMENTAL if CONFIG_BT_LL_SW_SPLIT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1038`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1038)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT)、[`CONFIG_BT_ISO_CENTRAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_CENTRAL)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_SET_HOST_FEATURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SET_HOST_FEATURE)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CENTRAL_RESERVE_MAX"></a>

## 322.29 `CONFIG_BT_CTLR_CENTRAL_RESERVE_MAX`

**提示（Prompt）**：中心设备按最大数据 PDU 大小预留时间（maximum data PDU size time reservation for Central）

**说明（Help）**

考虑到数据长度（Data length）可能从默认 `27` 字节更新为所支持的最大大小，按最大数据 PDU 大小预留时间。如果禁用最大时间预留，则采用启动／启用中心设备角色（Central role）时默认数据长度所对应的时间预留量。注意：本快照中，此值仅用于为多个中心设备连接安排间距，尚不用于实际的 ticker 时间预留（ticker time reservations）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CENTRAL && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:823`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L823)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CENTRAL_SPACING"></a>

## 322.30 `CONFIG_BT_CTLR_CENTRAL_SPACING`

**提示（Prompt）**：中心设备连接间距（Central Connection Spacing）

**说明（Help）**

多个同时活动的中心设备角色（central roles）之间的首选连接间距，单位为微秒。控制器会根据当前使用的数据长度和物理层（PHY）计算所需的时间预留量，并采用首选间距与计算所得时间预留量中的较大值。精度由平台相关 ticker 时钟的分辨率决定。

范围上限是一个向上取整的值，为调整控制器无线电处理开销以及编码 PHY（Coded PHY）的 S8 编码方案 PDU 时长留出空间，即：无线电事件开销 + `17040`（PDU 发送，Tx）+ `150`（tIFS）+ `4`（活动时钟抖动，active clock jitter）+ `17040`（PDU 接收，rx）=（无线电事件开销 + `34234`）微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_SCHED_ADVANCED && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:804`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L804)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_SCHED_ADVANCED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SCHED_ADVANCED)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CHANNEL_SOUNDING"></a>

## 322.31 `CONFIG_BT_CTLR_CHANNEL_SOUNDING`

**提示（Prompt）**：信道探测支持（Channel Sounding support）

**说明（Help）**

在控制器（Controller）中启用蓝牙 6.0 信道探测（Channel Sounding）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CHANNEL_SOUNDING_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_CHANNEL_SOUNDING
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_SET_HOST_FEATURE
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1174)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CHANNEL_SOUNDING_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CHANNEL_SOUNDING_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CHANNEL_SOUNDING`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CHANNEL_SOUNDING)、[`CONFIG_BT_CTLR_SET_HOST_FEATURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SET_HOST_FEATURE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CHANNEL_SOUNDING_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CHAN_SEL_2"></a>

## 322.32 `CONFIG_BT_CTLR_CHAN_SEL_2`

**提示（Prompt）**：信道选择算法 #2（Channel Selection Algorithm #2）

**说明（Help）**

在控制器（Controller）中启用蓝牙 5.0 低功耗蓝牙信道选择算法 #2（LE Channel Selection Algorithm #2）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CONN || (CONFIG_BT_BROADCASTER && CONFIG_BT_CTLR_ADV_EXT) || CONFIG_BT_CTLR_ADV_PERIODIC || CONFIG_BT_CTLR_SYNC_PERIODIC) && CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_BT_CTLR_ADV_EXT
CONFIG_BT_CTLR_ADV_PERIODIC
CONFIG_BT_CTLR_ADV_PERIODIC_RSP
CONFIG_BT_CTLR_SYNC_PERIODIC
CONFIG_BT_CTLR_SYNC_PERIODIC_RSP
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:729`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L729)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_CTLR_ADV_PERIODIC`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_PERIODIC)、[`CONFIG_BT_CTLR_SYNC_PERIODIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_PERIODIC)、[`CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_ADV_PERIODIC_RSP`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_PERIODIC_RSP)、[`CONFIG_BT_CTLR_SYNC_PERIODIC_RSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_PERIODIC_RSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CIS_ACCEPT_MIN_OFFSET_STRICT"></a>

## 322.33 `CONFIG_BT_CTLR_CIS_ACCEPT_MIN_OFFSET_STRICT`

**提示（Prompt）**：严格执行 CIS 最小偏移检查（Enforce Strict CIS Minimum Offset Check）

**说明（Help）**

严格检查外设（peripheral）接受的连接等时流（CIS）最小偏移，以保证 ACL 连接不会与连接等时组（CIG）事件重叠。检查时考虑 ACL 连接事件的无线电与 CPU 开销，并确认 CIS 最小偏移大于 ACL 连接的时间预留量（time reservation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_PERIPHERAL_ISO && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:623`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L623)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_PERIPHERAL_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PERIPHERAL_ISO)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_COEX_DRIVERS"></a>

## 322.34 `CONFIG_BT_CTLR_COEX_DRIVERS`

**提示（Prompt）**：蓝牙共存驱动（Bluetooth Co-existence Drivers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_BT_CTLR && DT_HAS_RADIO_GPIO_COEX_ENABLED && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/coex/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/coex/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_COEX_TICKER"></a>

## 322.35 `CONFIG_BT_CTLR_COEX_TICKER`

**提示（Prompt）**：共存 ticker（Coexistence Ticker）

**说明（Help）**

启用后，控制器包含共存设备（Coexistence device）的实现；共存引脚（coex pin）置为有效时，该实现会中止任何无线电状态（radio states）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_COEX_DRIVERS && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/coex/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/coex/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙共存驱动（Bluetooth Co-existence Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_COEX_DRIVERS`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_COEX_DRIVERS)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_COMPANY_ID"></a>

## 322.36 `CONFIG_BT_CTLR_COMPANY_ID`

**提示（Prompt）**：控制器公司标识符（Controller Company Id）

**说明（Help）**

设置将在 `VERSION_IND` PDU 中使用的蓝牙公司标识符（Bluetooth Company Identifier）。默认采用 `BT_COMPANY_ID`，芯片厂商和硬件制造商也可为控制器设置自己的公司标识符。完整列表见 [Bluetooth Company Identifiers](https://www.bluetooth.com/specifications/assigned-numbers/company-identifiers)。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_COMPANY_ID
```

**取值范围（Ranges）**

```text
[0x0000, 0xFFFF]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L170)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_COMPANY_ID`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_COMPANY_ID)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CONN_INTERVAL_LOW_LATENCY"></a>

## 322.37 `CONFIG_BT_CTLR_CONN_INTERVAL_LOW_LATENCY`

**提示（Prompt）**：允许低延迟连接间隔（Allow low latency connection intervals）

**说明（Help）**

允许低延迟连接间隔（low latency connection intervals）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1192)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CONN_ISO_AVOID_SEGMENTATION"></a>

## 322.38 `CONFIG_BT_CTLR_CONN_ISO_AVOID_SEGMENTATION`

**提示（Prompt）**：避免成帧模式下的 SDU 分片（Avoid SDU fragmentation for framed mode）

**说明（Help）**

创建连接等时组（CIG）时，`Max_PDU` 大小按照蓝牙核心规范 5.4（BT Core 5.4）Vol 6, Part G, Section 2.2 计算。然而，助听器配置文件（HAP）要求将 `Max_PDU` 强制设为合适的值来避免分段（segmentation）。由于非测试接口无法控制 `Max_PDU`，此配置提供一种方式，将 `Max_PDU` 强制设为 `Max_SDU + 5`，其中增加的部分为头和偏移（header + offset）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CENTRAL_ISO && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:314`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L314)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CENTRAL_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CENTRAL_ISO)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CONN_ISO_GROUPS"></a>

## 322.39 `CONFIG_BT_CTLR_CONN_ISO_GROUPS`

**提示（Prompt）**：低功耗蓝牙连接等时组（LE Connected Isochronous Groups）

**说明（Help）**

支持的连接等时组（CIGs）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CONN_ISO && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ISO_MAX_CIG
```

**取值范围（Ranges）**

```text
[1, 240]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1072`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1072)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_MAX_CIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_MAX_CIG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CONN_ISO_HCI_DATAPATH_SKIP_INVALID_DATA"></a>

## 322.40 `CONFIG_BT_CTLR_CONN_ISO_HCI_DATAPATH_SKIP_INVALID_DATA`

**提示（Prompt）**：不在 HCI 数据路径上传递无效 SDU（Do not pass invalid SDUs on HCI datapath）

**说明（Help）**

此选项允许应用决定是否通过 HCI 向上传递无效的服务数据单元（invalid SDUs）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CONN_ISO && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L307)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CONN_ISO_LOW_LATENCY_POLICY"></a>

## 322.41 `CONFIG_BT_CTLR_CONN_ISO_LOW_LATENCY_POLICY`

**提示（Prompt）**：低延迟 CIS 创建策略（CIS creation policy for low latency）

**说明（Help）**

选择此项以采用低延迟策略（low latency policy）创建 CIS。该策略优先采用紧凑安排有效载荷传输的 CIS 布局／配置（layout/configuration），尽可能降低延迟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CENTRAL_ISO && <choice CONFIG_BT_CTLR_CONN_ISO_POLICY_CHOICE>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:338`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L338)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → CIS 创建策略选择（CIS Creation Policy Selection）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CENTRAL_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CENTRAL_ISO)、[`CONFIG_BT_CTLR_CONN_ISO_POLICY_CHOICE`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CONN_ISO_POLICY_CHOICE)。

<a id="CONFIG_BT_CTLR_CONN_ISO_PDU_LEN_MAX"></a>

## 322.42 `CONFIG_BT_CTLR_CONN_ISO_PDU_LEN_MAX`

**提示（Prompt）**：连接等时信道 PDU 最大长度（Maximum Connected Isochronous Channel PDU Length）

**说明（Help）**

连接等时信道（Connected Isochronous Channel）协议数据单元（PDU）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CONN_ISO && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
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

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1088`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1088)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CONN_ISO_POLICY_CHOICE"></a>

## 322.43 `CONFIG_BT_CTLR_CONN_ISO_POLICY_CHOICE`

**提示（Prompt）**：CIS 创建策略选择（CIS Creation Policy Selection）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CTLR_CONN_ISO_RELIABILITY_POLICY
```

**可选项（Choices）**

```text
CONFIG_BT_CTLR_CONN_ISO_RELIABILITY_POLICY
CONFIG_BT_CTLR_CONN_ISO_LOW_LATENCY_POLICY
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:325`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L325)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_CONN_ISO_RELIABILITY_POLICY`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CONN_ISO_RELIABILITY_POLICY)、[`CONFIG_BT_CTLR_CONN_ISO_LOW_LATENCY_POLICY`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CONN_ISO_LOW_LATENCY_POLICY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CONN_ISO_RELIABILITY_POLICY"></a>

## 322.44 `CONFIG_BT_CTLR_CONN_ISO_RELIABILITY_POLICY`

**提示（Prompt）**：可靠性 CIS 创建策略（CIS creation policy for reliability）

**说明（Help）**

选择此项以采用可靠性策略（reliability policy）创建 CIS。该策略优先采用利用整个 `Max_Transmission_Latency` 范围的 CIS 布局／配置，以最大限度进行重传（retransmission）和有效载荷恢复（payload recovery）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CENTRAL_ISO && <choice CONFIG_BT_CTLR_CONN_ISO_POLICY_CHOICE>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:329`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L329)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → CIS 创建策略选择（CIS Creation Policy Selection）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CENTRAL_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CENTRAL_ISO)、[`CONFIG_BT_CTLR_CONN_ISO_POLICY_CHOICE`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CONN_ISO_POLICY_CHOICE)。

<a id="CONFIG_BT_CTLR_CONN_ISO_STREAMS"></a>

## 322.45 `CONFIG_BT_CTLR_CONN_ISO_STREAMS`

**提示（Prompt）**：低功耗蓝牙连接等时流（LE Connected Isochronous Streams）

**说明（Help）**

支持的连接等时流（CISes）最大总数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CONN_ISO && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ISO_MAX_CHAN
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1064`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1064)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_MAX_CHAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_MAX_CHAN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CONN_ISO_STREAMS_MAX_FT"></a>

## 322.46 `CONFIG_BT_CTLR_CONN_ISO_STREAMS_MAX_FT`

**提示（Prompt）**：低功耗蓝牙连接等时流最大刷新超时（LE Connected Isochronous Streams max flush timeout）

**说明（Help）**

连接等时流（CIS）刷新超时事件（flush timeout events）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CONN_ISO && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
255
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1113)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CONN_ISO_STREAMS_MAX_NSE"></a>

## 322.47 `CONFIG_BT_CTLR_CONN_ISO_STREAMS_MAX_NSE`

**提示（Prompt）**：低功耗蓝牙连接等时流最大子事件数（max number of subevents）

**说明（Help）**

连接等时流（CIS）子事件（subevents）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CONN_ISO && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
31
```

**取值范围（Ranges）**

```text
[1, 31]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CONN_ISO_STREAMS_PER_GROUP"></a>

## 322.48 `CONFIG_BT_CTLR_CONN_ISO_STREAMS_PER_GROUP`

**提示（Prompt）**：每组低功耗蓝牙连接等时流数量（LE Connected Isochronous Streams per Group）

**说明（Help）**

每个连接等时组（CIG）支持的连接等时流（CISes）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CONN_ISO && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 31]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1080`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1080)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CONN_META"></a>

## 322.49 `CONFIG_BT_CTLR_CONN_META`

**提示（Prompt）**：连接元数据扩展（Connection meta data extension）

**说明（Help）**

启用厂商专用的逐连接元数据（vendor specific per-connection meta data），将其作为下层链路层（LLL）连接对象的一部分。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:950`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L950)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CONN_PARAM_REQ"></a>

## 322.50 `CONFIG_BT_CTLR_CONN_PARAM_REQ`

**提示（Prompt）**：连接参数请求（Connection Parameter Request）

**说明（Help）**

在控制器（Controller）中启用蓝牙 v4.1 连接参数请求（Connection Parameter Request）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CONN_PARAM_REQ_SUPPORT && CONFIG_BT_CONN && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_EXT_REJ_IND
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:570`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L570)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CONN_PARAM_REQ_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_PARAM_REQ_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_EXT_REJ_IND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_EXT_REJ_IND)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_PARAM_REQ_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CONN_RANDOM_FORCE"></a>

## 322.51 `CONFIG_BT_CTLR_CONN_RANDOM_FORCE`

**提示（Prompt）**：外设错过锚点时进行随机强制调度（Random forced scheduling on missed anchor point）

**说明（Help）**

启用后，控制器采用传统行为：外设角色（peripheral role）错过锚点（anchor point）时，在下一次 ticker 调度中随机强制其获得优先权。

当设备有两个或更多间隔相近的连接，且其对端设备也有两个或更多相同间隔的连接时，调度可能锁定为一种轮转模式（round robin pattern），使两端的中心设备事件和外设事件都无法同步。加入随机性可打破这一固定轮转模式，使锚点能够同步（anchor point sync）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PERIPHERAL && CONFIG_BT_MAX_CONN > 1 && CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1160`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1160)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_MAX_CONN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAX_CONN)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CONN_RSSI"></a>

## 322.52 `CONFIG_BT_CTLR_CONN_RSSI`

**提示（Prompt）**：连接 RSSI（Connection RSSI）

**说明（Help）**

启用连接接收信号强度指示（RSSI）测量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CONN_RSSI_SUPPORT && CONFIG_BT_CONN && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HCI_RAW
```

**被选择（Selected by）**

```text
CONFIG_BT_CTLR_DF_CTE_RX
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:643`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L643)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CONN_RSSI_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_RSSI_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)、[`CONFIG_BT_CTLR_DF_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CTE_RX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CONN_RSSI_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CONN_RSSI_EVENT"></a>

## 322.53 `CONFIG_BT_CTLR_CONN_RSSI_EVENT`

**提示（Prompt）**：连接 RSSI 事件（Connection RSSI event）

**说明（Help）**

为连接接收信号强度指示（RSSI）测量生成事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CONN_RSSI && CONFIG_BT_CONN && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1174)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CONN_RSSI`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CONN_RSSI)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_CRYPTO"></a>

## 322.54 `CONFIG_BT_CTLR_CRYPTO`

**提示（Prompt）**：控制器中的密码功能（Crypto functions in Controller）

**说明（Help）**

使用控制器提供的随机数生成（random number generation）和 AES 加密（AES encryption）支持函数。原文指出，蓝牙核心规范要求支持 HCI `LE Rand` 和 HCI `LE Encrypt` 命令。

在通过 HCI 传输将应用／主机与控制器分离的构建中，或针对单 CPU SoC 的合并构建中，应用可使用自己符合 FIPS-197 的密码实现（cryptographic implementations）。此时可禁用控制器的密码实现，以节省 Flash 和 RAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_CRYPTO_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_CRYPTO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CRYPTO_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_CRYPTO_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DATA_LENGTH_CLEAR"></a>

## 322.55 `CONFIG_BT_CTLR_DATA_LENGTH_CLEAR`

**提示（Prompt）**：数据长度支持，仅限明文（Data Length Support, Cleartext only）

**说明（Help）**

在控制器中启用蓝牙 v4.2 低功耗蓝牙数据长度更新过程（LE Data Length Update procedure）支持，明文有效载荷（cleartext payloads）最大可达 `251` 字节。不支持加密连接（encrypted connections）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF51 && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:384`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L384)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DATA_LENGTH_MAX"></a>

## 322.56 `CONFIG_BT_CTLR_DATA_LENGTH_MAX`

**提示（Prompt）**：支持的最大数据长度（Maximum data length supported）

**说明（Help）**

设置控制器（Controller）支持的协议数据单元（PDU）最大数据长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DATA_LENGTH && CONFIG_BT_CONN && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BUF_ACL_RX_SIZE if CONFIG_BT_BUF_ACL_RX_SIZE <= 251
27
```

**取值范围（Ranges）**

```text
[27, CONFIG_BT_BUF_ACL_RX_SIZE] if CONFIG_BT_BUF_ACL_RX_SIZE < 251
[27, 251]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:609`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L609)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DATA_LENGTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DATA_LENGTH)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BUF_ACL_RX_SIZE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BUF_ACL_RX_SIZE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_DATA_LENGTH`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DEBUG_PINS"></a>

## 322.57 `CONFIG_BT_CTLR_DEBUG_PINS`

**提示（Prompt）**：蓝牙控制器调试引脚（Bluetooth Controller Debug Pins）

**说明（Help）**

为低功耗蓝牙控制器（Bluetooth LE Controller）启用调试 GPIO 翻转（toggling）。使用逻辑分析仪（logic analyzer）进行调试，或分析某些代码段的性能时，此功能很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(BOARD_NRF51DK_NRF51822 || BOARD_NRF52DK_NRF52832 || BOARD_NRF52DK_NRF52810 || BOARD_NRF52840DK_NRF52840 || BOARD_NRF52833DK_NRF52833 || BOARD_NRF5340DK_NRF5340_CPUNET || CONFIG_BOARD_RV32M1_VEGA) && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1470`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1470)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_RV32M1_VEGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RV32M1_VEGA)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RV32M1_VEGA`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DEBUG_PINS_CPUAPP"></a>

## 322.58 `CONFIG_BT_CTLR_DEBUG_PINS_CPUAPP`

**提示（Prompt）**：蓝牙控制器调试引脚（Bluetooth Controller Debug Pins）

**说明（Help）**

为蓝牙控制器调试 GPIO 翻转配置信号路由（route）。当协处理器（co-processor）使用蓝牙控制器调试引脚，而主处理器需要设置和／或路由这些信号时，启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
BOARD_NRF5340DK_NRF5340_CPUAPP && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:1251`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L1251)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_CTLR_DF"></a>

## 322.59 `CONFIG_BT_CTLR_DF`

**提示（Prompt）**：低功耗蓝牙测向（LE Direction Finding）

**说明（Help）**

启用蓝牙 5.1 测向（Direction Finding）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT || CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT) && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT)、[`CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT`、`CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_ADV_CTE_TX"></a>

## 322.60 `CONFIG_BT_CTLR_DF_ADV_CTE_TX`

**提示（Prompt）**：无连接 CTE 发送器功能（Connectionless CTE Transmitter feature）

**说明（Help）**

在控制器中启用蓝牙 v5.1 无连接恒定音调扩展发送器（Connectionless CTE Transmitter）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_CTE_TX && CONFIG_BT_CTLR_ADV_PERIODIC && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_ADV_EXT_PDU_EXTRA_DATA_MEMORY if CONFIG_BT_LL_SW_SPLIT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_CTE_TX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CTE_TX)、[`CONFIG_BT_CTLR_ADV_PERIODIC`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_PERIODIC)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_ADV_EXT_PDU_EXTRA_DATA_MEMORY`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT_PDU_EXTRA_DATA_MEMORY)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_ANT_SWITCH_1US"></a>

## 322.61 `CONFIG_BT_CTLR_DF_ANT_SWITCH_1US`

**提示（Prompt）**：1us 天线切换时隙支持（1us antenna switch slots）

**说明（Help）**

启用 `1us` 天线切换时隙（antenna switching slots）支持。根据蓝牙 v5.1，该天线切换模式是测向（Direction Finding）的可选模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_ANT_SWITCH_1US_SUPPORT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_ANT_SWITCH_1US_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_ANT_SWITCH_1US_SUPPORT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_DF_ANT_SWITCH_1US_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_ANT_SWITCH_RX"></a>

## 322.62 `CONFIG_BT_CTLR_DF_ANT_SWITCH_RX`

**提示（Prompt）**：CTE 接收期间的天线切换功能，AoA（antenna switching during CTE reception）

**说明（Help）**

启用接收恒定音调扩展（CTE）期间的天线切换（antenna switching）支持，也称为到达角模式（Angle of Arrival，AoA）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_CTE_RX && CONFIG_BT_CTLR_DF_ANT_SWITCH_2US_SUPPORT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CTE_RX)、[`CONFIG_BT_CTLR_DF_ANT_SWITCH_2US_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_ANT_SWITCH_2US_SUPPORT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_DF_ANT_SWITCH_2US_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_ANT_SWITCH_TX"></a>

## 322.63 `CONFIG_BT_CTLR_DF_ANT_SWITCH_TX`

**提示（Prompt）**：CTE 发送期间的天线切换功能，AoD（antenna switching during CTE transmission）

**说明（Help）**

启用发送恒定音调扩展（CTE）期间的天线切换（antenna switching）支持，也称为出发角模式（Angle of Departure，AoD）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_CTE_TX && CONFIG_BT_CTLR_DF_ANT_SWITCH_2US_SUPPORT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_CTE_TX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CTE_TX)、[`CONFIG_BT_CTLR_DF_ANT_SWITCH_2US_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_ANT_SWITCH_2US_SUPPORT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_DF_ANT_SWITCH_2US_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_CONN_CTE_REQ"></a>

## 322.64 `CONFIG_BT_CTLR_DF_CONN_CTE_REQ`

**提示（Prompt）**：连接 CTE 请求功能（Connection CTE Request feature）

**说明（Help）**

在控制器中启用蓝牙 v5.1 连接 CTE 请求（Connection CTE Request）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_CONN_CTE_RX && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_CONN_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CONN_CTE_RX)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_CONN_CTE_RSP"></a>

## 322.65 `CONFIG_BT_CTLR_DF_CONN_CTE_RSP`

**提示（Prompt）**：连接 CTE 响应功能（Connection CTE Response feature）

**说明（Help）**

在控制器中启用蓝牙 v5.1 连接 CTE 响应（Connection CTE Response）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_CONN_CTE_TX && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_CONN_CTE_TX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CONN_CTE_TX)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_CONN_CTE_RX"></a>

## 322.66 `CONFIG_BT_CTLR_DF_CONN_CTE_RX`

**提示（Prompt）**：基于连接的 CTE 接收器（Connection based CTE Receiver）

**说明（Help）**

在测向连接模式（direction finding connected mode）中启用恒定音调扩展（Constant Tone Extension，CTE）的接收与采样。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_CTE_RX && CONFIG_BT_CONN && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CTE_RX)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_CONN_CTE_TX"></a>

## 322.67 `CONFIG_BT_CTLR_DF_CONN_CTE_TX`

**提示（Prompt）**：基于连接的 CTE 发送器（Connection based CTE Transmitter）

**说明（Help）**

在测向连接模式（direction finding connected mode）中启用恒定音调扩展（Constant Tone Extension，CTE）的发送。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_CTE_TX && CONFIG_BT_CONN && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_CTE_TX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CTE_TX)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_CTE_RX"></a>

## 322.68 `CONFIG_BT_CTLR_DF_CTE_RX`

**提示（Prompt）**：恒定音调扩展接收功能（Reception of Constant Tone Extension feature）

**说明（Help）**

在控制器中启用恒定音调扩展（Constant Tone Extension，CTE）接收支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_CONN_RSSI if CONFIG_BT_CONN
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_CONN_RSSI`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CONN_RSSI)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_CTE_RX_SAMPLE_1US"></a>

## 322.69 `CONFIG_BT_CTLR_DF_CTE_RX_SAMPLE_1US`

**提示（Prompt）**：使用 1us 采样时隙接收 CTE（Reception of CTE with 1us sampling slots）

**说明（Help）**

启用恒定音调扩展（Constant Tone Extension，CTE）接收，在接收期间使用 `1us` 采样时隙（sampling slots）进行 IQ 采样。根据蓝牙 v5.1，该采样模式是测向（Direction Finding）的可选模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_CTE_RX_SAMPLE_1US_SUPPORT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_CTE_RX_SAMPLE_1US_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_CTE_RX_SAMPLE_1US_SUPPORT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_DF_CTE_RX_SAMPLE_1US_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_CTE_TX"></a>

## 322.70 `CONFIG_BT_CTLR_DF_CTE_TX`

**提示（Prompt）**：发送恒定音调扩展（Transmission of Constant Tone Extension）

**说明（Help）**

在控制器中启用恒定音调扩展（Constant Tone Extension，CTE）发送支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_DEBUG_ENABLE"></a>

## 322.71 `CONFIG_BT_CTLR_DF_DEBUG_ENABLE`

**提示（Prompt）**：启用蓝牙测向调试支持（Bluetooth Direction Finding debug support enable）

**说明（Help）**

此选项为控制器中的测向实现（Direction Finding implementation）启用调试支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:256`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L256)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_INIT_ANT_SEL_GPIOS"></a>

## 322.72 `CONFIG_BT_CTLR_DF_INIT_ANT_SEL_GPIOS`

**提示（Prompt）**：初始化负责天线切换的 GPIO（Initialization of GPIOs responsible for antenna switching）

**说明（Help）**

允许在无线电（Radio）初始化期间隐式初始化负责天线切换（antenna switching）的 GPIO。如果未启用此功能，无线电初始化过程不会初始化选用于驱动天线切换的 GPIO 引脚；此时应用负责正确初始化这些 GPIO。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_DF_ANT_SWITCH_TX || CONFIG_BT_CTLR_DF_ANT_SWITCH_RX) && CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_ANT_SWITCH_TX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_ANT_SWITCH_TX)、[`CONFIG_BT_CTLR_DF_ANT_SWITCH_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_ANT_SWITCH_RX)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_IQ_SAMPLES_CONVERT_2_BITS_SHIFT"></a>

## 322.73 `CONFIG_BT_CTLR_DF_IQ_SAMPLES_CONVERT_2_BITS_SHIFT`

**提示（Prompt）**：通过右移 2 位将 IQ 样本转换为 8 位宽（Conversion by 2 bits shift）

**说明（Help）**

无线电测向扩展（Radio Direction Finding Extension）提供的 IQ 样本宽度为 `12` 位。蓝牙 5.3 核心规范（Core Specification）Vol 4, Part E 的 7.7.65.21 和 7.7.65.22 节规定 IQ 样本宽度为 `8` 位。此配置启用转换：执行普通右移 `2` 位操作，再强制转换为 `int8_t`，将 12 位 IQ 样本变为 8 位。这会损失精度。只有确认样本不会饱和（saturate）时，才可使用此转换方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_DF_SCAN_CTE_RX || CONFIG_BT_CTLR_DF_CONN_CTE_RX) && <choice>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:287`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L287)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding） → IQ 样本从 12 位到 8 位的转换方式（IQ samples 12 bit to 8 bit conversion approach）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_SCAN_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_SCAN_CTE_RX)、[`CONFIG_BT_CTLR_DF_CONN_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CONN_CTE_RX)。

<a id="CONFIG_BT_CTLR_DF_IQ_SAMPLES_CONVERT_4_BITS_SHIFT"></a>

## 322.74 `CONFIG_BT_CTLR_DF_IQ_SAMPLES_CONVERT_4_BITS_SHIFT`

**提示（Prompt）**：通过右移 4 位将 IQ 样本转换为 8 位宽（Conversion by 4 bits shift）

**说明（Help）**

无线电测向扩展（Radio Direction Finding Extension）提供的 IQ 样本宽度为 `12` 位。蓝牙 5.3 核心规范（Core Specification）Vol 4, Part E 的 7.7.65.21 和 7.7.65.22 节规定 IQ 样本宽度为 `8` 位。此配置通过普通右移 `4` 位操作，将 12 位 IQ 样本转换为 8 位。由于仅使用最高有效的 8 位（8 MSB），会损失精度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_DF_SCAN_CTE_RX || CONFIG_BT_CTLR_DF_CONN_CTE_RX) && <choice>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:277`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L277)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding） → IQ 样本从 12 位到 8 位的转换方式（IQ samples 12 bit to 8 bit conversion approach）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_SCAN_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_SCAN_CTE_RX)、[`CONFIG_BT_CTLR_DF_CONN_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CONN_CTE_RX)。

<a id="CONFIG_BT_CTLR_DF_IQ_SAMPLES_CONVERT_USE_8_LSB"></a>

## 322.75 `CONFIG_BT_CTLR_DF_IQ_SAMPLES_CONVERT_USE_8_LSB`

**提示（Prompt）**：使用最低有效的 8 位将 IQ 样本转换为 8 位宽（Conversion by use of 8 LSB）

**说明（Help）**

无线电测向扩展（Radio Direction Finding Extension）提供的 IQ 样本宽度为 `12` 位。蓝牙 5.3 核心规范（Core Specification）Vol 4, Part E 的 7.7.65.21 和 7.7.65.22 节规定 IQ 样本宽度为 `8` 位。此配置保留最低有效的 8 位（8 least significant bits），将 12 位 IQ 样本转换为 8 位。只有确认实际样本的数值不超过 8 位表示范围时才可使用该方式，这可避免移位操作造成额外的精度损失。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF5340_CPUNET && (CONFIG_BT_CTLR_DF_SCAN_CTE_RX || CONFIG_BT_CTLR_DF_CONN_CTE_RX) && <choice>
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:298`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L298)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding） → IQ 样本从 12 位到 8 位的转换方式（IQ samples 12 bit to 8 bit conversion approach）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF5340_CPUNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUNET)、[`CONFIG_BT_CTLR_DF_SCAN_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_SCAN_CTE_RX)、[`CONFIG_BT_CTLR_DF_CONN_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CONN_CTE_RX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUNET`。

<a id="CONFIG_BT_CTLR_DF_MAX_ANT_SW_PATTERN_LEN"></a>

## 322.76 `CONFIG_BT_CTLR_DF_MAX_ANT_SW_PATTERN_LEN`

**提示（Prompt）**：天线切换模式最大长度（Maximum length of antenna switch pattern）

**说明（Help）**

定义控制器能够存储的天线切换模式（antenna switch pattern）最大长度。基于 nRF5x 的控制器受硬件限制，取值范围为 `2` 到 `38`，最大值为 `38`。对于通用场景，蓝牙核心规范 5.1（Bluetooth Core 5.1）要求该值位于 `2` 到 `75` 之间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
12
```

**取值范围（Ranges）**

```text
[2, 38] if CONFIG_SOC_COMPATIBLE_NRF
[2, 75] if !CONFIG_SOC_COMPATIBLE_NRF
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_SOC_COMPATIBLE_NRF`。

<a id="CONFIG_BT_CTLR_DF_PER_ADV_CTE_NUM_MAX"></a>

## 322.77 `CONFIG_BT_CTLR_DF_PER_ADV_CTE_NUM_MAX`

**提示（Prompt）**：无连接模式下发送的带恒定音调扩展 PDU 最大数量（transmitted PDUs with Constant Tone Extension）

**说明（Help）**

在单个周期性广播链（periodic advertising chain）中，支持发送的带恒定音调扩展（Constant Tone Extension）的 PDU 最大数量。范围取自 BT Core spec 5.1, Vol 4 Part E section 7.8.82 中 `HCI_LE_Set_Connectionless_IQ_Sampling_Enable` 的 `Max_Sampled_CTEs` 参数。

译注：本条说明发送数量，但原文引用的是接收采样使能命令；此处保留原始引用，不替换为推测的章节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_ADV_CTE_TX && CONFIG_BT_CTLR_ADV_PDU_LINK && CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_ADV_CTE_TX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_ADV_CTE_TX)、[`CONFIG_BT_CTLR_ADV_PDU_LINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_PDU_LINK)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_ADV_PDU_LINK`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_PER_SCAN_CTE_NUM_MAX"></a>

## 322.78 `CONFIG_BT_CTLR_DF_PER_SCAN_CTE_NUM_MAX`

**提示（Prompt）**：无连接模式下接收的带恒定音调扩展 PDU 最大数量（received PDUs with Constant Tone Extension）

**说明（Help）**

在单个周期性广播链（periodic advertising chain）中，支持接收的带恒定音调扩展（Constant Tone Extension）的 PDU 最大数量。范围取自 BT Core spec 5.1, Vol 4 Part E section 7.8.82 中 `HCI_LE_Set_Connectionless_IQ_Sampling_Enable` 的 `Max_Sampled_CTEs` 参数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_SCAN_CTE_RX && CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:191`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L191)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_SCAN_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_SCAN_CTE_RX)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_PHYEND_OFFSET_COMPENSATION_ENABLE"></a>

## 322.79 `CONFIG_BT_CTLR_DF_PHYEND_OFFSET_COMPENSATION_ENABLE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在 nRF52811、nRF52820、nRF52833、nRF5340 SoC 上，如果启用了 `CTEINLINECTRLEN`，且收到的 PDU 不含 `CTEInfo` 字段，生成 `PHYEND` 事件会出现延迟。此选项启用针对该延迟的变通处理（workaround），维持连接事件的帧间间隔（inter frame spacing，IFS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_CTE_RX && CONFIG_BT_CONN && (CONFIG_SOC_NRF52811 || CONFIG_SOC_NRF52820 || CONFIG_SOC_NRF52833 || CONFIG_SOC_NRF5340_CPUNET) && CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:262`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L262)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CTE_RX)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_SOC_NRF52811`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52811)、[`CONFIG_SOC_NRF52820`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52820)、[`CONFIG_SOC_NRF52833`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52833)、[`CONFIG_SOC_NRF5340_CPUNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUNET)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF52811`、`CONFIG_SOC_NRF52820`、`CONFIG_SOC_NRF52833`、`CONFIG_SOC_NRF5340_CPUNET`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_SAMPLE_CTE_FOR_PDU_WITH_BAD_CRC"></a>

## 322.80 `CONFIG_BT_CTLR_DF_SAMPLE_CTE_FOR_PDU_WITH_BAD_CRC`

**提示（Prompt）**：对 CRC 错误的 PDU 进行 CTE 采样（Sampling of CTE for PDUs with bad CRC）

**说明（Help）**

允许对循环冗余校验（CRC）错误的 PDU 进行恒定音调扩展（CTE）采样。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_SCAN_CTE_RX && CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_SCAN_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_SCAN_CTE_RX)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_SAMPLE_OFFSET_PHY_1M_SAMPLING_1US"></a>

## 322.81 `CONFIG_BT_CTLR_DF_SAMPLE_OFFSET_PHY_1M_SAMPLING_1US`

**提示（Prompt）**：PHY 1M、1US 样本间距的 CTE 相对采样偏移（CTE sampling offset relative）

**说明（Help）**

采样开始时间相对于采样时隙（sampling slot）起点的偏移，用 16M 时钟周期数表示，是有符号相对值。在 PHY 设为 `PHY 1M` 且采样时隙持续时间为 `1 us` 时使用。将偏移减小到 AoA/AoD 过程触发时刻之前不会再产生效果。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_COMPATIBLE_NRF && CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[-2048, 2047]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_SAMPLE_OFFSET_PHY_1M_SAMPLING_2US"></a>

## 322.82 `CONFIG_BT_CTLR_DF_SAMPLE_OFFSET_PHY_1M_SAMPLING_2US`

**提示（Prompt）**：PHY 1M、2US 样本间距的 CTE 相对采样偏移（CTE sampling offset relative）

**说明（Help）**

采样开始时间相对于采样时隙（sampling slot）起点的偏移，用 16M 时钟周期数表示，是有符号相对值。在 PHY 设为 `PHY 1M` 且采样时隙持续时间为 `2 us` 时使用。将偏移减小到 AoA/AoD 过程触发时刻之前不会再产生效果。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_COMPATIBLE_NRF && CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
6
```

**取值范围（Ranges）**

```text
[-2048, 2047]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:234`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L234)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_SAMPLE_OFFSET_PHY_2M_SAMPLING_1US"></a>

## 322.83 `CONFIG_BT_CTLR_DF_SAMPLE_OFFSET_PHY_2M_SAMPLING_1US`

**提示（Prompt）**：PHY 1M、1US 样本间距的 CTE 相对采样偏移（CTE sampling offset relative）

**说明（Help）**

采样开始时间相对于采样时隙（sampling slot）起点的偏移，用 16M 时钟周期数表示，是有符号相对值。在 PHY 设为 `PHY 1M` 且采样时隙持续时间为 `1 us` 时使用。将偏移减小到 AoA/AoD 过程触发时刻之前不会再产生效果。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_COMPATIBLE_NRF && CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
15
```

**取值范围（Ranges）**

```text
[-2048, 2047]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_SAMPLE_OFFSET_PHY_2M_SAMPLING_2US"></a>

## 322.84 `CONFIG_BT_CTLR_DF_SAMPLE_OFFSET_PHY_2M_SAMPLING_2US`

**提示（Prompt）**：PHY 1M、2US 样本间距的 CTE 相对采样偏移（CTE sampling offset relative）

**说明（Help）**

采样开始时间相对于采样时隙（sampling slot）起点的偏移，用 16M 时钟周期数表示，是有符号相对值。在 PHY 设为 `PHY 1M` 且采样时隙持续时间为 `2 us` 时使用。将偏移减小到 AoA/AoD 过程触发时刻之前不会再产生效果。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_COMPATIBLE_NRF && CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[-2048, 2047]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:245`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L245)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_SCAN_CTE_RX"></a>

## 322.85 `CONFIG_BT_CTLR_DF_SCAN_CTE_RX`

**提示（Prompt）**：无连接 CTE 接收器（Connectionless CTE Receiver）

**说明（Help）**

在控制器中启用蓝牙 v5.1 无连接 CTE 接收（connectionless CTE reception）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_CTE_RX && CONFIG_BT_CTLR_SYNC_PERIODIC && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CTE_RX)、[`CONFIG_BT_CTLR_SYNC_PERIODIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_PERIODIC)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_SWITCH_OFFSET"></a>

## 322.86 `CONFIG_BT_CTLR_DF_SWITCH_OFFSET`

**提示（Prompt）**：天线切换相对于 CRC 结束的偏移（Antenna switch offset relative to end of CRC）

**说明（Help）**

CRC 结束后开始天线切换（antenna switching）的偏移，用 16M 时钟周期数表示，是有符号值。将偏移减小到 AoA/AoD 过程触发时刻之前不会再产生效果。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_COMPATIBLE_NRF && CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[-2048, 2047]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:201`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L201)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_VS_CL_IQ_REPORT_16_BITS_IQ_SAMPLES"></a>

## 322.87 `CONFIG_BT_CTLR_DF_VS_CL_IQ_REPORT_16_BITS_IQ_SAMPLES`

**提示（Prompt）**：在无连接 IQ 报告中使用 16 位有符号整数 IQ 样本（16 bits signed integer IQ samples）

**说明（Help）**

测向（Direction Finding）的无连接 IQ 报告（connectionless IQ reports）提供一组在 CTE 采样期间采集的 IQ 样本。蓝牙 5.3 核心规范将 IQ 样本定义为 8 位有符号整数，参见 Vol 4, Part E section 7.7.65.21。此选项启用 HCI 层的厂商专用扩展（vendor specific extension），使无连接 IQ 报告以 16 位有符号整数格式保存样本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_SCAN_CTE_RX && CONFIG_BT_HCI_VS && CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:313`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L313)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_SCAN_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_SCAN_CTE_RX)、[`CONFIG_BT_HCI_VS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_VS)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DF_VS_CONN_IQ_REPORT_16_BITS_IQ_SAMPLES"></a>

## 322.88 `CONFIG_BT_CTLR_DF_VS_CONN_IQ_REPORT_16_BITS_IQ_SAMPLES`

**提示（Prompt）**：在连接 IQ 报告中使用 16 位有符号整数 IQ 样本（16 bits signed integer IQ samples）

**说明（Help）**

测向（Direction Finding）的连接 IQ 报告（connection IQ reports）提供一组在 CTE 采样期间采集的 IQ 样本。蓝牙 5.3 核心规范将 IQ 样本定义为 8 位有符号整数，参见 Vol 4, Part E section 7.7.65.22。此选项启用 HCI 层的厂商专用扩展（vendor specific extension），使连接 IQ 报告以 16 位有符号整数格式保存样本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_CONN_CTE_RX && CONFIG_BT_HCI_VS && CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_CTLR_DF && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.df:323`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.df#L323)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 低功耗蓝牙测向（LE Direction Finding）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_CONN_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CONN_CTE_RX)、[`CONFIG_BT_HCI_VS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_VS)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_CTLR_DF`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DTM"></a>

## 322.89 `CONFIG_BT_CTLR_DTM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在控制器（Controller）中启用直接测试模式（Direct Test Mode，DTM）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_CTLR_DTM_HCI
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.dtm:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.dtm#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_DTM_HCI`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DTM_HCI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DTM_HCI"></a>

## 322.90 `CONFIG_BT_CTLR_DTM_HCI`

**提示（Prompt）**：基于 HCI 的直接测试模式（Direct Test Mode over HCI）

**说明（Help）**

启用通过 HCI 传输进行的直接测试模式（Direct Test Mode）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DTM_HCI_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_DTM
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.dtm:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.dtm#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DTM_HCI_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DTM_HCI_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_DTM`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DTM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_DTM_HCI_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DTM_HCI_DF_IQ_REPORT"></a>

## 322.91 `CONFIG_BT_CTLR_DTM_HCI_DF_IQ_REPORT`

**提示（Prompt）**：无连接 IQ 报告 HCI 事件（Connectionless IQ report HCI event）[实验性，EXPERIMENTAL]

**说明（Help）**

允许在恒定音调扩展（Constant Tone Extension）接收之后生成 HCI `LE Connectionless IQ Report` 事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DF_CTE_RX && CONFIG_BT_CTLR_DTM_HCI_RX_V3 && CONFIG_BT_CTLR_DTM_HCI && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.dtm:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.dtm#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 基于 HCI 的直接测试模式（Direct Test Mode over HCI）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DF_CTE_RX`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DF_CTE_RX)、[`CONFIG_BT_CTLR_DTM_HCI_RX_V3`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DTM_HCI_RX_V3)、[`CONFIG_BT_CTLR_DTM_HCI`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DTM_HCI)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DTM_HCI_DF_IQ_REPORT_NUM_MAX"></a>

## 322.92 `CONFIG_BT_CTLR_DTM_HCI_DF_IQ_REPORT_NUM_MAX`

**提示（Prompt）**：IQ 报告池大小（IQ Report pool size）

**说明（Help）**

池中直接测试模式 IQ 报告（DTM IQ Reports）的最大数量，取决于上层测试器（upper tester）的测试数据包发送间隔。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DTM_HCI_DF_IQ_REPORT && CONFIG_BT_CTLR_DTM_HCI && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.dtm:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.dtm#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 基于 HCI 的直接测试模式（Direct Test Mode over HCI） → 无连接 IQ 报告 HCI 事件（Connectionless IQ report HCI event）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DTM_HCI_DF_IQ_REPORT`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DTM_HCI_DF_IQ_REPORT)、[`CONFIG_BT_CTLR_DTM_HCI`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DTM_HCI)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DTM_HCI_RX_V3"></a>

## 322.93 `CONFIG_BT_CTLR_DTM_HCI_RX_V3`

**提示（Prompt）**：HCI LE Receiver Test v3（低功耗蓝牙接收器测试 v3）

**说明（Help）**

启用直接测试模式（DTM）接收器测试命令（Receiver test command）v3 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DTM_HCI && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.dtm:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.dtm#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 基于 HCI 的直接测试模式（Direct Test Mode over HCI）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DTM_HCI`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DTM_HCI)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DTM_HCI_TX_V3"></a>

## 322.94 `CONFIG_BT_CTLR_DTM_HCI_TX_V3`

**提示（Prompt）**：HCI LE Transmitter Test v3（低功耗蓝牙发送器测试 v3）

**说明（Help）**

启用直接测试模式（DTM）发送器测试命令（Transmitter test command）v3 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DTM_HCI && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.dtm:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.dtm#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 基于 HCI 的直接测试模式（Direct Test Mode over HCI）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DTM_HCI`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DTM_HCI)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DTM_HCI_TX_V4"></a>

## 322.95 `CONFIG_BT_CTLR_DTM_HCI_TX_V4`

**提示（Prompt）**：HCI LE Transmitter Test v4（低功耗蓝牙发送器测试 v4）

**说明（Help）**

启用直接测试模式（DTM）发送器测试命令（Transmitter test command）v4 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_DTM_HCI && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.dtm:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.dtm#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 基于 HCI 的直接测试模式（Direct Test Mode over HCI）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_DTM_HCI`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DTM_HCI)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DUP_FILTER_ADV_SET_MAX"></a>

## 322.96 `CONFIG_BT_CTLR_DUP_FILTER_ADV_SET_MAX`

**提示（Prompt）**：扫描重复过滤器中的扩展广播集合数量（Extended Advertising Sets in scan duplicate filter）

**说明（Help）**

设置扩展扫描（Extended Scanning）期间，每个低功耗蓝牙地址可用于重复过滤的唯一广播集合标识符（Advertising Set ID）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_CTLR_ADV_EXT && CONFIG_BT_CTLR_DUP_FILTER_LEN > 0 && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:230`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L230)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_CTLR_DUP_FILTER_LEN`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DUP_FILTER_LEN)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DUP_FILTER_LEN"></a>

## 322.97 `CONFIG_BT_CTLR_DUP_FILTER_LEN`

**提示（Prompt）**：扫描重复过滤器中的地址数量（addresses in scan duplicate filter）

**说明（Help）**

设置扫描（scanning）期间可用于重复过滤的唯一低功耗蓝牙地址（Bluetooth LE addresses）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_DYNAMIC_INTERRUPTS"></a>

## 322.98 `CONFIG_BT_CTLR_DYNAMIC_INTERRUPTS`

**提示（Prompt）**：仅使用动态中断分配（Use Dynamic Interrupts allocation only）

**说明（Help）**

动态分配控制器所需的全部中断（interrupts）。这可确保在控制器初始化时正确连接中断，而非只在系统启动时连接。因此，应用可在运行时启用控制器及其中断服务例程（ISR），并在未启用蓝牙时将 SoC 外设用于自定义用途。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DYNAMIC_INTERRUPTS && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:688`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L688)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ECDH"></a>

## 322.99 `CONFIG_BT_CTLR_ECDH`

**提示（Prompt）**：椭圆曲线 Diffie-Hellman（Elliptic Curve Diffie-Hellman，ECDH）

**说明（Help）**

在控制器中启用蓝牙 v4.2 椭圆曲线 Diffie-Hellman（ECDH）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ECDH_SUPPORT && CONFIG_BT_CONN && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HCI_RAW
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:562`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L562)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ECDH_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ECDH_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_ECDH_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ENTROPY"></a>

## 322.100 `CONFIG_BT_CTLR_ENTROPY`

**提示（Prompt）**：控制器中的随机数生成（Random number generation in Controller）

**说明（Help）**

使用控制器选择的随机数生成（random number generation）方式。原帮助文本指出，蓝牙核心规范要求使用符合 FIPS PUB 140-2 的随机数生成器。取消选择此选项后，控制器可使用其他熵生成器（entropy generators）；它们可能不是真随机数生成器（true random number generators），因此这种实现会成为实验性实现。控制器实现也可在没有任何 Zephyr 驱动支持时，提供自定义裸机随机数生成器（bare-metal random number generator），即没有启用 `ENTROPY_HAS_DRIVER`。

译注：这里忠实保留所译快照对规范与符合性的表述，不据此宣称具体实现已经通过认证。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_ENTROPY_SUPPORT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_GENERATOR
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ENTROPY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ENTROPY_SUPPORT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_ENTROPY_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<!-- kconfig-navigation -->

[上一章](P321_subsys_bluetooth_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P323_subsys_bluetooth_配置项参考_4.md)
