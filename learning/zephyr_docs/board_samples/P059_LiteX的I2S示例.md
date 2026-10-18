---
id: learning.zephyr-docs.board-samples.page-59
title: LiteX的I2S示例
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/enjoydigital/litex/i2s/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="i2s-example"></a>

<a id="i2s-litex-example"></a>

# 第59章\_I2S 示例（I2S example）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/enjoydigital/litex/i2s/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 59.1 概述（Overview）

这是一个简单的 I2S 音频收发（Audio transceiver）示例，可以接入音乐源并收听。

> 译注——数据链路：I2S 是芯片间音频串行总线（Inter-IC Sound），PCM 是脉冲编码调制（Pulse-Code Modulation）。源码从 i2s_rx 读取数据，复制到发送缓冲区后交给 i2s_tx；两个声道均为 24 位样本，应用配置的帧时钟频率为 44100 Hz，仍需对应硬件提供正确时钟。

<a id="audio-format"></a>

## 59.2 音频格式（Audio Format）

驱动要求并提供具有以下参数的音频数据：

- 44100 Hz 采样率。

- 有符号 24 位 PCM。

- 立体声（Stereo）。

- 小端序（Little endian）。

<a id="building"></a>

## 59.3 构建（Building）

> 译注——执行目录与生成器：原文三行命令从 Zephyr 源码中的 samples/boards/enjoydigital/litex/i2s 应用目录开始，在应用下创建 build，再以 .. 指回应用源码。先按入门指南准备工具链和模块。最后的 make 要求 CMake 生成 Makefile；若实际选用 Ninja 等生成器，应使用对应工具，或在该 build 目录执行 cmake --build .。这里保留原命令，不把构建成功视作已下载和播放成功。

```text
mkdir build && cd build
cmake -DBOARD=litex_vexriscv ..
make
```

<a id="known-issues"></a>

## 59.4 已知问题（Known issues）

运行几分钟后似乎会出现一些音频延迟，这是因为声音驱动发送数据的速度无法跟上接收数据的速度。

> 译注——问题状态：这是原文保留的已知收发速率问题，本次没有运行音频实验，也没有据此修复驱动。示例循环还需结合读写返回值排查；仅观察短时声音正常，不能证明长时间无延迟或丢帧。本页没有随文音频附件。

> 译注——源码入口：[main.c](../../../samples/boards/enjoydigital/litex/i2s/src/main.c)；[prj.conf](../../../samples/boards/enjoydigital/litex/i2s/prj.conf)。链接相对本篇定位，仓库参照版本可能与本次上游快照不同。

对应官方文档源码：[samples/boards/enjoydigital/litex/i2s/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/enjoydigital/litex/i2s/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/enjoydigital/litex/i2s/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P058_AMD示例目录.md) · [返回大纲](大纲.md) · [下一章](P060_EnjoyDigital示例目录.md)
