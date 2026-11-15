---
id: learning.zephyr-docs.snippets.page-8
title: UART控制台配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/serial-console/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="uart-console-snippet-uart-console"></a>
<a id="snippet-uart-console"></a>

# 第8章\_UART控制台配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/serial-console/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 8.1 概述（Overview）

本配置片段（Snippet）启用控制台（Console）输出，输出设备为设备树`zephyr,console`所选的通用异步收发器（Universal Asynchronous Receiver-Transmitter，UART）。

> 译注——名称差异：官方页面标题写作“UART Console Snippet（uart-console）”，但当前[snippet.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/serial-console/snippet.yml)声明的名称是`serial-console`。选择片段时应以实际源码中的名称为准，使用`-S serial-console`，不要根据标题推导为`-S uart-console`。当前配置启用`CONFIG_CONSOLE`、`CONFIG_UART_CONSOLE`和`CONFIG_SERIAL`，没有另附设备树覆盖文件；串口设备仍取决于板级或应用已有的chosen配置。


> 译注——片段源码：[snippet.yml](../../../snippets/serial-console/snippet.yml)、[serial-console.conf](../../../snippets/serial-console/serial-console.conf)。片段定义中的名称为`serial-console`；本地参照版本可能与所保存的官方main版本不同。

对应官方文档源码：[snippets/serial-console/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/serial-console/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/serial-console/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P007_内置配置片段目录.md) · [返回大纲](大纲.md) · [下一章](P009_USB_CDC_ACM控制台配置片段.md)
