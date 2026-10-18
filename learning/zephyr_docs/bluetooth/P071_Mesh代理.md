---
id: learning.zephyr-docs.bluetooth.page-71
title: Mesh代理
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/proxy.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="proxy"></a>

<a id="bt-mesh-proxy"></a>

# 第71章\_代理（Proxy）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/proxy.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：这里的传统设备（legacy device）指通过 GATT 代理接入 Mesh 的设备，并不表示它已能直接收发 Mesh 广播。代理请求（solicitation）使支持按需代理的节点开始广播，后续仍须建立相应连接和协议交互。

代理功能允许手机等传统设备通过 GATT 接入 Bluetooth Mesh 网络。只有启用 [`CONFIG_BT_MESH_GATT_PROXY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT_PROXY) 才会编译此功能。其状态由配置服务端控制，初始值可通过 `bt_mesh_cfg_srv.gatt_proxy` 设置。 相关链接：[配置服务端（Configuration Server）](P077_Mesh配置服务端.md#bluetooth-mesh-models-cfg-srv)。

启用代理功能的节点可使用网络身份（Network Identity）与节点身份（Node Identity）广播，由配置客户端控制。 相关链接：[配置客户端（Configuration Client）](P076_Mesh配置客户端.md#bluetooth-mesh-models-cfg-cli)。

GATT Proxy 状态表示是否支持代理功能。

<a id="private-proxy"></a>

## 71.1 私有代理（Private Proxy）

支持代理功能与私有信标服务端模型的节点，可使用私有网络身份（Private Network Identity）和私有节点身份（Private Node Identity）类型广播，由私有信标客户端控制。这些标识类型允许传统设备经 GATT 连接网络，同时维护网络隐私。 相关链接：[私有信标服务端（Private Beacon Server）](P083_Mesh私有信标服务端.md#bluetooth-mesh-models-priv-beacon-srv)；[私有信标客户端（Private Beacon Client）](P082_Mesh私有信标客户端.md#bluetooth-mesh-models-priv-beacon-cli)。

Private GATT Proxy 状态表示是否支持私有代理功能。

<a id="proxy-solicitation"></a>

## 71.2 代理请求（Proxy Solicitation）

节点同时禁用 GATT Proxy 与 Private GATT Proxy 状态时，传统设备无法连接。但若节点支持按需私有代理服务端，可在不启用 Private GATT Proxy 状态的情况下，应请求发送可连接广播事件。传统设备调用 `bt_mesh_proxy_solicit()` 发送请求 PDU（Solicitation PDU），请求节点这样做。要启用该功能，编译设备时必须设置 [`CONFIG_BT_MESH_PROXY_SOLICITATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROXY_SOLICITATION)。 相关链接：[按需私有代理服务端（On-Demand Private Proxy Server）](P085_Mesh按需私有代理服务端.md#bluetooth-mesh-od-srv)。

请求 PDU 是非 Mesh、不可连接、非定向的广播消息，包含 Proxy Solicitation UUID，并用传统设备希望连接的子网网络密钥加密。PDU 包含该设备的源地址和序列号；序列号由该设备维护，每发送一个新的请求 PDU 就递增一次。

每个支持接收请求 PDU 的节点维护自己的请求重放保护列表（Solicitation Replay Protection List，SRPL）。SRPL 保存已处理有效请求 PDU 的请求序列号（Solicitation Sequence Number，SSEQ）与请求源（Solicitation Source，SSRC）对，防止请求机制遭受重放攻击。更新 SRPL 到持久化保存该变化之间的延迟由 [`CONFIG_BT_MESH_RPL_STORE_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RPL_STORE_TIMEOUT) 定义。

请求 PDU 重放保护列表配置客户端和服务端模型提供保存、清除 SRPL 条目的功能。支持该客户端模型的节点可调用 `bt_mesh_sol_pdu_rpl_clear()` 清除目标节点的部分 SRPL。客户端与服务端通信使用应用密钥加密，因此客户端可实例化在网络中的任意设备上。 相关链接：[请求 PDU 重放保护列表配置客户端（Solicitation PDU RPL Configuration Client）](P086_Mesh请求PDU重放保护列表配置客户端.md#bluetooth-mesh-srpl-cli)；[请求 PDU 重放保护列表配置服务端（Solicitation PDU RPL Configuration Server）](P087_Mesh请求PDU重放保护列表配置服务端.md#bluetooth-mesh-srpl-srv)。

节点收到请求 PDU 并认证成功后，开始发送使用私有网络身份类型的可连接广播。广播持续时间可由按需私有代理客户端模型配置。

<a id="api-reference"></a>

## 71.3 API 参考（API reference）

[代理（Proxy）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/proxy.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/proxy.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/proxy.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh配网](P070_Mesh配网.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh心跳](P072_Mesh心跳.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P070_Mesh配网.md) · [返回大纲](大纲.md) · [下一章](P072_Mesh心跳.md)

</details>

<!-- reading-navigation:end -->
