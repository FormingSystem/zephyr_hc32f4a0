---
id: learning.zephyr-docs.boards-nxp-imx-rt-multicore.page-3
title: MIMXRT1180-EVK
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1180_evk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mimxrt1180_evk"></a>

# 第3章\_MIMXRT1180-EVK

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1180_evk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mimxrt1180_evk.webp](images/mimxrt1180_evk.webp)](images/mimxrt1180_evk.webp)

MIMXRT1180-EVK

名称（Name）：

`mimxrt1180_evk`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mimxrt1189](https://docs.zephyrproject.org/latest/boards/index.html#soc=mimxrt1189)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt1180_evk/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

双核i.MX RT1180的Cortex-M33运行于240 MHz，Cortex-M7运行于792 MHz。此MCU支持宽温度范围，面向消费、工业及汽车市场并具备相应资质。

<a id="hardware"></a>

## 硬件（Hardware）


- MIMXRT1189CVM8C微控制器


  - 240 MHz Cortex-M33，带256 KB TCM及16 KB缓存（Cache）
  - 792 MHz Cortex-M7，带512 KB TCM及32 KB缓存
  - 1.5 MB SRAM
- 存储器（Memory）


  - 512 Mbit同步动态RAM（SDRAM）
  - 128 Mbit QSPI闪存
  - 512 Mbit HyperRAM
  - SD卡TF插槽
- 以太网（Ethernet）


  - 1000 Mbit/s以太网PHY
- 通用串行总线（USB）


  - 两个USB 2.0 OTG连接器
- 音频（Audio）


  - 3.5 mm立体声耳机插孔
  - 板载麦克风
  - 左右声道扬声器输出连接器
- 电源（Power）


  - 5 V直流电源插孔（DC Jack）
- 调试（Debug）


  - 20引脚JTAG连接器
  - 使用DAPLink的MCU-Link
- 扩展端口（Expansion Port）


  - Arduino接口（Interface）
- CAN总线连接器

MIMXRT1180 SoC及MIMXRT1180-EVK开发板的更多信息见以下资料：


- [i.MX RT1180网站](https://www.nxp.com/products/i.MX-RT1180)
- [i.MX RT1180数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/IMXRT1180EC.pdf)
- [i.MX RT1180参考手册（Reference Manual）](https://www.nxp.com/docs/en/reference-manual/IMXRT1180RM.pdf)
- [MIMXRT1180-EVK 网站](https://www.nxp.com/design/design-center/development-boards-and-designs/MIMXRT1180-EVK)
- [MIMXRT1180-EVK 开发板硬件用户指南（Board Hardware User’s Guide）](https://www.nxp.com/webapp/Download?colCode=UM12021&isHTMLorPDF=HTML)

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
<td>W9825G6KH</td>
<td>智能外部存储器控制器（SEMC）</td>
<td>通过设备配置数据块（DCD / Device Configuration Data Block）启用，该数据块在启动时设置智能外部存储器控制器（SEMC）。</td>
</tr>
<tr>
<td>W25Q128JWSIQ</td>
<td>FLEXSPI</td>
<td>通过闪存配置块（Flash Configuration Block）启用，该配置块在启动时设置FlexSPI。</td>
</tr>
</table>

<a id="supported-features"></a>

### 支持的功能（Supported Features）

NXP将MIMXRT1180-EVK视为i.MX RT118x系列功能覆盖更广的开发板，将其作为Zephyr完整平台支持的重点，并优先在该板启用新功能，以服务整个RT118x系列。

`mimxrt1180_evk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mimxrt1180_evk-hw-features"></a>

<a id="mimxrt1180_evk-mimxrt1180_evk/mimxrt1189/cm33-hw-features-section"></a>

#### `mimxrt1180_evk/mimxrt1189/cm33`目标（Target）

<a id="mimxrt1180_evk-mimxrt1180_evk/mimxrt1189/cm33-hw-features-panel"></a>

<a id="mimxrt1180_evk-mimxrt1180_evk/mimxrt1189/cm33-hw-features-memory"></a>

该开发板目标的片上存储容量：8 MiB RAM、16 MiB Flash。

<a id="mimxrt1180_evk-mimxrt1180_evk/mimxrt1189/cm33-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L442">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L456">已禁用：1</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX交叉开关（XBAR / Crossbar Switch）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1704">已禁用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P016_nxp_mcux-xbar.md#std-dtcompatible-nxp-mcux-xbar"><code>nxp,mcux-xbar</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>板载（On-Board）</td>
<td>WM8962音频编解码器（Audio Codec）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L344">已启用：1</a>）</td>
<td><a href="../audio_stm32_ti_wolfson_binding_reference/P013_wolfson_wm8962.md#std-dtcompatible-wolfson-wm8962"><code>wolfson,wm8962</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L861">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L837">已禁用：2</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="4">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>i.MX模拟时钟控制模块（ANATOP / Analog Clock Controller Module）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P016_nxp_imx-anatop.md#std-dtcompatible-nxp-imx-anatop"><code>nxp,imx-anatop</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX第2版时钟控制模块（CCM）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L109">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P018_nxp_imx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2"><code>nxp,imx-ccm-rev2</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX RT118x ARM PLL时钟提供者（Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L120">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P030_nxp_imxrt118x-arm-pll.md#std-dtcompatible-nxp-imxrt118x-arm-pll"><code>nxp,imxrt118x-arm-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L127">已启用：2</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis模拟比较器（ACMP / Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L414">已禁用：4</a>）</td>
<td><a href="../hardware/P745_NXPKinetis模拟比较器绑定.md#dtbinding-nxp-kinetis-acmp"><code>nxp,kinetis-acmp</code></a></td>
</tr>
<tr>
<td rowspan="8">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX通用定时器（GPT / General-Purpose Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L403">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L391">已禁用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P004_nxp_imx-gpt.md#std-dtcompatible-nxp-imx-gpt"><code>nxp,imx-gpt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX四通道定时器（QTMR / Quad Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L494">已启用：8</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P005_nxp_imx-qtmr.md#std-dtcompatible-nxp-imx-qtmr"><code>nxp,imx-qtmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX四通道定时器通道（Quad Timer Channel）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L500">已禁用：32</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P007_nxp_imx-tmr.md#std-dtcompatible-nxp-imx-tmr"><code>nxp,imx-tmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP系统计数器（SYS_CTR / System Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L873">已禁用：1</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P002_nxp_sysctr.md#std-dtcompatible-nxp-sysctr"><code>nxp,sysctr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗周期中断定时器（LPIT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L887">已禁用：3</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P012_nxp_lpit.md#std-dtcompatible-nxp-lpit"><code>nxp,lpit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>低功耗周期中断定时器节点的子节点，表示一个独立定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L897">已禁用：12</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P011_nxp_lpit-channel.md#std-dtcompatible-nxp-lpit-channel"><code>nxp,lpit-channel</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗定时器（LPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L992">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1003">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr"><code>nxp,lptmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP时间戳定时器（TSTMR / Time Stamp Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1025">已启用：2</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P004_nxp_tstmr.md#std-dtcompatible-nxp-tstmr"><code>nxp,tstmr</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX 12位数模转换器（DAC12）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L472">已启用：1</a>）</td>
<td><a href="../hardware/P765_NXPDAC12数模转换器绑定.md#dtbinding-nxp-dac12"><code>nxp,dac12</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1355">已启用：2</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="1">分布式交换架构（DSA）</td>
<td>片上（On-Chip）</td>
<td>分布式交换架构（DSA）交换机（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L788">已启用：1</a>）</td>
<td><a href="../network_radio_frontend_binding_reference/P001_nxp_netc-switch.md#std-dtcompatible-nxp-netc-switch"><code>nxp,netc-switch</code></a></td>
</tr>
<tr>
<td rowspan="1">错误检测与纠正（EDAC）</td>
<td>片上（On-Chip）</td>
<td>NXP存储器ECC控制器（MECC）的错误检测与纠正（EDAC）绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L368">已启用：2</a>）</td>
<td><a href="../edac_syscon_binding_reference/P004_nxp_mecc.md#std-dtcompatible-nxp-mecc"><code>nxp,mecc</code></a></td>
</tr>
<tr>
<td rowspan="6">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L742">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P008_nxp_imx-netc.md#std-dtcompatible-nxp-imx-netc"><code>nxp,imx-netc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC物理站点接口（PSI / Physical Station Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L748">已启用：2</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P006_nxp_imx-netc-psi.md#std-dtcompatible-nxp-imx-netc-psi"><code>nxp,imx-netc-psi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP NETC精确时间协议（PTP）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L770">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P009_nxp_netc-ptp-clock.md#std-dtcompatible-nxp-netc-ptp-clock"><code>nxp,netc-ptp-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC外部MDIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L777">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P003_nxp_imx-netc-emdio.md#std-dtcompatible-nxp-imx-netc-emdio"><code>nxp,imx-netc-emdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L53">已启用：2</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Realtek RTL8211F以太网物理层（PHY）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L59">已启用：3</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P012_realtek_rtl8211f.md#std-dtcompatible-realtek-rtl8211f"><code>realtek,rtl8211f</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX快速通用输入输出（RGPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L254">已启用：6</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P001_nxp_imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio"><code>nxp,imx-rgpio</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP SRC第2版复位原因标志读取（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1239">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P007_nxp_imx-src-rev2.md#std-dtcompatible-nxp-imx-src-rev2"><code>nxp,imx-src-rev2</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件自旋锁（Hardware Spinlock）</td>
<td>片上（On-Chip）</td>
<td>NXP SEMA42硬件信号量（Hardware Semaphore）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1688">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1696">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42"><code>nxp,sema42</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L302">已禁用：6</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1580">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1607">已禁用：3</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1318">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1305">已禁用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="2">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>NXP KPP控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1421">已启用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P010_nxp_mcux-kpp.md#std-dtcompatible-nxp-mcux-kpp"><code>nxp,mcux-kpp</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>用作Zephyr邮箱（MBOX）的NXP i.MX消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x_cm33.dtsi?plain=1#L68">已启用：2</a>）</td>
<td><a href="../intercore_reference/P047_NXPiMX消息单元邮箱绑定.md#dtbinding-nxp-mbox-imx-mu"><code>nxp,mbox-imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP AHB SRAM控制器（SRAMC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1796">已禁用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P002_nxp_sramc.md#std-dtcompatible-nxp-sramc"><code>nxp,sramc</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1039">已禁用：2</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>NXP FlexSPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L207">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P023_nxp_imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor"><code>nxp,imx-flexspi-nor</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L219">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="5">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>这个兼容性绑定（Compatible Binding）应应用于设备的<code>iomuxc</code>设备树源文件（DTS）节点。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L79">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P023_nxp_imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc"><code>nxp,imx-iomuxc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>该节点在MCUX RT SoC设备树中设置了pinctrl节点标签（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L83">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P013_nxp_mcux-rt11xx-pinctrl.md#std-dtcompatible-nxp-mcux-rt11xx-pinctrl"><code>nxp,mcux-rt11xx-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>该节点在MCUX RT SoC设备树中设置了pinctrl节点标签（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L89">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P012_nxp_mcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl"><code>nxp,mcux-rt-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX BLK CTRL NS AONMIX模块控制（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L95">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P019_nxp_imx-blkctrl-ns-aon.md#std-dtcompatible-nxp-imx-blkctrl-ns-aon"><code>nxp,imx-blkctrl-ns-aon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX BLK CTRL WAKEUP模块控制（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L102">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P020_nxp_imx-blkctrl-wakeup.md#std-dtcompatible-nxp-imx-blkctrl-wakeup"><code>nxp,imx-blkctrl-wakeup</code></a></td>
</tr>
<tr>
<td rowspan="3">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>包含mcux-pwm子模块的NXP eFLEX PWM模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1055">已启用：4</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P003_nxp_flexpwm.md#std-dtcompatible-nxp-flexpwm"><code>nxp,flexpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1116">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1060">已禁用：15</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P005_nxp_imx-pwm.md#std-dtcompatible-nxp-imx-pwm"><code>nxp,imx-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1245">已禁用：6</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P008_nxp_kinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm"><code>nxp,kinetis-tpm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>NXP VREF SoC外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L481">已禁用：1</a>）</td>
<td><a href="../hardware/P652_NXP参考电压绑定.md#dtbinding-nxp-vref"><code>nxp,vref</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1331">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1343">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P014_nxp_imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc"><code>nxp,imx-usdhc</code></a></td>
</tr>
<tr>
<td rowspan="2">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>NXP温度传感器（TMPSNS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1573">已启用：1</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P015_nxp_tmpsns.md#std-dtcompatible-nxp-tmpsns"><code>nxp,tmpsns</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型正交解码器（EQDC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1713">已禁用：4</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P006_nxp_mcux-eqdc.md#std-dtcompatible-nxp-mcux-eqdc"><code>nxp,mcux-eqdc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L134">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L144">已禁用：11</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1443">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1409">已禁用：5</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x_cm33.dtsi?plain=1#L47">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x_cm33.dtsi?plain=1#L52">已禁用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td rowspan="2">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1541">已启用：2</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1561">已启用：2</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>NXP外部看门狗监测器（External Watchdog Monitor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1400">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P007_nxp_ewm.md#std-dtcompatible-nxp-ewm"><code>nxp,ewm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP RT看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1491">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1501">已禁用：4</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P012_nxp_rtwdog.md#std-dtcompatible-nxp-rtwdog"><code>nxp,rtwdog</code></a></td>
</tr>
</table>

<a id="mimxrt1180_evk-mimxrt1180_evk/mimxrt1189/cm7-hw-features-section"></a>

#### `mimxrt1180_evk/mimxrt1189/cm7`目标（Target）

<a id="mimxrt1180_evk-mimxrt1180_evk/mimxrt1189/cm7-hw-features-panel"></a>

<a id="mimxrt1180_evk-mimxrt1180_evk/mimxrt1189/cm7-hw-features-memory"></a>

该开发板目标的片上存储容量：256 KiB RAM、256 KiB Flash。

<a id="mimxrt1180_evk-mimxrt1180_evk/mimxrt1189/cm7-hw-features-table"></a>

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
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L38">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L442">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L456">已禁用：1</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX交叉开关（XBAR / Crossbar Switch）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1704">已禁用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P016_nxp_mcux-xbar.md#std-dtcompatible-nxp-mcux-xbar"><code>nxp,mcux-xbar</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>板载（On-Board）</td>
<td>WM8962音频编解码器（Audio Codec）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L344">已启用：1</a>）</td>
<td><a href="../audio_stm32_ti_wolfson_binding_reference/P013_wolfson_wm8962.md#std-dtcompatible-wolfson-wm8962"><code>wolfson,wm8962</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L861">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L837">已禁用：2</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="4">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>i.MX模拟时钟控制模块（ANATOP / Analog Clock Controller Module）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P016_nxp_imx-anatop.md#std-dtcompatible-nxp-imx-anatop"><code>nxp,imx-anatop</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX第2版时钟控制模块（CCM）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L109">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P018_nxp_imx-ccm-rev2.md#std-dtcompatible-nxp-imx-ccm-rev2"><code>nxp,imx-ccm-rev2</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX RT118x ARM PLL时钟提供者（Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L120">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P030_nxp_imxrt118x-arm-pll.md#std-dtcompatible-nxp-imxrt118x-arm-pll"><code>nxp,imxrt118x-arm-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L127">已启用：2</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis模拟比较器（ACMP / Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L414">已禁用：4</a>）</td>
<td><a href="../hardware/P745_NXPKinetis模拟比较器绑定.md#dtbinding-nxp-kinetis-acmp"><code>nxp,kinetis-acmp</code></a></td>
</tr>
<tr>
<td rowspan="8">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX通用定时器（GPT / General-Purpose Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L403">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L391">已禁用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P004_nxp_imx-gpt.md#std-dtcompatible-nxp-imx-gpt"><code>nxp,imx-gpt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX四通道定时器（QTMR / Quad Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L494">已启用：8</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P005_nxp_imx-qtmr.md#std-dtcompatible-nxp-imx-qtmr"><code>nxp,imx-qtmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX四通道定时器通道（Quad Timer Channel）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L500">已禁用：32</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P007_nxp_imx-tmr.md#std-dtcompatible-nxp-imx-tmr"><code>nxp,imx-tmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP系统计数器（SYS_CTR / System Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L873">已禁用：1</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P002_nxp_sysctr.md#std-dtcompatible-nxp-sysctr"><code>nxp,sysctr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗周期中断定时器（LPIT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L887">已禁用：3</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P012_nxp_lpit.md#std-dtcompatible-nxp-lpit"><code>nxp,lpit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>低功耗周期中断定时器节点的子节点，表示一个独立定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L897">已禁用：12</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P011_nxp_lpit-channel.md#std-dtcompatible-nxp-lpit-channel"><code>nxp,lpit-channel</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗定时器（LPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L992">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1003">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr"><code>nxp,lptmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP时间戳定时器（TSTMR / Time Stamp Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1025">已启用：2</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P004_nxp_tstmr.md#std-dtcompatible-nxp-tstmr"><code>nxp,tstmr</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX 12位数模转换器（DAC12）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L472">已启用：1</a>）</td>
<td><a href="../hardware/P765_NXPDAC12数模转换器绑定.md#dtbinding-nxp-dac12"><code>nxp,dac12</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1355">已启用：2</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="1">分布式交换架构（DSA）</td>
<td>片上（On-Chip）</td>
<td>分布式交换架构（DSA）交换机（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L788">已启用：1</a>）</td>
<td><a href="../network_radio_frontend_binding_reference/P001_nxp_netc-switch.md#std-dtcompatible-nxp-netc-switch"><code>nxp,netc-switch</code></a></td>
</tr>
<tr>
<td rowspan="1">错误检测与纠正（EDAC）</td>
<td>片上（On-Chip）</td>
<td>NXP存储器ECC控制器（MECC）的错误检测与纠正（EDAC）绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L368">已启用：2</a>）</td>
<td><a href="../edac_syscon_binding_reference/P004_nxp_mecc.md#std-dtcompatible-nxp-mecc"><code>nxp,mecc</code></a></td>
</tr>
<tr>
<td rowspan="6">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L742">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P008_nxp_imx-netc.md#std-dtcompatible-nxp-imx-netc"><code>nxp,imx-netc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC物理站点接口（PSI / Physical Station Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L748">已启用：2</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P006_nxp_imx-netc-psi.md#std-dtcompatible-nxp-imx-netc-psi"><code>nxp,imx-netc-psi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP NETC精确时间协议（PTP）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L770">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P009_nxp_netc-ptp-clock.md#std-dtcompatible-nxp-netc-ptp-clock"><code>nxp,netc-ptp-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC外部MDIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L777">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P003_nxp_imx-netc-emdio.md#std-dtcompatible-nxp-imx-netc-emdio"><code>nxp,imx-netc-emdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L53">已启用：2</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Realtek RTL8211F以太网物理层（PHY）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L59">已启用：3</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P012_realtek_rtl8211f.md#std-dtcompatible-realtek-rtl8211f"><code>realtek,rtl8211f</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX快速通用输入输出（RGPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L254">已启用：6</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P001_nxp_imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio"><code>nxp,imx-rgpio</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP SRC第2版复位原因标志读取（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1239">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P007_nxp_imx-src-rev2.md#std-dtcompatible-nxp-imx-src-rev2"><code>nxp,imx-src-rev2</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件自旋锁（Hardware Spinlock）</td>
<td>片上（On-Chip）</td>
<td>NXP SEMA42硬件信号量（Hardware Semaphore）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1688">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1696">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42"><code>nxp,sema42</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L302">已禁用：6</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1580">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1607">已禁用：3</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1318">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1305">已禁用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="2">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>NXP KPP控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1421">已启用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P010_nxp_mcux-kpp.md#std-dtcompatible-nxp-mcux-kpp"><code>nxp,mcux-kpp</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>用作Zephyr邮箱（MBOX）的NXP i.MX消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x_cm7.dtsi?plain=1#L55">已启用：2</a>）</td>
<td><a href="../intercore_reference/P047_NXPiMX消息单元邮箱绑定.md#dtbinding-nxp-mbox-imx-mu"><code>nxp,mbox-imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP AHB SRAM控制器（SRAMC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1796">已禁用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P002_nxp_sramc.md#std-dtcompatible-nxp-sramc"><code>nxp,sramc</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1039">已禁用：2</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L47">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>NXP FlexSPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L207">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P023_nxp_imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor"><code>nxp,imx-flexspi-nor</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/mimxrt1180_evk.dtsi?plain=1#L219">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="5">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>这个兼容性绑定（Compatible Binding）应应用于设备的<code>iomuxc</code>设备树源文件（DTS）节点。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L79">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P023_nxp_imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc"><code>nxp,imx-iomuxc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>该节点在MCUX RT SoC设备树中设置了pinctrl节点标签（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L83">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P013_nxp_mcux-rt11xx-pinctrl.md#std-dtcompatible-nxp-mcux-rt11xx-pinctrl"><code>nxp,mcux-rt11xx-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>该节点在MCUX RT SoC设备树中设置了pinctrl节点标签（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L89">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P012_nxp_mcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl"><code>nxp,mcux-rt-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX BLK CTRL NS AONMIX模块控制（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L95">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P019_nxp_imx-blkctrl-ns-aon.md#std-dtcompatible-nxp-imx-blkctrl-ns-aon"><code>nxp,imx-blkctrl-ns-aon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX BLK CTRL WAKEUP模块控制（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L102">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P020_nxp_imx-blkctrl-wakeup.md#std-dtcompatible-nxp-imx-blkctrl-wakeup"><code>nxp,imx-blkctrl-wakeup</code></a></td>
</tr>
<tr>
<td rowspan="3">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>包含mcux-pwm子模块的NXP eFLEX PWM模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1055">已启用：4</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P003_nxp_flexpwm.md#std-dtcompatible-nxp-flexpwm"><code>nxp,flexpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1116">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1060">已禁用：15</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P005_nxp_imx-pwm.md#std-dtcompatible-nxp-imx-pwm"><code>nxp,imx-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1245">已禁用：6</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P008_nxp_kinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm"><code>nxp,kinetis-tpm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>NXP VREF SoC外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L481">已禁用：1</a>）</td>
<td><a href="../hardware/P652_NXP参考电压绑定.md#dtbinding-nxp-vref"><code>nxp,vref</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1331">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1343">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P014_nxp_imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc"><code>nxp,imx-usdhc</code></a></td>
</tr>
<tr>
<td rowspan="2">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>NXP温度传感器（TMPSNS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1573">已禁用：1</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P015_nxp_tmpsns.md#std-dtcompatible-nxp-tmpsns"><code>nxp,tmpsns</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型正交解码器（EQDC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1713">已禁用：4</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P006_nxp_mcux-eqdc.md#std-dtcompatible-nxp-mcux-eqdc"><code>nxp,mcux-eqdc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L244">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L134">已禁用：11</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1443">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1409">已禁用：5</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x_cm7.dtsi?plain=1#L34">已禁用：2</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="2">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1541">已启用：2</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1561">已启用：2</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>NXP外部看门狗监测器（External Watchdog Monitor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1400">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P007_nxp_ewm.md#std-dtcompatible-nxp-ewm"><code>nxp,ewm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP RT看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1491">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1501">已禁用：4</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P012_nxp_rtwdog.md#std-dtcompatible-nxp-rtwdog"><code>nxp,rtwdog</code></a></td>
</tr>
</table>

<a id="connections-and-i-os"></a>

### 连接与I/O（Connections and I/Os）

MIMXRT1180 SoC有6对引脚复用／GPIO控制器。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>GPIO_AON_04</td>
<td>通用输入输出（GPIO）</td>
<td>SW8</td>
</tr>
<tr>
<td>GPIO_AD_27</td>
<td>通用输入输出（GPIO）</td>
<td>发光二极管（LED）</td>
</tr>
<tr>
<td>GPIO_AON_08</td>
<td>LPUART1_TX</td>
<td>M33核UART控制台</td>
</tr>
<tr>
<td>GPIO_AON_09</td>
<td colspan="2">LPUART1_RX | M33核UART控制台</td>
</tr>
<tr>
<td>GPIO_AON_19</td>
<td colspan="2">LPUART12_TX | M7核UART控制台</td>
</tr>
<tr>
<td>GPIO_AON_20</td>
<td>LPUART12_RX</td>
<td>M7核UART控制台</td>
</tr>
<tr>
<td>GPIO_SD_B1_00</td>
<td colspan="2">SPI1_CS0 | SPI</td>
</tr>
<tr>
<td>GPIO_SD_B1_01</td>
<td colspan="2">SPI1_CLK | SPI</td>
</tr>
<tr>
<td>GPIO_SD_B1_02</td>
<td colspan="2">SPI1_SDO | SPI</td>
</tr>
<tr>
<td>GPIO_SD_B1_03</td>
<td colspan="2">SPI1_SDI | SPI</td>
</tr>
</table>

M7核UART连接到USB转UART连接器J60；也可断开JP7，在MCU-Link的J53连接器上启用第二路UART。

<a id="system-clock"></a>

### 系统时钟（System Clock）

MIMXRT1180配置为使用SysTick作为系统时钟源，原文列出的频率为240 MHz；面向M7核时也使用SysTick，频率为792 MHz。

<a id="ele-active-timer-requirement"></a>

### ELE活动定时器要求（Active Timer Requirement）

RT1180平台要求定期与EdgeLock安全隔离区（ELE）通信，否则会触发系统复位。根据RT1180系统参考手册（SRM）第3.11节“ELE active timer”，至少每24小时向ELE发送一次ping。

Zephyr通过软件定时器每23小时自动向ELE发送一次ping，为可能的时钟误差留出余量。此机制对应用透明，无需用户干预。

详情见RT1180 SRM第3.11节。

<a id="itcm-and-dtcm"></a>

### 指令及数据紧耦合存储器（ITCM / DTCM）

若将zephyr,flash放入ITCM，或将zephyr,sram放入DTCM，应从对应存储器设备节点删除zephyr,memory-region属性。例如，以下覆盖文件将CM33的zephyr,sram移到DTCM：

```text
boards/nxp/mimxrt1180_evk/cm33_sram_dtcm.overlay
```

<a id="serial-port"></a>

### 串口（Serial Port）

MIMXRT1180 SoC有12路UART，LPUART1配置为CM33控制台，LPUART12配置为CM7控制台，其余未使用。

<a id="ethernet"></a>

### 以太网（Ethernet）

NETC以太网驱动支持管理物理站点接口（PSI），NETC DSA驱动支持管理交换机端口。当前DSA仅支持交换功能，尚不能通过DSA主端口管理；主端口支持仍待实现。

```text
                +--------+                  +--------+
                | ENETC1 |                  | ENETC0 |
                |        |                  |        |
                | Pseudo |                  |  1G    |
                |  MAC   |                  |  MAC   |
                +--------+                  +--------+
                    | zero copy interface       |
+-------------- +--------+----------------+     |
|               | Pseudo |                |     |
|               |  MAC   |                |     |
|               |        |                |     |
|               | Port 4 |                |     |
|               +--------+                |     |
|           SWITCH       CORE             |     |
+--------+ +--------+ +--------+ +--------+     |
| Port 0 | | Port 1 | | Port 2 | | Port 3 |     |
|        | |        | |        | |        |     |
|  1G    | |  1G    | |  1G    | |  1G    |     |
|  MAC   | |  MAC   | |  MAC   | |  MAC   |     |
+--------+-+--------+-+--------+-+--------+     |
    |          |          |          |          |
NETC External Interfaces (4 switch ports, 1 end-point port)
```

<a id="dual-core-operation"></a>

## 双核运行（Dual Core Operation）

MIMXRT1180 EVK支持Cortex-M33及Cortex-M7双核运行。CM33默认是启动核，负责初始化系统并启动CM7。

<a id="cm7-execution-modes"></a>

### CM7执行模式（Execution Modes）

CM7可从以下3种存储器执行代码：


1. ITCM，默认：将CM7代码从闪存复制到指令紧耦合存储器（ITCM）后执行，速度较快，但代码容量受ITCM限制。
2. 闪存（Flash）：CM7直接从闪存就地执行（XIP），支持更大的代码容量，但可能比ITCM慢。CM7从闪存启动时，必须由CM33配置可信资源域控制器（TRDC）的执行权限。
3. HyperRAM：将CM7代码从闪存复制到外部HyperRAM后执行，支持更大的代码容量，但可能比ITCM慢。注意，CM33的默认数据区zephyr,sram也在HyperRAM中，必须避免两核占用区域重叠。下文提供把CM33数据移到DTCM的方案。

<a id="configuring-cm7-execution-memory"></a>

### 配置CM7代码执行存储器

使用以下Kconfig选项配置CM7执行存储器：

```text
CONFIG_CM7_BOOT_FROM_FLASH=n  # For RAM execution, ITCM or HyperRAM (default)
CONFIG_CM7_BOOT_FROM_FLASH=y  # For flash execution
```

通过west构建时，可在命令行指定该选项：

```text
 # For ITCM execution (default)
 west build -b mimxrt1180_evk/mimxrt1189/cm33 samples/drivers/mbox --sysbuild

 # For flash execution
 west build -b mimxrt1180_evk/mimxrt1189/cm33 <sample_path> --sysbuild -- \
   -D<remote_app_name>_EXTRA_DTC_OVERLAY_FILE=${ZEPHYR_BASE}/boards/nxp/mimxrt1180_evk/cm7_flash_boot.overlay \
   -DCONFIG_CM7_BOOT_FROM_FLASH=y -D<remote_app_name>_CONFIG_CM7_BOOT_FROM_FLASH=y

west build -b mimxrt1180_evk/mimxrt1189/cm33 samples/drivers/mbox --sysbuild -- \
   -Dremote_EXTRA_DTC_OVERLAY_FILE=${ZEPHYR_BASE}/boards/nxp/mimxrt1180_evk/cm7_flash_boot.overlay \
   -DCONFIG_CM7_BOOT_FROM_FLASH=y -Dremote_CONFIG_CM7_BOOT_FROM_FLASH=y

 # For HyperRAM execution
 west build -b mimxrt1180_evk//cm33 samples/drivers/mbox --sysbuild -- \
   -Dremote_EXTRA_DTC_OVERLAY_FILE=${ZEPHYR_BASE}/boards/nxp/mimxrt1180_evk/cm7_code_hyperram.overlay \
   -DEXTRA_DTC_OVERLAY_FILE=${ZEPHYR_BASE}/boards/nxp/mimxrt1180_evk/cm33_sram_dtcm.overlay
```

<a id="flash-boot-overlay"></a>

### 闪存启动覆盖文件（Flash Boot Overlay）

CM7从闪存执行时，需要应用设备树覆盖文件，正确配置闪存。文件位于：

```text
boards/nxp/mimxrt1180_evk/cm7_flash_boot.overlay
```

此覆盖文件将CM7代码执行位置从ITCM改为闪存。

<a id="hyperram-execution-overlay"></a>

### HyperRAM执行覆盖文件（HyperRAM Execution Overlay）

CM7从HyperRAM执行时，需要应用设备树覆盖文件，示例文件位于：

```text
boards/nxp/mimxrt1180_evk/cm7_code_hyperram.overlay
```

还需在以下文件中修改板卡MPU属性：

```text
boards/nxp/mimxrt1180_evk/cm7/mpu_regions.c
```

修改以下代码行，设置flash属性，使HyperRAM区域允许执行代码：

```text
#if DT_NODE_HAS_STATUS_OKAY(DT_NODELABEL(hyperram0))
     MPU_REGION_ENTRY("HYPER_RAM", REGION_HYPER_RAM_BASE_ADDRESS,
-                        REGION_RAM_ATTR(REGION_HYPER_RAM_SIZE)),
+                        REGION_FLASH_ATTR(REGION_HYPER_RAM_SIZE)),
#endif
```

<a id="memory-usage"></a>

### 内存使用（Memory Usage）


- 从RAM执行：将CM7代码从闪存复制到ITCM或HyperRAM。
- 从闪存执行：CM7直接从闪存执行，可容纳比ITCM更大的代码。

<a id="performance-considerations"></a>

### 性能考量（Performance Considerations）


- 从ITCM执行：利用低延迟的内部ITCM获得更快执行速度。
- 从外部存储器执行：外部闪存或HyperRAM的访问耗时可能更长，导致执行较慢。

  不过，外部存储器可以容纳更大的代码。

<a id="dual-core-samples-debugging"></a>

### 双核示例调试（Dual Core Samples Debugging）

调试双核示例时，确保SW5处于0100模式。CM33负责复制及启动CM7。调试CM7时，可在复位向量或main函数中加入无限while循环，再将调试器附加到CM7。

CM7只能在复位后再次启动，因此烧录后务必复位开发板。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`mimxrt1180_evk`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

默认运行工具（Runner）为LinkServer，烧录及调试都使用调试探针。此板默认使用MCU-Link CMSIS-DAP板载探针。原文说明pyOCD尚不支持对此板外部闪存编程，请使用以下其他受支持探针之一。（[板载MCU-Link CMSIS-DAP调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#mcu-link-cmsis-onboard-debug-probe)；[pyOCD调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#pyocd-debug-host-tools)）

<a id="using-j-link"></a>

<a id="using-j-link-rt1180"></a>

#### 使用J-Link

使用接在J37上的外部J-Link Plus时，确保J-Link版本高于V7.94g，并安装JP5。

调试CM33时，SW5须设为0100；调试CM7时须设为0001。原文说明，板上默认启动核为CM33，此处CM7镜像仅支持在调试时运行。

安装J-Link调试主机工具（Debug Host Tools），并确保工具位于搜索路径中。（[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)）

可将板载调试电路更新为Segger J-Link固件，也可将外部J-Link探针连接EVK。（[J-Link外部调试探针（External Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#jlink-external-debug-probe)）

<a id="using-linkserver"></a>

#### 使用LinkServer

确保LinkServer版本高于V1.5.30，并移除JP5，原文称这是默认设置。

调试CM33时，SW5须设为0100；调试CM7时须设为0001。原文说明，板上默认启动核为CM33，此处CM7镜像仅支持在调试时运行。

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

无论选用何种探针，控制台均使用MCU-Link作为USB转串口适配器。原文此处要求JP5和JP3均短接，并称其出厂默认短接，以连接UART信号；这与上文LinkServer步骤的JP5状态不一致，分别保留。

用USB线缆将PC连接J53。

在串口终端中使用以下设置，例如minicom或PuTTY：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

### 烧录（Flashing）

下面以CM33核上的[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

上电前确认SW5设为0100b。

```text
# From the root of the zephyr repository
west build -b mimxrt1180_evk/mimxrt1189/cm33 samples/hello_world
west flash
```

给开发板断电再上电，打开串口终端并按SW3复位，终端应显示以下消息：

```text
***** Booting Zephyr OS v3.7.0-xxx-xxxxxxxxxxxxx *****
Hello World! mimxrt1180_evk/mimxrt1189/cm33
```

<a id="debugging"></a>

### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b mimxrt1180_evk/mimxrt1189/cm33 samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
***** Booting Zephyr OS v3.7.0-xxx-xxxxxxxxxxxxx *****
Hello World! mimxrt1180_evk/mimxrt1189/cm33
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

CM33默认启动CM7；CM7从闪存执行需TRDC权限，HyperRAM执行需避免与CM33数据重叠并修改MPU属性。双核调试与单独CM7调试的SW5模式不同。LinkServer要求JP5移除，而串口段又称JP5默认短接，两处原文分别保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [MIMXRT1180-EVK](https://www.nxp.com/design/design-center/development-boards-and-designs/MIMXRT1180-EVK)：HTTP Error 404: Not Found。
- [IMXRT1180EC.pdf](https://www.nxp.com/docs/en/data-sheet/IMXRT1180EC.pdf)：HTTP Error 404: Not Found。
- [IMXRT1180RM.pdf](https://www.nxp.com/docs/en/reference-manual/IMXRT1180RM.pdf)：HTTP Error 404: Not Found。
- [i.MX-RT1180](https://www.nxp.com/products/i.MX-RT1180)：HTTP Error 404: Not Found。
- [Download?colCode=UM12021&isHTMLorPDF=HTML](https://www.nxp.com/webapp/Download?colCode=UM12021&isHTMLorPDF=HTML)：HTTP Error 404: Not Found。

---

[上一章](P002_MIMXRT1170-EVK.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_MIMXRT2660-EVK.md)
