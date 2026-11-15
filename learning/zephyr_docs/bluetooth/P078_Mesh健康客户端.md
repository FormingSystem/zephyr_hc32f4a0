---
id: learning.zephyr-docs.bluetooth.page-78
title: Mesh健康客户端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/health_cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="health-client"></a>

<a id="bluetooth-mesh-models-health-cli"></a>

# 第78章\_健康客户端（Health Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/health_cli.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：健康模型（Health model）提供设备诊断，不是医学健康监测协议。客户端查询故障并控制关注状态，便于把网络地址与实际设备对应起来。

健康客户端与健康服务端交互，读取诊断信息并控制节点的关注状态（attention state）。

健康客户端 API 的所有消息传递函数都以 `cli` 为首个参数，它是本次调用所用客户端模型实例的指针。第二个参数 `ctx` 是消息上下文（message context），包含目标节点使用的网络密钥索引、应用密钥索引和单播地址。

健康客户端模型可选，可实例化在任意元素上。但若某个非主元素实例化了该模型，主元素也必须包含一个实例。

规范定义的故障值列表见[健康故障（Health faults）](P079_Mesh健康服务端.md#bluetooth-mesh-health-faults)。

<a id="api-reference"></a>

## 78.1 API 参考（API reference）

[健康客户端模型（Health Client Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/health_cli.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/health_cli.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/health_cli.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh配置服务端](P077_Mesh配置服务端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh健康服务端](P079_Mesh健康服务端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P077_Mesh配置服务端.md) · [返回大纲](大纲.md) · [下一章](P079_Mesh健康服务端.md)

</details>

<!-- reading-navigation:end -->
