---
id: learning.zephyr-docs.boards-nxp-frdm-imx-kinetis.page-4
title: FRDM-iMXRT1186
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/frdm_imxrt1186/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="frdm_imxrt1186"></a>

# 第4章\_FRDM-iMXRT1186

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/frdm_imxrt1186/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id2"></a>

[![官方原图：../../../../_images/frdm_imxrt1186.webp](images/frdm_imxrt1186.webp)](images/frdm_imxrt1186.webp)

FRDM-iMXRT1186

名称（Name）：

`frdm_imxrt1186`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mimxrt1186](https://docs.zephyrproject.org/latest/boards/index.html#soc=mimxrt1186)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_imxrt1186/doc/index.rst/../..)<a id="frdm-imxrt1186"></a>

<a id="id1"></a>

## FRDM-iMXRT1186

<a id="overview"></a>

### 概述（Overview）

NXP FRDM-IMXRT1186是基于i.MX RT1186跨界MCU的经济型开发板，兼顾高性能及实时能力。易于访问的I/O支持扩展板，可快速原型开发及评估可编程逻辑控制器（PLC）、远程I/O、电机控制及其他工业自动化应用。

<a id="hardware"></a>

### 硬件（Hardware）


- i.MX RT1186跨界处理器（Crossover Processor）：


  - 800 MHz Arm Cortex-M7核
  - 300 MHz Arm Cortex-M33核
  - 原文称，这是首款集成Gbps时间敏感网络（TSN）交换机的实时MCU，支持多种协议，用于连接既有系统与工业4.0通信
  - 原文称，这是首款集成EdgeLock®安全隔离区（Secure Enclave）的跨界MCU
  - 最高1.5 MB支持纠错码（ECC）保护的SRAM，包含供Cortex-M7使用的512 KB紧耦合存储器（TCM）及供Cortex-M33使用的256 KB TCM
- 板载存储器（Board Memory）


  - 256 Mbit HyperRAM存储器
  - 512 Mbit HyperFlash闪存
  - 128 Mbit QSPI闪存
- 连接能力（Connectivity）


  - 两个用于TSN交换机的10/100/1000M以太网连接器
  - 两个用于EtherCAT或TSN交换机的10/100M以太网连接器
  - 一个Type-C USB OTG连接器
  - 一个CAN收发器
- 调试能力（Debug Capabilities）


  - JTAG连接器
  - 板载MCU-Link调试器
- 扩展连接器（Expansion Connectors）


  - ARDUINO® UNO R3排针
  - FRDM排针
  - FlexSPI从端（Follower）排针
  - SRAMC排针
  - 电机排针（Motor Header）

i.MX RT1186 SoC及FRDM-iMXRT1186更多信息：


- [i.MX RT1180网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1180-crossover-mcu-dual-core-arm-cortex-m7-and-cortex-m33-with-tsn-switch:i.MX-RT1180)
- [i.MX RT1180数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/IMXRT1180CEC.pdf)
- [i.MX RT1180参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=IMXRT1180RM)
- [FRDM-iMXRT1186网站](https://www.nxp.com/design/design-center/development-boards-and-designs/FRDM-IMXRT1186#on-board-devices)
- [FRDM-iMXRT1186用户指南（User Guide）](https://www.nxp.com/webapp/Download?colCode=UM12450)
- [FRDM-iMXRT1186原理图（Schematics）](https://www.nxp.com/webapp/Download?colCode=FRDM-IMXRT1186-DESIGN-FILES)

<a id="board-variants"></a>

#### 开发板变体（Board Variants）

此板提供3种变体：


- frdm_imxrt1186/mimxrt1186/cm33：运行于Cortex-M33，使用内部SRAM和闪存；这是默认可启动内核。存储器称呼按原文保留。
- frdm_imxrt1186/mimxrt1186/cm7：运行于Cortex-M7，使用内部SRAM和闪存，必须由CM33启动。
- frdm_imxrt1186/mimxrt1186/cm7/extmem：运行于Cortex-M7，将外部HyperRAM用作zephyr,sram、外部HyperFlash用作zephyr,flash，供需要超出内部可用RAM或闪存容量的应用使用。ITCM及DTCM仍可放置时间要求严格的代码和数据。

注意（Note）

使用extmem变体时，通过J-Link调试脚本初始化外部存储器，确保使用前配置正确。

<a id="supported-features"></a>

#### 支持的功能（Supported Features）

FRDM-iMXRT1186是经济型开发平台。NXP将MIMXRT1180-EVK视为i.MX RT118x系列功能更完整的开发板（Superset Board），并以其作为Zephyr完整平台支持（Full Platform Support）的重点，优先为它启用新功能，以支持整个RT118x系列。相比MIMXRT1180-EVK，FRDM-iMXRT1186的部分功能可能受限或不可用。

`frdm_imxrt1186`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="frdm_imxrt1186-hw-features"></a>

<a id="frdm_imxrt1186-frdm_imxrt1186/mimxrt1186/cm33-hw-features-section"></a>

##### `frdm_imxrt1186/mimxrt1186/cm33`目标（Target）

<a id="frdm_imxrt1186-frdm_imxrt1186/mimxrt1186/cm33-hw-features-panel"></a>

<a id="frdm_imxrt1186-frdm_imxrt1186/mimxrt1186/cm33-hw-features-memory"></a>

该开发板目标的片上存储容量：8 MiB RAM、16 MiB Flash。

<a id="frdm_imxrt1186-frdm_imxrt1186/mimxrt1186/cm33-hw-features-table"></a>

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
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L837">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L861">已禁用：1</a>）</td>
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
<td>NXP Kinetis模拟比较器（ACMP / Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L428">已禁用：1</a>）</td>
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
<td>NXP系统计数器（SYS_CTR / System Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L873">已启用：1</a>）</td>
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
<td>NXP低功耗定时器（LPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L992">已禁用：3</a>）</td>
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
<td>NXP存储器ECC控制器（MECC）的错误检测与纠正（EDAC）绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L368">已禁用：2</a>）</td>
<td><a href="../edac_syscon_binding_reference/P004_nxp_mecc.md#std-dtcompatible-nxp-mecc"><code>nxp,mecc</code></a></td>
</tr>
<tr>
<td rowspan="5">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L742">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P008_nxp_imx-netc.md#std-dtcompatible-nxp-imx-netc"><code>nxp,imx-netc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC物理站点接口（PSI / Physical Station Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L759">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L748">已禁用：1</a>）</td>
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
<td>Motorcomm YT8531以太网PHY（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L263">已启用：2</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P008_motorcomm_yt8531.md#std-dtcompatible-motorcomm-yt8531"><code>motorcomm,yt8531</code></a></td>
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
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L324">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L302">已禁用：3</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1580">已禁用：3</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1305">已禁用：2</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="2">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>NXP KPP控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1421">已禁用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P010_nxp_mcux-kpp.md#std-dtcompatible-nxp-mcux-kpp"><code>nxp,mcux-kpp</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L46">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L57">已启用：1</a>）</td>
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
<td rowspan="3">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>兼容Atmel AT24系列的I2C电可擦除可编程只读存储器（EEPROM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L101">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P004_atmel_at24.md#std-dtcompatible-atmel-at24"><code>atmel,at24</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP FlexSPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L194">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P023_nxp_imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor"><code>nxp,imx-flexspi-nor</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L206">已启用：1</a>）</td>
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
<td>NXP MCUX脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1182">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1060">已禁用：15</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P005_nxp_imx-pwm.md#std-dtcompatible-nxp-imx-pwm"><code>nxp,imx-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1245">已禁用：4</a>）</td>
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
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1343">已禁用：1</a>）</td>
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
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L134">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L144">已禁用：7</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1431">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1409">已禁用：5</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x_cm33.dtsi?plain=1#L52">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x_cm33.dtsi?plain=1#L47">已禁用：1</a>）</td>
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
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1541">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1561">已禁用：1</a>）</td>
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

<a id="frdm_imxrt1186-frdm_imxrt1186/mimxrt1186/cm7-hw-features-section"></a>

##### `frdm_imxrt1186/mimxrt1186/cm7`目标（Target）

<a id="frdm_imxrt1186-frdm_imxrt1186/mimxrt1186/cm7-hw-features-panel"></a>

<a id="frdm_imxrt1186-frdm_imxrt1186/mimxrt1186/cm7-hw-features-memory"></a>

该开发板目标的片上存储容量：256 KiB RAM、256 KiB Flash。

<a id="frdm_imxrt1186-frdm_imxrt1186/mimxrt1186/cm7-hw-features-table"></a>

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
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L837">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L861">已禁用：1</a>）</td>
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
<td>NXP Kinetis模拟比较器（ACMP / Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L428">已禁用：1</a>）</td>
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
<td>NXP系统计数器（SYS_CTR / System Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L873">已启用：1</a>）</td>
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
<td>NXP低功耗定时器（LPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L992">已禁用：3</a>）</td>
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
<td>NXP存储器ECC控制器（MECC）的错误检测与纠正（EDAC）绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L368">已禁用：2</a>）</td>
<td><a href="../edac_syscon_binding_reference/P004_nxp_mecc.md#std-dtcompatible-nxp-mecc"><code>nxp,mecc</code></a></td>
</tr>
<tr>
<td rowspan="5">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L742">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P008_nxp_imx-netc.md#std-dtcompatible-nxp-imx-netc"><code>nxp,imx-netc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC物理站点接口（PSI / Physical Station Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L759">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L748">已禁用：1</a>）</td>
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
<td>Motorcomm YT8531以太网PHY（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L263">已启用：2</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P008_motorcomm_yt8531.md#std-dtcompatible-motorcomm-yt8531"><code>motorcomm,yt8531</code></a></td>
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
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L324">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L302">已禁用：3</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1580">已禁用：3</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1305">已禁用：2</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="2">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>NXP KPP控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1421">已禁用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P010_nxp_mcux-kpp.md#std-dtcompatible-nxp-mcux-kpp"><code>nxp,mcux-kpp</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L46">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L57">已启用：1</a>）</td>
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
<td rowspan="3">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>兼容Atmel AT24系列的I2C电可擦除可编程只读存储器（EEPROM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L101">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P004_atmel_at24.md#std-dtcompatible-atmel-at24"><code>atmel,at24</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP FlexSPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L194">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P023_nxp_imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor"><code>nxp,imx-flexspi-nor</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L206">已启用：1</a>）</td>
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
<td>NXP MCUX脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1182">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1060">已禁用：15</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P005_nxp_imx-pwm.md#std-dtcompatible-nxp-imx-pwm"><code>nxp,imx-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1245">已禁用：4</a>）</td>
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
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1343">已禁用：1</a>）</td>
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
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L154">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L134">已禁用：7</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1431">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1409">已禁用：5</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x_cm7.dtsi?plain=1#L39">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x_cm7.dtsi?plain=1#L34">已禁用：1</a>）</td>
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
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1541">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1561">已禁用：1</a>）</td>
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

<a id="frdm_imxrt1186-frdm_imxrt1186/mimxrt1186/cm7/extmem-hw-features-section"></a>

##### `frdm_imxrt1186/mimxrt1186/cm7/extmem`目标（Target）

<a id="frdm_imxrt1186-frdm_imxrt1186/mimxrt1186/cm7/extmem-hw-features-panel"></a>

<a id="frdm_imxrt1186-frdm_imxrt1186/mimxrt1186/cm7/extmem-hw-features-memory"></a>

该开发板目标的片上存储容量：8 MiB RAM、16 MiB Flash。

<a id="frdm_imxrt1186-frdm_imxrt1186/mimxrt1186/cm7/extmem-hw-features-table"></a>

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
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L442">已禁用：2</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX交叉开关（XBAR / Crossbar Switch）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1704">已禁用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P016_nxp_mcux-xbar.md#std-dtcompatible-nxp-mcux-xbar"><code>nxp,mcux-xbar</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L837">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L861">已禁用：1</a>）</td>
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
<td>NXP Kinetis模拟比较器（ACMP / Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L428">已禁用：1</a>）</td>
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
<td>NXP系统计数器（SYS_CTR / System Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L873">已启用：1</a>）</td>
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
<td>NXP低功耗定时器（LPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L992">已禁用：3</a>）</td>
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
<td>NXP存储器ECC控制器（MECC）的错误检测与纠正（EDAC）绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L368">已禁用：2</a>）</td>
<td><a href="../edac_syscon_binding_reference/P004_nxp_mecc.md#std-dtcompatible-nxp-mecc"><code>nxp,mecc</code></a></td>
</tr>
<tr>
<td rowspan="5">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L742">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P008_nxp_imx-netc.md#std-dtcompatible-nxp-imx-netc"><code>nxp,imx-netc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX NETC物理站点接口（PSI / Physical Station Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L759">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L748">已禁用：1</a>）</td>
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
<td>Motorcomm YT8531以太网PHY（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L263">已启用：2</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P008_motorcomm_yt8531.md#std-dtcompatible-motorcomm-yt8531"><code>motorcomm,yt8531</code></a></td>
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
<td>NXP SEMA42硬件信号量（Hardware Semaphore）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1688">已禁用：2</a>）</td>
<td><a href="../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42"><code>nxp,sema42</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L324">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L302">已禁用：3</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1580">已禁用：3</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1305">已禁用：2</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="2">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>NXP KPP控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1421">已禁用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P010_nxp_mcux-kpp.md#std-dtcompatible-nxp-mcux-kpp"><code>nxp,mcux-kpp</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L46">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L57">已启用：1</a>）</td>
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
<td rowspan="3">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>兼容Atmel AT24系列的I2C电可擦除可编程只读存储器（EEPROM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L101">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P004_atmel_at24.md#std-dtcompatible-atmel-at24"><code>atmel,at24</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP FlexSPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L194">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P023_nxp_imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor"><code>nxp,imx-flexspi-nor</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt1186/frdm_imxrt1186.dtsi?plain=1#L206">已启用：1</a>）</td>
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
<td>NXP MCUX脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1182">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1060">已禁用：15</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P005_nxp_imx-pwm.md#std-dtcompatible-nxp-imx-pwm"><code>nxp,imx-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1245">已禁用：4</a>）</td>
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
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1343">已禁用：1</a>）</td>
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
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L154">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L134">已禁用：7</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1431">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1409">已禁用：5</a>）</td>
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
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1541">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt118x/nxp_rt118x.dtsi?plain=1#L1561">已禁用：1</a>）</td>
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

#### 连接与I/O（Connections and I/Os）

i.MX RT1186 SoC有多个GPIO控制器，开发板默认配置使用以下引脚：

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>GPIO_AON_08</td>
<td>LPUART1_TX</td>
<td>CM33 UART控制台发送（TX）</td>
</tr>
<tr>
<td>GPIO_AON_09</td>
<td>LPUART1_RX</td>
<td>CM33 UART控制台接收（RX）</td>
</tr>
<tr>
<td>GPIO_AD_13</td>
<td>LPUART3_TX</td>
<td>CM7 UART控制台发送（TX）</td>
</tr>
<tr>
<td>GPIO_AD_14</td>
<td>LPUART3_RX</td>
<td>CM7 UART控制台接收（RX）</td>
</tr>
<tr>
<td>GPIO2_IO09</td>
<td>通用输入输出（GPIO）</td>
<td>红色LED（Red LED）</td>
</tr>
<tr>
<td>GPIO2_IO11</td>
<td>通用输入输出（GPIO）</td>
<td>绿色LED（Green LED）</td>
</tr>
<tr>
<td>GPIO3_IO07</td>
<td>通用输入输出（GPIO）</td>
<td>蓝色LED（Blue LED）</td>
</tr>
<tr>
<td>GPIO4_IO12</td>
<td>通用输入输出（GPIO）</td>
<td>用户按键SW4</td>
</tr>
<tr>
<td>GPIO_AD_15</td>
<td>模数转换器（ADC）</td>
<td>ADC1通道1</td>
</tr>
<tr>
<td>GPIO_AD_16</td>
<td>模数转换器（ADC）</td>
<td>ADC1通道0</td>
</tr>
<tr>
<td>GPIO_AD_17</td>
<td>I3C2_PUR</td>
<td>I3C2上拉（Pull-up），Arduino接口</td>
</tr>
<tr>
<td>GPIO_AD_18</td>
<td>I3C2_SCL</td>
<td>I3C2 SCL，Arduino D15</td>
</tr>
<tr>
<td>GPIO_AD_19</td>
<td>I3C2_SDA</td>
<td>I3C2 SDA，Arduino D14</td>
</tr>
</table>

注意（Note）

使用Arduino排针上的I3C2需要改装硬件：焊接R30／R31，将Arduino D14／D15连接到GPIO_AD_18／19；将R297／R299移到1—3位置，断开GPIO_EMC_B2_19／20与Arduino排针的连接。详情见FRDM-iMXRT1186原理图。I3C2与连接板载EEPROM的LPI2C3共用GPIO_AD_18／19，因此启用I3C2的覆盖文件必须禁用LPI2C3及EEPROM。

<a id="system-clock"></a>

#### 系统时钟（System Clock）

i.MX RT1186 SoC配置为以SysTick作为系统时钟源。Cortex-M33最高运行频率300 MHz，Cortex-M7最高800 MHz。

<a id="ele-active-timer-requirement"></a>

#### ELE活动定时器要求（Active Timer Requirement）

RT1180平台要求定期与EdgeLock安全隔离区（ELE）通信，否则会触发系统复位。根据RT1180系统参考手册（SRM）第3.11节“ELE active timer”，至少每24小时向ELE发送一次ping。

Zephyr通过软件定时器每23小时自动向ELE发送一次ping，为可能的时钟误差留出余量。此机制对应用透明，无需用户干预。

详情见RT1180 SRM第3.11节。

<a id="itcm-and-dtcm"></a>

#### 指令及数据紧耦合存储器（ITCM / DTCM）

若将zephyr,flash放入ITCM，或将zephyr,sram放入DTCM，应从对应存储器设备节点删除zephyr,memory-region属性。例如，以下覆盖文件将CM33的zephyr,sram移到DTCM：

```text
boards/nxp/frdm_imxrt1186/cm33_sram_dtcm.overlay
```

<a id="ethernet"></a>

#### 以太网（Ethernet）

NETC以太网驱动支持管理物理站点接口（PSI），NETC DSA驱动支持管理交换机端口。当前DSA仅支持交换功能，尚不能通过DSA主端口管理；主端口支持仍待实现。

FRDM-iMXRT1186提供以下网络接口：


- swp0及swp1：可供使用的用户端口（User Ports）。
- swp2：DSA CPU端口，不属于用户端口。
- eth0：DSA连接端口（Conduit Port），不属于用户端口。

FRDM-iMXRT1186的两个以太网连接器由NETC的ETH0／ETH2与EtherCAT的ECAT0／ECAT1共享。使用网络接口前，按下述方式设置跳线，使连接器连接NETC：


- 选择ETH0而非ECAT0：J12短接1—2脚，J13短接2—3脚。
- 选择ETH2而非ECAT1：J18短接1—2脚，J17短接2—3脚。

注意（Note）

预期DHCP可在swp0和swp1上工作。

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

<a id="serial-port"></a>

#### 串口（Serial Port）

i.MX RT1186 SoC有8个LPUART外设，LPUART1／3配置为控制台，可通过Debug USB连接器访问。

<a id="programming-and-debugging"></a>

### 烧录与调试（Programming and Debugging）

`frdm_imxrt1186`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

#### 配置调试探针（Configuring a Debug Probe）

烧录和调试均使用调试探针，默认配置为MCU-Link CMSIS-DAP板载调试探针。（[板载MCU-Link CMSIS-DAP调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#mcu-link-cmsis-onboard-debug-probe)）

调试CM33时，确保J60设置为1:OFF、2:OFF、3:ON。

调试CM7时，确保J60设置为1:ON、2:OFF、3:OFF。

<a id="using-linkserver"></a>

##### 使用LinkServer

LinkServer是此板默认调试主机工具，无需额外配置。

<a id="using-j-link"></a>

##### 使用J-Link

安装J-Link调试主机工具（Debug Host Tools），并确保工具位于搜索路径中。（[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)）

有两种选择：


1. 短接J40，将板载MCU-Link调试电路更新为SEGGER J-Link固件。
2. 短接J58，使用连接J54的外部J-Link调试探针；注意J54默认未安装。（[J-Link外部调试探针（External Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#jlink-external-debug-probe)）

<a id="configuring-a-console"></a>

#### 配置控制台（Configuring a Console）

用USB Type-C线缆将PC连接J23，再用minicom、PuTTY等串口终端，设置如下：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

#### 烧录（Flashing）

以下以CM33核的[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b frdm_imxrt1186/mimxrt1186/cm33 samples/hello_world
west flash
```

打开串口终端，按复位键SW2复位开发板，应显示以下消息。注意：使用LPUART3作为串口时，必须移除J34跳线。

```text
*** Booting Zephyr OS build v4.x.x ***
Hello World! frdm_imxrt1186/mimxrt1186/cm33
```

注意：默认可启动内核为CM33，CM7不能独立启动。

CM7必须由CM33启动。

<a id="debugging"></a>

#### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b frdm_imxrt1186/mimxrt1186/cm33 samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
*** Booting Zephyr OS build v4.x.x ***
Hello World! frdm_imxrt1186/mimxrt1186/cm33
```

<a id="support-resources-for-zephyr"></a>

#### Zephyr支持资源（Support Resources）


- [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)
- [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)
- [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- NXP Zephyr主页，包含培训资源（[NXP的Zephyr专题页面](https://nxp.com/zephyr)）
- [NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## 译注

CM7必须由CM33启动；extmem目标通过J-Link脚本初始化外部存储器。ELE看门狗要求至少每24小时发送ping，软件定时器按23小时预留误差。I3C2与EEPROM所在LPI2C3共用引脚，硬件返工后还须停用冲突节点。保留ITCM／DTCM属性删除要求、DSA交换机限制、以太网跳线、CM33／CM7启动拨码以及两种J-Link连接位置。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [FRDM-IMXRT1186](https://www.nxp.com/design/design-center/development-boards-and-designs/FRDM-IMXRT1186#on-board-devices)：HTTP Error 404: Not Found。
- [IMXRT1180CEC.pdf](https://www.nxp.com/docs/en/data-sheet/IMXRT1180CEC.pdf)：HTTP Error 404: Not Found。
- [i-mx-rt1180-crossover-mcu-dual-core-arm-cortex-m7-and-cortex-m33-with-tsn-switch:i.MX-RT1180](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1180-crossover-mcu-dual-core-arm-cortex-m7-and-cortex-m33-with-tsn-switch:i.MX-RT1180)：HTTP Error 404: Not Found。
- [Download?colCode=FRDM-IMXRT1186-DESIGN-FILES](https://www.nxp.com/webapp/Download?colCode=FRDM-IMXRT1186-DESIGN-FILES)：HTTP Error 404: Not Found。
- [Download?colCode=IMXRT1180RM](https://www.nxp.com/webapp/Download?colCode=IMXRT1180RM)：HTTP Error 404: Not Found。
- [Download?colCode=UM12450](https://www.nxp.com/webapp/Download?colCode=UM12450)：HTTP Error 404: Not Found。

---

[上一章](P003_FRDM-IMXRT1152.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_FRDM-IMXRT700.md)
