---
id: learning.zephyr-docs.driver_samples.page-14
title: LoRa示例目录
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/lora/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lora"></a>

# 第14章\_LoRa示例目录

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/lora/index.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

## 14.1\_示例范围

这些示例演示使用[LoRa远距离无线通信](../services_overview/P006_LoRa与LoRaWAN.md#lora-api)。

| 示例 | 功能 |
| --- | --- |
| [LoRa占空比（Duty Cycle）接收](P015_LoRa占空比示例.md#lora-duty-cycle) | 使用硬件接收占空比机制接收分组，实现无线唤醒（Wake-on-radio） |
| [LoRa接收（Receive）](P016_LoRa接收示例.md#lora-receive) | 使用LoRa无线电，以同步和异步两种模式接收分组 |
| [LoRa发送（Send）](P017_LoRa发送示例.md#lora-send) | 使用LoRa无线电每秒发送预配置载荷 |

> 译注——目录与时序：本页是官方目录，三个示例的配置和运行过程在各自译文中单独说明。“每秒”沿用原摘要，实际发送循环还包含无线传输耗时，详见发送示例的时序译注。


对应官方文档源码：[samples/drivers/lora/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/lora/index.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/lora/index.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P013_GNSS定位示例.md) · [返回大纲](大纲.md) · [下一章](P015_LoRa占空比示例.md)
