---
id: learning.zephyr-docs.snippets.page-47
title: Nordic独立STM日志配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/nordic/nordic-log-stm/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nordic-standalone-stm-logging-snippet-nordic-log-stm"></a>
<a id="nordic-log-stm"></a>

# 第47章\_Nordic独立STM日志配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/nordic/nordic-log-stm/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 47.1 概述（Overview）

本片段允许构建将日志写入CoreSight系统跟踪宏单元（System Trace Macrocell，STM）激励端口（Stimulus Port）的Zephyr。

数据收集到嵌入式跟踪路由器（Embedded Trace Router，ETR）缓冲区。ETR缓冲区中的数据被解码后，以人可读的形式通过通用异步收发器（Universal Asynchronous Receiver-Transmitter，UART）输出。

> 译注——本地解码：当前配置启用STMESP日志前端及`CONFIG_LOG_FRONTEND_STMESP_FSC`；nRF54H20应用核覆盖启用TBM并将CoreSight模式设为`stm-etr`。这一页面强调UART上的人可读输出，与[字典日志片段](P048_Nordic字典STM日志配置片段.md)输出待解码数据的流程不同。具体数据通路见[CoreSight系统跟踪日志](../observability/P012_CoreSight系统跟踪日志.md)。


> 译注——片段源码：[snippet.yml](../../../snippets/nordic/nordic-log-stm/snippet.yml)、[log_stm.conf](../../../snippets/nordic/nordic-log-stm/log_stm.conf)。片段名称为`nordic-log-stm`；板目标匹配规则及其追加文件见定义中的`boards`。本地参照版本可能与所保存的官方main版本不同，当前官方源码及摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[snippets/nordic/nordic-log-stm/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/nordic/nordic-log-stm/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/nordic/nordic-log-stm/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P046_Nordic_PPR原位执行配置片段.md) · [返回大纲](大纲.md) · [下一章](P048_Nordic字典STM日志配置片段.md)
