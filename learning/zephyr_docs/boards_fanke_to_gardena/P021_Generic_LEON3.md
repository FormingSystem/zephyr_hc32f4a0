---
id: learning.zephyr-docs.boards-fanke-to-gardena.page-21
title: Generic LEON3
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/gaisler/generic_leon3/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="generic_leon3"></a>

# 第21章\_通用LEON3（Generic LEON3）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/gaisler/generic_leon3/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`generic_leon3`

厂商（Vendor）：

[Gaisler](https://docs.zephyrproject.org/latest/boards/index.html#vendor=gaisler)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[sparc](https://docs.zephyrproject.org/latest/boards/index.html#arch=sparc)

片上系统（SoC）：

[leon3](https://docs.zephyrproject.org/latest/boards/index.html#soc=leon3)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gaisler/generic_leon3/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

此开发板配置适用于GRLIB GPL发行版提供的LEON3处理器模板设计，也可用于TSIM3 LEON3仿真器的评估版本（Evaluation Version）。

<a id="hardware"></a>

## 硬件（Hardware）

该配置兼容大多数GRLIB LEON3 FPGA模板设计，例如Digilent Arty A7、Terasic DE0-Nano及Microsemi M2GL-EVAL-KIT。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`generic_leon3`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

<a id="building"></a>

### 构建（Building）

`generic_leon3`应用可按常规方法构建，详见构建应用。为此目标构建时，将`BOARD`变量设为`generic_leon3`。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)）

<a id="running-on-hardware"></a>

### 在硬件上运行（Running on Hardware）

通过GRMON连接，然后加载并运行应用。下面以Terasic DE2-115 Cyclone IV FPGA开发板为例。

```text
$ grmon -altjtag -u
  GRMON debug monitor v3.2.8 eval version

  Copyright (C) 2020 Cobham Gaisler - All rights reserved.
  For latest updates, go to http://www.gaisler.com/
  Comments or bug-reports to support@gaisler.com

JTAG chain (1): EP3C120/EP4CE115
  GRLIB build version: 4250
  Detected frequency:  50.0 MHz

  Component                            Vendor
  LEON3 SPARC V8 Processor             Cobham Gaisler
  AHB Debug UART                       Cobham Gaisler
  JTAG Debug Link                      Cobham Gaisler
  GR Ethernet MAC                      Cobham Gaisler
  GRDMAC DMA Controller                Cobham Gaisler
  LEON2 Memory Controller              European Space Agency
  AHB/APB Bridge                       Cobham Gaisler
  LEON3 Debug Support Unit             Cobham Gaisler
  Generic UART                         Cobham Gaisler
  Multi-processor Interrupt Ctrl.      Cobham Gaisler
  Modular Timer Unit                   Cobham Gaisler
  General Purpose I/O port             Cobham Gaisler
  SPI Controller                       Cobham Gaisler
  AHB Status Register                  Cobham Gaisler

  Use command 'info sys' to print a detailed report of attached cores

grmon3> load zephyr/zephyr.elf
      40000000 text              16.2kB /  16.2kB   [===============>] 100%
      400040A8 initlevel           40B              [===============>] 100%
      400040D0 rodata             484B              [===============>] 100%
      400042B4 datas               20B              [===============>] 100%
      400042C8 sw_isr_table       256B              [===============>] 100%
      400043C8 devices             36B              [===============>] 100%
  Total size: 16.98kB (1.91Mbit/s)
  Entry point 0x40000000
  Image zephyr/zephyr.elf loaded

grmon3> run
*** Booting Zephyr OS build zephyr-v2.4.0-30-ga124c31ec4cf  ***
Hello World! generic_leon3
```

<a id="running-in-simulation"></a>

### 在仿真器中运行（Running in Simulation）

同一个应用二进制文件可在TSIM3 LEON3仿真器中运行。

```text
$ tsim-leon3
 TSIM3 LEON3 SPARC simulator, version 3.0.2 (evaluation version)

 Copyright (C) 2020, Cobham Gaisler - all rights reserved.
 This software may only be used with a valid license.
 For latest updates, go to https://www.gaisler.com/
 Comments or bug-reports to support@gaisler.com

Number of CPUs: 2
system frequency: 50.000 MHz
icache: 1 * 4 KiB, 16 bytes/line (4 KiB total)
dcache: 1 * 4 KiB, 16 bytes/line (4 KiB total)
Allocated 4096 KiB SRAM memory, in 1 bank at 0x40000000
Allocated 32 MiB SDRAM memory, in 1 bank at 0x60000000
Allocated 2048 KiB ROM memory at 0x00000000

tsim> load zephyr/zephyr.elf
  section: text, addr: 0x40000000, size 16552 bytes
  section: initlevel, addr: 0x400040a8, size 40 bytes
  section: rodata, addr: 0x400040d0, size 484 bytes
  section: datas, addr: 0x400042b4, size 20 bytes
  section: sw_isr_table, addr: 0x400042c8, size 256 bytes
  section: devices, addr: 0x400043c8, size 36 bytes
  Read 436 symbols
tsim> run
  Initializing and starting from 0x40000000
*** Booting Zephyr OS build zephyr-v2.4.0-30-ga124c31ec4cf  ***
Hello World! generic_leon3
```

<a id="references"></a>

## 参考资料（References）


- [GRLIB IP库与LEON3，GPL版本](https://www.gaisler.com/index.php/downloads/leongrlib)
- [TSIM3 LEON3仿真器（Simulator）](https://www.gaisler.com/index.php/products/simulators/tsim3/tsim3-leon3)
- [GRMON3调试监控器（Debug Monitor）](https://www.gaisler.com/index.php/products/debug-tools/grmon3)

## 译注

GRMON在硬件上加载运行与TSIM3仿真分别保留，本文没有将模拟器运行等同于实板验证。

---

[上一章](P020_UCAN.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P022_GR716-MINI_Development_Board.md)
