---
id: learning.zephyr-docs.kconfig-reference.page-329
title: "`subsys/bluetooth`配置项参考（10/13）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第329章\_`subsys/bluetooth`配置项参考（10/13）

本章翻译官方 Kconfig 数据库中 `subsys/bluetooth` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_MESH_PB_ADV_USE_RELAY_SETS"></a>

## 329.1 `CONFIG_BT_MESH_PB_ADV_USE_RELAY_SETS`

**提示（Prompt）**：使用中继广播集合发送配网 PDU（relay advertising sets for provisioning PDUs）

**说明（Help）**

使用中继广播集合发送配网 PDU（relay advertising sets for provisioning PDUs）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_RELAY_ADV_SETS > 0 && CONFIG_BT_MESH_PB_ADV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:260`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L260)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning） → 广播承载配网支持（PB-ADV support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RELAY_ADV_SETS`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RELAY_ADV_SETS)、[`CONFIG_BT_MESH_PB_ADV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_PB_ADV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_PB_GATT"></a>

## 329.2 `CONFIG_BT_MESH_PB_GATT`

**提示（Prompt）**：GATT 承载配网服务器支持（PB-GATT Server support）

**说明（Help）**

启用后，允许通过 GATT 为设备配网（provisioned）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_MESH_GATT_SERVER
CONFIG_BT_MESH_PROV
CONFIG_BT_MESH_PB_GATT_COMMON
CONFIG_BT_MESH_PROVISIONEE
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:303`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L303)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_GATT_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT_SERVER)、[`CONFIG_BT_MESH_PROV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROV)、[`CONFIG_BT_MESH_PB_GATT_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PB_GATT_COMMON)、[`CONFIG_BT_MESH_PROVISIONEE`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_PROVISIONEE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_MESH_GATT_SERVER`、`CONFIG_BT_MESH_PROV`、`CONFIG_BT_MESH_PB_GATT_COMMON`。

<a id="CONFIG_BT_MESH_PB_GATT_CLIENT"></a>

## 329.3 `CONFIG_BT_MESH_PB_GATT_CLIENT`

**提示（Prompt）**：GATT 承载配网客户端支持（PB-GATT Client support）

**说明（Help）**

启用后，允许配网器（provisioner）通过 GATT 为设备配网。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CENTRAL && CONFIG_BT_CONN && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_MESH_PROV
CONFIG_BT_GATT_CLIENT
CONFIG_BT_MESH_GATT_CLIENT
CONFIG_BT_MESH_PB_GATT_COMMON
CONFIG_BT_MESH_PROVISIONER
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:321`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L321)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning）

**配置项引用（Symbol References）**：[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_PROV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROV)、[`CONFIG_BT_GATT_CLIENT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_MESH_GATT_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT_CLIENT)、[`CONFIG_BT_MESH_PB_GATT_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PB_GATT_COMMON)、[`CONFIG_BT_MESH_PROVISIONER`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_PROVISIONER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_MESH_PROV`、`CONFIG_BT_MESH_GATT_CLIENT`、`CONFIG_BT_MESH_PB_GATT_COMMON`。

<a id="CONFIG_BT_MESH_PB_GATT_USE_DEVICE_NAME"></a>

## 329.4 `CONFIG_BT_MESH_PB_GATT_USE_DEVICE_NAME`

**提示（Prompt）**：在扫描响应中包含蓝牙设备名称（Bluetooth device name in scan response）

**说明（Help）**

启用 PB-GATT 时，在扫描响应（scan response）中包含 GAP 设备名称（device name）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PB_GATT && CONFIG_BT_CONN && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:313`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L313)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning） → GATT 承载配网服务器支持（PB-GATT Server support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PB_GATT`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_PB_GATT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_PENDING_STORE"></a>

## 329.5 `CONFIG_BT_MESH_PENDING_STORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于延后保存待存储 Mesh 数据（pending mesh data）的调度器。使用设置子系统（settings subsystem）时会启用；不使用设置子系统、但通过该调度器安排存储操作的存储后端也会选择它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_SETTINGS
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1858`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1858)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SETTINGS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_SETTINGS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_PRIV_BEACONS"></a>

## 329.6 `CONFIG_BT_MESH_PRIV_BEACONS`

**提示（Prompt）**：私有信标支持（private beacons）

**说明（Help）**

启用私有信标（private beacons）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1554`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1554)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 信标（Beacons）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_PRIV_BEACON_CLI"></a>

## 329.7 `CONFIG_BT_MESH_PRIV_BEACON_CLI`

**提示（Prompt）**：私有信标客户端模型支持（Private Beacon Client Model）

**说明（Help）**

启用私有信标客户端模型（Private Beacon Client model）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PRIV_BEACONS && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1336`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1336)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PRIV_BEACONS`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_PRIV_BEACONS)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_PRIV_BEACON_SRV"></a>

## 329.8 `CONFIG_BT_MESH_PRIV_BEACON_SRV`

**提示（Prompt）**：私有信标服务器模型支持（Private Beacon Server Model）

**说明（Help）**

启用私有信标服务器模型（Private Beacon Server model）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_MODEL_EXTENSIONS && CONFIG_BT_MESH_PRIV_BEACONS && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1330`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1330)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_MODEL_EXTENSIONS`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_MODEL_EXTENSIONS)、[`CONFIG_BT_MESH_PRIV_BEACONS`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_PRIV_BEACONS)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_PROVISIONEE"></a>

## 329.9 `CONFIG_BT_MESH_PROVISIONEE`

**提示（Prompt）**：待配网设备角色支持（Provisionee role support）

**说明（Help）**

启用后，允许将设备配入 Mesh 网络（provisioned into a mesh network）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_MESH_PB_ADV || CONFIG_BT_MESH_PB_GATT) && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_BT_MESH_PB_GATT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:335`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L335)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PB_ADV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_PB_ADV)、[`CONFIG_BT_MESH_PB_GATT`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_PB_GATT)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_PROVISIONER"></a>

## 329.10 `CONFIG_BT_MESH_PROVISIONER`

**提示（Prompt）**：配网器支持（Provisioner support）

**说明（Help）**

启用后，支持为远端设备配网（provisioning remote devices）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_CDB && CONFIG_BT_MESH_PROV && (CONFIG_BT_MESH_PB_ADV || CONFIG_BT_MESH_PB_GATT_CLIENT) && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_MESH_PB_GATT_CLIENT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:378`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L378)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CDB`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_CDB)、[`CONFIG_BT_MESH_PROV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROV)、[`CONFIG_BT_MESH_PB_ADV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_PB_ADV)、[`CONFIG_BT_MESH_PB_GATT_CLIENT`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_PB_GATT_CLIENT)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MESH_PROV`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_PROV_OOB_API_LEGACY"></a>

## 329.11 `CONFIG_BT_MESH_PROV_OOB_API_LEGACY`

**提示（Prompt）**：缩减最大带外认证大小支持（Reduced maximum OOB authentication size）[已弃用，DEPRECATED]

**说明（Help）**

默认最大带外认证（OOB authentication）大小为 `32` 字节。启用后，使用仅兼容规范 v1.1 及更早版本的传统 API（legacy API），将带外认证限制为最多 `8` 字节。此选项用于向后兼容；由于安全性降低，不建议用于新设计。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PROV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:366`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L366)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MESH_PROV`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_PROV_OOB_PUBLIC_KEY"></a>

## 329.12 `CONFIG_BT_MESH_PROV_OOB_PUBLIC_KEY`

**提示（Prompt）**：带外公钥支持（OOB Public key support）

**说明（Help）**

如果通过带外技术（Out of Band，OOB）交换公钥（public key），则启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PROVISIONEE && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:342`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L342)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning） → 待配网设备角色支持（Provisionee role support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONEE`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_PROVISIONEE)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_PROXY_CLIENT"></a>

## 329.13 `CONFIG_BT_MESH_PROXY_CLIENT`

**提示（Prompt）**：代理客户端支持（Proxy client support）

**说明（Help）**

启用 Mesh GATT 代理客户端（Proxy Client）支持，即能够在 Mesh GATT 服务（Service）与 Mesh 网络之间充当代理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CENTRAL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_GATT_CLIENT
CONFIG_BT_MESH_GATT_CLIENT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1489`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1489)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 代理（Proxy）

**配置项引用（Symbol References）**：[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_GATT_CLIENT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_MESH_GATT_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT_CLIENT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_MESH_GATT_CLIENT`。

<a id="CONFIG_BT_MESH_PROXY_FILTER_SIZE"></a>

## 329.14 `CONFIG_BT_MESH_PROXY_FILTER_SIZE`

**提示（Prompt）**：每个代理客户端的过滤条目最大数量（filter entries per Proxy Client）

**说明（Help）**

指定本地节点支持的代理过滤条目（Proxy Filter entries）数量，帮助减少发给代理客户端（proxy client）的非必要流量。此值由应用需求决定，应足够大，使代理客户端能以默认接纳列表过滤类型（accept list filter type），通过该代理服务器节点与多个设备通信。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_GATT_PROXY && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 32767]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1476`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1476)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 代理（Proxy） → GATT 代理服务支持（GATT Proxy Service support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_GATT_PROXY`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_GATT_PROXY)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_PROXY_SOLICITATION"></a>

## 329.15 `CONFIG_BT_MESH_PROXY_SOLICITATION`

**提示（Prompt）**：代理请求功能（Proxy solicitation feature）

**说明（Help）**

启用请求 PDU（Solicitation PDUs）发送支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_MESH_SOLICITATION
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1502`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1502)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 代理（Proxy）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_SOLICITATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SOLICITATION)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_MESH_SOLICITATION`。

<a id="CONFIG_BT_MESH_PROXY_SRPL_SIZE"></a>

## 329.16 `CONFIG_BT_MESH_PROXY_SRPL_SIZE`

**提示（Prompt）**：请求重放保护列表大小（solicitation replay protection list，SRPL）

**说明（Help）**

SRPL 的大小。该列表用于判断收到的请求 PDU（Solicitation PDU）是否有效。满足下列任一条件即有效：

- 收到的 PDU 的 `SSRC` 字段值已保存在 SRPL 中，且其 `SSEQ` 字段值大于对应的已存储 SSEQ。
- 该 SSRC 尚未存入列表，且 SRPL 仍有空间保存新条目。

译注：原文第二种条件将列表写为 `RPL`；本条上下文与后续容量判断均为 `SRPL`，这里指出该名称差异。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_OD_PRIV_PROXY_SRV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1369`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1369)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 按需私有代理服务器模型支持（On-Demand Private Proxy Server model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_OD_PRIV_PROXY_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_OD_PRIV_PROXY_SRV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_PROXY_USE_DEVICE_NAME"></a>

## 329.17 `CONFIG_BT_MESH_PROXY_USE_DEVICE_NAME`

**提示（Prompt）**：在扫描响应中包含蓝牙设备名称（Bluetooth device name in scan response）

**说明（Help）**

启用 GATT 代理（GATT Proxy）功能时，在扫描响应（scan response）中包含 GAP 设备名称（device name）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_GATT_PROXY && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1470`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1470)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 代理（Proxy） → GATT 代理服务支持（GATT Proxy Service support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_GATT_PROXY`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_GATT_PROXY)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_RELAY"></a>

## 329.18 `CONFIG_BT_MESH_RELAY`

**提示（Prompt）**：中继支持（Relay support）

**说明（Help）**

支持作为 Mesh 中继节点（Mesh Relay Node）运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:470`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L470)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 网络层（Network layer）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_RELAY_ADV_SETS"></a>

## 329.19 `CONFIG_BT_MESH_RELAY_ADV_SETS`

**提示（Prompt）**：最大同时中继消息数量（Maximum simultaneous relay messages）

**说明（Help）**

支持的最大同时中继消息数量，要求控制器支持多个广播集合（advertising sets）。注意：子网桥接（Subnet Bridge）功能也使用中继广播集合。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_MESH_RELAY || CONFIG_BT_MESH_BRG_CFG_SRV) && CONFIG_BT_MESH_ADV_EXT && <choice CONFIG_BT_MESH_ADV>
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, CONFIG_BT_EXT_ADV_MAX_ADV_SET]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser） → 广播者模式（Advertiser mode） → 扩展广播（Extended advertising）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RELAY`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RELAY)、[`CONFIG_BT_MESH_BRG_CFG_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BRG_CFG_SRV)、[`CONFIG_BT_MESH_ADV_EXT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV_EXT)、[`CONFIG_BT_MESH_ADV`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV)、[`CONFIG_BT_EXT_ADV_MAX_ADV_SET`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV_MAX_ADV_SET)。

<a id="CONFIG_BT_MESH_RELAY_BUF_COUNT"></a>

## 329.20 `CONFIG_BT_MESH_RELAY_BUF_COUNT`

**提示（Prompt）**：中继消息广播缓冲区数量（advertising buffers for relayed messages）

**说明（Help）**

可用于待中继消息的广播缓冲区数量。较多缓冲区提高 Mesh 网络可靠性；较少缓冲区降低中继节点（Relay Node）的消息延迟，但也会增加丢包。

评估消息延迟时，还应考虑 `BT_MESH_RELAY_RETRANSMIT_COUNT` 和 `BT_MESH_RELAY_RETRANSMIT_INTERVAL`。增大 `BT_MESH_RELAY_ADV_SETS` 可在维持延迟的同时增加缓冲区数量。

注意：子网桥接（Subnet Bridge）功能也使用中继广播缓冲区。如果同时启用中继和子网桥接，应考虑增加的负载。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_MESH_RELAY || CONFIG_BT_MESH_BRG_CFG_SRV) && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:505`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L505)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 网络层（Network layer）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RELAY`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RELAY)、[`CONFIG_BT_MESH_BRG_CFG_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BRG_CFG_SRV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_RELAY_ENABLED"></a>

## 329.21 `CONFIG_BT_MESH_RELAY_ENABLED`

**提示（Prompt）**：默认启用中继功能（Relay feature enabled by default）

**说明（Help）**

控制设备首次启动或未配网（unprovisioned）时是否默认启用中继功能（Relay feature）。可在运行时使用 `bt_mesh_relay_set()` 更改。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_RELAY && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:477`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L477)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 网络层（Network layer） → 中继支持（Relay support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RELAY`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RELAY)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_RELAY_RETRANSMIT_COUNT"></a>

## 329.22 `CONFIG_BT_MESH_RELAY_RETRANSMIT_COUNT`

**提示（Prompt）**：中继重传次数（Relay Retransmit Count）

**说明（Help）**

控制中继消息在首次发送之外的初始重传次数（retransmissions），可以通过运行时配置更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_RELAY && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:485`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L485)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 网络层（Network layer） → 中继支持（Relay support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RELAY`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RELAY)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_RELAY_RETRANSMIT_INTERVAL"></a>

## 329.23 `CONFIG_BT_MESH_RELAY_RETRANSMIT_INTERVAL`

**提示（Prompt）**：中继重传间隔（Relay Retransmit Interval）

**说明（Help）**

控制中继消息重传之间的初始间隔，单位为毫秒，可以通过运行时配置更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_RELAY && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[10, 330]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:494`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L494)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 网络层（Network layer） → 中继支持（Relay support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RELAY`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RELAY)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_RPL_STORAGE_MODE"></a>

## 329.24 `CONFIG_BT_MESH_RPL_STORAGE_MODE`

**提示（Prompt）**：重放保护列表存储模式（Replay protection list storage mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_RPL_STORAGE_MODE_SETTINGS
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_RPL_STORAGE_MODE_SETTINGS
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:765`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L765)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 重放保护列表（Replay Protection List）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_RPL_STORAGE_MODE_SETTINGS`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RPL_STORAGE_MODE_SETTINGS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_RPL_STORAGE_MODE_SETTINGS"></a>

## 329.25 `CONFIG_BT_MESH_RPL_STORAGE_MODE_SETTINGS`

**提示（Prompt）**：在 Settings 中持久化保存 RPL（Persistent storage of RPL in Settings）

**说明（Help）**

在设置子系统（Settings）中持久化保存重放保护列表（RPL）。如果未启用 `BT_SETTINGS`，此选择项提供 RPL 的非持久化实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_RPL_STORAGE_MODE>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:769`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L769)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 重放保护列表（Replay Protection List） → 重放保护列表存储模式（Replay protection list storage mode）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RPL_STORAGE_MODE`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RPL_STORAGE_MODE)。

<a id="CONFIG_BT_MESH_RPL_STORE_TIMEOUT"></a>

## 329.26 `CONFIG_BT_MESH_RPL_STORE_TIMEOUT`

**提示（Prompt）**：保存未写入的 RPL 与 SRPL 条目之前的最小间隔（Minimum interval for unsaved entries）

**说明（Help）**

定义将未保存的 RPL 与 SRPL 条目写入持久存储（persistent storage）之前的时间，单位为秒。SRPL 始终通过设置子系统保存；只有 RPL 存储模式使用此超时安排存储时，RPL 才受此值影响。

设得过大时，如果节点在定时器触发前断电，可能形成安全漏洞。使用 Flash 作为持久存储时，设得过小则可能最终磨损 Flash。但如果 RPL 更新不频繁，设为 `0`，即立即写入，也可能合理。

设为 `-1` 会禁用该定时器。在设置存储模式（settings storage mode）下，用户随后负责使用 `bt_mesh_rpl_pending_store` 保存待写入的 RPL 条目。与此同时，因 IV 索引更新或恢复而失效的重放列表仍会立即保存。

合理平衡此超时与 `bt_mesh_rpl_pending_store` 的调用，可降低安全漏洞和 Flash 磨损风险。未保存 RPL、导致重启后暴露于重放风险，会使设备无法执行规范要求的重放保护（replay protection）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PENDING_STORE && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[-1, 1000000]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1895`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1895)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 持久化存储（Persistent storage）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PENDING_STORE`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_PENDING_STORE)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_RPR_AD_TYPES_MAX"></a>

## 329.27 `CONFIG_BT_MESH_RPR_AD_TYPES_MAX`

**提示（Prompt）**：扩展扫描中的最大 AD 类型数量（Max AD types in extended scanning）

**说明（Help）**

扩展扫描（extended scanning）期间，远程配网服务器（Remote Provisioning Server）可在扫描报告中包含一组从未配网设备广播数据中收集的广播数据类型（AD types）。此选项控制单个服务器可扫描、客户端可请求的最大 AD 类型数量。

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
[1, 16]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1235`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1235)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 远程配网配置（Remote Provisioning configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_RPR_CLI"></a>

## 329.28 `CONFIG_BT_MESH_RPR_CLI`

**提示（Prompt）**：远程配网客户端模型支持（Remote Provisioning Client model）

**说明（Help）**

远程配网客户端（Remote Provisioning Client）实例化在配网器节点上，通过 Mesh 网络将配网消息以隧道方式传送给远程配网服务器（Remote Provisioning Server），从而为新设备配网。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PROVISIONER && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1224`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1224)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONER`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_PROVISIONER)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_RPR_SRV"></a>

## 329.29 `CONFIG_BT_MESH_RPR_SRV`

**提示（Prompt）**：远程配网服务器模型支持（Remote Provisioning Server model）

**说明（Help）**

远程配网服务器（Remote Provisioning Server）作为配网过程的代理。配网器通过 Mesh 将配网消息以隧道方式发送到该服务器，由服务器直接与未配网节点（unprovisioned node）通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1216)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_RPR_SRV_AD_DATA_MAX"></a>

## 329.30 `CONFIG_BT_MESH_RPR_SRV_AD_DATA_MAX`

**提示（Prompt）**：可报告的最大附加广播数据量（Max additional advertisement data to report）

**说明（Help）**

扩展扫描（extended scanning）期间报告附加广播数据（additional advertisement data）所用的缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
31
```

**取值范围（Ranges）**

```text
[3, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1254`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1254)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 远程配网配置（Remote Provisioning configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_RPR_SRV_SCANNED_ITEMS_MAX"></a>

## 329.31 `CONFIG_BT_MESH_RPR_SRV_SCANNED_ITEMS_MAX`

**提示（Prompt）**：远程配网服务器可扫描的未配网设备最大数量（Max scannable unprovisioned devices）

**说明（Help）**

单个远程配网服务器（Remote Provisioning Server）可保存的不同未配网设备最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[4, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1246`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1246)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 远程配网配置（Remote Provisioning configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_RX_BLOB_CHUNK_SIZE"></a>

## 329.32 `CONFIG_BT_MESH_RX_BLOB_CHUNK_SIZE`

**提示（Prompt）**：BLOB 服务器分片大小（BLOB Server chunk size）

**说明（Help）**

设置 BLOB 服务器的分片大小（chunk size）。实际最大分片大小取决于可支持的分段（segments）数量；如果设置值过大，会被限制到实际可用的最大值。另请参阅 `BT_MESH_RX_SEG_MAX` 以及节点能够接收的最大 SDU。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_BT_MESH_ALIGN_CHUNK_SIZE_TO_MAX_SEGMENT && CONFIG_BT_MESH_BLOB_SRV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[8, 377]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:989`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L989)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → BLOB 传输服务器模型支持（BLOB Transfer Server model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ALIGN_CHUNK_SIZE_TO_MAX_SEGMENT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ALIGN_CHUNK_SIZE_TO_MAX_SEGMENT)、[`CONFIG_BT_MESH_BLOB_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_SRV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_RX_SEG_MAX"></a>

## 329.33 `CONFIG_BT_MESH_RX_SEG_MAX`

**提示（Prompt）**：入站消息的最大分段数（Maximum number of segments in incoming messages）

**说明（Help）**

入站消息支持的最大分段（segments）数量。通常应根据本地节点支持的模型微调，即根据节点必须能够接收的最大消息有效载荷决定。此值影响内存和调用栈消耗，因此默认值低于规范允许的最大值 `32` 段。

最大入站 SDU 大小等于该数量的 `12` 倍，其中 `4` 或 `8` 字节用于传输层消息完整性校验值（Transport Layer MIC）。例如，`5` 段对应最大 `60` 字节 SDU；使用 4 字节 MIC 时留给应用层数据 `56` 字节，使用 8 字节 MIC 时留出 `52` 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_RX_SEG_MSG_COUNT > 0 && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
6 if CONFIG_BT_MESH_BLOB_SRV || CONFIG_BT_MESH_BLOB_CLI || CONFIG_BT_MESH_RPR_SRV || CONFIG_BT_MESH_RPR_CLI
3
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:572`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L572)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RX_SEG_MSG_COUNT`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RX_SEG_MSG_COUNT)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_BLOB_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_SRV)、[`CONFIG_BT_MESH_BLOB_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_CLI)、[`CONFIG_BT_MESH_RPR_SRV`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RPR_SRV)、[`CONFIG_BT_MESH_RPR_CLI`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RPR_CLI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_RX_SEG_MSG_COUNT"></a>

## 329.34 `CONFIG_BT_MESH_RX_SEG_MSG_COUNT`

**提示（Prompt）**：最大同时入站分段消息数量（simultaneous incoming segmented messages）

**说明（Help）**

最大同时入站多段消息和／或可靠消息（multi-segment and/or reliable messages）数量。注意：Mesh 分段与重组（Segmentation/reassembly）是规范要求的必备功能；设为零会使设备无法接收任何 Mesh 分段消息。

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
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:543`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L543)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SAR_CFG_CLI"></a>

## 329.35 `CONFIG_BT_MESH_SAR_CFG_CLI`

**提示（Prompt）**：SAR 配置客户端模型支持（SAR Configuration Client Model）

**说明（Help）**

启用分段与重组（SAR）配置客户端模型支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_MESH_SAR_CFG
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1273`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1273)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_SAR_CFG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_CFG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_MESH_SAR_CFG`。

<a id="CONFIG_BT_MESH_SAR_CFG_SRV"></a>

## 329.36 `CONFIG_BT_MESH_SAR_CFG_SRV`

**提示（Prompt）**：SAR 配置服务器模型支持（SAR Configuration Server model）

**说明（Help）**

启用分段与重组（SAR）配置服务器模型支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_MESH_SAR_CFG
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1267`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1267)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_SAR_CFG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_CFG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_MESH_SAR_CFG`。

<a id="CONFIG_BT_MESH_SAR_RX_ACK_DELAY_INC"></a>

## 329.37 `CONFIG_BT_MESH_SAR_RX_ACK_DELAY_INC`

**提示（Prompt）**：确认延迟增量（Acknowledgment delay increment）

**说明（Help）**

控制收到新分段后、延迟发送确认消息（acknowledgment message）的间隔增量。增量以分段（segments）为计量单位，计算公式为 `CONFIG_BT_MESH_SAR_RX_ACK_DELAY_INC + 1.5`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x01
```

**取值范围（Ranges）**

```text
[0x00, 0x07]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:696`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L696)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT"></a>

## 329.38 `CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT`

**提示（Prompt）**：确认消息重传总次数（Total acknowledgment message retransmissions）

**说明（Help）**

当分段消息的分段数量超过 `CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD` 时，此值定义协议栈额外发送的确认消息（acknowledgment message）重传总次数。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x00
```

**取值范围（Ranges）**

```text
[0x00, 0x03]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:726`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L726)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SAR_RX_DISCARD_TIMEOUT"></a>

## 329.39 `CONFIG_BT_MESH_SAR_RX_DISCARD_TIMEOUT`

**提示（Prompt）**：分段消息接收的丢弃超时（Discard timeout for reception of a segmented message）

**说明（Help）**

定义自最后一个成功接收的分段（segment）起，等待多久后放弃接收该分段消息（segmented message）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x01
```

**取值范围（Ranges）**

```text
[0x00, 0x0F]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:718`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L718)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SAR_RX_SEG_INT_STEP"></a>

## 329.40 `CONFIG_BT_MESH_SAR_RX_SEG_INT_STEP`

**提示（Prompt）**：分段接收间隔步进（Segments reception interval step）

**说明（Help）**

定义收到新分段后、延迟发送确认消息（acknowledgment message）所用的分段接收间隔步进。间隔单位为毫秒，计算公式为 `(CONFIG_BT_MESH_SAR_RX_SEG_INT_STEP + 1) * 10 ms`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x05
```

**取值范围（Ranges）**

```text
[0x00, 0x0F]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:707`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L707)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD"></a>

## 329.41 `CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD`

**提示（Prompt）**：确认重传阈值（Acknowledgments retransmission threshold）

**说明（Help）**

定义确认重传（acknowledgment retransmissions）的阈值，以一条分段消息的分段数量表示。当分段数量大于此阈值时，协议栈会额外重传每条确认消息，次数由 `CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT` 决定。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x03
```

**取值范围（Ranges）**

```text
[0x00, 0x1F]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:685`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L685)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_COUNT"></a>

## 329.42 `CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_COUNT`

**提示（Prompt）**：向组播地址重传的总次数（Total retransmissions to multicast address）

**说明（Help）**

控制向组播地址（multicast address）重传分段消息（segmented message）的总次数。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x02
```

**取值范围（Ranges）**

```text
[0x00, 0x0F]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:666`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L666)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_INT"></a>

## 329.43 `CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_INT`

**提示（Prompt）**：向组播地址重传的间隔（Interval between retransmissions to multicast address）

**说明（Help）**

控制向组播地址（multicast address）重传一条分段消息全部分段的间隔。单位为毫秒，计算公式为 `(CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_INT + 1) * 25 ms`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x09
```

**取值范围（Ranges）**

```text
[0x00, 0x0F]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:674`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L674)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SAR_TX_SEG_INT_STEP"></a>

## 329.44 `CONFIG_BT_MESH_SAR_TX_SEG_INT_STEP`

**提示（Prompt）**：连续发送两个分段之间的间隔（Interval between sending two consecutive segments）

**说明（Help）**

控制分段消息（segmented message）中连续发送两个分段的间隔。单位为毫秒，计算公式为 `(CONFIG_BT_MESH_SAR_TX_SEG_INT_STEP + 1) * 10 ms`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x05
```

**取值范围（Ranges）**

```text
[0x00, 0x0F]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:616`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L616)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_COUNT"></a>

## 329.45 `CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_COUNT`

**提示（Prompt）**：向单播地址重传的最大次数（Maximum retransmissions to unicast address）

**说明（Help）**

控制向单播地址（unicast address）重传分段消息（segmented message）的最大次数，达到后放弃传输。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x02
```

**取值范围（Ranges）**

```text
[0x00, 0x0F]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:626`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L626)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_INC"></a>

## 329.46 `CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_INC`

**提示（Prompt）**：向单播地址重传缺失分段的间隔增量（Retransmissions interval increment）

**说明（Help）**

控制向单播地址（unicast address）延迟重传未获确认分段（unacknowledged segments）所用的间隔增量。单位为毫秒，计算公式为 `(CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_INC + 1) * 25 ms`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x01
```

**取值范围（Ranges）**

```text
[0x00, 0x0F]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:655`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L655)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_STEP"></a>

## 329.47 `CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_STEP`

**提示（Prompt）**：向单播地址重传缺失分段的间隔步进（Retransmissions interval step）

**说明（Help）**

控制向单播地址（unicast address）延迟重传未获确认分段（unacknowledged segments）所用的间隔步进。单位为毫秒，计算公式为 `(CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_STEP + 1) * 25 ms`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x07
```

**取值范围（Ranges）**

```text
[0x00, 0x0F]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:644`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L644)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_WITHOUT_PROG_COUNT"></a>

## 329.48 `CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_WITHOUT_PROG_COUNT`

**提示（Prompt）**：向单播地址无进展重传的最大次数（Maximum retransmissions without progress）

**说明（Help）**

如果超时期间未收到确认，或收到的确认仅包含已经确认过的分段（segments），此值定义协议栈向单播地址（unicast address）重传该分段消息的最大次数。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x02
```

**取值范围（Ranges）**

```text
[0x00, 0x0F]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:634`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L634)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SEG_BUFS"></a>

## 329.49 `CONFIG_BT_MESH_SEG_BUFS`

**提示（Prompt）**：可用分段缓冲区数量（Number of segment buffers available）

**说明（Help）**

入站和出站分段消息从同一个池（pool）分配分段（segments）。每个分段是 `12` 字节块，同一时刻只能由一条消息使用。

出站消息在开始发送时分配全部分段；每个分段一旦获得接收方确认，就逐个释放。入站消息在事务（transaction）开始时分配全部分段，直到完整收到消息后才释放。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[CONFIG_BT_MESH_RX_SEG_MAX, 16384] if CONFIG_BT_MESH_RX_SEG_MAX > CONFIG_BT_MESH_TX_SEG_MAX
[CONFIG_BT_MESH_TX_SEG_MAX, 16384]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:555`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L555)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_RX_SEG_MAX`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RX_SEG_MAX)、[`CONFIG_BT_MESH_TX_SEG_MAX`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_TX_SEG_MAX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SELF_TEST"></a>

## 329.50 `CONFIG_BT_MESH_SELF_TEST`

**提示（Prompt）**：执行自检（Perform self-tests）

**说明（Help）**

添加额外自检（self-tests），每次初始化 Mesh 网络时运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1967`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1967)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SEQ_STORE_RATE"></a>

## 329.51 `CONFIG_BT_MESH_SEQ_STORE_RATE`

**提示（Prompt）**：存储中的序列号更新频率（How often sequence number gets updated in storage）

**说明（Help）**

定义本地序列号（sequence number）在持久存储中更新的频率，例如 Flash。值为 `100` 表示每递增 `100` 次后保存一次。节点发送消息十分频繁时，较大值更合理；不频繁时，设为 `0`，即每次递增都更新存储，也可能合理。

协议栈初始化时，会将该数值加到最后保存的序列号上，以保证启动时的值大于断电前最后使用的值。

译注：原文将 `0` 定义为每次保存，同时用“加上该数值”概括启动行为；这里保留两处说明，不将该概括扩展成对零值边界的实现推断。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1 if !CONFIG_BT_SETTINGS
128
```

**取值范围（Ranges）**

```text
[0, 1000000]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1878`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1878)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 持久化存储（Persistent storage）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SETTINGS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_SETTINGS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SETTINGS_WORKQ"></a>

## 329.52 `CONFIG_BT_MESH_SETTINGS_WORKQ`

**提示（Prompt）**：在独立工作队列中保存蓝牙 Mesh 设置（separate work queue for Bluetooth Mesh settings）

**说明（Help）**

启用一个独立的协作式线程（cooperative thread），用于保存蓝牙 Mesh 配置。禁用时，协议栈配置保存在系统工作队列（system workqueue）中；保存待写入数据期间，系统工作队列会被阻塞。如果 Flash 驱动执行擦除，阻塞时间可能显著增加。

启用后，蓝牙 Mesh 不再因此阻塞系统工作队列；当 Flash 驱动等待控制器分配写入数据和／或擦除所需 Flash 页的时间时，仍可处理入站和出站消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1921`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1921)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 持久化存储（Persistent storage）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SETTINGS_WORKQ_STACK_SIZE"></a>

## 329.53 `CONFIG_BT_MESH_SETTINGS_WORKQ_STACK_SIZE`

**提示（Prompt）**：设置工作队列栈大小（Stack size of the settings workq）

**说明（Help）**

设置工作队列（settings workqueue）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_SETTINGS_WORKQ && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1200 if CONFIG_BT_MESH_RPR_SRV
900
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1942`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1942)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 持久化存储（Persistent storage） → 在独立工作队列中保存蓝牙 Mesh 设置（separate work queue for Bluetooth Mesh settings）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_SETTINGS_WORKQ`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SETTINGS_WORKQ)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_RPR_SRV`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RPR_SRV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL"></a>

## 329.54 `CONFIG_BT_MESH_SHELL`

**提示（Prompt）**：蓝牙 Mesh Shell（Bluetooth Mesh shell）

**说明（Help）**

启用向控制台提供蓝牙 Mesh 命令的 Shell 模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_SHELL
CONFIG_BT_PRIVATE_SHELL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_BT_PRIVATE_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PRIVATE_SHELL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_PRIVATE_SHELL`。

<a id="CONFIG_BT_MESH_SHELL_BLOB_CLI"></a>

## 329.55 `CONFIG_BT_MESH_SHELL_BLOB_CLI`

**提示（Prompt）**：BLOB 传输客户端 Shell 命令支持（BLOB Transfer Client shell commands）

**说明（Help）**

BLOB 传输客户端（BLOB Transfer Client）的 Shell 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_BLOB_CLI && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BLOB_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_CLI)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_BLOB_IO_FLASH"></a>

## 329.56 `CONFIG_BT_MESH_SHELL_BLOB_IO_FLASH`

**提示（Prompt）**：BLOB IO 闪存流 Shell 命令支持（BLOB IO flash stream shell commands）

**说明（Help）**

BLOB 传输客户端（BLOB Transfer Client）的 Shell 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_BLOB_IO_FLASH && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BLOB_IO_FLASH`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_IO_FLASH)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_BLOB_SRV"></a>

## 329.57 `CONFIG_BT_MESH_SHELL_BLOB_SRV`

**提示（Prompt）**：BLOB 传输服务器 Shell 命令支持（BLOB Transfer Server shell commands）

**说明（Help）**

BLOB 传输服务器（BLOB Transfer Server）的 Shell 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_BLOB_SRV && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BLOB_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_SRV)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_BRG_CFG_CLI"></a>

## 329.58 `CONFIG_BT_MESH_SHELL_BRG_CFG_CLI`

**提示（Prompt）**：桥接配置客户端 Shell 命令支持（Bridge Configuration Client shell commands）

**说明（Help）**

启用桥接配置客户端（Bridge Configuration Client）的 Shell 命令支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_BRG_CFG_CLI && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BRG_CFG_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BRG_CFG_CLI)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_CDB"></a>

## 329.59 `CONFIG_BT_MESH_SHELL_CDB`

**提示（Prompt）**：配置数据库 Shell 命令支持（CDB shell commands）

**说明（Help）**

启用配置数据库（CDB）的 Shell 命令支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_CDB && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CDB`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_CDB)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_CFG_CLI"></a>

## 329.60 `CONFIG_BT_MESH_SHELL_CFG_CLI`

**提示（Prompt）**：配置客户端 Shell 命令支持（Configuration Client shell commands）

**说明（Help）**

启用配置客户端（Configuration Client）的 Shell 命令支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_CFG_CLI && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CFG_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_CFG_CLI)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_DFD_SRV"></a>

## 329.61 `CONFIG_BT_MESH_SHELL_DFD_SRV`

**提示（Prompt）**：固件分发服务器 Shell 命令支持（Firmware Distribution Server shell commands）

**说明（Help）**

固件分发服务器（Firmware Distribution Server）的 Shell 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_DFD_SRV && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFD_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_DFD_SRV)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_DFU_CLI"></a>

## 329.62 `CONFIG_BT_MESH_SHELL_DFU_CLI`

**提示（Prompt）**：固件更新客户端 Shell 命令支持（Firmware Update Client shell commands）

**说明（Help）**

固件更新客户端（Firmware Update Client）的 Shell 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_DFU_CLI && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFU_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_DFU_CLI)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_DFU_METADATA"></a>

## 329.63 `CONFIG_BT_MESH_SHELL_DFU_METADATA`

**提示（Prompt）**：DFU 元数据 Shell 命令支持（DFU metadata shell commands）

**说明（Help）**

设备固件更新元数据（DFU metadata）的 Shell 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_DFU_METADATA && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFU_METADATA`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_DFU_METADATA)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_DFU_SLOT"></a>

## 329.64 `CONFIG_BT_MESH_SHELL_DFU_SLOT`

**提示（Prompt）**：DFU 槽位 API Shell 命令支持（DFU slot API shell commands）

**说明（Help）**

设备固件更新槽位 API（DFU slot API）的 Shell 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_DFU_SLOTS && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_MESH_SHELL_DFU_CLI || CONFIG_BT_MESH_SHELL_DFD_SRV
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFU_SLOTS`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_DFU_SLOTS)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_SHELL_DFU_CLI`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL_DFU_CLI)、[`CONFIG_BT_MESH_SHELL_DFD_SRV`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL_DFD_SRV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_DFU_SRV"></a>

## 329.65 `CONFIG_BT_MESH_SHELL_DFU_SRV`

**提示（Prompt）**：固件更新服务器 Shell 命令支持（Firmware Update Server shell commands）

**说明（Help）**

固件更新服务器（Firmware Update Server）的 Shell 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_DFU_SRV && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFU_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_DFU_SRV)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_GATT_PROXY"></a>

## 329.66 `CONFIG_BT_MESH_SHELL_GATT_PROXY`

**提示（Prompt）**：GATT 代理 Shell 命令支持（GATT Proxy shell commands）

**说明（Help）**

启用 GATT 代理（GATT Proxy）的 Shell 命令支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_MESH_GATT_PROXY || CONFIG_BT_MESH_PROXY_CLIENT) && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_GATT_PROXY`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_GATT_PROXY)、[`CONFIG_BT_MESH_PROXY_CLIENT`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_PROXY_CLIENT)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_HEALTH_CLI"></a>

## 329.67 `CONFIG_BT_MESH_SHELL_HEALTH_CLI`

**提示（Prompt）**：健康客户端 Shell 命令支持（Health Client shell commands）

**说明（Help）**

启用健康客户端（Health Client）的 Shell 命令支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_HEALTH_CLI && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_HEALTH_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_HEALTH_CLI)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_HEALTH_SRV_INSTANCE"></a>

## 329.68 `CONFIG_BT_MESH_SHELL_HEALTH_SRV_INSTANCE`

**提示（Prompt）**：Shell 健康服务器实例支持（shell Health Server instance）

**说明（Help）**

在蓝牙 Mesh Shell 模块中启用健康服务器模型实例（Health Server model instance）及故障控制 Shell 命令。要使用该实例，将 `bt_mesh_shell_health_srv` 添加到设备组成数据（composition data）；使用 `BT_MESH_SHELL_HEALTH_PUB_DEFINE` 实例化发布上下文（publication context）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_SHELL_TEST && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell） → 测试 Shell 命令支持（test shell commands）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_SHELL_TEST`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL_TEST)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_LARGE_COMP_DATA_CLI"></a>

## 329.69 `CONFIG_BT_MESH_SHELL_LARGE_COMP_DATA_CLI`

**提示（Prompt）**：大型组成数据客户端 Shell 命令支持（Large Composition Data Client shell commands）

**说明（Help）**

大型组成数据客户端（Large Composition Data Client）的 Shell 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LARGE_COMP_DATA_CLI && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LARGE_COMP_DATA_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LARGE_COMP_DATA_CLI)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_LOW_POWER"></a>

## 329.70 `CONFIG_BT_MESH_SHELL_LOW_POWER`

**提示（Prompt）**：低功耗节点 Shell 命令支持（Low Power node shell commands）

**说明（Help）**

启用低功耗节点（Low Power node）的 Shell 命令支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LOW_POWER && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LOW_POWER)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_OP_AGG_CLI"></a>

## 329.71 `CONFIG_BT_MESH_SHELL_OP_AGG_CLI`

**提示（Prompt）**：操作码聚合器客户端 Shell 命令支持（Opcodes Aggregator Client shell commands）

**说明（Help）**

操作码聚合器客户端（Opcodes Aggregator Client）的 Shell 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_OP_AGG_CLI && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_OP_AGG_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_OP_AGG_CLI)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_PRIV_BEACON_CLI"></a>

## 329.72 `CONFIG_BT_MESH_SHELL_PRIV_BEACON_CLI`

**提示（Prompt）**：私有信标客户端 Shell 命令支持（Private Beacons Client shell commands）

**说明（Help）**

私有信标客户端（Private Beacons Client）的 Shell 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PRIV_BEACON_CLI && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PRIV_BEACON_CLI`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_PRIV_BEACON_CLI)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_PROV"></a>

## 329.73 `CONFIG_BT_MESH_SHELL_PROV`

**提示（Prompt）**：配网 Shell 命令支持（provisioning shell commands）

**说明（Help）**

启用配网（provisioning）Shell 命令支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PROV && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROV)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MESH_PROV`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_PROV_CTX_INSTANCE"></a>

## 329.74 `CONFIG_BT_MESH_SHELL_PROV_CTX_INSTANCE`

**提示（Prompt）**：Shell 配网上下文实例支持（shell provisioning context instance）

**说明（Help）**

在蓝牙 Mesh Shell 模块中启用配网上下文实例（provisioning context instance），以及若干配网命令和目标实用功能（target utility features）。要使用该实例，在 Mesh 初始化时使用 `bt_mesh_shell_prov`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_SHELL_PROV && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell） → 配网 Shell 命令支持（provisioning shell commands）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_SHELL_PROV`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL_PROV)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_RPR_CLI"></a>

## 329.75 `CONFIG_BT_MESH_SHELL_RPR_CLI`

**提示（Prompt）**：远程配网客户端 Shell 命令支持（Remote Provisioning Client shell commands）

**说明（Help）**

远程配网客户端（Remote Provisioning Client）的 Shell 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_RPR_CLI && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L147)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RPR_CLI`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RPR_CLI)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_SAR_CFG_CLI"></a>

## 329.76 `CONFIG_BT_MESH_SHELL_SAR_CFG_CLI`

**提示（Prompt）**：SAR 配置客户端 Shell 命令支持（SAR Configuration Client shell commands）

**说明（Help）**

分段与重组配置客户端（SAR Configuration Client）的 Shell 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_SAR_CFG_CLI && CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_SAR_CFG_CLI`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SAR_CFG_CLI)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SHELL_TEST"></a>

## 329.77 `CONFIG_BT_MESH_SHELL_TEST`

**提示（Prompt）**：测试 Shell 命令支持（test shell commands）

**说明（Help）**

启用 Mesh 测试 Shell 命令（test mesh shell commands）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_SHELL && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/shell/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/shell/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 蓝牙 Mesh Shell（Bluetooth Mesh shell）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SOL_ADV_XMIT"></a>

## 329.78 `CONFIG_BT_MESH_SOL_ADV_XMIT`

**提示（Prompt）**：Solicitation PDU 重传次数（Solicitation PDU retransmission count）

**说明（Help）**

请求 PDU（Solicitation PDU）广播的重复次数。`0` 表示只发送一次，不重传。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PROXY_SOLICITATION && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1508`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1508)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 代理（Proxy） → 代理请求功能（Proxy solicitation feature）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROXY_SOLICITATION`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_PROXY_SOLICITATION)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SOL_PDU_RPL_CLI"></a>

## 329.79 `CONFIG_BT_MESH_SOL_PDU_RPL_CLI`

**提示（Prompt）**：Solicitation PDU RPL 配置客户端模型支持（Solicitation PDU RPL Configuration Client model）

**说明（Help）**

请求 PDU 重放保护列表配置客户端（Solicitation PDU RPL Configuration Client）用于从节点的请求重放保护列表（SRPL）中移除地址，该节点须支持相应的配置服务器模型（Solicitation PDU RPL Configuration Server model）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1381`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1381)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT"></a>

## 329.80 `CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT`

**提示（Prompt）**：Solicitation PDU 重放保护列表配置客户端模型超时，单位为毫秒（Solicitation PDU RPL Configuration Client）

**说明（Help）**

此超时控制请求 PDU 重放保护列表配置客户端（Solicitation PDU RPL Configuration Client）等待响应消息到达的时间，可在运行时通过 `bt_mesh_sol_pdu_rpl_cli_timeout_set` 更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_SOL_PDU_RPL_CLI && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1389`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1389)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → Solicitation PDU RPL 配置客户端模型支持（Solicitation PDU RPL Configuration Client model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_SOL_PDU_RPL_CLI`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SOL_PDU_RPL_CLI)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_STATISTIC"></a>

## 329.81 `CONFIG_BT_MESH_STATISTIC`

**提示（Prompt）**：Mesh 通信统计（Mesh communication statistics）[实验性，EXPERIMENTAL]

**说明（Help）**

此模块统计接收、中继和发送的帧（frames），帮助评估通信质量及已配置广播者实例（advertiser instances）数量是否充足。启用低功耗节点（LPN）功能时，模块还会在每个轮询周期对协议事件加时间戳，测量 LPN 友谊时序参数 `ReceiveDelay` 和 `ReceiveWindow`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1973`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1973)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_STORE_TIMEOUT"></a>

## 329.82 `CONFIG_BT_MESH_STORE_TIMEOUT`

**提示（Prompt）**：执行持久化存储前的延迟，单位为秒（Delay before storing persistently）

**说明（Help）**

定义发生更改后，待保存的变更实际写入持久存储（persistent storage，例如 Flash）之前的延迟，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 1000000]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1869`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1869)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 持久化存储（Persistent storage）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_SUBNET_COUNT"></a>

## 329.83 `CONFIG_BT_MESH_SUBNET_COUNT`

**提示（Prompt）**：每个网络的 Mesh 子网最大数量（Maximum mesh subnets per network）

**说明（Help）**

指定一个 Mesh 网络可同时参与的子网（subnets）数量。

译注：原文主语写为 Mesh network；此处保留该表述。

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

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1817`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1817)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 能力（Capabilities）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_TX_BLOB_CHUNK_SEND_INTERVAL"></a>

## 329.84 `CONFIG_BT_MESH_TX_BLOB_CHUNK_SEND_INTERVAL`

**提示（Prompt）**：BLOB 客户端分片发送间隔（BLOB Client chunk send interval）

**说明（Help）**

设置 BLOB 传输期间发送分片（chunks）的间隔，单位为毫秒。

注意：如果各分片之间没有发送延迟，BLOB 传输可能使网络过于繁忙，导致其他通信无法成功。

注意：设置此间隔时应考虑超时基数（timeout base）等时序限制，必要时相应调整；否则间隔可能相对超时设置过大，造成超时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_BLOB_CLI && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 2147483647]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1029`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1029)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → BLOB 传输客户端模型支持（BLOB Transfer Client model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BLOB_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_CLI)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_TX_BLOB_CHUNK_SIZE"></a>

## 329.85 `CONFIG_BT_MESH_TX_BLOB_CHUNK_SIZE`

**提示（Prompt）**：BLOB 客户端分片大小（BLOB Client chunk size）

**说明（Help）**

设置 BLOB 客户端的分片大小（chunk size）。实际最大分片大小取决于可支持的分段（segments）数量；如果设置值过大，会被限制到实际可用的最大值。另请参阅 `BT_MESH_TX_SEG_MAX` 以及节点能够接收的最大 SDU。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_BT_MESH_ALIGN_CHUNK_SIZE_TO_MAX_SEGMENT && CONFIG_BT_MESH_BLOB_CLI && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 377]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1017`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1017)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → BLOB 传输客户端模型支持（BLOB Transfer Client model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ALIGN_CHUNK_SIZE_TO_MAX_SEGMENT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ALIGN_CHUNK_SIZE_TO_MAX_SEGMENT)、[`CONFIG_BT_MESH_BLOB_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_CLI)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_TX_SEG_MAX"></a>

## 329.86 `CONFIG_BT_MESH_TX_SEG_MAX`

**提示（Prompt）**：出站消息的最大分段数（Maximum segments in outgoing messages）

**说明（Help）**

出站消息支持的最大分段（segments）数量。通常应根据本地节点支持的模型微调，即根据节点必须能够发送的最大消息有效载荷决定。此值影响内存消耗，因此默认值低于规范允许的最大值 `32` 段。

最大出站 SDU 大小等于该数量的 `12` 倍，其中 `4` 或 `8` 字节用于传输层消息完整性校验值（Transport Layer MIC）。例如，`5` 段对应最大 `60` 字节 SDU；使用 4 字节 MIC 时留给应用层数据 `56` 字节，使用 8 字节 MIC 时留出 `52` 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_TX_SEG_MSG_COUNT > 0 && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
6 if CONFIG_BT_MESH_BLOB_SRV || CONFIG_BT_MESH_BLOB_CLI || CONFIG_BT_MESH_RPR_SRV || CONFIG_BT_MESH_RPR_CLI
3
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:594`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L594)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_TX_SEG_MSG_COUNT`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_TX_SEG_MSG_COUNT)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_BLOB_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_SRV)、[`CONFIG_BT_MESH_BLOB_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_CLI)、[`CONFIG_BT_MESH_RPR_SRV`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RPR_SRV)、[`CONFIG_BT_MESH_RPR_CLI`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_RPR_CLI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_TX_SEG_MSG_COUNT"></a>

## 329.87 `CONFIG_BT_MESH_TX_SEG_MSG_COUNT`

**提示（Prompt）**：最大同时出站分段消息数量（simultaneous outgoing segmented messages）

**说明（Help）**

最大同时出站多段消息和／或可靠消息（multi-segment and/or reliable messages）数量。注意：Mesh 分段与重组（Segmentation/reassembly）是规范要求的必备功能；设为零会使设备无法发送任何 Mesh 分段消息。

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
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:531`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L531)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 传输层分段与重组配置（Transport SAR configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_UNPROV_BEACON_INT"></a>

## 329.88 `CONFIG_BT_MESH_UNPROV_BEACON_INT`

**提示（Prompt）**：未配网信标发送间隔，单位为秒（interval to send the unprovisioned beacon）

**说明（Help）**

指定设备发送未配网信标（unprovisioned beacon）的间隔，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 10]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:249`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L249)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning） → 广播承载配网支持（PB-ADV support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_WORKQ_CONTEXT"></a>

## 329.89 `CONFIG_BT_MESH_WORKQ_CONTEXT`

**提示（Prompt）**：广播线程选择（Advertising thread selection）

**说明（Help）**

定义发送 Mesh 消息的上下文（context）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_ADV_EXT && <choice CONFIG_BT_MESH_ADV>
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_WORKQ_MESH
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_WORKQ_MESH
CONFIG_BT_MESH_WORKQ_SYS
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser） → 广播者模式（Advertiser mode） → 扩展广播（Extended advertising）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ADV_EXT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV_EXT)、[`CONFIG_BT_MESH_ADV`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV)、[`CONFIG_BT_MESH_WORKQ_MESH`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_WORKQ_MESH)、[`CONFIG_BT_MESH_WORKQ_SYS`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_WORKQ_SYS)。

<a id="CONFIG_BT_MESH_WORKQ_MESH"></a>

## 329.90 `CONFIG_BT_MESH_WORKQ_MESH`

**提示（Prompt）**：Mesh 专用工作队列（Mesh-specific workqueue）

**说明（Help）**

选择后，Mesh 从专用工作队列（mesh-specific workqueue）发送消息，以确保消息始终能够发送。应用需确保该工作队列大小足够，建议最小值参阅 `BT_MESH_ADV_STACK_SIZE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_WORKQ_CONTEXT>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser） → 广播者模式（Advertiser mode） → 扩展广播（Extended advertising） → 广播线程选择（Advertising thread selection）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_WORKQ_CONTEXT`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_WORKQ_CONTEXT)。

<a id="CONFIG_BT_MESH_WORKQ_SYS"></a>

## 329.91 `CONFIG_BT_MESH_WORKQ_SYS`

**提示（Prompt）**：系统工作队列（System workqueue）

**说明（Help）**

选择后，Mesh 从系统工作队列（system work queue）发送消息。应用需确保系统工作队列栈大小 `SYSTEM_WORKQUEUE_STACK_SIZE` 足够，建议最小值参阅 `BT_MESH_ADV_STACK_SIZE`。

启用后，如果 Mesh 尝试发送消息，而主机耗尽了由 `CONFIG_BT_BUF_CMD_TX_COUNT` 控制的 HCI 命令缓冲区，系统工作队列会阻塞，直到有命令缓冲区释放。这可能形成死锁（deadlock）：主机无法使用系统工作队列释放 Mesh 正在等待的缓冲区。为缓解此问题，应确保 HCI 命令缓冲区数量充足。

此外，Mesh 消息的发送延迟还会受系统工作队列上其他使用者影响，降低 Mesh 消息发送的可靠性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_WORKQ_CONTEXT>
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser） → 广播者模式（Advertiser mode） → 扩展广播（Extended advertising） → 广播线程选择（Advertising thread selection）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_WORKQ_CONTEXT`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_WORKQ_CONTEXT)。

<a id="CONFIG_BT_MICP_MIC_CTLR"></a>

## 329.92 `CONFIG_BT_MICP_MIC_CTLR`

**提示（Prompt）**：麦克风控制配置文件麦克风控制器支持（Microphone Control Profile Microphone Controller）

**说明（Help）**

启用麦克风控制配置文件（Microphone Control Profile）的麦克风控制器角色（Microphone Controller role）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_CLIENT && CONFIG_BT_GATT_AUTO_DISCOVER_CCC && CONFIG_BT_BONDABLE && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.micp:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.micp#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_CLIENT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_GATT_AUTO_DISCOVER_CCC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_AUTO_DISCOVER_CCC)、[`CONFIG_BT_BONDABLE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BONDABLE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MICP_MIC_CTLR_AICS"></a>

## 329.93 `CONFIG_BT_MICP_MIC_CTLR_AICS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项便于检查是否为麦克风控制配置文件（MICP）客户端启用了音频输入控制服务（AICS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MICP_MIC_CTLR && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_MICP_MIC_CTLR_MAX_AICS_INST > 0
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.micp:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.micp#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 麦克风控制配置文件麦克风控制器支持（Microphone Control Profile Microphone Controller）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_CTLR`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MICP_MIC_CTLR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MICP_MIC_CTLR_MAX_AICS_INST`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MICP_MIC_CTLR_MAX_AICS_INST)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MICP_MIC_CTLR_MAX_AICS_INST"></a>

## 329.94 `CONFIG_BT_MICP_MIC_CTLR_MAX_AICS_INST`

**提示（Prompt）**：可设置的音频输入控制服务最大实例数（Audio Input Control Service instances）

**说明（Help）**

设置可配置并使用的音频输入控制服务（Audio Input Control Service，AICS）最大实例数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MICP_MIC_CTLR && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, CONFIG_BT_AICS_CLIENT_MAX_INSTANCE_COUNT]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.micp:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.micp#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 麦克风控制配置文件麦克风控制器支持（Microphone Control Profile Microphone Controller）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_CTLR`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MICP_MIC_CTLR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AICS_CLIENT_MAX_INSTANCE_COUNT`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AICS_CLIENT_MAX_INSTANCE_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MICP_MIC_DEV"></a>

## 329.95 `CONFIG_BT_MICP_MIC_DEV`

**提示（Prompt）**：麦克风控制配置文件麦克风设备支持（Microphone Control Profile Microphone Device）

**说明（Help）**

启用麦克风控制配置文件（Microphone Control Profile）的麦克风设备（Microphone Device）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_DYNAMIC_DB && CONFIG_BT_BONDABLE && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.micp:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.micp#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_DYNAMIC_DB`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_DYNAMIC_DB)、[`CONFIG_BT_BONDABLE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BONDABLE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MICP_MIC_DEV_AICS"></a>

## 329.96 `CONFIG_BT_MICP_MIC_DEV_AICS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项便于检查是否为麦克风控制配置文件的麦克风设备（Microphone Control Profile Microphone Device）启用了 AICS。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MICP_MIC_DEV && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_MICP_MIC_DEV_AICS_INSTANCE_COUNT > 0
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.micp:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.micp#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 麦克风控制配置文件麦克风设备支持（Microphone Control Profile Microphone Device）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_DEV`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MICP_MIC_DEV)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MICP_MIC_DEV_AICS_INSTANCE_COUNT`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MICP_MIC_DEV_AICS_INSTANCE_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MICP_MIC_DEV_AICS_INSTANCE_COUNT"></a>

## 329.97 `CONFIG_BT_MICP_MIC_DEV_AICS_INSTANCE_COUNT`

**提示（Prompt）**：麦克风控制服务麦克风设备的音频输入控制服务实例数（Audio Input Control Service instance count）

**说明（Help）**

设置麦克风控制配置文件的麦克风设备（Microphone Control Profile Microphone Device）所使用的音频输入控制服务（Audio Input Control Services）实例数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MICP_MIC_DEV && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, CONFIG_BT_AICS_MAX_INSTANCE_COUNT]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.micp:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.micp#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 麦克风控制配置文件麦克风设备支持（Microphone Control Profile Microphone Device）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_DEV`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MICP_MIC_DEV)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AICS_MAX_INSTANCE_COUNT`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AICS_MAX_INSTANCE_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MPL"></a>

## 329.98 `CONFIG_BT_MPL`

**提示（Prompt）**：媒体播放器支持（Support for media player）

**说明（Help）**

启用媒体播放器（media player）支持。注意：提供的媒体播放器只是示例，只有模拟实现（mock-up），不会实际播放任何媒体。若要真正播放媒体，必须扩展示例、将其连接到真实媒体播放器，或替换为真实媒体播放器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mpl:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mpl#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MPL_GROUP_TITLE_MAX"></a>

## 329.99 `CONFIG_BT_MPL_GROUP_TITLE_MAX`

**提示（Prompt）**：曲目组标题最大长度（Max length of title of a group of tracks）

**说明（Help）**

设置媒体播放器中任意曲目组标题（group title）的最大字节数，包括空终止符（null termination）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MPL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MPL_TRACK_TITLE_MAX
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mpl:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mpl#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器支持（Support for media player）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MPL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MPL_TRACK_TITLE_MAX`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_MPL_TRACK_TITLE_MAX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MPL_ICON_BITMAP_SIZE"></a>

## 329.100 `CONFIG_BT_MPL_ICON_BITMAP_SIZE`

**提示（Prompt）**：媒体播放器图标位图对象大小（Media player Icon bitmap object size）

**说明（Help）**

设置图标对象（icon object）的最大大小，单位为八位字节（octets）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MPL_OBJECTS && CONFIG_BT_MPL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
127
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mpl:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mpl#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器支持（Support for media player） → 媒体播放器对象支持（Support for media player objects）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL_OBJECTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_MPL_OBJECTS)、[`CONFIG_BT_MPL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MPL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<!-- kconfig-navigation -->

[上一章](P328_subsys_bluetooth_配置项参考_9.md) · [返回大纲](大纲.md) · [下一章](P330_subsys_bluetooth_配置项参考_11.md)
