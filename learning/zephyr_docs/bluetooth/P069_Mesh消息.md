---
id: learning.zephyr-docs.bluetooth.page-69
title: Mesh消息
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/msg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="message"></a>

<a id="bluetooth-mesh-msg"></a>

# 第69章\_Mesh 消息（Message）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/msg.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：本页原文仅包含消息模块说明与 API 入口。消息缓冲区（message buffer）保存编码数据，消息上下文（message context）保存发送／接收参数；需确认消息上下文（acknowledged message context）还跟踪请求与响应。详细结构和函数以链接的独立 API 页面为准。

Bluetooth Mesh 消息模块提供一组结构、宏和函数，用于准备消息缓冲区，管理消息上下文及需确认消息的上下文。

<a id="api-reference"></a>

## 69.1 API 参考（API reference）

[Mesh 消息（Message）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/msg.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/msg.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/msg.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh模型](P068_Mesh模型.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh配网](P070_Mesh配网.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P068_Mesh模型.md) · [返回大纲](大纲.md) · [下一章](P070_Mesh配网.md)

</details>

<!-- reading-navigation:end -->
