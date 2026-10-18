---
id: learning.zephyr-docs.boards-nxp-remaining.page-2
title: MCX-N5XX-EVK
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/mcx_nx4x_evk/doc/mcx_n5xx_evk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mcx_n5xx_evk"></a>

# 第2章\_MCX-N5XX-EVK

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/mcx_nx4x_evk/doc/mcx_n5xx_evk.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mcx_n9xx_evk.webp](images/mcx_n9xx_evk.webp)](images/mcx_n9xx_evk.webp)

MCX-N5XX-EVK

名称（Name）：

`mcx_n5xx_evk`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mcxn547](https://docs.zephyrproject.org/latest/boards/index.html#soc=mcxn547)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mcx_nx4x_evk/doc/mcx_n5xx_evk.rst/../..)<a id="overview"></a>

## 概述（Overview）

MCX-N5XX-EVK与[MCX-N9XX-EVK](P003_MCX-N9XX-EVK.md)非常相似，使用说明参见后者页面。主要区别是此板使用MCXN547，而非MCXN947。

MCX-N547 SoC及MCX-N5XX-EVK开发板的更多信息见：


- [MCX-N547 SoC网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-n-series-microcontrollers/mcx-n94x-54x-highly-integrated-multicore-mcus-with-on-chip-accelerators-intelligent-peripherals-and-advanced-security:MCX-N94X-N54X)
- [MCX-N5XX-EVK网站](https://www.nxp.com/design/design-center/development-boards-and-designs/MCX-N5XX-EVK)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`mcx_n5xx_evk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mcx_n5xx_evk-hw-features"></a>

<a id="mcx_n5xx_evk-mcx_n5xx_evk/mcxn547/cpu0-hw-features-section"></a>

#### `mcx_n5xx_evk/mcxn547/cpu0`目标（Target）

<a id="mcx_n5xx_evk-mcx_n5xx_evk/mcxn547/cpu0-hw-features-panel"></a>

<a id="mcx_n5xx_evk-mcx_n5xx_evk/mcxn547/cpu0-hw-features-memory"></a>

该开发板目标的片上存储容量：320 KiB RAM、2 MiB Flash。

<a id="mcx_n5xx_evk-mcx_n5xx_evk/mcxn547/cpu0-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1195">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1218">已禁用：1</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="2">音频（Audio）</td>
<td>板载（On-Board）</td>
<td>Dialog DA7212音频编解码器（Audio Codec）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk_cpu0.dtsi?plain=1#L112">已启用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P008_dlg_da7212.md#std-dtcompatible-dlg-da7212"><code>dlg,da7212</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP脉冲密度调制麦克风接口（PDM / MICFIL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L911">已启用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P014_nxp_micfil.md#std-dtcompatible-nxp-micfil"><code>nxp,micfil</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1272">已启用：1</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L145">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟监测（Clock Monitor）</td>
<td>片上（On-Chip）</td>
<td>NXP频率测量（FREQME）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L164">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P004_nxp_freqme.md#std-dtcompatible-nxp-freqme"><code>nxp,freqme</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗比较器（LPCMP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1258">已禁用：2</a>）</td>
<td><a href="../hardware/P747_NXP低功耗比较器绑定.md#dtbinding-nxp-lpcmp"><code>nxp,lpcmp</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1090">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1102">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗定时器（LPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1282">已启用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr"><code>nxp,lptmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器（Multirate Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1343">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P015_nxp_mrt.md#std-dtcompatible-nxp-mrt"><code>nxp,mrt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1354">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1360">已禁用：3</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P014_nxp_mrt-channel.md#std-dtcompatible-nxp-mrt-channel"><code>nxp,mrt-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1459">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P006_nxp_crc.md#std-dtcompatible-nxp-crc"><code>nxp,crc</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>NXP EdgeLock安全子系统（Secure Subsystem）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1481">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P003_nxp_els.md#std-dtcompatible-nxp-els"><code>nxp,els</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX低功耗数模转换器（LPDAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L896">已启用：1</a>）</td>
<td><a href="../hardware/P770_NXP低功耗数模转换器绑定.md#dtbinding-nxp-lpdac"><code>nxp,lpdac</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L825">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L841">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SmartDMA控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1160">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P007_nxp_smartdma.md#std-dtcompatible-nxp-smartdma"><code>nxp,smartdma</code></a></td>
</tr>
<tr>
<td rowspan="1">数字信号处理（DSP）</td>
<td>片上（On-Chip）</td>
<td>NXP PowerQuad数字信号处理（DSP）协处理器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1466">已启用：1</a>）</td>
<td><a href="../sound_haptic_binding_reference/P004_nxp_powerquad.md#std-dtcompatible-nxp-powerquad"><code>nxp,powerquad</code></a></td>
</tr>
<tr>
<td rowspan="2">错误检测与纠正（EDAC）</td>
<td>片上（On-Chip）</td>
<td>NXP错误注入模块（Error Injection Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L339">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P002_nxp_eim.md#std-dtcompatible-nxp-eim"><code>nxp,eim</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP错误报告模块（Error Reporting Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L409">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P003_nxp_erm.md#std-dtcompatible-nxp-erm"><code>nxp,erm</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP ENET QOS以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L984">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P003_nxp_enet-qos.md#std-dtcompatible-nxp-enet-qos"><code>nxp,enet-qos</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 精确时间协议时钟（Precision Time Protocol，PTP Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L995">已禁用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P006_snps_dwmac-ptp-clock.md#std-dtcompatible-snps-dwmac-ptp-clock"><code>snps,dwmac-ptp-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 的管理数据输入输出控制器（MDIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1000">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P010_snps_dwmac-mdio.md#std-dtcompatible-snps-dwmac-mdio"><code>snps,dwmac-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L243">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP MSF1闪存模块（FMU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L857">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P018_nxp_msf1.md#std-dtcompatible-nxp-msf1"><code>nxp,msf1</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Kinetis通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L279">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L329">已禁用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P002_nxp_kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio"><code>nxp,kinetis-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP LCD 8080接口上引出的GPIO引脚，例如LCD-PAR-035面板使用的引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L86">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P003_nxp_lcd-8080.md#std-dtcompatible-nxp-lcd-8080"><code>nxp,lcd-8080</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC 128位唯一标识符（Unique Identifier）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L876">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P009_nxp_lpc-uid.md#std-dtcompatible-nxp-lpc-uid"><code>nxp,lpc-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件自旋锁（Hardware Spinlock）</td>
<td>片上（On-Chip）</td>
<td>NXP SEMA42硬件信号量（Hardware Semaphore）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1450">已启用：1</a>）</td>
<td><a href="../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42"><code>nxp,sema42</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L534">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L446">已禁用：8</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1407">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1390">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1317">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1304">已禁用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="2">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>NXP TSI V6触摸感应输入设备（Touch Sensing Input Device）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1473">已启用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P011_nxp_tsi-input.md#std-dtcompatible-nxp-tsi-input"><code>nxp,tsi-input</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L63">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L24">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L46">已禁用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>作为Zephyr邮箱（MBOX）的NXP邮箱单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L816">已启用：1</a>）</td>
<td><a href="../intercore_reference/P048_NXPMAILBOX邮箱绑定.md#dtbinding-nxp-mbox-mailbox"><code>nxp,mbox-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>低功耗Flexcomm（Low Power Flexcomm）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L456">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L417">已禁用：6</a>）</td>
<td><a href="../hardware/P702_NXP低功耗灵活通信接口绑定.md#dtbinding-nxp-lp-flexcomm"><code>nxp,lp-flexcomm</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示总线接口（MIPI-DBI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO LCD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1337">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P005_nxp_mipi-dbi-flexio-lcdif.md#std-dtcompatible-nxp-mipi-dbi-flexio-lcdif"><code>nxp,mipi-dbi-flexio-lcdif</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1330">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L866">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP FlexSPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L194">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P023_nxp_imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor"><code>nxp,imx-flexspi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">多路复用器（MUX）</td>
<td>片上（On-Chip）</td>
<td>NXP输入复用器（INPUTMUX）外设绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L156">已启用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux"><code>nxp,inputmux</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>NXP OTPC电子熔丝（eFuse）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L890">已启用：1</a>）</td>
<td><a href="../otp_binding_reference/P005_nxp_otpc.md#std-dtcompatible-nxp-otpc"><code>nxp,otpc</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L237">已启用：6</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P017_nxp_port-pinmux.md#std-dtcompatible-nxp-port-pinmux"><code>nxp,port-pinmux</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L110">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P016_nxp_port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl"><code>nxp,port-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="3">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>NXP系统电源控制器（SPC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1424">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P001_nxp_spc.md#std-dtcompatible-nxp-spc"><code>nxp,spc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP内核模式控制器（CMC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1438">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P014_nxp_cmc.md#std-dtcompatible-nxp-cmc"><code>nxp,cmc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP智能电源开关（VBAT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1444">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P002_nxp_vbat.md#std-dtcompatible-nxp-vbat"><code>nxp,vbat</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>此电源域在进入及退出指定电源状态（Power State）时开启或关闭设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L103">已启用：1</a>）</td>
<td><a href="../power_domain_binding_reference/P007_power-domain-soc-state-change.md#std-dtcompatible-power-domain-soc-state-change"><code>power-domain-soc-state-change</code></a></td>
</tr>
<tr>
<td rowspan="3">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>包含mcux-pwm子模块的NXP eFLEX PWM模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1025">已启用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P003_nxp_flexpwm.md#std-dtcompatible-nxp-flexpwm"><code>nxp,flexpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1031">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1064">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P005_nxp_imx-pwm.md#std-dtcompatible-nxp-imx-pwm"><code>nxp,imx-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP状态可配置定时器（SCTimer）脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1150">已启用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P012_nxp_sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm"><code>nxp,sctimer-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>NXP VREF SoC外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1179">已启用：1</a>）</td>
<td><a href="../hardware/P652_NXP参考电压绑定.md#dtbinding-nxp-vref"><code>nxp,vref</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L150">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P009_nxp_lpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset"><code>nxp,lpc-syscon-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>NXP EdgeLock安全子系统的真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1486">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P017_nxp_els-trng.md#std-dtcompatible-nxp-els-trng"><code>nxp,els-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>独立实时时钟（IRTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1379">已启用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P012_nxp_irtc.md#std-dtcompatible-nxp-irtc"><code>nxp,irtc</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1169">已启用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P014_nxp_imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc"><code>nxp,imx-usdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX正交解码器（QDC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1076">已禁用：2</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P007_nxp_mcux-qdc.md#std-dtcompatible-nxp-mcux-qdc"><code>nxp,mcux-qdc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L510">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L428">已禁用：8</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L476">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L435">已禁用：9</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn54x.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L135">已启用：3</a>）</td>
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
<td>i.MX RT5xx／6xx上的NXP操作系统定时器（OS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L882">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P008_nxp_os-timer.md#std-dtcompatible-nxp-os-timer"><code>nxp,os-timer</code></a></td>
</tr>
<tr>
<td rowspan="3">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>设备模式下的NPX Kinetis USBFSOTG控制器，厂商缩写NPX按原文保留（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1233">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P007_nxp_kinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd"><code>nxp,kinetis-usbd</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1243">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1252">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>LPC窗口看门狗定时器（Windowed Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1008">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P011_nxp_lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt"><code>nxp,lpc-wwdt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP外部看门狗监测器（External Watchdog Monitor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1017">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P007_nxp_ewm.md#std-dtcompatible-nxp-ewm"><code>nxp,ewm</code></a></td>
</tr>
<tr>
<td rowspan="1">唤醒控制器（Wakeup Controller）</td>
<td>片上（On-Chip）</td>
<td>作为唤醒控制器（WUC）的NXP唤醒单元（WUU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1431">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P008_nxp_wuc-wuu.md#std-dtcompatible-nxp-wuc-wuu"><code>nxp,wuc-wuu</code></a></td>
</tr>
</table>

<a id="mcx_n5xx_evk-mcx_n5xx_evk/mcxn547/cpu0/ns-hw-features-section"></a>

#### `mcx_n5xx_evk/mcxn547/cpu0/ns`目标（Target）

<a id="mcx_n5xx_evk-mcx_n5xx_evk/mcxn547/cpu0/ns-hw-features-panel"></a>

<a id="mcx_n5xx_evk-mcx_n5xx_evk/mcxn547/cpu0/ns-hw-features-memory"></a>

该开发板目标的片上存储容量：128 KiB RAM、2 MiB Flash。

<a id="mcx_n5xx_evk-mcx_n5xx_evk/mcxn547/cpu0/ns-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1195">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1218">已禁用：1</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="2">音频（Audio）</td>
<td>板载（On-Board）</td>
<td>Dialog DA7212音频编解码器（Audio Codec）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk_cpu0.dtsi?plain=1#L112">已启用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P008_dlg_da7212.md#std-dtcompatible-dlg-da7212"><code>dlg,da7212</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP脉冲密度调制麦克风接口（PDM / MICFIL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L911">已启用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P014_nxp_micfil.md#std-dtcompatible-nxp-micfil"><code>nxp,micfil</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1272">已启用：1</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L145">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟监测（Clock Monitor）</td>
<td>片上（On-Chip）</td>
<td>NXP频率测量（FREQME）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L164">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P004_nxp_freqme.md#std-dtcompatible-nxp-freqme"><code>nxp,freqme</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗比较器（LPCMP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1258">已禁用：2</a>）</td>
<td><a href="../hardware/P747_NXP低功耗比较器绑定.md#dtbinding-nxp-lpcmp"><code>nxp,lpcmp</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1090">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1102">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗定时器（LPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1282">已启用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr"><code>nxp,lptmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器（Multirate Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1343">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P015_nxp_mrt.md#std-dtcompatible-nxp-mrt"><code>nxp,mrt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1354">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1360">已禁用：3</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P014_nxp_mrt-channel.md#std-dtcompatible-nxp-mrt-channel"><code>nxp,mrt-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1459">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P006_nxp_crc.md#std-dtcompatible-nxp-crc"><code>nxp,crc</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>NXP EdgeLock安全子系统（Secure Subsystem）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1481">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P003_nxp_els.md#std-dtcompatible-nxp-els"><code>nxp,els</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX低功耗数模转换器（LPDAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L896">已启用：1</a>）</td>
<td><a href="../hardware/P770_NXP低功耗数模转换器绑定.md#dtbinding-nxp-lpdac"><code>nxp,lpdac</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L825">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L841">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SmartDMA控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1160">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P007_nxp_smartdma.md#std-dtcompatible-nxp-smartdma"><code>nxp,smartdma</code></a></td>
</tr>
<tr>
<td rowspan="1">数字信号处理（DSP）</td>
<td>片上（On-Chip）</td>
<td>NXP PowerQuad数字信号处理（DSP）协处理器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1466">已启用：1</a>）</td>
<td><a href="../sound_haptic_binding_reference/P004_nxp_powerquad.md#std-dtcompatible-nxp-powerquad"><code>nxp,powerquad</code></a></td>
</tr>
<tr>
<td rowspan="2">错误检测与纠正（EDAC）</td>
<td>片上（On-Chip）</td>
<td>NXP错误注入模块（Error Injection Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L339">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P002_nxp_eim.md#std-dtcompatible-nxp-eim"><code>nxp,eim</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP错误报告模块（Error Reporting Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L409">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P003_nxp_erm.md#std-dtcompatible-nxp-erm"><code>nxp,erm</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP ENET QOS以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L984">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P003_nxp_enet-qos.md#std-dtcompatible-nxp-enet-qos"><code>nxp,enet-qos</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 精确时间协议时钟（Precision Time Protocol，PTP Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L995">已禁用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P006_snps_dwmac-ptp-clock.md#std-dtcompatible-snps-dwmac-ptp-clock"><code>snps,dwmac-ptp-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 的管理数据输入输出控制器（MDIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1000">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P010_snps_dwmac-mdio.md#std-dtcompatible-snps-dwmac-mdio"><code>snps,dwmac-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L243">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP MSF1闪存模块（FMU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L857">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P018_nxp_msf1.md#std-dtcompatible-nxp-msf1"><code>nxp,msf1</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Kinetis通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L279">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L329">已禁用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P002_nxp_kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio"><code>nxp,kinetis-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP LCD 8080接口上引出的GPIO引脚，例如LCD-PAR-035面板使用的引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L86">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P003_nxp_lcd-8080.md#std-dtcompatible-nxp-lcd-8080"><code>nxp,lcd-8080</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC 128位唯一标识符（Unique Identifier）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L876">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P009_nxp_lpc-uid.md#std-dtcompatible-nxp-lpc-uid"><code>nxp,lpc-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件自旋锁（Hardware Spinlock）</td>
<td>片上（On-Chip）</td>
<td>NXP SEMA42硬件信号量（Hardware Semaphore）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1450">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42"><code>nxp,sema42</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L534">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L446">已禁用：8</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1407">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1390">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1317">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1304">已禁用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="2">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>NXP TSI V6触摸感应输入设备（Touch Sensing Input Device）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1473">已启用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P011_nxp_tsi-input.md#std-dtcompatible-nxp-tsi-input"><code>nxp,tsi-input</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L63">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L24">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L46">已禁用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>作为Zephyr邮箱（MBOX）的NXP邮箱单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L816">已启用：1</a>）</td>
<td><a href="../intercore_reference/P048_NXPMAILBOX邮箱绑定.md#dtbinding-nxp-mbox-mailbox"><code>nxp,mbox-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>低功耗Flexcomm（Low Power Flexcomm）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L456">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L417">已禁用：6</a>）</td>
<td><a href="../hardware/P702_NXP低功耗灵活通信接口绑定.md#dtbinding-nxp-lp-flexcomm"><code>nxp,lp-flexcomm</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示总线接口（MIPI-DBI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO LCD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1337">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P005_nxp_mipi-dbi-flexio-lcdif.md#std-dtcompatible-nxp-mipi-dbi-flexio-lcdif"><code>nxp,mipi-dbi-flexio-lcdif</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1330">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L866">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP FlexSPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L194">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P023_nxp_imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor"><code>nxp,imx-flexspi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">多路复用器（MUX）</td>
<td>片上（On-Chip）</td>
<td>NXP输入复用器（INPUTMUX）外设绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L156">已启用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux"><code>nxp,inputmux</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>NXP OTPC电子熔丝（eFuse）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L890">已启用：1</a>）</td>
<td><a href="../otp_binding_reference/P005_nxp_otpc.md#std-dtcompatible-nxp-otpc"><code>nxp,otpc</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L237">已启用：6</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P017_nxp_port-pinmux.md#std-dtcompatible-nxp-port-pinmux"><code>nxp,port-pinmux</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L110">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P016_nxp_port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl"><code>nxp,port-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="3">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>NXP系统电源控制器（SPC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1424">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P001_nxp_spc.md#std-dtcompatible-nxp-spc"><code>nxp,spc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP内核模式控制器（CMC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1438">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P014_nxp_cmc.md#std-dtcompatible-nxp-cmc"><code>nxp,cmc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP智能电源开关（VBAT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1444">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P002_nxp_vbat.md#std-dtcompatible-nxp-vbat"><code>nxp,vbat</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>此电源域在进入及退出指定电源状态（Power State）时开启或关闭设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L103">已启用：1</a>）</td>
<td><a href="../power_domain_binding_reference/P007_power-domain-soc-state-change.md#std-dtcompatible-power-domain-soc-state-change"><code>power-domain-soc-state-change</code></a></td>
</tr>
<tr>
<td rowspan="3">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>包含mcux-pwm子模块的NXP eFLEX PWM模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1025">已启用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P003_nxp_flexpwm.md#std-dtcompatible-nxp-flexpwm"><code>nxp,flexpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1031">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1064">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P005_nxp_imx-pwm.md#std-dtcompatible-nxp-imx-pwm"><code>nxp,imx-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP状态可配置定时器（SCTimer）脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1150">已启用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P012_nxp_sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm"><code>nxp,sctimer-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>NXP VREF SoC外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1179">已启用：1</a>）</td>
<td><a href="../hardware/P652_NXP参考电压绑定.md#dtbinding-nxp-vref"><code>nxp,vref</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L150">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P009_nxp_lpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset"><code>nxp,lpc-syscon-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>NXP EdgeLock安全子系统的真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1486">已禁用：1</a>）</td>
<td><a href="../rng_binding_reference/P017_nxp_els-trng.md#std-dtcompatible-nxp-els-trng"><code>nxp,els-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>独立实时时钟（IRTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1379">已启用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P012_nxp_irtc.md#std-dtcompatible-nxp-irtc"><code>nxp,irtc</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1169">已启用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P014_nxp_imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc"><code>nxp,imx-usdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX正交解码器（QDC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1076">已禁用：2</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P007_nxp_mcux-qdc.md#std-dtcompatible-nxp-mcux-qdc"><code>nxp,mcux-qdc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L510">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L428">已禁用：8</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L476">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L435">已禁用：9</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn54x_ns.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L135">已启用：3</a>）</td>
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
<td>i.MX RT5xx／6xx上的NXP操作系统定时器（OS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L882">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P008_nxp_os-timer.md#std-dtcompatible-nxp-os-timer"><code>nxp,os-timer</code></a></td>
</tr>
<tr>
<td rowspan="3">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>设备模式下的NPX Kinetis USBFSOTG控制器，厂商缩写NPX按原文保留（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1233">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P007_nxp_kinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd"><code>nxp,kinetis-usbd</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1243">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1252">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>LPC窗口看门狗定时器（Windowed Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1008">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P011_nxp_lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt"><code>nxp,lpc-wwdt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP外部看门狗监测器（External Watchdog Monitor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1017">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P007_nxp_ewm.md#std-dtcompatible-nxp-ewm"><code>nxp,ewm</code></a></td>
</tr>
<tr>
<td rowspan="1">唤醒控制器（Wakeup Controller）</td>
<td>片上（On-Chip）</td>
<td>作为唤醒控制器（WUC）的NXP唤醒单元（WUU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1431">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P008_nxp_wuc-wuu.md#std-dtcompatible-nxp-wuc-wuu"><code>nxp,wuc-wuu</code></a></td>
</tr>
</table>

<a id="mcx_n5xx_evk-mcx_n5xx_evk/mcxn547/cpu1-hw-features-section"></a>

#### `mcx_n5xx_evk/mcxn547/cpu1`目标（Target）

<a id="mcx_n5xx_evk-mcx_n5xx_evk/mcxn547/cpu1-hw-features-panel"></a>

<a id="mcx_n5xx_evk-mcx_n5xx_evk/mcxn547/cpu1-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、2 MiB Flash。

<a id="mcx_n5xx_evk-mcx_n5xx_evk/mcxn547/cpu1-hw-features-table"></a>

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
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1195">已禁用：2</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>片上（On-Chip）</td>
<td>NXP脉冲密度调制麦克风接口（PDM / MICFIL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L911">已启用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P014_nxp_micfil.md#std-dtcompatible-nxp-micfil"><code>nxp,micfil</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1272">已禁用：1</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L145">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟监测（Clock Monitor）</td>
<td>片上（On-Chip）</td>
<td>NXP频率测量（FREQME）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L164">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P004_nxp_freqme.md#std-dtcompatible-nxp-freqme"><code>nxp,freqme</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗比较器（LPCMP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1258">已禁用：2</a>）</td>
<td><a href="../hardware/P747_NXP低功耗比较器绑定.md#dtbinding-nxp-lpcmp"><code>nxp,lpcmp</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1090">已禁用：5</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗定时器（LPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1282">已启用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr"><code>nxp,lptmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器（Multirate Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1343">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P015_nxp_mrt.md#std-dtcompatible-nxp-mrt"><code>nxp,mrt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1354">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P014_nxp_mrt-channel.md#std-dtcompatible-nxp-mrt-channel"><code>nxp,mrt-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1459">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P006_nxp_crc.md#std-dtcompatible-nxp-crc"><code>nxp,crc</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>NXP EdgeLock安全子系统（Secure Subsystem）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1481">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P003_nxp_els.md#std-dtcompatible-nxp-els"><code>nxp,els</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX低功耗数模转换器（LPDAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L896">已禁用：1</a>）</td>
<td><a href="../hardware/P770_NXP低功耗数模转换器绑定.md#dtbinding-nxp-lpdac"><code>nxp,lpdac</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L825">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L841">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SmartDMA控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1160">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P007_nxp_smartdma.md#std-dtcompatible-nxp-smartdma"><code>nxp,smartdma</code></a></td>
</tr>
<tr>
<td rowspan="1">数字信号处理（DSP）</td>
<td>片上（On-Chip）</td>
<td>NXP PowerQuad数字信号处理（DSP）协处理器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1466">已启用：1</a>）</td>
<td><a href="../sound_haptic_binding_reference/P004_nxp_powerquad.md#std-dtcompatible-nxp-powerquad"><code>nxp,powerquad</code></a></td>
</tr>
<tr>
<td rowspan="2">错误检测与纠正（EDAC）</td>
<td>片上（On-Chip）</td>
<td>NXP错误注入模块（Error Injection Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L339">已禁用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P002_nxp_eim.md#std-dtcompatible-nxp-eim"><code>nxp,eim</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP错误报告模块（Error Reporting Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L409">已禁用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P003_nxp_erm.md#std-dtcompatible-nxp-erm"><code>nxp,erm</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>NXP ENET QOS以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L984">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P003_nxp_enet-qos.md#std-dtcompatible-nxp-enet-qos"><code>nxp,enet-qos</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 精确时间协议时钟（Precision Time Protocol，PTP Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L995">已禁用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P006_snps_dwmac-ptp-clock.md#std-dtcompatible-snps-dwmac-ptp-clock"><code>snps,dwmac-ptp-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 的管理数据输入输出控制器（MDIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1000">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P010_snps_dwmac-mdio.md#std-dtcompatible-snps-dwmac-mdio"><code>snps,dwmac-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L243">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP MSF1闪存模块（FMU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L857">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P018_nxp_msf1.md#std-dtcompatible-nxp-msf1"><code>nxp,msf1</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Kinetis通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L279">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L329">已禁用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P002_nxp_kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio"><code>nxp,kinetis-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP LCD 8080接口上引出的GPIO引脚，例如LCD-PAR-035面板使用的引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L86">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P003_nxp_lcd-8080.md#std-dtcompatible-nxp-lcd-8080"><code>nxp,lcd-8080</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC 128位唯一标识符（Unique Identifier）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L876">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P009_nxp_lpc-uid.md#std-dtcompatible-nxp-lpc-uid"><code>nxp,lpc-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件自旋锁（Hardware Spinlock）</td>
<td>片上（On-Chip）</td>
<td>NXP SEMA42硬件信号量（Hardware Semaphore）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1450">已启用：1</a>）</td>
<td><a href="../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42"><code>nxp,sema42</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L446">已禁用：10</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1390">已禁用：2</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1304">已禁用：2</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="2">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>NXP TSI V6触摸感应输入设备（Touch Sensing Input Device）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1473">已禁用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P011_nxp_tsi-input.md#std-dtcompatible-nxp-tsi-input"><code>nxp,tsi-input</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L63">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L24">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L46">已禁用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>作为Zephyr邮箱（MBOX）的NXP邮箱单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L816">已启用：1</a>）</td>
<td><a href="../intercore_reference/P048_NXPMAILBOX邮箱绑定.md#dtbinding-nxp-mbox-mailbox"><code>nxp,mbox-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>低功耗Flexcomm（Low Power Flexcomm）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L500">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L417">已禁用：9</a>）</td>
<td><a href="../hardware/P702_NXP低功耗灵活通信接口绑定.md#dtbinding-nxp-lp-flexcomm"><code>nxp,lp-flexcomm</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示总线接口（MIPI-DBI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO LCD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1337">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P005_nxp_mipi-dbi-flexio-lcdif.md#std-dtcompatible-nxp-mipi-dbi-flexio-lcdif"><code>nxp,mipi-dbi-flexio-lcdif</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1330">已禁用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L866">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP FlexSPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mcx_nx4x_evk/mcx_nx4x_evk.dtsi?plain=1#L194">已禁用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P023_nxp_imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor"><code>nxp,imx-flexspi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">多路复用器（MUX）</td>
<td>片上（On-Chip）</td>
<td>NXP输入复用器（INPUTMUX）外设绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L156">已禁用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux"><code>nxp,inputmux</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>NXP OTPC电子熔丝（eFuse）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L890">已启用：1</a>）</td>
<td><a href="../otp_binding_reference/P005_nxp_otpc.md#std-dtcompatible-nxp-otpc"><code>nxp,otpc</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L237">已启用：6</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P017_nxp_port-pinmux.md#std-dtcompatible-nxp-port-pinmux"><code>nxp,port-pinmux</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L110">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P016_nxp_port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl"><code>nxp,port-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="3">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>NXP系统电源控制器（SPC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1424">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P001_nxp_spc.md#std-dtcompatible-nxp-spc"><code>nxp,spc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP内核模式控制器（CMC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1438">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P014_nxp_cmc.md#std-dtcompatible-nxp-cmc"><code>nxp,cmc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP智能电源开关（VBAT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1444">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P002_nxp_vbat.md#std-dtcompatible-nxp-vbat"><code>nxp,vbat</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>此电源域在进入及退出指定电源状态（Power State）时开启或关闭设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L103">已启用：1</a>）</td>
<td><a href="../power_domain_binding_reference/P007_power-domain-soc-state-change.md#std-dtcompatible-power-domain-soc-state-change"><code>power-domain-soc-state-change</code></a></td>
</tr>
<tr>
<td rowspan="3">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>包含mcux-pwm子模块的NXP eFLEX PWM模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1025">已启用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P003_nxp_flexpwm.md#std-dtcompatible-nxp-flexpwm"><code>nxp,flexpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1031">已禁用：4</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P005_nxp_imx-pwm.md#std-dtcompatible-nxp-imx-pwm"><code>nxp,imx-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP状态可配置定时器（SCTimer）脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1150">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P012_nxp_sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm"><code>nxp,sctimer-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>NXP VREF SoC外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1179">已禁用：1</a>）</td>
<td><a href="../hardware/P652_NXP参考电压绑定.md#dtbinding-nxp-vref"><code>nxp,vref</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L150">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P009_nxp_lpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset"><code>nxp,lpc-syscon-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>NXP EdgeLock安全子系统的真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1486">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P017_nxp_els-trng.md#std-dtcompatible-nxp-els-trng"><code>nxp,els-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>独立实时时钟（IRTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1379">已禁用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P012_nxp_irtc.md#std-dtcompatible-nxp-irtc"><code>nxp,irtc</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1169">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P014_nxp_imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc"><code>nxp,imx-usdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX正交解码器（QDC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1076">已禁用：2</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P007_nxp_mcux-qdc.md#std-dtcompatible-nxp-mcux-qdc"><code>nxp,mcux-qdc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L510">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L428">已禁用：9</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L435">已禁用：10</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxn54x.dtsi?plain=1#L20">已禁用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L135">已启用：3</a>）</td>
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
<td>i.MX RT5xx／6xx上的NXP操作系统定时器（OS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L882">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P008_nxp_os-timer.md#std-dtcompatible-nxp-os-timer"><code>nxp,os-timer</code></a></td>
</tr>
<tr>
<td rowspan="3">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>设备模式下的NPX Kinetis USBFSOTG控制器，厂商缩写NPX按原文保留（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1233">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P007_nxp_kinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd"><code>nxp,kinetis-usbd</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1243">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1252">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>LPC窗口看门狗定时器（Windowed Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1008">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P011_nxp_lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt"><code>nxp,lpc-wwdt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP外部看门狗监测器（External Watchdog Monitor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1017">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P007_nxp_ewm.md#std-dtcompatible-nxp-ewm"><code>nxp,ewm</code></a></td>
</tr>
<tr>
<td rowspan="1">唤醒控制器（Wakeup Controller）</td>
<td>片上（On-Chip）</td>
<td>作为唤醒控制器（WUC）的NXP唤醒单元（WUU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxn/nxp_mcxnx4x_common.dtsi?plain=1#L1431">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P008_nxp_wuc-wuu.md#std-dtcompatible-nxp-wuc-wuu"><code>nxp,wuc-wuu</code></a></td>
</tr>
</table>

## 译注

N5XX-EVK使用MCXN547，主要说明转至N9XX-EVK；本页自己的目标与功能表完整保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [MCX-N5XX-EVK](https://www.nxp.com/design/design-center/development-boards-and-designs/MCX-N5XX-EVK)：HTTP Error 404: Not Found。
- [mcx-n94x-54x-highly-integrated-multicore-mcus-with-on-chip-accelerators-intelligent-peripherals-and-advanced-security:MCX-N94X-N54X](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-n-series-microcontrollers/mcx-n94x-54x-highly-integrated-multicore-mcus-with-on-chip-accelerators-intelligent-peripherals-and-advanced-security:MCX-N94X-N54X)：HTTP Error 404: Not Found。

---

[上一章](P001_LS1046A_RDB.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_MCX-N9XX-EVK.md)
