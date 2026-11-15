---
id: learning.zephyr-docs.kconfig-reference.page-331
title: "`subsys/bluetooth`配置项参考（12/13）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第331章\_`subsys/bluetooth`配置项参考（12/13）

本章翻译官方 Kconfig 数据库中 `subsys/bluetooth` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_SETTINGS_CCC_STORE_ON_WRITE"></a>

## 331.1 `CONFIG_BT_SETTINGS_CCC_STORE_ON_WRITE`

**提示（Prompt）**：CCC 值写入后立即存储（Store CCC value immediately after write）

**说明（Help）**

客户端配置特征（Client Configuration Characteristic）值更新后立即保存。禁用时，CCC 仅在断开连接时保存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_SETTINGS && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_SETTINGS_DELAYED_STORE
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:233`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L233)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 持久化保存蓝牙状态与配置（Store Bluetooth state and configuration persistently）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_SETTINGS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_SETTINGS)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SETTINGS_DELAYED_STORE`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SETTINGS_DELAYED_STORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SETTINGS_CF_STORE_ON_WRITE"></a>

## 331.2 `CONFIG_BT_SETTINGS_CF_STORE_ON_WRITE`

**提示（Prompt）**：CF 值写入后立即存储（Store CF value immediately after write）

**说明（Help）**

客户端支持功能（Client Supported Features）值更新后立即保存。禁用时，CF 仅在断开连接时保存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_GATT_CACHING && CONFIG_BT_SETTINGS && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_SETTINGS_DELAYED_STORE
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:243`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L243)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 持久化保存蓝牙状态与配置（Store Bluetooth state and configuration persistently）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_GATT_CACHING`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CACHING)、[`CONFIG_BT_SETTINGS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_SETTINGS)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SETTINGS_DELAYED_STORE`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SETTINGS_DELAYED_STORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SETTINGS_DELAYED_STORE"></a>

## 331.3 `CONFIG_BT_SETTINGS_DELAYED_STORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

写入后立即触发 CF 与 CCC 存储，在工作队列上下文（workqueue context）中执行，以免长时间阻塞蓝牙接收线程（BT RX thread）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SETTINGS && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_SETTINGS_CCC_STORE_ON_WRITE
CONFIG_BT_SETTINGS_CF_STORE_ON_WRITE
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:218`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L218)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 持久化保存蓝牙状态与配置（Store Bluetooth state and configuration persistently）

**配置项引用（Symbol References）**：[`CONFIG_BT_SETTINGS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_SETTINGS)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SETTINGS_CCC_STORE_ON_WRITE`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SETTINGS_CCC_STORE_ON_WRITE)、[`CONFIG_BT_SETTINGS_CF_STORE_ON_WRITE`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SETTINGS_CF_STORE_ON_WRITE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SETTINGS_DELAYED_STORE_MS"></a>

## 331.4 `CONFIG_BT_SETTINGS_DELAYED_STORE_MS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

高级选项：控制设置写入生效之前的超时（settings write timeout）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SETTINGS && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:226`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L226)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 持久化保存蓝牙状态与配置（Store Bluetooth state and configuration persistently）

**配置项引用（Symbol References）**：[`CONFIG_BT_SETTINGS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_SETTINGS)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SETTINGS_USE_PRINTK"></a>

## 331.5 `CONFIG_BT_SETTINGS_USE_PRINTK`

**提示（Prompt）**：使用 snprintk 编码蓝牙设置键字符串（Bluetooth settings key strings）

**说明（Help）**

选择后，蓝牙设置使用 `snprintk` 编码键字符串（key strings）；否则采用更快的内置函数。后者的缺点是，如果已经启用 `printk`，程序内存占用会更大。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS && CONFIG_PRINTK && CONFIG_BT_SETTINGS && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:252`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L252)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 持久化保存蓝牙状态与配置（Store Bluetooth state and configuration persistently）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)、[`CONFIG_PRINTK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PRINTK)、[`CONFIG_BT_SETTINGS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_SETTINGS)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SHELL"></a>

## 331.6 `CONFIG_BT_SHELL`

**提示（Prompt）**：蓝牙 Shell（Bluetooth shell）

**说明（Help）**

启用向控制台提供蓝牙命令的 Shell 模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_SHELL
CONFIG_SHELL_GETOPT
CONFIG_GETOPT_LONG
CONFIG_BT_PRIVATE_SHELL
CONFIG_BT_TICKER_NEXT_SLOT_GET if CONFIG_BT_LL_SW_SPLIT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:426`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L426)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SHELL_GETOPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_GETOPT)、[`CONFIG_GETOPT_LONG`](P197_lib_配置项参考_1.md#CONFIG_GETOPT_LONG)、[`CONFIG_BT_PRIVATE_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PRIVATE_SHELL)、[`CONFIG_BT_TICKER_NEXT_SLOT_GET`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TICKER_NEXT_SLOT_GET)、[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_PRIVATE_SHELL`。

<a id="CONFIG_BT_SHORTER_CONNECTION_INTERVALS"></a>

## 331.7 `CONFIG_BT_SHORTER_CONNECTION_INTERVALS`

**提示（Prompt）**：更短的连接间隔（Shorter Connection Intervals）

**说明（Help）**

启用蓝牙 6.2 更短连接间隔（Shorter Connection Intervals）功能支持。版本号按所译官方快照保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS_SUPPORT) && CONFIG_BT_LE_EXTENDED_FEAT_SET && CONFIG_BT_SUBRATING && CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L265)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS_SUPPORT)、[`CONFIG_BT_LE_EXTENDED_FEAT_SET`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LE_EXTENDED_FEAT_SET)、[`CONFIG_BT_SUBRATING`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SUBRATING)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_SHORTER_CONNECTION_INTERVALS_SUPPORT`。

<a id="CONFIG_BT_SIGNING"></a>

## 331.8 `CONFIG_BT_SIGNING`

**提示（Prompt）**：数据签名支持（Data signing support）[已弃用，DEPRECATED]

**说明（Help）**

启用数据签名（data signing），用于在未加密连接中传输经过认证的数据（authenticated data）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:552`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L552)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SMP"></a>

## 331.9 `CONFIG_BT_SMP`

**提示（Prompt）**：安全管理协议支持（Security Manager Protocol support）

**说明（Help）**

启用安全管理协议（Security Manager Protocol，SMP）支持，使设备能够通过低功耗蓝牙（LE）配对。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_CRYPTO
CONFIG_BT_RPA
CONFIG_BT_ECC if !CONFIG_BT_SMP_OOB_LEGACY_PAIR_ONLY
```

**被选择（Selected by）**

```text
CONFIG_BT_OTS
CONFIG_BT_CLASSIC
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:424`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L424)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CRYPTO`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CRYPTO)、[`CONFIG_BT_RPA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_RPA)、[`CONFIG_BT_ECC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ECC)、[`CONFIG_BT_SMP_OOB_LEGACY_PAIR_ONLY`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP_OOB_LEGACY_PAIR_ONLY)、[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_RPA`。

<a id="CONFIG_BT_SMP_ALLOW_UNAUTH_OVERWRITE"></a>

## 331.10 `CONFIG_BT_SMP_ALLOW_UNAUTH_OVERWRITE`

**提示（Prompt）**：允许已配对设备进行未经认证的配对（unauthenticated pairing for paired device）

**说明（Help）**

如果对端已存在未经身份认证的绑定（unauthenticated bond），允许它发起的所有未经认证配对尝试。这会允许攻击者复制对端地址，连接并发起未经认证的配对过程，以替换现有绑定。禁用时，要建立新绑定，必须先通过 `bt_unpair` 显式删除旧绑定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:603`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L603)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SMP_APP_PAIRING_ACCEPT"></a>

## 331.11 `CONFIG_BT_SMP_APP_PAIRING_ACCEPT`

**提示（Prompt）**：接受或拒绝配对发起（Accept or reject pairing initiative）

**说明（Help）**

收到配对请求或配对响应时，询问应用是否接受并继续配对。此功能适用于 SMP 配对，不影响安全简单配对（SSP）；后者仍会继续配对而不询问应用。如果不允许配对，应用可返回错误码，该值会被转换为 SMP 返回值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:559`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L559)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SMP_DERIVE_LK"></a>

## 331.12 `CONFIG_BT_SMP_DERIVE_LK`

**提示（Prompt）**：从 LE LTK 派生 BR/EDR 链路密钥（Derive the BR/EDR link key from the LE LTK）

**说明（Help）**

在通过低功耗蓝牙（LE）进行安全连接（Secure Connections）配对时，请求从 LE 长期密钥（LTK）派生 BR/EDR 链路密钥，作为跨传输密钥派生（Cross-Transport Key Derivation）的一部分；参见 Core Specification 6.3, Vol 3, Part H, Section 2.4.2.4。

禁用会从配对请求和配对响应的密钥分发字段中清除 `LinkKey` 位，以免对端保留本设备从未派生的链路密钥。如果设备不得因 LE 配对而附带生成 BR/EDR 绑定，应禁用此项。在启用期间已派生的密钥仍会保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:636`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L636)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SMP_DERIVE_LTK"></a>

## 331.13 `CONFIG_BT_SMP_DERIVE_LTK`

**提示（Prompt）**：从 BR/EDR 链路密钥派生 LE LTK（Derive the LE LTK from the BR/EDR link key）

**说明（Help）**

接受 BR/EDR 上的安全管理过程（Security Manager procedure），作为跨传输密钥派生（Cross-Transport Key Derivation）的一部分，从 BR/EDR 链路密钥派生 LE 长期密钥（LTK）；参见 Core Specification 6.3, Vol 3, Part H, Section 2.4.2.5。

禁用会拒绝整个过程，而不只是拒绝 LTK 派生：IRK、身份地址（identity address）和 CSRK 也不会通过 BR/EDR 分发，因此无法再解析仅通过 BR/EDR 绑定对端的可解析私有地址（RPAs）。这是有意的行为，因为单独的身份信息本身就会创建 LE 绑定条目。

L2CAP 信息响应也会省略 BR/EDR 安全管理固定信道（Security Manager fixed channel），以免对端启动随后必被拒绝的过程。如果设备不得因 BR/EDR 配对而附带生成 LE 绑定，应禁用此项。在启用期间已派生的密钥仍会保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:614`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L614)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SMP_DISABLE_LEGACY_JW_PASSKEY"></a>

## 331.14 `CONFIG_BT_SMP_DISABLE_LEGACY_JW_PASSKEY`

**提示（Prompt）**：禁止使用不安全的传统配对方法（insecure legacy pairing methods）

**说明（Help）**

禁用传统配对中的直接配对（Just Works）和通行密钥配对（Passkey）方法，以提高安全性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!(CONFIG_BT_SMP_SC_PAIR_ONLY || CONFIG_BT_SMP_SC_ONLY || CONFIG_BT_SMP_OOB_LEGACY_PAIR_ONLY) && CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:595`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L595)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP_SC_PAIR_ONLY`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP_SC_PAIR_ONLY)、[`CONFIG_BT_SMP_SC_ONLY`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP_SC_ONLY)、[`CONFIG_BT_SMP_OOB_LEGACY_PAIR_ONLY`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP_OOB_LEGACY_PAIR_ONLY)、[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SMP_ENFORCE_MITM"></a>

## 331.15 `CONFIG_BT_SMP_ENFORCE_MITM`

**提示（Prompt）**：强制中间人攻击防护（Enforce MITM protection）

**说明（Help）**

启用后，只要本地输入输出能力（IO Capabilities）允许生成经过认证的密钥，安全管理器（Security Manager）就会在认证需求标志（Authentication Requirements Flags）中设置中间人防护（MITM）选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:770`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L770)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SMP_ERR_TO_STR"></a>

## 331.16 `CONFIG_BT_SMP_ERR_TO_STR`

**提示（Prompt）**：以字符串打印 SMP 错误码（SMP error codes as strings）[实验性，EXPERIMENTAL]

**说明（Help）**

启用以字符串形式打印 SMP 错误码（error codes）的功能。详情参见 `bt_smp_err_to_str()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:443`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L443)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SMP_FORCE_BREDR"></a>

## 331.17 `CONFIG_BT_SMP_FORCE_BREDR`

**提示（Prompt）**：强制在 BR/EDR 上使用蓝牙 SMP（Force Bluetooth SMP over BR/EDR）

**说明（Help）**

即使控制器不支持 BR/EDR 安全连接（Secure Connections），也启用 BR/EDR 上的 SMP。此选项仅供测试，绝不应在生产设备上启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP_LOG_LEVEL_DBG && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1122)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP_LOG_LEVEL_DBG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_SMP_LEGACY_PAIR_ONLY"></a>

## 331.18 `CONFIG_BT_SMP_LEGACY_PAIR_ONLY`

**提示（Prompt）**：强制传统配对（Force legacy pairing）

**说明（Help）**

强制使用传统配对（legacy pairing）。在两个 Zephyr 蓝牙设备之间测试传统配对时需要此项，否则设备默认使用安全连接配对（Secure Connections pairing）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TESTING && !(CONFIG_BT_SMP_SC_PAIR_ONLY || CONFIG_BT_SMP_SC_ONLY) && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1158)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙测试（Bluetooth Testing）

**配置项引用（Symbol References）**：[`CONFIG_BT_TESTING`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TESTING)、[`CONFIG_BT_SMP_SC_PAIR_ONLY`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP_SC_PAIR_ONLY)、[`CONFIG_BT_SMP_SC_ONLY`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP_SC_ONLY)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_SMP_MIN_ENC_KEY_SIZE"></a>

## 331.19 `CONFIG_BT_SMP_MIN_ENC_KEY_SIZE`

**提示（Prompt）**：接受的最小加密密钥长度，单位为八位字节（Minimum encryption key size accepted in octets）

**说明（Help）**

设置配对期间可接受的最小加密密钥长度（minimum encryption key size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[7, 16]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:804`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L804)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SMP_OOB_LEGACY_PAIR_ONLY"></a>

## 331.20 `CONFIG_BT_SMP_OOB_LEGACY_PAIR_ONLY`

**提示（Prompt）**：强制传统带外配对（Force Out Of Band Legacy pairing）

**说明（Help）**

禁用传统配对（Legacy）和低功耗安全连接配对（LE SC），强制采用传统带外配对（legacy OOB）。

译注：原文先写禁用 `Legacy`，随后又要求 `legacy OOB`；这里保留其措辞，后者特指带外方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!(CONFIG_BT_SMP_SC_PAIR_ONLY || CONFIG_BT_SMP_SC_ONLY) && CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:589`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L589)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP_SC_PAIR_ONLY`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP_SC_PAIR_ONLY)、[`CONFIG_BT_SMP_SC_ONLY`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP_SC_ONLY)、[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SMP_SC_ONLY"></a>

## 331.21 `CONFIG_BT_SMP_SC_ONLY`

**提示（Prompt）**：仅安全连接模式（Secure Connections Only Mode）

**说明（Help）**

启用仅安全连接模式（Secure Connection Only Mode）。除仅要求安全模式 1、级别 1（无安全保护）的服务外，设备只能使用安全模式 1、级别 4。级别 4 表示经过身份认证并启用加密的 LE 安全连接配对（authenticated LE Secure Connections pairing）。启用此项会禁用传统配对（legacy pairing）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_SMP_SC_PAIR_ONLY
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:579`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L579)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SMP_SC_PAIR_ONLY`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP_SC_PAIR_ONLY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SMP_SC_PAIR_ONLY"></a>

## 331.22 `CONFIG_BT_SMP_SC_PAIR_ONLY`

**提示（Prompt）**：禁用传统配对（Disable legacy pairing）

**说明（Help）**

禁用 LE 传统配对（legacy pairing），强制使用 LE 安全连接配对（secure connection pairing）。禁用传统配对后仍可使用安全模式 1 的所有级别，但不支持与不具备安全连接配对能力的设备配对。若需强制更高安全级别，应使用“仅安全连接模式”（Secure Connections Only Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_BT_SMP_SC_ONLY
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:569`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L569)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SMP_SC_ONLY`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP_SC_ONLY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SMP_SELFTEST"></a>

## 331.23 `CONFIG_BT_SMP_SELFTEST`

**提示（Prompt）**：初始化时执行蓝牙 SMP 自检（Bluetooth SMP self tests on init）

**说明（Help）**

启用启动时执行的 SMP 自检（self-tests），验证安全与密码功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP_LOG_LEVEL_DBG && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1115)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP_LOG_LEVEL_DBG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_SMP_USB_HCI_CTLR_WORKAROUND"></a>

## 331.24 `CONFIG_BT_SMP_USB_HCI_CTLR_WORKAROUND`

**提示（Prompt）**：USB HCI 控制器事件乱序的变通处理（Workaround for out-of-order events）

**说明（Help）**

支持某些 USB HCI 控制器：由于使用不同 USB 端点（endpoints），它们有时会乱序发送 HCI 事件和 ACL 数据。启用后，中心设备角色（central role）接受密钥分发数据之前，不再要求先收到加密变更事件（encryption-change event）。这会引入潜在漏洞，因为中心设备无法检测密钥是否经由加密链路分发。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TESTING && CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:701`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L701)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TESTING`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TESTING)、[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_STACK_SELECTION"></a>

## 331.25 `CONFIG_BT_STACK_SELECTION`

**提示（Prompt）**：蓝牙协议栈选择（Bluetooth Stack Selection）

**说明（Help）**

选择要编译的蓝牙协议栈（Bluetooth stack）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_HCI
```

**可选项（Choices）**

```text
CONFIG_BT_HCI
CONFIG_BT_CUSTOM
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT_CUSTOM`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CUSTOM)。

<a id="CONFIG_BT_STORE_DEBUG_KEYS"></a>

## 331.26 `CONFIG_BT_STORE_DEBUG_KEYS`

**提示（Prompt）**：存储调试模式绑定（Store Debug Mode bonds）

**说明（Help）**

允许存储以下绑定：任一设备使用核心规范 Vol 3, Part H, 2.3.5.6.1 所述预定义 Diffie-Hellman 私钥／公钥对。警告：此选项可能允许任何人解密空中传输流量（on-air traffic）。强烈不建议在生产环境使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:759`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L759)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SUBRATING"></a>

## 331.27 `CONFIG_BT_SUBRATING`

**提示（Prompt）**：低功耗蓝牙连接子速率（LE Connection Subrating）

**说明（Help）**

启用低功耗蓝牙连接子速率（LE Connection Subrating）功能支持，其定义见蓝牙核心规范 Version 5.4，Vol 6, Part B, Section 4.6.35。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_SUBRATING_SUPPORT) && CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:218`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L218)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_SUBRATING_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SUBRATING_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_SUBRATING_SUPPORT`。

<a id="CONFIG_BT_SYSTEM_WORKQUEUE_COOP"></a>

## 331.28 `CONFIG_BT_SYSTEM_WORKQUEUE_COOP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由向系统工作队列（system workqueue）提交工作、且依赖其以协作式优先级（cooperative priority）运行的蓝牙组件选择。如果构建没有选择任何这类组件，则保留应用为系统工作队列选择的优先级。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_H5
CONFIG_BT_STM32WB0
CONFIG_BT_HCI_HOST
CONFIG_BT_CTLR_PRIVACY
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_H5`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H5)、[`CONFIG_BT_STM32WB0`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WB0)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_CTLR_PRIVACY`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_PRIVACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS"></a>

## 331.29 `CONFIG_BT_TBS`

**提示（Prompt）**：电话承载服务支持（Telephone Bearer Service Support）

**说明（Help）**

启用电话承载服务（Telephone Bearer Service）支持。默认仅初始化通用电话承载服务（GTBS）。若需要特定 TBS 服务，须将 `BT_TBS_BEARER_COUNT` 设为非零以启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_DYNAMIC_DB && CONFIG_BT_SMP && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_DYNAMIC_DB`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_DYNAMIC_DB)、[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_BEARER_COUNT"></a>

## 331.30 `CONFIG_BT_TBS_BEARER_COUNT`

**提示（Prompt）**：设备实例化的承载实例数量（bearer instances）

**说明（Help）**

设置要实例化的电话承载服务（TBS）实例数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 电话承载服务支持（Telephone Bearer Service Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_ACCEPT_CALL"></a>

## 331.31 `CONFIG_BT_TBS_CLIENT_ACCEPT_CALL`

**提示（Prompt）**：接听呼叫支持（Support Accept Call）

**说明（Help）**

启用接听来电（answering an incoming call）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L184)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_BEARER_LIST_CURRENT_CALLS"></a>

## 331.32 `CONFIG_BT_TBS_CLIENT_BEARER_LIST_CURRENT_CALLS`

**提示（Prompt）**：支持读取承载当前呼叫列表（Bearer List Current Calls）

**说明（Help）**

启用承载当前呼叫列表（Bearer List Current Calls）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_BEARER_PROVIDER_NAME"></a>

## 331.33 `CONFIG_BT_TBS_CLIENT_BEARER_PROVIDER_NAME`

**提示（Prompt）**：支持读取承载提供方名称（Bearer Provider Name）

**说明（Help）**

启用承载提供方名称（Bearer Provider Name）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_BEARER_SIGNAL_STRENGTH"></a>

## 331.34 `CONFIG_BT_TBS_CLIENT_BEARER_SIGNAL_STRENGTH`

**提示（Prompt）**：支持读取承载信号强度（Bearer Signal Strength）

**说明（Help）**

启用承载信号强度（Bearer Signal Strength）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_BEARER_TECHNOLOGY"></a>

## 331.35 `CONFIG_BT_TBS_CLIENT_BEARER_TECHNOLOGY`

**提示（Prompt）**：支持读取承载技术（Bearer Technology）

**说明（Help）**

启用承载技术（Bearer Technology）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_BEARER_UCI"></a>

## 331.36 `CONFIG_BT_TBS_CLIENT_BEARER_UCI`

**提示（Prompt）**：支持读取承载 UCI（Bearer UCI）

**说明（Help）**

启用承载 UCI（Bearer UCI）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_BEARER_URI_SCHEMES_SUPPORTED_LIST"></a>

## 331.37 `CONFIG_BT_TBS_CLIENT_BEARER_URI_SCHEMES_SUPPORTED_LIST`

**提示（Prompt）**：支持读取承载 URI 方案支持列表（Bearer URI Schemes Supported List）

**说明（Help）**

启用承载 URI 方案支持列表（Bearer URI Schemes Supported List）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_CALL_FRIENDLY_NAME"></a>

## 331.38 `CONFIG_BT_TBS_CLIENT_CALL_FRIENDLY_NAME`

**提示（Prompt）**：支持读取呼叫友好名称（Call Friendly Name）

**说明（Help）**

启用呼叫友好名称（Call Friendly Name）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:233`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L233)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_CCID"></a>

## 331.39 `CONFIG_BT_TBS_CLIENT_CCID`

**提示（Prompt）**：支持读取内容控制 ID（Content Control ID）

**说明（Help）**

启用内容控制 ID（Content Control ID）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_CP_PROCEDURES"></a>

## 331.40 `CONFIG_BT_TBS_CLIENT_CP_PROCEDURES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项表示至少有一个可用控制点过程（control point procedure）。禁用时，表示可以将控制点优化掉。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_TBS_CLIENT_ACCEPT_CALL || CONFIG_BT_TBS_CLIENT_TERMINATE_CALL || CONFIG_BT_TBS_CLIENT_HOLD_CALL || CONFIG_BT_TBS_CLIENT_RETRIEVE_CALL || CONFIG_BT_TBS_CLIENT_ORIGINATE_CALL || CONFIG_BT_TBS_CLIENT_JOIN_CALLS) && CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L170)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT_ACCEPT_CALL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_ACCEPT_CALL)、[`CONFIG_BT_TBS_CLIENT_TERMINATE_CALL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_TERMINATE_CALL)、[`CONFIG_BT_TBS_CLIENT_HOLD_CALL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_HOLD_CALL)、[`CONFIG_BT_TBS_CLIENT_RETRIEVE_CALL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_RETRIEVE_CALL)、[`CONFIG_BT_TBS_CLIENT_ORIGINATE_CALL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_ORIGINATE_CALL)、[`CONFIG_BT_TBS_CLIENT_JOIN_CALLS`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_JOIN_CALLS)、[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_GTBS"></a>

## 331.41 `CONFIG_BT_TBS_CLIENT_GTBS`

**提示（Prompt）**：通用电话承载服务客户端支持（Generic Telephone Bearer Service client support）

**说明（Help）**

启用面向通用电话承载服务（GTBS）的呼叫控制客户端（Call Control client）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_CLIENT && CONFIG_BT_GATT_AUTO_DISCOVER_CCC && CONFIG_BT_SMP && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_CLIENT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_GATT_AUTO_DISCOVER_CCC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_AUTO_DISCOVER_CCC)、[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_HOLD_CALL"></a>

## 331.42 `CONFIG_BT_TBS_CLIENT_HOLD_CALL`

**提示（Prompt）**：呼叫保持支持（Support Hold Call）

**说明（Help）**

启用将呼叫置于保持状态（putting a call on hold）的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:196`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L196)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_INCOMING_CALL"></a>

## 331.43 `CONFIG_BT_TBS_CLIENT_INCOMING_CALL`

**提示（Prompt）**：支持读取来电（Incoming Call）

**说明（Help）**

启用来电（Incoming Call）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_INCOMING_URI"></a>

## 331.44 `CONFIG_BT_TBS_CLIENT_INCOMING_URI`

**提示（Prompt）**：支持读取来电目标承载 URI（Incoming Call Target Bearer URI）

**说明（Help）**

启用来电目标承载 URI（Incoming Call Target Bearer URI）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_JOIN_CALLS"></a>

## 331.45 `CONFIG_BT_TBS_CLIENT_JOIN_CALLS`

**提示（Prompt）**：合并呼叫支持（Support Join Calls）

**说明（Help）**

启用合并呼叫（joining calls）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT_MAX_CALLS > 1 && CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:214`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L214)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT_MAX_CALLS`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MAX_CALLS)、[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_MAX_CALLS"></a>

## 331.46 `CONFIG_BT_TBS_CLIENT_MAX_CALLS`

**提示（Prompt）**：支持的最大呼叫数（Maximum Number Of Calls Supported）

**说明（Help）**

设置客户端在每个电话承载服务（TBS）实例上支持的最大呼叫数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_MAX_TBS_INSTANCES"></a>

## 331.47 `CONFIG_BT_TBS_CLIENT_MAX_TBS_INSTANCES`

**提示（Prompt）**：可设置的 TBS 最大实例数（Maximum number of TBS instances to setup）

**说明（Help）**

设置可配置并使用的电话承载服务（Telephone Bearer Service，TBS）最大实例数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT_TBS && CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 3]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT_TBS`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_TBS)、[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_MINIMAL"></a>

## 331.48 `CONFIG_BT_TBS_CLIENT_MINIMAL`

**提示（Prompt）**：不含可选过程的最小 TBS 客户端（Minimal TBS Client）

**说明（Help）**

禁用电话承载服务（TBS）客户端的全部可选过程（optional procedures）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_OPTIONAL_OPCODES"></a>

## 331.49 `CONFIG_BT_TBS_CLIENT_OPTIONAL_OPCODES`

**提示（Prompt）**：支持读取可选操作码（Optional Opcodes）

**说明（Help）**

启用可选操作码（Optional Opcodes）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_ORIGINATE_CALL"></a>

## 331.50 `CONFIG_BT_TBS_CLIENT_ORIGINATE_CALL`

**提示（Prompt）**：发起呼叫支持（Support Originate Call）

**说明（Help）**

启用发起呼叫（originating a call）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:208`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L208)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_READ_BEARER_SIGNAL_INTERVAL"></a>

## 331.51 `CONFIG_BT_TBS_CLIENT_READ_BEARER_SIGNAL_INTERVAL`

**提示（Prompt）**：支持读取承载信号强度报告间隔（Bearer Signal Strength Reporting Interval）

**说明（Help）**

启用承载信号强度报告间隔（Bearer Signal Strength Reporting Interval）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_RETRIEVE_CALL"></a>

## 331.52 `CONFIG_BT_TBS_CLIENT_RETRIEVE_CALL`

**提示（Prompt）**：恢复呼叫支持（Support Retrieve Call）

**说明（Help）**

启用恢复被保持呼叫（retrieving a call on hold）的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_SET_BEARER_SIGNAL_INTERVAL"></a>

## 331.53 `CONFIG_BT_TBS_CLIENT_SET_BEARER_SIGNAL_INTERVAL`

**提示（Prompt）**：支持设置承载信号强度报告间隔（Bearer Signal Strength Reporting Interval）

**说明（Help）**

启用承载信号强度报告间隔（Bearer Signal Strength Reporting Interval）设置支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_STATUS_FLAGS"></a>

## 331.54 `CONFIG_BT_TBS_CLIENT_STATUS_FLAGS`

**提示（Prompt）**：支持读取状态标志（Status Flags）

**说明（Help）**

启用状态标志（Status Flags）读取支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_TBS"></a>

## 331.55 `CONFIG_BT_TBS_CLIENT_TBS`

**提示（Prompt）**：电话承载服务客户端支持（Telephone Bearer Service client support）

**说明（Help）**

启用面向电话承载服务（TBS）的呼叫控制客户端（Call Control client）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_CLIENT && CONFIG_BT_GATT_AUTO_DISCOVER_CCC && CONFIG_BT_SMP && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_CLIENT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_GATT_AUTO_DISCOVER_CCC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_AUTO_DISCOVER_CCC)、[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_CLIENT_TERMINATE_CALL"></a>

## 331.56 `CONFIG_BT_TBS_CLIENT_TERMINATE_CALL`

**提示（Prompt）**：终止呼叫支持（Support Terminate Call）

**说明（Help）**

启用终止呼叫（terminating a call）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
!CONFIG_BT_TBS_CLIENT_MINIMAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:190`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L190)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_MINIMAL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS_CLIENT_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_LOCK_TIMEOUT"></a>

## 331.57 `CONFIG_BT_TBS_LOCK_TIMEOUT`

**提示（Prompt）**：处理并发操作的超时，单位为毫秒（timeout when handling concurrent operations）

**说明（Help）**

如果另一个线程已有写操作正在进行，TBS 实现在拒绝新的写请求（write request）之前等待的最大毫秒数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, 1000]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 电话承载服务支持（Telephone Bearer Service Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_MAX_CALLS"></a>

## 331.58 `CONFIG_BT_TBS_MAX_CALLS`

**提示（Prompt）**：电话承载服务支持的最大呼叫数（Telephone Bearer Service Maximum Number Of Calls Supported）

**说明（Help）**

设置服务为每个承载（bearer）支持的最大呼叫数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 电话承载服务支持（Telephone Bearer Service Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_MAX_FRIENDLY_NAME_LENGTH"></a>

## 331.59 `CONFIG_BT_TBS_MAX_FRIENDLY_NAME_LENGTH`

**提示（Prompt）**：支持的友好名称最大长度（maximum friendly name length）

**说明（Help）**

设置友好名称（friendly name）的最大长度，单位为八位字节（octets），不包含 `NULL` 终止符。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_TBS || CONFIG_BT_TBS_CLIENT) && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[1, 512]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:258`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L258)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS)、[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_MAX_PROVIDER_NAME_LENGTH"></a>

## 331.60 `CONFIG_BT_TBS_MAX_PROVIDER_NAME_LENGTH`

**提示（Prompt）**：承载提供方名称最大长度（maximum bearer provider name length）

**说明（Help）**

设置承载提供方名称（bearer provider name）的最大长度，单位为八位字节（octets），不包含 `NULL` 终止符。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_TBS || CONFIG_BT_TBS_CLIENT) && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[1, 512]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:251`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L251)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS)、[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_MAX_SCHEME_LIST_LENGTH"></a>

## 331.61 `CONFIG_BT_TBS_MAX_SCHEME_LIST_LENGTH`

**提示（Prompt）**：URI 方案列表最大长度（maximum URI scheme list length）

**说明（Help）**

设置 URI 方案列表（URI scheme list）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TBS && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[1, 512]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 电话承载服务支持（Telephone Bearer Service Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TBS_MAX_URI_LENGTH"></a>

## 331.62 `CONFIG_BT_TBS_MAX_URI_LENGTH`

**提示（Prompt）**：支持的呼叫 URI 最大长度（maximum call URI length）

**说明（Help）**

设置支持的呼叫 URI 最大长度，单位为八位字节（octets），不包含 `NULL` 终止符。如果某个呼叫 URI 比此值更长，呼叫请求会被拒绝。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_TBS || CONFIG_BT_TBS_CLIENT) && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[4, 253]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tbs:243`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tbs#L243)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS)、[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TESTING"></a>

## 331.63 `CONFIG_BT_TESTING`

**提示（Prompt）**：蓝牙测试（Bluetooth Testing）

**说明（Help）**

启用自定义蓝牙测试接口（custom Bluetooth testing interface），只应用于测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1141)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_TICKER_EXT"></a>

## 331.64 `CONFIG_BT_TICKER_EXT`

**提示（Prompt）**：Ticker 扩展（Ticker extensions）

**说明（Help）**

启用 ticker 扩展，例如重新调度 `slot_window` 非零的 ticker 节点。通过 ticker 接口函数可用的 `_ext` 版本调用这些扩展。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_BT_TICKER_LOW_LAT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_BROADCASTER
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1317`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1317)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_TICKER_LOW_LAT`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TICKER_LOW_LAT)、[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_TICKER_EXT_EXPIRE_INFO"></a>

## 331.65 `CONFIG_BT_TICKER_EXT_EXPIRE_INFO`

**提示（Prompt）**：带其他 ticker 到期信息的 ticker 超时（Ticker timeout with other ticker's expire information）

**说明（Help）**

允许 ticker 返回到期信息（expiration info）。通过扩展 ticker 接口，请求在 ticker 回调中返回另一个 ticker ID 的到期信息。它使用扩展接口和具有不同上下文的回调函数，以尽可能保持现有 ticker 接口不变。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TICKER_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1335`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1335)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → Ticker 扩展（Ticker extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_TICKER_EXT`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TICKER_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_TICKER_EXT_SLOT_WINDOW_YIELD"></a>

## 331.66 `CONFIG_BT_TICKER_EXT_SLOT_WINDOW_YIELD`

**提示（Prompt）**：带时隙窗口的 ticker 始终让步（Tickers with slot window always yields）

**说明（Help）**

强制具有时隙窗口扩展（slot window extensions）的 ticker 让步于普通 ticker，并安排到其时隙窗口末尾。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TICKER_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_MESH || CONFIG_BT_CTLR_ADV_ISO
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1327`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1327)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → Ticker 扩展（Ticker extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_TICKER_EXT`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TICKER_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_CTLR_ADV_ISO`](P322_subsys_bluetooth_配置项参考_3.md#CONFIG_BT_CTLR_ADV_ISO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_TICKER_JOB_IDLE_GET"></a>

## 331.67 `CONFIG_BT_TICKER_JOB_IDLE_GET`

**提示（Prompt）**：获取 Ticker Job 空闲状态（Ticker Job Idle Get）

**说明（Help）**

启用查询 Ticker Job 执行上下文空闲状态（idle state）的接口。当其进入空闲状态、没有待处理操作时，使用该接口禁用 Ticker Job 执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_TICKER_LOW_LAT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1275`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1275)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TICKER_LOW_LAT`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TICKER_LOW_LAT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_TICKER_LAZY_GET"></a>

## 331.68 `CONFIG_BT_TICKER_LAZY_GET`

**提示（Prompt）**：获取下一 ticker 时隙及惰性计数（Ticker Next Slot Get with Lazy）

**说明（Help）**

启用遍历活动 ticker 节点的接口，返回相对于参考 tick 的到期 tick（tick to expire）和惰性计数（lazy count）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TICKER_NEXT_SLOT_GET && CONFIG_BT_TICKER_NEXT_SLOT_GET_MATCH && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER
CONFIG_BT_LLL_VENDOR_NORDIC
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1299`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1299)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 获取下一 ticker 时隙（Ticker Next Slot Get）

**配置项引用（Symbol References）**：[`CONFIG_BT_TICKER_NEXT_SLOT_GET`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TICKER_NEXT_SLOT_GET)、[`CONFIG_BT_TICKER_NEXT_SLOT_GET_MATCH`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TICKER_NEXT_SLOT_GET_MATCH)、[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER)、[`CONFIG_BT_LLL_VENDOR_NORDIC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LLL_VENDOR_NORDIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_TICKER_LOW_LAT"></a>

## 331.69 `CONFIG_BT_TICKER_LOW_LAT`

**提示（Prompt）**：Ticker 低延迟模式（Ticker low latency mode）

**说明（Help）**

启用传统 ticker 调度（legacy ticker scheduling），推迟重叠 ticker 节点的超时，避免在无线电接收／发送（RX/TX）期间产生 ticker 中断。启用后会禁用 ticker 优先级及“必须到期”（must expire）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_NRF51
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1251`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1251)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_TICKER_NEXT_SLOT_GET"></a>

## 331.70 `CONFIG_BT_TICKER_NEXT_SLOT_GET`

**提示（Prompt）**：获取下一 ticker 时隙（Ticker Next Slot Get）

**说明（Help）**

启用遍历活动 ticker 节点并返回到期 tick（tick to expire）的接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_LLL_VENDOR_NORDIC
CONFIG_BT_SHELL
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1284`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1284)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_LLL_VENDOR_NORDIC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LLL_VENDOR_NORDIC)、[`CONFIG_BT_SHELL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SHELL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_TICKER_NEXT_SLOT_GET_MATCH"></a>

## 331.71 `CONFIG_BT_TICKER_NEXT_SLOT_GET_MATCH`

**提示（Prompt）**：带匹配回调的下一 ticker 时隙获取（Ticker Next Slot Get with match callback）

**说明（Help）**

启用遍历活动 ticker 节点的接口，对每个找到的节点调用回调。回调返回 `true` 时，停止遍历并调用普通操作回调（normal operation callback）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TICKER_NEXT_SLOT_GET && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_TICKER_SLOT_AGNOSTIC
```

**被选择（Selected by）**

```text
CONFIG_BT_LLL_VENDOR_NORDIC
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1307)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 获取下一 ticker 时隙（Ticker Next Slot Get）

**配置项引用（Symbol References）**：[`CONFIG_BT_TICKER_NEXT_SLOT_GET`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TICKER_NEXT_SLOT_GET)、[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TICKER_SLOT_AGNOSTIC`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TICKER_SLOT_AGNOSTIC)、[`CONFIG_BT_LLL_VENDOR_NORDIC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LLL_VENDOR_NORDIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_TICKER_PREFER_START_BEFORE_STOP"></a>

## 331.72 `CONFIG_BT_TICKER_PREFER_START_BEFORE_STOP`

**提示（Prompt）**：Ticker 优先处理启动请求，再处理停止请求（prefer start before stop request）

**说明（Help）**

在竞态条件（race conditions）下，如果某个用户执行上下文针对给定 ticker 节点，向 `ticker_job` 排入多个启动和停止操作，则优先处理启动操作。

未启用此选项时，默认行为是推迟全部启动请求，直到所有用户上下文入队的全部停止请求都处理完成。原文解释，这种默认行为是为了在竞态下、启动之后跟随停止请求或启动请求先于停止请求时，确保该 ticker 节点始终得到调度，并在超时时由执行上下文依据自身执行状态做决定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_LLL_VENDOR_NORDIC
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1367`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1367)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_LLL_VENDOR_NORDIC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LLL_VENDOR_NORDIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_TICKER_PRIORITY_SET"></a>

## 331.73 `CONFIG_BT_TICKER_PRIORITY_SET`

**提示（Prompt）**：使用基于优先级冲突解决的 ticker（priority based collision resolution）

**说明（Help）**

为 ticker 提供持久的优先级值（persistent priority value），用于解决冲突。启用优先级功能时，厂商需要自定义上层链路层（ULL），避免反复跳过重叠事件。

原因是 `next_has_priority` 检查使用惰性值（lazy value）：当前被跳过事件成为下一个事件后，其 lazy 值加 `1`，因而总出现 `lazy_next > lazy_current`。如果事件间隔之间的全部时间持续被重叠 ticker 占用，就会发生这种重复跳过。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TICKER_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1345`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1345)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → Ticker 扩展（Ticker extensions）

**配置项引用（Symbol References）**：[`CONFIG_BT_TICKER_EXT`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TICKER_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_TICKER_REMAINDER_GET"></a>

## 331.74 `CONFIG_BT_TICKER_REMAINDER_GET`

**提示（Prompt）**：获取下一 ticker 时隙及余量（Ticker Next Slot Get with Remainder）

**说明（Help）**

启用遍历活动 ticker 节点的接口，返回相对于参考 tick 的到期 tick（tick to expire）及余量（remainder）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TICKER_REMAINDER_SUPPORT && CONFIG_BT_TICKER_NEXT_SLOT_GET && CONFIG_BT_TICKER_NEXT_SLOT_GET_MATCH && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_LLL_VENDOR_NORDIC
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1290`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1290)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 获取下一 ticker 时隙（Ticker Next Slot Get）

**配置项引用（Symbol References）**：[`CONFIG_BT_TICKER_REMAINDER_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_REMAINDER_SUPPORT)、[`CONFIG_BT_TICKER_NEXT_SLOT_GET`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TICKER_NEXT_SLOT_GET)、[`CONFIG_BT_TICKER_NEXT_SLOT_GET_MATCH`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TICKER_NEXT_SLOT_GET_MATCH)、[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_LLL_VENDOR_NORDIC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LLL_VENDOR_NORDIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TICKER_REMAINDER_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_TICKER_SLOT_AGNOSTIC"></a>

## 331.75 `CONFIG_BT_TICKER_SLOT_AGNOSTIC`

**提示（Prompt）**：忽略时隙的 ticker 模式（Slot agnostic ticker mode）

**说明（Help）**

启用忽略时隙的 ticker 模式（slot agnostic ticker mode），不处理时隙预留和冲突，而是作为简单的多实例可编程定时器运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1360`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1360)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_TICKER_START_REMAINDER"></a>

## 331.76 `CONFIG_BT_TICKER_START_REMAINDER`

**提示（Prompt）**：Ticker Start 余量参数（Ticker Start Remainder Parameter）

**说明（Help）**

启用 Ticker Start 接口的余量参数（remainder parameter），用于首次到期超时（first expire timeout）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TICKER_REMAINDER_SUPPORT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_LLL_VENDOR_NORDIC
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1268`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1268)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_TICKER_REMAINDER_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TICKER_REMAINDER_SUPPORT)、[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_LLL_VENDOR_NORDIC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LLL_VENDOR_NORDIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TICKER_REMAINDER_SUPPORT`、`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_TICKER_UPDATE"></a>

## 331.77 `CONFIG_BT_TICKER_UPDATE`

**提示（Prompt）**：Ticker 更新（Ticker Update）

**说明（Help）**

启用 Ticker Update 接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_LLL_VENDOR_NORDIC
CONFIG_BT_LLL_VENDOR_OPENISA
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1260`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1260)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_LLL_VENDOR_NORDIC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LLL_VENDOR_NORDIC)、[`CONFIG_BT_LLL_VENDOR_OPENISA`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LLL_VENDOR_OPENISA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_TMAP"></a>

## 331.78 `CONFIG_BT_TMAP`

**提示（Prompt）**：电话与媒体音频配置文件（Telephony and Media Audio Profile）

**说明（Help）**

启用后将启用电话与媒体音频配置文件（TMAP）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_CAP_ACCEPTOR || CONFIG_BT_CAP_INITIATOR) && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.tmap:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.tmap#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_ACCEPTOR`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CAP_ACCEPTOR)、[`CONFIG_BT_CAP_INITIATOR`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CAP_INITIATOR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TPS"></a>

## 331.79 `CONFIG_BT_TPS`

**提示（Prompt）**：GATT 发射功率服务（GATT TX Power service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/Kconfig.tps:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/Kconfig.tps#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TRANSMIT_POWER_CONTROL"></a>

## 331.80 `CONFIG_BT_TRANSMIT_POWER_CONTROL`

**提示（Prompt）**：低功耗蓝牙功率控制（LE Power Control）

**说明（Help）**

启用低功耗蓝牙功率控制请求（LE Power Control Request）功能支持，其定义见蓝牙核心规范（Bluetooth Core specification）Version 5.4，Vol 6, Part B, Section 4.6.31。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_LE_POWER_CONTROL_SUPPORT) && CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:204`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L204)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_LE_POWER_CONTROL_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_LE_POWER_CONTROL_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_LE_POWER_CONTROL_SUPPORT`。

<a id="CONFIG_BT_TX_PROCESSOR_STACK_SIZE"></a>

## 331.81 `CONFIG_BT_TX_PROCESSOR_STACK_SIZE`

**提示（Prompt）**：发送处理器线程栈大小（TX processor thread stack size）

**说明（Help）**

发送处理器线程（TX processor thread）的栈大小。所需栈大小取决于启用哪些主机功能及功能数量。可尝试减小以节省 RAM，或在栈溢出（stack overflow）时增大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TX_PROCESSOR_THREAD && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 发送处理器线程，禁用可能导致死锁（TX processor thread, disabling may cause deadlocks）

**配置项引用（Symbol References）**：[`CONFIG_BT_TX_PROCESSOR_THREAD`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TX_PROCESSOR_THREAD)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_TX_PROCESSOR_THREAD"></a>

## 331.82 `CONFIG_BT_TX_PROCESSOR_THREAD`

**提示（Prompt）**：发送处理器线程，禁用可能导致死锁（TX processor thread, disabling may cause deadlocks）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if !CONFIG_SOC_SERIES_NRF51
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51)。

<a id="CONFIG_BT_USER_CONN_PARAM_REJECTED"></a>

## 331.83 `CONFIG_BT_USER_CONN_PARAM_REJECTED`

**提示（Prompt）**：向用户通知连接参数更新被拒绝（connection parameter update rejection）

**说明（Help）**

当应用发起的连接参数更新请求（connection parameter update request）被对端拒绝时，允许通过应用回调通知。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:399`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L399)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_USER_DATA_LEN_UPDATE"></a>

## 331.84 `CONFIG_BT_USER_DATA_LEN_UPDATE`

**提示（Prompt）**：用户控制数据长度更新过程（User control of Data Length Update Procedure）

**说明（Help）**

允许应用发起数据长度更新过程（Data Length Update Procedure），也可注册回调，接收连接数据长度变化的通知。当前数据长度信息可从连接信息（connection info）获得。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_DATA_LEN_UPDATE && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:390`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L390)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_DATA_LEN_UPDATE`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DATA_LEN_UPDATE)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_USER_PHY_UPDATE"></a>

## 331.85 `CONFIG_BT_USER_PHY_UPDATE`

**提示（Prompt）**：用户控制物理层更新过程（User control of PHY Update Procedure）

**说明（Help）**

允许应用发起物理层更新过程（PHY Update Procedure），也可注册回调，接收连接 PHY 变化的通知。当前 PHY 信息可从连接信息（connection info）获得。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PHY_UPDATE && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:342`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L342)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_PHY_UPDATE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PHY_UPDATE)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_USE_DEBUG_KEYS"></a>

## 331.86 `CONFIG_BT_USE_DEBUG_KEYS`

**提示（Prompt）**：安全管理器调试模式（Security Manager Debug Mode）

**说明（Help）**

使安全管理器（Security Manager）进入调试模式（Debug Mode），使用 Core Specification Vol. 3, Part H, 2.3.5.6.1 所述预定义 Diffie-Hellman 私钥／公钥对。警告：此选项允许任何人解密空中传输流量（on-air traffic）。强烈不建议在生产环境使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:723`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L723)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_VCP_VOL_CTLR"></a>

## 331.87 `CONFIG_BT_VCP_VOL_CTLR`

**提示（Prompt）**：音量控制配置文件音量控制器支持（Volume Control Profile Volume Controller）

**说明（Help）**

启用音量控制配置文件（Volume Control Profile）的音量控制器（Volume Controller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_CLIENT && CONFIG_BT_GATT_AUTO_DISCOVER_CCC && CONFIG_BT_SMP && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vcp:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vcp#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_CLIENT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_GATT_AUTO_DISCOVER_CCC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_AUTO_DISCOVER_CCC)、[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_VCP_VOL_CTLR_AICS"></a>

## 331.88 `CONFIG_BT_VCP_VOL_CTLR_AICS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项便于检查是否为音量控制服务（VCS）客户端启用了音频输入控制服务（AICS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_VCP_VOL_CTLR && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_VCP_VOL_CTLR_MAX_AICS_INST > 0
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vcp:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vcp#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 音量控制配置文件音量控制器支持（Volume Control Profile Volume Controller）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_CTLR`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VCP_VOL_CTLR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_VCP_VOL_CTLR_MAX_AICS_INST`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VCP_VOL_CTLR_MAX_AICS_INST)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_VCP_VOL_CTLR_MAX_AICS_INST"></a>

## 331.89 `CONFIG_BT_VCP_VOL_CTLR_MAX_AICS_INST`

**提示（Prompt）**：可设置的 AICS 最大实例数（Maximum number of AICS instances to setup）

**说明（Help）**

设置可配置并使用的音频输入控制服务（Audio Input Control Service，AICS）最大实例数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_VCP_VOL_CTLR && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 3]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vcp:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vcp#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 音量控制配置文件音量控制器支持（Volume Control Profile Volume Controller）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_CTLR`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VCP_VOL_CTLR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_VCP_VOL_CTLR_MAX_VOCS_INST"></a>

## 331.90 `CONFIG_BT_VCP_VOL_CTLR_MAX_VOCS_INST`

**提示（Prompt）**：可设置的 VOCS 最大实例数（Maximum number of VOCS instances to setup）

**说明（Help）**

设置可配置并使用的音量偏移控制服务（Volume Offset Control Service，VOCS）最大实例数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_VCP_VOL_CTLR && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, CONFIG_BT_VOCS_CLIENT_MAX_INSTANCE_COUNT]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vcp:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vcp#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 音量控制配置文件音量控制器支持（Volume Control Profile Volume Controller）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_CTLR`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VCP_VOL_CTLR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_VOCS_CLIENT_MAX_INSTANCE_COUNT`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VOCS_CLIENT_MAX_INSTANCE_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_VCP_VOL_CTLR_VOCS"></a>

## 331.91 `CONFIG_BT_VCP_VOL_CTLR_VOCS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项便于检查是否为音量控制服务（VCS）客户端启用了音量偏移控制服务（VOCS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_VCP_VOL_CTLR && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_VCP_VOL_CTLR_MAX_VOCS_INST > 0
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vcp:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vcp#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 音量控制配置文件音量控制器支持（Volume Control Profile Volume Controller）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_CTLR`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VCP_VOL_CTLR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_VCP_VOL_CTLR_MAX_VOCS_INST`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VCP_VOL_CTLR_MAX_VOCS_INST)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_VCP_VOL_REND"></a>

## 331.92 `CONFIG_BT_VCP_VOL_REND`

**提示（Prompt）**：音量控制配置文件音量呈现器支持（Volume Control Profile Volume Renderer）

**说明（Help）**

启用音量控制配置文件（Volume Control Profile）的音量呈现器角色（Volume Renderer role）及音量控制服务（Volume Control Service）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_DYNAMIC_DB && CONFIG_BT_SMP && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vcp:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vcp#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_DYNAMIC_DB`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_DYNAMIC_DB)、[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_VCP_VOL_REND_AICS"></a>

## 331.93 `CONFIG_BT_VCP_VOL_REND_AICS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项便于检查是否为音量控制服务（VCS）启用了音频输入控制服务（AICS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_VCP_VOL_REND && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_VCP_VOL_REND_AICS_INSTANCE_COUNT > 0
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vcp:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vcp#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 音量控制配置文件音量呈现器支持（Volume Control Profile Volume Renderer）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_REND`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VCP_VOL_REND)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_VCP_VOL_REND_AICS_INSTANCE_COUNT`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VCP_VOL_REND_AICS_INSTANCE_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_VCP_VOL_REND_AICS_INSTANCE_COUNT"></a>

## 331.94 `CONFIG_BT_VCP_VOL_REND_AICS_INSTANCE_COUNT`

**提示（Prompt）**：VCS 的音频输入控制服务实例数（Audio Input Control Service instance count）

**说明（Help）**

设置音量控制服务（VCS）所用音频输入控制服务（Audio Input Control Services）的实例数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_VCP_VOL_REND && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, CONFIG_BT_AICS_MAX_INSTANCE_COUNT]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vcp:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vcp#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 音量控制配置文件音量呈现器支持（Volume Control Profile Volume Renderer）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_REND`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VCP_VOL_REND)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AICS_MAX_INSTANCE_COUNT`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AICS_MAX_INSTANCE_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_VCP_VOL_REND_VOCS"></a>

## 331.95 `CONFIG_BT_VCP_VOL_REND_VOCS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项便于检查是否为音量控制服务（VCS）启用了音量偏移控制服务（VOCS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_VCP_VOL_REND && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_VCP_VOL_REND_VOCS_INSTANCE_COUNT > 0
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vcp:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vcp#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 音量控制配置文件音量呈现器支持（Volume Control Profile Volume Renderer）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_REND`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VCP_VOL_REND)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_VCP_VOL_REND_VOCS_INSTANCE_COUNT`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VCP_VOL_REND_VOCS_INSTANCE_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_VCP_VOL_REND_VOCS_INSTANCE_COUNT"></a>

## 331.96 `CONFIG_BT_VCP_VOL_REND_VOCS_INSTANCE_COUNT`

**提示（Prompt）**：音量偏移控制服务实例数（Volume Offset Control Service instance count）

**说明（Help）**

设置音量偏移控制服务（Volume Offset Control Services）的实例数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_VCP_VOL_REND && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, CONFIG_BT_VOCS_MAX_INSTANCE_COUNT]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vcp:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vcp#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 音量控制配置文件音量呈现器支持（Volume Control Profile Volume Renderer）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_REND`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VCP_VOL_REND)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_VOCS_MAX_INSTANCE_COUNT`](P332_subsys_bluetooth_配置项参考_13.md#CONFIG_BT_VOCS_MAX_INSTANCE_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_VCP_VOL_REND_VOL_FLAGS_NOTIFIABLE"></a>

## 331.97 `CONFIG_BT_VCP_VOL_REND_VOL_FLAGS_NOTIFIABLE`

**提示（Prompt）**：音量标志通知支持（Volume Flags notifiable support）

**说明（Help）**

允许客户端订阅音量标志特征（Volume Flags characteristic）的通知。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_VCP_VOL_REND && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vcp:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vcp#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 音量控制配置文件音量呈现器支持（Volume Control Profile Volume Renderer）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_REND`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VCP_VOL_REND)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_VOCS"></a>

## 331.98 `CONFIG_BT_VOCS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项启用音量控制服务（Volume Control Service）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_VOCS_MAX_INSTANCE_COUNT > 0
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vocs:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vocs#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_VOCS_MAX_INSTANCE_COUNT`](P332_subsys_bluetooth_配置项参考_13.md#CONFIG_BT_VOCS_MAX_INSTANCE_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_VOCS_CLIENT"></a>

## 331.99 `CONFIG_BT_VOCS_CLIENT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项启用音量偏移控制服务（Volume Offset Control Service）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_AUTO_DISCOVER_CCC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_VOCS_CLIENT_MAX_INSTANCE_COUNT > 0
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vocs:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vocs#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_AUTO_DISCOVER_CCC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_AUTO_DISCOVER_CCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_VOCS_CLIENT_MAX_INSTANCE_COUNT`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VOCS_CLIENT_MAX_INSTANCE_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_VOCS_CLIENT_MAX_INSTANCE_COUNT"></a>

## 331.100 `CONFIG_BT_VOCS_CLIENT_MAX_INSTANCE_COUNT`

**提示（Prompt）**：音量偏移控制服务客户端最大实例数（Volume Offset Control Service client max instance count）

**说明（Help）**

设置音量偏移控制服务客户端（Volume Offset Control Service clients）的最大实例数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 15]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.vocs:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.vocs#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<!-- kconfig-navigation -->

[上一章](P330_subsys_bluetooth_配置项参考_11.md) · [返回大纲](大纲.md) · [下一章](P332_subsys_bluetooth_配置项参考_13.md)
