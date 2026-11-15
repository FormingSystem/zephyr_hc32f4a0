---
id: learning.zephyr-docs.snippets.page-16
title: XIAO串口控制台配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/xiao-serial-console/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="xiao-uart-serial-console-snippet-xiao-serial-console"></a>
<a id="snippet-xiao-serial-console"></a>

# 第16章\_XIAO串口控制台配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/xiao-serial-console/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 16.1 概述（Overview）

本片段通过标准XIAO通用异步收发器（Universal Asynchronous Receiver-Transmitter，UART）引脚启用控制台输出，将`zephyr,console`设置为`&xiao_serial`。

> 译注——设备节点：当前覆盖文件还启用`xiao_serial`节点并将`zephyr,shell-uart`指向它。使用前要求目标设备树确实提供该节点；“标准XIAO引脚”不等于所有开发板都具备同名串口或相同封装引脚。


> 译注——片段源码：[snippet.yml](../../../snippets/xiao-serial-console/snippet.yml)、[xiao-serial-console.conf](../../../snippets/xiao-serial-console/xiao-serial-console.conf)、[xiao-serial-console.overlay](../../../snippets/xiao-serial-console/xiao-serial-console.overlay)。片段定义中的名称为`xiao-serial-console`；本地参照版本可能与所保存的官方main版本不同。

对应官方文档源码：[snippets/xiao-serial-console/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/xiao-serial-console/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/xiao-serial-console/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P015_半主机跟踪配置片段.md) · [返回大纲](大纲.md) · [下一章](P017_Slot1分区配置片段.md)
