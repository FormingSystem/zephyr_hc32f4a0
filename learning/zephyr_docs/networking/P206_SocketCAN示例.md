---
id: learning.zephyr-docs.networking.page-206
title: SocketCAN示例
kind: reference
status: maintained
domains: [zephyr, networking, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/can/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="socket-can"></a>

# 第206章\_SocketCAN示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/can/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 206.1 概述（Overview）

SocketCAN示例是一个服务器／客户端应用，使用BSD套接字API发送和接收原始CAN帧（Raw CAN frame）。应用由以下功能组成：

- 设置函数：创建CAN套接字，将其绑定到CAN网络接口，再为套接字安装CAN过滤器，使应用能够接收CAN帧。
- 接收函数：开始监听CAN套接字，并打印CAN帧信息。
- 发送函数：开始向总线发送原始CAN帧。

源码位于[samples/net/sockets/can](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/can)。

<a id="requirements"></a>

## 206.2 要求（Requirements）

需要支持CAN总线（CANBUS）的开发板，例如[Nucleo L432KC](https://docs.zephyrproject.org/latest/boards/st/nucleo_l432kc/doc/index.html#nucleo_l432kc)或[STM32F072B Discovery](https://docs.zephyrproject.org/latest/boards/st/stm32f072b_disco/doc/index.html#stm32f072b_disco)。

<a id="building-and-running"></a>

## 206.3 构建与运行（Building and Running）

按以下方式构建SocketCAN示例：

```sh
west build -b <board to use> samples/net/sockets/can -- -DCONF_FILE=<config file to use>
```

面向`nucleo_l432kc`的原文示例：

```sh
west build -b nucleo_l432kc samples/net/sockets/can
west build -t run
```

> 译注——硬件运行与回环：原文使用`west build -t run`，但该命令是否可用取决于目标板提供的运行目标；真实开发板应按对应板级文档完成烧录与观察，不能把此命令直接当作通用烧录命令。当前示例的`CONFIG_SAMPLE_SOCKETCAN_LOOPBACK_MODE`默认启用，先将控制器设置为回环模式（Loopback mode），因此无需第二块板也能演示收发；这不等于验证了外部CAN总线。源码默认发送ID为`0x1`、长度为8字节的帧，数据为`F0`至`F7`，过滤器也匹配该标准ID。

<a id="see-also"></a>

## 206.4 另请参阅（See also）

[BSD套接字兼容API（BSD Sockets compatible API）](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)、[SocketCAN库（SocketCAN library）](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html)。


> 译注——实现依据：[samples/net/sockets/can/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/sockets/can/Kconfig)、[samples/net/sockets/can/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/sockets/can/src/main.c)。以上为本次核对的官方来源；分支内容可能继续变化，保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库相对链接用于版本对照。

对应官方文档源码：[samples/net/sockets/can/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/sockets/can/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/net/sockets/can/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/net/sockets/can/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P205_套接字对示例.md) · [返回大纲](大纲.md) · [下一章](P207_网络统计示例.md)
