---
id: learning.zephyr-docs.boards-st-discovery-eval.page-49
title: STM32MP215F-DK Evaluation Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/st/stm32mp215f_dk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="stm32mp215f_dk"></a>

# 第49章\_STM32MP215F-DK评估板（Evaluation Board）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/st/stm32mp215f_dk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/stm32mp215f_dk.webp](images/stm32mp215f_dk.webp)](images/stm32mp215f_dk.webp)

STM32MP215F-DK评估板（Evaluation Board）

名称（Name）：

`stm32mp215f_dk`

厂商（Vendor）：

[意法半导体（STMicroelectronics）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=st)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[stm32mp215fxx](https://docs.zephyrproject.org/latest/boards/index.html#soc=stm32mp215fxx)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32mp215f_dk/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

STM32MP215F-DK Discovery套件是STM32MP215F的完整演示及开发平台，该微处理器基于1.5 GHz Arm Cortex-A35及Cortex-M33。Zephyr移植为运行于M33，作为A35的协处理器。

<a id="features"></a>

### 功能（Features）：


- VFBGA273封装STM32MP215FAN3，包含最高1.5 GHz的Arm Cortex-A35及300 MHz Cortex-M33
- 意法半导体电源管理芯片STPMIC2L
- 16 Gbit LPDDR4 DRAM
- 100 Mbit/s以太网RMII
- USB 2.0总线供电
- 4个用户LED
- 2个用户键、1个防篡改键及1个复位键
- 唤醒按键
- 四个启动引脚开关（Boot Pin Switches）
- 开发板连接器（Board Connectors）：


  - 以太网RJ45接口
  - USB 2.0 Type-C接口
  - microSD™卡座
  - 双通道MIPI CSI-2®摄像头模块扩展连接器
  - LTDC显示连接器
  - M.2 E-Key连接器，支持Wi-Fi及Bluetooth SDIO模块
  - GPIO扩展连接器
  - VBAT备份电源
  - MIPI10 JTAG连接器
  - 用于调试的STDC14连接器
- 基于上游开源Linux的STM32 MPU OpenSTLinux发行版，以及带示例的STM32CubeMP2软件
- 开发环境包括Linux Yocto Project、Buildroot及STM32CubeIDE

<a id="id3"></a>

更多信息见[STM32MP215F-DK网站](https://www.st.com/en/evaluation-tools/stm32mp215f-dk.html#overview)[注1](#id2)。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="cores"></a>

### 内核（Cores）：


- 64位单核Arm Cortex-A35，最高1.5 GHz；每核32 Kbyte指令L1缓存及32 Kbyte数据L1缓存，128 Kbyte L2缓存，支持Arm NEON及TrustZone
- 32位Arm Cortex-M33，带FPU／MPU，最高300 MHz；16 Kbyte指令及16 Kbyte数据L1缓存，支持TrustZone

<a id="memories"></a>

### 存储器（Memories）：


- 外部DDR最高4 Gbytes，支持16位DDR3L-1600、DDR4-1600及LPDDR4-1600
- 456 Kbyte内部SRAM：256 Kbyte AXI SYSRAM、64 Kbyte AHB SRAM、备份域中带ECC的128 Kbyte AHB SRAM及8 Kbyte SRAM
- 1路Octo-SPI存储器接口
- 灵活外部存储器控制器，数据总线最大16位；通过并行接口连接外部集成电路（IC）及支持最高8位纠错码（ECC）的单层单元（SLC）NAND存储器

<a id="security-safety"></a>

### 信息安全／功能安全（Security/Safety）：


- 安全启动、TrustZone外设、主动防篡改、环境监测、显示安全图层及硬件加速器
- 完整资源隔离框架（Resource Isolation Framework）

<a id="reset-and-power-management"></a>

### 复位及电源管理：


- 多分区I/O供电：1.71～1.95 V及2.7／3.0～3.6 V
- 上电复位POR、掉电复位PDR、可编程电压检测PVD及欠压复位BOR
- 用于RETRAM、BKPSRAM及VSW的片上LDO与电源开关
- Cortex-A35专用电源
- 内部温度传感器
- 低功耗模式：睡眠Sleep、停止Stop及待机Standby
- 待机模式保留DDR存储器内容
- 用于配套PMIC芯片的控制接口

<a id="clock-management"></a>

### 时钟管理（Clock Management）：


- 内部振荡器：64 MHz HSI、16 MHz MSI及32 kHz LSI
- 外部振荡器：16～48 MHz HSE及32.768 kHz LSE
- 最多7个支持小数模式的PLL；原文随后连接“通用输入输出”标题
- 最多123个支持中断的安全I/O端口
- 最多6个唤醒输入
- 最多7个防篡改输入及5个主动防篡改输出；原文随后连接“互连矩阵”标题
- 总线矩阵（Bus Matrices）
- 128／64／32位STNoC互连，最高600 MHz
- 32位Arm AMBA AHB互连，最高300 MHz
- 3个DMA控制器，用于减轻CPU负载
- 总共48个物理通道
- 3个双主端口高性能通用DMA控制器HPDMA，每个16通道

<a id="up-to-37-communication-peripherals"></a>

### 最多37个通信外设：


- 3路I2C FM+，1 Mbit/s，支持SMBus／PMBus
- 3路I3C，12.5 Mbit/s
- 3路UART、4路USART及1路LPUART；USART支持12.5 Mbit/s、ISO7816、LIN、IrDA及SPI
- 6路SPI，50 Mbit/s，其中3路通过内部音频PLL或外部时钟实现满足音频精度的全双工I2S；另可由OCTOSPI提供1路、USART提供4路
- 4路SAI，支持I2S、PDM及SPDIF发送的立体声音频
- SPDIF接收，4个输入
- 3路SDMMC，最高8位，支持SD／eMMC／SDIO
- 最多2个支持CAN FD的CAN控制器，其中1个支持时间触发CAN（TTCAN）
- 1路USB 2.0高速主机，内置480 Mbit/s PHY
- 1路USB 2.0高速双数据角色接口，内置480 Mbit/s PHY
- 最多2路千兆以太网
- 支持时间敏感网络TSN、IEEE 1588v2硬件及MII／RMII／RGMII
- 摄像头接口1：500万像素、30 fps
- MIPI CSI-2，2条数据通道，每条最高2.5 Gbit/s
- 8～16位并行接口，最高120 MHz
- 支持RGB、YUV、JPG及RawBayer，带轻量图像信号处理器ISP
- Lite-ISP支持去马赛克、缩小及裁剪，具有3条像素处理管线
- 摄像头接口2：100万像素、15 fps
- 8～14位并行接口，最高80 MHz
- 支持RGB、YUV及JPG
- 裁剪（Cropping）
- 数字并行接口，最多16位输入或输出

<a id="analog-peripherals"></a>

### 5个模拟外设：


- 2个ADC，最高12位分辨率，每个最高5 Msps，最多23个通道
- 内部数字温度传感器DTS
- 1个多功能数字滤波器MDF，最多4通道／4滤波器
- ADC参考电压可用内部VREFBUF或外部VREF+

<a id="graphics"></a>

### 图形（Graphics）：


- LCD-TFT控制器，最高24位并行RGB888
- 最高全高清FHD，1920×1080、60 fps
- 3个图层，包含1个安全图层
- 支持YUV

<a id="up-to-28-timers-and-5-watchdogs"></a>

### 最多28个定时器及5个看门狗：


- 4个32位定时器，最多支持4路IC/OC/PWM、脉冲计数及正交增量编码器输入
- 两个16位高级电机控制定时器（Advanced Motor Control Timers）
- 10个16位通用定时器，含2个不带PWM的基本定时器
- 五个16位低功耗定时器
- 安全RTC，具有亚秒精度及硬件日历
- 4个Cortex-A35系统定时器：安全、非安全、虚拟及虚拟机监控器
- 2个Cortex-M33 SysTick定时器：安全及非安全
- 5个看门狗：4个独立看门狗及1个窗口看门狗

<a id="hardware-acceleration"></a>

### 硬件加速（Hardware Acceleration）：


- 2个密码处理器CRYP，支持AES-128／192／256及DES／TDES
- 带侧信道攻击防护（SCA）的安全AES-256
- 带SCA防护的RSA、ECC及ECDSA
- 2个HASH单元，支持SHA-1、SHA-224、SHA-256、SHA3及HMAC
- 2个真随机数发生器
- 循环冗余校验计算单元（CRC Calculation Unit）
- DDR即时加解密，AES-128及AES-256
- Octo-SPI Flash即时解密OTFDEC，AES-128

<a id="debug-mode"></a>

### 调试模式（Debug Mode）：


- Arm CoreSight 跟踪与调试（Trace and Debug），支持 SWD 和 JTAG 接口。

更多STM32MP215F信息见：


- <a id="id5"></a>

  ST官网的STM32MP215F产品页[注2](#id4)（[STM32MP215F在ST官网的产品页](https://www.st.com/en/microcontrollers-microprocessors/stm32mp215f.html)）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`stm32mp215f_dk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="stm32mp215f_dk-hw-features"></a>

<a id="stm32mp215f_dk-stm32mp215f_dk/stm32mp215fxx/m33-hw-features-section"></a>

#### `stm32mp215f_dk/stm32mp215fxx/m33`目标（Target）

<a id="stm32mp215f_dk-stm32mp215f_dk/stm32mp215fxx/m33-hw-features-panel"></a>

<a id="stm32mp215f_dk-stm32mp215f_dk/stm32mp215fxx/m33-hw-features-memory"></a>

该开发板目标的片上存储容量：8 MiB RAM、8 MiB Flash。

<a id="stm32mp215f_dk-stm32mp215f_dk/stm32mp215fxx/m33-hw-features-table"></a>

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
<td>STM32H7系列及兼容器件的FDCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L152">已禁用：2</a>）</td>
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
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>STM32MP2 GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L67">已启用：12</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P030_st_stm32mp2-gpio.md#std-dtcompatible-st-stm32mp2-gpio"><code>st,stm32mp2-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>STM32 I2C V2 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp211_m33.dtsi?plain=1#L47">已禁用：3</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P008_st_stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2"><code>st,stm32-i2c-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>STM32H5 I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L286">已禁用：3</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P010_st_stm32-i3c.md#std-dtcompatible-st-stm32-i3c"><code>st,stm32-i3c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32mp215f_dk/stm32mp215f_dk_stm32mp215fxx_m33.dts?plain=1#L32">已启用：1</a>）</td>
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
<td>STM32 外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp211_m33.dtsi?plain=1#L13">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32mp215f_dk/stm32mp215f_dk_stm32mp215fxx_m33.dts?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>STM32 引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L60">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P004_st_stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl"><code>st,stm32-pinctrl</code></a></td>
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
<td>STM32 通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L254">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L262">已禁用：2</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P015_st_stm32-uart.md#std-dtcompatible-st-stm32-uart"><code>st,stm32-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>STM32H7 串行外设接口控制器（SPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L170">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L182">已禁用：5</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P013_st_stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi"><code>st,stm32h7-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
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

原文说明STM32MP215F-DK评估板原理图尚未提供。

<a id="system-clock"></a>

### 系统时钟（System Clock）

<a id="cortex-a35"></a>

#### Cortex®-A35

Zephyr尚不支持。

<a id="cortex-m33"></a>

#### Cortex®-M33

Cortex-M33内核配置为300 MHz时钟。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`stm32mp215f_dk`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

在STM32MP215F-DK上运行Zephyr前，须先为Cortex-A35配置Linux环境。M33作为协处理器运行Zephyr，需要A35通过remoteproc加载并启动固件。

<a id="id10"></a>

<a id="id12"></a>

可按入门软件包[Starter Package](https://wiki.st.com/stm32mpu/wiki/STM32MP21_Discovery_kits_-_Starter_Package) [注4](#id9)安装官方ST OpenSTLinux发行版；更多步骤见[STM32MPU Wiki](https://wiki.st.com/stm32mpu/wiki/Main_Page) [注5](#id11)。

<a id="loading-the-firmware"></a>

### 加载固件（Loading the Firmware）

安装OpenSTLinux后，当前发行版由Cortex-A35负责将Zephyr镜像加载到DDR及／或SRAM，并启动Cortex-M33。应用可用west构建，下面以[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)为例。

```text
# From the root of the zephyr repository
west build -b stm32mp215f_dk/stm32mp215fxx/m33 samples/basic/blinky
```

<a id="id7"></a>

将固件复制到开发板文件系统，再用Linux remoteproc框架启动；详情见“[STM32MP215F启动Cortex-M33固件](https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs)”[注3](#id6)。

<a id="debugging"></a>

### 调试（Debugging）

<a id="id14"></a>

可用社区／主线[OpenOCD项目](https://github.com/openocd-org/openocd)[注6](#id13)及GDB调试，原文测试提交为fc566d7。其tcl/target/st/stm32mp21x.cfg提供STM32MP21x支持；上游没有现成的board/stm32mp21x_dk.cfg，因此本开发板提供support/openocd_stm32mp215f_dk_m33.cfg。

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
west build -b stm32mp215f_dk/stm32mp215fxx/m33 samples/basic/blinky -- -DOPENOCD=/path/to/openocd/src/openocd -DSTM32MP_OPENOCD_SCRIPTS=/path/to/openocd/tcl
```


- <a id="id8"></a>

  将固件复制到板上，并用remoteproc加载及启动，步骤见“[STM32MP215F启动Cortex-M33固件](https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs)”[注3](#id6)；橙色LED应闪烁。
- 附加到目标：

```text
$ west attach
```

Cortex-A35及Cortex-M33共用物理调试／SWD端口，但对应不同访问端口（Access Ports）。板卡配置同时启用两者并固定GDB端口，使west attach稳定连接M33的3334端口，A35仍可从3333端口访问，例如gdb-multiarch -ex "target extended-remote :3333"。

<a id="references"></a>

### 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [STM32MP215F-DK官方产品概述](https://www.st.com/en/evaluation-tools/stm32mp215f-dk.html#overview)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.st.com/en/microcontrollers-microprocessors/stm32mp215f.html](https://www.st.com/en/microcontrollers-microprocessors/stm32mp215f.html)

<a id="id6"></a>

〔3〕 ([1](#id7),[2](#id8)) [https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs](https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs)

<a id="id9"></a>

〔[4](#id10)〕 [https://wiki.st.com/stm32mpu/wiki/STM32MP21_Discovery_kits_-_Starter_Package](https://wiki.st.com/stm32mpu/wiki/STM32MP21_Discovery_kits_-_Starter_Package)

<a id="id11"></a>

〔[5](#id12)〕 [https://wiki.st.com/stm32mpu/wiki/Main_Page](https://wiki.st.com/stm32mpu/wiki/Main_Page)

<a id="id13"></a>

〔[6](#id14)〕 [https://github.com/openocd-org/openocd](https://github.com/openocd-org/openocd)

## 译注

Zephyr运行于300 MHz M33，须由A35上的Linux remoteproc加载启动；原文OpenOCD测试提交fc566d7，M33/A35的GDB端口分别3334/3333。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [Linux_remoteproc_framework_overview](https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs)：The read operation timed out。
- [Main_Page](https://wiki.st.com/stm32mpu/wiki/Main_Page)：The read operation timed out。
- [STM32MP21_Discovery_kits_-_Starter_Package](https://wiki.st.com/stm32mpu/wiki/STM32MP21_Discovery_kits_-_Starter_Package)：The read operation timed out。
- [stm32mp215f-dk.html](https://www.st.com/en/evaluation-tools/stm32mp215f-dk.html#overview)：HTTP Error 567: Unknown Status。
- [stm32mp215f.html](https://www.st.com/en/microcontrollers-microprocessors/stm32mp215f.html)：HTTP Error 567: Unknown Status。

---

[上一章](P048_STM32MP157x-DK2_Discovery.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P050_STM32MP257F-DK_Discovery_Kit.md)
