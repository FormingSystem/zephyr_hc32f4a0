---
id: learning.zephyr-docs.snippets.page-21
title: Silicon_Labs包跟踪接口配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/silabs-pti/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="silicon-labs-packet-trace-interface-silabs-pti"></a>
<a id="silabs-pti"></a>

# 第21章\_Silicon\_Labs包跟踪接口配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/silabs-pti/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 21.1 概述（Overview）

本片段用于为Silicon Labs Series 2器件构建Zephyr应用，使无线电数据包经由包跟踪接口（Packet Trace Interface，PTI）输出，供调试工具使用。

```sh
west build -S silabs-pti [...]
```

<a id="requirements"></a>

## 21.2 要求（Requirements）

硬件须支持[`silabs,pti`](../debug_binding_reference/P006_Silicon_Labs数据包跟踪绑定.md#std-dtcompatible-silabs-pti)。

还需要节点标签（Node Label）为`pti_default`的引脚控制（Pin Control，pinctrl）配置，其中包含PTI引脚分配。

> 译注——接入条件：当前覆盖文件引用已有的`pti`节点，将`pinctrl-0`指向`pti_default`并启用该节点；配置文件启用`CONFIG_DEBUG_DRIVER`。片段不替读者决定实际管脚连线，也不意味着其他厂商芯片支持PTI。


> 译注——片段源码：[snippet.yml](../../../snippets/silabs-pti/snippet.yml)、[pti.conf](../../../snippets/silabs-pti/pti.conf)、[pti.overlay](../../../snippets/silabs-pti/pti.overlay)。片段定义中的名称为`silabs-pti`；本地参照版本可能与所保存的官方main版本不同。

> 译注——构建占位符：原文`[...]`表示由读者补充的板目标、应用路径等构建参数，实际执行时不能保留方括号省略号。构建位置与片段搜索方法见[使用配置片段](P002_使用配置片段.md)。本文仅翻译和核对，没有执行这些命令。

对应官方文档源码：[snippets/silabs-pti/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/silabs-pti/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/silabs-pti/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P020_蓝牙LE控制器配置片段.md) · [返回大纲](大纲.md) · [下一章](P022_Xen控制域配置片段.md)
