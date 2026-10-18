---
id: learning.zephyr-docs.boards-amd.page-7
title: Versal 2 RPU development board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/amd/versal2_rpu/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="versal2_rpu"></a>

# 第7章\_Versal 2实时处理单元开发板（RPU Development Board）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/amd/versal2_rpu/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`versal2_rpu`

厂商（Vendor）：

[Advanced Micro Devices（AMD）, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=amd)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[amd_versal2_rpu](https://docs.zephyrproject.org/latest/boards/index.html#soc=amd_versal2_rpu)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/amd/versal2_rpu/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

此配置为Xilinx Versal2片上系统上的R52实时处理单元（RPU）提供支持，可采用以下工作方式：


- 两个独立R52内核，各自具有紧耦合存储器（TCM）
- 或者组成带紧耦合存储器（TCM）的单个双核锁步单元（Dual Lock-Step Unit）

该处理单元基于ARM Cortex-R52 CPU，还启用以下设备：


- ARM GIC v3中断控制器（Interrupt Controller）
- 全局定时计数器（Global Timer Counter）
- 服务器基础系统架构通用异步收发器（SBSA UART）

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`versal2_rpu`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="versal2_rpu-hw-features"></a>

<a id="versal2_rpu-versal2_rpu/amd_versal2_rpu-hw-features-section"></a>

#### `versal2_rpu/amd_versal2_rpu`目标（Target）

<a id="versal2_rpu-versal2_rpu/amd_versal2_rpu-hw-features-panel"></a>

<a id="versal2_rpu-versal2_rpu/amd_versal2_rpu-hw-features-memory"></a>

该开发板目标的片上存储容量：2096960 KiB RAM、N/A Flash。

<a id="versal2_rpu-versal2_rpu/amd_versal2_rpu-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>片上（On-Chip）</td>
<td>ARM Cortex-R52处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/versal2_r52.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P011_arm_cortex-r52.md#std-dtcompatible-arm-cortex-r52"><code>arm,cortex-r52</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/amd/versal2_rpu/versal2_rpu.dts?plain=1#L18">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>AMD/Xilinx三通道定时计数器（TTC / Triple Timer Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal2.dtsi?plain=1#L288">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P015_xlnx_ttc.md#std-dtcompatible-xlnx-ttc"><code>xlnx,ttc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>AMD/Xilinx TTC定时器实例（Timer Instance）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal2.dtsi?plain=1#L298">已启用：3</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P014_xlnx_ttc-counter.md#std-dtcompatible-xlnx-ttc-counter"><code>xlnx,ttc-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Xilinx ADMA直接存储器访问控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal2.dtsi?plain=1#L208">已启用：8</a>）</td>
<td><a href="../dma_binding_reference/P007_amd_versal2-dma-1.0.md#std-dtcompatible-amd-versal2-dma-1.0"><code>amd,versal2-dma-1.0</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/versal2_r52.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>AMD-Xilinx处理器间中断邮箱控制器（IPI / Inter Processor Interrupt Mailbox Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal2.dtsi?plain=1#L32">已禁用：16</a>）</td>
<td><a href="../intercore_reference/P057_Versal核间中断邮箱绑定.md#dtbinding-xlnx-mbox-versal-ipi-mailbox"><code>xlnx,mbox-versal-ipi-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM服务器基础系统架构通用异步收发器（SBSA UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal2.dtsi?plain=1#L16">已启用：2</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P009_arm_sbsa-uart.md#std-dtcompatible-arm-sbsa-uart"><code>arm,sbsa-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/amd/versal2_rpu/versal2_rpu.dts?plain=1#L30">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/versal2_r52.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="devices"></a>

### 设备（Devices）

<a id="system-timer"></a>

#### 系统定时器（System Timer）

此开发板配置采用100 MHz的系统定时器节拍频率（Tick Frequency）。

<a id="serial-port"></a>

#### 串口（Serial Port）

此开发板配置使用片上UART0作为唯一的串行通信通道。

<a id="memories"></a>

#### 存储器（Memories）

虽然DTS文件定义了闪存（Flash）、DDR和片上存储器（OCM）区域，但应用的全部代码和数据都加载到指向DDR存储器的`sram0`区域。目前`ocm0`区域可供使用，只是默认不在其中放置内容。

<a id="known-problems-or-limitations"></a>

### 已知问题或限制（Known Problems or Limitations）

不支持以下平台功能：


- 仅支持R52子系统的第一个内核。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

按通常方式构建和烧录。以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b versal2_rpu samples/hello_world
west flash
```

控制台上应显示以下消息：

```text
Hello World! versal2_rpu/amd_versal2_rpu
```

<a id="references"></a>

## 参考资料（References）


1. ARMv8-R架构参考手册（Architecture Reference Manual），ARM DDI 0568A.c ID110520
2. Cortex-R52和Cortex-R52F技术参考手册（Technical Reference Manual），ARM DDI r1p4 100026_0104_01_en

---

[上一章](P006_AMD_Versal_Gen_2_APU_Development_Board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P008_AMD_Versal_APU_Development_Board.md)
