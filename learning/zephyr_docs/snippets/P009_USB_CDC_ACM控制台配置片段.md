---
id: learning.zephyr-docs.snippets.page-9
title: USB_CDC_ACM控制台配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/cdc-acm-console/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="cdc-acm-console-snippet-cdc-acm-console"></a>
<a id="snippet-cdc-acm-console"></a>

# 第9章\_USB\_CDC\_ACM控制台配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/cdc-acm-console/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

原构建格式：

```sh
west build -S cdc-acm-console [...]
```

<a id="overview"></a>

## 9.1 概述（Overview）

本片段把串口控制台输出重定向到通信设备类抽象控制模型（Communications Device Class Abstract Control Model，CDC ACM）UART。使用哪个USB设备，由[设备树（Devicetree）](../devicetree/P013_设备树文档入口.md#devicetree)配置。

<a id="requirements"></a>

## 9.2 要求（Requirements）

硬件须支持以下配置：

- [`CONFIG_USB_DEVICE_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK)。
- [`CONFIG_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL)。
- [`CONFIG_CONSOLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CONSOLE)。
- [`CONFIG_UART_CONSOLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CONSOLE)。
- [`CONFIG_UART_LINE_CTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_LINE_CTRL)。

还需要一个节点标签（Node Label）为`zephyr_udc0`的设备树节点，指向已经启用且有驱动支持的USB设备节点。在[生成的设备树](../devicetree/P006_设备树操作指南.md#get-devicetree-outputs)中，它大致如下：

```dts
zephyr_udc0: usbd@deadbeef {
     compatible = "vnd,usb-device";
     /* ... */
};
```

> 译注——栈版本：原页面要求列出[`CONFIG_USB_DEVICE_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK)，当前官方[配置文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/cdc-acm-console/cdc-acm-console.conf)已启用`CONFIG_USB_DEVICE_STACK_NEXT`和`CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT`。原要求按来源保留，实际依赖应与所使用源码版本匹配。覆盖文件在`zephyr_udc0`下创建CDC ACM UART，并同时设置控制台和Shell串口；`usbd@deadbeef`与`vnd,usb-device`是原示意占位内容，不能直接复制为真实芯片的地址和compatible。


> 译注——片段源码：[snippet.yml](../../../snippets/cdc-acm-console/snippet.yml)、[cdc-acm-console.conf](../../../snippets/cdc-acm-console/cdc-acm-console.conf)、[cdc-acm-console.overlay](../../../snippets/cdc-acm-console/cdc-acm-console.overlay)。片段定义中的名称为`cdc-acm-console`；本地参照版本可能与所保存的官方main版本不同。

> 译注——构建占位符：原文`[...]`表示由读者补充的板目标、应用路径等构建参数，实际执行时不能保留方括号省略号。构建位置与片段搜索方法见[使用配置片段](P002_使用配置片段.md)。本文仅翻译和核对，没有执行这些命令。

对应官方文档源码：[snippets/cdc-acm-console/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/cdc-acm-console/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/cdc-acm-console/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P008_UART控制台配置片段.md) · [返回大纲](大纲.md) · [下一章](P010_RAM控制台配置片段.md)
