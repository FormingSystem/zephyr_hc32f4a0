---
id: learning.zephyr-docs.boards-nxp-remaining.page-8
title: MR-NavQ95B
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/mr_navq95b/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mr_navq95b"></a>

# 第8章\_MR-NavQ95B

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/mr_navq95b/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mr_navq95b.webp](images/mr_navq95b.webp)](images/mr_navq95b.webp)

MR-NavQ95B

名称（Name）：

`mr_navq95b`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mimx9596](https://docs.zephyrproject.org/latest/boards/index.html#soc=mimx9596)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mr_navq95b/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id17"></a>

[NXP MR-NAVQ95](https://github.com/NXP-Robotics/MR-NAVQ95) [注8](#id16)是面向移动机器人应用的开源开发板，基于NXP i.MX95应用处理器，提供异构多核（Heterogeneous Multicore）处理能力，可结合实时负载与高性能应用处理。

平台集成Cortex-A55应用核、Cortex-M7及Cortex-M33实时核。目前Zephyr支持主要针对Cortex-M7，该核通常用于实时固件。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="processor"></a>

### 处理器（Processor）


- NXP i.MX95片上系统（SoC）


  - 6个Arm Cortex-A55核
  - 1个Arm Cortex-M7核
  - 1个Arm Cortex-M33核

<a id="memory"></a>

### 存储器（Memory）


- 片上SRAM：1376 KiB，带ECC
- 外部LPDDR5：16 GiB，带内联ECC及加密
- 外部闪存：64 MiB八线SPI NOR

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`mr_navq95b`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mr_navq95b-hw-features"></a>

<a id="mr_navq95b-mr_navq95b/mimx9596/m7-hw-features-section"></a>

#### `mr_navq95b/mimx9596/m7`目标（Target）

<a id="mr_navq95b-mr_navq95b/mimx9596/m7-hw-features-panel"></a>

<a id="mr_navq95b-mr_navq95b/mimx9596/m7-hw-features-memory"></a>

该开发板目标的片上存储容量：256 KiB RAM、256 KiB Flash。

<a id="mr_navq95b-mr_navq95b/mimx9596/m7-hw-features-table"></a>

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
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP逐次逼近型ADC（SAR ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1220">已禁用：1</a>）</td>
<td><a href="../hardware/P854_NXP逐次逼近ADC绑定.md#dtbinding-nxp-sar-adc"><code>nxp,sar-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>i.MX数据紧耦合存储器（DTCM / Data Tightly Coupled Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L140">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P012_nxp_imx-dtcm.md#std-dtcompatible-nxp-imx-dtcm"><code>nxp,imx-dtcm</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>片上（On-Chip）</td>
<td>NXP脉冲密度调制麦克风接口（PDM / MICFIL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L481">已禁用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P014_nxp_micfil.md#std-dtcompatible-nxp-micfil"><code>nxp,micfil</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L371">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L359">已禁用：3</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗定时器（LPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L743">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr"><code>nxp,lptmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP时间戳定时器（TSTMR / Time Stamp Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L774">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L767">已禁用：1</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P004_nxp_tstmr.md#std-dtcompatible-nxp-tstmr"><code>nxp,tstmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗周期中断定时器（LPIT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L781">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P012_nxp_lpit.md#std-dtcompatible-nxp-lpit"><code>nxp,lpit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>低功耗周期中断定时器节点的子节点，表示一个独立定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L791">已启用：8</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P011_nxp_lpit-channel.md#std-dtcompatible-nxp-lpit-channel"><code>nxp,lpit-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">数字音频接口（DAI）</td>
<td>片上（On-Chip）</td>
<td>NXP同步音频接口（SAI / Synchronous Audio Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L455">已禁用：1</a>）</td>
<td><a href="../dai_binding_reference/P008_nxp_dai-sai.md#std-dtcompatible-nxp-dai-sai"><code>nxp,dai-sai</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>面向DSI面板的Socionext DPU显示控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1054">已禁用：1</a>）</td>
<td><a href="../display_sinowealth_sitronix_solomon_binding_reference/P013_socionext_dpu.md#std-dtcompatible-socionext-dpu"><code>socionext,dpu</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L222">已禁用：2</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="6">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX网络控制器（NETC）模块控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1075">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P005_nxp_imx-netc-blk-ctrl.md#std-dtcompatible-nxp-imx-netc-blk-ctrl"><code>nxp,imx-netc-blk-ctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1086">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P008_nxp_imx-netc.md#std-dtcompatible-nxp-imx-netc"><code>nxp,imx-netc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC物理站点接口（PSI / Physical Station Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1094">已禁用：3</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P006_nxp_imx-netc-psi.md#std-dtcompatible-nxp-imx-netc-psi"><code>nxp,imx-netc-psi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP NETC虚拟站接口（VSI / Virtual Station Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1143">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1132">已禁用：4</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P007_nxp_imx-netc-vsi.md#std-dtcompatible-nxp-imx-netc-vsi"><code>nxp,imx-netc-vsi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC外部MDIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1198">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P003_nxp_imx-netc-emdio.md#std-dtcompatible-nxp-imx-netc-emdio"><code>nxp,imx-netc-emdio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP NETC精确时间协议（PTP）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1210">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P009_nxp_netc-ptp-clock.md#std-dtcompatible-nxp-netc-ptp-clock"><code>nxp,netc-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="7">固件（Firmware）</td>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口共享内存（SHMEM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L67">已启用：1</a>）</td>
<td><a href="../hardware/P602_SCMI共享内存绑定.md#dtbinding-arm-scmi-shmem"><code>arm,scmi-shmem</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>采用门铃（Doorbell）及共享内存（SHMEM）传输的系统控制与管理接口（SCMI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L74">已启用：1</a>）</td>
<td><a href="../hardware/P600_SCMI邮箱传输绑定.md#dtbinding-arm-scmi"><code>arm,scmi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口电源域协议（Power Domain Protocol）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L83">已启用：1</a>）</td>
<td><a href="../hardware/P604_SCMI电源域协议绑定.md#dtbinding-arm-scmi-power"><code>arm,scmi-power</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI系统电源协议（System Power Protocol）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L89">已启用：1</a>）</td>
<td><a href="../hardware/P607_SCMI系统电源协议绑定.md#dtbinding-arm-scmi-system"><code>arm,scmi-system</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口时钟协议（Clock Protocol）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L94">已启用：1</a>）</td>
<td><a href="../hardware/P603_SCMI时钟协议绑定.md#dtbinding-arm-scmi-clock"><code>arm,scmi-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI引脚控制（Pinctrl）协议（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L100">已启用：1</a>）</td>
<td><a href="../hardware/P606_SCMI引脚控制协议绑定.md#dtbinding-arm-scmi-pinctrl"><code>arm,scmi-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI CPU域协议（CPU Domain Protocol）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L109">已启用：1</a>）</td>
<td><a href="../hardware/P608_NXP%20SCMI处理器协议绑定.md#dtbinding-nxp-scmi-cpu"><code>nxp,scmi-cpu</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX快速通用输入输出（RGPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L182">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L172">已禁用：3</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P001_nxp_imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio"><code>nxp,imx-rgpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L580">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L313">已禁用：7</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L468">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L843">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L856">已禁用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX数字信号处理器（DSP）中断控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L884">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L983">已禁用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P002_nxp_irqsteer-intc.md#std-dtcompatible-nxp-irqsteer-intc"><code>nxp,irqsteer-intc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX IRQ_STEER主控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L892">已启用：10</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L993">已禁用：6</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P003_nxp_irqsteer-master.md#std-dtcompatible-nxp-irqsteer-master"><code>nxp,irqsteer-master</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>用作Zephyr邮箱（MBOX）的NXP i.MX消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L869">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L876">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P047_NXPiMX消息单元邮箱绑定.md#dtbinding-nxp-mbox-imx-mu"><code>nxp,mbox-imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示串行接口（MIPI-DSI）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX MIPI DSI DWC显示串行接口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1063">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P015_nxp_mipi-dsi-dwc.md#std-dtcompatible-nxp-mipi-dsi-dwc"><code>nxp,mipi-dsi-dwc</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L145">已禁用：2</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>NXP FlexSPI MX25UM51345G闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L50">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P021_nxp_imx-flexspi-mx25um51345g.md#std-dtcompatible-nxp-imx-flexspi-mx25um51345g"><code>nxp,imx-flexspi-mx25um51345g</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L64">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>MCUX片上系统（SoC）的设备树（Devicetree）为该节点设置了<code>pinctrl</code>节点标签。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L104">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P004_nxp_imx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl"><code>nxp,imx93-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口电源域（Power Domain）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L120">已启用：2</a>）</td>
<td><a href="../hardware/P613_SCMI电源域绑定.md#dtbinding-arm-scmi-power-domain"><code>arm,scmi-power-domain</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L273">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L303">已禁用：3</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P008_nxp_kinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm"><code>nxp,kinetis-tpm</code></a></td>
</tr>
<tr>
<td rowspan="5">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>BMI08X惯性测量单元的加速度计（Accel）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L143">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P013_bosch_bmi08x-accel.md#std-dtcompatible-bosch-bmi08x-accel"><code>bosch,bmi08x-accel</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>BMI08X惯性测量单元的陀螺仪（Gyro）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L158">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P014_bosch_bmi08x-gyro.md#std-dtcompatible-bosch-bmi08x-gyro"><code>bosch,bmi08x-gyro</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ICM45686高精度六轴运动跟踪器件。在.dts或.dtsi文件中设置accel-pm、accel-range、accel-odr、gyro-pm、gyro-range及gyro-odr属性时，可包含icm45686.h并使用其中定义的宏。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L117">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P042_invensense_icm45686.md#std-dtcompatible-invensense-icm45686"><code>invensense,icm45686</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>BMP581是连接I3C总线的气压传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L198">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P022_bosch_bmp581.md#std-dtcompatible-bosch-bmp581"><code>bosch,bmp581</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Bosch BMM350地磁传感器，I3C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L203">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P019_bosch_bmm350.md#std-dtcompatible-bosch-bmm350"><code>bosch,bmm350</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L437">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L419">已禁用：6</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L161">已启用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L649">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L335">已禁用：6</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
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
<td>NXP看门狗（WDOG32）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1235">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P014_nxp_wdog32.md#std-dtcompatible-nxp-wdog32"><code>nxp,wdog32</code></a></td>
</tr>
</table>

<a id="mr_navq95b-mr_navq95b/mimx9596/m7/ddr-hw-features-section"></a>

#### `mr_navq95b/mimx9596/m7/ddr`目标（Target）

<a id="mr_navq95b-mr_navq95b/mimx9596/m7/ddr-hw-features-panel"></a>

<a id="mr_navq95b-mr_navq95b/mimx9596/m7/ddr-hw-features-memory"></a>

该开发板目标的片上存储容量：4 MiB RAM、N/A Flash。

<a id="mr_navq95b-mr_navq95b/mimx9596/m7/ddr-hw-features-table"></a>

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
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP逐次逼近型ADC（SAR ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1220">已禁用：1</a>）</td>
<td><a href="../hardware/P854_NXP逐次逼近ADC绑定.md#dtbinding-nxp-sar-adc"><code>nxp,sar-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>i.MX数据紧耦合存储器（DTCM / Data Tightly Coupled Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L140">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P012_nxp_imx-dtcm.md#std-dtcompatible-nxp-imx-dtcm"><code>nxp,imx-dtcm</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>片上（On-Chip）</td>
<td>NXP脉冲密度调制麦克风接口（PDM / MICFIL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L481">已禁用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P014_nxp_micfil.md#std-dtcompatible-nxp-micfil"><code>nxp,micfil</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L371">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L359">已禁用：3</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗定时器（LPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L743">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr"><code>nxp,lptmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP时间戳定时器（TSTMR / Time Stamp Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L774">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L767">已禁用：1</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P004_nxp_tstmr.md#std-dtcompatible-nxp-tstmr"><code>nxp,tstmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗周期中断定时器（LPIT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L781">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P012_nxp_lpit.md#std-dtcompatible-nxp-lpit"><code>nxp,lpit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>低功耗周期中断定时器节点的子节点，表示一个独立定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L791">已启用：8</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P011_nxp_lpit-channel.md#std-dtcompatible-nxp-lpit-channel"><code>nxp,lpit-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">数字音频接口（DAI）</td>
<td>片上（On-Chip）</td>
<td>NXP同步音频接口（SAI / Synchronous Audio Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L455">已禁用：1</a>）</td>
<td><a href="../dai_binding_reference/P008_nxp_dai-sai.md#std-dtcompatible-nxp-dai-sai"><code>nxp,dai-sai</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>面向DSI面板的Socionext DPU显示控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1054">已禁用：1</a>）</td>
<td><a href="../display_sinowealth_sitronix_solomon_binding_reference/P013_socionext_dpu.md#std-dtcompatible-socionext-dpu"><code>socionext,dpu</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L222">已禁用：2</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="6">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX网络控制器（NETC）模块控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1075">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P005_nxp_imx-netc-blk-ctrl.md#std-dtcompatible-nxp-imx-netc-blk-ctrl"><code>nxp,imx-netc-blk-ctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1086">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P008_nxp_imx-netc.md#std-dtcompatible-nxp-imx-netc"><code>nxp,imx-netc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC物理站点接口（PSI / Physical Station Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1094">已禁用：3</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P006_nxp_imx-netc-psi.md#std-dtcompatible-nxp-imx-netc-psi"><code>nxp,imx-netc-psi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP NETC虚拟站接口（VSI / Virtual Station Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1143">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1132">已禁用：4</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P007_nxp_imx-netc-vsi.md#std-dtcompatible-nxp-imx-netc-vsi"><code>nxp,imx-netc-vsi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC外部MDIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1198">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P003_nxp_imx-netc-emdio.md#std-dtcompatible-nxp-imx-netc-emdio"><code>nxp,imx-netc-emdio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP NETC精确时间协议（PTP）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1210">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P009_nxp_netc-ptp-clock.md#std-dtcompatible-nxp-netc-ptp-clock"><code>nxp,netc-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="7">固件（Firmware）</td>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口共享内存（SHMEM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L67">已启用：1</a>）</td>
<td><a href="../hardware/P602_SCMI共享内存绑定.md#dtbinding-arm-scmi-shmem"><code>arm,scmi-shmem</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>采用门铃（Doorbell）及共享内存（SHMEM）传输的系统控制与管理接口（SCMI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L74">已启用：1</a>）</td>
<td><a href="../hardware/P600_SCMI邮箱传输绑定.md#dtbinding-arm-scmi"><code>arm,scmi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口电源域协议（Power Domain Protocol）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L83">已启用：1</a>）</td>
<td><a href="../hardware/P604_SCMI电源域协议绑定.md#dtbinding-arm-scmi-power"><code>arm,scmi-power</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI系统电源协议（System Power Protocol）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L89">已启用：1</a>）</td>
<td><a href="../hardware/P607_SCMI系统电源协议绑定.md#dtbinding-arm-scmi-system"><code>arm,scmi-system</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口时钟协议（Clock Protocol）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L94">已启用：1</a>）</td>
<td><a href="../hardware/P603_SCMI时钟协议绑定.md#dtbinding-arm-scmi-clock"><code>arm,scmi-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI引脚控制（Pinctrl）协议（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L100">已启用：1</a>）</td>
<td><a href="../hardware/P606_SCMI引脚控制协议绑定.md#dtbinding-arm-scmi-pinctrl"><code>arm,scmi-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI CPU域协议（CPU Domain Protocol）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L109">已启用：1</a>）</td>
<td><a href="../hardware/P608_NXP%20SCMI处理器协议绑定.md#dtbinding-nxp-scmi-cpu"><code>nxp,scmi-cpu</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX快速通用输入输出（RGPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L182">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L172">已禁用：3</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P001_nxp_imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio"><code>nxp,imx-rgpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L580">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L313">已禁用：7</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L468">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L843">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L856">已禁用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX数字信号处理器（DSP）中断控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L884">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L983">已禁用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P002_nxp_irqsteer-intc.md#std-dtcompatible-nxp-irqsteer-intc"><code>nxp,irqsteer-intc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX IRQ_STEER主控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L892">已启用：10</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L993">已禁用：6</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P003_nxp_irqsteer-master.md#std-dtcompatible-nxp-irqsteer-master"><code>nxp,irqsteer-master</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>用作Zephyr邮箱（MBOX）的NXP i.MX消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L869">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L876">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P047_NXPiMX消息单元邮箱绑定.md#dtbinding-nxp-mbox-imx-mu"><code>nxp,mbox-imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示串行接口（MIPI-DSI）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX MIPI DSI DWC显示串行接口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1063">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P015_nxp_mipi-dsi-dwc.md#std-dtcompatible-nxp-mipi-dsi-dwc"><code>nxp,mipi-dsi-dwc</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L145">已禁用：2</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>NXP FlexSPI MX25UM51345G闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L50">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P021_nxp_imx-flexspi-mx25um51345g.md#std-dtcompatible-nxp-imx-flexspi-mx25um51345g"><code>nxp,imx-flexspi-mx25um51345g</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L64">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>MCUX片上系统（SoC）的设备树（Devicetree）为该节点设置了<code>pinctrl</code>节点标签。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L104">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P004_nxp_imx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl"><code>nxp,imx93-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口电源域（Power Domain）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L120">已启用：2</a>）</td>
<td><a href="../hardware/P613_SCMI电源域绑定.md#dtbinding-arm-scmi-power-domain"><code>arm,scmi-power-domain</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L273">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L303">已禁用：3</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P008_nxp_kinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm"><code>nxp,kinetis-tpm</code></a></td>
</tr>
<tr>
<td rowspan="5">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>BMI08X惯性测量单元的加速度计（Accel）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L143">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P013_bosch_bmi08x-accel.md#std-dtcompatible-bosch-bmi08x-accel"><code>bosch,bmi08x-accel</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>BMI08X惯性测量单元的陀螺仪（Gyro）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L158">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P014_bosch_bmi08x-gyro.md#std-dtcompatible-bosch-bmi08x-gyro"><code>bosch,bmi08x-gyro</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ICM45686高精度六轴运动跟踪器件。在.dts或.dtsi文件中设置accel-pm、accel-range、accel-odr、gyro-pm、gyro-range及gyro-odr属性时，可包含icm45686.h并使用其中定义的宏。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L117">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P042_invensense_icm45686.md#std-dtcompatible-invensense-icm45686"><code>invensense,icm45686</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>BMP581是连接I3C总线的气压传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L198">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P022_bosch_bmp581.md#std-dtcompatible-bosch-bmp581"><code>bosch,bmp581</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Bosch BMM350地磁传感器，I3C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L203">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P019_bosch_bmm350.md#std-dtcompatible-bosch-bmm350"><code>bosch,bmm350</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L437">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L419">已禁用：6</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L161">已启用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L649">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L335">已禁用：6</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
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
<td>NXP看门狗（WDOG32）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1235">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P014_nxp_wdog32.md#std-dtcompatible-nxp-wdog32"><code>nxp,wdog32</code></a></td>
</tr>
</table>

<a id="mr_navq95b-mr_navq95b/mimx9596/m7/flash-hw-features-section"></a>

#### `mr_navq95b/mimx9596/m7/flash`目标（Target）

<a id="mr_navq95b-mr_navq95b/mimx9596/m7/flash-hw-features-panel"></a>

<a id="mr_navq95b-mr_navq95b/mimx9596/m7/flash-hw-features-memory"></a>

该开发板目标的片上存储容量：256 KiB RAM、64 MiB Flash。

<a id="mr_navq95b-mr_navq95b/mimx9596/m7/flash-hw-features-table"></a>

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
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP逐次逼近型ADC（SAR ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1220">已禁用：1</a>）</td>
<td><a href="../hardware/P854_NXP逐次逼近ADC绑定.md#dtbinding-nxp-sar-adc"><code>nxp,sar-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>i.MX数据紧耦合存储器（DTCM / Data Tightly Coupled Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L140">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P012_nxp_imx-dtcm.md#std-dtcompatible-nxp-imx-dtcm"><code>nxp,imx-dtcm</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>片上（On-Chip）</td>
<td>NXP脉冲密度调制麦克风接口（PDM / MICFIL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L481">已禁用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P014_nxp_micfil.md#std-dtcompatible-nxp-micfil"><code>nxp,micfil</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L371">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L359">已禁用：3</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗定时器（LPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L743">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr"><code>nxp,lptmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP时间戳定时器（TSTMR / Time Stamp Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L774">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L767">已禁用：1</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P004_nxp_tstmr.md#std-dtcompatible-nxp-tstmr"><code>nxp,tstmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗周期中断定时器（LPIT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L781">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P012_nxp_lpit.md#std-dtcompatible-nxp-lpit"><code>nxp,lpit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>低功耗周期中断定时器节点的子节点，表示一个独立定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L791">已启用：8</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P011_nxp_lpit-channel.md#std-dtcompatible-nxp-lpit-channel"><code>nxp,lpit-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">数字音频接口（DAI）</td>
<td>片上（On-Chip）</td>
<td>NXP同步音频接口（SAI / Synchronous Audio Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L455">已禁用：1</a>）</td>
<td><a href="../dai_binding_reference/P008_nxp_dai-sai.md#std-dtcompatible-nxp-dai-sai"><code>nxp,dai-sai</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>面向DSI面板的Socionext DPU显示控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1054">已禁用：1</a>）</td>
<td><a href="../display_sinowealth_sitronix_solomon_binding_reference/P013_socionext_dpu.md#std-dtcompatible-socionext-dpu"><code>socionext,dpu</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L222">已禁用：2</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="6">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX网络控制器（NETC）模块控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1075">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P005_nxp_imx-netc-blk-ctrl.md#std-dtcompatible-nxp-imx-netc-blk-ctrl"><code>nxp,imx-netc-blk-ctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1086">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P008_nxp_imx-netc.md#std-dtcompatible-nxp-imx-netc"><code>nxp,imx-netc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC物理站点接口（PSI / Physical Station Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1094">已禁用：3</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P006_nxp_imx-netc-psi.md#std-dtcompatible-nxp-imx-netc-psi"><code>nxp,imx-netc-psi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP NETC虚拟站接口（VSI / Virtual Station Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1143">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1132">已禁用：4</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P007_nxp_imx-netc-vsi.md#std-dtcompatible-nxp-imx-netc-vsi"><code>nxp,imx-netc-vsi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC外部MDIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1198">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P003_nxp_imx-netc-emdio.md#std-dtcompatible-nxp-imx-netc-emdio"><code>nxp,imx-netc-emdio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP NETC精确时间协议（PTP）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1210">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P009_nxp_netc-ptp-clock.md#std-dtcompatible-nxp-netc-ptp-clock"><code>nxp,netc-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="7">固件（Firmware）</td>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口共享内存（SHMEM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L67">已启用：1</a>）</td>
<td><a href="../hardware/P602_SCMI共享内存绑定.md#dtbinding-arm-scmi-shmem"><code>arm,scmi-shmem</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>采用门铃（Doorbell）及共享内存（SHMEM）传输的系统控制与管理接口（SCMI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L74">已启用：1</a>）</td>
<td><a href="../hardware/P600_SCMI邮箱传输绑定.md#dtbinding-arm-scmi"><code>arm,scmi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口电源域协议（Power Domain Protocol）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L83">已启用：1</a>）</td>
<td><a href="../hardware/P604_SCMI电源域协议绑定.md#dtbinding-arm-scmi-power"><code>arm,scmi-power</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI系统电源协议（System Power Protocol）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L89">已启用：1</a>）</td>
<td><a href="../hardware/P607_SCMI系统电源协议绑定.md#dtbinding-arm-scmi-system"><code>arm,scmi-system</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口时钟协议（Clock Protocol）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L94">已启用：1</a>）</td>
<td><a href="../hardware/P603_SCMI时钟协议绑定.md#dtbinding-arm-scmi-clock"><code>arm,scmi-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI引脚控制（Pinctrl）协议（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L100">已启用：1</a>）</td>
<td><a href="../hardware/P606_SCMI引脚控制协议绑定.md#dtbinding-arm-scmi-pinctrl"><code>arm,scmi-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SCMI CPU域协议（CPU Domain Protocol）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L109">已启用：1</a>）</td>
<td><a href="../hardware/P608_NXP%20SCMI处理器协议绑定.md#dtbinding-nxp-scmi-cpu"><code>nxp,scmi-cpu</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX快速通用输入输出（RGPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L182">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L172">已禁用：3</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P001_nxp_imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio"><code>nxp,imx-rgpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L580">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L313">已禁用：7</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L468">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L843">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L856">已禁用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX数字信号处理器（DSP）中断控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L884">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L983">已禁用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P002_nxp_irqsteer-intc.md#std-dtcompatible-nxp-irqsteer-intc"><code>nxp,irqsteer-intc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX IRQ_STEER主控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L892">已启用：10</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L993">已禁用：6</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P003_nxp_irqsteer-master.md#std-dtcompatible-nxp-irqsteer-master"><code>nxp,irqsteer-master</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>用作Zephyr邮箱（MBOX）的NXP i.MX消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L869">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L876">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P047_NXPiMX消息单元邮箱绑定.md#dtbinding-nxp-mbox-imx-mu"><code>nxp,mbox-imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示串行接口（MIPI-DSI）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX MIPI DSI DWC显示串行接口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1063">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P015_nxp_mipi-dsi-dwc.md#std-dtcompatible-nxp-mipi-dsi-dwc"><code>nxp,mipi-dsi-dwc</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L145">已禁用：2</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>NXP FlexSPI MX25UM51345G闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L50">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P021_nxp_imx-flexspi-mx25um51345g.md#std-dtcompatible-nxp-imx-flexspi-mx25um51345g"><code>nxp,imx-flexspi-mx25um51345g</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L64">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>MCUX片上系统（SoC）的设备树（Devicetree）为该节点设置了<code>pinctrl</code>节点标签。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L104">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P004_nxp_imx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl"><code>nxp,imx93-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>SCMI系统控制与管理接口电源域（Power Domain）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L120">已启用：2</a>）</td>
<td><a href="../hardware/P613_SCMI电源域绑定.md#dtbinding-arm-scmi-power-domain"><code>arm,scmi-power-domain</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L273">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L303">已禁用：3</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P008_nxp_kinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm"><code>nxp,kinetis-tpm</code></a></td>
</tr>
<tr>
<td rowspan="5">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>BMI08X惯性测量单元的加速度计（Accel）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L143">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P013_bosch_bmi08x-accel.md#std-dtcompatible-bosch-bmi08x-accel"><code>bosch,bmi08x-accel</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>BMI08X惯性测量单元的陀螺仪（Gyro）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L158">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P014_bosch_bmi08x-gyro.md#std-dtcompatible-bosch-bmi08x-gyro"><code>bosch,bmi08x-gyro</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ICM45686高精度六轴运动跟踪器件。在.dts或.dtsi文件中设置accel-pm、accel-range、accel-odr、gyro-pm、gyro-range及gyro-odr属性时，可包含icm45686.h并使用其中定义的宏。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L117">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P042_invensense_icm45686.md#std-dtcompatible-invensense-icm45686"><code>invensense,icm45686</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>BMP581是连接I3C总线的气压传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L198">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P022_bosch_bmp581.md#std-dtcompatible-bosch-bmp581"><code>bosch,bmp581</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Bosch BMM350地磁传感器，I3C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mr_navq95b/mr_navq95b_mimx9596_m7.dts?plain=1#L203">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P019_bosch_bmm350.md#std-dtcompatible-bosch-bmm350"><code>bosch,bmm350</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L437">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L419">已禁用：6</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L161">已启用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L649">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L335">已禁用：6</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
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
<td>NXP看门狗（WDOG32）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx95_m7.dtsi?plain=1#L1235">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P014_nxp_wdog32.md#std-dtcompatible-nxp-wdog32"><code>nxp,wdog32</code></a></td>
</tr>
</table>

<a id="connectivity"></a>

### 连接能力（Connectivity）

<a id="id18"></a>

<a id="id24"></a>

[NXP MR-NAVQ95](https://github.com/NXP-Robotics/MR-NAVQ95) [注8](#id16)由一块底板及可选扩展模块组成，扩展模块提供额外接口和功能。此框图[注10](#id23)概述可用的扩展板及外设。（[框图（Block Diagram）](images/mr-navq95b-overview.png)）

这些接口采用复用方式，实际可用性取决于开发板配置及i.MX95的引脚复用（Pinmux）设置。

<a id="serial-console"></a>

## 串口控制台（Serial Console）

默认串口控制台路由到UART2，可通过I/O扩展板USB-C连接器J10上的USB转UART桥访问；主板独立的JST-GH连接器J2也引出UART2。

<a id="build-and-run-hello-world"></a>

## 构建并运行Hello World

<a id="id20"></a>

建议在SD卡上安装NavQ95镜像，以初始化M33及A55核，并在启动时由M7运行MCUboot，从而支持从外部闪存运行Zephyr固件。此SD卡镜像的构建及下载说明见[NXP IMX-MANIFEST-NAVQ95](https://github.com/NXP-Robotics/imx-manifest-navq95) [注9](#id19)。

为MR-NAVQ95B构建在指令紧耦合存储器（ITCM）中运行的Zephyr应用：

```text
west build -b mr_navq95b/mimx9596/m7 samples/hello_world/
```

构建从MX25UM51345G外部闪存运行的应用：

```text
west build -b mr_navq95b/mimx9596/m7/flash samples/hello_world/
```

可将Segger J-Link探针连接J7来上传二进制镜像：

```text
west flash
```

注意（Note）

向外部闪存烧录需要pyOCD支持mimx95_cm7_mx25um目标。原文撰写时，此支持尚未合入。

按以下步骤获取支持mimx95_cm7_mx25um的pyOCD：


- 安装pyOCD，通过板载JTAG器件烧录镜像。
- 将pyOCD克隆到自选目录，并检出pr-imx95分支：

  ```text
  git clone https://github.com/NXP-Robotics/pyOCD -b pr-imx95
  ```
- 构建pyOCD：

  ```text
  cd pyocd-private
  python3 -m pip install .
  ```

从外部闪存运行固件时，标准启动流程如下：


1. 系统管理器（System Manager，Cortex-M33）初始化系统
2. 将MCUboot加载到TCM
3. MCUboot验证外部闪存中的固件
4. 从闪存就地执行固件（XIP）

<a id="ethernet-running-a-netc-vsi-alongside-linux"></a>

## 以太网：与Linux并行运行NETC虚拟站点接口（VSI）

i.MX95的NETC／ENETC以太网控制器由A55上的Linux与M7上的Zephyr共享。Linux通过物理站点接口（PSI）拥有物理端口及PHY，其网络接口名为end0；M7上的Zephyr使用同一控制器的虚拟站点接口（VSI），即虚拟功能（VF）enetc0_vsi1／ENETC0 VF1，经共享端口收发数据。

VF属于物理功能（PF），因此Linux必须先创建并移交VF，M7才能使用。M7驱动不访问PHY或PF，仅启动自己的站点接口，并通过NETC VSI至PSI消息通道，请求PSI设置其MAC过滤器。

<a id="linux-device-tree"></a>

### Linux设备树（Device Tree）

<a id="id21"></a>

Linux设备树无需为M7专门修改。默认NavQ95 Linux镜像，见[NXP IMX-MANIFEST-NAVQ95](https://github.com/NXP-Robotics/imx-manifest-navq95) [注9](#id19)，已将ENETC0 PF启用为end0并支持SR-IOV，足以满足要求。VF在运行时创建，见下文，而非静态描述在设备树中。

<a id="bringing-up-the-vf-from-linux"></a>

### 从Linux启动VF

Linux启动后，在A55上以root身份执行以下步骤一次；其中end0为ENETC0 PF，其VF1将移交M7。

```text
# Keep Linux's VF driver off the VF so the M7 can own it, then create VF0+VF1.
echo 0 > /sys/class/net/end0/device/sriov_drivers_autoprobe
echo 2 > /sys/class/net/end0/device/sriov_numvfs

# Resolve the VF1 PCI address and let it DMA and raise MSI-X interrupts.
vf=$(basename "$(readlink -f /sys/class/net/end0/device/virtfn1)")
setpci -s "$vf" COMMAND=0x0006          # Bus Master Enable
setpci -s "$vf" CAP_MSIX+2.w=0x8000:0x8000

# Trust the VF so the PSI honours the M7 driver's MAC-filter requests.
ip link set end0 vf 1 trust on
```

完成后，M7 VSI驱动检测到VF已启用，并通过end0接入网络。

注意（Note）

<a id="id22"></a>

NavQ95板级支持包（BSP，见[NXP IMX-MANIFEST-NAVQ95](https://github.com/NXP-Robotics/imx-manifest-navq95) [注9](#id19)）提供enetc-vsi-handoff-mcore服务，在启动时执行这些步骤，因此通常无需手动运行。此处列出步骤供自定义配置使用。

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

〔8〕 ([1](#id17),[2](#id18)) [https://github.com/NXP-Robotics/MR-NAVQ95](https://github.com/NXP-Robotics/MR-NAVQ95)

<a id="id19"></a>

〔9〕 ([1](#id20),[2](#id21),[3](#id22)) [https://github.com/NXP-Robotics/imx-manifest-navq95](https://github.com/NXP-Robotics/imx-manifest-navq95)

<a id="id23"></a>

〔[10](#id24)〕 [https://github.com/NXP-Robotics/MR-NAVQ95/blob/main/images/mr-navq95b-overview.png](images/mr-navq95b-overview.png)

## 译注

原图框图链接指向GitHub文件浏览页，下载的是同一文件的原始PNG，媒体清单同时记录页面链接与原始下载地址。保留M7的ITCM／外部闪存构建、原文尚未合入的pyOCD分支说明，以及Linux创建并移交NETC VF的步骤；后者通常由BSP服务自动执行。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。

---

[上一章](P007_MR-MCXN-T1.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_RD-RW612-BGA.md)
