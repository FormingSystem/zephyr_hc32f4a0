---
id: learning.zephyr-docs.bluetooth.page-47
title: 基本音频配置文件BAP
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/audio/bap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="basic-audio-profile"></a>

<a id="bluetooth-bap"></a>

# 第47章\_基本音频配置文件（Basic Audio Profile，BAP）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/audio/bap.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="api-reference"></a>

## 47.1 API 参考（API Reference）

[蓝牙基本音频配置文件（Bluetooth Basic Audio Profile）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html)

相关代码示例（Related code samples）

- [基本音频配置文件（Basic Audio Profile，BAP）广播助手（Broadcast Assistant）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/bap_broadcast_assistant/README.html#bluetooth_bap_broadcast_assistant)：使用 BAP 广播助手功能。

- [基本音频配置文件（Basic Audio Profile，BAP）广播接收端（Broadcast Sink）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/bap_broadcast_sink/README.html#bluetooth_bap_broadcast_sink)：使用 BAP 广播接收端功能。

- [基本音频配置文件（Basic Audio Profile，BAP）广播发送端（Broadcast Source）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/bap_broadcast_source/README.html#bluetooth_bap_broadcast_source)：使用 BAP 广播发送端功能。

- [基本音频配置文件（Basic Audio Profile，BAP）单播客户端（Unicast Client）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/bap_unicast_client/README.html#bluetooth_bap_unicast_client)：使用 BAP 单播客户端功能。

- [基本音频配置文件（Basic Audio Profile，BAP）单播服务端（Unicast Server）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/bap_unicast_server/README.html#bluetooth_bap_unicast_server)：使用 BAP 单播服务端功能。

- [通用音频配置文件（Common Audio Profile，CAP）接受方（Acceptor）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/cap_acceptor/README.html#bluetooth_cap_acceptor)：通过 CAP 接受方角色向 CAP 发起方（Initiator）广播音频可用性。

- [通用音频配置文件（Common Audio Profile，CAP）切换（Handover）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/cap_handover/README.html#bluetooth_cap_handover)：连接 CAP 接受方并执行 CAP 切换过程。

- [通用音频配置文件（Common Audio Profile，CAP）发起方（Initiator）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/cap_initiator/README.html#bluetooth_cap_initiator)：连接 CAP 接受方，建立单播或广播音频流。

- [公共广播配置文件（Public Broadcast Profile，PBP）公共广播接收端（Public Broadcast Sink）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/pbp_public_broadcast_sink/README.html#bluetooth_public_broadcast_sink)：使用 PBP 公共广播接收端功能。

- [公共广播配置文件（Public Broadcast Profile，PBP）公共广播发送端（Public Broadcast Source）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/pbp_public_broadcast_source/README.html#bluetooth_public_broadcast_source)：使用 PBP 公共广播发送端功能。

- [电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）广播媒体接收方（Broadcast Media Receiver，BMR）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/tmap_bmr/README.html#ble_peripheral_tmap_bmr)：实现 TMAP 的 BMR 角色。

- [电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）广播媒体发送方（Broadcast Media Sender，BMS）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/tmap_bms/README.html#ble_peripheral_tmap_bms)：实现 LE Audio TMAP 的 BMS 角色。

- [电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）中心设备（Central）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/tmap_central/README.html#ble_peripheral_tmap_central)：实现 TMAP 的通话网关（Call Gateway，CG）与单播媒体发送方（Unicast Media Sender，UMS）角色。

- [电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）外围设备（Peripheral）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/tmap_peripheral/README.html#ble_peripheral_tmap_peripheral)：实现 TMAP 的通话终端（Call Terminal，CT）与单播媒体接收方（Unicast Media Receiver，UMR）角色。

[BAP 单播客户端 API（BAP Unicast Client APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html)

[BAP 单播服务端 API（BAP Unicast Server APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__server.html)

[BAP 广播 API（BAP Broadcast APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html)

[BAP 广播接收端 API（BAP Broadcast Sink APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__sink.html)

[BAP 广播发送端 API（BAP Broadcast Source APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/audio/bap.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/audio/bap.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/audio/bap.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件或连接音频设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：低功耗音频协议栈](P046_低功耗音频协议栈.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：通用音频配置文件CAP](P048_通用音频配置文件CAP.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P046_低功耗音频协议栈.md) · [返回大纲](大纲.md) · [下一章](P048_通用音频配置文件CAP.md)

</details>

<!-- reading-navigation:end -->
