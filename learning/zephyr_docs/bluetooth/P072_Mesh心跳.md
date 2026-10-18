---
id: learning.zephyr-docs.bluetooth.page-72
title: Mesh心跳
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/heartbeat.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="heartbeat"></a>

<a id="bluetooth-mesh-heartbeat"></a>

# 第72章\_心跳（Heartbeat）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/heartbeat.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：本页的距离指网络跳数，不是米、RSSI 测距或物理距离。心跳订阅按源地址、目的地址和时间窗口筛选；消息能通过无线电接收并不等于它符合当前心跳订阅条件。

心跳功能用于监控 Bluetooth Mesh 节点并确定节点之间的距离。

心跳功能通过配置服务端模型配置。 相关链接：[配置服务端（Configuration Server）](P077_Mesh配置服务端.md#bluetooth-mesh-models-cfg-srv)。

<a id="heartbeat-messages"></a>

## 72.1 心跳消息（Heartbeat messages）

心跳消息作为传输控制数据包在网络中发送，仅使用网络密钥加密。消息包含发送时的原始生存时间（Time To Live，TTL）值，以及表示节点已启用功能的位字段。接收节点可据此判断消息到达前经历了多少次中继，以及发送节点支持哪些功能。

可用的心跳功能标志：

- [`BT_MESH_FEAT_RELAY`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#gac588eefe83db94784a420ce063f02b55)

- [`BT_MESH_FEAT_PROXY`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#gaee648ce202316c56d4d588cb0ad5aeb4)

- [`BT_MESH_FEAT_FRIEND`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga8f27086b3bc3c4a6e14621836f9f8e80)

- [`BT_MESH_FEAT_LOW_POWER`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#gaad71a36c82b4e4d3fa334ecff5cc0171)

> 译注——标志对照：RELAY 表示中继，PROXY 表示代理，FRIEND 表示友谊节点功能，LOW_POWER 表示低功耗节点功能；这些是协议功能状态，不是四类不同的物理距离。

<a id="heartbeat-publication"></a>

## 72.2 心跳发布（Heartbeat publication）

心跳发布由配置模型控制，可通过两种方式触发：

周期发布（Periodic publication）

节点按固定间隔发布新的心跳消息，可配置为发送一定数量后停止，或无限持续。

触发发布（Triggered publication）

节点每次有功能状态变化时发布新的心跳消息；哪些功能可触发发布可以配置。

这两种发布方式可以组合使用。

<a id="heartbeat-subscription"></a>

## 72.3 心跳订阅（Heartbeat subscription）

一个节点同一时间可配置为订阅一个节点的心跳消息。要接收该心跳，源地址和目的地址都必须匹配配置的订阅参数。

心跳订阅始终有时间限制；订阅期间，节点持续记录收到的心跳数量，以及收到的最小和最大跳数。

所有匹配订阅参数的心跳都交给 `bt_mesh_hb_cb::recv` 事件处理函数。

心跳订阅期结束时，调用 `bt_mesh_hb_cb::sub_end` 回调。

<a id="api-reference"></a>

## 72.4 API 参考（API reference）

[心跳（Heartbeat）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__heartbeat.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/heartbeat.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/heartbeat.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/heartbeat.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh代理](P071_Mesh代理.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh运行时配置](P073_Mesh运行时配置.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P071_Mesh代理.md) · [返回大纲](大纲.md) · [下一章](P073_Mesh运行时配置.md)

</details>

<!-- reading-navigation:end -->
