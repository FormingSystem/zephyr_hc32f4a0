---
id: learning.zephyr-docs.boards-nxp-frdm-imx-kinetis.page-5
title: FRDM-IMXRT700
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/frdm_imxrt700/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="frdm_imxrt700"></a>

# 第5章\_FRDM-IMXRT700

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/frdm_imxrt700/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`frdm_imxrt700`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mimxrt798s](https://docs.zephyrproject.org/latest/boards/index.html#soc=mimxrt798s)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_imxrt700/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

FRDM-IMXRT700是基于NXP i.MX RT700跨界MCU的紧凑、低成本开发板。i.MX RT700是多核器件，包含高性能主计算子系统（Main-compute）、第二个始终开启的感知计算子系统（Always-on Sense-compute）及专用协处理器。


- 主计算子系统包含主Arm® Cortex®-M33内核CPU0及集成的Cadence® Tensilica® HiFi 4 DSP。
- 感知计算子系统包含第二个Arm® Cortex®-M33内核CPU1及集成的Cadence® Tensilica® HiFi 1 DSP。

此Zephyr移植当前为两个Cortex-M33核提供基础支持，目标为cm33_cpu0及cm33_cpu1。

<a id="hardware"></a>

## 硬件（Hardware）


- MIMXRT798S片上系统（SoC）：


  - Arm Cortex-M33 CPU0主计算核
  - Arm Cortex-M33 CPU1感知计算核
  - HiFi 4及HiFi 1 DSP核，此移植尚不支持
- 板载MCU-Link调试探针，提供UART、SWD及SPI／I2C桥接
- 用于代码存储的四线SPI闪存，连接XSPI0
- RGB用户LED及用户按键
- 兼容Arduino和mikroBUS的扩展排针

<a id="id2"></a>

i.MX RT700 SoC更多信息见[i.MX RT700网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-rt-crossover-mcus/i-mx-rt700-crossover-mcu-with-arm-cortex-m33-npu-dsp-and-gpu-cores:i.MX-RT700) [注1](#id1)。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`frdm_imxrt700`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="frdm_imxrt700-hw-features"></a>

<a id="frdm_imxrt700-frdm_imxrt700/mimxrt798s/cm33_cpu0-hw-features-section"></a>

#### `frdm_imxrt700/mimxrt798s/cm33_cpu0`目标（Target）

<a id="frdm_imxrt700-frdm_imxrt700/mimxrt798s/cm33_cpu0-hw-features-panel"></a>

<a id="frdm_imxrt700-frdm_imxrt700/mimxrt798s/cm33_cpu0-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、32 MiB Flash。

<a id="frdm_imxrt700-frdm_imxrt700/mimxrt798s/cm33_cpu0-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L107">已禁用：1</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>片上（On-Chip）</td>
<td>NXP脉冲密度调制麦克风接口（PDM / MICFIL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1088">已禁用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P014_nxp_micfil.md#std-dtcompatible-nxp-micfil"><code>nxp,micfil</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L151">已启用：8</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟监测（Clock Monitor）</td>
<td>片上（On-Chip）</td>
<td>NXP频率测量（FREQME）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L174">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P004_nxp_freqme.md#std-dtcompatible-nxp-freqme"><code>nxp,freqme</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis模拟比较器（ACMP / Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1392">已禁用：1</a>）</td>
<td><a href="../hardware/P745_NXPKinetis模拟比较器绑定.md#dtbinding-nxp-kinetis-acmp"><code>nxp,kinetis-acmp</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>通过计数器API提供的NXP IRTC唤醒定时器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L137">已禁用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P008_nxp_irtc-wake-timer.md#std-dtcompatible-nxp-irtc-wake-timer"><code>nxp,irtc-wake-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L257">已禁用：5</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器（Multirate Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1233">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P015_nxp_mrt.md#std-dtcompatible-nxp-mrt"><code>nxp,mrt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1244">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P014_nxp_mrt-channel.md#std-dtcompatible-nxp-mrt-channel"><code>nxp,mrt-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1441">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P006_nxp_crc.md#std-dtcompatible-nxp-crc"><code>nxp,crc</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L317">已禁用：2</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>板载（On-Board）</td>
<td>NXP XSPI闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt700/frdm_imxrt700_mimxrt798s_cm33_cpu0.dts?plain=1#L116">已禁用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P019_nxp_xspi-nor.md#std-dtcompatible-nxp-xspi-nor"><code>nxp,xspi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Kinetis通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L366">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L392">已禁用：6</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P002_nxp_kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio"><code>nxp,kinetis-gpio</code></a></td>
</tr>
<tr>
<td rowspan="2">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP RSTCTL复位原因标志读取（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L138">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P013_nxp_rstctl-hwinfo.md#std-dtcompatible-nxp-rstctl-hwinfo"><code>nxp,rstctl-hwinfo</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP LPC 128位唯一标识符（Unique Identifier）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1426">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P009_nxp_lpc-uid.md#std-dtcompatible-nxp-lpc-uid"><code>nxp,lpc-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件自旋锁（Hardware Spinlock）</td>
<td>片上（On-Chip）</td>
<td>NXP SEMA42硬件信号量（Hardware Semaphore）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L203">已禁用：2</a>）</td>
<td><a href="../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42"><code>nxp,sema42</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L502">已禁用：15</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1303">已禁用：3</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt700/frdm_imxrt700_mimxrt798s_cm33_cpu0.dts?plain=1#L44">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt700/frdm_imxrt700_mimxrt798s_cm33_cpu0.dts?plain=1#L30">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>用作Zephyr邮箱（MBOX）的NXP i.MX消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1059">已禁用：3</a>）</td>
<td><a href="../intercore_reference/P047_NXPiMX消息单元邮箱绑定.md#dtbinding-nxp-mbox-imx-mu"><code>nxp,mbox-imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>低功耗Flexcomm（Low Power Flexcomm）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L470">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L512">已禁用：13</a>）</td>
<td><a href="../hardware/P702_NXP低功耗灵活通信接口绑定.md#dtbinding-nxp-lp-flexcomm"><code>nxp,lp-flexcomm</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示总线接口（MIPI-DBI）</td>
<td>片上（On-Chip）</td>
<td>NXP DCnano LCD控制器的显示总线接口（DBI）设置（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1367">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P004_nxp_mipi-dbi-dcnano-lcdif.md#std-dtcompatible-nxp-mipi-dbi-dcnano-lcdif"><code>nxp,mipi-dbi-dcnano-lcdif</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示串行接口（MIPI-DSI）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX MIPI DSI双通道显示串行接口（2L）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1378">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P014_nxp_mipi-dsi-2l.md#std-dtcompatible-nxp-mipi-dsi-2l"><code>nxp,mipi-dsi-2l</code></a></td>
</tr>
<tr>
<td rowspan="2">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1269">已禁用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX RTxxx DSP控制驱动，适用于i.MX RT700 HiFi 4 DSP（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L72">已禁用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P005_nxp_rt700-dsp-ctrl-hifi4.md#std-dtcompatible-nxp-rt700-dsp-ctrl-hifi4"><code>nxp,rt700-dsp-ctrl-hifi4</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt700/frdm_imxrt700_mimxrt798s_cm33_cpu0.dts?plain=1#L127">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">多路复用器（MUX）</td>
<td>片上（On-Chip）</td>
<td>NXP输入复用器（INPUTMUX）外设绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L166">已禁用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux"><code>nxp,inputmux</code></a></td>
</tr>
<tr>
<td rowspan="1">非易失存储器（NVMEM）</td>
<td>片上（On-Chip）</td>
<td>非易失存储器固定布局（Fixed Layout for Non-Volatile Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1406">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P009_fixed-layout.md#std-dtcompatible-fixed-layout"><code>fixed-layout</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>NXP RT7xx片上一次性可编程存储器（OCOTP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1401">已禁用：1</a>）</td>
<td><a href="../otp_binding_reference/P006_nxp_rt7xx-ocotp.md#std-dtcompatible-nxp-rt7xx-ocotp"><code>nxp,rt7xx-ocotp</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>LPC I/O引脚配置（IOCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L187">已启用：3</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P007_nxp_lpc-iocon.md#std-dtcompatible-nxp-lpc-iocon"><code>nxp,lpc-iocon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>RT600／RT500引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P018_nxp_rt-iocon-pinctrl.md#std-dtcompatible-nxp-rt-iocon-pinctrl"><code>nxp,rt-iocon-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>此电源域在进入及退出指定电源状态（Power State）时开启或关闭设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../power_domain_binding_reference/P007_power-domain-soc-state-change.md#std-dtcompatible-power-domain-soc-state-change"><code>power-domain-soc-state-change</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NXP状态可配置定时器（SCTimer）脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1357">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P012_nxp_sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm"><code>nxp,sctimer-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP RSTCTL外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L123">已启用：4</a>）</td>
<td><a href="../reset_controller_binding_reference/P011_nxp_rstctl.md#std-dtcompatible-nxp-rstctl"><code>nxp,rstctl</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>独立实时时钟（IRTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L128">已禁用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P012_nxp_irtc.md#std-dtcompatible-nxp-irtc"><code>nxp,irtc</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1207">已禁用：2</a>）</td>
<td><a href="../sdhc_binding_reference/P014_nxp_imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc"><code>nxp,imx-usdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>NXP PMC温度传感器（PMC-TMPSNS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1419">已禁用：1</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P011_nxp_pmc-tmpsns.md#std-dtcompatible-nxp-pmc-tmpsns"><code>nxp,pmc-tmpsns</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L483">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L525">已禁用：13</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L491">已禁用：16</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L58">已启用：6</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已禁用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX RT5xx／6xx上的NXP操作系统定时器（OS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1277">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P008_nxp_os-timer.md#std-dtcompatible-nxp-os-timer"><code>nxp,os-timer</code></a></td>
</tr>
<tr>
<td rowspan="3">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1159">已禁用：2</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB主机控制器（Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1170">已禁用：2</a>）</td>
<td><a href="../usb_soc_binding_reference/P009_nxp_uhc-ehci.md#std-dtcompatible-nxp-uhc-ehci"><code>nxp,uhc-ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1201">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td rowspan="2">视频（Video）</td>
<td>片上（On-Chip）</td>
<td>NXP JPEG解码器可解码JPEG／mJPEG压缩帧（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1449">已禁用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P009_nxp_jpegdec.md#std-dtcompatible-nxp-jpegdec"><code>nxp,jpegdec</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP PNG解码器可解码PNG压缩帧（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1457">已禁用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P011_nxp_pngdec.md#std-dtcompatible-nxp-pngdec"><code>nxp,pngdec</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>LPC窗口看门狗定时器（Windowed Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1285">已禁用：2</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P011_nxp_lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt"><code>nxp,lpc-wwdt</code></a></td>
</tr>
<tr>
<td rowspan="1">唤醒控制器（Wakeup Controller）</td>
<td>片上（On-Chip）</td>
<td>用作唤醒控制器（WUC）的NXP睡眠控制器（SLEEPCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L158">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P007_nxp_sleepcon-wuc.md#std-dtcompatible-nxp-sleepcon-wuc"><code>nxp,sleepcon-wuc</code></a></td>
</tr>
<tr>
<td rowspan="1">扩展串行外设接口（xSPI）</td>
<td>片上（On-Chip）</td>
<td>NXP XSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L101">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L27">已禁用：2</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P015_nxp_xspi.md#std-dtcompatible-nxp-xspi"><code>nxp,xspi</code></a></td>
</tr>
</table>

<a id="frdm_imxrt700-frdm_imxrt700/mimxrt798s/cm33_cpu1-hw-features-section"></a>

#### `frdm_imxrt700/mimxrt798s/cm33_cpu1`目标（Target）

<a id="frdm_imxrt700-frdm_imxrt700/mimxrt798s/cm33_cpu1-hw-features-panel"></a>

<a id="frdm_imxrt700-frdm_imxrt700/mimxrt798s/cm33_cpu1-hw-features-memory"></a>

该开发板目标的片上存储容量：256 KiB RAM、512 KiB Flash。

<a id="frdm_imxrt700-frdm_imxrt700/mimxrt798s/cm33_cpu1-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L14">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L107">已禁用：1</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L151">已启用：8</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis模拟比较器（ACMP / Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L404">已禁用：1</a>）</td>
<td><a href="../hardware/P745_NXPKinetis模拟比较器绑定.md#dtbinding-nxp-kinetis-acmp"><code>nxp,kinetis-acmp</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L88">已禁用：3</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Kinetis通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L156">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L169">已禁用：2</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P002_nxp_kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio"><code>nxp,kinetis-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP RSTCTL复位原因标志读取（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L138">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P013_nxp_rstctl-hwinfo.md#std-dtcompatible-nxp-rstctl-hwinfo"><code>nxp,rstctl-hwinfo</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件自旋锁（Hardware Spinlock）</td>
<td>片上（On-Chip）</td>
<td>NXP SEMA42硬件信号量（Hardware Semaphore）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L203">已禁用：2</a>）</td>
<td><a href="../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42"><code>nxp,sema42</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L225">已禁用：5</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L130">已禁用：2</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt700/frdm_imxrt700_mimxrt798s_cm33_cpu1.dts?plain=1#L39">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_imxrt700/frdm_imxrt700_mimxrt798s_cm33_cpu1.dts?plain=1#L29">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>用作Zephyr邮箱（MBOX）的NXP i.MX消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L356">已禁用：3</a>）</td>
<td><a href="../intercore_reference/P047_NXPiMX消息单元邮箱绑定.md#dtbinding-nxp-mbox-imx-mu"><code>nxp,mbox-imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>低功耗Flexcomm（Low Power Flexcomm）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L275">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L195">已禁用：3</a>）</td>
<td><a href="../hardware/P702_NXP低功耗灵活通信接口绑定.md#dtbinding-nxp-lp-flexcomm"><code>nxp,lp-flexcomm</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>LPC I/O引脚配置（IOCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L187">已启用：2</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P007_nxp_lpc-iocon.md#std-dtcompatible-nxp-lpc-iocon"><code>nxp,lpc-iocon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>RT600／RT500引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P018_nxp_rt-iocon-pinctrl.md#std-dtcompatible-nxp-rt-iocon-pinctrl"><code>nxp,rt-iocon-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP RSTCTL外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L123">已启用：4</a>）</td>
<td><a href="../reset_controller_binding_reference/P011_nxp_rstctl.md#std-dtcompatible-nxp-rstctl"><code>nxp,rstctl</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>独立实时时钟（IRTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L62">已禁用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P012_nxp_irtc.md#std-dtcompatible-nxp-irtc"><code>nxp,irtc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L287">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L207">已禁用：3</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L214">已禁用：4</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L58">已启用：6</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已禁用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX RT5xx／6xx上的NXP操作系统定时器（OS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L397">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P008_nxp_os-timer.md#std-dtcompatible-nxp-os-timer"><code>nxp,os-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">唤醒控制器（Wakeup Controller）</td>
<td>片上（On-Chip）</td>
<td>用作唤醒控制器（WUC）的NXP睡眠控制器（SLEEPCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L80">已禁用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P007_nxp_sleepcon-wuc.md#std-dtcompatible-nxp-sleepcon-wuc"><code>nxp,sleepcon-wuc</code></a></td>
</tr>
<tr>
<td rowspan="1">扩展串行外设接口（xSPI）</td>
<td>片上（On-Chip）</td>
<td>NXP XSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L27">已禁用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P015_nxp_xspi.md#std-dtcompatible-nxp-xspi"><code>nxp,xspi</code></a></td>
</tr>
</table>

此基础移植为frdm_imxrt700目标启用以下功能：

<table>
<tr>
<th>接口（Interface）</th>
<th>控制器（Controller）</th>
<th>驱动／组件（Driver/Component）</th>
</tr>
<tr>
<td>通用输入输出（GPIO）</td>
<td>片上（On-Chip）</td>
<td>通用输入输出（gpio）</td>
</tr>
<tr>
<td>通用异步收发器（UART）</td>
<td>片上（On-Chip）</td>
<td>串口，作为调试控制台</td>
</tr>
</table>

其他外设将在后续工作中启用。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`frdm_imxrt700`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
</table>

此板使用J-Link调试探针烧录及调试，例如刷入J-Link固件的板载MCU-Link，或外部J-Link。

注意（Note）

当前尚不支持LinkServer。原文指出，当前版本没有FRDM-IMXRT700板定义，且仅提供i.MX RT700 XSPI的八线闪存加载器，无法编程此板的四线SPI NOR闪存。待LinkServer加入支持后，原文将在此记录支持版本，并补充相应烧录及调试步骤。

<a id="building"></a>

### 构建（Building）

CPU0调试控制台经MCU-Link桥连接FLEXCOMM0，即LPUART0；CPU1使用FLEXCOMM19，即LPUART19。

为CPU0构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例，原文标题“Build and the”不完整：

```text
# From the root of the zephyr repository
west build -b frdm_imxrt700/mimxrt798s/cm33_cpu0 samples/hello_world
west flash
```

为CPU0构建[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)示例：

```text
# From the root of the zephyr repository
west build -b frdm_imxrt700/mimxrt798s/cm33_cpu0 samples/basic/blinky
west flash
```

以感知计算核CPU1为目标时，使用frdm_imxrt700/mimxrt798s/cm33_cpu1。

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-rt-crossover-mcus/i-mx-rt700-crossover-mcu-with-arm-cortex-m33-npu-dsp-and-gpu-cores:i.MX-RT700](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-rt-crossover-mcus/i-mx-rt700-crossover-mcu-with-arm-cortex-m33-npu-dsp-and-gpu-cores:i.MX-RT700)

## 译注

DSP硬件存在及自动生成表中的控制器条目，不代表Zephyr已支持DSP核；原文仅支持基于Cortex-M33的处理单元。当前LinkServer缺少板卡定义且闪存加载器不适合板上Quad SPI器件，按原文使用J-Link。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [i-mx-rt700-crossover-mcu-with-arm-cortex-m33-npu-dsp-and-gpu-cores:i.MX-RT700](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-rt-crossover-mcus/i-mx-rt700-crossover-mcu-with-arm-cortex-m33-npu-dsp-and-gpu-cores:i.MX-RT700)：HTTP Error 404: Not Found。

---

[上一章](P004_FRDM-iMXRT1186.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_FRDM-K22F.md)
