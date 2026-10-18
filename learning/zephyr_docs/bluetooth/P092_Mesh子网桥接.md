---
id: learning.zephyr-docs.bluetooth.page-92
title: Mesh子网桥接
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/brg_cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="subnet-bridge"></a>

<a id="bluetooth-mesh-brg-cfg"></a>

# 第92章\_子网桥接（Subnet Bridge）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/brg_cfg.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：子网（subnet）由共享网络密钥定义，不是 IP 子网。子网桥（Subnet Bridge）按表控制跨子网转发；中继（Relay）是相关但不同的功能，正文明确指出桥接可使用中继资源而不启用普通中继功能。

《Bluetooth Mesh Protocol Specification》1.1 版引入了子网桥接功能，使网络能够用子网隔离不同区域，同时允许相邻的不同子网内指定设备安全通信。

此功能允许选定节点作为子网桥（Subnet Bridge），在相邻子网节点之间转发消息，实现受控通信。

子网桥接包含两个模型：

- [桥接配置服务端（Bridge Configuration Server）](P094_Mesh桥接配置服务端.md#bluetooth-mesh-models-brg-cfg-srv)

- [桥接配置客户端（Bridge Configuration Client）](P093_Mesh桥接配置客户端.md#bluetooth-mesh-models-brg-cfg-cli)

支持子网桥接必须实现桥接配置服务端；客户端可选，用于配置其他节点上的子网桥。这两个模型定义了配置和管理桥接所需的状态、消息和行为。

子网桥接的配置和管理由桥接配置服务端和客户端完成。实现客户端模型的节点可作为子网桥接功能的配置管理器（Configuration Manager）。

<a id="concepts"></a>

## 92.1 概念（Concepts）

为更好理解子网桥接及其能力，先介绍几个相关概念。

<a id="subnet"></a>

### 92.1.1 子网（Subnet）

子网是 Mesh 网络中共享同一网络密钥的一组节点，可在网络层安全通信。各子网独立运行，节点在该组内交换消息；一个节点可同时属于多个子网。

<a id="subnet-bridge-node"></a>

### 92.1.2 子网桥节点（Subnet Bridge node）

子网桥节点同时属于多个子网，并启用了桥接功能；只有这样的节点才能执行子网桥接。它跨子网分组转发消息，连接各子网并允许它们通信。

子网桥节点有一个基于主网络密钥（primary NetKey）的主子网，负责 IV 更新过程并把更新传播到其他子网。被转发消息的次级子网称为被桥接子网（bridged subnets）。

<a id="bridging-table"></a>

### 92.1.3 桥接表（Bridging Table）

桥接表保存节点所桥接的子网条目，由桥接配置服务端管理。

桥接表条目数量上限由 [`CONFIG_BT_MESH_BRG_TABLE_ITEMS_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_BRG_TABLE_ITEMS_MAX) 定义，默认取最小值 16，允许的最大值为 255。

<a id="enabling-or-disabling-the-subnet-bridge-feature"></a>

## 92.2 启用或禁用子网桥接（Enabling or disabling the Subnet Bridge feature）

桥接配置客户端或配置管理器调用 [`bt_mesh_brg_cfg_cli_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga6643d4d043af4b0cb30470a5c9a46f38)，向目标节点的桥接配置服务端发送 Subnet Bridge Set 消息，即可启用或禁用桥接。

<a id="adding-or-removing-subnets"></a>

## 92.3 添加或移除子网（Adding or removing subnets）

客户端调用 [`bt_mesh_brg_cfg_cli_table_add()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga8f055e8ee384e8ea4887a56720959b26) 或 [`bt_mesh_brg_cfg_cli_table_remove()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#gabdb919dcf177b8d5c8a28b057469bf18)，向目标服务端发送 Bridging Table Add 或 Bridging Table Remove 消息，添加或移除桥接表条目。

<a id="subnet-bridge-states"></a>

<a id="bluetooth-mesh-brg-cfg-states"></a>

## 92.4 子网桥接状态（Subnet Bridge states）

子网桥接具有以下状态：

- 子网桥接（Subnet Bridge）：表示节点是否启用桥接。客户端调用 [`bt_mesh_brg_cfg_cli_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga6a4507190e425013a9d21ea0a1be1b5c) 向服务端发送 Subnet Bridge Get 消息，即可读取。

- 桥接表（Bridging Table）：保存桥接表内容。客户端调用 [`bt_mesh_brg_cfg_cli_table_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#gacd3811be7b87d2d9187aed6c50945b85) 向目标节点发送 Bridging Table Get 消息，可请求条目列表。

  客户端还可调用 [`bt_mesh_brg_cfg_cli_subnets_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga04bb227d14d4f478e4f32a8ca87d2c38)，向目标服务端发送 Bridged Subnets Get 消息，取得当前桥接的子网列表。

- 桥接表大小（Bridging Table Size）：报告表可容纳的最大条目数。客户端调用 [`bt_mesh_brg_cfg_cli_table_size_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga99951987bd6787e3e1348d8e51e64fe5) 发送 Bridging Table Size Get 消息读取；这是只读状态。

<a id="subnet-bridging-and-replay-protection"></a>

## 92.5 子网桥接与重放保护（Subnet bridging and replay protection）

子网桥接在子网之间转发消息，需要有效的重放保护来保证网络安全。以下说明关键注意事项。

<a id="relay-buffer-considerations"></a>

### 92.5.1 中继缓冲区（Relay buffer considerations）

子网桥转发跨子网消息时，从中继缓冲池分配缓冲区。中继缓冲区数量由 Kconfig 选项 [`CONFIG_BT_MESH_RELAY_BUF_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RELAY_BUF_COUNT) 配置。

启用 [`CONFIG_BT_MESH_ADV_EXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_ADV_EXT) 时，消息通过中继广播集（relay advertising sets）发送，广播集数量由 [`CONFIG_BT_MESH_RELAY_ADV_SETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RELAY_ADV_SETS) 配置。

即使禁用了中继功能 [`CONFIG_BT_MESH_RELAY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RELAY)，仍可使用中继缓冲池和广播集。

<a id="replay-protection-and-bridging-table"></a>

### 92.5.2 重放保护与桥接表（Replay protection and Bridging Table）

子网桥必须对所有发往被桥接子网的访问层消息（Access messages）和传输控制消息（Transport Control messages）实施重放保护。

重放保护列表（Replay Protection List，RPL）与桥接表配合保证安全：

- 对每个获准向被桥接子网发送消息的源地址，子网桥保存其最新 IVISeq。

- 消息的 IVISeq 小于或等于已存值时会被丢弃；有效消息在转发前更新已存 IVISeq。

RPL 与桥接表必须保持同步，因为每条桥接消息在转发前都必须通过重放保护检查。

注意（Note）

RPL 容量应随桥接表增长而调整。被桥接子网增多时，需要跟踪更多源地址和 IVISeq，因此需要更大的 RPL 保持有效保护。

<a id="subnet-bridge-and-directed-forwarding"></a>

## 92.6 子网桥接与定向转发（Subnet Bridge and Directed Forwarding）

Bluetooth Mesh 定向转发（Mesh Directed Forwarding，MDF）通过优化中继路径，提高跨子网节点之间的路由效率。MDF 可通过路径发现和转发增强子网桥接，但当前实现不支持此功能。

<a id="api-reference"></a>

## 92.7 API 参考（API reference）

本节提供桥接配置模型共用的类型和定义。

[桥接配置公共头文件（Bridge Configuration common header）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/brg_cfg.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/brg_cfg.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/brg_cfg.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh远程配网服务端](P091_Mesh远程配网服务端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh桥接配置客户端](P093_Mesh桥接配置客户端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P091_Mesh远程配网服务端.md) · [返回大纲](大纲.md) · [下一章](P093_Mesh桥接配置客户端.md)

</details>

<!-- reading-navigation:end -->
