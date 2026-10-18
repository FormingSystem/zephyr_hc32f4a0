---
id: learning.zephyr-docs.boards-nxp-remaining.page-6
title: MR-CANHUBK3
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/mr_canhubk3/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mr_canhubk3"></a>

# 第6章\_MR-CANHUBK3

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/mr_canhubk3/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mr_canhubk3_top.jpg](images/mr_canhubk3_top.jpg)](images/mr_canhubk3_top.jpg)

MR-CANHUBK3

名称（Name）：

`mr_canhubk3`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[s32k344](https://docs.zephyrproject.org/latest/boards/index.html#soc=s32k344)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mr_canhubk3/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id17"></a>

<a id="id21"></a>

[NXP MR-CANHUBK3](https://www.nxp.com/design/development-boards/automotive-development-platforms/s32k-mcu-platforms/s32k344-evaluation-board-for-mobile-robotics-incorporating-100baset1-and-six-can-fd:MR-CANHUBK344) [注8](#id16)是用于自主移动机器人（AMR）、自动导引车（AGV）等移动机器人应用的评估板，采用基于Arm Cortex-M7锁步（Lock-Step）内核的[NXP S32K344](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k3-microcontrollers-for-automotive-general-purpose:S32K3) [注9](#id20)通用汽车微控制器。

<a id="hardware"></a>

## 硬件（Hardware）


- NXP S32K344


  - Arm Cortex-M7锁步核，最高160 MHz
  - 4 MB程序闪存，带ECC
  - 320 KB RAM，带ECC
  - 100 Mbps以太网、CAN FD、FlexIO及QSPI
  - 12位、1 Msps模数转换器（ADC），16位eMIOS定时器
- <a id="id23"></a>

  [NXP FS26安全系统基础芯片](https://www.nxp.com/products/power-management/pmics-and-sbcs/safety-sbcs/safety-system-basis-chip-with-low-power-fit-for-asil-d:FS26)（Safety System Basis Chip）[注10](#id22)
- 接口（Interfaces）


  - 控制台UART
  - 6路CAN FD
  - 100Base-T1以太网
  - JST-GH连接器及I/O排针，提供I2C、SPI、GPIO、PWM等信号

<a id="id18"></a>

硬件与设计资源的更多信息见[NXP MR-CANHUBK3](https://www.nxp.com/design/development-boards/automotive-development-platforms/s32k-mcu-platforms/s32k344-evaluation-board-for-mobile-robotics-incorporating-100baset1-and-six-can-fd:MR-CANHUBK344) [注8](#id16)网站。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`mr_canhubk3`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mr_canhubk3-hw-features"></a>

<a id="mr_canhubk3-mr_canhubk3/s32k344-hw-features-section"></a>

#### `mr_canhubk3/s32k344`目标（Target）

<a id="mr_canhubk3-mr_canhubk3/s32k344-hw-features-panel"></a>

<a id="mr_canhubk3-mr_canhubk3/s32k344-hw-features-memory"></a>

该开发板目标的片上存储容量：320 KiB RAM、4048 KiB Flash。

<a id="mr_canhubk3-mr_canhubk3/s32k344-hw-features-table"></a>

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
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L19">已启用：2</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP S32逐次逼近型模数转换器（SAR ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L558">已禁用：3</a>）</td>
<td><a href="../hardware/P853_NXPS32逐次逼近ADC绑定.md#dtbinding-nxp-s32-adc-sar"><code>nxp,s32-adc-sar</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L477">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L488">已禁用：5</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP S32时钟发生器IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L88">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P014_nxp_s32-clock.md#std-dtcompatible-nxp-s32-clock"><code>nxp,s32-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP S32系统定时器模块（STM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L927">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P018_nxp_s32-sys-timer.md#std-dtcompatible-nxp-s32-sys-timer"><code>nxp,s32-sys-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>板载（On-Board）</td>
<td>I2C总线上的Solomon SSD1306显示控制器（Display Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L397">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P061_solomon_ssd1306.md#std-dtcompatible-solomon-ssd1306"><code>solomon,ssd1306</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L681">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 GMAC／EMAC驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L654">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P010_nxp_s32-gmac.md#std-dtcompatible-nxp-s32-gmac"><code>nxp,s32-gmac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 的管理数据输入输出控制器（MDIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L668">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P010_snps_dwmac-mdio.md#std-dtcompatible-snps-dwmac-mdio"><code>snps,dwmac-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>TJA1103物理层（PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L473">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P010_nxp_tja1103.md#std-dtcompatible-nxp-tja1103"><code>nxp,tja1103</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 精确时间协议时钟（Precision Time Protocol，PTP Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L676">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P006_snps_dwmac-ptp-clock.md#std-dtcompatible-snps-dwmac-ptp-clock"><code>snps,dwmac-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP C40闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P008_nxp_c40-flash-controller.md#std-dtcompatible-nxp-c40-flash-controller"><code>nxp,c40-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>NXP SIUL2 GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L133">已启用：8</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L115">已禁用：6</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P028_nxp_siul2-gpio.md#std-dtcompatible-nxp-siul2-gpio"><code>nxp,siul2-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L538">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L548">已禁用：1</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L147">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SIUL2外部中断请求控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L105">已启用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P006_nxp_siul2-eirq.md#std-dtcompatible-nxp-siul2-eirq"><code>nxp,siul2-eirq</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32唤醒单元（Wake-up Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L334">已禁用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P005_nxp_s32-wkpu.md#std-dtcompatible-nxp-s32-wkpu"><code>nxp,s32-wkpu</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L49">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L99">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="4">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>用于NXP S32 SoC的增强型模块化I/O子系统（eMIOS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L703">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L813">已禁用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P007_nxp_s32-emios.md#std-dtcompatible-nxp-s32-emios"><code>nxp,s32-emios</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L868">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>用于NXP S32 SoC的逻辑控制单元（Logic Control Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L888">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L882">已禁用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P008_nxp_s32-lcu.md#std-dtcompatible-nxp-s32-lcu"><code>nxp,s32-lcu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>用于NXP S32 SoC的触发多路复用控制（Trigger Multiplexing Control）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L894">已启用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P009_nxp_s32-trgmux.md#std-dtcompatible-nxp-s32-trgmux"><code>nxp,s32-trgmux</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="3">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>NXP C40内部闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L76">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P015_nxp_c40-flash.md#std-dtcompatible-nxp-c40-flash"><code>nxp,c40-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>连接NXP S32 QSPI总线的QSPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L328">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P005_nxp_s32-qspi-nor.md#std-dtcompatible-nxp-s32-qspi-nor"><code>nxp,s32-qspi-nor</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存或其他非易失性存储器的固定分区（Fixed Partitions）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L341">已启用：1</a>）</td>
<td><a href="../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions"><code>fixed-partitions</code></a></td>
</tr>
<tr>
<td rowspan="1">物理层（PHY）</td>
<td>板载（On-Board）</td>
<td>由简单GPIO控制的CAN收发器（Transceiver）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L163">已启用：6</a>）</td>
<td><a href="../phy_binding_reference/P001_can-transceiver-gpio.md#std-dtcompatible-can-transceiver-gpio"><code>can-transceiver-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>用于S32K3 SoC的NXP SIUL2引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P019_nxp_s32k3-siul2-pinctrl.md#std-dtcompatible-nxp-s32k3-siul2-pinctrl"><code>nxp,s32k3-siul2-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="3">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>NXP S32K3xx电源管理控制器（PMC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L900">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P019_nxp_s32k3-pmc.md#std-dtcompatible-nxp-s32k3-pmc"><code>nxp,s32k3-pmc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32模块进入控制（MC_ME / Module Entry）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L905">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P017_nxp_s32-mc-me.md#std-dtcompatible-nxp-s32-mc-me"><code>nxp,s32-mc-me</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32模块复位生成（MC_RGM / Module Reset Generation）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L911">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P018_nxp_s32-mc-rgm.md#std-dtcompatible-nxp-s32-mc-rgm"><code>nxp,s32-mc-rgm</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>用于S32 SoC的NXP S32 eMIOS脉宽调制（PWM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L751">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L861">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P011_nxp_s32-emios-pwm.md#std-dtcompatible-nxp-s32-emios-pwm"><code>nxp,s32-emios-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexIO脉宽调制（PWM）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L875">已启用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P002_nxp_flexio-pwm.md#std-dtcompatible-nxp-flexio-pwm"><code>nxp,flexio-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">四线串行外设接口（QSPI）</td>
<td>片上（On-Chip）</td>
<td>NXP S32四线串行外设接口（QSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L469">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P007_nxp_s32-qspi.md#std-dtcompatible-nxp-s32-qspi"><code>nxp,s32-qspi</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>NXP S32正交解码器（Quadrature Decoder）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L115">已启用：1</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P012_nxp_qdec-s32.md#std-dtcompatible-nxp-qdec-s32"><code>nxp,qdec-s32</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L357">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L341">已禁用：15</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L618">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L582">已禁用：5</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L61">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>板载（On-Board）</td>
<td>FS26系统基础芯片（SBC）看门狗驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L437">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P008_nxp_fs26-wdog.md#std-dtcompatible-nxp-fs26-wdog"><code>nxp,fs26-wdog</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>软件看门狗定时器（SWT / Software Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L918">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P013_nxp_s32-swt.md#std-dtcompatible-nxp-s32-swt"><code>nxp,s32-swt</code></a></td>
</tr>
</table>

<a id="mr_canhubk3-mr_canhubk3/s32k344/mcuboot-hw-features-section"></a>

#### `mr_canhubk3/s32k344/mcuboot`目标（Target）

<a id="mr_canhubk3-mr_canhubk3/s32k344/mcuboot-hw-features-panel"></a>

<a id="mr_canhubk3-mr_canhubk3/s32k344/mcuboot-hw-features-memory"></a>

该开发板目标的片上存储容量：320 KiB RAM、4048 KiB Flash。

<a id="mr_canhubk3-mr_canhubk3/s32k344/mcuboot-hw-features-table"></a>

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
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L19">已启用：2</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP S32逐次逼近型模数转换器（SAR ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L558">已禁用：3</a>）</td>
<td><a href="../hardware/P853_NXPS32逐次逼近ADC绑定.md#dtbinding-nxp-s32-adc-sar"><code>nxp,s32-adc-sar</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L477">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L488">已禁用：5</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP S32时钟发生器IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L88">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P014_nxp_s32-clock.md#std-dtcompatible-nxp-s32-clock"><code>nxp,s32-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP S32系统定时器模块（STM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L927">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P018_nxp_s32-sys-timer.md#std-dtcompatible-nxp-s32-sys-timer"><code>nxp,s32-sys-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>板载（On-Board）</td>
<td>I2C总线上的Solomon SSD1306显示控制器（Display Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L397">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P061_solomon_ssd1306.md#std-dtcompatible-solomon-ssd1306"><code>solomon,ssd1306</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L681">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 GMAC／EMAC驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L654">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P010_nxp_s32-gmac.md#std-dtcompatible-nxp-s32-gmac"><code>nxp,s32-gmac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 的管理数据输入输出控制器（MDIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L668">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P010_snps_dwmac-mdio.md#std-dtcompatible-snps-dwmac-mdio"><code>snps,dwmac-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>TJA1103物理层（PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L473">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P010_nxp_tja1103.md#std-dtcompatible-nxp-tja1103"><code>nxp,tja1103</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 精确时间协议时钟（Precision Time Protocol，PTP Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L676">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P006_snps_dwmac-ptp-clock.md#std-dtcompatible-snps-dwmac-ptp-clock"><code>snps,dwmac-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP C40闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P008_nxp_c40-flash-controller.md#std-dtcompatible-nxp-c40-flash-controller"><code>nxp,c40-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>NXP SIUL2 GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L133">已启用：8</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L115">已禁用：6</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P028_nxp_siul2-gpio.md#std-dtcompatible-nxp-siul2-gpio"><code>nxp,siul2-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L538">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L548">已禁用：1</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L147">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SIUL2外部中断请求控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L105">已启用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P006_nxp_siul2-eirq.md#std-dtcompatible-nxp-siul2-eirq"><code>nxp,siul2-eirq</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32唤醒单元（Wake-up Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L334">已禁用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P005_nxp_s32-wkpu.md#std-dtcompatible-nxp-s32-wkpu"><code>nxp,s32-wkpu</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L49">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L99">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="4">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>用于NXP S32 SoC的增强型模块化I/O子系统（eMIOS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L703">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L813">已禁用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P007_nxp_s32-emios.md#std-dtcompatible-nxp-s32-emios"><code>nxp,s32-emios</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L868">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>用于NXP S32 SoC的逻辑控制单元（Logic Control Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L888">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L882">已禁用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P008_nxp_s32-lcu.md#std-dtcompatible-nxp-s32-lcu"><code>nxp,s32-lcu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>用于NXP S32 SoC的触发多路复用控制（Trigger Multiplexing Control）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L894">已启用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P009_nxp_s32-trgmux.md#std-dtcompatible-nxp-s32-trgmux"><code>nxp,s32-trgmux</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="3">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>NXP C40内部闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L76">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P015_nxp_c40-flash.md#std-dtcompatible-nxp-c40-flash"><code>nxp,c40-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>连接NXP S32 QSPI总线的QSPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L328">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P005_nxp_s32-qspi-nor.md#std-dtcompatible-nxp-s32-qspi-nor"><code>nxp,s32-qspi-nor</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存或其他非易失性存储器的固定分区（Fixed Partitions）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L341">已启用：1</a>）</td>
<td><a href="../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions"><code>fixed-partitions</code></a></td>
</tr>
<tr>
<td rowspan="1">物理层（PHY）</td>
<td>板载（On-Board）</td>
<td>由简单GPIO控制的CAN收发器（Transceiver）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L163">已启用：6</a>）</td>
<td><a href="../phy_binding_reference/P001_can-transceiver-gpio.md#std-dtcompatible-can-transceiver-gpio"><code>can-transceiver-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>用于S32K3 SoC的NXP SIUL2引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P019_nxp_s32k3-siul2-pinctrl.md#std-dtcompatible-nxp-s32k3-siul2-pinctrl"><code>nxp,s32k3-siul2-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="3">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>NXP S32K3xx电源管理控制器（PMC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L900">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P019_nxp_s32k3-pmc.md#std-dtcompatible-nxp-s32k3-pmc"><code>nxp,s32k3-pmc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32模块进入控制（MC_ME / Module Entry）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L905">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P017_nxp_s32-mc-me.md#std-dtcompatible-nxp-s32-mc-me"><code>nxp,s32-mc-me</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32模块复位生成（MC_RGM / Module Reset Generation）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L911">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P018_nxp_s32-mc-rgm.md#std-dtcompatible-nxp-s32-mc-rgm"><code>nxp,s32-mc-rgm</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>用于S32 SoC的NXP S32 eMIOS脉宽调制（PWM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L751">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L861">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P011_nxp_s32-emios-pwm.md#std-dtcompatible-nxp-s32-emios-pwm"><code>nxp,s32-emios-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexIO脉宽调制（PWM）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L875">已启用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P002_nxp_flexio-pwm.md#std-dtcompatible-nxp-flexio-pwm"><code>nxp,flexio-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">四线串行外设接口（QSPI）</td>
<td>片上（On-Chip）</td>
<td>NXP S32四线串行外设接口（QSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L469">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P007_nxp_s32-qspi.md#std-dtcompatible-nxp-s32-qspi"><code>nxp,s32-qspi</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>NXP S32正交解码器（Quadrature Decoder）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L115">已启用：1</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P012_nxp_qdec-s32.md#std-dtcompatible-nxp-qdec-s32"><code>nxp,qdec-s32</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L357">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L341">已禁用：15</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L618">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L582">已禁用：5</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L61">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>板载（On-Board）</td>
<td>FS26系统基础芯片（SBC）看门狗驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_canhubk3/mr_canhubk3_common.dtsi?plain=1#L437">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P008_nxp_fs26-wdog.md#std-dtcompatible-nxp-fs26-wdog"><code>nxp,fs26-wdog</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>软件看门狗定时器（SWT / Software Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k344_m7.dtsi?plain=1#L918">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P013_nxp_s32-swt.md#std-dtcompatible-nxp-s32-swt"><code>nxp,s32-swt</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

每个GPIO端口分为两组引脚（Banks）：低位组为0—15脚，高位组为16—31脚。例如，PTA2对应gpioa_l低位组的第2脚，PTA20对应gpioa_h高位组的第4脚。

GPIO控制器可按SoC支持情况，将外部输入焊盘中断路由至SIUL2外部中断请求（EIRQ）或唤醒单元（WKPU）中断控制器。默认路由至SIUL2 EIRQ；只有按[dts/bindings/gpio/nxp,siul2-gpio.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/gpio/nxp,siul2-gpio.yaml)说明显式配置后，才定向至WKPU。

各中断控制器支持哪些GPIO，请查阅器件参考手册。

注意（Note）

当前开发板配置不支持唤醒事件及电源管理功能。唤醒单元（WKPU）仅作为中断控制器使用。

<a id="leds"></a>

#### 发光二极管（LEDs）

MR-CANHUBK3有一个用户RGB LED：

<table>
<tr>
<th>设备树节点（Devicetree Node）</th>
<th>颜色（Color）</th>
<th>引脚（Pin）</th>
<th>引脚功能（Pin Functions）</th>
</tr>
<tr>
<td>led0 / user_led1_red</td>
<td>红色（Red）</td>
<td>PTE14</td>
<td>FXIO D7 / EMIOS0 CH19</td>
</tr>
<tr>
<td>led1 / user_led1_green</td>
<td>绿色（Green）</td>
<td>PTA27</td>
<td>FXIO D5 / EMIOS1 CH10 / EMIOS2 CH10</td>
</tr>
<tr>
<td>led2 / user_led1_blue</td>
<td>蓝色（Blue）</td>
<td>PTE12</td>
<td>FXIO D8 / EMIOS1 CH5</td>
</tr>
</table>

除RGB LED外，MR-CANHUBK3还有6个红色LED，分别位于各CAN连接器旁：

<table>
<tr>
<th>设备树节点（Devicetree Node）</th>
<th>颜色（Color）</th>
<th>引脚（Pin）</th>
<th>引脚功能（Pin Functions）</th>
</tr>
<tr>
<td>can_led0</td>
<td>红色（Red）</td>
<td>PTC18</td>
<td>FXIO D6 / FXIO D12 / EMIOS2 CH12</td>
</tr>
<tr>
<td>can_led1</td>
<td>红色（Red）</td>
<td>PTE5</td>
<td>FXIO D7 / EMIOS1 CH5 / EMIOS0 CH 19</td>
</tr>
<tr>
<td>can_led2</td>
<td>红色（Red）</td>
<td>PTD20</td>
<td>EMIOS1 CH17 / EMIOS2 CH0</td>
</tr>
<tr>
<td>can_led3</td>
<td>红色（Red）</td>
<td>PTB24</td>
<td>FXIO D5 / EMIOS1 CH20 / EMIOS2 CH20</td>
</tr>
<tr>
<td>can_led4</td>
<td>红色（Red）</td>
<td>PTB26</td>
<td>FXIO D7 / EMIOS1 CH22 / EMIOS2 CH22</td>
</tr>
<tr>
<td>can_led5</td>
<td>红色（Red）</td>
<td>PTD31</td>
<td>FXIO D6 / EMIOS2 CH22</td>
</tr>
</table>

用户可自行控制这些LED，输出0时LED亮起。

<a id="buttons"></a>

#### 按键（Buttons）

MR-CANHUBK3有两个用户按键：

<table>
<tr>
<th>设备树节点（Devicetree Node）</th>
<th>标签（Label）</th>
<th>引脚（Pin）</th>
<th>引脚功能（Pin Functions）</th>
</tr>
<tr>
<td>sw0 / user_button_1</td>
<td>SW1</td>
<td>PTD15</td>
<td>EIRQ31</td>
</tr>
<tr>
<td>sw0 / user_button_2</td>
<td>SW2</td>
<td>PTA25</td>
<td>EIRQ5 / WKPU34</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

Arm Cortex-M7锁步（Lock-Step）内核配置为运行于160 MHz。

<a id="serial-console"></a>

### 串口控制台（Serial Console）

默认串口控制台由lpuart2提供，位于7引脚DCD-LZ调试连接器P6。

<table>
<tr>
<th>连接器（Connector）</th>
<th>引脚（Pin）</th>
<th>引脚功能（Pin Function）</th>
</tr>
<tr>
<td>P6.2</td>
<td>PTA9</td>
<td>LPUART2_TX</td>
</tr>
<tr>
<td>P6.3</td>
<td>PTA8</td>
<td>LPUART2_RX</td>
</tr>
</table>

<a id="can"></a>

### 控制器局域网（CAN）

CAN通过FLEXCAN接口提供，共6个实例。

<table>
<tr>
<th>设备树节点（Devicetree Node）</th>
<th>引脚（Pin）</th>
<th>引脚功能（Pin Function）</th>
<th>总线连接器（Bus Connector）</th>
</tr>
<tr>
<td>flexcan0</td>
<td>PTA6<br><br>PTA7</td>
<td>PTA6_CAN0_RX<br><br>PTA7_CAN0_TX</td>
<td>P12/P13</td>
</tr>
<tr>
<td>flexcan1</td>
<td>PTC9<br><br>PTC8</td>
<td>PTC9_CAN0_RX<br><br>PTC8_CAN0_TX</td>
<td>P14/P15</td>
</tr>
<tr>
<td>flexcan2</td>
<td>PTE25<br><br>PTE24</td>
<td>PTE25_CAN0_RX<br><br>PTE24_CAN0_TX</td>
<td>P16/P17</td>
</tr>
<tr>
<td>flexcan3</td>
<td>PTC29<br><br>PTC28</td>
<td>PTC29_CAN0_RX<br><br>PTC28_CAN0_TX</td>
<td>P18/019</td>
</tr>
<tr>
<td>flexcan4</td>
<td>PTC31<br><br>PTC30</td>
<td>PTC31_CAN0_RX<br><br>PTC30_CAN0_TX</td>
<td>P20/P21</td>
</tr>
<tr>
<td>flexcan5</td>
<td>PTC11<br><br>PTC10</td>
<td>PTC11_CAN0_RX<br><br>PTC10_CAN0_TX</td>
<td>P22/P23</td>
</tr>
</table>

注意（Note）

受硬件抽象层软件开发包（HAL SDK）限制，CAN最多支持64个消息缓冲区（Message Buffer，MB）；对于同时活动、使用8字节载荷的实例，最多支持32个消息缓冲区。配置时需注意：


1. [CONFIG_CAN_MCUX_FLEXCAN_MAX_FILTERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_MCUX_FLEXCAN_MAX_FILTERS)必须小于下表所列的最大消息缓冲区数量。

<table>
<tr>
<th>设备树节点（Devicetree Node）</th>
<th>载荷（Payload）</th>
<th>硬件支持（Hardware Support）</th>
<th>软件支持（Software Support）</th>
</tr>
<tr>
<td>flexcan0</td>
<td>8字节<br><br>16字节<br><br>32字节<br><br>64字节</td>
<td>96个消息缓冲区（MB）<br><br>63个消息缓冲区（MB）<br><br>36个消息缓冲区（MB）<br><br>21个消息缓冲区（MB）</td>
<td>64个消息缓冲区（MB）<br><br>42个消息缓冲区（MB）<br><br>24个消息缓冲区（MB）<br><br>14个消息缓冲区（MB）</td>
</tr>
<tr>
<td>flexcan1</td>
<td>8字节<br><br>16字节<br><br>32字节<br><br>64字节</td>
<td>64个消息缓冲区（MB）<br><br>42个消息缓冲区（MB）<br><br>24个消息缓冲区（MB）<br><br>14个消息缓冲区（MB）</td>
<td>64个消息缓冲区（MB）<br><br>42个消息缓冲区（MB）<br><br>24个消息缓冲区（MB）<br><br>14个消息缓冲区（MB）</td>
</tr>
<tr>
<td>flexcan2</td>
<td>8字节<br><br>16字节<br><br>32字节<br><br>64字节</td>
<td>64个消息缓冲区（MB）<br><br>42个消息缓冲区（MB）<br><br>24个消息缓冲区（MB）<br><br>14个消息缓冲区（MB）</td>
<td>64个消息缓冲区（MB）<br><br>42个消息缓冲区（MB）<br><br>24个消息缓冲区（MB）<br><br>14个消息缓冲区（MB）</td>
</tr>
<tr>
<td>flexcan3</td>
<td>8字节<br><br>16字节<br><br>32字节<br><br>64字节</td>
<td>32个消息缓冲区（MB）<br><br>21个消息缓冲区（MB）<br><br>12个消息缓冲区（MB）<br><br>7个消息缓冲区（MB）</td>
<td>32个消息缓冲区（MB）<br><br>21个消息缓冲区（MB）<br><br>12个消息缓冲区（MB）<br><br>7个消息缓冲区（MB）</td>
</tr>
<tr>
<td>flexcan4</td>
<td>8字节<br><br>16字节<br><br>32字节<br><br>64字节</td>
<td>32个消息缓冲区（MB）<br><br>21个消息缓冲区（MB）<br><br>12个消息缓冲区（MB）<br><br>7个消息缓冲区（MB）</td>
<td>32个消息缓冲区（MB）<br><br>21个消息缓冲区（MB）<br><br>12个消息缓冲区（MB）<br><br>7个消息缓冲区（MB）</td>
</tr>
<tr>
<td>flexcan5</td>
<td>8字节<br><br>16字节<br><br>32字节<br><br>64字节</td>
<td>32个消息缓冲区（MB）<br><br>21个消息缓冲区（MB）<br><br>12个消息缓冲区（MB）<br><br>7个消息缓冲区（MB）</td>
<td>32个消息缓冲区（MB）<br><br>21个消息缓冲区（MB）<br><br>12个消息缓冲区（MB）<br><br>7个消息缓冲区（MB）</td>
</tr>
</table>

注意（Note）

<a id="id19"></a>

CAN总线通常需要在两端各接120 Ω终端电阻，可使用随附的CAN终端板实现。更多细节见[NXP MR-CANHUBK3](https://www.nxp.com/design/development-boards/automotive-development-platforms/s32k-mcu-platforms/s32k344-evaluation-board-for-mobile-robotics-incorporating-100baset1-and-six-can-fd:MR-CANHUBK344) [注8](#id16)硬件用户手册第6.3节“CAN连接器”。

<a id="i2c"></a>

### 集成电路间总线（I2C）

I2C通过LPI2C接口提供，lpi2c0及lpi2c1分别位于连接器P4及P3。

<table>
<tr>
<th>连接器（Connector）</th>
<th>引脚（Pin）</th>
<th>引脚功能（Pin Function）</th>
</tr>
<tr>
<td>P3.2</td>
<td>PTD9</td>
<td>LPI2C1_SCL</td>
</tr>
<tr>
<td>P3.3</td>
<td>PTD8</td>
<td>LPI2C1_SDA</td>
</tr>
<tr>
<td>P4.3</td>
<td>PTD14</td>
<td>LPI2C0_SCL</td>
</tr>
<tr>
<td>P4.4</td>
<td>PTD13</td>
<td>LPI2C0_SDA</td>
</tr>
</table>

配套显示板可通过P4连接lpi2c0。

<a id="adc"></a>

### 模数转换器（ADC）

ADC通过3个SAR ADC控制器实例提供，通道分为精密（Precision）、标准（Standard）及外部（External）3组。

注意（Note）

同一实例的所有通道在同一时刻只能使用一个通道组。

<a id="fs26-sbc-watchdog"></a>

### FS26系统基础芯片看门狗（SBC Watchdog）

正常上电后，必须在256 ms窗口内用有效令牌刷新FS26看门狗，否则看门狗会向MCU发出复位信号。此开发板配置启用FS26看门狗驱动，由该驱动完成初始化。

注意（Note）

也可按以下步骤使FS26进入调试模式，此时看门狗禁用：


1. 给开发板断电。
2. 拔下默认连接的JP1跳线帽，使1—2脚断开。
3. 给开发板上电。
4. 重新连接JP1，使1—2脚短接。

<a id="external-flash"></a>

### 外部闪存（External Flash）

板载MX25L6433F是64 Mbit多I/O串行NOR闪存，连接QSPI控制器A1端口。开发板配置将其选为默认闪存控制器。

<a id="ethernet"></a>

### 以太网（Ethernet）

<a id="id25"></a>

此板有一个以太网媒体访问控制器（EMAC），连接[NXP TJA1103](https://www.nxp.com/products/interfaces/ethernet-/automotive-ethernet-phys/asil-b-compliant-100base-t1-ethernet-phy:TJA1103) [注11](#id24) 100Base-T1以太网PHY。当前PHY驱动功能有限，可将引脚绑带（Pin Strapping）的默认配置，即RMII、主机、启用自主模式及极性校正，覆盖为从机模式。

<a id="id27"></a>

100Base-T1信号位于P9，可通过[RDDRONE-T1ADAPT](https://www.nxp.com/products/interfaces/ethernet-/automotive-ethernet-phys/ethernet-media-converter-for-drones-rovers-mobile-robotics-and-automotive:RDDRONE-T1ADAPT) [注12](#id26)等以太网介质转换器转换成100Base-T。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`mr_canhubk3`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-trace32">trace32</a></td>
<td>✅</td>
<td>✅</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

mr_canhubk3应用可按“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）中的常规方法构建。

<a id="id29"></a>

<a id="id31"></a>

<a id="id33"></a>

此板支持[Lauterbach TRACE32](https://www.lauterbach.com) [注13](#id28)、[SEGGER J-Link](https://wiki.segger.com/NXP_S32K3xx) [注14](#id30)及[pyOCD](https://pyocd.io/) [注15](#id32)运行工具，用于烧录和调试。主机工具安装方法分别见对应的调试主机工具（Debug Host Tools）说明，默认运行工具为J-Link。（[Lauterbach TRACE32调试主机工具](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#lauterbach-trace32-debug-host-tools)；[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)；[pyOCD调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#pyocd-debug-host-tools)）

使用TRACE32时，确保版本不低于2024.09。

<a id="flashing"></a>

### 烧录（Flashing）

运行west flash，通过SEGGER J-Link烧录应用；也可用west flash -r trace32选择Lauterbach TRACE32，或west flash -r pyocd选择pyOCD。

Lauterbach TRACE32运行工具还支持从命令行传入以下附加选项：

```text
west flash -r trace32 --startup-args elfFile=<elf_path> loadTo=<flash/sram>
   eraseFlash=<yes/no> verifyFlash=<yes/no>
```

其中：


- `<elf_path>`为输出目录中Zephyr应用ELF文件的路径。
- loadTo=flash将应用加载到SoC内部程序闪存，要求设置[CONFIG_XIP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XIP)；loadTo=sram将应用加载到SRAM。默认值为flash。
- eraseFlash=yes在将应用下载到闪存或SRAM之前，擦除SoC内部闪存的全部内容，此操作需要一定时间。默认值为no。
- verifyFlash=yes在编程后核验SoC内部闪存内容，应与loadTo=flash配合使用。默认值为no。

例如，要擦除并核验闪存内容：

```text
west flash -r trace32 --startup-args elfFile=build/zephyr/zephyr.elf loadTo=flash eraseFlash=yes verifyFlash=yes
```

<a id="mcuboot"></a>

### MCUboot

此板支持使用MCUboot链式加载应用（Application Chain-loading）。

<a id="build-flash"></a>

#### 构建与烧录（Build & Flash）

要同时构建MCUboot及flash_shell示例，并生成可供烧录的HEX文件，运行：

```text
west build -p -b mr_canhubk3/s32k344/mcuboot samples/drivers/flash_shell --sysbuild
west flash
```

生成的构建产物为：


- MCUboot：build/mcuboot/zephyr/zephyr.hex
- 应用，未签名：build/flash_shell/zephyr/zephyr.hex

<a id="troubleshooting"></a>

#### 故障排查（Troubleshooting）

> 若MCUboot输出“Image in the primary slot is not valid”（主槽中的镜像无效），或停在“Jumping to the first image slot”（跳转到第一个镜像槽）之后，应用可能使用了512字节头部签名。请使用--header-size 0x400重新签名并烧录。
>
> 不要为由MCUboot链式加载的应用添加IVT；IVT只为独立／XIP镜像或MCUboot自身生成。

<a id="debugging"></a>

### 调试（Debugging）

运行west debug，通过SEGGER J-Link启动GDB会话；也可运行west debug -r trace32或west debug -r pyocd，分别启动Lauterbach TRACE32或pyOCD调试界面。

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- <a id="id3"></a>

  [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)[注1](#id2)
- <a id="id5"></a>

  [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)[注2](#id4)
- <a id="id7"></a>

  <a id="id9"></a>

  [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode) [注3](#id6)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html) [注4](#id8)
- <a id="id11"></a>

  [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)[注5](#id10)
- <a id="id13"></a>

  [NXP的Zephyr专题页面](https://nxp.com/zephyr) [注6](#id12)，含培训资源
- <a id="id15"></a>

  NXP Zephyr支持社区论坛 [注7](#id14)（[NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)）

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)

<a id="id4"></a>

〔[2](#id5)〕 [https://github.com/nxp-zephyr/nxp-zsdk](https://github.com/nxp-zephyr/nxp-zsdk)

<a id="id6"></a>

〔[3](#id7)〕 [https://mcuxpresso.nxp.com/mcux-vscode](https://mcuxpresso.nxp.com/mcux-vscode)

<a id="id8"></a>

〔[4](#id9)〕 [https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)

<a id="id10"></a>

〔[5](#id11)〕 [https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)

<a id="id12"></a>

〔[6](#id13)〕 [https://nxp.com/zephyr](https://nxp.com/zephyr)

<a id="id14"></a>

〔[7](#id15)〕 [https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

<a id="id16"></a>

〔8〕 ([1](#id17),[2](#id18),[3](#id19)) [https://www.nxp.com/design/development-boards/automotive-development-platforms/s32k-mcu-platforms/s32k344-evaluation-board-for-mobile-robotics-incorporating-100baset1-and-six-can-fd:MR-CANHUBK344](https://www.nxp.com/design/development-boards/automotive-development-platforms/s32k-mcu-platforms/s32k344-evaluation-board-for-mobile-robotics-incorporating-100baset1-and-six-can-fd:MR-CANHUBK344)

<a id="id20"></a>

〔[9](#id21)〕 [https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k3-microcontrollers-for-automotive-general-purpose:S32K3](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k3-microcontrollers-for-automotive-general-purpose:S32K3)

<a id="id22"></a>

〔[10](#id23)〕 [https://www.nxp.com/products/power-management/pmics-and-sbcs/safety-sbcs/safety-system-basis-chip-with-low-power-fit-for-asil-d:FS26](https://www.nxp.com/products/power-management/pmics-and-sbcs/safety-sbcs/safety-system-basis-chip-with-low-power-fit-for-asil-d:FS26)

<a id="id24"></a>

〔[11](#id25)〕 [https://www.nxp.com/products/interfaces/ethernet-/automotive-ethernet-phys/asil-b-compliant-100base-t1-ethernet-phy:TJA1103](https://www.nxp.com/products/interfaces/ethernet-/automotive-ethernet-phys/asil-b-compliant-100base-t1-ethernet-phy:TJA1103)

<a id="id26"></a>

〔[12](#id27)〕 [https://www.nxp.com/products/interfaces/ethernet-/automotive-ethernet-phys/ethernet-media-converter-for-drones-rovers-mobile-robotics-and-automotive:RDDRONE-T1ADAPT](https://www.nxp.com/products/interfaces/ethernet-/automotive-ethernet-phys/ethernet-media-converter-for-drones-rovers-mobile-robotics-and-automotive:RDDRONE-T1ADAPT)

<a id="id28"></a>

〔[13](#id29)〕 [https://www.lauterbach.com](https://www.lauterbach.com)

<a id="id30"></a>

〔[14](#id31)〕 [https://wiki.segger.com/NXP_S32K3xx](https://wiki.segger.com/NXP_S32K3xx)

<a id="id32"></a>

〔[15](#id33)〕 [https://pyocd.io/](https://pyocd.io/)

## 译注

WKPU仅用作中断控制器，不支持唤醒及电源管理；CAN缓冲区受HAL限制。FS26上电后256 ms刷新窗口、QSPI默认闪存、T1以太网模式及MCUboot头部0x400要求均保留。原文两个用户按键均使用sw0别名，表格照录；不在译文擅自改动。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [s32k344-evaluation-board-for-mobile-robotics-incorporating-100baset1-and-six-can-fd:MR-CANHUBK344](https://www.nxp.com/design/development-boards/automotive-development-platforms/s32k-mcu-platforms/s32k344-evaluation-board-for-mobile-robotics-incorporating-100baset1-and-six-can-fd:MR-CANHUBK344)：HTTP Error 404: Not Found。
- [asil-b-compliant-100base-t1-ethernet-phy:TJA1103](https://www.nxp.com/products/interfaces/ethernet-/automotive-ethernet-phys/asil-b-compliant-100base-t1-ethernet-phy:TJA1103)：HTTP Error 404: Not Found。
- [ethernet-media-converter-for-drones-rovers-mobile-robotics-and-automotive:RDDRONE-T1ADAPT](https://www.nxp.com/products/interfaces/ethernet-/automotive-ethernet-phys/ethernet-media-converter-for-drones-rovers-mobile-robotics-and-automotive:RDDRONE-T1ADAPT)：HTTP Error 404: Not Found。
- [safety-system-basis-chip-with-low-power-fit-for-asil-d:FS26](https://www.nxp.com/products/power-management/pmics-and-sbcs/safety-sbcs/safety-system-basis-chip-with-low-power-fit-for-asil-d:FS26)：HTTP Error 404: Not Found。
- [s32k3-microcontrollers-for-automotive-general-purpose:S32K3](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k3-microcontrollers-for-automotive-general-purpose:S32K3)：HTTP Error 404: Not Found。

---

[上一章](P005_MCXW72-EVK.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_MR-MCXN-T1.md)
