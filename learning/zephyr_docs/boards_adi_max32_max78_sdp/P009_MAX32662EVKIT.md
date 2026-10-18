---
id: learning.zephyr-docs.boards-adi-max32-max78-sdp.page-9
title: MAX32662EVKIT
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/adi/max32662evkit/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="max32662evkit"></a>

# 第9章\_MAX32662EVKIT

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/adi/max32662evkit/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/max32662evkit.webp](images/max32662evkit.webp)](images/max32662evkit.webp)

MAX32662EVKIT

名称（Name）：

`max32662evkit`

厂商（Vendor）：

[Analog Devices, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=adi)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[max32662](https://docs.zephyrproject.org/latest/boards/index.html#soc=max32662)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32662evkit/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

MAX32662评估套件（EV Kit）提供一个平台，用于评估MAX32662微控制器的能力。该器件是面向电池供电边缘设备（Edge Devices）的经济型、超低功耗、高集成度32位微控制器。

Zephyr移植版本运行在MAX32662微控制器（MCU）上。

<a id="hardware"></a>

## 硬件（Hardware）


- MAX32662微控制器（MCU）：


  - 面向低功耗、高可靠性设备的高能效微控制器


    - 256 KB闪存（Flash）
    - 80 KB SRAM，可选择在最低功耗备份模式（BACKUP Mode）下保留内容
    - 16 KB统一缓存（Unified Cache）
    - 存储器保护单元（MPU / Memory Protection Unit）
    - 支持双电源或单电源运行，电压范围1.7–3.6 V
    - 宽工作温度范围：−40 °C至+105 °C
  - 灵活的时钟方案（Clocking Schemes）


    - 内部高速时钟（High-Speed），100 MHz
    - 内部低功耗时钟（Low-Power），7.3728 MHz
    - 超低功耗时钟（Ultra-Low-Power），80 kHz
    - 16–32 MHz，需要外部晶体（External Crystal）
    - 32.768 kHz，需要外部晶体（External Crystal）
    - CPU和低功耗定时器（Low-Power Timer）的外部时钟输入
  - 通过电源管理（Power Management）尽可能延长电池供电应用的运行时间


    - 活动模式（ACTIVE）下，0.9 V、最高12 MHz运行CoreMark®时为50 μA/MHz
    - 活动模式（ACTIVE）下，1.1 V、最高100 MHz运行While(1)时为44 μA/MHz
    - VDDIO = 1.8 V时，备份模式（BACKUP）下完整存储器保持电流为2.15 μA
    - VDDIO = 3.3 V时，备份模式（BACKUP）下完整存储器保持电流为2.4 μA
    - 350 nA超低功耗实时时钟（RTC）
    - 由低功耗定时器（Low-Power Timer）唤醒
  - 通过合理的外设组合提供平台扩展能力（Platform Scalability）


    - 最多21个通用输入输出（I/O）引脚
    - 四通道、12位、1 Msps模数转换器（ADC）
    - 两路SPI控制器／目标（Controller/Target）
    - 一路I2S控制器／目标（Controller/Target）
    - 两路四线UART
    - 两路I2C控制器／目标（Controller/Target）
    - 一路CAN 2.0B控制器
    - 四通道标准DMA控制器
    - 三个32位定时器（Timers）
    - 一个32位低功耗定时器（Low-Power Timer）
    - 一个看门狗定时器（Watchdog Timer）
    - CMOS电平的32.768 kHz校准输出（Calibration Output）
    - AES-128/192/256硬件加速器（Hardware Accelerator）
- MAX32662EVKIT的优势与功能（Benefits and Features）：


  - 用于CAN Bus 2.0B的3针接线端子（Terminal Block）
  - 128 × 128、1.45英寸彩色TFT显示屏，带SPI接口
  - 可选板载高精度参考电压（High-Precision Voltage Reference）
  - USB 2.0 Micro-B转串行UART
  - 通过0.1英寸间距排针访问全部GPIO信号
  - 通过0.1英寸间距排针访问四路模拟输入（Analog Inputs）
  - 10针串行线调试排针（SWD Header）
  - USB端口为开发板供电
  - 板载低压差稳压器（LDO Regulators）
  - 通过跳线分别测量所有芯片供电轨（IC Rails）的功耗
  - 一个通用LED
  - 一个通用按键开关（Pushbutton Switch）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`max32662evkit`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="max32662evkit-hw-features"></a>

<a id="max32662evkit-max32662evkit/max32662-hw-features-section"></a>

#### `max32662evkit/max32662`目标（Target）

<a id="max32662evkit-max32662evkit/max32662-hw-features-panel"></a>

<a id="max32662evkit-max32662evkit/max32662-hw-features-memory"></a>

该开发板目标的片上存储容量：16 KiB RAM、256 KiB Flash。

<a id="max32662evkit-max32662evkit/max32662-hw-features-table"></a>

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
<td>ADI MAX32逐次逼近模数转换器（SAR ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L241">已禁用：1</a>）</td>
<td><a href="../hardware/P863_ADIMAX32逐次逼近ADC绑定.md#dtbinding-adi-max32-adc-sar"><code>adi,max32-adc-sar</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32控制器局域网（CAN）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32662.dtsi?plain=1#L145">已启用：1</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P001_adi_max32-can.md#std-dtcompatible-adi-max32-can"><code>adi,max32-can</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L64">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L78">已禁用：4</a>）</td>
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
<td>ADI MAX32计数器（Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L260">已禁用：4</a>）</td>
<td><a href="../counter_binding_reference/P001_adi_max32-counter.md#std-dtcompatible-adi-max32-counter"><code>adi,max32-counter</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ADI MAX32兼容实时时钟计数器（Counter RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32662.dtsi?plain=1#L138">已启用：1</a>）</td>
<td><a href="../counter_binding_reference/P002_adi_max32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter"><code>adi,max32-rtc-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>板载（On-Board）</td>
<td>Sitronix ST7735X显示控制器（Display Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32662evkit/max32662evkit.dts?plain=1#L64">已启用：1</a>）</td>
<td><a href="../display_sinowealth_sitronix_solomon_binding_reference/P010_sitronix_st7735r.md#std-dtcompatible-sitronix-st7735r"><code>sitronix,st7735r</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32直接存储器访问（DMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32662.dtsi?plain=1#L93">已启用：1</a>）</td>
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
<td>MAX32通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L175">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P011_adi_max32-gpio.md#std-dtcompatible-adi-max32-gpio"><code>adi,max32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32 I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L149">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L139">已禁用：1</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P001_adi_max32-i2c.md#std-dtcompatible-adi-max32-i2c"><code>adi,max32-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32662evkit/max32662evkit.dts?plain=1#L38">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32662evkit/max32662evkit.dts?plain=1#L29">已启用：1</a>）</td>
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
<td>ADI MAX32脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L265">已禁用：3</a>）</td>
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
<td>MAX32通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L202">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L210">已禁用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P001_adi_max32-uart.md#std-dtcompatible-adi-max32-uart"><code>adi,max32-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32662.dtsi?plain=1#L103">已启用：2</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P001_adi_max32-spi.md#std-dtcompatible-adi-max32-spi"><code>adi,max32-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32662.dtsi?plain=1#L53">已启用：8</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L252">已禁用：4</a>）</td>
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
<td>MAX32XXX看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L233">已启用：1</a>）</td>
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
<td>参考电压使能（VREF EN）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>将外部参考电压（External Voltage Reference）连接到VREF引脚，必须在软件中启用。更多信息见外部参考电压（VREF）一节。</td></tr><tr><td>断开外部参考电压。</td></tr></table></td>
</tr>
<tr>
<td>JP2</td>
<td>I2C1_SCL_PU</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>将上拉电阻连接到I2C1A_SCL（P0.6），由V_AUX供电。</td></tr><tr><td>断开I2C1A_SCL（P0.6）的上拉电阻，其电源来自V_AUX。</td></tr></table></td>
</tr>
<tr>
<td>JP3</td>
<td>N/A</td>
<td>N/A</td>
<td>不存在（Does Not Exist）。</td>
</tr>
<tr>
<td>JP4</td>
<td>I2C1_SDA_PU</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>将上拉电阻连接到I2C1A_SDA（P0.9），由V_AUX供电。</td></tr><tr><td>断开I2C1A_SDA（P0.9）的上拉电阻，其电源来自V_AUX。</td></tr></table></td>
</tr>
<tr>
<td>JP5</td>
<td>LED0使能（LED0 EN）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>启用LED0。</td></tr><tr><td>禁用LED0。</td></tr></table></td>
</tr>
<tr>
<td>JP6</td>
<td>CTS0A使能（CTS0A EN）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>将USB转串口桥（USB-to-Serial Bridge）连接到UART0A_CTS（P0.20）。</td></tr><tr><td>断开USB转串口桥与UART0A_CTS（P0.20）。</td></tr></table></td>
</tr>
<tr>
<td>JP7</td>
<td>RX0A使能（RX0A EN）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>将USB转串口桥（USB-to-Serial Bridge）连接到UART0A_RX（P0.11）。</td></tr><tr><td>断开USB转串口桥与UART0A_RX（P0.11）。</td></tr></table></td>
</tr>
<tr>
<td>JP8</td>
<td>TX0A使能（TX0A EN）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>将USB转串口桥（USB-to-Serial Bridge）连接到UART0A_TX（P0.10）。</td></tr><tr><td>断开USB转串口桥与UART0A_TX（P0.10）。</td></tr></table></td>
</tr>
<tr>
<td>JP9</td>
<td>RTS0A使能（RTS0A EN）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>将USB转串口桥（USB-to-Serial Bridge）连接到UART0A_RTS（P0.19）。</td></tr><tr><td>断开USB转串口桥与UART0A_RTS（P0.19）。</td></tr></table></td>
</tr>
<tr>
<td>JP10</td>
<td>内核电源使能（VCORE EN）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>将1V1连接到VCORE。</td></tr><tr><td>断开1V1与VCORE。</td></tr></table></td>
</tr>
<tr>
<td>JP11</td>
<td>VDDIO/VDDASEL</td>
<td><table><tr><td>2-1</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>将1V8连接到V_AUX、VDDIO EN跳线JP12及VDDA EN跳线JP13。</td></tr><tr><td>将3V3连接到V_AUX、VDDIO EN跳线JP12及VDDA EN跳线JP13。</td></tr></table></td>
</tr>
<tr>
<td>JP12</td>
<td>I/O电源使能（VDDIO EN）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>将JP11选择的电压连接到VDDIO。</td></tr><tr><td>断开VDDIO的供电电压。</td></tr></table></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`max32662evkit`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-jlink"><code>jlink</code></a></td>
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

<a id="flashing"></a>

### 烧录（Flashing）

Arm®调试访问端口（DAP / Debug Access Port）在应用开发期间提供外部调试接口。DAP是标准Arm CoreSight®串行线调试端口，使用SWDCLK和SWDIO两线串行接口，通过10针排针J3访问。逻辑电平设为V_AUX（1V8或3V3），取决于JP11跳线帽的位置。此外，也可通过J3访问UART1A端口。

将调试探针连接到主机后，执行`west flash`即可将固件镜像写入闪存（Flash）。要执行整片擦除（Full Erase），在`west flash`命令中加入`--erase`选项。

注意（Note）

该开发板默认使用OpenOCD调试接口。也可覆盖运行工具（Runner），在west命令后添加`--runner jlink`，使用Segger J-Link及其原生工具。应通过合适的适配板和线缆，将J-Link连接到标准2 × 5针调试接口J3。

<a id="debugging"></a>

### 调试（Debugging）

请参考[烧录（Flashing）](#flashing)一节，并将`west flash`替换为`west debug`执行调试。

<a id="references"></a>

## 参考资料（References）


- [MAX32662EVKIT网页（Web Page）](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max32662evkit.html)

---

[上一章](P008_MAX32660EVSYS.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_MAX32666EVKIT.md)
