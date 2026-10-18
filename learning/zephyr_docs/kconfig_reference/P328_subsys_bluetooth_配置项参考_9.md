---
id: learning.zephyr-docs.kconfig-reference.page-328
title: "`subsys/bluetooth`配置项参考（9/13）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第328章\_`subsys/bluetooth`配置项参考（9/13）

本章翻译官方 Kconfig 数据库中 `subsys/bluetooth` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_MESH_BLOB_CLI"></a>

## 328.1 `CONFIG_BT_MESH_BLOB_CLI`

**提示（Prompt）**：BLOB 传输客户端模型支持（BLOB Transfer Client model）

**说明（Help）**

启用二进制大对象（Binary Large Object，BLOB）传输客户端模型（Transfer Client model）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1003`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1003)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BLOB_CLI_BLOCK_RETRIES"></a>

## 328.2 `CONFIG_BT_MESH_BLOB_CLI_BLOCK_RETRIES`

**提示（Prompt）**：每块重试次数（Number of retries per block）

**说明（Help）**

控制客户端针对每个块（block），尝试向 BLOB 接收方重新发送缺失分片（chunks）的次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_BLOB_CLI && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1010`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1010)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → BLOB 传输客户端模型支持（BLOB Transfer Client model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BLOB_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_CLI)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BLOB_IO_FLASH"></a>

## 328.3 `CONFIG_BT_MESH_BLOB_IO_FLASH`

**提示（Prompt）**：BLOB 闪存流（BLOB flash stream）

**说明（Help）**

启用 BLOB 闪存流（flash stream），直接从 Flash 读取 BLOB 或向 Flash 写入 BLOB。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_MESH_BLOB_SRV || CONFIG_BT_MESH_BLOB_CLI) && CONFIG_FLASH_MAP && CONFIG_FLASH_PAGE_LAYOUT && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1061`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1061)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BLOB_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_SRV)、[`CONFIG_BT_MESH_BLOB_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_CLI)、[`CONFIG_FLASH_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MAP)、[`CONFIG_FLASH_PAGE_LAYOUT`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_PAGE_LAYOUT)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BLOB_IO_FLASH_BLOCK_CACHE"></a>

## 328.4 `CONFIG_BT_MESH_BLOB_IO_FLASH_BLOCK_CACHE`

**提示（Prompt）**：在 RAM 缓存每个 BLOB 块并按写入块对齐后一次刷写（write-block-aligned flush）

**说明（Help）**

在 RAM 中缓存整个 BLOB 块（block），直到该块最后一个分片（chunk）到达时再编程 Flash，使每个 Flash 写入块（write-block）在两次擦除之间只编程一次，而非每收到一个分片就编程一次。

对于需要显式擦除（explicit-erase）、且写入块为 ECC 保护的编程单元（phrase）的 Flash，每次擦除后该单元可能只允许编程一次，因此需要此功能，例如某些 NXP MCXW SoC 的内部 Flash。如果不使用它，当 BLOB 分片大小不是 Flash 写入块大小的整数倍时，相邻两个分片会分别编程它们共享的写入块；第二次编程会破坏 ECC 校验综合值（ECC syndrome），导致下一次读取出现故障。

启用后，每个 BLOB 闪存流需要一个块大小的 RAM 缓冲区（`CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MAX`）。如果 Flash 允许在两次擦除之间多次编程同一个写入块，例如普通 NOR 或 RRAM，应保持禁用：默认的逐分片写入路径已经正确，且无需额外 RAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_BLOB_IO_FLASH && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1080`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1080)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → BLOB 闪存流（BLOB flash stream）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BLOB_IO_FLASH`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_IO_FLASH)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BLOB_IO_FLASH_WRITE_BLOCK_SIZE_MAX"></a>

## 328.5 `CONFIG_BT_MESH_BLOB_IO_FLASH_WRITE_BLOCK_SIZE_MAX`

**提示（Prompt）**：支持的最大写入块大小（Maximum supported write block size）

**说明（Help）**

将该值设为设备写入块大小（write block size）的整数倍时，BLOB IO Flash 模块支持需要显式擦除（explicit erase）的闪存设备。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_BLOB_IO_FLASH && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1073`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1073)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → BLOB 闪存流（BLOB flash stream）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BLOB_IO_FLASH`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_IO_FLASH)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BLOB_REPORT_TIMEOUT"></a>

## 328.6 `CONFIG_BT_MESH_BLOB_REPORT_TIMEOUT`

**提示（Prompt）**：拉取模式的部分块报告间隔（Partial Block Report interval in Pull mode）

**说明（Help）**

拉取模式 BLOB 传输服务器（Pull BLOB Transfer Server）用于报告缺失分片（chunks）的定时器值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_BLOB_SRV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 31]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:982`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L982)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → BLOB 传输服务器模型支持（BLOB Transfer Server model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BLOB_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_SRV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BLOB_SIZE_MAX"></a>

## 328.7 `CONFIG_BT_MESH_BLOB_SIZE_MAX`

**提示（Prompt）**：最大 BLOB 大小，单位为字节（Largest BLOB size in bytes）

**说明（Help）**

BLOB 传输服务器（Transfer Server）可接收的最大对象大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_BLOB_SRV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
524288
```

**取值范围（Ranges）**

```text
[1, 3257617792]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:955`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L955)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → BLOB 传输服务器模型支持（BLOB Transfer Server model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BLOB_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_SRV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BLOB_SRV"></a>

## 328.8 `CONFIG_BT_MESH_BLOB_SRV`

**提示（Prompt）**：BLOB 传输服务器模型支持（BLOB Transfer Server model）

**说明（Help）**

启用二进制大对象（Binary Large Object，BLOB）传输服务器模型（Transfer Server model）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:937`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L937)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BLOB_SRV_PULL_REQ_COUNT"></a>

## 328.9 `CONFIG_BT_MESH_BLOB_SRV_PULL_REQ_COUNT`

**提示（Prompt）**：每次拉取请求的分片数量（Number of chunks to request for each pull）

**说明（Help）**

在拉取模式（Pull BLOB Transfer Mode）下，BLOB 传输服务器向客户端请求固定数量的分片（chunks）。此选项控制请求中的分片数量。如果 BLOB 传输服务器实例化在低功耗节点（Low Power node）上，拉取请求数量会被缩减，以免友谊队列（Friend queue）溢出。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_BLOB_SRV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:944`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L944)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → BLOB 传输服务器模型支持（BLOB Transfer Server model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BLOB_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_SRV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BRG_CFG_CLI"></a>

## 328.10 `CONFIG_BT_MESH_BRG_CFG_CLI`

**提示（Prompt）**：桥接配置客户端模型支持（Bridge Configuration Client model）

**说明（Help）**

桥接配置客户端（Bridge Configuration Client）用于支持能够配置其他节点子网桥接功能（subnet bridge functionality）的节点。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1417`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1417)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BRG_CFG_CLI_TIMEOUT"></a>

## 328.11 `CONFIG_BT_MESH_BRG_CFG_CLI_TIMEOUT`

**提示（Prompt）**：桥接配置客户端模型超时，单位为毫秒（Bridge Configuration Client model timeout）

**说明（Help）**

此超时控制桥接配置客户端（bridge configuration client）等待响应消息到达的时间，可在运行时通过 `bt_mesh_brg_cfg_cli_timeout_set` 更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_BRG_CFG_CLI && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1425`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1425)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 桥接配置客户端模型支持（Bridge Configuration Client model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BRG_CFG_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BRG_CFG_CLI)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BRG_CFG_SRV"></a>

## 328.12 `CONFIG_BT_MESH_BRG_CFG_SRV`

**提示（Prompt）**：桥接配置服务器模型支持（Bridge Configuration Server model）

**说明（Help）**

桥接配置服务器模型（Bridge Configuration Server model）用于支持配置节点的子网桥接功能（subnet bridge functionality）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_MODEL_EXTENSIONS && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1398`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1398)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_MODEL_EXTENSIONS`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_MODEL_EXTENSIONS)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_BRG_TABLE_ITEMS_MAX"></a>

## 328.13 `CONFIG_BT_MESH_BRG_TABLE_ITEMS_MAX`

**提示（Prompt）**：桥接表最大条目数（Maximum number of entries in the bridging table）

**说明（Help）**

桥接表（bridging table）的最大条目数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[16, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1408`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1408)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 子网桥接配置（Subnet Bridge configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_CDB"></a>

## 328.14 `CONFIG_BT_MESH_CDB`

**提示（Prompt）**：Mesh 配置数据库（Mesh Configuration Database）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:386`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L386)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_CDB_APP_KEY_COUNT"></a>

## 328.15 `CONFIG_BT_MESH_CDB_APP_KEY_COUNT`

**提示（Prompt）**：数据库中应用密钥最大数量（Maximum number of application keys in the database）

**说明（Help）**

指定配置数据库（configuration database）最多可保存的应用密钥（application keys）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_CDB && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 4096]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:407`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L407)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning） → Mesh 配置数据库（Mesh Configuration Database）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CDB`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_CDB)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_CDB_KEY_SYNC"></a>

## 328.16 `CONFIG_BT_MESH_CDB_KEY_SYNC`

**提示（Prompt）**：密钥同步支持（Keys synchronization support）

**说明（Help）**

启用后，支持在 Mesh 协议栈与配置数据库（CDB）之间同步密钥。通过配置服务器消息（Configuration Server messages）在 Mesh 协议栈执行的密钥添加、移除和更新操作，会自动同步到 CDB。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_CDB && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:415`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L415)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning） → Mesh 配置数据库（Mesh Configuration Database）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CDB`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_CDB)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_CDB_NODE_COUNT"></a>

## 328.17 `CONFIG_BT_MESH_CDB_NODE_COUNT`

**提示（Prompt）**：数据库中节点最大数量（Maximum number of nodes in the database）

**说明（Help）**

指定每个网络最多可在配置数据库（configuration database）中保存的节点（nodes）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_CDB && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 4096]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:391`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L391)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning） → Mesh 配置数据库（Mesh Configuration Database）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CDB`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_CDB)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_CDB_SUBNET_COUNT"></a>

## 328.18 `CONFIG_BT_MESH_CDB_SUBNET_COUNT`

**提示（Prompt）**：数据库中子网最大数量（Maximum number of subnets in the database）

**说明（Help）**

指定配置数据库（configuration database）最多可保存的子网（subnets）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_CDB && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 4096]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:399`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L399)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning） → Mesh 配置数据库（Mesh Configuration Database）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CDB`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_CDB)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_CFG_CLI"></a>

## 328.19 `CONFIG_BT_MESH_CFG_CLI`

**提示（Prompt）**：配置客户端模型支持（Configuration Client Model）

**说明（Help）**

启用配置客户端模型（configuration client model）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:903`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L903)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_CFG_CLI_TIMEOUT"></a>

## 328.20 `CONFIG_BT_MESH_CFG_CLI_TIMEOUT`

**提示（Prompt）**：配置客户端模型超时，单位为毫秒（Config Client model timeout）

**说明（Help）**

此超时控制配置客户端（config client）等待响应消息到达的时间，可在运行时通过 `bt_mesh_cfg_cli_timeout_set` 更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_CFG_CLI && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:910`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L910)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 配置客户端模型支持（Configuration Client Model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CFG_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_CFG_CLI)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_COMP_PAGE_1"></a>

## 328.21 `CONFIG_BT_MESH_COMP_PAGE_1`

**提示（Prompt）**：组成数据页 1 支持（Composition Data Page 1）

**说明（Help）**

启用组成数据页 1（Composition Data Page 1）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:812`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L812)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 访问层（Access layer）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_COMP_PAGE_2"></a>

## 328.22 `CONFIG_BT_MESH_COMP_PAGE_2`

**提示（Prompt）**：组成数据页 2 支持（Composition Data Page 2）

**说明（Help）**

启用组成数据页 2（Composition Data Page 2）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:829`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L829)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 访问层（Access layer）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_COMP_PST_BUF_SIZE"></a>

## 328.23 `CONFIG_BT_MESH_COMP_PST_BUF_SIZE`

**提示（Prompt）**：组成数据页持久化缓冲区大小（Composition Data Page persistence buffer size）

**说明（Help）**

在栈上分配的缓冲区，用于 Flash 操作期间临时保存组成数据页（Composition Data Pages）。大小应与应用中最大的组成数据页相适应。注意：设备固件更新后，该缓冲区仍应足够大，以恢复之前保存的数据页。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:834`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L834)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 访问层（Access layer）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_CRPL"></a>

## 328.24 `CONFIG_BT_MESH_CRPL`

**提示（Prompt）**：重放保护列表最大容量（Maximum capacity of the replay protection list）

**说明（Help）**

指定重放保护列表（replay protection list）的最大容量。此选项类似网络消息缓存大小（network message cache size），但用途是防止重放攻击（replay attacks）。

注意：根据其他蓝牙规范要求，为确保 CRPL 具有足够空间用于节点正常运行，在节点启用子网桥接（subnet bridge）功能时，应在项目配置文件中增加 CRPL 容量；增加量至少应为项目指定的桥接表条目数 `BT_MESH_BRG_TABLE_ITEMS_MAX`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
26 if CONFIG_BT_MESH_BRG_CFG_SRV
10
```

**取值范围（Ranges）**

```text
[2, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:748`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L748)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer） → 重放保护列表（Replay Protection List）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_BRG_CFG_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BRG_CFG_SRV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_CRYPTO_LIB"></a>

## 328.25 `CONFIG_BT_MESH_CRYPTO_LIB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于 Mesh 安全的密码库支持（Crypto library support for mesh security）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_DERIVE
CONFIG_PSA_WANT_ALG_CMAC
CONFIG_PSA_WANT_ALG_ECB_NO_PADDING
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_ALG_CCM
CONFIG_PSA_WANT_KEY_TYPE_HMAC
CONFIG_PSA_WANT_ALG_HMAC
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ECC_SECP_R1_256
CONFIG_BT_MESH_SECURE_STORAGE if CONFIG_BT_SETTINGS && CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS
```

**弱选择（Implies）**

```text
CONFIG_MBEDTLS_AES_ROM_TABLES if CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1523`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1523)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_DERIVE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_DERIVE)、[`CONFIG_PSA_WANT_ALG_CMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CMAC)、[`CONFIG_PSA_WANT_ALG_ECB_NO_PADDING`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECB_NO_PADDING)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_ALG_CCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CCM)、[`CONFIG_PSA_WANT_KEY_TYPE_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_HMAC)、[`CONFIG_PSA_WANT_ALG_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HMAC)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)、[`CONFIG_BT_MESH_SECURE_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SECURE_STORAGE)、[`CONFIG_BT_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SETTINGS)、[`CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS)、[`CONFIG_MBEDTLS_AES_ROM_TABLES`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_AES_ROM_TABLES)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_MESH_SECURE_STORAGE`。

<a id="CONFIG_BT_MESH_DEBUG_USE_ID_ADDR"></a>

## 328.26 `CONFIG_BT_MESH_DEBUG_USE_ID_ADDR`

**提示（Prompt）**：所有广播均使用身份地址（identity address for all advertising）

**说明（Help）**

强制所有广播使用本地身份地址（local identity address）。这有助于调试，例如分析跟踪记录（traces）；但会损害设备隐私，因此绝不能在生产构建（production build）中启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:229`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L229)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 广播者（Advertiser）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_DEFAULT_TTL"></a>

## 328.27 `CONFIG_BT_MESH_DEFAULT_TTL`

**提示（Prompt）**：默认生存时间值（Default TTL value）

**说明（Help）**

控制出站消息的默认生存时间（TTL）值，可以通过运行时配置更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
7
```

**取值范围（Ranges）**

```text
[0, 128]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:738`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L738)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 传输层（Transport layer）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_DELAYABLE_PUBLICATION"></a>

## 328.28 `CONFIG_BT_MESH_DELAYABLE_PUBLICATION`

**提示（Prompt）**：可延迟发布（Delayable publication）

**说明（Help）**

启用后，周期性发布（periodic publications）随机延迟 `20` 到 `50ms`；协议栈启动时或调用 `bt_mesh_model_publish()` 触发的发布延迟 `20` 到 `500ms`。此选项降低多个节点同时发布时的冲突概率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:890`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L890)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 访问层（Access layer）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_DFD_SRV"></a>

## 328.29 `CONFIG_BT_MESH_DFD_SRV`

**提示（Prompt）**：固件分发服务器模型支持（Firmware Distribution Server model）

**说明（Help）**

启用固件分发服务器模型（Firmware Distribution Server model）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_BLOB_SRV && CONFIG_BT_MESH_DFU_CLI && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1174)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BLOB_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_SRV)、[`CONFIG_BT_MESH_DFU_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_DFU_CLI)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD"></a>

## 328.30 `CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD`

**提示（Prompt）**：DFU 映像带外上传支持（DFU image OOB upload）

**说明（Help）**

启用用于固件分发的映像带外上传（OOB upload）支持。启用后，必须实现若干回调并使用初始化宏 `BT_MESH_DFD_SRV_INIT_OOB`。所需回调详情参见 `bt_mesh_dfd_srv_cb` 的 API 文档。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_DFD_SRV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1206)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 固件分发服务器模型支持（Firmware Distribution Server model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFD_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_DFD_SRV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_DFD_SRV_SLOT_MAX_SIZE"></a>

## 328.31 `CONFIG_BT_MESH_DFD_SRV_SLOT_MAX_SIZE`

**提示（Prompt）**：可存储的最大 DFU 映像（Largest DFU image that can be stored）

**说明（Help）**

定义单个槽位（slot）可存储的最大设备固件更新映像（DFU image）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_DFD_SRV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_BLOB_SIZE_MAX
```

**取值范围（Ranges）**

```text
[0, CONFIG_BT_MESH_BLOB_SIZE_MAX]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1183`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1183)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 固件分发服务器模型支持（Firmware Distribution Server model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFD_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_DFD_SRV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_BLOB_SIZE_MAX`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_SIZE_MAX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_DFD_SRV_SLOT_SPACE"></a>

## 328.32 `CONFIG_BT_MESH_DFD_SRV_SLOT_SPACE`

**提示（Prompt）**：DFU 映像总存储空间（Total DFU image storage space）

**说明（Help）**

定义固件分发服务器（Firmware Distribution Server）专用于保存 DFU 映像的总存储空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_DFD_SRV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_DFD_SRV_SLOT_MAX_SIZE
```

**取值范围（Ranges）**

```text
[0, 4294967295]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1190`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1190)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 固件分发服务器模型支持（Firmware Distribution Server model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFD_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_DFD_SRV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_DFD_SRV_SLOT_MAX_SIZE`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_DFD_SRV_SLOT_MAX_SIZE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_DFD_SRV_TARGETS_MAX"></a>

## 328.33 `CONFIG_BT_MESH_DFD_SRV_TARGETS_MAX`

**提示（Prompt）**：目标节点最大数量（Maximum Target node count）

**说明（Help）**

定义固件分发服务器（Firmware Distribution Server）可同时面向的目标节点（Target nodes）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_DFD_SRV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1198`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1198)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 固件分发服务器模型支持（Firmware Distribution Server model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFD_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_DFD_SRV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_DFU_CLI"></a>

## 328.34 `CONFIG_BT_MESH_DFU_CLI`

**提示（Prompt）**：固件更新客户端模型支持（Firmware Update Client model）

**说明（Help）**

启用固件更新客户端模型（Firmware Update Client model）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_MODEL_EXTENSIONS && CONFIG_BT_MESH_BLOB_CLI && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1109)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_MODEL_EXTENSIONS`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_MODEL_EXTENSIONS)、[`CONFIG_BT_MESH_BLOB_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_CLI)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_DFU_FWID_MAXLEN"></a>

## 328.35 `CONFIG_BT_MESH_DFU_FWID_MAXLEN`

**提示（Prompt）**：DFU 固件标识最大长度（DFU FWID max length）

**说明（Help）**

定义 Mesh 协议栈能够管理的、用于描述映像的厂商专用版本信息（vendor-specific version information）最大长度。注意：原文明确指出，只有 `106` 个八位字节（octets）的大小才能使设备符合蓝牙 Mesh DFU 规范。设为小于 `106` 时，如果固件映像带有更长的厂商专用版本信息，设备将无法管理该映像。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
106
```

**取值范围（Ranges）**

```text
[0, 106]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1119)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 固件更新模型配置（Firmware Update model configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_DFU_METADATA"></a>

## 328.36 `CONFIG_BT_MESH_DFU_METADATA`

**提示（Prompt）**：默认元数据格式支持（default metadata format）

**说明（Help）**

添加一组函数，用于按蓝牙 Mesh DFU 子系统定义的格式编码和解码固件元数据（firmware metadata）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1139)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 固件更新模型配置（Firmware Update model configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_DFU_METADATA_MAXLEN"></a>

## 328.37 `CONFIG_BT_MESH_DFU_METADATA_MAXLEN`

**提示（Prompt）**：DFU 元数据最大长度（DFU metadata max length）

**说明（Help）**

定义映像元数据（metadata）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[18, 255] if CONFIG_BT_MESH_DFU_METADATA
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1131)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 固件更新模型配置（Firmware Update model configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_DFU_METADATA`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_DFU_METADATA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_DFU_SLOTS"></a>

## 328.38 `CONFIG_BT_MESH_DFU_SLOTS`

**提示（Prompt）**：固件映像槽位管理器（Firmware image slot manager）

**说明（Help）**

启用 DFU 映像槽位管理器（image slot manager），为固件更新客户端模型（Firmware Update Client model）管理固件分发槽位。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_MESH_DFU_CLI
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1155)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_DFU_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_DFU_CLI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_DFU_SLOT_CNT"></a>

## 328.39 `CONFIG_BT_MESH_DFU_SLOT_CNT`

**提示（Prompt）**：固件映像槽位数量（Number of firmware image slots）

**说明（Help）**

定义 DFU 映像槽位管理器（image slot manager）可同时维护的固件槽位（firmware slots）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_DFU_SLOTS && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 32767]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1164)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 固件映像槽位管理器（Firmware image slot manager）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFU_SLOTS`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_DFU_SLOTS)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_DFU_SRV"></a>

## 328.40 `CONFIG_BT_MESH_DFU_SRV`

**提示（Prompt）**：固件更新服务器模型支持（Firmware Update Server model）

**说明（Help）**

启用固件更新服务器模型（Firmware Update Server model）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_MODEL_EXTENSIONS && CONFIG_BT_MESH_BLOB_SRV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1102)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_MODEL_EXTENSIONS`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_MODEL_EXTENSIONS)、[`CONFIG_BT_MESH_BLOB_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_BLOB_SRV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_DFU_URI_MAXLEN"></a>

## 328.41 `CONFIG_BT_MESH_DFU_URI_MAXLEN`

**提示（Prompt）**：DFU URI 最大长度（DFU URI max length）

**说明（Help）**

定义映像 URI 的最大长度，不包含字符串终止符（string terminator）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1145)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 固件更新模型配置（Firmware Update model configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_ECDH_P256_CMAC_AES128_AES_CCM"></a>

## 328.42 `CONFIG_BT_MESH_ECDH_P256_CMAC_AES128_AES_CCM`

**提示（Prompt）**：带外认证的 CMAC AES128 支持（CMAC AES128 for OOB authentication）

**说明（Help）**

启用后，支持将 CMAC AES128 用于带外认证（OOB authentication）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PROV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:348`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L348)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MESH_PROV`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_ECDH_P256_HMAC_SHA256_AES_CCM"></a>

## 328.43 `CONFIG_BT_MESH_ECDH_P256_HMAC_SHA256_AES_CCM`

**提示（Prompt）**：带外认证的 HMAC SHA256 支持（HMAC SHA256 for OOB authentication）

**说明（Help）**

启用后，支持将 HMAC SHA256 用于带外认证（OOB authentication）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PROV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:355`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L355)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MESH_PROV`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_FRIEND"></a>

## 328.44 `CONFIG_BT_MESH_FRIEND`

**提示（Prompt）**：作为友谊节点运行的支持（acting as a Friend Node）

**说明（Help）**

启用后，允许设备作为友谊节点（Friend Node）运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1746`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1746)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_FRIEND_ADV_LATENCY"></a>

## 328.45 `CONFIG_BT_MESH_FRIEND_ADV_LATENCY`

**提示（Prompt）**：启用广播的延迟（Latency for enabling advertising）

**说明（Help）**

从请求 Friend 广播到实际开始广播之间的延迟，单位为毫秒。用于调节 `ReceiveDelay`，让友谊节点（Friend）提前开始发送消息，以补偿从消息交给蓝牙主机到广播实际启动之间的时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_FRIEND && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1802`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1802)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 作为友谊节点运行的支持（acting as a Friend Node）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_FRIEND`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_FRIEND)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_FRIEND_ENABLED"></a>

## 328.46 `CONFIG_BT_MESH_FRIEND_ENABLED`

**提示（Prompt）**：默认启用友谊功能（Friend feature enabled by default）

**说明（Help）**

控制设备首次启动或未配网（unprovisioned）时，是否默认启用友谊功能（Friend feature）。可在运行时使用 `bt_mesh_friend_set()` 更改。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_FRIEND && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1753`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1753)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 作为友谊节点运行的支持（acting as a Friend Node）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_FRIEND`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_FRIEND)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_FRIEND_LPN_COUNT"></a>

## 328.47 `CONFIG_BT_MESH_FRIEND_LPN_COUNT`

**提示（Prompt）**：支持的低功耗节点数量（Number of supported LPN nodes）

**说明（Help）**

友谊节点（Friend）可以同时建立友谊关系（Friendship）的低功耗节点（Low Power Nodes）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_FRIEND && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 1000]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1784`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1784)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 作为友谊节点运行的支持（acting as a Friend Node）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_FRIEND`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_FRIEND)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_FRIEND_QUEUE_SIZE"></a>

## 328.48 `CONFIG_BT_MESH_FRIEND_QUEUE_SIZE`

**提示（Prompt）**：每个友谊队列支持的最小缓冲区数量（Minimum buffers per Friend Queue）

**说明（Help）**

每个本地友谊队列（Friend Queue）可用于存储的最小缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_FRIEND && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[2, 65536]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1768`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1768)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 作为友谊节点运行的支持（acting as a Friend Node）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_FRIEND`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_FRIEND)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_FRIEND_RECV_WIN"></a>

## 328.49 `CONFIG_BT_MESH_FRIEND_RECV_WIN`

**提示（Prompt）**：友谊节点接收窗口（Friend Receive Window）

**说明（Help）**

友谊节点（Friend node）支持的接收窗口（Receive Window），单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_FRIEND && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
255
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1761`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1761)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 作为友谊节点运行的支持（acting as a Friend Node）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_FRIEND`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_FRIEND)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_FRIEND_SEG_RX"></a>

## 328.50 `CONFIG_BT_MESH_FRIEND_SEG_RX`

**提示（Prompt）**：每个低功耗节点的不完整分段列表数量（incomplete segment lists per LPN）

**说明（Help）**

对于本节点为之提供友谊服务的每个低功耗节点（LPN），跟踪的不完整分段列表（incomplete segment lists）数量。换言之，它决定消息进入友谊队列（Friend queue）时，可以同时从多少个元素（elements）接收分段消息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_FRIEND && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 1000]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1792`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1792)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 作为友谊节点运行的支持（acting as a Friend Node）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_FRIEND`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_FRIEND)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_FRIEND_SUB_LIST_SIZE"></a>

## 328.51 `CONFIG_BT_MESH_FRIEND_SUB_LIST_SIZE`

**提示（Prompt）**：友谊订阅列表大小（Friend Subscription List Size）

**说明（Help）**

友谊节点（Friend node）可为一个低功耗节点（Low Power node）支持的订阅列表（Subscription List）大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_FRIEND && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 1023]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1776`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1776)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 作为友谊节点运行的支持（acting as a Friend Node）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_FRIEND`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_FRIEND)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_GATT_PROXY"></a>

## 328.52 `CONFIG_BT_MESH_GATT_PROXY`

**提示（Prompt）**：GATT 代理服务支持（GATT Proxy Service support）

**说明（Help）**

启用 Mesh GATT 代理服务（Proxy Service）支持，即能够在 Mesh GATT 客户端与 Mesh 网络之间充当代理（proxy）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_MESH_GATT_SERVER
CONFIG_BT_MESH_PROXY
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1440`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1440)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 代理（Proxy）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_GATT_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT_SERVER)、[`CONFIG_BT_MESH_PROXY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROXY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_MESH_GATT_SERVER`、`CONFIG_BT_MESH_PROXY`。

<a id="CONFIG_BT_MESH_GATT_PROXY_ENABLED"></a>

## 328.53 `CONFIG_BT_MESH_GATT_PROXY_ENABLED`

**提示（Prompt）**：默认启用 GATT 代理（GATT Proxy enabled）

**说明（Help）**

控制是否默认启用 GATT 代理（GATT Proxy）功能，可以通过运行时配置更改。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_GATT_PROXY && CONFIG_BT_MESH_GATT_PROXY && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1451`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1451)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 代理（Proxy） → GATT 代理服务支持（GATT Proxy Service support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_GATT_PROXY`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_GATT_PROXY)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_HEALTH_CLI"></a>

## 328.54 `CONFIG_BT_MESH_HEALTH_CLI`

**提示（Prompt）**：健康客户端模型支持（Health Client Model）

**说明（Help）**

启用健康客户端模型（health client model）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:920`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L920)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_HEALTH_CLI_TIMEOUT"></a>

## 328.55 `CONFIG_BT_MESH_HEALTH_CLI_TIMEOUT`

**提示（Prompt）**：健康客户端模型超时，单位为毫秒（Health Client model timeout）

**说明（Help）**

此超时控制健康客户端（health client）等待响应消息到达的时间，可在运行时通过 `bt_mesh_health_cli_timeout_set` 更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_HEALTH_CLI && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2000
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:927`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L927)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 健康客户端模型支持（Health Client Model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_HEALTH_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_HEALTH_CLI)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_IVU_DIVIDER"></a>

## 328.56 `CONFIG_BT_MESH_IVU_DIVIDER`

**提示（Prompt）**：IV 更新状态刷新定时器的分割数（Divider for IV Update state refresh timer）

**说明（Help）**

当 IV 更新状态进入正常运行（Normal operation）或 IV 更新进行中（IV Update in Progress）时，需要跟踪在该状态下已经经过多少小时，因为规范要求至少维持 `96` 小时；其中“更新进行中”还具有 `144` 小时的上限。

为在节点偶尔断电的情况下也满足该要求，需要持久化存储节点在该状态下经过的小时数。由于持续时间允许一定范围，不必每小时都存储一次。具体频率很大程度上取决于节点的使用方式和电源类型。

没有适合所有情况的最佳值，因此此选项允许指定分割数（divider），即把最短的 96 小时划分成多少个间隔。每个间隔结束后，将节点在当前状态下的持续时间保存到 Flash。例如，默认值 `4` 表示每 `24` 小时保存一次状态（`96 / 4`）。

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
[2, 96]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1577`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1577)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → IV 索引与序列号（IV Index & Sequence number）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_IV_UPDATE_SEQ_LIMIT"></a>

## 328.57 `CONFIG_BT_MESH_IV_UPDATE_SEQ_LIMIT`

**提示（Prompt）**：启动 IV 更新的序列号阈值（Sequence number limit to start IV update）

**说明（Help）**

指定启动初始化向量更新（IV update）的序列号值（sequence number value）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x800000
```

**取值范围（Ranges）**

```text
[0x000001, 0xFFFFFE]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1570`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1570)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → IV 索引与序列号（IV Index & Sequence number）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_IV_UPDATE_TEST"></a>

## 328.58 `CONFIG_BT_MESH_IV_UPDATE_TEST`

**提示（Prompt）**：测试 IV 更新过程（Test the IV Update Procedure）

**说明（Help）**

移除 IV 更新过程（IV Update Procedure）的 `96` 小时限制，允许随时改变状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1564`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1564)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → IV 索引与序列号（IV Index & Sequence number）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LABEL_COUNT"></a>

## 328.59 `CONFIG_BT_MESH_LABEL_COUNT`

**提示（Prompt）**：用于虚拟地址的标签 UUID 最大数量（Label UUIDs for Virtual Addresses）

**说明（Help）**

指定可存储的标签 UUID（Label UUIDs）数量。

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
[0, 4096]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1849`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1849)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 能力（Capabilities）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LARGE_COMP_DATA_CLI"></a>

## 328.60 `CONFIG_BT_MESH_LARGE_COMP_DATA_CLI`

**提示（Prompt）**：大型组成数据客户端模型支持（Large Composition Data Client model）

**说明（Help）**

启用大型组成数据客户端模型（Large Composition Data Client model）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1323`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1323)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LARGE_COMP_DATA_SRV"></a>

## 328.61 `CONFIG_BT_MESH_LARGE_COMP_DATA_SRV`

**提示（Prompt）**：大型组成数据服务器模型支持（Large Composition Data Server Model）

**说明（Help）**

启用大型组成数据服务器模型（Large Composition Data Server model）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_MODEL_EXTENSIONS && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1306`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1306)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_MODEL_EXTENSIONS`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_MODEL_EXTENSIONS)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LOOPBACK_BUFS"></a>

## 328.62 `CONFIG_BT_MESH_LOOPBACK_BUFS`

**提示（Prompt）**：回环缓冲区数量（Number of loopback buffers）

**说明（Help）**

为网络回环机制（network loopback mechanism）分配的缓冲区数量。设备向自身发送消息时使用回环（loopback）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:431`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L431)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 网络层（Network layer）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LOW_POWER"></a>

## 328.63 `CONFIG_BT_MESH_LOW_POWER`

**提示（Prompt）**：低功耗功能支持（Support for Low Power features）

**说明（Help）**

启用后，允许设备作为低功耗节点（Low Power Node）运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1605`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1605)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LPN_AUTO"></a>

## 328.64 `CONFIG_BT_MESH_LPN_AUTO`

**提示（Prompt）**：配网完成后自动寻找友谊节点（Friend nodes）

**说明（Help）**

配网（provisioning）完成后自动启用低功耗节点（LPN）功能，并开始寻找友谊节点（Friend nodes）。禁用时，需要调用 `bt_mesh_lpn_set(true)` 手动启用 LPN 模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LOW_POWER && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1635`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1635)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 低功耗功能支持（Support for Low Power features）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LOW_POWER)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LPN_AUTO_TIMEOUT"></a>

## 328.65 `CONFIG_BT_MESH_LPN_AUTO_TIMEOUT`

**提示（Prompt）**：从最后收到消息到进入 LPN 模式的时间（Time before going to LPN mode）

**说明（Help）**

节点从收到最后一条消息开始，到开始寻找友谊节点（Friend nodes）之前的等待时间，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LPN_AUTO && CONFIG_BT_MESH_LOW_POWER && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
15
```

**取值范围（Ranges）**

```text
[0, 3600]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1643`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1643)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 低功耗功能支持（Support for Low Power features） → 配网完成后自动寻找友谊节点（Friend nodes）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LPN_AUTO`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LPN_AUTO)、[`CONFIG_BT_MESH_LOW_POWER`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LOW_POWER)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LPN_ESTABLISHMENT"></a>

## 328.66 `CONFIG_BT_MESH_LPN_ESTABLISHMENT`

**提示（Prompt）**：以低功耗方式建立友谊关系（Friendship establishment using low power）

**说明（Help）**

通过降低扫描占空比（scan duty cycle），以低功耗方式建立友谊关系（Friendship）。缺点是，在成功与友谊节点（Friend node）建立关系之前，节点可能漏掉发给自己的消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LOW_POWER && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1612`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1612)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 低功耗功能支持（Support for Low Power features）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LOW_POWER)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LPN_GROUPS"></a>

## 328.67 `CONFIG_BT_MESH_LPN_GROUPS`

**提示（Prompt）**：低功耗节点可订阅的组数量（Number of groups the LPN can subscribe to）

**说明（Help）**

低功耗节点（LPN）可订阅的最大组（groups）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LOW_POWER && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[0, 16384]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1731`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1731)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 低功耗功能支持（Support for Low Power features）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LOW_POWER)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LPN_INIT_POLL_TIMEOUT"></a>

## 328.68 `CONFIG_BT_MESH_LPN_INIT_POLL_TIMEOUT`

**提示（Prompt）**：PollTimeout 定时器起始值（starting value of the PollTimeout timer）

**说明（Help）**

首次建立友谊关系（Friendship）时 `PollTimeout` 定时器的初始值。此后，超时值会逐步增长至实际的 `PollTimeout`，每次迭代加倍。值以 `100` 毫秒为单位，例如 `300` 表示 `30` 秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LOW_POWER && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_LPN_POLL_TIMEOUT
```

**取值范围（Ranges）**

```text
[10, CONFIG_BT_MESH_LPN_POLL_TIMEOUT]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1711`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1711)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 低功耗功能支持（Support for Low Power features）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LOW_POWER)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_LPN_POLL_TIMEOUT`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LPN_POLL_TIMEOUT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LPN_MIN_QUEUE_SIZE"></a>

## 328.69 `CONFIG_BT_MESH_LPN_MIN_QUEUE_SIZE`

**提示（Prompt）**：可接受的友谊队列最小大小（MinQueueSizeLog）

**说明（Help）**

`MinQueueSizeLog` 字段定义为 `log_2(N)`，其中 `N` 是友谊节点（Friend node）的友谊队列（Friend Queue）至少能够存储的、最大大小的下层传输 PDU（Lower Transport PDUs）数量。例如，`MinQueueSizeLog` 为 `1` 时，`N = 2`；为 `7` 时，`N = 128`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LOW_POWER && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 7]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1676`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1676)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 低功耗功能支持（Support for Low Power features）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LOW_POWER)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LPN_OFFER_WAIT_TIMEOUT"></a>

## 328.70 `CONFIG_BT_MESH_LPN_OFFER_WAIT_TIMEOUT`

**提示（Prompt）**：发送 Friend Request 后等待 Friend Offer 的时间（Time to wait for Friend Offers）

**说明（Help）**

低功耗节点（Low Power node）等待友谊提议消息（Friend Offer messages）的时间，单位为毫秒，从发送友谊请求（Friend Request）后 `100 ms` 开始计时。蓝牙 Mesh 协议规范建议最多监听 `1` 秒。

启用 `BT_MESH_LPN_ESTABLISHMENT` 时，该值也表示扫描器保持启用的时长。如果没有收到可接受的 Friend Offer，将在 `BT_MESH_LPN_RETRY_TIMEOUT` 之后发送下一个 Friend Request。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LOW_POWER && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1000
```

**取值范围（Ranges）**

```text
[100, 10000]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1622`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1622)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 低功耗功能支持（Support for Low Power features）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LOW_POWER)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LPN_POLL_TIMEOUT"></a>

## 328.71 `CONFIG_BT_MESH_LPN_POLL_TIMEOUT`

**提示（Prompt）**：PollTimeout 定时器值（value of the PollTimeout timer）

**说明（Help）**

`PollTimeout` 定时器测量低功耗节点（Low Power node）连续发送的两个请求之间的时间。如果定时器到期前友谊节点（Friend node）没有收到请求，则认为友谊关系（friendship）已经终止。值以 `100` 毫秒为单位，例如 `300` 表示 `30` 秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LOW_POWER && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
300
```

**取值范围（Ranges）**

```text
[10, 244735]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1699`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1699)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 低功耗功能支持（Support for Low Power features）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LOW_POWER)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LPN_RECV_DELAY"></a>

## 328.72 `CONFIG_BT_MESH_LPN_RECV_DELAY`

**提示（Prompt）**：本地节点请求的接收延迟（Receive delay requested by the local node）

**说明（Help）**

`ReceiveDelay` 是低功耗节点（Low Power node）发送请求到开始监听响应之间的时间，给友谊节点（Friend node）准备响应留出时间。值以毫秒为单位。使用 `BT_MESH_ADV_LEGACY` 时，受传统广播者实现限制，最小延迟不得低于 `50ms`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LOW_POWER && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[50, 255] if CONFIG_BT_MESH_ADV_LEGACY
[10, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1686`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1686)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 低功耗功能支持（Support for Low Power features）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LOW_POWER)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_ADV_LEGACY`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH_ADV_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LPN_RECV_WIN_FACTOR"></a>

## 328.73 `CONFIG_BT_MESH_LPN_RECV_WIN_FACTOR`

**提示（Prompt）**：Friend Offer Delay 计算所用的接收窗口因子（ReceiveWindowFactor）

**说明（Help）**

所支持的接收窗口（Receive Window）对友谊提议延迟（Friend Offer Delay）计算的贡献系数。编码对应关系为：`0 = 1`、`1 = 1.5`、`2 = 2`、`3 = 2.5`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LOW_POWER && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 3]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1668`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1668)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 低功耗功能支持（Support for Low Power features）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LOW_POWER)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LPN_RETRY_TIMEOUT"></a>

## 328.74 `CONFIG_BT_MESH_LPN_RETRY_TIMEOUT`

**提示（Prompt）**：友谊请求重试超时（Retry timeout for Friend requests）

**说明（Help）**

如果前一次友谊请求（Friend Request）未收到任何可接受的友谊提议（Friend Offers），两次请求之间的间隔，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LOW_POWER && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 3600]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1652`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1652)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 低功耗功能支持（Support for Low Power features）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LOW_POWER)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LPN_RSSI_FACTOR"></a>

## 328.75 `CONFIG_BT_MESH_LPN_RSSI_FACTOR`

**提示（Prompt）**：Friend Offer Delay 计算所用的 RSSI 因子（RSSIFactor）

**说明（Help）**

友谊节点（Friend node）测量的 RSSI 对友谊提议延迟（Friend Offer Delay）计算的贡献系数。编码对应关系为：`0 = 1`、`1 = 1.5`、`2 = 2`、`3 = 2.5`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LOW_POWER && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 3]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1660`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1660)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 低功耗功能支持（Support for Low Power features）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LOW_POWER)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LPN_SCAN_LATENCY"></a>

## 328.76 `CONFIG_BT_MESH_LPN_SCAN_LATENCY`

**提示（Prompt）**：启用扫描的延迟（Latency for enabling scanning）

**说明（Help）**

启用扫描（scanning）所需的延迟，单位为毫秒。实际表示在接收窗口（Receive Window）之前需要提前多久请求启用扫描。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LOW_POWER && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
15
```

**取值范围（Ranges）**

```text
[0, 50]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1722`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1722)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 低功耗功能支持（Support for Low Power features）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LOW_POWER)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_LPN_SUB_ALL_NODES_ADDR"></a>

## 328.77 `CONFIG_BT_MESH_LPN_SUB_ALL_NODES_ADDR`

**提示（Prompt）**：自动订阅所有节点地址（Automatically subscribe all nodes address）

**说明（Help）**

建立友谊关系（friendship）后，自动订阅所有节点地址（all nodes address）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LOW_POWER && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1738`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1738)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 低功耗功能支持（Support for Low Power features）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LOW_POWER)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_MAX_CONN"></a>

## 328.78 `CONFIG_BT_MESH_MAX_CONN`

**提示（Prompt）**：最大同时蓝牙连接数（Maximum number of simultaneous Bluetooth connections）

**说明（Help）**

蓝牙 Mesh 协议栈可同时使用的蓝牙连接（Bluetooth connections）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MAX_CONN
```

**取值范围（Ranges）**

```text
[1, CONFIG_BT_MAX_CONN]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1957`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1957)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MAX_CONN`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MAX_CONN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_MODELS_METADATA_PAGE_LEN"></a>

## 328.79 `CONFIG_BT_MESH_MODELS_METADATA_PAGE_LEN`

**提示（Prompt）**：模型元数据页最大长度（Maximum length of the Models Metadata Page）

**说明（Help）**

此值为设备上全部模型（models）的元数据（metadata）总长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_LARGE_COMP_DATA_SRV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
150
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1314`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1314)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 大型组成数据服务器模型支持（Large Composition Data Server Model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LARGE_COMP_DATA_SRV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_LARGE_COMP_DATA_SRV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_MODEL_EXTENSIONS"></a>

## 328.80 `CONFIG_BT_MESH_MODEL_EXTENSIONS`

**提示（Prompt）**：模型扩展支持（Support for Model extensions）

**说明（Help）**

启用模型扩展（model extension）概念支持，使接入层（Access layer）能够获知 Mesh 模型之间的关系。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:806`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L806)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 访问层（Access layer）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_MODEL_EXTENSION_LIST_SIZE"></a>

## 328.81 `CONFIG_BT_MESH_MODEL_EXTENSION_LIST_SIZE`

**提示（Prompt）**：模型扩展列表大小（Model extensions list size）

**说明（Help）**

指定可保存的模型关系（model relations）数量，等于 `bt_mesh_model_extend` 与 `bt_mesh_model_correspond` 的调用次数总和。该信息用于构建组成数据页 1（Composition Data Page 1）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_COMP_PAGE_1 && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0 if !CONFIG_BT_MESH_MODEL_EXTENSIONS
10
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:818`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L818)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 访问层（Access layer） → 组成数据页 1 支持（Composition Data Page 1）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_COMP_PAGE_1`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_COMP_PAGE_1)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_MODEL_EXTENSIONS`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_MODEL_EXTENSIONS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_MODEL_GROUP_COUNT"></a>

## 328.82 `CONFIG_BT_MESH_MODEL_GROUP_COUNT`

**提示（Prompt）**：每个模型的组地址订阅最大数量（group address subscriptions per model）

**说明（Help）**

指定每个模型最多可订阅的组地址（group addresses）数量。

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

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1841`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1841)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 能力（Capabilities）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_MODEL_KEY_COUNT"></a>

## 328.83 `CONFIG_BT_MESH_MODEL_KEY_COUNT`

**提示（Prompt）**：每个模型的应用密钥最大数量（application keys per model）

**说明（Help）**

指定每个模型最多可绑定的应用密钥（application keys）数量。

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

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1833`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1833)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 能力（Capabilities）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_MODEL_VND_MSG_CID_FORCE"></a>

## 328.84 `CONFIG_BT_MESH_MODEL_VND_MSG_CID_FORCE`

**提示（Prompt）**：强制厂商模型使用 CID 匹配的操作码（opcodes with matching CID）[已弃用，DEPRECATED]

**说明（Help）**

强制厂商模型（vendor models）只使用 CID 字段与模型 CID 匹配的操作码（opcodes）。此选项已弃用，不应继续使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:799`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L799)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 访问层（Access layer）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_MSG_CACHE_SIZE"></a>

## 328.85 `CONFIG_BT_MESH_MSG_CACHE_SIZE`

**提示（Prompt）**：网络消息缓存大小（Network message cache size）

**说明（Help）**

节点缓存的消息数量，用于避免再次处理最近见过的重复消息。此选项与重放保护列表（replay protection list）相似，但目的不同。网络消息缓存（network message cache）帮助避免不必要的解密操作和中继，并消除中继环路（relay loops）。

设得过小可能造成不必要的网络流量；设得过大则可能增加每个接收网络 PDU 的处理时间，并按比例增加 RAM 占用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[2, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:456`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L456)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 网络层（Network layer）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_NETWORK_TRANSMIT_COUNT"></a>

## 328.86 `CONFIG_BT_MESH_NETWORK_TRANSMIT_COUNT`

**提示（Prompt）**：网络发送次数（Network Transmit Count）

**说明（Help）**

控制原始消息在首次发送之外的初始重传次数（retransmissions），可以通过运行时配置更改。

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
[0, 7]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:438`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L438)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 网络层（Network layer）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_NETWORK_TRANSMIT_INTERVAL"></a>

## 328.87 `CONFIG_BT_MESH_NETWORK_TRANSMIT_INTERVAL`

**提示（Prompt）**：网络发送间隔（Network Transmit Interval）

**说明（Help）**

控制原始消息重传之间的初始间隔，单位为毫秒，可以通过运行时配置更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[10, 330]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:447`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L447)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 网络层（Network layer）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_NODE_ID_TIMEOUT"></a>

## 328.88 `CONFIG_BT_MESH_NODE_ID_TIMEOUT`

**提示（Prompt）**：节点身份广播超时（Node Identity advertising timeout）

**说明（Help）**

决定本地节点使用节点身份（Node Identity）进行广播的持续时间，单位为秒。规范限制为 `60` 秒，并暗示该值也是合适的取值，因此保留默认值最稳妥。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_GATT_PROXY && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
60
```

**取值范围（Ranges）**

```text
[1, 60]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1459`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1459)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 代理（Proxy） → GATT 代理服务支持（GATT Proxy Service support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_GATT_PROXY`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_GATT_PROXY)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_OD_PRIV_PROXY_CLI"></a>

## 328.89 `CONFIG_BT_MESH_OD_PRIV_PROXY_CLI`

**提示（Prompt）**：按需私有代理客户端模型支持（On-Demand Private Proxy Client model）

**说明（Help）**

按需私有代理客户端（On-Demand Private Proxy Client）可配置和查询按需私有代理服务器（Servers）的状态。该状态决定对端在收到请求 PDU（Solicitation PDU）后，是否广播私有网络身份类型（Private Network Identity type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1343`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1343)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT"></a>

## 328.90 `CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT`

**提示（Prompt）**：Solicitation PDU 重放保护列表配置客户端模型超时，单位为毫秒（Solicitation PDU RPL Configuration Client）

**说明（Help）**

此超时控制按需私有代理客户端（On-Demand Private Proxy Client）等待响应消息到达的时间，可在运行时通过 `bt_mesh_od_priv_proxy_cli_timeout_set` 更改。

译注：原提示文本使用 `Solicitation PDU RPL Configuration Client`，帮助正文及 API 则指向 `On-Demand Private Proxy Client`；此处保留原文差异。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_OD_PRIV_PROXY_CLI && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1351`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1351)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 按需私有代理客户端模型支持（On-Demand Private Proxy Client model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_OD_PRIV_PROXY_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_OD_PRIV_PROXY_CLI)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_OD_PRIV_PROXY_SRV"></a>

## 328.91 `CONFIG_BT_MESH_OD_PRIV_PROXY_SRV`

**提示（Prompt）**：按需私有代理服务器模型支持（On-Demand Private Proxy Server model）

**说明（Help）**

按需私有代理服务器（On-Demand Private Proxy Server）支持配置节点以私有网络身份类型（Private Network Identity type）进行广播。启用时也会启用请求 PDU 重放保护列表配置服务器模型（Solicitation PDU RPL Configuration Server model）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PRIV_BEACON_SRV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_MESH_SOLICITATION
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1360`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1360)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PRIV_BEACON_SRV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PRIV_BEACON_SRV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_SOLICITATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SOLICITATION)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_MESH_SOLICITATION`。

<a id="CONFIG_BT_MESH_OOB_AUTH_REQUIRED"></a>

## 328.92 `CONFIG_BT_MESH_OOB_AUTH_REQUIRED`

**提示（Prompt）**：带外认证强制使用 HMAC SHA256（OOB authentication mandates HMAC SHA256）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_ECDH_P256_HMAC_SHA256_AES_CCM && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:362`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L362)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning） → 带外认证的 HMAC SHA256 支持（HMAC SHA256 for OOB authentication）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ECDH_P256_HMAC_SHA256_AES_CCM`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_ECDH_P256_HMAC_SHA256_AES_CCM)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_OP_AGG_CLI"></a>

## 328.93 `CONFIG_BT_MESH_OP_AGG_CLI`

**提示（Prompt）**：操作码聚合器客户端模型支持（Opcode Aggregator Client Model）

**说明（Help）**

启用操作码聚合器客户端模型（Opcode Aggregator Client model）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_MESH_OP_AGG
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1288`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1288)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_OP_AGG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_OP_AGG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_MESH_OP_AGG`。

<a id="CONFIG_BT_MESH_OP_AGG_CLI_TIMEOUT"></a>

## 328.94 `CONFIG_BT_MESH_OP_AGG_CLI_TIMEOUT`

**提示（Prompt）**：操作码聚合器客户端模型超时，单位为毫秒（Opcodes Aggregator Client model timeout）

**说明（Help）**

此超时控制操作码聚合器客户端（Opcodes Aggregator Client）等待响应消息到达的时间，可在运行时通过 `bt_mesh_op_agg_cli_timeout_set` 更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_OP_AGG_CLI && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
10000
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1296`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1296)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models） → 操作码聚合器客户端模型支持（Opcode Aggregator Client Model）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_OP_AGG_CLI`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_OP_AGG_CLI)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_OP_AGG_SRV"></a>

## 328.95 `CONFIG_BT_MESH_OP_AGG_SRV`

**提示（Prompt）**：操作码聚合器服务器模型支持（Opcode Aggregator Server Model）

**说明（Help）**

启用操作码聚合器服务器模型（Opcode Aggregator Server model）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_MESH_OP_AGG
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:1282`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L1282)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 模型（Models）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_OP_AGG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_OP_AGG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_MESH_OP_AGG`。

<a id="CONFIG_BT_MESH_PB_ADV"></a>

## 328.96 `CONFIG_BT_MESH_PB_ADV`

**提示（Prompt）**：广播承载配网支持（PB-ADV support）

**说明（Help）**

启用后，允许通过广播承载（advertising bearer）为设备配网（provisioned）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_MESH_PROV
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:241`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L241)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_PROV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_MESH_PROV`。

<a id="CONFIG_BT_MESH_PB_ADV_LINK_CLOSE_RETRANSMIT_COUNT"></a>

## 328.97 `CONFIG_BT_MESH_PB_ADV_LINK_CLOSE_RETRANSMIT_COUNT`

**提示（Prompt）**：Link Close 重传次数（Link Close retransmit count）

**说明（Help）**

控制原始链路关闭（Link Close）消息在首次发送之外的重传次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PB_ADV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
7 if CONFIG_BT_MESH_PB_ADV_USE_RELAY_SETS
2
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:283`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L283)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning） → 广播承载配网支持（PB-ADV support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PB_ADV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_PB_ADV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_PB_ADV_USE_RELAY_SETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PB_ADV_USE_RELAY_SETS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_PB_ADV_RETRANS_TIMEOUT"></a>

## 328.98 `CONFIG_BT_MESH_PB_ADV_RETRANS_TIMEOUT`

**提示（Prompt）**：配网 PDU 重传超时（Timeout of retransmit provisioning PDUs）

**说明（Help）**

配网 PDU（provisioning PDUs）重传的超时值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PB_ADV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
500
```

**取值范围（Ranges）**

```text
[100, 800]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:292`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L292)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning） → 广播承载配网支持（PB-ADV support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PB_ADV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_PB_ADV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_PB_ADV_TRANS_ACK_RETRANSMIT_COUNT"></a>

## 328.99 `CONFIG_BT_MESH_PB_ADV_TRANS_ACK_RETRANSMIT_COUNT`

**提示（Prompt）**：Link Ack 与 Transaction Ack 重传次数（retransmit count）

**说明（Help）**

控制原始链路确认（Link Ack）及事务确认（Transaction Acknowledgment）PDU 在首次发送之外的重传次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PB_ADV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:275`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L275)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning） → 广播承载配网支持（PB-ADV support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PB_ADV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_PB_ADV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MESH_PB_ADV_TRANS_PDU_RETRANSMIT_COUNT"></a>

## 328.100 `CONFIG_BT_MESH_PB_ADV_TRANS_PDU_RETRANSMIT_COUNT`

**提示（Prompt）**：Link Open 与 Transaction PDU 重传次数（retransmit count）

**说明（Help）**

控制原始链路打开（Link Open）与事务（Transaction）PDU 在首次发送之外的重传次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MESH_PB_ADV && CONFIG_BT_MESH && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
7 if CONFIG_BT_MESH_PB_ADV_USE_RELAY_SETS
0
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../mesh/Kconfig:266`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../mesh/Kconfig#L266)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙 Mesh 支持（Bluetooth Mesh support） → 配网（Provisioning） → 广播承载配网支持（PB-ADV support）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PB_ADV`](P328_subsys_bluetooth_配置项参考_9.md#CONFIG_BT_MESH_PB_ADV)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_PB_ADV_USE_RELAY_SETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PB_ADV_USE_RELAY_SETS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<!-- kconfig-navigation -->

[上一章](P327_subsys_bluetooth_配置项参考_8.md) · [返回大纲](大纲.md) · [下一章](P329_subsys_bluetooth_配置项参考_10.md)
