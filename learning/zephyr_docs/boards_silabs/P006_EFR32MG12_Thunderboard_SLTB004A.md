---
id: learning.zephyr-docs.boards-silabs.page-6
title: EFR32MG12 Thunderboard SLTB004A
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/silabs/dev_kits/sltb004a/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="sltb004a"></a>

# 第6章\_EFR32MG12 Thunderboard，SLTB004A

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/silabs/dev_kits/sltb004a/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../../_images/sltb004a.jpg](images/sltb004a.jpg)](images/sltb004a.jpg)

EFR32MG12 Thunderboard，SLTB004A

名称（Name）：

`sltb004a`

厂商（Vendor）：

[芯科科技（Silicon Laboratories）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=silabs)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[efr32mg12p332f1024gl125](https://docs.zephyrproject.org/latest/boards/index.html#soc=efr32mg12p332f1024gl125)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/dev_kits/sltb004a/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

EFR32MG12 Thunderboard，也称Thunderboard Sense 2，搭载基于Arm Cortex-M4F的EFR32MG12系列MCU，具有低功耗能力。

<a id="hardware"></a>

## 硬件（Hardware）


- EFR32MG12 Mighty Gecko无线SoC，工作频率38.4 MHz
- Arm Cortex-M4内核，256 kB RAM及1024 kB闪存
- 旺宏（Macronix）超低功耗8 Mbit SPI闪存，MX25R8035F
- 用于无线传输的2.4 GHz陶瓷天线
- Silicon Labs Si7021相对湿度及温度传感器
- Silicon Labs Si1133紫外线指数及环境光传感器
- Silicon Labs Si7210霍尔效应传感器
- Bosch Sensortec BMP280气压传感器
- ams CCS811室内空气质量气体传感器
- TDK InvenSense ICM-20648六轴惯性传感器
- TDK InvenSense ICS-43434微机电系统（MEMS）麦克风
- 四个Broadcom高亮度RGB LED，ASMT-YTB7-0AA02
- 一个双色LED及两个按键
- 电源使能信号，支持精细功耗控制
- 板载SEGGER J-Link便于编程及调试，包含USB虚拟COM端口
- Mini Simplicity连接器，用于能耗分析及高级无线网络调试
- 引出焊盘，用于访问GPIO及连接外部硬件
- 复位按键（Reset Button）
- USB与电池供电自动切换
- CR2032纽扣电池座及外部电池连接器

EFR32MG12 SoC及Thunderboard Sense 2更多信息见：


- [EFR32MG12数据手册](https://www.silabs.com/documents/public/data-sheets/efr32mg12-datasheet.pdf)
- [EFR32MG12参考手册](https://www.silabs.com/documents/public/reference-manuals/efr32xg12-rm.pdf)
- [SLTB004A用户指南](https://www.silabs.com/documents/public/user-guides/ug309-sltb004a-user-guide.pdf)
- [SLTB004A原理图](https://www.silabs.com/documents/public/schematic-files/BRD4166A-D00-schematic.pdf)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`sltb004a`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="sltb004a-hw-features"></a>

<a id="sltb004a-sltb004a/efr32mg12p332f1024gl125-hw-features-section"></a>

#### `sltb004a/efr32mg12p332f1024gl125`目标（Target）

<a id="sltb004a-sltb004a/efr32mg12p332f1024gl125-hw-features-panel"></a>

<a id="sltb004a-sltb004a/efr32mg12p332f1024gl125-hw-features-memory"></a>

此开发板目标可用存储器：256 KiB RAM、1 MiB 闪存。

<a id="sltb004a-sltb004a/efr32mg12p332f1024gl125-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L24">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Gecko Series 1模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L117">已禁用：1</a>）</td>
<td><a href="../hardware/P899_SiliconLabsGecko模数转换器绑定.md#dtbinding-silabs-gecko-adc"><code>silabs,gecko-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2蓝牙主机控制器接口（Bluetooth HCI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/efr32xg12.dtsi?plain=1#L10">已禁用：1</a>）</td>
<td><a href="../bluetooth_vendor_hci_binding_reference/P015_silabs_bt-hci-efr32.md#std-dtcompatible-silabs-bt-hci-efr32"><code>silabs,bt-hci-efr32</code></a></td>
</tr>
<tr>
<td rowspan="6">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Silabs Gecko时钟管理单元（Clock Management Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L90">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P030_silabs_series0-cmu.md#std-dtcompatible-silabs-series0-cmu"><code>silabs,series0-cmu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0低频晶体振荡器（LFXO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L35">已启用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P003_silabs_series0-lfxo.md#std-dtcompatible-silabs-series0-lfxo"><code>silabs,series0-lfxo</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0低频RC振荡器（LFRCO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L42">已禁用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P002_silabs_series0-lfrco.md#std-dtcompatible-silabs-series0-lfrco"><code>silabs,series0-lfrco</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0高频晶体振荡器（HFXO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L49">已启用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P001_silabs_series0-hfxo.md#std-dtcompatible-silabs-series0-hfxo"><code>silabs,series0-hfxo</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L55">已禁用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L68">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L61">已禁用：1</a>）</td>
<td><a href="../timer_reference/P110_固定比例时钟绑定.md#dtbinding-fixed-factor-clock"><code>fixed-factor-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Gecko闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L99">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P006_silabs_gecko-flash-controller.md#std-dtcompatible-silabs-gecko-flash-controller"><code>silabs,gecko-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0—2 GPIO外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L199">已启用：1</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P013_silabs_gecko-gpio.md#std-dtcompatible-silabs-gecko-gpio"><code>silabs,gecko-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0—2 GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L209">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L218">已禁用：4</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P012_silabs_gecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port"><code>silabs,gecko-gpio-port</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0—2 I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L170">已启用：2</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P004_silabs_gecko-i2c.md#std-dtcompatible-silabs-gecko-i2c"><code>silabs,gecko-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb004a/sltb004a.dts?plain=1#L49">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb004a/sltb004a.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb004a/sltb004a.dts?plain=1#L67">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L108">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>这些属性用于支持Zephyr的<code>spi-nor</code>闪存驱动通过Zephyr SPI API，使用基于M25P80的标准命令集控制串行闪存（Serial Flash Memory）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb004a/sltb004a.dts?plain=1#L126">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor"><code>jedec,spi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Silabs Gecko引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L318">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P025_silabs_gecko-pinctrl.md#std-dtcompatible-silabs-gecko-pinctrl"><code>silabs,gecko-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Gecko PWM端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L303">已启用：1</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P007_silabs_gecko-pwm.md#std-dtcompatible-silabs-gecko-pwm"><code>silabs,gecko-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>GECKO真随机数发生器（TRNG / True Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L310">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P013_silabs_gecko-trng.md#std-dtcompatible-silabs-gecko-trng"><code>silabs,gecko-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Gecko实时计数器（Real-Time Counter，RTCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L190">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P009_silabs_gecko-rtcc.md#std-dtcompatible-silabs-gecko-rtcc"><code>silabs,gecko-rtcc</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>CCS811数字空气质量传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb004a/sltb004a.dts?plain=1#L178">已启用：1</a>）</td>
<td><a href="../sensor_ams_aosong_bosch_binding_reference/P001_ams_ccs811.md#std-dtcompatible-ams-ccs811"><code>ams,ccs811</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Gecko通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L126">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L135">已禁用：2</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P008_silabs_gecko-usart.md#std-dtcompatible-silabs-gecko-usart"><code>silabs,gecko-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Gecko低能耗UART（LEUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L162">已启用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P006_silabs_gecko-leuart.md#std-dtcompatible-silabs-gecko-leuart"><code>silabs,gecko-leuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L144">已启用：1</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P007_silabs_usart-spi.md#std-dtcompatible-silabs-usart-spi"><code>silabs,usart-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0–2看门狗（WDOG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L282">已启用：2</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P011_silabs_gecko-wdog.md#std-dtcompatible-silabs-gecko-wdog"><code>silabs,gecko-wdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

EFR32MG12 SoC具有八个GPIO控制器：PORTA、PORTB、PORTC、PORTD、PORTF、PORTI、PORTJ及PORTK。

下表Name列为引脚名称，例如PE2表示PORTE第2脚，#27表示位置位域（Location Bitfield），与板卡及微控制器的数据手册、用户手册一致。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PD8</td>
<td>通用输入输出（GPIO）</td>
<td>LED0，红色</td>
</tr>
<tr>
<td>PD9</td>
<td>通用输入输出（GPIO）</td>
<td>LED1，绿色</td>
</tr>
<tr>
<td>PD14</td>
<td>通用输入输出（GPIO）</td>
<td>SW0按键PB0</td>
</tr>
<tr>
<td>PD15</td>
<td>通用输入输出（GPIO）</td>
<td>按键PB1</td>
</tr>
<tr>
<td>PA0</td>
<td>UART_TX</td>
<td>UART发送控制台：VCOM_TX，US0_TX，#0</td>
</tr>
<tr>
<td>PA1</td>
<td>UART_RX</td>
<td>UART接收控制台：VCOM_RX，US0_RX，#0</td>
</tr>
<tr>
<td>PF3</td>
<td>UART_TX</td>
<td>EXP12_UART_TX，LEU0_TX，#27</td>
</tr>
<tr>
<td>PF4</td>
<td>UART_RX</td>
<td>EXP14_UART_RX，LEU0_RX，#27</td>
</tr>
<tr>
<td>PC10</td>
<td>I2C_SDA</td>
<td>EXP16_I2C_SDA，I2C0_SDA，#15</td>
</tr>
<tr>
<td>PC11</td>
<td>I2C_SCL</td>
<td>EXP15_I2C_SCL，I2C0_SCL，#15</td>
</tr>
<tr>
<td>PB6</td>
<td>I2C_SDA</td>
<td>CCS811_I2C_SDA，I2C1_SDA，#6</td>
</tr>
<tr>
<td>PB7</td>
<td>I2C_SCL</td>
<td>CCS811_I2C_SCL，I2C1_SCL，#6</td>
</tr>
<tr>
<td>PK0</td>
<td>SPI_MOSI</td>
<td>闪存MOSI：US2_TX，#29</td>
</tr>
<tr>
<td>PK2</td>
<td>SPI_MISO</td>
<td>闪存MISO：US2_RX，#30</td>
</tr>
<tr>
<td>PF7</td>
<td>SPI_SCLK</td>
<td>闪存串行时钟SCLK：US2_CLK，#18</td>
</tr>
<tr>
<td>PK1</td>
<td>SPI_CS</td>
<td>闪存片选（Chip Select），GPIO</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

EFR32MG12 SoC配置为使用板载38.4 MHz外部振荡器。

<a id="serial-port"></a>

### 串口（Serial Port）

EFR32MG12 SoC具有四个USART及一个低能耗UART（Low Energy UART，LEUART），原文列LEUART最大波特率9600。USART0配置为Zephyr控制台，连接到板载J-Link；J-Link将该接口呈现为虚拟COM端口，用于通用应用串行数据传输。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`sltb004a`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

注意（Note）

原文要求首次使用套件前，在Simplicity Studio更新J-Link固件。

<a id="flashing"></a>

### 烧录（Flashing）

SLTB004A内置[J-Link](https://www.segger.com/jlink-debug-probes.html)串口及调试适配器，提供：


- 与主机的USB连接，同时呈现大容量存储（Mass Storage）及USB串口。
- 串行闪存设备（Serial Flash Device），实现USB闪存盘文件存储
- 通过接口USB串口转接的物理UART连接

<a id="flashing-an-application-to-sltb004a"></a>

#### 向SLTB004A烧录应用

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例，构建Zephyr内核及应用：

```text
# From the root of the zephyr repository
west build -b sltb004a samples/hello_world
```

通过USB将SLTB004A连接主机，应能看到大容量存储设备TB004及USB串口。将生成的zephyr.bin复制到SLTB004A驱动器。

打开串口终端（如minicom或PuTTY），设置如下：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

复位开发板后，应能在相应串口（Serial Port）看到以下消息：

```text
Hello World! sltb004a
```

## 译注

Thunderboard Sense 2使用38.4 MHz晶体和USART0控制台；原文LEUART最高9600波特的说明单独保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [efr32mg12-datasheet.pdf](https://www.silabs.com/documents/public/data-sheets/efr32mg12-datasheet.pdf)：HTTP Error 403: Forbidden。
- [efr32xg12-rm.pdf](https://www.silabs.com/documents/public/reference-manuals/efr32xg12-rm.pdf)：HTTP Error 403: Forbidden。
- [BRD4166A-D00-schematic.pdf](https://www.silabs.com/documents/public/schematic-files/BRD4166A-D00-schematic.pdf)：HTTP Error 403: Forbidden。
- [ug309-sltb004a-user-guide.pdf](https://www.silabs.com/documents/public/user-guides/ug309-sltb004a-user-guide.pdf)：HTTP Error 403: Forbidden。

---

[上一章](P005_SiWx917_Wi-Fi_6_and_Bluetooth_LE_SoC_Dev_Kit_BRD2605A.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_EFM32GG12_Thunderboard_SLTB009A.md)
