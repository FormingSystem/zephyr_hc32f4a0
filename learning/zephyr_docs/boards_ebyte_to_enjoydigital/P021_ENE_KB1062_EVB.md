---
id: learning.zephyr-docs.boards-ebyte-to-enjoydigital.page-21
title: ENE KB1062 EVB
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ene/kb1062_evb/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="kb1062_evb"></a>

# 第21章\_ENE KB1062_EVB

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ene/kb1062_evb/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`kb1062_evb`

厂商（Vendor）：

[ENE Technology, Inc.公司](https://docs.zephyrproject.org/latest/boards/index.html#vendor=ene)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[kb1062](https://docs.zephyrproject.org/latest/boards/index.html#soc=kb1062)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ene/kb1062_evb/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

KB1062_EVB套件是评估ENE KB106X系列微控制器的开发平台，需要搭配KB1062器件使用。

<a id="hardware"></a>

## 硬件（Hardware）


- ARM Cortex-M3处理器（Processor）
- 256 KB闪存及64 KB RAM
- ADC与GPIO排针（Headers）
- SER串口（Serial Port）
- 风扇脉宽调制接口（FAN PWM）
- ENE调试接口（Debug Interface）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`kb1062_evb`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="kb1062_evb-hw-features"></a>

<a id="kb1062_evb-kb1062_evb/kb1062-hw-features-section"></a>

#### `kb1062_evb/kb1062`目标（Target）

<a id="kb1062_evb-kb1062_evb/kb1062-hw-features-panel"></a>

<a id="kb1062_evb-kb1062_evb/kb1062-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、256 KiB Flash。

<a id="kb1062_evb-kb1062_evb/kb1062-hw-features-table"></a>

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
<td>ARM Cortex-M3处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P021_arm_cortex-m3.md#std-dtcompatible-arm-cortex-m3"><code>arm,cortex-m3</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>ENE KB106X模数转换（ADC）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L122">已禁用：1</a>）</td>
<td><a href="../hardware/P887_ENEKB106x模数转换器绑定.md#dtbinding-ene-kb106x-adc"><code>ene,kb106x-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>ENE KB106X通用输入输出（GPIO）端口节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L64">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L74">已禁用：3</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P019_ene_kb106x-gpio.md#std-dtcompatible-ene-kb106x-gpio"><code>ene,kb106x-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>ENE I2C／系统管理总线（SMB）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L192">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L201">已禁用：5</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P016_ene_kb106x-i2c.md#std-dtcompatible-ene-kb106x-i2c"><code>ene,kb106x-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ene/kb1062_evb/kb1062_evb.dts?plain=1#L33">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ene/kb1062_evb/kb1062_evb.dts?plain=1#L43">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>ENE通用配置（General Configuration）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P004_ene_kb106x-gcfg.md#std-dtcompatible-ene-kb106x-gcfg"><code>ene,kb106x-gcfg</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>ENE KB106X引脚控制器是单实例节点（Singleton Node），负责控制引脚功能选择及属性（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L57">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P020_ene_kb106x-pinctrl.md#std-dtcompatible-ene-kb106x-pinctrl"><code>ene,kb106x-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>ENE脉宽调制器（PWM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L129">已禁用：4</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P013_ene_kb106x-pwm.md#std-dtcompatible-ene-kb106x-pwm"><code>ene,kb106x-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ENE KB106X通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L115">已启用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P019_ene_kb106x-uart.md#std-dtcompatible-ene-kb106x-uart"><code>ene,kb106x-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">转速计（Tachometer）</td>
<td>片上（On-Chip）</td>
<td>ENE KB106X转速计（Tachometer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L168">已禁用：4</a>）</td>
<td><a href="../auxdisplay_iio_tach_binding_reference/P013_ene_kb106x-tach.md#std-dtcompatible-ene-kb106x-tach"><code>ene,kb106x-tach</code></a></td>
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
<td>ENE看门狗定时器（Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L161">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P011_ene_kb106x-watchdog.md#std-dtcompatible-ene-kb106x-watchdog"><code>ene,kb106x-watchdog</code></a></td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

KB106x MCU配置为使用48 MHz内部振荡器及片上数字锁相环（DPLL），生成48 MHz／24 MHz嵌入式控制器（EC）时钟。见处理器时钟控制寄存器，以及第5.1节General Configuration（通用配置）。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`kb1062_evb`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

KB1062的片上48 MHz源及48／24 MHz EC时钟选择、安装调试排针的条件依原文保留。

---

[上一章](P020_ENE.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P022_ENE_KB1200_EVB.md)
