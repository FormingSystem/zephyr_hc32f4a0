---
id: learning.zephyr-docs.usb.api-113
title: UMP格式与MIDI协议依据
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ump112.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第113章\_UMP格式与MIDI协议依据

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ump112.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 113.1\_阅读说明与来源

译注：本页说明UMP流响应器、配置对象或其实现依据。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

这些定义以下列文档为依据：《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议——包含 UMP 格式的 MIDI 1.0 协议》（Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol With MIDI 1.0 Protocol in UMP Format），文档版本 1.1.2，MIDI 协会文档编号 M2-104-UM。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol With MIDI 1.0 Protocol in UMP Format - Document version 1.1.2 (MIDI Association Document: M2-104-UM)](https://midi.org/universal-midi-packet-ump-and-midi-2-0-protocol-specification)。

## 113.2\_源码跟踪与使用边界

译注依据保存的[官方响应器头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/ump_stream_responder.h)、[实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/ump_stream_responder.c)、[CMake入口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/CMakeLists.txt)和[Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/Kconfig)，摘要见[来源记录](../SOURCES.md)。本仓库的[头文件](../../../lib/midi2/ump_stream_responder.h)与[实现](../../../lib/midi2/ump_stream_responder.c)可用于源码跟踪，版本可能与网页不同；本批未构建或执行MIDI硬件验证。

[上一章](P112_UMP流响应器实现参考.md) · [返回大纲](大纲.md) · [下一章](P114_UMP功能块设备树配置.md)
