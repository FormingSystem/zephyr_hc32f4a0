---
id: learning.zephyr-docs.snippets.page-31
title: Espressif_4MB闪存配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/espressif/flash-4M/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="espressif-flash-4mb"></a>
<a id="espressif-flash-4m"></a>

# 第31章\_Espressif\_4MB闪存配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/espressif/flash-4M/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 31.1 概述（Overview）

本配置片段（Snippet）允许选择ESP32芯片的4 MB串行外设接口闪存（Serial Peripheral Interface Flash，SPI Flash）变体。

> 译注——容量与分区：原页面使用“4MB”的名称。当前片段按板目标匹配不同SoC的设备树覆盖文件；对应覆盖文件将`flash0`的容量设为`DT_SIZE_M(4)`，删除原`partitions`节点，并引入相应的官方分区定义。因此它不仅改变容量描述，也会影响分区布局。实际器件必须具备相应容量，片段不能增加物理Flash；已有自定义分区也需要检查与覆盖文件的关系。


> 译注——片段源码：[snippet.yml](../../../snippets/espressif/flash-4M/snippet.yml)。片段名称为`espressif-flash-4M`；板目标匹配规则及其追加文件见定义中的`boards`。本地参照版本可能与所保存的官方main版本不同，当前官方源码及摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[snippets/espressif/flash-4M/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/espressif/flash-4M/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/espressif/flash-4M/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P030_Espressif_2MB闪存配置片段.md) · [返回大纲](大纲.md) · [下一章](P032_Espressif_8MB闪存配置片段.md)
