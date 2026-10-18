---
id: learning.zephyr-docs.board-samples.page-111
title: Espressif示例目录
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/espressif/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="espressif-esp32-boards"></a>

# 第111章\_Espressif ESP32 开发板示例（Espressif ESP32 boards）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/espressif/index.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

这些示例演示在 Zephyr 中使用 Espressif ESP32 开发板。

> 译注——阅读边界：本页按官方目录列出 ESP32 示例；Flash IPM 沿用已译的处理器间通信专题，ULP 子目录也有独立译文。目录完成不代表 Espressif 的全部板卡介绍、设备树绑定或API已翻译，这些仍按全站清单分别登记。

- [深度睡眠（Deep Sleep）](P093_深度睡眠.md#esp32-deep-sleep)：在 ESP32 上使用定时器、GPIO 和 EXT1 唤醒源进入深度睡眠。

- [ESP-NOW 无线通信（ESP-NOW）](P107_ESP_NOW无线通信.md#espnow)：在两块 ESP32 开发板之间收发 ESP-NOW 广播心跳信标。

- [ESP32 正交解码器按单元阈值触发（ESP32 qdec per-unit threshold trigger）](P097_正交解码器阈值触发.md#esp32-qdec-trigger)：为 ESP32 PCNT 驱动安装按单元的阈值回调。

- [闪存加密（Flash Encryption）](P108_闪存加密.md#esp32-flash-encryption)：使用 ESP32 闪存加密功能，对闪存中的数据进行加密和解密。

- [ESP32 上的闪存 IPM（Flash IPM on ESP32）](../intercore_reference/P078_ESP32闪存IPM示例.md#flash-ipm)：使用处理器间邮箱（Inter-Processor Mailbox，IPM）在 CPU 核之间共享闪存 API。

- [轻度睡眠（Light Sleep）](P094_轻度睡眠.md#esp32-light-sleep)：使用 ESP32 轻度睡眠节电，同时保持内存、CPU 和外设状态。

- [内存映射闪存（Memory-Mapped Flash）](P095_内存映射闪存.md#esp32-flash-memory-mapped)：向存储分区写入数据，再通过闪存 API 和内存映射指针读取。

- [像素处理加速器（Pixel processing accelerator）](P098_像素处理加速器.md#esp32-ppa-srm)：使用像素处理加速器对图像执行缩放、旋转和镜像。

- [外部 SPI 内存（SPIRAM）](P096_外部SPI内存.md#esp32-spiram)：从 SPIRAM 分配内存。

- Wi-Fi 网状网络（Wi-Fi Mesh）：构建自组织多跳 Wi-Fi 网状网络。 相关链接：[Wi-Fi 网状网络 IP 通信（Wi-Fi Mesh IP）](P109_WiFi网状网络.md#wifi-mesh)。

- [Wi-Fi 网状网络 IP 通信（Wi-Fi Mesh IP）](P110_WiFi网状网络IP通信.md#wifi-mesh-ip)：通过自组织 Wi-Fi 网状网络承载 IP，并由根节点提供 NAT 转发。

- [XTAL32K 看门狗定时器（XTAL32K Watchdog Timer，WDT）](P099_32kHz晶振看门狗.md#esp32-xt-wdt)：外部 32K 晶体失效时触发看门狗中断。

<a id="ulp"></a>

## 111.1 [超低功耗协处理器（Ultra Low Power coprocessor，ULP）](P100_ULP协处理器示例目录.md)

<a id="lp-core"></a>

### 111.1.1 [低功耗 CPU（Low-Power CPU，LP CORE）](P101_低功耗CPU示例目录.md)

- [低功耗核调试（Debug ULP）](P102_低功耗核调试.md#debug-ulp)：调试 ESP32-C6 的低功耗核。

- [低功耗核串口回显（Echo ULP）](P103_低功耗核串口回显.md#echo-ulp)：通过 Zephyr UART API 使用 ESP32-C6 低功耗核的低功耗串口。

- [主核中断低功耗核（Interrupt ULP）](P105_主核中断低功耗核.md#interrupt-ulp)：高性能核向低功耗核发出中断。

- [低功耗核 GPIO 唤醒（LP GPIO Wakeup）](P104_低功耗核GPIO唤醒.md#lp-gpio-wakeup)：低功耗 GPIO 电平变化时，由低功耗核将高性能核从深度睡眠中唤醒。

- [低功耗核定时器唤醒（LP Timer Wakeup）](P106_低功耗核定时器唤醒.md#lp-timer-wakeup)：低功耗核通过低功耗定时器，周期性地将高性能核从深度睡眠中唤醒。

对应官方文档源码：[samples/boards/espressif/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/espressif/index.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/espressif/index.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或改写密钥与eFuse。

[上一章](P110_WiFi网状网络IP通信.md) · [返回大纲](大纲.md) · [下一章](P112_开发板示例总目录.md)
