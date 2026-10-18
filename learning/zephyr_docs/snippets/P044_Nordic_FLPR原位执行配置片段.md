---
id: learning.zephyr-docs.snippets.page-44
title: Nordic_FLPR原位执行配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/nordic/nordic-flpr-xip/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nordic-flpr-snippet-with-execution-in-place-nordic-flpr-xip"></a>
<a id="nordic-flpr-xip"></a>

# 第44章\_Nordic\_FLPR原位执行配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/nordic/nordic-flpr-xip/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 44.1 概述（Overview）

本片段允许构建具备下述能力的Zephyr：从应用核心（Application Core）启动Nordic快速轻量外设处理器（Fast Lightweight Peripheral Processor，FLPR）。

FLPR代码应从电阻式随机存取存储器（Resistive Random-Access Memory，RRAM）执行，因此FLPR镜像必须面向`xip`开发板变体构建，或者启用[`CONFIG_XIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XIP)。这里的XIP指原位执行（Execute in Place）。

> 译注——镜像匹配：启用启动侧片段不等于已经把另一核心镜像改成XIP布局。当前nRF54L15覆盖把`execution-memory`设为`cpuflpr_rram`；nRF54H20覆盖则引用`cpuflpr_code_partition`并删除`source-memory`属性。原文以RRAM描述执行位置，实际节点及存储介质应依据所用SoC和镜像布局核对，不能直接照搬其他器件的地址。


> 译注——片段源码：[snippet.yml](../../../snippets/nordic/nordic-flpr-xip/snippet.yml)、[nordic-flpr-xip.overlay](../../../snippets/nordic/nordic-flpr-xip/nordic-flpr-xip.overlay)。片段名称为`nordic-flpr-xip`；板目标匹配规则及其追加文件见定义中的`boards`。本地参照版本可能与所保存的官方main版本不同，当前官方源码及摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[snippets/nordic/nordic-flpr-xip/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/nordic/nordic-flpr-xip/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/nordic/nordic-flpr-xip/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P043_Nordic_FLPR_SRAM执行配置片段.md) · [返回大纲](大纲.md) · [下一章](P045_Nordic_PPR配置片段.md)
