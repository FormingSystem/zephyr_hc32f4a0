---
id: learning.zephyr-docs.boards-adafruit-feather-and-grand-central.page-3
title: Feather M4 Express
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/adafruit/feather_m4_express/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit_feather_m4_express"></a>

# 第3章\_Feather M4 Express

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/adafruit/feather_m4_express/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/adafruit_feather_m4_express.webp](images/adafruit_feather_m4_express.webp)](images/adafruit_feather_m4_express.webp)

Feather M4 Express

名称（Name）：

`adafruit_feather_m4_express`

厂商（Vendor）：

[Adafruit Industries, LLC](https://docs.zephyrproject.org/latest/boards/index.html#vendor=adafruit)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[samd51j19a](https://docs.zephyrproject.org/latest/boards/index.html#soc=samd51j19a)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/feather_m4_express/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Adafruit Feather M4 Express是一款紧凑、轻巧的ARM开发板，板载微型NeoPixel、2 MiB SPI闪存（SPI Flash）、充电状态指示LED、用户LED、USB接口、21个GPIO引脚以及一小块原型制作区域（Prototyping Area）。

<a id="hardware"></a>

## 硬件（Hardware）


- ATSAMD51J19A ARM Cortex-M4处理器，运行频率120 MHz
- 512 KiB闪存（Flash）和192 KiB随机存储器（RAM）
- 2 MiB SPI闪存（SPI Flash）
- 经校准的内部8 MHz振荡器（Trimmed Internal Oscillator）
- 1个用户LED（User LED）
- 1个RGB NeoPixel LED
- 原生USB端口（Native USB Port）
- 1个复位按键（Reset Button）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`adafruit_feather_m4_express`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="adafruit_feather_m4_express-hw-features"></a>

<a id="adafruit_feather_m4_express-adafruit_feather_m4_express/samd51j19a-hw-features-section"></a>

#### `adafruit_feather_m4_express/samd51j19a`目标（Target）

<a id="adafruit_feather_m4_express-adafruit_feather_m4_express/samd51j19a-hw-features-panel"></a>

<a id="adafruit_feather_m4_express-adafruit_feather_m4_express/samd51j19a-hw-features-memory"></a>

该开发板目标的片上存储容量：192 KiB RAM、512 KiB Flash。

<a id="adafruit_feather_m4_express-adafruit_feather_m4_express/samd51j19a-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L59">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM0系列模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L346">已禁用：2</a>）</td>
<td><a href="../hardware/P858_AtmelSAM0模数转换器绑定.md#dtbinding-atmel-sam0-adc"><code>atmel,sam0-adc</code></a></td>
</tr>
<tr>
<td rowspan="2">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>用于定位Atmel SAM0设备的设备ID（Device ID，即序列号）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L86">已启用：1</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P008_atmel_sam0-id.md#std-dtcompatible-atmel-sam0-id"><code>atmel,sam0-id</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAM0多协议串行通信单元（SERCOM），支持UART、SPI和I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L181">已禁用：6</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P009_atmel_sam0-sercom.md#std-dtcompatible-atmel-sam0-sercom"><code>atmel,sam0-sercom</code></a></td>
</tr>
<tr>
<td rowspan="3">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM0主时钟控制器（MCLK / Main Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L94">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P011_atmel_sam0-mclk.md#std-dtcompatible-atmel-sam0-mclk"><code>atmel,sam0-mclk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAM0 32 kHz振荡器控制器（OSC32KCTRL / Oscillator Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L101">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P012_atmel_sam0-osc32kctrl.md#std-dtcompatible-atmel-sam0-osc32kctrl"><code>atmel,sam0-osc32kctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAMD0通用时钟控制器（GCLK / Generic Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L108">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P010_atmel_sam0-gclk.md#std-dtcompatible-atmel-sam0-gclk"><code>atmel,sam0-gclk</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>以32位模式运行的Atmel SAM0基本定时器／计数器（TC / Timer Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L419">已禁用：3</a>）</td>
<td><a href="../counter_binding_reference/P011_atmel_sam0-tc32.md#std-dtcompatible-atmel-sam0-tc32"><code>atmel,sam0-tc32</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAMD5x/E5x系列数模转换器（DAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L395">已禁用：1</a>）</td>
<td><a href="../hardware/P764_AtmelSAMD5x数模转换器绑定.md#dtbinding-atmel-samd5x-dac"><code>atmel,samd5x-dac</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM0直接存储器访问控制器（DMA Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L137">已启用：1</a>）</td>
<td><a href="../dma_binding_reference/P011_atmel_sam0-dmac.md#std-dtcompatible-atmel-sam0-dmac"><code>atmel,sam0-dmac</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM0非易失性存储器控制器（NVMC / Non-Volatile Memory Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L116">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P007_atmel_sam0-nvmctrl.md#std-dtcompatible-atmel-sam0-nvmctrl"><code>atmel,sam0-nvmctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>SAM0 GPIO端口（PORT）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L276">已启用：4</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P030_atmel_sam0-gpio.md#std-dtcompatible-atmel-sam0-gpio"><code>atmel,sam0-gpio</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAM0系列外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L146">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P008_atmel_sam0-eic.md#std-dtcompatible-atmel-sam0-eic"><code>atmel,sam0-eic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/feather_m4_express/adafruit_feather_m4_express.dts?plain=1#L31">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L68">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L127">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM0引脚复用（PINMUX）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L155">已启用：4</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P015_atmel_sam0-pinmux.md#std-dtcompatible-atmel-sam0-pinmux"><code>atmel,sam0-pinmux</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAM0引脚控制容器（Pinctrl Container）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L269">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P014_atmel_sam0-pinctrl.md#std-dtcompatible-atmel-sam0-pinctrl"><code>atmel,sam0-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>脉宽调制模式（PWM Mode）下的Atmel SAM0 TC定时器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L408">已启用：1</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P008_atmel_sam0-tc-pwm.md#std-dtcompatible-atmel-sam0-tc-pwm"><code>atmel,sam0-tc-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>脉宽调制模式（PWM Mode）下的Atmel SAM0 TCC定时器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L452">已启用：1</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P009_atmel_sam0-tcc-pwm.md#std-dtcompatible-atmel-sam0-tcc-pwm"><code>atmel,sam0-tcc-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM随机数发生器（RNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L326">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P004_atmel_sam-trng.md#std-dtcompatible-atmel-sam-trng"><code>atmel,sam-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM0实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L332">已禁用：1</a>）</td>
<td><a href="../rtc_binding_reference/P005_atmel_sam0-rtc.md#std-dtcompatible-atmel-sam0-rtc"><code>atmel,sam0-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM0 SERCOM UART驱动（Driver）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L236">已启用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P012_atmel_sam0-uart.md#std-dtcompatible-atmel-sam0-uart"><code>atmel,sam0-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM0 SERCOM SPI控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L192">已启用：1</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P009_atmel_sam0-spi.md#std-dtcompatible-atmel-sam0-spi"><code>atmel,sam0-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L76">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>设备模式（Device Mode）下的Atmel SAM0 USB（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L317">已启用：1</a>）</td>
<td><a href="../usb_controller_binding_reference/P006_atmel_sam0-usb.md#std-dtcompatible-atmel-sam0-usb"><code>atmel,sam0-usb</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM0看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L175">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P008_atmel_sam0-watchdog.md#std-dtcompatible-atmel-sam0-watchdog"><code>atmel,sam0-watchdog</code></a></td>
</tr>
</table>

Zephyr可以使用默认的Cortex-M系统节拍定时器（SYSTICK），也可以使用SAM0专用的实时时钟（RTC）。要使用RTC，请设置`CONFIG_CORTEX_M_SYSTICK=n`，并将`CONFIG_SYS_CLOCK_TICKS_PER_SEC`设为不大于32 kHz除以7的值，即不超过4500。

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="id3"></a>

<a id="id5"></a>

<a id="id7"></a>

[Adafruit学习系统（Learning System）](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51)[注1](#id2)提供了开发板的详细信息，包括[引脚分配（Pinouts）](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/pinouts)[注2](#id4)和[原理图（Schematic）](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/downloads)[注3](#id6)。

<a id="system-clock"></a>

### 系统时钟（System Clock）

SAMD51微控制器（MCU）配置为使用32 kHz内部振荡器（Internal Oscillator），配合片上锁相环（PLL）生成120 MHz系统时钟。

<a id="serial-port"></a>

### 串口（Serial Port）

SAMD51微控制器（MCU）有6个基于SERCOM的USART。Feather使用SERCOM5作为Zephyr控制台（Console），通过引脚0（RX）和1（TX）引出。

<a id="spi-port"></a>

### SPI端口（SPI Port）

SAMD51微控制器（MCU）有6个基于SERCOM的SPI接口。Feather可以将SERCOM1配置为SPI模式，通过SCK（SCLK）、MO（MOSI）和MI（MISO）引脚连接设备。

<a id="pwm"></a>

### 脉宽调制（PWM）

SAMD51具有3个脉宽调制发生器（PWM Generators），每个最多6个通道。TCC_0分辨率为24位，其余发生器为16位。TCC_1的引脚2映射到PA18（D7），引脚3映射到PA19（D9）。

<a id="usb-device-port"></a>

### USB设备端口（USB Device Port）

SAMD51微控制器（MCU）的[USB](https://docs.zephyrproject.org/latest/services/connectivity/usb/index.html#usb)设备端口可用于与主机PC通信。更多内容见USB示例应用，例如[USB CDC ACM UART示例](../usb/P054_CDCACM串口示例.md#usb-cdc-acm)；它创建一个虚拟串口（Virtual Serial Port），将收到的字符回显给主机PC。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`adafruit_feather_m4_express`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>rtt</th>
<th>debugserver</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-bossac">bossac</a></td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

Feather出厂时预装兼容BOSSA的UF2引导加载程序（Bootloader）。快速连续按两次复位按键，即可进入引导加载程序。

另外，启用[`CONFIG_USB_CDC_ACM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_CDC_ACM)后，执行`west flash`时会自动进入引导加载程序（Bootloader）。

<a id="flashing"></a>

### 烧录（Flashing）


1. 构建Zephyr内核和[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例应用：

  ```text
  west build -b adafruit_feather_m4_express samples/hello_world
  ```
2. 使用USB将Feather连接到主机。
3. 将3.3 V USB转串口适配器连接到开发板和主机。开发板引脚连接见前面的[串口（Serial Port）](#serial-port)一节。
4. 运行你惯用的终端程序，监听输出。Linux下的终端设备应为`/dev/ttyUSB0`，例如：

  ```text
  $ minicom -D /dev/ttyUSB0 -o
  ```

  `-o`选项让`minicom`不发送调制解调器初始化字符串（Modem Initialization String）。连接参数应配置如下：


  - 速率（Speed）：115200波特率
  - 数据位（Data）：8位
  - 奇偶校验（Parity）：无（None）
  - 停止位（Stop Bits）：1位
5. 快速连续按两次复位按键，进入引导加载程序模式（Bootloader Mode）。
6. 烧录镜像（Flash the Image）：

  ```text
  west build -b adafruit_feather_m4_express samples/hello_world
  west flash
  ```

  终端中应显示`Hello World! adafruit_feather_m4_express`。

<a id="debugging"></a>

### 调试（Debugging）

除了内置引导加载程序（Bootloader），还可以使用Segger J-Link等串行线调试探针（SWD Probe）烧录和调试Feather。


1. <a id="id9"></a>

  将Feather的SWCLK、SWDIO、RESET、GND和3V3引脚，分别连接到[J-Link](https://www.segger.com/products/debug-probes/j-link/technology/interface-description/)[注4](#id8)的SWCLK、SWDIO、RESET、GND和VTref引脚。
2. 烧录镜像（Flash the Image）：

  ```text
  west build -b adafruit_feather_m4_express samples/hello_world
  west flash -r openocd
  ```
3. 开始调试（Start Debugging）：

  ```text
  west build -b adafruit_feather_m4_express samples/hello_world
  west debug
  ```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51)

<a id="id4"></a>

〔[2](#id5)〕 [https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/pinouts](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/pinouts)

<a id="id6"></a>

〔[3](#id7)〕 [https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/downloads](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/downloads)

<a id="id8"></a>

〔[4](#id9)〕 [https://www.segger.com/products/debug-probes/j-link/technology/interface-description/](https://www.segger.com/products/debug-probes/j-link/technology/interface-description/)

---

[上一章](P002_Feather_M0_LoRa.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_Feather_nRF52840_Express_Sense_.md)
