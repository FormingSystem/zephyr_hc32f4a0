---
id: learning.zephyr-docs.intercore_reference.mboxextra-31
title: RTxxx非对称多处理邮箱示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nxp/adsp/rtxxx/amp_mbox/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="amp_mbox"></a>

# 第31章\_RTxxx非对称多处理邮箱示例

原文：[mbox API AMP sample](https://docs.zephyrproject.org/latest/samples/boards/nxp/adsp/rtxxx/amp_mbox/README.html)。读取日期：2026-10-13，`latest`。

本例展示受支持的恩智浦（NXP）i.MX RTxxx 平台如何在非对称多处理（Asymmetric Multiprocessing，AMP）场景中使用数字信号处理器（Digital Signal Processor，DSP）域。应用程序接口（Application Programming Interface，API）使用邮箱（Mailbox，MBOX）进行通信。[官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/boards/nxp/adsp/rtxxx/amp_mbox)位于`samples/boards/nxp/adsp/rtxxx/amp_mbox`。

## 31.1\_Cortex-M与DSP域的职责

Cortex-M 和 DSP 域分别使用独立工程，再通过系统构建（Sysbuild）合成为一个最终镜像（Image）。Cortex-M 域负责 DSP 域的时钟和电源设置、代码加载及启动，然后通过邮箱 API 发送一条简单消息；在本例覆盖的器件上，邮箱接口映射到消息单元（Messaging Unit，MU）外设。

DSP 域向选定的控制台通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）打印“hello world”消息；收到发送来的消息时，也将其打印出来。

## 31.2\_构建、烧录和调试探针

可按以下原命令在受支持开发板上构建并启动；`<board>`为开发板标识：

```shell
west build -b <board> -o --sysbuild samples/boards/nxp/adsp/rtxxx/amp_mbox
west flash -r jlink
```

原页列出的受支持开发板为`mimxrt685_evk/mimxrt685s/cm33`。

建议板载调试探针（Debug Probe）运行 J-Link 固件，或使用独立 J-Link 探针，因为 J-Link 能直接调试基于 Xtensa 的 DSP 核心。这里保留原命令中的`-o`和`-r jlink`参数。

## 31.3\_示例输出

原输出如下；OS 指操作系统（Operating System），ARM、DSP 前缀区分输出端：

```text
*** Booting Zephyr OS build v4.1.0-1858-g6bd0a62b0bde ***
Hello World! mimxrt685_evk/mimxrt685s/cm33
[ARM] Starting DSP...
*** Booting Zephyr OS build v4.1.0-1858-g6bd0a62b0bde ***
[DSP] Hello World! mimxrt685_evk/mimxrt685s/hifi4
[DSP] Button pressed!
```

Cortex-M 端先打印问候并启动 DSP；DSP 端随后打印问候，以及“按钮已按下（Button pressed!）”消息。日志中的`v4.1.0-1858-g6bd0a62b0bde`为官方示例保留的版本信息，不代表本译文读取时的最新版本。通用邮箱接口见[公共接口](P014_邮箱驱动公共接口.md)。

---

[上一章：BCM2711邮箱绑定头文件源码](P030_BCM2711邮箱绑定头文件源码.md) · [下一章：ADI硬件信号量邮箱绑定](P032_ADI硬件信号量邮箱绑定.md) · [返回大纲](大纲.md)
