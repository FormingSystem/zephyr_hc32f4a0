---
id: learning.zephyr-docs.board-samples.page-31
title: nrfx外设资源共享
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/nrfx_prs/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nrf_nrfx_prs"></a>

# 第31章\_nrfx 外设资源共享（nrfx peripheral resource sharing）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nordic/nrfx_prs/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nordic/nrfx_prs/README.rst/..)

<a id="overview"></a>

## 31.1 概述（Overview）

本示例展示如何在 Zephyr 中使用共享同一 ID 与基地址（Base address）的 nRF 外设。这些外设共享某些硬件资源，因此不能同时使用，但可以在它们之间切换，交替使用。按照原文所述的 Zephyr 驱动模型，驱动在启动时初始化外设后无法将其反初始化，因此不能用 Zephyr API 实现这种切换。所以，本示例对需要切换的外设实例（SPIM2 与 UARTE2）直接使用 nrfx 驱动，而对相同外设类型的其他实例仍使用标准 Zephyr 驱动（标准 Zephyr 控制台使用 UARTE0，SPIM1 用于执行额外的示例传输）。

> 译注——原文版本边界：当前上游 include/zephyr/device.h 已声明 device_deinit()，其可用性受 CONFIG_DEVICE_DEINIT_SUPPORT 和具体驱动支持约束，未支持时会返回 -ENOTSUP。因此原文关于无法反初始化的描述不能推广为当前所有 Zephyr 设备的结论；本示例仍直接调用 nrfx_uarte_uninit()／nrfx_spim_uninit() 后切换实例。

示例使用两个按钮：

- 按下按钮 1，可以请求通过当前已初始化的外设（SPIM2 或 UARTE2）执行一次传输。

- 按下按钮 2，可以在两个外设之间切换。

没有按下按钮时，每隔五秒通过 SPIM1 执行一次后台传输。

示例在标准控制台上输出全部已发送和已接收字节的十六进制编码。因此，在开发板上正确连接回环线路（Loopback wiring）后——SPIM 的 MOSI 与 MISO 引脚相连，UARTE 的 TX 与 RX 引脚相连——就能检查某个外设发送的内容是否原样接收回来。没有这类接线时，UARTE 收不到数据，SPIM 收到的全部是零。请查阅 [samples/boards/nordic/nrfx_prs/boards](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/nordic/nrfx_prs/boards) 目录中的覆盖文件，确认示例所支持开发板的 MOSI/MISO 与 TX/RX 引脚分配。

> 译注——共享并非并行：PRS 为外设资源共享（Peripheral Resource Sharing）；SPIM 为 SPI 主机实例，UARTE 为带 EasyDMA 的 UART 实例。SPIM2 与 UARTE2 交替占有资源，SPIM1 的后台传输和 UARTE0 的控制台使用其他实例。回环引脚要按所选板的 overlay 确认，数据 UART 的引脚与波特率不能直接套用控制台设置。

<a id="requirements"></a>

## 31.2 前提条件（Requirements）

原示例已在 Nordic Semiconductor nRF9160 DK（nrf9160dk/nrf9160）与 nRF5340 DK（nrf5340dk/nrf5340/cpuapp）开发板上测试。

<a id="building-and-running"></a>

## 31.3 构建与运行（Building and Running）

> 译注——执行前提：除本页另有说明的目录外，west 命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先准备[入门指南](../getting_started/大纲.md)所需的主机工具、west 工作区、模块与目标工具链；应用、配置及 overlay 为官方源码，构建目录由工具生成。构建成功后再按目标板文档烧录，失败时返回构建输出或板文档检查；下方日志是官方预期示例，本次未执行硬件步骤。

代码位于 [samples/boards/nordic/nrfx_prs](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/nordic/nrfx_prs)。

构建并烧录应用：

```text
west build -b nrf9160dk/nrf9160 samples/boards/nordic/nrfx_prs
west flash
```

按下按钮 1，通过 SPIM2 或 UARTE2 触发一次示例传输。按下按钮 2，切换传输使用的外设类型。

没有按下按钮时，通过 SPIM1 执行后台传输。

> 译注——实现入口：[samples/boards/nordic/nrfx_prs/src/main.c](../../../samples/boards/nordic/nrfx_prs/src/main.c)与[samples/boards/nordic/nrfx_prs/prj.conf](../../../samples/boards/nordic/nrfx_prs/prj.conf)。仓库源码仅作参照，版本可能与本次官方页面不同；本地链接按文档位置相对解析。 反初始化接口见[本仓库 device.h](../../../include/zephyr/device.h)及[本次上游接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/device.h)。

对应官方文档源码：[samples/boards/nordic/nrfx_prs/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/nrfx_prs/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nordic/nrfx_prs/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P030_nrfx外设驱动示例.md) · [返回大纲](大纲.md) · [下一章](P032_SPIS唤醒.md)
