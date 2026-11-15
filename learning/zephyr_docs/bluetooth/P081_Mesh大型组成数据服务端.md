---
id: learning.zephyr-docs.bluetooth.page-81
title: Mesh大型组成数据服务端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/lcd_srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="large-composition-data-server"></a>

<a id="bluetooth-mesh-lcd-srv"></a>

# 第81章\_大型组成数据服务端（Large Composition Data Server）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/lcd_srv.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：元数据列表的结束标记与“没有元数据”的宏有不同用途；应用仍须确保指针指向有效数据。客户端读取的是服务端模型公开的条目，不是任意设备内存。

大型组成数据服务端是 Bluetooth Mesh 规范定义的基础模型。该模型可选，通过 [`CONFIG_BT_MESH_LARGE_COMP_DATA_SRV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_LARGE_COMP_DATA_SRV) 启用。

该模型在《Bluetooth Mesh Protocol Specification》1.1 版引入，用于提供无法放入一条 Config Composition Data Status 消息的组成数据页面，以及模型实例的元数据。

大型组成数据服务端不提供独立控制 API，由大型组成数据客户端控制；它仅接受用本节点设备密钥加密的消息。 相关链接：[大型组成数据客户端（Large Composition Data Client）](P080_Mesh大型组成数据客户端.md#bluetooth-mesh-lcd-cli)。

若存在大型组成数据服务端模型，只能在主元素上实例化。

<a id="models-metadata"></a>

## 81.1 模型元数据（Models metadata）

大型组成数据服务端允许每个模型提供一份专用元数据列表，供客户端读取。列表通过 [`bt_mesh_model.metadata`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model.html#af5b948709773e5388c30d457ec2a9559) 字段关联到 [`bt_mesh_model`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model.html)，包含一个或多个 [`bt_mesh_models_metadata_entry`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__models__metadata__entry.html) 条目。每个条目包含元数据长度、ID 和原始数据指针，可用 [`BT_MESH_MODELS_METADATA_ENTRY`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaa2587adac719c50c311ae41c548b853c) 宏创建。列表末尾必须有 [`BT_MESH_MODELS_METADATA_END`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaab5fe51071f6e54debd9136ac6a70a49)。模型没有元数据时，可改用辅助宏 [`BT_MESH_MODELS_METADATA_NONE`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga56b518123ab47cb3ae4a249f471ae556)。

<a id="api-reference"></a>

### 81.1.1 API 参考（API reference）

[大型组成数据服务端模型（Large Composition Data Server model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__srv.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/lcd_srv.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/lcd_srv.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/lcd_srv.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh大型组成数据客户端](P080_Mesh大型组成数据客户端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh私有信标客户端](P082_Mesh私有信标客户端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P080_Mesh大型组成数据客户端.md) · [返回大纲](大纲.md) · [下一章](P082_Mesh私有信标客户端.md)

</details>

<!-- reading-navigation:end -->
