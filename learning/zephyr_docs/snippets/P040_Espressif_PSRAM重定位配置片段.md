---
id: learning.zephyr-docs.snippets.page-40
title: Espressif_PSRAM重定位配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/espressif/psram-reloc/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="espressif-psram-relocations"></a>
<a id="espressif-psram-reloc"></a>

# 第40章\_Espressif\_PSRAM重定位配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/espressif/psram-reloc/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 40.1 概述（Overview）

本片段允许启用将Flash中的段（Section）重定位（Relocation）到伪静态随机存取存储器（Pseudo-Static Random-Access Memory，PSRAM）的功能。

> 译注——当前开关：片段启用`CONFIG_ESP_SPIRAM`、`CONFIG_SPIRAM_FETCH_INSTRUCTIONS`和`CONFIG_SPIRAM_RODATA`，涉及从PSRAM取指令及放置只读数据。它没有在这个配置文件中选择PSRAM容量；实际存储器、容量和平台支持仍须具备，不能理解为任意Flash内容都自动搬移。


> 译注——片段源码：[snippet.yml](../../../snippets/espressif/psram-reloc/snippet.yml)、[esp_psram_reloc.conf](../../../snippets/espressif/psram-reloc/esp_psram_reloc.conf)。片段名称为`espressif-psram-reloc`；追加配置见定义中的`append`。本地参照版本可能与所保存的官方main版本不同，当前官方源码及摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[snippets/espressif/psram-reloc/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/espressif/psram-reloc/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/espressif/psram-reloc/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P039_Espressif_8MB伪静态RAM配置片段.md) · [返回大纲](大纲.md) · [下一章](P041_Espressif_PSRAM网络缓冲配置片段.md)
