---
id: learning.zephyr-docs.bluetooth.page-88
title: Mesh操作码聚合器客户端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/op_agg_cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="opcodes-aggregator-client"></a>

<a id="bluetooth-mesh-models-op-agg-cli"></a>

# 第88章\_操作码聚合器客户端（Opcodes Aggregator Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/op_agg_cli.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：聚合（aggregation）把多条访问层消息放入一个序列。源客户端需要异步接口，使聚合器能够收集请求；使用聚合器不能自动消除目标模型所需的密钥绑定。

操作码聚合器客户端是 Bluetooth Mesh 规范定义的基础模型。该模型可选，通过 [`CONFIG_BT_MESH_OP_AGG_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_OP_AGG_CLI) 启用。

该模型在《Bluetooth Mesh Protocol Specification》1.1 版引入，用于向支持操作码聚合器服务端的节点分发一系列访问层消息（access layer messages）。 相关链接：[操作码聚合器服务端（Opcodes Aggregator Server）](P089_Mesh操作码聚合器服务端.md#bluetooth-mesh-models-op-agg-srv)。

操作码聚合器客户端使用目标节点的设备密钥，或配置客户端配置的应用密钥，与操作码聚合器服务端通信。

若存在操作码聚合器客户端模型，只能在主元素上实例化。

该客户端初始化时隐式绑定到设备密钥；它还应绑定到产生消息序列的各客户端模型所绑定的相同应用密钥。

若要聚合某客户端模型发出的消息，该模型应支持异步 API，例如通过回调完成交互。

<a id="api-reference"></a>

## 88.1 API 参考（API reference）

[操作码聚合器客户端模型（Opcodes Aggregator Client model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/op_agg_cli.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/op_agg_cli.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/op_agg_cli.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh请求PDU重放保护列表配置服务端](P087_Mesh请求PDU重放保护列表配置服务端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh操作码聚合器服务端](P089_Mesh操作码聚合器服务端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P087_Mesh请求PDU重放保护列表配置服务端.md) · [返回大纲](大纲.md) · [下一章](P089_Mesh操作码聚合器服务端.md)

</details>

<!-- reading-navigation:end -->
