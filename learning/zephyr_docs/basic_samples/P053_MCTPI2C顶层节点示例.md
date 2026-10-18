---
id: learning.zephyr-docs.basic_samples.page-53
title: MCTPI2C顶层节点示例
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/pmci/mctp/i2c_gpio_bus_host/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mctp_i2c_bus_host"></a>

# 第53章\_MCTPI2C顶层节点示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/pmci/mctp/i2c_gpio_bus_host/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

[在GitHub上浏览示例源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/pmci/mctp/i2c_gpio_bus_host/README.rst/..)。

<a id="overview"></a>

## 53.1 概述（Overview）

设置一个MCTP顶层节点（Top Node），通过I2C与任意数量的已连接端点（Endpoint）通信。

<a id="requirements"></a>

## 53.2 要求（Requirements）

需要具有I2C接口及若干GPIO的开发板，每个连接到总线的端点通过相应GPIO触发通知。

<a id="wiring"></a>

## 53.3 接线（Wiring）

使用公共I2C总线的一对SDA/SCL信号线连接任意数量的开发板，并在设备树中配置。每块端点板还应有一根GPIO信号线，用于通知该端点的写请求（Endpoint Write Request）。

> 译注——实现对照：当前实现的本地EID为20，依次向配置列表中的各端点发送“ping”，每次发送后休眠1000毫秒。FRDM-MCXN947覆盖文件将EID 11、12分别映射到十进制I2C地址70、71及各自的GPIO。端点列表、总线地址、信号线与实际连接必须一致；原文中的“任意数量”不表示会自动发现并配置任意接入设备。

<a id="building-and-running"></a>

## 53.4 构建与运行（Building and Running）

以下为官方页面原有命令：

```sh
west build -b frdm_mcxn947_mcxn947_cpu0 samples/subsys/pmci/mctp/i2c_gpio_bus_host
west build -t run
```

> 译注——板目标与实板步骤：原命令使用下划线形式的`frdm_mcxn947_mcxn947_cpu0`，当前板目标为`frdm_mcxn947/mcxn947/cpu0`。原文的`west build -t run`不应直接当作实板烧录命令；所核对的板配置提供的是实板烧录工具（Runner）接入。下面单独给出使用当前板目标、独立构建目录和`west flash`的操作写法，未改写原命令，也未声称已完成实板验证。

> 译注——执行前提：在已准备所用Zephyr版本的Python依赖、目标工具链和该板烧录工具的UCRT64 Bash或Linux Bash中，以Zephyr源码根目录执行。先核对本页角色对应的设备树覆盖和两端连接。只有构建成功后才向对应角色的板烧录；构建失败先检查目标和配置，烧录失败先检查烧录工具及连接。通信启动后应检查两端实际收发日志，不能把固件启动或单次发送成功等同于双向交互通过。构建目录相对于当前源码根解析，不依赖作者机器位置。

```sh
west build -d build/mctp-i2c-host -b frdm_mcxn947/mcxn947/cpu0 samples/subsys/pmci/mctp/i2c_gpio_bus_host
west flash -d build/mctp-i2c-host
```

<a id="references"></a>

## 53.5 参考资料（References）

- [MCTP基础规范2019（MCTP Base Specification 2019）](https://www.dmtf.org/sites/default/files/standards/documents/DSP0236_1.3.1.pdf)，原文指向DSP0236 1.3.1版。


> 译注——实现依据：[samples/subsys/pmci/mctp/i2c_gpio_bus_host/tests.yaml](../../../samples/subsys/pmci/mctp/i2c_gpio_bus_host/tests.yaml)、[samples/subsys/pmci/mctp/i2c_gpio_bus_host/prj.conf](../../../samples/subsys/pmci/mctp/i2c_gpio_bus_host/prj.conf)、[samples/subsys/pmci/mctp/i2c_gpio_bus_host/boards/frdm_mcxn947_mcxn947_cpu0.overlay](../../../samples/subsys/pmci/mctp/i2c_gpio_bus_host/boards/frdm_mcxn947_mcxn947_cpu0.overlay)、[boards/nxp/frdm_mcxn947/board.yml](../../../boards/nxp/frdm_mcxn947/board.yml)、[boards/nxp/frdm_mcxn947/board.cmake](../../../boards/nxp/frdm_mcxn947/board.cmake)。仓库内参照使用相对链接；官方main快照与本地版本可能不同，所核对文件的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/subsys/pmci/mctp/i2c_gpio_bus_host/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/pmci/mctp/i2c_gpio_bus_host/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/subsys/pmci/mctp/i2c_gpio_bus_host/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/subsys/pmci/mctp/i2c_gpio_bus_host/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P052_MCTPI2C端点示例.md) · [返回大纲](大纲.md) · [下一章](P054_MCTPI3C端点示例.md)
