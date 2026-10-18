---
id: learning.zephyr-docs.boards-nxp-remaining.page-12
title: S32K5XXCVB
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/s32k5xxcvb/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="s32k5xxcvb"></a>

# 第12章\_S32K5XXCVB

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/s32k5xxcvb/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`s32k5xxcvb`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[s32k566](https://docs.zephyrproject.org/latest/boards/index.html#soc=s32k566)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/s32k5xxcvb/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id16"></a>

NXP S32K5XXCVB基于[NXP S32K5系列](https://www.nxp.com/products/S32K5)[注8](#id15)汽车微控制器。该系列在S32K3基础上扩展，以更低功耗提供更高性能、更大内存及更强的车载网络通信能力。

S32K5 MCU包含：侧重计算的Arm Cortex-R52核、侧重平台功能的Arm Cortex-M7核，以及侧重低功耗的Arm Cortex-M4核。

Zephyr操作系统已移植到Cortex-M7及Cortex-R52核。


- s32k5xxcvb/s32k566/m7用于S32K566 Cortex-M7，默认从代码磁阻RAM（Code MRAM）执行。
- s32k5xxcvb/s32k566/r52用于S32K566 Cortex-R52，默认从代码MRAM执行。

<a id="hardware"></a>

## 硬件（Hardware）


- NXP S32K566


  - Arm Cortex-M7共6核，两种配置为3组锁步，或2组锁步加2个独立核；默认采用第二种。
  - Arm Cortex-R52：一个包含两个Cortex-R52核的R52集群
  - Cortex-M7使用1.5 MB SRAM，带ECC
  - Cortex-R52连接1 MB SRAM，带ECC
  - 所有内核共用32 MB代码磁性RAM（Code Magnetic RAM），带ECC
  - 集成以太网交换机、CAN FD／XL及QSPI
  - 14位、3 Msps ADC，24位eMIOS定时器等

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`s32k5xxcvb`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="s32k5xxcvb-hw-features"></a>

<a id="s32k5xxcvb-s32k5xxcvb/s32k566/m7-hw-features-section"></a>

#### `s32k5xxcvb/s32k566/m7`目标（Target）

<a id="s32k5xxcvb-s32k5xxcvb/s32k566/m7-hw-features-panel"></a>

<a id="s32k5xxcvb-s32k5xxcvb/s32k566/m7-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、32 MiB Flash。

<a id="s32k5xxcvb-s32k5xxcvb/s32k566/m7-hw-features-table"></a>

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
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566_m7.dtsi?plain=1#L16">已启用：4</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP S32逐次逼近型模数转换器（SAR ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L787">已禁用：3</a>）</td>
<td><a href="../hardware/P853_NXPS32逐次逼近ADC绑定.md#dtbinding-nxp-s32-adc-sar"><code>nxp,s32-adc-sar</code></a></td>
</tr>
<tr>
<td rowspan="2">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L703">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L550">已禁用：17</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32 CANXL控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L970">已禁用：1</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P002_nxp_s32-canxl.md#std-dtcompatible-nxp-s32-canxl"><code>nxp,s32-canxl</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP S32时钟发生器IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L38">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P014_nxp_s32-clock.md#std-dtcompatible-nxp-s32-clock"><code>nxp,s32-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP S32系统定时器模块（STM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566_m7.dtsi?plain=1#L48">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P018_nxp_s32-sys-timer.md#std-dtcompatible-nxp-s32-sys-timer"><code>nxp,s32-sys-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP周期中断定时器（PIT / Periodic Interrupt Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566_m7.dtsi?plain=1#L80">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P017_nxp_pit.md#std-dtcompatible-nxp-pit"><code>nxp,pit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>周期中断定时器节点的子节点，用于表示单个定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566_m7.dtsi?plain=1#L90">已禁用：16</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P016_nxp_pit-channel.md#std-dtcompatible-nxp-pit-channel"><code>nxp,pit-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L1066">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>NXP SIUL2 GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L166">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L82">已禁用：13</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P028_nxp_siul2-gpio.md#std-dtcompatible-nxp-siul2-gpio"><code>nxp,siul2-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L711">已禁用：5</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32k5xxcvb/s32k5xxcvb_s32k566.dtsi?plain=1#L45">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SIUL2外部中断请求控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L157">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L73">已禁用：4</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P006_nxp_siul2-eirq.md#std-dtcompatible-nxp-siul2-eirq"><code>nxp,siul2-eirq</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32k5xxcvb/s32k5xxcvb_s32k566.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>用于NXP S32 SoC的增强型模块化I/O子系统（eMIOS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L808">已禁用：3</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P007_nxp_s32-emios.md#std-dtcompatible-nxp-s32-emios"><code>nxp,s32-emios</code></a></td>
</tr>
<tr>
<td rowspan="3">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>连接NXP S32 XSPI总线的XSPI HyperRAM（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32k5xxcvb/s32k5xxcvb_s32k566.dtsi?plain=1#L148">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P007_nxp_s32-xspi-hyperram.md#std-dtcompatible-nxp-s32-xspi-hyperram"><code>nxp,s32-xspi-hyperram</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存或其他非易失性存储器的固定分区（Fixed Partitions）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32k5xxcvb/s32k5xxcvb_s32k566.dtsi?plain=1#L162">已启用：1</a>）</td>
<td><a href="../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions"><code>fixed-partitions</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>用于S32K5 SoC的NXP S32引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L58">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P020_nxp_s32k5-pinctrl.md#std-dtcompatible-nxp-s32k5-pinctrl"><code>nxp,s32k5-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>NXP S32模块进入控制（MC_ME / Module Entry）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L63">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P017_nxp_s32-mc-me.md#std-dtcompatible-nxp-s32-mc-me"><code>nxp,s32-mc-me</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexTimer模块（FTM）PWM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L762">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P004_nxp_ftm-pwm.md#std-dtcompatible-nxp-ftm-pwm"><code>nxp,ftm-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>用于S32 SoC的NXP S32 eMIOS脉宽调制（PWM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L855">已禁用：3</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P011_nxp_s32-emios-pwm.md#std-dtcompatible-nxp-s32-emios-pwm"><code>nxp,s32-emios-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L376">已禁用：25</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L978">已禁用：8</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L12">已启用：4</a>）</td>
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
<td>软件看门狗定时器（SWT / Software Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L779">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L771">已禁用：5</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P013_nxp_s32-swt.md#std-dtcompatible-nxp-s32-swt"><code>nxp,s32-swt</code></a></td>
</tr>
<tr>
<td rowspan="3">扩展串行外设接口（xSPI）</td>
<td>片上（On-Chip）</td>
<td>NXP S32扩展串行外设接口（XSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L754">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P014_nxp_s32-xspi.md#std-dtcompatible-nxp-s32-xspi"><code>nxp,s32-xspi</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP S32扩展串行外设接口（XSPI）安全闪存保护（SFP）MDAD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32k5xxcvb/s32k5xxcvb_s32k566.dtsi?plain=1#L125">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P013_nxp_s32-xspi-sfp-mdad.md#std-dtcompatible-nxp-s32-xspi-sfp-mdad"><code>nxp,s32-xspi-sfp-mdad</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP S32扩展串行外设接口（XSPI）安全闪存保护（SFP）FRAD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32k5xxcvb/s32k5xxcvb_s32k566.dtsi?plain=1#L134">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P012_nxp_s32-xspi-sfp-frad.md#std-dtcompatible-nxp-s32-xspi-sfp-frad"><code>nxp,s32-xspi-sfp-frad</code></a></td>
</tr>
</table>

<a id="s32k5xxcvb-s32k5xxcvb/s32k566/r52-hw-features-section"></a>

#### `s32k5xxcvb/s32k566/r52`目标（Target）

<a id="s32k5xxcvb-s32k5xxcvb/s32k566/r52-hw-features-panel"></a>

<a id="s32k5xxcvb-s32k5xxcvb/s32k566/r52-hw-features-memory"></a>

该开发板目标的片上存储容量：1 MiB RAM、32 MiB Flash。

<a id="s32k5xxcvb-s32k5xxcvb/s32k566/r52-hw-features-table"></a>

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
<td>ARM Cortex-R52处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566_r52.dtsi?plain=1#L16">已启用：2</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P011_arm_cortex-r52.md#std-dtcompatible-arm-cortex-r52"><code>arm,cortex-r52</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP S32逐次逼近型模数转换器（SAR ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L787">已禁用：3</a>）</td>
<td><a href="../hardware/P853_NXPS32逐次逼近ADC绑定.md#dtbinding-nxp-s32-adc-sar"><code>nxp,s32-adc-sar</code></a></td>
</tr>
<tr>
<td rowspan="2">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L703">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L550">已禁用：17</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32 CANXL控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L970">已禁用：1</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P002_nxp_s32-canxl.md#std-dtcompatible-nxp-s32-canxl"><code>nxp,s32-canxl</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP S32时钟发生器IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L38">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P014_nxp_s32-clock.md#std-dtcompatible-nxp-s32-clock"><code>nxp,s32-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP S32系统定时器模块（STM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566_r52.dtsi?plain=1#L52">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P018_nxp_s32-sys-timer.md#std-dtcompatible-nxp-s32-sys-timer"><code>nxp,s32-sys-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP周期中断定时器（PIT / Periodic Interrupt Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566_r52.dtsi?plain=1#L68">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P017_nxp_pit.md#std-dtcompatible-nxp-pit"><code>nxp,pit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>周期中断定时器节点的子节点，用于表示单个定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566_r52.dtsi?plain=1#L77">已禁用：8</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P016_nxp_pit-channel.md#std-dtcompatible-nxp-pit-channel"><code>nxp,pit-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L1066">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>NXP SIUL2 GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L166">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L82">已禁用：13</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P028_nxp_siul2-gpio.md#std-dtcompatible-nxp-siul2-gpio"><code>nxp,siul2-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L711">已禁用：5</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32k5xxcvb/s32k5xxcvb_s32k566.dtsi?plain=1#L45">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP SIUL2外部中断请求控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L157">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L73">已禁用：4</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P006_nxp_siul2-eirq.md#std-dtcompatible-nxp-siul2-eirq"><code>nxp,siul2-eirq</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566_r52.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32k5xxcvb/s32k5xxcvb_s32k566.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>用于NXP S32 SoC的增强型模块化I/O子系统（eMIOS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L808">已禁用：3</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P007_nxp_s32-emios.md#std-dtcompatible-nxp-s32-emios"><code>nxp,s32-emios</code></a></td>
</tr>
<tr>
<td rowspan="3">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>连接NXP S32 XSPI总线的XSPI HyperRAM（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32k5xxcvb/s32k5xxcvb_s32k566.dtsi?plain=1#L148">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P007_nxp_s32-xspi-hyperram.md#std-dtcompatible-nxp-s32-xspi-hyperram"><code>nxp,s32-xspi-hyperram</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存或其他非易失性存储器的固定分区（Fixed Partitions）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32k5xxcvb/s32k5xxcvb_s32k566.dtsi?plain=1#L162">已启用：1</a>）</td>
<td><a href="../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions"><code>fixed-partitions</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>用于S32K5 SoC的NXP S32引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L58">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P020_nxp_s32k5-pinctrl.md#std-dtcompatible-nxp-s32k5-pinctrl"><code>nxp,s32k5-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>NXP S32模块进入控制（MC_ME / Module Entry）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L63">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P017_nxp_s32-mc-me.md#std-dtcompatible-nxp-s32-mc-me"><code>nxp,s32-mc-me</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexTimer模块（FTM）PWM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L762">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P004_nxp_ftm-pwm.md#std-dtcompatible-nxp-ftm-pwm"><code>nxp,ftm-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>用于S32 SoC的NXP S32 eMIOS脉宽调制（PWM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L855">已禁用：3</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P011_nxp_s32-emios-pwm.md#std-dtcompatible-nxp-s32-emios-pwm"><code>nxp,s32-emios-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L376">已禁用：25</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L978">已禁用：8</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L12">已启用：4</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566_r52.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>软件看门狗定时器（SWT / Software Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L779">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L771">已禁用：3</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P013_nxp_s32-swt.md#std-dtcompatible-nxp-s32-swt"><code>nxp,s32-swt</code></a></td>
</tr>
<tr>
<td rowspan="3">扩展串行外设接口（xSPI）</td>
<td>片上（On-Chip）</td>
<td>NXP S32扩展串行外设接口（XSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32k566.dtsi?plain=1#L754">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P014_nxp_s32-xspi.md#std-dtcompatible-nxp-s32-xspi"><code>nxp,s32-xspi</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP S32扩展串行外设接口（XSPI）安全闪存保护（SFP）MDAD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32k5xxcvb/s32k5xxcvb_s32k566.dtsi?plain=1#L125">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P013_nxp_s32-xspi-sfp-mdad.md#std-dtcompatible-nxp-s32-xspi-sfp-mdad"><code>nxp,s32-xspi-sfp-mdad</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP S32扩展串行外设接口（XSPI）安全闪存保护（SFP）FRAD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32k5xxcvb/s32k5xxcvb_s32k566.dtsi?plain=1#L134">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P012_nxp_s32-xspi-sfp-frad.md#std-dtcompatible-nxp-s32-xspi-sfp-frad"><code>nxp,s32-xspi-sfp-frad</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

参考手册（RM）的Port列在本Zephyr移植中组织为端口和引脚，以保持与GPIO驱动一致。

下表汇总参考手册Port列到Zephyr端口／引脚的映射。使用GPIO驱动或为设备驱动配置引脚复用时，需采用此映射。

<table>
<tr>
<th>参考手册中的端口（Ports in RM）</th>
<th>Zephyr端口／引脚（Ports/Pins）</th>
</tr>
<tr>
<td>GPIO0 - GPIO15</td>
<td>PA0 - PA15</td>
</tr>
<tr>
<td>GPIO16 - GPIO31</td>
<td>PB0 - PB15</td>
</tr>
<tr>
<td>GPIO32 - GPIO47</td>
<td>PC0 - PC15</td>
</tr>
<tr>
<td>GPIO48 - GPIO63</td>
<td>PD0 - PD15</td>
</tr>
<tr>
<td>GPIO64 - GPIO78</td>
<td>PE0 - PE14</td>
</tr>
<tr>
<td>GPIO80 - GPIO95</td>
<td>PF0 - PF15</td>
</tr>
<tr>
<td>GPIO96 - GPIO111</td>
<td>PG0 - PG15</td>
</tr>
<tr>
<td>GPIO112 - GPIO127</td>
<td>PH0 - PH15</td>
</tr>
<tr>
<td>GPIO128 - GPIO138</td>
<td>PI0 - PI10</td>
</tr>
<tr>
<td>GPIO160 - GPIO175</td>
<td>PK0 - PK15</td>
</tr>
<tr>
<td>GPIO176 - GPIO191</td>
<td>PL0 - PL15</td>
</tr>
<tr>
<td>GPIO192 - GPIO207</td>
<td>PM0 - PM15</td>
</tr>
<tr>
<td>GPIO208 - GPIO223</td>
<td>PN0 - PN15</td>
</tr>
<tr>
<td>GPIO224 - GPIO239</td>
<td>PO0 - PO15</td>
</tr>
<tr>
<td>GPIO240 - GPIO254</td>
<td>PP0 - PP14</td>
</tr>
<tr>
<td>GPIO256 - GPIO263</td>
<td>PQ0 - PQ7</td>
</tr>
<tr>
<td>GPIO304 - GPIO319</td>
<td>PT0 - PT15</td>
</tr>
<tr>
<td>GPIO320 - GPIO335</td>
<td>PU0 - PU15</td>
</tr>
<tr>
<td>GPIO336 - GPIO351</td>
<td>PV0 - PV15</td>
</tr>
<tr>
<td>GPIO352 - GPIO363</td>
<td>PW0 - PW11</td>
</tr>
</table>

<a id="leds"></a>

#### 发光二极管（LEDs）

此板有3个用户RGB LED，数量描述按原文保留：

<table>
<tr>
<th>设备树节点（Devicetree Node）</th>
<th>颜色（Color）</th>
<th>引脚（Pin）</th>
</tr>
<tr>
<td>led0 / user_led_red</td>
<td>红色（Red）</td>
<td>PP1</td>
</tr>
<tr>
<td>led1 / user_led_green</td>
<td>绿色（Green）</td>
<td>PO2</td>
</tr>
<tr>
<td>led2 / user_led_blue</td>
<td>蓝色（Blue）</td>
<td>PN10</td>
</tr>
</table>

用户可自行控制LED，输出1时LED亮起。

<a id="buttons"></a>

#### 按键（Buttons）

此板有两个用户按键：

<table>
<tr>
<th>设备树节点（Devicetree Node）</th>
<th>标签（Label）</th>
<th>引脚（Pin）</th>
</tr>
<tr>
<td>sw0 / user_button_0</td>
<td>USERSW0</td>
<td>PF3</td>
</tr>
<tr>
<td>sw1 / user_button_1</td>
<td>USERSW1</td>
<td>PF9</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）


- Arm Cortex-M7：200 MHz。
- Arm Cortex-R52：800 MHz。

<a id="set-up-the-board"></a>

### 设置开发板（Set-up the Board）

把外部调试探针连接到开发板JTAG Cortex ETM连接器J17，并根据探针能力，通过USB或以太网连接主机。

<a id="nxp-s32k5xx-mb-shield"></a>

### NXP S32K5XX-MB扩展板（Shield）

Zephyr的NXP S32K5XX-MB扩展板配置可扩展此板的I/O连接能力。（[NXP S32K5XX-MB扩展板（Shield）](https://docs.zephyrproject.org/latest/boards/shields/nxp_s32k5xx_mb/doc/index.html#nxp-s32k5xx-mb)）

此扩展板提供串行UART接口。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`s32k5xxcvb`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-trace32">trace32</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
</tr>
</table>

s32k5xxcvb应用可按“构建应用”中的常规方法构建。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)）

此板支持以下调试工具对应的west运行工具：


- [Lauterbach TRACE32](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#lauterbach-trace32-debug-host-tools)

加载固件前，请先按所选调试工具的安装步骤完成设置。

<a id="debugging"></a>

### 调试（Debugging）

可按以下方式为s32k5xxcvb/s32k566/m7构建并调试[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例：

```text
# From the root of the zephyr repository
west build -b s32k5xxcvb/s32k566/m7 samples/hello_world
west debug
```

<a id="flashing"></a>

### 烧录（Flashing）

若只需将应用下载到开发板并运行，按以下步骤操作。

```text
west build -b s32k5xxcvb/s32k566/m7 samples/hello_world
west flash
```

<a id="core-selection"></a>

### 核选择（Core Selection）

此Zephyr移植只能以单核运行，默认使用所选开发板目标的第一个核。若要在其他核上执行应用，必须从命令行覆盖全部运行工具参数：

```text
west <debug/flash> --startup-args elfFile=<elf_path> coreType=<m7/r52> loadTo=<mram/sram> core=<core_id>
```

`<elf_path>`为输出目录中Zephyr应用ELF文件的路径。

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- <a id="id2"></a>

  [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)[注1](#id1)
- <a id="id4"></a>

  [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)[注2](#id3)
- <a id="id6"></a>

  <a id="id8"></a>

  [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode) [注3](#id5)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html) [注4](#id7)
- <a id="id10"></a>

  [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)[注5](#id9)
- <a id="id12"></a>

  [NXP的Zephyr专题页面](https://nxp.com/zephyr) [注6](#id11)，含培训资源
- <a id="id14"></a>

  NXP Zephyr支持社区论坛 [注7](#id13)（[NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)）

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)

<a id="id3"></a>

〔[2](#id4)〕 [https://github.com/nxp-zephyr/nxp-zsdk](https://github.com/nxp-zephyr/nxp-zsdk)

<a id="id5"></a>

〔[3](#id6)〕 [https://mcuxpresso.nxp.com/mcux-vscode](https://mcuxpresso.nxp.com/mcux-vscode)

<a id="id7"></a>

〔[4](#id8)〕 [https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)

<a id="id9"></a>

〔[5](#id10)〕 [https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)

<a id="id11"></a>

〔[6](#id12)〕 [https://nxp.com/zephyr](https://nxp.com/zephyr)

<a id="id13"></a>

〔[7](#id14)〕 [https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

<a id="id15"></a>

〔[8](#id16)〕 [https://www.nxp.com/products/S32K5](https://www.nxp.com/products/S32K5)

## 译注

S32K566的M7及R52均默认从代码MRAM执行，当前移植只支持单核。参考手册GPIO编号到Zephyr端口的映射含编号缺口，按原表保留；非默认核调试需覆盖全部运行工具参数。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [S32K5](https://www.nxp.com/products/S32K5)：HTTP Error 404: Not Found。

---

[上一章](P011_S32K148EVB-Q176.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_X-S32Z27X-DC_DC2.md)
