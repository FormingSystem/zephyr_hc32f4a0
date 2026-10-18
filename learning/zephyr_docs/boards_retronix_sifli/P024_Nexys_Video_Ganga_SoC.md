---
id: learning.zephyr-docs.boards-retronix-sifli.page-24
title: Nexys Video Ganga SoC
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shakti/nexys_ganga/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nexys_ganga"></a>

# 第24章\_Nexys Video上的Ganga SoC

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shakti/nexys_ganga/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`nexys_ganga`

厂商（Vendor）：

[SHAKTI处理器计划（Processor Program）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=shakti)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：



片上系统（SoC）：

[ganga](https://docs.zephyrproject.org/latest/boards/index.html#soc=ganga)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/shakti/nexys_ganga/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

SHAKTI由印度理工学院马德拉斯分校（IIT Madras）的RISE团队开发，原文称其为印度首个本土开源RISC-V处理器项目。Ganga是64位RV64IMAC SHAKTI SoC，提供核内本地中断控制器（CLINT）、平台级中断控制器（PLIC）、机器定时器，以及Zephyr控制台使用的UART。

此板级目标在采用Xilinx Artix-7 FPGA的Digilent Nexys Video上，以软核（Soft Core）形式运行Ganga SoC。应用可经板载USB JTAG芯片，通过JTAG加载到FPGA。

完整硬件源码及比特流（Bitstream）构建、加载步骤均已提供，见下方参考资料。

更多信息见以下参考资料：


- [SHAKTI处理器项目](https://shakti.org.in/)
- [SHAKTI gc2025源码](https://gitlab.com/shaktiproject/gc2025)
- [Nexys Video参考手册](https://digilent.com/reference/programmable-logic/nexys-video/reference-manual)

<a id="hardware"></a>

## 硬件（Hardware）


- Ganga CPU，RV64IMAC指令集，运行于40 MHz
- CLINT及PLIC中断控制器，带机器定时器（Machine Timer）
- 256 MB RAM
- Zephyr控制台使用的UART，波特率19200
- 通过板载USB JTAG芯片提供JTAG接口

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`nexys_ganga`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="nexys_ganga-hw-features"></a>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`nexys_ganga`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

加载任何Zephyr应用前，必须先用Ganga比特流配置FPGA；构建及加载步骤见SHAKTI gc2025源码。比特流加载后，即可按常规方式构建及烧录Zephyr应用。

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

开发板通过UART0提供控制台，所用串口终端应采用以下设置：


- 波特率：19200
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

可通过uart0设备树节点的current-speed属性更改波特率。

<a id="flashing"></a>

### 烧录（Flashing）

支持通过openocd运行工具执行west flash，以下为[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例：

```text
# From the root of the zephyr repository
west build -b nexys_ganga samples/hello_world
west flash
```

加载后，终端应显示类似以下消息：

```text
*** Booting Zephyr OS build ... ***
Hello World! nexys_ganga/ganga
```

应用加载到FPGA块RAM（Block RAM），不会持久保存；下次重新配置FPGA时会恢复原状态。

<a id="debugging"></a>

### 调试（Debugging）

支持通过openocd运行工具执行west debug，以下为[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例：

```text
# From the root of the zephyr repository
west build -b nexys_ganga samples/hello_world
west debug
```

<a id="references"></a>

## 参考资料（References）

## 译注

Nexys Ganga须先加载FPGA比特流，之后再加载Zephyr到块RAM；重配FPGA后应用不保留。默认控制台19200波特率，不套用其他板卡的115200。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [reference-manual](https://digilent.com/reference/programmable-logic/nexys-video/reference-manual)：HTTP Error 403: Forbidden。

---

[上一章](P023_SHAKTI.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P025_SiFli_Technologies.md)
