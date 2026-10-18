---
id: learning.zephyr-docs.boards-cdac-to-cthings.page-14
title: Pebble Round 2
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/coredevices/pr2/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="pr2"></a>

# 第14章\_Pebble Round 2

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/coredevices/pr2/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/pr2.webp](images/pr2.webp)](images/pr2.webp)

Pebble Round 2

名称（Name）：

`pr2`

厂商（Vendor）：

[Core Devices LLC公司](https://docs.zephyrproject.org/latest/boards/index.html#vendor=coredevices)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[sf32lb52jud6](https://docs.zephyrproject.org/latest/boards/index.html#soc=sf32lb52jud6)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/coredevices/pr2/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Pebble Round 2是一款基于SF32LB52x系列SoC的智能手表。

<a id="id3"></a>

更多手表信息见[RePebble网站](https://repebble.com/)[注1](#id2)。

<a id="hardware"></a>

## 硬件（Hardware）

Pebble Round 2提供以下硬件组件：


- 思澈（SiFli）SF32LB52JUD6
- nPM1300电源管理芯片（PMIC），用于供电及电池充电
- GD25Q256E 256 Mb QSPI NOR闪存
- JDI LS013B7DD02像素内存储（MiP / Memory-in-Pixel）64色圆形显示屏
- CST816T电容触摸显示驱动器（Capacitive Touch Display Driver）
- 由AW9346E驱动的RGB背光
- W1160环境光传感器
- 四个实体按键
- LIS2DW12低功耗加速度计（Accelerometer）
- MMC5603NJ磁力计（Magnetometer）
- 双PDM麦克风
- 由AW86225CSR驱动的线性谐振致动器（LRA）
- 编程连接器（Programming Connector）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`pr2`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="pr2-hw-features"></a>

<a id="pr2-pr2/sf32lb52jud6-hw-features-section"></a>

#### `pr2/sf32lb52jud6`目标（Target）

<a id="pr2-pr2/sf32lb52jud6-hw-features-panel"></a>

<a id="pr2-pr2/sf32lb52jud6-hw-features-memory"></a>

该开发板目标的片上存储容量：511 KiB RAM、N/A Flash。

<a id="pr2-pr2/sf32lb52jud6-hw-features-table"></a>

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
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB模数转换（ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L359">已禁用：1</a>）</td>
<td><a href="../hardware/P898_SiFliSF32LB通用模数转换器绑定.md#dtbinding-sifli-sf32lb-gpadc"><code>sifli,sf32lb-gpadc</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB音频编解码器（Audio Codec）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L226">已禁用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P016_sifli_sf32lb-audcodec.md#std-dtcompatible-sifli-sf32lb-audcodec"><code>sifli,sf32lb-audcodec</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>在应用CPU与蓝牙低功耗CPU（LCPU）之间交换蓝牙主机控制器接口（HCI）流量的邮箱设备（Mailbox Device）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L196">已禁用：1</a>）</td>
<td><a href="../bluetooth_vendor_hci_binding_reference/P014_sifli_sf32lb-mailbox.md#std-dtcompatible-sifli-sf32lb-mailbox"><code>sifli,sf32lb-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="4">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）复位与时钟控制器（RCC / Reset and Clock Controller）是一种多功能外设，负责所有SoC外设的复位及其时钟控制（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P026_sifli_sf32lb-rcc-clk.md#std-dtcompatible-sifli-sf32lb-rcc-clk"><code>sifli,sf32lb-rcc-clk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）DLL是一种由RCC控制的数字锁相环（Digital Phase-Locked Loop）外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L82">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L87">已禁用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P024_sifli_sf32lb-dll.md#std-dtcompatible-sifli-sf32lb-dll"><code>sifli,sf32lb-dll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L40">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L33">已禁用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB HXT48时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L58">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P025_sifli_sf32lb-hxt48.md#std-dtcompatible-sifli-sf32lb-hxt48"><code>sifli,sf32lb-hxt48</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L169">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P009_sifli_sf32lb-crc.md#std-dtcompatible-sifli-sf32lb-crc"><code>sifli,sf32lb-crc</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB系列加密加速器（Crypto Accelerator），AES／HASH（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L176">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P011_sifli_sf32lb-crypto.md#std-dtcompatible-sifli-sf32lb-crypto"><code>sifli,sf32lb-crypto</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB液晶显示控制器（LCDC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L123">已禁用：1</a>）</td>
<td><a href="../display_panel_renesas_sharp_binding_reference/P016_sifli_sf32lb-lcdc.md#std-dtcompatible-sifli-sf32lb-lcdc"><code>sifli,sf32lb-lcdc</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>SF32LB直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L184">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P017_sifli_sf32lb-dmac.md#std-dtcompatible-sifli-sf32lb-dmac"><code>sifli,sf32lb-dmac</code></a></td>
</tr>
<tr>
<td rowspan="3">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>nPM1300通用输入输出（GPIO）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/coredevices/pr2/pr2.dts?plain=1#L124">已启用：1</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P011_nordic_npm1300-gpio.md#std-dtcompatible-nordic-npm1300-gpio"><code>nordic,npm1300-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SF32LB GPIO父节点（Parent）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L310">已启用：1</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P009_sifli_sf32lb-gpio-parent.md#std-dtcompatible-sifli-sf32lb-gpio-parent"><code>sifli,sf32lb-gpio-parent</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SF32LB通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L324">已启用：2</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P010_sifli_sf32lb-gpio.md#std-dtcompatible-sifli-sf32lb-gpio"><code>sifli,sf32lb-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L270">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L300">已禁用：1</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P003_sifli_sf32lb-i2c.md#std-dtcompatible-sifli-sf32lb-i2c"><code>sifli,sf32lb-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/coredevices/pr2/pr2.dts?plain=1#L30">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="2">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB复位与时钟控制（RCC / Reset and Clock Control）是一种多功能外设，负责所有SoC外设的复位与时钟控制（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L68">已启用：1</a>）</td>
<td><a href="../hardware/P716_SF32LB复位与时钟控制绑定.md#dtbinding-sifli-sf32lb-rcc"><code>sifli,sf32lb-rcc</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Nordic nPM1300（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/coredevices/pr2/pr2.dts?plain=1#L105">已启用：1</a>）</td>
<td><a href="../hardware/P685_nPM1300多功能设备绑定.md#dtbinding-nordic-npm1300"><code>nordic,npm1300</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示总线接口（MIPI-DBI）</td>
<td>片上（On-Chip）</td>
<td>SF32LB液晶显示控制器（LCDC）的MIPI显示总线接口（DBI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L129">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P008_sifli_sf32lb-lcdc-mipi-dbi.md#std-dtcompatible-sifli-sf32lb-lcdc-mipi-dbi"><code>sifli,sf32lb-lcdc-mipi-dbi</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="3">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>工作在QSPI NOR模式的思澈（SiFli）SF32LB存储器外设接口（MPI / Memory Peripheral Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L156">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P012_sifli_sf32lb-mpi-qspi-nor.md#std-dtcompatible-sifli-sf32lb-mpi-qspi-nor"><code>sifli,sf32lb-mpi-qspi-nor</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>QSPI总线上的通用NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/coredevices/pr2/pr2.dts?plain=1#L158">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P025_jedec_qspi-nor.md#std-dtcompatible-jedec-qspi-nor"><code>jedec,qspi-nor</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/coredevices/pr2/pr2.dts?plain=1#L166">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB系列电子熔丝（eFuse）一次性可编程（OTP）存储器控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L345">已禁用：1</a>）</td>
<td><a href="../otp_binding_reference/P008_sifli_sf32lb-efuse.md#std-dtcompatible-sifli-sf32lb-efuse"><code>sifli,sf32lb-efuse</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>SF32LB52x引脚复用与配置控制器（HPSYS_PINMUX / Pin Multiplexer and Pin Configuration Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L99">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P023_sifli_sf32lb52x-pinmux.md#std-dtcompatible-sifli-sf32lb52x-pinmux"><code>sifli,sf32lb52x-pinmux</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB常开域（AON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L383">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P005_sifli_sf32lb-aon.md#std-dtcompatible-sifli-sf32lb-aon"><code>sifli,sf32lb-aon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB52x电源管理单元控制器（PMUC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L388">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P006_sifli_sf32lb52x-pmuc.md#std-dtcompatible-sifli-sf32lb52x-pmuc"><code>sifli,sf32lb52x-pmuc</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>SF32LB高级定时器（ATIM）脉宽调制（PWM）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L116">已禁用：1</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P005_sifli_sf32lb-atim-pwm.md#std-dtcompatible-sifli-sf32lb-atim-pwm"><code>sifli,sf32lb-atim-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）PWM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L376">已禁用：1</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P006_sifli_sf32lb-gpt-pwm.md#std-dtcompatible-sifli-sf32lb-gpt-pwm"><code>sifli,sf32lb-gpt-pwm</code></a></td>
</tr>
<tr>
<td rowspan="2">稳压器（Regulator）</td>
<td>板载（On-Board）</td>
<td>Nordic nPM1300电源管理芯片（PMIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/coredevices/pr2/pr2.dts?plain=1#L131">已启用：1</a>）</td>
<td><a href="../hardware/P662_nPM1300稳压器绑定.md#dtbinding-nordic-npm1300-regulator"><code>nordic,npm1300-regulator</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB52x外设低压差稳压器（LDO Regulators）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L392">已启用：1</a>）</td>
<td><a href="../hardware/P656_SF32LB52X低压差稳压器绑定.md#dtbinding-sifli-sf32lb52x-ldo"><code>sifli,sf32lb52x-ldo</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB复位控制器（Reset Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L93">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P016_sifli_sf32lb-rcc-rctl.md#std-dtcompatible-sifli-sf32lb-rcc-rctl"><code>sifli,sf32lb-rcc-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">保持存储器（Retained Memory）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB实时时钟（RTC）支持的保持存储区（Retained Memory Area）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L426">已禁用：1</a>）</td>
<td><a href="../hardware/P628_SF32LB_RTC备份内存绑定.md#dtbinding-sifli-sf32lb-rtc-backup"><code>sifli,sf32lb-rtc-backup</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB真随机数发生器（TRNG / True Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L135">已禁用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P012_sifli_sf32lb-trng.md#std-dtcompatible-sifli-sf32lb-trng"><code>sifli,sf32lb-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L415">已禁用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P008_sifli_sf32lb-rtc.md#std-dtcompatible-sifli-sf32lb-rtc"><code>sifli,sf32lb-rtc</code></a></td>
</tr>
<tr>
<td rowspan="2">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>SF32LB温度传感器（Temperature Sensor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L233">已禁用：1</a>）</td>
<td><a href="../sensor_realtek_rohm_sensirion_binding_reference/P030_sifli_sf32lb-tsen.md#std-dtcompatible-sifli-sf32lb-tsen"><code>sifli,sf32lb-tsen</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NPM1300 PMIC充电器（Charger）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/coredevices/pr2/pr2.dts?plain=1#L111">已启用：1</a>）</td>
<td><a href="../sensor_microchip_nordic_nxp_binding_reference/P018_nordic_npm1300-charger.md#std-dtcompatible-nordic-npm1300-charger"><code>nordic,npm1300-charger</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB通用同步异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L203">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L210">已禁用：2</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P004_sifli_sf32lb-usart.md#std-dtcompatible-sifli-sf32lb-usart"><code>sifli,sf32lb-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>用于SF32LB系列微控制器的思澈（SiFli）SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L250">已禁用：2</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P004_sifli_sf32lb-spi.md#std-dtcompatible-sifli-sf32lb-spi"><code>sifli,sf32lb-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x-ram012.dtsi?plain=1#L15">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）系统配置（HPSYS_CFG / System Configuration）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L354">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P007_sifli_sf32lb-cfg.md#std-dtcompatible-sifli-sf32lb-cfg"><code>sifli,sf32lb-cfg</code></a></td>
</tr>
<tr>
<td rowspan="3">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB高级定时器（ATIM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L109">已禁用：1</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P001_sifli_sf32lb-atim.md#std-dtcompatible-sifli-sf32lb-atim"><code>sifli,sf32lb-atim</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>思澈（SiFli）SF32LB通用定时器（GPT / General Purpose Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L369">已禁用：1</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P002_sifli_sf32lb-gptim.md#std-dtcompatible-sifli-sf32lb-gptim"><code>sifli,sf32lb-gptim</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>此绑定（Binding）描述思澈（SiFli）SF32LB看门狗定时器（WDT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/sifli/sf32lb52x.dtsi?plain=1#L241">已启用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P010_sifli_sf32lb-wdt.md#std-dtcompatible-sifli-sf32lb-wdt"><code>sifli,sf32lb-wdt</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`pr2`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
<tr>
<td>sftool</td>
<td>✅（默认 / default）</td>
<td></td>
</tr>
</table>

<a id="id5"></a>

更多信息见[sftool网站](https://github.com/OpenSiFli/sftool)[注2](#id4)。

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://repebble.com/](https://repebble.com/)

<a id="id4"></a>

〔[2](#id5)〕 [https://github.com/OpenSiFli/sftool](https://github.com/OpenSiFli/sftool)

## 译注

原文将名为DLL的外设描述为数字锁相环；译文保留这段表述，不自行改成其他时钟单元。全部MiP显示、触摸和电源管理硬件信息与Zephyr功能表分别保留。

---

[上一章](P013_Pebble_2_Duo.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P015_Pebble_Time_2.md)
