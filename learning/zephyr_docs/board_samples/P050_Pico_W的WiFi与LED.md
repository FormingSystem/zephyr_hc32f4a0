---
id: learning.zephyr-docs.board-samples.page-50
title: Pico_W的WiFi与LED
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/raspberrypi/pico_w_wifi_led/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="pico-w-wifi-led"></a>

# 第50章\_Pico W 的 WiFi 与 LED（Pico W WiFi + LED）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/raspberrypi/pico_w_wifi_led/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/raspberrypi/pico_w_wifi_led/README.rst/..)

<a id="overview"></a>

## 50.1 概述（Overview）

本示例展示在 Raspberry Pi Pico W 和 Pico 2 W 上同时运行 WiFi 与 LED。后台线程通过 CYW43 GPIO 驱动使板载 LED 闪烁，主线程则执行 WiFi 扫描。

> 译注——LED 的硬件路径：本次 overlay 将 led0 指向 cyw43_gpio 的 GPIO 0，所以通过 WiFi 芯片的 GPIO 控制板载 LED；不要将它误改为普通 RP2040／RP2350 引脚。后台线程每 500 ms 翻转一次，主线程的扫描与之并行。

<a id="requirements"></a>

## 50.2 前提条件（Requirements）

本示例需要搭载 Infineon CYW43439 WiFi 芯片的开发板：

> 译注——板目标与版本：W 后缀对应无线版本。本次上游 Pico 2 W overlay 文件名为 rpi_pico2_rp2350a_m33_0_w.overlay，与 m33_0 板目标一致；本仓库参照源码仍可能使用旧的 m33 文件名，不能混用新旧命名或据文件缺失直接认定板不受支持。

- Raspberry Pi Pico W（`rpi_pico/rp2040/w`）

- Raspberry Pi Pico 2 W（`rpi_pico2/rp2350a/m33_0/w`）

<a id="building-and-running"></a>

## 50.3 构建与运行（Building and Running）

> 译注——执行前提：west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具、工作区、模块和目标工具链；应用与 overlay 为官方源码，构建目录由工具生成。构建成功后按具体板文档处理下载与启动，不能把通用 west flash 视为所有板都采用同一种连接方式。失败时先检查构建输出、目标板配置和实际硬件；本次没有运行这些命令或进行实板测量。

```text
# From the root of the zephyr repository
west build -b rpi_pico2/rp2350a/m33_0/w samples/boards/raspberrypi/pico_w_wifi_led
west flash
```

<a id="sample-output"></a>

## 50.4 输出示例（Sample Output）

> 译注——扫描完成判据：SSID 为服务集标识符（Service Set Identifier，即网络名称），CH 为信道，RSSI 为接收信号强度指示（Received Signal Strength Indicator）。扫描只发现网络，不代表已连接接入点或能访问互联网。源码最多等待 scan_done 信号量 15 秒，却未检查 k_sem_take() 返回值；Demo complete 不能单独证明扫描成功，应查看扫描结果和 WiFi scan complete 事件及错误信息。

```text
*** Booting Zephyr OS build v4.3.0 ***
Pico W WiFi + LED Demo
LED blinking started
Starting WiFi scan...
  SSID: MyNetwork              CH:  6 RSSI: -45
WiFi scan complete
Demo complete - LED continues blinking
```

<a id="see-also"></a>

## 50.5 另请参阅（See also）

[通用输入输出（General-Purpose Input/Output，GPIO）](../hardware/P266_GPIO公共接口.md)

> 译注——源码入口：[main.c](../../../samples/boards/raspberrypi/pico_w_wifi_led/src/main.c)；[prj.conf](../../../samples/boards/raspberrypi/pico_w_wifi_led/prj.conf)。本地参照实现使用相对路径，版本可能与本次网页不同。 新版 Pico 2 W 配置见[上游 overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/raspberrypi/pico_w_wifi_led/boards/rpi_pico2_rp2350a_m33_0_w.overlay)。

对应官方文档源码：[samples/boards/raspberrypi/pico_w_wifi_led/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/raspberrypi/pico_w_wifi_led/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/raspberrypi/pico_w_wifi_led/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P049_TI示例目录.md) · [返回大纲](大纲.md) · [下一章](P051_Raspberry_Pi板信息.md)
