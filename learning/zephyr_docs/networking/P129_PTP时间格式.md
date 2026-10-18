---
id: learning.zephyr-docs.networking.page-129
title: PTP时间格式
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/ptp_time.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第129章\_PTP时间格式

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/ptp_time.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

精确时间协议（Precision Time Protocol，PTP）的时间结构可以以纳秒（Nanosecond）精度格式保存时间信息。扩展时间戳格式（Extended Timestamp Format）还可以表示不足一纳秒的时间分量。

通用精确时间协议（generic Precision Time Protocol，gPTP）的实现使用这种 PTP 时间格式。

## 2. API 参考（API Reference）

[PTP 时间（PTP Time）](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__time.html)。

相关代码示例：[gPTP 示例](P121_gPTP示例.md#gptp)，启用 gPTP 支持，并通过网络命令行（net-shell）监测功能。

> 译注——表示与精度：这里描述数据格式能表达的时间分辨率，不是任意设备实际同步精度的保证。时间戳结构和转换接口可跟踪官方 [`include/zephyr/net/ptp_time.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/ptp_time.h)。


<a id="precision-time-protocol-ptp-time-format"></a>
<a id="ptp-time-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="overview"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：PTP精确时间协议](P128_PTP精确时间协议.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：网络时间表示](P130_网络时间表示.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P128_PTP精确时间协议.md) · [返回大纲](大纲.md) · [下一章](P130_网络时间表示.md)

</details>

<!-- reading-navigation:end -->
