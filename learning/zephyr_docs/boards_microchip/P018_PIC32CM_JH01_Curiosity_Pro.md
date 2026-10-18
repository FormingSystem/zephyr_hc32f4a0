---
id: learning.zephyr-docs.boards-microchip.page-18
title: PIC32CM JH01 Curiosity Pro
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/microchip/pic32c/pic32cm_jh01_cpro/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="pic32cm_jh01_cpro"></a>

# 第18章\_PIC32CM JH01 Curiosity Pro

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/microchip/pic32c/pic32cm_jh01_cpro/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../../_images/pic32cm_jh01_cpro.webp](images/pic32cm_jh01_cpro.webp)](images/pic32cm_jh01_cpro.webp)

PIC32CM JH01 Curiosity Pro

名称（Name）：

`pic32cm_jh01_cpro`

厂商（Vendor）：

[微芯科技（Microchip Technology Inc.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=microchip)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[pic32cm5164jh01100](https://docs.zephyrproject.org/latest/boards/index.html#soc=pic32cm5164jh01100)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/pic32c/pic32cm_jh01_cpro/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

PIC32CM JH01 Curiosity Pro评估套件用于评估Microchip PIC32CM JH01微控制器，料号EV81X90A。套件提供多种功能，帮助用户开始使用PIC32CM JH01外设，并了解如何将器件集成到自己的设计。

<a id="hardware"></a>

## 硬件（Hardware）


- 100引脚TQFP封装的PIC32CM5164 JH01微控制器
- 32.768 kHz晶体振荡器（Crystal Oscillator）
- 32 MHz晶体振荡器
- 512 KiB闪存及64 KiB RAM
- 一个黄色用户LED
- 一个绿色开发板电源LED
- 一个机械式用户按键
- 1个复位按键（Reset Button）
- 一个带驱动屏蔽（Driven Shield）的触摸按键
- Trust Anchor TA100安全元件（Secure Element）
- 虚拟COM端口（CDC）
- 通过串行线调试（SWD）对板上PIC32CM JH01编程及调试
- Arduino Uno连接器

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`pic32cm_jh01_cpro`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="pic32cm_jh01_cpro-hw-features"></a>

<a id="pic32cm_jh01_cpro-pic32cm_jh01_cpro/pic32cm5164jh01100-hw-features-section"></a>

#### `pic32cm_jh01_cpro/pic32cm5164jh01100`目标（Target）

<a id="pic32cm_jh01_cpro-pic32cm_jh01_cpro/pic32cm5164jh01100-hw-features-panel"></a>

<a id="pic32cm_jh01_cpro-pic32cm_jh01_cpro/pic32cm5164jh01100-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、8405248 B Flash。

<a id="pic32cm_jh01_cpro-pic32cm_jh01_cpro/pic32cm5164jh01100-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Microchip ADC G1驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L334">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L351">已禁用：1</a>）</td>
<td><a href="../hardware/P859_MicrochipG1模数转换器绑定.md#dtbinding-microchip-adc-g1"><code>microchip,adc-g1</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>Microchip SERCOM模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L218">已禁用：5</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P013_microchip_sercom-g1.md#std-dtcompatible-microchip-sercom-g1"><code>microchip,sercom-g1</code></a></td>
</tr>
<tr>
<td rowspan="11">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Microchip PIC32CM_JH SoC系列时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P007_microchip_pic32cm-jh-clock.md#std-dtcompatible-microchip-pic32cm-jh-clock"><code>microchip,pic32cm-jh-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_JH晶体振荡器（XOSC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L63">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P016_microchip_pic32cm-jh-xosc.md#std-dtcompatible-microchip-pic32cm-jh-xosc"><code>microchip,pic32cm-jh-xosc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_JH内部振荡器（OSC48M）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L67">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P014_microchip_pic32cm-jh-osc48m.md#std-dtcompatible-microchip-pic32cm-jh-osc48m"><code>microchip,pic32cm-jh-osc48m</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_JH FDPLL时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L71">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P008_microchip_pic32cm-jh-fdpll.md#std-dtcompatible-microchip-pic32cm-jh-fdpll"><code>microchip,pic32cm-jh-fdpll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_JH RTC时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P015_microchip_pic32cm-jh-rtc.md#std-dtcompatible-microchip-pic32cm-jh-rtc"><code>microchip,pic32cm-jh-rtc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_JH外部晶体振荡器（XOSC32K）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L80">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P017_microchip_pic32cm-jh-xosc32k.md#std-dtcompatible-microchip-pic32cm-jh-xosc32k"><code>microchip,pic32cm-jh-xosc32k</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_JH内部振荡器（OSC32K）控制（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L84">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P013_microchip_pic32cm-jh-osc32k.md#std-dtcompatible-microchip-pic32cm-jh-osc32k"><code>microchip,pic32cm-jh-osc32k</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_JH通用时钟发生器（Generic Clock Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L88">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P009_microchip_pic32cm-jh-gclkgen.md#std-dtcompatible-microchip-pic32cm-jh-gclkgen"><code>microchip,pic32cm-jh-gclkgen</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_JH通用时钟外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L92">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P010_microchip_pic32cm-jh-gclkperiph.md#std-dtcompatible-microchip-pic32cm-jh-gclkperiph"><code>microchip,pic32cm-jh-gclkperiph</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_JH CPU主时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P011_microchip_pic32cm-jh-mclkcpu.md#std-dtcompatible-microchip-pic32cm-jh-mclkcpu"><code>microchip,pic32cm-jh-mclkcpu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CM_JH MCLK外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L102">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P012_microchip_pic32cm-jh-mclkperiph.md#std-dtcompatible-microchip-pic32cm-jh-mclkperiph"><code>microchip,pic32cm-jh-mclkperiph</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1模拟比较器（Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L368">已禁用：1</a>）</td>
<td><a href="../hardware/P756_Microchip模拟比较器通道绑定.md#dtbinding-microchip-ac-g1-comparator"><code>microchip,ac-g1-comparator</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Microchip TC（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L262">已启用：1</a>）</td>
<td><a href="../microchip_soc_counter_binding_reference/P009_microchip_tc-g1-counter.md#std-dtcompatible-microchip-tc-g1-counter"><code>microchip,tc-g1-counter</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip TC G1外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L277">已禁用：6</a>）</td>
<td><a href="../microchip_soc_counter_binding_reference/P010_microchip_tc-g1.md#std-dtcompatible-microchip-tc-g1"><code>microchip,tc-g1</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip TCC G1定时器／计数器外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_5164_jh.dtsi?plain=1#L39">已禁用：1</a>）</td>
<td><a href="../microchip_soc_counter_binding_reference/P013_microchip_tcc-g1.md#std-dtcompatible-microchip-tcc-g1"><code>microchip,tcc-g1</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip TCC G1计数器外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_5164_jh.dtsi?plain=1#L52">已启用：1</a>）</td>
<td><a href="../microchip_soc_counter_binding_reference/P012_microchip_tcc-g1-counter.md#std-dtcompatible-microchip-tcc-g1-counter"><code>microchip,tcc-g1-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>Microchip G2 DAC（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_5164_jh.dtsi?plain=1#L120">已启用：1</a>）</td>
<td><a href="../hardware/P777_MicrochipG2数模转换器绑定.md#dtbinding-microchip-dac-g2"><code>microchip,dac-g2</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Microchip G2 DMA控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L208">已启用：1</a>）</td>
<td><a href="../intel_microchip_dma_binding_reference/P014_microchip_dmac-g2-dma.md#std-dtcompatible-microchip-dmac-g2-dma"><code>microchip,dmac-g2-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip NVMCTRL（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L185">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P023_microchip_nvmctrl-g2.md#std-dtcompatible-microchip-nvmctrl-g2"><code>microchip,nvmctrl-g2</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Microchip Port G1 GPIO（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L176">已启用：3</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P001_microchip_port-g1-gpio.md#std-dtcompatible-microchip-port-g1-gpio"><code>microchip,port-g1-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1硬件信息（hwinfo）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L44">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P005_microchip_hwinfo-g1.md#std-dtcompatible-microchip-hwinfo-g1"><code>microchip,hwinfo-g1</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Microchip SERCOM G1 I2C驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L251">已启用：1</a>）</td>
<td><a href="../i2c_infineon_ite_nordic_binding_reference/P012_microchip_sercom-g1-i2c.md#std-dtcompatible-microchip-sercom-g1-i2c"><code>microchip,sercom-g1-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/pic32c/pic32cm_jh01_cpro/pic32cm_jh01_cpro.dts?plain=1#L53">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip EIC G1设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L149">已启用：1</a>）</td>
<td><a href="../infineon_microchip_interrupt_binding_reference/P007_microchip_eic-g1-intc.md#std-dtcompatible-microchip-eic-g1-intc"><code>microchip,eic-g1-intc</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/pic32c/pic32cm_jh01_cpro/pic32cm_jh01_cpro.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/pic32c/pic32cm_jh01_cpro/pic32cm_jh01_cpro.dts?plain=1#L44">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M内存保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P004_arm_armv6m-mpu.md#std-dtcompatible-arm-armv6m-mpu"><code>arm,armv6m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>Microchip Flash G2（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L197">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P003_microchip_flash-g2.md#std-dtcompatible-microchip-flash-g2"><code>microchip,flash-g2</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Microchip PORT引脚控制（Pinctrl）容器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L169">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P006_microchip_port-g1-pinctrl.md#std-dtcompatible-microchip-port-g1-pinctrl"><code>microchip,port-g1-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1 SUPC（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L113">已禁用：1</a>）</td>
<td><a href="../power_control_binding_reference/P007_microchip_supc-g1.md#std-dtcompatible-microchip-supc-g1"><code>microchip,supc-g1</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1 TCC PWM驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_5164_jh.dtsi?plain=1#L65">已启用：1</a>）</td>
<td><a href="../pwm_intel_microchip_nxp_binding_reference/P011_microchip_tcc-g1-pwm.md#std-dtcompatible-microchip-tcc-g1-pwm"><code>microchip,tcc-g1-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip PWM TC G1驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_5164_jh.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../pwm_intel_microchip_nxp_binding_reference/P010_microchip_tc-g1-pwm.md#std-dtcompatible-microchip-tc-g1-pwm"><code>microchip,tc-g1-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip RSTC复位（Reset）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L108">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P006_microchip_rstc-g1-reset.md#std-dtcompatible-microchip-rstc-g1-reset"><code>microchip,rstc-g1-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1 RTC驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L135">已启用：1</a>）</td>
<td><a href="../rtc_binding_reference/P015_microchip_rtc-g1.md#std-dtcompatible-microchip-rtc-g1"><code>microchip,rtc-g1</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip SERCOM UART控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh_100.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P019_microchip_sercom-g1-uart.md#std-dtcompatible-microchip-sercom-g1-uart"><code>microchip,sercom-g1-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Microchip SERCOM SPI（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh_100.dtsi?plain=1#L24">已启用：1</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P009_microchip_sercom-g1-spi.md#std-dtcompatible-microchip-sercom-g1-spi"><code>microchip,sercom-g1-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L52">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1看门狗（Watchdog）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L121">已禁用：1</a>）</td>
<td><a href="../soc_pmic_watchdog_binding_reference/P010_microchip_wdt-g1.md#std-dtcompatible-microchip-wdt-g1"><code>microchip,wdt-g1</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

PIC32CM JH01 Curiosity Pro用户指南提供开发板连接详情。（[PIC32CM JH01 Curiosity Pro用户指南（User Guide）](https://ww1.microchip.com/downloads/aemDocuments/documents/MCU32/ProductDocuments/UserGuides/PIC32CM-JH01-Curiosity-Pro-Evaluation-Kit-User-Guide-DS70005482.pdf)）

<a id="programming-debugging"></a>

## 编程与调试（Programming & Debugging）

`pic32cm_jh01_cpro`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>复位（reset）</th>
<th>调试服务器（debugserver）</th>
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
<td>mplab_ipe</td>
<td>✅</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-pyocd">pyocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

<a id="setting-up-the-debug-interface"></a>

### 设置调试接口（Debug Interface）

此板支持通过MPLAB VS Code扩展、PyOCD或J-Link调试。应选择与所连接调试硬件匹配的设置。

<a id="debug-adapter-for-mplab-setup"></a>

### MPLAB调试适配器（Debug Adapter）设置

使用Microchip MPLAB扩展配置Visual Studio Code调试的方法见“Microchip MPLAB VS Code调试”。以下launch.json配置可用于通过MPLAB扩展调试此板。（[Microchip MPLAB VS Code调试（Debugging）](P002_Microchip_MPLAB_VS_Code_Debugging.md#microchip-mplab-vscode-debugging)）

```text
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "MPLAB Debug Zephyr : pic32cm_jh01_cpro",
      "type": "mplab-core-da",
      "request": "launch",
      "program": "${workspaceFolder}/zephyr/build/zephyr/zephyr.elf",
      "tool": "${command:pickTool}",
      "stopOnEntry": true,
      "device": "PIC32CM5164JH01100"
    }
  ]
}
```

<a id="pyocd-setup"></a>

### PyOCD设置（Setup）


1. 安装器件包（Device Pack）


  - 使用以下命令添加PIC32CM系列器件支持：

  ```text
  pyocd pack install pic32cm
  ```
2. 验证器件支持（Device Support）


  - 确认能够识别目标：

  ```text
  pyocd list --targets
  ```


  - 应看到类似以下条目：

  ```text
  pic32cm5164jh01100        Microchip                PIC32CM5164JH01100           PIC32CM-JH   pack
  ```
3. 连接开发板（Connect the Board）


  - 将开发板DEBUG USB端口连接主机。
  - 该连接为开发板供电，并提供对板载嵌入式调试器（EDBG）的访问，使PyOCD能够对目标微控制器编程及调试。

<a id="j-link-setup"></a>

### J-Link设置（Setup）


1. 安装J-Link软件（Install J-Link Software）


  - 从Segger下载并安装[J-Link软件](https://www.segger.com/downloads/jlink)工具。
  - 确认已安装的J-Link可执行文件，例如JLink及JLinkGDBServer，已加入系统PATH。
2. 连接开发板（Connect the Board）


  - 将J32调试探针连接到开发板的CORTEX DEBUG排针。（[J32调试探针（Debug Probe）](https://www.microchip.com/en-us/development-tool/dv164232)）
  - 通过USB将J32调试探针另一端连接到主机PC。
  - 将开发板DEBUG USB端口连接主机，为开发板供电。

<a id="flash-using-mplab-ipe"></a>

### 使用MPLAB IPE烧录（Flash）

使用MPLAB IPE烧录的方法见“使用Microchip MPLAB IPE烧录”。（[使用Microchip MPLAB IPE烧录（Flashing）](P001_Flashing_with_Microchip_MPLAB_IPE.md#microchip-mplab-ipe-flashing)）

<a id="building-and-flashing-the-application"></a>

### 构建与烧录应用（Building and Flashing）


1. 构建应用（Build the Application）

  可用west工具构建Blinky等Zephyr示例应用。从Zephyr工作区执行以下命令：

  ```text
  west build -b pic32cm_jh01_cpro -p -s samples/basic/blinky
  ```

  这将为pic32cm_jh01_cpro开发板构建Blinky应用。
2. 烧录设备（Flash the Device）

  构建完成后，用以下命令烧录固件：

  ```text
  west flash
  ```

  默认情况下，此命令使用PyOCD运行工具（Runner）对器件编程。

  若同时连接了CORTEX DEBUG排针上的J-Link探针和DEBUG USB端口上的PyOCD兼容调试接口，可按如下方式显式选择所需运行工具：

  ```text
  west flash --runner jlink
  ```

  或

  ```text
  west flash --runner pyocd
  ```

  这样即可使用相应的已连接接口烧录应用。
3. 观察结果（Observe the Result）

  烧录后LED0应开始闪烁，表明应用成功运行。

<a id="references"></a>

## 参考资料（References）

PIC32CM JH01产品页面：

[https://www.microchip.com/en-us/product/PIC32CM5164JH01100](https://www.microchip.com/en-us/product/PIC32CM5164JH01100)

PIC32CM JH01 Curiosity Pro评估套件页面：

[https://www.microchip.com/en-us/development-tool/ev81x90a](https://www.microchip.com/en-us/development-tool/ev81x90a)

## 译注

MPLAB扩展、PyOCD和J-Link是不同调试配置，需对应已连接硬件；默认烧录使用PyOCD，可显式指定运行工具。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [dv164232](https://www.microchip.com/en-us/development-tool/dv164232)：HTTP Error 403: Forbidden。
- [ev81x90a](https://www.microchip.com/en-us/development-tool/ev81x90a)：HTTP Error 403: Forbidden。
- [PIC32CM5164JH01100](https://www.microchip.com/en-us/product/PIC32CM5164JH01100)：HTTP Error 403: Forbidden。

---

[上一章](P017_PIC32CM_JH01_Curiosity_Nano_Touch_Evaluation_Kit.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P019_PIC32CM_PL10_Curiosity_Nano.md)
