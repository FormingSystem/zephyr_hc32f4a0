---
id: learning.zephyr-docs.observability.trace-1
title: MIPI跟踪协议解码器
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/services/debugging/mipi_stp_decoder.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第10章\_MIPI跟踪协议解码器

原文：[MIPI STP Decoder](https://docs.zephyrproject.org/latest/services/debugging/mipi_stp_decoder.html)。读取日期：2026-10-13，`latest`。

## 10.1\_协议与模块

**MIPI系统跟踪协议（MIPI System Trace Protocol，MIPI STP）**是一种通用基础协议，可供多种面向特定应用的跟踪协议共用。它作为封装协议，把通常来自不同跟踪源、包含不同跟踪协议的流合并起来。

数据流由**操作码（Opcode）**及其后的可选数据、可选时间戳（Timestamp）组成；最短操作码为 4 位。操作码包括：8、16、32、64 位数据操作，可带标记或不带标记、带时间戳或不带时间戳；流识别操作，包含主设备（Master）和通道（Channel）；同步操作 `ASYNC`，以及其他操作。

一个应用实例是 Arm CoreSight **系统跟踪宏单元（System Trace Macrocell，STM）**：写入激励端口（Stimulus Port）寄存器的数据直接映射为 STP 流。

本模块采用 STP 第 2 版（STPv2），可在芯片上解码数据流。

## 10.2\_使用方式

初始化解码器时提供回调（Callback），每解出一个操作码便调用一次。操作码之间存在依赖，例如时间戳可能是相对值，因此解码器保存内部状态。

解码器可以处于同步或未同步状态，初始状态可配置。未与数据流同步时，它会逐个半字节（Nibble，4 位）解码，寻找 `ASYNC` 操作码。调用 [`mipi_stp_decoder_sync_loss()`](P027_MIPI_STP解码接口.md) 可通知解码器同步丢失；调用 [`mipi_stp_decoder_decode()`](P027_MIPI_STP解码接口.md) 解码数据。

## 10.3\_限制

- 只支持小端（Little Endian）架构。
- 解码半字节时，核心若支持非对齐内存访问（Unaligned Memory Access），效率会更高。实现提供通用版本和采用非对齐访问的优化版本；Arm Cortex-M 使用优化版本，但 Cortex-M0 除外。
- 只实现了最常用操作码的一个有限子集。

## 10.4\_接口文档

详见 [STP解码器应用程序编程接口（Application Programming Interface，API）](P027_MIPI_STP解码接口.md)。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：调试服务目录](P009_调试服务目录.md) · [本模块主线目录](../reading/observability.md) · [全部主线](../reading/README.md) · [下一篇：CoreSight跟踪解复用器](P011_CoreSight跟踪解复用器.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：调试服务目录](P009_调试服务目录.md) · [下一章：CoreSight跟踪解复用器](P011_CoreSight跟踪解复用器.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
