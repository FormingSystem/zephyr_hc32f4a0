---
id: learning.zephyr-docs.bluetooth.page-68
title: Mesh模型
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/models.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mesh-models"></a>

<a id="bluetooth-mesh-models"></a>

# 第68章\_Mesh 模型（Mesh models）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/models.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：本页是官方模型目录。各客户端（Client）和服务端（Server）正文、BLOB／DFU 子页以及自动生成 API 分别跟踪；本页翻译完成不代表这些子页均已译完。SAR 表示分段与重组（Segmentation and Reassembly），PDU 表示协议数据单元（Protocol Data Unit），RPL 表示重放保护列表（Replay Protection List）。

<a id="foundation-models"></a>

## 68.1 基础模型（Foundation models）

Bluetooth Mesh 规范定义了基础模型，供网络管理员配置和诊断 Mesh 节点。

- [桥接配置客户端（Bridge Configuration Client）](P093_Mesh桥接配置客户端.md)

- [桥接配置服务端（Bridge Configuration Server）](P094_Mesh桥接配置服务端.md)

- [配置客户端（Configuration Client）](P076_Mesh配置客户端.md)

- [配置服务端（Configuration Server）](P077_Mesh配置服务端.md)

- [健康客户端（Health Client）](P078_Mesh健康客户端.md)

- [健康服务端（Health Server）](P079_Mesh健康服务端.md)

- [大型组成数据客户端（Large Composition Data Client）](P080_Mesh大型组成数据客户端.md)

- [大型组成数据服务端（Large Composition Data Server）](P081_Mesh大型组成数据服务端.md)

- [按需私有代理客户端（On-Demand Private Proxy Client）](P084_Mesh按需私有代理客户端.md)

- [按需私有代理服务端（On-Demand Private Proxy Server）](P085_Mesh按需私有代理服务端.md)

- [操作码聚合器客户端（Opcodes Aggregator Client）](P088_Mesh操作码聚合器客户端.md)

- [操作码聚合器服务端（Opcodes Aggregator Server）](P089_Mesh操作码聚合器服务端.md)

- [私有信标客户端（Private Beacon Client）](P082_Mesh私有信标客户端.md)

- [私有信标服务端（Private Beacon Server）](P083_Mesh私有信标服务端.md)

- [远程配网客户端（Remote Provisioning Client）](P090_Mesh远程配网客户端.md)

- [远程配网服务端（Remote Provisioning Server）](P091_Mesh远程配网服务端.md)

- [SAR 配置客户端（SAR Configuration Client）](P096_MeshSAR配置客户端.md)

- [SAR 配置服务端（SAR Configuration Server）](P097_MeshSAR配置服务端.md)

- [请求 PDU 重放保护列表配置客户端（Solicitation PDU RPL Configuration Client）](P086_Mesh请求PDU重放保护列表配置客户端.md)

- [请求 PDU 重放保护列表配置服务端（Solicitation PDU RPL Configuration Server）](P087_Mesh请求PDU重放保护列表配置服务端.md)

<a id="model-specification-models"></a>

## 68.2 模型规范定义的模型（Model specification models）

除 Bluetooth Mesh 规范定义的基础模型外，《Bluetooth Mesh Model Specification》还定义了多种模型，其中部分已在 Zephyr 中实现：

- [二进制大对象传输模型（BLOB Transfer models）](P098_Mesh大对象传输.md)

- [设备固件更新（Device Firmware Update，DFU）](P102_Mesh设备固件更新.md)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/models.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/models.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/models.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh访问层](P067_Mesh访问层.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh消息](P069_Mesh消息.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P067_Mesh访问层.md) · [返回大纲](大纲.md) · [下一章](P069_Mesh消息.md)

</details>

<!-- reading-navigation:end -->
