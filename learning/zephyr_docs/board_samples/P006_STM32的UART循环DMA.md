---
id: learning.zephyr-docs.board-samples.page-6
title: STM32的UART循环DMA
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/st/uart/circular_dma/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="uart-circular-dma"></a>

# 第6章\_UART 循环模式（UART circular mode）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/st/uart/circular_dma/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/uart/circular_dma/README.rst/..)

<a id="overview"></a>

## 6.1 概述（Overview）

本示例演示 STM32 UART 串口驱动如何使用循环模式 DMA，读取控制台数据并回显。

> 译注——数据通路：本次源码用异步 UART 回调接收数据，经软件环形缓冲区交给线程，再以轮询方式回显。RX 缓冲区为 10 字节，软件环形缓冲区为 1000 字节；这是示例实现，不代表循环 DMA 能无限保存数据或保证任意速率下零丢失。串口波特率取设备树 `current-speed`，还须与终端一致。

默认使用通常分配给 Zephyr Shell 的 UART 外设，因此大多数开发板应能运行本示例。

> 译注——UART 选择与 DMA 配置：源码通过 `DT_CHOSEN(zephyr_shell_uart)` 选择 UART，这表示使用该设备树选择项，不代表本例正在运行完整 Shell。官方板级覆盖文件还需配置 RX DMA、循环模式、相关控制器及请求映射；仅启用 UART 不能自动获得循环 DMA。另一板须使用自己的 DMA 控制器和请求编号。

<a id="building-and-running"></a>

## 6.2 构建与运行（Building and Running）

> 译注——执行环境与文件：以下构建命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具链、west 工作区和相应板定义；`samples/...` 是官方原有应用目录。原命令给出的板名仅对应示例，未显式给出 `-b` 时应指定实际受支持的板，不能依赖未知缓存。设备树和 Kconfig 片段写入相应配置文件，不作为终端命令执行；构建输出由工具生成。构建成功后按板文档烧录，并按正文核对串口或硬件现象，失败时回查配置、设备就绪和连接条件。本次仅翻译与核对来源，未执行构建、烧录或硬件实验。

按以下方式构建并烧录，将 `nucleo_g071rb` 替换为所用开发板：

```text
west build -b nucleo_g071rb samples/boards/st/uart/circular_dma
west flash
```

<a id="sample-output"></a>

### 6.2.1 输出示例（Sample Output）

```text
Enter message to fill RX buffer size and press enter :
# Type e.g. :
# "Lorem Ipsum is simply dummy text of the printing and typesetting industry.
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
# when an unknown printer took a galley of type and scrambled it to make a type specimen book.
# It has survived not only five centuries, but also the leap into electronic typesetting,
# remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing software
# like Aldus PageMaker including versions of Lorem Ipsum."

Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting,
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, and more recently with desktop publishing software
like Aldus PageMaker including versions of Lorem Ipsum.
```

<a id="see-also"></a>

## 6.3 另请参阅（See also）

[UART](../hardware/P330_UART公共接口.md)

> 译注——源码入口：[samples/boards/st/uart/circular_dma/src/main.c](../../../samples/boards/st/uart/circular_dma/src/main.c)；[samples/boards/st/uart/circular_dma/prj.conf](../../../samples/boards/st/uart/circular_dma/prj.conf)。链接相对于所在译文，可随仓库移动；本地源码版本可能与官网快照不同。

对应官方文档源码：[samples/boards/st/uart/circular_dma/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/st/uart/circular_dma/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/st/uart/circular_dma/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P005_STM32的PWM主模式.md) · [返回大纲](大纲.md) · [下一章](P007_STM32单线UART.md)
