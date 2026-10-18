---
id: learning.zephyr-docs.boards-gd-to-iar.page-18
title: Icetower Development Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/google/icetower/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="google_icetower"></a>

# 第18章\_Icetower开发板（Development Board）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/google/icetower/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`google_icetower`

厂商（Vendor）：

[Google, Inc.（谷歌）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=google)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[stm32h743xx](https://docs.zephyrproject.org/latest/boards/index.html#soc=stm32h743xx)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/google/icetower/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Google Icetower是Google为指纹相关功能开发而创建的开发板。

<a id="id4"></a>

开发板提供指纹传感器连接器，通过[μServo](https://chromium.googlesource.com/chromiumos/third_party/hdctools/+/master/docs/servo_micro.md)[注2](#id3)连接器引出控制台，可使用μServo或SWD烧录MCU。

<a id="hardware"></a>

## 硬件（Hardware）


- LQFP100封装的STM32H7A3VIT6

<a id="pin-mapping"></a>

### 引脚映射（Pin Mapping）

<a id="default-zephyr-peripheral-mapping"></a>

#### Zephyr 默认外设映射（Peripheral Mapping）：


- `USART_1 TX/RX : PA9/PA10`
- `SPI_1 CS/CLK/MISO/MOSI : PA4/PA5/PA6/PA7`
- `SPI_4 CS/CLK/MISO/MOSI : PE11/PE12/PE13/PE14`

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`google_icetower`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>✅</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-stm32cubeprogrammer">stm32cubeprogrammer</a></td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

<a id="id2"></a>

按常规方式为`google_icetower`开发板构建应用，通过μServo或接到J4的外部J-Link烧录。若使用μServo，请按照[Chromium EC烧录文档](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board)[注1](#id1)操作。

<a id="debugging"></a>

### 调试（Debugging）

通过SWD使用J-Link或ST-Link。注意，必须将SW2设到CORESIGHT位置。

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board)

<a id="id3"></a>

〔[2](#id4)〕 [https://chromium.googlesource.com/chromiumos/third_party/hdctools/+/master/docs/servo_micro.md](https://chromium.googlesource.com/chromiumos/third_party/hdctools/+/master/docs/servo_micro.md)

---

[上一章](P017_Dragonclaw_Development_Board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P019_Google_Inc..md)
