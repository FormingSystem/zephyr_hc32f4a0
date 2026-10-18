---
id: learning.zephyr-docs.basic_samples.page-54
title: MCTPI3C端点示例
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/pmci/mctp/i3c_bus_endpoint/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mctp_i3c_bus_endpoint"></a>

# 第54章\_MCTPI3C端点示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/pmci/mctp/i3c_bus_endpoint/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

[在GitHub上浏览示例源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/pmci/mctp/i3c_bus_endpoint/README.rst/..)。

<a id="overview"></a>

## 54.1 概述（Overview）

设置一个MCTP端点节点（Endpoint Node），它可以与顶层节点（Top Node）通信，并与其他MCTP端点进行对等通信。

<a id="requirements"></a>

## 54.2 要求（Requirements）

需要具有I3C接口、且该接口能够承担目标（Target）角色的开发板。

<a id="wiring"></a>

## 54.3 接线（Wiring）

通过公共I3C总线的一对SDA/SCL信号线，连接承担控制器（Controller）角色的开发板。

> 译注——实现对照：当前示例使用`MCTP_I3C_TARGET_DT_DEFINE`及`CONFIG_MCTP_I3C_TARGET`，收到消息后经工作队列向固定EID 20回复“pong”。NPCX4M8F覆盖文件设置本端EID为11，并在I3C设备中配置目标PID；MCTP EID与I3C设备PID用途不同。源码启动日志仍写成“MCTP Host”，不能据此把端点判断为控制器。原文提到对等通信能力，当前应用逻辑实际展示的是向固定总线所有者应答。

<a id="building-and-running"></a>

## 54.4 构建与运行（Building and Running）

以下为官方页面原有命令：

```sh
west build -b npcx4m8f_evb samples/subsys/pmci/mctp/i3c_bus_endpoint
west build -t run
```

> 译注——板目标与实板步骤：本页原命令的`npcx4m8f_evb`与当前板定义一致。原文的`west build -t run`不应直接当作实板烧录命令；所核对的板配置提供的是实板烧录工具（Runner）接入。下面单独给出使用当前板目标、独立构建目录和`west flash`的操作写法，未改写原命令，也未声称已完成实板验证。

> 译注——执行前提：在已准备所用Zephyr版本的Python依赖、目标工具链和该板烧录工具的UCRT64 Bash或Linux Bash中，以Zephyr源码根目录执行。先核对本页角色对应的设备树覆盖和两端连接。只有构建成功后才向对应角色的板烧录；构建失败先检查目标和配置，烧录失败先检查烧录工具及连接。通信启动后应检查两端实际收发日志，不能把固件启动或单次发送成功等同于双向交互通过。构建目录相对于当前源码根解析，不依赖作者机器位置。

```sh
west build -d build/mctp-i3c-endpoint -b npcx4m8f_evb samples/subsys/pmci/mctp/i3c_bus_endpoint
west flash -d build/mctp-i3c-endpoint
```

<a id="references"></a>

## 54.5 参考资料（References）

- [MCTP基础规范2019（MCTP Base Specification 2019）](https://www.dmtf.org/sites/default/files/standards/documents/DSP0236_1.3.1.pdf)，原文指向DSP0236 1.3.1版。


> 译注——实现依据：[samples/subsys/pmci/mctp/i3c_bus_endpoint/prj.conf](../../../samples/subsys/pmci/mctp/i3c_bus_endpoint/prj.conf)、[samples/subsys/pmci/mctp/i3c_bus_endpoint/boards/npcx4m8f_evb.overlay](../../../samples/subsys/pmci/mctp/i3c_bus_endpoint/boards/npcx4m8f_evb.overlay)、[boards/nuvoton/npcx4m8f_evb/board.yml](../../../boards/nuvoton/npcx4m8f_evb/board.yml)、[boards/nuvoton/npcx4m8f_evb/board.cmake](../../../boards/nuvoton/npcx4m8f_evb/board.cmake)。仓库内参照使用相对链接；官方main快照与本地版本可能不同，所核对文件的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/subsys/pmci/mctp/i3c_bus_endpoint/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/pmci/mctp/i3c_bus_endpoint/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/subsys/pmci/mctp/i3c_bus_endpoint/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/subsys/pmci/mctp/i3c_bus_endpoint/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P053_MCTPI2C顶层节点示例.md) · [返回大纲](大纲.md) · [下一章](P055_MCTPI3C顶层节点示例.md)
