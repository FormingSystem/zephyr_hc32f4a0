---
id: learning.zephyr-docs.boards-realtek-ruiside-sifive.page-6
title: RTL8752H Evaluation Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/realtek/rtl8752h_evb/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rtl8752h_evb"></a>

# 第6章\_RTL8752H评估板（Evaluation Board）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/realtek/rtl8752h_evb/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id2"></a>

[![官方原图：../../../../_images/rtl8752h_evb.webp](images/rtl8752h_evb.webp)](images/rtl8752h_evb.webp)

RTL8752H评估板（Evaluation Board）

名称（Name）：

`rtl8752h_evb`

厂商（Vendor）：

[Realtek Semiconductor Corp.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=realtek)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[rtl8752hjf](https://docs.zephyrproject.org/latest/boards/index.html#soc=rtl8752hjf)、[rtl8752hmf](https://docs.zephyrproject.org/latest/boards/index.html#soc=rtl8752hmf)、[rtl8752hkf](https://docs.zephyrproject.org/latest/boards/index.html#soc=rtl8752hkf)及[rtl8752hjl](https://docs.zephyrproject.org/latest/boards/index.html#soc=rtl8752hjl)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/realtek/rtl8752h_evb/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

RTL8752H以超低功耗支持Bluetooth 5.4、2.4 GHz及IEEE 802.15.4（Thread／Zigbee）。它配有40 MHz Arm Cortex-M0+处理器、大容量闪存及SRAM和灵活的GPIO，可用于遥控器、Mesh智能家居、小型人机界面（HMI）设备、低成本可穿戴设备、智慧健康医疗、智能表计、智能锁及电子货架标签等。

<a id="id4"></a>

更多信息见[RTL8752H介绍](https://www.realmcu.com/en/Home/Products/RTL8752H-Series)[注1](#id3)。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="rtl8752h-series-features"></a>

### RTL8752H系列功能（Series Features）

其特性包括：


- Arm Cortex-M0+，最高频率40 MHz
- 120 KB SRAM
- 512 KB或1024 KB闪存，取决于具体型号
- 低功耗蓝牙（Bluetooth Low Energy）及802.15.4
- 支持安全启动（Secure Boot）
- 外设接口（Peripheral Interface）：


  - 灵活的GPIO设计
  - 硬件按键扫描（Keyscan）及正交解码器（Quad-decoder）
  - 内置红外收发器及接收器（IR Transceiver／Receiver）
  - 实时计数器（RTC / Real-Time Counters）
  - 2路SPI主机／从机、8个定时器、2路I2C、8路PWM及2路UART
  - I8080／四线SPI（QSPI）
  - 400 ksps、12位、6通道辅助ADC（AUXADC）
  - I2S／脉冲编码调制（PCM）接口
  - 内部32 kHz RC振荡器（RCOSC），用于维持BLE连接
  - 内置可编程增益放大器（PGA）及音频ADC
  - AES-128／192／256加解密引擎及真随机数发生器（TRNG）
- 射频性能（RF Performance）：发射功率可调为0、4或7.5 dBm，详情见数据手册；BLE在1 Mbit/s时接收灵敏度为−97 dBm；IEEE 802.15.4在250 kbit/s O-QPSK DSSS模式下接收灵敏度为−102 dBm；快速自动增益控制（AGC）改善接收动态范围。

<a id="board-features"></a>

### 开发板功能（Board Features）

RTL8752H评估板采用可更换子板（Daughterboard），子板上搭载RTL8752H SoC，支持以下子板：


- RTL8752HJL／RTL8752HMF子板（Daughter Board）
- RTL8752HJF／RTL8752HKF子板（Daughter Board）

<a id="id6"></a>

更多板卡信息见[RTL8752H评估板指南](https://docs.realmcu.com/sdk/rtl8752h/common/en/latest/evb_guide/text_en/README.html)[注2](#id5)。

`rtl8752h_evb`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="rtl8752h_evb-hw-features"></a>

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hjf-hw-features-section"></a>

#### `rtl8752h_evb/rtl8752hjf`目标（Target）

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hjf-hw-features-panel"></a>

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hjf-hw-features-memory"></a>

该开发板目标的片上存储容量：57 KiB RAM、1 MiB Flash。

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hjf-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Bee模数转换器（ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L443">已禁用：1</a>）</td>
<td><a href="../hardware/P896_RealtekBee模数转换器绑定.md#dtbinding-realtek-bee-adc"><code>realtek,bee-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee SoC的蓝牙主机控制器接口（HCI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L55">已启用：1</a>）</td>
<td><a href="../bluetooth_vendor_hci_binding_reference/P011_realtek_bee-bt-hci.md#std-dtcompatible-realtek-bee-bt-hci"><code>realtek,bee-bt-hci</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Bee时钟控制器（Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L61">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P022_realtek_bee-cctl.md#std-dtcompatible-realtek-bee-cctl"><code>realtek,bee-cctl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L455">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee定时器，用作计数器（Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L229">已禁用：6</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P011_realtek_bee-counter-timer.md#std-dtcompatible-realtek-bee-counter-timer"><code>realtek,bee-counter-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek Bee实时时钟（RTC）计数器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L367">已禁用：1</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P010_realtek_bee-counter-rtc.md#std-dtcompatible-realtek-bee-counter-rtc"><code>realtek,bee-counter-rtc</code></a></td>
</tr>
<tr>
<td rowspan="2">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee系列AES硬件加速器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L383">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P007_realtek_bee-aes.md#std-dtcompatible-realtek-bee-aes"><code>realtek,bee-aes</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek Bee系列SHA-256硬件加速器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L389">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P008_realtek_bee-sha256.md#std-dtcompatible-realtek-bee-sha256"><code>realtek,bee-sha256</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Bee直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L401">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P011_realtek_bee-dma.md#std-dtcompatible-realtek-bee-dma"><code>realtek,bee-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee NOR闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L113">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P023_realtek_bee-nor-flash-controller.md#std-dtcompatible-realtek-bee-nor-flash-controller"><code>realtek,bee-nor-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Bee通用输入输出（GPIO）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L180">已启用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P011_realtek_bee-gpio.md#std-dtcompatible-realtek-bee-gpio"><code>realtek,bee-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Bee I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L345">已禁用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P010_realtek_bee-i2c.md#std-dtcompatible-realtek-bee-i2c"><code>realtek,bee-i2c</code></a></td>
</tr>
<tr>
<td rowspan="2">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>Bee按键扫描（Keyscan）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L337">已禁用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P016_realtek_bee-keyscan.md#std-dtcompatible-realtek-bee-keyscan"><code>realtek,bee-keyscan</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/realtek/rtl8752h_evb/rtl8752h_evb_common.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/realtek/rtl8752h_evb/rtl8752h_evb_common.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L121">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P008_realtek_bee-nor-flash.md#std-dtcompatible-realtek-bee-nor-flash"><code>realtek,bee-nor-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Bee引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L175">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P003_realtek_bee-pinctrl.md#std-dtcompatible-realtek-bee-pinctrl"><code>realtek,bee-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee定时器，用作脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L234">已禁用：6</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P016_realtek_bee-pwm.md#std-dtcompatible-realtek-bee-pwm"><code>realtek,bee-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L395">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P003_realtek_bee-trng.md#std-dtcompatible-realtek-bee-trng"><code>realtek,bee-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>Bee基本正交解码器（QDEC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L375">已禁用：1</a>）</td>
<td><a href="../sensor_realtek_rohm_sensirion_binding_reference/P005_realtek_bee-basic-qdec.md#std-dtcompatible-realtek-bee-basic-qdec"><code>realtek,bee-basic-qdec</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Bee通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L213">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L196">已禁用：2</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P004_realtek_bee-uart.md#std-dtcompatible-realtek-bee-uart"><code>realtek,bee-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Bee串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L412">已禁用：3</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P012_realtek_bee-spi.md#std-dtcompatible-realtek-bee-spi"><code>realtek,bee-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L73">已启用：5</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek Bee定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L222">已禁用：6</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P011_realtek_bee-timer.md#std-dtcompatible-realtek-bee-timer"><code>realtek,bee-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee内核看门狗定时器（Core Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L190">已禁用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P002_realtek_bee-core-wdt.md#std-dtcompatible-realtek-bee-core-wdt"><code>realtek,bee-core-wdt</code></a></td>
</tr>
</table>

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hjl-hw-features-section"></a>

#### `rtl8752h_evb/rtl8752hjl`目标（Target）

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hjl-hw-features-panel"></a>

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hjl-hw-features-memory"></a>

该开发板目标的片上存储容量：57 KiB RAM、512 KiB Flash。

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hjl-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Bee模数转换器（ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L443">已禁用：1</a>）</td>
<td><a href="../hardware/P896_RealtekBee模数转换器绑定.md#dtbinding-realtek-bee-adc"><code>realtek,bee-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee SoC的蓝牙主机控制器接口（HCI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L55">已启用：1</a>）</td>
<td><a href="../bluetooth_vendor_hci_binding_reference/P011_realtek_bee-bt-hci.md#std-dtcompatible-realtek-bee-bt-hci"><code>realtek,bee-bt-hci</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Bee时钟控制器（Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L61">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P022_realtek_bee-cctl.md#std-dtcompatible-realtek-bee-cctl"><code>realtek,bee-cctl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L455">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee定时器，用作计数器（Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L229">已禁用：6</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P011_realtek_bee-counter-timer.md#std-dtcompatible-realtek-bee-counter-timer"><code>realtek,bee-counter-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek Bee实时时钟（RTC）计数器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L367">已禁用：1</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P010_realtek_bee-counter-rtc.md#std-dtcompatible-realtek-bee-counter-rtc"><code>realtek,bee-counter-rtc</code></a></td>
</tr>
<tr>
<td rowspan="2">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee系列AES硬件加速器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L383">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P007_realtek_bee-aes.md#std-dtcompatible-realtek-bee-aes"><code>realtek,bee-aes</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek Bee系列SHA-256硬件加速器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L389">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P008_realtek_bee-sha256.md#std-dtcompatible-realtek-bee-sha256"><code>realtek,bee-sha256</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Bee直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L401">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P011_realtek_bee-dma.md#std-dtcompatible-realtek-bee-dma"><code>realtek,bee-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee NOR闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L113">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P023_realtek_bee-nor-flash-controller.md#std-dtcompatible-realtek-bee-nor-flash-controller"><code>realtek,bee-nor-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Bee通用输入输出（GPIO）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L180">已启用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P011_realtek_bee-gpio.md#std-dtcompatible-realtek-bee-gpio"><code>realtek,bee-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Bee I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L345">已禁用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P010_realtek_bee-i2c.md#std-dtcompatible-realtek-bee-i2c"><code>realtek,bee-i2c</code></a></td>
</tr>
<tr>
<td rowspan="2">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>Bee按键扫描（Keyscan）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L337">已禁用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P016_realtek_bee-keyscan.md#std-dtcompatible-realtek-bee-keyscan"><code>realtek,bee-keyscan</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/realtek/rtl8752h_evb/rtl8752h_evb_common.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/realtek/rtl8752h_evb/rtl8752h_evb_common.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L121">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P008_realtek_bee-nor-flash.md#std-dtcompatible-realtek-bee-nor-flash"><code>realtek,bee-nor-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Bee引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L175">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P003_realtek_bee-pinctrl.md#std-dtcompatible-realtek-bee-pinctrl"><code>realtek,bee-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee定时器，用作脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L234">已禁用：6</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P016_realtek_bee-pwm.md#std-dtcompatible-realtek-bee-pwm"><code>realtek,bee-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L395">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P003_realtek_bee-trng.md#std-dtcompatible-realtek-bee-trng"><code>realtek,bee-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>Bee基本正交解码器（QDEC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L375">已禁用：1</a>）</td>
<td><a href="../sensor_realtek_rohm_sensirion_binding_reference/P005_realtek_bee-basic-qdec.md#std-dtcompatible-realtek-bee-basic-qdec"><code>realtek,bee-basic-qdec</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Bee通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L213">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L196">已禁用：2</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P004_realtek_bee-uart.md#std-dtcompatible-realtek-bee-uart"><code>realtek,bee-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Bee串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L412">已禁用：3</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P012_realtek_bee-spi.md#std-dtcompatible-realtek-bee-spi"><code>realtek,bee-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L73">已启用：5</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek Bee定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L222">已禁用：6</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P011_realtek_bee-timer.md#std-dtcompatible-realtek-bee-timer"><code>realtek,bee-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee内核看门狗定时器（Core Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L190">已禁用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P002_realtek_bee-core-wdt.md#std-dtcompatible-realtek-bee-core-wdt"><code>realtek,bee-core-wdt</code></a></td>
</tr>
</table>

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hkf-hw-features-section"></a>

#### `rtl8752h_evb/rtl8752hkf`目标（Target）

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hkf-hw-features-panel"></a>

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hkf-hw-features-memory"></a>

该开发板目标的片上存储容量：57 KiB RAM、1 MiB Flash。

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hkf-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Bee模数转换器（ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L443">已禁用：1</a>）</td>
<td><a href="../hardware/P896_RealtekBee模数转换器绑定.md#dtbinding-realtek-bee-adc"><code>realtek,bee-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee SoC的蓝牙主机控制器接口（HCI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L55">已启用：1</a>）</td>
<td><a href="../bluetooth_vendor_hci_binding_reference/P011_realtek_bee-bt-hci.md#std-dtcompatible-realtek-bee-bt-hci"><code>realtek,bee-bt-hci</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Bee时钟控制器（Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L61">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P022_realtek_bee-cctl.md#std-dtcompatible-realtek-bee-cctl"><code>realtek,bee-cctl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L455">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee定时器，用作计数器（Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L229">已禁用：6</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P011_realtek_bee-counter-timer.md#std-dtcompatible-realtek-bee-counter-timer"><code>realtek,bee-counter-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek Bee实时时钟（RTC）计数器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L367">已禁用：1</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P010_realtek_bee-counter-rtc.md#std-dtcompatible-realtek-bee-counter-rtc"><code>realtek,bee-counter-rtc</code></a></td>
</tr>
<tr>
<td rowspan="2">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee系列AES硬件加速器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L383">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P007_realtek_bee-aes.md#std-dtcompatible-realtek-bee-aes"><code>realtek,bee-aes</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek Bee系列SHA-256硬件加速器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L389">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P008_realtek_bee-sha256.md#std-dtcompatible-realtek-bee-sha256"><code>realtek,bee-sha256</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Bee直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L401">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P011_realtek_bee-dma.md#std-dtcompatible-realtek-bee-dma"><code>realtek,bee-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee NOR闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L113">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P023_realtek_bee-nor-flash-controller.md#std-dtcompatible-realtek-bee-nor-flash-controller"><code>realtek,bee-nor-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Bee通用输入输出（GPIO）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L180">已启用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P011_realtek_bee-gpio.md#std-dtcompatible-realtek-bee-gpio"><code>realtek,bee-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Bee I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L345">已禁用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P010_realtek_bee-i2c.md#std-dtcompatible-realtek-bee-i2c"><code>realtek,bee-i2c</code></a></td>
</tr>
<tr>
<td rowspan="2">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>Bee按键扫描（Keyscan）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L337">已禁用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P016_realtek_bee-keyscan.md#std-dtcompatible-realtek-bee-keyscan"><code>realtek,bee-keyscan</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/realtek/rtl8752h_evb/rtl8752h_evb_common.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/realtek/rtl8752h_evb/rtl8752h_evb_common.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L121">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P008_realtek_bee-nor-flash.md#std-dtcompatible-realtek-bee-nor-flash"><code>realtek,bee-nor-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Bee引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L175">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P003_realtek_bee-pinctrl.md#std-dtcompatible-realtek-bee-pinctrl"><code>realtek,bee-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee定时器，用作脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L234">已禁用：6</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P016_realtek_bee-pwm.md#std-dtcompatible-realtek-bee-pwm"><code>realtek,bee-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L395">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P003_realtek_bee-trng.md#std-dtcompatible-realtek-bee-trng"><code>realtek,bee-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>Bee基本正交解码器（QDEC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L375">已禁用：1</a>）</td>
<td><a href="../sensor_realtek_rohm_sensirion_binding_reference/P005_realtek_bee-basic-qdec.md#std-dtcompatible-realtek-bee-basic-qdec"><code>realtek,bee-basic-qdec</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Bee通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L213">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L196">已禁用：2</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P004_realtek_bee-uart.md#std-dtcompatible-realtek-bee-uart"><code>realtek,bee-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Bee串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L412">已禁用：3</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P012_realtek_bee-spi.md#std-dtcompatible-realtek-bee-spi"><code>realtek,bee-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L73">已启用：5</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek Bee定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L222">已禁用：6</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P011_realtek_bee-timer.md#std-dtcompatible-realtek-bee-timer"><code>realtek,bee-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee内核看门狗定时器（Core Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L190">已禁用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P002_realtek_bee-core-wdt.md#std-dtcompatible-realtek-bee-core-wdt"><code>realtek,bee-core-wdt</code></a></td>
</tr>
</table>

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hmf-hw-features-section"></a>

#### `rtl8752h_evb/rtl8752hmf`目标（Target）

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hmf-hw-features-panel"></a>

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hmf-hw-features-memory"></a>

该开发板目标的片上存储容量：57 KiB RAM、512 KiB Flash。

<a id="rtl8752h_evb-rtl8752h_evb/rtl8752hmf-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Bee模数转换器（ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L443">已禁用：1</a>）</td>
<td><a href="../hardware/P896_RealtekBee模数转换器绑定.md#dtbinding-realtek-bee-adc"><code>realtek,bee-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee SoC的蓝牙主机控制器接口（HCI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L55">已启用：1</a>）</td>
<td><a href="../bluetooth_vendor_hci_binding_reference/P011_realtek_bee-bt-hci.md#std-dtcompatible-realtek-bee-bt-hci"><code>realtek,bee-bt-hci</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Bee时钟控制器（Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L61">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P022_realtek_bee-cctl.md#std-dtcompatible-realtek-bee-cctl"><code>realtek,bee-cctl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L455">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee定时器，用作计数器（Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L229">已禁用：6</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P011_realtek_bee-counter-timer.md#std-dtcompatible-realtek-bee-counter-timer"><code>realtek,bee-counter-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek Bee实时时钟（RTC）计数器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L367">已禁用：1</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P010_realtek_bee-counter-rtc.md#std-dtcompatible-realtek-bee-counter-rtc"><code>realtek,bee-counter-rtc</code></a></td>
</tr>
<tr>
<td rowspan="2">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee系列AES硬件加速器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L383">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P007_realtek_bee-aes.md#std-dtcompatible-realtek-bee-aes"><code>realtek,bee-aes</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek Bee系列SHA-256硬件加速器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L389">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P008_realtek_bee-sha256.md#std-dtcompatible-realtek-bee-sha256"><code>realtek,bee-sha256</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Bee直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L401">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P011_realtek_bee-dma.md#std-dtcompatible-realtek-bee-dma"><code>realtek,bee-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee NOR闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L113">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P023_realtek_bee-nor-flash-controller.md#std-dtcompatible-realtek-bee-nor-flash-controller"><code>realtek,bee-nor-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Bee通用输入输出（GPIO）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L180">已启用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P011_realtek_bee-gpio.md#std-dtcompatible-realtek-bee-gpio"><code>realtek,bee-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Bee I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L345">已禁用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P010_realtek_bee-i2c.md#std-dtcompatible-realtek-bee-i2c"><code>realtek,bee-i2c</code></a></td>
</tr>
<tr>
<td rowspan="2">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>Bee按键扫描（Keyscan）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L337">已禁用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P016_realtek_bee-keyscan.md#std-dtcompatible-realtek-bee-keyscan"><code>realtek,bee-keyscan</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/realtek/rtl8752h_evb/rtl8752h_evb_common.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/realtek/rtl8752h_evb/rtl8752h_evb_common.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L121">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P008_realtek_bee-nor-flash.md#std-dtcompatible-realtek-bee-nor-flash"><code>realtek,bee-nor-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Bee引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L175">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P003_realtek_bee-pinctrl.md#std-dtcompatible-realtek-bee-pinctrl"><code>realtek,bee-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee定时器，用作脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L234">已禁用：6</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P016_realtek_bee-pwm.md#std-dtcompatible-realtek-bee-pwm"><code>realtek,bee-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L395">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P003_realtek_bee-trng.md#std-dtcompatible-realtek-bee-trng"><code>realtek,bee-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>Bee基本正交解码器（QDEC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L375">已禁用：1</a>）</td>
<td><a href="../sensor_realtek_rohm_sensirion_binding_reference/P005_realtek_bee-basic-qdec.md#std-dtcompatible-realtek-bee-basic-qdec"><code>realtek,bee-basic-qdec</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Bee通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L213">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L196">已禁用：2</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P004_realtek_bee-uart.md#std-dtcompatible-realtek-bee-uart"><code>realtek,bee-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Bee串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L412">已禁用：3</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P012_realtek_bee-spi.md#std-dtcompatible-realtek-bee-spi"><code>realtek,bee-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L73">已启用：5</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek Bee定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L222">已禁用：6</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P011_realtek_bee-timer.md#std-dtcompatible-realtek-bee-timer"><code>realtek,bee-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Realtek Bee内核看门狗定时器（Core Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/bee/rtl8752h.dtsi?plain=1#L190">已禁用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P002_realtek_bee-core-wdt.md#std-dtcompatible-realtek-bee-core-wdt"><code>realtek,bee-core-wdt</code></a></td>
</tr>
</table>

<a id="prerequisites"></a>

## 前置条件（Prerequisites）

运行应用前，必须将Realtek提供的特定镜像编程到设备。运行以下命令获取这些镜像：

```text
$ west blobs fetch hal_realtek --allow-regex 'bee/rtl8752h/.*'
```

这些镜像需使用mpcli下载。mpcli用法及开发板进入下载模式的方法见“使用MPCli”。（[使用MPCli（Using MPCli）](#using-mpcli)）

```text
west flash --port /dev/ttyX --mp-json <zephyr workspace>/modules/hal/realtek/bee/tools/mpcli/configs/rtl8752h_essential_images.json
```

<a id="flashing"></a>

## 烧录（Flashing）

`rtl8752h_evb`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-mpcli"><code>mpcli</code></a></td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-rtkprog">rtkprog</a></td>
<td>✅</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

<a id="using-mpcli"></a>

<a id="id1"></a>

### 使用MPCli（Using MPCli）

MPCli是RTL8752H评估板的默认烧录运行工具（Flash Runner），通过UART接口烧录。板载FT232RL USB转UART转换器可直接用于烧录及日志输出。请按Realtek Bee Flash Programmer（MPCli）说明设置MPCli。（[Realtek Bee闪存编程工具（MPCli）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-mpcli)）

![官方原图：rtl8752h_evb_download_mode](images/rtl8752h_evb_download_mode.webp)


1. 用线缆将开发板USB端口CON1连接电脑。
2. 用跳线将P3_0连接RX，P3_1连接TX。
3. 用杜邦线将P0_3（LOG）拉低。
4. 复位开发板以进入下载模式。

```text
west build -b rtl8752h_evb/rtl8752hkf samples/hello_world
west flash --port /dev/ttyX
```

下载后将P0_3（LOG）恢复为悬空（Floating），再复位开发板运行应用。

注意（Note）

west flash默认从包含build目录的根目录执行；若在其他目录运行，需要用--build-dir或-d指定构建目录。

<a id="using-j-link"></a>

### 使用J-Link

<a id="id8"></a>

也可通过--runner或-r选项选择J-Link烧录。J-Link配置方法见[J-Link设置指南](https://github.com/rtkconnectivity/realtek-zephyr-project/wiki/J%E2%80%90Link-Setup-Guide)[注3](#id7)。

```text
west build -b rtl8752h_evb/rtl8752hkf samples/hello_world
west flash -r jlink
```

<a id="visualizing-the-message"></a>

## 查看输出消息（Visualizing the Message）

查看日志时按以下步骤操作：


1. 连接UART：

  > - 连接板上USB端口CON1。
  > - 用跳线将P3_0连接RX，P3_1连接TX；此UART接口与[MPCli](#using-mpcli)使用的接口相同。
2. 打开熟悉的串行通信工具：

  > - 将波特率设为115200。
3. 按复位键：

  > - 应在终端中看到Hello World! rtl8752h_evb/rtl8752hkf。

<a id="debugging"></a>

## 调试（Debugging）

<a id="id9"></a>

首先按[J-Link设置指南](https://github.com/rtkconnectivity/realtek-zephyr-project/wiki/J%E2%80%90Link-Setup-Guide)[注3](#id7)配置J-Link，之后即可按常规方式调试应用。

```text
# From the root of the zephyr repository
west build -b rtl8752h_evb/rtl8752hkf samples/hello_world
west debug -r jlink
```

<a id="references"></a>

## 参考资料（References）

<a id="id3"></a>

〔[1](#id4)〕 [https://www.realmcu.com/en/Home/Products/RTL8752H-Series](https://www.realmcu.com/en/Home/Products/RTL8752H-Series)

<a id="id5"></a>

〔[2](#id6)〕 [https://docs.realmcu.com/sdk/rtl8752h/common/en/latest/evb_guide/text_en/README.html](https://docs.realmcu.com/sdk/rtl8752h/common/en/latest/evb_guide/text_en/README.html)

<a id="id7"></a>

〔3〕 ([1](#id8),[2](#id9)) [https://github.com/rtkconnectivity/realtek-zephyr-project/wiki/J%E2%80%90Link-Setup-Guide](https://github.com/rtkconnectivity/realtek-zephyr-project/wiki/J%E2%80%90Link-Setup-Guide)

## 译注

RTL8752H需先获取并写入厂商必要镜像。P0_3（LOG）拉低后复位进入下载，完成后恢复悬空再复位；MPCli与日志共用串口。各子板闪存容量不同。

---

[上一章](P005_RTL8721Dx_Evaluation_Board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_RTL87x2G_Model_A_Evaluation_Board.md)
