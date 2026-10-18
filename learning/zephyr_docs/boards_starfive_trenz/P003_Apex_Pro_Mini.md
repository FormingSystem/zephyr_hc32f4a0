---
id: learning.zephyr-docs.boards-starfive-trenz.page-3
title: Apex Pro Mini
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/steelseries/apex_pro_mini/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="apex_pro_mini"></a>

# 第3章\_Apex Pro Mini

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/steelseries/apex_pro_mini/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/apex_pro_mini.webp](images/apex_pro_mini.webp)](images/apex_pro_mini.webp)

Apex Pro Mini

名称（Name）：

`apex_pro_mini`

厂商（Vendor）：

[SteelSeries](https://docs.zephyrproject.org/latest/boards/index.html#vendor=steelseries)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[stm32l412xx](https://docs.zephyrproject.org/latest/boards/index.html#soc=stm32l412xx)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/steelseries/apex_pro_mini/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

SteelSeries Apex Pro Mini是一款采用STM32L412RB Arm Cortex-M4微控制器的机械键盘。


- STM32微控制器，LQFP64封装
- 62个按键
- 62个RGB LED
- USB-C端口

包含以下外设：


- Lumissil IS31FL3743B LED驱动器
- 复旦微电子（FMSH）FM25Q128，128 Mbit串行闪存

注意（Note）

此驱动基于法语AZERTY版本开发，该版本ENTER键高2U。QWERTY版为61键而非62键，差别包括：


- ENTER上方增加K29反斜杠键（BACKSLASH）
- 移除K45 SUP，以容纳更宽的左Shift键
- 移除K42 STAR，以容纳ENTER键

<a id="installation"></a>

## 安装（Installation）

空格键下方有2.54 mm通孔SWD排针，可通过ST-LINK或其他兼容STM32的探针编程，引脚见板上丝印：

<table>
<tr>
<td>3V3</td>
<td>串行线调试数据（SWDIO）</td>
<td>串行线时钟（SWCLK）</td>
<td>nRST</td>
<td>地（GND）</td>
</tr>
</table>

要烧录新固件，必须完全擦除出厂固件，以解除STM32L4闪存保护。原文步骤如下：


- 打开STM32CubeProgrammer并连接目标。
- 在选项字节（OB）部分勾选PCROP_RDB；原文在此写作RDB。
- 在PCROP保护中，将PCROP_START设为0xFFFF、PCROP_END设为0x0；结束值小于起始值可禁用保护。
- 在写保护（Write Protection）中，将WRP1A_STRT及WRP1B_STRT设为0x3F，将WRP1A_END及WRP1B_END设为0x0，同样通过结束值小于起始值禁用保护。
- 再到读出保护（Read Out Protection），将BB改为AA。

PCROP只有在ROP值从BB降为AA时才解除。若操作失败，需再次将ROP设为BB，并确认已正确勾选PCROP_RDP；原文此处为RDP，与前述RDB拼写不同。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

注意（Note）

目前尚不支持LED驱动器。

`apex_pro_mini`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="apex_pro_mini-hw-features"></a>

<a id="apex_pro_mini-apex_pro_mini/stm32l412xx-hw-features-section"></a>

#### `apex_pro_mini/stm32l412xx`目标（Target）

<a id="apex_pro_mini-apex_pro_mini/stm32l412xx-hw-features-panel"></a>

<a id="apex_pro_mini-apex_pro_mini/stm32l412xx-hw-features-memory"></a>

此板级目标的片上存储：40 KiB RAM及128 KiB Flash。

<a id="apex_pro_mini-apex_pro_mini/stm32l412xx-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>STM32模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L470">已禁用：1</a>）</td>
<td><a href="../hardware/P839_STM32模数转换器绑定.md#dtbinding-st-stm32-adc"><code>st,stm32-adc</code></a></td>
</tr>
<tr>
<td rowspan="7">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>STM32复位和时钟控制器（RCC / Reset and Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L185">已启用：1</a>）</td>
<td><a href="../timer_reference/P126_STM32复位与时钟控制绑定.md#dtbinding-st-stm32-rcc"><code>st,stm32-rcc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 外部高速时钟（HSE Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L71">已禁用：1</a>）</td>
<td><a href="../timer_reference/P129_STM32高速外部时钟绑定.md#dtbinding-st-stm32-hse-clock"><code>st,stm32-hse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L77">已启用：3</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32多速内部时钟（MSI Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L84">已禁用：1</a>）</td>
<td><a href="../timer_reference/P132_STM32多速内部时钟绑定.md#dtbinding-st-stm32-msi-clock"><code>st,stm32-msi-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低速外部时钟（LSE Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L91">已禁用：1</a>）</td>
<td><a href="../timer_reference/P130_STM32低速外部时钟绑定.md#dtbinding-st-stm32-lse-clock"><code>st,stm32-lse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32L4与L5器件的锁相环节点绑定（PLL Node Binding）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L106">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L112">已禁用：1</a>）</td>
<td><a href="../timer_reference/P148_STM32L4锁相环时钟绑定.md#dtbinding-st-stm32l4-pll-clock"><code>st,stm32l4-pll-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 微控制器时钟输出（Microcontroller Clock Output，MCO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L120">已禁用：1</a>）</td>
<td><a href="../timer_reference/P134_STM32时钟输出绑定.md#dtbinding-st-stm32-clock-mco"><code>st,stm32-clock-mco</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>STM32 计数器（Counters）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L355">已禁用：5</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P007_st_stm32-counter.md#std-dtcompatible-st-stm32-counter"><code>st,stm32-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>STM32 CRC 计算单元（Calculation Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L594">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P011_st_stm32-crc.md#std-dtcompatible-st-stm32-crc"><code>st,stm32-crc</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>STM32直接存储器访问控制器（DMA Controller，V2）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L503">已禁用：2</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P008_st_stm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2"><code>st,stm32-dma-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 系列闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L128">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P011_st_stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller"><code>st,stm32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用输入输出控制器（GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L219">已启用：4</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P029_st_stm32-gpio.md#std-dtcompatible-st-stm32-gpio"><code>st,stm32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>STM32 I2C V2 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L293">已禁用：3</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P008_st_stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2"><code>st,stm32-i2c-v2</code></a></td>
</tr>
<tr>
<td rowspan="2">输入（Input）</td>
<td>板载（On-Board）</td>
<td>基于GPIO的键盘矩阵输入设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/steelseries/apex_pro_mini/apex_pro_mini.dts?plain=1#L37">已启用：1</a>）</td>
<td><a href="../input_adc_touch_matrix_binding_reference/P018_gpio-kbd-matrix.md#std-dtcompatible-gpio-kbd-matrix"><code>gpio-kbd-matrix</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>行列到按键的映射器（Row-column to Key Mapper）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/steelseries/apex_pro_mini/apex_pro_mini.dts?plain=1#L64">已启用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P002_input-keymap.md#std-dtcompatible-input-keymap"><code>input-keymap</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L196">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P001_st_stm32-exti.md#std-dtcompatible-st-stm32-exti"><code>st,stm32-exti</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/steelseries/apex_pro_mini/apex_pro_mini.dts?plain=1#L22">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="3">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>STM32闪存（Flash Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L138">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P016_st_stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash"><code>st,stm32-nv-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>这些属性用于支持Zephyr的<code>spi-nor</code>闪存驱动通过Zephyr SPI API，使用基于M25P80的标准命令集控制串行闪存（Serial Flash Memory）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/steelseries/apex_pro_mini/apex_pro_mini.dts?plain=1#L176">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor"><code>jedec,spi-nor</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存或其他非易失性存储器的固定分区（Fixed Partitions）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/steelseries/apex_pro_mini/apex_pro_mini.dts?plain=1#L210">已启用：1</a>）</td>
<td><a href="../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions"><code>fixed-partitions</code></a></td>
</tr>
<tr>
<td rowspan="1">非易失存储器（NVMEM）</td>
<td>片上（On-Chip）</td>
<td>非易失存储器固定布局（Fixed Layout for Non-Volatile Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L159">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P009_fixed-layout.md#std-dtcompatible-fixed-layout"><code>fixed-layout</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>STM32 嵌入式非易失一次性可编程存储器（NVM OTP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L155">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L148">已禁用：1</a>）</td>
<td><a href="../otp_binding_reference/P010_st_stm32-nvm-otp.md#std-dtcompatible-st-stm32-nvm-otp"><code>st,stm32-nvm-otp</code></a></td>
</tr>
<tr>
<td rowspan="1">物理层（PHY）</td>
<td>片上（On-Chip）</td>
<td>用于所有内置于 USB IP 的 USB 收发器（USB Transceivers）的绑定。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l412.dtsi?plain=1#L74">已启用：1</a>）</td>
<td><a href="../phy_binding_reference/P008_usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv"><code>usb-nop-xceiv</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>STM32 引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L212">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P004_st_stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl"><code>st,stm32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>STM32 电源控制器（Power Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L559">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P010_st_stm32-pwr.md#std-dtcompatible-st-stm32-pwr"><code>st,stm32-pwr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32唤醒线控制器（Wake-up Lines Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L563">已禁用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P009_st_stm32-pwr-wkupctrl.md#std-dtcompatible-st-stm32-pwr-wkupctrl"><code>st,stm32-pwr-wkupctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>STM32 脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L378">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L349">已禁用：3</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P011_st_stm32-pwm.md#std-dtcompatible-st-stm32-pwm"><code>st,stm32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">四线串行外设接口（QSPI）</td>
<td>片上（On-Chip）</td>
<td>STM32 四线串行外设接口控制器（QSPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L317">已禁用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P011_st_stm32-qspi.md#std-dtcompatible-st-stm32-qspi"><code>st,stm32-qspi</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 复位与时钟控制器（Reset and Clock Control，RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L190">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P017_st_stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl"><code>st,stm32-rcc-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>STM32 随机数生成器（Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L547">已禁用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P016_st_stm32-rng.md#std-dtcompatible-st-stm32-rng"><code>st,stm32-rng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>STM32 实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L459">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P014_st_stm32-rtc.md#std-dtcompatible-st-stm32-rtc"><code>st,stm32-rtc</code></a></td>
</tr>
<tr>
<td rowspan="4">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>STM32 正交解码器（Quadrature Decoder）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L360">已禁用：2</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P028_st_stm32-qdec.md#std-dtcompatible-st-stm32-qdec"><code>st,stm32-qdec</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系列温度节点（TEMP），用于以两个温度点完成生产校准的传感器。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L603">已禁用：1</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P029_st_stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal"><code>st,stm32-temp-cal</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 参考电压（VREF+）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L614">已启用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P003_st_stm32-vref.md#std-dtcompatible-st-stm32-vref"><code>st,stm32-vref</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 电池电压（VBAT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L622">已启用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P001_st_stm32-vbat.md#std-dtcompatible-st-stm32-vbat"><code>st,stm32-vbat</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L266">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L275">已禁用：2</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P016_st_stm32-usart.md#std-dtcompatible-st-stm32-usart"><code>st,stm32-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低功耗通用异步收发器（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L284">已禁用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P014_st_stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart"><code>st,stm32-lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">系统管理总线（SMbus）</td>
<td>片上（On-Chip）</td>
<td>STM32 系统管理总线控制器（SMBus Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L629">已禁用：3</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P013_st_stm32-smbus.md#std-dtcompatible-st-stm32-smbus"><code>st,stm32-smbus</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>带嵌入式接收和发送先进先出队列（Rx / Tx FIFOs）的STM32 SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L327">已启用：2</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P009_st_stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo"><code>st,stm32-spi-fifo</code></a></td>
</tr>
<tr>
<td rowspan="3">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 定时器（Timers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L367">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L338">已禁用：4</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P008_st_stm32-timers.md#std-dtcompatible-st-stm32-timers"><code>st,stm32-timers</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低功耗定时器（LPTIM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L523">已禁用：2</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P007_st_stm32-lptim.md#std-dtcompatible-st-stm32-lptim"><code>st,stm32-lptim</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>STM32 USB控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l412.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../usb_stm32_audio_binding_reference/P006_st_stm32-usb.md#std-dtcompatible-st-stm32-usb"><code>st,stm32-usb</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>STM32 看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L252">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P001_st_stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog"><code>st,stm32-watchdog</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系统窗口看门狗（System Window Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L258">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P002_st_stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog"><code>st,stm32-window-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="peripheral-mapping"></a>

#### 外设映射（Peripheral Mapping）：


- SPI1闪存驱动：PB3／PB4／PA5／PA15
- SPI2 LED控制器：PB12／PB13／PA14／PA15
- 按键列C1—C14：PA0／PA1／PA2／PA3／PA4／PA5／PA6／PA7／PC4／PC5／PC0／PC3／PC1／PC2
- 按键行R1—R5：PA11／PB10／PB2／PB1／PB0
- SWD调试端口：PA13／PA14
- USB端口：PA11／PA12
- 测试点：PA8／PB6／PB8／PB9／PC10／PC11／PC12／PC13／PC14／PC15／PC8／PC9／PD2

<a id="keyboard-mapping"></a>

#### 键盘映射（Keyboard Mapping）：

<table>
<tr>
<th>按键列（Column）</th>
<th>C1</th>
<th>C2</th>
<th>C3</th>
<th>C4</th>
<th>C5</th>
<th>C6</th>
<th>C7</th>
<th>C8</th>
<th>C9</th>
<th>C10</th>
<th>C11</th>
<th>C12</th>
<th>C13</th>
<th>C14</th>
</tr>
<tr>
<td>通用输入输出（GPIO）</td>
<td>PA0</td>
<td>PA1</td>
<td>PA2</td>
<td>PA3</td>
<td>PA4</td>
<td>PA5</td>
<td>PA6</td>
<td>PA7</td>
<td>PC4</td>
<td>PC5</td>
<td>PC0</td>
<td>PC1</td>
<td>PC2</td>
<td>PC3</td>
</tr>
</table>

<table>
<tr>
<th>按键行（Row）</th>
<th>R1</th>
<th>R2</th>
<th>R3</th>
<th>R4</th>
<th>R5</th>
</tr>
<tr>
<td>通用输入输出（GPIO）</td>
<td>PB11</td>
<td>PB10</td>
<td>PB2</td>
<td>PB1</td>
<td>PB0</td>
</tr>
</table>

下表描述电气连接，而非几何位置。例如K15退格键（BACKSPACE）地址为第12列、第5行，但实际位于右上角K13旁。

<table>
<tr>
<th></th>
<th>C1</th>
<th>C2</th>
<th>C3</th>
<th>C4</th>
<th>C5</th>
<th>C6</th>
<th>C7</th>
<th>C8</th>
<th>C9</th>
<th>C10</th>
<th>C11</th>
<th>C12</th>
<th>C13</th>
<th>C14</th>
</tr>
<tr>
<td>R1</td>
<td>K1</td>
<td>K2</td>
<td>K3</td>
<td>K4</td>
<td>K5</td>
<td>K6</td>
<td>K7</td>
<td>K8</td>
<td>K9</td>
<td>K10</td>
<td>K11</td>
<td>K12</td>
<td>K13</td>
<td></td>
</tr>
<tr>
<td>R2</td>
<td>K16</td>
<td>K17</td>
<td>K18</td>
<td>K19</td>
<td>K20</td>
<td>K21</td>
<td>K22</td>
<td>K23</td>
<td>K24</td>
<td>K25</td>
<td>K26</td>
<td>K27</td>
<td>K28</td>
<td></td>
</tr>
<tr>
<td>R3</td>
<td>K30</td>
<td>K31</td>
<td>K32</td>
<td>K33</td>
<td>K34</td>
<td>K35</td>
<td>K36</td>
<td>K37</td>
<td>K38</td>
<td>K39</td>
<td>K40</td>
<td>K41</td>
<td>K42</td>
<td>K43</td>
</tr>
<tr>
<td>R4</td>
<td>K44</td>
<td>K45</td>
<td>K46</td>
<td>K47</td>
<td>K48</td>
<td>K49</td>
<td>K50</td>
<td>K51</td>
<td>K52</td>
<td>K53</td>
<td>K54</td>
<td>K55</td>
<td></td>
<td>K57</td>
</tr>
<tr>
<td>R5</td>
<td>K58</td>
<td>K59</td>
<td>K60</td>
<td></td>
<td>K62</td>
<td></td>
<td></td>
<td>K65</td>
<td>K66</td>
<td>K67</td>
<td>K68</td>
<td>K15</td>
<td></td>
<td></td>
</tr>
</table>

<a id="led-driver-mapping"></a>

#### LED驱动器映射（LED Driver Mapping）：

下面是Lumissil驱动器上的LED映射。

<table>
<tr>
<th>功能（Function）</th>
<th>颜色（Color）</th>
<th>区域（Area）</th>
</tr>
<tr>
<td>CS1</td>
<td>蓝色（Blue）</td>
<td>K1-K11</td>
</tr>
<tr>
<td>CS2</td>
<td>绿色（Green）</td>
<td>K1-K11</td>
</tr>
<tr>
<td>CS3</td>
<td>红色（Red）</td>
<td>K1-K11</td>
</tr>
<tr>
<td>CS4</td>
<td>蓝色（Blue）</td>
<td>K16-K26</td>
</tr>
<tr>
<td>CS5</td>
<td>绿色（Green）</td>
<td>K16-K26</td>
</tr>
<tr>
<td>CS6</td>
<td>红色（Red）</td>
<td>K16-K26</td>
</tr>
<tr>
<td>CS7</td>
<td>蓝色（Blue）</td>
<td>K30-K40</td>
</tr>
<tr>
<td>CS8</td>
<td>绿色（Green）</td>
<td>K30-K40</td>
</tr>
<tr>
<td>CS9</td>
<td>红色（Red）</td>
<td>K30-K40</td>
</tr>
<tr>
<td>CS10</td>
<td>蓝色（Blue）</td>
<td>K44-K54</td>
</tr>
<tr>
<td>CS11</td>
<td>绿色（Green）</td>
<td>K44-K54</td>
</tr>
<tr>
<td>CS12</td>
<td>红色（Red）</td>
<td>K44-K54</td>
</tr>
<tr>
<td>CS13</td>
<td>蓝色（Blue）</td>
<td>K55,K56,K58-K68</td>
</tr>
<tr>
<td>CS14</td>
<td>绿色（Green）</td>
<td>K55,K56,K58-K68</td>
</tr>
<tr>
<td>CS15</td>
<td>红色（Red）</td>
<td>K55,K56,K58-K68</td>
</tr>
<tr>
<td>CS16</td>
<td>蓝色（Blue）</td>
<td>K12-K15,K27-K29,K41-K43,K57</td>
</tr>
<tr>
<td>CS17</td>
<td>绿色（Green）</td>
<td>K12-K15,K27-K29,K41-K43,K57</td>
</tr>
<tr>
<td>CS18</td>
<td>红色（Red）</td>
<td>K12-K15,K27-K29,K41-K43,K57</td>
</tr>
</table>

<table>
<tr>
<th>功能（Function）</th>
<th>各列按键（Column Keys）</th>
</tr>
<tr>
<td>SW1</td>
<td>K1, K12, K16, K30, K43, K44, K58, K68</td>
</tr>
<tr>
<td>SW2</td>
<td>K2, K13, K17, K31, K45, K59</td>
</tr>
<tr>
<td>SW3</td>
<td>K3, K14, K18, K32, K46, K60</td>
</tr>
<tr>
<td>SW4</td>
<td>K4, K15, K19, K33, K47, K62</td>
</tr>
<tr>
<td>SW5</td>
<td>K5, K20, K27, K34, K48</td>
</tr>
<tr>
<td>SW6</td>
<td>K6, K21, K28, K35, K49</td>
</tr>
<tr>
<td>SW7</td>
<td>K7, K22, K29, K36, K50, K56, K65, K66</td>
</tr>
<tr>
<td>SW8</td>
<td>K8, K23, K37, K41, K51</td>
</tr>
<tr>
<td>SW9</td>
<td>K9, K24, K38, K42, K52, K67</td>
</tr>
<tr>
<td>SW10</td>
<td>K10, K25, K29, K39, K53</td>
</tr>
<tr>
<td>SW11</td>
<td>K11, K26, K40, K54, K55, K57</td>
</tr>
</table>

## 译注

Apex Pro Mini首次解除保护会擦除出厂固件。原文选项字节名称同时出现PCROP_RDB与PCROP_RDP，保留原拼写；键位表描述电气矩阵，不能当作物理排列。法国AZERTY与QWERTY键数和K29／K45／K42差别分别保留。RGB硬件存在但LED驱动尚未支持。

---

[上一章](P002_VisionFive_2_JH7110.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_SteelSeries.md)
