---
id: learning.zephyr-docs.snippets.page-19
title: 原生模拟器HCI_UART配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/hci-uart-native-sim/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="native-simulator-support-for-hci-uart-snippet-hci-uart-native-sim"></a>
<a id="snippet-hci-uart-native-sim"></a>

# 第19章\_原生模拟器HCI\_UART配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/hci-uart-native-sim/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

原构建格式：

```sh
west build -S hci-uart-native-sim [...]
```

<a id="overview"></a>

## 19.1 概述（Overview）

本片段允许原生模拟器（Native Simulator）使用连接到主机计算机的`hci_uart`。它适合与真实蓝牙控制器进行测试，例如与运行Zephyr的设备连接。

> 译注——设备选择：主机控制器接口（Host Controller Interface，HCI）在此通过UART传输。当前官方覆盖文件禁用`bt_hci_userchan`，创建`zephyr,native-tty-uart`串口及其`zephyr,bt-hci-uart`子节点，并把`zephyr,bt-hci`改为后者。默认串口为Linux设备路径`/dev/ttyACM0`，速率为2000000；这不是作者仓库位置，实际端口和控制器传输参数必须按连接情况匹配。


> 译注——片段源码：[snippet.yml](../../../snippets/hci-uart-native-sim/snippet.yml)、[hci-uart-native-sim.conf](../../../snippets/hci-uart-native-sim/hci-uart-native-sim.conf)、[hci-uart-native-sim.overlay](../../../snippets/hci-uart-native-sim/hci-uart-native-sim.overlay)。片段定义中的名称为`hci-uart-native-sim`；本地参照版本可能与所保存的官方main版本不同。

> 译注——构建占位符：原文`[...]`表示由读者补充的板目标、应用路径等构建参数，实际执行时不能保留方括号省略号。构建位置与片段搜索方法见[使用配置片段](P002_使用配置片段.md)。本文仅翻译和核对，没有执行这些命令。

对应官方文档源码：[snippets/hci-uart-native-sim/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/hci-uart-native-sim/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/hci-uart-native-sim/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P018_原生模拟器SocketCAN配置片段.md) · [返回大纲](大纲.md) · [下一章](P020_蓝牙LE控制器配置片段.md)
