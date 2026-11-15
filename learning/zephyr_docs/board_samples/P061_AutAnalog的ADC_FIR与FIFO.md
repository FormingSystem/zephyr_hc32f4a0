---
id: learning.zephyr-docs.board-samples.page-61
title: AutAnalog的ADC_FIR与FIFO
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/infineon/autanalog/fir_fifo/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="autanalog_fir_fifo"></a>

# 第61章\_AutAnalog ADC 的 FIR 与 FIFO（AutAnalog ADC FIR+FIFO）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/infineon/autanalog/fir_fifo/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/infineon/autanalog/fir_fifo/README.rst/..)

<a id="overview"></a>

## 61.1 概述（Overview）

本示例展示 AutAnalog 逐次逼近型 ADC（Successive Approximation Register ADC，SAR ADC）的 FIR 与 FIFO 功能：

> 译注——术语与通道：ADC 为模数转换器（Analog-to-Digital Converter），FIR 为有限冲激响应（Finite Impulse Response）滤波器，FIFO 为先进先出（First In, First Out）缓冲。通道 0、8、24、25 是同一物理输入及其处理结果，不是四个独立模拟输入引脚。

- 每秒采样四个 ADC 通道：一个原始 GPIO 输入（P15.0）、同一输入经内部多路复用器（Multiplexer，MUX）后的通道，以及两个 FIR 滤波器伪通道（Pseudo-channel）。

- FIR0 是在设备树中配置的四抽头移动平均滤波器（4-tap moving average），使用四个 Q1.15 定点格式的 `0x2000` 系数。

> 译注——定点系数：Q1.15 中 0x2000／32768 = 0.25，四个相同抽头的系数之和为 1。FIR0 来自设备树，FIR1 由应用加载相同系数；不能把十六进制整数 8192 当作浮点增益。

- FIR1 是由应用在运行时加载的四抽头移动平均滤波器。

- 每个通道将结果送入专属 FIFO 缓冲区。达到 FIFO 水位线（Watermark）时，驱动触发回调，应用批量取出全部四个缓冲区的数据。

<a id="building-and-running"></a>

## 61.2 构建与运行（Building and Running）

> 译注——执行前提：本节 west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具、模块、工具链及对应板。构建目录由工具生成，下载与启动方式按具体板文档核对。本次仅核对文档和源码，未执行构建、烧录或硬件实验。

本示例需要：

- 在 `zephyr,user` 节点的 `io-channels` 属性中配置 ADC 通道。

- ADC 控制器下的两个 FIR 子节点。

- ADC 控制器下的一个 `fifo` 子节点。

对于 [PSOC™ Edge E84 评估套件（PSOC™ Edge E84 Evaluation Kit）](https://docs.zephyrproject.org/latest/boards/infineon/kit_pse84_eval/doc/index.html#kit_pse84_eval)，`kit_pse84_eval/pse846gps2dbzc4a/m55` 的覆盖文件配置如下：

- 通道 0：原始 GPIO 输入 P15.0，送入 FIFO 缓冲区 0。

- 通道 8：P15.0 经 MUX 后的输入，送入 FIFO 缓冲区 1。

- 通道 24：FIR0 伪通道，送入 FIFO 缓冲区 2。

- 通道 25：FIR1 伪通道，送入 FIFO 缓冲区 3。

- FIR0 系数从设备树加载，FIR1 系数在运行时加载。

- 每个缓冲区的 FIFO 水位线设为四个字（Word）。

> 译注——单位与容量：水位线四个字是触发阈值，不是四个字节，也不是整个 FIFO 的容量。源码回调分别读取四个缓冲区，每个最多取八个字；主循环在 adc_read() 返回后打印记录，并休眠 1000 ms。

可以按以下方式构建并烧录示例：

```text
west build -b kit_pse84_eval/pse846gps2dbzc4a/m55 samples/boards/infineon/autanalog/fir_fifo
west flash
```

<a id="sample-output"></a>

### 61.2.1 输出示例（Sample output）

应得到类似下面的输出：

> 译注——观察含义：GPIO、MUX、FIR0、FIR1 是四条数据路径，status 是事件状态位，mV 为毫伏。原始日志中的 36 和 65 mV 是某次输入结果；稳态下各路径相近并不能单独证明滤波器的动态响应已经验证。

```text
ADC reading[0]:
- adc0, channel 0: 36 = 65 mV
- adc0, channel 8: 36 = 65 mV
- adc0, channel 24: 36 = 65 mV
- adc0, channel 25: 36 = 65 mV
FIFO: watermark event (status=0x0000000f)
FIFO[0] GPIO: 4 words - 36 36 36 36
FIFO[1] MUX : 4 words - 36 36 36 36
FIFO[2] FIR0: 4 words - 36 36 36 36
FIFO[3] FIR1: 4 words - 36 36 36 36
```

<a id="see-also"></a>

## 61.3 另请参阅（See also）

[模数转换器（Analog-to-Digital Converter，ADC）](../hardware/P463_ADC公共接口参考.md)

> 译注——源码入口：[main.c](../../../samples/boards/infineon/autanalog/fir_fifo/src/main.c)；[prj.conf](../../../samples/boards/infineon/autanalog/fir_fifo/prj.conf)。链接相对本篇定位，仓库参照版本可能与本次上游快照不同。

对应官方文档源码：[samples/boards/infineon/autanalog/fir_fifo/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/infineon/autanalog/fir_fifo/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/infineon/autanalog/fir_fifo/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P060_EnjoyDigital示例目录.md) · [返回大纲](大纲.md) · [下一章](P062_Infineon示例目录.md)
