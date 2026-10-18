---
id: learning.zephyr-docs.boards-nxp-imx-rt10xx.page-8
title: MIMXRT1062-FMURT6
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1062_fmurt6/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mimxrt1062_fmurt6"></a>

# 第8章\_MIMXRT1062-FMURT6

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1062_fmurt6/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mimxrt1062_fmurt6.webp](images/mimxrt1062_fmurt6.webp)](images/mimxrt1062_fmurt6.webp)

MIMXRT1062-FMURT6

名称（Name）：

`mimxrt1062_fmurt6`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mimxrt1062](https://docs.zephyrproject.org/latest/boards/index.html#soc=mimxrt1062)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt1062_fmurt6/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

MIMXRT1062_FMURT6加入跨界处理器系列，原文说明它将i.MX RT系列扩展为3个可伸缩系列。

i.MX RT1062将片上SRAM倍增至1 MB，同时保持与RT1050引脚兼容。它增加适合实时应用的高速GPIO、CAN FD及同步并行NAND／NOR／PSRAM控制器等功能，采用最高600 MHz Arm Cortex-M7核。

<a id="hardware"></a>

## 硬件（Hardware）


- MIMXRT1062DVL6B微控制器，600 MHz、1024 KB片上存储器
- 存储器（Memory）


  - 256 Mbit同步动态RAM（SDRAM）
  - 512 Mbit HyperFlash闪存
  - SD卡TF插槽
- 以太网（Ethernet）


  - 10/100 Mbit/s以太网物理层收发器（Ethernet PHY）
- 通用串行总线（USB）


  - USB 2.0 OTG连接器
  - USB 2.0主机连接器
- 音频（Audio）


  - 3.5 mm立体声耳机插孔
  - 板载麦克风
  - 左右声道扬声器输出连接器
- 电源（Power）


  - 5 V直流电源插孔（DC Jack）
- 调试（Debug）


  - 20引脚JTAG连接器
  - 使用DAPLink的OpenSDA
- 传感器（Sensor）


  - BMI088六轴电子罗盘（E-compass），名称按原文保留
- 扩展端口（Expansion Port）


  - Arduino接口（Interface）
- CAN总线连接器

MIMXRT1062 SoC及MIMXRT1062-FMURT6开发板的更多信息见以下资料：


- [i.MX RT1060 网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/i.mx-rt1060-crossover-processor-with-arm-cortex-m7-core:i.MX-RT1060)
- [i.MX RT1060 参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=IMXRT1060RM)
- [MIMXRT1062-FMURT6 用户指南（User Guide）](https://docs.px4.io/main/en/)
- [MIMXRT1062-FMURT6 原理图（Schematics）](https://github.com/NXPHoverGames/NXP-FMUMRT6)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`mimxrt1062_fmurt6`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mimxrt1062_fmurt6-hw-features"></a>

<a id="mimxrt1062_fmurt6-mimxrt1062_fmurt6/mimxrt1062-hw-features-section"></a>

#### `mimxrt1062_fmurt6/mimxrt1062`目标（Target）

<a id="mimxrt1062_fmurt6-mimxrt1062_fmurt6/mimxrt1062-hw-features-panel"></a>

<a id="mimxrt1062_fmurt6-mimxrt1062_fmurt6/mimxrt1062-hw-features-memory"></a>

该开发板目标的片上存储容量：256 KiB RAM、64 MiB Flash。

<a id="mimxrt1062_fmurt6-mimxrt1062_fmurt6/mimxrt1062-hw-features-table"></a>

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
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUA 12B1MSPS逐次逼近模数转换器（SAR ADC），MCUA拼写沿用原文（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L631">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L641">已禁用：1</a>）</td>
<td><a href="../hardware/P852_NXPMCUX12位逐次逼近ADC绑定.md#dtbinding-nxp-mcux-12b1msps-sar"><code>nxp,mcux-12b1msps-sar</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX交叉开关（XBAR / Crossbar Switch）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1169">已禁用：3</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P016_nxp_mcux-xbar.md#std-dtcompatible-nxp-mcux-xbar"><code>nxp,mcux-xbar</code></a></td>
</tr>
<tr>
<td rowspan="2">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L978">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L988">已禁用：1</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P017_nxp_flexcan.md#std-dtcompatible-nxp-flexcan"><code>nxp,flexcan</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L998">已禁用：1</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="5">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>i.MX时钟控制模块（CCM / Clock Controller Module）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L311">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P021_nxp_imx-ccm.md#std-dtcompatible-nxp-imx-ccm"><code>nxp,imx-ccm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L317">已启用：3</a>）</td>
<td><a href="../timer_reference/P110_固定比例时钟绑定.md#dtbinding-fixed-factor-clock"><code>fixed-factor-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX CCM分数锁相环（Fractional PLL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L335">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P017_nxp_imx-ccm-fnpll.md#std-dtcompatible-nxp-imx-ccm-fnpll"><code>nxp,imx-ccm-fnpll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX模拟时钟控制模块（ANATOP / Analog Clock Controller Module）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1022">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P016_nxp_imx-anatop.md#std-dtcompatible-nxp-imx-anatop"><code>nxp,imx-anatop</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L75">已启用：4</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="6">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX通用定时器（GPT / General-Purpose Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L176">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P004_nxp_imx-gpt.md#std-dtcompatible-nxp-imx-gpt"><code>nxp,imx-gpt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX四通道定时器（QTMR / Quad Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L187">已启用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P005_nxp_imx-qtmr.md#std-dtcompatible-nxp-imx-qtmr"><code>nxp,imx-qtmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX四通道定时器通道（Quad Timer Channel）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L193">已禁用：16</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P007_nxp_imx-tmr.md#std-dtcompatible-nxp-imx-tmr"><code>nxp,imx-tmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SNVS低功耗／高功耗域实时时钟计数器（LP/HP Realtime Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L351">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P006_nxp_imx-snvs-rtc.md#std-dtcompatible-nxp-imx-snvs-rtc"><code>nxp,imx-snvs-rtc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP周期中断定时器（PIT / Periodic Interrupt Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1210">已禁用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P017_nxp_pit.md#std-dtcompatible-nxp-pit"><code>nxp,pit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>周期中断定时器节点的子节点，用于表示单个定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1220">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P016_nxp_pit-channel.md#std-dtcompatible-nxp-pit-channel"><code>nxp,pit-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>NXP数据协处理器（DCP / Data Co-Processor）密码加速器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1197">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P004_nxp_mcux-dcp.md#std-dtcompatible-nxp-mcux-dcp"><code>nxp,mcux-dcp</code></a></td>
</tr>
<tr>
<td rowspan="1">调试（Debug）</td>
<td>片上（On-Chip）</td>
<td>ARMv7仪器化跟踪宏单元（ITM / Instrumentation Trace Macrocell）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L44">已启用：1</a>）</td>
<td><a href="../debug_binding_reference/P001_ARMv7M_ITM调试绑定.md#std-dtcompatible-arm-armv7m-itm"><code>arm,armv7m-itm</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX增强型LCD接口（eLCDIF / Enhanced LCD Interface）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L495">已禁用：1</a>）</td>
<td><a href="../display_ilitek_matrix_nxp_binding_reference/P018_nxp_imx-elcdif.md#std-dtcompatible-nxp-imx-elcdif"><code>nxp,imx-elcdif</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L958">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP PXP二维DMA引擎（2D DMA Engine）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1035">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P005_nxp_pxp.md#std-dtcompatible-nxp-pxp"><code>nxp,pxp</code></a></td>
</tr>
<tr>
<td rowspan="5">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP ENET以太网IP模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L835">已启用：2</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P004_nxp_enet.md#std-dtcompatible-nxp-enet"><code>nxp,enet</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET MAC／二层（L2）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt1060.dtsi?plain=1#L40">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L840">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P001_nxp_enet-mac.md#std-dtcompatible-nxp-enet-mac"><code>nxp,enet-mac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET管理数据输入输出（MDIO）功能（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt1060.dtsi?plain=1#L49">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L849">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P002_nxp_enet-mdio.md#std-dtcompatible-nxp-enet-mdio"><code>nxp,enet-mdio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP ENET精确时间协议（PTP / Precision Time Protocol）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L856">已禁用：2</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P002_nxp_enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock"><code>nxp,enet-ptp-clock</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L433">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L368">已启用：9</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P030_nxp_imx-gpio.md#std-dtcompatible-nxp-imx-gpio"><code>nxp,imx-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L440">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L462">已禁用：1</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1043">已禁用：3</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L42">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="3">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexRAM片上RAM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L101">已启用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P015_nxp_flexram.md#std-dtcompatible-nxp-flexram"><code>nxp,flexram</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP智能外部存储器控制器（SEMC / Smart External Memory Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L160">已启用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P016_nxp_imx-semc.md#std-dtcompatible-nxp-imx-semc"><code>nxp,imx-semc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX SNVS低功耗通用寄存器，用作电池后备RAM（Battery-Backed RAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L363">已启用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P001_nxp_imx-snvs-gpr.md#std-dtcompatible-nxp-imx-snvs-gpr"><code>nxp,imx-snvs-gpr</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1245">已禁用：3</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>NXP FlexSPI HyperFlash闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L195">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P018_nxp_imx-flexspi-hyperflash.md#std-dtcompatible-nxp-imx-flexspi-hyperflash"><code>nxp,imx-flexspi-hyperflash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L215">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>NXP片上一次性可编程存储器（OCOTP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1253">已禁用：1</a>）</td>
<td><a href="../otp_binding_reference/P004_nxp_ocotp.md#std-dtcompatible-nxp-ocotp"><code>nxp,ocotp</code></a></td>
</tr>
<tr>
<td rowspan="3">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>这个兼容性绑定（Compatible Binding）应应用于设备的<code>iomuxc</code>设备树源文件（DTS）节点。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L484">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P023_nxp_imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc"><code>nxp,imx-iomuxc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>该节点在MCUX RT SoC设备树中设置了pinctrl节点标签（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L489">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P012_nxp_mcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl"><code>nxp,mcux-rt-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX I/O复用控制器（IOMUXC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1029">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P021_nxp_imx-gpr.md#std-dtcompatible-nxp-imx-gpr"><code>nxp,imx-gpr</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>包含mcux-pwm子模块的NXP eFLEX PWM模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L651">已启用：4</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P003_nxp_flexpwm.md#std-dtcompatible-nxp-flexpwm"><code>nxp,flexpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L702">已启用：8</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L656">已禁用：8</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P005_nxp_imx-pwm.md#std-dtcompatible-nxp-imx-pwm"><code>nxp,imx-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>板载（On-Board）</td>
<td>固定电压稳压器（Fixed Voltage Regulators）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L57">已启用：6</a>）</td>
<td><a href="../hardware/P635_固定稳压器设备树绑定.md#dtbinding-regulator-fixed"><code>regulator-fixed</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Kinetis真随机数发生器（TRNG / True Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L870">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P020_nxp_kinetis-trng.md#std-dtcompatible-nxp-kinetis-trng"><code>nxp,kinetis-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L927">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L939">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P014_nxp_imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc"><code>nxp,imx-usdhc</code></a></td>
</tr>
<tr>
<td rowspan="5">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>通过I2C访问的Bosch BMP388压力传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L274">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P020_bosch_bmp388.md#std-dtcompatible-bosch-bmp388"><code>bosch,bmp388</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Bosch BMM150地磁传感器（Geomagnetic Sensor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L286">已禁用：1</a>）</td>
<td><a href="../compatible_binding_reference/P018_bosch_bmm150.md#std-dtcompatible-bosch-bmm150"><code>bosch,bmm150</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通过SPI访问的STMicroelectronics ISM330DHCX六轴惯性测量单元（IMU）传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1062_fmurt6/mimxrt1062_fmurt6.dts?plain=1#L339">已禁用：1</a>）</td>
<td><a href="../compatible_binding_reference/P076_st_ism330dhcx.md#std-dtcompatible-st-ism330dhcx"><code>st,ism330dhcx</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX正交解码器（QDEC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1141">已禁用：4</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P008_nxp_mcux-qdec.md#std-dtcompatible-nxp-mcux-qdec"><code>nxp,mcux-qdec</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP片上温度监视器（On-Die Temperature Monitor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1204">已禁用：1</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P013_nxp_tempmon.md#std-dtcompatible-nxp-tempmon"><code>nxp,tempmon</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L561">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L551">已禁用：4</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L132">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L146">已禁用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L503">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L515">已禁用：2</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX通用硬件定时器（GPT / General-Purpose HW Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L169">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P007_nxp_gpt-hw-timer.md#std-dtcompatible-nxp-gpt-hw-timer"><code>nxp,gpt-hw-timer</code></a></td>
</tr>
<tr>
<td rowspan="3">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L877">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L887">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB主机控制器（Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L897">已禁用：2</a>）</td>
<td><a href="../usb_soc_binding_reference/P009_nxp_uhc-ehci.md#std-dtcompatible-nxp-uhc-ehci"><code>nxp,uhc-ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L915">已禁用：2</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td rowspan="1">视频（Video）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX CMOS传感器接口（Sensor Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L951">已禁用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P008_nxp_imx-csi.md#std-dtcompatible-nxp-imx-csi"><code>nxp,imx-csi</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>i.MX RT看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1008">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1015">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P009_nxp_imx-wdog.md#std-dtcompatible-nxp-imx-wdog"><code>nxp,imx-wdog</code></a></td>
</tr>
</table>

注意（Note）

尚未支持的其他功能可参考[MIMXRT1064-EVK](P009_MIMXRT1064-EVK.md#mimxrt1064_evk)，它是NXP i.MX RT10xx系列功能覆盖更广的开发板。NXP优先在该板落实Zephyr完整平台支持，因此该板可能已有可复用于mimxrt1060_evk的额外功能。

<a id="connections-and-i-os"></a>

### 连接与I/O（Connections and I/Os）

MIMXRT1062 SoC有5对引脚复用／GPIO控制器。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>GPIO_AD_B1_08</td>
<td>FLEXCAN1发送（TX）</td>
<td>控制器局域网（CAN）</td>
</tr>
<tr>
<td>GPIO_B0_03</td>
<td>FLEXCAN1接收（RX）</td>
<td>控制器局域网（CAN）</td>
</tr>
<tr>
<td>GPIO_AD_B0_06</td>
<td>PWM2A0</td>
<td>脉宽调制（PWM）</td>
</tr>
<tr>
<td>GPIO_EMC_08</td>
<td>PWM2A1</td>
<td>脉宽调制（PWM）</td>
</tr>
<tr>
<td>GPIO_EMC_10</td>
<td>PWM2A2</td>
<td>脉宽调制（PWM）</td>
</tr>
<tr>
<td>GPIO_AD_B0_09</td>
<td>PWM2A3</td>
<td>脉宽调制（PWM）</td>
</tr>
<tr>
<td>GPIO_EMC_31</td>
<td>LPUART7_TX</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>GPIO_EMC_32</td>
<td>LPUART7_RX</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>GPIO_B0_04</td>
<td>LPI2C2_SCL</td>
<td>集成电路间总线（I2C）</td>
</tr>
<tr>
<td>GPIO_B0_05</td>
<td>LPI2C2_SDA</td>
<td>集成电路间总线（I2C）</td>
</tr>
<tr>
<td>GPIO_AD_B1_00</td>
<td>LPI2C1_SCL</td>
<td>集成电路间总线（I2C）</td>
</tr>
<tr>
<td>GPIO_AD_B1_01</td>
<td>LPI2C1_SDA</td>
<td>集成电路间总线（I2C）</td>
</tr>
<tr>
<td>GPIO_AD_B0_12</td>
<td>LPI2C4_SCL</td>
<td>集成电路间总线（I2C）</td>
</tr>
<tr>
<td>GPIO_AD_B0_13</td>
<td>LPI2C4_SDA</td>
<td>集成电路间总线（I2C）</td>
</tr>
<tr>
<td>唤醒（WAKEUP）</td>
<td>通用输入输出（GPIO）</td>
<td>SW0</td>
</tr>
<tr>
<td>GPIO_B1_01</td>
<td>ENET_RX_DATA00</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_B1_02</td>
<td>ENET_RX_DATA01</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_B1_03</td>
<td>ENET_RX_EN</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_B0_12</td>
<td>ENET_TX_DATA00</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_B0_13</td>
<td>ENET_TX_DATA01</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_B0_14</td>
<td>ENET_TX_EN</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_B0_15</td>
<td>ENET_REF_CLK</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_B1_00</td>
<td>ENET_RX_ER</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_B1_12</td>
<td>通用输入输出（GPIO）</td>
<td>SD卡（SD Card）</td>
</tr>
<tr>
<td>GPIO_B1_14</td>
<td>USDHC1_VSELECT</td>
<td>SD卡（SD Card）</td>
</tr>
<tr>
<td>GPIO_EMC_40</td>
<td>ENET_MDC</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_B0_01</td>
<td>ENET_MDIO</td>
<td>以太网（Ethernet）</td>
</tr>
<tr>
<td>GPIO_SD_B0_00</td>
<td>USDHC1_CMD</td>
<td>SD卡（SD Card）</td>
</tr>
<tr>
<td>GPIO_SD_B0_01</td>
<td>USDHC1_CLK</td>
<td>SD卡（SD Card）</td>
</tr>
<tr>
<td>GPIO_SD_B0_02</td>
<td>USDHC1_DATA0</td>
<td>SD卡（SD Card）</td>
</tr>
<tr>
<td>GPIO_SD_B0_03</td>
<td>USDHC1_DATA1</td>
<td>SD卡（SD Card）</td>
</tr>
<tr>
<td>GPIO_SD_B0_04</td>
<td>USDHC1_DATA2</td>
<td>SD卡（SD Card）</td>
</tr>
<tr>
<td>GPIO_SD_B0_05</td>
<td>USDHC1_DATA3</td>
<td>SD卡（SD Card）</td>
</tr>
<tr>
<td>GPIO_EMC_27</td>
<td>LPSPI1_SCK</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>GPIO_EMC_28</td>
<td>LPSPI1_SDO</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>GPIO_EMC_29</td>
<td>LPSPI1_SDI</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>GPIO_EMC_00</td>
<td>LPSPI2_SCK</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>GPIO_EMC_02</td>
<td>LPSPI2_SDO</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>GPIO_EMC_03</td>
<td>LPSPI2_SDI</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>GPIO_AD_B1_15</td>
<td>LPSPI3_SCK</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>GPIO_AD_B1_14</td>
<td>LPSPI3_SDO</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>GPIO_AD_B1_13</td>
<td>LPSPI3_SDI</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>GPIO_AD_B1_11</td>
<td>模数转换器（ADC）</td>
<td>ADC1通道0</td>
</tr>
<tr>
<td>GPIO_AD_B1_09</td>
<td>模数转换器（ADC）</td>
<td>ADC1通道14</td>
</tr>
<tr>
<td>GPIO_AD_B0_15</td>
<td>模数转换器（ADC）</td>
<td>ADC1通道4</td>
</tr>
<tr>
<td>GPIO_AD_B1_02</td>
<td>UART2_TX_GPS1</td>
<td>GPS的UART</td>
</tr>
<tr>
<td>GPIO_AD_B1_03</td>
<td>UART2_RX_GPS1</td>
<td>GPS的UART</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

MIMXRT1062 SoC配置为使用SysTick作为系统时钟源，原文列出的运行频率为600 MHz。

启用电源管理后，板上的32 kHz低频振荡器将作为通用定时器（GPT）的时钟源，用于生成系统时钟。这有助于进入更低功耗状态，但会降低时间分辨率。

<a id="serial-port"></a>

### 串口（Serial Port）

MIMXRT1062 SoC有8路UART，LPUART7配置为控制台，LPUART8及LPUART2用于GPS／磁力计（MAG），LPUART3及LPUART4用于遥测（Telemetry），其余未使用。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`mimxrt1062_fmurt6`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

按通常方式构建并烧录应用，详见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）与“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

<a id="configuring-a-debug-probe"></a>

### 配置调试探针（Configuring a Debug Probe）

烧录及调试都使用调试探针。此板默认配置为使用OpenSDA DAPLink板载探针，但原文说明pyOCD尚不支持对此板外部闪存编程，因此必须改用以下探针之一。（[OpenSDA DAPLink板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#opensda-daplink-onboard-debug-probe)；[pyOCD调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#pyocd-debug-host-tools)）

<a id="using-j-link"></a>

<a id="using-j-link-rt1062"></a>

#### 使用J-Link

安装J-Link调试主机工具（Debug Host Tools），并确保工具位于搜索路径中。（[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)）

i.MX RT106x的HyperFlash支持需要J-Link V7.80或更高版本。

可将板载调试电路更新为Segger J-Link固件，或将外部J-Link接到FMURT6的J23 FMU调试端口。运行JLink.exe，将设备／内核选择为MIMXRT106A-ALEXA。（[J-Link外部调试探针（External Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#jlink-external-debug-probe)）

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

无论选择哪种调试探针，串行控制台都使用OpenSDA微控制器作为USB转串口适配器。

用USB线缆将PC连接PixHawk调试适配器。

在串口终端中使用以下设置，例如minicom或PuTTY：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="using-swo"></a>

#### 使用串行线输出（SWO）

设置CONFIG_LOG_BACKEND_SWO=y，可用SWO作为日志后端。SWO查看器应配置为CPU频率132 MHz、SWO频率7500 kHz，数值按原文保留。

<a id="flashing"></a>

### 烧录（Flashing）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b mimxrt1062_fmurt6 samples/hello_world
west flash
```

打开串口终端，按SW9复位开发板，终端应显示以下消息：

```text
***** Booting Zephyr OS v3.20.0 *****
Hello World! mimxrt1062_fmurt6
```

<a id="debugging"></a>

### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b mimxrt1062_fmurt6 samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
***** Booting Zephyr OS v3.20.0 *****
Hello World! mimxrt1062_fmurt6
```

<a id="troubleshooting"></a>

### 故障排查（Troubleshooting）

若west flash或调试命令失败，并停在runners.jlink执行阶段，请确认J-Link探针已正确配置、供电并连接FMURT6。

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)
- [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)
- [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- NXP Zephyr主页，包含培训资源（[NXP的Zephyr专题页面](https://nxp.com/zephyr)）
- [NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## 译注

原文将BMI088称为六轴电子罗盘，按来源保留。控制台为LPUART7；GPS／MAG及遥测使用其他UART。J-Link设备ID为MIMXRT106A-ALEXA，HyperFlash要求J-Link V7.80或更高版本。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [i.mx-rt1060-crossover-processor-with-arm-cortex-m7-core:i.MX-RT1060](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/i.mx-rt1060-crossover-processor-with-arm-cortex-m7-core:i.MX-RT1060)：HTTP Error 404: Not Found。
- [Download?colCode=IMXRT1060RM](https://www.nxp.com/webapp/Download?colCode=IMXRT1060RM)：HTTP Error 404: Not Found。

---

[上一章](P007_MIMXRT1060-EVK.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_MIMXRT1064-EVK.md)
