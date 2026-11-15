---
id: learning.zephyr-docs.bluetooth.page-82
title: Mesh私有信标客户端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/priv_beacon_cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="private-beacon-client"></a>

<a id="bluetooth-mesh-models-priv-beacon-cli"></a>

# 第82章\_私有信标客户端（Private Beacon Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/priv_beacon_cli.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：私有信标（Private Beacon）的随机化用于降低网络外设备跟踪与读取状态的能力，不能把它等同于匿名应用通信或免除密钥管理。

私有信标客户端是 Bluetooth Mesh 规范定义的基础模型，通过 [`CONFIG_BT_MESH_PRIV_BEACON_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PRIV_BEACON_CLI) 启用。

该模型在《Bluetooth Mesh Protocol Specification》1.1 版引入，用于配置私有信标服务端模型。 相关链接：[私有信标服务端（Private Beacon Server）](P083_Mesh私有信标服务端.md#bluetooth-mesh-models-priv-beacon-srv)。

私有信标（Private Beacons）功能定期随机化信标输入数据，为不同 Bluetooth Mesh 信标提供隐私保护，防止网络外设备跟踪节点，并隐藏网络 IV 索引、IV 更新和密钥刷新状态。

私有信标客户端使用目标节点的设备密钥与私有信标服务端通信；既可配置其他节点，也可通过本地私有信标服务端自配置。 相关链接：[私有信标服务端（Private Beacon Server）](P083_Mesh私有信标服务端.md#bluetooth-mesh-models-priv-beacon-srv)。

私有信标客户端 API 的所有配置函数都以 `net_idx` 和 `addr` 为前两个参数，应分别设为目标节点配网时使用的网络索引和主单播地址。

若存在私有信标客户端模型，只能在主元素上实例化。

<a id="api-reference"></a>

## 82.1 API 参考（API reference）

[Bluetooth Mesh 私有信标客户端（Bluetooth Mesh Private Beacon Client）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/priv_beacon_cli.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/priv_beacon_cli.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/priv_beacon_cli.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh大型组成数据服务端](P081_Mesh大型组成数据服务端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh私有信标服务端](P083_Mesh私有信标服务端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P081_Mesh大型组成数据服务端.md) · [返回大纲](大纲.md) · [下一章](P083_Mesh私有信标服务端.md)

</details>

<!-- reading-navigation:end -->
