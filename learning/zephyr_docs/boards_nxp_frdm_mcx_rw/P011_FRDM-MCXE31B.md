---
id: learning.zephyr-docs.boards-nxp-frdm-mcx-rw.page-11
title: FRDM-MCXE31B
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxe31b/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="frdm_mcxe31b"></a>

# 第11章\_FRDM-MCXE31B

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxe31b/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/frdm_mcxe31b.webp](images/frdm_mcxe31b.webp)](images/frdm_mcxe31b.webp)

FRDM-MCXE31B

名称（Name）：

`frdm_mcxe31b`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mcxe31b](https://docs.zephyrproject.org/latest/boards/index.html#soc=mcxe31b)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_mcxe31b/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

FRDM-MCXE31B是基于NXP MCXE31B微控制器（MCU）的设计及评估平台。MCXE31B采用Arm Cortex-M7内核，最高160 MHz，供电范围2.97—5.5 V。

<a id="hardware"></a>

## 硬件（Hardware）


- MCXE31B Arm Cortex-M7微控制器，最高160 MHz
- 4 MB双存储体片内闪存
- 320 KB SRAM加192 KB紧耦合存储器（TCM）
- 2路I2C总线
- 6路SPI
- 16路UART
- 支持CMSIS-DAP的板载MCU-Link调试器
- Arduino排针及mikroBUS

MCXE31B SoC及FRDM-MCXE31B开发板的更多信息见以下资料：


- [MCXE31X 数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/MCXEP172M160FB0.pdf)
- [MCXE31X 参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=MCXE31XRM&location=null)
- [FRDM-MCXE31B 开发板用户手册（Board User Manual）](https://www.nxp.com/webapp/Download?colCode=UM12330&location=null&isHTMLorPDF=HTML)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`frdm_mcxe31b`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="frdm_mcxe31b-hw-features"></a>

<a id="frdm_mcxe31b-frdm_mcxe31b@default/mcxe31b-hw-features-section"></a>

#### `frdm_mcxe31b@default/mcxe31b`目标（Target）

<a id="frdm_mcxe31b-frdm_mcxe31b@default/mcxe31b-hw-features-panel"></a>

<a id="frdm_mcxe31b-frdm_mcxe31b@default/mcxe31b-hw-features-memory"></a>

该开发板目标的片上存储容量：288 KiB RAM、3920 KiB Flash。

<a id="frdm_mcxe31b-frdm_mcxe31b@default/mcxe31b-hw-features-table"></a>

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
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L16">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP逐次逼近型ADC（SAR ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L50">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L61">已禁用：2</a>）</td>
<td><a href="../hardware/P854_NXP逐次逼近ADC绑定.md#dtbinding-nxp-sar-adc"><code>nxp,sar-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L473">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L482">已禁用：5</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="4">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>快速内部RC振荡器（Fast Internal RC Oscillator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L467">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P014_nxp_firc.md#std-dtcompatible-nxp-firc"><code>nxp,firc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>快速外部晶体振荡器（Fast External Crystal Oscillator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L535">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P015_nxp_fxosc.md#std-dtcompatible-nxp-fxosc"><code>nxp,fxosc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>支持无毛刺时钟切换的时钟生成模块（Clock Generation Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L811">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P010_nxp_mc-cgm.md#std-dtcompatible-nxp-mc-cgm"><code>nxp,mc-cgm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>锁相环（Phase-locked Loop）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L970">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P013_nxp_plldig.md#std-dtcompatible-nxp-plldig"><code>nxp,plldig</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟监测（Clock Monitor）</td>
<td>片上（On-Chip）</td>
<td>NXP时钟监测单元频率检查模块（CMU_FC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L94">已禁用：4</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P001_nxp_cmu-fc.md#std-dtcompatible-nxp-cmu-fc"><code>nxp,cmu-fc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP时钟监测单元频率计（CMU_FM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L103">已禁用：2</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P002_nxp_cmu-fm.md#std-dtcompatible-nxp-cmu-fm"><code>nxp,cmu-fm</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗比较器（LPCMP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L567">已禁用：3</a>）</td>
<td><a href="../hardware/P747_NXP低功耗比较器绑定.md#dtbinding-nxp-lpcmp"><code>nxp,lpcmp</code></a></td>
</tr>
<tr>
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP周期中断定时器（PIT / Periodic Interrupt Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L865">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L900">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P017_nxp_pit.md#std-dtcompatible-nxp-pit"><code>nxp,pit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>周期中断定时器节点的子节点，用于表示单个定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L875">已禁用：12</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P016_nxp_pit-channel.md#std-dtcompatible-nxp-pit-channel"><code>nxp,pit-channel</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP系统定时器模块（STM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1321">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1329">已禁用：1</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P001_nxp_stm.md#std-dtcompatible-nxp-stm"><code>nxp,stm</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L154">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P006_nxp_crc.md#std-dtcompatible-nxp-crc"><code>nxp,crc</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L183">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="2">错误检测与纠正（EDAC）</td>
<td>片上（On-Chip）</td>
<td>NXP错误注入模块（Error Injection Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L204">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P002_nxp_eim.md#std-dtcompatible-nxp-eim"><code>nxp,eim</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP错误报告模块（Error Reporting Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L452">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P003_nxp_erm.md#std-dtcompatible-nxp-erm"><code>nxp,erm</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP ENET QOS以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L294">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P003_nxp_enet-qos.md#std-dtcompatible-nxp-enet-qos"><code>nxp,enet-qos</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 的管理数据输入输出控制器（MDIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L308">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P010_snps_dwmac-mdio.md#std-dtcompatible-snps-dwmac-mdio"><code>snps,dwmac-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L249">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 精确时间协议时钟（Precision Time Protocol，PTP Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L315">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P006_snps_dwmac-ptp-clock.md#std-dtcompatible-snps-dwmac-ptp-clock"><code>snps,dwmac-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP C40闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L24">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P008_nxp_c40-flash-controller.md#std-dtcompatible-nxp-c40-flash-controller"><code>nxp,c40-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="3">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>NXP SIUL2 GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1130">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1096">已禁用：9</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P028_nxp_siul2-gpio.md#std-dtcompatible-nxp-siul2-gpio"><code>nxp,siul2-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L71">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP LCD 8080接口上引出的GPIO引脚，例如LCD-PAR-035面板使用的引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L100">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P003_nxp_lcd-8080.md#std-dtcompatible-nxp-lcd-8080"><code>nxp,lcd-8080</code></a></td>
</tr>
<tr>
<td rowspan="2">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP复位生成模块（MC_RGM / Reset Generation Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L824">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P010_nxp_mc-rgm.md#std-dtcompatible-nxp-mc-rgm"><code>nxp,mc-rgm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP一次性可编程（OTP）唯一芯片标识符（UID）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P011_nxp_otp-uid.md#std-dtcompatible-nxp-otp-uid"><code>nxp,otp-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件自旋锁（Hardware Spinlock）</td>
<td>片上（On-Chip）</td>
<td>NXP SEMA42硬件信号量（Hardware Semaphore）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1068">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42"><code>nxp,sema42</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L591">已启用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1024">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1040">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L61">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP SIUL2外部中断请求控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1086">已启用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P006_nxp_siul2-eirq.md#std-dtcompatible-nxp-siul2-eirq"><code>nxp,siul2-eirq</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32唤醒单元（Wake-up Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1378">已禁用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P005_nxp_s32-wkpu.md#std-dtcompatible-nxp-s32-wkpu"><code>nxp,s32-wkpu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L42">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示总线接口（MIPI-DBI）</td>
<td>板载（On-Board）</td>
<td>NXP FlexIO LCD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L372">已启用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P005_nxp_mipi-dbi-flexio-lcdif.md#std-dtcompatible-nxp-mipi-dbi-flexio-lcdif"><code>nxp,mipi-dbi-flexio-lcdif</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L527">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td rowspan="1">多位串行外设接口（Multi-Bit SPI）</td>
<td>片上（On-Chip）</td>
<td>具有多比特SPI（MSPI）接口的NXP QSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L995">已禁用：1</a>）</td>
<td><a href="../mspi_binding_reference/P008_nxp_qspi.md#std-dtcompatible-nxp-qspi"><code>nxp,qspi</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>MSPI总线上的通用NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L418">已禁用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P024_jedec_nor-mspi.md#std-dtcompatible-jedec-nor"><code>jedec,nor</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP C40内部闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31b.dtsi?plain=1#L103">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P015_nxp_c40-flash.md#std-dtcompatible-nxp-c40-flash"><code>nxp,c40-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">多路复用器（MUX）</td>
<td>片上（On-Chip）</td>
<td>NXP TRGMUX外设封装器（Peripheral Wrapper）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1360">已禁用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P005_nxp_trgmux.md#std-dtcompatible-nxp-trgmux"><code>nxp,trgmux</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>MCXE31X SoC的NXP SIUL2引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P015_nxp_mcxe31x-siul2-pinctrl.md#std-dtcompatible-nxp-mcxe31x-siul2-pinctrl"><code>nxp,mcxe31x-siul2-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>增强型模块化输入输出子系统（eMIOS / Enhanced Modular IO SubSystem）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L320">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L364">已禁用：2</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P001_nxp_emios.md#std-dtcompatible-nxp-emios"><code>nxp,emios</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP eMIOS脉宽调制（PWM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L357">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L401">已禁用：2</a>）</td>
<td><a href="../pwm_intel_microchip_nxp_binding_reference/P020_nxp_emios-pwm.md#std-dtcompatible-nxp-emios-pwm"><code>nxp,emios-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>NXP实时时钟（RTC），JDP代RTC IP（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1008">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P001_nxp_rtc-jdp.md#std-dtcompatible-nxp-rtc-jdp"><code>nxp,rtc-jdp</code></a></td>
</tr>
<tr>
<td rowspan="2">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>FXLS8974三轴加速度传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L397">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P051_nxp_fxls8974.md#std-dtcompatible-nxp-fxls8974"><code>nxp,fxls8974</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP片上温度传感器（TEMPSENSE）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1352">已禁用：1</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P014_nxp_tempsense.md#std-dtcompatible-nxp-tempsense"><code>nxp,tempsense</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L723">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L683">已禁用：15</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L611">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L623">已禁用：5</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31b.dtsi?plain=1#L35">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>软件看门狗定时器（SWT / Software Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1337">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P013_nxp_s32-swt.md#std-dtcompatible-nxp-s32-swt"><code>nxp,s32-swt</code></a></td>
</tr>
</table>

<a id="frdm_mcxe31b-frdm_mcxe31b@w25q64/mcxe31b-hw-features-section"></a>

#### `frdm_mcxe31b@w25q64/mcxe31b`目标（Target）

<a id="frdm_mcxe31b-frdm_mcxe31b@w25q64/mcxe31b-hw-features-panel"></a>

<a id="frdm_mcxe31b-frdm_mcxe31b@w25q64/mcxe31b-hw-features-memory"></a>

该开发板目标的片上存储容量：288 KiB RAM、3920 KiB Flash。

<a id="frdm_mcxe31b-frdm_mcxe31b@w25q64/mcxe31b-hw-features-table"></a>

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
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L16">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP逐次逼近型ADC（SAR ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L50">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L61">已禁用：2</a>）</td>
<td><a href="../hardware/P854_NXP逐次逼近ADC绑定.md#dtbinding-nxp-sar-adc"><code>nxp,sar-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L473">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L482">已禁用：5</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="4">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>快速内部RC振荡器（Fast Internal RC Oscillator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L467">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P014_nxp_firc.md#std-dtcompatible-nxp-firc"><code>nxp,firc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>快速外部晶体振荡器（Fast External Crystal Oscillator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L535">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P015_nxp_fxosc.md#std-dtcompatible-nxp-fxosc"><code>nxp,fxosc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>支持无毛刺时钟切换的时钟生成模块（Clock Generation Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L811">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P010_nxp_mc-cgm.md#std-dtcompatible-nxp-mc-cgm"><code>nxp,mc-cgm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>锁相环（Phase-locked Loop）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L970">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P013_nxp_plldig.md#std-dtcompatible-nxp-plldig"><code>nxp,plldig</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟监测（Clock Monitor）</td>
<td>片上（On-Chip）</td>
<td>NXP时钟监测单元频率检查模块（CMU_FC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L94">已禁用：4</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P001_nxp_cmu-fc.md#std-dtcompatible-nxp-cmu-fc"><code>nxp,cmu-fc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP时钟监测单元频率计（CMU_FM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L103">已禁用：2</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P002_nxp_cmu-fm.md#std-dtcompatible-nxp-cmu-fm"><code>nxp,cmu-fm</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗比较器（LPCMP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L567">已禁用：3</a>）</td>
<td><a href="../hardware/P747_NXP低功耗比较器绑定.md#dtbinding-nxp-lpcmp"><code>nxp,lpcmp</code></a></td>
</tr>
<tr>
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP周期中断定时器（PIT / Periodic Interrupt Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L865">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L900">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P017_nxp_pit.md#std-dtcompatible-nxp-pit"><code>nxp,pit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>周期中断定时器节点的子节点，用于表示单个定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L875">已禁用：12</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P016_nxp_pit-channel.md#std-dtcompatible-nxp-pit-channel"><code>nxp,pit-channel</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP系统定时器模块（STM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1321">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1329">已禁用：1</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P001_nxp_stm.md#std-dtcompatible-nxp-stm"><code>nxp,stm</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L154">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P006_nxp_crc.md#std-dtcompatible-nxp-crc"><code>nxp,crc</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L183">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="2">错误检测与纠正（EDAC）</td>
<td>片上（On-Chip）</td>
<td>NXP错误注入模块（Error Injection Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L204">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P002_nxp_eim.md#std-dtcompatible-nxp-eim"><code>nxp,eim</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP错误报告模块（Error Reporting Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L452">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P003_nxp_erm.md#std-dtcompatible-nxp-erm"><code>nxp,erm</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP ENET QOS以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L294">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P003_nxp_enet-qos.md#std-dtcompatible-nxp-enet-qos"><code>nxp,enet-qos</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 的管理数据输入输出控制器（MDIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L308">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P010_snps_dwmac-mdio.md#std-dtcompatible-snps-dwmac-mdio"><code>snps,dwmac-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L249">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 精确时间协议时钟（Precision Time Protocol，PTP Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L315">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P006_snps_dwmac-ptp-clock.md#std-dtcompatible-snps-dwmac-ptp-clock"><code>snps,dwmac-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP C40闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L24">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P008_nxp_c40-flash-controller.md#std-dtcompatible-nxp-c40-flash-controller"><code>nxp,c40-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="3">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>NXP SIUL2 GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1130">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1096">已禁用：9</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P028_nxp_siul2-gpio.md#std-dtcompatible-nxp-siul2-gpio"><code>nxp,siul2-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L71">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP LCD 8080接口上引出的GPIO引脚，例如LCD-PAR-035面板使用的引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L100">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P003_nxp_lcd-8080.md#std-dtcompatible-nxp-lcd-8080"><code>nxp,lcd-8080</code></a></td>
</tr>
<tr>
<td rowspan="2">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP复位生成模块（MC_RGM / Reset Generation Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L824">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P010_nxp_mc-rgm.md#std-dtcompatible-nxp-mc-rgm"><code>nxp,mc-rgm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP一次性可编程（OTP）唯一芯片标识符（UID）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P011_nxp_otp-uid.md#std-dtcompatible-nxp-otp-uid"><code>nxp,otp-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件自旋锁（Hardware Spinlock）</td>
<td>片上（On-Chip）</td>
<td>NXP SEMA42硬件信号量（Hardware Semaphore）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1068">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42"><code>nxp,sema42</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L591">已启用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1024">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1040">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L61">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP SIUL2外部中断请求控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1086">已启用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P006_nxp_siul2-eirq.md#std-dtcompatible-nxp-siul2-eirq"><code>nxp,siul2-eirq</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32唤醒单元（Wake-up Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1378">已禁用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P005_nxp_s32-wkpu.md#std-dtcompatible-nxp-s32-wkpu"><code>nxp,s32-wkpu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L42">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示总线接口（MIPI-DBI）</td>
<td>板载（On-Board）</td>
<td>NXP FlexIO LCD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L372">已启用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P005_nxp_mipi-dbi-flexio-lcdif.md#std-dtcompatible-nxp-mipi-dbi-flexio-lcdif"><code>nxp,mipi-dbi-flexio-lcdif</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L527">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td rowspan="1">多位串行外设接口（Multi-Bit SPI）</td>
<td>片上（On-Chip）</td>
<td>具有多比特SPI（MSPI）接口的NXP QSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L995">已启用：1</a>）</td>
<td><a href="../mspi_binding_reference/P008_nxp_qspi.md#std-dtcompatible-nxp-qspi"><code>nxp,qspi</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>MSPI总线上的通用NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L418">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P024_jedec_nor-mspi.md#std-dtcompatible-jedec-nor"><code>jedec,nor</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP C40内部闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31b.dtsi?plain=1#L103">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P015_nxp_c40-flash.md#std-dtcompatible-nxp-c40-flash"><code>nxp,c40-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">多路复用器（MUX）</td>
<td>片上（On-Chip）</td>
<td>NXP TRGMUX外设封装器（Peripheral Wrapper）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1360">已禁用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P005_nxp_trgmux.md#std-dtcompatible-nxp-trgmux"><code>nxp,trgmux</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>MCXE31X SoC的NXP SIUL2引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P015_nxp_mcxe31x-siul2-pinctrl.md#std-dtcompatible-nxp-mcxe31x-siul2-pinctrl"><code>nxp,mcxe31x-siul2-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>增强型模块化输入输出子系统（eMIOS / Enhanced Modular IO SubSystem）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L320">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L364">已禁用：2</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P001_nxp_emios.md#std-dtcompatible-nxp-emios"><code>nxp,emios</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP eMIOS脉宽调制（PWM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L357">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L401">已禁用：2</a>）</td>
<td><a href="../pwm_intel_microchip_nxp_binding_reference/P020_nxp_emios-pwm.md#std-dtcompatible-nxp-emios-pwm"><code>nxp,emios-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>NXP实时时钟（RTC），JDP代RTC IP（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1008">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P001_nxp_rtc-jdp.md#std-dtcompatible-nxp-rtc-jdp"><code>nxp,rtc-jdp</code></a></td>
</tr>
<tr>
<td rowspan="2">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>FXLS8974三轴加速度传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxe31b/frdm_mcxe31b.dts?plain=1#L397">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P051_nxp_fxls8974.md#std-dtcompatible-nxp-fxls8974"><code>nxp,fxls8974</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP片上温度传感器（TEMPSENSE）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1352">已禁用：1</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P014_nxp_tempsense.md#std-dtcompatible-nxp-tempsense"><code>nxp,tempsense</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L723">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L683">已禁用：15</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L611">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L623">已禁用：5</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31b.dtsi?plain=1#L35">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>软件看门狗定时器（SWT / Software Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxe/nxp_mcxe31x_common.dtsi?plain=1#L1337">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P013_nxp_s32-swt.md#std-dtcompatible-nxp-s32-swt"><code>nxp,s32-swt</code></a></td>
</tr>
</table>

<a id="shields-for-supported-features"></a>

### 支持相应功能的扩展板（Shields）

上表部分功能使用Zephyr扩展板测试，以下扩展板已在此板上测试：


- [NXP LCD_PAR_S035 TFT LCD模块](https://docs.zephyrproject.org/latest/boards/shields/lcd_par_s035/doc/index.html#lcd-par-s035)：支持显示接口（Display）；此板通过片上FlexIO外设连接扩展板的MIPI_DBI接口。

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

每个GPIO端口分为两组引脚（Banks）：低位组为0—15脚，高位组为16—31脚。例如，PTA2对应gpioa_l低位组的第2脚，PTA20对应gpioa_h高位组的第4脚。

GPIO控制器可按SoC支持情况，将外部输入焊盘中断路由至SIUL2外部中断请求（EIRQ）或唤醒单元（WKPU）中断控制器。默认路由至SIUL2 EIRQ；只有按[dts/bindings/gpio/nxp,siul2-gpio.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/gpio/nxp,siul2-gpio.yaml)说明显式配置后，才定向至WKPU。

各中断控制器支持哪些GPIO，请查阅器件参考手册。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PTC16</td>
<td>通用输入输出（GPIO）</td>
<td>红色LED（Red LED）</td>
</tr>
<tr>
<td>PTB22</td>
<td>通用输入输出（GPIO）</td>
<td>绿色LED（Green LED）</td>
</tr>
<tr>
<td>PTC14</td>
<td>通用输入输出（GPIO）</td>
<td>蓝色LED（Blue LED）</td>
</tr>
<tr>
<td>PTE3</td>
<td>LPUART5_RX</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>PTE14</td>
<td>LPUART5_TX</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>PTA7</td>
<td>FLEXCAN0</td>
<td>CAN0发送（TX）</td>
</tr>
<tr>
<td>PTA6</td>
<td>FLEXCAN0</td>
<td>CAN0接收（RX）</td>
</tr>
<tr>
<td>PTB4</td>
<td>EMAC</td>
<td>以太网管理数据输入输出（MDIO）</td>
</tr>
<tr>
<td>PTB5</td>
<td>EMAC</td>
<td>以太网管理数据时钟（MDC）</td>
</tr>
<tr>
<td>PTC0</td>
<td>EMAC</td>
<td>以太网RMII接收数据1（RXD1）</td>
</tr>
<tr>
<td>PTC1</td>
<td>EMAC</td>
<td>以太网RMII接收数据0（RXD0）</td>
</tr>
<tr>
<td>PTC2</td>
<td>EMAC</td>
<td>以太网RMII发送数据0（TXD0）</td>
</tr>
<tr>
<td>PTC3</td>
<td>通用输入输出（GPIO）</td>
<td>以太网PHY复位</td>
</tr>
<tr>
<td>PTC17</td>
<td>EMAC</td>
<td>以太网RMII接收数据有效（RX_DV）</td>
</tr>
<tr>
<td>PTD7</td>
<td>EMAC</td>
<td>以太网RMII发送数据1（TXD1）</td>
</tr>
<tr>
<td><code>PTD11</code></td>
<td>EMAC</td>
<td>以太网RMII参考时钟（REF_CLK）</td>
</tr>
<tr>
<td>PTD12</td>
<td>EMAC</td>
<td>以太网RMII发送使能（TX_EN）</td>
</tr>
</table>

<a id="ethernet"></a>

### 以太网（Ethernet）

板上使用Microchip LAN8741 10/100 Mbit/s PHY，MDIO地址为0，经简化媒体独立接口（RMII）连接MCXE31B的以太网MAC（EMAC）。EMAC采用Synopsys DesignWare Ethernet QoS核，由通用[drivers/ethernet/dwc_mac](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac)驱动管理，而非基于NXP HAL的eth_nxp_enet_qos驱动。

PHY提供50 MHz RMII参考时钟，SoC从PTD11接收并二分频，为MAC的MII侧提供时钟。驱动也支持通过phy-connection-type选择MII，但此板实际布线为RMII。

<a id="system-clock"></a>

### 系统时钟（System Clock）

MCXE31B SoC配置为使用160 MHz锁相环（PLL）作为系统时钟源。

<a id="serial-port"></a>

### 串口（Serial Port）

MCXE31B的LPUART5用于控制台。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`frdm_mcxe31b`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-linkserver">linkserver</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td></td>
<td></td>
<td>✅</td>
</tr>
</table>

按通常方式构建并烧录应用，详见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）与“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

<a id="configuring-a-debug-probe"></a>

### 配置调试探针（Configuring a Debug Probe）

烧录和调试均使用调试探针，默认配置为MCU-Link CMSIS-DAP板载调试探针。

<a id="using-linkserver"></a>

#### 使用LinkServer

默认运行工具（Runner）为LinkServer，支持出厂MCU-Link固件。只有板载调试电路固件被更换时，才需按MCU-Link CMSIS-DAP板载调试探针说明重新写入默认固件；写入前短接JP3，进入ISP模式。（[板载MCU-Link CMSIS-DAP调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#mcu-link-cmsis-onboard-debug-probe)）

<a id="using-j-link"></a>

#### 使用J-Link

有两种方案。第一种按MCU-Link J-Link板载调试探针说明，将板载调试电路更新为Segger J-Link固件；写入前短接JP3，进入ISP模式。第二种将外部J-Link调试探针连接到10引脚SWD连接器J14。两种方案都需给west传入-r jlink，选择J-Link运行工具。（[MCU-Link J-Link板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#mcu-link-jlink-onboard-debug-probe)；[J-Link外部调试探针（External Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#jlink-external-debug-probe)）

```text
west flash -r jlink
```

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

用USB线缆将PC连接到J13，在所选串口终端（如minicom、PuTTY）中使用以下设置：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

### 烧录（Flashing）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b frdm_mcxe31b samples/hello_world
west flash
```

打开串口终端，复位开发板（按下RESET按键），应能在终端中看到以下消息：

```text
*** Booting Zephyr OS build v4.2.0-2092-g17e93a718422 ***
Hello World! frdm_mcxe31b/mcxe31b
```

<a id="debugging"></a>

### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b frdm_mcxe31b samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
*** Booting Zephyr OS build v4.2.0-2092-g17e93a718422 ***
Hello World! frdm_mcxe31b/mcxe31b
```

<a id="troubleshooting"></a>

### 故障排查（Troubleshooting）

<a id="using-segger-systemview-and-rtt"></a>

#### 使用Segger SystemView及RTT

此SoC使用SEGGER SystemView或实时传输（RTT）时，必须在SystemView或RTT Viewer中手动设置RTT控制块地址。该地址为_SEGGER_RTT符号的位置，可通过调试器或链接器输出的zephyr.map文件查找。

必须手动指定控制块地址，是因为此SoC支持带纠错码（ECC）的RAM。当ECC已启用、待搜索RAM区域尚未初始化为已知值时，SEGGER工具若在ECC RAM中搜索控制块，将引发故障（Fault）。

<a id="qspi-flash"></a>

## 四线SPI闪存（QSPI Flash）

FRDM-MCXE31B板载Winbond W25Q64、64 Mbit QSPI NOR闪存。默认未连接QSPI数据和时钟信号，因此默认板卡目标停用w25q64节点，而w25q64板卡修订版本启用该节点。

注意（Note）

使用板载QSPI闪存前，需要焊接R126、R128、R129、R130、R131及R133，并移除R153和R154。

完成硬件返工后，为frdm_mcxe31b@w25q64修订版本构建MSPI闪存示例samples/drivers/mspi/mspi_flash，测试该闪存：

```text
# From the root of the zephyr repository
west build -b frdm_mcxe31b@w25q64 samples/drivers/mspi/mspi_flash
west flash
```

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)
- [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)
- [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- NXP Zephyr主页，包含培训资源（[NXP的Zephyr专题页面](https://nxp.com/zephyr)）
- [NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## 译注

GPIO端口分为低位与高位两组，每组16脚；EIRQ与WKPU中断路由按设备树配置。以太网使用通用dwc_mac驱动及PHY提供的50 MHz时钟。此板QSPI电阻编号与MCXE247不同，不能交叉套用。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [MCXEP172M160FB0.pdf](https://www.nxp.com/docs/en/data-sheet/MCXEP172M160FB0.pdf)：HTTP Error 404: Not Found。
- [Download?colCode=MCXE31XRM&location=null](https://www.nxp.com/webapp/Download?colCode=MCXE31XRM&location=null)：HTTP Error 404: Not Found。
- [Download?colCode=UM12330&location=null&isHTMLorPDF=HTML](https://www.nxp.com/webapp/Download?colCode=UM12330&location=null&isHTMLorPDF=HTML)：HTTP Error 404: Not Found。

---

[上一章](P010_FRDM-MCXE247.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P012_FRDM-MCXL255.md)
