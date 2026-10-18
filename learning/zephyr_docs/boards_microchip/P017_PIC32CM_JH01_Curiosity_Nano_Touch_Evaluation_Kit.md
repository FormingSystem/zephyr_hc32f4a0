---
id: learning.zephyr-docs.boards-microchip.page-17
title: PIC32CM JH01 Curiosity Nano Touch Evaluation Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/microchip/pic32c/pic32cm_jh01_cnano/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="pic32cm_jh01_cnano"></a>

# 第17章\_PIC32CM JH01 Curiosity Nano+ Touch评估套件

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/microchip/pic32c/pic32cm_jh01_cnano/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../../_images/pic32cm_jh01_cnano.webp](images/pic32cm_jh01_cnano.webp)](images/pic32cm_jh01_cnano.webp)

PIC32CM JH01 Curiosity Nano+ Touch评估套件

名称（Name）：

`pic32cm_jh01_cnano`

厂商（Vendor）：

[微芯科技（Microchip Technology Inc.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=microchip)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[pic32cm5164jh01048](https://docs.zephyrproject.org/latest/boards/index.html#soc=pic32cm5164jh01048)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/pic32c/pic32cm_jh01_cnano/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

PIC32CM JH01 Curiosity Nano+ Touch评估套件EV29G58A搭载PIC32CM5164JH01048微控制器（MCU）。该套件便于访问MCU功能并开发自定义应用。

<a id="hardware"></a>

## 硬件（Hardware）


- PIC32CM5164JH01048 MCU
- 基于Arm® Cortex®-M0+的MCU
- 一个黄色用户LED
- 一个机械用户开关
- 一个用户触摸按键
- CAN接口
- LIN接口
- 调试器USB接口


  - 可用于开发板供电
  - 编程或调试开发板时必须使用此接口
- 板载Nano调试器（nEDBG）


  - 一个绿色电源／状态LED
  - 编程与调试（Programming and Debugging）
  - 通信设备类（CDC / Communications Device Class）虚拟COM端口
  - 一个逻辑分析仪DGI GPIO
  - 目标器件通过板载Nano调试器编程及调试，无需外部编程器或调试工具
- 可调目标电压（Adjustable Target Voltage）


  - 由板载调试器控制的MIC5353低压差稳压器（LDO）
  - 输出电压1.7—3.6 V
  - 最大输出电流500 mA，受环境温度及输出电压限制

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`pic32cm_jh01_cnano`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="pic32cm_jh01_cnano-hw-features"></a>

<a id="pic32cm_jh01_cnano-pic32cm_jh01_cnano/pic32cm5164jh01048-hw-features-section"></a>

#### `pic32cm_jh01_cnano/pic32cm5164jh01048`目标（Target）

<a id="pic32cm_jh01_cnano-pic32cm_jh01_cnano/pic32cm5164jh01048-hw-features-panel"></a>

<a id="pic32cm_jh01_cnano-pic32cm_jh01_cnano/pic32cm5164jh01048-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、8405248 B Flash。

<a id="pic32cm_jh01_cnano-pic32cm_jh01_cnano/pic32cm5164jh01048-hw-features-table"></a>

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
<td>Microchip ADC G1驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L334">已禁用：2</a>）</td>
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
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Microchip TC（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L262">已启用：1</a>）</td>
<td><a href="../microchip_soc_counter_binding_reference/P009_microchip_tc-g1-counter.md#std-dtcompatible-microchip-tc-g1-counter"><code>microchip,tc-g1-counter</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip TC G1外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L277">已禁用：7</a>）</td>
<td><a href="../microchip_soc_counter_binding_reference/P010_microchip_tc-g1.md#std-dtcompatible-microchip-tc-g1"><code>microchip,tc-g1</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip TCC G1定时器／计数器外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_5164_jh.dtsi?plain=1#L39">已禁用：3</a>）</td>
<td><a href="../microchip_soc_counter_binding_reference/P013_microchip_tcc-g1.md#std-dtcompatible-microchip-tcc-g1"><code>microchip,tcc-g1</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>Microchip G2 DAC（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_5164_jh.dtsi?plain=1#L120">已禁用：1</a>）</td>
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
<td>Microchip Port G1 GPIO（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L176">已启用：2</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P001_microchip_port-g1-gpio.md#std-dtcompatible-microchip-port-g1-gpio"><code>microchip,port-g1-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1硬件信息（hwinfo）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L44">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P005_microchip_hwinfo-g1.md#std-dtcompatible-microchip-hwinfo-g1"><code>microchip,hwinfo-g1</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/pic32c/pic32cm_jh01_cnano/pic32cm_jh01_cnano.dts?plain=1#L38">已启用：1</a>）</td>
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
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/pic32c/pic32cm_jh01_cnano/pic32cm_jh01_cnano.dts?plain=1#L29">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
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
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip RSTC复位（Reset）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L108">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P006_microchip_rstc-g1-reset.md#std-dtcompatible-microchip-rstc-g1-reset"><code>microchip,rstc-g1-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1 RTC驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L135">已禁用：1</a>）</td>
<td><a href="../rtc_binding_reference/P015_microchip_rtc-g1.md#std-dtcompatible-microchip-rtc-g1"><code>microchip,rtc-g1</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip SERCOM UART控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32cm_jh/common/pic32cm_jh.dtsi?plain=1#L229">已启用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P019_microchip_sercom-g1-uart.md#std-dtcompatible-microchip-sercom-g1-uart"><code>microchip,sercom-g1-uart</code></a></td>
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

PIC32CM JH01 Curiosity Nano用户指南提供开发板连接详情。（[PIC32CM JH01 Curiosity Nano用户指南（User Guide）](https://ww1.microchip.com/downloads/aemDocuments/documents/MCU32/ProductDocuments/UserGuides/PIC32CM-JH01-Curiosity-Nano%2B-Touch-User-Guide-DS70005552.pdf)）

<a id="programming-debugging"></a>

## 编程与调试（Programming & Debugging）

`pic32cm_jh01_cnano`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

<a id="flash-using-mplab-ipe"></a>

### 使用MPLAB IPE烧录（Flash）

使用MPLAB IPE烧录的方法见“使用Microchip MPLAB IPE烧录”。（[使用Microchip MPLAB IPE烧录（Flashing）](P001_Flashing_with_Microchip_MPLAB_IPE.md#microchip-mplab-ipe-flashing)）

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
    pic32cm5164jh01048        Microchip                PIC32CM5164JH01048           PIC32CM-JH   pack
    ```
3. 连接开发板（Connect the Board）


  - 将开发板DEBUG USB端口J18连接主机。
  - 该连接为开发板供电，并提供对板载嵌入式调试器（EDBG）的访问，使PyOCD能够对目标微控制器编程及调试。

<a id="building-and-flashing-the-application"></a>

### 构建与烧录应用（Building and Flashing）


1. 构建应用（Build the Application）

  可用west工具构建Blinky等Zephyr示例应用。从Zephyr工作区执行以下命令：

  ```text
  west build -b pic32cm_jh01_cnano -p -s samples/basic/blinky
  ```

  这将为pic32cm_jh01_cnano开发板构建Blinky应用。
2. 烧录设备（Flash the Device）

  构建完成后，用以下命令烧录固件：

  ```text
  west flash
  ```
3. 观察结果（Observe the Result）

  烧录后LED1应开始闪烁，表明应用成功运行。

<a id="references"></a>

## 参考资料（References）

PIC32CM JH01产品页面：

[https://www.microchip.com/en-us/product/PIC32CM5164JH01048](https://www.microchip.com/en-us/product/PIC32CM5164JH01048)

PIC32CM JH01 Curiosity Nano评估套件页面：

[https://www.microchip.com/en-us/development-tool/ev29g58a](https://www.microchip.com/en-us/development-tool/ev29g58a)

## 译注

原文自动生成目标表列8405248 B闪存，仍保留其统计值；板载调试器在不同段落分别称nEDBG及EDBG。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [ev29g58a](https://www.microchip.com/en-us/development-tool/ev29g58a)：HTTP Error 403: Forbidden。
- [PIC32CM5164JH01048](https://www.microchip.com/en-us/product/PIC32CM5164JH01048)：HTTP Error 403: Forbidden。

---

[上一章](P016_PIC32CM_GC00_Curiosity_Pro.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P018_PIC32CM_JH01_Curiosity_Pro.md)
