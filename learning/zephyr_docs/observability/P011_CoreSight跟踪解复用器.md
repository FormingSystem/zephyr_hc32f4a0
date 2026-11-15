---
id: learning.zephyr-docs.observability.trace-2
title: CoreSight跟踪解复用器
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/services/debugging/cs_trace_defmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第11章\_CoreSight跟踪解复用器

原文：[ARM Coresight Trace Deformatter](https://docs.zephyrproject.org/latest/services/debugging/cs_trace_defmt.html)。读取日期：2026-10-13，`latest`。

## 11.1\_帧封装与片上解码

**跟踪格式器（Trace Formatter）**把多条跟踪流封装为单一输出流，每条流由 7 位标识符（Identifier，ID）区分。格式器使用 16 字节帧，每帧最多封装 15 字节数据。

例如，**嵌入式跟踪路由器（Embedded Trace Router，ETR）**使用这种格式；其随机存取存储器（Random Access Memory，RAM）环形缓冲区可以保存来自不同跟踪流的数据。跟踪数据通常由主机离线解码，而**跟踪解格式器（Trace Deformatter）**可在应用运行期间于芯片上解开帧封装、分离各条流，也就是解复用（Demultiplex）。

## 11.2\_使用方式

初始化解格式器时提供用户回调（Callback）。通过 [`cs_trace_defmt_process()`](P026_CoreSight解格式接口.md) 以 16 字节块为单位解码数据。每当流发生切换或到达块末尾时，便调用回调，向其提供流 ID 和数据。

## 11.3\_接口文档

详见 [CoreSight跟踪解格式器应用程序编程接口（Application Programming Interface，API）](P026_CoreSight解格式接口.md)。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：MIPI跟踪协议解码器](P010_MIPI跟踪协议解码器.md) · [本模块主线目录](../reading/observability.md) · [全部主线](../reading/README.md) · [下一篇：CoreSight系统跟踪日志](P012_CoreSight系统跟踪日志.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：MIPI跟踪协议解码器](P010_MIPI跟踪协议解码器.md) · [下一章：CoreSight系统跟踪日志](P012_CoreSight系统跟踪日志.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
