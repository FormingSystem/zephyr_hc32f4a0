---
id: learning.zephyr-docs.bluetooth.page-76
title: Mesh配置客户端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/cfg_cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="configuration-client"></a>

<a id="bluetooth-mesh-models-cfg-cli"></a>

# 第76章\_配置客户端（Configuration Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/cfg_cli.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：客户端（Client）与服务端（Server）指 Mesh 模型角色，不是电脑与开发板的固定分工。配置客户端以目标节点的设备密钥操作目标配置；参数中的网络索引和主单播地址必须对应实际目标。

配置客户端模型是 Bluetooth Mesh 规范定义的基础模型（foundation model），用于配置 Mesh 节点的大多数参数，包括加密密钥、模型配置和功能启用状态。

配置客户端使用目标节点的设备密钥（device key）与配置服务端通信；既可配置其他节点，也可通过本地配置服务端完成自配置。 相关链接：[配置服务端（Configuration Server）](P077_Mesh配置服务端.md#bluetooth-mesh-models-cfg-srv)。

配置客户端 API 的所有配置函数都以 `net_idx` 和 `addr` 为前两个参数，应分别设为目标节点配网时使用的网络索引和主单播地址（primary unicast address）。

配置客户端模型可选；若组成数据（Composition Data）包含该模型，它只能实例化在主元素（primary element）上。

<a id="api-reference"></a>

## 76.1 API 参考（API reference）

[配置客户端模型（Configuration Client Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/cfg_cli.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/cfg_cli.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/cfg_cli.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh统计](P075_Mesh统计.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh配置服务端](P077_Mesh配置服务端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P075_Mesh统计.md) · [返回大纲](大纲.md) · [下一章](P077_Mesh配置服务端.md)

</details>

<!-- reading-navigation:end -->
