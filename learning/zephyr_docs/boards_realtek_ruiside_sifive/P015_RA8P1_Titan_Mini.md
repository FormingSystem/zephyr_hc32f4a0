---
id: learning.zephyr-docs.boards-realtek-ruiside-sifive.page-15
title: RA8P1 Titan Mini
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ruiside/ra8p1_titan_mini/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="ra8p1_titan_mini"></a>

# 第15章\_RA8P1 Titan Mini

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ruiside/ra8p1_titan_mini/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/ra8p1_titan_mini.webp](images/ra8p1_titan_mini.webp)](images/ra8p1_titan_mini.webp)

RA8P1 Titan Mini

名称（Name）：

`ra8p1_titan_mini`

厂商（Vendor）：

[上海睿赛德电子科技有限公司（Shanghai Ruiside Electronic Technology Co., Ltd.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=ruiside)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[r7ka8p1kflcac](https://docs.zephyrproject.org/latest/boards/index.html#soc=r7ka8p1kflcac)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ruiside/ra8p1_titan_mini/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Titan Board Mini是RT-Thread推出的开发板，基于Renesas R7KA8P1芯片，采用Cortex-M85及Cortex-M33双核架构。它为工程师提供灵活且完整的开发平台，帮助开发者深入了解及实践嵌入式物联网。

RA8P1 MCU集成最高1 GHz的高性能Arm Cortex-M85核，以及最高250 MHz的Arm Cortex-M33核，具有以下功能：


- 最多1 MB磁阻式RAM（MRAM）
- 2 MB SRAM，包括256 KB CM85紧耦合存储器（TCM）RAM、128 KB CM33 TCM RAM及1664 KB用户SRAM
- Arm Ethos-U55神经网络处理器（NPU）
- 八线串行外设接口（OSPI / Octal Serial Peripheral Interface）
- 三层以太网交换模块（ESWM）、USB全速（USBFS）、USB高速（USBHS）及SD／MMC主机接口
- 图形LCD控制器（GLCDC）
- 二维绘图引擎（DRW / 2D Drawing Engine）
- MIPI DSI／CSI接口
- 模拟外设（Analog Peripherals）
- 信息安全与功能安全（Security and Safety）功能

<a id="key-features"></a>

### 主要特性（Key Features）


- Renesas R7KA8P1 MCU，289引脚FBGA封装
- Arm Cortex-M85核，最高1 GHz
- Arm Cortex-M33核，最高250 MHz
- Arm Ethos-U55神经网络处理器（NPU），用于AI加速
- 最多1 MB MRAM及2 MB SRAM
- 两个支持千兆以太网的外部端口
- 支持时间敏感网络（TSN），包括IEEE 802.1AS-2020、IEEE 802.1Qbv／802.3br及IEEE 802.1Qbu
- 支持网络冗余（Network Redundancy），包括设备级环网（DLR）及并行冗余协议（PRP）
- 主机接口：并行、串行、双线、四线及八线
- 存储器接口：Octa-SPI、Quad-SPI、HyperRAM、HyperFLASH及SRAM
- UART、RS-485、CAN FD、I2C、SPI、OSPI、SDHI、USBHS及USBFS接口
- 官方RT-Thread SDK中提供PWM定时器、ADC、RTC、看门狗、PDM麦克风、IMU、显示及摄像头示例
- SWD调试接口，支持J-Link调试器

<a id="id3"></a>

更多板卡信息见[RA8P1 Titan Mini Board GitHub仓库](https://github.com/RT-Thread-Studio/sdk-bsp-ra8p1-titan-mini)[注1](#id2)。

<a id="hardware"></a>

## 硬件（Hardware）

详细硬件信息见：


- <a id="id9"></a>

  RA8P1 MCU：[RA8P1系列硬件用户手册](https://www.renesas.com/us/en/document/mah/ra8p1-group-users-manual-hardware)[注3](#id8)
- <a id="id4"></a>

  Titan Board Mini：[RA8P1 Titan Mini Board GitHub仓库](https://github.com/RT-Thread-Studio/sdk-bsp-ra8p1-titan-mini)[注1](#id2)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`ra8p1_titan_mini`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="ra8p1_titan_mini-hw-features"></a>

<a id="ra8p1_titan_mini-ra8p1_titan_mini/r7ka8p1kflcac/cm33-hw-features-section"></a>

#### `ra8p1_titan_mini/r7ka8p1kflcac/cm33`目标（Target）

<a id="ra8p1_titan_mini-ra8p1_titan_mini/r7ka8p1kflcac/cm33-hw-features-panel"></a>

<a id="ra8p1_titan_mini-ra8p1_titan_mini/r7ka8p1kflcac/cm33-hw-features-memory"></a>

该开发板目标的片上存储容量：640 KiB RAM、256 KiB Flash。

<a id="ra8p1_titan_mini-ra8p1_titan_mini/r7ka8p1kflcac/cm33-hw-features-table"></a>

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
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="3">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA ADC_B控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L266">已禁用：1</a>）</td>
<td><a href="../hardware/P865_RenesasRAADCB控制器绑定.md#dtbinding-renesas-ra-adc-b-controller"><code>renesas,ra-adc-b-controller</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA ADC_B扫描组（Scan Group）配置节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L276">已禁用：9</a>）</td>
<td><a href="../hardware/P866_RenesasRAADCB扫描组绑定.md#dtbinding-renesas-ra-adc-b-scan-group"><code>renesas,ra-adc-b-scan-group</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA ADC_B转换器单元（Converter Unit）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L330">已禁用：2</a>）</td>
<td><a href="../hardware/P867_RenesasRAADCB实例绑定.md#dtbinding-renesas-ra-adc-b"><code>renesas,ra-adc-b</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA的Arm Ethos-U NPU前端（Frontend）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L12">已禁用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P019_renesas_ra-npu.md#std-dtcompatible-renesas-ra-npu"><code>renesas,ra-npu</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA脉冲密度调制接口（PDM-IF）的一个通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1075">已禁用：3</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P015_renesas_ra-pdm.md#std-dtcompatible-renesas-ra-pdm"><code>renesas,ra-pdm</code></a></td>
</tr>
<tr>
<td rowspan="8">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA时钟生成电路（Clock Generation Circuit）的外部时钟配置（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P029_renesas_ra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock"><code>renesas,ra-cgc-external-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L33">已启用：4</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA子时钟（Sub-Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L51">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P004_renesas_ra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk"><code>renesas,ra-cgc-subclk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA时钟生成电路的锁相环时钟（PLL Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L57">已启用：2</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P003_renesas_ra-cgc-pll.md#std-dtcompatible-renesas-ra-cgc-pll"><code>renesas,ra-cgc-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA时钟生成电路（Clock Generation Circuit）的PLL时钟输出线（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L67">已启用：6</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P002_renesas_ra-cgc-pll-out.md#std-dtcompatible-renesas-ra-cgc-pll-out"><code>renesas,ra-cgc-pll-out</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA时钟控制节点的pclk模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L118">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P030_renesas_ra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block"><code>renesas,ra-cgc-pclk-block</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA时钟控制外设时钟（Peripheral Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L128">已启用：18</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L222">已禁用：9</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P001_renesas_ra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk"><code>renesas,ra-cgc-pclk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA外部总线时钟（External Bus Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L206">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P028_renesas_ra-cgc-busclk.md#std-dtcompatible-renesas-ra-cgc-busclk"><code>renesas,ra-cgc-busclk</code></a></td>
</tr>
<tr>
<td rowspan="3">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA高速模拟比较器（ACMPHS）全局节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1134">已禁用：1</a>）</td>
<td><a href="../hardware/P748_RenesasRA高速模拟比较器全局绑定.md#dtbinding-renesas-ra-acmphs-global"><code>renesas,ra-acmphs-global</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA高速模拟比较器（ACMPHS）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1139">已禁用：4</a>）</td>
<td><a href="../hardware/P749_RenesasRA高速模拟比较器绑定.md#dtbinding-renesas-ra-acmphs"><code>renesas,ra-acmphs</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA低电压检测（LVD）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1164">已禁用：4</a>）</td>
<td><a href="../hardware/P750_RenesasRA电压检测器绑定.md#dtbinding-renesas-ra-lvd"><code>renesas,ra-lvd</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>用作计数器的Renesas RA异步通用定时器（AGT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L908">已禁用：2</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P014_renesas_ra-agt-counter.md#std-dtcompatible-renesas-ra-agt-counter"><code>renesas,ra-agt-counter</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA超低功耗定时器（ULPT）计数器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1016">已禁用：2</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P015_renesas_ra-ulpt-counter.md#std-dtcompatible-renesas-ra-ulpt-counter"><code>renesas,ra-ulpt-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1120">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P008_renesas_ra-crc.md#std-dtcompatible-renesas-ra-crc"><code>renesas,ra-crc</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>Renesas图形LCD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L82">已禁用：1</a>）</td>
<td><a href="../display_panel_renesas_sharp_binding_reference/P011_renesas_ra-glcdc.md#std-dtcompatible-renesas-ra-glcdc"><code>renesas,ra-glcdc</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1110">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P012_renesas_ra-dma.md#std-dtcompatible-renesas-ra-dma"><code>renesas,ra-dma</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA以太网媒体访问控制器（MAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L955">已禁用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P015_renesas_ra-eswm.md#std-dtcompatible-renesas-ra-eswm"><code>renesas,ra-eswm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA以太网媒体访问控制器（MAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L968">已禁用：2</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P016_renesas_ra-ethernet-rmac.md#std-dtcompatible-renesas-ra-ethernet-rmac"><code>renesas,ra-ethernet-rmac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA外部管理数据输入输出控制器（MDIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L982">已禁用：2</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P005_renesas_ra-mdio-rmac.md#std-dtcompatible-renesas-ra-mdio-rmac"><code>renesas,ra-mdio-rmac</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA闪存／MRAM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L92">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P029_renesas_ra-mram-controller.md#std-dtcompatible-renesas-ra-mram-controller"><code>renesas,ra-mram-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA通用输入输出端口（GPIO I/O Port）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L125">已启用：12</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L216">已禁用：2</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P014_renesas_ra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport"><code>renesas,ra-gpio-ioport</code></a></td>
</tr>
<tr>
<td rowspan="2">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L353">已禁用：3</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P014_renesas_ra-iic.md#std-dtcompatible-renesas-ra-iic"><code>renesas,ra-iic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA SCI-B I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L390">已禁用：10</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P012_renesas_ra-i2c-sci-b.md#std-dtcompatible-renesas-ra-i2c-sci-b"><code>renesas,ra-i2c-sci-b</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1052">已禁用：2</a>）</td>
<td><a href="../i2s_binding_reference/P014_renesas_ra-i2s-ssie.md#std-dtcompatible-renesas-ra-i2s-ssie"><code>renesas,ra-i2s-ssie</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1041">已禁用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P008_renesas_ra-i3c.md#std-dtcompatible-renesas-ra-i3c"><code>renesas,ra-i3c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ruiside/ra8p1_titan_mini/ra8p1_titan_mini.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ruiside/ra8p1_titan_mini/ra8p1_titan_mini.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">本地互连网络（LIN）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA LIN SCI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L407">已禁用：10</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P002_renesas_ra-lin-sci-b.md#std-dtcompatible-renesas-ra-lin-sci-b"><code>renesas,ra-lin-sci-b</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>Renesas核间通信邮箱（IPC MBOX）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L62">已禁用：2</a>）</td>
<td><a href="../intercore_reference/P051_RenesasRA邮箱绑定.md#dtbinding-renesas-ra-ipc-mbox"><code>renesas,ra-ipc-mbox</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA SDRAM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1102">已启用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P005_renesas_ra-sdram.md#std-dtcompatible-renesas-ra-sdram"><code>renesas,ra-sdram</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示串行接口（MIPI-DSI）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA MIPI DSI主机（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L89">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P016_renesas_ra-mipi-dsi.md#std-dtcompatible-renesas-ra-mipi-dsi"><code>renesas,ra-mipi-dsi</code></a></td>
</tr>
<tr>
<td rowspan="5">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA串行通信接口（SCI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L449">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L377">已禁用：9</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P020_renesas_ra-sci.md#std-dtcompatible-renesas-ra-sci"><code>renesas,ra-sci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA异步通用定时器（AGT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L899">已禁用：2</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P014_renesas_ra-agt.md#std-dtcompatible-renesas-ra-agt"><code>renesas,ra-agt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA超低功耗定时器（ULPT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1003">已启用：2</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P021_renesas_ra-ulpt.md#std-dtcompatible-renesas-ra-ulpt"><code>renesas,ra-ulpt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA外部中断（External Interrupt）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1340">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1232">已禁用：31</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P017_renesas_ra-external-interrupt.md#std-dtcompatible-renesas-ra-external-interrupt"><code>renesas,ra-external-interrupt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA绘图引擎（DRW）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1560">已禁用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P015_renesas_ra-drw.md#std-dtcompatible-renesas-ra-drw"><code>renesas,ra-drw</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L41">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA系列的磁阻式RAM（MRAM）存储器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L25">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P009_renesas_ra-nv-mram.md#std-dtcompatible-renesas-ra-nv-mram"><code>renesas,ra-nv-mram</code></a></td>
</tr>
<tr>
<td rowspan="1">八线串行外设接口（OCTOSPI）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA八线SPI（OSPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L100">已禁用：2</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P001_renesas_ra-ospi-b.md#std-dtcompatible-renesas-ra-ospi-b"><code>renesas,ra-ospi-b</code></a></td>
</tr>
<tr>
<td rowspan="2">物理层（PHY）</td>
<td>片上（On-Chip）</td>
<td>用于所有内置于 USB IP 的 USB 收发器（USB Transceivers）的绑定。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1644">已启用：1</a>）</td>
<td><a href="../phy_binding_reference/P008_usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv"><code>usb-nop-xceiv</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA高速USB内部物理层控制器（USBHS Internal PHY Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1649">已启用：1</a>）</td>
<td><a href="../phy_binding_reference/P003_renesas_ra-usbphyc.md#std-dtcompatible-renesas-ra-usbphyc"><code>renesas,ra-usbphyc</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L86">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P006_renesas_ra-pinctrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs"><code>renesas,ra-pinctrl-pfs</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA电池备份域（Battery Backup Domain）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L66">已禁用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P004_renesas_ra-battery-backup.md#std-dtcompatible-renesas-ra-battery-backup"><code>renesas,ra-battery-backup</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L759">已禁用：14</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P019_renesas_ra-pwm.md#std-dtcompatible-renesas-ra-pwm"><code>renesas,ra-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA RSIP-E51A真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L120">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P004_renesas_ra-rsip-e50d-trng.md#std-dtcompatible-renesas-ra-rsip-e50d-trng"><code>renesas,ra-rsip-e50d-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1552">已禁用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P006_renesas_ra-rtc.md#std-dtcompatible-renesas-ra-rtc"><code>renesas,ra-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA SD主机控制器（SDHC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1520">已禁用：2</a>）</td>
<td><a href="../sdhc_binding_reference/P017_renesas_ra-sdhc.md#std-dtcompatible-renesas-ra-sdhc"><code>renesas,ra-sdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA SCI_B UART控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L456">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L384">已禁用：9</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P008_renesas_ra8-uart-sci-b.md#std-dtcompatible-renesas-ra8-uart-sci-b"><code>renesas,ra8-uart-sci-b</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA SCI B SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L398">已禁用：10</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P015_renesas_ra-spi-sci-b.md#std-dtcompatible-renesas-ra-spi-sci-b"><code>renesas,ra-spi-sci-b</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA8 SPI_B控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L737">已禁用：2</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P018_renesas_ra8-spi-b.md#std-dtcompatible-renesas-ra8-spi-b"><code>renesas,ra8-spi-b</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L46">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA ULPT定时器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1011">已启用：2</a>）</td>
<td><a href="../renesas_timer_binding_reference/P001_renesas_ra-ulpt-timer.md#std-dtcompatible-renesas-ra-ulpt-timer"><code>renesas,ra-ulpt-timer</code></a></td>
</tr>
<tr>
<td rowspan="4">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA USB全速控制器（Full-Speed Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1194">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P018_renesas_ra-usbfs.md#std-dtcompatible-renesas-ra-usbfs"><code>renesas,ra-usbfs</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA USB设备控制器（Device Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1202">已禁用：2</a>）</td>
<td><a href="../usb_soc_binding_reference/P016_renesas_ra-udc.md#std-dtcompatible-renesas-ra-udc"><code>renesas,ra-udc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA USB主机控制器（Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1207">已禁用：2</a>）</td>
<td><a href="../usb_soc_binding_reference/P017_renesas_ra-uhc.md#std-dtcompatible-renesas-ra-uhc"><code>renesas,ra-uhc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA USB高速控制器（High-Speed Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1213">已禁用：1</a>）</td>
<td><a href="../usb_stm32_audio_binding_reference/P001_renesas_ra-usbhs.md#std-dtcompatible-renesas-ra-usbhs"><code>renesas,ra-usbhs</code></a></td>
</tr>
<tr>
<td rowspan="1">视频（Video）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA捕获引擎单元（CEU / Capture Engine Unit）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1544">已禁用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P020_renesas_ra-ceu.md#std-dtcompatible-renesas-ra-ceu"><code>renesas,ra-ceu</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA看门狗（WDT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1127">已禁用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P005_renesas_ra-wdt.md#std-dtcompatible-renesas-ra-wdt"><code>renesas,ra-wdt</code></a></td>
</tr>
</table>

<a id="ra8p1_titan_mini-ra8p1_titan_mini/r7ka8p1kflcac/cm85-hw-features-section"></a>

#### `ra8p1_titan_mini/r7ka8p1kflcac/cm85`目标（Target）

<a id="ra8p1_titan_mini-ra8p1_titan_mini/r7ka8p1kflcac/cm85-hw-features-panel"></a>

<a id="ra8p1_titan_mini-ra8p1_titan_mini/r7ka8p1kflcac/cm85-hw-features-memory"></a>

该开发板目标的片上存储容量：1 MiB RAM、768 KiB Flash。

<a id="ra8p1_titan_mini-ra8p1_titan_mini/r7ka8p1kflcac/cm85-hw-features-table"></a>

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
<td>ARM Cortex-M85处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P006_arm_cortex-m85.md#std-dtcompatible-arm-cortex-m85"><code>arm,cortex-m85</code></a></td>
</tr>
<tr>
<td rowspan="3">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA ADC_B控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L266">已禁用：1</a>）</td>
<td><a href="../hardware/P865_RenesasRAADCB控制器绑定.md#dtbinding-renesas-ra-adc-b-controller"><code>renesas,ra-adc-b-controller</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA ADC_B扫描组（Scan Group）配置节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L276">已禁用：9</a>）</td>
<td><a href="../hardware/P866_RenesasRAADCB扫描组绑定.md#dtbinding-renesas-ra-adc-b-scan-group"><code>renesas,ra-adc-b-scan-group</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA ADC_B转换器单元（Converter Unit）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L330">已禁用：2</a>）</td>
<td><a href="../hardware/P867_RenesasRAADCB实例绑定.md#dtbinding-renesas-ra-adc-b"><code>renesas,ra-adc-b</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA的Arm Ethos-U NPU前端（Frontend）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L12">已禁用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P019_renesas_ra-npu.md#std-dtcompatible-renesas-ra-npu"><code>renesas,ra-npu</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA脉冲密度调制接口（PDM-IF）的一个通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1075">已禁用：3</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P015_renesas_ra-pdm.md#std-dtcompatible-renesas-ra-pdm"><code>renesas,ra-pdm</code></a></td>
</tr>
<tr>
<td rowspan="2">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA CAN FD控制器全局节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L929">已禁用：1</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P004_renesas_ra-canfd-global.md#std-dtcompatible-renesas-ra-canfd-global"><code>renesas,ra-canfd-global</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L938">已禁用：2</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P005_renesas_ra-canfd.md#std-dtcompatible-renesas-ra-canfd"><code>renesas,ra-canfd</code></a></td>
</tr>
<tr>
<td rowspan="8">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA时钟生成电路（Clock Generation Circuit）的外部时钟配置（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P029_renesas_ra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock"><code>renesas,ra-cgc-external-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L33">已启用：4</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA子时钟（Sub-Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L51">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P004_renesas_ra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk"><code>renesas,ra-cgc-subclk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA时钟生成电路的锁相环时钟（PLL Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L57">已启用：2</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P003_renesas_ra-cgc-pll.md#std-dtcompatible-renesas-ra-cgc-pll"><code>renesas,ra-cgc-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA时钟生成电路（Clock Generation Circuit）的PLL时钟输出线（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L67">已启用：6</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P002_renesas_ra-cgc-pll-out.md#std-dtcompatible-renesas-ra-cgc-pll-out"><code>renesas,ra-cgc-pll-out</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA时钟控制节点的pclk模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L118">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P030_renesas_ra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block"><code>renesas,ra-cgc-pclk-block</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA时钟控制外设时钟（Peripheral Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L128">已启用：18</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L222">已禁用：9</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P001_renesas_ra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk"><code>renesas,ra-cgc-pclk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA外部总线时钟（External Bus Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L206">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P028_renesas_ra-cgc-busclk.md#std-dtcompatible-renesas-ra-cgc-busclk"><code>renesas,ra-cgc-busclk</code></a></td>
</tr>
<tr>
<td rowspan="3">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA高速模拟比较器（ACMPHS）全局节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1134">已禁用：1</a>）</td>
<td><a href="../hardware/P748_RenesasRA高速模拟比较器全局绑定.md#dtbinding-renesas-ra-acmphs-global"><code>renesas,ra-acmphs-global</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA高速模拟比较器（ACMPHS）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1139">已禁用：4</a>）</td>
<td><a href="../hardware/P749_RenesasRA高速模拟比较器绑定.md#dtbinding-renesas-ra-acmphs"><code>renesas,ra-acmphs</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA低电压检测（LVD）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1164">已禁用：4</a>）</td>
<td><a href="../hardware/P750_RenesasRA电压检测器绑定.md#dtbinding-renesas-ra-lvd"><code>renesas,ra-lvd</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>用作计数器的Renesas RA异步通用定时器（AGT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L908">已禁用：2</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P014_renesas_ra-agt-counter.md#std-dtcompatible-renesas-ra-agt-counter"><code>renesas,ra-agt-counter</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA超低功耗定时器（ULPT）计数器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1016">已禁用：2</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P015_renesas_ra-ulpt-counter.md#std-dtcompatible-renesas-ra-ulpt-counter"><code>renesas,ra-ulpt-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1120">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P008_renesas_ra-crc.md#std-dtcompatible-renesas-ra-crc"><code>renesas,ra-crc</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>Renesas图形LCD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L82">已禁用：1</a>）</td>
<td><a href="../display_panel_renesas_sharp_binding_reference/P011_renesas_ra-glcdc.md#std-dtcompatible-renesas-ra-glcdc"><code>renesas,ra-glcdc</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1110">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P012_renesas_ra-dma.md#std-dtcompatible-renesas-ra-dma"><code>renesas,ra-dma</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA以太网媒体访问控制器（MAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L955">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P015_renesas_ra-eswm.md#std-dtcompatible-renesas-ra-eswm"><code>renesas,ra-eswm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA以太网媒体访问控制器（MAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L975">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L968">已禁用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P016_renesas_ra-ethernet-rmac.md#std-dtcompatible-renesas-ra-ethernet-rmac"><code>renesas,ra-ethernet-rmac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA外部管理数据输入输出控制器（MDIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L982">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L992">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P005_renesas_ra-mdio-rmac.md#std-dtcompatible-renesas-ra-mdio-rmac"><code>renesas,ra-mdio-rmac</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Realtek RTL8211F以太网物理层（PHY）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ruiside/ra8p1_titan_mini/ra8p1_titan_mini_r7ka8p1kflcac_cm85.dts?plain=1#L167">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P012_realtek_rtl8211f.md#std-dtcompatible-realtek-rtl8211f"><code>realtek,rtl8211f</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA闪存／MRAM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L92">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P029_renesas_ra-mram-controller.md#std-dtcompatible-renesas-ra-mram-controller"><code>renesas,ra-mram-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA通用输入输出端口（GPIO I/O Port）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L125">已启用：12</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L216">已禁用：2</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P014_renesas_ra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport"><code>renesas,ra-gpio-ioport</code></a></td>
</tr>
<tr>
<td rowspan="2">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L361">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L353">已禁用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P014_renesas_ra-iic.md#std-dtcompatible-renesas-ra-iic"><code>renesas,ra-iic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA SCI-B I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L390">已禁用：10</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P012_renesas_ra-i2c-sci-b.md#std-dtcompatible-renesas-ra-i2c-sci-b"><code>renesas,ra-i2c-sci-b</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1052">已禁用：2</a>）</td>
<td><a href="../i2s_binding_reference/P014_renesas_ra-i2s-ssie.md#std-dtcompatible-renesas-ra-i2s-ssie"><code>renesas,ra-i2s-ssie</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1041">已禁用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P008_renesas_ra-i3c.md#std-dtcompatible-renesas-ra-i3c"><code>renesas,ra-i3c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ruiside/ra8p1_titan_mini/ra8p1_titan_mini.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P004_ARMv8_1_M_NVIC.md#std-dtcompatible-arm-v8.1m-nvic"><code>arm,v8.1m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ruiside/ra8p1_titan_mini/ra8p1_titan_mini.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">本地互连网络（LIN）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA LIN SCI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L407">已禁用：10</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P002_renesas_ra-lin-sci-b.md#std-dtcompatible-renesas-ra-lin-sci-b"><code>renesas,ra-lin-sci-b</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>Renesas核间通信邮箱（IPC MBOX）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L62">已禁用：2</a>）</td>
<td><a href="../intercore_reference/P051_RenesasRA邮箱绑定.md#dtbinding-renesas-ra-ipc-mbox"><code>renesas,ra-ipc-mbox</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA SDRAM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1102">已启用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P005_renesas_ra-sdram.md#std-dtcompatible-renesas-ra-sdram"><code>renesas,ra-sdram</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示串行接口（MIPI-DSI）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA MIPI DSI主机（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L89">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P016_renesas_ra-mipi-dsi.md#std-dtcompatible-renesas-ra-mipi-dsi"><code>renesas,ra-mipi-dsi</code></a></td>
</tr>
<tr>
<td rowspan="5">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA串行通信接口（SCI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L449">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L377">已禁用：9</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P020_renesas_ra-sci.md#std-dtcompatible-renesas-ra-sci"><code>renesas,ra-sci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA异步通用定时器（AGT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L899">已禁用：2</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P014_renesas_ra-agt.md#std-dtcompatible-renesas-ra-agt"><code>renesas,ra-agt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA超低功耗定时器（ULPT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1003">已启用：2</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P021_renesas_ra-ulpt.md#std-dtcompatible-renesas-ra-ulpt"><code>renesas,ra-ulpt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA外部中断（External Interrupt）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1268">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1232">已禁用：30</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P017_renesas_ra-external-interrupt.md#std-dtcompatible-renesas-ra-external-interrupt"><code>renesas,ra-external-interrupt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA绘图引擎（DRW）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1560">已禁用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P015_renesas_ra-drw.md#std-dtcompatible-renesas-ra-drw"><code>renesas,ra-drw</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P006_arm_armv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu"><code>arm,armv8.1m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA系列的磁阻式RAM（MRAM）存储器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L25">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P009_renesas_ra-nv-mram.md#std-dtcompatible-renesas-ra-nv-mram"><code>renesas,ra-nv-mram</code></a></td>
</tr>
<tr>
<td rowspan="1">八线串行外设接口（OCTOSPI）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA八线SPI（OSPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L100">已禁用：2</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P001_renesas_ra-ospi-b.md#std-dtcompatible-renesas-ra-ospi-b"><code>renesas,ra-ospi-b</code></a></td>
</tr>
<tr>
<td rowspan="2">物理层（PHY）</td>
<td>片上（On-Chip）</td>
<td>用于所有内置于 USB IP 的 USB 收发器（USB Transceivers）的绑定。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1644">已启用：1</a>）</td>
<td><a href="../phy_binding_reference/P008_usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv"><code>usb-nop-xceiv</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA高速USB内部物理层控制器（USBHS Internal PHY Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1649">已启用：1</a>）</td>
<td><a href="../phy_binding_reference/P003_renesas_ra-usbphyc.md#std-dtcompatible-renesas-ra-usbphyc"><code>renesas,ra-usbphyc</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L86">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P006_renesas_ra-pinctrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs"><code>renesas,ra-pinctrl-pfs</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA电池备份域（Battery Backup Domain）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L66">已禁用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P004_renesas_ra-battery-backup.md#std-dtcompatible-renesas-ra-battery-backup"><code>renesas,ra-battery-backup</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L759">已禁用：14</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P019_renesas_ra-pwm.md#std-dtcompatible-renesas-ra-pwm"><code>renesas,ra-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA RSIP-E51A真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L120">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P004_renesas_ra-rsip-e50d-trng.md#std-dtcompatible-renesas-ra-rsip-e50d-trng"><code>renesas,ra-rsip-e50d-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1552">已禁用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P006_renesas_ra-rtc.md#std-dtcompatible-renesas-ra-rtc"><code>renesas,ra-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA SD主机控制器（SDHC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1520">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1532">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P017_renesas_ra-sdhc.md#std-dtcompatible-renesas-ra-sdhc"><code>renesas,ra-sdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA SCI_B UART控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L456">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L384">已禁用：9</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P008_renesas_ra8-uart-sci-b.md#std-dtcompatible-renesas-ra8-uart-sci-b"><code>renesas,ra8-uart-sci-b</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA SCI B SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L398">已禁用：10</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P015_renesas_ra-spi-sci-b.md#std-dtcompatible-renesas-ra-spi-sci-b"><code>renesas,ra-spi-sci-b</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA8 SPI_B控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L737">已禁用：2</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P018_renesas_ra8-spi-b.md#std-dtcompatible-renesas-ra8-spi-b"><code>renesas,ra8-spi-b</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L46">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P008_ARMv8_1_M_SysTick.md#std-dtcompatible-arm-armv8.1m-systick"><code>arm,armv8.1m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA ULPT定时器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1011">已启用：2</a>）</td>
<td><a href="../renesas_timer_binding_reference/P001_renesas_ra-ulpt-timer.md#std-dtcompatible-renesas-ra-ulpt-timer"><code>renesas,ra-ulpt-timer</code></a></td>
</tr>
<tr>
<td rowspan="4">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA USB全速控制器（Full-Speed Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1194">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P018_renesas_ra-usbfs.md#std-dtcompatible-renesas-ra-usbfs"><code>renesas,ra-usbfs</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA USB设备控制器（Device Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1202">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1221">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P016_renesas_ra-udc.md#std-dtcompatible-renesas-ra-udc"><code>renesas,ra-udc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA USB主机控制器（Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1207">已禁用：2</a>）</td>
<td><a href="../usb_soc_binding_reference/P017_renesas_ra-uhc.md#std-dtcompatible-renesas-ra-uhc"><code>renesas,ra-uhc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA USB高速控制器（High-Speed Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1213">已禁用：1</a>）</td>
<td><a href="../usb_stm32_audio_binding_reference/P001_renesas_ra-usbhs.md#std-dtcompatible-renesas-ra-usbhs"><code>renesas,ra-usbhs</code></a></td>
</tr>
<tr>
<td rowspan="1">视频（Video）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA捕获引擎单元（CEU / Capture Engine Unit）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1544">已禁用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P020_renesas_ra-ceu.md#std-dtcompatible-renesas-ra-ceu"><code>renesas,ra-ceu</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA看门狗（WDT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1127">已禁用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P005_renesas_ra-wdt.md#std-dtcompatible-renesas-ra-wdt"><code>renesas,ra-wdt</code></a></td>
</tr>
</table>

<a id="dual-core-operation"></a>

## 双核运行（Dual Core Operation）

Titan Board Mini支持Cortex-M85（CPU0）及Cortex-M33（CPU1）双核运行。默认CM85为启动核，负责初始化系统并启动CM33。

<a id="memory-usage"></a>

### 内存使用（Memory Usage）

原文说明MRAM（Flash）及SRAM默认在两个核之间均分，可通过以下节点手动修改地址和容量；注意该描述与本页目标表所列容量不一致，两处均保留。


- CPU0：&code_mram_cm85及&sram0
- CPU1：&code_mram_cm33及&sram1

注意（Note）


- MRAM可用范围：0x0200_0000至0x0210_0000，1 MB
- SRAM可用范围：0x2200_0000至0x221A_0000，1664 KB

<a id="dual-core-flashing"></a>

### 双核烧录（Dual Core Flashing）

烧录或调试双核示例时，CM85镜像必须选择[CONFIG_SOC_RA_ENABLE_START_SECOND_CORE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RA_ENABLE_START_SECOND_CORE)。CM85负责在soc_late_init_hook中启动CM33。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`ra8p1_titan_mini`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-pyocd">pyocd</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

ra8p1_titan_mini板级配置的应用可按常规方式构建、烧录及调试，详情见“构建应用”及“运行应用”。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）

<a id="serial-console"></a>

### 串口控制台（Serial Console）

CM85及CM33两个目标都使用UART2提供Zephyr控制台及shell。UART2位于外部UART接口引脚，读取日志时应使用外部USB转UART适配器连接这些引脚。

以下为CM85核上的[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例。

```text
# From the root of the zephyr repository
west build -b ra8p1_titan_mini/r7ka8p1kflcac/cm85 samples/hello_world
west flash
```

打开串口终端并复位开发板，应在终端中看到以下信息：

```text
***** Booting Zephyr OS v4.2.0-xxx-xxxxxxxxxxxxx *****
Hello World! ra8p1_titan_mini/r7ka8p1kflcac/cm85
```

对于CM33核，使用--sysbuild流程构建最小的第一核启动镜像，由它启动CM33。

```text
# From the root of the zephyr repository
west build -b ra8p1_titan_mini/r7ka8p1kflcac/cm33 --sysbuild samples/hello_world
west flash
```

<a id="flashing"></a>

### 烧录（Flashing）

可通过SWD接口使用J-Link调试器向Titan Board Mini烧录程序。

向开发板烧录程序时：


1. 将J-Link调试器连接开发板SWD接口及主机。
2. 执行west命令：

  ```text
  west flash
  ```

<a id="mcuboot-bootloader"></a>

### MCUboot 引导加载程序（MCUboot Bootloader）

Sysbuild可以构建并烧录开发板启动所需的全部镜像。

使用Sysbuild构建示例应用：

```text
# From the root of the zephyr repository
west build -b ra8p1_titan_mini/r7ka8p1kflcac/cm85 --sysbuild samples/hello_world -- -DSB_CONFIG_BOOTLOADER_MCUBOOT=y
west flash
```

默认情况下，Sysbuild会创建MCUboot及用户应用镜像。

Sysbuild生成的构建目录结构与传统Zephyr构建不同，输出按域（Domain）子目录组织：

```text
build/
|-- hello_world
|   `-- zephyr
|       |-- zephyr.elf
|       |-- zephyr.hex
|       |-- zephyr.bin
|       |-- zephyr.signed.bin
|       `-- zephyr.signed.hex
|-- mcuboot
|   `-- zephyr
|       |-- zephyr.elf
|       |-- zephyr.hex
|       `-- zephyr.bin
`-- domains.yaml
```

注意（Note）

使用--sysbuild选项时，每次执行全新（Pristine）构建都会重新构建及烧录MCUboot。

在后续构建中仅烧录用户应用时，可使用：

```text
west flash --domain hello_world
```

系统构建的更多信息见“Sysbuild（System Build）”文档。（[系统构建（Sysbuild / System Build）](../sysbuild/P001_系统构建.md#sysbuild)）

终端中应出现以下消息：

```text
*** Booting MCUboot v2.2.0-171-g8513be710e5e ***
*** Using Zephyr OS build v4.2.0-6156-ged85ac9ffda9 ***
I: Starting bootloader
I: Image index: 0, Swap type: none
I: Image index: 0, Swap type: none
I: Primary image: magic=unset, swap_type=0x1, copy_done=0x3, image_ok=0x3
I: Secondary image: magic=unset, swap_type=0x1, copy_done=0x3, image_ok=0x3
I: Boot source: none
I: Image index: 0, Swap type: none
I: Image index: 0, Swap type: none
I: Image index: 0, Swap type: none
I: Image index: 0, Swap type: none
I: Bootloader chainload address offset: 0x10000
I: Image version: v0.0.0
I: Jumping to the first image slot
*** Booting Zephyr OS build v4.2.0-6156-ged85ac9ffda9 ***
Hello World! ra8p1_titan_mini/r7ka8p1kflcac/cm85
```

<a id="references"></a>

## 参考资料（References）


- <a id="id5"></a>

  [RA8P1 Titan Mini Board GitHub仓库](https://github.com/RT-Thread-Studio/sdk-bsp-ra8p1-titan-mini)[注1](#id2)
- <a id="id7"></a>

  [RA8P1 MCU系列网站](https://www.renesas.com/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ra8p1-1ghz-arm-cortex-m85-and-ethos-u55-npu-based-ai-microcontroller)[注2](#id6)

<a id="id2"></a>

〔1〕 ([1](#id3),[2](#id4),[3](#id5)) [https://github.com/RT-Thread-Studio/sdk-bsp-ra8p1-titan-mini](https://github.com/RT-Thread-Studio/sdk-bsp-ra8p1-titan-mini)

<a id="id6"></a>

〔[2](#id7)〕 [https://www.renesas.com/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ra8p1-1ghz-arm-cortex-m85-and-ethos-u55-npu-based-ai-microcontroller](https://www.renesas.com/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ra8p1-1ghz-arm-cortex-m85-and-ethos-u55-npu-based-ai-microcontroller)

<a id="id8"></a>

〔[3](#id9)〕 [https://www.renesas.com/us/en/document/mah/ra8p1-group-users-manual-hardware](https://www.renesas.com/us/en/document/mah/ra8p1-group-users-manual-hardware)

## 译注

Titan Mini的CM85与CM33均使用外部UART2，不能套用Titan的UART5／UART6接线。J-Link通过SWD烧录；原文RT-Thread SDK示例不等于Zephyr全部支持。均分内存说明与生成容量表的差异保留。

---

[上一章](P014_RA8P1_Titan.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P016_HiFive1.md)
