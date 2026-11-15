---
id: learning.zephyr-docs.snippets.page-43
title: Nordic_FLPR_SRAM执行配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/nordic/nordic-flpr/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nordic-flpr-snippet-with-execution-from-sram-nordic-flpr"></a>
<a id="nordic-flpr"></a>

# 第43章\_Nordic\_FLPR\_SRAM执行配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/nordic/nordic-flpr/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 43.1 概述（Overview）

本片段允许构建具备下述能力的Zephyr：从应用核心（Application Core）启动Nordic快速轻量外设处理器（Fast Lightweight Peripheral Processor，FLPR）。

FLPR代码应从静态随机存取存储器（Static Random-Access Memory，SRAM）执行，因此构建FLPR镜像时必须不使用`xip`开发板变体，或者禁用[`CONFIG_XIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XIP)。

> 译注——启动方与执行方：这个片段配置启动FLPR的应用核心；原文对[`CONFIG_XIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XIP)的要求针对FLPR镜像，不能把两侧构建混为一份配置。当前通用覆盖文件启用`cpuflpr_vpr`，并按SoC及板型追加内存、通信或资源预留配置。例如nRF54L15覆盖中，`execution-memory`指向FLPR的SRAM区域，`source-memory`指向存放镜像的RRAM区域。具体布局并非所有支持平台相同。


> 译注——片段源码：[snippet.yml](../../../snippets/nordic/nordic-flpr/snippet.yml)、[nordic-flpr.overlay](../../../snippets/nordic/nordic-flpr/nordic-flpr.overlay)。片段名称为`nordic-flpr`；板目标匹配规则及其追加文件见定义中的`boards`。本地参照版本可能与所保存的官方main版本不同，当前官方源码及摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[snippets/nordic/nordic-flpr/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/nordic/nordic-flpr/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/nordic/nordic-flpr/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P042_Nordic配置片段目录.md) · [返回大纲](大纲.md) · [下一章](P044_Nordic_FLPR原位执行配置片段.md)
