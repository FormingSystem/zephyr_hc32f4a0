---
id: learning.zephyr-docs.boards-panasonic-particle-pcbcupid-peregrine.page-7
title: PAN B611 Evaluation Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/panasonic/panb611evb/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="panb611evb"></a>

# 第7章\_PAN B611评估板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/panasonic/panb611evb/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/panb611evb.webp](images/panb611evb.webp)](images/panb611evb.webp)

PAN B611评估板

名称（Name）：

`panb611evb`

厂商（Vendor）：

[松下（Panasonic Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=panasonic)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)、[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[nrf54l15](https://docs.zephyrproject.org/latest/boards/index.html#soc=nrf54l15)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/panasonic/panb611evb/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

PAN B611评估板panb611evb是PAN B611模块的开发工具，该模块基于Nordic Semiconductor nRF54L15芯片。

<a id="id3"></a>

PAN B611模块变体及评估板的更多信息见[产品网站](https://pideu.panasonic.de/development-hub/panb611/)[注1](#id2)。

<a id="usage"></a>

## 用途（Usage）

<a id="id8"></a>

<a id="id5"></a>

PAN B611评估板的[panb611evb用户指南](https://pideu.panasonic.de/development-hub/panb611/evaluation_board/user_guide/)[注3](#id7)位于松下无线连接开发中心[注2](#id4)。（[松下无线连接开发中心（Panasonic Wireless Connectivity Development Hub）](https://pideu.panasonic.de/development-hub/)）

用户指南详细介绍以下内容及其他事项：


- 引脚映射（Pin Mapping）
- 供电选项（Powering Options）
- 引出排针接口（Breakout Pin Header Interface）
- 电流消耗测量（Current Consumption Measurement）
- 软件开发（Software Development）

以及其他事项。

<a id="id10"></a>

<a id="id6"></a>

PANB611原理图位于松下无线连接开发中心[注2](#id4)的[PANB611下载区](https://pideu.panasonic.de/development-hub/panb611/downloads/)[注4](#id9)。（[松下无线连接开发中心（Panasonic Wireless Connectivity Development Hub）](https://pideu.panasonic.de/development-hub/)）

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`panb611evb`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>✅</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>nrfutil</td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

panb611evb/nrf54l15/cpuapp目标的应用可按常规方法构建、烧录及调试。构建和运行详情见“构建应用”及“运行应用”。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）

<a id="id2"></a>

〔[1](#id3)〕 [https://pideu.panasonic.de/development-hub/panb611/](https://pideu.panasonic.de/development-hub/panb611/)

<a id="id4"></a>

〔2〕 ([1](#id5),[2](#id6)) [https://pideu.panasonic.de/development-hub/](https://pideu.panasonic.de/development-hub/)

<a id="id7"></a>

〔[3](#id8)〕 [https://pideu.panasonic.de/development-hub/panb611/evaluation_board/user_guide/](https://pideu.panasonic.de/development-hub/panb611/evaluation_board/user_guide/)

<a id="id9"></a>

〔[4](#id10)〕 [https://pideu.panasonic.de/development-hub/panb611/downloads/](https://pideu.panasonic.de/development-hub/panb611/downloads/)

## 译注

PAN B611基于nRF54L15，应用核使用panb611evb/nrf54l15/cpuapp目标。

---

[上一章](P006_PAN1783_Evaluation_Board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P008_Argon.md)
