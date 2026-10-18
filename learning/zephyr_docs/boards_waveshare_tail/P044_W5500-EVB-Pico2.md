---
id: learning.zephyr-docs.boards-waveshare-tail.page-44
title: W5500-EVB-Pico2
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/wiznet/w5500_evb_pico2/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="w5500_evb_pico2"></a>

# 第44章\_W5500-EVB-Pico2

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/wiznet/w5500_evb_pico2/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/w5500_evb_pico2.webp](images/w5500_evb_pico2.webp)](images/w5500_evb_pico2.webp)

W5500-EVB-Pico2

名称（Name）：

`w5500_evb_pico2`

厂商（Vendor）：

[WIZnet Co., Ltd.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=wiznet)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[rp2350a](https://docs.zephyrproject.org/latest/boards/index.html#soc=rp2350a)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/wiznet/w5500_evb_pico2/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

W5500-EVB-Pico2是基于RP2350A及全硬件TCP/IP控制器W5500的评估板，基本使用方式与Raspberry Pi Pico2相同，另通过W5500提供以太网。USB引导加载器支持无需适配器的拖放烧录，也可通过外部适配器使用SWD烧录及调试。

<a id="hardware"></a>

## 硬件（Hardware）


- 双核Arm Cortex-M33或Hazard3，最高150 MHz
- 520 KB片上SRAM
- 16 MB板载QSPI闪存，支持就地执行（XIP）
- 26个GPIO
- 3路模拟输入（Analog Inputs）
- 2个通用异步收发器外设（UART Peripherals）
- 2个串行外设接口控制器（SPI Controllers）
- 2个I2C控制器
- 24路PWM
- USB 1.1控制器，支持主机／设备模式（Host / Device）
- 3个PIO模块，共12个状态机
- 板载LED（On-board LED）
- 1个看门狗定时器外设（Watchdog Timer Peripheral）
- 1个高速发送（HSTX）外设
- WIZnet W5500以太网MAC／PHY

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`w5500_evb_pico2`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="w5500_evb_pico2-hw-features"></a>

<a id="w5500_evb_pico2-w5500_evb_pico2/rp2350a/m33_0-hw-features-section"></a>

#### `w5500_evb_pico2/rp2350a/m33_0`目标（Target）

<a id="w5500_evb_pico2-w5500_evb_pico2/rp2350a/m33_0-hw-features-panel"></a>

<a id="w5500_evb_pico2-w5500_evb_pico2/rp2350a/m33_0-hw-features-memory"></a>

该开发板目标的片上存储容量：520 KiB RAM、2 MiB Flash。

<a id="w5500_evb_pico2-w5500_evb_pico2/rp2350a/m33_0-hw-features-table"></a>

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
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L37">已启用：2</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L342">已启用：1</a>）</td>
<td><a href="../hardware/P894_RaspberryPiPico模数转换器绑定.md#dtbinding-raspberrypi-pico-adc"><code>raspberrypi,pico-adc</code></a></td>
</tr>
<tr>
<td rowspan="5">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico时钟（Clock）的表示（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L47">已启用：11</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L174">已禁用：2</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P017_raspberrypi_pico-clock.md#std-dtcompatible-raspberrypi-pico-clock"><code>raspberrypi,pico-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico锁相环（PLL）的表示（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L128">已启用：2</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P018_raspberrypi_pico-pll.md#std-dtcompatible-raspberrypi-pico-pll"><code>raspberrypi,pico-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico环形振荡器（Ring Oscillator）的表示（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L150">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P019_raspberrypi_pico-rosc.md#std-dtcompatible-raspberrypi-pico-rosc"><code>raspberrypi,pico-rosc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico外部振荡器（External Oscillator）的表示（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L168">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P020_raspberrypi_pico-xosc.md#std-dtcompatible-raspberrypi-pico-xosc"><code>raspberrypi,pico-xosc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico时钟控制器（Clock Controller）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L220">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P016_raspberrypi_pico-clock-controller.md#std-dtcompatible-raspberrypi-pico-clock-controller"><code>raspberrypi,pico-clock-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L366">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L382">已禁用：1</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P008_raspberrypi_pico-timer.md#std-dtcompatible-raspberrypi-pico-timer"><code>raspberrypi,pico-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico SHA-256硬件加速器（Accelerator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L405">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P006_raspberrypi_pico-sha256.md#std-dtcompatible-raspberrypi-pico-sha256"><code>raspberrypi,pico-sha256</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico直接存储器访问（DMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L425">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P009_raspberrypi_pico-dma.md#std-dtcompatible-raspberrypi-pico-dma"><code>raspberrypi,pico-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>WIZnet W5500以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wiznet/w5500_evb_pico2/w5500_evb_pico2.dtsi?plain=1#L133">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P018_wiznet_w5500.md#std-dtcompatible-wiznet-w5500"><code>wiznet,w5500</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L197">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P021_raspberrypi_pico-flash-controller.md#std-dtcompatible-raspberrypi-pico-flash-controller"><code>raspberrypi,pico-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="3">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L242">已启用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P006_raspberrypi_pico-gpio.md#std-dtcompatible-raspberrypi-pico-gpio"><code>raspberrypi,pico-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico GPIO端口（Port）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L255">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L264">已禁用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P005_raspberrypi_pico-gpio-port.md#std-dtcompatible-raspberrypi-pico-gpio-port"><code>raspberrypi,pico-gpio-port</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通过Raspberry Pi Pico排针引出的GPIO（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wiznet/w5500_evb_pico2/w5500_evb_pico2.dtsi?plain=1#L24">已启用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P007_raspberrypi_pico-header.md#std-dtcompatible-raspberrypi-pico-header"><code>raspberrypi,pico-header</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L318">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L330">已禁用：1</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P008_raspberrypi_pico-i2c.md#std-dtcompatible-raspberrypi-pico-i2c"><code>raspberrypi,pico-i2c</code></a></td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wiznet/w5500_evb_pico2/w5500_evb_pico2.dtsi?plain=1#L57">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wiznet/w5500_evb_pico2/w5500_evb_pico2.dtsi?plain=1#L66">已禁用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico处理器间邮箱（Interprocessor Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L494">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P050_Pico邮箱绑定.md#dtbinding-raspberrypi-pico-mbox"><code>raspberrypi,pico-mbox</code></a></td>
</tr>
<tr>
<td rowspan="3">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico电源管理器（POWMAN / Power Manager）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L418">已启用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P012_raspberrypi_pico-powman.md#std-dtcompatible-raspberrypi-pico-powman"><code>raspberrypi,pico-powman</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico可编程输入输出（PIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L451">已禁用：3</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P011_raspberrypi_pico-pio.md#std-dtcompatible-raspberrypi-pico-pio"><code>raspberrypi,pico-pio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico单周期输入输出（SIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L490">已启用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P013_raspberrypi_pico-sio.md#std-dtcompatible-raspberrypi-pico-sio"><code>raspberrypi,pico-sio</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L205">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L518">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P025_raspberrypi_pico-pinctrl.md#std-dtcompatible-raspberrypi-pico-pinctrl"><code>raspberrypi,pico-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L353">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P014_raspberrypi_pico-pwm.md#std-dtcompatible-raspberrypi-pico-pwm"><code>raspberrypi,pico-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico内核电源稳压器（Core Supply Regulator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L411">已启用：1</a>）</td>
<td><a href="../hardware/P654_RaspberryPi内核供电稳压器绑定.md#dtbinding-raspberrypi-core-supply-regulator"><code>raspberrypi,core-supply-regulator</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico复位控制器（Reset Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L214">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P012_raspberrypi_pico-reset.md#std-dtcompatible-raspberrypi-pico-reset"><code>raspberrypi,pico-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico随机数发生器／熵源（RNG / Entropy）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L484">已禁用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P001_raspberrypi_pico-rng.md#std-dtcompatible-raspberrypi-pico-rng"><code>raspberrypi,pico-rng</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico系列温度传感器（Temperature Sensor）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L523">已启用：1</a>）</td>
<td><a href="../sensor_realtek_rohm_sensirion_binding_reference/P003_raspberrypi_pico-temp.md#std-dtcompatible-raspberrypi-pico-temp"><code>raspberrypi,pico-temp</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L274">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L284">已禁用：1</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P002_raspberrypi_pico-uart.md#std-dtcompatible-raspberrypi-pico-uart"><code>raspberrypi,pico-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L294">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L306">已禁用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P010_raspberrypi_pico-spi.md#std-dtcompatible-raspberrypi-pico-spi"><code>raspberrypi,pico-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L192">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico USB设备控制器（USB Device Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L440">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P014_raspberrypi_pico-usbd.md#std-dtcompatible-raspberrypi-pico-usbd"><code>raspberrypi,pico-usbd</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/raspberrypi/rpi_pico/rp2350.dtsi?plain=1#L398">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P015_raspberrypi_pico-watchdog.md#std-dtcompatible-raspberrypi-pico-watchdog"><code>raspberrypi,pico-watchdog</code></a></td>
</tr>
</table>

<a id="pin-mapping"></a>

### 引脚映射（Pin Mapping）

RP2350A SoC外设可路由到开发板上的不同引脚，路由配置可通过设备树源码（DTS）修改。各外设支持的路由请参阅数据手册。

W5500_EVB_PICO2外部引脚映射与Raspberry Pi Pico2相同。GPIO25连接板载LED，因此blinky可正常使用。GPIO29即ADC_CH3内部连接VSYS/3测量电压。W5500连接SPI0的P16—P19，复位及中断分别为P20和P21，这些引脚也与边缘连接器共用。

<a id="id3"></a>

原理图及其他认证资料见[W5500评估板Pico2文档](https://docs.wiznet.io/Product/Chip/Ethernet/W5500/w5500-evb-pico2)[注1](#id2)。

<a id="default-zephyr-peripheral-mapping"></a>

#### Zephyr 默认外设映射（Peripheral Mapping）：


- `UART0_TX : P0`
- `UART0_RX : P1`
- I2C0串行数据（SDA）：P4
- I2C0串行时钟（SCL）：P5
- I2C1 SDA：P14
- I2C1 SCL：P15
- SPI0_RX：P16
- SPI0_CSN：P17
- `SPI0_SCK : P18`
- `SPI0_TX : P19`
- W5500复位：P20
- W5500中断：P21
- ADC通道0（ADC_CH0）：P26
- ADC通道1（ADC_CH1）：P27
- ADC通道2（ADC_CH2）：P28
- ADC_CH3：P29

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`w5500_evb_pico2`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>调试服务器（debugserver）</th>
<th>实时传输（rtt）</th>
<th>连接调试会话（attach）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd"><code>openocd</code></a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>probe-rs</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-uf2">uf2</a></td>
<td>✅</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

注意（Note）

原文说明Zephyr SDK所附OpenOCD当前不支持RP2350。调试需使用Raspberry Pi OpenOCD分支，或Segger J-Link等外部探针；该说明按来源页面的版本背景保留。

烧录和调试总体流程与[Raspberry Pi Pico](../boards_rak_raspberry_raytac/P012_Raspberry_Pi_Pico.md#rpi_pico)相同，见其“编程与调试”文档。下面以构建并烧录[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)为例。（[烧录与调试（Programming and Debugging）](../boards_rak_raspberry_raytac/P012_Raspberry_Pi_Pico.md#rpi-pico-programming-and-debugging)；[Raspberry Pi Pico](../boards_rak_raspberry_raytac/P012_Raspberry_Pi_Pico.md#rpi_pico)）

```text
# From the root of the zephyr repository
west build -b w5500_evb_pico2/rp2350a/m33_0 samples/basic/blinky
west flash --openocd /usr/local/bin/openocd
```

<a id="id2"></a>

〔[1](#id3)〕 [https://docs.wiznet.io/Product/Chip/Ethernet/W5500/w5500-evb-pico2](https://docs.wiznet.io/Product/Chip/Ethernet/W5500/w5500-evb-pico2)

## 译注

W5500-EVB-Pico2的RP2350 OpenOCD限制按原文版本背景保留，不能当作所有未来SDK的结论。

---

[上一章](P043_W5500-EVB-Pico.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P045_W55RP20-EVB-Pico.md)
