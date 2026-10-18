---
id: learning.zephyr-docs.boards-st-discovery-eval.page-8
title: SensorTile.box PRO
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/st/sensortile_box_pro/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="sensortile_box_pro"></a>

# 第8章\_SensorTile.box PRO传感器套件

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/st/sensortile_box_pro/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/sensortile_box_pro.jpg](images/sensortile_box_pro.jpg)](images/sensortile_box_pro.jpg)

SensorTile.box PRO传感器套件

名称（Name）：

`sensortile_box_pro`

厂商（Vendor）：

[意法半导体（STMicroelectronics）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=st)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[stm32u585xx](https://docs.zephyrproject.org/latest/boards/index.html#soc=stm32u585xx)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/sensortile_box_pro/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

STEVAL-MKBOXPRO（SensorTile.box PRO）搭载基于Arm Cortex-M33的STM32U585AI MCU，是即用型无线物联网及可穿戴传感平台盒装套件，便于使用和开发基于远程运动及环境数据的应用。

SensorTile.box PRO装在小型塑料盒内，配有长续航充电电池，通过Bluetooth®与普通智能手机通信并提供传感器数据。

<a id="id3"></a>

更多信息见[SensorTile.box PRO网站](https://www.st.com/en/evaluation-tools/steval-mkboxpro.html)[注1](#id2)。

<a id="supported-features"></a>

## 支持的功能（Supported Features）

SensorTile.box PRO通过BLE或USB向智能手机／PC上的主机应用提供运动、环境及音频传感数据，可实现：


- 针对腰带佩戴位置优化的计步器
- 利用云端AI学习进行婴儿哭声检测
- 气压及环境监测
- 车辆／货物追踪
- 振动监测
- 指南针及倾角仪
- 传感器数据记录器（Data Logger）

完整传感器清单见“运动与环境传感器”章节。（[运动与环境传感器（Motion and Environmental Sensors）](#motion-and-environmental-sensors)）

`sensortile_box_pro`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="sensortile_box_pro-hw-features"></a>

<a id="sensortile_box_pro-sensortile_box_pro/stm32u585xx-hw-features-section"></a>

### `sensortile_box_pro/stm32u585xx`目标（Target）

<a id="sensortile_box_pro-sensortile_box_pro/stm32u585xx-hw-features-panel"></a>

<a id="sensortile_box_pro-sensortile_box_pro/stm32u585xx-hw-features-memory"></a>

该开发板目标的片上存储容量：768 KiB RAM、2 MiB Flash。

<a id="sensortile_box_pro-sensortile_box_pro/stm32u585xx-hw-features-table"></a>

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
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L36">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>STM32模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L897">已启用：2</a>）</td>
<td><a href="../hardware/P839_STM32模数转换器绑定.md#dtbinding-st-stm32-adc"><code>st,stm32-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>片上（On-Chip）</td>
<td>STM32多功能数字滤波器（MDF）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u575.dtsi?plain=1#L59">已禁用：1</a>）</td>
<td><a href="../audio_stm32_ti_wolfson_binding_reference/P003_st_stm32-mdf.md#std-dtcompatible-st-stm32-mdf"><code>st,stm32-mdf</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>板载（On-Board）</td>
<td>意法半导体SPI协议V2，兼容BlueNRG-1及后续器件（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L162">已启用：1</a>）</td>
<td><a href="../bluetooth_st_transport_binding_reference/P003_st_hci-spi-v2.md#std-dtcompatible-st-hci-spi-v2"><code>st,hci-spi-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>STM32 FDCAN灵活数据速率CAN控制器（CAN FD Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L952">已禁用：1</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P012_st_stm32-fdcan.md#std-dtcompatible-st-stm32-fdcan"><code>st,stm32-fdcan</code></a></td>
</tr>
<tr>
<td rowspan="7">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>STM32U5复位与时钟控制器（RCC / Reset and Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L230">已启用：1</a>）</td>
<td><a href="../timer_reference/P170_STM32U5复位与时钟控制绑定.md#dtbinding-st-stm32u5-rcc"><code>st,stm32u5-rcc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 外部高速时钟（HSE Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L90">已禁用：1</a>）</td>
<td><a href="../timer_reference/P129_STM32高速外部时钟绑定.md#dtbinding-st-stm32-hse-clock"><code>st,stm32-hse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L103">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L96">已禁用：3</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32U5多速率内部时钟（Multi Speed Internal Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L110">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L117">已禁用：1</a>）</td>
<td><a href="../timer_reference/P160_STM32U5多速内部时钟绑定.md#dtbinding-st-stm32u5-msi-clock"><code>st,stm32u5-msi-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低速外部时钟（LSE Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L124">已启用：1</a>）</td>
<td><a href="../timer_reference/P130_STM32低速外部时钟绑定.md#dtbinding-st-stm32-lse-clock"><code>st,stm32-lse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32U5锁相环（PLL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L146">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L152">已禁用：2</a>）</td>
<td><a href="../timer_reference/P150_STM32U5锁相环时钟绑定.md#dtbinding-st-stm32u5-pll-clock"><code>st,stm32u5-pll-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 微控制器时钟输出（Microcontroller Clock Output，MCO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L166">已禁用：1</a>）</td>
<td><a href="../timer_reference/P134_STM32时钟输出绑定.md#dtbinding-st-stm32-clock-mco"><code>st,stm32-clock-mco</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>STM32 计数器（Counters）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L586">已禁用：11</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P007_st_stm32-counter.md#std-dtcompatible-st-stm32-counter"><code>st,stm32-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>STM32 CRC 计算单元（Calculation Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L1070">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P011_st_stm32-crc.md#std-dtcompatible-st-stm32-crc"><code>st,stm32-crc</code></a></td>
</tr>
<tr>
<td rowspan="2">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>STM32哈希处理器（HASH Processor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L975">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P017_st_stm32-hash.md#std-dtcompatible-st-stm32-hash"><code>st,stm32-hash</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32高级加密标准加速器（AES Accelerator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_crypt.dtsi?plain=1#L9">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P015_st_stm32-aes.md#std-dtcompatible-st-stm32-aes"><code>st,stm32-aes</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>STM32 系列数模转换器（DAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L889">已启用：1</a>）</td>
<td><a href="../hardware/P760_STM32数模转换器绑定.md#dtbinding-st-stm32-dac"><code>st,stm32-dac</code></a></td>
</tr>
<tr>
<td rowspan="2">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>STM32 NeoChrom-GPU2D加速器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L1078">已禁用：1</a>）</td>
<td><a href="../display_st_ultrachip_zephyr_binding_reference/P002_st_neochrom-gpu2d.md#std-dtcompatible-st-neochrom-gpu2d"><code>st,neochrom-gpu2d</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 Chrom-ART 图形加速器（Accelerator，DMA2D）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u575.dtsi?plain=1#L107">已禁用：1</a>）</td>
<td><a href="../display_st_ultrachip_zephyr_binding_reference/P003_st_stm32-dma2d.md#std-dtcompatible-st-stm32-dma2d"><code>st,stm32-dma2d</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>STM32U5直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L963">已启用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P012_st_stm32u5-dma.md#std-dtcompatible-st-stm32u5-dma"><code>st,stm32u5-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 系列闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L174">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P011_st_stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller"><code>st,stm32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用输入输出控制器（GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L271">已启用：9</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P029_st_stm32-gpio.md#std-dtcompatible-st-stm32-gpio"><code>st,stm32-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>串行线／JTAG连接器（Serial Wire–JTAG Connector）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L1089">已启用：1</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P006_swj-connector.md#std-dtcompatible-swj-connector"><code>swj-connector</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>STM32 I2C V2 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L436">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L460">已禁用：2</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P008_st_stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2"><code>st,stm32-i2c-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>STM32 串行音频接口块控制器（SAI Block Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L542">已禁用：2</a>）</td>
<td><a href="../i2s_binding_reference/P017_st_stm32-sai.md#std-dtcompatible-st-stm32-sai"><code>st,stm32-sai</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L48">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32G0 外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L242">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P002_st_stm32g0-exti.md#std-dtcompatible-st-stm32g0-exti"><code>st,stm32g0-exti</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L24">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 灵活存储器控制器（Flexible Memory Controller，FMC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_extra.dtsi?plain=1#L56">已禁用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P013_st_stm32-fmc.md#std-dtcompatible-st-stm32-fmc"><code>st,stm32-fmc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32灵活存储器控制器（FMC / Flexible Memory Controller），用于NOR Flash、PSRAM和SRAM（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_extra.dtsi?plain=1#L62">已禁用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P011_st_stm32-fmc-nor-psram.md#std-dtcompatible-st-stm32-fmc-nor-psram"><code>st,stm32-fmc-nor-psram</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>STM32闪存（Flash Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L183">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P016_st_stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash"><code>st,stm32-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">非易失存储器（NVMEM）</td>
<td>片上（On-Chip）</td>
<td>非易失存储器固定布局（Fixed Layout for Non-Volatile Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L204">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P009_fixed-layout.md#std-dtcompatible-fixed-layout"><code>fixed-layout</code></a></td>
</tr>
<tr>
<td rowspan="1">八线串行外设接口（OCTOSPI）</td>
<td>片上（On-Chip）</td>
<td>STM32八线SPI控制器（OSPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L836">已禁用：2</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P002_st_stm32-ospi.md#std-dtcompatible-st-stm32-ospi"><code>st,stm32-ospi</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>STM32 嵌入式非易失一次性可编程存储器（NVM OTP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L200">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L193">已禁用：1</a>）</td>
<td><a href="../otp_binding_reference/P010_st_stm32-nvm-otp.md#std-dtcompatible-st-stm32-nvm-otp"><code>st,stm32-nvm-otp</code></a></td>
</tr>
<tr>
<td rowspan="1">物理层（PHY）</td>
<td>片上（On-Chip）</td>
<td>用于所有内置于 USB IP 的 USB 收发器（USB Transceivers）的绑定。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_usbotg_fs.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../phy_binding_reference/P008_usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv"><code>usb-nop-xceiv</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>STM32 引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L264">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P004_st_stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl"><code>st,stm32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>STM32U5电源控制器（Power Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L992">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P016_st_stm32u5-pwr.md#std-dtcompatible-st-stm32u5-pwr"><code>st,stm32u5-pwr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32唤醒线控制器（Wake-up Lines Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L1003">已禁用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P009_st_stm32-pwr-wkupctrl.md#std-dtcompatible-st-stm32-pwr-wkupctrl"><code>st,stm32-pwr-wkupctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>STM32 脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L636">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L580">已禁用：7</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P011_st_stm32-pwm.md#std-dtcompatible-st-stm32-pwm"><code>st,stm32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>STM32参考电压缓冲器稳压器（VREFBUF Regulator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L983">已禁用：1</a>）</td>
<td><a href="../hardware/P638_STM32参考电压缓冲器绑定.md#dtbinding-st-stm32-vrefbuf"><code>st,stm32-vrefbuf</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 复位与时钟控制器（Reset and Clock Control，RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L236">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P017_st_stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl"><code>st,stm32-rcc-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>STM32 随机数生成器（Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L862">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P016_st_stm32-rng.md#std-dtcompatible-st-stm32-rng"><code>st,stm32-rng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>STM32 实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L532">已禁用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P014_st_stm32-rtc.md#std-dtcompatible-st-stm32-rtc"><code>st,stm32-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>STM32 SDMMC 主机控制器（Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L879">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_extra.dtsi?plain=1#L46">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P019_st_stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc"><code>st,stm32-sdmmc</code></a></td>
</tr>
<tr>
<td rowspan="9">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>通过SPI访问的意法半导体LSM6DSV16X六轴惯性测量单元（IMU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L189">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P094_st_lsm6dsv16x.md#std-dtcompatible-st-lsm6dsv16x"><code>st,lsm6dsv16x</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通过SPI访问的意法半导体LIS2DU12三轴超低功耗加速度计（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L199">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P081_st_lis2du12.md#std-dtcompatible-st-lis2du12"><code>st,lis2du12</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通过I2C连接的意法半导体LPS22DF压力及温度传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L240">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P086_st_lps22df.md#std-dtcompatible-st-lps22df"><code>st,lps22df</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通过I2C总线访问的意法半导体LIS2MDL磁力计（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L247">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P085_st_lis2mdl.md#std-dtcompatible-st-lis2mdl"><code>st,lis2mdl</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通过I2C连接的意法半导体STTS22H温度传感器。在.dts或.dtsi文件中设置sampling-rate属性时，可包含stts22h.h并使用其中的宏。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/sensortile_box_pro/sensortile_box_pro.dts?plain=1#L254">已启用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P005_st_stts22h-i2c.md#std-dtcompatible-st-stts22h"><code>st,stts22h</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 正交解码器（Quadrature Decoder）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L591">已禁用：6</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P028_st_stm32-qdec.md#std-dtcompatible-st-stm32-qdec"><code>st,stm32-qdec</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系列温度节点（TEMP），用于以两个温度点完成生产校准的传感器。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L1099">已启用：1</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P029_st_stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal"><code>st,stm32-temp-cal</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 参考电压（VREF+）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L1111">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L1120">已禁用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P003_st_stm32-vref.md#std-dtcompatible-st-stm32-vref"><code>st,stm32-vref</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 电池电压（VBAT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L1136">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L1129">已禁用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P001_st_stm32-vbat.md#std-dtcompatible-st-stm32-vbat"><code>st,stm32-vbat</code></a></td>
</tr>
<tr>
<td rowspan="3">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L352">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_extra.dtsi?plain=1#L19">已禁用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P016_st_stm32-usart.md#std-dtcompatible-st-stm32-usart"><code>st,stm32-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L370">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L379">已禁用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P015_st_stm32-uart.md#std-dtcompatible-st-stm32-uart"><code>st,stm32-uart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低功耗通用异步收发器（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L388">已禁用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P014_st_stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart"><code>st,stm32-lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">系统管理总线（SMbus）</td>
<td>片上（On-Chip）</td>
<td>STM32 系统管理总线控制器（SMBus Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L1143">已禁用：4</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P013_st_stm32-smbus.md#std-dtcompatible-st-stm32-smbus"><code>st,stm32-smbus</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>STM32H7 串行外设接口控制器（SPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L397">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L423">已禁用：1</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P013_st_stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi"><code>st,stm32h7-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">USB Type-C 端口控制器（USB Type-C Port Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 USB Type-C／电力传输（Power Delivery）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_extra.dtsi?plain=1#L83">已禁用：1</a>）</td>
<td><a href="../usbc_tcpc_binding_reference/P005_st_stm32-ucpd.md#std-dtcompatible-st-stm32-ucpd"><code>st,stm32-ucpd</code></a></td>
</tr>
<tr>
<td rowspan="3">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32U5低功耗定时器（LPTIM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L484">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L496">已禁用：3</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P009_st_stm32u5-lptim.md#std-dtcompatible-st-stm32u5-lptim"><code>st,stm32u5-lptim</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 定时器（Timers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L626">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L570">已禁用：9</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P008_st_stm32-timers.md#std-dtcompatible-st-stm32-timers"><code>st,stm32-timers</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>STM32 全速 USB OTG 控制器（OTGFS Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_usbotg_fs.dtsi?plain=1#L12">已启用：1</a>）</td>
<td><a href="../usb_stm32_audio_binding_reference/P004_st_stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs"><code>st,stm32-otgfs</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>STM32 看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L328">已启用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P001_st_stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog"><code>st,stm32-watchdog</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系统窗口看门狗（System Window Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L335">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P002_st_stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog"><code>st,stm32-window-watchdog</code></a></td>
</tr>
</table>

<a id="hardware"></a>

## 硬件（Hardware）

<a id="id5"></a>

<a id="id7"></a>

以下概述开发板主要功能，更多信息见[UM3133](https://www.st.com/resource/en/user_manual/um3133-getting-started-with-sensortilebox-pro-multisensors-and-wireless-connectivity-development-kit-for-any-intelligent-iot-node-stmicroelectronics.pdf)[注2](#id4)及原理图[注3](#id6)。（[原理图（Schematic）](https://www.st.com/resource/en/schematic_pack/steval-mkboxpro-schematic.pdf)）

STM32U585xx属于STM32U5超低功耗微控制器系列，基于Arm® Cortex®-M33 32位RISC内核，最高工作频率160 MHz。


- 支持FlexPowerControl的超低功耗设计：待机电流最低300 nA，运行模式19.5 µA/MHz
- 内核：Arm® 32位Cortex®-M33 CPU，支持TrustZone®及FPU
- 性能基准（Performance Benchmark）：


  - 原文性能指标为1.5 DMPIS/MHz（Drystone 2.1），拼写照录
  - 651 CoreMark®，4.07 CoreMark®/MHz
- 安全与密码功能（Security and Cryptography）


  - Arm® TrustZone®，I/O、存储器及外设可配置安全属性
  - 灵活的生命周期方案，支持读出保护（RDP）及密码保护调试
  - 通过唯一启动入口与安全隐藏保护区域（Hide Protection，HDP）建立信任根
  - 通过内置根安全服务（Root Secure Services）进行安全固件安装
  - 利用硬件唯一密钥（Hardware Unique Key，HUK）进行安全数据存储
  - 支持使用TF-M进行安全固件更新
  - 2个AES协处理器，其中1个抵抗DPA
  - 抵抗DPA的公钥加速器（Public Key Accelerator）
  - Octo-SPI外部存储器即时解密（On-the-fly Decryption）
  - 哈希（HASH）硬件加速器
  - 主动防篡改（Active Tampers）
  - 符合NIST SP800-90B的真随机数发生器
  - 96位唯一标识（Unique ID）
  - 用于用户数据的512字节一次性可编程存储器（OTP）
  - 主动防篡改（Active Tampers）
- 时钟管理（Clock Management）：


  - 4～50 MHz晶体振荡器
  - 用于实时时钟（RTC）的32 kHz低速外部晶体振荡器（LSE）
  - 内部16 MHz RC振荡器，出厂校准（Factory-Trimmed），精度±1%
  - 内部低功耗32 kHz RC振荡器，精度±5%
  - 2个内部多速率振荡器，范围100 kHz～48 MHz；其中1个可由LSE自动微调，精度优于±0.25%
  - 三个锁相环（PLL），用于系统时钟、USB、音频和ADC
  - 内部48 MHz时钟，带时钟恢复（Clock Recovery）
- 电源管理（Power Management）


  - 嵌入式低压差稳压器（LDO）
  - 内置SMPS降压转换器，支持运行中切换与电压调节
- RTC，带硬件日历及校准
- 最多136个高速I/O，多数耐受5 V；最多14个I/O具有独立供电，最低1.08 V
- 最多24个电容感应通道，支持触摸键、线性及旋转触摸传感器
- 最多17个定时器及2个看门狗


  - 两个16位高级电机控制定时器（Advanced Motor-Control）
  - 2个32位及5个16位通用定时器
  - 4个16位低功耗定时器，可在停止模式工作
  - 两个看门狗（Watchdogs）
  - 2个系统节拍（SysTick）定时器
- 自适应实时加速器（ART Accelerator）


  - 8 Kbyte指令缓存，支持从Flash及外部存储器零等待执行；最高160 MHz，带MPU，性能240 DMIPS，支持DSP
  - 外部存储器使用4 Kbyte数据缓存（Data Cache）
- 存储器（Memories）


  - 2 Mbytes Flash，支持ECC、双存储区读写并行，其中512 Kbytes耐久度100 kcycles
  - 关闭ECC时786 Kbyte SRAM；开启ECC时722 Kbyte SRAM，其中最多322 Kbyte支持ECC
  - 外部存储器接口，支持SRAM、PSRAM、NOR、NAND及FRAM
  - 2路Octo-SPI存储器接口
- 丰富的模拟外设（Analog Peripherals），采用独立供电


  - 14位ADC，2.5 Msps，通过硬件过采样分辨率可达16位
  - 12位ADC，2.5 Msps，支持硬件过采样，可在Stop 2模式自主运行
  - 12位DAC，支持低功耗采样保持
  - 2个运算放大器，内置PGA
  - 2个超低功耗比较器
- 最多22个通信接口


  - USB Type-C／USB电力传输控制器
  - USB OTG 2.0全速控制器
  - 两个串行音频接口（SAI）
  - 4路I2C FM+（1 Mbit/s），支持SMBus/PMBus
  - 六路USART，支持ISO 7816、LIN、IrDA和调制解调器（Modem）
  - 3路SPI，将双OCTOSPI配置为SPI模式后合计5路
  - 一路灵活数据速率CAN（FDCAN）
  - 2路SDMMC接口
  - 16通道及4通道DMA控制器，可在停止模式工作
  - 1个多功能数字滤波器（含6个滤波器），以及1个带声音活动检测的音频数字滤波器
- 循环冗余校验计算单元（CRC Calculation Unit）
- 开发支持：串行线调试（SWD）、JTAG及嵌入式跟踪宏单元（Embedded Trace Macrocell™）
- 真随机数发生器（RNG / True Random Number Generator）
- 图形功能（Graphic Features）


  - Chrom-ART Accelerator（DMA2D）加速图形内容生成
  - 1路数字摄像头接口
- 数学协处理器（Mathematical Co-processor）

> - 坐标旋转数字计算（CORDIC），加速三角函数
> - 滤波数学加速器（Filter Mathematical Accelerator，FMAC）

STM32U585AI的更多信息见：


- <a id="id9"></a>

  [STM32U585在ST官网的产品页](https://www.st.com/en/microcontrollers-microprocessors/stm32u575-585.html)[注4](#id8)
- <a id="id11"></a>

  [STM32U585参考手册（Reference Manual）](https://www.st.com/resource/en/reference_manual/rm0456-stm32u575585-armbased-32bit-mcus-stmicroelectronics.pdf) [注5](#id10)

<a id="motion-and-environmental-sensors"></a>

### 运动与环境传感器（Motion and Environmental Sensors）

> - <a id="id13"></a>
>
>   LSM6DSV16X六轴IMU，见[lsm6dsv16x数据手册](https://www.st.com/en/mems-and-sensors/lsm6dsv16x.html)[注6](#id12)
> - <a id="id15"></a>
>
>   LIS2MDL三轴磁力计，见[lis2mdl数据手册](https://www.st.com/en/mems-and-sensors/lis2mdl.html)[注7](#id14)
> - <a id="id17"></a>
>
>   LPS22DF高度计／压力传感器，见[lps22df数据手册](https://www.st.com/en/mems-and-sensors/lps22df.html)[注8](#id16)
> - <a id="id19"></a>
>
>   LIS2DU12三轴加速度计，见[lis2du12数据手册](https://www.st.com/en/mems-and-sensors/lis2du12.html)[注9](#id18)
> - <a id="id21"></a>
>
>   STTS22H数字温度传感器，见原文链接名称[stts22hh数据手册](https://www.st.com/en/mems-and-sensors/stts22h.html)[注10](#id20)
> - <a id="id23"></a>
>
>   MP23db01HP麦克风／音频传感器，见[mp23db01hp数据手册](https://www.st.com/en/mems-and-sensors/mp23db01hp.html)[注11](#id22)

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）


- 4个用户LED


  - led0：绿色
  - led1：红色，与BLE共用
  - led2：黄色
  - led3：蓝色
- 4个按键／开关


  - BT1用户按键，可供用户应用使用
  - BT2／BOOT0用户按键，可供应用使用；硬件复位后保持按下可让SensorTile.box PRO进入DFU模式，参见rst按键及编程调试章节（[烧录与调试（Programming and Debugging）](#programming-and-debugging)）
  - rst复位按键，外壳上没有对应操作口
  - 电源开关，用于开关开发板电源

<a id="system-clock"></a>

### 系统时钟（System Clock）

SensorTile.box PRO系统时钟可来自内部振荡器、外部振荡器或主PLL。默认由16 MHz外部振荡器驱动PLL产生80 MHz，可提高至120 MHz。内部AHB、APB1及APB2 AMBA总线均运行于80 MHz。

<a id="serial-port"></a>

### 串口（Serial Port）

SensorTile.box PRO有4路U(S)ART，UART4连接到JTAG/SWD接口，可用于控制台。

<a id="usb-interface"></a>

### USB接口

SensorTile.box PRO可通过USB-C接口作为USB设备连接PC主机。应用可将其声明为标准或厂商设备类，例如CDC、大容量存储类，或兼具两者的复合设备。

<a id="bluenrg-lp-chip"></a>

### BlueNRG-LP芯片

<a id="id25"></a>

<a id="id27"></a>

<a id="id29"></a>

本板配有意法半导体[BlueNRG-LP](https://www.st.com/en/wireless-connectivity/bluenrg-lp.html)芯片[注12](#id24)。在SensorTile.box PRO运行Zephyr蓝牙示例前，须将BlueNRG升级为兼容Zephyr BLE协议栈的固件，可使用[SensorTile.box PRO BLE固件升级包](https://github.com/STMicroelectronics/stsw-mkbox-bleco/blob/master/ble_fw_upg_app/README.rst)[注13](#id26)中的应用完成。系列BLE二进制固件信息见[stsw-mkbox-bleco](https://www.st.com/en/embedded-software/stsw-mkbox-bleco.html)[注14](#id28)。

<a id="console"></a>

### 控制台（Console）

Zephyr控制台输出有两种选择：


- 使用适用于各板卡的通用CDC ACM UART后端配置
- 使用SWD连接器JP2上的UART4，可通过JTAG适配器连接SensorTile.box PRO，同时使用SWD及控制台线路。

  在UART上启用控制台及Shell：


  - 在prj.conf中设置CONFIG_BOARD_SERIAL_BACKEND_CDC_ACM=n，覆盖开发板默认配置。
  - 添加名为<board>.overlay的覆盖文件：

```text
/ {
    chosen {
       zephyr,console = &uart4;
       zephyr,shell-uart = &uart4;
     };
  };
```

控制台默认参数为115200、8N1。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`sensortile_box_pro`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
<tr>
<td>dfu-util</td>
<td>✅（默认 / default）</td>
<td></td>
</tr>
</table>

ST SensorTile.box PRO有两种烧录方法：


1. 使用DFU软件工具

  <a id="id31"></a>

  按住BOOT0上电或复位，可进入STM32U585 ROM启动加载器的DFU模式，只需USB-C线，无需其他硬件。“烧录与调试主机工具（[Flash & Debug Host Tools](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#flash-debug-host-tools)）”完整支持该方法。更多信息见[AN2606](http://www.st.com/content/ccc/resource/technical/document/application_note/b9/9b/16/3a/12/1e/40/0c/CD00167594.pdf/files/CD00167594.pdf/jcr:content/translations/en.CD00167594.pdf)[注15](#id30)的STM32U585xx章节。
2. 使用SWD硬件工具

  此方法需要将额外调试硬件，例如ST-LINK/V3，连接到板卡SWD接口。

<a id="dfu-flashing"></a>

### DFU烧录（DFU Flashing）

<a id="install-dfu-util"></a>

#### 安装dfu-util

<a id="id33"></a>

原文建议dfu-util至少为v0.9。Debian及Ubuntu的软件包可能较旧，必要时可从源码构建；源码获取及构建步骤见[DFU-UTIL网站](http://dfu-util.sourceforge.net/)[注16](#id32)。

<a id="flash-an-application-to-sensortile-box-pro"></a>

#### 向SensorTile.box PRO烧录应用

按住BOOT0，将USB-C线连接SensorTile.box PRO的USB OTG接口及电脑，使开发板进入DFU模式。

确认开发板确实处于DFU模式：

```text
$ sudo dfu-util -l
dfu-util 0.9

Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
Copyright 2010-2019 Tormod Volden and Stefan Schmidt
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

Found DFU: [0483:df11] ver=2200, devnum=74, cfg=1, intf=0, path="2-2", alt=2, name="@OTP Memory /0x1FFF7000/01*0001Ke", serial="204A325D574D"
Found DFU: [0483:df11] ver=2200, devnum=74, cfg=1, intf=0, path="2-2", alt=1, name="@Option Bytes  /0x1FF00000/01*040 e/0x1FF01000/01*040 e", serial="204A325D574D"
Found DFU: [0483:df11] ver=2200, devnum=74, cfg=1, intf=0, path="2-2", alt=0, name="@Internal Flash  /0x08000000/512*0004Kg", serial="204A325D574D"
```

Linux 主机上应显示以下确认信息：

```text
$ dmesg
usb 2-2: new full-speed USB device number 74 using xhci_hcd
usb 2-2: New USB device found, idVendor=0483, idProduct=df11
usb 2-2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 2-2: Product: STM32  BOOTLOADER
usb 2-2: Manufacturer: STMicroelectronics
usb 2-2: SerialNumber: 204A325D574D
```

可构建并烧录[SensorTile.box Pro sensors](../board_samples/P014_SensorTile.box_Pro传感器示例.md#sensortile_box_pro_sensors)示例，读取传感器数据并在控制台输出。

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.st.com/en/evaluation-tools/steval-mkboxpro.html](https://www.st.com/en/evaluation-tools/steval-mkboxpro.html)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.st.com/resource/en/user_manual/um3133-getting-started-with-sensortilebox-pro-multisensors-and-wireless-connectivity-development-kit-for-any-intelligent-iot-node-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um3133-getting-started-with-sensortilebox-pro-multisensors-and-wireless-connectivity-development-kit-for-any-intelligent-iot-node-stmicroelectronics.pdf)

<a id="id6"></a>

〔[3](#id7)〕 [https://www.st.com/resource/en/schematic_pack/steval-mkboxpro-schematic.pdf](https://www.st.com/resource/en/schematic_pack/steval-mkboxpro-schematic.pdf)

<a id="id8"></a>

〔[4](#id9)〕 [https://www.st.com/en/microcontrollers-microprocessors/stm32u575-585.html](https://www.st.com/en/microcontrollers-microprocessors/stm32u575-585.html)

<a id="id10"></a>

〔[5](#id11)〕 [https://www.st.com/resource/en/reference_manual/rm0456-stm32u575585-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0456-stm32u575585-armbased-32bit-mcus-stmicroelectronics.pdf)

<a id="id12"></a>

〔[6](#id13)〕 [https://www.st.com/en/mems-and-sensors/lsm6dsv16x.html](https://www.st.com/en/mems-and-sensors/lsm6dsv16x.html)

<a id="id14"></a>

〔[7](#id15)〕 [https://www.st.com/en/mems-and-sensors/lis2mdl.html](https://www.st.com/en/mems-and-sensors/lis2mdl.html)

<a id="id16"></a>

〔[8](#id17)〕 [https://www.st.com/en/mems-and-sensors/lps22df.html](https://www.st.com/en/mems-and-sensors/lps22df.html)

<a id="id18"></a>

〔[9](#id19)〕 [https://www.st.com/en/mems-and-sensors/lis2du12.html](https://www.st.com/en/mems-and-sensors/lis2du12.html)

<a id="id20"></a>

〔[10](#id21)〕 [https://www.st.com/en/mems-and-sensors/stts22h.html](https://www.st.com/en/mems-and-sensors/stts22h.html)

<a id="id22"></a>

〔[11](#id23)〕 [https://www.st.com/en/mems-and-sensors/mp23db01hp.html](https://www.st.com/en/mems-and-sensors/mp23db01hp.html)

<a id="id24"></a>

〔[12](#id25)〕 [https://www.st.com/en/wireless-connectivity/bluenrg-lp.html](https://www.st.com/en/wireless-connectivity/bluenrg-lp.html)

<a id="id26"></a>

〔[13](#id27)〕 [https://github.com/STMicroelectronics/stsw-mkbox-bleco/blob/master/ble_fw_upg_app/README.rst](https://github.com/STMicroelectronics/stsw-mkbox-bleco/blob/master/ble_fw_upg_app/README.rst)

<a id="id28"></a>

〔[14](#id29)〕 [https://www.st.com/en/embedded-software/stsw-mkbox-bleco.html](https://www.st.com/en/embedded-software/stsw-mkbox-bleco.html)

<a id="id30"></a>

〔[15](#id31)〕 [http://www.st.com/content/ccc/resource/technical/document/application_note/b9/9b/16/3a/12/1e/40/0c/CD00167594.pdf/files/CD00167594.pdf/jcr:content/translations/en.CD00167594.pdf](http://www.st.com/content/ccc/resource/technical/document/application_note/b9/9b/16/3a/12/1e/40/0c/CD00167594.pdf/files/CD00167594.pdf/jcr:content/translations/en.CD00167594.pdf)

<a id="id32"></a>

〔[16](#id33)〕 [http://dfu-util.sourceforge.net/](http://dfu-util.sourceforge.net/)

## 译注

U585型号的DFU工具最低0.9，BlueNRG-LP还需兼容固件；UART4的JP2连接及其他串口排针分别保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [](http://dfu-util.sourceforge.net/)：HTTP Error 403: Forbidden。
- [en.CD00167594.pdf](http://www.st.com/content/ccc/resource/technical/document/application_note/b9/9b/16/3a/12/1e/40/0c/CD00167594.pdf/files/CD00167594.pdf/jcr:content/translations/en.CD00167594.pdf)：HTTP Error 567: Unknown Status。
- [stsw-mkbox-bleco.html](https://www.st.com/en/embedded-software/stsw-mkbox-bleco.html)：HTTP Error 567: Unknown Status。
- [steval-mkboxpro.html](https://www.st.com/en/evaluation-tools/steval-mkboxpro.html)：HTTP Error 567: Unknown Status。
- [lis2du12.html](https://www.st.com/en/mems-and-sensors/lis2du12.html)：HTTP Error 567: Unknown Status。
- [lis2mdl.html](https://www.st.com/en/mems-and-sensors/lis2mdl.html)：HTTP Error 567: Unknown Status。
- [lps22df.html](https://www.st.com/en/mems-and-sensors/lps22df.html)：HTTP Error 567: Unknown Status。
- [lsm6dsv16x.html](https://www.st.com/en/mems-and-sensors/lsm6dsv16x.html)：HTTP Error 567: Unknown Status。
- [mp23db01hp.html](https://www.st.com/en/mems-and-sensors/mp23db01hp.html)：HTTP Error 567: Unknown Status。
- [stts22h.html](https://www.st.com/en/mems-and-sensors/stts22h.html)：HTTP Error 567: Unknown Status。
- [stm32u575-585.html](https://www.st.com/en/microcontrollers-microprocessors/stm32u575-585.html)：HTTP Error 567: Unknown Status。
- [bluenrg-lp.html](https://www.st.com/en/wireless-connectivity/bluenrg-lp.html)：HTTP Error 567: Unknown Status。
- [rm0456-stm32u575585-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0456-stm32u575585-armbased-32bit-mcus-stmicroelectronics.pdf)：HTTP Error 567: Unknown Status。
- [steval-mkboxpro-schematic.pdf](https://www.st.com/resource/en/schematic_pack/steval-mkboxpro-schematic.pdf)：HTTP Error 567: Unknown Status。
- [um3133-getting-started-with-sensortilebox-pro-multisensors-and-wireless-connectivity-development-kit-for-any-intelligent-iot-node-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um3133-getting-started-with-sensortilebox-pro-multisensors-and-wireless-connectivity-development-kit-for-any-intelligent-iot-node-stmicroelectronics.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P007_SensorTile.box.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_ST25DV_Discovery_MB1283_version.md)
