---
id: learning.zephyr-docs.board-samples.page-37
title: microbit巡线机器人
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/bbc/microbit/line_follower_robot/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bbc_microbit_line_follower_robot"></a>

# 第37章\_巡线机器人（Line following robot）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/bbc/microbit/line_follower_robot/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/bbc/microbit/line_follower_robot/README.rst/..)

<a id="overview"></a>

## 37.1 概述（Overview）

本示例控制一台独立运行的巡线机器人：它使用 DFRobot Maqueen 机器人底盘，搭载 BBC micro:bit 开发板。

<a id="requirements"></a>

## 37.2 前提条件（Requirements）

构建并运行本示例需要 [DFRobot Maqueen 机器人底盘（ROB0148）](https://www.dfrobot.com/product-1783.html)与 BBC micro:bit 开发板。用黑色胶带铺设供机器人跟随的线路。按下文说明构建程序并烧录到 BBC micro:bit，开启机器人电源，再将它放到黑色线路上。

> 译注——硬件与配置对应：原文指定 ROB0148 底盘。本次官方 overlay 从 zephyr,user 取得边缘连接器 13／14 的左右巡线输入，并将 I2C motorctl 节点地址设为 0x10。源码通过左右 GPIO 电平决定电机控制命令；相近名称底盘的电机协议和引脚不一定相同，应按实际硬件核对。

<a id="building-and-running"></a>

## 37.3 构建与运行（Building and running）

> 译注——执行前提：west 命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具、west 工作区、模块与目标工具链；应用和 overlay 为官方源码，构建目录由工具生成。选择与实物一致的板目标，构建成功后再烧录，失败时检查构建输出和板文档；本次没有执行构建、烧录或硬件实验。

使用以下命令构建并烧录此示例项目：

```text
west build -b bbc_microbit samples/boards/bbc/microbit/line_follower_robot
west flash
```

<a id="sample-output"></a>

## 37.4 输出示例（Sample Output）

示例程序控制机器人沿线路行驶，不向控制台输出内容。可以观看这个[机器人视频（robot video）](https://youtu.be/tIvoHQjo8a4)，了解它的运行效果。

> 译注——输出范围：原文“不向控制台输出”指正常巡线输出；本次 main.c 在 GPIO 或 I2C 设备未就绪时仍会 printk 错误信息。应观察机器人是否沿线运动，不能仅以串口安静认定成功。原文视频是指向 YouTube 的外部链接，正文没有内嵌或随附的视频文件；这里保留原始链接。

> 译注——源码入口：[main.c](../../../samples/boards/bbc/microbit/line_follower_robot/src/main.c)；[prj.conf](../../../samples/boards/bbc/microbit/line_follower_robot/prj.conf)；[bbc_microbit.overlay](../../../samples/boards/bbc/microbit/line_follower_robot/boards/bbc_microbit.overlay)。本地链接以本文为基准相对解析，源码版本可能与本次网页不同。

对应官方文档源码：[samples/boards/bbc/microbit/line_follower_robot/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/bbc/microbit/line_follower_robot/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/bbc/microbit/line_follower_robot/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P036_microbit_LED矩阵显示.md) · [返回大纲](大纲.md) · [下一章](P038_microbit_Pong游戏.md)
