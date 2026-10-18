---
id: learning.zephyr-docs.boards-nxp-frdm-imx-kinetis.page-15
title: FRDM-KW41Z
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/frdm_kw41z/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="frdm_kw41z"></a>

# 第15章\_FRDM-KW41Z

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/frdm_kw41z/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/frdm_kw41z.jpg](images/frdm_kw41z.jpg)](images/frdm_kw41z.jpg)

FRDM-KW41Z

名称（Name）：

`frdm_kw41z`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mkw41z4](https://docs.zephyrproject.org/latest/boards/index.html#soc=mkw41z4)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_kw41z/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

FRDM-KW41Z开发套件基于Kinetis® W系列KW41Z／31Z／21Z器件，简称KW41Z。器件采用ARM® Cortex®-M0+，集成2.4 GHz收发器，支持Bluetooth® Smart／低功耗蓝牙（BLE）v4.2、通用频移键控（Generic FSK）、IEEE® 802.15.4及Thread。

套件包含两块Freedom板，可作为开发板，也可作为连接主处理器的扩展板（Shield）。FRDM-KW41Z的外形及引脚布局兼容Arduino™ R3，提供更多扩展选择。

FRDM-KW41Z的高灵敏度2.4 GHz无线电使用PCB F型天线，也可旁路天线，通过SMA连接测试；开发板还提供多种电源、机械及电容触摸按键、开关、LED及集成传感器。

<a id="hardware"></a>

## 硬件（Hardware）


- 可配置为主机（Host），或作为连接主处理器的扩展板（Shield）
- 支持全部DC-DC配置：降压（Buck）、升压（Boost）及旁路（Bypass）
- PCB倒F型天线（Inverted F-type Antenna）
- SMA射频连接器（RF Connector）
- 已通过射频法规认证（RF Regulatory Certified）
- 用于空中固件升级（OTA）的串行闪存
- 板载NXP FXOS8700CQ数字传感器，集成三轴加速度计，量程±2g／±4g／±8g，以及三轴磁力计
- OpenSDA及JTAG调试

KW41Z SoC及FRDM-KW41Z更多信息：


- [KW41Z网站](https://www.nxp.com/products/wireless/zigbee/kinetis-kw41z-2.4-ghz-dual-mode-bluetooth-low-energy-and-802.15.4-wireless-radio-microcontroller-mcu-based-on-arm-cortex-m0-plus-core:KW41Z)
- [KW41Z数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/MKW41Z512.pdf)
- [KW41Z参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=MKW41Z512RM)
- [FRDM-KW41Z网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/w-serieswireless-conn.m0-plus-m4/freedom-development-kit-for-kinetis-kw41z-31z-21z-mcus:FRDM-KW41Z)
- [FRDM-KW41Z用户指南（User Guide）](https://www.nxp.com/webapp/Download?colCode=FRDMKW41ZUG)
- [FRDM-KW41Z原理图（Schematics）](https://www.nxp.com/webapp/Download?colCode=FRDM-KW41Z-SCH)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`frdm_kw41z`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="frdm_kw41z-hw-features"></a>

<a id="frdm_kw41z-frdm_kw41z/mkw41z4-hw-features-section"></a>

#### `frdm_kw41z/mkw41z4`目标（Target）

<a id="frdm_kw41z-frdm_kw41z/mkw41z4-hw-features-panel"></a>

<a id="frdm_kw41z-frdm_kw41z/mkw41z4-hw-features-memory"></a>

该开发板目标的片上存储容量：96 KiB RAM、512 KiB Flash。

<a id="frdm_kw41z-frdm_kw41z/mkw41z4-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Kinetis 16位模数转换器（ADC16）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L244">已启用：1</a>）</td>
<td><a href="../hardware/P850_NXPKinetisADC16绑定.md#dtbinding-nxp-kinetis-adc16"><code>nxp,kinetis-adc16</code></a></td>
</tr>
<tr>
<td rowspan="3">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis多用途时钟发生器（MCG）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P003_nxp_kinetis-mcg.md#std-dtcompatible-nxp-kinetis-mcg"><code>nxp,kinetis-mcg</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Kinetis系统集成模块（SIM）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L71">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P006_nxp_kinetis-sim.md#std-dtcompatible-nxp-kinetis-sim"><code>nxp,kinetis-sim</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L76">已启用：2</a>）</td>
<td><a href="../timer_reference/P110_固定比例时钟绑定.md#dtbinding-fixed-factor-clock"><code>fixed-factor-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis闪存模块A（FTFA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P014_nxp_kinetis-ftfa.md#std-dtcompatible-nxp-kinetis-ftfa"><code>nxp,kinetis-ftfa</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Kinetis通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L161">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L171">已禁用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P002_nxp_kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio"><code>nxp,kinetis-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kw41z/frdm_kw41z.dts?plain=1#L98">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP RCM获取复位原因标志（Reset Cause Flags）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P012_nxp_rcm-hwinfo.md#std-dtcompatible-nxp-rcm-hwinfo"><code>nxp,rcm-hwinfo</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Kinetis I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L123">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L112">已禁用：1</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P002_nxp_kinetis-i2c.md#std-dtcompatible-nxp-kinetis-i2c"><code>nxp,kinetis-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">低速率无线个域网（IEEE 802.15.4）</td>
<td>片上（On-Chip）</td>
<td>NXP KW41Z IEEE 802.15.4节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L259">已启用：1</a>）</td>
<td><a href="../lora_ieee802154_binding_reference/P006_nxp_kw41z-ieee802154.md#std-dtcompatible-nxp-kw41z-ieee802154"><code>nxp,kw41z-ieee802154</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kw41z/frdm_kw41z.dts?plain=1#L82">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kw41z/frdm_kw41z.dts?plain=1#L44">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kw41z/frdm_kw41z.dts?plain=1#L63">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L101">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L143">已启用：3</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P017_nxp_port-pinmux.md#std-dtcompatible-nxp-port-pinmux"><code>nxp,port-pinmux</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P016_nxp_port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl"><code>nxp,port-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L211">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L222">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P008_nxp_kinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm"><code>nxp,kinetis-tpm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Kinetis真随机数发生器（TRNG / True Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L252">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P020_nxp_kinetis-trng.md#std-dtcompatible-nxp-kinetis-trng"><code>nxp,kinetis-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>NXP实时时钟（RTC / Real Time Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L58">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P002_nxp_rtc.md#std-dtcompatible-nxp-rtc"><code>nxp,rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>FXOS8700六轴加速度计／磁力计传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kw41z/frdm_kw41z.dts?plain=1#L147">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P052_nxp_fxos8700.md#std-dtcompatible-nxp-fxos8700"><code>nxp,fxos8700</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L134">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP DSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L190">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L201">已禁用：1</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P018_nxp_dspi.md#std-dtcompatible-nxp-dspi"><code>nxp,dspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kwx/nxp_kw41z.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

KW41Z有3对引脚复用／GPIO控制器，FRDM-KW41Z当前仅启用PORTA／GPIOA及PORTC／GPIOC两对。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PTC1</td>
<td>通用输入输出（GPIO）</td>
<td>红色LED／FXOS8700中断1（INT1）</td>
</tr>
<tr>
<td>PTA19</td>
<td>通用输入输出（GPIO）</td>
<td>绿色LED（Green LED）</td>
</tr>
<tr>
<td>PTA18</td>
<td>通用输入输出（GPIO）</td>
<td>蓝色LED（Blue LED）</td>
</tr>
<tr>
<td>PTB2</td>
<td>模数转换器（ADC）</td>
<td>ADC0通道3</td>
</tr>
<tr>
<td>PTC2</td>
<td>I2C1_SCL</td>
<td>I2C／FXOS8700</td>
</tr>
<tr>
<td>PTC3</td>
<td>I2C1_SDA</td>
<td>I2C／FXOS8700</td>
</tr>
<tr>
<td>PTC4</td>
<td>通用输入输出（GPIO）</td>
<td>SW3</td>
</tr>
<tr>
<td>PTC5</td>
<td>通用输入输出（GPIO）</td>
<td>SW4</td>
</tr>
<tr>
<td>PTC6</td>
<td>LPUART0_RX</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>PTC7</td>
<td>LPUART0_TX</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>PTC16</td>
<td>SPI0_SCK</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>PTC17</td>
<td>SPI0_SOUT</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>PTC18</td>
<td>SPI0_SIN</td>
<td>串行外设接口（SPI）</td>
</tr>
<tr>
<td>PTC19</td>
<td>SPI0_PCS0</td>
<td>串行外设接口（SPI）</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

KW41Z使用板载32 MHz外部振荡器及片上FLL，生成40 MHz系统时钟。

<a id="serial-port"></a>

### 串口（Serial Port）

KW41Z只有一个UART，用于控制台。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`frdm_kw41z`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-pyocd">pyocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

按通常方式构建并烧录应用，详见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）与“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

<a id="configuring-a-debug-probe"></a>

### 配置调试探针（Configuring a Debug Probe）

烧录及调试均使用调试探针，默认配置为OpenSDA DAPLink板载调试探针。（[OpenSDA DAPLink板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#opensda-daplink-onboard-debug-probe)）

<a id="option-1-opensda-daplink-onboard-debug-probe-recommended"></a>

#### 选项1：OpenSDA DAPLink板载调试探针，推荐（[OpenSDA DAPLink板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#opensda-daplink-onboard-debug-probe)）

安装pyOCD调试主机工具，并确保工具位于搜索路径中。（[pyOCD调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#pyocd-debug-host-tools)）

按OpenSDA DAPLink板载调试探针说明，写入[OpenSDA DAPLink FRDM-KW41Z固件](https://www.nxp.com/downloads/en/reference-applications/OpenSDAv2.2_DAPLink_frdmkw41z_rev0241.zip)。（[OpenSDA DAPLink板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#opensda-daplink-onboard-debug-probe)）

<a id="option-2-opensda-jlink-onboard-debug-probe"></a>

#### 选项2：OpenSDA J-Link板载调试探针（[OpenSDA J-Link板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#opensda-jlink-onboard-debug-probe)）

安装J-Link调试主机工具（Debug Host Tools），并确保工具位于搜索路径中。（[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)）

按OpenSDA J-Link板载调试探针说明，写入[OpenSDA J-Link FRDM-KW41Z固件](https://www.segger.com/downloads/jlink/OpenSDA_FRDM-KW41Z)。（[OpenSDA J-Link板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#opensda-jlink-onboard-debug-probe)）

调用west build时添加-DBOARD_FLASH_RUNNER=jlink及-DBOARD_DEBUG_RUNNER=jlink，将运行工具改为J-Link。原文此处称默认工具为pyOCD，与前文默认LinkServer的说明不同：

```text
# From the root of the zephyr repository
west build -b frdm_kw41z samples/hello_world -- -DBOARD_FLASH_RUNNER=jlink -DBOARD_DEBUG_RUNNER=jlink
```

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

无论选择哪种调试探针，串行控制台都使用OpenSDA微控制器作为USB转串口适配器。

用USB线缆将PC连接J6。

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
west build -b frdm_kw41z samples/hello_world
west flash
```

打开串口终端，按SW1复位开发板，应显示以下消息：

```text
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! frdm_kw41z
```

<a id="debugging"></a>

### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b frdm_kw41z samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! frdm_kw41z
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

原文射频认证状态与产品描述按来源保留；3组GPIO中Zephyr仅启用A、C两组。32 MHz晶振和FLL产生的40 MHz系统时钟分别说明。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [MKW41Z512.pdf](https://www.nxp.com/docs/en/data-sheet/MKW41Z512.pdf)：HTTP Error 404: Not Found。
- [OpenSDAv2.2_DAPLink_frdmkw41z_rev0241.zip](https://www.nxp.com/downloads/en/reference-applications/OpenSDAv2.2_DAPLink_frdmkw41z_rev0241.zip)：HTTP Error 404: Not Found。
- [freedom-development-kit-for-kinetis-kw41z-31z-21z-mcus:FRDM-KW41Z](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/w-serieswireless-conn.m0-plus-m4/freedom-development-kit-for-kinetis-kw41z-31z-21z-mcus:FRDM-KW41Z)：HTTP Error 404: Not Found。
- [kinetis-kw41z-2.4-ghz-dual-mode-bluetooth-low-energy-and-802.15.4-wireless-radio-microcontroller-mcu-based-on-arm-cortex-m0-plus-core:KW41Z](https://www.nxp.com/products/wireless/zigbee/kinetis-kw41z-2.4-ghz-dual-mode-bluetooth-low-energy-and-802.15.4-wireless-radio-microcontroller-mcu-based-on-arm-cortex-m0-plus-core:KW41Z)：HTTP Error 404: Not Found。
- [Download?colCode=FRDM-KW41Z-SCH](https://www.nxp.com/webapp/Download?colCode=FRDM-KW41Z-SCH)：HTTP Error 404: Not Found。
- [Download?colCode=FRDMKW41ZUG](https://www.nxp.com/webapp/Download?colCode=FRDMKW41ZUG)：HTTP Error 404: Not Found。
- [Download?colCode=MKW41Z512RM](https://www.nxp.com/webapp/Download?colCode=MKW41Z512RM)：HTTP Error 404: Not Found。

---

[上一章](P014_FRDM-KL25Z.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P016_NXP_Semiconductors.md)
