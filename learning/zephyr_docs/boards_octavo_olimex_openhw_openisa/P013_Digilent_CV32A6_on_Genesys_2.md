---
id: learning.zephyr-docs.boards-octavo-olimex-openhw-openisa.page-13
title: Digilent CV32A6 on Genesys 2
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/openhwgroup/cv32a6_genesys_2/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="cv32a6_genesys_2"></a>

# 第13章\_Digilent Genesys 2上的CV32A6

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/openhwgroup/cv32a6_genesys_2/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/cv32a6_genesys_2.webp](images/cv32a6_genesys_2.webp)](images/cv32a6_genesys_2.webp)

Digilent Genesys 2上的CV32A6

名称（Name）：

`cv32a6_genesys_2`

厂商（Vendor）：

[OpenHW Group](https://docs.zephyrproject.org/latest/boards/index.html#vendor=openhwgroup)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[cv32a6](https://docs.zephyrproject.org/latest/boards/index.html#soc=cv32a6)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/openhwgroup/cv32a6_genesys_2/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Digilent Genesys 2配备Xilinx Kintex-7现场可编程门阵列（FPGA），可运行多种软核CPU（Softcore CPU）。此配置使用32位CVA6 RISC-V CPU。SoC包含连接板载DRAM的存储控制器、PLIC及CLINT中断控制器、连接USB UART的UART设备、通过FTDI USB JTAG芯片连接的RISC-V兼容调试模块、连接SD卡槽的Xilinx SPI接口，以及连接LED和开关的Xilinx GPIO。完整硬件源码见第一项参考资料，其中也提供编译及将配置加载到Genesys 2的说明。

更多信息见以下参考资料：


- [CVA6文档](https://github.com/openhwgroup/cva6)
- [Genesys 2参考手册（Reference Manual）](https://digilent.com/reference/programmable-logic/genesys-2/reference-manual)
- [Genesys 2原理图（Schematic）](https://digilent.com/reference/_media/reference/programmable-logic/genesys-2/genesys-2_sch.pdf)

<a id="hardware"></a>

## 硬件（Hardware）


- CVA6 CPU，支持RV32imac指令集，带平台级中断控制器（PLIC）及核本地中断控制器（CLINT）
- 1 GB DDR3 DRAM
- 10／100／1000以太网，铜缆接口及lowRISC以太网MAC
- 兼容ns16550a的USB UART，115200波特
- RISC-V调试模块，通过板载FTDI USB JTAG连接
- Xilinx SPI控制器，连接MicroSD卡槽
- Xilinx GPIO，连接7个开关及LED

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`cv32a6_genesys_2`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="cv32a6_genesys_2-hw-features"></a>

<a id="cv32a6_genesys_2-cv32a6_genesys_2/cv32a6-hw-features-section"></a>

#### `cv32a6_genesys_2/cv32a6`目标（Target）

<a id="cv32a6_genesys_2-cv32a6_genesys_2/cv32a6-hw-features-panel"></a>

<a id="cv32a6_genesys_2-cv32a6_genesys_2/cv32a6-hw-features-memory"></a>

该开发板目标的片上存储容量：1 GiB RAM、N/A Flash。

<a id="cv32a6_genesys_2-cv32a6_genesys_2/cv32a6-hw-features-table"></a>

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
<td>OpenHW Group CVA6 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cv32a6.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P024_openhwgroup_cva6.md#std-dtcompatible-openhwgroup-cva6"><code>openhwgroup,cva6</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L16">已启用：2</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Xilinx AXI DMA LogiCORE IP控制器，其兼容字符串是在配合AXI以太网子系统使用时生成的（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L108">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P017_xlnx_eth-dma.md#std-dtcompatible-xlnx-eth-dma"><code>xlnx,eth-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Xilinx AXI GPIO硬件IP（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L141">已启用：1</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P032_xlnx_xps-gpio-1.00.a.md#std-dtcompatible-xlnx-xps-gpio-1.00.a"><code>xlnx,xps-gpio-1.00.a</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>SiFive RISCV-V平台级中断控制器（PLIC / Platform-Local Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P009_sifive_plic-1.0.0.md#std-dtcompatible-sifive-plic-1.0.0"><code>sifive,plic-1.0.0</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive RISC-V内核本地中断器（Core-Local Interruptor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L88">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P010_sifive_clint0.md#std-dtcompatible-sifive-clint0"><code>sifive,clint0</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>RISC-V CPU中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cv32a6.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P006_riscv_cpu-intc.md#std-dtcompatible-riscv-cpu-intc"><code>riscv,cpu-intc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L55">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Xilinx AXI四线SPI（Quad SPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P020_xlnx_xps-spi-2.00.a.md#std-dtcompatible-xlnx-xps-spi-2.00.a"><code>xlnx,xps-spi-2.00.a</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>RISC-V机器模式定时器（Machine Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L95">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer"><code>riscv,machine-timer</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

<a id="loading-the-fpga-configuration"></a>

### 加载FPGA配置（Loading the FPGA Configuration）

向开发板加载Zephyr前，必须先用Xilinx Vivado生成位流（Bitstream），并加载到FPGA。步骤见CVA6文档。此配置兼容以下构建目标：cv32a6_imac_sv0、cv32a6_imac_sv32、cv32a6_imafc_sv32及cv32a6_ima_sv32_fpga。

<a id="flashing"></a>

### 烧录（Flashing）

openocd运行工具支持west flash，以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b cv32a6_genesys_2 samples/hello_world
west flash
```

<a id="debugging"></a>

### 调试（Debugging）

openocd运行工具支持west debug、attach及debugserver命令，以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b cv32a6_genesys_2 samples/hello_world
west debug
```

<a id="references"></a>

## 参考资料（References）

## 译注

CV32A6需先用Vivado生成并加载FPGA位流，再加载Zephyr；四种受支持的32位CVA6构建目标逐项保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [genesys-2_sch.pdf](https://digilent.com/reference/_media/reference/programmable-logic/genesys-2/genesys-2_sch.pdf)：HTTP Error 403: Forbidden。
- [reference-manual](https://digilent.com/reference/programmable-logic/genesys-2/reference-manual)：HTTP Error 403: Forbidden。

---

[上一章](P012_OLIMEX-STM32-P405.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_Digilent_CV64A6_on_Genesys_2.md)
