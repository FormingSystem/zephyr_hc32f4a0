---
id: learning.zephyr-docs.bluetooth.page-86
title: Mesh请求PDU重放保护列表配置客户端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/srpl_cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="solicitation-pdu-rpl-configuration-client"></a>

<a id="bluetooth-mesh-srpl-cli"></a>

# 第86章\_请求 PDU 重放保护列表配置客户端（Solicitation PDU RPL Configuration Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/srpl_cli.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：SRPL 是请求重放保护列表（Solicitation Replay Protection List）。本模型使用应用密钥（AppKey）通信；不能因为名称中有“配置”就照搬普通配置客户端的设备密钥（DevKey）用法。

请求 PDU 重放保护列表配置客户端是 Bluetooth Mesh 规范定义的基础模型。该模型可选，通过 [`CONFIG_BT_MESH_SOL_PDU_RPL_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SOL_PDU_RPL_CLI) 启用。

该模型在《Bluetooth Mesh Protocol Specification》1.1 版引入，用于从支持相应服务端的节点的请求重放保护列表（Solicitation Replay Protection List，SRPL）中移除地址。 相关链接：[请求 PDU 重放保护列表配置服务端（Solicitation PDU RPL Configuration Server）](P087_Mesh请求PDU重放保护列表配置服务端.md#bluetooth-mesh-srpl-srv)。

此客户端使用配置客户端所配置的应用密钥（application key），与请求 PDU 重放保护列表配置服务端通信。

若存在该客户端模型，只能在主元素上实例化。

<a id="configurations"></a>

## 86.1 配置（Configurations）

可通过传输超时选项 [`CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT) 配置其行为。`CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT` 指定客户端等待响应消息的时间，单位为毫秒；运行时可调用 [`bt_mesh_sol_pdu_rpl_cli_timeout_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html#gadabdbd95f39a498307e3ca9e50acfeb9) 修改。 相关链接：[`CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT)。

<a id="api-reference"></a>

## 86.2 API 参考（API reference）

[Bluetooth Mesh 请求 PDU 重放保护列表客户端（Bluetooth Mesh Solicitation PDU RPL Client）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/srpl_cli.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/srpl_cli.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/srpl_cli.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh按需私有代理服务端](P085_Mesh按需私有代理服务端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh请求PDU重放保护列表配置服务端](P087_Mesh请求PDU重放保护列表配置服务端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P085_Mesh按需私有代理服务端.md) · [返回大纲](大纲.md) · [下一章](P087_Mesh请求PDU重放保护列表配置服务端.md)

</details>

<!-- reading-navigation:end -->
