---
id: learning.zephyr-docs.kconfig-reference.page-386
title: "`subsys/mgmt`配置项参考（3/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第386章\_`subsys/mgmt`配置项参考（3/4）

本章翻译官方 Kconfig 数据库中 `subsys/mgmt` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVELS"></a>

## 386.1 `CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVELS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

zcbor 解码 SMP 响应必须支持的最小映射／列表嵌套层数，由 `MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_?` 选项自动生成。基础映射已计入；若某命令或组在基础映射上增加其他映射或列表，应选择相应的 `MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_?` 选项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
7 if CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_7
6 if CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_6
5 if CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_5
4 if CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_4
3 if CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3
2 if CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2
1 if CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_1
0
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/smp/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/smp/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_7)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_6)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_5)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_4)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_7`、`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_6`、`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_5`、`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_4`、`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3`、`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`、`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_1`。

<a id="CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVELS"></a>

## 386.2 `CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVELS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

zcbor 编码 SMP 响应必须支持的最小映射／列表嵌套层数，由 `MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_?` 选项自动生成。基础映射已计入；若某命令或组在基础映射上增加其他映射或列表，应选择相应的 `MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_?` 选项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
7 if CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_7
6 if CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_6
5 if CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_5
4 if CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_4
3 if CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3
2 if CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2
1 if CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_1 || CONFIG_ZCBOR_CANONICAL
0
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/smp/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/smp/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_7)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_6)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_5)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_4)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_1)、[`CONFIG_ZCBOR_CANONICAL`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR_CANONICAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_7`、`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_6`、`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_5`、`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_4`、`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3`、`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2`、`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_1`。

<a id="CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS"></a>

## 386.3 `CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS`

**提示（Prompt）**：SMP 命令状态钩子（command status hooks）

**说明（Help）**

启用 SMP 命令状态通知钩子，在收到或处理 SMP 消息时触发。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/smp/Kconfig:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/smp/Kconfig#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_SMP_LEGACY_RC_BEHAVIOUR"></a>

## 386.4 `CONFIG_MCUMGR_SMP_LEGACY_RC_BEHAVIOUR`

**提示（Prompt）**：旧版 rc 结果码响应行为（Legacy result code）

**说明（Help）**

恢复旧版结果码响应行为：状态为 `0` 时，响应中仍包含 `rc`。禁用后采用新行为，仅在结果码非零，即发生错误时返回 `rc`。若命令只返回结果码，则成功时的新行为产生空响应，而旧行为的响应仍有 `rc` 字段。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_SMP_SUPPORT_ORIGINAL_PROTOCOL && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 支持原始协议（original protocol）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_SMP_SUPPORT_ORIGINAL_PROTOCOL`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_SMP_SUPPORT_ORIGINAL_PROTOCOL)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_SMP_SUPPORT_ORIGINAL_PROTOCOL"></a>

## 386.5 `CONFIG_MCUMGR_SMP_SUPPORT_ORIGINAL_PROTOCOL`

**提示（Prompt）**：支持原始协议（original protocol）

**说明（Help）**

同时支持原始 SMP 协议和新协议：原始协议将所有错误放入 `rc` 字段，新协议为命令错误／结果码提供专门条目。客户端发送的请求头（request header）指明所选协议。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/smp/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/smp/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_SMP_VERBOSE_ERR_RESPONSE"></a>

## 386.6 `CONFIG_MCUMGR_SMP_VERBOSE_ERR_RESPONSE`

**提示（Prompt）**：支持详细错误响应（verbose error response）

**说明（Help）**

允许以 `rsn` 文本字符串形式编码 `rc` 的解释。返回 `MGMT_ERR_EUNKNOWN` 时，可借此补充错误来源信息。`rsn` 是 `rc` 之外的额外字符串，因此 `MCUMGR_TRANSPORT_NETBUF_SIZE` 必须足够大，能够同时编码两者。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_SMP_SUPPORT_ORIGINAL_PROTOCOL && CONFIG_MCUMGR
```

**被选择（Selected by）**

```text
CONFIG_MCUMGR_GRP_IMG_VERBOSE_ERR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/smp/Kconfig:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/smp/Kconfig#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 支持原始协议（original protocol）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_SMP_SUPPORT_ORIGINAL_PROTOCOL`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_SMP_SUPPORT_ORIGINAL_PROTOCOL)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_IMG_VERBOSE_ERR`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG_VERBOSE_ERR)。

<a id="CONFIG_MCUMGR_TRANSPORT_BT"></a>

## 386.7 `CONFIG_MCUMGR_TRANSPORT_BT`

**提示（Prompt）**：蓝牙 MCUmgr 简单管理协议传输（Bluetooth SMP transport）

**说明（Help）**

处理通过蓝牙（Bluetooth）收到的简单管理协议（SMP）命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PERIPHERAL && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.bluetooth:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.bluetooth#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_BT_CLIENT"></a>

## 386.8 `CONFIG_MCUMGR_TRANSPORT_BT_CLIENT`

**提示（Prompt）**：蓝牙 MCUmgr SMP 客户端传输（client transport）

**说明（Help）**

允许连接远程蓝牙 MCUmgr 服务器并向其发出命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CENTRAL && CONFIG_BT_GATT_CLIENT && CONFIG_MCUMGR_GRP_TRANSPORT && CONFIG_MCUMGR_TRANSPORT_BT && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.bluetooth:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.bluetooth#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 蓝牙 MCUmgr 简单管理协议传输（Bluetooth SMP transport）

**配置项引用（Symbol References）**：[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BT_GATT_CLIENT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CLIENT)、[`CONFIG_MCUMGR_GRP_TRANSPORT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_TRANSPORT)、[`CONFIG_MCUMGR_TRANSPORT_BT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL"></a>

## 386.9 `CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL`

**提示（Prompt）**：为 SMP 数据包交换请求特定连接参数

**说明（Help）**

处理 SMP 命令时，允许请求特定连接参数（connection parameters），以加快命令交换。若将 SMP 用于设备固件更新（DFU），建议启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SYSTEM_WORKQUEUE_PRIORITY < 0 && CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS && CONFIG_MCUMGR_TRANSPORT_BT && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.bluetooth:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.bluetooth#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 蓝牙 MCUmgr 简单管理协议传输（Bluetooth SMP transport）

**配置项引用（Symbol References）**：[`CONFIG_SYSTEM_WORKQUEUE_PRIORITY`](P002_kernel_配置项参考_2.md#CONFIG_SYSTEM_WORKQUEUE_PRIORITY)、[`CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS)、[`CONFIG_MCUMGR_TRANSPORT_BT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL_LATENCY"></a>

## 386.10 `CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL_LATENCY`

**提示（Prompt）**：SMP 数据包交换的外设延迟（Peripheral latency）

**说明（Help）**

SMP 数据包交换期间使用的外设延迟，以连接间隔（Connection Intervals）为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL && CONFIG_MCUMGR_TRANSPORT_BT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 499]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.bluetooth:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.bluetooth#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 蓝牙 MCUmgr 简单管理协议传输（Bluetooth SMP transport） → 为 SMP 数据包交换请求特定连接参数

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL)、[`CONFIG_MCUMGR_TRANSPORT_BT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL_MAX_INT"></a>

## 386.11 `CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL_MAX_INT`

**提示（Prompt）**：SMP 数据包交换的最大连接间隔

**说明（Help）**

SMP 数据包交换期间使用的最大连接间隔（connection interval），单位为 1.25 毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL && CONFIG_MCUMGR_TRANSPORT_BT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
9
```

**取值范围（Ranges）**

```text
[CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL_MIN_INT, 3200]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.bluetooth:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.bluetooth#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 蓝牙 MCUmgr 简单管理协议传输（Bluetooth SMP transport） → 为 SMP 数据包交换请求特定连接参数

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL)、[`CONFIG_MCUMGR_TRANSPORT_BT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL_MIN_INT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL_MIN_INT)。

<a id="CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL_MIN_INT"></a>

## 386.12 `CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL_MIN_INT`

**提示（Prompt）**：SMP 数据包交换的最小连接间隔

**说明（Help）**

SMP 数据包交换期间使用的最小连接间隔（connection interval），单位为 1.25 毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL && CONFIG_MCUMGR_TRANSPORT_BT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
6
```

**取值范围（Ranges）**

```text
[6, 3200]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.bluetooth:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.bluetooth#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 蓝牙 MCUmgr 简单管理协议传输（Bluetooth SMP transport） → 为 SMP 数据包交换请求特定连接参数

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL)、[`CONFIG_MCUMGR_TRANSPORT_BT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL_RESTORE_TIME"></a>

## 386.13 `CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL_RESTORE_TIME`

**提示（Prompt）**：连接参数恢复时间（毫秒）

**说明（Help）**

SMP 特征（characteristic）无活动达到此时间后，将连接参数恢复为外设首选值 `BT_GAP_PERIPHERAL_PREF_PARAMS`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL && CONFIG_MCUMGR_TRANSPORT_BT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
5000
```

**取值范围（Ranges）**

```text
[1000, 65535]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.bluetooth:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.bluetooth#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 蓝牙 MCUmgr 简单管理协议传输（Bluetooth SMP transport） → 为 SMP 数据包交换请求特定连接参数

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL)、[`CONFIG_MCUMGR_TRANSPORT_BT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL_RETRY_TIME"></a>

## 386.14 `CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL_RETRY_TIME`

**提示（Prompt）**：连接参数更新重试时间（毫秒）

**说明（Help）**

连接参数更新因错误失败时，此项指定下一次更新尝试的时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL && CONFIG_MCUMGR_TRANSPORT_BT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
1000
```

**取值范围（Ranges）**

```text
[1, 5000]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.bluetooth:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.bluetooth#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 蓝牙 MCUmgr 简单管理协议传输（Bluetooth SMP transport） → 为 SMP 数据包交换请求特定连接参数

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL)、[`CONFIG_MCUMGR_TRANSPORT_BT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL_TIMEOUT"></a>

## 386.15 `CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL_TIMEOUT`

**提示（Prompt）**：SMP 数据包交换的监督超时（Supervision timeout）

**说明（Help）**

SMP 数据包交换期间使用的监督超时（supervision timeout），单位为 10 毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL && CONFIG_MCUMGR_TRANSPORT_BT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
42
```

**取值范围（Ranges）**

```text
[10, 3200]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.bluetooth:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.bluetooth#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 蓝牙 MCUmgr 简单管理协议传输（Bluetooth SMP transport） → 为 SMP 数据包交换请求特定连接参数

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT_CONN_PARAM_CONTROL)、[`CONFIG_MCUMGR_TRANSPORT_BT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_BT_DYNAMIC_SVC_REGISTRATION"></a>

## 386.16 `CONFIG_MCUMGR_TRANSPORT_BT_DYNAMIC_SVC_REGISTRATION`

**提示（Prompt）**：运行时注册 SMP 服务（Register at runtime）

**说明（Help）**

启用后，SMP 服务在启动时自动注册，随后可通过专用 API 动态注册／注销。否则，服务静态定义并注册。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_DYNAMIC_DB && CONFIG_MCUMGR_TRANSPORT_BT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.bluetooth:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.bluetooth#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 蓝牙 MCUmgr 简单管理协议传输（Bluetooth SMP transport）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_DYNAMIC_DB`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_DYNAMIC_DB)、[`CONFIG_MCUMGR_TRANSPORT_BT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_BT_PERM"></a>

## 386.17 `CONFIG_MCUMGR_TRANSPORT_BT_PERM`

**提示（Prompt）**：SMP 服务使用的权限（Permission）

**说明（Help）**

SMP 服务的通用属性配置文件（GATT）特征权限设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_BT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW_AUTHEN if CONFIG_BT_SMP
CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW
CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW_ENCRYPT
CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW_AUTHEN
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.bluetooth:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.bluetooth#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 蓝牙 MCUmgr 简单管理协议传输（Bluetooth SMP transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_BT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW_AUTHEN`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW_AUTHEN)、[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW)、[`CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW_ENCRYPT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW_ENCRYPT)。

<a id="CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW"></a>

## 386.18 `CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW`

**提示（Prompt）**：允许读写（Read and write allowed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_BT_PERM>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.bluetooth:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.bluetooth#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 蓝牙 MCUmgr 简单管理协议传输（Bluetooth SMP transport） → SMP 服务使用的权限（Permission）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_BT_PERM`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT_PERM)。

<a id="CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW_AUTHEN"></a>

## 386.19 `CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW_AUTHEN`

**提示（Prompt）**：访问需要加密与身份认证（Require encryption and authentication for access）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && <choice CONFIG_MCUMGR_TRANSPORT_BT_PERM>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.bluetooth:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.bluetooth#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 蓝牙 MCUmgr 简单管理协议传输（Bluetooth SMP transport） → SMP 服务使用的权限（Permission）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_MCUMGR_TRANSPORT_BT_PERM`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT_PERM)。

<a id="CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW_ENCRYPT"></a>

## 386.20 `CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW_ENCRYPT`

**提示（Prompt）**：访问需要加密（Require encryption for access）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && <choice CONFIG_MCUMGR_TRANSPORT_BT_PERM>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.bluetooth:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.bluetooth#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 蓝牙 MCUmgr 简单管理协议传输（Bluetooth SMP transport） → SMP 服务使用的权限（Permission）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_MCUMGR_TRANSPORT_BT_PERM`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT_PERM)。

<a id="CONFIG_MCUMGR_TRANSPORT_BT_REASSEMBLY"></a>

## 386.21 `CONFIG_MCUMGR_TRANSPORT_BT_REASSEMBLY`

**提示（Prompt）**：在蓝牙 SMP 传输中重组数据包（Reassemble packets）

**说明（Help）**

启用后，SMP 蓝牙（BT）传输先缓冲并重组收到的数据包分片（fragments），再交给后续处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_BT && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_TRANSPORT_REASSEMBLY
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.bluetooth:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.bluetooth#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 蓝牙 MCUmgr 简单管理协议传输（Bluetooth SMP transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_BT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_REASSEMBLY`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_REASSEMBLY)。

<a id="CONFIG_MCUMGR_TRANSPORT_DUMMY"></a>

## 386.22 `CONFIG_MCUMGR_TRANSPORT_DUMMY`

**提示（Prompt）**：虚拟 SMP 后端（Dummy backend）

**说明（Help）**

启用虚拟 SMP 后端，用于无需真实接口或驱动的 SMP 功能单元测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BASE64 && CONFIG_CRC && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.dummy:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.dummy#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_BASE64`](P197_lib_配置项参考_1.md#CONFIG_BASE64)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_DUMMY_RX_BUF_SIZE"></a>

## 386.23 `CONFIG_MCUMGR_TRANSPORT_DUMMY_RX_BUF_SIZE`

**提示（Prompt）**：虚拟接口 MCUmgr 分片接收缓冲区大小

**说明（Help）**

指定 MCUmgr 虚拟后端接收缓冲区大小，单位为字节。必须足够大，容纳 MCUmgr 客户端发送的任意一行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_DUMMY && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.dummy:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.dummy#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 虚拟 SMP 后端（Dummy backend）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_DUMMY`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_DUMMY)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN"></a>

## 386.24 `CONFIG_MCUMGR_TRANSPORT_LORAWAN`

**提示（Prompt）**：LoRaWAN MCUmgr 简单管理协议传输（SMP transport）

**说明（Help）**

处理通过 LoRaWAN 收到的 SMP 命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORAWAN && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.lorawan:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.lorawan#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN_CONFIRMED_UPLINKS"></a>

## 386.25 `CONFIG_MCUMGR_TRANSPORT_LORAWAN_CONFIRMED_UPLINKS`

**提示（Prompt）**：上行使用确认数据包（confirmed packets）

**说明（Help）**

启用后，用确认上行数据包（confirmed uplink packets）发送响应；否则使用不确认数据包（unconfirmed packets）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_LORAWAN && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.lorawan:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.lorawan#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → LoRaWAN MCUmgr 简单管理协议传输（SMP transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LORAWAN`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN_FRAGMENTED_UPLINKS"></a>

## 386.26 `CONFIG_MCUMGR_TRANSPORT_LORAWAN_FRAGMENTED_UPLINKS`

**提示（Prompt）**：分片上行消息（Fragment uplink messages）

**说明（Help）**

消息过大、无法装入单条上行消息时，将其拆为多条上行消息。禁用后，不发送过大的上行消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_LORAWAN && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.lorawan:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.lorawan#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → LoRaWAN MCUmgr 简单管理协议传输（SMP transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LORAWAN`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN_FRAME_PORT"></a>

## 386.27 `CONFIG_MCUMGR_TRANSPORT_LORAWAN_FRAME_PORT`

**提示（Prompt）**：LoRaWAN SMP 帧端口（frame port）

**说明（Help）**

用于 LoRaWAN 下行和上行通信的帧端口。此端口收到的所有消息均视为 SMP 数据包。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_LORAWAN && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 223]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.lorawan:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.lorawan#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → LoRaWAN MCUmgr 简单管理协议传输（SMP transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LORAWAN`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA"></a>

## 386.28 `CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA`

**提示（Prompt）**：收到部分数据包时发送空包（empty packet）

**说明（Help）**

收到服务器发来的部分分片消息后，发送空数据包，使下一数据包无需等待下一个发送窗口即可接收。注意：此功能需要专用线程，以免阻塞系统工作队列（system workqueue）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_LORAWAN_REASSEMBLY && CONFIG_MCUMGR_TRANSPORT_LORAWAN && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.lorawan:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.lorawan#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → LoRaWAN MCUmgr 简单管理协议传输（SMP transport） → 重组 LoRaWAN SMP 消息（Reassemble）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_REASSEMBLY`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_REASSEMBLY)、[`CONFIG_MCUMGR_TRANSPORT_LORAWAN`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA_RETRIES"></a>

## 386.29 `CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA_RETRIES`

**提示（Prompt）**：轮询线程重试次数（Poll thread retries）

**说明（Help）**

收到部分帧后，线程通过发送空包轮询以获取后续数据包。本项指定该线程发送 LoRaWAN 消息失败时的重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA && CONFIG_MCUMGR_TRANSPORT_LORAWAN && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.lorawan:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.lorawan#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → LoRaWAN MCUmgr 简单管理协议传输（SMP transport） → 重组 LoRaWAN SMP 消息（Reassemble） → 收到部分数据包时发送空包（empty packet）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA)、[`CONFIG_MCUMGR_TRANSPORT_LORAWAN`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA_STACK_SIZE"></a>

## 386.30 `CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA_STACK_SIZE`

**提示（Prompt）**：轮询线程栈大小（Poll thread stack size）

**说明（Help）**

收到部分帧后，通过空包轮询后续数据包的线程所用栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA && CONFIG_MCUMGR_TRANSPORT_LORAWAN && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
1800
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.lorawan:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.lorawan#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → LoRaWAN MCUmgr 简单管理协议传输（SMP transport） → 重组 LoRaWAN SMP 消息（Reassemble） → 收到部分数据包时发送空包（empty packet）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA)、[`CONFIG_MCUMGR_TRANSPORT_LORAWAN`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA_THREAD_PRIORITY"></a>

## 386.31 `CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA_THREAD_PRIORITY`

**提示（Prompt）**：轮询线程优先级（Poll thread priority）

**说明（Help）**

收到部分帧后，通过空包轮询后续数据包的线程所用优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA && CONFIG_MCUMGR_TRANSPORT_LORAWAN && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.lorawan:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.lorawan#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → LoRaWAN MCUmgr 简单管理协议传输（SMP transport） → 重组 LoRaWAN SMP 消息（Reassemble） → 收到部分数据包时发送空包（empty packet）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_POLL_FOR_DATA)、[`CONFIG_MCUMGR_TRANSPORT_LORAWAN`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN_REASSEMBLY"></a>

## 386.32 `CONFIG_MCUMGR_TRANSPORT_LORAWAN_REASSEMBLY`

**提示（Prompt）**：重组 LoRaWAN SMP 消息（Reassemble）

**说明（Help）**

将下行 LoRaWAN 消息重组，以接收超过单个消息大小的完整消息；否则仅支持大小不超过单个数据包的消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_LORAWAN && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_TRANSPORT_REASSEMBLY
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.lorawan:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.lorawan#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → LoRaWAN MCUmgr 简单管理协议传输（SMP transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LORAWAN`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_REASSEMBLY`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_REASSEMBLY)。

<a id="CONFIG_MCUMGR_TRANSPORT_NETBUF_AVAILABLE"></a>

## 386.33 `CONFIG_MCUMGR_TRANSPORT_NETBUF_AVAILABLE`

**提示（Prompt）**：查询可用 MCUmgr 缓冲区的功能

**说明（Help）**

启用后，可使用 `smp_packet_buffers_available` 查询空闲 MCUmgr 缓冲区数量。仅应用于调试或测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_BUF_POOL_USAGE && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF_POOL_USAGE`](P198_lib_配置项参考_2.md#CONFIG_NET_BUF_POOL_USAGE)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_NETBUF_COUNT"></a>

## 386.34 `CONFIG_MCUMGR_TRANSPORT_NETBUF_COUNT`

**提示（Prompt）**：MCUmgr 缓冲区数量（Number of buffers）

**说明（Help）**

为 MCUmgr 分配的 `net_buf` 数量，请求和响应都使用这些缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
2 if CONFIG_MCUMGR_TRANSPORT_UDP
4
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_UDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP)。

<a id="CONFIG_MCUMGR_TRANSPORT_NETBUF_MIN_USER_DATA_SIZE"></a>

## 386.35 `CONFIG_MCUMGR_TRANSPORT_NETBUF_MIN_USER_DATA_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于确定用户数据最小大小的隐藏选项（hidden option）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
24 if CONFIG_MCUMGR_TRANSPORT_UDP && CONFIG_NET_IPV6
20 if CONFIG_MCUMGR_TRANSPORT_UDP && CONFIG_MCUMGR_TRANSPORT_UDP_IPV4 && CONFIG_NET_SOCKETS_PACKET
8 if CONFIG_MCUMGR_TRANSPORT_UDP && CONFIG_MCUMGR_TRANSPORT_UDP_IPV4
8 if CONFIG_MCUMGR_TRANSPORT_BT
4
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_UDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_MCUMGR_TRANSPORT_UDP_IPV4`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP_IPV4)、[`CONFIG_NET_SOCKETS_PACKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_PACKET)、[`CONFIG_MCUMGR_TRANSPORT_BT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT)。

<a id="CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE"></a>

## 386.36 `CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE`

**提示（Prompt）**：每个 MCUmgr 缓冲区的大小

**说明（Help）**

每个 MCUmgr 缓冲区的大小，单位为字节。必须满足以下关系：

```text
MCUMGR_TRANSPORT_NETBUF_SIZE >= transport-specific-MTU + transport-overhead
```

即缓冲区至少容纳具体传输的最大传输单元（MTU）加上传输额外开销。启用 `MCUMGR_TRANSPORT_SHELL` 时，应至少设为 `CONFIG_SHELL_BACKEND_DUMMY_BUF_SIZE + 32`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
2048 if CONFIG_MCUMGR_TRANSPORT_UDP
384
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_UDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP)。

<a id="CONFIG_MCUMGR_TRANSPORT_NETBUF_USER_DATA_SIZE"></a>

## 386.37 `CONFIG_MCUMGR_TRANSPORT_NETBUF_USER_DATA_SIZE`

**提示（Prompt）**：MCUmgr 缓冲区用户数据大小（user data size）

**说明（Help）**

为每个 MCUmgr 缓冲区分配的用户数据大小，单位为字节。各传输方式要求不同：UART 和命令行（shell）使用 `4` 字节即可，蓝牙（Bluetooth）使用 `8` 字节即可。UDP 则必须足以保存 IPv4／IPv6 地址。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_TRANSPORT_NETBUF_MIN_USER_DATA_SIZE
```

**取值范围（Ranges）**

```text
[CONFIG_MCUMGR_TRANSPORT_NETBUF_MIN_USER_DATA_SIZE, 128]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_NETBUF_MIN_USER_DATA_SIZE`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_NETBUF_MIN_USER_DATA_SIZE)。

<a id="CONFIG_MCUMGR_TRANSPORT_RAW_DUMMY"></a>

## 386.38 `CONFIG_MCUMGR_TRANSPORT_RAW_DUMMY`

**提示（Prompt）**：虚拟原始 UART MCUmgr 后端，非控制台 SMP 格式

**说明（Help）**

启用虚拟 MCUmgr UART 后端，不使用控制台上的 SMP 格式（SMP over console），也不对数据进行 base64 编码。用于无需真实接口或驱动的 SMP 功能单元测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.raw_dummy:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.raw_dummy#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_RAW_DUMMY_BRIDGE_CONFIG_DETAILS"></a>

## 386.39 `CONFIG_MCUMGR_TRANSPORT_RAW_DUMMY_BRIDGE_CONFIG_DETAILS`

**提示（Prompt）**：模拟配置详情数据（Fake config details data）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_TRANSPORT_INFO_FUNCTIONS && CONFIG_MCUMGR_TRANSPORT_RAW_DUMMY && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.raw_dummy:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.raw_dummy#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 虚拟原始 UART MCUmgr 后端，非控制台 SMP 格式

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_TRANSPORT_INFO_FUNCTIONS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_TRANSPORT_INFO_FUNCTIONS)、[`CONFIG_MCUMGR_TRANSPORT_RAW_DUMMY`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_RAW_DUMMY)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_RAW_DUMMY_RX_BUF_SIZE"></a>

## 386.40 `CONFIG_MCUMGR_TRANSPORT_RAW_DUMMY_RX_BUF_SIZE`

**提示（Prompt）**：虚拟接口 MCUmgr 分片接收缓冲区大小

**说明（Help）**

指定原始 MCUmgr 虚拟后端接收缓冲区大小，单位为字节。必须足够大，容纳 MCUmgr 客户端发送的任意一行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_RAW_DUMMY && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.raw_dummy:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.raw_dummy#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 虚拟原始 UART MCUmgr 后端，非控制台 SMP 格式

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_RAW_DUMMY`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_RAW_DUMMY)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_RAW_UART"></a>

## 386.41 `CONFIG_MCUMGR_TRANSPORT_RAW_UART`

**提示（Prompt）**：原始 UART MCUmgr 传输，非控制台 SMP 格式

**说明（Help）**

处理通过 UART 收到、未采用控制台 SMP 格式（SMP over console）编码的 MCUmgr 命令，即不含附加字段或 base64 编码。比 `CONFIG_MCUMGR_TRANSPORT_UART` 更轻量，可通过二进制、非文本 UART 接收 MCUmgr 命令，无需额外线程。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CONSOLE && CONFIG_UART_MCUMGR && CONFIG_UART_MCUMGR_RAW_PROTOCOL && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_TRANSPORT_SERIAL_HAS_RAW_BINARY_NON_SMP_OVER_CONSOLE
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.raw_uart:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.raw_uart#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_UART_MCUMGR`](P066_drivers_console_配置项参考.md#CONFIG_UART_MCUMGR)、[`CONFIG_UART_MCUMGR_RAW_PROTOCOL`](P066_drivers_console_配置项参考.md#CONFIG_UART_MCUMGR_RAW_PROTOCOL)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_SERIAL_HAS_RAW_BINARY_NON_SMP_OVER_CONSOLE`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_SERIAL_HAS_RAW_BINARY_NON_SMP_OVER_CONSOLE)。

<a id="CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT"></a>

## 386.42 `CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT`

**提示（Prompt）**：输入过期（Input expiration）

**说明（Help）**

启用后，通过原始 UART 传输收到的不完整或错误 MCUmgr 命令，在指定时间后超时，防止因始终未收到预期的完整数据包而锁死 UART。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_RAW_UART && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.raw_uart:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.raw_uart#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 原始 UART MCUmgr 传输，非控制台 SMP 格式

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_RAW_UART`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_RAW_UART)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT_TIME_MS"></a>

## 386.43 `CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT_TIME_MS`

**提示（Prompt）**：输入过期超时（Input expiration timeout）

**说明（Help）**

UART 传输首次收到数据后，经过此时间便判定超时，并清空接收缓冲区以等待新命令，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT && CONFIG_MCUMGR_TRANSPORT_RAW_UART && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
3000
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.raw_uart:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.raw_uart#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 原始 UART MCUmgr 传输，非控制台 SMP 格式 → 输入过期（Input expiration）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT)、[`CONFIG_MCUMGR_TRANSPORT_RAW_UART`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_RAW_UART)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_REASSEMBLY"></a>

## 386.44 `CONFIG_MCUMGR_TRANSPORT_REASSEMBLY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 SMP 后端进行数据包重组（packet reassembly）所需的结构体和函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**被选择（Selected by）**

```text
CONFIG_MCUMGR_TRANSPORT_BT_REASSEMBLY
CONFIG_MCUMGR_TRANSPORT_LORAWAN_REASSEMBLY
CONFIG_MCUMGR_TRANSPORT_SPI
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_BT_REASSEMBLY`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_BT_REASSEMBLY)、[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_REASSEMBLY`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_REASSEMBLY)、[`CONFIG_MCUMGR_TRANSPORT_SPI`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_SPI)。

<a id="CONFIG_MCUMGR_TRANSPORT_SERIAL_HAS_RAW_BINARY_NON_SMP_OVER_CONSOLE"></a>

## 386.45 `CONFIG_MCUMGR_TRANSPORT_SERIAL_HAS_RAW_BINARY_NON_SMP_OVER_CONSOLE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由实现原始二进制串行传输、非控制台 SMP 格式的传输方式选择的隐藏 Kconfig 选项，使 `serial_util.c` 提供相应功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**被选择（Selected by）**

```text
CONFIG_MCUMGR_TRANSPORT_RAW_UART
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.common:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.common#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 公共传输配置（Common transport configuration）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_RAW_UART`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_RAW_UART)。

<a id="CONFIG_MCUMGR_TRANSPORT_SERIAL_HAS_SMP_OVER_CONSOLE"></a>

## 386.46 `CONFIG_MCUMGR_TRANSPORT_SERIAL_HAS_SMP_OVER_CONSOLE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由实现控制台 SMP 传输（SMP over console）的传输方式选择的隐藏 Kconfig 选项，使 `serial_util.c` 提供相应功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**被选择（Selected by）**

```text
CONFIG_MCUMGR_TRANSPORT_SHELL
CONFIG_MCUMGR_TRANSPORT_UART
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.common:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.common#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 公共传输配置（Common transport configuration）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_SHELL`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_SHELL)、[`CONFIG_MCUMGR_TRANSPORT_UART`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UART)。

<a id="CONFIG_MCUMGR_TRANSPORT_SHELL"></a>

## 386.47 `CONFIG_MCUMGR_TRANSPORT_SHELL`

**提示（Prompt）**：命令行 MCUmgr SMP 传输（Shell transport）

**说明（Help）**

处理通过命令行（shell）收到的 SMP 命令，使同一命令行同时用于 MCUmgr 命令和普通命令行命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_BASE64 && CONFIG_CRC && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_TRANSPORT_SERIAL_HAS_SMP_OVER_CONSOLE
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.shell:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.shell#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_BASE64`](P197_lib_配置项参考_1.md#CONFIG_BASE64)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_SERIAL_HAS_SMP_OVER_CONSOLE`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_SERIAL_HAS_SMP_OVER_CONSOLE)。

<a id="CONFIG_MCUMGR_TRANSPORT_SHELL_INPUT_TIMEOUT"></a>

## 386.48 `CONFIG_MCUMGR_TRANSPORT_SHELL_INPUT_TIMEOUT`

**提示（Prompt）**：命令行输入过期（Shell input expiration）

**说明（Help）**

启用后，通过命令行传输收到的不完整或错误 MCUmgr 命令，在指定时间后超时，防止因始终未收到头部指明的完整数据包而锁死命令行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_SHELL && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.shell:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.shell#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 命令行 MCUmgr SMP 传输（Shell transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_SHELL`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_SHELL)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_SHELL_INPUT_TIMEOUT_TIME"></a>

## 386.49 `CONFIG_MCUMGR_TRANSPORT_SHELL_INPUT_TIMEOUT_TIME`

**提示（Prompt）**：命令行输入过期超时（Shell input expiration timeout）

**说明（Help）**

串行传输收到有效 MCUmgr 头部后，经过此时间便判定超时，并恢复命令行正常运行，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_SHELL_INPUT_TIMEOUT && CONFIG_MCUMGR_TRANSPORT_SHELL && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
3000
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.shell:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.shell#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 命令行 MCUmgr SMP 传输（Shell transport） → 命令行输入过期（Shell input expiration）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_SHELL_INPUT_TIMEOUT`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_SHELL_INPUT_TIMEOUT)、[`CONFIG_MCUMGR_TRANSPORT_SHELL`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_SHELL)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_SHELL_MTU"></a>

## 386.50 `CONFIG_MCUMGR_TRANSPORT_SHELL_MTU`

**提示（Prompt）**：命令行 SMP 最大传输单元（MTU）【已弃用 DEPRECATED】

**说明（Help）**

命令行传输 `get_mtu` 回调返回的值。SMP 层不使用该回调，因此此选项与回调一起弃用。控制台 SMP 帧（SMP over console frames）限制为 127 字节，最大 SMP 数据包大小由 `MCUMGR_TRANSPORT_NETBUF_SIZE` 设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_SHELL && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.shell:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.shell#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 命令行 MCUmgr SMP 传输（Shell transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_SHELL`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_SHELL)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_SHELL_MTU_DEPRECATED"></a>

## 386.51 `CONFIG_MCUMGR_TRANSPORT_SHELL_MTU_DEPRECATED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示 `MCUMGR_TRANSPORT_SHELL_MTU` 已偏离默认值。此选项已弃用（deprecated）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_SHELL && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y if CONFIG_MCUMGR_TRANSPORT_SHELL_MTU != 256
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.shell:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.shell#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 命令行 MCUmgr SMP 传输（Shell transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_SHELL`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_SHELL)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_SHELL_MTU`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_SHELL_MTU)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_MCUMGR_TRANSPORT_SHELL_RX_BUF_COUNT"></a>

## 386.52 `CONFIG_MCUMGR_TRANSPORT_SHELL_RX_BUF_COUNT`

**提示（Prompt）**：命令行 SMP 接收缓冲区数量（RX buffer count）

**说明（Help）**

通过命令行（shell）接收 SMP 分片使用的缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_SHELL && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.shell:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.shell#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 命令行 MCUmgr SMP 传输（Shell transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_SHELL`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_SHELL)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_SPI"></a>

## 386.53 `CONFIG_MCUMGR_TRANSPORT_SPI`

**提示（Prompt）**：SPI MCUmgr 简单管理协议传输（SMP transport）

**说明（Help）**

处理通过 SPI 收到的 SMP 命令。设备作为 SPI 外设（peripheral）与 SPI 控制器（controller）交换原始 SMP 数据包。数据就绪 GPIO（data-ready GPIO）用于通知控制器已有响应可读。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && CONFIG_SPI_PERIPHERAL && CONFIG_SPI && CONFIG_GPIO && DT_HAS_ZEPHYR_SMP_SPI_ENABLED && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_SPI_ASYNC
CONFIG_MCUMGR_TRANSPORT_REASSEMBLY
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.spi:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.spi#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_SPI_PERIPHERAL`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_PERIPHERAL)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_SPI_ASYNC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ASYNC)、[`CONFIG_MCUMGR_TRANSPORT_REASSEMBLY`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_REASSEMBLY)。

<a id="CONFIG_MCUMGR_TRANSPORT_SPI_MTU"></a>

## 386.54 `CONFIG_MCUMGR_TRANSPORT_SPI_MTU`

**提示（Prompt）**：SPI SMP 最大传输单元（MTU）

**说明（Help）**

单次 SPI 事务中发送或接收的原始 SMP 数据块最大大小，单位为字节，必须满足：

```text
MCUMGR_TRANSPORT_SPI_MTU <= MCUMGR_TRANSPORT_NETBUF_SIZE
```

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_SPI && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[8, CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.spi:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.spi#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → SPI MCUmgr 简单管理协议传输（SMP transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_SPI`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_SPI)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE)。

<a id="CONFIG_MCUMGR_TRANSPORT_UART"></a>

## 386.55 `CONFIG_MCUMGR_TRANSPORT_UART`

**提示（Prompt）**：UART MCUmgr SMP 传输（transport）

**说明（Help）**

处理通过 UART 收到的 SMP 命令，是 `MCUMGR_TRANSPORT_SHELL` 的轻量替代方式，无需额外线程即可接收 UART 上的 MCUmgr 命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CONSOLE && CONFIG_BASE64 && CONFIG_CRC && CONFIG_UART_MCUMGR && !CONFIG_UART_MCUMGR_RAW_PROTOCOL && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_TRANSPORT_SERIAL_HAS_SMP_OVER_CONSOLE
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.uart:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.uart#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_BASE64`](P197_lib_配置项参考_1.md#CONFIG_BASE64)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)、[`CONFIG_UART_MCUMGR`](P066_drivers_console_配置项参考.md#CONFIG_UART_MCUMGR)、[`CONFIG_UART_MCUMGR_RAW_PROTOCOL`](P066_drivers_console_配置项参考.md#CONFIG_UART_MCUMGR_RAW_PROTOCOL)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_SERIAL_HAS_SMP_OVER_CONSOLE`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_SERIAL_HAS_SMP_OVER_CONSOLE)。

<a id="CONFIG_MCUMGR_TRANSPORT_UART_ASYNC"></a>

## 386.56 `CONFIG_MCUMGR_TRANSPORT_UART_ASYNC`

**提示（Prompt）**：可用时使用 UART 异步 API（async API）

**说明（Help）**

若所选 MCUmgr UART 端口支持，则使用 UART 异步 API（async API）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_MCUMGR_TRANSPORT_UART || CONFIG_MCUMGR_TRANSPORT_RAW_UART) && CONFIG_UART_ASYNC_API && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.common:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.common#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 公共传输配置（Common transport configuration）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_UART`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UART)、[`CONFIG_MCUMGR_TRANSPORT_RAW_UART`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_RAW_UART)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_UART_ASYNC_BUFS"></a>

## 386.57 `CONFIG_MCUMGR_TRANSPORT_UART_ASYNC_BUFS`

**提示（Prompt）**：UART 异步接收缓冲区数量（async RX buffers）

**说明（Help）**

UART 异步 API 要求注册接收缓冲区（RX buffers）。接收写到缓冲区末尾时，会发送事件请求下一个缓冲区，以免因缓冲空间耗尽而停止接收。至少需要两个缓冲区，才能顺畅地连续接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_UART_ASYNC && (CONFIG_MCUMGR_TRANSPORT_UART || CONFIG_MCUMGR_TRANSPORT_RAW_UART) && CONFIG_UART_ASYNC_API && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[2, 8]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.common:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.common#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 公共传输配置（Common transport configuration） → 可用时使用 UART 异步 API（async API）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_UART_ASYNC`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UART_ASYNC)、[`CONFIG_MCUMGR_TRANSPORT_UART`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UART)、[`CONFIG_MCUMGR_TRANSPORT_RAW_UART`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_RAW_UART)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_UART_ASYNC_BUF_SIZE"></a>

## 386.58 `CONFIG_MCUMGR_TRANSPORT_UART_ASYNC_BUF_SIZE`

**提示（Prompt）**：单个 UART 异步接收缓冲区大小

**说明（Help）**

用于异步接收（asynchronous RX）的单个缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_UART_ASYNC && (CONFIG_MCUMGR_TRANSPORT_UART || CONFIG_MCUMGR_TRANSPORT_RAW_UART) && CONFIG_UART_ASYNC_API && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.common:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.common#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 公共传输配置（Common transport configuration） → 可用时使用 UART 异步 API（async API）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_UART_ASYNC`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UART_ASYNC)、[`CONFIG_MCUMGR_TRANSPORT_UART`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UART)、[`CONFIG_MCUMGR_TRANSPORT_RAW_UART`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_RAW_UART)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_UART_ASYNC_RX_TIMEOUT_US"></a>

## 386.59 `CONFIG_MCUMGR_TRANSPORT_UART_ASYNC_RX_TIMEOUT_US`

**提示（Prompt）**：刷新接收缓冲区的超时（RX buffer flush timeout）

**说明（Help）**

使用较高波特率（baudrate）时，减小此值可能提高数据吞吐量。原文举例称，`1599us` 在 `115200` 波特下对应 `23` 字节。值过小可能产生多余中断，过大则可能降低吞吐量。译注：保留原文示例数值；实际字节传输时间还取决于 UART 帧格式，原文未在此说明该条件。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_UART_ASYNC && (CONFIG_MCUMGR_TRANSPORT_UART || CONFIG_MCUMGR_TRANSPORT_RAW_UART) && CONFIG_UART_ASYNC_API && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
1599
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.common:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.common#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → 公共传输配置（Common transport configuration） → 可用时使用 UART 异步 API（async API）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_UART_ASYNC`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UART_ASYNC)、[`CONFIG_MCUMGR_TRANSPORT_UART`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UART)、[`CONFIG_MCUMGR_TRANSPORT_RAW_UART`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_RAW_UART)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_UART_MTU"></a>

## 386.60 `CONFIG_MCUMGR_TRANSPORT_UART_MTU`

**提示（Prompt）**：UART SMP 最大传输单元（MTU）【已弃用 DEPRECATED】

**说明（Help）**

UART 传输 `get_mtu` 回调返回的值。SMP 层不使用该回调，因此此选项与回调一起弃用。控制台 SMP 帧（SMP over console frames）限制为 127 字节，最大 SMP 数据包大小由 `MCUMGR_TRANSPORT_NETBUF_SIZE` 设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_UART && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.uart:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.uart#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → UART MCUmgr SMP 传输（transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_UART`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UART)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_UART_MTU_DEPRECATED"></a>

## 386.61 `CONFIG_MCUMGR_TRANSPORT_UART_MTU_DEPRECATED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示 `MCUMGR_TRANSPORT_UART_MTU` 已偏离默认值。此选项已弃用（deprecated）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_UART && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y if CONFIG_MCUMGR_TRANSPORT_UART_MTU != 256
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.uart:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.uart#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → UART MCUmgr SMP 传输（transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_UART`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UART)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_UART_MTU`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UART_MTU)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_MCUMGR_TRANSPORT_UDP"></a>

## 386.62 `CONFIG_MCUMGR_TRANSPORT_UDP`

**提示（Prompt）**：UDP MCUmgr SMP 传输（transport）

**说明（Help）**

处理通过 UDP 收到的 SMP 命令，启动一个线程监听配置的 UDP 端口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP && CONFIG_NET_SOCKETS && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_NET_CONNECTION_MANAGER
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.udp:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.udp#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_NET_CONNECTION_MANAGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONNECTION_MANAGER)。

<a id="CONFIG_MCUMGR_TRANSPORT_UDP_AUTOMATIC_INIT"></a>

## 386.63 `CONFIG_MCUMGR_TRANSPORT_UDP_AUTOMATIC_INIT`

**提示（Prompt）**：UDP SMP 自动启动（autostart）

**说明（Help）**

启动时自动启动 UDP SMP 传输，无需应用编写启动代码。否则，用户应用必须通过 `smp_udp_open` 和 `smp_udp_close` 手动启停传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MCUMGR_TRANSPORT_UDP_DTLS && CONFIG_MCUMGR_TRANSPORT_UDP && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.udp:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.udp#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → UDP MCUmgr SMP 传输（transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_UDP_DTLS`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP_DTLS)、[`CONFIG_MCUMGR_TRANSPORT_UDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_UDP_DTLS"></a>

## 386.64 `CONFIG_MCUMGR_TRANSPORT_UDP_DTLS`

**提示（Prompt）**：数据报传输层安全协议（DTLS）

**说明（Help）**

为 UDP 传输启用数据报传输层安全协议（DTLS）。此后不再支持普通未经认证的连接，也不会在启动时自动开启传输。应用必须先向系统添加并配置证书，再调用 `smp_udp_open` 打开传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_UDP && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS
CONFIG_MBEDTLS_ENABLE_HEAP
CONFIG_NET_SOCKETS_SOCKOPT_TLS
CONFIG_NET_SOCKETS_ENABLE_DTLS
CONFIG_TLS_CREDENTIALS
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.udp:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.udp#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → UDP MCUmgr SMP 传输（transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_UDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_ENABLE_HEAP`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_ENABLE_HEAP)、[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_NET_SOCKETS_ENABLE_DTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_ENABLE_DTLS)、[`CONFIG_TLS_CREDENTIALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLS_CREDENTIALS)。

<a id="CONFIG_MCUMGR_TRANSPORT_UDP_DTLS_TLS_TAG"></a>

## 386.65 `CONFIG_MCUMGR_TRANSPORT_UDP_DTLS_TLS_TAG`

**提示（Prompt）**：TLS 凭据标签（credential tag）

**说明（Help）**

启动 UDP 传输之前，应用必须将证书添加到本项指定的 TLS 标签（tag）下。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_UDP_DTLS && CONFIG_MCUMGR_TRANSPORT_UDP && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.udp:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.udp#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → UDP MCUmgr SMP 传输（transport） → 数据报传输层安全协议（DTLS）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_UDP_DTLS`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP_DTLS)、[`CONFIG_MCUMGR_TRANSPORT_UDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_UDP_IPV4"></a>

## 386.66 `CONFIG_MCUMGR_TRANSPORT_UDP_IPV4`

**提示（Prompt）**：UDP SMP 使用 IPv4

**说明（Help）**

为 SMP UDP 启用 IPv4 寻址，可与 IPv6 同时启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && CONFIG_MCUMGR_TRANSPORT_UDP && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.udp:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.udp#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → UDP MCUmgr SMP 传输（transport）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_MCUMGR_TRANSPORT_UDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_UDP_IPV6"></a>

## 386.67 `CONFIG_MCUMGR_TRANSPORT_UDP_IPV6`

**提示（Prompt）**：UDP SMP 使用 IPv6

**说明（Help）**

为 SMP UDP 启用 IPv6 寻址，可与 IPv4 同时启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6 && CONFIG_MCUMGR_TRANSPORT_UDP && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.udp:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.udp#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → UDP MCUmgr SMP 传输（transport）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_MCUMGR_TRANSPORT_UDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_UDP_MTU"></a>

## 386.68 `CONFIG_MCUMGR_TRANSPORT_UDP_MTU`

**提示（Prompt）**：UDP SMP 最大传输单元（MTU）

**说明（Help）**

通过 UDP 发送或接收的 SMP 帧最大大小，单位为字节，必须满足：

```text
MCUMGR_TRANSPORT_UDP_MTU <= MCUMGR_TRANSPORT_NETBUF_SIZE
```

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_UDP && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE if CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE < 1500
1500
```

**取值范围（Ranges）**

```text
[1, CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.udp:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.udp#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → UDP MCUmgr SMP 传输（transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_UDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE)。

<a id="CONFIG_MCUMGR_TRANSPORT_UDP_PORT"></a>

## 386.69 `CONFIG_MCUMGR_TRANSPORT_UDP_PORT`

**提示（Prompt）**：UDP SMP 端口（port）

**说明（Help）**

SMP 服务器监听 SMP 命令的 UDP 端口。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_UDP && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
1337
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.udp:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.udp#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → UDP MCUmgr SMP 传输（transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_UDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_UDP_STACK_SIZE"></a>

## 386.70 `CONFIG_MCUMGR_TRANSPORT_UDP_STACK_SIZE`

**提示（Prompt）**：UDP SMP 栈大小（stack size）

**说明（Help）**

SMP UDP 监听线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_UDP && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.udp:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.udp#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → UDP MCUmgr SMP 传输（transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_UDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_UDP_THREAD_PRIO"></a>

## 386.71 `CONFIG_MCUMGR_TRANSPORT_UDP_THREAD_PRIO`

**提示（Prompt）**：UDP SMP 线程优先级（thread priority）

**说明（Help）**

SMP UDP 监听线程的调度优先级（scheduling priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_TRANSPORT_UDP && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig.udp:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig.udp#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → UDP MCUmgr SMP 传输（transport）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_UDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_WORKQUEUE_STACK_SIZE"></a>

## 386.72 `CONFIG_MCUMGR_TRANSPORT_WORKQUEUE_STACK_SIZE`

**提示（Prompt）**：MCUmgr 传输工作队列栈大小

**说明（Help）**

MCUmgr 传输子系统工作队列（work queue）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_TRANSPORT_WORKQUEUE_THREAD_PRIO"></a>

## 386.73 `CONFIG_MCUMGR_TRANSPORT_WORKQUEUE_THREAD_PRIO`

**提示（Prompt）**：MCUmgr 传输工作队列线程优先级

**说明（Help）**

MCUmgr 传输子系统工作队列（work queue）的调度优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
-1 if CONFIG_ZTEST
3
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/transport/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)。

<a id="CONFIG_OSDP"></a>

## 386.74 `CONFIG_OSDP`

**提示（Prompt）**：开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**说明（Help）**

加入开放式受监督设备协议（OSDP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_CRC
```

**弱选择（Implies）**

```text
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_UART_INTERRUPT_DRIVEN
CONFIG_UART_USE_RUNTIME_CONFIGURE
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management）

**配置项引用（Symbol References）**：[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_USE_RUNTIME_CONFIGURE)。

<a id="CONFIG_OSDP_CMD_RETRY_WAIT_SEC"></a>

## 386.75 `CONFIG_OSDP_CMD_RETRY_WAIT_SEC`

**提示（Prompt）**：命令出错后的重试等待时间（秒）

**说明（Help）**

命令失败后，在重试或发送后续命令之前等待的时间，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_CP && CONFIG_OSDP
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.cp:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.cp#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_CP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_CP)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_CRYPTO_DRV_NAME"></a>

## 386.76 `CONFIG_OSDP_CRYPTO_DRV_NAME`

**提示（Prompt）**：OSDP 使用的密码驱动（Crypto driver）

**说明（Help）**

OSDP 安全通道（Secure Channel）使用 AES-128 保护控制面板（CP）与外围设备（PD）之间的通信。在此提供一个可用密码驱动的名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_SC_ENABLED && CONFIG_OSDP
```

**默认值（Defaults）**

```text
"CRYPTO_MTLS"
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 安全通道（Secure Channel）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_SC_ENABLED`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_OSDP_SC_ENABLED)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_LOG_LEVEL"></a>

## 386.77 `CONFIG_OSDP_LOG_LEVEL`

**提示（Prompt）**：OSDP 日志级别（Logging Level）

**说明（Help）**

设置 OSDP 驱动的日志级别（logging level）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_MASTER_KEY"></a>

## 386.78 `CONFIG_OSDP_MASTER_KEY`

**提示（Prompt）**：安全通道主密钥（Secure Channel Master Key）

**说明（Help）**

16 字节 OSDP 安全通道主密钥（master key）的十六进制字符串表示。启用安全通道时，此密钥为必需项。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_SC_ENABLED && CONFIG_OSDP_MODE_CP && CONFIG_OSDP
```

**默认值（Defaults）**

```text
"NONE"
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.cp:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.cp#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_SC_ENABLED`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_OSDP_SC_ENABLED)、[`CONFIG_OSDP_MODE_CP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_CP)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_MODE_CP"></a>

## 386.79 `CONFIG_OSDP_MODE_CP`

**提示（Prompt）**：将 OSDP 配置为控制面板模式（Control Panel mode）

**说明（Help）**

将此设备配置为控制面板（Control Panel，CP）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 工作模式（Mode of Operation）

<a id="CONFIG_OSDP_MODE_PD"></a>

## 386.80 `CONFIG_OSDP_MODE_PD`

**提示（Prompt）**：将 OSDP 配置为外围设备模式（Peripheral Device mode）

**说明（Help）**

将此设备配置为外围设备（Peripheral Device，PD）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 工作模式（Mode of Operation）

<a id="CONFIG_OSDP_NUM_CONNECTED_PD"></a>

## 386.81 `CONFIG_OSDP_NUM_CONNECTED_PD`

原库同名定义共 2 条；本项为数据库第 14679 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

外围设备（PD）模式下，已连接 PD 的数量始终为 `1`，不可配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_NUM_CONNECTED_PD--record-14680"></a>

## 386.82 `CONFIG_OSDP_NUM_CONNECTED_PD`

原库同名定义共 2 条；本项为数据库第 14680 条记录，各定义分别保留。

**提示（Prompt）**：已连接外围设备数量（Number of connected Peripheral Devices）

**说明（Help）**

外围设备（PD）模式下，已连接 PD 的数量始终为 `1`，不可配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_CP && CONFIG_OSDP
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 126]
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.cp:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.cp#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_CP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_CP)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PACKET_TRACE"></a>

## 386.83 `CONFIG_OSDP_PACKET_TRACE`

**提示（Prompt）**：将 OSDP 收发字节打印到控制台

**说明（Help）**

为调试，将通过 OSDP 发送和接收的字节打印到控制台（console），使用 `LOG_HEXDUMP_DBG()` 实现，输出可能非常多。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_ADDRESS"></a>

## 386.84 `CONFIG_OSDP_PD_ADDRESS`

**提示（Prompt）**：外围设备地址（Peripheral Device Address）

**说明（Help）**

最低 7 位表示消息目标外围设备（PD）的地址，或发送响应的 PD 地址。`0x7F` 保留为广播地址（broadcast address），所有 PD 都会响应。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 126]
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_ADDRESS_LIST"></a>

## 386.85 `CONFIG_OSDP_PD_ADDRESS_LIST`

**提示（Prompt）**：已连接外围设备地址列表（addresses）

**说明（Help）**

以逗号分隔的外围设备（PD）地址列表。值的数量必须与上方配置的已连接 PD 数量完全一致。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_CP && CONFIG_OSDP
```

**默认值（Defaults）**

```text
"1"
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.cp:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.cp#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_CP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_CP)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_CAP_CARD_DATA_FORMAT_COMP_LEVEL"></a>

## 386.86 `CONFIG_OSDP_PD_CAP_CARD_DATA_FORMAT_COMP_LEVEL`

**提示（Prompt）**：符合性级别（Compliance Level）

**说明（Help）**

可选值：

- `01`：外围设备（PD）以位数组形式向控制面板（CP）发送卡数据，最多 1024 位。
- `02`：PD 以二进制编码十进制（BCD）字符数组形式发送卡数据，最多 256 个字符。
- `03`：PD 可使用位数组或 BCD 字符数组发送卡数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 3]
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:215`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L215)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 外围设备能力（PD Capabilities） → 卡数据格式（Card Data Format）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_CAP_CONTACT_STATUS_MONITORING_COMP_LEVEL"></a>

## 386.87 `CONFIG_OSDP_PD_CAP_CONTACT_STATUS_MONITORING_COMP_LEVEL`

**提示（Prompt）**：符合性级别（Compliance Level）

**说明（Help）**

可选值：

- `01`：外围设备（PD）监测并报告电路状态，不提供线路监督（supervision），按默认规则将触点状态解释为活动／非活动状态。
- `02`：在 `01` 基础上，允许配置开路／闭路状态到活动／非活动状态的编码关系；用户可将每个电路配置为常闭（normally closed）或常开（normally open）。
- `03`：在 `02` 基础上，支持受监督监测（supervised monitoring），各电路的工作模式由配置决定。
- `04`：在 `03` 基础上，支持在厂商规定范围内自定义线路末端（End-Of-Line）设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 外围设备能力（PD Capabilities） → 触点状态监测（Contact Status Monitoring）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_CAP_CONTACT_STATUS_MONITORING_NUM_ITEMS"></a>

## 386.88 `CONFIG_OSDP_PD_CAP_CONTACT_STATUS_MONITORING_NUM_ITEMS`

**提示（Prompt）**：项目数量（Number of items）

**说明（Help）**

输入（Inputs）的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 外围设备能力（PD Capabilities） → 触点状态监测（Contact Status Monitoring）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_CAP_OUTPUT_CONTROL_COMP_LEVEL"></a>

## 386.89 `CONFIG_OSDP_PD_CAP_OUTPUT_CONTROL_COMP_LEVEL`

**提示（Prompt）**：符合性级别（Compliance Level）

**说明（Help）**

可选值：

- `01`：外围设备（PD）能按控制面板（CP）的直接命令激活或停用输出。
- `02`：在 `01` 基础上，允许配置输出驱动器的非活动状态。通常，非活动输出对应 PD 未供电且输出设备（继电器）未励磁的状态；反向驱动设置则使 PD 在非活动状态给输出励磁，在活动状态取消励磁，从而支持失效安全／失效保安（fail-safe/fail-secure）工作模式。
- `03`：在 `01` 基础上，支持输出定时命令（timed commands），按指定持续时间维持指定输出状态。
- `04`：同时具备 `02` 和 `03` 的能力，即正常／反向驱动及定时操作。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 外围设备能力（PD Capabilities） → 输出控制（Output Control）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_CAP_OUTPUT_CONTROL_NUM_ITEMS"></a>

## 386.90 `CONFIG_OSDP_PD_CAP_OUTPUT_CONTROL_NUM_ITEMS`

**提示（Prompt）**：项目数量（Number of items）

**说明（Help）**

输出（Outputs）的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 外围设备能力（PD Capabilities） → 输出控制（Output Control）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_CAP_READER_AUDIBLE_OUTPUT_COMP_LEVEL"></a>

## 386.91 `CONFIG_OSDP_PD_CAP_READER_AUDIBLE_OUTPUT_COMP_LEVEL`

**提示（Prompt）**：符合性级别（Compliance Level）

**说明（Help）**

可选值：

- `01`：外围设备（PD）仅支持开／关控制。
- `02`：PD 支持定时命令（timed commands）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 外围设备能力（PD Capabilities） → 声音输出（Audible Output）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_CAP_READER_AUDIBLE_OUTPUT_NUM_ITEMS"></a>

## 386.92 `CONFIG_OSDP_PD_CAP_READER_AUDIBLE_OUTPUT_NUM_ITEMS`

**提示（Prompt）**：项目数量（Number of items）

**说明（Help）**

每个读卡器的声音指示器（audible annunciators）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:183`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L183)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 外围设备能力（PD Capabilities） → 声音输出（Audible Output）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_CAP_READER_LED_CONTROL_COMP_LEVEL"></a>

## 386.93 `CONFIG_OSDP_PD_CAP_READER_LED_CONTROL_COMP_LEVEL`

**提示（Prompt）**：符合性级别（Compliance Level）

**说明（Help）**

可选值：

- `01`：外围设备（PD）仅支持开／关控制。
- `02`：PD 支持定时命令（timed commands）。
- `03`：在 `02` 基础上，支持双色 LED（bi-color LEDs）。
- `04`：在 `02` 基础上，支持三色 LED（tri-color LEDs）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 外围设备能力（PD Capabilities） → LED 控制（LED Control）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_CAP_READER_LED_CONTROL_NUM_ITEMS"></a>

## 386.94 `CONFIG_OSDP_PD_CAP_READER_LED_CONTROL_NUM_ITEMS`

**提示（Prompt）**：项目数量（Number of items）

**说明（Help）**

每个读卡器的 LED 数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 外围设备能力（PD Capabilities） → LED 控制（LED Control）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_CAP_READER_TEXT_OUTPUT_COMP_LEVEL"></a>

## 386.95 `CONFIG_OSDP_PD_CAP_READER_TEXT_OUTPUT_COMP_LEVEL`

**提示（Prompt）**：符合性级别（Compliance Level）

**说明（Help）**

可选值：

- `00`：外围设备（PD）不支持文本显示。
- `01`：支持 1 行，每行 16 个字符。
- `02`：支持 2 行，每行 16 个字符。
- `03`：支持 4 行，每行 16 个字符。
- `04`：待定（TBD）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 外围设备能力（PD Capabilities） → 文本输出（Text Output）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_CAP_READER_TEXT_OUTPUT_NUM_ITEMS"></a>

## 386.96 `CONFIG_OSDP_PD_CAP_READER_TEXT_OUTPUT_NUM_ITEMS`

**提示（Prompt）**：项目数量（Number of items）

**说明（Help）**

每个读卡器的文本显示器（textual displays）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:205`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L205)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 外围设备能力（PD Capabilities） → 文本输出（Text Output）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_CAP_TIME_KEEPING_COMP_LEVEL"></a>

## 386.97 `CONFIG_OSDP_PD_CAP_TIME_KEEPING_COMP_LEVEL`

**提示（Prompt）**：符合性级别（Compliance Level）

**说明（Help）**

可选值：

- `00`：外围设备（PD）不支持时间／日期功能。
- `01`：PD 能按 `osdp_TDSET` 命令处理时间／日期设置。
- `02`：PD 能在本地更新时间和日期。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:232`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L232)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 外围设备能力（PD Capabilities） → 计时功能（Time Keeping）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_COMMAND_QUEUE_SIZE"></a>

## 386.98 `CONFIG_OSDP_PD_COMMAND_QUEUE_SIZE`

原库同名定义共 2 条；本项为数据库第 14696 条记录，各定义分别保留。

**提示（Prompt）**：OSDP 外围设备命令队列大小（command queue size）

**说明（Help）**

可为单个外围设备（PD）排队的命令数量。在控制面板（CP）模式下，队列大小乘以已连接 PD 数量，因此总占用可能迅速增长。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_COMMAND_QUEUE_SIZE--record-14697"></a>

## 386.99 `CONFIG_OSDP_PD_COMMAND_QUEUE_SIZE`

原库同名定义共 2 条；本项为数据库第 14697 条记录，各定义分别保留。

**提示（Prompt）**：OSDP 外围设备命令队列大小（command queue size）

**说明（Help）**

可为单个外围设备（PD）排队的命令数量。在控制面板（CP）模式下，队列大小乘以已连接 PD 数量，因此总占用可能迅速增长。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_CP && CONFIG_OSDP
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.cp:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.cp#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_CP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_CP)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_ID_FIRMWARE_VERSION"></a>

## 386.100 `CONFIG_OSDP_PD_ID_FIRMWARE_VERSION`

**提示（Prompt）**：外围设备固件版本（PD Firmware Version）

**说明（Help）**

固件修订代码（firmware revision code）：

- 位 `0–7`：构建版本号（build version number）。
- 位 `8–15`：次版本号（minor version number）。
- 位 `16–23`：主版本号（major version number）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
0x00010100
```

**取值范围（Ranges）**

```text
[0, 0x00FFFFFF]
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → 外围设备标识信息（Peripheral Device ID Information）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<!-- kconfig-navigation -->

[上一章](P385_subsys_mgmt_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P387_subsys_mgmt_配置项参考_4.md)
