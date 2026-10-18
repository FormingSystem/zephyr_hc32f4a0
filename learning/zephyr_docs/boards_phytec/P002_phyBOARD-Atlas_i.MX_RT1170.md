---
id: learning.zephyr-docs.boards-phytec.page-2
title: phyBOARD-Atlas i.MX RT1170
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/phytec/phyboard_atlas/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="phyboard_atlas"></a>

# 第2章\_phyBOARD-Atlas i.MX RT1170

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/phytec/phyboard_atlas/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/phyboard_atlas.webp](images/phyboard_atlas.webp)](images/phyboard_atlas.webp)

phyBOARD-Atlas i.MX RT1170

名称（Name）：

`phyboard_atlas`

厂商（Vendor）：

[PHYTEC](https://docs.zephyrproject.org/latest/boards/index.html#vendor=phytec)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mimxrt1176](https://docs.zephyrproject.org/latest/boards/index.html#soc=mimxrt1176)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/phytec/phyboard_atlas/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

PHYTEC phyBOARD-Atlas i.MX RT1170搭载phyCORE-i.MX RT1170核心模块（System on Module，SoM）。该模块基于NXP双核i.MX RT1170，Cortex-M7运行于1 GHz，Cortex-M4运行于400 MHz。

<a id="hardware"></a>

## 硬件（Hardware）


- MIMXRT1176DVMAA微控制器


  - 1 GHz Cortex-M7及400 MHz Cortex-M4
  - 2 MB SRAM，其中Cortex-M7具有512 KB紧耦合存储器（TCM），Cortex-M4具有256 KB TCM
- 存储器（Memory）


  - 512 Mbit同步动态RAM（SDRAM）
  - 128 Mbit QSPI闪存
  - 512 Mbit八线闪存（Octal Flash）
- 接口（Interfaces）


  - MicroSD：一个卡槽
  - USB：两个USB 2.0 OTG
  - 以太网：一路10／100／1000BASE-T及一路10／100BASE-T，RJ45接口
  - 扩展：一个M.2连接器
  - 显示：一路MIPI DSI
  - 摄像头：一路MIPI CSI
  - 音频：标准音频接口
  - 串口：一路RS232，2×5排针，以及一路RS485
  - UART：通过扩展接口提供一路
  - CAN：一路，2×5排针
  - LED：一个RGB用户LED
  - 扩展接口：60引脚
  - 安全：OPTIGA TPM SLB 9670可信平台模块，符合TPM 2.0
  - 电源输入：USB-C，5 V／3 A
- 调试（Debug）

  > - Micro-USB串口调试接口
  > - JTAG：通过扩展接口提供

phyCORE-i.MX RT1170及phyBOARD-Atlas i.MX RT1170的更多信息见以下资料：


- <a id="id3"></a>

  [phyCORE-i.MX RT1170产品页](https://www.phytec.com/product/phycore-rt1170)[注1](#id2)
- <a id="id5"></a>

  [phyBOARD-Atlas i.MX RT1170产品页](https://www.phytec.com/product/phyboard-rt1170-development-kit/)[注2](#id4)

<a id="external-memory"></a>

### 外部存储器（External Memory）

此平台具有以下外部存储器：

<table>
<tr>
<th>器件（Device）</th>
<th>控制器（Controller）</th>
<th>状态（Status）</th>
</tr>
<tr>
<td>MT48LC16M16A2B4-7EIT同步动态RAM（SDRAM）</td>
<td>智能外部存储器控制器（SEMC）</td>
<td>通过设备配置数据块（DCD）启用，在启动时设置智能外部存储器控制器（SEMC）。</td>
</tr>
<tr>
<td>MX25U12832FM2I02 QSPI闪存</td>
<td>FLEXSPI</td>
<td>通过闪存配置块（FCB）启用，在启动时设置FlexSPI。</td>
</tr>
</table>

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`phyboard_atlas`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="phyboard_atlas-hw-features"></a>

<a id="phyboard_atlas-phyboard_atlas/mimxrt1176/cm7-hw-features-section"></a>

#### `phyboard_atlas/mimxrt1176/cm7`目标（Target）

<a id="phyboard_atlas-phyboard_atlas/mimxrt1176/cm7-hw-features-panel"></a>

<a id="phyboard_atlas-phyboard_atlas/mimxrt1176/cm7-hw-features-memory"></a>

该开发板目标的片上存储容量：64 MiB RAM、16 MiB Flash。

<a id="phyboard_atlas-phyboard_atlas/mimxrt1176/cm7-hw-features-table"></a>

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
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx_cm7.dtsi?plain=1#L16">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L1013">已禁用：2</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX交叉开关（XBAR / Crossbar Switch）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L1337">已禁用：3</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P016_nxp_mcux-xbar.md#std-dtcompatible-nxp-mcux-xbar"><code>nxp,mcux-xbar</code></a></td>
</tr>
<tr>
<td rowspan="2">音频（Audio）</td>
<td>板载（On-Board）</td>
<td>Texas Instruments TLV320AIC3110音频数模转换器（DAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/phytec/phyboard_atlas/phyboard_atlas.dtsi?plain=1#L133">已启用：1</a>）</td>
<td><a href="../audio_stm32_ti_wolfson_binding_reference/P009_ti_tlv320aic3110.md#std-dtcompatible-ti-tlv320aic3110"><code>ti,tlv320aic3110</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP脉冲密度调制麦克风接口（PDM / MICFIL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L1223">已禁用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P014_nxp_micfil.md#std-dtcompatible-nxp-micfil"><code>nxp,micfil</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L972">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L948">已禁用：2</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="4">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>i.MX第2版时钟控制模块（CCM）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L205">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P018_nxp_imx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2"><code>nxp,imx-ccm-rev2</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX RT11xx ARM PLL时钟提供者（Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L217">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P001_nxp_imxrt11xx-arm-pll.md#std-dtcompatible-nxp-imxrt11xx-arm-pll"><code>nxp,imxrt11xx-arm-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX模拟时钟控制模块（ANATOP / Analog Clock Controller Module）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L1071">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P016_nxp_imx-anatop.md#std-dtcompatible-nxp-imx-anatop"><code>nxp,imx-anatop</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis模拟比较器（ACMP / Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L1043">已禁用：4</a>）</td>
<td><a href="../hardware/P745_NXPKinetis模拟比较器绑定.md#dtbinding-nxp-kinetis-acmp"><code>nxp,kinetis-acmp</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX通用定时器（GPT / General-Purpose Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L118">已启用：5</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P004_nxp_imx-gpt.md#std-dtcompatible-nxp-imx-gpt"><code>nxp,imx-gpt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP周期中断定时器（PIT / Periodic Interrupt Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L1365">已启用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P017_nxp_pit.md#std-dtcompatible-nxp-pit"><code>nxp,pit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>周期中断定时器节点的子节点，用于表示单个定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L1375">已禁用：8</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P016_nxp_pit-channel.md#std-dtcompatible-nxp-pit-channel"><code>nxp,pit-channel</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SNVS低功耗／高功耗域实时时钟计数器（LP/HP Realtime Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/phytec/phycore_rt1170_common.dtsi?plain=1#L35">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P006_nxp_imx-snvs-rtc.md#std-dtcompatible-nxp-imx-snvs-rtc"><code>nxp,imx-snvs-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX 12位数模转换器（DAC12）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L69">已启用：1</a>）</td>
<td><a href="../hardware/P765_NXPDAC12数模转换器绑定.md#dtbinding-nxp-dac12"><code>nxp,dac12</code></a></td>
</tr>
<tr>
<td rowspan="2">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX增强型LCD接口（eLCDIF / Enhanced LCD Interface）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L399">已禁用：1</a>）</td>
<td><a href="../display_ilitek_matrix_nxp_binding_reference/P018_nxp_imx-elcdif.md#std-dtcompatible-nxp-imx-elcdif"><code>nxp,imx-elcdif</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX第2版LCD接口（LCDIFV2）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L407">已禁用：1</a>）</td>
<td><a href="../display_ilitek_matrix_nxp_binding_reference/P019_nxp_imx-lcdifv2.md#std-dtcompatible-nxp-imx-lcdifv2"><code>nxp,imx-lcdifv2</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L1078">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L1098">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP PXP二维DMA引擎（2D DMA Engine）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L1117">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P005_nxp_pxp.md#std-dtcompatible-nxp-pxp"><code>nxp,pxp</code></a></td>
</tr>
<tr>
<td rowspan="6">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP ENET以太网IP模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L794">已启用：2</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P004_nxp_enet.md#std-dtcompatible-nxp-enet"><code>nxp,enet</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET MAC／二层（L2）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L799">已启用：2</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P001_nxp_enet-mac.md#std-dtcompatible-nxp-enet-mac"><code>nxp,enet-mac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET管理数据输入输出（MDIO）功能（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L808">已启用：2</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P002_nxp_enet-mdio.md#std-dtcompatible-nxp-enet-mdio"><code>nxp,enet-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Microchip KSZ8081以太网PHY设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/phytec/phyboard_atlas/phyboard_atlas.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P001_microchip_ksz8081.md#std-dtcompatible-microchip-ksz8081"><code>microchip,ksz8081</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET精确时间协议（PTP / Precision Time Protocol）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L815">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L845">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P002_nxp_enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock"><code>nxp,enet-ptp-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>TI DP83867以太网物理层（PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/phytec/phycore_rt1170_common.dtsi?plain=1#L77">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P014_ti_dp83867.md#std-dtcompatible-ti-dp83867"><code>ti,dp83867</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L223">已启用：15</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P030_nxp_imx-gpio.md#std-dtcompatible-nxp-imx-gpio"><code>nxp,imx-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP 44引脚板对板（BTB）摄像头连接器引出的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/phytec/phyboard_atlas/phyboard_atlas_mimxrt1176_cm7.dts?plain=1#L38">已启用：1</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P026_nxp_cam-44pins-connector.md#std-dtcompatible-nxp-cam-44pins-connector"><code>nxp,cam-44pins-connector</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP SRC第2版复位原因标志读取（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L1303">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P007_nxp_imx-src-rev2.md#std-dtcompatible-nxp-imx-src-rev2"><code>nxp,imx-src-rev2</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L321">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L310">已禁用：4</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L1131">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L1154">已禁用：3</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/phytec/phyboard_atlas/phyboard_atlas.dtsi?plain=1#L24">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">处理器间消息（IPM）</td>
<td>片上（On-Chip）</td>
<td>i.MX消息单元（Messaging Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx_cm7.dtsi?plain=1#L129">已启用：1</a>）</td>
<td><a href="../intercore_reference/P072_NXPiMX消息单元绑定.md#dtbinding-nxp-imx-mu"><code>nxp,imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>片上（On-Chip）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/phytec/phycore_rt1170_common.dtsi?plain=1#L16">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP智能外部存储器控制器（SEMC / Smart External Memory Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L102">已启用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P016_nxp_imx-semc.md#std-dtcompatible-nxp-imx-semc"><code>nxp,imx-semc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexRAM片上RAM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx_cm7.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P015_nxp_flexram.md#std-dtcompatible-nxp-flexram"><code>nxp,flexram</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示串行接口（MIPI-DSI）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX MIPI显示串行接口（DSI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L414">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P013_nxp_imx-mipi-dsi.md#std-dtcompatible-nxp-imx-mipi-dsi"><code>nxp,imx-mipi-dsi</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L778">已禁用：2</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx_cm7.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="3">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/phytec/phycore_rt1170_common.dtsi?plain=1#L100">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P023_nxp_imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor"><code>nxp,imx-flexspi-nor</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/phytec/phycore_rt1170_common.dtsi?plain=1#L113">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>兼容Atmel AT24系列的I2C电可擦除可编程只读存储器（EEPROM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/phytec/phycore_rt1170_common.dtsi?plain=1#L48">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P004_atmel_at24.md#std-dtcompatible-atmel-at24"><code>atmel,at24</code></a></td>
</tr>
<tr>
<td rowspan="1">物理层（PHY）</td>
<td>板载（On-Board）</td>
<td>由简单GPIO控制的CAN收发器（Transceiver）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/phytec/phyboard_atlas/phyboard_atlas.dtsi?plain=1#L65">已启用：1</a>）</td>
<td><a href="../phy_binding_reference/P001_can-transceiver-gpio.md#std-dtcompatible-can-transceiver-gpio"><code>can-transceiver-gpio</code></a></td>
</tr>
<tr>
<td rowspan="4">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>这个兼容性绑定（Compatible Binding）应应用于设备的<code>iomuxc</code>设备树源文件（DTS）节点。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L376">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P023_nxp_imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc"><code>nxp,imx-iomuxc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>该节点在MCUX RT SoC设备树中设置了pinctrl节点标签（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L381">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P013_nxp_mcux-rt11xx-pinctrl.md#std-dtcompatible-nxp-mcux-rt11xx-pinctrl"><code>nxp,mcux-rt11xx-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>该节点在MCUX RT SoC设备树中设置了pinctrl节点标签（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L387">已禁用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P012_nxp_mcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl"><code>nxp,mcux-rt-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX I/O复用控制器（IOMUXC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L393">已启用：2</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P021_nxp_imx-gpr.md#std-dtcompatible-nxp-imx-gpr"><code>nxp,imx-gpr</code></a></td>
</tr>
<tr>
<td rowspan="3">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NXP四路定时器（QTMR）脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L173">已禁用：4</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P010_nxp_qtmr-pwm.md#std-dtcompatible-nxp-qtmr-pwm"><code>nxp,qtmr-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>包含mcux-pwm子模块的NXP eFLEX PWM模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L594">已启用：4</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P003_nxp_flexpwm.md#std-dtcompatible-nxp-flexpwm"><code>nxp,flexpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L599">已禁用：16</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P005_nxp_imx-pwm.md#std-dtcompatible-nxp-imx-pwm"><code>nxp,imx-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>i.MX密码加速与保障模块（CAAM / Cryptographic Acceleration and Assurance Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx_cm7.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P018_nxp_imx-caam.md#std-dtcompatible-nxp-imx-caam"><code>nxp,imx-caam</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L885">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L897">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P014_nxp_imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc"><code>nxp,imx-usdhc</code></a></td>
</tr>
<tr>
<td rowspan="2">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>ICM-40627运动跟踪器件（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/phytec/phyboard_atlas/phyboard_atlas.dtsi?plain=1#L141">已启用：1</a>）</td>
<td><a href="../sensor_espressif_honeywell_invensense_binding_reference/P019_invensense_icm40627-i2c.md#std-dtcompatible-invensense-icm40627"><code>invensense,icm40627</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX正交解码器（QDEC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L1309">已禁用：4</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P008_nxp_mcux-qdec.md#std-dtcompatible-nxp-mcux-qdec"><code>nxp,mcux-qdec</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L498">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L514">已禁用：8</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L78">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L90">已禁用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L474">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L426">已禁用：5</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L1007">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX通用硬件定时器（GPT / General-Purpose HW Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L111">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P007_nxp_gpt-hw-timer.md#std-dtcompatible-nxp-gpt-hw-timer"><code>nxp,gpt-hw-timer</code></a></td>
</tr>
<tr>
<td rowspan="2">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L853">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L863">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L873">已启用：2</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td rowspan="2">视频（Video）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX CMOS传感器接口（Sensor Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L909">已禁用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P008_nxp_imx-csi.md#std-dtcompatible-nxp-imx-csi"><code>nxp,imx-csi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MIPI CSI-2接收接口（Rx）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L922">已禁用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P010_nxp_mipi-csi2rx.md#std-dtcompatible-nxp-mipi-csi2rx"><code>nxp,mipi-csi2rx</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>NXP外部看门狗监测器（External Watchdog Monitor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L60">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P007_nxp_ewm.md#std-dtcompatible-nxp-ewm"><code>nxp,ewm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX RT看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt11xx/nxp_rt11xx.dtsi?plain=1#L984">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P009_nxp_imx-wdog.md#std-dtcompatible-nxp-imx-wdog"><code>nxp,imx-wdog</code></a></td>
</tr>
</table>

<a id="connections-and-i-os"></a>

### 连接与I/O（Connections and I/Os）

MIMXRT1170 SoC有6对引脚复用／GPIO控制器。

<table>
<tr>
<td>名称（Name）</td>
<td>功能（Function）</td>
<td>用途（Usage）</td>
</tr>
<tr>
<td>GPIO_AD_35</td>
<td>通用输入输出（GPIO）</td>
<td>用户按键（User Button）</td>
</tr>
<tr>
<td>GPIO_SNVS_08</td>
<td>通用输入输出（GPIO）</td>
<td>SoM上的红色LED</td>
</tr>
<tr>
<td>GPIO_SNVS_09</td>
<td>通用输入输出（GPIO）</td>
<td>SoM上的绿色LED</td>
</tr>
<tr>
<td>GPIO_AD_14</td>
<td>通用输入输出（GPIO）</td>
<td>载板（Carrier Board）上的红色LED</td>
</tr>
<tr>
<td>GPIO_LPSR_13</td>
<td>通用输入输出（GPIO）</td>
<td>载板上的绿色LED</td>
</tr>
<tr>
<td>GPIO_AD_18</td>
<td>LPI2C2_SCL</td>
<td>EEPROM</td>
</tr>
<tr>
<td>GPIO_AD_19</td>
<td>LPI2C2_SDA</td>
<td>EEPROM</td>
</tr>
<tr>
<td>GPIO_LPSR_08</td>
<td>LPI2C5_SCL</td>
<td>加速度计、编解码器（CODEC）及显示屏</td>
</tr>
<tr>
<td>GPIO_LPSR_09</td>
<td>LPI2C5_SDA</td>
<td>加速度计、编解码器（CODEC）及显示屏</td>
</tr>
<tr>
<td>GPIO_AD_24</td>
<td>LPUART1_TX</td>
<td>CM7 UART控制台</td>
</tr>
<tr>
<td>GPIO_AD_25</td>
<td>LPUART1_RX</td>
<td>CM7 UART控制台</td>
</tr>
<tr>
<td>GPIO_AD_28</td>
<td>LPUART5_TX</td>
<td>通用异步收发器（UART）</td>
</tr>
<tr>
<td>GPIO_AD_29</td>
<td>LPUART5_RX</td>
<td>通用异步收发器（UART）</td>
</tr>
<tr>
<td>GPIO_EMC_B1_40</td>
<td>LPUART6_TX</td>
<td>CM4 UART控制台</td>
</tr>
<tr>
<td>GPIO_EMC_B1_41</td>
<td>LPUART6_RX</td>
<td>CM4 UART控制台</td>
</tr>
<tr>
<td>GPIO_AD_00</td>
<td>CTP_INT</td>
<td>显示（Display）</td>
</tr>
<tr>
<td>GPIO_AD_01</td>
<td>CTP_RST_B</td>
<td>显示（Display）</td>
</tr>
<tr>
<td>GPIO_DISP_B2_05</td>
<td>PWR_EN</td>
<td>显示（Display）</td>
</tr>
<tr>
<td>GPIO_AD_30</td>
<td>Backlight_CTL</td>
<td>显示（Display）</td>
</tr>
<tr>
<td>GPIO_AD_32</td>
<td>ENET_MDC</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_AD_33</td>
<td>ENET_MDIO</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_DISP_B2_02</td>
<td>ENET_TX_DATA00</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_DISP_B2_03</td>
<td>ENET_TX_DATA01</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_DISP_B2_04</td>
<td>ENET_TX_EN</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_DISP_B2_05</td>
<td>ENET_TX_CLK</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_DISP_B2_06</td>
<td>ENET_RX_DATA00</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_DISP_B2_07</td>
<td>ENET_RX_DATA01</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_DISP_B2_08</td>
<td>ENET_RX_EN</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_DISP_B2_09</td>
<td>ENET_RX_ER</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_EMC_B2_19</td>
<td>ENET_RGMII_MDC</td>
<td>千兆以太网（Ethernet 1G）</td>
</tr>
<tr>
<td>GPIO_EMC_B2_20</td>
<td>ENET_RGMII_MDIO</td>
<td>千兆以太网（Ethernet 1G）</td>
</tr>
<tr>
<td>GPIO_DISP_B1_09</td>
<td>ENET_RGMII_TX_DATA00</td>
<td>千兆以太网（Ethernet 1G）</td>
</tr>
<tr>
<td>GPIO_DISP_B1_08</td>
<td>ENET_RGMII_TX_DATA01</td>
<td>千兆以太网（Ethernet 1G）</td>
</tr>
<tr>
<td>GPIO_DISP_B1_07</td>
<td>ENET_RGMII_TX_DATA02</td>
<td>千兆以太网（Ethernet 1G）</td>
</tr>
<tr>
<td>GPIO_DISP_B1_06</td>
<td>ENET_RGMII_TX_DATA03</td>
<td>千兆以太网（Ethernet 1G）</td>
</tr>
<tr>
<td>GPIO_DISP_B1_10</td>
<td>ENET_RGMII_TX_EN</td>
<td>千兆以太网（Ethernet 1G）</td>
</tr>
<tr>
<td>GPIO_DISP_B1_11</td>
<td>ENET_RGMII_TX_CLK</td>
<td>千兆以太网（Ethernet 1G）</td>
</tr>
<tr>
<td>GPIO_DISP_B1_02</td>
<td>ENET_RGMII_RX_DATA00</td>
<td>千兆以太网（Ethernet 1G）</td>
</tr>
<tr>
<td>GPIO_DISP_B1_03</td>
<td>ENET_RGMII_RX_DATA01</td>
<td>千兆以太网（Ethernet 1G）</td>
</tr>
<tr>
<td>GPIO_DISP_B1_04</td>
<td>ENET_RGMII_RX_DATA02</td>
<td>千兆以太网（Ethernet 1G）</td>
</tr>
<tr>
<td>GPIO_DISP_B1_05</td>
<td>ENET_RGMII_RX_DATA03</td>
<td>千兆以太网（Ethernet 1G）</td>
</tr>
<tr>
<td>GPIO_DISP_B1_00</td>
<td>ENET_RGMII_RX_EN</td>
<td>千兆以太网（Ethernet 1G）</td>
</tr>
<tr>
<td>GPIO_DISP_B1_01</td>
<td>ENET_RGMII_RX_CLK</td>
<td>千兆以太网（Ethernet 1G）</td>
</tr>
<tr>
<td>GPIO_AD_02</td>
<td>LPUART8_TX</td>
<td>RS-232</td>
</tr>
<tr>
<td>GPIO_AD_03</td>
<td>LPUART8_RX</td>
<td>RS-232</td>
</tr>
<tr>
<td>GPIO_AD_04</td>
<td>LPUART8_CTS</td>
<td>RS-232</td>
</tr>
<tr>
<td>GPIO_AD_05</td>
<td>LPUART8_RTS</td>
<td>RS-232</td>
</tr>
<tr>
<td>GPIO_SD_B2_05</td>
<td>FLEXSPI1_DQS</td>
<td>闪存编程（Flash Programming）</td>
</tr>
<tr>
<td>GPIO_SD_B2_06</td>
<td>FLEXSPI1_SS0</td>
<td>闪存编程（Flash Programming）</td>
</tr>
<tr>
<td>GPIO_SD_B2_07</td>
<td>FLEXSPI1_SCLK</td>
<td>闪存编程（Flash Programming）</td>
</tr>
<tr>
<td>GPIO_SD_B2_08</td>
<td>FLEXSPI1_DATA00</td>
<td>闪存编程（Flash Programming）</td>
</tr>
<tr>
<td>GPIO_SD_B2_09</td>
<td>FLEXSPI1_DATA01</td>
<td>闪存编程（Flash Programming）</td>
</tr>
<tr>
<td>GPIO_SD_B2_10</td>
<td>FLEXSPI1_DATA02</td>
<td>闪存编程（Flash Programming）</td>
</tr>
<tr>
<td>GPIO_SD_B2_11</td>
<td>FLEXSPI1_DATA03</td>
<td>闪存编程（Flash Programming）</td>
</tr>
<tr>
<td>GPIO_LPSR_00</td>
<td>CAN3_TX</td>
<td>FlexCAN</td>
</tr>
<tr>
<td>GPIO_LPSR_01</td>
<td>CAN3_RX</td>
<td>FlexCAN</td>
</tr>
<tr>
<td>GPIO_AD_17_SAI1_MCLK</td>
<td>SAI_MCLK</td>
<td>CODEC/SAI</td>
</tr>
<tr>
<td>GPIO_AD_20_SAI1_RX_DATA00</td>
<td>SAI1_RX_DATA00</td>
<td>CODEC/SAI</td>
</tr>
<tr>
<td>GPIO_AD_21_SAI1_TX_DATA00</td>
<td>SAI1_TX_DATA00</td>
<td>CODEC/SAI</td>
</tr>
<tr>
<td>GPIO_AD_22_SAI1_TX_BCLK</td>
<td>SAI1_TX_BCLK</td>
<td>CODEC/SAI</td>
</tr>
<tr>
<td>GPIO_AD_23_SAI1_TX_SYNC</td>
<td>SAI1_TX_SYNC</td>
<td>CODEC/SAI</td>
</tr>
<tr>
<td>GPIO_SD_B1_00</td>
<td>USDHC1_CMD</td>
<td>SD 主机控制器（SDHC）</td>
</tr>
<tr>
<td>GPIO_SD_B1_01</td>
<td>USDHC1_CLK</td>
<td>SD 主机控制器（SDHC）</td>
</tr>
<tr>
<td>GPIO_SD_B1_02</td>
<td>USDHC1_DATA0</td>
<td>SD 主机控制器（SDHC）</td>
</tr>
<tr>
<td>GPIO_SD_B1_03</td>
<td>USDHC1_DATA1</td>
<td>SD 主机控制器（SDHC）</td>
</tr>
<tr>
<td>GPIO_SD_B1_04</td>
<td>USDHC1_DATA2</td>
<td>SD 主机控制器（SDHC）</td>
</tr>
<tr>
<td>GPIO_SD_B1_05</td>
<td>USDHC1_DATA3</td>
<td>SD 主机控制器（SDHC）</td>
</tr>
<tr>
<td>GPIO_AD_09</td>
<td>USB_OTG1_ID</td>
<td>通用串行总线（USB）</td>
</tr>
<tr>
<td>GPIO_AD_10</td>
<td>USB_OTG1_PWR</td>
<td>通用串行总线（USB）</td>
</tr>
<tr>
<td>GPIO_AD_11</td>
<td>USB_OTG1_OC</td>
<td>通用串行总线（USB）</td>
</tr>
<tr>
<td>GPIO_AD_08</td>
<td>USB_OTG2_ID</td>
<td>通用串行总线（USB）</td>
</tr>
<tr>
<td>GPIO_AD_07</td>
<td>USB_OTG2_PWR</td>
<td>通用串行总线（USB）</td>
</tr>
<tr>
<td>GPIO_AD_06</td>
<td>USB_OTG2_OC</td>
<td>通用串行总线（USB）</td>
</tr>
</table>

<a id="dual-core-samples"></a>

## 双核示例（Dual Core Samples）

<table>
<tr>
<th>内核（Core）</th>
<th>启动地址（Boot Address）</th>
<th>备注（Comment）</th>
</tr>
<tr>
<td>Cortex-M7</td>
<td>0x30000000[630K]</td>
<td>主核（Primary Core）</td>
</tr>
<tr>
<td>Cortex-M4</td>
<td>0x20020000[96k]</td>
<td>从片上RAM（OCRAM）启动</td>
</tr>
</table>

<table>
<tr>
<th>存储器（Memory）</th>
<th>地址[容量]（Address[Size]）</th>
<th>备注（Comment）</th>
</tr>
<tr>
<td>flexspi1</td>
<td>0x30000000[16M]</td>
<td>Cortex-M7闪存</td>
</tr>
<tr>
<td>sdram0</td>
<td>0x80030000[64M]</td>
<td>Cortex-M7 RAM</td>
</tr>
<tr>
<td>ocram</td>
<td>0x20020000[512K]</td>
<td>Cortex-M4“闪存”区域，原文带引号</td>
</tr>
<tr>
<td>sram1</td>
<td>0x20000000[128K]</td>
<td>Cortex-M4 RAM</td>
</tr>
<tr>
<td>ocram2</td>
<td>0x200C0000[512K]</td>
<td>邮箱／共享内存（Mailbox / Shared Memory）</td>
</tr>
</table>

只有ocram2的前16 KB设有适合共享内存使用的MPU区域属性。

<a id="system-clock"></a>

### 系统时钟（System Clock）

MIMXRT1170配置为使用SysTick作为系统时钟源，原文列出的频率为996 MHz；面向M4核时也使用SysTick，频率为400 MHz。

启用电源管理后，板上的32 kHz低频振荡器将作为通用定时器（GPT）的时钟源，用于生成系统时钟。这有助于进入更低功耗状态，但会降低时间分辨率。

<a id="serial-port"></a>

### 串口（Serial Port）

MIMXRT1170有12路UART，LPUART1用作CM7控制台，LPUART6用作CM4控制台，LPUART8用于RS232，其余未使用。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

按通常方式构建并烧录应用，详见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）与“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

使用板载FTDI UART转USB芯片，将两路内部UART转换为USB接口X15。

在串口终端中使用以下设置，例如minicom或PuTTY：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

### 烧录（Flashing）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b phyboard_atlas/mimxrt1176/cm7 samples/hello_world
west flash
```

终端中应出现以下消息：

```text
***** Booting Zephyr OS v4.1.0-xxxx-xxxxxxxxxxxxx *****
Hello World! phyboard_atlas/mimxrt1176/cm7
```

<a id="debugging"></a>

### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b phyboard_atlas/mimxrt1176/cm7 samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
***** Booting Zephyr OS v4.1.0-xxxx-xxxxxxxxxxxxx *****
Hello World! phyboard_atlas/mimxrt1176/cm7
```

注意（Note）

使用J-Link 7.50或更新版本。原文说明调试仅支持运行CM4镜像，因为默认启动核为CM7；此限制按原文保留。

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.phytec.com/product/phycore-rt1170](https://www.phytec.com/product/phycore-rt1170)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.phytec.com/product/phyboard-rt1170-development-kit/](https://www.phytec.com/product/phyboard-rt1170-development-kit/)

## 译注

Atlas硬件为M7加M4双核，当前自动生成目标为CM7；原文调试段却称仅支持CM4镜像，已明确标注保留。

---

[上一章](P001_PHYTEC.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_phyBOARD-Electra_AM64x_M4F_Core.md)
