---
id: learning.zephyr-docs.snippets.page-45
title: Nordic_PPR配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/nordic/nordic-ppr/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nordic-ppr-snippet-nordic-ppr"></a>
<a id="nordic-ppr"></a>

# 第45章\_Nordic\_PPR配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/nordic/nordic-ppr/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 45.1 概述（Overview）

本片段允许构建具备下述能力的Zephyr：从另一个核心启动Nordic外设处理器（Peripheral Processor，PPR）。

> 译注——原页范围：本页原文只说明从另一核心启动PPR，没有给出编译、装载和运行整套命令。当前通用覆盖文件启用`cpuppr_vpr`，板级规则再追加相应SoC覆盖；它不能代替PPR镜像本身的构建及匹配。需要原位执行的对应片段见[下一章](P046_Nordic_PPR原位执行配置片段.md)。


> 译注——片段源码：[snippet.yml](../../../snippets/nordic/nordic-ppr/snippet.yml)、[nordic-ppr.overlay](../../../snippets/nordic/nordic-ppr/nordic-ppr.overlay)。片段名称为`nordic-ppr`；板目标匹配规则及其追加文件见定义中的`boards`。本地参照版本可能与所保存的官方main版本不同，当前官方源码及摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[snippets/nordic/nordic-ppr/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/nordic/nordic-ppr/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/nordic/nordic-ppr/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P044_Nordic_FLPR原位执行配置片段.md) · [返回大纲](大纲.md) · [下一章](P046_Nordic_PPR原位执行配置片段.md)
