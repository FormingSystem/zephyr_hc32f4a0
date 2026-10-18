---
id: learning.zephyr-docs.kconfig-reference.page-327
title: "`subsys/bluetooth`配置项参考（8/13）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第327章\_`subsys/bluetooth`配置项参考（8/13）

本章翻译官方 Kconfig 数据库中 `subsys/bluetooth` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_ISO_TEST_PARAMS"></a>

## 327.1 `CONFIG_BT_ISO_TEST_PARAMS`

**提示（Prompt）**：ISO 测试参数支持（ISO test parameters support）

**说明（Help）**

启用高级等时参数（advanced ISO parameters）后，可以使用 ISO 测试参数创建连接等时组（CIG）或广播等时组（BIG）。这些参数原本用于测试，但也可让主机设置更多通常由控制器控制的选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ISO && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:387`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L387)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_ISO`。

<a id="CONFIG_BT_ISO_TX_BUF_COUNT"></a>

## 327.2 `CONFIG_BT_ISO_TX_BUF_COUNT`

**提示（Prompt）**：等时发送缓冲区数量（Number of Isochronous TX buffers）

**说明（Help）**

可用于发送等时信道 SDU（Isochronous channel SDUs）的缓冲区数量。

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

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:352`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L352)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_ISO`。

<a id="CONFIG_BT_ISO_TX_MTU"></a>

## 327.3 `CONFIG_BT_ISO_TX_MTU`

**提示（Prompt）**：等时发送缓冲区支持的最大 MTU（Maximum supported MTU for Isochronous TX buffers）

**说明（Help）**

等时信道发送缓冲区（Isochronous channels TX buffers）的最大传输单元（MTU）。此值表示实际数据有效载荷，不包含 HCI ISO 数据包的可选字段，例如 `struct bt_hci_iso_sdu_ts_hdr`。设为 `247` 时，可在使用时间戳（timestamps）、`Data_Total_Length` 为 `255` 的单个 HCI ISO 数据包中容纳 `247` 字节数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ISO && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
247
```

**取值范围（Ranges）**

```text
[1, 4095]
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:359`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L359)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_ISO`。

<a id="CONFIG_BT_ISO_UNICAST"></a>

## 327.4 `CONFIG_BT_ISO_UNICAST`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用蓝牙单播等时信道（Bluetooth Unicast Isochronous channels）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_ISO
CONFIG_BT_ISO_TX
CONFIG_BT_ISO_RX
```

**被选择（Selected by）**

```text
CONFIG_BT_ISO_PERIPHERAL
CONFIG_BT_ISO_CENTRAL
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:286`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L286)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO)、[`CONFIG_BT_ISO_TX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_TX)、[`CONFIG_BT_ISO_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_RX)、[`CONFIG_BT_ISO_PERIPHERAL`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_ISO_PERIPHERAL)、[`CONFIG_BT_ISO_CENTRAL`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_ISO_CENTRAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_ISO`、`CONFIG_BT_ISO_TX`、`CONFIG_BT_ISO_RX`。

<a id="CONFIG_BT_KEYS_OVERWRITE_OLDEST"></a>

## 327.5 `CONFIG_BT_KEYS_OVERWRITE_OLDEST`

**提示（Prompt）**：密钥存储已满时覆盖最旧密钥（Overwrite the oldest key if key storage is full）

**说明（Help）**

当发生配对尝试且密钥存储（key storage）已满时，会从当前未使用的密钥中选择最旧的一个，并由正在配对的设备覆盖。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:789`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L789)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_KEYS_SAVE_AGING_COUNTER_ON_PAIRING"></a>

## 327.6 `CONFIG_BT_KEYS_SAVE_AGING_COUNTER_ON_PAIRING`

**提示（Prompt）**：每次成功配对后存储老化计数器（Store aging counter after successful pairing）

**说明（Help）**

启用后，每次配对成功都会将老化计数器（aging counter）保存到设置存储（settings）。这会增加 Flash 磨损，但能更准确地找到最旧且未使用的配对信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SETTINGS && CONFIG_BT_KEYS_OVERWRITE_OLDEST && CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:796`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L796)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support） → 密钥存储已满时覆盖最旧密钥（Overwrite the oldest key if key storage is full）

**配置项引用（Symbol References）**：[`CONFIG_BT_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SETTINGS)、[`CONFIG_BT_KEYS_OVERWRITE_OLDEST`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_KEYS_OVERWRITE_OLDEST)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_L2CAP_BR_MONITOR_TIMEOUT"></a>

## 327.7 `CONFIG_BT_L2CAP_BR_MONITOR_TIMEOUT`

**提示（Prompt）**：监视超时，单位为毫秒（Monitor timeout）

**说明（Help）**

对于增强重传模式（Enhanced Retransmission mode），如果链路存在刷新超时（flush timeout），且双方配置了相同的刷新超时值，则监视超时（Monitor timeout）至少应与重传超时（Retransmission timeout）一样大。否则，监视超时应为刷新超时的 `6` 倍，并受下限为重传超时值、上限为 `12000` 毫秒的限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_L2CAP_RET_FC && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
12000 if CONFIG_BT_L2CAP_ENH_RET
CONFIG_BT_L2CAP_BR_RET_TIMEOUT
```

**取值范围（Ranges）**

```text
[CONFIG_BT_L2CAP_BR_RET_TIMEOUT, 12000]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_L2CAP_RET_FC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_RET_FC)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_L2CAP_ENH_RET`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_L2CAP_ENH_RET)、[`CONFIG_BT_L2CAP_BR_RET_TIMEOUT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_L2CAP_BR_RET_TIMEOUT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_L2CAP_RET_FC`。

<a id="CONFIG_BT_L2CAP_BR_RET_TIMEOUT"></a>

## 327.8 `CONFIG_BT_L2CAP_BR_RET_TIMEOUT`

**提示（Prompt）**：重传超时，单位为毫秒（Retransmission timeout）

**说明（Help）**

重传超时（Retransmission timeout）应为刷新超时（flush timeout）的 `3` 倍，下限为 `1000` 毫秒，上限为 `2000` 毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_L2CAP_RET_FC && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2000
```

**取值范围（Ranges）**

```text
[1000, 2000]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:142`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L142)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_L2CAP_RET_FC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_RET_FC)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_L2CAP_RET_FC`。

<a id="CONFIG_BT_L2CAP_CONNLESS"></a>

## 327.9 `CONFIG_BT_L2CAP_CONNLESS`

**提示（Prompt）**：蓝牙 L2CAP 无连接数据接收（connectionless data reception）[实验性，EXPERIMENTAL]

**说明（Help）**

启用蓝牙 L2CAP 无连接数据接收（connectionless data reception）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_BT_L2CAP_CONN_RTX_TIMEOUT"></a>

## 327.10 `CONFIG_BT_L2CAP_CONN_RTX_TIMEOUT`

**提示（Prompt）**：连接请求的 L2CAP RTX 定时器，单位为秒（L2CAP RTX timer for conn requests）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
40
```

**取值范围（Ranges）**

```text
[1, 60]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.l2cap:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.l2cap#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → L2CAP 选项（L2CAP Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_L2CAP_DYNAMIC_CHANNEL"></a>

## 327.11 `CONFIG_BT_L2CAP_DYNAMIC_CHANNEL`

**提示（Prompt）**：L2CAP 动态信道支持（L2CAP Dynamic Channel support）

**说明（Help）**

启用低功耗蓝牙面向连接信道（LE Connection oriented Channels）支持，允许创建动态 L2CAP 信道（Dynamic L2CAP Channels）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_OTS
CONFIG_BT_OTS_CLIENT
CONFIG_BT_CLASSIC
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.l2cap:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.l2cap#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → L2CAP 选项（L2CAP Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_OTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OTS)、[`CONFIG_BT_OTS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OTS_CLIENT)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_L2CAP_ECRED"></a>

## 327.12 `CONFIG_BT_L2CAP_ECRED`

**提示（Prompt）**：L2CAP 增强型基于信用的流控支持（Enhanced Credit Based Flow Control）

**说明（Help）**

为动态 L2CAP 信道启用具有增强型基于信用的流控（Enhanced Credit Based Flow Control）能力的低功耗蓝牙面向连接信道（LE Connection oriented Channels）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_L2CAP_DYNAMIC_CHANNEL && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.l2cap:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.l2cap#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → L2CAP 选项（L2CAP Options） → L2CAP 动态信道支持（L2CAP Dynamic Channel support）

**配置项引用（Symbol References）**：[`CONFIG_BT_L2CAP_DYNAMIC_CHANNEL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_L2CAP_DYNAMIC_CHANNEL)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_L2CAP_ENH_RET"></a>

## 327.13 `CONFIG_BT_L2CAP_ENH_RET`

**提示（Prompt）**：蓝牙 L2CAP 增强重传（enhanced retransmission）[实验性，EXPERIMENTAL]

**说明（Help）**

启用蓝牙 L2CAP 增强重传（enhanced retransmission）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_BT_AVRCP_BROWSING
CONFIG_BT_GOEP
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_AVRCP_BROWSING`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AVRCP_BROWSING)、[`CONFIG_BT_GOEP`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_GOEP)。

<a id="CONFIG_BT_L2CAP_EXT_WIN_SIZE"></a>

## 327.14 `CONFIG_BT_L2CAP_EXT_WIN_SIZE`

**提示（Prompt）**：蓝牙 L2CAP 扩展窗口大小选项（Extended window size Option）[实验性，EXPERIMENTAL]

**说明（Help）**

启用蓝牙 L2CAP 扩展窗口大小选项（Extended window size Option）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_L2CAP_STREAM || CONFIG_BT_L2CAP_ENH_RET) && CONFIG_BT_L2CAP_RET_FC && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_L2CAP_STREAM`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_L2CAP_STREAM)、[`CONFIG_BT_L2CAP_ENH_RET`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_L2CAP_ENH_RET)、[`CONFIG_BT_L2CAP_RET_FC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_RET_FC)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_L2CAP_RET_FC`。

<a id="CONFIG_BT_L2CAP_FC"></a>

## 327.15 `CONFIG_BT_L2CAP_FC`

**提示（Prompt）**：蓝牙 L2CAP 流控模式（flow control mode）[实验性，EXPERIMENTAL]

**说明（Help）**

启用蓝牙 L2CAP 流控模式（flow control mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_BT_L2CAP_FCS"></a>

## 327.16 `CONFIG_BT_L2CAP_FCS`

**提示（Prompt）**：蓝牙 L2CAP 帧校验序列选项（FCS Option）[实验性，EXPERIMENTAL]

**说明（Help）**

启用蓝牙 L2CAP 帧校验序列选项（FCS Option）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_L2CAP_STREAM || CONFIG_BT_L2CAP_ENH_RET) && CONFIG_BT_L2CAP_RET_FC && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_L2CAP_STREAM`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_L2CAP_STREAM)、[`CONFIG_BT_L2CAP_ENH_RET`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_L2CAP_ENH_RET)、[`CONFIG_BT_L2CAP_RET_FC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_RET_FC)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_L2CAP_RET_FC`。

<a id="CONFIG_BT_L2CAP_MAX_WINDOW_SIZE"></a>

## 327.17 `CONFIG_BT_L2CAP_MAX_WINDOW_SIZE`

**提示（Prompt）**：重传与流控的最大窗口大小（Maximum Windows Size of Retransmission and Flow Control）

**说明（Help）**

重传（Retransmission）与流控（Flow Control）的最大窗口大小。最小值也是默认值，为 `1`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_L2CAP_RET_FC && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_L2CAP_RET_FC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_RET_FC)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_L2CAP_RET_FC`。

<a id="CONFIG_BT_L2CAP_MPS"></a>

## 327.18 `CONFIG_BT_L2CAP_MPS`

**提示（Prompt）**：蓝牙 L2CAP 重传与流控的 MPS（MPS for retransmission and Flow control）

**说明（Help）**

蓝牙 L2CAP 重传与流控的 MPS（MPS for retransmission and Flow control）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_L2CAP_RET_FC && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
48
```

**取值范围（Ranges）**

```text
[48, CONFIG_BT_L2CAP_TX_MTU]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_L2CAP_RET_FC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_RET_FC)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_L2CAP_TX_MTU`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_L2CAP_TX_MTU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_L2CAP_RET_FC`。

<a id="CONFIG_BT_L2CAP_QOS"></a>

## 327.19 `CONFIG_BT_L2CAP_QOS`

**提示（Prompt）**：蓝牙 L2CAP 服务质量选项（QoS Option）[实验性，EXPERIMENTAL]

**说明（Help）**

允许协商蓝牙 L2CAP 服务质量（QoS）配置选项。仅支持尽力而为服务类型（Best Effort）；对端请求有保证服务类型（Guaranteed）时，会反向提议 Best Effort。如果未启用此选项，配置请求（Configuration Request）中的 QoS 选项会得到未知选项（Unknown Option）响应。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_BT_L2CAP_RECONFIGURE_EXPLICIT"></a>

## 327.20 `CONFIG_BT_L2CAP_RECONFIGURE_EXPLICIT`

**提示（Prompt）**：L2CAP 显式重新配置 API（Explicit reconfigure API）[实验性，EXPERIMENTAL]

**说明（Help）**

启用用于显式重新配置 L2CAP 信道 MTU 与 MPS 的 API（explicit reconfiguration API）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.l2cap:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.l2cap#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → L2CAP 选项（L2CAP Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_L2CAP_RET"></a>

## 327.21 `CONFIG_BT_L2CAP_RET`

**提示（Prompt）**：蓝牙 L2CAP 重传模式（retransmission mode）[实验性，EXPERIMENTAL]

**说明（Help）**

启用蓝牙 L2CAP 重传模式（retransmission mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_BT_L2CAP_RX_FLUSH_TO"></a>

## 327.22 `CONFIG_BT_L2CAP_RX_FLUSH_TO`

**提示（Prompt）**：接受的最小蓝牙 L2CAP 接收刷新超时，单位为毫秒（minimum L2CAP RX flush Timeout）

**说明（Help）**

配置处理对端 L2CAP 刷新超时配置时，可接受的最小接收刷新超时（RX flush timeout）。刷新超时适用于同一个 ACL 逻辑传输（logical transport）上的全部信道，但可逐包覆盖：通过 HCI ACL 数据包中的 `Packet_Boundary_Flag`，将单个 L2CAP 数据包标记为不可自动刷新（non-automatically-flushable）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x0001 if CONFIG_BT_A2DP_SINK
0xFFFF
```

**取值范围（Ranges）**

```text
[0x0001, 0xFFFF]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_A2DP_SINK`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_A2DP_SINK)。

<a id="CONFIG_BT_L2CAP_SEG_RECV"></a>

## 327.23 `CONFIG_BT_L2CAP_SEG_RECV`

**提示（Prompt）**：L2CAP 直接接收分段 API（Receive segment direct API）[实验性，EXPERIMENTAL]

**说明（Help）**

启用直接接收 L2CAP SDU 分段（segments）的 API，绕过主机固定功能的 SDU 重组器（re-assembler）、接收 SDU 缓冲区管理和信用发放器（credit issuer）。该 API 强制符合 L2CAP 技术规范（TS），除此之外尽可能保持灵活性和语义简单性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.l2cap:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.l2cap#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → L2CAP 选项（L2CAP Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_L2CAP_STREAM"></a>

## 327.24 `CONFIG_BT_L2CAP_STREAM`

**提示（Prompt）**：蓝牙 L2CAP 流传输模式（streaming mode）[实验性，EXPERIMENTAL]

**说明（Help）**

启用蓝牙 L2CAP 流传输模式（streaming mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_BT_L2CAP_TX_BUF_COUNT"></a>

## 327.25 `CONFIG_BT_L2CAP_TX_BUF_COUNT`

**提示（Prompt）**：L2CAP 发送缓冲区数量（Number of L2CAP TX buffers）

**说明（Help）**

可用于发送 L2CAP 数据包的缓冲区数量（TX buffers）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BUF_ACL_TX_COUNT
```

**取值范围（Ranges）**

```text
[2, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.l2cap:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.l2cap#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → L2CAP 选项（L2CAP Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BUF_ACL_TX_COUNT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BUF_ACL_TX_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_L2CAP_TX_FRAG_COUNT"></a>

## 327.26 `CONFIG_BT_L2CAP_TX_FRAG_COUNT`

**提示（Prompt）**：L2CAP 发送分片缓冲区数量（Number of L2CAP TX fragment buffers）

**说明（Help）**

可用于保存发送缓冲区分片（fragments of TX buffers）的缓冲区数量。警告：设为 `0` 意味着应用必须确保已入队的发送缓冲区永远不需要分片，即控制器缓冲区必须足够大。如果无法保证这一点，且没有专用分片缓冲区（fragment buffers），可能发生死锁（deadlock）。大多数情况下，默认值 `2` 是稳妥的选择。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.l2cap:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.l2cap#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → L2CAP 选项（L2CAP Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_L2CAP_TX_MTU"></a>

## 327.27 `CONFIG_BT_L2CAP_TX_MTU`

**提示（Prompt）**：L2CAP 发送缓冲区支持的最大 L2CAP MTU（Maximum supported L2CAP MTU）

**说明（Help）**

L2CAP 发送缓冲区（TX buffers）的最大 L2CAP MTU。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
253 if CONFIG_BT_CLASSIC
66 if CONFIG_BT_EATT
65 if CONFIG_BT_SMP
64 if CONFIG_BT_BAP_UNICAST_SERVER || CONFIG_BT_BAP_UNICAST_CLIENT || CONFIG_BT_BAP_BROADCAST_SINK || CONFIG_BT_BAP_SCAN_DELEGATOR || CONFIG_BT_BAP_BROADCAST_ASSISTANT
49 if CONFIG_BT_HAS || CONFIG_BT_HAS_CLIENT
33 if CONFIG_BT_MESH_GATT
23
```

**取值范围（Ranges）**

```text
[66, 2000] if CONFIG_BT_EATT
[65, 2000] if CONFIG_BT_SMP
[23, 2000]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.l2cap:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.l2cap#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → L2CAP 选项（L2CAP Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_EATT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_EATT)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_BAP_UNICAST_SERVER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAP_UNICAST_SERVER)、[`CONFIG_BT_BAP_UNICAST_CLIENT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAP_UNICAST_CLIENT)、[`CONFIG_BT_BAP_BROADCAST_SINK`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_SINK)、[`CONFIG_BT_BAP_SCAN_DELEGATOR`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_SCAN_DELEGATOR)、[`CONFIG_BT_BAP_BROADCAST_ASSISTANT`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT)、[`CONFIG_BT_HAS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HAS)、[`CONFIG_BT_HAS_CLIENT`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HAS_CLIENT)、[`CONFIG_BT_MESH_GATT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_MESH_GATT`。

<a id="CONFIG_BT_LE_EXTENDED_FEAT_SET"></a>

## 327.28 `CONFIG_BT_LE_EXTENDED_FEAT_SET`

**提示（Prompt）**：链路层扩展功能集（LL Extended Feature Set）

**说明（Help）**

启用链路层扩展功能集（LL Extended Feature Set）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_EXTENDED_FEAT_SET_SUPPORT) && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_EXTENDED_FEAT_SET_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_EXTENDED_FEAT_SET_SUPPORT)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_EXTENDED_FEAT_SET_SUPPORT`。

<a id="CONFIG_BT_LE_LOCAL_MINIMUM_REQUIRED_FEATURE_PAGE"></a>

## 327.29 `CONFIG_BT_LE_LOCAL_MINIMUM_REQUIRED_FEATURE_PAGE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

必须支持的最小功能页（minimum required feature page）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LE_EXTENDED_FEAT_SET && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1 if CONFIG_BT_FRAME_SPACE_UPDATE || CONFIG_BT_SHORTER_CONNECTION_INTERVALS
0
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_LE_EXTENDED_FEAT_SET`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LE_EXTENDED_FEAT_SET)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_FRAME_SPACE_UPDATE`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_FRAME_SPACE_UPDATE)、[`CONFIG_BT_SHORTER_CONNECTION_INTERVALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SHORTER_CONNECTION_INTERVALS)。

<a id="CONFIG_BT_LE_MAX_LOCAL_SUPPORTED_FEATURE_PAGE"></a>

## 327.30 `CONFIG_BT_LE_MAX_LOCAL_SUPPORTED_FEATURE_PAGE`

**提示（Prompt）**：支持的最大功能页（Maximum supported feature page）

**说明（Help）**

可为本地支持功能存储的最大功能页（feature page）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LE_EXTENDED_FEAT_SET && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_LE_LOCAL_MINIMUM_REQUIRED_FEATURE_PAGE
```

**取值范围（Ranges）**

```text
[CONFIG_BT_LE_LOCAL_MINIMUM_REQUIRED_FEATURE_PAGE, 10]
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_LE_EXTENDED_FEAT_SET`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LE_EXTENDED_FEAT_SET)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_LE_LOCAL_MINIMUM_REQUIRED_FEATURE_PAGE`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LE_LOCAL_MINIMUM_REQUIRED_FEATURE_PAGE)。

<a id="CONFIG_BT_LIMITED_DISCOVERABLE_DURATION"></a>

## 327.31 `CONFIG_BT_LIMITED_DISCOVERABLE_DURATION`

**提示（Prompt）**：设备处于有限可发现模式的最长持续时间，单位为秒（limited discoverable mode）

**说明（Help）**

设置设备处于有限可发现模式（limited discoverable mode）的最长持续时间，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
60
```

**取值范围（Ranges）**

```text
[31, 60]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_LIM_ADV_TIMEOUT"></a>

## 327.32 `CONFIG_BT_LIM_ADV_TIMEOUT`

**提示（Prompt）**：有限广播超时，以 1 秒为单位（Timeout for limited advertising）

**说明（Help）**

达到该超时后，设置了 `BT_LE_AD_LIMITED` 标志的广播应终止。按照 BT Core Spec 5.2, Vol 3, Part C, Appendix A（规范性附录，NORMATIVE）“定时器与常量”（TIMERS AND CONSTANTS）的要求，该值不得超过 `180s`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_BROADCASTER && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[1, 180]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:288`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L288)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_LLL_VENDOR_NORDIC"></a>

## 327.33 `CONFIG_BT_LLL_VENDOR_NORDIC`

**提示（Prompt）**：使用 Nordic 下层链路层（Use Nordic LLL）

**说明（Help）**

使用 Nordic 下层链路层（Lower Link Layer）实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_COMPATIBLE_NRF && !n && !n && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_CTLR_ENTROPY_SUPPORT
CONFIG_ENTROPY_NRF5_RNG if CONFIG_BT_CTLR_ENTROPY && !CONFIG_SOC_COMPATIBLE_NRF54LX
CONFIG_ENTROPY_NRF5_BIAS_CORRECTION if CONFIG_ENTROPY_NRF5_RNG
CONFIG_EXPERIMENTAL if !CONFIG_ENTROPY_HAS_DRIVER
CONFIG_BT_HAS_HCI_VS
CONFIG_BT_HCI_VS_FATAL_ERROR_SUPPORT
CONFIG_BT_CTLR_CRYPTO_SUPPORT
CONFIG_BT_CTLR_LE_ENC_SUPPORT if CONFIG_BT_CTLR_CRYPTO_SUPPORT && !CONFIG_BT_CTLR_DATA_LENGTH_CLEAR && !CONFIG_BT_CTLR_PHY_2M_NRF
CONFIG_BT_CTLR_PRIVACY_SUPPORT if CONFIG_BT_CTLR_CRYPTO_SUPPORT && !CONFIG_SOC_SERIES_NRF51
CONFIG_BT_CTLR_CONN_PARAM_REQ_SUPPORT
CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT
CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG_SUPPORT
CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT if !CONFIG_BT_CTLR_LE_ENC_SUPPORT || CONFIG_HAS_HW_NRF_CCM_LFLEN_8BIT || CONFIG_SOC_COMPATIBLE_NRF54LX || CONFIG_BT_CTLR_DATA_LENGTH_CLEAR
CONFIG_BT_CTLR_EXT_SCAN_FP_SUPPORT
CONFIG_BT_CTLR_PHY_2M_SUPPORT if CONFIG_HAS_HW_NRF_RADIO_BLE_2M || CONFIG_BT_CTLR_PHY_2M_NRF
CONFIG_BT_CTLR_PHY_CODED_SUPPORT if CONFIG_HAS_HW_NRF_RADIO_BLE_CODED
CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT if CONFIG_BT_CTLR_PHY_2M_SUPPORT || CONFIG_BT_CTLR_PHY_CODED_SUPPORT
CONFIG_BT_CTLR_ADV_EXT_SUPPORT
CONFIG_BT_CTLR_ADV_PERIODIC_SUPPORT
CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT
CONFIG_BT_CTLR_ADV_ISO_SUPPORT
CONFIG_BT_CTLR_SYNC_ISO_SUPPORT
CONFIG_BT_CTLR_BROADCAST_ISO_ENC_SUPPORT
CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT
CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT
CONFIG_BT_CTLR_DF_SUPPORT if CONFIG_HAS_HW_NRF_RADIO_DFE
CONFIG_BT_CTLR_CTEINLINE_SUPPORT if CONFIG_HAS_HW_NRF_RADIO_DFE
CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT
CONFIG_BT_CTLR_MIN_USED_CHAN_SUPPORT
CONFIG_BT_CTLR_SCA_UPDATE_SUPPORT
CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT
CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT
CONFIG_BT_CTLR_DTM_HCI_SUPPORT
CONFIG_BT_CTLR_CONN_RSSI_SUPPORT
CONFIG_BT_CTLR_XTAL_ADVANCED_SUPPORT
CONFIG_BT_CTLR_SCHED_ADVANCED_SUPPORT
CONFIG_BT_CTLR_TIFS_HW_SUPPORT
CONFIG_BT_CTLR_ULL_LLL_PRIO_SUPPORT
CONFIG_BT_TICKER_REMAINDER_SUPPORT if !CONFIG_SOC_COMPATIBLE_NRF54LX
CONFIG_BT_TICKER_UPDATE if CONFIG_BT_BROADCASTER || CONFIG_BT_CONN || (CONFIG_BT_OBSERVER && CONFIG_BT_CTLR_ADV_EXT)
CONFIG_BT_TICKER_START_REMAINDER if CONFIG_BT_TICKER_REMAINDER_SUPPORT && CONFIG_BT_CTLR_CENTRAL_ISO
CONFIG_BT_TICKER_REMAINDER_GET if CONFIG_BT_TICKER_REMAINDER_SUPPORT && CONFIG_BT_BROADCASTER && CONFIG_BT_CTLR_ADV_EXT
CONFIG_BT_TICKER_LAZY_GET if CONFIG_BT_CTLR_ADV_PERIODIC || CONFIG_BT_CTLR_CONN_ISO || CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER
CONFIG_BT_TICKER_NEXT_SLOT_GET if (CONFIG_BT_BROADCASTER && CONFIG_BT_CTLR_ADV_EXT) || CONFIG_BT_CENTRAL || CONFIG_BT_CTLR_CONN_ISO
CONFIG_BT_TICKER_NEXT_SLOT_GET_MATCH if (CONFIG_BT_BROADCASTER && CONFIG_BT_CTLR_ADV_EXT) || CONFIG_BT_CENTRAL || CONFIG_BT_CTLR_CONN_ISO
CONFIG_BT_TICKER_CNTR_FREE_RUNNING if CONFIG_SOC_COMPATIBLE_NRF54LX
CONFIG_BT_TICKER_PREFER_START_BEFORE_STOP if CONFIG_BT_TICKER_SLOT_AGNOSTIC
CONFIG_BT_CTLR_ASSERT_OPTIMIZE_FOR_SIZE_SUPPORT if CONFIG_CPU_CORTEX_M
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)、[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_ENTROPY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ENTROPY_SUPPORT)、[`CONFIG_ENTROPY_NRF5_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NRF5_RNG)、[`CONFIG_BT_CTLR_ENTROPY`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ENTROPY)、[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_ENTROPY_NRF5_BIAS_CORRECTION`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NRF5_BIAS_CORRECTION)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_BT_HAS_HCI_VS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HAS_HCI_VS)、[`CONFIG_BT_HCI_VS_FATAL_ERROR_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_VS_FATAL_ERROR_SUPPORT)、[`CONFIG_BT_CTLR_CRYPTO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CRYPTO_SUPPORT)、[`CONFIG_BT_CTLR_LE_ENC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_LE_ENC_SUPPORT)、[`CONFIG_BT_CTLR_DATA_LENGTH_CLEAR`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DATA_LENGTH_CLEAR)、[`CONFIG_BT_CTLR_PHY_2M_NRF`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_PHY_2M_NRF)、[`CONFIG_BT_CTLR_PRIVACY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PRIVACY_SUPPORT)、[`CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_BT_CTLR_CONN_PARAM_REQ_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_PARAM_REQ_SUPPORT)、[`CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT)、[`CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG_SUPPORT)、[`CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT)、[`CONFIG_HAS_HW_NRF_CCM_LFLEN_8BIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_CCM_LFLEN_8BIT)、[`CONFIG_BT_CTLR_EXT_SCAN_FP_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_EXT_SCAN_FP_SUPPORT)、[`CONFIG_BT_CTLR_PHY_2M_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_2M_SUPPORT)、[`CONFIG_HAS_HW_NRF_RADIO_BLE_2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_RADIO_BLE_2M)、[`CONFIG_BT_CTLR_PHY_CODED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_CODED_SUPPORT)、[`CONFIG_HAS_HW_NRF_RADIO_BLE_CODED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_RADIO_BLE_CODED)、[`CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT)、[`CONFIG_BT_CTLR_ADV_EXT_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_EXT_SUPPORT)、[`CONFIG_BT_CTLR_ADV_PERIODIC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_PERIODIC_SUPPORT)、[`CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT)、[`CONFIG_BT_CTLR_ADV_ISO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_ISO_SUPPORT)、[`CONFIG_BT_CTLR_SYNC_ISO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_ISO_SUPPORT)、[`CONFIG_BT_CTLR_BROADCAST_ISO_ENC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_BROADCAST_ISO_ENC_SUPPORT)、[`CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT)、[`CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT)、[`CONFIG_BT_CTLR_DF_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_SUPPORT)、[`CONFIG_HAS_HW_NRF_RADIO_DFE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_RADIO_DFE)、[`CONFIG_BT_CTLR_CTEINLINE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CTEINLINE_SUPPORT)、[`CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT)、[`CONFIG_BT_CTLR_MIN_USED_CHAN_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_MIN_USED_CHAN_SUPPORT)、[`CONFIG_BT_CTLR_SCA_UPDATE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SCA_UPDATE_SUPPORT)、[`CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT)、[`CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT)、[`CONFIG_BT_CTLR_DTM_HCI_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DTM_HCI_SUPPORT)、[`CONFIG_BT_CTLR_CONN_RSSI_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_RSSI_SUPPORT)、[`CONFIG_BT_CTLR_XTAL_ADVANCED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_XTAL_ADVANCED_SUPPORT)、[`CONFIG_BT_CTLR_SCHED_ADVANCED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SCHED_ADVANCED_SUPPORT)、[`CONFIG_BT_CTLR_TIFS_HW_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_TIFS_HW_SUPPORT)、[`CONFIG_BT_CTLR_ULL_LLL_PRIO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ULL_LLL_PRIO_SUPPORT)、[`CONFIG_BT_TICKER_REMAINDER_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_REMAINDER_SUPPORT)、[`CONFIG_BT_TICKER_UPDATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_UPDATE)、[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_BT_TICKER_START_REMAINDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_START_REMAINDER)、[`CONFIG_BT_CTLR_CENTRAL_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_CENTRAL_ISO)、[`CONFIG_BT_TICKER_REMAINDER_GET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_REMAINDER_GET)、[`CONFIG_BT_TICKER_LAZY_GET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_LAZY_GET)、[`CONFIG_BT_CTLR_ADV_PERIODIC`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_PERIODIC)、[`CONFIG_BT_CTLR_CONN_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_ISO)、[`CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER)、[`CONFIG_BT_TICKER_NEXT_SLOT_GET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_NEXT_SLOT_GET)、[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BT_TICKER_NEXT_SLOT_GET_MATCH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_NEXT_SLOT_GET_MATCH)、[`CONFIG_BT_TICKER_CNTR_FREE_RUNNING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_CNTR_FREE_RUNNING)、[`CONFIG_BT_TICKER_PREFER_START_BEFORE_STOP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_PREFER_START_BEFORE_STOP)、[`CONFIG_BT_TICKER_SLOT_AGNOSTIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_SLOT_AGNOSTIC)、[`CONFIG_BT_CTLR_ASSERT_OPTIMIZE_FOR_SIZE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ASSERT_OPTIMIZE_FOR_SIZE_SUPPORT)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF`、`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_ENTROPY_SUPPORT`、`CONFIG_SOC_COMPATIBLE_NRF54LX`、`CONFIG_BT_HCI_VS_FATAL_ERROR_SUPPORT`、`CONFIG_BT_CTLR_CRYPTO_SUPPORT`、`CONFIG_BT_CTLR_LE_ENC_SUPPORT`、`CONFIG_BT_CTLR_PRIVACY_SUPPORT`、`CONFIG_BT_CTLR_CONN_PARAM_REQ_SUPPORT`、`CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT`、`CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG_SUPPORT`、`CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT`、`CONFIG_HAS_HW_NRF_CCM_LFLEN_8BIT`、`CONFIG_BT_CTLR_EXT_SCAN_FP_SUPPORT`、`CONFIG_BT_CTLR_PHY_2M_SUPPORT`、`CONFIG_HAS_HW_NRF_RADIO_BLE_2M`、`CONFIG_BT_CTLR_PHY_CODED_SUPPORT`、`CONFIG_HAS_HW_NRF_RADIO_BLE_CODED`、`CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT`、`CONFIG_BT_CTLR_ADV_EXT_SUPPORT`、`CONFIG_BT_CTLR_ADV_PERIODIC_SUPPORT`、`CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT`、`CONFIG_BT_CTLR_ADV_ISO_SUPPORT`、`CONFIG_BT_CTLR_SYNC_ISO_SUPPORT`、`CONFIG_BT_CTLR_BROADCAST_ISO_ENC_SUPPORT`、`CONFIG_BT_CTLR_CENTRAL_ISO_SUPPORT`、`CONFIG_BT_CTLR_PERIPHERAL_ISO_SUPPORT`、`CONFIG_BT_CTLR_DF_SUPPORT`、`CONFIG_HAS_HW_NRF_RADIO_DFE`、`CONFIG_BT_CTLR_CTEINLINE_SUPPORT`、`CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT`、`CONFIG_BT_CTLR_MIN_USED_CHAN_SUPPORT`、`CONFIG_BT_CTLR_SCA_UPDATE_SUPPORT`、`CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT`、`CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT`、`CONFIG_BT_CTLR_DTM_HCI_SUPPORT`、`CONFIG_BT_CTLR_CONN_RSSI_SUPPORT`、`CONFIG_BT_CTLR_XTAL_ADVANCED_SUPPORT`、`CONFIG_BT_CTLR_SCHED_ADVANCED_SUPPORT`、`CONFIG_BT_CTLR_TIFS_HW_SUPPORT`、`CONFIG_BT_CTLR_ULL_LLL_PRIO_SUPPORT`、`CONFIG_BT_TICKER_REMAINDER_SUPPORT`、`CONFIG_BT_CTLR_CONN_ISO`、`CONFIG_BT_TICKER_CNTR_FREE_RUNNING`、`CONFIG_BT_CTLR_ASSERT_OPTIMIZE_FOR_SIZE_SUPPORT`。

<a id="CONFIG_BT_LLL_VENDOR_OPENISA"></a>

## 327.34 `CONFIG_BT_LLL_VENDOR_OPENISA`

**提示（Prompt）**：使用 OpenISA 下层链路层（Use OpenISA LLL）

**说明（Help）**

使用 OpenISA 下层链路层（Lower Link Layer）实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_OPENISA_RV32M1 && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_HAS_HCI_VS
CONFIG_BT_CTLR_ENTROPY_SUPPORT
CONFIG_BT_CTLR_CRYPTO_SUPPORT
CONFIG_BT_CTLR_LE_ENC_SUPPORT if CONFIG_BT_CTLR_CRYPTO_SUPPORT && !CONFIG_BT_CTLR_DATA_LENGTH_CLEAR
CONFIG_BT_CTLR_PRIVACY_SUPPORT if CONFIG_BT_CTLR_CRYPTO_SUPPORT
CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT
CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT
CONFIG_BT_TICKER_REMAINDER_SUPPORT
CONFIG_BT_TICKER_UPDATE if CONFIG_BT_BROADCASTER || CONFIG_BT_CONN
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_SOC_OPENISA_RV32M1`](P298_soc_openisa_配置项参考.md#CONFIG_SOC_OPENISA_RV32M1)、[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HAS_HCI_VS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HAS_HCI_VS)、[`CONFIG_BT_CTLR_ENTROPY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ENTROPY_SUPPORT)、[`CONFIG_BT_CTLR_CRYPTO_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CRYPTO_SUPPORT)、[`CONFIG_BT_CTLR_LE_ENC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_LE_ENC_SUPPORT)、[`CONFIG_BT_CTLR_DATA_LENGTH_CLEAR`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_DATA_LENGTH_CLEAR)、[`CONFIG_BT_CTLR_PRIVACY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PRIVACY_SUPPORT)、[`CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT)、[`CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT)、[`CONFIG_BT_TICKER_REMAINDER_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_REMAINDER_SUPPORT)、[`CONFIG_BT_TICKER_UPDATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_UPDATE)、[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_ENTROPY_SUPPORT`、`CONFIG_BT_CTLR_CRYPTO_SUPPORT`、`CONFIG_BT_CTLR_LE_ENC_SUPPORT`、`CONFIG_BT_CTLR_PRIVACY_SUPPORT`、`CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT`、`CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT`、`CONFIG_BT_TICKER_REMAINDER_SUPPORT`。

<a id="CONFIG_BT_LL_SW_SPLIT"></a>

## 327.35 `CONFIG_BT_LL_SW_SPLIT`

**提示（Prompt）**：基于软件的低功耗蓝牙链路层（Software-based Bluetooth LE Link Layer）

**说明（Help）**

使用 Zephyr 软件低功耗蓝牙链路层（Bluetooth LE Link Layer）的 ULL／LLL 分离式实现（split implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_BT_HCI_LL_SW_SPLIT_ENABLED && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_BT_CTLR
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_LOG_SNIFFER_INFO"></a>

## 327.36 `CONFIG_BT_LOG_SNIFFER_INFO`

**提示（Prompt）**：为嗅探器记录蓝牙信息（Bluetooth log information for sniffer）

**说明（Help）**

允许蓝牙协议栈记录 DH 私钥、长期密钥（LTK）等信息，嗅探器（sniffers）可用这些信息解密连接，而不必使用调试密钥（Debug keys）。警告：此选项会打印包括长期密钥在内的私密安全密钥。强烈不建议在生产环境使用此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1130)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_LONG_WQ"></a>

## 327.37 `CONFIG_BT_LONG_WQ`

**提示（Prompt）**：长时间运行任务的专用工作队列（Dedicated workqueue for long-running tasks）

**说明（Help）**

添加用于长时间运行任务（long-running tasks）专用工作队列的 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_GATT_CACHING
y if CONFIG_BT_ECC
```

**被选择（Selected by）**

```text
CONFIG_BT_MESH_PROV
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:401`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L401)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_GATT_CACHING`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CACHING)、[`CONFIG_BT_ECC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ECC)、[`CONFIG_BT_MESH_PROV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MESH_PROV`。

<a id="CONFIG_BT_LONG_WQ_INIT_PRIO"></a>

## 327.38 `CONFIG_BT_LONG_WQ_INIT_PRIO`

**提示（Prompt）**：长任务工作队列初始化优先级（Long workqueue init priority）

**说明（Help）**

设置长任务工作队列（long workqueue）的初始化优先级（init priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LONG_WQ && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:425`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L425)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 长时间运行任务的专用工作队列（Dedicated workqueue for long-running tasks）

**配置项引用（Symbol References）**：[`CONFIG_BT_LONG_WQ`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LONG_WQ)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_LONG_WQ_PRIO"></a>

## 327.39 `CONFIG_BT_LONG_WQ_PRIO`

**提示（Prompt）**：长任务工作队列优先级，应为可抢占式（Long workqueue priority, preemptible）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LONG_WQ && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, CONFIG_NUM_PREEMPT_PRIORITIES]
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:420`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L420)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 长时间运行任务的专用工作队列（Dedicated workqueue for long-running tasks）

**配置项引用（Symbol References）**：[`CONFIG_BT_LONG_WQ`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LONG_WQ)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_NUM_PREEMPT_PRIORITIES`](P001_kernel_配置项参考_1.md#CONFIG_NUM_PREEMPT_PRIORITIES)。

<a id="CONFIG_BT_LONG_WQ_STACK_SIZE"></a>

## 327.40 `CONFIG_BT_LONG_WQ_STACK_SIZE`

**提示（Prompt）**：长任务工作队列栈大小（Long workqueue stack size）

**说明（Help）**

长任务工作队列（long workqueue）所用的栈大小。大多数情况下最好使用默认值；但实际需求取决于底层密码后端（crypto backend），因此可用此选项微调栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LONG_WQ && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
4096 if CONFIG_NO_OPTIMIZATIONS
1400 if CONFIG_BT_ECC
1300 if CONFIG_BT_GATT_CACHING
1024
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_arduino_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_arduino_wifi_bt/Kconfig.defconfig)。

```text
2560
```

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
2560
```

**定义位置（Location）**：[`subsys/bluetooth/common/Kconfig:409`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/common/Kconfig#L409)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 长时间运行任务的专用工作队列（Dedicated workqueue for long-running tasks）

**配置项引用（Symbol References）**：[`CONFIG_BT_LONG_WQ`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LONG_WQ)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_NO_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NO_OPTIMIZATIONS)、[`CONFIG_BT_ECC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ECC)、[`CONFIG_BT_GATT_CACHING`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CACHING)。

<a id="CONFIG_BT_MAP"></a>

## 327.41 `CONFIG_BT_MAP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用消息访问配置文件（MAP profile）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_GOEP
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_BT_MAP_MCE
CONFIG_BT_MAP_MSE
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:887`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L887)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_GOEP`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_GOEP)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_MAP_MCE`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MAP_MCE)、[`CONFIG_BT_MAP_MSE`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MAP_MSE)。

<a id="CONFIG_BT_MAP_MCE"></a>

## 327.42 `CONFIG_BT_MAP_MCE`

**提示（Prompt）**：蓝牙 MAP 配置文件消息客户端设备功能（Messaging Client Equipment Function）

**说明（Help）**

启用 MAP 配置文件的消息客户端设备功能（messaging client equipment function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_MAP
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:894`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L894)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MAP`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MAP)。

<a id="CONFIG_BT_MAP_MSE"></a>

## 327.43 `CONFIG_BT_MAP_MSE`

**提示（Prompt）**：蓝牙 MAP 配置文件消息服务器设备功能（Messaging Server Equipment Function）

**说明（Help）**

启用 MAP 配置文件的消息服务器设备功能（messaging server equipment function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_MAP
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:900`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L900)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MAP`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MAP)。

<a id="CONFIG_BT_MAX_CONN"></a>

## 327.44 `CONFIG_BT_MAX_CONN`

**提示（Prompt）**：最大同时连接数（Maximum number of simultaneous connections）

**说明（Help）**

支持同时存在的蓝牙连接（Bluetooth connections）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2 if CONFIG_BT_MESH_GATT_CLIENT
1
```

**取值范围（Ranges）**

```text
[1, 250]
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_GATT_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT_CLIENT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MESH_GATT_CLIENT`。

<a id="CONFIG_BT_MAX_PAIRED"></a>

## 327.45 `CONFIG_BT_MAX_PAIRED`

**提示（Prompt）**：已配对设备最大数量（Maximum number of paired devices）

**说明（Help）**

已配对蓝牙设备（paired Bluetooth devices）的最大数量。最小值也是默认值，为 `1`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1 if CONFIG_BT_SMP
0
```

**取值范围（Ranges）**

```text
[1, 250] if CONFIG_BT_SMP
[0, 250]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:818`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L818)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MAX_SCO_CONN"></a>

## 327.46 `CONFIG_BT_MAX_SCO_CONN`

**提示（Prompt）**：最大同时 SCO 连接数（Maximum number of simultaneous SCO connections）

**说明（Help）**

支持同时存在的蓝牙同步连接（Bluetooth synchronous connections）最大数量。最小值也是默认值，为 `1`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 3]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_MAYFLY_YIELD_AFTER_CALL"></a>

## 327.47 `CONFIG_BT_MAYFLY_YIELD_AFTER_CALL`

**提示（Prompt）**：首次调用后从 mayfly 线程让出执行（Yield from mayfly thread after first call）

**说明（Help）**

每次调用只处理一个 mayfly 回调，这是传统行为（legacy behavior）。如果设为 `n`，则在让出执行（yielding）之前，执行被调用方（callee）全部待处理的 mayfly。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1239)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_MCC"></a>

## 327.48 `CONFIG_BT_MCC`

**提示（Prompt）**：媒体控制客户端支持（Media Control Client Support）

**说明（Help）**

启用媒体控制客户端（Media Control Client）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_CLIENT && CONFIG_BT_GATT_AUTO_DISCOVER_CCC && CONFIG_BT_SMP && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_CLIENT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_GATT_AUTO_DISCOVER_CCC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_AUTO_DISCOVER_CCC)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_GROUP_RECORDS_MAX"></a>

## 327.49 `CONFIG_BT_MCC_GROUP_RECORDS_MAX`

**提示（Prompt）**：组对象中的最大记录数（Maximum number of records in a group object）

**说明（Help）**

设置组对象（group object）中的最大记录数。如果收到的组对象包含更多记录，其余记录会被忽略。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC_OTS && CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
25
```

**取值范围（Ranges）**

```text
[0, 500]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support） → 媒体控制客户端的对象传输服务支持（Object Transfer Service）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC_OTS`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_OTS)、[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_ICON_URL_MAX"></a>

## 327.50 `CONFIG_BT_MCC_ICON_URL_MAX`

**提示（Prompt）**：媒体播放器图标 URL 最大长度（Max length of media player icon URL）

**说明（Help）**

设置媒体播放器图标 URL（media player icon URL）的最大字节数，包括空终止符（null termination）。如果 URL 更长，媒体控制客户端会在读取时截断它。

译注：原文后句写为截断“名称（name）”；本条上下文是图标 URL。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
40
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_MEDIA_PLAYER_NAME_MAX"></a>

## 327.51 `CONFIG_BT_MCC_MEDIA_PLAYER_NAME_MAX`

**提示（Prompt）**：媒体播放器名称最大长度（Max length of media player name）

**说明（Help）**

设置媒体播放器名称（media player name）的最大字节数，包括空终止符（null termination）。名称更长时，媒体控制客户端在读取时将其截断。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_MINIMAL"></a>

## 327.52 `CONFIG_BT_MCC_MINIMAL`

**提示（Prompt）**：不含可选过程的最小媒体控制客户端（Minimal Media Control Client）

**说明（Help）**

禁用媒体控制客户端（Media Control Client）中的全部可选过程（optional procedures）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_OTC_OBJ_BUF_SIZE"></a>

## 327.53 `CONFIG_BT_MCC_OTC_OBJ_BUF_SIZE`

**提示（Prompt）**：MCC 中用于 OTC 对象的缓冲区大小（buffer for OTC object in MCC）

**说明（Help）**

设置用于接收对象内容（object content）的缓冲区大小，单位为八位字节（octets）。应设得足够大，以容纳所有预期对象。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC_OTS && CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
512
```

**取值范围（Ranges）**

```text
[1, 65536]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support） → 媒体控制客户端的对象传输服务支持（Object Transfer Service）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC_OTS`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_OTS)、[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_OTS"></a>

## 327.54 `CONFIG_BT_MCC_OTS`

**提示（Prompt）**：媒体控制客户端的对象传输服务支持（Object Transfer Service）

**说明（Help）**

配置媒体控制客户端（Media Control Client）对媒体控制服务（Media Control Service）中所包含对象传输服务（Object Transfer Service）的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OTS_CLIENT && CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OTS_CLIENT)、[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_READ_CONTENT_CONTROL_ID"></a>

## 327.55 `CONFIG_BT_MCC_READ_CONTENT_CONTROL_ID`

**提示（Prompt）**：支持读取内容控制 ID（Content Control ID）

**说明（Help）**

启用内容控制 ID（Content Control ID）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:218`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L218)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_READ_MEDIA_CONTROL_POINT_OPCODES_SUPPORTED"></a>

## 327.56 `CONFIG_BT_MCC_READ_MEDIA_CONTROL_POINT_OPCODES_SUPPORTED`

**提示（Prompt）**：支持读取支持的媒体控制点操作码（Media Control Point Opcodes Supported）

**说明（Help）**

启用“支持的媒体控制点操作码”（Media Control Point Opcodes Supported）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:212`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L212)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_READ_MEDIA_PLAYER_ICON_URL"></a>

## 327.57 `CONFIG_BT_MCC_READ_MEDIA_PLAYER_ICON_URL`

**提示（Prompt）**：支持读取媒体播放器图标 URL（Media Player Icon URL）

**说明（Help）**

允许读取媒体信息过程（Read Media Information procedure）可选择地读取媒体播放器图标 URL（Media Player Icon URL）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_READ_MEDIA_STATE"></a>

## 327.58 `CONFIG_BT_MCC_READ_MEDIA_STATE`

**提示（Prompt）**：支持读取媒体状态（Media State）

**说明（Help）**

启用媒体状态（Media State）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:200`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L200)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_READ_PLAYBACK_SPEED"></a>

## 327.59 `CONFIG_BT_MCC_READ_PLAYBACK_SPEED`

**提示（Prompt）**：支持读取播放速度（Playback Speed）

**说明（Help）**

启用播放速度（Playback Speed）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_READ_PLAYING_ORDER"></a>

## 327.60 `CONFIG_BT_MCC_READ_PLAYING_ORDER`

**提示（Prompt）**：支持读取播放顺序（Playing Order）

**说明（Help）**

启用播放顺序（Playing Order）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L182)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_READ_PLAYING_ORDER_SUPPORTED"></a>

## 327.61 `CONFIG_BT_MCC_READ_PLAYING_ORDER_SUPPORTED`

**提示（Prompt）**：支持读取支持的播放顺序（Playing Order Supported）

**说明（Help）**

启用“支持的播放顺序”（Playing Order Supported）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L194)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_READ_SEEKING_SPEED"></a>

## 327.62 `CONFIG_BT_MCC_READ_SEEKING_SPEED`

**提示（Prompt）**：支持读取搜索速度（Seeking Speed）

**说明（Help）**

启用搜索速度（Seeking Speed）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:176`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L176)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_READ_TRACK_DURATION"></a>

## 327.63 `CONFIG_BT_MCC_READ_TRACK_DURATION`

**提示（Prompt）**：支持读取曲目时长（Track Duration）

**说明（Help）**

启用曲目时长（Track Duration）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_READ_TRACK_POSITION"></a>

## 327.64 `CONFIG_BT_MCC_READ_TRACK_POSITION`

**提示（Prompt）**：支持读取曲目位置（Track Position）

**说明（Help）**

启用曲目位置（Track Position）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_READ_TRACK_TITLE"></a>

## 327.65 `CONFIG_BT_MCC_READ_TRACK_TITLE`

**提示（Prompt）**：支持读取曲目标题（Track Title）

**说明（Help）**

启用曲目标题（Track Title）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_READ_TRACK_TITLE_ENABLE_SUBSCRIPTION"></a>

## 327.66 `CONFIG_BT_MCC_READ_TRACK_TITLE_ENABLE_SUBSCRIPTION`

**提示（Prompt）**：支持启用或禁用曲目标题订阅（subscription of Track Title）

**说明（Help）**

启用曲目标题（Track Title）订阅支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_SEGMENT_NAME_MAX"></a>

## 327.67 `CONFIG_BT_MCC_SEGMENT_NAME_MAX`

**提示（Prompt）**：曲目分段名称最大长度（Max length of name of a track segment）

**说明（Help）**

设置媒体播放器中任意曲目分段名称（track segment name）的最大字节数，包括空终止符（null termination）。名称更长时，媒体控制客户端在读取时将其截断。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
25
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_SET_MEDIA_CONTROL_POINT"></a>

## 327.68 `CONFIG_BT_MCC_SET_MEDIA_CONTROL_POINT`

**提示（Prompt）**：支持设置媒体控制点（Media Control Point）

**说明（Help）**

启用媒体控制点（Media Control Point）设置支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L206)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_SET_PLAYBACK_SPEED"></a>

## 327.69 `CONFIG_BT_MCC_SET_PLAYBACK_SPEED`

**提示（Prompt）**：支持设置播放速度（Playback Speed）

**说明（Help）**

启用播放速度（Playback Speed）设置支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L170)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_SET_PLAYING_ORDER"></a>

## 327.70 `CONFIG_BT_MCC_SET_PLAYING_ORDER`

**提示（Prompt）**：支持设置播放顺序（Playing Order）

**说明（Help）**

启用播放顺序（Playing Order）设置支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:188`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L188)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_SET_TRACK_POSITION"></a>

## 327.71 `CONFIG_BT_MCC_SET_TRACK_POSITION`

**提示（Prompt）**：支持设置曲目位置（Track Position）

**说明（Help）**

启用曲目位置（Track Position）设置支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_MCC_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_MINIMAL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_SHELL"></a>

## 327.72 `CONFIG_BT_MCC_SHELL`

**提示（Prompt）**：媒体控制客户端 Shell 支持（Media Control Client Shell Support）

**说明（Help）**

启用媒体控制客户端（Media Control Client）的 Shell 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_SHELL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SHELL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_TOTAL_OBJ_CONTENT_MEM"></a>

## 327.73 `CONFIG_BT_MCC_TOTAL_OBJ_CONTENT_MEM`

**提示（Prompt）**：存储对象内容的总内存大小（Total memory size for object content）

**说明（Help）**

设置存储对象内容（object content）的总内存大小，单位为八位字节（octets）。它决定总内存池缓冲区大小，读取对象内容时从该池分配内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC_OTS && CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 65536]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support） → 媒体控制客户端的对象传输服务支持（Object Transfer Service）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC_OTS`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_OTS)、[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_TRACK_SEGS_MAX_CNT"></a>

## 327.74 `CONFIG_BT_MCC_TRACK_SEGS_MAX_CNT`

**提示（Prompt）**：曲目分段对象中的最大曲目分段数（track segments in a track segment object）

**说明（Help）**

设置曲目分段对象（track segment object）中的最大曲目分段数。如果收到的对象更大，其余数据会被忽略。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC_OTS && CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
25
```

**取值范围（Ranges）**

```text
[0, 500]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support） → 媒体控制客户端的对象传输服务支持（Object Transfer Service）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC_OTS`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC_OTS)、[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCC_TRACK_TITLE_MAX"></a>

## 327.75 `CONFIG_BT_MCC_TRACK_TITLE_MAX`

**提示（Prompt）**：曲目标题最大长度（Max length of the title of a track）

**说明（Help）**

设置媒体播放器中任意曲目标题（track title）的最大字节数，包括空终止符（null termination）。标题更长时，媒体控制客户端在读取时将其截断。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
40
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体控制客户端支持（Media Control Client Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MCS"></a>

## 327.76 `CONFIG_BT_MCS`

**提示（Prompt）**：媒体控制服务支持（Media Control Service Support）

**说明（Help）**

启用媒体控制服务（Media Control Service）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCTL_LOCAL_PLAYER_REMOTE_CONTROL && CONFIG_BT_GATT_DYNAMIC_DB && CONFIG_BT_SMP && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mcs:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mcs#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_MCTL_LOCAL_PLAYER_REMOTE_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCTL_LOCAL_PLAYER_REMOTE_CONTROL)、[`CONFIG_BT_GATT_DYNAMIC_DB`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_DYNAMIC_DB)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH"></a>

## 327.77 `CONFIG_BT_MESH`

**提示（Prompt）**：蓝牙 Mesh 支持（Bluetooth Mesh support）

**说明（Help）**

启用蓝牙 Mesh（Bluetooth Mesh）支持。具体可用功能可能依赖协议栈已启用的其他功能，例如 GATT 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_BROADCASTER && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_POLL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER)、[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_POLL`](P002_kernel_配置项参考_2.md#CONFIG_POLL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG"></a>

## 327.78 `CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG`

**提示（Prompt）**：接入层可延迟发送消息（Access layer TX delayable message）

**说明（Help）**

启用对接入层规范（Access layer specification）中消息发送建议的遵循。这些建议是可选的，但如果设备参与通信密集的网络，接收到大量需要响应的请求，则强烈建议遵循。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:844`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L844)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 访问层（Access layer）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG_CHUNK_COUNT"></a>

## 327.79 `CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG_CHUNK_COUNT`

**提示（Prompt）**：最大可用块数量（Maximum number of available chunks）

**说明（Help）**

接入层（Access layer）为存储模型有效载荷（model payload）可分配的最大块（chunks）数量。建议将块大小保持在合理的较小值，以避免不必要的内存浪费。

译注：本选项设置块数量；关于块大小的建议来自原帮助文本。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:880`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L880)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 访问层（Access layer） → 接入层可延迟发送消息（Access layer TX delayable message）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG_CHUNK_SIZE"></a>

## 327.80 `CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG_CHUNK_SIZE`

**提示（Prompt）**：可延迟消息存储块最大大小（Maximum delayable message storage chunk）

**说明（Help）**

接入层（Access layer）用于切分模型消息（model message）的内存块大小。接入层会从池中分配足够数量的块（chunks），以保存完整的模型有效载荷（model payload）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:873`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L873)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 访问层（Access layer） → 接入层可延迟发送消息（Access layer TX delayable message）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG_COUNT"></a>

## 327.81 `CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG_COUNT`

**提示（Prompt）**：同时延迟处理的消息数量（Number of simultaneously delayed messages）

**说明（Help）**

接入层（Access layer）能够同时管理延迟发送的消息最大数量。只有接入层有足够内存存储这些消息的模型有效载荷（model payload）时，才能处理该数量的消息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:865`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L865)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 访问层（Access layer） → 接入层可延迟发送消息（Access layer TX delayable message）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG_CTX_ENABLED"></a>

## 327.82 `CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG_CTX_ENABLED`

**提示（Prompt）**：通知消息上下文中的可延迟消息（delayable message in notification message context）

**说明（Help）**

控制是否默认在操作码通知（opcode notifications）的消息上下文中启用可延迟消息（delayable message）功能，使任意模型的服务器部分无需额外配置上下文即可使用该功能。注意：禁用后，所有基础模型（foundation models）都将停止使用可延迟消息功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:855`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L855)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 访问层（Access layer） → 接入层可延迟发送消息（Access layer TX delayable message）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_ACCESS_LAYER_MSG"></a>

## 327.83 `CONFIG_BT_MESH_ACCESS_LAYER_MSG`

**提示（Prompt）**：直接访问蓝牙接入层消息（Direct access to Bluetooth access layer messages）

**说明（Help）**

允许应用直接访问蓝牙接入层消息（Bluetooth access layer messages），无需实例化蓝牙 Mesh 模型（models）。

注意：启用后，对于任何通过网络缓存检查的消息，蓝牙 Mesh 协议栈都会保存其认证序列（authentication sequence），即使设备没有所需的应用密钥，或消息采用未知模型操作码，也会如此。因此，设备可能为协议栈无法处理的消息更新重放保护缓存（replay protection cache）。例如，大量发送协议栈无法处理的广播消息，可能造成持久存储器磨损。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:784`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L784)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 访问层（Access layer）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_ADV"></a>

## 327.84 `CONFIG_BT_MESH_ADV`

**提示（Prompt）**：广播者模式（Advertiser mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_ADV_EXT if CONFIG_BT_EXT_ADV
CONFIG_BT_MESH_ADV_LEGACY
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_ADV_LEGACY
CONFIG_BT_MESH_ADV_EXT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_ADV_EXT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV_EXT)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_MESH_ADV_LEGACY`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_ADV_BUF_COUNT"></a>

## 327.85 `CONFIG_BT_MESH_ADV_BUF_COUNT`

**提示（Prompt）**：本地消息广播缓冲区数量（advertising buffers for local messages）

**说明（Help）**

可用于发送本地消息（local messages）的广播缓冲区数量，应根据节点可同时发送的本地消息数量选择。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
6
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:220`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L220)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_ADV_EXT"></a>

## 327.86 `CONFIG_BT_MESH_ADV_EXT`

**提示（Prompt）**：扩展广播（Extended advertising）

**说明（Help）**

使用扩展广播命令（extended advertising commands）操作广播者（advertiser）。扩展广播比传统广播（legacy advertising）更快、内存消耗更少，但并非所有控制器都支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CTLR_ADV_EXT || !CONFIG_HAS_BT_CTLR) && CONFIG_BT_EXT_ADV && <choice CONFIG_BT_MESH_ADV>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser） → 广播者模式（Advertiser mode）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ADV_EXT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CTLR_ADV_EXT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_MESH_ADV`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_MESH_ADV_EXT_FRIEND_SEPARATE"></a>

## 327.87 `CONFIG_BT_MESH_ADV_EXT_FRIEND_SEPARATE`

**提示（Prompt）**：为 Friend 广播使用独立的扩展广播集合（separate extended advertising set）

**说明（Help）**

为友谊节点广播（Friend advertising）使用独立的扩展广播集合，否则使用共享集合。使用独立集合时，友谊节点（Friend node）可以尽量靠近 `ReceiveWindow` 起点发送友谊消息（friendship messages），从而缩短低功耗节点（Low Power node）的扫描时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_FRIEND && CONFIG_BT_MESH_ADV_EXT && <choice CONFIG_BT_MESH_ADV>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L206)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser） → 广播者模式（Advertiser mode） → 扩展广播（Extended advertising）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_FRIEND`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_FRIEND)、[`CONFIG_BT_MESH_ADV_EXT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV_EXT)、[`CONFIG_BT_MESH_ADV`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV)。

<a id="CONFIG_BT_MESH_ADV_EXT_GATT_SEPARATE"></a>

## 327.88 `CONFIG_BT_MESH_ADV_EXT_GATT_SEPARATE`

**提示（Prompt）**：为 GATT 服务器广播使用独立的扩展广播集合（GATT Server Advertising）

**说明（Help）**

为 GATT 服务器广播（GATT Server Advertising）使用独立的扩展广播集合（extended advertising set），否则使用共享集合。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_GATT_SERVER && CONFIG_BT_MESH_ADV_EXT && <choice CONFIG_BT_MESH_ADV>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:199`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L199)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser） → 广播者模式（Advertiser mode） → 扩展广播（Extended advertising）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_GATT_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT_SERVER)、[`CONFIG_BT_MESH_ADV_EXT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV_EXT)、[`CONFIG_BT_MESH_ADV`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MESH_GATT_SERVER`。

<a id="CONFIG_BT_MESH_ADV_EXT_RELAY_USING_MAIN_ADV_SET"></a>

## 327.89 `CONFIG_BT_MESH_ADV_EXT_RELAY_USING_MAIN_ADV_SET`

**提示（Prompt）**：使用主广播集合中继消息（main advertising set to relay messages）

**说明（Help）**

启用后，当有消息需要中继（relay）、`CONFIG_BT_MESH_RELAY_ADV_SETS` 定义的全部中继广播集合都忙于中继，而主广播集合没有忙于发送本地消息时，协议栈会使用主广播集合中继该消息。这可最大限度提高广播集合利用率，有利于密集的中继发送。

当 `CONFIG_BT_MESH_RELAY_RETRANSMIT_COUNT` 大于零时，可能明显延迟本地消息发送。启用友谊功能（Friend feature）且节点已建立友谊关系（friendship）时，此选项也可能延迟本地消息发送，从而要求增大 `CONFIG_BT_MESH_FRIEND_RECV_WIN`；这又会增加低功耗节点（Low Power node）的功耗。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_RELAY_ADV_SETS > 0 && CONFIG_BT_MESH_ADV_EXT && <choice CONFIG_BT_MESH_ADV>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser） → 广播者模式（Advertiser mode） → 扩展广播（Extended advertising）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RELAY_ADV_SETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RELAY_ADV_SETS)、[`CONFIG_BT_MESH_ADV_EXT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV_EXT)、[`CONFIG_BT_MESH_ADV`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV)。

<a id="CONFIG_BT_MESH_ADV_LEGACY"></a>

## 327.90 `CONFIG_BT_MESH_ADV_LEGACY`

**提示（Prompt）**：传统广播（Legacy advertising）

**说明（Help）**

使用传统广播命令（legacy advertising commands）发送 Mesh 消息。传统广播显著慢于扩展广播，但所有控制器都支持。警告：受 HCI 接口 API 限制，传统广播者（legacy advertiser）偶尔会执行比请求次数更多的消息重传。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_ADV>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser） → 广播者模式（Advertiser mode）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ADV`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV)。

<a id="CONFIG_BT_MESH_ADV_PRIO"></a>

## 327.91 `CONFIG_BT_MESH_ADV_PRIO`

原库同名定义共 2 条；本项为数据库第 2617 条记录，各定义分别保留。

**提示（Prompt）**：Mesh 广播者线程优先级（Mesh advertiser thread priority）

**说明（Help）**

蓝牙 Mesh 广播线程（adv thread）的优先级。注意：这是高级设置，除非确有必要，否则不应修改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_ADV_LEGACY && <choice CONFIG_BT_MESH_ADV>
```

**默认值（Defaults）**

```text
7
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser） → 广播者模式（Advertiser mode） → 传统广播（Legacy advertising）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ADV_LEGACY`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV_LEGACY)、[`CONFIG_BT_MESH_ADV`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV)。

<a id="CONFIG_BT_MESH_ADV_PRIO--record-2618"></a>

## 327.92 `CONFIG_BT_MESH_ADV_PRIO`

原库同名定义共 2 条；本项为数据库第 2618 条记录，各定义分别保留。

**提示（Prompt）**：Mesh 广播者线程优先级（Mesh advertiser thread priority）

**说明（Help）**

蓝牙 Mesh 广播线程（adv thread）的优先级。注意：这是高级设置，除非确有必要，否则不应修改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_WORKQ_MESH && CONFIG_BT_MESH_ADV_EXT && <choice CONFIG_BT_MESH_ADV>
```

**默认值（Defaults）**

```text
7
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser） → 广播者模式（Advertiser mode） → 扩展广播（Extended advertising）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_WORKQ_MESH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_WORKQ_MESH)、[`CONFIG_BT_MESH_ADV_EXT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV_EXT)、[`CONFIG_BT_MESH_ADV`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV)。

<a id="CONFIG_BT_MESH_ADV_STACK_SIZE"></a>

## 327.93 `CONFIG_BT_MESH_ADV_STACK_SIZE`

原库同名定义共 2 条；本项为数据库第 2619 条记录，各定义分别保留。

**提示（Prompt）**：Mesh 广播者线程栈大小（Mesh advertiser thread stack size）

**说明（Help）**

蓝牙 Mesh 广播线程（adv thread）的栈大小。注意：这是高级设置，除非确有必要，否则不应修改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_ADV_LEGACY && <choice CONFIG_BT_MESH_ADV>
```

**默认值（Defaults）**

```text
1800 if CONFIG_BT_MESH_PROVISIONER
1536 if CONFIG_BT_MESH_PROXY
776 if CONFIG_BT_MESH_PRIV_BEACONS
768
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser） → 广播者模式（Advertiser mode） → 传统广播（Legacy advertising）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ADV_LEGACY`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV_LEGACY)、[`CONFIG_BT_MESH_ADV`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV)、[`CONFIG_BT_MESH_PROVISIONER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROVISIONER)、[`CONFIG_BT_MESH_PROXY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROXY)、[`CONFIG_BT_MESH_PRIV_BEACONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PRIV_BEACONS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MESH_PROXY`。

<a id="CONFIG_BT_MESH_ADV_STACK_SIZE--record-2620"></a>

## 327.94 `CONFIG_BT_MESH_ADV_STACK_SIZE`

原库同名定义共 2 条；本项为数据库第 2620 条记录，各定义分别保留。

**提示（Prompt）**：Mesh 扩展广播者线程栈大小（Mesh extended advertiser thread stack size）

**说明（Help）**

蓝牙 Mesh 广播线程（adv thread）的栈大小。注意：这是高级设置，除非确有必要，否则不应修改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_WORKQ_MESH && CONFIG_BT_MESH_ADV_EXT && <choice CONFIG_BT_MESH_ADV>
```

**默认值（Defaults）**

```text
2048 if CONFIG_BT_MESH_PROVISIONER
1536 if CONFIG_BT_MESH_PROXY
776 if CONFIG_BT_MESH_PRIV_BEACONS
768
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser） → 广播者模式（Advertiser mode） → 扩展广播（Extended advertising）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_WORKQ_MESH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_WORKQ_MESH)、[`CONFIG_BT_MESH_ADV_EXT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV_EXT)、[`CONFIG_BT_MESH_ADV`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV)、[`CONFIG_BT_MESH_PROVISIONER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROVISIONER)、[`CONFIG_BT_MESH_PROXY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROXY)、[`CONFIG_BT_MESH_PRIV_BEACONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PRIV_BEACONS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MESH_PROXY`。

<a id="CONFIG_BT_MESH_ALIGN_CHUNK_SIZE_TO_MAX_SEGMENT"></a>

## 327.95 `CONFIG_BT_MESH_ALIGN_CHUNK_SIZE_TO_MAX_SEGMENT`

**提示（Prompt）**：将分片大小对齐到最大分段消息大小（Align chunk size to max segmented message size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1046`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1046)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → BLOB 模型公共配置（BLOB models common configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_APP_KEY_COUNT"></a>

## 327.96 `CONFIG_BT_MESH_APP_KEY_COUNT`

**提示（Prompt）**：每个网络的应用密钥最大数量（Maximum number of application keys per network）

**说明（Help）**

指定设备在每个网络中可存储的应用密钥（application keys）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 4096]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1825`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1825)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 能力（Capabilities）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BEACON_ENABLED"></a>

## 327.97 `CONFIG_BT_MESH_BEACON_ENABLED`

**提示（Prompt）**：默认启用安全网络信标（Secure network beacon enabled）

**说明（Help）**

控制是否默认启用安全网络信标（Secure network beacon）功能，可以通过运行时配置更改。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1547`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1547)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 信标（Beacons）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MAX"></a>

## 327.98 `CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MAX`

**提示（Prompt）**：最大块大小（Maximum block size）

**说明（Help）**

BLOB 传输（transfer）可接受的最大块大小（block size）。传输块大小应为 `2` 的某次幂，且位于最小块大小与最大块大小之间。如果不存在这样的值，编译时会发出警告。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_BLOB_SRV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
4096
```

**取值范围（Ranges）**

```text
[CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MIN, 1048576]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:972`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L972)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → BLOB 传输服务器模型支持（BLOB Transfer Server model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BLOB_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_SRV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MIN`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MIN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MIN"></a>

## 327.99 `CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MIN`

**提示（Prompt）**：最小块大小（Minimum block size）

**说明（Help）**

BLOB 传输（transfer）可接受的最小块大小（block size）。传输块大小应为 `2` 的某次幂，且位于最小块大小与最大块大小之间。如果不存在这样的值，编译时会发出警告。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_BLOB_SRV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
4096
```

**取值范围（Ranges）**

```text
[64, 1048576]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:962`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L962)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → BLOB 传输服务器模型支持（BLOB Transfer Server model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BLOB_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_SRV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX"></a>

## 327.100 `CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX`

**提示（Prompt）**：每块最大分片数（Maximum chunk count per block）

**说明（Help）**

一次 BLOB 传输包含若干块（blocks），每块又由若干分片（chunks）组成。此选项控制每块的最大分片数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[1, 2992]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1050`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1050)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → BLOB 模型公共配置（BLOB models common configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<!-- kconfig-navigation -->

[上一章](P326_subsys_bluetooth_配置项参考_7.md) · [返回大纲](大纲.md) · [下一章](P328_subsys_bluetooth_配置项参考_9.md)
