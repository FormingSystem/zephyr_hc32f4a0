---
id: learning.zephyr-docs.bluetooth.page-83
title: Mesh私有信标服务端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/priv_beacon_srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="private-beacon-server"></a>

<a id="bluetooth-mesh-models-priv-beacon-srv"></a>

# 第83章\_私有信标服务端（Private Beacon Server）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/priv_beacon_srv.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：编译启用、模型实例化和已保存设置加载是不同阶段。正文说明接收私有信标不要求实例化本服务端，而发送需要；重新启动时持久化设置可能覆盖代码里的初值。

私有信标服务端是 Bluetooth Mesh 规范定义的基础模型，通过 [`CONFIG_BT_MESH_PRIV_BEACON_SRV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PRIV_BEACON_SRV) 启用。

该模型在《Bluetooth Mesh Protocol Specification》1.1 版引入，控制节点的私有信标（Private Beacon）、私有 GATT 代理（Private GATT Proxy）和私有节点身份（Private Node Identity）状态。

私有信标功能定期随机化信标输入数据，防止网络外设备跟踪节点，并隐藏网络 IV 索引、IV 更新和密钥刷新状态。设备要发送私有信标，必须实例化私有信标服务端；但即使没有此模型，节点也会处理收到的私有信标。

私有信标服务端不提供独立控制 API，由私有信标客户端控制；它仅接受用本节点设备密钥加密的消息。 相关链接：[私有信标客户端（Private Beacon Client）](P082_Mesh私有信标客户端.md#bluetooth-mesh-models-priv-beacon-cli)。

应用可通过传给 [`BT_MESH_MODEL_PRIV_BEACON_SRV`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__srv.html#gac2e5a8847c2abf94feddfc78d0589dc2) 的 `bt_mesh_priv_beacon_srv` 实例配置初始参数。若节点已通过设置子系统保存过配置变化，加载设置时可能覆盖这些初始值。

若存在私有信标服务端模型，只能在主元素上实例化。

<a id="api-reference"></a>

## 83.1 API 参考（API reference）

[Bluetooth Mesh 私有信标服务端（Bluetooth Mesh Private Beacon Server）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__srv.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/priv_beacon_srv.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/priv_beacon_srv.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/priv_beacon_srv.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh私有信标客户端](P082_Mesh私有信标客户端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh按需私有代理客户端](P084_Mesh按需私有代理客户端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P082_Mesh私有信标客户端.md) · [返回大纲](大纲.md) · [下一章](P084_Mesh按需私有代理客户端.md)

</details>

<!-- reading-navigation:end -->
