---
id: learning.zephyr-docs.boards-nxp-remaining.page-13
title: X-S32Z27X-DC DC2
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/s32z2xxdc2/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="s32z2xxdc2"></a>

# 第13章\_X-S32Z27X-DC (DC2)

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/s32z2xxdc2/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`s32z2xxdc2`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[s32z270](https://docs.zephyrproject.org/latest/boards/index.html#soc=s32z270)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/s32z2xxdc2/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

X-S32Z27X-DC（DC2）基于NXP S32Z2实时处理器，其包含两个实时单元（Real-Time Unit，RTU），每个RTU有4个Arm Cortex-R52核，可灵活配置分离／锁步（Split/Lock）模式。

每个SoC／RTU组合对应一个Zephyr开发板目标：


- s32z2xxdc2/s32z270/rtu0，对应S32Z270／RTU0
- s32z2xxdc2/s32z270/rtu1，对应S32Z270／RTU1

<a id="hardware"></a>

## 硬件（Hardware）

<a id="id16"></a>

硬件及设计资源信息见[NXP S32Z2实时处理器网站](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32z-and-s32e-real-time-processors/s32z2-safe-and-secure-high-performance-real-time-processors:S32Z2)[注8](#id15)。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`s32z2xxdc2`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="s32z2xxdc2-hw-features"></a>

<a id="s32z2xxdc2-s32z2xxdc2@B/s32z270/rtu0-hw-features-section"></a>

#### `s32z2xxdc2@B/s32z270/rtu0`目标（Target）

<a id="s32z2xxdc2-s32z2xxdc2@B/s32z270/rtu0-hw-features-panel"></a>

<a id="s32z2xxdc2-s32z2xxdc2@B/s32z270/rtu0-hw-features-memory"></a>

该开发板目标的片上存储容量：1 MiB RAM、7 MiB Flash。

<a id="s32z2xxdc2-s32z2xxdc2@B/s32z270/rtu0-hw-features-table"></a>

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
<td>ARM Cortex-R52处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L19">已启用：4</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P011_arm_cortex-r52.md#std-dtcompatible-arm-cortex-r52"><code>arm,cortex-r52</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP S32逐次逼近型模数转换器（SAR ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1107">已禁用：2</a>）</td>
<td><a href="../hardware/P853_NXPS32逐次逼近ADC绑定.md#dtbinding-nxp-s32-adc-sar"><code>nxp,s32-adc-sar</code></a></td>
</tr>
<tr>
<td rowspan="2">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 CANXL控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L719">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L733">已禁用：1</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P002_nxp_s32-canxl.md#std-dtcompatible-nxp-s32-canxl"><code>nxp,s32-canxl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L747">已禁用：24</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP S32时钟发生器IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L86">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P014_nxp_s32-clock.md#std-dtcompatible-nxp-s32-clock"><code>nxp,s32-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP S32系统定时器模块（STM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L24">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P018_nxp_s32-sys-timer.md#std-dtcompatible-nxp-s32-sys-timer"><code>nxp,s32-sys-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP周期中断定时器（PIT / Periodic Interrupt Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L101">已禁用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P017_nxp_pit.md#std-dtcompatible-nxp-pit"><code>nxp,pit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>周期中断定时器节点的子节点，用于表示单个定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L111">已禁用：6</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P016_nxp_pit-channel.md#std-dtcompatible-nxp-pit-channel"><code>nxp,pit-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>NXP S32硬件安全引擎（HSE）消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1901">已禁用：8</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P005_nxp_s32-crypto-hse-mu.md#std-dtcompatible-nxp-s32-crypto-hse-mu"><code>nxp,s32-crypto-hse-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1149">已禁用：4</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 NETC外部管理数据输入输出（MDIO）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L662">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P004_nxp_s32-netc-emdio.md#std-dtcompatible-nxp-s32-netc-emdio"><code>nxp,s32-netc-emdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32 NETC物理站点接口（PSI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L670">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P011_nxp_s32-netc-psi.md#std-dtcompatible-nxp-s32-netc-psi"><code>nxp,s32-netc-psi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32 NETC虚拟站点接口（VSI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L676">已禁用：7</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P012_nxp_s32-netc-vsi.md#std-dtcompatible-nxp-s32-netc-vsi"><code>nxp,s32-netc-vsi</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>NXP SIUL2 GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L244">已禁用：15</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P028_nxp_siul2-gpio.md#std-dtcompatible-nxp-siul2-gpio"><code>nxp,siul2-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1127">已禁用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L105">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SIUL2外部中断请求控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L234">已禁用：4</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P006_nxp_siul2-eirq.md#std-dtcompatible-nxp-siul2-eirq"><code>nxp,siul2-eirq</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>NXP S32消息接收单元（Message Receive Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L592">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L600">已禁用：7</a>）</td>
<td><a href="../intercore_reference/P049_NXPS32消息接收单元绑定.md#dtbinding-nxp-s32-mru"><code>nxp,s32-mru</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>用于NXP S32 SoC的增强型模块化I/O子系统（eMIOS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1281">已禁用：2</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P007_nxp_s32-emios.md#std-dtcompatible-nxp-s32-emios"><code>nxp,s32-emios</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>连接NXP S32 QSPI总线的QSPI HyperFlash（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L102">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P004_nxp_s32-qspi-hyperflash.md#std-dtcompatible-nxp-s32-qspi-hyperflash"><code>nxp,s32-qspi-hyperflash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存或其他非易失性存储器的固定分区（Fixed Partitions）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L116">已启用：1</a>）</td>
<td><a href="../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions"><code>fixed-partitions</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>用于S32Z／E SoC的NXP SIUL2引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P021_nxp_s32ze-siul2-pinctrl.md#std-dtcompatible-nxp-s32ze-siul2-pinctrl"><code>nxp,s32ze-siul2-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">外设传感器接口（PSI5）</td>
<td>片上（On-Chip）</td>
<td>NXP S32外设传感器接口（PSI5）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1576">已禁用：2</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P015_nxp_s32-psi5.md#std-dtcompatible-nxp-s32-psi5"><code>nxp,s32-psi5</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>用于S32 SoC的NXP S32 eMIOS脉宽调制（PWM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1361">已禁用：2</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P011_nxp_s32-emios-pwm.md#std-dtcompatible-nxp-s32-emios-pwm"><code>nxp,s32-emios-pwm</code></a></td>
</tr>
<tr>
<td rowspan="3">四线串行外设接口（QSPI）</td>
<td>片上（On-Chip）</td>
<td>NXP S32四线串行外设接口（QSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1454">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1462">已禁用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P007_nxp_s32-qspi.md#std-dtcompatible-nxp-s32-qspi"><code>nxp,s32-qspi</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP S32四线串行外设接口（QSPI）安全闪存保护（SFP）MDAD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L82">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P006_nxp_s32-qspi-sfp-mdad.md#std-dtcompatible-nxp-s32-qspi-sfp-mdad"><code>nxp,s32-qspi-sfp-mdad</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP S32四线串行外设接口（QSPI）安全闪存保护（SFP）FRAD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P005_nxp_s32-qspi-sfp-frad.md#std-dtcompatible-nxp-s32-qspi-sfp-frad"><code>nxp,s32-qspi-sfp-frad</code></a></td>
</tr>
<tr>
<td rowspan="1">单边沿半字节传输（SENT）</td>
<td>片上（On-Chip）</td>
<td>NXP S32单边沿半字节传输（SENT / Single Edge Nibble Transmission）接收控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1470">已禁用：2</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P016_nxp_s32-sent.md#std-dtcompatible-nxp-s32-sent"><code>nxp,s32-sent</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 LINFlexD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L125">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L133">已禁用：12</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P018_nxp_s32-linflexd.md#std-dtcompatible-nxp-s32-linflexd"><code>nxp,s32-linflexd</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L472">已禁用：10</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P005_nxp_s32-spi.md#std-dtcompatible-nxp-s32-spi"><code>nxp,s32-spi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP DSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L582">已禁用：1</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P018_nxp_dspi.md#std-dtcompatible-nxp-dspi"><code>nxp,dspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L115">已启用：3</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>软件看门狗定时器（SWT / Software Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L56">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L65">已禁用：4</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P013_nxp_s32-swt.md#std-dtcompatible-nxp-s32-swt"><code>nxp,s32-swt</code></a></td>
</tr>
</table>

<a id="s32z2xxdc2-s32z2xxdc2@B/s32z270/rtu1-hw-features-section"></a>

#### `s32z2xxdc2@B/s32z270/rtu1`目标（Target）

<a id="s32z2xxdc2-s32z2xxdc2@B/s32z270/rtu1-hw-features-panel"></a>

<a id="s32z2xxdc2-s32z2xxdc2@B/s32z270/rtu1-hw-features-memory"></a>

该开发板目标的片上存储容量：1 MiB RAM、7 MiB Flash。

<a id="s32z2xxdc2-s32z2xxdc2@B/s32z270/rtu1-hw-features-table"></a>

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
<td>ARM Cortex-R52处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L43">已启用：4</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P011_arm_cortex-r52.md#std-dtcompatible-arm-cortex-r52"><code>arm,cortex-r52</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP S32逐次逼近型模数转换器（SAR ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1107">已禁用：2</a>）</td>
<td><a href="../hardware/P853_NXPS32逐次逼近ADC绑定.md#dtbinding-nxp-s32-adc-sar"><code>nxp,s32-adc-sar</code></a></td>
</tr>
<tr>
<td rowspan="2">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 CANXL控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L719">已禁用：2</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P002_nxp_s32-canxl.md#std-dtcompatible-nxp-s32-canxl"><code>nxp,s32-canxl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L747">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L762">已禁用：23</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP S32时钟发生器IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L86">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P014_nxp_s32-clock.md#std-dtcompatible-nxp-s32-clock"><code>nxp,s32-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP S32系统定时器模块（STM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L24">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P018_nxp_s32-sys-timer.md#std-dtcompatible-nxp-s32-sys-timer"><code>nxp,s32-sys-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP周期中断定时器（PIT / Periodic Interrupt Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L101">已禁用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P017_nxp_pit.md#std-dtcompatible-nxp-pit"><code>nxp,pit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>周期中断定时器节点的子节点，用于表示单个定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L111">已禁用：6</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P016_nxp_pit-channel.md#std-dtcompatible-nxp-pit-channel"><code>nxp,pit-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>NXP S32硬件安全引擎（HSE）消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1901">已禁用：8</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P005_nxp_s32-crypto-hse-mu.md#std-dtcompatible-nxp-s32-crypto-hse-mu"><code>nxp,s32-crypto-hse-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1149">已禁用：4</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 NETC外部管理数据输入输出（MDIO）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L662">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P004_nxp_s32-netc-emdio.md#std-dtcompatible-nxp-s32-netc-emdio"><code>nxp,s32-netc-emdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32 NETC物理站点接口（PSI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L670">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P011_nxp_s32-netc-psi.md#std-dtcompatible-nxp-s32-netc-psi"><code>nxp,s32-netc-psi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32 NETC虚拟站点接口（VSI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L676">已禁用：7</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P012_nxp_s32-netc-vsi.md#std-dtcompatible-nxp-s32-netc-vsi"><code>nxp,s32-netc-vsi</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>NXP SIUL2 GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L244">已禁用：15</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P028_nxp_siul2-gpio.md#std-dtcompatible-nxp-siul2-gpio"><code>nxp,siul2-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1127">已禁用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L105">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SIUL2外部中断请求控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L234">已禁用：4</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P006_nxp_siul2-eirq.md#std-dtcompatible-nxp-siul2-eirq"><code>nxp,siul2-eirq</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>NXP S32消息接收单元（Message Receive Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L624">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L592">已禁用：7</a>）</td>
<td><a href="../intercore_reference/P049_NXPS32消息接收单元绑定.md#dtbinding-nxp-s32-mru"><code>nxp,s32-mru</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>用于NXP S32 SoC的增强型模块化I/O子系统（eMIOS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1281">已禁用：2</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P007_nxp_s32-emios.md#std-dtcompatible-nxp-s32-emios"><code>nxp,s32-emios</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>连接NXP S32 QSPI总线的QSPI HyperFlash（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L102">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P004_nxp_s32-qspi-hyperflash.md#std-dtcompatible-nxp-s32-qspi-hyperflash"><code>nxp,s32-qspi-hyperflash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存或其他非易失性存储器的固定分区（Fixed Partitions）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L116">已启用：1</a>）</td>
<td><a href="../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions"><code>fixed-partitions</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>用于S32Z／E SoC的NXP SIUL2引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P021_nxp_s32ze-siul2-pinctrl.md#std-dtcompatible-nxp-s32ze-siul2-pinctrl"><code>nxp,s32ze-siul2-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">外设传感器接口（PSI5）</td>
<td>片上（On-Chip）</td>
<td>NXP S32外设传感器接口（PSI5）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1576">已禁用：2</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P015_nxp_s32-psi5.md#std-dtcompatible-nxp-s32-psi5"><code>nxp,s32-psi5</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>用于S32 SoC的NXP S32 eMIOS脉宽调制（PWM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1361">已禁用：2</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P011_nxp_s32-emios-pwm.md#std-dtcompatible-nxp-s32-emios-pwm"><code>nxp,s32-emios-pwm</code></a></td>
</tr>
<tr>
<td rowspan="3">四线串行外设接口（QSPI）</td>
<td>片上（On-Chip）</td>
<td>NXP S32四线串行外设接口（QSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1454">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1462">已禁用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P007_nxp_s32-qspi.md#std-dtcompatible-nxp-s32-qspi"><code>nxp,s32-qspi</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP S32四线串行外设接口（QSPI）安全闪存保护（SFP）MDAD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L82">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P006_nxp_s32-qspi-sfp-mdad.md#std-dtcompatible-nxp-s32-qspi-sfp-mdad"><code>nxp,s32-qspi-sfp-mdad</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP S32四线串行外设接口（QSPI）安全闪存保护（SFP）FRAD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P005_nxp_s32-qspi-sfp-frad.md#std-dtcompatible-nxp-s32-qspi-sfp-frad"><code>nxp,s32-qspi-sfp-frad</code></a></td>
</tr>
<tr>
<td rowspan="1">单边沿半字节传输（SENT）</td>
<td>片上（On-Chip）</td>
<td>NXP S32单边沿半字节传输（SENT / Single Edge Nibble Transmission）接收控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1470">已禁用：2</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P016_nxp_s32-sent.md#std-dtcompatible-nxp-s32-sent"><code>nxp,s32-sent</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 LINFlexD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L125">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L133">已禁用：12</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P018_nxp_s32-linflexd.md#std-dtcompatible-nxp-s32-linflexd"><code>nxp,s32-linflexd</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L472">已禁用：10</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P005_nxp_s32-spi.md#std-dtcompatible-nxp-s32-spi"><code>nxp,s32-spi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP DSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L582">已禁用：1</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P018_nxp_dspi.md#std-dtcompatible-nxp-dspi"><code>nxp,dspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L115">已启用：3</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>软件看门狗定时器（SWT / Software Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L56">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L65">已禁用：4</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P013_nxp_s32-swt.md#std-dtcompatible-nxp-s32-swt"><code>nxp,s32-swt</code></a></td>
</tr>
</table>

<a id="s32z2xxdc2-s32z2xxdc2@D/s32z270/rtu0-hw-features-section"></a>

#### `s32z2xxdc2@D/s32z270/rtu0`目标（Target）

<a id="s32z2xxdc2-s32z2xxdc2@D/s32z270/rtu0-hw-features-panel"></a>

<a id="s32z2xxdc2-s32z2xxdc2@D/s32z270/rtu0-hw-features-memory"></a>

该开发板目标的片上存储容量：1 MiB RAM、7 MiB Flash。

<a id="s32z2xxdc2-s32z2xxdc2@D/s32z270/rtu0-hw-features-table"></a>

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
<td>ARM Cortex-R52处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L19">已启用：4</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P011_arm_cortex-r52.md#std-dtcompatible-arm-cortex-r52"><code>arm,cortex-r52</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP S32逐次逼近型模数转换器（SAR ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1107">已禁用：2</a>）</td>
<td><a href="../hardware/P853_NXPS32逐次逼近ADC绑定.md#dtbinding-nxp-s32-adc-sar"><code>nxp,s32-adc-sar</code></a></td>
</tr>
<tr>
<td rowspan="2">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 CANXL控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L719">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L733">已禁用：1</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P002_nxp_s32-canxl.md#std-dtcompatible-nxp-s32-canxl"><code>nxp,s32-canxl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L747">已禁用：24</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP S32时钟发生器IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L86">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P014_nxp_s32-clock.md#std-dtcompatible-nxp-s32-clock"><code>nxp,s32-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP S32系统定时器模块（STM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L24">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P018_nxp_s32-sys-timer.md#std-dtcompatible-nxp-s32-sys-timer"><code>nxp,s32-sys-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP周期中断定时器（PIT / Periodic Interrupt Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L101">已禁用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P017_nxp_pit.md#std-dtcompatible-nxp-pit"><code>nxp,pit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>周期中断定时器节点的子节点，用于表示单个定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L111">已禁用：6</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P016_nxp_pit-channel.md#std-dtcompatible-nxp-pit-channel"><code>nxp,pit-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>NXP S32硬件安全引擎（HSE）消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1901">已禁用：8</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P005_nxp_s32-crypto-hse-mu.md#std-dtcompatible-nxp-s32-crypto-hse-mu"><code>nxp,s32-crypto-hse-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1149">已禁用：4</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 NETC外部管理数据输入输出（MDIO）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L662">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P004_nxp_s32-netc-emdio.md#std-dtcompatible-nxp-s32-netc-emdio"><code>nxp,s32-netc-emdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32 NETC物理站点接口（PSI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L670">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P011_nxp_s32-netc-psi.md#std-dtcompatible-nxp-s32-netc-psi"><code>nxp,s32-netc-psi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32 NETC虚拟站点接口（VSI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L676">已禁用：7</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P012_nxp_s32-netc-vsi.md#std-dtcompatible-nxp-s32-netc-vsi"><code>nxp,s32-netc-vsi</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>NXP SIUL2 GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L244">已禁用：15</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P028_nxp_siul2-gpio.md#std-dtcompatible-nxp-siul2-gpio"><code>nxp,siul2-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1127">已禁用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L105">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SIUL2外部中断请求控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L234">已禁用：4</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P006_nxp_siul2-eirq.md#std-dtcompatible-nxp-siul2-eirq"><code>nxp,siul2-eirq</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>NXP S32消息接收单元（Message Receive Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L592">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L600">已禁用：7</a>）</td>
<td><a href="../intercore_reference/P049_NXPS32消息接收单元绑定.md#dtbinding-nxp-s32-mru"><code>nxp,s32-mru</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>用于NXP S32 SoC的增强型模块化I/O子系统（eMIOS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1281">已禁用：2</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P007_nxp_s32-emios.md#std-dtcompatible-nxp-s32-emios"><code>nxp,s32-emios</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>连接NXP S32 QSPI总线的QSPI HyperFlash（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L102">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P004_nxp_s32-qspi-hyperflash.md#std-dtcompatible-nxp-s32-qspi-hyperflash"><code>nxp,s32-qspi-hyperflash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存或其他非易失性存储器的固定分区（Fixed Partitions）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L116">已启用：1</a>）</td>
<td><a href="../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions"><code>fixed-partitions</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>用于S32Z／E SoC的NXP SIUL2引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P021_nxp_s32ze-siul2-pinctrl.md#std-dtcompatible-nxp-s32ze-siul2-pinctrl"><code>nxp,s32ze-siul2-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">外设传感器接口（PSI5）</td>
<td>片上（On-Chip）</td>
<td>NXP S32外设传感器接口（PSI5）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1576">已禁用：2</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P015_nxp_s32-psi5.md#std-dtcompatible-nxp-s32-psi5"><code>nxp,s32-psi5</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>用于S32 SoC的NXP S32 eMIOS脉宽调制（PWM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1361">已禁用：2</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P011_nxp_s32-emios-pwm.md#std-dtcompatible-nxp-s32-emios-pwm"><code>nxp,s32-emios-pwm</code></a></td>
</tr>
<tr>
<td rowspan="3">四线串行外设接口（QSPI）</td>
<td>片上（On-Chip）</td>
<td>NXP S32四线串行外设接口（QSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1454">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1462">已禁用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P007_nxp_s32-qspi.md#std-dtcompatible-nxp-s32-qspi"><code>nxp,s32-qspi</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP S32四线串行外设接口（QSPI）安全闪存保护（SFP）MDAD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L82">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P006_nxp_s32-qspi-sfp-mdad.md#std-dtcompatible-nxp-s32-qspi-sfp-mdad"><code>nxp,s32-qspi-sfp-mdad</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP S32四线串行外设接口（QSPI）安全闪存保护（SFP）FRAD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P005_nxp_s32-qspi-sfp-frad.md#std-dtcompatible-nxp-s32-qspi-sfp-frad"><code>nxp,s32-qspi-sfp-frad</code></a></td>
</tr>
<tr>
<td rowspan="1">单边沿半字节传输（SENT）</td>
<td>片上（On-Chip）</td>
<td>NXP S32单边沿半字节传输（SENT / Single Edge Nibble Transmission）接收控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1470">已禁用：2</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P016_nxp_s32-sent.md#std-dtcompatible-nxp-s32-sent"><code>nxp,s32-sent</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 LINFlexD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L197">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L125">已禁用：12</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P018_nxp_s32-linflexd.md#std-dtcompatible-nxp-s32-linflexd"><code>nxp,s32-linflexd</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L472">已禁用：10</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P005_nxp_s32-spi.md#std-dtcompatible-nxp-s32-spi"><code>nxp,s32-spi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP DSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L582">已禁用：1</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P018_nxp_dspi.md#std-dtcompatible-nxp-dspi"><code>nxp,dspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L115">已启用：3</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>软件看门狗定时器（SWT / Software Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L56">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L65">已禁用：4</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P013_nxp_s32-swt.md#std-dtcompatible-nxp-s32-swt"><code>nxp,s32-swt</code></a></td>
</tr>
</table>

<a id="s32z2xxdc2-s32z2xxdc2@D/s32z270/rtu1-hw-features-section"></a>

#### `s32z2xxdc2@D/s32z270/rtu1`目标（Target）

<a id="s32z2xxdc2-s32z2xxdc2@D/s32z270/rtu1-hw-features-panel"></a>

<a id="s32z2xxdc2-s32z2xxdc2@D/s32z270/rtu1-hw-features-memory"></a>

该开发板目标的片上存储容量：1 MiB RAM、7 MiB Flash。

<a id="s32z2xxdc2-s32z2xxdc2@D/s32z270/rtu1-hw-features-table"></a>

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
<td>ARM Cortex-R52处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L43">已启用：4</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P011_arm_cortex-r52.md#std-dtcompatible-arm-cortex-r52"><code>arm,cortex-r52</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP S32逐次逼近型模数转换器（SAR ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1107">已禁用：2</a>）</td>
<td><a href="../hardware/P853_NXPS32逐次逼近ADC绑定.md#dtbinding-nxp-s32-adc-sar"><code>nxp,s32-adc-sar</code></a></td>
</tr>
<tr>
<td rowspan="2">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 CANXL控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L719">已禁用：2</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P002_nxp_s32-canxl.md#std-dtcompatible-nxp-s32-canxl"><code>nxp,s32-canxl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L747">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L762">已禁用：23</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP S32时钟发生器IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L86">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P014_nxp_s32-clock.md#std-dtcompatible-nxp-s32-clock"><code>nxp,s32-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP S32系统定时器模块（STM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L24">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P018_nxp_s32-sys-timer.md#std-dtcompatible-nxp-s32-sys-timer"><code>nxp,s32-sys-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP周期中断定时器（PIT / Periodic Interrupt Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L101">已禁用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P017_nxp_pit.md#std-dtcompatible-nxp-pit"><code>nxp,pit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>周期中断定时器节点的子节点，用于表示单个定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L111">已禁用：6</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P016_nxp_pit-channel.md#std-dtcompatible-nxp-pit-channel"><code>nxp,pit-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>NXP S32硬件安全引擎（HSE）消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1901">已禁用：8</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P005_nxp_s32-crypto-hse-mu.md#std-dtcompatible-nxp-s32-crypto-hse-mu"><code>nxp,s32-crypto-hse-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1149">已禁用：4</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 NETC外部管理数据输入输出（MDIO）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L662">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P004_nxp_s32-netc-emdio.md#std-dtcompatible-nxp-s32-netc-emdio"><code>nxp,s32-netc-emdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32 NETC物理站点接口（PSI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L670">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P011_nxp_s32-netc-psi.md#std-dtcompatible-nxp-s32-netc-psi"><code>nxp,s32-netc-psi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP S32 NETC虚拟站点接口（VSI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L676">已禁用：7</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P012_nxp_s32-netc-vsi.md#std-dtcompatible-nxp-s32-netc-vsi"><code>nxp,s32-netc-vsi</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>NXP SIUL2 GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L244">已禁用：15</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P028_nxp_siul2-gpio.md#std-dtcompatible-nxp-siul2-gpio"><code>nxp,siul2-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1127">已禁用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L105">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SIUL2外部中断请求控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L234">已禁用：4</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P006_nxp_siul2-eirq.md#std-dtcompatible-nxp-siul2-eirq"><code>nxp,siul2-eirq</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>NXP S32消息接收单元（Message Receive Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L624">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L592">已禁用：7</a>）</td>
<td><a href="../intercore_reference/P049_NXPS32消息接收单元绑定.md#dtbinding-nxp-s32-mru"><code>nxp,s32-mru</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>用于NXP S32 SoC的增强型模块化I/O子系统（eMIOS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1281">已禁用：2</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P007_nxp_s32-emios.md#std-dtcompatible-nxp-s32-emios"><code>nxp,s32-emios</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>连接NXP S32 QSPI总线的QSPI HyperFlash（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L102">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P004_nxp_s32-qspi-hyperflash.md#std-dtcompatible-nxp-s32-qspi-hyperflash"><code>nxp,s32-qspi-hyperflash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存或其他非易失性存储器的固定分区（Fixed Partitions）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L116">已启用：1</a>）</td>
<td><a href="../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions"><code>fixed-partitions</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>用于S32Z／E SoC的NXP SIUL2引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P021_nxp_s32ze-siul2-pinctrl.md#std-dtcompatible-nxp-s32ze-siul2-pinctrl"><code>nxp,s32ze-siul2-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">外设传感器接口（PSI5）</td>
<td>片上（On-Chip）</td>
<td>NXP S32外设传感器接口（PSI5）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1576">已禁用：2</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P015_nxp_s32-psi5.md#std-dtcompatible-nxp-s32-psi5"><code>nxp,s32-psi5</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>用于S32 SoC的NXP S32 eMIOS脉宽调制（PWM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1361">已禁用：2</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P011_nxp_s32-emios-pwm.md#std-dtcompatible-nxp-s32-emios-pwm"><code>nxp,s32-emios-pwm</code></a></td>
</tr>
<tr>
<td rowspan="3">四线串行外设接口（QSPI）</td>
<td>片上（On-Chip）</td>
<td>NXP S32四线串行外设接口（QSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1454">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1462">已禁用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P007_nxp_s32-qspi.md#std-dtcompatible-nxp-s32-qspi"><code>nxp,s32-qspi</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP S32四线串行外设接口（QSPI）安全闪存保护（SFP）MDAD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L82">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P006_nxp_s32-qspi-sfp-mdad.md#std-dtcompatible-nxp-s32-qspi-sfp-mdad"><code>nxp,s32-qspi-sfp-mdad</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP S32四线串行外设接口（QSPI）安全闪存保护（SFP）FRAD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P005_nxp_s32-qspi-sfp-frad.md#std-dtcompatible-nxp-s32-qspi-sfp-frad"><code>nxp,s32-qspi-sfp-frad</code></a></td>
</tr>
<tr>
<td rowspan="1">单边沿半字节传输（SENT）</td>
<td>片上（On-Chip）</td>
<td>NXP S32单边沿半字节传输（SENT / Single Edge Nibble Transmission）接收控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L1470">已禁用：2</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P016_nxp_s32-sent.md#std-dtcompatible-nxp-s32-sent"><code>nxp,s32-sent</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 LINFlexD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L197">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L125">已禁用：12</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P018_nxp_s32-linflexd.md#std-dtcompatible-nxp-s32-linflexd"><code>nxp,s32-linflexd</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP S32 SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L472">已禁用：10</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P005_nxp_s32-spi.md#std-dtcompatible-nxp-s32-spi"><code>nxp,s32-spi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP DSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L582">已禁用：1</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P018_nxp_dspi.md#std-dtcompatible-nxp-dspi"><code>nxp,dspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_r52.dtsi?plain=1#L115">已启用：3</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>软件看门狗定时器（SWT / Software Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L56">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/s32/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L65">已禁用：4</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P013_nxp_s32-swt.md#std-dtcompatible-nxp-s32-swt"><code>nxp,s32-swt</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

SoC焊盘（Pads）在本移植中组织为端口和引脚，以与GPIO及HAL驱动一致。下表汇总焊盘到端口／引脚的映射，使用GPIO驱动或为设备驱动配置引脚复用时必须考虑此映射。

<table>
<tr>
<th>焊盘（Pads）</th>
<th>端口／引脚（Port/Pins）</th>
</tr>
<tr>
<td>PAD_000 - PAD_015</td>
<td>PA0 - PA15</td>
</tr>
<tr>
<td>PAD_016 - PAD_030</td>
<td>PB0 - PB14</td>
</tr>
<tr>
<td>PAD_031</td>
<td>PC15</td>
</tr>
<tr>
<td>PAD_032 - PAD_047</td>
<td>PD0 - PD15</td>
</tr>
<tr>
<td>PAD_048 - PAD_063</td>
<td>PE0 - PE15</td>
</tr>
<tr>
<td>PAD_064 - PAD_079</td>
<td>PF0 - PF15</td>
</tr>
<tr>
<td>PAD_080 - PAD_091</td>
<td>PG0 - PG11</td>
</tr>
<tr>
<td>PAD_092 - PAD_095</td>
<td>PH12 - PH15</td>
</tr>
<tr>
<td>PAD_096 - PAD_111</td>
<td>PI0 - PI15</td>
</tr>
<tr>
<td>PAD_112 - PAD_127</td>
<td>PJ0 - PJ15</td>
</tr>
<tr>
<td>PAD_128 - PAD_143</td>
<td>PK0 - PK15</td>
</tr>
<tr>
<td>PAD_144 - PAD_145</td>
<td>PL0 - PL1</td>
</tr>
<tr>
<td>PAD_146 - PAD_159</td>
<td>PM2 - PM15</td>
</tr>
<tr>
<td>PAD_160 - PAD_169</td>
<td>PN0 - PN9</td>
</tr>
<tr>
<td>PAD_170 - PAD_173</td>
<td>PO10 - PO13</td>
</tr>
</table>

此板不带用户LED或开关，而[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)、[Button](../basic_samples/P003_按钮输入.md#button)等示例需要这些器件。请按各示例说明为此板启用相应支持。

<a id="system-clock"></a>

### 系统时钟（System Clock）

Cortex-R52核配置为运行于1 GHz。

<a id="serial-port"></a>

### 串口（Serial Port）

SoC有12个可工作于UART模式的LINFlexD实例。默认通过Micro-USB B型连接器J119访问控制台。

<a id="watchdog"></a>

### 看门狗（Watchdog）

看门狗驱动只支持定时器到期触发中断。此板当前从SRAM运行Zephyr，因此不支持系统复位。

<a id="ethernet"></a>

### 以太网（Ethernet）

NETC驱动支持管理物理站点接口PSI0和／或一个虚拟站点接口VSI，其他VSI应分配给系统中的其他核。网络控制器配置方法见“[S32网络控制器（NETC）](../board_samples/P079_S32网络控制器.md#nxp_s32_netc)”。

<a id="controller-area-network"></a>

### 控制器局域网（CAN / Controller Area Network）

<a id="canexcel"></a>

#### CANEXCEL

CANEXCEL支持经典CAN（CAN 2.0）及CAN FD，不支持远程传输请求（Remote Transmission Request）。

此板目前未为CANEXCEL端口安装CAN收发器。若需与外部总线通信，必须另加收发器，可使用任何引脚兼容且支持CAN 2.0及CAN FD协议的收发器。

<a id="flexcan"></a>

#### FlexCAN

FlexCAN支持经典CAN（CAN 2.0）及CAN FD。

<a id="adc"></a>

### 模数转换器（ADC）

ADC由两个SAR ADC控制器实例提供，每个实例分辨率为12位。通道分为精密（Precision）及内部／标准（Internal/Standard）两组。

注意（Note）

同一实例的所有通道在同一时刻只能使用一个通道组。

<a id="edma"></a>

### 增强型DMA（EDMA）

EDMA模块包含4个EDMA3实例：实例0有32通道，实例1、4及5各有16通道。

<a id="external-flash"></a>

### 外部闪存（External Flash）

板载S26HS512T是512 Mbit HyperFlash，连接QSPI控制器A1端口。此开发板配置将其选为默认闪存控制器。

<a id="crypto"></a>

### 密码运算（CRYPTO）

硬件安全引擎（HSE）支持散列（Hashing）及对称密码（Symmetric Cipher）等密码运算，可使用基于RAM的密钥目录，密钥长度128或256位，支持ECB、CBC及CTR模式。

注意（Note）

驱动假定HSE固件已经安装并配置，例如密钥目录已格式化、所用消息单元（MU）实例已启用。安装及配置过程见《HSE固件用户手册》，需联系NXP销售或经销商以获取该文档。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`s32z2xxdc2`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>调试服务器（debugserver）</th>
<th>连接调试会话（attach）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-nxp-s32dbg">nxp_s32dbg</a></td>
<td></td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-trace32">trace32</a></td>
<td>✅</td>
<td>✅</td>
<td></td>
<td></td>
</tr>
</table>

s32z2xxdc2应用可按“构建应用”中的常规方法构建。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)）

目前此板只能将Zephyr应用二进制加载到核内部SRAM并从中执行。

此板支持以下调试工具对应的west运行工具：


- [NXP S32调试探针](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#nxp-s32-debug-probe)，默认
- [Lauterbach TRACE32](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#lauterbach-trace32-debug-host-tools)

加载固件前，请先按所选调试工具的安装步骤完成设置。

<a id="set-up-the-board"></a>

### 设置开发板（Set-up the Board）

把外部调试探针连接到开发板JTAG连接器J134，并根据探针能力，通过USB或以太网连接主机。

<a id="id18"></a>

查看串口输出时，将开发板USB／UART端口J119连接主机，并运行终端程序监听输出。例如使用跨平台[pySerial miniterm](https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm) [注9](#id17)：

```text
python -m serial.tools.miniterm <port> 115200
```

将`<port>`替换成开发板对应端口，例如Linux下的/dev/ttyUSB0。

<a id="debugging"></a>

### 调试（Debugging）

可按以下方式为s32z2xxdc2/s32z270/rtu0构建并调试[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例：

```text
# From the root of the zephyr repository
west build -b s32z2xxdc2/s32z270/rtu0 samples/hello_world
west debug
```

默认PCB修订版本为B。若使用较新PCB，需选择相应开发板定义，例如修订版本D：

```text
west build -b s32z2xxdc2@D/s32z270/rtu0 samples/hello_world
west debug
```

此时可进行常规调试，设置断点后用c继续执行。终端中应显示以下消息：

```text
Hello World! s32z2xxdc2
```

若使用Lauterbach TRACE32调试，改为运行：

```text
west debug -r trace32
```

<a id="flashing"></a>

### 烧录（Flashing）

若只需将应用下载到开发板SRAM并运行，按以下步骤操作。

只有Lauterbach TRACE32运行工具支持flash命令：

```text
west build -b s32z2xxdc2/s32z270/rtu0 samples/hello_world
west flash -r trace32
```

注意（Note）

目前Lauterbach的flash及debug启动脚本执行相同的SoC初始化与应用加载步骤，均将应用加载到SRAM。区别在于flash隐藏TRACE32界面，执行应用后退出。

要使用NXP S32调试探针达到类似行为，可让debug命令以GDB批处理模式（Batch Mode）运行：

```text
west debug --tool-opt='--batch'
```

<a id="rtu-and-core-configuration"></a>

### RTU与核配置（RTU and Core Configuration）

此Zephyr移植只能在任一Cortex-R52核上单核运行，支持锁步（Lock-step）或分离锁步（Split-lock）模式。默认使用所选RTU的第一个核，并采用复位时的锁步配置。

若要构建分离锁步模式，必须在应用Kconfig文件中禁用[CONFIG_DCLS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DCLS)。

默认开发板配置按构建设置生成运行工具参数。若需调试其他核，使用：

<a id="tab-0-bG9ja3N0ZXAgY29uZmlndXJhdGlvbg=="></a>

<a id="tab-0-c3BsaXQtbG9jayBjb25maWd1cmF0aW9u"></a>

<a id="panel-0-bG9ja3N0ZXAgY29uZmlndXJhdGlvbg=="></a>

**锁步配置（Lockstep Configuration）**

```text
west debug --core-name='R52_<rtu_id>_<core_id>_LS'
```

<a id="panel-0-c3BsaXQtbG9jayBjb25maWd1cmF0aW9u"></a>

**分离锁步配置（Split-lock Configuration）**

```text
west debug --core-name='R52_<rtu_id>_<core_id>'
```

其中：


- `<rtu_id>`为从0开始的RTU索引。
- `<core_id>`为所选RTU内从0开始的核索引，即运行Zephyr应用的核，取0、1、2或3。

例如，为s32z2xxdc2/s32z270/rtu0构建采用分离锁步配置的[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例：

```text
west build -b s32z2xxdc2/s32z270/rtu0 samples/hello_world -- -DCONFIG_DCLS=n
```

在RTU0的第二个核上以分离锁步模式执行此示例：

```text
west debug --core-name='R52_0_1'
```

使用Lauterbach TRACE32时，必须从命令行覆盖全部运行工具参数：

```text
west debug -r trace32 --startup-args elfFile=<elf_path> rtu=<rtu_id> core=<core_id> lockstep=<yes/no>
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

〔[8](#id16)〕 [https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32z-and-s32e-real-time-processors/s32z2-safe-and-secure-high-performance-real-time-processors:S32Z2](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32z-and-s32e-real-time-processors/s32z2-safe-and-secure-high-performance-real-time-processors:S32Z2)

<a id="id17"></a>

〔[9](#id18)〕 [https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm](https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm)

## 译注

S32Z2当前从SRAM执行，TRACE32的flash命令也只加载SRAM。默认PCB为B，D版须显式选择；锁步／分离锁步设置、RTU及核索引、无用户LED／按键、CANEXCEL需外部收发器，以及HSE预装条件分别保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [s32z2-safe-and-secure-high-performance-real-time-processors:S32Z2](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32z-and-s32e-real-time-processors/s32z2-safe-and-secure-high-performance-real-time-processors:S32Z2)：HTTP Error 404: Not Found。

---

[上一章](P012_S32K5XXCVB.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_TWR-KE18F.md)
