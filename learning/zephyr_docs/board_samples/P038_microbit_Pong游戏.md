---
id: learning.zephyr-docs.board-samples.page-38
title: microbit_Pong游戏
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/bbc/microbit/pong/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bbc_microbit_pong"></a>

# 第38章\_Pong 游戏（Pong game）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/bbc/microbit/pong/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/bbc/microbit/pong/README.rst/..)

<a id="overview"></a>

## 38.1 概述（Overview）

以单人模式玩 Pong，或让两台 micro:bit 设备通过蓝牙连接进行双人游戏。

游戏通过 micro:bit 的两个按钮（标记为 A 和 B）控制球拍。启动后先选择游戏模式：按 A 在单人和多人模式之间切换，按 B 确认当前选择。开始游戏时，持球一方同时按下两个按钮发球。

> 译注——按键与画面：Single 表示单人，Multi 表示多人；先完成选择，再用 A、B 控制球拍。源码用 50×50 虚拟坐标计算运动，最终映射到 5×5 LED，并未增加物理分辨率。同时按键的源码判定阈值为 100 ms，因此发球不是任意先后按两次按钮。

选择多人模式后，游戏会尝试寻找并连接另一台同样处于多人模式的 micro:bit。

> 译注——连接前提：两块板均运行该游戏并选择 Multi，才符合原文的自动发现／连接流程；不是用手机连接任意蓝牙设备来替代第二位玩家。蓝牙连接实现位于 ble.c，出现连接失败时先核对两端模式、固件与广播扫描状态。

如果开发板的引脚 0 连接了压电蜂鸣器（Piezo buzzer），球碰到墙壁或球拍时会通过它发出提示音。

> 译注——板版本边界：原文的外接蜂鸣器说明与给出的 bbc_microbit 构建目标对应；本次源码另有 bbc_microbit_v2 的 PWM overlay。不要仅凭 v2 存在配置就把本页所有接线说明套到 v2，需同时核对所用板定义和蜂鸣器连接。

<a id="building-and-running"></a>

## 38.2 构建与运行（Building and running）

> 译注——执行前提：west 命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具、west 工作区、模块与目标工具链；应用和 overlay 为官方源码，构建目录由工具生成。选择与实物一致的板目标，构建成功后再烧录，失败时检查构建输出和板文档；本次没有执行构建、烧录或硬件实验。

```text
west build -b bbc_microbit samples/boards/bbc/microbit/pong
west flash
```

> 译注——源码入口：[main.c](../../../samples/boards/bbc/microbit/pong/src/main.c)；[prj.conf](../../../samples/boards/bbc/microbit/pong/prj.conf)；[ble.c](../../../samples/boards/bbc/microbit/pong/src/ble.c)。本地链接以本文为基准相对解析，源码版本可能与本次网页不同。

对应官方文档源码：[samples/boards/bbc/microbit/pong/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/bbc/microbit/pong/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/bbc/microbit/pong/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P037_microbit巡线机器人.md) · [返回大纲](大纲.md) · [下一章](P039_microbit声音输出.md)
