---
id: learning.zephyr-docs.boards-nxp-frdm-mcx-rw.page-13
title: FRDM-MCXN236
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxn236/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="frdm_mcxn236"></a>

# 第13章\_FRDM-MCXN236

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxn236/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/frdm_mcxn236.webp](images/frdm_mcxn236.webp)](images/frdm_mcxn236.webp)

FRDM-MCXN236

名称（Name）：

`frdm_mcxn236`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mcxn236](https://docs.zephyrproject.org/latest/boards/index.html#soc=mcxn236)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_mcxn236/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

FRDM-MCXN236是紧凑、可扩展的开发板，用于MCX N23X微控制器的快速原型开发。工业标准排针便于访问MCU I/O，板上集成开放标准串行接口、外部闪存及MCU-Link调试器。MCX N系列是高性能、低功耗微控制器，利用智能外设及加速器提供多任务处理能力和高效性能。

<a id="hardware"></a>

## 硬件（Hardware）


- MCX-N236 Arm Cortex-M33微控制器，运行频率150 MHz
- 1 MB双存储体片内闪存
- 352 KB RAM
- 带片上高速物理层（HS PHY）的USB高速主机／设备接口，使用高速USB Type-C连接器
- 8路低功耗Flexcomm，每路支持SPI、I2C及UART
- 2路支持FD的FlexCAN、2路I3C及2路SAI
- 支持CMSIS-DAP的板载MCU-Link调试器
- Arduino排针、FlexIO／LCD排针、SmartDMA／摄像头排针及mikroBUS

MCX-N236 SoC及FRDM-MCXN236开发板的更多信息见以下资料：


- [MCX-N236 SoC网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-n-series-microcontrollers/mcx-n23x-highly-integrated-mcus-with-on-chip-accelerators-intelligent-peripherals-and-advanced-security:MCX-N23X)
- [MCX-N236 数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/MCXN23x.pdf)
- [MCX-N236 参考手册（Reference Manual）](https://www.nxp.com/docs/en/reference-manual/MCXN23xRM.pdf)
- [FRDM-MCXN236 网站](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-n23x-mcus:FRDM-MCXN236)
- [FRDM-MCXN236 用户指南（User Guide）](https://www.nxp.com/document/guide/getting-started-with-frdm-mcxn236:GS-FRDM-MCXN236)
- [FRDM-MCXN236 开发板用户手册（Board User Manual）](https://www.nxp.com/docs/en/user-manual/UM12041.pdf)
- [FRDM-MCXN236 原理图（Schematics）](https://www.nxp.com/webapp/Download?colCode=SPF-90828)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`frdm_mcxn236`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="frdm_mcxn236-hw-features"></a>

<a id="frdm_mcxn236-frdm_mcxn236/mcxn236-hw-features-section"></a>

#### `frdm_mcxn236/mcxn236`目标（Target）

<a id="frdm_mcxn236-frdm_mcxn236/mcxn236-hw-features-panel"></a>

<a id="frdm_mcxn236-frdm_mcxn236/mcxn236-hw-features-memory"></a>

该开发板目标的片上存储容量：192 KiB RAM、1 MiB Flash。

<a id="frdm_mcxn236-frdm_mcxn236/mcxn236-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L990">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1020">已禁用：1</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="2">音频（Audio）</td>
<td>板载（On-Board）</td>
<td>Dialog DA7212音频编解码器（Audio Codec）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L214">已启用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P008_dlg_da7212.md#std-dtcompatible-dlg-da7212"><code>dlg,da7212</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP脉冲密度调制麦克风接口（PDM / MICFIL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1245">已启用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P014_nxp_micfil.md#std-dtcompatible-nxp-micfil"><code>nxp,micfil</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1076">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1066">已禁用：1</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L157">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟监测（Clock Monitor）</td>
<td>片上（On-Chip）</td>
<td>NXP频率测量（FREQME）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L176">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P004_nxp_freqme.md#std-dtcompatible-nxp-freqme"><code>nxp,freqme</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗比较器（LPCMP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1052">已禁用：2</a>）</td>
<td><a href="../hardware/P747_NXP低功耗比较器绑定.md#dtbinding-nxp-lpcmp"><code>nxp,lpcmp</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L914">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L926">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗定时器（LPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1125">已启用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr"><code>nxp,lptmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器（Multirate Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1147">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P015_nxp_mrt.md#std-dtcompatible-nxp-mrt"><code>nxp,mrt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1158">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1164">已禁用：3</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P014_nxp_mrt-channel.md#std-dtcompatible-nxp-mrt-channel"><code>nxp,mrt-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1313">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P006_nxp_crc.md#std-dtcompatible-nxp-crc"><code>nxp,crc</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>NXP EdgeLock安全子系统（Secure Subsystem）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1320">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P003_nxp_els.md#std-dtcompatible-nxp-els"><code>nxp,els</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L733">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L749">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SmartDMA控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1194">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P007_nxp_smartdma.md#std-dtcompatible-nxp-smartdma"><code>nxp,smartdma</code></a></td>
</tr>
<tr>
<td rowspan="2">错误检测与纠正（EDAC）</td>
<td>片上（On-Chip）</td>
<td>NXP错误注入模块（Error Injection Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L351">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P002_nxp_eim.md#std-dtcompatible-nxp-eim"><code>nxp,eim</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP错误报告模块（Error Reporting Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L403">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P003_nxp_erm.md#std-dtcompatible-nxp-erm"><code>nxp,erm</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP MSF1闪存模块（FMU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L763">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P018_nxp_msf1.md#std-dtcompatible-nxp-msf1"><code>nxp,msf1</code></a></td>
</tr>
<tr>
<td rowspan="4">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Kinetis通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L291">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L341">已禁用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P002_nxp_kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio"><code>nxp,kinetis-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L69">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP LCD 8080接口上引出的GPIO引脚，例如LCD-PAR-035面板使用的引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L101">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P003_nxp_lcd-8080.md#std-dtcompatible-nxp-lcd-8080"><code>nxp,lcd-8080</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ArduCam 20引脚排针式摄像头连接器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L111">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P021_arducam_dvp-20pin-connector.md#std-dtcompatible-arducam-dvp-20pin-connector"><code>arducam,dvp-20pin-connector</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC 128位唯一标识符（Unique Identifier）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L783">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P009_nxp_lpc-uid.md#std-dtcompatible-nxp-lpc-uid"><code>nxp,lpc-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L527">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L439">已禁用：6</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1211">已启用：2</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1112">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1099">已禁用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L51">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>低功耗Flexcomm（Low Power Flexcomm）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L493">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L411">已禁用：4</a>）</td>
<td><a href="../hardware/P702_NXP低功耗灵活通信接口绑定.md#dtbinding-nxp-lp-flexcomm"><code>nxp,lp-flexcomm</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示总线接口（MIPI-DBI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO LCD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1093">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P005_nxp_mipi-dbi-flexio-lcdif.md#std-dtcompatible-nxp-mipi-dbi-flexio-lcdif"><code>nxp,mipi-dbi-flexio-lcdif</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1086">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L772">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">多路复用器（MUX）</td>
<td>片上（On-Chip）</td>
<td>NXP输入复用器（INPUTMUX）外设绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L168">已启用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux"><code>nxp,inputmux</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>NXP OTPC电子熔丝（eFuse）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L797">已启用：1</a>）</td>
<td><a href="../otp_binding_reference/P005_nxp_otpc.md#std-dtcompatible-nxp-otpc"><code>nxp,otpc</code></a></td>
</tr>
<tr>
<td rowspan="1">性能状态（Performance State）</td>
<td>片上（On-Chip）</td>
<td>NXP MCXN系列性能状态（pstate）自定义属性实现（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L41">已启用：3</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P002_nxp_mcxn-pstate.md#std-dtcompatible-nxp-mcxn-pstate"><code>nxp,mcxn-pstate</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L249">已启用：6</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P017_nxp_port-pinmux.md#std-dtcompatible-nxp-port-pinmux"><code>nxp,port-pinmux</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L123">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P016_nxp_port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl"><code>nxp,port-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="3">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>NXP系统电源控制器（SPC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1287">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P001_nxp_spc.md#std-dtcompatible-nxp-spc"><code>nxp,spc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP内核模式控制器（CMC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1301">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P014_nxp_cmc.md#std-dtcompatible-nxp-cmc"><code>nxp,cmc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP智能电源开关（VBAT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1307">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P002_nxp_vbat.md#std-dtcompatible-nxp-vbat"><code>nxp,vbat</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>此电源域在进入及退出指定电源状态（Power State）时开启或关闭设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L117">已启用：1</a>）</td>
<td><a href="../power_domain_binding_reference/P007_power-domain-soc-state-change.md#std-dtcompatible-power-domain-soc-state-change"><code>power-domain-soc-state-change</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>包含mcux-pwm子模块的NXP eFLEX PWM模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L812">已启用：2</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P003_nxp_flexpwm.md#std-dtcompatible-nxp-flexpwm"><code>nxp,flexpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L869">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L818">已禁用：7</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P005_nxp_imx-pwm.md#std-dtcompatible-nxp-imx-pwm"><code>nxp,imx-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>NXP VREF SoC外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L974">已启用：1</a>）</td>
<td><a href="../hardware/P652_NXP参考电压绑定.md#dtbinding-nxp-vref"><code>nxp,vref</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L162">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P009_nxp_lpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset"><code>nxp,lpc-syscon-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>NXP EdgeLock安全子系统的真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1325">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P017_nxp_els-trng.md#std-dtcompatible-nxp-els-trng"><code>nxp,els-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>独立实时时钟（IRTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1183">已启用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P012_nxp_irtc.md#std-dtcompatible-nxp-irtc"><code>nxp,irtc</code></a></td>
</tr>
<tr>
<td rowspan="3">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>FXLS8974三轴加速度传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L206">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P051_nxp_fxls8974.md#std-dtcompatible-nxp-fxls8974"><code>nxp,fxls8974</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP LPADC_TEMP40温度传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1015">已禁用：1</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P005_nxp_lpadc-temp40.md#std-dtcompatible-nxp-lpadc-temp40"><code>nxp,lpadc-temp40</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX正交解码器（QDC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1331">已禁用：2</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P007_nxp_mcux-qdc.md#std-dtcompatible-nxp-mcux-qdc"><code>nxp,mcux-qdc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L503">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L421">已禁用：6</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L554">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L428">已禁用：7</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L147">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX RT5xx／6xx上的NXP操作系统定时器（OS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L789">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P008_nxp_os-timer.md#std-dtcompatible-nxp-os-timer"><code>nxp,os-timer</code></a></td>
</tr>
<tr>
<td rowspan="2">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1037">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1046">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td rowspan="1">视频（Video）</td>
<td>板载（On-Board）</td>
<td>NXP SmartDMA视频驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L403">已禁用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P012_nxp_video-smartdma.md#std-dtcompatible-nxp-video-smartdma"><code>nxp,video-smartdma</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>LPC窗口看门狗定时器（Windowed Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L803">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P011_nxp_lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt"><code>nxp,lpc-wwdt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP外部看门狗监测器（External Watchdog Monitor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1203">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P007_nxp_ewm.md#std-dtcompatible-nxp-ewm"><code>nxp,ewm</code></a></td>
</tr>
<tr>
<td rowspan="1">唤醒控制器（Wakeup Controller）</td>
<td>片上（On-Chip）</td>
<td>作为唤醒控制器（WUC）的NXP唤醒单元（WUU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1294">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P008_nxp_wuc-wuu.md#std-dtcompatible-nxp-wuc-wuu"><code>nxp,wuc-wuu</code></a></td>
</tr>
</table>

<a id="frdm_mcxn236-frdm_mcxn236/mcxn236/ns-hw-features-section"></a>

#### `frdm_mcxn236/mcxn236/ns`目标（Target）

<a id="frdm_mcxn236-frdm_mcxn236/mcxn236/ns-hw-features-panel"></a>

<a id="frdm_mcxn236-frdm_mcxn236/mcxn236/ns-hw-features-memory"></a>

该开发板目标的片上存储容量：160 KiB RAM、1 MiB Flash。

<a id="frdm_mcxn236-frdm_mcxn236/mcxn236/ns-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L990">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1020">已禁用：1</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="2">音频（Audio）</td>
<td>板载（On-Board）</td>
<td>Dialog DA7212音频编解码器（Audio Codec）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L214">已启用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P008_dlg_da7212.md#std-dtcompatible-dlg-da7212"><code>dlg,da7212</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP脉冲密度调制麦克风接口（PDM / MICFIL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1245">已启用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P014_nxp_micfil.md#std-dtcompatible-nxp-micfil"><code>nxp,micfil</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1076">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1066">已禁用：1</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L157">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟监测（Clock Monitor）</td>
<td>片上（On-Chip）</td>
<td>NXP频率测量（FREQME）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L176">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P004_nxp_freqme.md#std-dtcompatible-nxp-freqme"><code>nxp,freqme</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗比较器（LPCMP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1052">已禁用：2</a>）</td>
<td><a href="../hardware/P747_NXP低功耗比较器绑定.md#dtbinding-nxp-lpcmp"><code>nxp,lpcmp</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L914">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L926">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗定时器（LPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1125">已启用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr"><code>nxp,lptmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器（Multirate Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1147">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P015_nxp_mrt.md#std-dtcompatible-nxp-mrt"><code>nxp,mrt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1158">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1164">已禁用：3</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P014_nxp_mrt-channel.md#std-dtcompatible-nxp-mrt-channel"><code>nxp,mrt-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1313">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P006_nxp_crc.md#std-dtcompatible-nxp-crc"><code>nxp,crc</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>NXP EdgeLock安全子系统（Secure Subsystem）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1320">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P003_nxp_els.md#std-dtcompatible-nxp-els"><code>nxp,els</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L733">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L749">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SmartDMA控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1194">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P007_nxp_smartdma.md#std-dtcompatible-nxp-smartdma"><code>nxp,smartdma</code></a></td>
</tr>
<tr>
<td rowspan="2">错误检测与纠正（EDAC）</td>
<td>片上（On-Chip）</td>
<td>NXP错误注入模块（Error Injection Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L351">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P002_nxp_eim.md#std-dtcompatible-nxp-eim"><code>nxp,eim</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP错误报告模块（Error Reporting Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L403">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P003_nxp_erm.md#std-dtcompatible-nxp-erm"><code>nxp,erm</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP MSF1闪存模块（FMU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L763">已禁用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P018_nxp_msf1.md#std-dtcompatible-nxp-msf1"><code>nxp,msf1</code></a></td>
</tr>
<tr>
<td rowspan="4">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Kinetis通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L291">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L341">已禁用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P002_nxp_kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio"><code>nxp,kinetis-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L69">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP LCD 8080接口上引出的GPIO引脚，例如LCD-PAR-035面板使用的引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L101">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P003_nxp_lcd-8080.md#std-dtcompatible-nxp-lcd-8080"><code>nxp,lcd-8080</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ArduCam 20引脚排针式摄像头连接器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L111">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P021_arducam_dvp-20pin-connector.md#std-dtcompatible-arducam-dvp-20pin-connector"><code>arducam,dvp-20pin-connector</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC 128位唯一标识符（Unique Identifier）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L783">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P009_nxp_lpc-uid.md#std-dtcompatible-nxp-lpc-uid"><code>nxp,lpc-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L527">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L439">已禁用：6</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1211">已启用：2</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1112">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1099">已禁用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L51">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>低功耗Flexcomm（Low Power Flexcomm）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L493">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L411">已禁用：4</a>）</td>
<td><a href="../hardware/P702_NXP低功耗灵活通信接口绑定.md#dtbinding-nxp-lp-flexcomm"><code>nxp,lp-flexcomm</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示总线接口（MIPI-DBI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO LCD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1093">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P005_nxp_mipi-dbi-flexio-lcdif.md#std-dtcompatible-nxp-mipi-dbi-flexio-lcdif"><code>nxp,mipi-dbi-flexio-lcdif</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1086">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L772">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">多路复用器（MUX）</td>
<td>片上（On-Chip）</td>
<td>NXP输入复用器（INPUTMUX）外设绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L168">已启用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux"><code>nxp,inputmux</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>NXP OTPC电子熔丝（eFuse）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L797">已启用：1</a>）</td>
<td><a href="../otp_binding_reference/P005_nxp_otpc.md#std-dtcompatible-nxp-otpc"><code>nxp,otpc</code></a></td>
</tr>
<tr>
<td rowspan="1">性能状态（Performance State）</td>
<td>片上（On-Chip）</td>
<td>NXP MCXN系列性能状态（pstate）自定义属性实现（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L41">已启用：3</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P002_nxp_mcxn-pstate.md#std-dtcompatible-nxp-mcxn-pstate"><code>nxp,mcxn-pstate</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L249">已启用：6</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P017_nxp_port-pinmux.md#std-dtcompatible-nxp-port-pinmux"><code>nxp,port-pinmux</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L123">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P016_nxp_port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl"><code>nxp,port-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="3">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>NXP系统电源控制器（SPC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1287">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P001_nxp_spc.md#std-dtcompatible-nxp-spc"><code>nxp,spc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP内核模式控制器（CMC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1301">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P014_nxp_cmc.md#std-dtcompatible-nxp-cmc"><code>nxp,cmc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP智能电源开关（VBAT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1307">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P002_nxp_vbat.md#std-dtcompatible-nxp-vbat"><code>nxp,vbat</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>此电源域在进入及退出指定电源状态（Power State）时开启或关闭设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L117">已启用：1</a>）</td>
<td><a href="../power_domain_binding_reference/P007_power-domain-soc-state-change.md#std-dtcompatible-power-domain-soc-state-change"><code>power-domain-soc-state-change</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>包含mcux-pwm子模块的NXP eFLEX PWM模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L812">已启用：2</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P003_nxp_flexpwm.md#std-dtcompatible-nxp-flexpwm"><code>nxp,flexpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L869">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L818">已禁用：7</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P005_nxp_imx-pwm.md#std-dtcompatible-nxp-imx-pwm"><code>nxp,imx-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>NXP VREF SoC外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L974">已启用：1</a>）</td>
<td><a href="../hardware/P652_NXP参考电压绑定.md#dtbinding-nxp-vref"><code>nxp,vref</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L162">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P009_nxp_lpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset"><code>nxp,lpc-syscon-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>NXP EdgeLock安全子系统的真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1325">已禁用：1</a>）</td>
<td><a href="../rng_binding_reference/P017_nxp_els-trng.md#std-dtcompatible-nxp-els-trng"><code>nxp,els-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>独立实时时钟（IRTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1183">已启用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P012_nxp_irtc.md#std-dtcompatible-nxp-irtc"><code>nxp,irtc</code></a></td>
</tr>
<tr>
<td rowspan="3">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>FXLS8974三轴加速度传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L206">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P051_nxp_fxls8974.md#std-dtcompatible-nxp-fxls8974"><code>nxp,fxls8974</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP LPADC_TEMP40温度传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1015">已禁用：1</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P005_nxp_lpadc-temp40.md#std-dtcompatible-nxp-lpadc-temp40"><code>nxp,lpadc-temp40</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX正交解码器（QDC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1331">已禁用：2</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P007_nxp_mcux-qdc.md#std-dtcompatible-nxp-mcux-qdc"><code>nxp,mcux-qdc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L503">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L421">已禁用：6</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L554">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L428">已禁用：7</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L147">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>i.MX RT5xx／6xx上的NXP操作系统定时器（OS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L789">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P008_nxp_os-timer.md#std-dtcompatible-nxp-os-timer"><code>nxp,os-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td rowspan="2">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1037">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1046">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td rowspan="1">视频（Video）</td>
<td>板载（On-Board）</td>
<td>NXP SmartDMA视频驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L403">已禁用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P012_nxp_video-smartdma.md#std-dtcompatible-nxp-video-smartdma"><code>nxp,video-smartdma</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>LPC窗口看门狗定时器（Windowed Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L803">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P011_nxp_lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt"><code>nxp,lpc-wwdt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP外部看门狗监测器（External Watchdog Monitor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1203">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P007_nxp_ewm.md#std-dtcompatible-nxp-ewm"><code>nxp,ewm</code></a></td>
</tr>
<tr>
<td rowspan="1">唤醒控制器（Wakeup Controller）</td>
<td>片上（On-Chip）</td>
<td>作为唤醒控制器（WUC）的NXP唤醒单元（WUU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn23x_common.dtsi?plain=1#L1294">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P008_nxp_wuc-wuu.md#std-dtcompatible-nxp-wuc-wuu"><code>nxp,wuc-wuu</code></a></td>
</tr>
</table>

<a id="shields-for-supported-features"></a>

### 支持相应功能的扩展板（Shields）

上表部分功能使用Zephyr扩展板测试，以下扩展板已在此板上测试：


- [NXP LCD_PAR_S035 TFT LCD模块](https://docs.zephyrproject.org/latest/boards/shields/lcd_par_s035/doc/index.html#lcd-par-s035)：支持显示接口（Display）；此板通过片上FlexIO外设连接扩展板的MIPI_DBI接口。
- [DVP 20引脚OV7670摄像头模块](https://docs.zephyrproject.org/latest/boards/shields/dvp_20pin_ov7670/doc/index.html#dvp-20pin-ov7670)：支持SmartDMA视频接口。

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

MCX-N236 SoC有6个GPIO控制器，可通过引脚复用（Pinmux）寄存器配置引脚功能。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>P0_PIO1_8</td>
<td>通用异步收发器（UART）</td>
<td>UART接收（RX）</td>
</tr>
<tr>
<td>P1_PIO1_9</td>
<td>通用异步收发器（UART）</td>
<td>UART发送（TX）</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

MCX-N236 SoC配置为使用150 MHz PLL0作为系统时钟源。

<a id="serial-port"></a>

### 串口（Serial Port）

FRDM-MCXN236 SoC有8路FLEXCOMM串行通信接口，Flexcomm 4配置为控制台UART。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`frdm_mcxn236`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

烧录和调试均使用调试探针，默认配置为MCU-Link CMSIS-DAP板载调试探针。

<a id="using-linkserver"></a>

#### 使用LinkServer

默认运行工具为LinkServer，支持出厂MCU-Link固件。只有板载调试电路固件被更换时，才需按MCU-Link CMSIS-DAP板载调试探针说明重新写入默认固件；写入前短接JP5，进入设备固件升级（DFU）模式。（[板载MCU-Link CMSIS-DAP调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#mcu-link-cmsis-onboard-debug-probe)）

<a id="using-j-link"></a>

#### 使用J-Link

有两种方案。第一种按MCU-Link J-Link板载调试探针说明，将板载调试电路更新为Segger J-Link固件；写入前短接JP5，进入DFU模式。第二种将外部J-Link调试探针连接到10引脚SWD连接器J12，并短接JP7。两种方案都需给west传入-r jlink，选择J-Link运行工具。（[MCU-Link J-Link板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#mcu-link-jlink-onboard-debug-probe)；[J-Link外部调试探针（External Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#jlink-external-debug-probe)）

```text
west flash -r jlink
```

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

用USB线缆将PC连接到J10，在所选串口终端（如minicom、PuTTY）中使用以下设置：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

### 烧录（Flashing）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b frdm_mcxn236 samples/hello_world
west flash
```

打开串口终端，复位开发板（按下RESET按键），应能在终端中看到以下消息：

```text
*** Booting Zephyr OS build v3.6.0-4478-ge6c3a42f5f52 ***
Hello World! frdm_mcxn236/mcxn236
```

<a id="debugging"></a>

### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b frdm_mcxn236/mcxn236 samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
*** Booting Zephyr OS build v3.6.0-4478-ge6c3a42f5f52 ***
Hello World! frdm_mcxn236/mcxn236
```

<a id="troubleshooting"></a>

### 故障排查（Troubleshooting）

<a id="using-segger-systemview-and-rtt"></a>

#### 使用Segger SystemView及RTT

此SoC使用SEGGER SystemView或实时传输（RTT）时，必须在SystemView或RTT Viewer中手动设置RTT控制块地址。该地址为_SEGGER_RTT符号的位置，可通过调试器或链接器输出的zephyr.map文件查找。

必须手动指定控制块地址，是因为此SoC支持带纠错码（ECC）的RAM。当ECC已启用、待搜索RAM区域尚未初始化为已知值时，SEGGER工具若在ECC RAM中搜索控制块，将引发故障（Fault）。

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)
- [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)
- [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- NXP Zephyr主页，包含培训资源（[NXP的Zephyr专题页面](https://nxp.com/zephyr)）
- [NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [frdm-development-board-for-mcx-n23x-mcus:FRDM-MCXN236](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-n23x-mcus:FRDM-MCXN236)：HTTP Error 404: Not Found。
- [MCXN23x.pdf](https://www.nxp.com/docs/en/data-sheet/MCXN23x.pdf)：HTTP Error 404: Not Found。
- [MCXN23xRM.pdf](https://www.nxp.com/docs/en/reference-manual/MCXN23xRM.pdf)：HTTP Error 404: Not Found。
- [UM12041.pdf](https://www.nxp.com/docs/en/user-manual/UM12041.pdf)：HTTP Error 404: Not Found。
- [getting-started-with-frdm-mcxn236:GS-FRDM-MCXN236](https://www.nxp.com/document/guide/getting-started-with-frdm-mcxn236:GS-FRDM-MCXN236)：HTTP Error 404: Not Found。
- [mcx-n23x-highly-integrated-mcus-with-on-chip-accelerators-intelligent-peripherals-and-advanced-security:MCX-N23X](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-n-series-microcontrollers/mcx-n23x-highly-integrated-mcus-with-on-chip-accelerators-intelligent-peripherals-and-advanced-security:MCX-N23X)：HTTP Error 404: Not Found。
- [Download?colCode=SPF-90828](https://www.nxp.com/webapp/Download?colCode=SPF-90828)：HTTP Error 404: Not Found。

---

[上一章](P012_FRDM-MCXL255.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_FRDM-MCXN947.md)
