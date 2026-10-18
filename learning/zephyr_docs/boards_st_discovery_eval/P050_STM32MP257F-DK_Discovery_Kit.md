---
id: learning.zephyr-docs.boards-st-discovery-eval.page-50
title: STM32MP257F-DK Discovery Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/st/stm32mp257f_dk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="stm32mp257f_dk"></a>

# 第50章\_STM32MP257F-DK探索套件（Discovery Kit）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/st/stm32mp257f_dk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/stm32mp257f_dk.webp](images/stm32mp257f_dk.webp)](images/stm32mp257f_dk.webp)

STM32MP257F-DK探索套件（Discovery Kit）

名称（Name）：

`stm32mp257f_dk`

厂商（Vendor）：

[意法半导体（STMicroelectronics）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=st)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[stm32mp257fxx](https://docs.zephyrproject.org/latest/boards/index.html#soc=stm32mp257fxx)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32mp257f_dk/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

STM32MP257F-DK是STM32MP257F微处理器及STPMIC25配套芯片的完整演示与开发平台，具有1.5 GHz Arm双核Cortex-A35及400 MHz Cortex-M33。Zephyr运行于M33，作为A35的协处理器。

<a id="features"></a>

### 功能（Features）：


- VFBGA424封装STM32MP257FAK3，包含Arm双核Cortex-A35及Cortex-M33
- 意法半导体电源管理芯片STPMIC25
- 32 Gbit LPDDR4 DRAM
- 64 Gbit eMMC v5.1
- 1 Gbit/s以太网RGMII
- 2路USB 2.0高速接口
- USB 3.0超高速（SuperSpeed）PD，支持双电源角色DRP及双数据角色DRD
- Wi-Fi 802.11 b/g/n
- Bluetooth低功耗LE
- 4个用户LED
- 2个用户键、1个防篡改键及1个复位键
- 唤醒按键
- 四个启动引脚开关（Boot Pin Switches）
- 开发板连接器（Board Connectors）：


  - 以太网RJ45接口
  - 2个层叠式USB 2.0高速Type-A接口
  - USB 3.0 Type-C PD接口
  - microSD™卡座
  - 双通道MIPI CSI-2®摄像头模块扩展连接器
  - 高清多媒体接口（HDMI®）
  - 低压差分信号（LVDS）
  - GPIO扩展连接器
  - VBAT备份电源
- 板载STLINK-V3EC：


  - 调试器支持USB重新枚举为虚拟COM端口及调试端口
  - 通过USB Type-C为开发板供电
- 基于上游开源Linux的STM32 MPU OpenSTLinux发行版，以及带示例的STM32CubeMP2软件
- 开发环境包括Linux Yocto Project、Buildroot及STM32CubeIDE

<a id="id3"></a>

更多信息见[STM32MP257F-DK网站](https://www.st.com/en/evaluation-tools/stm32mp257f-dk.html#overview)[注1](#id2)。

<a id="hardware"></a>

## 硬件（Hardware）


- 内核（Cores）


  - 64位Arm双核Cortex-A35，最高1.5 GHz
  - 32位Arm® Cortex®-M33，带浮点单元（FPU）、存储器保护单元（MPU）及Arm® TrustZone®，最高400 MHz
- 存储器（Memories）


  - 外部DDR最高4 Gbytes
  - 808 Kbyte内部SRAM
  - 2路Octo-SPI存储器接口
  - 灵活外部存储器控制器，数据总线最多 16 位。
- 电源（Power）


  - STPMIC25用于电压调节，包含多个降压（Buck）及低压差（LDO）稳压器
  - USB-C电源输入
- 时钟管理（Clock Management）


  - 32.768 kHz外部低速（LSE）晶体
  - 40 MHz外部高速（HSE）晶体
  - 内部64 MHz HSI振荡器
  - 内部4 MHz CSI振荡器
  - 内部32 kHz LSI振荡器
  - 五个独立锁相环（PLL），支持整数及小数模式（Integer/Fractional Mode）
- 信息安全／功能安全（Security/Safety）


  - 安全启动、TrustZone®外设、主动防篡改（Active Tamper）、环境监控、安全显示图层及硬件加速器
  - 完整资源隔离框架（Resource Isolation Framework）
- 连接能力（Connectivity）


  - 1路千兆以太网RGMII
  - USB 2.0高速主机，双端口
  - USB Type-C双角色端口DRP
  - GPIO扩展连接器
- 显示与摄像头（Display & Camera）


  - 4通道LVDS接口
  - 2通道CSI-2摄像头接口
- 调试（Debug）


  - 板载STLINK-V3EC调试器，提供VCP、JTAG及SWD

更多STM32MP257F信息见：


- <a id="id7"></a>

  ST官网的STM32MP257F产品页[注3](#id6)（[STM32MP257F在ST官网的产品页](https://www.st.com/en/microcontrollers-microprocessors/stm32mp257f.html)）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`stm32mp257f_dk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="stm32mp257f_dk-hw-features"></a>

<a id="stm32mp257f_dk-stm32mp257f_dk/stm32mp257fxx/m33-hw-features-section"></a>

#### `stm32mp257f_dk/stm32mp257fxx/m33`目标（Target）

<a id="stm32mp257f_dk-stm32mp257f_dk/stm32mp257fxx/m33-hw-features-panel"></a>

<a id="stm32mp257f_dk-stm32mp257f_dk/stm32mp257fxx/m33-hw-features-memory"></a>

该开发板目标的片上存储容量：8 MiB RAM、8 MiB Flash。

<a id="stm32mp257f_dk-stm32mp257f_dk/stm32mp257fxx/m33-hw-features-table"></a>

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
<td>STM32H7系列及兼容器件的FDCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L152">已禁用：3</a>）</td>
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
<td>引出到Raspberry Pi CSI摄像头连接器的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32mp257f_dk/stm32mp257f_dk_stm32mp257fxx_m33.dts?plain=1#L50">已启用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P004_raspberrypi_csi-connector.md#std-dtcompatible-raspberrypi-csi-connector"><code>raspberrypi,csi-connector</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>STM32 I2C V2 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp251_m33.dtsi?plain=1#L187">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp251_m33.dtsi?plain=1#L103">已禁用：7</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P008_st_stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2"><code>st,stm32-i2c-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>STM32H5 I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L286">已禁用：4</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P010_st_stm32-i3c.md#std-dtcompatible-st-stm32-i3c"><code>st,stm32-i3c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32mp257f_dk/stm32mp257f_dk_stm32mp257fxx_m33.dts?plain=1#L34">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
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
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32mp257f_dk/stm32mp257f_dk_stm32mp257fxx_m33.dts?plain=1#L25">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
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
<td>STM32 通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L270">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L230">已禁用：3</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P016_st_stm32-usart.md#std-dtcompatible-st-stm32-usart"><code>st,stm32-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L262">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L254">已禁用：4</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P015_st_stm32-uart.md#std-dtcompatible-st-stm32-uart"><code>st,stm32-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>STM32H7 串行外设接口控制器（SPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L170">已禁用：8</a>）</td>
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

STM32MP257F-DK原理图见：[STM32MP257F-DK Discovery套件原理图](https://www.st.com/resource/en/schematic_pack/mb1605-mp257f-c01-schematic.pdf)[注2](#id4)。

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

`stm32mp257f_dk`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>调试服务器（debugserver）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

<a id="prerequisite"></a>

### 前提条件（Prerequisite）

在STM32MP257F-DK运行Zephyr前，须先为Cortex-A35配置Linux环境；M33作为协处理器运行Zephyr，需要A35通过remoteproc加载并启动固件。

<a id="id12"></a>

<a id="id14"></a>

可按[Starter Package](https://wiki.stmicroelectronics.cn/stm32mpu/wiki/STM32MP25_Discovery_kits_-_Starter_Package)入门软件包[注5](#id11)安装官方ST OpenSTLinux发行版；更多步骤见[STM32MPU Wiki](https://wiki.st.com/stm32mpu/wiki/Main_Page) [注6](#id13)。

<a id="loading-the-firmware"></a>

### 加载固件（Loading the Firmware）

安装OpenSTLinux后，当前发行版由Cortex-A35负责将Zephyr镜像加载到DDR及／或SRAM，并启动Cortex-M33。应用可用west构建，下面以[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)为例。

```text
# From the root of the zephyr repository
west build -b stm32mp257f_dk/stm32mp257fxx/m33 samples/basic/blinky
```

<a id="id9"></a>

将固件复制到开发板文件系统，再用Linux remoteproc框架启动；详情见“[STM32MP257F启动Cortex-M33固件](https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs)”[注4](#id8)。

<a id="debugging"></a>

### 调试（Debugging）

<a id="id16"></a>

可用社区／主线[OpenOCD项目](https://github.com/openocd-org/openocd)[注7](#id15)及GDB调试，原文测试提交为fc566d7。该项目提供board/st/stm32mp257f-dk.cfg；本板在其上提供support/openocd_stm32mp257f_dk_m33.cfg，同时启用A35及M33并固定GDB端口。

Zephyr SDK所带OpenOCD通常过旧，缺少所需板卡／目标脚本，或interface/stlink.cfg不兼容，因此应从源码构建社区／主线OpenOCD：

```text
$ git clone https://github.com/openocd-org/openocd
$ cd openocd
$ ./bootstrap with-submodules
$ ./configure --enable-internal-jimtcl --enable-stlink
$ make
```

除非系统已安装jimtcl，否则必须使用--enable-internal-jimtcl。构建ST-Link驱动还需要libusb-1.0开发头文件，例如Debian／Ubuntu的libusb-1.0-0-dev。

然后为west同时指定构建出的程序及其脚本目录：

```text
$ west build -- -DOPENOCD=/path/to/openocd/src/openocd \
    -DSTM32MP_OPENOCD_SCRIPTS=/path/to/openocd/tcl
```

固件必须先由Cortex-A35启动，随后才能使用OpenOCD将调试器附加到运行中的Zephyr固件。


- 构建示例：

```text
# From the root of the zephyr repository
west build -b stm32mp257f_dk/stm32mp257fxx/m33 samples/basic/blinky -- -DOPENOCD=/path/to/openocd/src/openocd -DSTM32MP_OPENOCD_SCRIPTS=/path/to/openocd/tcl
```


- <a id="id10"></a>

  将固件复制到板上，并用remoteproc加载及启动，步骤见“[STM32MP257F启动Cortex-M33固件](https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs)”[注4](#id8)；橙色LED应闪烁。
- 附加到目标：

```text
$ west attach
```

Cortex-A35的SMP双核及Cortex-M33共用物理调试／SWD端口，但对应独立访问端口。板卡配置同时启用两者并固定GDB端口，使west attach稳定连接M33的3334端口；A35可从3333端口访问，例如gdb-multiarch -ex "target extended-remote :3333"。

<a id="references"></a>

### 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [STM32MP257F-DK官方产品概述](https://www.st.com/en/evaluation-tools/stm32mp257f-dk.html#overview)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.st.com/resource/en/schematic_pack/mb1605-mp257f-c01-schematic.pdf](https://www.st.com/resource/en/schematic_pack/mb1605-mp257f-c01-schematic.pdf)

<a id="id6"></a>

〔[3](#id7)〕 [https://www.st.com/en/microcontrollers-microprocessors/stm32mp257f.html](https://www.st.com/en/microcontrollers-microprocessors/stm32mp257f.html)

<a id="id8"></a>

〔4〕 ([1](#id9),[2](#id10)) [https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs](https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs)

<a id="id11"></a>

〔[5](#id12)〕 [https://wiki.stmicroelectronics.cn/stm32mpu/wiki/STM32MP25_Discovery_kits_-_Starter_Package](https://wiki.stmicroelectronics.cn/stm32mpu/wiki/STM32MP25_Discovery_kits_-_Starter_Package)

<a id="id13"></a>

〔[6](#id14)〕 [https://wiki.st.com/stm32mpu/wiki/Main_Page](https://wiki.st.com/stm32mpu/wiki/Main_Page)

<a id="id15"></a>

〔[7](#id16)〕 [https://github.com/openocd-org/openocd](https://github.com/openocd-org/openocd)

## 译注

Zephyr运行于M33；Linux环境、remoteproc加载与OpenOCD附加流程均保留，M33端口3334，A35 SMP双核端口3333。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [Linux_remoteproc_framework_overview](https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs)：The read operation timed out。
- [Main_Page](https://wiki.st.com/stm32mpu/wiki/Main_Page)：The read operation timed out。
- [STM32MP25_Discovery_kits_-_Starter_Package](https://wiki.stmicroelectronics.cn/stm32mpu/wiki/STM32MP25_Discovery_kits_-_Starter_Package)：HTTP Error 567: Unknown Status。
- [stm32mp257f-dk.html](https://www.st.com/en/evaluation-tools/stm32mp257f-dk.html#overview)：HTTP Error 567: Unknown Status。
- [stm32mp257f.html](https://www.st.com/en/microcontrollers-microprocessors/stm32mp257f.html)：HTTP Error 567: Unknown Status。
- [mb1605-mp257f-c01-schematic.pdf](https://www.st.com/resource/en/schematic_pack/mb1605-mp257f-c01-schematic.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P049_STM32MP215F-DK_Evaluation_Board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P051_STM32MP257F-EV1_Evaluation_Board.md)
