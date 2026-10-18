---
id: learning.zephyr-docs.boards-pimoroni-radxa.page-11
title: Decawave DWM1001
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/qorvo/decawave_dwm1001_dev/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="decawave_dwm1001_dev"></a>

# 第11章\_Decawave DWM1001

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qorvo/decawave_dwm1001_dev/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`decawave_dwm1001_dev`

厂商（Vendor）：

[Qorvo, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=qorvo)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[nrf52832](https://docs.zephyrproject.org/latest/boards/index.html#soc=nrf52832)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/qorvo/decawave_dwm1001_dev/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

DWM1001开发板包含DWM1001模块、电池连接器及充电电路、LED、按键、Raspberry Pi连接器及USB连接器。板上还配有J-Link OB，提供调试及虚拟COM端口（Virtual COM Port）功能。

<a id="id6"></a>

<a id="id4"></a>

<a id="id2"></a>

开发板信息见[Qorvo（Decawave）DWM1001-DEV网站](https://www.qorvo.com/products/p/DWM1001-DEV)[注3](#id5)，板上模块信息见[Qorvo（Decawave）DWM1001网站](https://www.qorvo.com/products/p/DWM1001C)[注2](#id3)；芯片的官方参考资料见[nRF52832网站](https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52832)[注1](#id1)。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`decawave_dwm1001_dev`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>复位（reset）</th>
<th>调试服务器（debugserver）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-jlink">jlink</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td></td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-pyocd">pyocd</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

decawave_dwm1001_dev板级配置的应用可按常规流程构建、烧录及调试。构建及运行详情见“[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)”及“[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)”。

<a id="flashing"></a>

### 烧录（Flashing）

按照[Nordic nRF5x Segger J-Link](../debugging/P005_Nordic_Segger_JLink.md#nordic-segger)页面安装并配置所需软件，更多信息见[烧录（Flashing）](../debugging/P005_Nordic_Segger_JLink.md#nordic-segger-flashing)。随后按常规方式构建和烧录应用；详见[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)和[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)。

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

首先运行常用终端程序查看输出。

```text
$ minicom -D <tty_device> -b 115200
```

将<tty_device>替换为nRF52 DK所在串口，例如Linux下的/dev/ttyACM0。

随后按通常方式构建并烧录应用。

```text
# From the root of the zephyr repository
west build -b decawave_dwm1001_dev samples/hello_world
west flash
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52832](https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52832)

<a id="id3"></a>

〔[2](#id4)〕 [https://www.qorvo.com/products/p/DWM1001C](https://www.qorvo.com/products/p/DWM1001C)

<a id="id5"></a>

〔[3](#id6)〕 [https://www.qorvo.com/products/p/DWM1001-DEV](https://www.qorvo.com/products/p/DWM1001-DEV)

## 译注

DWM1001开发板含J-Link OB及虚拟COM端口；保留模块和开发板资料入口的区别。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [nRF52832](https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52832)：HTTP Error 403: Forbidden。
- [DWM1001-DEV](https://www.qorvo.com/products/p/DWM1001-DEV)：HTTP Error 429: Too Many Requests。
- [DWM1001C](https://www.qorvo.com/products/p/DWM1001C)：HTTP Error 429: Too Many Requests。

---

[上一章](P010_QCC744M_Evaluation_Kit.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P012_Decawave_DWM3001CDK.md)
