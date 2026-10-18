---
id: learning.zephyr-docs.boards-gd-to-iar.page-20
title: Quincy
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/google/quincy/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="google_quincy"></a>

# 第20章\_Quincy

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/google/quincy/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`google_quincy`

厂商（Vendor）：

[Google, Inc.（谷歌）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=google)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[npcx9mfp](https://docs.zephyrproject.org/latest/boards/index.html#soc=npcx9mfp)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/google/quincy/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Google Quincy是用于指纹相关功能开发的开发板。

开发板提供指纹传感器连接器，通过μServo及USB连接器引出UART控制台，可使用μServo或SWD烧录MCU。

<a id="hardware"></a>

## 硬件（Hardware）


- VFBGA144封装的NPCX99FPA0BX

<a id="peripheral-mapping"></a>

### 外设映射（Peripheral Mapping）


- UART_1（控制台 / CONSOLE）TX/RX：GPIO65／GPIO64
- UART_2（编程 / PROG）TX/RX：GPIO86／GPIO75
- SPI_0（SHI）CS/CLK/MISO/MOSI：GPIO53／GPIO55／GPIO47／GPIO46
- SPI_1（SPIP）CS/CLK/MISO/MOSI：GPIOA6／GPIOA1／GPIO95／GPIOA3
- SPI_2（GP）CS/CLK/MISO/MOSI：GPIO30／GPIO25／GPIO24／GPIO31

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`google_quincy`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>调试服务器（debugserver）</th>
<th>复位（reset）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-jlink">jlink</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
</table>

<a id="id2"></a>

<a id="id4"></a>

按常规方式为`google_quincy`目标构建应用，通过μServo或接到J4的外部J-Link烧录。若使用μServo，请按照[Chromium EC烧录文档](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board)[注1](#id1)及[Chromium Servo Micro文档](https://chromium.googlesource.com/chromiumos/third_party/hdctools/+/master/docs/servo_micro.md)[注2](#id3)操作。

<a id="debugging"></a>

### 调试（Debugging）

通过SWD使用J-Link。

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board)

<a id="id3"></a>

〔[2](#id4)〕 [https://chromium.googlesource.com/chromiumos/third_party/hdctools/+/master/docs/servo_micro.md](https://chromium.googlesource.com/chromiumos/third_party/hdctools/+/master/docs/servo_micro.md)

---

[上一章](P019_Google_Inc..md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P021_Twinkie_V2.md)
