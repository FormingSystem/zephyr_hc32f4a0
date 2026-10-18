---
id: learning.zephyr-docs.board-samples.page-7
title: STM32单线UART
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/st/uart/single_wire/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="uart-stm32-single-wire"></a>

# 第7章\_单线 UART（Single-wire UART）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/st/uart/single_wire/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/uart/single_wire/README.rst/..)

<a id="overview"></a>

## 7.1 概述（Overview）

本简单应用演示 STM32 设备的单线／半双工 UART 功能，只需少量适配即可在多种 STM32 开发板上运行。在硬件映射中为开发板添加 `single_wire_uart_loopback` 测试夹具（Fixture），即可让 Twister 自动检查本示例输出。

<a id="hardware-setup"></a>

## 7.2 硬件连接（Hardware Setup）

需要在开发板的 UART 引脚之间建立物理连接；具体引脚连接方式请参阅对应的板级覆盖文件。

> 译注——物理连线与测试夹具：本例有两个 UART 设备，设备树别名为 `single-line-uart1` 和 `single-line-uart2`。官方 stm32f3_disco 覆盖文件分别选 USART2 的 PA2 与 UART4 的 PC10，并为两者启用 `single-wire`；其他板必须查自己的覆盖文件。Twister 中的 `single_wire_uart_loopback` 只是声明测试夹具存在，不能代替实际连接。

<a id="building-and-running"></a>

## 7.3 构建与运行（Building and Running）

> 译注——执行环境与文件：以下构建命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具链、west 工作区和相应板定义；`samples/...` 是官方原有应用目录。原命令给出的板名仅对应示例，未显式给出 `-b` 时应指定实际受支持的板，不能依赖未知缓存。设备树和 Kconfig 片段写入相应配置文件，不作为终端命令执行；构建输出由工具生成。构建成功后按板文档烧录，并按正文核对串口或硬件现象，失败时回查配置、设备就绪和连接条件。本次仅翻译与核对来源，未执行构建、烧录或硬件实验。

按以下方式构建并烧录，将 `stm32f3_disco` 替换为所用开发板：

> ```text
> west build -b stm32f3_disco samples/boards/st/uart/single_wire
> west flash
> ```

烧录后，控制台不应出现失败报告，而应每隔 2 秒重复输出以下消息：

> 译注——收发节拍：源码从第一个 UART 轮询发送字符 `c`，等待 50 毫秒后从第二个 UART 读取，随后休眠 2000 毫秒。因此原文“每 2 秒”是概括描述；成功输出为 Received c（收到字符 c），失败报告或设备未就绪应先回查节点、引脚、连线与波特率。

```text
Received c
```

<a id="see-also"></a>

## 7.4 另请参阅（See also）

[UART](../hardware/P330_UART公共接口.md)

> 译注——源码入口：[samples/boards/st/uart/single_wire/src/main.c](../../../samples/boards/st/uart/single_wire/src/main.c)；[samples/boards/st/uart/single_wire/prj.conf](../../../samples/boards/st/uart/single_wire/prj.conf)。链接相对于所在译文，可随仓库移动；本地源码版本可能与官网快照不同。

对应官方文档源码：[samples/boards/st/uart/single_wire/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/st/uart/single_wire/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/st/uart/single_wire/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P006_STM32的UART循环DMA.md) · [返回大纲](大纲.md) · [下一章](P008_STM32的PWM示例目录.md)
