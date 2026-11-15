---
id: learning.zephyr-docs.board-samples.page-96
title: 外部SPI内存
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/espressif/spiram_test/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="esp32-spiram"></a>

# 第96章\_外部 SPI 内存（SPIRAM）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/espressif/spiram_test/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/espressif/spiram_test/README.rst/..)

<a id="overview"></a>

## 96.1 概述（Overview）

本示例展示如何通过 [`shared_multi_heap_aligned_alloc()`](../lowheap_reference/P009_共享多堆公共接口.md#ga328b199253da06ed724e9b0157167ede)，使用 `SMH_REG_ATTR_EXTERNAL` 属性从 SPIRAM 分配内存，检查分配是否正确，再调用 [`shared_multi_heap_free()`](../lowheap_reference/P009_共享多堆公共接口.md#gab968bf26483d22939aaa7c2b1b6743ad) 释放内存。它还会从内部内存分配空间，并检查地址范围是否正确。

> 译注——实际测试：SPIRAM 指通过串行外设接口（Serial Peripheral Interface，SPI）访问的外部 RAM，此示例的设备树对象为 psram0。源码申请 32 KiB、32 字节对齐的外部空间，分别用 8／16／32 位访问写入并核对固定模式，再释放；内部空间另用 k_malloc(4096) 分配。app.overlay 将 PSRAM 大小设为 2 MiB，仍须与所用硬件及配置核对。

<a id="supported-socs"></a>

## 96.2 支持的 SoC（Supported SoCs）

此示例代码目前支持以下 SoC：

> 译注——成功判据缺陷：本次 main.c 在写入前没有检查外部申请结果是否为 NULL；最终失败条件写成“地址不是外部 RAM，并且三种访问错误数均为零”。因此存在错误计数时仍可能打印 pass。tests.yaml 只匹配两条 pass 文本，也不能补足这个缺陷。阅读时应同时核对地址类别、分配成功和三个错误计数为零；本译文未修改上游程序或声称实测通过。

- ESP32

- ESP32-S2

- ESP32-S3

- ESP32-C5

- ESP32-P4

<a id="building-and-running"></a>

## 96.3 构建与运行（Building and Running）

> 译注——执行前提：下面主机命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具、模块、工具链与目标板。west flash 会下载固件；串口输出块是原文示例，提示符和日志不作为命令执行。本批未构建、烧录或运行硬件实验。

确保开发板已经通过 USB 端口连接。

```text
west build -b esp32s3_devkitc/esp32s3/procpu samples/boards/espressif/spiram_test
west flash
```

如果使用其他受支持的 Espressif 开发板，请将上述命令的参数替换为相应板名，例如 `esp32s2_devkitc`。

<a id="sample-output"></a>

### 96.3.1 示例输出（Sample Output）

要查看本示例输出，可运行 `west espressif monitor`，或使用其他串口控制台程序，例如 minicom、putty、screen。本例使用 `west espressif monitor`，它会自动检测位于 `/dev/ttyUSB0` 的串口：

```text
$ west espressif monitor
```

```text
*** Booting Zephyr OS build v3.7.0-446-g93c9da66944c ***
SPIRAM mem test pass
Internal mem test pass
```

> 译注——源码入口：[src/main.c](../../../samples/boards/espressif/spiram_test/src/main.c)；[app.overlay](../../../samples/boards/espressif/spiram_test/app.overlay)；[tests.yaml](../../../samples/boards/espressif/spiram_test/tests.yaml)。这些相对链接用于仓库内跟踪；本次译注核对的上游快照摘要见来源记录，仓库版本可能不同。

对应官方文档源码：[samples/boards/espressif/spiram_test/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/espressif/spiram_test/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/espressif/spiram_test/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P095_内存映射闪存.md) · [返回大纲](大纲.md) · [下一章](P097_正交解码器阈值触发.md)
