---
id: learning.zephyr-docs.bluetooth.page-48
title: 通用音频配置文件CAP
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/audio/cap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="common-audio-profile"></a>

<a id="bluetooth-cap"></a>

# 第48章\_通用音频配置文件（Common Audio Profile，CAP）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/audio/cap.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="api-reference"></a>

## 48.1 API 参考（API Reference）

[通用音频配置文件（Common Audio Profile，CAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html)

相关代码示例（Related code samples）

- [通用音频配置文件（Common Audio Profile，CAP）接受方（Acceptor）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/cap_acceptor/README.html#bluetooth_cap_acceptor)：通过 CAP 接受方角色向 CAP 发起方（Initiator）广播音频可用性。

- [通用音频配置文件（Common Audio Profile，CAP）切换（Handover）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/cap_handover/README.html#bluetooth_cap_handover)：连接 CAP 接受方并执行 CAP 切换过程。

- [通用音频配置文件（Common Audio Profile，CAP）发起方（Initiator）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/cap_initiator/README.html#bluetooth_cap_initiator)：连接 CAP 接受方，建立单播或广播音频流。

- [电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）广播媒体发送方（Broadcast Media Sender，BMS）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/tmap_bms/README.html#ble_peripheral_tmap_bms)：实现 LE Audio TMAP 的 BMS 角色。

- [电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）中心设备（Central）](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/tmap_central/README.html#ble_peripheral_tmap_central)：实现 TMAP 的通话网关（Call Gateway，CG）与单播媒体发送方（Unicast Media Sender，UMS）角色。

对应官方文档源码：[doc/services/connectivity/bluetooth/api/audio/cap.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/audio/cap.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/audio/cap.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件或连接音频设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：基本音频配置文件BAP](P047_基本音频配置文件BAP.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：蓝牙协调集](P049_蓝牙协调集.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P047_基本音频配置文件BAP.md) · [返回大纲](大纲.md) · [下一章](P049_蓝牙协调集.md)

</details>

<!-- reading-navigation:end -->
