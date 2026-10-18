---
id: learning.zephyr-docs.board-samples.page-51
title: Raspberry_Pi板信息
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/raspberrypi/rpi_board_info/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="rpi-board-info"></a>

# 第51章\_Raspberry Pi 开发板信息（Raspberry Pi Board Info）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/raspberrypi/rpi_board_info/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/raspberrypi/rpi_board_info/README.rst/..)

<a id="overview"></a>

## 51.1 概述（Overview）

本示例展示如何通过 Raspberry Pi VideoCore 固件接口查询 Raspberry Pi 特有的开发板信息。

> 译注——接口适用范围：这是通过 VideoCore 固件邮箱查询板信息的示例，使用 raspberrypi,bcm283x-firmware 设备；它与上一页 Pico W 的 CYW43 接口不同，不能在 Pico 微控制器上直接套用。

应用通过 VideoCore 固件邮箱接口（Mailbox interface）取得开发板修订码，并将它解码为便于阅读的字段，例如：

- 开发板修订编号（Board revision number）。

- 开发板类型（例如 Pi 4 Model B rev 1.4）。

- 处理器类型（例如 BCM2711）。

- 已安装内存容量（例如 2 GB）。

- 制造商（例如 Sony UK）。

这展示了如何利用底层固件通信，在运行时识别硬件细节。

> 译注——修订码解码边界：本次源码按 new-style 编码拆出内存、厂商、处理器、板型与修订字段，并用有限查找表显示名称；旧式或未知修订码不能自动得到完整准确名称。它不是运行内存容量测试，也不是从 Linux 系统文件读取信息。

<a id="requirements"></a>

## 51.2 前提条件（Requirements）

本示例需要 Raspberry Pi 开发板，例如：

- Raspberry Pi 4 Model B（`rpi_4b`）

<a id="building-and-running"></a>

## 51.3 构建与运行（Building and Running）

> 译注——执行前提：west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具、工作区、模块和目标工具链；应用与 overlay 为官方源码，构建目录由工具生成。构建成功后按具体板文档处理下载与启动，不能把通用 west flash 视为所有板都采用同一种连接方式。失败时先检查构建输出、目标板配置和实际硬件；本次没有运行这些命令或进行实板测量。

```text
# From the root of the zephyr repository
west build -b rpi_4b samples/boards/raspberrypi/rpi_board_info
west flash
```

<a id="sample-output"></a>

## 51.4 输出示例（Sample Output）

> 译注——输出含义：Board revision 为原始修订码，Board type 为板型，Processor 为处理器，Memory 为编码表示的内存容量，Manufacturer 为制造商。原文 0x00b03114、Pi 4 Model B rev 1.4、BCM2711、2GB、Sony UK 是同一示例板的结果，不能用这些值判断另一块板是否正常。

```text
*** Booting Zephyr OS build v4.4.0-rc1-337-g31a485318520 ***
--- Raspberry Pi Board Info ---
Board revision   : 0x00b03114
Board type       : Pi 4 Model B rev 1.4
Processor        : BCM2711
Memory           : 2GB
Manufacturer     : Sony UK
-------------------------------
```

> 译注——源码入口：[main.c](../../../samples/boards/raspberrypi/rpi_board_info/src/main.c)；[prj.conf](../../../samples/boards/raspberrypi/rpi_board_info/prj.conf)。本地参照实现使用相对路径，版本可能与本次网页不同。

对应官方文档源码：[samples/boards/raspberrypi/rpi_board_info/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/raspberrypi/rpi_board_info/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/raspberrypi/rpi_board_info/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P050_Pico_W的WiFi与LED.md) · [返回大纲](大纲.md) · [下一章](P052_Raspberry_Pi示例目录.md)
