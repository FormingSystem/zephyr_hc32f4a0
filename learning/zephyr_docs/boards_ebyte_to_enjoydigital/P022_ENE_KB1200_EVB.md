---
id: learning.zephyr-docs.boards-ebyte-to-enjoydigital.page-22
title: ENE KB1200 EVB
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ene/kb1200_evb/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="kb1200_evb"></a>

# 第22章\_ENE KB1200_EVB

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ene/kb1200_evb/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`kb1200_evb`

厂商（Vendor）：

[ENE Technology, Inc.公司](https://docs.zephyrproject.org/latest/boards/index.html#vendor=ene)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[kb1200](https://docs.zephyrproject.org/latest/boards/index.html#soc=kb1200)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ene/kb1200_evb/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

KB1200_EVB套件是评估ENE KB1200系列微控制器的开发平台，需要搭配KB1200器件使用。

<a id="hardware"></a>

## 硬件（Hardware）


- ARM Cortex-M4F处理器
- 512 KB闪存及320 KB RAM
- ADC与GPIO排针（Headers）
- SER1、SER2及SER3
- 风扇脉宽调制接口（FAN PWM）
- ENE调试接口（Debug Interface）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`kb1200_evb`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="kb1200_evb-hw-features"></a>

<a id="kb1200_evb-kb1200_evb/kb1200-hw-features-section"></a>

#### `kb1200_evb/kb1200`目标（Target）

<a id="kb1200_evb-kb1200_evb/kb1200-hw-features-panel"></a>

<a id="kb1200_evb-kb1200_evb/kb1200-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、256 KiB Flash。

<a id="kb1200_evb-kb1200_evb/kb1200-hw-features-table"></a>

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
<td>ARM Cortex-M4 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P024_arm_cortex-m4.md#std-dtcompatible-arm-cortex-m4"><code>arm,cortex-m4</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>ENE KB1200模数转换（ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L128">已启用：1</a>）</td>
<td><a href="../hardware/P888_ENEKB1200模数转换器绑定.md#dtbinding-ene-kb1200-adc"><code>ene,kb1200-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>ENE KB1200 GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L63">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L73">已禁用：3</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P020_ene_kb1200-gpio.md#std-dtcompatible-ene-kb1200-gpio"><code>ene,kb1200-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>ENE I2C／系统管理总线（SMB）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L250">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L259">已禁用：8</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P017_ene_kb1200-i2c.md#std-dtcompatible-ene-kb1200-i2c"><code>ene,kb1200-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ene/kb1200_evb/kb1200_evb.dts?plain=1#L30">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ene/kb1200_evb/kb1200_evb.dts?plain=1#L40">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>ENE电源管理器（Power Manager）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P006_ene_kb1200-pmu.md#std-dtcompatible-ene-kb1200-pmu"><code>ene,kb1200-pmu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ENE通用配置（General Configuration）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L51">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P005_ene_kb1200-gcfg.md#std-dtcompatible-ene-kb1200-gcfg"><code>ene,kb1200-gcfg</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>ENE KB1200引脚控制器是单实例节点（Singleton Node），负责控制引脚功能选择及属性（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P021_ene_kb1200-pinctrl.md#std-dtcompatible-ene-kb1200-pinctrl"><code>ene,kb1200-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>ENE脉宽调制器（PWM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L135">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L142">已禁用：8</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P014_ene_kb1200-pwm.md#std-dtcompatible-ene-kb1200-pwm"><code>ene,kb1200-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ENE KB1200通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L104">已启用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P020_ene_kb1200-uart.md#std-dtcompatible-ene-kb1200-uart"><code>ene,kb1200-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">转速计（Tachometer）</td>
<td>片上（On-Chip）</td>
<td>ENE KB1200转速计（Tachometer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L219">已启用：4</a>）</td>
<td><a href="../auxdisplay_iio_tach_binding_reference/P014_ene_kb1200-tach.md#std-dtcompatible-ene-kb1200-tach"><code>ene,kb1200-tach</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>ENE看门狗定时器（Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L243">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P012_ene_kb1200-watchdog.md#std-dtcompatible-ene-kb1200-watchdog"><code>ene,kb1200-watchdog</code></a></td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

KB1200 MCU配置为使用96 MHz内部振荡器及片上DPLL，生成96 MHz／48 MHz／24 MHz／12 MHz嵌入式控制器（EC）时钟。见处理器时钟控制寄存器，以及第5.1节General Configuration（通用配置）。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`kb1200_evb`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

安装正确的排针后，开发板支持SWD调试接口。

通过SWD烧录时，需要安装编程器驱动。例如SEGGER J-Link驱动位于[https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)。

<a id="debugging"></a>

### 调试（Debugging）

使用J-Link的SWD接口（Use SWD with a J-Link）

<a id="references"></a>

### 参考资料（References）

## 译注

KB1200的片上96 MHz源及96／48／24／12 MHz EC时钟选择依原文保留，未套用KB1062配置。

---

[上一章](P021_ENE_KB1062_EVB.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P023_EnjoyDigital.md)
