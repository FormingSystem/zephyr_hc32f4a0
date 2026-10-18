---
id: learning.zephyr-docs.snippets.page-49
title: Nordic字典STM_TPIU日志配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/nordic/nordic-log-stm-tpiu-dict/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nordic-dictionary-based-stm-to-tpiu-logging-snippet-nordic-log-stm-tpiu-dict"></a>
<a id="nordic-log-stm-tpiu-dict"></a>

# 第49章\_Nordic字典STM\_TPIU日志配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/nordic/nordic-log-stm-tpiu-dict/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 49.1 概述（Overview）

本片段允许构建将基于字典的日志（Dictionary-based Logging）写入CoreSight系统跟踪宏单元（System Trace Macrocell，STM）激励端口（Stimulus Port）的Zephyr。

数据写入跟踪端口接口单元（Trace Port Interface Unit，TPIU）接口，可使用`nrfutil trace`采集，并转换为人可读格式。

> 译注——硬件出口：当前nRF54H20应用核覆盖将CoreSight模式设为`stm-tpiu`，并引用`tpiu_default`引脚控制配置。它与使用ETR缓冲区后经UART输出的片段是不同的数据通路，采集工具与连接条件也应按TPIU配置准备。详细关系见[CoreSight系统跟踪日志](../observability/P012_CoreSight系统跟踪日志.md)。


> 译注——片段源码：[snippet.yml](../../../snippets/nordic/nordic-log-stm-tpiu-dict/snippet.yml)、[log_stm_dict.conf](../../../snippets/nordic/nordic-log-stm-tpiu-dict/log_stm_dict.conf)。片段名称为`nordic-log-stm-tpiu-dict`；板目标匹配规则及其追加文件见定义中的`boards`。本地参照版本可能与所保存的官方main版本不同，当前官方源码及摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[snippets/nordic/nordic-log-stm-tpiu-dict/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/nordic/nordic-log-stm-tpiu-dict/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/nordic/nordic-log-stm-tpiu-dict/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P048_Nordic字典STM日志配置片段.md) · [返回大纲](大纲.md) · [下一章](P050_TI配置片段目录.md)
