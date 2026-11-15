---
id: learning.zephyr-docs.bluetooth.page-96
title: MeshSAR配置客户端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/sar_cfg_cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="sar-configuration-client"></a>

<a id="bluetooth-mesh-sar-cfg-cli"></a>

# 第96章\_SAR 配置客户端（SAR Configuration Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/sar_cfg_cli.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：发送端和接收端状态分别管理分段发送与确认／重组行为。本客户端通过网络配置远端节点，读取或设置成功不等于应用消息已可靠交付，业务层仍须按自己的模型处理结果。

SAR 配置客户端是 Bluetooth Mesh 规范定义的基础模型。该模型可选，通过 [`CONFIG_BT_MESH_SAR_CFG_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_CFG_CLI) 启用。

该模型在《Bluetooth Mesh Protocol Specification》1.1 版引入，用于配置支持 SAR 配置服务端的节点的下传输层行为。 相关链接：[SAR 配置服务端（SAR Configuration Server）](P097_MeshSAR配置服务端.md#bluetooth-mesh-sar-cfg-srv)。

客户端可发送 SAR 配置消息，查询或更改服务端支持的 SAR 发送端和 SAR 接收端状态。

SAR 发送端过程用于查询和配置服务端的发送端状态，分别调用 [`bt_mesh_sar_cfg_cli_transmitter_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga893ef5861708bec12f87b9f9cc64b9fc) 和 [`bt_mesh_sar_cfg_cli_transmitter_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga32e2a580b24a41761911e88413e9664e) 读取、设置目标节点状态。

SAR 接收端过程用于查询和配置服务端的接收端状态，分别调用 [`bt_mesh_sar_cfg_cli_receiver_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga444c99254ef2ccdd10dac08a94219d79) 和 [`bt_mesh_sar_cfg_cli_receiver_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga884025b2baf8559950ba6dc83e9ef486) 读取、设置目标节点状态。

两种状态的详情见 SAR 状态章节。 相关链接：[SAR 状态（SAR states）](P095_Mesh分段与重组.md#bt-mesh-sar-cfg-states)。

元素可随时发送 SAR 配置客户端消息，查询或更改对端服务端模型支持的状态。SAR 配置客户端仅接受用目标 SAR 配置服务端所在节点的设备密钥加密的消息。

若存在 SAR 配置客户端模型，只能在主元素上实例化。

<a id="api-reference"></a>

## 96.1 API 参考（API reference）

[Bluetooth Mesh SAR 配置客户端模型（Bluetooth Mesh SAR Configuration Client Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/sar_cfg_cli.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/sar_cfg_cli.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/sar_cfg_cli.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh分段与重组](P095_Mesh分段与重组.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：MeshSAR配置服务端](P097_MeshSAR配置服务端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P095_Mesh分段与重组.md) · [返回大纲](大纲.md) · [下一章](P097_MeshSAR配置服务端.md)

</details>

<!-- reading-navigation:end -->
