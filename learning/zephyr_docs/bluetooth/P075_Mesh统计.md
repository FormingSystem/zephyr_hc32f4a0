---
id: learning.zephyr-docs.bluetooth.page-75
title: Mesh统计
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/statistic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mesh-statistic"></a>

<a id="bluetooth-mesh-stat"></a>

# 第75章\_Mesh 统计（Mesh Statistic）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/statistic.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：低功耗节点（Low Power Node，LPN）通过友谊节点（Friend node）接收缓存消息；帧数和发送尝试次数反映协议栈观测，不能直接当作应用交付成功次数；接收延迟（ReceiveDelay）和接收窗口（ReceiveWindow）的测量单位为微秒，比较时应先统一配置与测量的单位。

统计 API 提供 Bluetooth Mesh 通信的运行时监控。

<a id="frame-statistic"></a>

## 75.1 帧统计（Frame statistic）

帧统计 API 可监控不同接口收到的帧数，以及计划和成功执行的发送、中继尝试次数。

该 API 帮助用户评估广播器配置参数的效率和设备扫描能力；可通过自定义值方便地扩展监控参数。

<a id="lpn-timing-measurement"></a>

## 75.2 LPN 时序测量（LPN timing measurement）

启用 [`CONFIG_BT_MESH_LOW_POWER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_LOW_POWER) 时，统计模块对协议事件加时间戳，以测量 LPN 友谊关系（friendship）的时序参数：

- T1：轮询发送完成（Poll TX complete）。

- T2：扫描器启用，即接收延迟（ReceiveDelay）已结束。

- T3：收到 Friend 响应，或接收窗口（ReceiveWindow）到期。

模块用这些时间戳计算实测 ReceiveDelay（T2 - T1）和 ReceiveWindow（T3 - T2），单位为微秒。应用可据此对照配置的友谊参数，评估实际空口时序。

应用可随时读取和重置统计值。

<a id="api-reference"></a>

## 75.3 API 参考（API reference）

[统计（Statistic）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/statistic.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/statistic.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/statistic.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh配置数据库](P074_Mesh配置数据库.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh配置客户端](P076_Mesh配置客户端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P074_Mesh配置数据库.md) · [返回大纲](大纲.md) · [下一章](P076_Mesh配置客户端.md)

</details>

<!-- reading-navigation:end -->
