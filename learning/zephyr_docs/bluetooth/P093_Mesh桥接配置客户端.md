---
id: learning.zephyr-docs.bluetooth.page-93
title: Mesh桥接配置客户端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/brg_cfg_cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bridge-configuration-client"></a>

<a id="bluetooth-mesh-models-brg-cfg-cli"></a>

# 第93章\_桥接配置客户端（Bridge Configuration Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/brg_cfg_cli.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：桥接配置客户端管理目标节点的桥接状态和桥接表；它不会仅凭本地创建一个实例就让网络中所有节点自动桥接。目标必须支持相应服务端，并具备所需子网和密钥。

桥接配置客户端是 Bluetooth Mesh 规范定义的基础模型。该模型可选，通过 [`CONFIG_BT_MESH_BRG_CFG_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_BRG_CFG_CLI) 启用。

该客户端用于配置包含桥接配置服务端的另一 Mesh 节点的子网桥接功能，访问层安全使用目标服务端所在节点的设备密钥。 相关链接：[桥接配置服务端（Bridge Configuration Server）](P094_Mesh桥接配置服务端.md#bluetooth-mesh-models-brg-cfg-srv)。

若存在桥接配置客户端模型，只能在主元素上实例化。

<a id="api-reference"></a>

## 93.1 API 参考（API reference）

[桥接配置客户端模型（Bridge Configuration Client Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/brg_cfg_cli.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/brg_cfg_cli.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/brg_cfg_cli.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh子网桥接](P092_Mesh子网桥接.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh桥接配置服务端](P094_Mesh桥接配置服务端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P092_Mesh子网桥接.md) · [返回大纲](大纲.md) · [下一章](P094_Mesh桥接配置服务端.md)

</details>

<!-- reading-navigation:end -->
