---
id: learning.zephyr-docs.boards-gd-to-iar.page-9
title: GD32F450I-EVAL
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/gd/gd32f450i_eval/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="gd32f450i_eval"></a>

# 第9章\_GD32F450I-EVAL

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/gd/gd32f450i_eval/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/gd32f450i_eval.webp](images/gd32f450i_eval.webp)](images/gd32f450i_eval.webp)

GD32F450I-EVAL

名称（Name）：

`gd32f450i_eval`

厂商（Vendor）：

[兆易创新半导体（GigaDevice Semiconductor）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=gd)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[gd32f450](https://docs.zephyrproject.org/latest/boards/index.html#soc=gd32f450)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32f450i_eval/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

GD32F450I-EVAL是用于GD32F450IK Cortex-M4F拓展性能微控制器（Stretch Performance MCU）原型开发的硬件平台。

GD32F450IK采用单核Arm Cortex-M4F MCU，最高200 MHz，支持闪存零等待状态（Zero Wait States）访问，提供3072kiB Flash、256kiB SRAM及140个GPIO。

<a id="hardware"></a>

## 硬件（Hardware）


- GD32F450IKT6微控制器（MCU）
- AT24C02C 2 Kb EEPROM
- GD25Q32C 16 Mbit SPI及QSPI NOR闪存，容量按原文保留
- GD9FS1G8F2A 1 Gbit NAND闪存
- Micron MT48LC16M16A2P-6AIT 256 Mbit同步动态随机存储器（SDRAM）
- 3个用户LED
- 3个用户按键
- 1路USART，J1连接器上的RS232接口
- 1个接到ADC输入的电位器（POT）
- 耳机接口（Headphone Interface）
- Micro SD卡接口
- USB全速（FS）接口
- 高速USB连接器（USB HS）
- 1路CAN
- 以太网接口（Ethernet Interface）
- 3.5英寸RGB LCD，320 × 480
- OV2640数字摄像头（Digital Camera）
- 板载GD-Link编程器（Programmer）
- J-Link／JTAG连接器

GD32F450 SoC及GD32F450I-EVAL开发板更多信息见：


- [兆易创新Cortex-M4F拓展性能SoC网站（Stretch Performance SoC Website）](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m4/stretch-performance-line/)
- [GD32F450xx数据手册（Datasheet）](https://www.gd32mcu.com/data/documents/datasheet/GD32F450xx_Datasheet_Rev2.3.pdf)
- [GD32F4xx用户手册（User Manual）](https://www.gd32mcu.com/data/documents/userManual/GD32F4xx_User_Manual_Rev3.0.pdf)
- [GD32F450I-EVAL用户手册（User Manual）](http://www.gd32mcu.com/download/down/document_id/120/path_type/1)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`gd32f450i_eval`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="gd32f450i_eval-hw-features"></a>

<a id="gd32f450i_eval-gd32f450i_eval/gd32f450-hw-features-section"></a>

#### `gd32f450i_eval/gd32f450`目标（Target）

<a id="gd32f450i_eval-gd32f450i_eval/gd32f450-hw-features-panel"></a>

<a id="gd32f450i_eval-gd32f450i_eval/gd32f450-hw-features-memory"></a>

该开发板目标的片上存储容量：192 KiB RAM、3 MiB Flash。

<a id="gd32f450i_eval-gd32f450i_eval/gd32f450-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L269">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L280">已禁用：2</a>）</td>
<td><a href="../hardware/P844_GD32模数转换器绑定.md#dtbinding-gd-gd32-adc"><code>gd,gd32-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>兆易创新复位与时钟单元（RCU）时钟控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L77">已启用：1</a>）</td>
<td><a href="../timer_reference/P184_GD32时钟控制绑定.md#dtbinding-gd-gd32-cctl"><code>gd,gd32-cctl</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L452">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L434">已禁用：13</a>）</td>
<td><a href="../counter_binding_reference/P018_gd_gd32-timer.md#std-dtcompatible-gd-gd32-timer"><code>gd,gd32-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32系列数模转换器（DAC）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L187">已启用：1</a>）</td>
<td><a href="../hardware/P761_GD32数模转换器绑定.md#dtbinding-gd-gd32-dac"><code>gd,gd32-dac</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>带先进先出缓冲区（FIFO）的GD32 DMA控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L677">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L664">已禁用：1</a>）</td>
<td><a href="../dma_binding_reference/P016_gd_gd32-dma-v1.md#std-dtcompatible-gd-gd32-dma-v1"><code>gd,gd32-dma-v1</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>GD32闪存控制器（FMC）有三种类型（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L90">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P013_gd_gd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller"><code>gd,gd32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>GD32通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L343">已启用：7</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L373">已禁用：2</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P027_gd_gd32-gpio.md#std-dtcompatible-gd-gd32-gpio"><code>gd,gd32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32 I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L197">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L210">已禁用：2</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P020_gd_gd32-i2c.md#std-dtcompatible-gd-gd32-i2c"><code>gd,gd32-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f450i_eval/gd32f450i_eval.dts?plain=1#L44">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>兆易创新外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L308">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P007_gd_gd32-exti.md#std-dtcompatible-gd-gd32-exti"><code>gd,gd32-exti</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f450i_eval/gd32f450i_eval.dts?plain=1#L25">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f450i_eval/gd32f450i_eval.dts?plain=1#L66">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>兆易创新复位与时钟单元（RCU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../hardware/P705_GD32复位与时钟单元绑定.md#dtbinding-gd-gd32-rcu"><code>gd,gd32-rcu</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32系统配置寄存器（System Configuration Registers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L302">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P009_gd_gd32-syscfg.md#std-dtcompatible-gd-gd32-syscfg"><code>gd,gd32-syscfg</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="3">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>GD32 FMC v3的闪存绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L98">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P018_gd_gd32-nv-flash-v3.md#std-dtcompatible-gd-gd32-nv-flash-v3"><code>gd,gd32-nv-flash-v3</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>兼容Atmel AT24系列的I2C电可擦除可编程只读存储器（EEPROM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f450i_eval/gd32f450i_eval.dts?plain=1#L147">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P004_atmel_at24.md#std-dtcompatible-atmel-at24"><code>atmel,at24</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>这些属性用于支持Zephyr的<code>spi-nor</code>闪存驱动通过Zephyr SPI API，使用基于M25P80的标准命令集控制串行闪存（Serial Flash Memory）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f450i_eval/gd32f450i_eval.dts?plain=1#L170">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor"><code>jedec,spi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>GD32引脚控制器，复用功能模型（AF Model）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L336">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P024_gd_gd32-pinctrl-af.md#std-dtcompatible-gd-gd32-pinctrl-af"><code>gd,gd32-pinctrl-af</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L463">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L445">已禁用：11</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P018_gd_gd32-pwm.md#std-dtcompatible-gd-gd32-pwm"><code>gd,gd32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>GD32备份SRAM低压差稳压器（BLDO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L39">已禁用：1</a>）</td>
<td><a href="../hardware/P637_GD32备份低压差稳压器绑定.md#dtbinding-gd-gd32-bldo"><code>gd,gd32-bldo</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>兆易创新RCU复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L83">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P003_gd_gd32-rctl.md#std-dtcompatible-gd-gd32-rctl"><code>gd,gd32-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">保持存储器（Retained Memory）</td>
<td>片上（On-Chip）</td>
<td>GD32备份SRAM保持存储器（Retained Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L63">已禁用：1</a>）</td>
<td><a href="../hardware/P625_GD32备份SRAM绑定.md#dtbinding-gd-gd32-backup-sram"><code>gd,gd32-backup-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32真随机数发生器（TRNG / True Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L107">已禁用：1</a>）</td>
<td><a href="../rng_binding_reference/P008_gd_gd32-trng.md#std-dtcompatible-gd-gd32-trng"><code>gd,gd32-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>兆易创新通用同步异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L115">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L124">已禁用：7</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P006_gd_gd32-usart.md#std-dtcompatible-gd-gd32-usart"><code>gd,gd32-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32 SPI（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f450.dtsi?plain=1#L38">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L236">已禁用：5</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P016_gd_gd32-spi.md#std-dtcompatible-gd-gd32-spi"><code>gd,gd32-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>GD32独立看门狗定时器（Free Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L321">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P015_gd_gd32-fwdgt.md#std-dtcompatible-gd-gd32-fwdgt"><code>gd,gd32-fwdgt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>GD32窗口看门狗定时器（Window Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f4xx/gd32f4xx.dtsi?plain=1#L327">已禁用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P016_gd_gd32-wwdgt.md#std-dtcompatible-gd-gd32-wwdgt"><code>gd,gd32-wwdgt</code></a></td>
</tr>
</table>

<a id="serial-port"></a>

### 串口（Serial Port）

GD32F450I-EVAL有一个串行通信端口，默认USART0的TX接PA9、RX接PA10。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`gd32f450i_eval`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>调试服务器（debugserver）</th>
<th>复位（reset）</th>
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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
</table>

编程前，按以下要求设置启动和串口跳线：


- J2／3：均选择2–3位置，从用户存储器启动
- J5：选择1–2位置，标为USART0

<a id="using-gd-link"></a>

### 使用GD-Link

GD32F450I-EVAL带有板载GD-Link编程器／调试器，可通过USB烧录和调试。另有JTAG排针J1，可配合Segger J-Link等工具使用。


1. 构建Zephyr内核和[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例应用：

  ```text
  west build -b gd32f450i_eval samples/hello_world
  ```
2. 启动串口终端监听输出。在Linux下，设备名通常类似`/dev/ttyUSB0`。例如：

  ```text
  minicom -D /dev/ttyUSB0 -o
  ```

  `-o`选项让`minicom`不发送调制解调器初始化字符串（Modem Initialization String）。连接参数应配置如下：

  > - 速率（Speed）：115200波特率
  > - 数据位（Data）：8位
  > - 奇偶校验（Parity）：无（None）
  > - 停止位（Stop Bits）：1位
3. 烧录镜像：

  ```text
  west build -b gd32f450i_eval samples/hello_world
  west flash
  ```

  终端应显示“Hello World! gd32f450i_eval”。
4. 调试镜像的方法：

  ```text
  west build -b gd32f450i_eval samples/hello_world
  west debug
  ```

## 译注

原文GD25Q32C容量写16Mbit；不依据型号名称推断并静默改写容量。

---

[上一章](P008_GD32F407V-START.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_GD32F450V-START.md)
