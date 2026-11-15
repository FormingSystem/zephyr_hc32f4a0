---
id: learning.zephyr-docs.bluetooth.page-84
title: Mesh按需私有代理客户端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/od_cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="on-demand-private-proxy-client"></a>

<a id="bluetooth-mesh-od-cli"></a>

# 第84章\_按需私有代理客户端（On-Demand Private Proxy Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/od_cli.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：请求 PDU 是请求协议数据单元（Solicitation Protocol Data Unit）；本客户端配置“收到请求后广播多久”，不是直接向任意设备发起 GATT 连接。客户端等待响应的超时与服务端广播持续时间也不是同一个参数。

按需私有代理客户端是 Bluetooth Mesh 规范定义的基础模型。该模型可选，通过 [`CONFIG_BT_MESH_OD_PRIV_PROXY_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_OD_PRIV_PROXY_CLI) 启用。

该模型在《Bluetooth Mesh Protocol Specification》1.1 版引入，用于设置和读取按需私有 GATT 代理（On-Demand Private GATT Proxy）状态。该状态规定节点收到请求 PDU（Solicitation PDU）后，以私有网络身份（Private Network Identity）类型广播 Mesh 代理服务（Mesh Proxy Service）的持续时间。

按需私有代理客户端使用目标服务端实例所在节点的设备密钥，与按需私有代理服务端通信。

若存在按需私有代理客户端模型，只能在主元素上实例化。

<a id="configurations"></a>

## 84.1 配置（Configurations）

可通过传输超时选项 [`CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT) 配置客户端行为。`CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT` 指定等待状态响应消息的时间，单位为毫秒；运行时可调用 [`bt_mesh_od_priv_proxy_cli_timeout_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html#gad613c78e708f0df5aabda9e16fae6a2c) 修改。 相关链接：[`CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT)。

<a id="api-reference"></a>

## 84.2 API 参考（API reference）

[Bluetooth Mesh 按需私有 GATT 代理客户端（Bluetooth Mesh On-Demand Private GATT Proxy Client）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/od_cli.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/od_cli.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/od_cli.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh私有信标服务端](P083_Mesh私有信标服务端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh按需私有代理服务端](P085_Mesh按需私有代理服务端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P083_Mesh私有信标服务端.md) · [返回大纲](大纲.md) · [下一章](P085_Mesh按需私有代理服务端.md)

</details>

<!-- reading-navigation:end -->
