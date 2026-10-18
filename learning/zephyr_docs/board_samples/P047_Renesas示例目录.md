---
id: learning.zephyr-docs.board-samples.page-47
title: Renesas示例目录
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/renesas/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="renesas"></a>

# 第47章\_Renesas

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/renesas/index.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

这些示例展示如何在 Zephyr 中使用 Renesas 开发板。

> 译注——跨专题导航：OpenAMP 与比较器已有独立专题译文，ELC 与 LVD 在本册。目录中的四个示例均沿用各自官方适用平台，不把 RA 的 ELC 配置和 RX 的 LVD 接口当作同一硬件功能。

- [OpenAMP Linux 与 Zephyr RPMsg（OpenAMP Linux Zephyr RPMsg）](../intercore_reference/P091_RenesasLinux与Zephyr通信示例.md#rz-openamp-linux-zephyr)：使用 OpenAMP 库，使运行 Linux 的应用核与运行 Zephyr 的实时核能够交换消息。

- [Renesas 比较器（Renesas comparator）](../hardware/P098_Renesas比较器示例.md#renesas_comparator)：监测比较器输出。

- [Renesas ELC 示例（Renesas ELC Sample）](P045_Renesas事件链接控制器.md#renesas-elc)：将 Renesas ELC 与 PWM 功能集成。

- [使用比较器的 Renesas 低电压检测示例（Renesas Low-voltage Detection Sample using Comparator）](P046_Renesas低电压检测.md#renesas_lvd)：演示监测电压并对其变化作出响应。

对应官方文档源码：[samples/boards/renesas/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/renesas/index.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/renesas/index.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P046_Renesas低电压检测.md) · [返回大纲](大纲.md) · [下一章](P048_TI_CC13x2与CC26x2系统关闭.md)
