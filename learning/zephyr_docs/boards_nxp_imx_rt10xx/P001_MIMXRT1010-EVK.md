---
id: learning.zephyr-docs.boards-nxp-imx-rt10xx.page-1
title: MIMXRT1010-EVK
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1010_evk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mimxrt1010_evk"></a>

# 第1章\_MIMXRT1010-EVK

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1010_evk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mimxrt1010_evk.jpg](images/mimxrt1010_evk.jpg)](images/mimxrt1010_evk.jpg)

MIMXRT1010-EVK

名称（Name）：

`mimxrt1010_evk`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mimxrt1011](https://docs.zephyrproject.org/latest/boards/index.html#soc=mimxrt1011)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt1010_evk/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

i.MX RT1010以低成本低矮四方扁平封装（LQFP）为i.MX RT跨界处理器（Crossover Processor）系列提供新的入门选择，同时保留该系列的高性能及易用性。NXP MCUXpresso软件和工具完整支持此器件。

<a id="hardware"></a>

## 硬件（Hardware）


- MIMXRT1011DAE5A微控制器（MCU）
- 存储器（Memory）


  - 128 Mbit QSPI闪存
- 连接能力（Connectivity）


  - Micro-USB主机及OTG连接器
  - Arduino接口（Interface）
- 音频（Audio）


  - 音频编解码器（Audio Codec）
  - 四极耳机音频插孔
  - 外部扬声器连接
  - 麦克风（Microphone）
- 调试（Debug）


  - 10引脚JTAG连接器
  - 使用DAPLink的OpenSDA

MIMXRT1010 SoC及MIMXRT1010-EVK开发板的更多信息见以下资料：


- [i.MX RT1010 网站](https://www.nxp.com/imxrt1010)
- [i.MX RT1010 数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/IMXRT1010CEC.pdf)
- [i.MX RT1010 参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=IMXRT1010RM)
- [MIMXRT1010-EVK 网站](https://www.nxp.com/MIMXRT1010-EVK)
- [MIMXRT1010-EVK 用户指南（User Guide）](https://www.nxp.com/webapp/Download?colCode=MIMXRT1010EVKHUG)
- [MIMXRT1010-EVK 设计文件（Design Files）](https://www.nxp.com/webapp/Download?colCode=IMXRT1010-EVK-DESIGN-FILES)

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
<td>AT25SF128A</td>
<td>FLEXSPI</td>
<td>通过闪存配置块（Flash Configuration Block）启用，该配置块在启动时设置FlexSPI。</td>
</tr>
</table>

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`mimxrt1010_evk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mimxrt1010_evk-hw-features"></a>

<a id="mimxrt1010_evk-mimxrt1010_evk/mimxrt1011-hw-features-section"></a>

#### `mimxrt1010_evk/mimxrt1011`目标（Target）

<a id="mimxrt1010_evk-mimxrt1010_evk/mimxrt1011-hw-features-panel"></a>

<a id="mimxrt1010_evk-mimxrt1010_evk/mimxrt1011-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、16 MiB Flash。

<a id="mimxrt1010_evk-mimxrt1010_evk/mimxrt1011-hw-features-table"></a>

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
<td rowspan="5">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>i.MX时钟控制模块（CCM / Clock Controller Module）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L311">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P021_nxp_imx-ccm.md#std-dtcompatible-nxp-imx-ccm"><code>nxp,imx-ccm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L323">已启用：2</a>）</td>
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
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX通用定时器（GPT / General-Purpose Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L176">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P004_nxp_imx-gpt.md#std-dtcompatible-nxp-imx-gpt"><code>nxp,imx-gpt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SNVS低功耗／高功耗域实时时钟计数器（LP/HP Realtime Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L351">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P006_nxp_imx-snvs-rtc.md#std-dtcompatible-nxp-imx-snvs-rtc"><code>nxp,imx-snvs-rtc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP周期中断定时器（PIT / Periodic Interrupt Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1210">已启用：1</a>）</td>
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
<td>NXP数据协处理器（DCP / Data Co-Processor）密码加速器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt1010.dtsi?plain=1#L129">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P004_nxp_mcux-dcp.md#std-dtcompatible-nxp-mcux-dcp"><code>nxp,mcux-dcp</code></a></td>
</tr>
<tr>
<td rowspan="1">调试（Debug）</td>
<td>片上（On-Chip）</td>
<td>ARMv7仪器化跟踪宏单元（ITM / Instrumentation Trace Macrocell）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L44">已启用：1</a>）</td>
<td><a href="../debug_binding_reference/P001_ARMv7M_ITM调试绑定.md#std-dtcompatible-arm-armv7m-itm"><code>arm,armv7m-itm</code></a></td>
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
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L368">已启用：3</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P030_nxp_imx-gpio.md#std-dtcompatible-nxp-imx-gpio"><code>nxp,imx-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1010_evk/mimxrt1010_evk.dts?plain=1#L57">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt1010.dtsi?plain=1#L140">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt1010.dtsi?plain=1#L151">已禁用：1</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt1010.dtsi?plain=1#L300">已禁用：2</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1010_evk/mimxrt1010_evk.dts?plain=1#L47">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1010_evk/mimxrt1010_evk.dts?plain=1#L38">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexRAM片上RAM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L101">已启用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P015_nxp_flexram.md#std-dtcompatible-nxp-flexram"><code>nxp,flexram</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX SNVS低功耗通用寄存器，用作电池后备RAM（Battery-Backed RAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L363">已启用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P001_nxp_imx-snvs-gpr.md#std-dtcompatible-nxp-imx-snvs-gpr"><code>nxp,imx-snvs-gpr</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1245">已禁用：1</a>）</td>
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
<td>NXP FlexSPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1010_evk/mimxrt1010_evk.dts?plain=1#L99">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P023_nxp_imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor"><code>nxp,imx-flexspi-nor</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1010_evk/mimxrt1010_evk.dts?plain=1#L111">已启用：1</a>）</td>
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
<td>包含mcux-pwm子模块的NXP eFLEX PWM模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt1010.dtsi?plain=1#L212">已启用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P003_nxp_flexpwm.md#std-dtcompatible-nxp-flexpwm"><code>nxp,flexpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt1010.dtsi?plain=1#L217">已禁用：4</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P005_nxp_imx-pwm.md#std-dtcompatible-nxp-imx-pwm"><code>nxp,imx-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Kinetis真随机数发生器（TRNG / True Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L870">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P020_nxp_kinetis-trng.md#std-dtcompatible-nxp-kinetis-trng"><code>nxp,kinetis-trng</code></a></td>
</tr>
<tr>
<td rowspan="2">传感器（Sensors）</td>
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
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L551">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L561">已禁用：3</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt1010.dtsi?plain=1#L104">已启用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt1010.dtsi?plain=1#L173">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt1010.dtsi?plain=1#L185">已禁用：1</a>）</td>
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
<td>NXP EHCI USB主机控制器（Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L897">已禁用：2</a>）</td>
<td><a href="../usb_soc_binding_reference/P009_nxp_uhc-ehci.md#std-dtcompatible-nxp-uhc-ehci"><code>nxp,uhc-ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L915">已禁用：2</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt1010.dtsi?plain=1#L268">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>i.MX RT看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt10xx/nxp_rt10xx.dtsi?plain=1#L1008">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P009_nxp_imx-wdog.md#std-dtcompatible-nxp-imx-wdog"><code>nxp,imx-wdog</code></a></td>
</tr>
</table>

注意（Note）

尚未支持的其他功能可参考[MIMXRT1064-EVK](P009_MIMXRT1064-EVK.md#mimxrt1064_evk)，它是NXP i.MX RT10xx系列功能覆盖更广的开发板（Superset Board）。NXP优先在该板落实Zephyr完整平台支持（Full Platform Support），因此该板可能已有可复用于mimxrt1010_evk的额外功能：

<a id="connections-and-i-os"></a>

### 连接与I/O（Connections and I/Os）

MIMXRT1010 SoC有5对引脚复用／GPIO控制器。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>GPIO_11</td>
<td>通用输入输出（GPIO）</td>
<td>发光二极管（LED）</td>
</tr>
<tr>
<td>GPIO_SD_05</td>
<td>通用输入输出（GPIO）</td>
<td>SW4</td>
</tr>
<tr>
<td>GPIO_10</td>
<td>LPUART1_TX</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>GPIO_09</td>
<td>LPUART1_RX</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>GPIO_01</td>
<td>LPI2C1_SDA</td>
<td>I2C串行数据（SDA）</td>
</tr>
<tr>
<td>GPIO_02</td>
<td>LPI2C1_CLK</td>
<td>I2C串行时钟（SCL）</td>
</tr>
<tr>
<td>GPIO_AD_03</td>
<td>LPSPI1_SDI</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>GPIO_AD_04</td>
<td>LPSPI1_SDO</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>GPIO_AD_05</td>
<td>LPSPI1_PCS0</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>GPIO_AD_06</td>
<td>LPSPI1_SCK</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>GPIO_AD_01</td>
<td>模数转换器（ADC）</td>
<td>ADC1通道1</td>
</tr>
<tr>
<td>GPIO_AD_02</td>
<td>模数转换器（ADC）</td>
<td>ADC1通道2</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

MIMXRT1010 SoC配置为使用SysTick作为系统时钟源，原文列出的运行频率为500 MHz。

启用电源管理后，板上的32 kHz低频振荡器将作为通用定时器（GPT）的时钟源，用于生成系统时钟。这有助于进入更低功耗状态，但会降低时间分辨率。

<a id="serial-port"></a>

### 串口（Serial Port）

MIMXRT1010 SoC有4路UART，LPUART1配置为控制台，其余未使用。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`mimxrt1010_evk`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

此板支持3种调试主机工具。先安装所选工具，再按“配置调试探针”（[Configuring a Debug Probe](#configuring-a-debug-probe)）说明配置开发板。


- LinkServer调试主机工具，默认，NXP提供支持（[LinkServer调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#linkserver-debug-host-tools)）
- J-Link调试主机工具，NXP提供支持（[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)）
- pyOCD调试主机工具，NXP不提供支持（[pyOCD调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#pyocd-debug-host-tools)）

主机工具及开发板配置完成后，即可按常规方式构建及烧录应用，详情见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）及“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

<a id="configuring-a-debug-probe"></a>

### 配置调试探针（Configuring a Debug Probe）

RT1010的SWD隔离跳线为J61／J62，DFU模式跳线为J22，10引脚JTAG／SWD排针为J55。

烧录及调试都使用调试探针。此板提供板载LPC-Link2探针，其默认固件为LPC-Link2 DAPLink。（[LPC-Link2板载调试探针](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#lpc-link2-onboard-debug-probe)；[LPC-Link2 DAPLink板载调试探针](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#lpclink2-daplink-onboard-debug-probe)）

根据安装的主机工具，按以下说明配置调试探针：


- J-Link调试主机工具：[LPC-Link2探针使用J-Link](#using-j-link-with-lpc-link2-probe)（[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)）
- LinkServer调试主机工具：[LPC-Link2探针使用CMSIS-DAP](#using-cmsis-dap-with-lpc-link2-probe)（[LinkServer调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#linkserver-debug-host-tools)）
- pyOCD调试主机工具：[LPC-Link2探针使用CMSIS-DAP](#using-cmsis-dap-with-lpc-link2-probe)（[pyOCD调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#pyocd-debug-host-tools)）

<a id="using-cmsis-dap-with-lpc-link2-probe"></a>

#### LPC-Link2探针使用CMSIS-DAP


1. 按[LPC-Link2 CMSIS-DAP板载调试探针](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#lpclink2-cmsis-onboard-debug-probe)说明，重新写入此板的默认调试固件。
2. 确保安装SWD隔离跳线。

<a id="using-j-link-with-lpc-link2-probe"></a>

#### LPC-Link2探针使用J-Link

有两种方案：将板载调试电路更新为Segger J-Link固件，或将外部J-Link调试探针接到EVK。（[J-Link外部调试探针（External Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#jlink-external-debug-probe)）

更新板载调试电路的步骤如下：


1. 将EVK电源切换为调试USB以外的来源，因为J-Link固件不会通过调试USB为EVK供电。
2. 按LPC-Link2 J-Link板载调试探针说明，重新写入此板的默认调试固件。（[LPC-Link2 J-Link板载调试探针（Onboard Debug Probe）](../debugging/P003_调试探针.md#lpclink2-jlink-onboard-debug-probe)）
3. 确保安装SWD隔离跳线。

使用外部J-Link时，先移除SWD隔离跳线，再连接外部JTAG／SWD排针。

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

无论选用何种调试探针，串口控制台均使用OpenSDA微控制器作为USB转串口适配器。确认J31和J32已短接，出厂默认短接，以便将UART信号接至OpenSDA。

用USB线缆将PC连接J41。

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
west build -b mimxrt1010_evk samples/hello_world
west flash
```

打开串口终端，按SW9复位开发板，终端应显示以下消息：

```text
Hello World! mimxrt1010_evk
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

原文使用SysTick作为system clock source的表述按来源保留；电源管理下改用32 kHz时钟源驱动GPT会降低分辨率。板载J-Link固件不通过调试USB为EVK供电；外部探针与板载探针的SWD隔离跳线状态不同。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [MIMXRT1010-EVK](https://www.nxp.com/MIMXRT1010-EVK)：HTTP Error 404: Not Found。
- [IMXRT1010CEC.pdf](https://www.nxp.com/docs/en/data-sheet/IMXRT1010CEC.pdf)：HTTP Error 404: Not Found。
- [imxrt1010](https://www.nxp.com/imxrt1010)：HTTP Error 404: Not Found。
- [Download?colCode=IMXRT1010-EVK-DESIGN-FILES](https://www.nxp.com/webapp/Download?colCode=IMXRT1010-EVK-DESIGN-FILES)：HTTP Error 404: Not Found。
- [Download?colCode=IMXRT1010RM](https://www.nxp.com/webapp/Download?colCode=IMXRT1010RM)：HTTP Error 404: Not Found。
- [Download?colCode=MIMXRT1010EVKHUG](https://www.nxp.com/webapp/Download?colCode=MIMXRT1010EVKHUG)：HTTP Error 404: Not Found。

---

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_MIMXRT1015-EVK.md)
