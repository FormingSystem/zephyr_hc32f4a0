---
id: learning.zephyr-docs.snippets.page-14
title: SystemView_RTT跟踪配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/rtt-tracing/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="systemview-rtt-tracing-snippet-rtt-tracing"></a>
<a id="snippet-rtt-tracing"></a>

# 第14章\_SystemView\_RTT跟踪配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/rtt-tracing/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

原构建格式：

```sh
west build -S rtt-tracing [...]
```

<a id="overview"></a>

## 14.1 概述（Overview）

本片段在跟踪子系统（Tracing Subsystem）中启用SEGGER SystemView的实时传输（Real Time Transfer，RTT）支持。

<a id="requirements"></a>

## 14.2 要求（Requirements）

硬件须支持：

- [`CONFIG_HAS_SEGGER_RTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SEGGER_RTT)。

> 译注——启动时机：当前官方配置启用`CONFIG_SEGGER_SYSTEMVIEW`，但将`CONFIG_SEGGER_SYSTEMVIEW_BOOT_ENABLE`和`CONFIG_SEGGER_SYSVIEW_POST_MORTEM_MODE`设为`n`。因此选择片段不表示一定在启动时自动开始记录，也不能把RTT控制台文字当作SystemView事件流。


> 译注——片段源码：[snippet.yml](../../../snippets/rtt-tracing/snippet.yml)、[rtt-tracing.conf](../../../snippets/rtt-tracing/rtt-tracing.conf)。片段定义中的名称为`rtt-tracing`；本地参照版本可能与所保存的官方main版本不同。

> 译注——构建占位符：原文`[...]`表示由读者补充的板目标、应用路径等构建参数，实际执行时不能保留方括号省略号。构建位置与片段搜索方法见[使用配置片段](P002_使用配置片段.md)。本文仅翻译和核对，没有执行这些命令。

对应官方文档源码：[snippets/rtt-tracing/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/rtt-tracing/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/rtt-tracing/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P013_RAM跟踪配置片段.md) · [返回大纲](大纲.md) · [下一章](P015_半主机跟踪配置片段.md)
