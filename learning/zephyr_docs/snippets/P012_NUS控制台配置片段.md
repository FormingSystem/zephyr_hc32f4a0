---
id: learning.zephyr-docs.snippets.page-12
title: NUS控制台配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/nus-console/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nus-console-snippet-nus-console"></a>
<a id="snippet-nus-console"></a>

# 第12章\_NUS控制台配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/nus-console/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

原构建格式：

```sh
west build -S nus-console [...]
```

<a id="overview"></a>

## 12.1 概述（Overview）

本片段把串口控制台输出重定向到基于Nordic UART服务（Nordic UART Service，NUS）的UART实例，传输使用低功耗蓝牙（Bluetooth Low Energy，Bluetooth LE）。使用的蓝牙串口设备应通过[设备树（Devicetree）](../devicetree/P013_设备树文档入口.md#devicetree)配置。

<a id="requirements"></a>

## 12.2 要求（Requirements）

硬件须支持：

- [`CONFIG_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT)。
- [`CONFIG_BT_PERIPHERAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PERIPHERAL)。
- [`CONFIG_BT_ZEPHYR_NUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ZEPHYR_NUS)。
- [`CONFIG_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL)。
- [`CONFIG_CONSOLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CONSOLE)。
- [`CONFIG_UART_CONSOLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CONSOLE)。

> 译注——实例：当前官方覆盖文件创建compatible为`zephyr,nus-uart`的节点，并将控制台与Shell串口同时指向它。配置文件启用蓝牙外设、NUS、UART蓝牙驱动及自动启动蓝牙，并调整部分数据包缓冲配置；这不会把普通有线串口自动变成蓝牙控制器，仍须有相应蓝牙硬件和驱动。


> 译注——片段源码：[snippet.yml](../../../snippets/nus-console/snippet.yml)、[nus-console.conf](../../../snippets/nus-console/nus-console.conf)、[nus-console.overlay](../../../snippets/nus-console/nus-console.overlay)。片段定义中的名称为`nus-console`；本地参照版本可能与所保存的官方main版本不同。

> 译注——构建占位符：原文`[...]`表示由读者补充的板目标、应用路径等构建参数，实际执行时不能保留方括号省略号。构建位置与片段搜索方法见[使用配置片段](P002_使用配置片段.md)。本文仅翻译和核对，没有执行这些命令。

对应官方文档源码：[snippets/nus-console/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/nus-console/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/nus-console/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P011_RTT控制台配置片段.md) · [返回大纲](大纲.md) · [下一章](P013_RAM跟踪配置片段.md)
