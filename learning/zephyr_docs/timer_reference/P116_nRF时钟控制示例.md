---
id: learning.zephyr-docs.timer_reference.clocksample-116
title: nRF时钟控制示例
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/clock_control/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="nrf_clock_control"></a>

# 第116章\_nRF时钟控制示例

原文：[nRF clock control](https://docs.zephyrproject.org/latest/samples/boards/nordic/clock_control/README.html)。读取日期：2026-10-13，`latest`。

本示例演示如何向 Nordic 的 nRF 时钟提出最低要求（Minimum Clock Requirements），并取得启动时间（Startup Time），以确保及时满足时钟要求。

[浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/boards/nordic/clock_control)。

## 116.1\_硬件要求

需要基于 nRF54H20 的开发板。

## 116.2\_构建、烧录与运行

示例构建时，为某个特定时钟测试一组特定要求。时钟在设备树覆盖文件（Devicetree Overlay）中指定；要求由以下示例专用 Kconfig 构建配置项定义：

| 配置项 | 对应要求 |
| --- | --- |
| `CONFIG_SAMPLE_CLOCK_FREQUENCY_HZ` | 时钟频率（Clock Frequency），单位为赫兹（Hertz，Hz） |
| `CONFIG_SAMPLE_CLOCK_ACCURACY_PPM` | 时钟准确度（Clock Accuracy），单位为百万分率（Parts Per Million，PPM） |
| `CONFIG_SAMPLE_CLOCK_PRECISION` | 时钟精度要求（Clock Precision） |

原文另外列出以下配置项，用于控制请求保持相关的时间：`CONFIG_SAMPLE_PRE_REQUEST_TIMEOUT`和`CONFIG_SAMPLE_KEEP_REQUEST_TIMEOUT`。原页没有给出它们的具体单位与默认值，此处不推定。

每个时钟都有配置及覆盖文件示例。原文注明这些配置可在`tests.yaml`中找到，通过 west 的`-T`参数应用。下面是针对`FLL16M`时钟的原始构建命令：

```bash
west build -b nrf54h20dk/nrf54h20/cpuapp -T sample.boards.nrf.clock_control.fll16m samples/boards/nordic/clock_control
```

命令从 Zephyr 源码根目录执行，目标为`nrf54h20dk/nrf54h20/cpuapp`，使用名为`sample.boards.nrf.clock_control.fll16m`的测试配置。原页本节标题包括烧录和运行，但只给出了这条构建命令，没有额外列出烧录命令。

## 116.3\_示例输出

下面完整保留原始输出。其中`minimum`表示请求的最低要求，`resolved`表示解析后的要求；`us`为微秒（Microsecond，µs），`ms`为毫秒（Millisecond）。

```text
clock name: fll16m
minimum frequency request: 0Hz
minimum accuracy request: 30PPM
minimum precision request: 0

resolved frequency request: 16000000Hz
resolved accuracy request: 30PPM
resolved precision request: 0

startup time for requested spec: 850us

requesting minimum clock specs
request applied to clock in 1ms

releasing requested clock specs
clock spec request released
```

该次输出先显示`fll16m`的请求：频率0 Hz、准确度30 PPM、精度值0；随后解析为16000000 Hz、30 PPM、精度值0。所请求规格的启动时间为850 µs，请求在1 ms内应用到时钟，最后释放请求并确认释放完成。这是官方示例记录，不能将其中的0值直接理解为关闭时钟，也不能将这些时间当作所有硬件的固定时限。

---

[上一章：Alif时钟多路复用绑定](P115_Alif时钟多路复用绑定.md) · [下一章：LiteX时钟控制示例](P117_LiteX时钟控制示例.md) · [返回大纲](大纲.md)
