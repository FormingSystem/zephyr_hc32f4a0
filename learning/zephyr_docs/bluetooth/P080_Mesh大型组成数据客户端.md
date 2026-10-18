---
id: learning.zephyr-docs.bluetooth.page-80
title: Mesh大型组成数据客户端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/lcd_cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="large-composition-data-client"></a>

<a id="bluetooth-mesh-lcd-cli"></a>

# 第80章\_大型组成数据客户端（Large Composition Data Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/lcd_cli.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：组成数据（Composition Data）描述节点的元素、模型和功能；模型元数据（models metadata）补充各模型的描述信息。本模型读取这些信息，不等于修改节点组成。

大型组成数据客户端是 Bluetooth Mesh 规范定义的基础模型。该模型可选，通过 [`CONFIG_BT_MESH_LARGE_COMP_DATA_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_LARGE_COMP_DATA_CLI) 启用。

该模型在《Bluetooth Mesh Protocol Specification》1.1 版引入，支持从具备大型组成数据服务端的节点读取无法放入一条 Config Composition Data Status 消息的组成数据页面，以及节点上模型实例的元数据（metadata）。 相关链接：[大型组成数据服务端（Large Composition Data Server）](P081_Mesh大型组成数据服务端.md#bluetooth-mesh-lcd-srv)。

大型组成数据客户端使用目标服务端实例所在节点的设备密钥，与大型组成数据服务端通信。

若存在大型组成数据客户端模型，只能在主元素上实例化。

<a id="api-reference"></a>

## 80.1 API 参考（API reference）

[大型组成数据客户端模型（Large Composition Data Client model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__cli.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/lcd_cli.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/lcd_cli.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/lcd_cli.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh健康服务端](P079_Mesh健康服务端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh大型组成数据服务端](P081_Mesh大型组成数据服务端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P079_Mesh健康服务端.md) · [返回大纲](大纲.md) · [下一章](P081_Mesh大型组成数据服务端.md)

</details>

<!-- reading-navigation:end -->
