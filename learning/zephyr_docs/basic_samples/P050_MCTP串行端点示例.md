---
id: learning.zephyr-docs.basic_samples.page-50
title: MCTP串行端点示例
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/pmci/mctp/endpoint/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mctp_endpoint_sample"></a>

# 第50章\_MCTP串行端点示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/pmci/mctp/endpoint/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

[在GitHub上浏览示例源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/pmci/mctp/endpoint/README.rst/..)。

<a id="overview"></a>

## 50.1 概述（Overview）

设置一个MCTP节点，通过通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）监听发往特定MCTP端点标识（Endpoint ID，EID）的“hello”消息，并用“world”响应。

<a id="requirements"></a>

## 50.2 要求（Requirements）

需要提供UART访问能力的开发板和片上系统（System on Chip，SoC），以及实现UART异步API（UART Async API）的驱动。

<a id="wiring"></a>

## 50.3 接线（Wiring）

将监听UART的引脚连接到运行MCTP主机示例的开发板：本板UART发送引脚（TX）连接主机板接收引脚（RX），本板UART接收引脚连接主机板发送引脚，两块板的地也应相连。

还可以连接逻辑分析仪（Logic Analyzer），监听UART并检查传输的数据。

> 译注——实现对照：当前实现把本地EID设为10、远端EID设为20，接收回调按发送方EID选择处理分支，再通过工作队列发送“world”。它没有比较载荷是否等于“hello”，也没有把载荷长度和消息内容作为应答条件；因此，原文描述的是示例的预期交互，不是严格的请求验证。UART设备取自设备树的`arduino_serial`节点。

<a id="building-and-running"></a>

## 50.4 构建与运行（Building and Running）

以下为官方页面原有命令：

```sh
west build -b nrf52840_nrf52840dk samples/subsys/pmci/mctp/endpoint
west build -t run
```

> 译注——板目标与实板步骤：原命令中的`nrf52840_nrf52840dk`与当前官方板目标不符，当前测试配置列出的是`nrf52840dk/nrf52840`。原文的`west build -t run`不应直接当作实板烧录命令；所核对的板配置提供的是实板烧录工具（Runner）接入。下面单独给出使用当前板目标、独立构建目录和`west flash`的操作写法，未改写原命令，也未声称已完成实板验证。

> 译注——执行前提：在已准备所用Zephyr版本的Python依赖、目标工具链和该板烧录工具的UCRT64 Bash或Linux Bash中，以Zephyr源码根目录执行。先核对本页角色对应的设备树覆盖和两端连接。只有构建成功后才向对应角色的板烧录；构建失败先检查目标和配置，烧录失败先检查烧录工具及连接。通信启动后应检查两端实际收发日志，不能把固件启动或单次发送成功等同于双向交互通过。构建目录相对于当前源码根解析，不依赖作者机器位置。

```sh
west build -d build/mctp-uart-endpoint -b nrf52840dk/nrf52840 samples/subsys/pmci/mctp/endpoint
west flash -d build/mctp-uart-endpoint
```

> 译注——测试匹配与日志版本：当前`tests.yaml`中的接收匹配使用“for eid”或“for endpoint”，而对应源码打印的是“from eid”或“from endpoint”；启动行对`EID:`后空格的写法也不一致。配置中存在这些匹配表达式并不证明当前示例能通过测试，需按实际版本核对。本文不修改上游源码或测试配置。

<a id="references"></a>

## 50.5 参考资料（References）

- [MCTP基础规范2019（MCTP Base Specification 2019）](https://www.dmtf.org/sites/default/files/standards/documents/DSP0236_1.3.1.pdf)，原文指向DSP0236 1.3.1版。


> 译注——实现依据：[samples/subsys/pmci/mctp/endpoint/tests.yaml](../../../samples/subsys/pmci/mctp/endpoint/tests.yaml)、[samples/subsys/pmci/mctp/endpoint/prj.conf](../../../samples/subsys/pmci/mctp/endpoint/prj.conf)、[samples/subsys/pmci/mctp/endpoint/boards/nrf52840dk_nrf52840.overlay](../../../samples/subsys/pmci/mctp/endpoint/boards/nrf52840dk_nrf52840.overlay)、[boards/nordic/nrf52840dk/board.yml](../../../boards/nordic/nrf52840dk/board.yml)、[boards/nordic/nrf52840dk/board.cmake](../../../boards/nordic/nrf52840dk/board.cmake)。仓库内参照使用相对链接；官方main快照与本地版本可能不同，所核对文件的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/subsys/pmci/mctp/endpoint/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/pmci/mctp/endpoint/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/subsys/pmci/mctp/endpoint/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/subsys/pmci/mctp/endpoint/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P049_MCTP示例目录.md) · [返回大纲](大纲.md) · [下一章](P051_MCTP串行主机示例.md)
