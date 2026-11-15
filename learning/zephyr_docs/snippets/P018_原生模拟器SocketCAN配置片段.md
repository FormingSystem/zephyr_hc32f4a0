---
id: learning.zephyr-docs.snippets.page-18
title: 原生模拟器SocketCAN配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/socketcan-native-sim/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="socketcan-on-native-simulator-snippet-socketcan-native-sim"></a>
<a id="snippet-socketcan-native-sim"></a>

# 第18章\_原生模拟器SocketCAN配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/socketcan-native-sim/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

原构建格式：

```sh
west build -S socketcan-native-sim [...]
```

<a id="overview"></a>

## 18.1 概述（Overview）

本片段在[原生模拟器（Native Simulator，native_sim）](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)上启用Linux SocketCAN支持。

默认情况下，原生模拟器期望存在名为`zcan0`的SocketCAN网络设备，该名称在[boards/native/native_sim/native_sim.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/native/native_sim/native_sim.dts)中指定。可以为已有SocketCAN网络设备添加这一备用名称（Alternative Name）。下面以新建的虚拟控制器局域网（Virtual CAN）设备`vcan0`为例：

```sh
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link property add dev vcan0 altname zcan0
```

在运行原生模拟器之前，必须配置并启用SocketCAN设备：

```sh
sudo ip link set vcan0 up
```

> 译注——执行环境：`modprobe`和`ip link`属于Linux主机网络配置，原命令会创建并启用虚拟接口；它们不在Zephyr Shell或Windows PowerShell中执行。当前片段启用CAN并使设备树`can0`节点可用，将`zephyr,canbus`指向该节点。虚拟CAN测试不等于验证物理收发器或实际总线接线。


> 译注——片段源码：[snippet.yml](../../../snippets/socketcan-native-sim/snippet.yml)、[socketcan-native-sim.conf](../../../snippets/socketcan-native-sim/socketcan-native-sim.conf)、[socketcan-native-sim.overlay](../../../snippets/socketcan-native-sim/socketcan-native-sim.overlay)。片段定义中的名称为`socketcan-native-sim`；本地参照版本可能与所保存的官方main版本不同。

> 译注——构建占位符：原文`[...]`表示由读者补充的板目标、应用路径等构建参数，实际执行时不能保留方括号省略号。构建位置与片段搜索方法见[使用配置片段](P002_使用配置片段.md)。本文仅翻译和核对，没有执行这些命令。

对应官方文档源码：[snippets/socketcan-native-sim/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/socketcan-native-sim/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/socketcan-native-sim/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P017_Slot1分区配置片段.md) · [返回大纲](大纲.md) · [下一章](P019_原生模拟器HCI_UART配置片段.md)
