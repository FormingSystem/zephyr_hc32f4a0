---
id: learning.zephyr-docs.snippets.page-10
title: RAM控制台配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/ram-console/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ram-console-snippet-ram-console"></a>
<a id="snippet-ram-console"></a>

# 第10章\_RAM控制台配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/ram-console/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

原构建格式：

```sh
west build -S ram-console [...]
```

<a id="overview"></a>

## 10.1 概述（Overview）

本片段把控制台输出重定向到随机存取存储器（Random-Access Memory，RAM）缓冲区。默认情况下，RAM控制台缓冲区是放在RAM区域中的全局数组，构建前无法确定其地址。RAM控制台驱动也支持将缓冲区放入具有预定义地址的专用段（Section）。

<a id="how-to-enable-ram-console-buffer-section"></a>

## 10.2 启用RAM控制台缓冲区段（How to enable RAM console buffer section）

为本片段添加板级设备树覆盖文件（DTS Overlay），在`chosen`节点中加入`zephyr,ram-console`属性，并添加compatible为[`zephyr,memory-region`](../hardware/P557_内存区域绑定.md#std-dtcompatible-zephyr-memory-region)的内存区域节点，如下所示：

```dts
/ {
    chosen {
        zephyr,ram-console = &snippet_ram_console;
    };

   snippet_ram_console: memory@93d00000 {
        compatible = "zephyr,memory-region";
        reg = <0x93d00000 DT_SIZE_K(4)>;
        zephyr,memory-region = "RAM_CONSOLE";
   };
};
```

> 译注——区域与环绕：`0x93d00000`是原示例的目标内存地址，不能直接用于任意芯片。当前官方[驱动](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/console/ram_console.c)使用`CONFIG_RAM_CONSOLE_BUFFER_SIZE`并保留一个字节确保空字符结尾，写满可用部分后环绕覆盖。当前[Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/console/Kconfig)在存在启用的chosen内存节点时选择专用段模式；驱动会检查缓冲区不能超过区域大小。这是控制台文字缓冲区，与[RAM跟踪](P013_RAM跟踪配置片段.md)的事件流及写满行为不同。


> 译注——片段源码：[snippet.yml](../../../snippets/ram-console/snippet.yml)、[ram-console.conf](../../../snippets/ram-console/ram-console.conf)。片段定义中的名称为`ram-console`；本地参照版本可能与所保存的官方main版本不同。

> 译注——构建占位符：原文`[...]`表示由读者补充的板目标、应用路径等构建参数，实际执行时不能保留方括号省略号。构建位置与片段搜索方法见[使用配置片段](P002_使用配置片段.md)。本文仅翻译和核对，没有执行这些命令。

对应官方文档源码：[snippets/ram-console/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/ram-console/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/ram-console/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P009_USB_CDC_ACM控制台配置片段.md) · [返回大纲](大纲.md) · [下一章](P011_RTT控制台配置片段.md)
