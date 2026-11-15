---
id: learning.zephyr-docs.bluetooth.page-87
title: Mesh请求PDU重放保护列表配置服务端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/srpl_srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="solicitation-pdu-rpl-configuration-server"></a>

<a id="bluetooth-mesh-srpl-srv"></a>

# 第87章\_请求 PDU 重放保护列表配置服务端（Solicitation PDU RPL Configuration Server）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/srpl_srv.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：SSRC 是请求源（Solicitation Source），SSEQ 是请求序列号（Solicitation Sequence Number）。保存这对信息可拒绝已经处理的请求；本模型控制的是该列表，不是普通访问消息的全部重放保护状态。

请求 PDU 重放保护列表配置服务端是 Bluetooth Mesh 规范定义的基础模型；节点启用按需私有代理服务端时，会启用本模型。 相关链接：[按需私有代理服务端（On-Demand Private Proxy Server）](P085_Mesh按需私有代理服务端.md#bluetooth-mesh-od-srv)。

该模型在《Bluetooth Mesh Protocol Specification》1.1 版引入，管理设备保存的请求重放保护列表（SRPL）。SRPL 用于拒绝节点已经处理过的请求 PDU。节点成功处理一条有效请求 PDU 后，把其请求源字段 SSRC 和请求序列号字段 SSEQ 存入 SRPL。

本服务端不提供独立控制 API，由对应客户端控制；它仅接受用配置客户端配置的应用密钥加密的消息。 相关链接：[请求 PDU 重放保护列表配置客户端（Solicitation PDU RPL Configuration Client）](P086_Mesh请求PDU重放保护列表配置客户端.md#bluetooth-mesh-srpl-cli)。

若存在该服务端模型，只能在主元素上实例化。

<a id="configurations"></a>

## 87.1 配置（Configurations）

可通过 [`CONFIG_BT_MESH_PROXY_SRPL_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROXY_SRPL_SIZE) 设置该服务端使用的 SRPL 大小。

<a id="api-reference"></a>

## 87.2 API 参考（API reference）

[Bluetooth Mesh 请求 PDU 重放保护列表服务端（Bluetooth Mesh Solicitation PDU RPL Server）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__srv.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/srpl_srv.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/srpl_srv.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/srpl_srv.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh请求PDU重放保护列表配置客户端](P086_Mesh请求PDU重放保护列表配置客户端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh操作码聚合器客户端](P088_Mesh操作码聚合器客户端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P086_Mesh请求PDU重放保护列表配置客户端.md) · [返回大纲](大纲.md) · [下一章](P088_Mesh操作码聚合器客户端.md)

</details>

<!-- reading-navigation:end -->
