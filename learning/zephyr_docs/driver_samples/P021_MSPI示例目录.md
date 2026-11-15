---
id: learning.zephyr-docs.driver_samples.page-21
title: MSPI示例目录
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/mspi/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="multi-bit-spi-bus-mspi"></a>

# 第21章\_MSPI示例目录

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/mspi/index.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

## 21.1\_示例范围

这些示例演示如何使用[多位SPI总线（Multi-bit SPI Bus，MSPI）](../hardware/P065_多位SPI总线.md#mspi-api)驱动API。

| 示例 | 功能 |
| --- | --- |
| [Ambiq MSPI时序扫描（Timing Scan）](P025_Ambiq_MSPI时序扫描示例.md#mspi-timing-scan) | 为指定开发板上的指定设备寻找合适时序 |
| [JEDEC MSPI-NOR闪存](P023_MSPI_NOR闪存示例.md#mspi-flash) | 通过Flash API访问MSPI NOR串行闪存器件 |
| [MSPI异步传输（Asynchronous Transfer）](P022_MSPI异步传输示例.md#mspi-async) | 通过MSPI API异步访问MSPI存储器件 |
| [MSPI吞吐量性能测试（Throughput Performance Test）](P024_MSPI吞吐量示例.md#mspi-throughput) | 使用不同缓冲区大小和分组数量测量MSPI吞吐量 |

> 译注——阅读顺序：本页是官方目录。各子页分别说明API访问、擦写、性能测量与时序选择，不把目录页的完成算成所有示例实现已验证。


对应官方文档源码：[samples/drivers/mspi/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/mspi/index.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/mspi/index.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P020_HL78xx调制解调器示例.md) · [返回大纲](大纲.md) · [下一章](P022_MSPI异步传输示例.md)
