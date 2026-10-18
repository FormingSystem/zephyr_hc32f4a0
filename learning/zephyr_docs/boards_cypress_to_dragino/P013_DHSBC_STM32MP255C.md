---
id: learning.zephyr-docs.boards-cypress-to-dragino.page-13
title: DHSBC STM32MP255C
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/dh/stm32mp255c_dhsbc/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="stm32mp255c_dhsbc"></a>

# 第13章\_DHSBC STM32MP255C

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/dh/stm32mp255c_dhsbc/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/dhsbc-stm32mp255c.webp](images/dhsbc-stm32mp255c.webp)](images/dhsbc-stm32mp255c.webp)

DHSBC STM32MP255C

名称（Name）：

`stm32mp255c_dhsbc`

厂商（Vendor）：

[DH electronics GmbH公司](https://docs.zephyrproject.org/latest/boards/index.html#vendor=dh)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[stm32mp255cxx](https://docs.zephyrproject.org/latest/boards/index.html#soc=stm32mp255cxx)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/dh/stm32mp255c_dhsbc/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

DHSBC STM32MP255C是一款工业级、开箱即用的单板计算机（Single Board Computer），专为物联网（IoT）及人机界面（HMI）应用开发。它基于可焊接、引脚兼容的DHCOS STM32MP2系统模块（System on Module），支持模块化、可扩展的系统架构。该平台面向高性能、超过十年的长期供货及严苛工业环境。

DHSBC STM32MP255C完整支持主线Linux，包括Vivante GPU，为图形用户界面及复杂应用开发提供面向未来的软件基础。集成的安全启动（Secure Boot）、安全存储（Secure Storage）等功能保护敏感数据，支持安全设计（Security by Design）方法。连接能力覆盖千兆以太网、WiFi和蓝牙；多媒体功能包括3D GPU、显示、摄像头及视频。集成STPMIC25电源管理芯片后，也适用于高能效和低功耗模式要求的应用。

Zephyr OS移植运行于Cortex®-M33内核，作为Cortex®-A35内核的协处理器（Coprocessor），在应用内核运行Linux高性能处理的同时实现实时和低功耗应用。

<a id="features"></a>

### Features:


- STM32MP255CAK3微处理器，VFBGA424封装，包含双核Arm® Cortex®-A35、一个Cortex®-M33及一个Cortex®-M0+
- ST电源管理芯片STPMIC25DPQR
- 4 GB动态随机存储器（DRAM），32位LPDDR4-2400
- 16 GB eMMC闪存
- 4 MB SPI NOR闪存
- 4 kB EEPROM
- 两路1 Gbit/s以太网，RGMII接口
- 高速USB主机集线器（Host Hub）
- 高速USB Type-C 3.2 Gen 1x1，支持DisplayPort替代模式（Alt Mode）
- Bluetooth® v5.4 BR／EDR／LE
- WiFi，2.4 GHz、5 GHz及6 GHz三频段，支持IEEE 802.11a/b/g/n/ac/ax
- 电源及复位按键
- 四个启动引脚开关（Boot Pin Switches）
- 开发板连接器（Board Connectors）：


  - 两个以太网RJ45接口
  - 一个USB主机Type-A接口
  - USB Type-C®，数据
  - USB Type-C®，供电
  - microSD™卡座
  - 双通道MIPI CSI-2®摄像头模块扩展连接器
  - 低压差分信号（LVDS）
  - 三针UART连接器，串行控制台
  - Raspberry Pi 40针扩展连接器
  - 供RTC及备份SRAM使用的VBAT
  - 联合测试行动组调试接口（JTAG）
- Linux® Yocto项目板级支持包（BSP）

<a id="id3"></a>

<a id="id11"></a>

<a id="id13"></a>

更多开发板及SoC信息见[STM32MP255C-DHSBC网站](https://www.dh-electronics.com/en/embedded-products/development-carrier-boards/detail/dhsbc-stm32mp255c)[注1](#id2)、[STM32MP255C网站](https://www.st.com/en/microcontrollers-microprocessors/stm32mp255c.html)[注5](#id10)，以及[STM32MP255C参考手册](https://www.st.com/resource/en/reference_manual/rm0457-stm32mp25xx-advanced-armbased-3264bit-mpus-stmicroelectronics.pdf)[注6](#id12)。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="cores"></a>

### Cores:


- 64位双核Arm® Cortex®-A35，最高1.2 GHz


  - 每个Cortex®-A35内核具有32 Kbyte指令及32 Kbyte数据一级缓存（L1 I/D Cache）
  - 512 Kbyte统一二级缓存（Unified L2 Cache）
  - Arm® NEON™及Arm® TrustZone®
- 32位Arm® Cortex®-M33，带浮点单元（FPU）、存储器保护单元（MPU）及Arm® TrustZone®，最高400 MHz


  - Cortex®-M33具有16 Kbyte一级指令缓存（ICache）及16 Kbyte一级数据缓存（DCache）
- SmartRun域中的32位Arm® Cortex®-M0+，最高200 MHz，自主模式（Autonomous Mode）下最高16 MHz

<a id="memories"></a>

### 存储器（Memories）：


- 4 Gbyte外部DDR存储器，32位LPDDR4-2400
- 808 Kbyte内部SRAM：256 Kbyte AXI SYSRAM、128 Kbyte AXI视频RAM或SYSRAM扩展区、256 Kbyte AHB SRAM、备份域中带ECC的128 Kbyte AHB SRAM、备份域中带ECC的8 Kbyte SRAM，以及SmartRun域中的32 Kbyte SRAM。总量与分项依原文保留。
- 两个八线SPI存储器接口（Octo-SPI Memory Interfaces）
- 灵活外部存储器控制器，数据总线最大16位；通过并行接口连接外部集成电路（IC）及支持最高8位纠错码（ECC）的单层单元（SLC）NAND存储器

<a id="power"></a>

### 电源（Power）


- STPMIC25用于电压调节，包含多个降压（Buck）及低压差（LDO）稳压器
- USB-C电源输入
- VBAT备份电池连接器，供RTC及备份SRAM使用

<a id="clock-management"></a>

### 时钟管理（Clock Management）


- 外部振荡器（External Oscillators）：


  - 32.768 kHz外部低速（LSE）晶体
  - 40 MHz外部高速（HSE）晶体
- 内部振荡器（Internal Oscillators）：


  - 64 MHz内部高速（HSI）振荡器
  - 4 MHz内部CSI振荡器
  - 32 kHz内部低速（LSI）振荡器
  - 五个独立锁相环（PLL），支持整数及小数模式（Integer/Fractional Mode）

<a id="security-safety"></a>

### Security/Safety


- 安全启动、TrustZone®外设、主动防篡改（Active Tamper）、环境监控、安全显示图层及硬件加速器
- 完整资源隔离框架（Resource Isolation Framework）

<a id="connectivity"></a>

### 连接能力（Connectivity）


- 两路千兆以太网，RGMII
- USB 2.0高速主机（High-Speed Host）
- USB Type-C®
- Raspberry Pi 40针扩展连接器

<a id="display-camera"></a>

### 显示与摄像头（Display & Camera）


- 低压差分信号（LVDS）接口：一路双链路，两个四通道LVDS连接器
- MIPI-CSI2接口：一个双通道连接器

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`stm32mp255c_dhsbc`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="stm32mp255c_dhsbc-hw-features"></a>

<a id="stm32mp255c_dhsbc-stm32mp255c_dhsbc/stm32mp255cxx/m33-hw-features-section"></a>

#### `stm32mp255c_dhsbc/stm32mp255cxx/m33`目标（Target）

<a id="stm32mp255c_dhsbc-stm32mp255c_dhsbc/stm32mp255cxx/m33-hw-features-panel"></a>

<a id="stm32mp255c_dhsbc-stm32mp255c_dhsbc/stm32mp255cxx/m33-hw-features-memory"></a>

该开发板目标的片上存储容量：8 MiB RAM、8 MiB Flash。

<a id="stm32mp255c_dhsbc-stm32mp255c_dhsbc/stm32mp255cxx/m33-hw-features-table"></a>

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
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L24">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>STM32H7系列及兼容器件的FDCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L152">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L161">已禁用：2</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P013_st_stm32h7-fdcan.md#std-dtcompatible-st-stm32h7-fdcan"><code>st,stm32h7-fdcan</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>STM32MP2复位与时钟控制器（RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../timer_reference/P182_STM32MP2复位与时钟控制绑定.md#dtbinding-st-stm32mp2-rcc"><code>st,stm32mp2-rcc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L332">已启用：2</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>STM32 CRC 计算单元（Calculation Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L323">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P011_st_stm32-crc.md#std-dtcompatible-st-stm32-crc"><code>st,stm32-crc</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>STM32MP2 GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L67">已启用：12</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P030_st_stm32mp2-gpio.md#std-dtcompatible-st-stm32mp2-gpio"><code>st,stm32mp2-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通过Raspberry Pi 40针排针引出的GPIO（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/dh/stm32mp255c_dhsbc/raspberrypi_40pins_connector.dtsi?plain=1#L7">已启用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P009_raspberrypi-40pins-header.md#std-dtcompatible-raspberrypi-40pins-header"><code>raspberrypi-40pins-header</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>STM32 I2C V2 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp251_m33.dtsi?plain=1#L103">已禁用：8</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P008_st_stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2"><code>st,stm32-i2c-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>STM32H5 I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L286">已禁用：4</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P010_st_stm32-i3c.md#std-dtcompatible-st-stm32-i3c"><code>st,stm32-i3c</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp251_m33.dtsi?plain=1#L14">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P001_st_stm32-exti.md#std-dtcompatible-st-stm32-exti"><code>st,stm32-exti</code></a></td>
</tr>
<tr>
<td rowspan="1">处理器间消息（IPM）</td>
<td>片上（On-Chip）</td>
<td>STM32 处理器间通信控制器邮箱（IPCC Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L54">已启用：1</a>）</td>
<td><a href="../intercore_reference/P075_STM32处理器间通信控制器绑定.md#dtbinding-st-stm32-ipcc-mailbox"><code>st,stm32-ipcc-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>STM32 引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L60">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P004_st_stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl"><code>st,stm32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>STM32 脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp251_m33.dtsi?plain=1#L233">已禁用：1</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P011_st_stm32-pwm.md#std-dtcompatible-st-stm32-pwm"><code>st,stm32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 复位与时钟控制器（Reset and Clock Control，RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L48">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P017_st_stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl"><code>st,stm32-rcc-rctl</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L230">已禁用：4</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P016_st_stm32-usart.md#std-dtcompatible-st-stm32-usart"><code>st,stm32-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L254">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L262">已禁用：4</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P015_st_stm32-uart.md#std-dtcompatible-st-stm32-uart"><code>st,stm32-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>STM32H7 串行外设接口控制器（SPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp251_m33.dtsi?plain=1#L72">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L170">已禁用：7</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P013_st_stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi"><code>st,stm32h7-spi</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 定时器（Timers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp251_m33.dtsi?plain=1#L223">已禁用：1</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P008_st_stm32-timers.md#std-dtcompatible-st-stm32-timers"><code>st,stm32-timers</code></a></td>
</tr>
<tr>
<td rowspan="1">视频（Video）</td>
<td>片上（On-Chip）</td>
<td>STM32数字摄像头接口像素处理器（DCMIPP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp251_m33.dtsi?plain=1#L240">已禁用：1</a>）</td>
<td><a href="../video_st_sony_emulation_binding_reference/P005_st_stm32-dcmipp.md#std-dtcompatible-st-stm32-dcmipp"><code>st,stm32-dcmipp</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>STM32 看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L308">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P001_st_stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog"><code>st,stm32-watchdog</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系统窗口看门狗（System Window Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L316">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P002_st_stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog"><code>st,stm32-window-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="id5"></a>

连接方式与I/O说明见DHSBC STM32MP255C开发板快速入门指南：[STM32MP255C-DHSBC quick start guide](https://wiki.dh-electronics.com/images/e/ef/DOC_DHSBC-STM32MP25-Quick-Start-Guide_R01_2025-09-11.pdf)[注2](#id4)。

<a id="system-clock"></a>

### 系统时钟（System Clock）

<a id="cortex-a35"></a>

#### Cortex®-A35

Zephyr尚不支持。

<a id="cortex-m33"></a>

#### Cortex®-M33

Cortex®-M33内核配置为运行于400 MHz。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`stm32mp255c_dhsbc`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>✅</td>
<td></td>
</tr>
</table>

<a id="prerequisite"></a>

### 前提条件（Prerequisite）

在DHSBC STM32MP255C上运行Zephyr前，需要先为Cortex®-A35内核配置Linux®环境。Cortex®-M33作为协处理器运行Zephyr，需要Cortex®-A35通过远程处理器（remoteproc）框架加载并启动固件。

<a id="id7"></a>

<a id="id9"></a>

配置Linux环境的一种方式是使用DH electronics KAS／Yocto仓库构建Linux镜像，见[STM32MP255C-DHSBC kas yocto](https://github.com/dh-electronics/kas-dhsom)[注3](#id6)；也可使用预构建镜像，见[STM32MP255C-DHSBC prebuild images](https://github.com/dh-electronics/prebuilt-test-images-dhsom)[注4](#id8)。

<a id="id18"></a>

另一种方式是按Starter Package 5使用OpenSTLinux发行版；详细步骤见[STM32MPU维基（Wiki）](https://wiki.st.com/stm32mpu/wiki/Main_Page)[注8](#id17)。

<a id="loading-the-firmware"></a>

### 加载固件（Loading the Firmware）

开发板安装Linux发行版后，由Cortex®-A35将Zephyr固件镜像加载到DDR和／或SRAM，并启动Cortex®-M33内核。可以使用west构建应用，以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例。

```text
# From the root of the zephyr repository
west build -b stm32mp255c_dhsbc/stm32mp255cxx/m33 samples/hello_world
```

将固件复制到开发板文件系统，再使用Linux remoteproc框架启动。

启动固件：

```text
$ cp zephyr.elf /lib/firmware/
$ echo -n zephyr.elf > /sys/class/remoteproc/remoteproc0/firmware
$ echo start > /sys/class/remoteproc/remoteproc0/state
```

停止固件：

```text
$ echo stop > /sys/class/remoteproc/remoteproc0/state
```

<a id="id15"></a>

更多步骤见ST维基中的[STM32MP257F启动Cortex-M33固件](https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs)（boot Cortex-M33 firmware）页面[注7](#id14)。

<a id="debugging"></a>

### 调试（Debugging）

可使用J-Link配合J-Link Software Pack，或ST-Link配合OpenOCD调试应用；默认使用J-Link。

<a id="id20"></a>

使用ST-Link时，必须使用ST的最新OpenOCD版本，文件见[device-stm-openocd](https://github.com/STMicroelectronics/device-stm-openocd/tree/main)[注9](#id19)。通过`west attach`的`--openocd`及`--openocd-search`选项指定该版本。

必须先由Cortex®-A35启动固件，然后才能将调试器附加（Attach）到正在运行的Zephyr固件。


- 构建示例（Build the Sample）

```text
# From the root of the zephyr repository
west build -b stm32mp255c_dhsbc/stm32mp255cxx/m33 samples/drivers/uart/echo_bot
```


- <a id="id16"></a>

  将固件复制到开发板，通过remoteproc加载并启动，见[STM32MP257F启动Cortex-M33固件](https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs)页面[注7](#id14)。固件将在`raspberry_pi_serial`上回显收到的全部字节。
- 通过J-Link附加到目标：

```text
$ west attach
```


- 也可通过ST-Link与OpenOCD附加到目标，假定ST的OpenOCD已下载到`/opt/device-stm-openocd`：

```text
$ west attach --runner openocd \
  --openocd "/opt/device-stm-openocd/prebuilt/openocd" \
  --openocd-search "/opt/device-stm-openocd/prebuilt/scripts/"
```

<a id="references"></a>

### 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.dh-electronics.com/en/embedded-products/development-carrier-boards/detail/dhsbc-stm32mp255c](https://www.dh-electronics.com/en/embedded-products/development-carrier-boards/detail/dhsbc-stm32mp255c)

<a id="id4"></a>

〔[2](#id5)〕 [https://wiki.dh-electronics.com/images/e/ef/DOC_DHSBC-STM32MP25-Quick-Start-Guide_R01_2025-09-11.pdf](https://wiki.dh-electronics.com/images/e/ef/DOC_DHSBC-STM32MP25-Quick-Start-Guide_R01_2025-09-11.pdf)

<a id="id6"></a>

〔[3](#id7)〕 [https://github.com/dh-electronics/kas-dhsom](https://github.com/dh-electronics/kas-dhsom)

<a id="id8"></a>

〔[4](#id9)〕 [https://github.com/dh-electronics/prebuilt-test-images-dhsom](https://github.com/dh-electronics/prebuilt-test-images-dhsom)

<a id="id10"></a>

〔[5](#id11)〕 [https://www.st.com/en/microcontrollers-microprocessors/stm32mp255c.html](https://www.st.com/en/microcontrollers-microprocessors/stm32mp255c.html)

<a id="id12"></a>

〔[6](#id13)〕 [https://www.st.com/resource/en/reference_manual/rm0457-stm32mp25xx-advanced-armbased-3264bit-mpus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0457-stm32mp25xx-advanced-armbased-3264bit-mpus-stmicroelectronics.pdf)

<a id="id14"></a>

〔7〕 ([1](#id15),[2](#id16)) [https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs](https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs)

<a id="id17"></a>

〔[8](#id18)〕 [https://wiki.st.com/stm32mpu/wiki/Main_Page](https://wiki.st.com/stm32mpu/wiki/Main_Page)

<a id="id19"></a>

〔[9](#id20)〕 [https://github.com/STMicroelectronics/device-stm-openocd/tree/main](https://github.com/STMicroelectronics/device-stm-openocd/tree/main)

## 译注

M33固件须由运行Linux的A35通过remoteproc启动，之后才附加调试器。文中的/lib/firmware和/sys是目标Linux系统目录；/opt/device-stm-openocd是上游示例的工具安装目录，均不表示本译文仓库位置。具体安装位置按读者环境调整。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [Linux_remoteproc_framework_overview](https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs)：The read operation timed out。
- [Main_Page](https://wiki.st.com/stm32mpu/wiki/Main_Page)：The read operation timed out。
- [stm32mp255c.html](https://www.st.com/en/microcontrollers-microprocessors/stm32mp255c.html)：HTTP Error 567: Unknown Status。
- [rm0457-stm32mp25xx-advanced-armbased-3264bit-mpus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0457-stm32mp25xx-advanced-armbased-3264bit-mpus-stmicroelectronics.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P012_DH_electronics.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_Arty.md)
