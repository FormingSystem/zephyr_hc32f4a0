---
id: learning.zephyr-docs.hardware.scmisample-1
title: SCMI平台交互示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/firmware/scmi/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="scmi"></a>

# 第599章\_SCMI平台交互示例

原文：[SCMI Platform Interaction](https://docs.zephyrproject.org/latest/samples/drivers/firmware/scmi/README.html)。读取日期：2026-10-13，`latest`。

## 599.1\_概述

此简单演示让运行 Zephyr 的**系统控制与管理接口（System Control and Management Interface，SCMI）代理（Agent）**使用不同协议与 SCMI 平台交互，打印系统部分组件的信息并对其进行配置。

[官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/firmware/scmi)提供完整实现。

## 599.2\_构建

在 Zephyr 仓库根目录，使用工作区管理工具 west 为 `imx95_evk/mimx9596/m7` 目标构建：

```shell
# From the root of the zephyr repository
west build -b imx95_evk/mimx9596/m7 samples/drivers/firmware/scmi
```

## 599.3\_交互命令与输出

示例的命令行界面提供 `scmi` 命令组，其中 `clk` 子命令组用于**时钟协议（Clock Protocol）**操作。下表翻译官方输出中的帮助说明；命令和参数名称保留原样。

| 命令 | 用法 | 中文含义 |
| --- | --- | --- |
| `version` | `version` | 取得协议版本 |
| `summary` | `summary` | 取得**时钟树（Clock Tree）**概览 |
| `info` | `info <clock_id>` | 取得指定时钟的详细信息 |
| `set-enabled` | `set-enabled <clock_id> on\|off` | 启用或禁用指定时钟 |
| `set-rate` | `set-rate <clock_id> <rate>` | 设置时钟频率，单位为赫兹（Hertz，Hz） |
| `set-parent` | `set-parent <clock_id> <parent_id>` | 设置时钟的**父时钟（Parent Clock）** |

`clock_id` 为时钟标识符，`parent_id` 为父时钟标识符，`rate` 为频率。输出表头 `ID`、`Name`、`Enabled`、`Rate(Hz)`、`Parent` 分别表示标识符、名称、启用状态、频率和父时钟；`Y` 表示已启用，`N/A` 表示没有可用对应项。

以下完整保留官方示例输出，含时钟节点名称和原始数值：

```text
uart:~$ scmi
scmi - ARM SCMI commands
Subcommands:
  clk  : Clock protocol commands
uart:~$ scmi clk
clk - Clock protocol commands
Subcommands:
  version      : get protocol version
                 Usage: version
  summary      : get clock tree summary
                 Usage: summary
  info         : get detailed clock information
                 Usage: info <clock_id>
  set-enabled  : enable/disable a clock
                 Usage: set-enabled <clock_id> on|off
  set-rate     : set a clock's rate (in Hz)
                 Usage: set-rate <clock_id> <rate>
  set-parent   : set a clock's parent
                 Usage: set-parent <clock_id> <parent_id>
uart:~$ scmi clk summary
+----------------------------------------------------------------------+
| ID |        Name        | Enabled |   Rate(Hz)  |        Parent      |
+----------------------------------------------------------------------+
|  0 |               ext  |    Y    |    25000000 |       ext_gpr_sel  |
+----------------------------------------------------------------------+
|  1 |            osc32k  |    Y    |       32768 |               N/A  |
+----------------------------------------------------------------------+
|  2 |            osc24m  |    Y    |    24000000 |               N/A  |
+----------------------------------------------------------------------+
|  3 |               fro  |    Y    |   256000000 |               N/A  |
+----------------------------------------------------------------------+
|  4 |       syspll1_vco  |    Y    |  4000000000 |               N/A  |
+----------------------------------------------------------------------+
|  5 |   syspll1_pfd0_un  |    Y    |  1000000000 |       syspll1_vco  |
+----------------------------------------------------------------------+
|  6 |      syspll1_pfd0  |    Y    |  1000000000 |   syspll1_pfd0_un  |
+----------------------------------------------------------------------+
|  7 |   syspll1_pfd0_di  |    Y    |   500000000 |   syspll1_pfd0_un  |
+----------------------------------------------------------------------+
uart:~$ scmi clk info 50
Name: lpspi2
Enabled status: Y
Rate (Hz): 50000000
Parent: syspll1_pfd1_di [10]
```

译注：这是官方页面中的示例输出，未在本翻译任务中运行，也未将其中的板卡和时钟数值改成本项目配置。

---

[上一章：固件驱动示例目录](P598_固件驱动示例目录.md) · [下一章：SCMI邮箱传输绑定](P600_SCMI邮箱传输绑定.md) · [返回大纲](大纲.md)
