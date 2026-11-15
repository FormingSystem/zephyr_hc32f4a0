---
id: learning.zephyr-docs.snippets.page-37
title: Espressif_2MB伪静态RAM配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/espressif/psram-2M/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="espressif-psram-2mb"></a>
<a id="espressif-psram-2m"></a>

# 第37章\_Espressif\_2MB伪静态RAM配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/espressif/psram-2M/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 37.1 概述（Overview）

本配置片段允许选择ESP32芯片的2 MB SPI伪静态随机存取存储器（Pseudo-Static Random-Access Memory，PSRAM）变体。

> 译注——配置与硬件：当前片段启用`CONFIG_ESP_SPIRAM`，并把`psram0`节点的`size`设置为`DT_SIZE_M(2)`。这是对已有外接或封装内PSRAM的配置，不能使没有该存储器的硬件获得额外容量。是否支持相应接口、时序与容量，仍取决于实际板型和器件。


> 译注——片段源码：[snippet.yml](../../../snippets/espressif/psram-2M/snippet.yml)、[esp_psram.conf](../../../snippets/espressif/psram-2M/esp_psram.conf)、[soc/esp_psram_2M.overlay](../../../snippets/espressif/psram-2M/soc/esp_psram_2M.overlay)。片段名称为`espressif-psram-2M`；追加配置见定义中的`append`。本地参照版本可能与所保存的官方main版本不同，当前官方源码及摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[snippets/espressif/psram-2M/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/espressif/psram-2M/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/espressif/psram-2M/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P036_Espressif_128MB闪存配置片段.md) · [返回大纲](大纲.md) · [下一章](P038_Espressif_4MB伪静态RAM配置片段.md)
