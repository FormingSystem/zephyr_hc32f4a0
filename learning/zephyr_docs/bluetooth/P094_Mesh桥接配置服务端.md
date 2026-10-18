---
id: learning.zephyr-docs.bluetooth.page-94
title: Mesh桥接配置服务端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/brg_cfg_srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bridge-configuration-server"></a>

<a id="bluetooth-mesh-models-brg-cfg-srv"></a>

# 第94章\_桥接配置服务端（Bridge Configuration Server）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/brg_cfg_srv.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：“可选”针对一般 Mesh 节点；要支持子网桥接，则必须包含本模型。它扩展配置服务端，并在主元素上实例化。桥接表大小是容量上限，不是当前已占用条目数。

桥接配置服务端是 Bluetooth Mesh 规范定义的基础模型。该模型可选，通过 [`CONFIG_BT_MESH_BRG_CFG_SRV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_BRG_CFG_SRV) 启用，并扩展配置服务端模型。 相关链接：[配置服务端（Configuration Server）](P077_Mesh配置服务端.md#bluetooth-mesh-models-cfg-srv)。

该模型在《Bluetooth Mesh Protocol Specification》1.1 版引入，用于支持和配置子网桥接功能。

桥接配置服务端由桥接配置客户端配置，仅接受用本节点设备密钥加密的消息。 相关链接：[桥接配置客户端（Bridge Configuration Client）](P093_Mesh桥接配置客户端.md#bluetooth-mesh-models-brg-cfg-cli)。

若存在桥接配置服务端模型，必须在主元素上实例化。

桥接配置服务端提供以下三种状态的访问能力：

- 子网桥接（Subnet Bridge）

- 桥接表（Bridging Table）

- 桥接表大小（Bridging Table Size）

状态详情见子网桥接状态章节。 相关链接：[子网桥接状态（Subnet Bridge states）](P092_Mesh子网桥接.md#bluetooth-mesh-brg-cfg-states)。

<a id="api-reference"></a>

## 94.1 API 参考（API reference）

[桥接配置服务端模型（Bridge Configuration Server Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__srv.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/brg_cfg_srv.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/brg_cfg_srv.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/brg_cfg_srv.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh桥接配置客户端](P093_Mesh桥接配置客户端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh分段与重组](P095_Mesh分段与重组.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P093_Mesh桥接配置客户端.md) · [返回大纲](大纲.md) · [下一章](P095_Mesh分段与重组.md)

</details>

<!-- reading-navigation:end -->
