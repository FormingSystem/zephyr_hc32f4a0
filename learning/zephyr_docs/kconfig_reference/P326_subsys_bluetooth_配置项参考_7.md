---
id: learning.zephyr-docs.kconfig-reference.page-326
title: "`subsys/bluetooth`配置项参考（7/13）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第326章\_`subsys/bluetooth`配置项参考（7/13）

本章翻译官方 Kconfig 数据库中 `subsys/bluetooth` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_GATT_NOTIFY_MULTIPLE"></a>

## 326.1 `CONFIG_BT_GATT_NOTIFY_MULTIPLE`

**提示（Prompt）**：GATT 多特征值通知支持（GATT Notify Multiple Characteristic Values support）

**说明（Help）**

启用 GATT 多特征值通知过程（Notify Multiple Characteristic Values procedure）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_CACHING && CONFIG_BT_GATT_CACHING && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options） → GATT 服务变更支持（GATT Service Changed support） → GATT 缓存支持（GATT Caching support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_CACHING`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CACHING)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GATT_NOTIFY_MULTIPLE_FLUSH_MS"></a>

## 326.2 `CONFIG_BT_GATT_NOTIFY_MULTIPLE_FLUSH_MS`

**提示（Prompt）**：将多个通知批量合入单个 PDU 的延迟（batching multiple notifications）

**说明（Help）**

设置一个时间窗口，单位为毫秒；窗口内连续到来的 GATT 通知（notifications）会被尝试追加到一起，形成单个 `ATT_MULTIPLE_HANDLE_VALUE_NTF` PDU。设为 `0` 时禁用批量合并（batching）；此时只能通过 `bt_gatt_notify_multiple` 发送这种 PDU。详情参阅 `bt_gatt_notify()` 的文档。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_NOTIFY_MULTIPLE && CONFIG_BT_GATT_CACHING && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 4000]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options） → GATT 服务变更支持（GATT Service Changed support） → GATT 缓存支持（GATT Caching support） → GATT 多特征值通知支持（GATT Notify Multiple Characteristic Values support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_NOTIFY_MULTIPLE`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_GATT_NOTIFY_MULTIPLE)、[`CONFIG_BT_GATT_CACHING`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CACHING)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GATT_READ_MULTIPLE"></a>

## 326.3 `CONFIG_BT_GATT_READ_MULTIPLE`

**提示（Prompt）**：GATT 多特征值读取支持（GATT Read Multiple Characteristic Values support）

**说明（Help）**

启用 GATT 多特征值读取过程（Read Multiple Characteristic Values procedure）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:195`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L195)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GATT_READ_MULT_VAR_LEN"></a>

## 326.4 `CONFIG_BT_GATT_READ_MULT_VAR_LEN`

**提示（Prompt）**：GATT 多个可变长度特征值读取支持（GATT Read Multiple Variable Length Characteristic Values support）

**说明（Help）**

启用 GATT 多个可变长度特征值读取过程（Read Multiple Variable Length Characteristic Values procedure）支持。启用 EATT 时必须支持，否则可选；参见 Core spec v5.3, Vol 3, Part G, Section 4.2, Table 4.1。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_BT_EATT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_EATT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_EATT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GATT_SERVICE_CHANGED"></a>

## 326.5 `CONFIG_BT_GATT_SERVICE_CHANGED`

**提示（Prompt）**：GATT 服务变更支持（GATT Service Changed support）

**说明（Help）**

启用服务变更特征（Service Changed characteristic）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L114)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GMAP"></a>

## 326.6 `CONFIG_BT_GMAP`

**提示（Prompt）**：游戏音频配置文件（Gaming Audio Profile）

**说明（Help）**

启用后将启用游戏音频配置文件（GMAP）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CAP_ACCEPTOR || CONFIG_BT_CAP_INITIATOR) && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.gmap:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.gmap#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_ACCEPTOR`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CAP_ACCEPTOR)、[`CONFIG_BT_CAP_INITIATOR`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CAP_INITIATOR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GOEP"></a>

## 326.7 `CONFIG_BT_GOEP`

**提示（Prompt）**：蓝牙通用对象交换配置文件（Bluetooth GOEP Profile）[实验性，EXPERIMENTAL]

**说明（Help）**

启用通用对象交换配置文件（GOEP profile）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_RFCOMM
CONFIG_BT_L2CAP_ENH_RET
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_BT_BIP
CONFIG_BT_PBAP
CONFIG_BT_MAP
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:705`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L705)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_RFCOMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_RFCOMM)、[`CONFIG_BT_L2CAP_ENH_RET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_ENH_RET)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_BIP`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BIP)、[`CONFIG_BT_PBAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PBAP)、[`CONFIG_BT_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAP)。

<a id="CONFIG_BT_GOEP_L2CAP_MTU"></a>

## 326.8 `CONFIG_BT_GOEP_L2CAP_MTU`

**提示（Prompt）**：GOEP 的 L2CAP MTU（L2CAP MTU for GOEP）

**说明（Help）**

GOEP 的 L2CAP 最大传输单元（MTU）最大大小。接收 MTU（RX MTU）会被截减，为 ACL 数据及类型开销和 L2CAP PDU 头（header）留出空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GOEP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BUF_ACL_RX_SIZE
```

**取值范围（Ranges）**

```text
[265, CONFIG_BT_BUF_ACL_RX_SIZE]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:728`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L728)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙通用对象交换配置文件（Bluetooth GOEP Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_GOEP`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_GOEP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BUF_ACL_RX_SIZE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BUF_ACL_RX_SIZE)。

<a id="CONFIG_BT_GOEP_RFCOMM_MTU"></a>

## 326.9 `CONFIG_BT_GOEP_RFCOMM_MTU`

**提示（Prompt）**：GOEP 的 RFCOMM MTU（RFCOMM MTU for GOEP）

**说明（Help）**

GOEP 的 RFCOMM 最大传输单元（MTU）最大大小。接收 MTU（RX MTU）会被截减，为 ACL 数据及类型开销、L2CAP PDU 头及 RFCOMM 头（header）留出空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GOEP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_RFCOMM_L2CAP_MTU
```

**取值范围（Ranges）**

```text
[265, CONFIG_BT_RFCOMM_L2CAP_MTU]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:714`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L714)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙通用对象交换配置文件（Bluetooth GOEP Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_GOEP`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_GOEP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_RFCOMM_L2CAP_MTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_RFCOMM_L2CAP_MTU)。

<a id="CONFIG_BT_HAS"></a>

## 326.10 `CONFIG_BT_HAS`

**提示（Prompt）**：助听访问服务支持（Hearing Access Service support）

**说明（Help）**

启用助听访问服务（Hearing Access Service）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_DYNAMIC_DB && CONFIG_BT_BAP_UNICAST_SERVER && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.has:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.has#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_DYNAMIC_DB`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_DYNAMIC_DB)、[`CONFIG_BT_BAP_UNICAST_SERVER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAP_UNICAST_SERVER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_HAS_ACTIVE_PRESET_INDEX"></a>

## 326.11 `CONFIG_BT_HAS_ACTIVE_PRESET_INDEX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用助听器活动预设索引特征（Hearing Aid Active Preset Index characteristic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HAS_PRESET_SUPPORT && CONFIG_BT_HAS && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_HAS_PRESET_SUPPORT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.has:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.has#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 助听访问服务支持（Hearing Access Service support）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_PRESET_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HAS_PRESET_SUPPORT)、[`CONFIG_BT_HAS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HAS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HAS_PRESET_SUPPORT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_HAS_CLIENT"></a>

## 326.12 `CONFIG_BT_HAS_CLIENT`

**提示（Prompt）**：助听访问服务客户端支持（Hearing Access Service Client support）

**说明（Help）**

启用助听访问服务客户端（Hearing Access Service Client）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_CLIENT && CONFIG_BT_GATT_AUTO_DISCOVER_CCC && CONFIG_BT_GATT_AUTO_UPDATE_MTU && CONFIG_BT_SMP && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.has:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.has#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_CLIENT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_GATT_AUTO_DISCOVER_CCC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_AUTO_DISCOVER_CCC)、[`CONFIG_BT_GATT_AUTO_UPDATE_MTU`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_AUTO_UPDATE_MTU)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_HAS_FEATURES_NOTIFIABLE"></a>

## 326.13 `CONFIG_BT_HAS_FEATURES_NOTIFIABLE`

**提示（Prompt）**：助听器功能通知支持（Hearing Aid Features Notifiable Support）

**说明（Help）**

允许客户端订阅助听器功能特征（Hearing Aid Features characteristic）的通知（notifications）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HAS && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.has:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.has#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 助听访问服务支持（Hearing Access Service support）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HAS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_HAS_HCI_VS"></a>

## 326.14 `CONFIG_BT_HAS_HCI_VS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项由蓝牙控制器设置，表示支持 Zephyr HCI 厂商专用命令与事件（Vendor-Specific Commands and Event）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_BT_HCI_IPC
CONFIG_BT_LLL_VENDOR_NORDIC
CONFIG_BT_LLL_VENDOR_OPENISA
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_IPC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_HCI_IPC)、[`CONFIG_BT_LLL_VENDOR_NORDIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LLL_VENDOR_NORDIC)、[`CONFIG_BT_LLL_VENDOR_OPENISA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LLL_VENDOR_OPENISA)。

<a id="CONFIG_BT_HAS_PRESET_CONTROL_POINT_NOTIFIABLE"></a>

## 326.15 `CONFIG_BT_HAS_PRESET_CONTROL_POINT_NOTIFIABLE`

**提示（Prompt）**：预设控制点通知支持（Preset Control Point Notifiable support）

**说明（Help）**

允许客户端订阅助听器预设控制点特征（Hearing Aid Preset Control Point characteristic）的通知（notifications）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_EATT && CONFIG_BT_HAS_PRESET_SUPPORT && CONFIG_BT_HAS && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.has:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.has#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 助听访问服务支持（Hearing Access Service support）

**配置项引用（Symbol References）**：[`CONFIG_BT_EATT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_EATT)、[`CONFIG_BT_HAS_PRESET_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HAS_PRESET_SUPPORT)、[`CONFIG_BT_HAS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HAS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HAS_PRESET_SUPPORT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_HAS_PRESET_COUNT"></a>

## 326.16 `CONFIG_BT_HAS_PRESET_COUNT`

**提示（Prompt）**：预设记录列表大小（Preset record list size）

**说明（Help）**

设置可注册的助听访问服务预设（Hearing Access Service Presets）数量。设为 `0` 会禁用预设支持。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HAS && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.has:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.has#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 助听访问服务支持（Hearing Access Service support）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HAS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_HAS_PRESET_NAME_DYNAMIC"></a>

## 326.17 `CONFIG_BT_HAS_PRESET_NAME_DYNAMIC`

**提示（Prompt）**：允许运行时设置预设名称（preset name at runtime）

**说明（Help）**

启用后，允许在运行时配置预设名称（preset name）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HAS_PRESET_SUPPORT && CONFIG_BT_HAS && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.has:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.has#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 助听访问服务支持（Hearing Access Service support）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_PRESET_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HAS_PRESET_SUPPORT)、[`CONFIG_BT_HAS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HAS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HAS_PRESET_SUPPORT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_HCI"></a>

## 326.18 `CONFIG_BT_HCI`

**提示（Prompt）**：基于 HCI（HCI-based）

**说明（Help）**

基于 HCI 的协议栈（HCI-based stack），包含可选的主机（host）与控制器（controller）部分，以及位于两者之间的 HCI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_STACK_SELECTION>
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙协议栈选择（Bluetooth Stack Selection）

**配置项引用（Symbol References）**：[`CONFIG_BT_STACK_SELECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_STACK_SELECTION)。

<a id="CONFIG_BT_HCI_ACL_FLOW_CONTROL"></a>

## 326.19 `CONFIG_BT_HCI_ACL_FLOW_CONTROL`

**提示（Prompt）**：控制器到主机的 ACL 流控支持（Controller to Host ACL flow control support）

**说明（Help）**

启用从控制器到主机的 ACL 缓冲区传送限流（throttling）支持。主机与控制器位于不同核心时尤其有用，可确保入站 ACL 缓冲区不会耗尽。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if !CONFIG_HAS_BT_CTLR && !CONFIG_BT_STM32_IPM && !CONFIG_BT_ESP32 && !CONFIG_BT_STM32WBA
y if CONFIG_BT_HCI_RAW
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/mchp_rnbd451_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/mchp_rnbd451_bt/Kconfig.defconfig)。

```text
n
```

来源：[`boards/shields/x_nucleo_bnrg2a1/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_bnrg2a1/Kconfig.defconfig)。

```text
n
```

来源：[`boards/shields/x_nucleo_idb05a1/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_idb05a1/Kconfig.defconfig)。

```text
n
```

来源：[`boards/shields/x_nucleo_wb05kn1/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_wb05kn1/Kconfig.defconfig)。

```text
n
```

来源：[`boards/shields/x_nucleo_wba25a1/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_wba25a1/Kconfig.defconfig)。

```text
n
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_STM32_IPM`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32_IPM)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_STM32WBA`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA)、[`CONFIG_BT_HCI_RAW`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI_RAW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_HCI_ERR_TO_STR"></a>

## 326.20 `CONFIG_BT_HCI_ERR_TO_STR`

**提示（Prompt）**：以字符串打印 HCI 错误码（HCI error codes as strings）[实验性，EXPERIMENTAL]

**说明（Help）**

启用以字符串形式打印 HCI 错误码（error codes）的功能。详情参见 `bt_hci_err_to_str()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:292`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L292)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_BT_HCI_MESH_EXT"></a>

## 326.21 `CONFIG_BT_HCI_MESH_EXT`

**提示（Prompt）**：Mesh HCI 命令支持（Mesh HCI Command support）

**说明（Help）**

启用蓝牙 Mesh HCI 命令（Bluetooth Mesh HCI Commands）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BROADCASTER && CONFIG_BT_OBSERVER && !CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:247`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L247)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HCI_RAW"></a>

## 326.22 `CONFIG_BT_HCI_RAW`

**提示（Prompt）**：原始 HCI 访问（RAW HCI access）

**说明（Help）**

允许应用通过原始 HCI 协议（RAW HCI protocol）访问蓝牙控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_USB_DEVICE_BLUETOOTH
CONFIG_USBD_BT_HCI
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_USB_DEVICE_BLUETOOTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_BLUETOOTH)、[`CONFIG_USBD_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_BT_HCI)。

<a id="CONFIG_BT_HCI_RAW_CMD_EXT"></a>

## 326.23 `CONFIG_BT_HCI_RAW_CMD_EXT`

**提示（Prompt）**：原始 HCI 命令扩展（RAW HCI Command Extension）

**说明（Help）**

启用 HCI 原始命令扩展（RAW command extension），使驱动能够注册自己的命令表扩展（command table extension）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HCI_TX_STACK_SIZE"></a>

## 326.24 `CONFIG_BT_HCI_TX_STACK_SIZE`

**提示（Prompt）**：HCI 发送线程栈大小（HCI Tx thread stack size）

**说明（Help）**

使用指定驱动执行 `bt_send` 所需的栈大小（stack size）。注意：这是高级设置，除非确有必要，否则不应修改。要修改此项，必须先选择 `BT_HCI_TX_STACK_SIZE_WITH_PROMPT`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
512 if CONFIG_BT_H4
512 if CONFIG_BT_H5
416 if CONFIG_BT_SPI
1280 if CONFIG_BT_LL_SW_SPLIT && (CONFIG_NO_OPTIMIZATIONS || CONFIG_BT_ISO_BROADCAST)
1024 if CONFIG_BT_LL_SW_SPLIT && CONFIG_BT_CENTRAL
768 if CONFIG_BT_LL_SW_SPLIT
512 if CONFIG_BT_USERCHAN
640 if CONFIG_BT_STM32_IPM
1024
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_H4`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4)、[`CONFIG_BT_H5`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H5)、[`CONFIG_BT_SPI`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SPI)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_NO_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NO_OPTIMIZATIONS)、[`CONFIG_BT_ISO_BROADCAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_BROADCAST)、[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BT_USERCHAN`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_USERCHAN)、[`CONFIG_BT_STM32_IPM`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32_IPM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_ISO_BROADCAST`。

<a id="CONFIG_BT_HCI_TX_STACK_SIZE_WITH_PROMPT"></a>

## 326.25 `CONFIG_BT_HCI_TX_STACK_SIZE_WITH_PROMPT`

**提示（Prompt）**：覆盖 HCI 发送线程栈大小（Override HCI Tx thread stack size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HCI_VS"></a>

## 326.26 `CONFIG_BT_HCI_VS`

**提示（Prompt）**：Zephyr HCI 厂商专用命令（Zephyr HCI Vendor-Specific Commands）

**说明（Help）**

在主机和／或控制器中启用 Zephyr HCI 厂商专用命令（Vendor-Specific Commands）支持，包括设置版本信息（Set Version Information）、支持的命令（Supported Commands）及支持的功能（Supported Features）这些厂商命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_HAS_HCI_VS || !CONFIG_HAS_BT_CTLR) && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HAS_HCI_VS
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/x_nucleo_idb05a1/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_idb05a1/Kconfig.defconfig)。

```text
n
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:218`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L218)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_HCI_VS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HAS_HCI_VS)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_HCI_VS_EVT_USER"></a>

## 326.27 `CONFIG_BT_HCI_VS_EVT_USER`

**提示（Prompt）**：用户处理厂商专用事件（User Vendor-Specific event handling）

**说明（Help）**

允许注册回调，将协议栈不认识的厂商专用事件（VS events）交给用户处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1169)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HCI_VS_EXT_DETECT"></a>

## 326.28 `CONFIG_BT_HCI_VS_EXT_DETECT`

**提示（Prompt）**：使用启发式方法预判 HCI 厂商扩展支持（heuristics for HCI vendor extensions support）

**说明（Help）**

使用启发式方法（heuristics）尝试提前判断控制器是否支持 HCI 厂商扩展，避免向可能以完全不同方式解释这些命令的控制器发送厂商命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_VS && !CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BOARD_QEMU_X86 || CONFIG_BOARD_QEMU_CORTEX_M3 || CONFIG_BOARD_NATIVE_SIM
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:237`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L237)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_VS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI_VS)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BOARD_QEMU_X86`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_QEMU_X86)、[`CONFIG_BOARD_QEMU_CORTEX_M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_QEMU_CORTEX_M3)、[`CONFIG_BOARD_NATIVE_SIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NATIVE_SIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BOARD_QEMU_X86`、`CONFIG_BOARD_QEMU_CORTEX_M3`、`CONFIG_BOARD_NATIVE_SIM`。

<a id="CONFIG_BT_HCI_VS_FATAL_ERROR"></a>

## 326.29 `CONFIG_BT_HCI_VS_FATAL_ERROR`

**提示（Prompt）**：允许 Zephyr 致命错误 HCI 厂商专用事件（Zephyr Fatal Error）

**说明（Help）**

允许针对不可恢复的系统和控制器错误，发出 HCI 厂商专用事件（Vendor-Specific events）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_VS && CONFIG_BT_HCI_VS_FATAL_ERROR_SUPPORT && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:230`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L230)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_VS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI_VS)、[`CONFIG_BT_HCI_VS_FATAL_ERROR_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_VS_FATAL_ERROR_SUPPORT)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_VS_FATAL_ERROR_SUPPORT`。

<a id="CONFIG_BT_HFP_AG"></a>

## 326.30 `CONFIG_BT_HFP_AG`

**提示（Prompt）**：蓝牙免提配置文件音频网关角色支持（Handsfree Profile AG Role）[实验性，EXPERIMENTAL]

**说明（Help）**

启用蓝牙音频网关（Audio Gateway，AG）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PRINTK && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_RFCOMM
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:196`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L196)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_PRINTK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PRINTK)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_RFCOMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_RFCOMM)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_BT_HFP_AG_3WAY_CALL"></a>

## 326.31 `CONFIG_BT_HFP_AG_3WAY_CALL`

**提示（Prompt）**：HFP 音频网关三方通话（Three-way calling for HFP AG）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 音频网关（AG）启用三方通话（Three-way calling）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:329`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L329)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_AG_ALERTING_TIMEOUT"></a>

## 326.32 `CONFIG_BT_HFP_AG_ALERTING_TIMEOUT`

**提示（Prompt）**：HFP 音频网关呼叫提醒／振铃超时（Call alerting/ringing timeout）[实验性，EXPERIMENTAL]

**说明（Help）**

设置呼叫提醒／振铃（alerting/ringing）的超时。如果超时前呼叫未进入活动状态（active），HFP 音频网关（AG）将停止该呼叫。单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
60
```

**取值范围（Ranges）**

```text
[10, 60]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:381`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L381)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_AG_CODEC_LC3_SWB"></a>

## 326.33 `CONFIG_BT_HFP_AG_CODEC_LC3_SWB`

**提示（Prompt）**：HFP 音频网关 LC3 超宽带编解码器支持（Codec LC3 SWB for HFP AG）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 音频网关（AG）启用 LC3 超宽带编解码器（LC3 SWB）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG_CODEC_NEG && CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:318`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L318)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → HFP 音频网关编解码器协商（Codec Negotiation for HFP AG）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG_CODEC_NEG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG_CODEC_NEG)、[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_AG_CODEC_MSBC"></a>

## 326.34 `CONFIG_BT_HFP_AG_CODEC_MSBC`

**提示（Prompt）**：HFP 音频网关 mSBC 编解码器支持（Codec mSBC for HFP AG）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 音频网关（AG）启用 mSBC 编解码器（codec）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG_CODEC_NEG && CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:313`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L313)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → HFP 音频网关编解码器协商（Codec Negotiation for HFP AG）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG_CODEC_NEG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG_CODEC_NEG)、[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_AG_CODEC_NEG"></a>

## 326.35 `CONFIG_BT_HFP_AG_CODEC_NEG`

**提示（Prompt）**：HFP 音频网关编解码器协商（Codec Negotiation for HFP AG）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 音频网关（AG）启用编解码器协商（Codec Negotiation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L307)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_AG_ECC"></a>

## 326.36 `CONFIG_BT_HFP_AG_ECC`

**提示（Prompt）**：HFP 音频网关增强呼叫控制（Enhanced call control for HFP AG）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 音频网关（AG）启用增强呼叫控制（Enhanced call control）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HFP_AG_3WAY_CALL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:348`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L348)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_AG_3WAY_CALL`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG_3WAY_CALL)。

<a id="CONFIG_BT_HFP_AG_ECNR"></a>

## 326.37 `CONFIG_BT_HFP_AG_ECNR`

**提示（Prompt）**：HFP 音频网关回声消除和／或降噪功能（EC and/or NR）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 音频网关（AG）启用回声消除（EC）和／或降噪（NR）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:324`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L324)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_AG_ECS"></a>

## 326.38 `CONFIG_BT_HFP_AG_ECS`

**提示（Prompt）**：HFP 音频网关增强呼叫状态（Enhanced call status for HFP AG）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 音频网关（AG）启用增强呼叫状态（Enhanced call status）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HFP_AG_3WAY_CALL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:342`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L342)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_AG_3WAY_CALL`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG_3WAY_CALL)。

<a id="CONFIG_BT_HFP_AG_ENH_VOICE_RECG"></a>

## 326.39 `CONFIG_BT_HFP_AG_ENH_VOICE_RECG`

**提示（Prompt）**：HFP 音频网关增强语音识别状态（Enhanced Voice Recognition Status）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 音频网关（AG）启用增强语音识别状态（Enhanced Voice Recognition Status）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_HFP_AG_VOICE_RECG
```

**被选择（Selected by）**

```text
CONFIG_BT_HFP_AG_VOICE_RECG_TEXT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:409`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L409)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_AG_VOICE_RECG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG_VOICE_RECG)、[`CONFIG_BT_HFP_AG_VOICE_RECG_TEXT`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG_VOICE_RECG_TEXT)。

<a id="CONFIG_BT_HFP_AG_EXT_ERR"></a>

## 326.40 `CONFIG_BT_HFP_AG_EXT_ERR`

**提示（Prompt）**：HFP 音频网关扩展错误结果码（Extended Error Result Codes）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 音频网关（AG）启用扩展错误结果码（Extended Error Result Codes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:301`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L301)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_AG_GET_ONGOING_CALL_TIMEOUT"></a>

## 326.41 `CONFIG_BT_HFP_AG_GET_ONGOING_CALL_TIMEOUT`

**提示（Prompt）**：通知获取进行中呼叫回调后的超时，单位为毫秒（get ongoing calls callback timeout）[实验性，EXPERIMENTAL]

**说明（Help）**

设置获取进行中呼叫（get ongoing calls）的回调通知发出后的超时时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
10000
```

**取值范围（Ranges）**

```text
[1000, 10000]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:450`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L450)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_AG_HF_INDICATORS"></a>

## 326.42 `CONFIG_BT_HFP_AG_HF_INDICATORS`

**提示（Prompt）**：HFP 音频网关免提指示器（HF Indicators for HFP AG）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 音频网关（AG）启用免提指示器（HF Indicators）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_HFP_AG_HF_INDICATOR_ENH_SAFETY
CONFIG_BT_HFP_AG_HF_INDICATOR_BATTERY
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:427`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L427)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_AG_HF_INDICATOR_ENH_SAFETY`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG_HF_INDICATOR_ENH_SAFETY)、[`CONFIG_BT_HFP_AG_HF_INDICATOR_BATTERY`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG_HF_INDICATOR_BATTERY)。

<a id="CONFIG_BT_HFP_AG_HF_INDICATOR_BATTERY"></a>

## 326.43 `CONFIG_BT_HFP_AG_HF_INDICATOR_BATTERY`

**提示（Prompt）**：HFP 音频网关免提电池电量指示器（HF Indicator Battery level）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 音频网关（AG）启用免提电池电量指示器（HF Indicator Battery level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_HFP_AG_HF_INDICATORS
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:438`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L438)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_AG_HF_INDICATORS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG_HF_INDICATORS)。

<a id="CONFIG_BT_HFP_AG_HF_INDICATOR_ENH_SAFETY"></a>

## 326.44 `CONFIG_BT_HFP_AG_HF_INDICATOR_ENH_SAFETY`

**提示（Prompt）**：HFP 音频网关免提增强安全指示器（HF Indicator Enhanced Safety）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 音频网关（AG）启用免提增强安全指示器（HF Indicator Enhanced Safety）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_HFP_AG_HF_INDICATORS
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:432`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L432)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_AG_HF_INDICATORS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG_HF_INDICATORS)。

<a id="CONFIG_BT_HFP_AG_INBAND_RINGTONE"></a>

## 326.45 `CONFIG_BT_HFP_AG_INBAND_RINGTONE`

**提示（Prompt）**：带内铃声能力（In-band ring tone capability）

**说明（Help）**

启用带内铃声能力（In-band ring tone capability）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:457`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L457)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_AG_INCOMING_TIMEOUT"></a>

## 326.46 `CONFIG_BT_HFP_AG_INCOMING_TIMEOUT`

**提示（Prompt）**：HFP 音频网关来电超时（Incoming call timeout for HFP AG）[实验性，EXPERIMENTAL]

**说明（Help）**

设置来电（incoming call）的超时。如果超时前呼叫未转入振铃状态（ringing state），HFP 音频网关（AG）将停止该呼叫。单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 10]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:372`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L372)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_AG_MAX_CALLS"></a>

## 326.47 `CONFIG_BT_HFP_AG_MAX_CALLS`

**提示（Prompt）**：HFP 音频网关支持的最大呼叫数（Maximum supported calls for HFP AG）[实验性，EXPERIMENTAL]

**说明（Help）**

设置 HFP 音频网关（AG）支持的最大呼叫数（calls）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2 if CONFIG_BT_HFP_AG_3WAY_CALL
1
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:334`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L334)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_AG_3WAY_CALL`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG_3WAY_CALL)。

<a id="CONFIG_BT_HFP_AG_OUTGOING_TIMEOUT"></a>

## 326.48 `CONFIG_BT_HFP_AG_OUTGOING_TIMEOUT`

**提示（Prompt）**：HFP 音频网关呼出超时（Call outgoing timeout for HFP AG）[实验性，EXPERIMENTAL]

**说明（Help）**

设置呼出（call outgoing）的超时。如果超时前呼叫未转入提醒状态（alerting state），HFP 音频网关（AG）将停止该呼叫。单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 10]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:363`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L363)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_AG_PHONE_NUMBER_MAX_LEN"></a>

## 326.49 `CONFIG_BT_HFP_AG_PHONE_NUMBER_MAX_LEN`

**提示（Prompt）**：HFP 音频网关支持的电话号码最大长度（max length of phone number）[实验性，EXPERIMENTAL]

**说明（Help）**

HFP 音频网关（AG）支持的电话号码（phone number）最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:390`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L390)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_AG_REJECT_CALL"></a>

## 326.50 `CONFIG_BT_HFP_AG_REJECT_CALL`

**提示（Prompt）**：HFP 音频网关拒接呼叫能力（Ability to reject a call）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 音频网关（AG）启用拒接呼叫（reject a call）的能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:444`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L444)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_AG_RING_NOTIFY_INTERVAL"></a>

## 326.51 `CONFIG_BT_HFP_AG_RING_NOTIFY_INTERVAL`

**提示（Prompt）**：振铃通知间隔（Ring notification interval）[实验性，EXPERIMENTAL]

**说明（Help）**

呼叫处于提醒状态（alert state）时的振铃通知间隔（Ring notification interval），单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:397`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L397)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_AG_TX_BUF_COUNT"></a>

## 326.52 `CONFIG_BT_HFP_AG_TX_BUF_COUNT`

**提示（Prompt）**：HFP 音频网关最大发送缓冲区数量（Maximum number of TX buffers）[实验性，EXPERIMENTAL]

**说明（Help）**

具有关联发送缓冲区（sending buf）的待处理发送缓冲区（pending TX buffers）最大数量。通常可保留默认值，其值等于协议栈内部池（stack-internal pool）的会话数量（sessions）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_RFCOMM_TX_MAX
```

**取值范围（Ranges）**

```text
[CONFIG_BT_RFCOMM_TX_MAX, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:354`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L354)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_RFCOMM_TX_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_RFCOMM_TX_MAX)。

<a id="CONFIG_BT_HFP_AG_VOICE_RECG"></a>

## 326.53 `CONFIG_BT_HFP_AG_VOICE_RECG`

**提示（Prompt）**：HFP 音频网关语音识别激活（Voice recognition activation）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 音频网关（AG）启用语音识别激活（Voice recognition activation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_HFP_AG_ENH_VOICE_RECG
CONFIG_BT_HFP_AG_VOICE_TAG
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:404`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L404)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_AG_ENH_VOICE_RECG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG_ENH_VOICE_RECG)、[`CONFIG_BT_HFP_AG_VOICE_TAG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG_VOICE_TAG)。

<a id="CONFIG_BT_HFP_AG_VOICE_RECG_TEXT"></a>

## 326.54 `CONFIG_BT_HFP_AG_VOICE_RECG_TEXT`

**提示（Prompt）**：HFP 音频网关语音识别文本（Voice Recognition Text）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 音频网关（AG）启用语音识别文本（Voice Recognition Text）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_HFP_AG_ENH_VOICE_RECG
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:415`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L415)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_AG_ENH_VOICE_RECG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG_ENH_VOICE_RECG)。

<a id="CONFIG_BT_HFP_AG_VOICE_TAG"></a>

## 326.55 `CONFIG_BT_HFP_AG_VOICE_TAG`

**提示（Prompt）**：HFP 音频网关为语音标签附加电话号码（Attach a phone number for a voice tag）[实验性，EXPERIMENTAL]

**说明（Help）**

允许 HFP 音频网关（AG）为语音标签（voice tag）附加电话号码（phone number）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_AG && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_HFP_AG_VOICE_RECG
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:421`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L421)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_AG_VOICE_RECG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG_VOICE_RECG)。

<a id="CONFIG_BT_HFP_HF"></a>

## 326.56 `CONFIG_BT_HFP_HF`

**提示（Prompt）**：蓝牙免提配置文件免提角色支持（Handsfree Profile HF Role）[实验性，EXPERIMENTAL]

**说明（Help）**

启用蓝牙免提端（Hands-Free，HF）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PRINTK && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_RFCOMM
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:188`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L188)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_PRINTK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PRINTK)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_RFCOMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_RFCOMM)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_BT_HFP_HF_3WAY_CALL"></a>

## 326.57 `CONFIG_BT_HFP_HF_3WAY_CALL`

**提示（Prompt）**：HFP 免提端三方通话（Three-way calling for HFP HF）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 免提端（HF）启用三方通话（Three-way calling）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_HF_CLI"></a>

## 326.58 `CONFIG_BT_HFP_HF_CLI`

**提示（Prompt）**：HFP 免提端来电号码显示能力（CLI presentation capability）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 免提端（HF）启用来电号码显示能力（CLI presentation capability）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:205`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L205)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_HF_CODEC_LC3_SWB"></a>

## 326.59 `CONFIG_BT_HFP_HF_CODEC_LC3_SWB`

**提示（Prompt）**：HFP 免提端 LC3 超宽带编解码器支持（Codec LC3 SWB for HFP HF）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 免提端（HF）启用 LC3 超宽带编解码器（LC3 SWB）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF_CODEC_NEG && CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:233`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L233)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF_CODEC_NEG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF_CODEC_NEG)、[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_HF_CODEC_MSBC"></a>

## 326.60 `CONFIG_BT_HFP_HF_CODEC_MSBC`

**提示（Prompt）**：HFP 免提端 mSBC 编解码器支持（Codec mSBC for HFP HF）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 免提端（HF）启用 mSBC 编解码器（codec）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF_CODEC_NEG && CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:228`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L228)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF_CODEC_NEG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF_CODEC_NEG)、[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_HF_CODEC_NEG"></a>

## 326.61 `CONFIG_BT_HFP_HF_CODEC_NEG`

**提示（Prompt）**：HFP 免提端编解码器协商（Codec Negotiation for HFP HF）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 免提端（HF）启用编解码器协商（Codec Negotiation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:217`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L217)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_HF_ECC"></a>

## 326.62 `CONFIG_BT_HFP_HF_ECC`

**提示（Prompt）**：HFP 免提端增强呼叫控制（Enhanced Call Control for HFP HF）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 免提端（HF）启用增强呼叫控制（Enhanced Call Control）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HFP_HF_3WAY_CALL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:250`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L250)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_HF_3WAY_CALL`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF_3WAY_CALL)。

<a id="CONFIG_BT_HFP_HF_ECNR"></a>

## 326.63 `CONFIG_BT_HFP_HF_ECNR`

**提示（Prompt）**：HFP 免提端回声消除和／或降噪功能（EC and/or NR）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 免提端（HF）启用回声消除（EC）和／或降噪（NR）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HFP_HF_ECS"></a>

## 326.64 `CONFIG_BT_HFP_HF_ECS`

**提示（Prompt）**：HFP 免提端增强呼叫状态（Enhanced Call Status for HFP HF）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 免提端（HF）启用增强呼叫状态（Enhanced Call Status）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HFP_HF_3WAY_CALL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:244`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L244)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_HF_3WAY_CALL`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF_3WAY_CALL)。

<a id="CONFIG_BT_HFP_HF_ENH_VOICE_RECG"></a>

## 326.65 `CONFIG_BT_HFP_HF_ENH_VOICE_RECG`

**提示（Prompt）**：HFP 免提端增强语音识别状态（Enhanced Voice Recognition Status）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 免提端（HF）启用增强语音识别状态（Enhanced Voice Recognition Status）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_HFP_HF_VOICE_RECG
```

**被选择（Selected by）**

```text
CONFIG_BT_HFP_HF_VOICE_RECG_TEXT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:269`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L269)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_HF_VOICE_RECG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF_VOICE_RECG)、[`CONFIG_BT_HFP_HF_VOICE_RECG_TEXT`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF_VOICE_RECG_TEXT)。

<a id="CONFIG_BT_HFP_HF_HF_INDICATORS"></a>

## 326.66 `CONFIG_BT_HFP_HF_HF_INDICATORS`

**提示（Prompt）**：HFP 免提端免提指示器（HF Indicators for HFP HF）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 免提端（HF）启用免提指示器（HF Indicators）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_HFP_HF_HF_INDICATOR_ENH_SAFETY
CONFIG_BT_HFP_HF_HF_INDICATOR_BATTERY
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:281`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L281)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_HF_HF_INDICATOR_ENH_SAFETY`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF_HF_INDICATOR_ENH_SAFETY)、[`CONFIG_BT_HFP_HF_HF_INDICATOR_BATTERY`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF_HF_INDICATOR_BATTERY)。

<a id="CONFIG_BT_HFP_HF_HF_INDICATOR_BATTERY"></a>

## 326.67 `CONFIG_BT_HFP_HF_HF_INDICATOR_BATTERY`

**提示（Prompt）**：HFP 免提端免提电池电量指示器（HF Indicator Battery level）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 免提端（HF）启用免提电池电量指示器（HF Indicator Battery level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_HFP_HF_HF_INDICATORS
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:292`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L292)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_HF_HF_INDICATORS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF_HF_INDICATORS)。

<a id="CONFIG_BT_HFP_HF_HF_INDICATOR_ENH_SAFETY"></a>

## 326.68 `CONFIG_BT_HFP_HF_HF_INDICATOR_ENH_SAFETY`

**提示（Prompt）**：HFP 免提端免提增强安全指示器（HF Indicator Enhanced Safety）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 免提端（HF）启用免提增强安全指示器（HF Indicator Enhanced Safety）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_HFP_HF_HF_INDICATORS
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:286`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L286)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_HF_HF_INDICATORS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF_HF_INDICATORS)。

<a id="CONFIG_BT_HFP_HF_MAX_CALLS"></a>

## 326.69 `CONFIG_BT_HFP_HF_MAX_CALLS`

**提示（Prompt）**：HFP 免提端支持的最大呼叫数（Maximum supported calls for HFP HF）[实验性，EXPERIMENTAL]

**说明（Help）**

设置 HFP 免提端（HF）支持的最大呼叫数（calls）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2 if CONFIG_BT_HFP_HF_3WAY_CALL
1
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:256`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L256)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_HF_3WAY_CALL`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF_3WAY_CALL)。

<a id="CONFIG_BT_HFP_HF_VOICE_RECG"></a>

## 326.70 `CONFIG_BT_HFP_HF_VOICE_RECG`

**提示（Prompt）**：HFP 免提端语音识别激活（Voice recognition activation）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 免提端（HF）启用语音识别激活（Voice recognition activation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_HFP_HF_ENH_VOICE_RECG
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:264`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L264)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_HF_ENH_VOICE_RECG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF_ENH_VOICE_RECG)。

<a id="CONFIG_BT_HFP_HF_VOICE_RECG_TEXT"></a>

## 326.71 `CONFIG_BT_HFP_HF_VOICE_RECG_TEXT`

**提示（Prompt）**：HFP 免提端语音识别文本（Voice Recognition Text）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 免提端（HF）启用语音识别文本（Voice Recognition Text）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_HFP_HF_ENH_VOICE_RECG
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:275`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L275)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_HF_ENH_VOICE_RECG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF_ENH_VOICE_RECG)。

<a id="CONFIG_BT_HFP_HF_VOLUME"></a>

## 326.72 `CONFIG_BT_HFP_HF_VOLUME`

**提示（Prompt）**：HFP 免提端远程音量控制（Remote audio volume control）[实验性，EXPERIMENTAL]

**说明（Help）**

为 HFP 免提端（HF）启用远程音量控制（Remote audio volume control）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HFP_HF && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_HID_DEVICE"></a>

## 326.73 `CONFIG_BT_HID_DEVICE`

**提示（Prompt）**：蓝牙人机接口设备端配置文件（Bluetooth HID Device Profile）[实验性，EXPERIMENTAL]

**说明（Help）**

启用人机接口设备端配置文件（HID Device profile）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_BT_DID
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:663`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L663)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_DID`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DID)。

<a id="CONFIG_BT_HID_HOST"></a>

## 326.74 `CONFIG_BT_HID_HOST`

**提示（Prompt）**：蓝牙人机接口主机端配置文件（Bluetooth HID Host Profile）[实验性，EXPERIMENTAL]

**说明（Help）**

启用人机接口主机端配置文件（HID Host profile）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:670`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L670)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_BT_HOST_CCM"></a>

## 326.75 `CONFIG_BT_HOST_CCM`

**提示（Prompt）**：主机侧 AES-CCM 模块（Host side AES-CCM module）

**说明（Help）**

在主机中启用基于软件的 AES-CCM 引擎（engine）。如果控制器的 AES 加密函数可用，则使用它们；否则使用 `BT_HOST_CRYPTO`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_EAD
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1089`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1089)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_EAD`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_EAD)。

<a id="CONFIG_BT_HOST_CRYPTO"></a>

## 326.76 `CONFIG_BT_HOST_CRYPTO`

**提示（Prompt）**：使用蓝牙主机实现的密码功能（crypto functionality in the Bluetooth host）

**说明（Help）**

如果控制器实现没有提供 AES 加密支持，此选项通过 PSA Crypto API 库增加该支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if !CONFIG_BT_CTLR_CRYPTO
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_ALG_ECB_NO_PADDING
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_CRYPTO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CRYPTO)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_ALG_ECB_NO_PADDING`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECB_NO_PADDING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_HOST_CRYPTO_PRNG"></a>

## 326.77 `CONFIG_BT_HOST_CRYPTO_PRNG`

**提示（Prompt）**：使用 PSA Crypto API 库生成随机数（random number generation）

**说明（Help）**

选择此项时，使用 PSA Crypto API 库生成随机数。这会额外消耗 RAM，但可能提高随机数生成速度。否则，通过多次 HCI 调用生成随机数，不额外消耗资源，但可能随随机数据长度增加而耗时较长。原文建议后一种方法通常用于 `16` 字节以内的数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HOST_CRYPTO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 使用蓝牙主机实现的密码功能（crypto functionality in the Bluetooth host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HOST_CRYPTO`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HOST_CRYPTO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_HRS"></a>

## 326.78 `CONFIG_BT_HRS`

**提示（Prompt）**：GATT 心率服务（GATT Heart Rate service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.hrs:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.hrs#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_HRS_DEFAULT_PERM"></a>

## 326.79 `CONFIG_BT_HRS_DEFAULT_PERM`

**提示（Prompt）**：HRS 特征使用的默认权限（Default permissions for HRS characteristics）

**说明（Help）**

未为报告（report）设置权限时，心率服务（HRS）特征属性使用的默认权限，也用于引导报告（boot reports）。

译注：原帮助文本包含 `report` 与 `boot reports` 的表述，此处保留；不据此为心率服务推定额外的报告格式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HRS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_HRS_DEFAULT_PERM_RW
```

**可选项（Choices）**

```text
CONFIG_BT_HRS_DEFAULT_PERM_RW
CONFIG_BT_HRS_DEFAULT_PERM_RW_ENCRYPT
CONFIG_BT_HRS_DEFAULT_PERM_RW_AUTHEN
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.hrs:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.hrs#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 心率服务（GATT Heart Rate service）

**配置项引用（Symbol References）**：[`CONFIG_BT_HRS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HRS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HRS_DEFAULT_PERM_RW`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HRS_DEFAULT_PERM_RW)、[`CONFIG_BT_HRS_DEFAULT_PERM_RW_ENCRYPT`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HRS_DEFAULT_PERM_RW_ENCRYPT)、[`CONFIG_BT_HRS_DEFAULT_PERM_RW_AUTHEN`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HRS_DEFAULT_PERM_RW_AUTHEN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_HRS_DEFAULT_PERM_RW"></a>

## 326.80 `CONFIG_BT_HRS_DEFAULT_PERM_RW`

**提示（Prompt）**：允许读写（Read and write allowed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HRS_DEFAULT_PERM>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.hrs:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.hrs#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 心率服务（GATT Heart Rate service） → HRS 特征使用的默认权限（Default permissions for HRS characteristics）

**配置项引用（Symbol References）**：[`CONFIG_BT_HRS_DEFAULT_PERM`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HRS_DEFAULT_PERM)。

<a id="CONFIG_BT_HRS_DEFAULT_PERM_RW_AUTHEN"></a>

## 326.81 `CONFIG_BT_HRS_DEFAULT_PERM_RW_AUTHEN`

**提示（Prompt）**：访问需要加密与身份认证（Require encryption and authentication for access）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HRS_DEFAULT_PERM>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.hrs:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.hrs#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 心率服务（GATT Heart Rate service） → HRS 特征使用的默认权限（Default permissions for HRS characteristics）

**配置项引用（Symbol References）**：[`CONFIG_BT_HRS_DEFAULT_PERM`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HRS_DEFAULT_PERM)。

<a id="CONFIG_BT_HRS_DEFAULT_PERM_RW_ENCRYPT"></a>

## 326.82 `CONFIG_BT_HRS_DEFAULT_PERM_RW_ENCRYPT`

**提示（Prompt）**：访问需要加密（Require encryption for access）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HRS_DEFAULT_PERM>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.hrs:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.hrs#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 心率服务（GATT Heart Rate service） → HRS 特征使用的默认权限（Default permissions for HRS characteristics）

**配置项引用（Symbol References）**：[`CONFIG_BT_HRS_DEFAULT_PERM`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HRS_DEFAULT_PERM)。

<a id="CONFIG_BT_IAS"></a>

## 326.83 `CONFIG_BT_IAS`

**提示（Prompt）**：GATT 即时警报服务支持（GATT Immediate Alert Service）[实验性，EXPERIMENTAL]

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ias/Kconfig.ias:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ias/Kconfig.ias#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_IAS_CLIENT"></a>

## 326.84 `CONFIG_BT_IAS_CLIENT`

**提示（Prompt）**：即时警报服务客户端（Immediate Alert Service Client）[实验性，Experimental]

**说明（Help）**

启用即时警报服务客户端（Immediate Alert Service Client）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_GATT_CLIENT
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ias/Kconfig.ias:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ias/Kconfig.ias#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_GATT_CLIENT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CLIENT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_IAS_SEC_AUTH"></a>

## 326.85 `CONFIG_BT_IAS_SEC_AUTH`

**提示（Prompt）**：写访问需要加密与身份认证（Require encryption and authentication for write access）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_SEC_CHOICE>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ias/Kconfig.ias:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ias/Kconfig.ias#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 即时警报服务支持（GATT Immediate Alert Service）[实验性，EXPERIMENTAL] → IAS 特征使用的默认权限（Default permissions for IAS characteristics）

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_SEC_CHOICE`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_IAS_SEC_CHOICE)。

<a id="CONFIG_BT_IAS_SEC_CHOICE"></a>

## 326.86 `CONFIG_BT_IAS_SEC_CHOICE`

**提示（Prompt）**：IAS 特征使用的默认权限（Default permissions for IAS characteristics）

**说明（Help）**

即时警报服务（IAS）特征属性的默认写权限（write permissions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_IAS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_IAS_SEC_NONE
```

**可选项（Choices）**

```text
CONFIG_BT_IAS_SEC_NONE
CONFIG_BT_IAS_SEC_ENC
CONFIG_BT_IAS_SEC_AUTH
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ias/Kconfig.ias:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ias/Kconfig.ias#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 即时警报服务支持（GATT Immediate Alert Service）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_IAS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_IAS_SEC_NONE`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_IAS_SEC_NONE)、[`CONFIG_BT_IAS_SEC_ENC`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_IAS_SEC_ENC)、[`CONFIG_BT_IAS_SEC_AUTH`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_IAS_SEC_AUTH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_IAS_SEC_ENC"></a>

## 326.87 `CONFIG_BT_IAS_SEC_ENC`

**提示（Prompt）**：写访问需要加密（Require encryption for write access）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_SEC_CHOICE>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ias/Kconfig.ias:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ias/Kconfig.ias#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 即时警报服务支持（GATT Immediate Alert Service）[实验性，EXPERIMENTAL] → IAS 特征使用的默认权限（Default permissions for IAS characteristics）

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_SEC_CHOICE`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_IAS_SEC_CHOICE)。

<a id="CONFIG_BT_IAS_SEC_NONE"></a>

## 326.88 `CONFIG_BT_IAS_SEC_NONE`

**提示（Prompt）**：不要求安全保护（No security required）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_SEC_CHOICE>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ias/Kconfig.ias:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ias/Kconfig.ias#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 即时警报服务支持（GATT Immediate Alert Service）[实验性，EXPERIMENTAL] → IAS 特征使用的默认权限（Default permissions for IAS characteristics）

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_SEC_CHOICE`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_IAS_SEC_CHOICE)。

<a id="CONFIG_BT_ID_ALLOW_UNAUTH_OVERWRITE"></a>

## 326.89 `CONFIG_BT_ID_ALLOW_UNAUTH_OVERWRITE`

**提示（Prompt）**：允许同一对端在其他本地身份上进行未经身份认证的配对（unauthenticated pairing with other local identity）

**说明（Help）**

当某个对端已在另一个本地身份（local identity）上建立未经身份认证的绑定（unauthenticated bond）时，此选项允许该对端发起未经身份认证的配对尝试。此配置仍会阻止在同一本地身份上进行未经身份认证的配对尝试。如果需要无条件允许配对过程，请参阅 `BT_SMP_ALLOW_UNAUTH_OVERWRITE` 配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_BT_SMP_ALLOW_UNAUTH_OVERWRITE && CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:690`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L690)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP_ALLOW_UNAUTH_OVERWRITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP_ALLOW_UNAUTH_OVERWRITE)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ID_MAX"></a>

## 326.90 `CONFIG_BT_ID_MAX`

**提示（Prompt）**：本地身份最大数量（Maximum number of local identities）

**说明（Help）**

支持的本地身份地址（local identity addresses）最大数量。对大多数产品，可放心保留默认值 `1`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 1] if CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL
[1, 250]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:973`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L973)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ID_UNPAIR_MATCHING_BONDS"></a>

## 326.91 `CONFIG_BT_ID_UNPAIR_MATCHING_BONDS`

**提示（Prompt）**：绑定时删除同一对端在其他本地身份上的绑定（Delete bond with other local identity）

**说明（Help）**

当某个绑定（bond）即将完成时，查找具有相同对端地址或身份解析密钥（IRK）的其他绑定，并在 `pairing_complete` 事件之前调用 `bt_unpair` 删除它。

重要：如果未启用此选项，当前实现会自动使此次绑定失败，原因见下文“解析列表限制（RL limitation）”。

重要：如果未启用此选项，设备作为外设（Peripheral）时可能已来不及中止绑定。配对在本地失败，但中心设备（Central）仍可能报告成功。发生这种情况时，Zephyr 外设会立即断开连接，原因见下文“安全管理协议限制（SMP limitation）”。

**解析列表限制（RL limitation）**

主机实现者认为，应用不太可能希望与同一对端保存多个绑定，因此优先考虑实现简单性，而没有提供这种能力。控制器上的解析列表（Resolve List）无法为一个远端地址容纳多个本地地址／IRK，这会使主机无法在主机绑定数据库与控制器解析列表之间建立一一对应关系，而实现使用解析列表时依赖这种对应关系。出于性能原因，实现者也希望在此情况下避免退回主机地址解析（Host Address Resolution）。

**安全管理协议限制（SMP limitation）**

安全管理协议（Security Manager Protocol）的配对失败命令（原文写为 `Paring Failed`）不能在配对过程（Pairing Process）之外发送。最后一个需要分发的传输专用密钥（Transport Specific Key）在链路层获得确认时，配对过程即告结束。主机无法控制这一确认时机，而密钥分发顺序又由规范固定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:653`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L653)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ISO_BROADCASTER"></a>

## 326.92 `CONFIG_BT_ISO_BROADCASTER`

**提示（Prompt）**：蓝牙等时广播者支持（Bluetooth Isochronous Broadcaster Support）

**说明（Help）**

启用蓝牙等时广播者（Bluetooth Isochronous Broadcaster）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_ADV_ISO_SUPPORT) && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_ISO_BROADCAST
CONFIG_BT_ISO_TX
CONFIG_BT_BROADCASTER
CONFIG_BT_PER_ADV
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:319`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L319)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_ADV_ISO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_ISO_SUPPORT)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_BROADCAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_BROADCAST)、[`CONFIG_BT_ISO_TX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_TX)、[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_PER_ADV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_ADV_ISO_SUPPORT`、`CONFIG_BT_ISO_BROADCAST`、`CONFIG_BT_ISO_TX`。

<a id="CONFIG_BT_ISO_CENTRAL"></a>

## 326.93 `CONFIG_BT_ISO_CENTRAL`

**提示（Prompt）**：蓝牙等时信道单播中心设备支持（Bluetooth Isochronous Channel Unicast Central Support）

**说明（Help）**

为中心设备角色（central role）启用蓝牙广播等时信道（Bluetooth Broadcast Isochronous channels）支持。

译注：原帮助文本写的是广播（Broadcast），但选项提示写的是单播中心设备（Unicast Central）；此处保留并指出原文不一致，不擅自替换。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT) && CONFIG_BT_CENTRAL && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_ISO_UNICAST
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:305`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L305)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT)、[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_UNICAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_UNICAST)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT`。

<a id="CONFIG_BT_ISO_MAX_BIG"></a>

## 326.94 `CONFIG_BT_ISO_MAX_BIG`

**提示（Prompt）**：支持的广播等时组最大数量（Maximum number of Broadcast Isochronous Groups，BIGs）

**说明（Help）**

主机支持的广播等时组（BIGs）最大数量。一个 BIG 可用于发送或接收，但不能同时执行两者。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ISO_BROADCAST && CONFIG_BT_ISO && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, CONFIG_BT_EXT_ADV_MAX_ADV_SET]
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:408`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L408)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO_BROADCAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_BROADCAST)、[`CONFIG_BT_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_EXT_ADV_MAX_ADV_SET`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV_MAX_ADV_SET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_ISO_BROADCAST`、`CONFIG_BT_ISO`。

<a id="CONFIG_BT_ISO_MAX_CHAN"></a>

## 326.95 `CONFIG_BT_ISO_MAX_CHAN`

**提示（Prompt）**：最大同时 ISO 信道数（Maximum number of simultaneous ISO channels）

**说明（Help）**

支持同时存在的蓝牙等时信道（Bluetooth isochronous channels）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ISO && CONFIG_BT_ISO && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MAX_CONN if CONFIG_BT_CONN
1
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:342`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L342)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MAX_CONN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAX_CONN)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_ISO`。

<a id="CONFIG_BT_ISO_MAX_CIG"></a>

## 326.96 `CONFIG_BT_ISO_MAX_CIG`

**提示（Prompt）**：支持的连接等时组最大数量（Maximum number of Connected Isochronous Groups，CIGs）

**说明（Help）**

主机支持的连接等时组（CIGs）最大数量。一个 CIG 可用于发送或接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ISO_UNICAST && CONFIG_BT_ISO && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:397`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L397)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO_UNICAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_UNICAST)、[`CONFIG_BT_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_ISO`。

<a id="CONFIG_BT_ISO_PERIPHERAL"></a>

## 326.97 `CONFIG_BT_ISO_PERIPHERAL`

**提示（Prompt）**：蓝牙等时信道单播外设支持（Bluetooth Isochronous Channel Unicast Peripheral Support）

**说明（Help）**

为外设角色（peripheral role）启用蓝牙单播等时信道（Bluetooth Unicast Isochronous channels）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT) && CONFIG_BT_PERIPHERAL && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_ISO_UNICAST
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:296`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L296)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT)、[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_UNICAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_UNICAST)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT`。

<a id="CONFIG_BT_ISO_RX_BUF_COUNT"></a>

## 326.98 `CONFIG_BT_ISO_RX_BUF_COUNT`

**提示（Prompt）**：等时接收缓冲区数量（Number of Isochronous RX buffers）

**说明（Help）**

可用于接收入站等时信道 SDU（Isochronous channel SDUs）的缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ISO && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:371`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L371)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_ISO`。

<a id="CONFIG_BT_ISO_RX_MTU"></a>

## 326.99 `CONFIG_BT_ISO_RX_MTU`

**提示（Prompt）**：等时接收缓冲区支持的最大 MTU（Maximum supported MTU for Isochronous RX buffers）

**说明（Help）**

等时信道接收缓冲区（Isochronous channels RX buffers）的最大传输单元（MTU）。此值表示实际数据有效载荷，不包含 HCI ISO 数据包的可选字段，例如 `struct bt_hci_iso_sdu_ts_hdr`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ISO && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
251
```

**取值范围（Ranges）**

```text
[23, 4095]
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:378`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L378)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_ISO`。

<a id="CONFIG_BT_ISO_SYNC_RECEIVER"></a>

## 326.100 `CONFIG_BT_ISO_SYNC_RECEIVER`

**提示（Prompt）**：蓝牙等时同步接收器支持（Bluetooth Isochronous Synchronized Receiver Support）

**说明（Help）**

启用蓝牙等时同步接收器（Bluetooth Isochronous Synchronized Receiver）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_SYNC_ISO_SUPPORT) && CONFIG_BT_OBSERVER && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_ISO_BROADCAST
CONFIG_BT_ISO_RX
CONFIG_BT_PER_ADV_SYNC
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:329`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L329)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_SYNC_ISO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_ISO_SUPPORT)、[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_BROADCAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_BROADCAST)、[`CONFIG_BT_ISO_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_RX)、[`CONFIG_BT_PER_ADV_SYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_SYNC_ISO_SUPPORT`、`CONFIG_BT_ISO_BROADCAST`、`CONFIG_BT_ISO_RX`。

<!-- kconfig-navigation -->

[上一章](P325_subsys_bluetooth_配置项参考_6.md) · [返回大纲](大纲.md) · [下一章](P327_subsys_bluetooth_配置项参考_8.md)
