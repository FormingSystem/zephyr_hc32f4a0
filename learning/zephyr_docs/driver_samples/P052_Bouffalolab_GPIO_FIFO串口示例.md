---
id: learning.zephyr-docs.driver_samples.page-52
title: Bouffalolab_GPIO_FIFO串口示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/gpio/bflb_bl61x_wo_uart/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bflb-bl61x-wo-uart"></a>

# 第52章\_Bouffalolab\_GPIO\_FIFO串口示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/gpio/bflb_bl61x_wo_uart/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 52.1\_概览（Overview）

本例通过实现UART，演示如何使用Bouffalolab GPIO先进先出队列（First In, First Out，FIFO）／Wire Out输出自定义协议。

可以尝试让16个引脚一起输出字符串，或者修改波特率（Baud Rate）、停止位（Stop Bit）数量、极性（Polarity）等参数。

<a id="requirements"></a>

## 52.2\_要求（Requirements）

把`app.overlay`中指定的输出引脚连接到开发板默认RX引脚，即可记录发送的消息。

也可以把UART适配器的RX接到输出引脚，并将其配置为115200波特、8N1格式。8N1表示8个数据位、无奇偶校验（No Parity）和1个停止位。

> 译注——配置来源：所读[app.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/gpio/bflb_bl61x_wo_uart/app.overlay)在wo-uart节点列出GPIO0的17、16号引脚；实际连线仍应以所用板和版本的配置为准。“16个引脚一起输出”是可扩展的实验方式，不表示随附覆盖文件已经配置16路输出。

<a id="building-and-running"></a>

## 52.3\_构建与运行（Building and Running）

可按以下方式构建本应用：

> 译注——执行位置：从已配置Zephyr环境的终端、Zephyr源码根目录执行以下原命令。先确认目标板和输出引脚配置；构建错误时先核对该板的BL61x GPIO Wire Out支持。原页只给出构建命令，固件加载方式按所用板文档处理。

```bash
# From the root of the zephyr repository
west build -b ai_m61_32s_kit samples/drivers/gpio/bflb_bl61x_wo_uart
```

若为其他受支持的板构建，把“ai_m61_32s_kit”改成该板名称。原文说明支持全部BL61x开发板。

<a id="sample-output"></a>

### 52.3.1\_示例输出（Sample Output）

开发板常规UART上的输出：

```text
*** Booting Zephyr OS build v4.3.0-5197-g336bac14b121 ***
Sent (0): Hello World!
Sent (0): Hello World!
Sent (0): Hello World!
Sent (0): Hello World!
```

指定输出引脚上的输出：

```text
Hello World!
Hello World!
Hello World!
Hello World!
```

> 译注——波形与日志：所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/gpio/bflb_bl61x_wo_uart/src/main.c)以Wire Out周期构造起始位、8个低位优先数据位和停止位，发送Hello World!及回车换行。115200是标称目标，实际周期数按硬件时钟取整；常规UART与Wire Out输出是不同路径。当前实现的发送日志为Sent:，原页中的Sent (0):保留为版本示例。本批没有生成波形或执行串口收发。

<a id="see-also"></a>

## 52.4\_相关接口（See also）

[Bouffalolab BL61x GPIO FIFO／Wire Out接口](../hardware/P283_BL61xGPIO线输出.md)。


对应官方文档源码：[samples/drivers/gpio/bflb_bl61x_wo_uart/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/gpio/bflb_bl61x_wo_uart/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/gpio/bflb_bl61x_wo_uart/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/gpio/bflb_bl61x_wo_uart/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P051_FPGA控制器示例.md) · [返回大纲](大纲.md) · [下一章](P053_eSPI接口示例.md)
