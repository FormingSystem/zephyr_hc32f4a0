---
id: learning.zephyr-docs.bluetooth.page-97
title: MeshSAR配置服务端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/sar_cfg_srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="sar-configuration-server"></a>

<a id="bluetooth-mesh-sar-cfg-srv"></a>

# 第97章\_SAR 配置服务端（SAR Configuration Server）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/sar_cfg_srv.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：SAR 配置模型控制 SAR 参数；即使没有该配置服务端，分段重组仍按协议栈配置运行，见[SAR机制](P095_Mesh分段与重组.md)。

SAR 配置服务端是 Bluetooth Mesh 规范定义的基础模型。该模型可选，通过 [`CONFIG_BT_MESH_SAR_CFG_SRV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_CFG_SRV) 启用。

该模型在《Bluetooth Mesh Protocol Specification》1.1 版引入，用于配置节点的分段与重组行为，并定义相应状态和消息。 相关链接：[分段与重组（SAR）](P095_Mesh分段与重组.md#bluetooth-mesh-sar-cfg)。

SAR 配置服务端定义发送端和接收端两种状态，详情见 SAR 状态章节。 相关链接：[SAR 状态（SAR states）](P095_Mesh分段与重组.md#bt-mesh-sar-cfg-states)。

该模型还支持这两种状态的读取（get）和设置（set）消息。

SAR 配置服务端不提供独立控制 API，由 SAR 配置客户端控制；它仅接受用本节点设备密钥加密的消息。 相关链接：[SAR 配置客户端（SAR Configuration Client）](P096_MeshSAR配置客户端.md#bluetooth-mesh-sar-cfg-cli)。

若存在 SAR 配置服务端模型，只能在主元素上实例化。

<a id="api-reference"></a>

## 97.1 API 参考（API reference）

[Bluetooth Mesh SAR 配置服务端模型（Bluetooth Mesh SAR Configuration Server Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__srv.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/sar_cfg_srv.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/sar_cfg_srv.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/sar_cfg_srv.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：MeshSAR配置客户端](P096_MeshSAR配置客户端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh大对象传输](P098_Mesh大对象传输.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P096_MeshSAR配置客户端.md) · [返回大纲](大纲.md) · [下一章](P098_Mesh大对象传输.md)

</details>

<!-- reading-navigation:end -->
