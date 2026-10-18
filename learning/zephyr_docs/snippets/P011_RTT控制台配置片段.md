---
id: learning.zephyr-docs.snippets.page-11
title: RTT控制台配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/rtt-console/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="rtt-console-snippet-rtt-console"></a>
<a id="snippet-rtt-console"></a>

# 第11章\_RTT控制台配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/rtt-console/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 11.1 概述（Overview）

本片段启用通过SEGGER实时传输（Real Time Transfer，RTT）输出控制台内容。

<a id="requirements"></a>

## 11.2 要求（Requirements）

需要支持：

- [`CONFIG_HAS_SEGGER_RTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SEGGER_RTT)。

> 译注——输出类型：当前片段启用`CONFIG_USE_SEGGER_RTT`、`CONFIG_CONSOLE`和`CONFIG_RTT_CONSOLE`。这用于控制台文字；SystemView跟踪另见[RTT跟踪片段](P014_SystemView_RTT跟踪配置片段.md)，两者不能仅因同用RTT就视为相同数据格式。


> 译注——片段源码：[snippet.yml](../../../snippets/rtt-console/snippet.yml)、[rtt-console.conf](../../../snippets/rtt-console/rtt-console.conf)。片段定义中的名称为`rtt-console`；本地参照版本可能与所保存的官方main版本不同。

对应官方文档源码：[snippets/rtt-console/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/rtt-console/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/rtt-console/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P010_RAM控制台配置片段.md) · [返回大纲](大纲.md) · [下一章](P012_NUS控制台配置片段.md)
