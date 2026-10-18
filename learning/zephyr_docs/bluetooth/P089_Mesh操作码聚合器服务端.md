---
id: learning.zephyr-docs.bluetooth.page-89
title: Mesh操作码聚合器服务端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/op_agg_srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="opcodes-aggregator-server"></a>

<a id="bluetooth-mesh-models-op-agg-srv"></a>

# 第89章\_操作码聚合器服务端（Opcodes Aggregator Server）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/op_agg_srv.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：当前实现对响应执行上下文有约束：目标模型处理请求时产生的响应被聚合，延后到另一工作项再回复不在本页描述的支持范围内。

操作码聚合器服务端是 Bluetooth Mesh 规范定义的基础模型。该模型可选，通过 [`CONFIG_BT_MESH_OP_AGG_SRV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_OP_AGG_SRV) 启用。

该模型在《Bluetooth Mesh Protocol Specification》1.1 版引入，用于处理一系列访问层消息。

操作码聚合器服务端接受用本节点设备密钥或应用密钥加密的消息。

若存在操作码聚合器服务端模型，只能在主元素上实例化。

目标服务端模型应绑定到用于加密该访问层消息序列的同一应用密钥。

操作码聚合器服务端处理聚合消息，把它们分发给相应模型及其消息处理函数。当前实现假定响应在接收消息的同一执行上下文中发送，不允许延后发送响应，例如转交工作队列后再发送。

<a id="api-reference"></a>

## 89.1 API 参考（API reference）

[操作码聚合器服务端模型（Opcodes Aggregator Server model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__srv.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/op_agg_srv.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/op_agg_srv.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/op_agg_srv.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh操作码聚合器客户端](P088_Mesh操作码聚合器客户端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh远程配网客户端](P090_Mesh远程配网客户端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P088_Mesh操作码聚合器客户端.md) · [返回大纲](大纲.md) · [下一章](P090_Mesh远程配网客户端.md)

</details>

<!-- reading-navigation:end -->
