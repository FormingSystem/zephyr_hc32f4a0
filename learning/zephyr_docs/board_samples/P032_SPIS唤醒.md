---
id: learning.zephyr-docs.board-samples.page-32
title: SPIS唤醒
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/spis_wakeup/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="spis-wakeup"></a>

# 第32章\_SPIS 唤醒（SPIS wake up）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nordic/spis_wakeup/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nordic/spis_wakeup/README.rst/..)

<a id="overview"></a>

## 32.1 概述（Overview）

本示例展示如何使用 nrf-spis 驱动额外的唤醒线（Wake line）。应用配置为 SPIS，在等待 SPI 传输时进入休眠。作为 SPIM 工作、同时处理唤醒线的外部设备（本示例中为另一个处理器核），在传输开始前唤醒该应用。示例使用 Nordic Semiconductor nRF54H20 DK 模拟两个独立设备，由两个独立处理器核控制 SPIS／SPIM 驱动：

> 译注——角色：SPIS 是 SPI 从机／外设端，SPIM 是 SPI 主机／控制器端；两者是不同处理器核上的硬件实例。WAKE 是额外的唤醒握手线，不能由 CS、SCK 或数据线省略替代。

- nrf54h20dk/nrf54h20/cpuapp 用作 SPIS 控制器设备。

- nrf54h20dk/nrf54h20/cpurad 用作 SPIM 控制器设备。

<a id="requirements"></a>

## 32.2 前提条件（Requirements）

本示例可在 nRF54H20 等多核 SoC 上运行，需要按下文额外接线。

<a id="wiring"></a>

## 32.3 接线（Wiring）

需要使用导线（跳线）连接 SPIS 与 SPIM 设备：

- SPIS WAKE <-> WAKE SPIM（唤醒线）

- SPIS CS <—–> CS SPIM（片选线）

- SPIS SCK <—> SCK SPIM（串行时钟线）

- SPIS MOSI <-> MOSI SPIM（主出从入数据线）

- SPIS MISO <-> MISO SPIM（主入从出数据线）

<a id="building-and-running"></a>

## 32.4 构建与运行（Building and Running）

> 译注——执行前提：除本页另有说明的目录外，west 命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先准备[入门指南](../getting_started/大纲.md)所需的主机工具、west 工作区、模块与目标工具链；应用、配置及 overlay 为官方源码，构建目录由工具生成。构建成功后再按目标板文档烧录，失败时返回构建输出或板文档检查；下方日志是官方预期示例，本次未执行硬件步骤。

代码位于 [samples/boards/nordic/spis_wakeup](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/nordic/spis_wakeup)。

构建并烧录应用：

> 译注——多核命令差异：原页下方命令未写 --sysbuild；本次 tests.yaml 明确设 sysbuild: true，sysbuild.cmake 负责加入 wakeup_trigger 远端应用。要按该实现构建两端，需在 west build 命令加入 --sysbuild，或使用正确的测试场景选择来取得系统构建配置。仅构建 cpuapp 应用不能据此认定 cpurad 的传输端已烧录；先核对生成的各域，再执行所选构建目录的烧录。

```text
west build -b nrf54h20dk/nrf54h20/cpuapp samples/boards/nordic/spis_wakeup
west flash
```

<a id="sample-output"></a>

### 32.4.1 输出示例（Sample Output）

nrf54h20/cpuapp：

> 译注——输出含义：waiting for SPI transfer 表示等待传输，woken up by 后打印接收到的对端标识，active for 500ms 表示忙等保持活动。示例先休眠 1.5 秒、传输前后各保留一段活动时间，用于观察状态，不是本次测得的功耗或唤醒延迟。

```text
[00:00:00.272,217] <inf> spi_wakeup: Hello world from nrf54h20dk@0.9.0/nrf54h20/cpuapp
[00:00:00.272,241] <inf> spi_wakeup: SPIS: waiting for SPI transfer; going to sleep...
[00:00:02.274,192] <inf> spi_wakeup: SPIS: woken up by nrf54h20/cpurad
[00:00:02.274,215] <inf> spi_wakeup: SPIS: will be active for 500ms after transfer
```

nrf54h20/cpurad：

```text
[00:00:00.272,195] <inf> spi_wakeup: Hello world from nrf54h20dk@0.9.0/nrf54h20/cpurad
[00:00:00.272,219] <inf> spi_wakeup: SPIM: going to sleep for 1.5s...
[00:00:01.772,352] <inf> spi_wakeup: SPIM: will be active for 500ms before transfer
[00:00:02.273,456] <inf> spi_wakeup: SPIM: transferring the CONFIG_BOARD_QUALIFIERS: 'nrf54h20/cpurad'
```

<a id="references"></a>

## 32.5 参考资料（References）

[dts/bindings/spi/nordic,nrf-spi-common.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/spi/nordic,nrf-spi-common.yaml)

<a id="see-also"></a>

## 32.6 另请参阅（See also）

[SPI](../hardware/P318_SPI公共接口.md)

> 译注——实现入口：[samples/boards/nordic/spis_wakeup/src/main.c](../../../samples/boards/nordic/spis_wakeup/src/main.c)与[samples/boards/nordic/spis_wakeup/prj.conf](../../../samples/boards/nordic/spis_wakeup/prj.conf)。仓库源码仅作参照，版本可能与本次官方页面不同；本地链接按文档位置相对解析。 配置依据见[本次上游 tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/spis_wakeup/tests.yaml)。

对应官方文档源码：[samples/boards/nordic/spis_wakeup/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/spis_wakeup/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nordic/spis_wakeup/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P031_nrfx外设资源共享.md) · [返回大纲](大纲.md) · [下一章](P033_Mesh开关模型.md)
