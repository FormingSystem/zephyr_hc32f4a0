---
id: learning.zephyr-docs.boards-adi-max32-max78-sdp.page-19
title: MAX78000EVKIT
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/adi/max78000evkit/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="max78000evkit"></a>

# 第19章\_MAX78000EVKIT

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/adi/max78000evkit/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/max78000evkit.webp](images/max78000evkit.webp)](images/max78000evkit.webp)

MAX78000EVKIT

名称（Name）：

`max78000evkit`

厂商（Vendor）：

[Analog Devices, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=adi)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[max78000](https://docs.zephyrproject.org/latest/boards/index.html#soc=max78000)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max78000evkit/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

MAX78000评估套件（EV Kit）提供一个平台，可利用MAX78000的能力构建新一代人工智能（AI）设备。板载硬件包括数字麦克风、陀螺仪／加速度计、并行摄像头模块支持，以及3.5英寸触控彩色TFT显示屏。第二块显示屏由功耗累积器（Power Accumulator）驱动，用于跟踪设备随时间变化的功耗。未占用的GPIO和模拟输入可通过0.1英寸间距排针方便地访问。主要系统电源和UART访问由USB Micro-B接口提供。USB转SPI桥可快速访问板载存储器，从而快速加载大型网络或图像。

Zephyr移植版本运行在MAX78000微控制器（MCU）上。

<a id="hardware"></a>

## 硬件（Hardware）


- MAX78000微控制器（MCU）：


  - 双核低功耗微控制器（Dual-Core Low-Power Microcontroller）


    - Arm Cortex-M4处理器，带浮点单元（FPU），最高100 MHz
    - 512 KB闪存（Flash）和128 KB SRAM
    - 通过16 KB指令缓存（Instruction Cache）优化性能
    - SRAM可选启用纠错码（ECC-SEC-DED），支持单错纠正、双错检测
    - 32位RISC-V协处理器（Coprocessor），最高60 MHz
    - 最多52个通用输入输出（I/O）引脚
    - 12位并行摄像头接口（Parallel Camera Interface）
    - 一路I2S主机／从机，用于数字音频接口
  - 神经网络加速器（Neural Network Accelerator）


    - 针对深度卷积神经网络（Deep Convolutional Neural Networks）高度优化
    - 可容纳442k个8位权重（Weights），支持1、2、4和8位权重
    - 可编程输入图像尺寸，最大1024 × 1024像素
    - 可编程网络深度（Network Depth），最多64层
    - 每层可编程网络通道宽度（Channel Widths），最多1024个通道
    - 一维与二维卷积处理（Convolution Processing）
    - 流式模式（Streaming Mode）
    - 可灵活支持其他网络类型，包括多层感知机（MLP）和循环神经网络（Recurrent Neural Networks）
  - 通过电源管理（Power Management）尽可能延长电池供电应用的运行时间


    - 集成单电感多输出（SIMO）开关电源（SMPS / Switch-Mode Power Supply）
    - SIMO供电电压范围为2.0–3.6 V
    - 动态电压调节（Dynamic Voltage Scaling）尽可能降低内核运行功耗
    - 3.0 V下从缓存执行while循环时为22.2 μA/MHz，仅CM4内核
    - 启用实时时钟（RTC）的低功耗模式下，可选择保留SRAM内容
  - 安全与完整性（Security and Integrity）


    - 可用的安全启动（Secure Boot）
    - AES 128/192/256硬件加速引擎（Hardware Acceleration Engine）
    - 真随机数发生器（TRNG）种子发生器（Seed Generator）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`max78000evkit`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="max78000evkit-hw-features"></a>

<a id="max78000evkit-max78000evkit/max78000/m4-hw-features-section"></a>

#### `max78000evkit/max78000/m4`目标（Target）

<a id="max78000evkit-max78000evkit/max78000/m4-hw-features-panel"></a>

<a id="max78000evkit-max78000evkit/max78000/m4-hw-features-memory"></a>

该开发板目标的片上存储容量：48 KiB RAM、512 KiB Flash。

<a id="max78000evkit-max78000evkit/max78000/m4-hw-features-table"></a>

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
<td>MAX32 RV32内核（Core）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L32">已启用：1</a>）</td>
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
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L64">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L71">已禁用：4</a>）</td>
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
<td>ADI MAX32兼容实时时钟计数器（Counter RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L332">已启用：1</a>）</td>
<td><a href="../counter_binding_reference/P002_adi_max32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter"><code>adi,max32-rtc-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32直接存储器访问（DMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max78000.dtsi?plain=1#L97">已启用：1</a>）</td>
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
<td>MAX32通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L175">已启用：4</a>）</td>
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
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max78000evkit/max78000evkit_max78000_m4.dts?plain=1#L40">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max78000evkit/max78000evkit_max78000_m4.dts?plain=1#L26">已启用：1</a>）</td>
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
<td>ADI MAX32脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L265">已禁用：6</a>）</td>
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
<td>ADI MAX32串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max78000-m4.dtsi?plain=1#L42">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max78000.dtsi?plain=1#L88">已禁用：1</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P001_adi_max32-spi.md#std-dtcompatible-adi-max32-spi"><code>adi,max32-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max78000.dtsi?plain=1#L70">已启用：4</a>）</td>
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
<td rowspan="1">单线总线（1-Wire）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32xxx微控制器（MCU）的1-Wire单总线主机（Master）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max78000.dtsi?plain=1#L106">已禁用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P006_adi_max32-w1.md#std-dtcompatible-adi-max32-w1"><code>adi,max32-w1</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>MAX32XXX看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L233">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max78000.dtsi?plain=1#L113">已禁用：1</a>）</td>
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
<td>LED1使能（LED1 EN）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>启用辅助LED1。</td></tr><tr><td>禁用辅助LED1。</td></tr></table></td>
</tr>
<tr>
<td>JP2</td>
<td>LED2使能（LED2 EN）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>启用辅助LED2。</td></tr><tr><td>禁用辅助LED2。</td></tr></table></td>
</tr>
<tr>
<td>JP3</td>
<td>TRIG1</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>启用功率监测事件触发1（Power Monitor Event Trigger 1）。</td></tr><tr><td>禁用功率监测事件触发1。</td></tr></table></td>
</tr>
<tr>
<td>JP4</td>
<td>TRIG2</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>启用功率监测事件触发2（Power Monitor Event Trigger 2）。</td></tr><tr><td>禁用功率监测事件触发2。</td></tr></table></td>
</tr>
<tr>
<td>JP5</td>
<td>VREGI</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>启用3V3 VREGI电源。</td></tr><tr><td>禁用3V3 VREGI电源。</td></tr></table></td>
</tr>
<tr>
<td>JP6</td>
<td>VREGIA</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>启用3V3 VREGIA电源。</td></tr><tr><td>禁用3V3 VREGIA电源。</td></tr></table></td>
</tr>
<tr>
<td>JP7</td>
<td>卷积神经网络升压（CNN BOOST）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>启用1V1升压低压差稳压器（Boost LDO）电源。</td></tr><tr><td>禁用1V1升压低压差稳压器电源。</td></tr></table></td>
</tr>
<tr>
<td>JP8</td>
<td>VDDA</td>
<td><table><tr><td>1-2</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>内部单电感多输出稳压器（SIMO）为VDDA供电。</td></tr><tr><td>外部低压差稳压器（LDO）为VDDA供电。</td></tr></table></td>
</tr>
<tr>
<td>JP9</td>
<td>VDDIO</td>
<td><table><tr><td>1-2</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>内部SIMO为VDDIO供电。</td></tr><tr><td>外部LDO为VDDIO供电。</td></tr></table></td>
</tr>
<tr>
<td>JP10</td>
<td>VDDIOH</td>
<td><table><tr><td>1-2</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>被测器件（DUT）的LDO为VDDIOH供电。</td></tr><tr><td>辅助（AUX）LDO为VDDIOH供电。</td></tr></table></td>
</tr>
<tr>
<td>JP11</td>
<td>VCOREB</td>
<td><table><tr><td>1-2</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>内部SIMO为VCOREB供电。</td></tr><tr><td>外部LDO为VCOREB供电。</td></tr></table></td>
</tr>
<tr>
<td>JP12</td>
<td>VCOREA</td>
<td><table><tr><td>1-2</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>内部SIMO为VCOREA供电。</td></tr><tr><td>外部LDO为VCOREA供电。</td></tr></table></td>
</tr>
<tr>
<td>JP13</td>
<td>VREGI功率监测旁路（PM BYPASS）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>旁路功率监测分流电阻（Power Monitor Shunt）。</td></tr><tr><td>使用功耗累积器（Power Accumulator）启用功率监测。</td></tr></table></td>
</tr>
<tr>
<td>JP14</td>
<td>卷积神经网络1V1电源（CNN 1V1）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>将1V1升压低压差稳压器（Boost LDO）连接到VCOREA。</td></tr><tr><td>禁用1V1升压低压差稳压器。</td></tr></table></td>
</tr>
<tr>
<td>JP15</td>
<td>VCOREA功率监测旁路（PM BYPASS）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>旁路功率监测分流电阻（Power Monitor Shunt）。</td></tr><tr><td>使用功耗累积器（Power Accumulator）启用功率监测。</td></tr></table></td>
</tr>
<tr>
<td>JP16</td>
<td>VCOREB功率监测旁路（PM BYPASS）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>旁路功率监测分流电阻（Power Monitor Shunt）。</td></tr><tr><td>使用功耗累积器（Power Accumulator）启用功率监测。</td></tr></table></td>
</tr>
<tr>
<td>JP17</td>
<td>VREG_A功率监测旁路（PM BYPASS）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>旁路功率监测分流电阻（Power Monitor Shunt）。</td></tr><tr><td>使用功耗累积器（Power Accumulator）启用功率监测。</td></tr></table></td>
</tr>
<tr>
<td>JP18</td>
<td>复位使能（RESET EN）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>允许RV JTAG适配器执行完整系统复位（Full System Reset）。</td></tr><tr><td>禁用RV JTAG适配器的系统复位。</td></tr></table></td>
</tr>
<tr>
<td>JP19</td>
<td>TFT背光（BL / Backlight）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>启用主TFT屏幕背光。</td></tr><tr><td>禁用主TFT屏幕背光。</td></tr></table></td>
</tr>
<tr>
<td>JP20</td>
<td>I2S时钟选择（CLK SEL）</td>
<td><table><tr><td>1-2</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>板载12.288 MHz振荡器驱动I2S时钟。</td></tr><tr><td>外部1V8 CMOS电平信号源驱动I2S时钟。</td></tr></table></td>
</tr>
<tr>
<td>JP21</td>
<td>被测器件电流（DUT I）</td>
<td><table><tr><td>1-2</td></tr><tr><td>开路（Open）</td></tr></table></td>
<td><table><tr><td>被测器件（DUT）的3V3总电流监测点</td></tr><tr><td>断开以接入电流表（Current Meter）。</td></tr></table></td>
</tr>
<tr>
<td>JP22</td>
<td>USB-SPI/CAM</td>
<td><table><tr><td>1-2</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>启用USB转SPI桥（Bridge）。</td></tr><tr><td>启用摄像头（Camera）。</td></tr></table></td>
</tr>
<tr>
<td>JH1</td>
<td>UART 0使能（UART 0 EN）</td>
<td><table><tr><td>1-2, 3-4</td></tr><tr><td>全部开路（All Open）</td></tr></table></td>
<td><table><tr><td>启用USB转UART0桥，采用软件流控制（Software Flow Control）。</td></tr><tr><td>禁用USB转UART0桥，允许复用端口引脚。</td></tr></table></td>
</tr>
<tr>
<td>JH2</td>
<td>UART 1使能（UART 1 EN）</td>
<td><table><tr><td>全部安装（All Installed）</td></tr><tr><td>全部开路（All Open）</td></tr></table></td>
<td><table><tr><td>启用USB转UART1桥。</td></tr><tr><td>禁用USB转UART1桥，允许复用端口引脚。</td></tr></table></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`max78000evkit`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

将外部调试探针（Debug Probe）连接到SWD端口，即可烧录MAX78000微控制器（MCU）。SWD调试通过Cortex 10针接口JH5接入，逻辑电平固定为VDDIO，即1.8 V。

将调试探针连接到主机后，执行`west flash`即可将固件镜像写入闪存（Flash）。要执行整片擦除（Full Erase），在`west flash`命令中加入`--erase`选项。

注意（Note）

该开发板默认使用OpenOCD调试接口。也可覆盖运行工具（Runner），在west命令后添加`--runner jlink`，使用Segger J-Link及其原生工具。应通过合适的适配板和线缆，将J-Link连接到标准2 × 5针调试接口JH5。

<a id="debugging"></a>

### 调试（Debugging）

请参考[烧录（Flashing）](#flashing)一节，并将`west flash`替换为`west debug`执行调试。

<a id="references"></a>

## 参考资料（References）


- [MAX78000EVKIT网页（Web Page）](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/max78000evkit.html)

---

[上一章](P018_MAX32690FTHR.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P020_MAX78000FTHR.md)
