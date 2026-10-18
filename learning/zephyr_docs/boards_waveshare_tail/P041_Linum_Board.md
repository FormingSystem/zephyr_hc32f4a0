---
id: learning.zephyr-docs.boards-waveshare-tail.page-41
title: Linum Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/witte/linum/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="linum"></a>

# 第41章\_Linum开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/witte/linum/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/linum-stm32h753bi-top.jpg](images/linum-stm32h753bi-top.jpg)](images/linum-stm32h753bi-top.jpg)

Linum开发板

名称（Name）：

`linum`

厂商（Vendor）：

[Witte Technology](https://docs.zephyrproject.org/latest/boards/index.html#vendor=witte)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[stm32h753xx](https://docs.zephyrproject.org/latest/boards/index.html#soc=stm32h753xx)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/witte/linum/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Linum是Witte Technology于2023年发布、基于STM32H753BI的开发板。两个扩展连接器分别用于带触摸的LCD及其他MCU外设，另有支持RS-232／RS-485的UART、CAN-FD总线及以太网。原文厂商拼作Witte Tenology。

<a id="hardware"></a>

## 硬件（Hardware）

开发板具有以下特性：


- 8—52 V供电
- SWD排针，供ST-Link使用；另有TC2030-IDC 6针Tag-Connect Plug-of-Nails连接器
- 25 MHz高速晶体
- 32.768 kHz RTC晶体
- 1路调试UART
- 1个RGB LED
- 1个无内部振荡器的蜂鸣器
- 1路单声道音频，最高3 W
- 1路10／100 Mbit/s以太网
- 1个MicroSD连接器，支持1位或4位总线
- 1路USB 2.0主机／设备
- 1颗512 Kbit EEPROM
- 1颗8 MB外部SRAM；原文此处称SRAM，后文称SDRAM
- 1颗16 MB NOR存储器
- 2个板载RS-232收发器，带RTS／CTS
- 2个板载RS-485收发器
- 2个板载CAN-FD收发器

扩展连接器1提供：


- 1路RBG 888显示接口；原文拼作RBG
- 1个电容触摸屏传感器

扩展连接器2提供：


- 1路SPI
- 1路I2C
- 1路单总线（One Wire）
- 2路数模转换器（DAC）
- 6路PWM
- 10路ADC

更多信息见[Witte Linum网站](https://wittetech.com/)。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`linum`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="linum-hw-features"></a>

<a id="linum-linum/stm32h753xx-hw-features-section"></a>

#### `linum/stm32h753xx`目标（Target）

<a id="linum-linum/stm32h753xx-hw-features-panel"></a>

<a id="linum-linum/stm32h753xx-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、2 MiB Flash。

<a id="linum-linum/stm32h753xx-hw-features-table"></a>

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
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L38">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>STM32模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1046">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1080">已禁用：1</a>）</td>
<td><a href="../hardware/P839_STM32模数转换器绑定.md#dtbinding-st-stm32-adc"><code>st,stm32-adc</code></a></td>
</tr>
<tr>
<td rowspan="2">音频（Audio）</td>
<td>片上（On-Chip）</td>
<td>意法半导体（STMicroelectronics）Σ-Δ调制器数字滤波器模块（DFSDM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L994">已禁用：1</a>）</td>
<td><a href="../audio_stm32_ti_wolfson_binding_reference/P002_st_stm32-dfsdm.md#std-dtcompatible-st-stm32-dfsdm"><code>st,stm32-dfsdm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>意法半导体（STMicroelectronics）DFSDM数字麦克风（DMIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1005">已禁用：4</a>）</td>
<td><a href="../audio_stm32_ti_wolfson_binding_reference/P001_st_stm32-dfsdm-dmic.md#std-dtcompatible-st-stm32-dfsdm-dmic"><code>st,stm32-dfsdm-dmic</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>STM32H7系列及兼容器件的FDCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L614">已启用：2</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P013_st_stm32h7-fdcan.md#std-dtcompatible-st-stm32h7-fdcan"><code>st,stm32h7-fdcan</code></a></td>
</tr>
<tr>
<td rowspan="8">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>STM32H7复位与时钟控制器（RCC / Reset and Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L205">已启用：1</a>）</td>
<td><a href="../timer_reference/P168_STM32H7复位与时钟控制绑定.md#dtbinding-st-stm32h7-rcc"><code>st,stm32h7-rcc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 外部高速时钟（HSE Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../timer_reference/P129_STM32高速外部时钟绑定.md#dtbinding-st-stm32-hse-clock"><code>st,stm32-hse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32高速内部时钟（HSI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L82">已禁用：1</a>）</td>
<td><a href="../timer_reference/P146_STM32H7内部高速时钟绑定.md#dtbinding-st-stm32h7-hsi-clock"><code>st,stm32h7-hsi-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L90">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L97">已禁用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低速外部时钟（LSE Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L104">已禁用：1</a>）</td>
<td><a href="../timer_reference/P130_STM32低速外部时钟绑定.md#dtbinding-st-stm32-lse-clock"><code>st,stm32-lse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32H7主锁相环（Main PLL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L119">已启用：3</a>）</td>
<td><a href="../timer_reference/P154_STM32H7锁相环时钟绑定.md#dtbinding-st-stm32h7-pll-clock"><code>st,stm32h7-pll-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 时钟多路复用器（Clock Multiplexer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L140">已禁用：1</a>）</td>
<td><a href="../timer_reference/P133_STM32时钟多路复用绑定.md#dtbinding-st-stm32-clock-mux"><code>st,stm32-clock-mux</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 微控制器时钟输出（Microcontroller Clock Output，MCO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L148">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L154">已禁用：1</a>）</td>
<td><a href="../timer_reference/P134_STM32时钟输出绑定.md#dtbinding-st-stm32-clock-mco"><code>st,stm32-clock-mco</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>STM32H7系列比较器（Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1314">已禁用：2</a>）</td>
<td><a href="../hardware/P741_STM32H7比较器绑定.md#dtbinding-st-stm32h7-comp"><code>st,stm32h7-comp</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>STM32 计数器（Counters）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L653">已禁用：14</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P007_st_stm32-counter.md#std-dtcompatible-st-stm32-counter"><code>st,stm32-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>STM32 CRC 计算单元（Calculation Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1332">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P011_st_stm32-crc.md#std-dtcompatible-st-stm32-crc"><code>st,stm32-crc</code></a></td>
</tr>
<tr>
<td rowspan="2">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>STM32密码加速器（Cryptographic Accelerator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h750.dtsi?plain=1#L14">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P016_st_stm32-cryp.md#std-dtcompatible-st-stm32-cryp"><code>st,stm32-cryp</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32哈希处理器（HASH Processor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h750.dtsi?plain=1#L23">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P017_st_stm32-hash.md#std-dtcompatible-st-stm32-hash"><code>st,stm32-hash</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>STM32 系列数模转换器（DAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1107">已禁用：1</a>）</td>
<td><a href="../hardware/P760_STM32数模转换器绑定.md#dtbinding-st-stm32-dac"><code>st,stm32-dac</code></a></td>
</tr>
<tr>
<td rowspan="2">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>STM32 Chrom-ART 图形加速器（Accelerator，DMA2D）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1349">已禁用：1</a>）</td>
<td><a href="../display_st_ultrachip_zephyr_binding_reference/P003_st_stm32-dma2d.md#std-dtcompatible-st-stm32-dma2d"><code>st,stm32-dma2d</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 LCD-TFT 显示控制器（Display Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h742.dtsi?plain=1#L52">已启用：1</a>）</td>
<td><a href="../display_st_ultrachip_zephyr_binding_reference/P004_st_stm32-ltdc.md#std-dtcompatible-st-stm32-ltdc"><code>st,stm32-ltdc</code></a></td>
</tr>
<tr>
<td rowspan="3">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>STM32 DMA 控制器（Controller，V1）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1115">已禁用：2</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P007_st_stm32-dma-v1.md#std-dtcompatible-st-stm32-dma-v1"><code>st,stm32-dma-v1</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32基本DMA控制器（BDMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1141">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P006_st_stm32-bdma.md#std-dtcompatible-st-stm32-bdma"><code>st,stm32-bdma</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 DMA 多路复用控制器（DMAMUX Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1154">已禁用：2</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P011_st_stm32-dmamux.md#std-dtcompatible-st-stm32-dmamux"><code>st,stm32-dmamux</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>ST STM32 以太网媒体访问控制器（Ethernet MAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1215">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P011_st_stm32h7-ethernet.md#std-dtcompatible-st-stm32h7-ethernet"><code>st,stm32h7-ethernet</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 的管理数据输入输出控制器（MDIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1229">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P010_snps_dwmac-mdio.md#std-dtcompatible-snps-dwmac-mdio"><code>snps,dwmac-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Microchip KSZ8081以太网PHY设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/witte/linum/linum.dts?plain=1#L285">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P001_microchip_ksz8081.md#std-dtcompatible-microchip-ksz8081"><code>microchip,ksz8081</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 精确时间协议时钟（Precision Time Protocol，PTP Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1236">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P006_snps_dwmac-ptp-clock.md#std-dtcompatible-snps-dwmac-ptp-clock"><code>snps,dwmac-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 系列闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L162">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P011_st_stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller"><code>st,stm32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用输入输出控制器（GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L248">已启用：11</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P029_st_stm32-gpio.md#std-dtcompatible-st-stm32-gpio"><code>st,stm32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>STM32 I2C V2 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L467">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L443">已禁用：3</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P008_st_stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2"><code>st,stm32-i2c-v2</code></a></td>
</tr>
<tr>
<td rowspan="2">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>STM32H7 I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L572">已禁用：3</a>）</td>
<td><a href="../i2s_binding_reference/P018_st_stm32h7-i2s.md#std-dtcompatible-st-stm32h7-i2s"><code>st,stm32h7-i2s</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 串行音频接口块控制器（SAI Block Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1286">已禁用：2</a>）</td>
<td><a href="../i2s_binding_reference/P017_st_stm32-sai.md#std-dtcompatible-st-stm32-sai"><code>st,stm32-sai</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>FT3267/FT5XX6/FT6XX6电容式触摸面板（Capacitive Touch Panels）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/witte/linum/linum.dts?plain=1#L217">已启用：1</a>）</td>
<td><a href="../input_adc_touch_matrix_binding_reference/P014_focaltech_ft5336.md#std-dtcompatible-focaltech-ft5336"><code>focaltech,ft5336</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L225">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P001_st_stm32-exti.md#std-dtcompatible-st-stm32-exti"><code>st,stm32-exti</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/witte/linum/linum.dts?plain=1#L37">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="3">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 电池备份 RAM（Battery-Backed RAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h742.dtsi?plain=1#L63">已禁用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P010_st_stm32-bbram.md#std-dtcompatible-st-stm32-bbram"><code>st,stm32-bbram</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32H7灵活存储器控制器（FMC / Flexible Memory Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1241">已启用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P016_st_stm32h7-fmc.md#std-dtcompatible-st-stm32h7-fmc"><code>st,stm32h7-fmc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 灵活存储器控制器中的 SDRAM 控制器（SDRAM Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1247">已启用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P012_st_stm32-fmc-sdram.md#std-dtcompatible-st-stm32-fmc-sdram"><code>st,stm32-fmc-sdram</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L45">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>STM32闪存（Flash Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h742.dtsi?plain=1#L15">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P016_st_stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash"><code>st,stm32-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">非易失存储器（NVMEM）</td>
<td>片上（On-Chip）</td>
<td>非易失存储器固定布局（Fixed Layout for Non-Volatile Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L179">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P009_fixed-layout.md#std-dtcompatible-fixed-layout"><code>fixed-layout</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>STM32 嵌入式非易失一次性可编程存储器（NVM OTP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L175">已启用：1</a>）</td>
<td><a href="../otp_binding_reference/P010_st_stm32-nvm-otp.md#std-dtcompatible-st-stm32-nvm-otp"><code>st,stm32-nvm-otp</code></a></td>
</tr>
<tr>
<td rowspan="1">物理层（PHY）</td>
<td>片上（On-Chip）</td>
<td>用于所有内置于 USB IP 的 USB 收发器（USB Transceivers）的绑定。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h742.dtsi?plain=1#L137">已启用：1</a>）</td>
<td><a href="../phy_binding_reference/P008_usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv"><code>usb-nop-xceiv</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>STM32 引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L241">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P004_st_stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl"><code>st,stm32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>STM32H7电源控制器（Power Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L216">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P014_st_stm32h7-pwr.md#std-dtcompatible-st-stm32h7-pwr"><code>st,stm32h7-pwr</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>STM32 脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L855">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L647">已禁用：11</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P011_st_stm32-pwm.md#std-dtcompatible-st-stm32-pwm"><code>st,stm32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">四线串行外设接口（QSPI）</td>
<td>片上（On-Chip）</td>
<td>STM32 四线串行外设接口控制器（QSPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1263">已禁用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P011_st_stm32-qspi.md#std-dtcompatible-st-stm32-qspi"><code>st,stm32-qspi</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>STM32参考电压缓冲器稳压器（VREFBUF Regulator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1340">已禁用：1</a>）</td>
<td><a href="../hardware/P638_STM32参考电压缓冲器绑定.md#dtbinding-st-stm32-vrefbuf"><code>st,stm32-vrefbuf</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 复位与时钟控制器（Reset and Clock Control，RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L210">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P017_st_stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl"><code>st,stm32-rcc-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>STM32 随机数生成器（Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1186">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P016_st_stm32-rng.md#std-dtcompatible-st-stm32-rng"><code>st,stm32-rng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>STM32 实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L432">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P014_st_stm32-rtc.md#std-dtcompatible-st-stm32-rtc"><code>st,stm32-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>STM32 SDMMC 主机控制器（Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1194">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1205">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P019_st_stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc"><code>st,stm32-sdmmc</code></a></td>
</tr>
<tr>
<td rowspan="4">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>STM32 正交解码器（Quadrature Decoder）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L658">已禁用：6</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P028_st_stm32-qdec.md#std-dtcompatible-st-stm32-qdec"><code>st,stm32-qdec</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系列温度节点（TEMP），用于以两个温度点完成生产校准的传感器。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1357">已禁用：1</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P029_st_stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal"><code>st,stm32-temp-cal</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 电池电压（VBAT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1369">已禁用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P001_st_stm32-vbat.md#std-dtcompatible-st-stm32-vbat"><code>st,stm32-vbat</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 参考电压（VREF+）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1375">已禁用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P003_st_stm32-vref.md#std-dtcompatible-st-stm32-vref"><code>st,stm32-vref</code></a></td>
</tr>
<tr>
<td rowspan="3">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L351">已启用：4</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P016_st_stm32-usart.md#std-dtcompatible-st-stm32-usart"><code>st,stm32-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L378">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L387">已禁用：3</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P015_st_stm32-uart.md#std-dtcompatible-st-stm32-uart"><code>st,stm32-uart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低功耗通用异步收发器（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L423">已禁用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P014_st_stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart"><code>st,stm32-lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">系统管理总线（SMbus）</td>
<td>片上（On-Chip）</td>
<td>STM32 系统管理总线控制器（SMBus Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1383">已禁用：4</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P013_st_stm32-smbus.md#std-dtcompatible-st-stm32-smbus"><code>st,stm32-smbus</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>STM32H7 串行外设接口控制器（SPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L491">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L505">已禁用：5</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P013_st_stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi"><code>st,stm32h7-spi</code></a></td>
</tr>
<tr>
<td rowspan="3">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 定时器（Timers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L844">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L636">已禁用：13</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P008_st_stm32-timers.md#std-dtcompatible-st-stm32-timers"><code>st,stm32-timers</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低功耗定时器（LPTIM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L982">已禁用：1</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P007_st_stm32-lptim.md#std-dtcompatible-st-stm32-lptim"><code>st,stm32-lptim</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>STM32 全速 USB OTG 控制器（OTGFS Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h742.dtsi?plain=1#L38">已启用：1</a>）</td>
<td><a href="../usb_stm32_audio_binding_reference/P004_st_stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs"><code>st,stm32-otgfs</code></a></td>
</tr>
<tr>
<td rowspan="2">视频（Video）</td>
<td>片上（On-Chip）</td>
<td>STM32数字摄像头接口（DCMI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1273">已禁用：1</a>）</td>
<td><a href="../video_st_sony_emulation_binding_reference/P004_st_stm32-dcmi.md#std-dtcompatible-st-stm32-dcmi"><code>st,stm32-dcmi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 JPEG硬件编解码器（HW Codec）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h742.dtsi?plain=1#L70">已禁用：1</a>）</td>
<td><a href="../video_st_sony_emulation_binding_reference/P006_st_stm32-jpeg.md#std-dtcompatible-st-stm32-jpeg"><code>st,stm32-jpeg</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>STM32 看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L337">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P001_st_stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog"><code>st,stm32-watchdog</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系统窗口看门狗（System Window Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L343">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P002_st_stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog"><code>st,stm32-window-watchdog</code></a></td>
</tr>
</table>

<a id="default-zephyr-peripheral-mapping"></a>

#### Zephyr 默认外设映射（Peripheral Mapping）：

<a id="board-leds"></a>

#### 板载LED（Board LEDs）

LINUM-STM32H753BI具有3个软件可控LED。

> <table>
> <tr>
> <th>RGB LED</th>
> <th>引脚（Pins）</th>
> </tr>
> <tr>
> <td>LED_R</td>
> <td>PG2</td>
> </tr>
> <tr>
> <td>LED_G</td>
> <td>PG3</td>
> </tr>
> <tr>
> <td>LED_B</td>
> <td>PB2</td>
> </tr>
> </table>

<a id="uart-usart"></a>

#### UART/USART

LINUM-STM32H753BI使用USART1作为串口控制台。

<a id="usart1"></a>

#### USART1

> <table>
> <tr>
> <th>USART1</th>
> <th>引脚（Pins）</th>
> </tr>
> <tr>
> <td>发送（TX）</td>
> <td>PB14</td>
> </tr>
> <tr>
> <td>接收（RX）</td>
> <td>PB15</td>
> </tr>
> </table>

两个板载RS-232收发器分别连接USART2及USART3。

> <table>
> <tr>
> <th>USART2</th>
> <th>引脚（Pins）</th>
> </tr>
> <tr>
> <td>发送数据（TXD）</td>
> <td>PD5</td>
> </tr>
> <tr>
> <td>接收数据（RXD）</td>
> <td>PD6</td>
> </tr>
> <tr>
> <td>允许发送（CTS）</td>
> <td>PD3</td>
> </tr>
> <tr>
> <td>请求发送（RTS）</td>
> <td>PD4</td>
> </tr>
> </table>
>
> <table>
> <tr>
> <th>USART3</th>
> <th>引脚（Pins）</th>
> </tr>
> <tr>
> <td>发送数据（TXD）</td>
> <td>PB10</td>
> </tr>
> <tr>
> <td>接收数据（RXD）</td>
> <td>PB11</td>
> </tr>
> <tr>
> <td>允许发送（CTS）</td>
> <td>PD11</td>
> </tr>
> <tr>
> <td>请求发送（RTS）</td>
> <td>PD12</td>
> </tr>
> </table>

两个板载RS-485收发器分别连接USART4及USART6；名称按原文保留。

> <table>
> <tr>
> <th>UART4</th>
> <th>引脚（Pins）</th>
> </tr>
> <tr>
> <td>发送数据（TXD）</td>
> <td>PB9</td>
> </tr>
> <tr>
> <td>接收数据（RXD）</td>
> <td>PB8</td>
> </tr>
> <tr>
> <td>DE</td>
> <td>PA15</td>
> </tr>
> </table>
>
> <table>
> <tr>
> <th>USART6</th>
> <th>引脚（Pins）</th>
> </tr>
> <tr>
> <td>发送数据（TXD）</td>
> <td>PC6</td>
> </tr>
> <tr>
> <td>接收数据（RXD）</td>
> <td>PC7</td>
> </tr>
> <tr>
> <td>DE</td>
> <td>PG12</td>
> </tr>
> </table>

<a id="sdmmc"></a>

#### SDMMC

LINUM-STM32H753BI的SD卡槽连接如下：

> <table>
> <tr>
> <th>SDMMC1</th>
> <th>引脚（Pins）</th>
> </tr>
> <tr>
> <td>SDMMC_D0</td>
> <td>PC8</td>
> </tr>
> <tr>
> <td>SDMMC_D1</td>
> <td>PC9</td>
> </tr>
> <tr>
> <td>SDMMC_D2</td>
> <td>PC10</td>
> </tr>
> <tr>
> <td>SDMMC_D3</td>
> <td>PC11</td>
> </tr>
> <tr>
> <td>SDMMC_DK</td>
> <td>PC12</td>
> </tr>
> </table>
>
> <table>
> <tr>
> <th>通用输入输出（GPIO）</th>
> <th>引脚（Pins）</th>
> </tr>
> <tr>
> <td>SDCARD_DETECTED</td>
> <td>PG7</td>
> </tr>
> <tr>
> <td>SDCARD_PWR_EN</td>
> <td>PD7</td>
> </tr>
> </table>

<a id="ethernet"></a>

#### 以太网（Ethernet）

以太网连接使用KSZ8081RNACA收发器。

> <table>
> <tr>
> <th>以太网（ETH）</th>
> <th>引脚（Pins）</th>
> </tr>
> <tr>
> <td>ETH_REF_CLK</td>
> <td>PA1</td>
> </tr>
> <tr>
> <td>ETH_MDIO</td>
> <td>PA2</td>
> </tr>
> <tr>
> <td>ETH_CRS_DV</td>
> <td>PA7</td>
> </tr>
> <tr>
> <td>ETH_MDC</td>
> <td>PC1</td>
> </tr>
> <tr>
> <td>ETH_RXD0</td>
> <td>PC4</td>
> </tr>
> <tr>
> <td>ETH_RXD1</td>
> <td>PC5</td>
> </tr>
> <tr>
> <td>ETH_TX_EN</td>
> <td>PG11</td>
> </tr>
> <tr>
> <td>ETH_TXD0</td>
> <td>PG13</td>
> </tr>
> <tr>
> <td>ETH_TXD1</td>
> <td>PG14</td>
> </tr>
> <tr>
> <td>ETH_CLK</td>
> <td>PA8</td>
> </tr>
> <tr>
> <td>ETH_RESET</td>
> <td>PI4</td>
> </tr>
> </table>

<a id="can-fd"></a>

#### CAN-FD

两个板载CAN-FD收发器分别连接FDCAN1及FDCAN2。

> <table>
> <tr>
> <th>FDCAN1</th>
> <th>引脚（Pins）</th>
> </tr>
> <tr>
> <td>发送数据（TXD）</td>
> <td>PH13</td>
> </tr>
> <tr>
> <td>接收数据（RXD）</td>
> <td>PH14</td>
> </tr>
> <tr>
> <td>STD</td>
> <td>PI2</td>
> </tr>
> </table>
>
> <table>
> <tr>
> <th>FDCAN2</th>
> <th>引脚（Pins）</th>
> </tr>
> <tr>
> <td>发送数据（TXD）</td>
> <td>PB13</td>
> </tr>
> <tr>
> <td>接收数据（RXD）</td>
> <td>PB12</td>
> </tr>
> <tr>
> <td>STD</td>
> <td>PE3</td>
> </tr>
> </table>

<a id="usb"></a>

#### 通用串行总线（USB）

LINUM-STM32H753BI具有一个USB端口。

> <table>
> <tr>
> <th>通用串行总线（USB）</th>
> <th>引脚（Pins）</th>
> </tr>
> <tr>
> <td>USB_VBUS</td>
> <td>PA9</td>
> </tr>
> <tr>
> <td>USB_N</td>
> <td>PA11</td>
> </tr>
> <tr>
> <td>USB_P</td>
> <td>PA12</td>
> </tr>
> <tr>
> <td>USB_EN</td>
> <td>PI12</td>
> </tr>
> <tr>
> <td>USB_FLT</td>
> <td>PI13</td>
> </tr>
> </table>

<a id="i2c3"></a>

#### I2C3

EEPROM及触摸屏传感器连接I2C3。

> <table>
> <tr>
> <th>I2C3</th>
> <th>引脚（Pins）</th>
> </tr>
> <tr>
> <td>串行时钟线（SCL）</td>
> <td>PH7</td>
> </tr>
> <tr>
> <td>串行数据线（SDA）</td>
> <td>PH8</td>
> </tr>
> </table>

<a id="external-sdram"></a>

#### 外部同步动态RAM（SDRAM）

LINUM-STM32H753BI的8 MB外部SDRAM连接灵活存储控制器（FMC）。

> <table>
> <tr>
> <th>灵活存储控制器（FMC）</th>
> <th>引脚（Pins）</th>
> </tr>
> <tr>
> <td>FMC_A0</td>
> <td>PF0</td>
> </tr>
> <tr>
> <td>FMC_A1</td>
> <td>PF1</td>
> </tr>
> <tr>
> <td>FMC_A2</td>
> <td>PF2</td>
> </tr>
> <tr>
> <td>FMC_A3</td>
> <td>PF3</td>
> </tr>
> <tr>
> <td>FMC_A4</td>
> <td>PF4</td>
> </tr>
> <tr>
> <td>FMC_A5</td>
> <td>PF5</td>
> </tr>
> <tr>
> <td>FMC_A6</td>
> <td>PF12</td>
> </tr>
> <tr>
> <td>FMC_A7</td>
> <td>PF13</td>
> </tr>
> <tr>
> <td>FMC_A8</td>
> <td>PF14</td>
> </tr>
> <tr>
> <td>FMC_A9</td>
> <td>PF15</td>
> </tr>
> <tr>
> <td>FMC_A10</td>
> <td>PG0</td>
> </tr>
> <tr>
> <td>FMC_A11</td>
> <td>PG1</td>
> </tr>
> <tr>
> <td>FMC_BA0</td>
> <td>PG4</td>
> </tr>
> <tr>
> <td>FMC_BA1</td>
> <td>PG5</td>
> </tr>
> <tr>
> <td>FMC_D0</td>
> <td>PD14</td>
> </tr>
> <tr>
> <td>FMC_D1</td>
> <td>PD15</td>
> </tr>
> <tr>
> <td>FMC_D2</td>
> <td>PD0</td>
> </tr>
> <tr>
> <td>FMC_D3</td>
> <td>PD1</td>
> </tr>
> <tr>
> <td>FMC_D4</td>
> <td>PE7</td>
> </tr>
> <tr>
> <td>FMC_D5</td>
> <td>PE8</td>
> </tr>
> <tr>
> <td>FMC_D6</td>
> <td>PE9</td>
> </tr>
> <tr>
> <td>FMC_D7</td>
> <td>PE10</td>
> </tr>
> <tr>
> <td>FMC_D8</td>
> <td>PE11</td>
> </tr>
> <tr>
> <td>FMC_D9</td>
> <td>PE12</td>
> </tr>
> <tr>
> <td>FMC_D10</td>
> <td>PE13</td>
> </tr>
> <tr>
> <td>FMC_D11</td>
> <td>PE14</td>
> </tr>
> <tr>
> <td>FMC_D12</td>
> <td>PE15</td>
> </tr>
> <tr>
> <td>FMC_D13</td>
> <td>PD8</td>
> </tr>
> <tr>
> <td>FMC_D14</td>
> <td>PD9</td>
> </tr>
> <tr>
> <td>FMC_D15</td>
> <td>PD10</td>
> </tr>
> <tr>
> <td>FMC_NBL0</td>
> <td>PE0</td>
> </tr>
> <tr>
> <td>FMC_NBL1</td>
> <td>PE1</td>
> </tr>
> <tr>
> <td>FMC_SDCKE0</td>
> <td>PC3</td>
> </tr>
> <tr>
> <td>FMC_SDCLK</td>
> <td>PG8</td>
> </tr>
> <tr>
> <td>FMC_SDNCAS</td>
> <td>PG15</td>
> </tr>
> <tr>
> <td>FMC_SDNEO</td>
> <td>PC2</td>
> </tr>
> <tr>
> <td>FMC_SDNRAS</td>
> <td>PF11</td>
> </tr>
> <tr>
> <td>FMC_SDNWE</td>
> <td>PC0</td>
> </tr>
> </table>

<a id="lcd"></a>

#### 液晶显示屏（LCD）

LINUM-STM32H753BI使用LCD-TFT显示控制器（LTDC）支持RGB接口LCD。

> <table>
> <tr>
> <th>LCD-TFT显示控制器（LTDC）</th>
> <th>引脚（Pins）</th>
> </tr>
> <tr>
> <td>LTDC_B0</td>
> <td>PJ12</td>
> </tr>
> <tr>
> <td>LTDC_B1</td>
> <td>PJ13</td>
> </tr>
> <tr>
> <td>LTDC_B2</td>
> <td>PJ14</td>
> </tr>
> <tr>
> <td>LTDC_B3</td>
> <td>PJ15</td>
> </tr>
> <tr>
> <td>LTDC_B4</td>
> <td>PK3</td>
> </tr>
> <tr>
> <td>LTDC_B5</td>
> <td>PK4</td>
> </tr>
> <tr>
> <td>LTDC_B6</td>
> <td>PK5</td>
> </tr>
> <tr>
> <td>LTDC_B7</td>
> <td>PK6</td>
> </tr>
> <tr>
> <td>LTDC_CLK</td>
> <td>PI14</td>
> </tr>
> <tr>
> <td>LTDC_DE</td>
> <td>PK7</td>
> </tr>
> <tr>
> <td>LTDC_G0</td>
> <td>PJ7</td>
> </tr>
> <tr>
> <td>LTDC_G1</td>
> <td>PJ8</td>
> </tr>
> <tr>
> <td>LTDC_G2</td>
> <td>PJ9</td>
> </tr>
> <tr>
> <td>LTDC_G3</td>
> <td>PJ10</td>
> </tr>
> <tr>
> <td>LTDC_G4</td>
> <td>PJ11</td>
> </tr>
> <tr>
> <td>LTDC_G5</td>
> <td>PK0</td>
> </tr>
> <tr>
> <td>LTDC_G6</td>
> <td>PK1</td>
> </tr>
> <tr>
> <td>LTDC_G7</td>
> <td>PK2</td>
> </tr>
> <tr>
> <td>LTDC_HSYNC</td>
> <td>PI10</td>
> </tr>
> <tr>
> <td>LTDC_R0</td>
> <td>PI15</td>
> </tr>
> <tr>
> <td>LTDC_R1</td>
> <td>PJ0</td>
> </tr>
> <tr>
> <td>LTDC_R2</td>
> <td>PJ1</td>
> </tr>
> <tr>
> <td>LTDC_R3</td>
> <td>PJ2</td>
> </tr>
> <tr>
> <td>LTDC_R4</td>
> <td>PJ3</td>
> </tr>
> <tr>
> <td>LTDC_R5</td>
> <td>PJ4</td>
> </tr>
> <tr>
> <td>LTDC_R6</td>
> <td>PJ5</td>
> </tr>
> <tr>
> <td>LTDC_R7</td>
> <td>PJ6</td>
> </tr>
> <tr>
> <td>LTDC_VSYNC</td>
> <td>PI9</td>
> </tr>
> <tr>
> <td>PWM_BACKLIGHT</td>
> <td>PH6</td>
> </tr>
> </table>

<a id="system-clock"></a>

#### 系统时钟（System Clock）

原文此处将板卡称为Linum H753ZI。系统时钟可由内部、外部振荡器或主PLL驱动，默认25 MHz外部高速时钟经PLL生成480 MHz。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`linum`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd"><code>openocd</code></a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td></td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-stm32cubeprogrammer">stm32cubeprogrammer</a></td>
<td>✅</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

linum应用可按常规方式构建及烧录，详见“构建应用”与“运行应用”。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）

注意（Note）

调试或编程Linum需使用外部调试／烧录工具连接SWD接口，J-Link及ST-Link是可直接兼容的例子。

<a id="flashing"></a>

### 烧录（Flashing）

<a id="flashing-an-application-to-the-linum-board"></a>

#### 向Linum开发板烧录应用

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

运行主机串口程序连接开发板；原文此处写Nucleo，与本页Linum型号不同。

```text
$ minicom -b 115200 -D /dev/ttyACM0
```

构建并烧录应用：

```text
# From the root of the zephyr repository
west build -b linum samples/hello_world
west flash
```

控制台上应显示以下消息：

```text
$ Hello World! linum
```

<a id="debugging"></a>

### 调试（Debugging）

可以按常规方式调试应用。下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b linum samples/hello_world
west debug
```

## 译注

Linum原文同时出现SRAM／SDRAM、H753BI／H753ZI、RBG／RGB及Nucleo板名差异，已注明。电气接口和电源范围按原文保留。

---

[上一章](P040_Witte.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P042_WIZnet.md)
