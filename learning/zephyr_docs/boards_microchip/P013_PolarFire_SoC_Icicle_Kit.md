---
id: learning.zephyr-docs.boards-microchip.page-13
title: PolarFire SoC Icicle Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/microchip/mpfs_icicle/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mpfs_icicle"></a>

# 第13章\_PolarFire SoC Icicle Kit

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/microchip/mpfs_icicle/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mpfs_icicle.webp](images/mpfs_icicle.webp)](images/mpfs_icicle.webp)

PolarFire SoC Icicle Kit

名称（Name）：

`mpfs_icicle`

厂商（Vendor）：

[微芯科技（Microchip Technology Inc.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=microchip)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[polarfire](https://docs.zephyrproject.org/latest/boards/index.html#soc=polarfire)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/mpfs_icicle/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Microchip PolarFire SoC Icicle Kit是基于PolarFire SoC FPGA的开发板，搭载Microchip MPFS250T FPGA。E51 RISC-V CPU可部署于mpfs_icicle开发板。更多信息见[Microchip网站](https://www.microchip.com/en-us/product/MPFS250T)。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`mpfs_icicle`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mpfs_icicle-hw-features"></a>

<a id="mpfs_icicle-mpfs_icicle/polarfire/e51-hw-features-section"></a>

#### `mpfs_icicle/polarfire/e51`目标（Target）

<a id="mpfs_icicle-mpfs_icicle/polarfire/e51-hw-features-panel"></a>

<a id="mpfs_icicle-mpfs_icicle/polarfire/e51-hw-features-memory"></a>

该开发板目标的片上存储容量：8 MiB RAM、N/A Flash。

<a id="mpfs_icicle-mpfs_icicle/polarfire/e51-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="2">中央处理器（CPU）</td>
<td>片上（On-Chip）</td>
<td>SiFive E51标准内核处理器（Standard Core CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P039_sifive_e51.md#std-dtcompatible-sifive-e51"><code>sifive,e51</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive U54标准内核处理器（Standard Core CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L38">已禁用：4</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P041_sifive_u54.md#std-dtcompatible-sifive-u54"><code>sifive,u54</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Microchip PolarFire SoC通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L293">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L271">已禁用：2</a>）</td>
<td><a href="../gpio_infineon_intel_ite_microchip_binding_reference/P030_microchip_mpfs-gpio.md#std-dtcompatible-microchip-mpfs-gpio"><code>microchip,mpfs-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Microchip MPFS I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L304">已启用：2</a>）</td>
<td><a href="../i2c_infineon_ite_nordic_binding_reference/P011_microchip_mpfs-i2c.md#std-dtcompatible-microchip-mpfs-i2c"><code>microchip,mpfs-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/mpfs_icicle/mpfs_icicle_common.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>RISC-V CPU中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L30">已启用：5</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P006_riscv_cpu-intc.md#std-dtcompatible-riscv-cpu-intc"><code>riscv,cpu-intc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive RISC-V内核本地中断器（Core-Local Interruptor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L123">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P010_sifive_clint0.md#std-dtcompatible-sifive-clint0"><code>sifive,clint0</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive RISCV-V平台级中断控制器（PLIC / Platform-Local Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L147">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P009_sifive_plic-1.0.0.md#std-dtcompatible-sifive-plic-1.0.0"><code>sifive,plic-1.0.0</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/mpfs_icicle/mpfs_icicle_common.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>这些属性用于支持Zephyr的<code>spi-nor</code>闪存驱动通过Zephyr SPI API，使用基于M25P80的标准命令集控制串行闪存（Serial Flash Memory）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/mpfs_icicle/mpfs_icicle_common.dtsi?plain=1#L52">已启用：2</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor"><code>jedec,spi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip MPFS复位控制器，<code>SOFT_RESET_CR</code>及<code>SUBBLK_CLOCK_CR</code>（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L176">已禁用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P005_microchip_mpfs-reset.md#std-dtcompatible-microchip-mpfs-reset"><code>microchip,mpfs-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Microchip微控制器子系统（MSS）实时时钟驱动（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L326">已启用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P001_microchip_rtc-mss.md#std-dtcompatible-microchip-rtc-mss"><code>microchip,rtc-mss</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L183">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L194">已禁用：4</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Microchip PolarFire SoC QSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L238">已启用：2</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P007_microchip_mpfs-qspi.md#std-dtcompatible-microchip-mpfs-qspi"><code>microchip,mpfs-qspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip PolarFire SoC SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L249">已启用：1</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P008_microchip_mpfs-spi.md#std-dtcompatible-microchip-mpfs-spi"><code>microchip,mpfs-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L113">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>系统控制器寄存器读写（System Controller Registers R/W）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L172">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P008_syscon.md#std-dtcompatible-syscon"><code>syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>RISC-V机器模式定时器（Machine Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L136">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer"><code>riscv,machine-timer</code></a></td>
</tr>
</table>

<a id="mpfs_icicle-mpfs_icicle/polarfire/u54-hw-features-section"></a>

#### `mpfs_icicle/polarfire/u54`目标（Target）

<a id="mpfs_icicle-mpfs_icicle/polarfire/u54-hw-features-panel"></a>

<a id="mpfs_icicle-mpfs_icicle/polarfire/u54-hw-features-memory"></a>

该开发板目标的片上存储容量：8 MiB RAM、N/A Flash。

<a id="mpfs_icicle-mpfs_icicle/polarfire/u54-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="2">中央处理器（CPU）</td>
<td>片上（On-Chip）</td>
<td>SiFive E51标准内核处理器（Standard Core CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L22">已禁用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P039_sifive_e51.md#std-dtcompatible-sifive-e51"><code>sifive,e51</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive U54标准内核处理器（Standard Core CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L38">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L55">已禁用：3</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P041_sifive_u54.md#std-dtcompatible-sifive-u54"><code>sifive,u54</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Microchip PolarFire SoC通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L293">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L271">已禁用：2</a>）</td>
<td><a href="../gpio_infineon_intel_ite_microchip_binding_reference/P030_microchip_mpfs-gpio.md#std-dtcompatible-microchip-mpfs-gpio"><code>microchip,mpfs-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Microchip MPFS I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L304">已启用：2</a>）</td>
<td><a href="../i2c_infineon_ite_nordic_binding_reference/P011_microchip_mpfs-i2c.md#std-dtcompatible-microchip-mpfs-i2c"><code>microchip,mpfs-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/mpfs_icicle/mpfs_icicle_common.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>RISC-V CPU中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L30">已启用：5</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P006_riscv_cpu-intc.md#std-dtcompatible-riscv-cpu-intc"><code>riscv,cpu-intc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive RISC-V内核本地中断器（Core-Local Interruptor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L123">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P010_sifive_clint0.md#std-dtcompatible-sifive-clint0"><code>sifive,clint0</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive RISCV-V平台级中断控制器（PLIC / Platform-Local Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L147">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P009_sifive_plic-1.0.0.md#std-dtcompatible-sifive-plic-1.0.0"><code>sifive,plic-1.0.0</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/mpfs_icicle/mpfs_icicle_common.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>这些属性用于支持Zephyr的<code>spi-nor</code>闪存驱动通过Zephyr SPI API，使用基于M25P80的标准命令集控制串行闪存（Serial Flash Memory）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/mpfs_icicle/mpfs_icicle_common.dtsi?plain=1#L52">已启用：2</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor"><code>jedec,spi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip MPFS复位控制器，<code>SOFT_RESET_CR</code>及<code>SUBBLK_CLOCK_CR</code>（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L176">已禁用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P005_microchip_mpfs-reset.md#std-dtcompatible-microchip-mpfs-reset"><code>microchip,mpfs-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Microchip微控制器子系统（MSS）实时时钟驱动（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L326">已启用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P001_microchip_rtc-mss.md#std-dtcompatible-microchip-rtc-mss"><code>microchip,rtc-mss</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L183">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L205">已禁用：3</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Microchip PolarFire SoC QSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L238">已启用：2</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P007_microchip_mpfs-qspi.md#std-dtcompatible-microchip-mpfs-qspi"><code>microchip,mpfs-qspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip PolarFire SoC SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L249">已启用：1</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P008_microchip_mpfs-spi.md#std-dtcompatible-microchip-mpfs-spi"><code>microchip,mpfs-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L113">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>系统控制器寄存器读写（System Controller Registers R/W）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L172">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P008_syscon.md#std-dtcompatible-syscon"><code>syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>RISC-V机器模式定时器（Machine Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L136">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer"><code>riscv,machine-timer</code></a></td>
</tr>
</table>

<a id="mpfs_icicle-mpfs_icicle/polarfire/u54/smp-hw-features-section"></a>

#### `mpfs_icicle/polarfire/u54/smp`目标（Target）

<a id="mpfs_icicle-mpfs_icicle/polarfire/u54/smp-hw-features-panel"></a>

<a id="mpfs_icicle-mpfs_icicle/polarfire/u54/smp-hw-features-memory"></a>

该开发板目标的片上存储容量：8 MiB RAM、N/A Flash。

<a id="mpfs_icicle-mpfs_icicle/polarfire/u54/smp-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="2">中央处理器（CPU）</td>
<td>片上（On-Chip）</td>
<td>SiFive E51标准内核处理器（Standard Core CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L22">已禁用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P039_sifive_e51.md#std-dtcompatible-sifive-e51"><code>sifive,e51</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive U54标准内核处理器（Standard Core CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L38">已启用：4</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P041_sifive_u54.md#std-dtcompatible-sifive-u54"><code>sifive,u54</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Microchip PolarFire SoC通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L293">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L271">已禁用：2</a>）</td>
<td><a href="../gpio_infineon_intel_ite_microchip_binding_reference/P030_microchip_mpfs-gpio.md#std-dtcompatible-microchip-mpfs-gpio"><code>microchip,mpfs-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Microchip MPFS I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L304">已启用：2</a>）</td>
<td><a href="../i2c_infineon_ite_nordic_binding_reference/P011_microchip_mpfs-i2c.md#std-dtcompatible-microchip-mpfs-i2c"><code>microchip,mpfs-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/mpfs_icicle/mpfs_icicle_common.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>RISC-V CPU中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L30">已启用：5</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P006_riscv_cpu-intc.md#std-dtcompatible-riscv-cpu-intc"><code>riscv,cpu-intc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive RISC-V内核本地中断器（Core-Local Interruptor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L123">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P010_sifive_clint0.md#std-dtcompatible-sifive-clint0"><code>sifive,clint0</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive RISCV-V平台级中断控制器（PLIC / Platform-Local Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L147">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P009_sifive_plic-1.0.0.md#std-dtcompatible-sifive-plic-1.0.0"><code>sifive,plic-1.0.0</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/mpfs_icicle/mpfs_icicle_common.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>这些属性用于支持Zephyr的<code>spi-nor</code>闪存驱动通过Zephyr SPI API，使用基于M25P80的标准命令集控制串行闪存（Serial Flash Memory）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/mpfs_icicle/mpfs_icicle_common.dtsi?plain=1#L52">已启用：2</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor"><code>jedec,spi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip MPFS复位控制器，<code>SOFT_RESET_CR</code>及<code>SUBBLK_CLOCK_CR</code>（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L176">已禁用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P005_microchip_mpfs-reset.md#std-dtcompatible-microchip-mpfs-reset"><code>microchip,mpfs-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Microchip微控制器子系统（MSS）实时时钟驱动（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L326">已启用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P001_microchip_rtc-mss.md#std-dtcompatible-microchip-rtc-mss"><code>microchip,rtc-mss</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L183">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L205">已禁用：3</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Microchip PolarFire SoC QSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L238">已启用：2</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P007_microchip_mpfs-qspi.md#std-dtcompatible-microchip-mpfs-qspi"><code>microchip,mpfs-qspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip PolarFire SoC SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L249">已启用：1</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P008_microchip_mpfs-spi.md#std-dtcompatible-microchip-mpfs-spi"><code>microchip,mpfs-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L113">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>系统控制器寄存器读写（System Controller Registers R/W）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L172">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P008_syscon.md#std-dtcompatible-syscon"><code>syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>RISC-V机器模式定时器（Machine Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/microchip/mpfs.dtsi?plain=1#L136">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer"><code>riscv,machine-timer</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 编程与调试（Programming and Debugging）

<a id="building"></a>

### 构建（Building）

mpfs_icicle开发板配置可按通常方式构建应用，参见[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)：

```text
west build -b mpfs_icicle
```

构建默认支持对称多处理（SMP）的变体：

```text
west build -b mpfs_icicle/polarfire/smp
```

<a id="flashing"></a>

### 烧录（Flashing）

向设备上传应用需要支持RISC-V的OpenOCD和GDB，可从SoftConsole SDK获取，下载及安装说明见[Microchip SoftConsole网站](https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/programming-and-debug/softconsole)。

安装所需工具后，可通过OpenOCD连接开发板，执行以下命令建立连接：

```text
sudo LD_LIBRARY_PATH=<softconsole_path>/openocd/bin \
<softconsole_path>/openocd/bin/openocd --command "set DEVICE MPFS" --file \
<softconsole_path>/openocd/share/openocd/scripts/board/microsemi-riscv.cfg
```

保持OpenOCD运行，在另一个终端中通过GDB将二进制文件上传到开发板。可使用SoftConsole SDK工具链提供的RISC-V GDB。

在GDB终端中使用以下命令连接设备并加载二进制文件：

```text
<softconsole_path>/riscv-unknown-elf-gcc/bin/riscv64-unknown-elf-gdb \
-ex "target extended-remote localhost:3333" \
-ex "set mem inaccessible-by-default off" \
-ex "set arch riscv:rv64" \
-ex "set riscv use_compressed_breakpoints no" \
-ex "load" <path_to_executable>
```

<a id="debugging"></a>

### 调试（Debugging）

详细说明见[应用调试（Application Debugging）](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)概述。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [MPFS250T](https://www.microchip.com/en-us/product/MPFS250T)：HTTP Error 403: Forbidden。
- [softconsole](https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/programming-and-debug/softconsole)：HTTP Error 403: Forbidden。

---

[上一章](P012_MEC17xxEVB_ASSY6941.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_PIC32CK_GC01_Curiosity_Ultra.md)
