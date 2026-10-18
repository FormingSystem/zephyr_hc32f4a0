---
id: learning.zephyr-docs.boards-adi-max32-max78-sdp.page-12
title: MAX32670EVKIT
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/adi/max32670evkit/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="max32670evkit"></a>

# 第12章\_MAX32670EVKIT

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/adi/max32670evkit/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/max32670evkit.webp](images/max32670evkit.webp)](images/max32670evkit.webp)

MAX32670EVKIT

名称（Name）：

`max32670evkit`

厂商（Vendor）：

[Analog Devices, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=adi)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[max32670](https://docs.zephyrproject.org/latest/boards/index.html#soc=max32670)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32670evkit/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

MAX32670评估套件（EV Kit）提供一个平台，用于评估MAX32670的能力。MAX32670是一款超低功耗、经济型、高可靠性32位微控制器，支持复杂的传感器处理设计，同时兼顾电池续航。它将灵活多用的电源管理单元（Power Management Unit）与强大的Arm® Cortex®-M4内核及浮点单元（FPU）结合。对于基于8位或16位微控制器的既有设计，MAX32670也提供了一条便捷、成本优化的升级路径。

Zephyr移植版本运行在MAX32670微控制器（MCU）上。

<a id="hardware"></a>

## 硬件（Hardware）


- MAX32670微控制器（MCU）：


  - 面向低功耗、高可靠性设备的高能效微控制器


    - Arm Cortex-M4内核，带浮点单元（FPU），最高100 MHz
    - 384 KB闪存（Flash Memory），带纠错功能（Error Correction）
    - 160 KB SRAM，启用ECC时为128 KB，可选择在最低功耗模式下保留内容
    - 16 KB统一缓存（Unified Cache），带纠错码（ECC）
    - UART引导加载程序（Bootloader）

      > - 支持双电源或单电源运行（Dual- or Single-Supply Operation）
      > - 超低的0.9–1.1 V VCORE供电电压
      > - 内部低压差稳压器（LDO）支持1.7–3.6 V单电源运行
    - 宽工作温度范围：−40 °C至+105 °C
  - 灵活的时钟方案（Clocking Schemes）


    - 内部100 MHz高速振荡器（High-Speed Oscillator）
    - 内部7.3728 MHz低功耗和80 kHz超低功耗振荡器（Oscillators）
    - 16–32 MHz振荡器，需要外部晶体（External Crystal）
    - 32.768 kHz振荡器，需要外部晶体（External Crystal）
    - 内核外部时钟输入（External Clock Input）
    - LPUART和低功耗定时器（LPTMR）的外部时钟输入
  - 通过电源管理（Power Management）尽可能延长电池供电应用的运行时间


    - 0.9 V、最高12 MHz时，活动电流（Active Current）为44 μA/MHz
    - 1.1 V、最高100 MHz时，活动电流（Active Current）为50 μA/MHz
    - VDD = 1.8 V时，备份模式（BACKUP）下完整存储器保持电流为2.6 μA
    - VDD = 1.8 V时，超低功耗实时时钟（RTC）电流为350 nA
    - 由低功耗UART（LPUART）或低功耗定时器（LPTMR）唤醒
  - 通过合理的外设组合提供平台扩展能力（Platform Scalability）


    - 最多31个通用输入输出（I/O）引脚
    - 最多三路SPI主机／从机，最高50 MHz
    - 最多三路四线UART
    - 一路低功耗UART（LPUART）
    - 最多三路I2C主机／从机，支持3.4 Mbps高速模式
    - 八通道标准DMA控制器
    - 最多四个32位定时器（TMR）
    - 最多两个32位低功耗定时器（LPTMR）
    - 两个窗口看门狗定时器（Windowed Watchdog Timers）
    - 一路I2S从机（Slave），用于数字音频接口
  - 安全与完整性（Security and Integrity）


    - 可用的安全启动（Secure Boot）
    - AES 128/192/256硬件加速引擎（Hardware Acceleration Engine）
    - 32位循环冗余校验加速引擎（CRC Acceleration Engine）
- MAX32670EVKIT的优势与功能（Benefits and Features）：


  - USB 2.0 Micro-B转串行UART桥（Bridge）
  - 通过板载跳线选择UART0或UART3接口
  - 板载基于MAX32625PICO的调试器（Debugger）
  - 引导加载使能电路（Boot Load Enable Circuitry）
  - 通过0.1英寸间距排针访问SPI和I2C信号
  - 通过0.1英寸间距排针访问GPIO及其他信号
  - USB端口为开发板供电
  - 板载单电感多输出稳压器（SIMO Regulator）及低压差稳压器（LDO），为芯片和外设供电
  - 通过跳线分别测量所有芯片供电轨（IC Rails）的功耗
  - 两个通用LED和一个通用按键开关（Pushbutton Switch）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`max32670evkit`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="max32670evkit-hw-features"></a>

<a id="max32670evkit-max32670evkit/max32670-hw-features-section"></a>

#### `max32670evkit/max32670`目标（Target）

<a id="max32670evkit-max32670evkit/max32670-hw-features-panel"></a>

<a id="max32670evkit-max32670evkit/max32670-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、384 KiB Flash。

<a id="max32670evkit-max32670evkit/max32670-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="2">中央处理器（CPU）</td>
<td>片上（On-Chip）</td>
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MAX32 RV32内核（Core）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L32">已禁用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P002_adi_max32-rv32.md#std-dtcompatible-adi-max32-rv32"><code>adi,max32-rv32</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32 10位模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L241">已禁用：1</a>）</td>
<td><a href="../hardware/P861_ADIMAX32十位ADC绑定.md#dtbinding-adi-max32-adc-10b"><code>adi,max32-adc-10b</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L64">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L71">已禁用：5</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MAX32全局控制（Global Control）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L130">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P004_adi_max32-gcr.md#std-dtcompatible-adi-max32-gcr"><code>adi,max32-gcr</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32计数器（Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L260">已禁用：6</a>）</td>
<td><a href="../counter_binding_reference/P001_adi_max32-counter.md#std-dtcompatible-adi-max32-counter"><code>adi,max32-counter</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ADI MAX32兼容实时时钟计数器（Counter RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32670.dtsi?plain=1#L168">已启用：1</a>）</td>
<td><a href="../counter_binding_reference/P002_adi_max32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter"><code>adi,max32-rtc-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32直接存储器访问（DMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32670.dtsi?plain=1#L89">已启用：1</a>）</td>
<td><a href="../dma_binding_reference/P002_adi_max32-dma.md#std-dtcompatible-adi-max32-dma"><code>adi,max32-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>MAX32XXX闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L111">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P001_adi_max32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller"><code>adi,max32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>MAX32通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L175">已启用：2</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P011_adi_max32-gpio.md#std-dtcompatible-adi-max32-gpio"><code>adi,max32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32 I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L139">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L149">已禁用：2</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P001_adi_max32-i2c.md#std-dtcompatible-adi-max32-i2c"><code>adi,max32-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32670evkit/max32670evkit.dts?plain=1#L40">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32670evkit/max32670evkit.dts?plain=1#L26">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32 SEMA邮箱（Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L194">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P032_ADI硬件信号量邮箱绑定.md#dtbinding-adi-mbox-max32-sema"><code>adi,mbox-max32-sema</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L119">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>MAX32引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L169">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P001_adi_max32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl"><code>adi,max32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L265">已禁用：4</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P003_adi_max32-pwm.md#std-dtcompatible-adi-max32-pwm"><code>adi,max32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32XXX真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L226">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P001_adi_max32-trng.md#std-dtcompatible-adi-max32-trng"><code>adi,max32-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>MAX32通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L202">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L210">已禁用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P001_adi_max32-uart.md#std-dtcompatible-adi-max32-uart"><code>adi,max32-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32670.dtsi?plain=1#L108">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32670.dtsi?plain=1#L118">已禁用：2</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P001_adi_max32-spi.md#std-dtcompatible-adi-max32-spi"><code>adi,max32-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32670.dtsi?plain=1#L40">已启用：8</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L252">已禁用：6</a>）</td>
<td><a href="../system_timer_binding_reference/P002_adi_max32-timer.md#std-dtcompatible-adi-max32-timer"><code>adi,max32-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>MAX32XXX看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L233">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32670.dtsi?plain=1#L99">已禁用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P001_adi_max32-watchdog.md#std-dtcompatible-adi-max32-watchdog"><code>adi,max32-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<table>
<tr>
<th>名称（Name）</th>
<th>名称（Name）</th>
<th>设置（Settings）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td>JP1</td>
<td>P0_22</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开红色LED与P0_22。</td></tr><tr><td>将红色LED连接到P0_22。</td></tr></table></td>
</tr>
<tr>
<td>JP2</td>
<td>P0_23</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开绿色LED与P0_23。</td></tr><tr><td>将绿色LED连接到P0_23。</td></tr></table></td>
</tr>
<tr>
<td>JP3</td>
<td>P0_20、P0_26</td>
<td><table><tr><td>2-1</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>将USB转串口连接到P0_8（UART0_RX）。</td></tr><tr><td>将USB转串口连接到P0_26（LPUART0_RX）。</td></tr></table></td>
</tr>
<tr>
<td>JP4</td>
<td>P0_9、P0_27</td>
<td><table><tr><td>2-1</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>将USB转串口连接到P0_9（UART0_TX）。</td></tr><tr><td>将USB转串口连接到P0_27（LPUART0_TX）。</td></tr></table></td>
</tr>
<tr>
<td>JP5</td>
<td>VDD</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开VDD电源。</td></tr><tr><td>为VDD接通电源。</td></tr></table></td>
</tr>
<tr>
<td>JP6</td>
<td>VCORE</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开VCORE电源。</td></tr><tr><td>为VCORE接通电源。</td></tr></table></td>
</tr>
<tr>
<td>JP7</td>
<td>单电感多输出稳压器选择2（SIMO RSEL2）</td>
<td><table><tr><td>1-2</td></tr><tr><td>3-4</td></tr><tr><td>5-6</td></tr></table></td>
<td><table><tr><td>将SIMO稳压器的输出2设置为0.9 V。</td></tr><tr><td>将SIMO稳压器的输出2设置为1.0 V。</td></tr><tr><td>将SIMO稳压器的输出2设置为1.1 V。</td></tr></table></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`max32670evkit`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

<a id="flashing"></a>

### 烧录（Flashing）

MAX32670评估套件集成了基于MAX32625PICO的调试器，以提供DAPLink功能。

将调试探针连接到主机后，执行`west flash`即可将固件镜像写入闪存（Flash）。要执行整片擦除（Full Erase），在`west flash`命令中加入`--erase`选项。

<a id="debugging"></a>

### 调试（Debugging）

请参考[烧录（Flashing）](#flashing)一节，并将`west flash`替换为`west debug`执行调试。

<a id="references"></a>

## 参考资料（References）


- [MAX32670EVKIT网页（Web Page）](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max32670evkit.html)

---

[上一章](P011_MAX32666FTHR.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_MAX32672EVKIT.md)
