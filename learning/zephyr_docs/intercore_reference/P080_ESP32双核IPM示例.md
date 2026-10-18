---
id: learning.zephyr-docs.intercore_reference.ipmsample-80
title: ESP32双核IPM示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/ipm/ipm_esp32/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="ipm-esp32"></a>

# 第80章\_ESP32双核IPM示例

原文：[IPM on ESP32](https://docs.zephyrproject.org/latest/samples/drivers/ipm/ipm_esp32/README.html)。读取日期：2026-10-13，`latest`。

本简单示例适用于多核ESP32片上系统（System on Chip，SoC），演示非对称多处理（Asymmetric Multiprocessing，AMP）应用使用的软件核间消息机制。

ESP32有APP和PRO两个中央处理器（Central Processing Unit，CPU）。PRO通过处理器间邮箱（Inter-Processor Mailbox，IPM）驱动向APP发送消息，等待APP的应答，再把应答内容打印到控制台。

原日志中的OS表示操作系统（Operating System），日志版本字符串和计数值按原样保留。


## 80.1\_通道与消息长度

ESP32核间消息机制最多支持四个通道：0和1保留给蓝牙（Bluetooth，BT）和Wi-Fi消息；2和3可供应用使用。每个通道的单条消息最多携带64字节数据，因此上层协议负责把更大的消息拆分为64字节块。

**原文措辞译注：**通道数量处原句为“up two four”，此处按其随后明确列出的通道0至3译为“最多四个”。

## 80.2\_构建与运行

使用系统构建（Sysbuild）构建ESP32 IPM示例：

```sh
west build -b esp32s3_devkitc/esp32s3/procpu --sysbuild samples/drivers/ipm/ipm_esp32
```

通过`west espressif monitor`，或minicom、PuTTY、screen等串口控制台（Serial Console）程序查看输出。

## 80.3\_原始输出

日志中的`PRO_CPU`和`APP_CPU`分别标识PRO与APP核心。输出表示PRO发送请求并等待远端应答，随后收到APP的运行时间节拍数（Uptime Ticks）。原日志中的Zephyr版本和数值保持原样：

```text
*** Booting Zephyr OS build v4.0.0-rc2-61-ga24efebe15e2 ***
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 502
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 10502
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 20503
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 30504
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 40505
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 50506
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 60507
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 70508
```

这里的节拍数是原输出内容，不是本次运行测量值。

源码入口：[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/ipm/ipm_esp32)。

另见[IPM公共接口](P058_处理器间消息公共接口.md)。

---

[上一章：处理器间邮箱示例目录](P079_处理器间邮箱示例目录.md) · [下一章：NXPiMX处理器间邮箱示例](P081_NXPiMX处理器间邮箱示例.md) · [返回大纲](大纲.md)
