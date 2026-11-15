---
id: learning.zephyr-docs.snippets.page-46
title: Nordic_PPR原位执行配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/nordic/nordic-ppr-xip/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nordic-boot-ppr-snippet-with-execution-in-place-nordic-ppr-xip"></a>
<a id="nordic-ppr-xip"></a>

# 第46章\_Nordic\_PPR原位执行配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/nordic/nordic-ppr-xip/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 46.1 概述（Overview）

本片段允许构建具备下述能力的Zephyr：从另一个核心启动Nordic外设处理器（Peripheral Processor，PPR）。

PPR代码应从磁阻式随机存取存储器（Magnetoresistive Random-Access Memory，MRAM）执行，因此PPR镜像必须面向`xip`开发板变体构建，或者启用[`CONFIG_XIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XIP)，以采用原位执行（Execute in Place，XIP）。

> 译注——执行位置：当前nRF54H20覆盖把PPR的`execution-memory`设为`cpuppr_code_partition`，并删除`source-memory`属性。应同时核对启动侧设备树和PPR镜像的链接布局；这里的片段选择不会自动验证另一镜像是否已经按该位置构建。


> 译注——片段源码：[snippet.yml](../../../snippets/nordic/nordic-ppr-xip/snippet.yml)、[nordic-ppr-xip.overlay](../../../snippets/nordic/nordic-ppr-xip/nordic-ppr-xip.overlay)。片段名称为`nordic-ppr-xip`；板目标匹配规则及其追加文件见定义中的`boards`。本地参照版本可能与所保存的官方main版本不同，当前官方源码及摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[snippets/nordic/nordic-ppr-xip/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/nordic/nordic-ppr-xip/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/nordic/nordic-ppr-xip/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P045_Nordic_PPR配置片段.md) · [返回大纲](大纲.md) · [下一章](P047_Nordic独立STM日志配置片段.md)
