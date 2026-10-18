---
id: learning.zephyr-docs.boards-01space-96boards.page-4
title: Argonkey
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/96boards/argonkey/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="96b_argonkey"></a>

# 第4章\_Argonkey

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/96boards/argonkey/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/96b_argonkey.jpg](images/96b_argonkey.jpg)](images/96b_argonkey.jpg)

Argonkey

名称（Name）：

`96b_argonkey`

厂商（Vendor）：

[96Boards](https://docs.zephyrproject.org/latest/boards/index.html#vendor=96boards)

状态（Status）：

未处于积极维护状态（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[stm32f412cx](https://docs.zephyrproject.org/latest/boards/index.html#soc=stm32f412cx)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/96boards/argonkey/doc/index.rst/../..)<a id="boards-argonkey"></a>

## 96Boards Argonkey

<a id="overview"></a>

### 概述（Overview）

96Boards Argonkey 基于 STMicroelectronics STM32F412CG Cortex-M4 CPU。

该板可作为全部符合 96Boards 标准系列产品的传感器集线器（Sensor Hub）平台，也可独立使用。

<a id="id2"></a>

![官方原图：96Boards Argonkey](images/96b_argonkey1.jpg)

96Boards Argonkey

<a id="hardware"></a>

### 硬件（Hardware）

96Boards Argonkey 提供以下硬件：


- UFQFPN48 封装的 STM32F412CG。
- 带浮点单元（FPU）的 ARM 32 位 Cortex-M4 CPU。
- CPU 最高频率 100 MHz。
- 工作电压 1.8 V。
- 1024 KB 闪存（Flash）。
- 256 KB 静态随机存储器（SRAM）。
- 板载传感器（Onboard Sensors）：


  - 湿度（Humidity）：STMicro HTS221。
  - 温度／压力（Temperature/Pressure）：STMicro LPS22HB。
  - 环境光感测（ALS）：Intersil ISL29034。
  - 接近感测（Proximity）：STMicro VL53L0X。
  - 加速度计／陀螺仪（Accelerometer/Gyroscope）：STMicro LSM6DSL。
  - 地磁（Geomagnetic）：STMicro LIS2MDL。
  - AMR 霍尔传感器（AMR Hall Sensor）：MRMS501A，沿用原文名称。
  - 麦克风（Microphone）：STMicro MP34DT05。
- 两个用户 LED。
- 16 个通用 LED。
- 支持外部中断（External Interrupt）的 GPIO。
- 通用异步收发器（UART）
- 3 个 I2C。
- 1 个 SPI。
- 1 个 I2S。

<a id="supported-features"></a>

#### 支持的功能（Supported Features）

`96b_argonkey` 开发板支持下列硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

`2 / 2`

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="96b_argonkey-hw-features"></a>

<a id="96b_argonkey-96b_argonkey/stm32f412cx-hw-features-section"></a>

##### `96b_argonkey/stm32f412cx` 目标（Target）

<a id="96b_argonkey-96b_argonkey/stm32f412cx-hw-features-panel"></a>

<a id="96b_argonkey-96b_argonkey/stm32f412cx-hw-features-memory"></a>

此开发板目标可用存储器：256 KiB RAM、1 MiB 闪存。

<a id="96b_argonkey-96b_argonkey/stm32f412cx-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>STM32F4 模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L611">已禁用：1</a>）</td>
<td><a href="../hardware/P841_STM32F4模数转换器绑定.md#dtbinding-st-stm32f4-adc"><code>st,stm32f4-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>板载（On-Board）</td>
<td>STMicroelectronics MPXXDTYY 数字脉冲密度调制麦克风系列（Digital PDM Microphone Family）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/96boards/argonkey/96b_argonkey.dts?plain=1#L137">已启用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P017_st_mpxxdtyy-i2s.md#std-dtcompatible-st-mpxxdtyy"><code>st,mpxxdtyy</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>STM32 CAN 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f412.dtsi?plain=1#L237">已禁用：2</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P011_st_stm32-bxcan.md#std-dtcompatible-st-stm32-bxcan"><code>st,stm32-bxcan</code></a></td>
</tr>
<tr>
<td rowspan="6">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>STM32F4 复位与时钟控制器（Reset and Clock Controller，RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L178">已启用：1</a>）</td>
<td><a href="../timer_reference/P127_STM32F4复位与时钟控制绑定.md#dtbinding-st-stm32f4-rcc"><code>st,stm32f4-rcc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 外部高速时钟（HSE Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L63">已启用：1</a>）</td>
<td><a href="../timer_reference/P129_STM32高速外部时钟绑定.md#dtbinding-st-stm32-hse-clock"><code>st,stm32-hse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L83">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L69">已禁用：2</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32F2、STM32F4、STM32F7 的锁相环节点绑定（PLL Node Binding）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L90">已启用：2</a>）</td>
<td><a href="../timer_reference/P128_STM32Fx锁相环时钟绑定.md#dtbinding-st-stm32fx-pll-clock"><code>st,stm32fx-pll-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 时钟多路复用器（Clock Multiplexer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f412.dtsi?plain=1#L20">已禁用：1</a>）</td>
<td><a href="../timer_reference/P133_STM32时钟多路复用绑定.md#dtbinding-st-stm32-clock-mux"><code>st,stm32-clock-mux</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 微控制器时钟输出（Microcontroller Clock Output，MCO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L98">已禁用：2</a>）</td>
<td><a href="../timer_reference/P134_STM32时钟输出绑定.md#dtbinding-st-stm32-clock-mco"><code>st,stm32-clock-mco</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>STM32 计数器（Counters）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L396">已禁用：14</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P007_st_stm32-counter.md#std-dtcompatible-st-stm32-counter"><code>st,stm32-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>STM32 DMA 控制器（Controller，V1）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L645">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L636">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P007_st_stm32-dma-v1.md#std-dtcompatible-st-stm32-dma-v1"><code>st,stm32-dma-v1</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 系列闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L112">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P011_st_stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller"><code>st,stm32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用输入输出控制器（GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L212">已启用：8</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P029_st_stm32-gpio.md#std-dtcompatible-st-stm32-gpio"><code>st,stm32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>STM32 I2C V1 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L318">已启用：3</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P007_st_stm32-i2c-v1.md#std-dtcompatible-st-stm32-i2c-v1"><code>st,stm32-i2c-v1</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>STM32 I2S 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f410.dtsi?plain=1#L66">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f410.dtsi?plain=1#L40">已禁用：3</a>）</td>
<td><a href="../i2s_binding_reference/P016_st_stm32-i2s.md#std-dtcompatible-st-stm32-i2s"><code>st,stm32-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/96boards/argonkey/96b_argonkey.dts?plain=1#L37">已启用：1</a>）</td>
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
<td>STM32 外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L189">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P001_st_stm32-exti.md#std-dtcompatible-st-stm32-exti"><code>st,stm32-exti</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>TI LP3943 LED 控制器。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/96boards/argonkey/96b_argonkey.dts?plain=1#L185">已启用：1</a>）</td>
<td><a href="../led_sct_ti_xpowers_binding_reference/P002_ti_lp3943.md#std-dtcompatible-ti-lp3943"><code>ti,lp3943</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/96boards/argonkey/96b_argonkey.dts?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 电池备份 RAM（Battery-Backed RAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L604">已禁用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P010_st_stm32-bbram.md#std-dtcompatible-st-stm32-bbram"><code>st,stm32-bbram</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>STM32F4 闪存（Flash Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L121">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P017_st_stm32f4-nv-flash.md#std-dtcompatible-st-stm32f4-nv-flash"><code>st,stm32f4-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">非易失存储器（NVMEM）</td>
<td>片上（On-Chip）</td>
<td>非易失存储器固定布局（Fixed Layout for Non-Volatile Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L152">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P009_fixed-layout.md#std-dtcompatible-fixed-layout"><code>fixed-layout</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>STM32 嵌入式非易失一次性可编程存储器（NVM OTP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L148">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L131">已禁用：1</a>）</td>
<td><a href="../otp_binding_reference/P010_st_stm32-nvm-otp.md#std-dtcompatible-st-stm32-nvm-otp"><code>st,stm32-nvm-otp</code></a></td>
</tr>
<tr>
<td rowspan="1">物理层（PHY）</td>
<td>片上（On-Chip）</td>
<td>用于所有内置于 USB IP 的 USB 收发器（USB Transceivers）的绑定。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L711">已启用：1</a>）</td>
<td><a href="../phy_binding_reference/P008_usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv"><code>usb-nop-xceiv</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>STM32 引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L205">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P004_st_stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl"><code>st,stm32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>STM32 电源控制器（Power Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L665">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P010_st_stm32-pwr.md#std-dtcompatible-st-stm32-pwr"><code>st,stm32-pwr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32F1 风格的唤醒引脚控制器（Wake-Up Pins Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L669">已禁用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P011_st_stm32f1-pwr-wkupctrl.md#std-dtcompatible-st-stm32f1-pwr-wkupctrl"><code>st,stm32f1-pwr-wkupctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>STM32 脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L390">已禁用：12</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P011_st_stm32-pwm.md#std-dtcompatible-st-stm32-pwm"><code>st,stm32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">四线串行外设接口（QSPI）</td>
<td>片上（On-Chip）</td>
<td>STM32 四线串行外设接口控制器（QSPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f412.dtsi?plain=1#L227">已禁用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P011_st_stm32-qspi.md#std-dtcompatible-st-stm32-qspi"><code>st,stm32-qspi</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 复位与时钟控制器（Reset and Clock Control，RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L183">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P017_st_stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl"><code>st,stm32-rcc-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>STM32 随机数生成器（Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f412.dtsi?plain=1#L210">已禁用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P016_st_stm32-rng.md#std-dtcompatible-st-stm32-rng"><code>st,stm32-rng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>STM32 实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L593">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P014_st_stm32-rtc.md#std-dtcompatible-st-stm32-rtc"><code>st,stm32-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>STM32 SDMMC 主机控制器（Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L655">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P019_st_stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc"><code>st,stm32-sdmmc</code></a></td>
</tr>
<tr>
<td rowspan="8">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>I2C 总线上的 STMicroelectronics HTS221 温湿度传感器（Humidity and Temperature Sensor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/96boards/argonkey/96b_argonkey.dts?plain=1#L160">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P069_st_hts221.md#std-dtcompatible-st-hts221"><code>st,hts221</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>STMicroelectronics LPS22HB 压力传感器（Pressure Sensor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/96boards/argonkey/96b_argonkey.dts?plain=1#L166">已启用：1</a>）</td>
<td><a href="../sensor_st_lis_lps_binding_reference/P021_st_lps22hb-press.md#std-dtcompatible-st-lps22hb-press"><code>st,lps22hb-press</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>STMicroelectronics VL53L0X 飞行时间传感器（Time of Flight Sensor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/96boards/argonkey/96b_argonkey.dts?plain=1#L171">已启用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P007_st_vl53l0x.md#std-dtcompatible-st-vl53l0x"><code>st,vl53l0x</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 正交解码器（Quadrature Decoder）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L401">已禁用：6</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P028_st_stm32-qdec.md#std-dtcompatible-st-stm32-qdec"><code>st,stm32-qdec</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通过 SPI 总线访问的 STMicroelectronics LSM6DSL 六轴加速度计与陀螺仪（6-Axis Accelerometer and Gyrometer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/96boards/argonkey/96b_argonkey.dts?plain=1#L120">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P090_st_lsm6dsl.md#std-dtcompatible-st-lsm6dsl"><code>st,lsm6dsl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系列温度节点（TEMP），用于以两个温度点完成生产校准的传感器。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L685">已禁用：1</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P029_st_stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal"><code>st,stm32-temp-cal</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 参考电压（VREF+）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L696">已禁用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P003_st_stm32-vref.md#std-dtcompatible-st-stm32-vref"><code>st,stm32-vref</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 电池电压（VBAT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L704">已禁用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P001_st_stm32-vbat.md#std-dtcompatible-st-stm32-vbat"><code>st,stm32-vbat</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L291">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L300">已禁用：3</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P016_st_stm32-usart.md#std-dtcompatible-st-stm32-usart"><code>st,stm32-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">系统管理总线（SMbus）</td>
<td>片上（On-Chip）</td>
<td>STM32 系统管理总线控制器（SMBus Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L716">已禁用：3</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P013_st_stm32-smbus.md#std-dtcompatible-st-stm32-smbus"><code>st,stm32-smbus</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>STM32 串行外设接口控制器（SPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L354">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f410.dtsi?plain=1#L29">已禁用：3</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P012_st_stm32-spi.md#std-dtcompatible-st-stm32-spi"><code>st,stm32-spi</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 定时器（Timers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L379">已禁用：14</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P008_st_stm32-timers.md#std-dtcompatible-st-stm32-timers"><code>st,stm32-timers</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>STM32 全速 USB OTG 控制器（OTGFS Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L365">已禁用：1</a>）</td>
<td><a href="../usb_stm32_audio_binding_reference/P004_st_stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs"><code>st,stm32-otgfs</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>STM32 看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L277">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P001_st_stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog"><code>st,stm32-watchdog</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系统窗口看门狗（System Window Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L283">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P002_st_stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog"><code>st,stm32-window-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

#### 连接与输入输出（Connections and IOs）

<a id="led"></a>

##### 发光二极管（LED）


- LED1／用户 LED1 = PB2。
- LED2／用户 LED2 = PC13。

<a id="push-buttons"></a>

##### 按键（Push Buttons）


- 按钮 = 复位 RST（BT1）。
- 按钮 = 用户 USR（BT2）。

<a id="system-clock"></a>

#### 系统时钟（System Clock）

96Boards Argonkey 可由内部振荡器或主锁相环（PLL）时钟驱动。默认配置使用 16 MHz 外部振荡器驱动主 PLL，生成 84 MHz 系统时钟（SYSCLK）。总线侧 AHB 为 84 MHz，APB1/APB2 为 42 MHz。

<a id="serial-port"></a>

#### 串口（Serial Port）

96Boards Argonkey 的 Zephyr 控制台输出分配给 USART1，默认配置为 115200、8N1。

<a id="i2c"></a>

##### 集成电路间总线（I2C）

96Boards Argonkey 最多有 3 个 I2C，默认引脚映射为：


- `I2C1_SCL : PB6`
- `I2C1_SDA : PB7`
- `I2C2_SCL : PB10`
- `I2C2_SDA : PB9`
- `I2C3_SCL : PA8`
- `I2C3_SCL : PB4`

I2C3 接到 P2 接插件，可连接外部传感器，最高速率 100 kbit/s。

<a id="spi"></a>

##### 串行外设接口（SPI）

96Boards Argonkey 有 2 个 SPI。SPI1 作为从机，与应用处理器（AP）通信；SPI2 作为主机，控制 LSM6DSL 传感器。默认引脚映射为：


- `SPI1_NSS : PA4`
- `SPI1_SCK : PA5`
- `SPI1_MISO : PA6`
- `SPI1_MOSI : PA7`
- `SPI2_NSS : PB12`
- `SPI2_SCK : PB13`
- `SPI2_MISO : PB14`
- `SPI2_MOSI : PB15`

<a id="programming-and-debugging"></a>

### 烧录与调试（Programming and Debugging）

<a id="building"></a>

#### 构建（Building）

以下以构建 [Hello World](../getting_started/P005_HelloWorld示例.md#hello_world) 应用为例。

```text
# From the root of the zephyr repository
west build -b 96b_argonkey samples/hello_world
```

<a id="flashing"></a>

#### 烧录（Flashing）

96Boards Argonkey 有两种烧录方式：ROM 引导加载程序和 SWD 调试端口，后者需要附加硬件。

<a id="id4"></a>

ROM 引导加载程序要求特定激活方式，可通过 BOOT0 引脚触发；它支持 USB（DFU）、UART、I2C 和 SPI 烧录，但本页只介绍 UART。启用和使用方法见应用笔记 [AN2606](https://www.st.com/resource/en/application_note/cd00167594.pdf) [注1](#id3)。

<a id="using-rom-bootloader"></a>

##### 使用 ROM 引导加载程序（ROM Bootloader）：

下面介绍在 Linux PC 上通过 UART 为 ArgonKey 烧录固件的基本步骤。


1. <a id="id10"></a>

  将 ArgonKey UART 连接到 Linux PC，例如使用 USB-TTL 串口线。原文烧录流程使用带 FTDI 芯片的 [TTL-232RG](http://www.ftdichip.com/Support/Documents/DataSheets/Cables/DS_TTL-232RG_CABLES.pdf) [注4](#id9) 线缆测试。ArgonKey UART 引脚位于开发板背面的 P3 低速扩展接插件。


  - GND（黑色）连接 ArgonKey GND（P3.1）。
  - TXD（橙色）连接 ArgonKey UART0_TXD（P3.5）。
  - RXD（黄色）连接 ArgonKey UART0_RXD（P3.7）。

  将 USB 线插入 Linux PC 后会生成设备 `/dev/ttyUSBx`，其中 x 通常为 0。
2. 强制 STM32F412CG 进入引导加载程序模式（Bootloader Mode）。


  - 将 BOOT0 接到 1V8，即连接 P2.1 和 P3.30。
  - 按下并松开 RST 按钮。
3. 使用 stm32flash 工具烧录 ArgonKey：

```text
$ stm32flash  -w zephyr.bin -v -g 0x08000000 /dev/ttyUSB0
```

<a id="id6"></a>

[stm32flash](https://sourceforge.net/p/stm32flash/wiki/Home/) [注2](#id5) 的更多信息见参考资料部分。

<a id="using-swd-debugger"></a>

##### 使用 SWD 调试器（SWD Debugger）：

选择商用 JTAG/SWD 硬件工具，连接到 ArgonKey 的 P4 接插件。

<a id="id8"></a>

原文称 ArgonKey 已使用 [ST-LINK/V2](https://www.st.com/en/development-tools/st-link-v2.html) [注3](#id7) 工具测试。该工具通过 USB 接到 PC 后呈现为具有大容量存储功能的 USB 复合设备；在 Linux 中挂载后，可将固件复制到该设备，由 ST-LINK 自动烧录到 ArgonKey。

示例（Example）：

```text
$ mount /dev/sdb /mnt
$ cp zephyr.bin /mnt
$ umount /mnt
```

<a id="debugging"></a>

#### 调试（Debugging）

<a id="references"></a>

### 参考资料（References）

<a id="id3"></a>

〔[1](#id4)〕 [https://www.st.com/resource/en/application_note/cd00167594.pdf](https://www.st.com/resource/en/application_note/cd00167594.pdf)

<a id="id5"></a>

〔[2](#id6)〕 [https://sourceforge.net/p/stm32flash/wiki/Home/](https://sourceforge.net/p/stm32flash/wiki/Home/)

<a id="id7"></a>

〔[3](#id8)〕 [https://www.st.com/en/development-tools/st-link-v2.html](https://www.st.com/en/development-tools/st-link-v2.html)

<a id="id9"></a>

〔[4](#id10)〕 [http://www.ftdichip.com/Support/Documents/DataSheets/Cables/DS_TTL-232RG_CABLES.pdf](http://www.ftdichip.com/Support/Documents/DataSheets/Cables/DS_TTL-232RG_CABLES.pdf)

## 译注

原文I2C3的PA8、PB4两行均标作SCL，且串口线缆示例写作TXD接TXD、RXD接RXD；此处保留原始标注。ST-LINK/V2的大容量存储烧录描述也为官方原文，不表示本文进行了硬件验证。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [DS_TTL-232RG_CABLES.pdf](http://www.ftdichip.com/Support/Documents/DataSheets/Cables/DS_TTL-232RG_CABLES.pdf)：HTTP Error 403: Forbidden。
- [](https://sourceforge.net/p/stm32flash/wiki/Home/)：HTTP Error 403: Forbidden。
- [st-link-v2.html](https://www.st.com/en/development-tools/st-link-v2.html)：HTTP Error 567: Unknown Status。
- [cd00167594.pdf](https://www.st.com/resource/en/application_note/cd00167594.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P003_Aerocore2.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_Avenger96.md)
