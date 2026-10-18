---
id: learning.zephyr-docs.snippets.page-41
title: Espressif_PSRAM网络缓冲配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/espressif/psram-wifi/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="espressif-psram-wi-fi-buffers"></a>
<a id="espressif-psram-wifi"></a>

# 第41章\_Espressif\_PSRAM网络缓冲配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/espressif/psram-wifi/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 41.1 概述（Overview）

本片段允许把Wi-Fi缓冲区配置为使用伪静态随机存取存储器（Pseudo-Static Random-Access Memory，PSRAM）。

> 译注——当前开关：配置文件设置`CONFIG_ESP_WIFI_HEAP_SPIRAM`和`CONFIG_ESP32_WIFI_NET_ALLOC_SPIRAM`。它用于选择Wi-Fi相关堆与网络分配的PSRAM路径，不是选择PSRAM容量的片段，也不表示所有应用缓冲区都改放到PSRAM。


> 译注——片段源码：[snippet.yml](../../../snippets/espressif/psram-wifi/snippet.yml)、[esp_psram_wifi.conf](../../../snippets/espressif/psram-wifi/esp_psram_wifi.conf)。片段名称为`espressif-psram-wifi`；追加配置见定义中的`append`。本地参照版本可能与所保存的官方main版本不同，当前官方源码及摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[snippets/espressif/psram-wifi/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/espressif/psram-wifi/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/espressif/psram-wifi/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P040_Espressif_PSRAM重定位配置片段.md) · [返回大纲](大纲.md) · [下一章](P042_Nordic配置片段目录.md)
