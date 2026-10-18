---
id: learning.zephyr-docs.boards-andes-antmicro.page-4
title: Myra SiP Baseboard
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/antmicro/myra_sip_baseboard/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="myra_sip_baseboard"></a>

# 第4章\_Myra系统级封装底板（SiP Baseboard）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/antmicro/myra_sip_baseboard/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/myra_sip_baseboard.webp](images/myra_sip_baseboard.webp)](images/myra_sip_baseboard.webp)

Myra系统级封装底板（SiP Baseboard）

名称（Name）：

`myra_sip_baseboard`

厂商（Vendor）：

[Antmicro](https://docs.zephyrproject.org/latest/boards/index.html#vendor=antmicro)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[myra](https://docs.zephyrproject.org/latest/boards/index.html#soc=myra)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/antmicro/myra_sip_baseboard/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Myra SiP Baseboard采用Antmicro的Myra系统级封装（SiP），集成STM32G491REI6微控制器、128 kB铁电随机存储器（FRAM）和FTDI FT231XQ USB转UART转换器。开发板配有温度、湿度和压力传感器，用于监测服务器机房的环境。

传感器位于可从主PCB分离的独立区域，可直接安装到需要的位置。开发板提供用于数据记录（Data Logging）的本地存储，以及防止数据丢失的备用电池（Battery Backup），可作为环境参数监测概念验证（PoC）方案的组成部分。

主要特性包括：


- STM32G491REI6微控制器，Cortex-M4内核、170 MHz
- 128 KB富士通铁电随机存储器（Fujitsu FRAM）
- FTDI FT231XQ USB转UART转换器（Converter）
- 50 × 26.5 mm印制电路板（PCB）
- USB-C接口，用于数据和供电
- SHT45温湿度传感器（Temperature / Humidity Sensor）
- BME280温度、湿度及压力传感器
- QWIIC接口，用于外设扩展（Peripheral Expansion）
- 带备用电池的实时时钟（RTC）

更多开发板信息见[Antmicro开放硬件门户（Open Hardware Portal）](https://openhardware.antmicro.com/boards/environment-sensor-sip-baseboard)。

<a id="hardware"></a>

## 硬件（Hardware）

Myra系统级封装（SiP）提供以下硬件：


- STM32G491REI6微控制器（MCU）：


  - ARM Cortex-M4 CPU，带浮点单元（FPU），最高170 MHz
  - 时钟源（Clock Sources）：


    - 4–48 MHz高速外部晶体振荡器（HSE）
    - 用于实时时钟（RTC）的32 kHz低速外部晶体振荡器（LSE）
    - 内部16 MHz RC振荡器，精度±1%
    - 内部低功耗32 kHz RC振荡器，精度±5%
    - 两个锁相环（PLL），用于系统时钟、USB、音频和ADC
  - 实时时钟（RTC），带硬件日历、闹钟和校准功能
  - 定时器（Timers）：


    - 一个32位定时器及两个16位定时器，最多提供四路输入捕获／输出比较／脉宽调制（IC/OC/PWM），或脉冲计数器及正交增量编码器（Quadrature / Incremental Encoder）输入
    - 三个16位高级电机控制定时器（Advanced Motor Control Timers），最多八路PWM通道，支持死区生成（Dead Time Generation）和紧急停止（Emergency Stop）
    - 一个16位定时器，带两路IC/OC和一路互补输出／PWM（OCN/PWM），支持死区生成和紧急停止
    - 两个看门狗定时器（Watchdog Timers），分别为独立看门狗和窗口看门狗
    - 两个16位基本定时器（Basic Timers）
    - 系统节拍定时器（SysTick Timer）
    - 一个低功耗定时器（Low-Power Timer）
  - I/O：最多86个高速I/O，多数耐受5 V
  - Memory:


    - 512 KB闪存，带纠错码（ECC）及专有代码读出保护（PCROP）
    - 96 KB SRAM，其中32 KB带硬件奇偶校验（Hardware Parity Check）
  - 模拟外设（Analog Peripherals）：


    - 三个16位模数转换器（ADC），最多36个通道，支持硬件过采样（Oversampling），分辨率最高16位
    - 四路12位数模转换器（DAC）通道
    - 四个超高速轨到轨模拟比较器（Rail-to-Rail Analog Comparators）
    - 四个运算放大器，内置可编程增益放大器（PGA）
    - 内部温度传感器和参考电压源，支持2.048 V、2.5 V及2.9 V三种输出电压
  - 通信接口（Communication Interfaces）：


    - 两个支持灵活数据速率的FDCAN控制器
    - 三路I2C快速增强模式（Fast Mode Plus），1 Mbit/s，20 mA灌电流（Current Sink），支持SMBus/PMBus
    - 五路USART/UART，支持ISO 7816、LIN、IrDA及调制解调器控制（Modem Control）
    - 一路低功耗UART（LPUART）
    - 三路SPI接口，其中两路复用半双工I²S
    - 一路串行音频接口（SAI）
    - USB 2.0全速，支持链路电源管理（LPM）和电池充电检测（BCD）
    - 红外接口（IRTIM / Infrared Interface）
    - USB Type-C™／USB电力传输（UCPD / USB Power Delivery）
  - 其他外设（Other Peripherals）：


    - 16通道DMA控制器
    - 真随机数发生器（RNG / True Random Number Generator）
    - 循环冗余校验计算单元（CRC），96位唯一标识（Unique ID）
    - 开发支持：串行线调试（SWD）、JTAG及嵌入式跟踪宏单元（Embedded Trace Macrocell™）
    - 符合ECOPACK2®要求的封装（Packages）
- 128 KB富士通MB85RS1MT铁电随机存储器（FRAM）：用于数据记录的本地存储，支持非易失性数据保存。
- FTDI FT231XQ USB转UART转换器：提供可靠的USB至UART接口。

STM32G491RE的更多信息见：


- [ST网站上的STM32G491RE（www.st.com）](https://www.st.com/en/microcontrollers-microprocessors/stm32g491re.html)

<a id="other-board-s-peripherals"></a>

### 开发板的其他外设：


- USB-C接口：用于数据和供电。
- SHT45传感器（Sensor）：


  - 相对湿度精度（Relative Humidity Accuracy）：±1.0% RH
  - 工作湿度范围：0–100% RH
  - 温度精度：±0.1 °C
  - 工作温度范围：−40 °C至125 °C
- BME280传感器（Sensor）：


  - 相对湿度精度：±3% RH
  - 温度精度：±1 C（单位依原文保留）
  - 压力精度：±1 hPa
  - 工作温度范围：−40 °C至85 °C
  - 压力范围：300–1100 hPa
- QWIIC接口：便于扩展外设。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`myra_sip_baseboard`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="myra_sip_baseboard-hw-features"></a>

<a id="myra_sip_baseboard-myra_sip_baseboard/myra-hw-features-section"></a>

#### `myra_sip_baseboard/myra`目标（Target）

<a id="myra_sip_baseboard-myra_sip_baseboard/myra-hw-features-panel"></a>

<a id="myra_sip_baseboard-myra_sip_baseboard/myra-hw-features-memory"></a>

该开发板目标的片上存储容量：112 KiB RAM、512 KiB Flash。

<a id="myra_sip_baseboard-myra_sip_baseboard/myra-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L35">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>STM32模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L111">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g491.dtsi?plain=1#L68">已禁用：1</a>）</td>
<td><a href="../hardware/P839_STM32模数转换器绑定.md#dtbinding-st-stm32-adc"><code>st,stm32-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>STM32 FDCAN灵活数据速率CAN控制器（CAN FD Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L437">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g491.dtsi?plain=1#L13">已禁用：1</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P012_st_stm32-fdcan.md#std-dtcompatible-st-stm32-fdcan"><code>st,stm32-fdcan</code></a></td>
</tr>
<tr>
<td rowspan="5">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>STM32复位和时钟控制器（RCC / Reset and Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L217">已启用：1</a>）</td>
<td><a href="../timer_reference/P126_STM32复位与时钟控制绑定.md#dtbinding-st-stm32-rcc"><code>st,stm32-rcc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 外部高速时钟（HSE Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L65">已启用：1</a>）</td>
<td><a href="../timer_reference/P129_STM32高速外部时钟绑定.md#dtbinding-st-stm32-hse-clock"><code>st,stm32-hse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L78">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L71">已禁用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低速外部时钟（LSE Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L85">已启用：1</a>）</td>
<td><a href="../timer_reference/P130_STM32低速外部时钟绑定.md#dtbinding-st-stm32-lse-clock"><code>st,stm32-lse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32G4主锁相环（Main PLL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L100">已启用：1</a>）</td>
<td><a href="../timer_reference/P143_STM32G4锁相环时钟绑定.md#dtbinding-st-stm32g4-pll-clock"><code>st,stm32g4-pll-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>STM32G4系列比较器（Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L846">已禁用：4</a>）</td>
<td><a href="../hardware/P740_STM32G4比较器绑定.md#dtbinding-st-stm32g4-comp"><code>st,stm32g4-comp</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>STM32 计数器（Counters）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L477">已禁用：11</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P007_st_stm32-counter.md#std-dtcompatible-st-stm32-counter"><code>st,stm32-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>STM32 CRC 计算单元（Calculation Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L882">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P011_st_stm32-crc.md#std-dtcompatible-st-stm32-crc"><code>st,stm32-crc</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>STM32 系列数模转换器（DAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L144">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L152">已禁用：1</a>）</td>
<td><a href="../hardware/P760_STM32数模转换器绑定.md#dtbinding-st-stm32-dac"><code>st,stm32-dac</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>STM32直接存储器访问控制器（DMA Controller，V2）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L741">已禁用：2</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P008_st_stm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2"><code>st,stm32-dma-v2</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 DMA 多路复用控制器（DMAMUX Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L758">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P011_st_stm32-dmamux.md#std-dtcompatible-st-stm32-dmamux"><code>st,stm32-dmamux</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 系列闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L160">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P011_st_stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller"><code>st,stm32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用输入输出控制器（GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L252">已启用：7</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P029_st_stm32-gpio.md#std-dtcompatible-st-stm32-gpio"><code>st,stm32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>STM32 I2C V2 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L368">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L380">已禁用：2</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P008_st_stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2"><code>st,stm32-i2c-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>STM32 串行音频接口块控制器（SAI Block Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L777">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P017_st_stm32-sai.md#std-dtcompatible-st-stm32-sai"><code>st,stm32-sai</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/antmicro/myra_sip_baseboard/myra_sip_baseboard.dts?plain=1#L42">已启用：1</a>）</td>
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
<td>STM32 外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L229">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P001_st_stm32-exti.md#std-dtcompatible-st-stm32-exti"><code>st,stm32-exti</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/antmicro/myra_sip_baseboard/myra_sip_baseboard.dts?plain=1#L25">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/antmicro/myra_sip_baseboard/myra_sip_baseboard.dts?plain=1#L34">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>STM32闪存（Flash Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L170">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P016_st_stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash"><code>st,stm32-nv-flash</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>富士通MB85RSXX SPI铁电随机存储器（FRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/antmicro/myra.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P015_fujitsu_mb85rsxx.md#std-dtcompatible-fujitsu-mb85rsxx"><code>fujitsu,mb85rsxx</code></a></td>
</tr>
<tr>
<td rowspan="1">非易失存储器（NVMEM）</td>
<td>片上（On-Chip）</td>
<td>非易失存储器固定布局（Fixed Layout for Non-Volatile Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L191">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P009_fixed-layout.md#std-dtcompatible-fixed-layout"><code>fixed-layout</code></a></td>
</tr>
<tr>
<td rowspan="1">运算放大器（OPAMP）</td>
<td>片上（On-Chip）</td>
<td>STM32G4运算放大器（OPAMP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L804">已禁用：3</a>）</td>
<td><a href="../hardware/P734_STM32G4运算放大器绑定.md#dtbinding-st-stm32g4-opamp"><code>st,stm32g4-opamp</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>STM32 嵌入式非易失一次性可编程存储器（NVM OTP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L187">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L180">已禁用：1</a>）</td>
<td><a href="../otp_binding_reference/P010_st_stm32-nvm-otp.md#std-dtcompatible-st-stm32-nvm-otp"><code>st,stm32-nvm-otp</code></a></td>
</tr>
<tr>
<td rowspan="1">物理层（PHY）</td>
<td>片上（On-Chip）</td>
<td>用于所有内置于 USB IP 的 USB 收发器（USB Transceivers）的绑定。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L917">已启用：1</a>）</td>
<td><a href="../phy_binding_reference/P008_usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv"><code>usb-nop-xceiv</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>STM32 引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L245">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P004_st_stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl"><code>st,stm32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>STM32 脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L505">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L471">已禁用：8</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P011_st_stm32-pwm.md#std-dtcompatible-st-stm32-pwm"><code>st,stm32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">四线串行外设接口（QSPI）</td>
<td>片上（On-Chip）</td>
<td>STM32 四线串行外设接口控制器（QSPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g491.dtsi?plain=1#L103">已禁用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P011_st_stm32-qspi.md#std-dtcompatible-st-stm32-qspi"><code>st,stm32-qspi</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 复位与时钟控制器（Reset and Clock Control，RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L223">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P017_st_stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl"><code>st,stm32-rcc-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>STM32 随机数生成器（Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L719">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P016_st_stm32-rng.md#std-dtcompatible-st-stm32-rng"><code>st,stm32-rng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>STM32 实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L708">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P014_st_stm32-rtc.md#std-dtcompatible-st-stm32-rtc"><code>st,stm32-rtc</code></a></td>
</tr>
<tr>
<td rowspan="6">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>BME280集成环境传感器（Environmental Sensor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/antmicro/myra_sip_baseboard/myra_sip_baseboard.dts?plain=1#L115">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P011_bosch_bme280.md#std-dtcompatible-bosch-bme280"><code>bosch,bme280</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Sensirion SHT4x湿度与温度传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/antmicro/myra_sip_baseboard/myra_sip_baseboard.dts?plain=1#L120">已启用：1</a>）</td>
<td><a href="../sensor_realtek_rohm_sensirion_binding_reference/P025_sensirion_sht4x.md#std-dtcompatible-sensirion-sht4x"><code>sensirion,sht4x</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 正交解码器（Quadrature Decoder）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L482">已禁用：6</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P028_st_stm32-qdec.md#std-dtcompatible-st-stm32-qdec"><code>st,stm32-qdec</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系列温度节点（TEMP），用于以两个温度点完成生产校准的传感器。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L891">已启用：1</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P029_st_stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal"><code>st,stm32-temp-cal</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 参考电压（VREF+）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L902">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g491.dtsi?plain=1#L114">已禁用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P003_st_stm32-vref.md#std-dtcompatible-st-stm32-vref"><code>st,stm32-vref</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 电池电压（VBAT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L910">已启用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P001_st_stm32-vbat.md#std-dtcompatible-st-stm32-vbat"><code>st,stm32-vbat</code></a></td>
</tr>
<tr>
<td rowspan="3">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L309">已禁用：3</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P016_st_stm32-usart.md#std-dtcompatible-st-stm32-usart"><code>st,stm32-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L336">已禁用：2</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P015_st_stm32-uart.md#std-dtcompatible-st-stm32-uart"><code>st,stm32-uart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低功耗通用异步收发器（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L345">已启用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P014_st_stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart"><code>st,stm32-lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">系统管理总线（SMbus）</td>
<td>片上（On-Chip）</td>
<td>STM32 系统管理总线控制器（SMBus Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L922">已禁用：3</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P013_st_stm32-smbus.md#std-dtcompatible-st-stm32-smbus"><code>st,stm32-smbus</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>带嵌入式接收和发送先进先出队列（Rx / Tx FIFOs）的STM32 SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L415">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L404">已禁用：2</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P009_st_stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo"><code>st,stm32-spi-fifo</code></a></td>
</tr>
<tr>
<td rowspan="1">USB Type-C 端口控制器（USB Type-C Port Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 USB Type-C／电力传输（Power Delivery）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L769">已禁用：1</a>）</td>
<td><a href="../usbc_tcpc_binding_reference/P005_st_stm32-ucpd.md#std-dtcompatible-st-stm32-ucpd"><code>st,stm32-ucpd</code></a></td>
</tr>
<tr>
<td rowspan="3">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低功耗定时器（LPTIM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L448">已启用：1</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P007_st_stm32-lptim.md#std-dtcompatible-st-stm32-lptim"><code>st,stm32-lptim</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 定时器（Timers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L489">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L460">已禁用：8</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P008_st_stm32-timers.md#std-dtcompatible-st-stm32-timers"><code>st,stm32-timers</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>STM32 USB控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L727">已禁用：1</a>）</td>
<td><a href="../usb_stm32_audio_binding_reference/P006_st_stm32-usb.md#std-dtcompatible-st-stm32-usb"><code>st,stm32-usb</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>STM32 看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L354">已启用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P001_st_stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog"><code>st,stm32-watchdog</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系统窗口看门狗（System Window Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L360">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P002_st_stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog"><code>st,stm32-window-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

Antmicro Myra SiP Baseboard为外设提供以下默认引脚映射（Pin Mappings）：


- `LPUART_1_TX : PA2`
- `LPUART_1_RX : PA3`
- `I2C_1_SCL : PB8`
- `I2C_1_SDA : PB9`
- `SPI_CS2 : PB2`
- `SPI_CS3 : PA7`
- `SPI_2_SCK : PB13`
- `SPI_2_MISO : PB14`
- `SPI_2_MOSI : PB15`
- `PWM_2_CH1 : PA5`
- `USER_PB : PC13`
- `LD2 : PA5`
- `ADC1_IN1 : PA0`
- `DAC1_OUT1 : PA4`
- `USB_MCU_N : PA11`
- `USB_MCU_P : PA12`
- `SWDIO-JMTS : PA13`
- `SWCLK-JTCK : PA14`
- `JTDI : PA15`
- `JTDO : PB3`
- `JTRST : PB4`
- FRAM_HOLD，低电平有效（ACTIVE LOW）：PB10
- FRAM_WP，低电平有效（ACTIVE LOW）：PB11
- FRAM_CS，低电平有效（ACTIVE LOW）：PB12
- `GPIO_PC10 : PC10`
- `GPIO_PC11 : PC11`
- `GPIO_PC12 : PC12`
- `PF0_OSC : PF0`

<a id="system-clock"></a>

### 系统时钟（System Clock）

系统时钟可由内部或外部振荡器驱动，也可由主锁相环（PLL）时钟驱动。默认选择增强模式（Boost Mode），使用170 MHz PLL时钟，其输入来自8 MHz高速外部振荡器（HSE）。虽然HSE振荡器通常支持最高48 MHz，但在此配置中明确设为8 MHz。

<a id="serial-port"></a>

### 串口（Serial Port）

Myra SiP Baseboard有五路U(S)ART。Zephyr控制台输出分配给LPUART1，默认设置为115200 8N1。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`myra_sip_baseboard`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

`myra_sip_baseboard`开发板目标上的应用可按通常方式构建和烧录，详情见[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)及[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)。

<a id="flashing"></a>

## 烧录（Flashing）

此开发板具有USB-JTAG接口，可使用OpenOCD。

通过USB端口将Myra SiP Baseboard连接到主机，然后构建并烧录应用。以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例。

```text
# From the root of the zephyr repository
west build -b myra_sip_baseboard samples/hello_world
west flash
```

随后运行主机串口程序连接Myra SiP Baseboard，例如使用picocom：

```text
$ picocom /dev/ttyUSB0 -b 115200
```

警告（Warning）

开发板只有一个端口，同时用于编程和控制台。因此，建议将`CONFIG_BOOT_DELAY`设置为一个任意延迟值；在设备上运行Twister测试时尤其需要注意，并应同时使用`--flash-before`和`--device-flash-timeout=120`选项。

```text
$ scripts/twister --device-testing --device-serial /dev/ttyUSB0 --device-serial-baud 115200 -p myra_sip_baseboard --flash-before --device-flash-timeout=120 -v
```

<a id="debugging"></a>

## 调试（Debugging）

可以按常规方式调试应用。下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b myra_sip_baseboard samples/hello_world
west debug
```

## 译注

原文硬件说明写96 KB SRAM，自动生成目标表写112 KiB RAM；ADC、UART和USB-JTAG支持等描述也按原文保留，未根据其他板卡或器件手册替换。本页不是本仓库的硬件实验记录。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [stm32g491re.html](https://www.st.com/en/microcontrollers-microprocessors/stm32g491re.html)：HTTP Error 567: Unknown Status。

---

[上一章](P003_Antmicro.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_STM32H7_HDMI_Board.md)
