---
id: learning.zephyr-docs.board-samples.page-78
title: DSP非对称多处理OpenAMP通信
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nxp/adsp/rtxxx/amp_talk/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="amp_talk"></a>

# 第78章\_OpenAMP DSP 非对称多处理示例（OpenAMP DSP AMP Sample）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nxp/adsp/rtxxx/amp_talk/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nxp/adsp/rtxxx/amp_talk/README.rst/..)

<a id="overview"></a>

## 78.1 概述（Overview）

本应用展示如何在 NXP RT700 系列处理器上使用 OpenAMP 实现多核通信，演示主核 CM33_0 与多个远端内核并发进行 OpenAMP 通信：

> 译注——术语与实例：AMP 为非对称多处理（Asymmetric Multiprocessing）；RPMSG 为远程处理器消息传递（Remote Processor Messaging），virtio 提供虚拟队列抽象。这里有主核到 CM33_1、主核到 HiFi4 两条独立通道，不是三个内核共用一条无区分消息队列。

- CM33_0 ↔ CM33_1：两个 Cortex-M33 内核之间的处理器间通信。

- CM33_0 ↔ HiFi4 DSP：ARM Cortex-M33 与 Cadence HiFi4 DSP 之间的通信。

应用演示以下功能：

- 多个并发的 OpenAMP／RPMSG 实例。

- 每条通信通道使用独立的共享内存区域。

- 与不同远端内核独立传递消息。

- 正确的资源隔离与同步。

<a id="architecture"></a>

## 78.2 架构（Architecture）

示例由三个独立应用组成：

1. 主核（Primary Core，CM33_0）：

  - 运行两个并发线程。

  - 管理与 CM33_1 和 HiFi4 DSP 的通信。

  - 在两条通道上都充当 RPMSG 主机（Host）。

2. 远端 CM33 内核（Remote CM33 Core，CM33_1）：

  - 作为 RPMSG 远端（Remote）运行。

  - 通过专用共享内存与 CM33_0 通信。

3. 远端 DSP 内核（Remote DSP Core，HiFi4）：

  - 作为 RPMSG 远端（Remote）运行。

  - 通过另一块共享内存区域与 CM33_0 通信。

<a id="building-the-application-for-mimxrt700-evk"></a>

## 78.3 为 mimxrt700\_evk 构建应用

> 译注——镜像和地址配对：本次 sysbuild 添加 openamp_remote（remote_cm33）与 remote（remote_hifi4），主端源码分别使用 zephyr,ipc 和 zephyr,ipc-hifi4。扩展远端时应同步共享内存、vring、IPM 节点和端点配置，不能只增加一个应用线程。

> 译注——执行前提：west 构建命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工作区、工具链、模块与具体板；下载按板文档核对。主机网络和模型转换步骤另按相应小节的执行环境处理。本次未构建、烧录或运行硬件实验。

```text
# From the root of the zephyr repository
west build -b mimxrt700_evk/mimxrt798s/cm33_cpu0 --sysbuild samples/boards/nxp/adsp/rtxxx/amp_talk/
west debug
```

打开 minicom、PuTTY 等串口终端，按以下设置连接开发板：

- 波特率：115200。

- 数据位：8 位。

- 校验：无。

- 停止位：1 位。

复位开发板后，相应串口将出现以下消息，分别来自主端和远端：

> 译注——日志顺序：两个主端线程并发，实际串口输出可能交错，原文先后排列不是必须遵循的调度顺序。主端与远端轮流递增消息，示例分别显示奇数和偶数；发生发送错误也会进入清理并打印 ended，因此结束行需要结合错误信息判断。

```text
*** Booting Zephyr OS build v4.2.0-4126-g68238d6377d2 ***
 [ARM] Starting DSP...
 *** Booting Zephyr OS build v4.2.0-4126-g68238d6377d2 ***
 [DSP] Starting application thread!
 OpenAMP[DSP] demo started
 Starting application threads!

 OpenAMP[main->CM33] demo started
 Main core received a message: 1
 Main core received a message: 3
 Main core received a message: 5
 Main core received a message: 7
 Main core received a message: 9
 Main core received a message: 11
 ...
 Main core received a message: 97
 Main core received a message: 99
 OpenAMP demo ended.

 OpenAMP[main->DSP] demo started
 [DSP] Remote core received a message: 0
 Main core received a message: 1
 [DSP] Remote core received a message: 2
 Main core received a message: 3
 [DSP] Remote core received a message: 4
 Main core received a message: 5
 [DSP] Remote core received a message: 6
 Main core received a message: 7
 [DSP] Remote core received a message: 8
 Main core received a message: 9
 [DSP] Remote core received a message: 10
 Main core received a message: 11
 ...
 [DSP] Remote core received a message: 98
 Main core received a message: 99
 OpenAMP demo ended.
 [DSP] OpenAMP demo ended.
```

```text
*** Booting Zephyr OS build v4.2.0-4126-g68238d6377d2 ***
Starting application thread!

OpenAMP[remote] demo started
Remote core received a message: 0
Remote core received a message: 2
Remote core received a message: 4
Remote core received a message: 6
Remote core received a message: 8
Remote core received a message: 10
Remote core received a message: 12
...
Remote core received a message: 96
Remote core received a message: 98
OpenAMP demo ended.
```

<a id="key-features"></a>

## 78.4 主要功能（Key Features）

- 并发通信（Concurrent Communication）：主核同时管理两条独立 OpenAMP 通道。

- 资源隔离（Resource Isolation）：每条通道使用独立共享内存区域和 IPM 实例。

- 多架构支持（Multi-Architecture Support）：演示 ARM Cortex-M33 到 Cortex-M33，以及 ARM 到 DSP 的通信。

- 可扩展设计（Scalable Design）：可扩展架构以支持更多远端内核。

<a id="technical-details"></a>

## 78.5 技术细节（Technical Details）

实现使用：

- 每条通信通道独立的 RPMSG virtio 设备。

- 独立共享内存池和区域。

- 专用的处理器间消息传递（Inter-Processor Messaging，IPM）实例。

- 正确的 OpenAMP 资源管理与清理。

本示例可作为参考，帮助在嵌入式系统中利用 OpenAMP 框架实现复杂多核通信。

> 译注——等待边界：名称服务和端点建立使用 K_FOREVER 信号量等待；远端未启动或内存／IPM配置不匹配时，主端可能一直等待。这些共享资源独立描述不等于已经建立针对恶意内核的安全隔离。

<a id="see-also"></a>

## 78.6 另请参阅（See also）

[处理器间消息传递（IPM）](../intercore_reference/P058_处理器间消息公共接口.md)

> 译注——源码入口：仓库相对参照：[src/main.c](../../../samples/boards/nxp/adsp/rtxxx/amp_talk/src/main.c)；[CMakeLists.txt](../../../samples/boards/nxp/adsp/rtxxx/amp_talk/CMakeLists.txt)；[remote_cm33/src/main.c](../../../samples/boards/nxp/adsp/rtxxx/amp_talk/remote_cm33/src/main.c)；[remote_hifi4/src/main.c](../../../samples/boards/nxp/adsp/rtxxx/amp_talk/remote_hifi4/src/main.c)；[sysbuild.cmake](../../../samples/boards/nxp/adsp/rtxxx/amp_talk/sysbuild.cmake)。本地版本可能与网页不同。

对应官方文档源码：[samples/boards/nxp/adsp/rtxxx/amp_talk/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nxp/adsp/rtxxx/amp_talk/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nxp/adsp/rtxxx/amp_talk/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P077_DSP非对称多处理闪灯.md) · [返回大纲](大纲.md) · [下一章](P079_S32网络控制器.md)
