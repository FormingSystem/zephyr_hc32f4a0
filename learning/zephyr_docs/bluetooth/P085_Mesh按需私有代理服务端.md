---
id: learning.zephyr-docs.bluetooth.page-85
title: Mesh按需私有代理服务端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/od_srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="on-demand-private-proxy-server"></a>

<a id="bluetooth-mesh-od-srv"></a>

# 第85章\_按需私有代理服务端（On-Demand Private Proxy Server）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/od_srv.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：本模型负责按需私有代理状态；请求重放保护列表配置服务端（Solicitation PDU RPL Configuration Server）和私有信标服务端（Private Beacon Server）是它的关联模型。启用 Kconfig 后仍应按应用组成数据要求放置模型实例。

按需私有代理服务端是 Bluetooth Mesh 规范定义的基础模型，通过 [`CONFIG_BT_MESH_OD_PRIV_PROXY_SRV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_OD_PRIV_PROXY_SRV) 启用。

该模型在《Bluetooth Mesh Protocol Specification》1.1 版引入，通过管理按需私有 GATT 代理状态，配置接收请求 PDU 的节点如何使用私有网络身份类型广播。

启用该模型时，也会启用请求 PDU 重放保护列表配置服务端。按需私有代理服务端还依赖节点上的私有信标服务端。 相关链接：[请求 PDU 重放保护列表配置服务端（Solicitation PDU RPL Configuration Server）](P087_Mesh请求PDU重放保护列表配置服务端.md#bluetooth-mesh-srpl-srv)；[私有信标服务端（Private Beacon Server）](P083_Mesh私有信标服务端.md#bluetooth-mesh-models-priv-beacon-srv)。

按需私有代理服务端不提供独立控制 API，由按需私有代理客户端控制；它仅接受用本节点设备密钥加密的消息。 相关链接：[按需私有代理客户端（On-Demand Private Proxy Client）](P084_Mesh按需私有代理客户端.md#bluetooth-mesh-od-cli)。

若存在按需私有代理服务端模型，只能在主元素上实例化。

<a id="api-reference"></a>

## 85.1 API 参考（API reference）

[Bluetooth Mesh 按需私有 GATT 代理服务端（Bluetooth Mesh On-Demand Private GATT Proxy Server）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__srv.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/od_srv.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/od_srv.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/od_srv.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh按需私有代理客户端](P084_Mesh按需私有代理客户端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh请求PDU重放保护列表配置客户端](P086_Mesh请求PDU重放保护列表配置客户端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P084_Mesh按需私有代理客户端.md) · [返回大纲](大纲.md) · [下一章](P086_Mesh请求PDU重放保护列表配置客户端.md)

</details>

<!-- reading-navigation:end -->
