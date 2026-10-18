---
id: learning.zephyr-docs.bluetooth.page-77
title: Mesh配置服务端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/cfg_srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="configuration-server"></a>

<a id="bluetooth-mesh-models-cfg-srv"></a>

# 第77章\_配置服务端（Configuration Server）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/cfg_srv.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：配置服务端是节点的必备基础模型。这里“不提供独立 API”指它由配置客户端消息控制，并不表示应用不需要声明模型实例或完成 Mesh 初始化。

配置服务端是 Bluetooth Mesh 规范定义的基础模型，控制节点的大多数参数。它不提供独立控制 API，而由配置客户端控制。 相关链接：[配置客户端（Configuration Client）](P076_Mesh配置客户端.md#bluetooth-mesh-models-cfg-cli)。

所有 Bluetooth Mesh 节点都必须有配置服务端模型，且只能实例化在主元素上。

<a id="api-reference"></a>

## 77.1 API 参考（API reference）

[配置服务端模型（Configuration Server Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__srv.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/cfg_srv.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/cfg_srv.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/cfg_srv.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh配置客户端](P076_Mesh配置客户端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh健康客户端](P078_Mesh健康客户端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P076_Mesh配置客户端.md) · [返回大纲](大纲.md) · [下一章](P078_Mesh健康客户端.md)

</details>

<!-- reading-navigation:end -->
