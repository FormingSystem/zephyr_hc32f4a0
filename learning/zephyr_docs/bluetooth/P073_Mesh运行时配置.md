---
id: learning.zephyr-docs.bluetooth.page-73
title: Mesh运行时配置
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="runtime-configuration"></a>

<a id="bluetooth-mesh-cfg"></a>

# 第73章\_运行时配置（Runtime Configuration）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/cfg.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：本地运行时配置用于当前节点的约束处理；配置客户端则管理远端节点。配网前改动不会自动成为持久化的网络配置，不能用本页接口替代完整配网及配置流程。

运行时配置 API 允许应用直接改变自身运行时配置，无须经过配置模型。

Bluetooth Mesh 节点通常应由带配置客户端模型的集中式网络配置器设备配置。每个节点实例化配置服务端模型，客户端与之通信以修改节点配置。有些情况下，节点无法依靠客户端发现或判断本地约束，例如电池电量低或拓扑变化；此时可通过本 API 在本地修改配置。 相关链接：[配置客户端（Configuration Client）](P076_Mesh配置客户端.md#bluetooth-mesh-models-cfg-cli)；[配置服务端（Configuration Server）](P077_Mesh配置服务端.md#bluetooth-mesh-models-cfg-srv)。

注意（Note）

节点配网之前进行的运行时配置更改不会写入[持久化存储](P066_Mesh核心.md#bluetooth-mesh-persistent-storage)。

<a id="api-reference"></a>

## 73.1 API 参考（API reference）

[运行时配置（Runtime Configuration）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/cfg.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/cfg.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/cfg.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh心跳](P072_Mesh心跳.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh配置数据库](P074_Mesh配置数据库.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P072_Mesh心跳.md) · [返回大纲](大纲.md) · [下一章](P074_Mesh配置数据库.md)

</details>

<!-- reading-navigation:end -->
