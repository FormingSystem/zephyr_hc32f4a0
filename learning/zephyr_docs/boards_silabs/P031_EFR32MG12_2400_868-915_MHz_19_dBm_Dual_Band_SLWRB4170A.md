---
id: learning.zephyr-docs.boards-silabs.page-31
title: EFR32MG12 2400 868-915 MHz 19 dBm Dual Band SLWRB4170A
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/silabs/radio_boards/slwrb4170a/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="slwrb4170a"></a>

# 第31章\_EFR32MG12 2400/868-915 MHz 19 dBm双频无线电板，SLWRB4170A

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/silabs/radio_boards/slwrb4170a/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../../_images/efr32mg12-slwrb4170a.jpg](images/efr32mg12-slwrb4170a.jpg)](images/efr32mg12-slwrb4170a.jpg)

EFR32MG12 2400/868-915 MHz 19 dBm双频无线电板，SLWRB4170A

名称（Name）：

`slwrb4170a`

厂商（Vendor）：

[芯科科技（Silicon Laboratories）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=silabs)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[efr32mg12p433f1024gm68](https://docs.zephyrproject.org/latest/boards/index.html#soc=efr32mg12p433f1024gm68)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/slwrb4170a/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

EFR32MG12 Mighty Gecko无线电板搭载基于Arm Cortex-M4F的EFR32MG12系列无线SoC，具有优良低功耗能力。

BRD4170A，也称SLWRB4170A，插接无线入门套件主板BRD4001A，作为一种无线电板获得支持。（[无线电板（Radio Boards）](P023_Radio_Boards.md#silabs-radio-boards)）

<a id="hardware"></a>

## 硬件（Hardware）


- EFR32MG12P433F1024GM68 Mighty Gecko片上系统（SoC）
- CPU内核：带浮点单元（FPU）的ARM Cortex-M4
- 闪存容量：1024 kB
- 随机存取存储器（RAM）：256 kB
- 发射功率：最高+19 dBm
- 工作频率：2.4 GHz及Sub-GHz
- 低频外部振荡器（LFXO）晶体32.768 kHz，高频外部振荡器（HFXO）晶体38.4 MHz。

EFR32MG12 SoC及BRD4170A更多信息见以下文档；原文此处板号与本页BRD4161A不同。


- [EFR32MG12网站](https://www.silabs.com/wireless/zigbee/efr32mg12-series-1-socs)
- [EFR32MG12数据手册](https://www.silabs.com/documents/public/data-sheets/efr32mg12-datasheet.pdf)
- [EFR32xG12参考手册](https://www.silabs.com/documents/public/reference-manuals/efr32xg12-rm.pdf)
- [BRD4170A用户指南](https://www.silabs.com/documents/public/user-guides/ug342-brd4170a-user-guide.pdf)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`slwrb4170a`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="slwrb4170a-hw-features"></a>

<a id="slwrb4170a-slwrb4170a/efr32mg12p433f1024gm68-hw-features-section"></a>

#### `slwrb4170a/efr32mg12p433f1024gm68`目标（Target）

<a id="slwrb4170a-slwrb4170a/efr32mg12p433f1024gm68-hw-features-panel"></a>

<a id="slwrb4170a-slwrb4170a/efr32mg12p433f1024gm68-hw-features-memory"></a>

此开发板目标可用存储器：256 KiB RAM、1 MiB 闪存。

<a id="slwrb4170a-slwrb4170a/efr32mg12p433f1024gm68-hw-features-table"></a>

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
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L75">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L61">已禁用：2</a>）</td>
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
<td>Silicon Labs Series 0—2 GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L209">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L254">已禁用：3</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P012_silabs_gecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port"><code>silabs,gecko-gpio-port</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0—2 I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L170">已禁用：2</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P004_silabs_gecko-i2c.md#std-dtcompatible-silabs-gecko-i2c"><code>silabs,gecko-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4170a/../common/efr32-series1-common.dtsi?plain=1#L43">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4170a/../common/efr32-series1-common.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L108">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>这些属性用于支持Zephyr的<code>spi-nor</code>闪存驱动通过Zephyr SPI API，使用基于M25P80的标准命令集控制串行闪存（Serial Flash Memory）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4170a/../common/efr32-series1-common.dtsi?plain=1#L82">已启用：1</a>）</td>
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
<td>Silicon Labs Gecko PWM端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L303">已禁用：1</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P007_silabs_gecko-pwm.md#std-dtcompatible-silabs-gecko-pwm"><code>silabs,gecko-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>GECKO真随机数发生器（TRNG / True Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L310">已禁用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P013_silabs_gecko-trng.md#std-dtcompatible-silabs-gecko-trng"><code>silabs,gecko-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Gecko实时计数器（Real-Time Counter，RTCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L190">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P009_silabs_gecko-rtcc.md#std-dtcompatible-silabs-gecko-rtcc"><code>silabs,gecko-rtcc</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Gecko通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L126">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L144">已禁用：2</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P008_silabs_gecko-usart.md#std-dtcompatible-silabs-gecko-usart"><code>silabs,gecko-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Gecko低能耗UART（LEUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L162">已禁用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P006_silabs_gecko-leuart.md#std-dtcompatible-silabs-gecko-leuart"><code>silabs,gecko-leuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L135">已启用：1</a>）</td>
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
<td>Silicon Labs Series 0–2看门狗（WDOG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L282">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg12/xg12.dtsi?plain=1#L290">已禁用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P011_silabs_gecko-wdog.md#std-dtcompatible-silabs-gecko-wdog"><code>silabs,gecko-wdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

下表Pin列为引脚名称，例如PA2表示PORTA第2脚，与板卡数据手册及用户手册一致。

<table>
<tr>
<th>引脚（Pin）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PF4</td>
<td>通用输入输出（GPIO）</td>
<td>LED0</td>
</tr>
<tr>
<td>PF5</td>
<td>通用输入输出（GPIO）</td>
<td>LED1</td>
</tr>
<tr>
<td>PF6</td>
<td>通用输入输出（GPIO）</td>
<td>按键PB0</td>
</tr>
<tr>
<td>PF7</td>
<td>通用输入输出（GPIO）</td>
<td>按键PB1</td>
</tr>
<tr>
<td>PA5</td>
<td>通用输入输出（GPIO）</td>
<td>板卡控制器使能：VCOM_ENABLE</td>
</tr>
<tr>
<td>PA0</td>
<td>USART0_TX</td>
<td>UART控制台：VCOM_TX，US0_TX，#0</td>
</tr>
<tr>
<td>PA1</td>
<td>USART0_RX</td>
<td>UART控制台：VCOM_RX，US0_RX，#0</td>
</tr>
<tr>
<td>PC6</td>
<td>SPI_MOSI</td>
<td>闪存MOSI：US1_TX，#11</td>
</tr>
<tr>
<td>PC7</td>
<td>SPI_MISO</td>
<td>闪存MISO：US1_RX，#11</td>
</tr>
<tr>
<td>PC8</td>
<td>SPI_SCLK</td>
<td>闪存串行时钟SCLK：US1_CLK，#11</td>
</tr>
<tr>
<td>PA4</td>
<td>SPI_CS</td>
<td>闪存片选（Chip Select），GPIO</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

EFR32MG12P SoC配置为使用板载38.4 MHz外部振荡器。

<a id="serial-port"></a>

### 串口（Serial Port）

EFR32MG12P SoC具有4个USART及1个低能耗UART（LEUART）。USART0连接板卡控制器，用作控制台。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`slwrb4170a`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td></td>
<td>✅</td>
</tr>
</table>

<a id="flashing"></a>

### 烧录（Flashing）

将BRD4170A无线电板安装到BRD4001A主板，通过USB连接主机。

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b slwrb4170a samples/hello_world
west flash
```

打开串口终端（如minicom或PuTTY），设置如下：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

复位开发板后，终端应显示以下消息：

```text
Hello World! slwrb4170a
```

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [efr32mg12-datasheet.pdf](https://www.silabs.com/documents/public/data-sheets/efr32mg12-datasheet.pdf)：HTTP Error 403: Forbidden。
- [efr32xg12-rm.pdf](https://www.silabs.com/documents/public/reference-manuals/efr32xg12-rm.pdf)：HTTP Error 403: Forbidden。
- [ug342-brd4170a-user-guide.pdf](https://www.silabs.com/documents/public/user-guides/ug342-brd4170a-user-guide.pdf)：HTTP Error 403: Forbidden。
- [efr32mg12-series-1-socs](https://www.silabs.com/wireless/zigbee/efr32mg12-series-1-socs)：HTTP Error 403: Forbidden。

---

[上一章](P030_EFR32MG12_2.4_GHz_19_dBm_SLWRB4161A.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P032_EFR32FG1_2400_868_MHz_13_dBm_Dual_Band_SLWRB4250B.md)
