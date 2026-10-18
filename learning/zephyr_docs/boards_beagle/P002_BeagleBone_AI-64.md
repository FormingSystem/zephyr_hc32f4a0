---
id: learning.zephyr-docs.boards-beagle.page-2
title: BeagleBone AI-64
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/beagle/beaglebone_ai64/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="beaglebone_ai64"></a>

# 第2章\_BeagleBone AI-64

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/beagle/beaglebone_ai64/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/beaglebone_ai_64.webp](images/beaglebone_ai_64.webp)](images/beaglebone_ai_64.webp)

BeagleBone AI-64

名称（Name）：

`beaglebone_ai64`

厂商（Vendor）：

[BeagleBoard.org基金会（Foundation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=beagle)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[j721e](https://docs.zephyrproject.org/latest/boards/index.html#soc=j721e)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/beagle/beaglebone_ai64/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

BeagleBone AI-64是基于TI J721E SoC的计算平台，该SoC面向汽车应用。

<a id="hardware"></a>

## 硬件（Hardware）

BeagleBone AI-64使用TI J721E SoC，包含主域（MAIN）、微控制器域（MCU）及唤醒域（WKUP）。本文介绍在MAIN和MCU域Cortex-R5F内核上运行Zephyr。

<a id="l1-memory-system"></a>

### 一级存储系统（L1 Memory System）


- 16 KB指令缓存（Instruction Cache）
- 16 KB数据缓存（Data Cache）
- 64 KB紧耦合存储器（TCM）

<a id="region-address-translation"></a>

### 区域地址转换（RAT / Region Address Translation）

RAT模块按区域进行地址转换，将32位输入地址转换为48位输出地址。如果某已配置区域处于启用状态，起始地址位于该区域的输入事务（Transaction）会进行地址转换。

<a id="vim-interrupt-controller"></a>

### 向量中断管理器（VIM）中断控制器

VIM汇聚设备中断并发送给R5F CPU。每个R5F内核支持512路中断输入，每路可为电平或脉冲触发，均为高电平有效。VIM为每个内核提供IRQ及FIQ两个中断输出。

<a id="supported-features"></a>

## 支持的功能（Supported Features）

`beaglebone_ai64`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="beaglebone_ai64-hw-features"></a>

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f0_0-hw-features-section"></a>

### `beaglebone_ai64/j721e/main_r5f0_0`目标（Target）

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f0_0-hw-features-panel"></a>

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f0_0-hw-features-memory"></a>

该开发板目标的片上存储容量：14 MiB RAM、N/A Flash。

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f0_0-hw-features-table"></a>

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
<td>ARM Cortex-R5F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P012_arm_cortex-r5f.md#std-dtcompatible-arm-cortex-r5f"><code>arm,cortex-r5f</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_main_r5f0_0.dts?plain=1#L56">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Davinci及Keystone器件的GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/j721e_main.dtsi?plain=1#L77">已禁用：24</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P014_ti_davinci-gpio.md#std-dtcompatible-ti-davinci-gpio"><code>ti,davinci-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L125">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L59">已禁用：6</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P013_ti_omap-i2c.md#std-dtcompatible-ti-omap-i2c"><code>ti,omap-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>TI向量中断管理器（VIM）是TI专用外部中断控制器IP，兼容R5F的向量中断控制器（VIC）端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L44">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P009_ti_vim.md#std-dtcompatible-ti-vim"><code>ti,vim</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP邮箱（MAILBOX）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L156">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L167">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P055_TIOMAP邮箱绑定.md#dtbinding-ti-omap-mailbox"><code>ti,omap-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>TI K3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P013_ti_k3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl"><code>ti,k3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L146">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L136">已禁用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>RMPSG UART设备（拼写依原文保留）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_main_r5f0_0.dts?plain=1#L62">已启用：1</a>）</td>
<td><a href="../intercore_reference/P187_RPMsg串口设备树绑定.md#dtbinding-rpmsg-uart"><code>rpmsg-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_main_r5f0_0.dts?plain=1#L33">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>TI双模式定时器（Dual-Mode Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L178">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L187">已禁用：3</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P012_ti_am654-timer.md#std-dtcompatible-ti-am654-timer"><code>ti,am654-timer</code></a></td>
</tr>
</table>

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f0_1-hw-features-section"></a>

### `beaglebone_ai64/j721e/main_r5f0_1`目标（Target）

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f0_1-hw-features-panel"></a>

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f0_1-hw-features-memory"></a>

该开发板目标的片上存储容量：14 MiB RAM、N/A Flash。

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f0_1-hw-features-table"></a>

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
<td>ARM Cortex-R5F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P012_arm_cortex-r5f.md#std-dtcompatible-arm-cortex-r5f"><code>arm,cortex-r5f</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_main_r5f0_1.dts?plain=1#L50">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Davinci及Keystone器件的GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/j721e_main.dtsi?plain=1#L77">已禁用：24</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P014_ti_davinci-gpio.md#std-dtcompatible-ti-davinci-gpio"><code>ti,davinci-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L59">已禁用：7</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P013_ti_omap-i2c.md#std-dtcompatible-ti-omap-i2c"><code>ti,omap-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>TI向量中断管理器（VIM）是TI专用外部中断控制器IP，兼容R5F的向量中断控制器（VIC）端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L44">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P009_ti_vim.md#std-dtcompatible-ti-vim"><code>ti,vim</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP邮箱（MAILBOX）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L156">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L167">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P055_TIOMAP邮箱绑定.md#dtbinding-ti-omap-mailbox"><code>ti,omap-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>TI K3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P013_ti_k3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl"><code>ti,k3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L136">已禁用：2</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>RMPSG UART设备（拼写依原文保留）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_main_r5f0_1.dts?plain=1#L56">已启用：1</a>）</td>
<td><a href="../intercore_reference/P187_RPMsg串口设备树绑定.md#dtbinding-rpmsg-uart"><code>rpmsg-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_main_r5f0_1.dts?plain=1#L27">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>TI双模式定时器（Dual-Mode Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L187">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L178">已禁用：3</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P012_ti_am654-timer.md#std-dtcompatible-ti-am654-timer"><code>ti,am654-timer</code></a></td>
</tr>
</table>

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f1_0-hw-features-section"></a>

### `beaglebone_ai64/j721e/main_r5f1_0`目标（Target）

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f1_0-hw-features-panel"></a>

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f1_0-hw-features-memory"></a>

该开发板目标的片上存储容量：14 MiB RAM、N/A Flash。

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f1_0-hw-features-table"></a>

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
<td>ARM Cortex-R5F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P012_arm_cortex-r5f.md#std-dtcompatible-arm-cortex-r5f"><code>arm,cortex-r5f</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_main_r5f1_0.dts?plain=1#L50">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Davinci及Keystone器件的GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/j721e_main.dtsi?plain=1#L77">已禁用：24</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P014_ti_davinci-gpio.md#std-dtcompatible-ti-davinci-gpio"><code>ti,davinci-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L59">已禁用：7</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P013_ti_omap-i2c.md#std-dtcompatible-ti-omap-i2c"><code>ti,omap-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>TI向量中断管理器（VIM）是TI专用外部中断控制器IP，兼容R5F的向量中断控制器（VIC）端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L44">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P009_ti_vim.md#std-dtcompatible-ti-vim"><code>ti,vim</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP邮箱（MAILBOX）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L167">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L156">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P055_TIOMAP邮箱绑定.md#dtbinding-ti-omap-mailbox"><code>ti,omap-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>TI K3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P013_ti_k3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl"><code>ti,k3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L136">已禁用：2</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>RMPSG UART设备（拼写依原文保留）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_main_r5f1_0.dts?plain=1#L56">已启用：1</a>）</td>
<td><a href="../intercore_reference/P187_RPMsg串口设备树绑定.md#dtbinding-rpmsg-uart"><code>rpmsg-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_main_r5f1_0.dts?plain=1#L27">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>TI双模式定时器（Dual-Mode Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L196">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L178">已禁用：3</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P012_ti_am654-timer.md#std-dtcompatible-ti-am654-timer"><code>ti,am654-timer</code></a></td>
</tr>
</table>

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f1_1-hw-features-section"></a>

### `beaglebone_ai64/j721e/main_r5f1_1`目标（Target）

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f1_1-hw-features-panel"></a>

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f1_1-hw-features-memory"></a>

该开发板目标的片上存储容量：14 MiB RAM、N/A Flash。

<a id="beaglebone_ai64-beaglebone_ai64/j721e/main_r5f1_1-hw-features-table"></a>

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
<td>ARM Cortex-R5F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P012_arm_cortex-r5f.md#std-dtcompatible-arm-cortex-r5f"><code>arm,cortex-r5f</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_main_r5f1_1.dts?plain=1#L50">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Davinci及Keystone器件的GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/j721e_main.dtsi?plain=1#L77">已禁用：24</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P014_ti_davinci-gpio.md#std-dtcompatible-ti-davinci-gpio"><code>ti,davinci-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L59">已禁用：7</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P013_ti_omap-i2c.md#std-dtcompatible-ti-omap-i2c"><code>ti,omap-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>TI向量中断管理器（VIM）是TI专用外部中断控制器IP，兼容R5F的向量中断控制器（VIC）端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L44">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P009_ti_vim.md#std-dtcompatible-ti-vim"><code>ti,vim</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP邮箱（MAILBOX）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L167">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L156">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P055_TIOMAP邮箱绑定.md#dtbinding-ti-omap-mailbox"><code>ti,omap-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>TI K3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P013_ti_k3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl"><code>ti,k3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L136">已禁用：2</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>RMPSG UART设备（拼写依原文保留）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_main_r5f1_1.dts?plain=1#L56">已启用：1</a>）</td>
<td><a href="../intercore_reference/P187_RPMsg串口设备树绑定.md#dtbinding-rpmsg-uart"><code>rpmsg-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_main_r5f1_1.dts?plain=1#L27">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>TI双模式定时器（Dual-Mode Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L205">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_main_r5.dtsi?plain=1#L178">已禁用：3</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P012_ti_am654-timer.md#std-dtcompatible-ti-am654-timer"><code>ti,am654-timer</code></a></td>
</tr>
</table>

<a id="beaglebone_ai64-beaglebone_ai64/j721e/mcu_r5f0_0-hw-features-section"></a>

### `beaglebone_ai64/j721e/mcu_r5f0_0`目标（Target）

<a id="beaglebone_ai64-beaglebone_ai64/j721e/mcu_r5f0_0-hw-features-panel"></a>

<a id="beaglebone_ai64-beaglebone_ai64/j721e/mcu_r5f0_0-hw-features-memory"></a>

该开发板目标的片上存储容量：14 MiB RAM、N/A Flash。

<a id="beaglebone_ai64-beaglebone_ai64/j721e/mcu_r5f0_0-hw-features-table"></a>

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
<td>ARM Cortex-R5F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_mcu_r5.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P012_arm_cortex-r5f.md#std-dtcompatible-arm-cortex-r5f"><code>arm,cortex-r5f</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_mcu_r5f0_0.dts?plain=1#L51">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>TI向量中断管理器（VIM）是TI专用外部中断控制器IP，兼容R5F的向量中断控制器（VIC）端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_mcu_r5.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P009_ti_vim.md#std-dtcompatible-ti-vim"><code>ti,vim</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP邮箱（MAILBOX）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_mcu_r5.dtsi?plain=1#L52">已启用：1</a>）</td>
<td><a href="../intercore_reference/P055_TIOMAP邮箱绑定.md#dtbinding-ti-omap-mailbox"><code>ti,omap-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_mcu.dtsi?plain=1#L15">已禁用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>RMPSG UART设备（拼写依原文保留）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_mcu_r5f0_0.dts?plain=1#L57">已启用：1</a>）</td>
<td><a href="../intercore_reference/P187_RPMsg串口设备树绑定.md#dtbinding-rpmsg-uart"><code>rpmsg-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_mcu_r5f0_0.dts?plain=1#L28">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>TI双模式定时器（Dual-Mode Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_mcu.dtsi?plain=1#L26">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_mcu.dtsi?plain=1#L35">已禁用：1</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P012_ti_am654-timer.md#std-dtcompatible-ti-am654-timer"><code>ti,am654-timer</code></a></td>
</tr>
</table>

<a id="beaglebone_ai64-beaglebone_ai64/j721e/mcu_r5f0_1-hw-features-section"></a>

### `beaglebone_ai64/j721e/mcu_r5f0_1`目标（Target）

<a id="beaglebone_ai64-beaglebone_ai64/j721e/mcu_r5f0_1-hw-features-panel"></a>

<a id="beaglebone_ai64-beaglebone_ai64/j721e/mcu_r5f0_1-hw-features-memory"></a>

该开发板目标的片上存储容量：14 MiB RAM、N/A Flash。

<a id="beaglebone_ai64-beaglebone_ai64/j721e/mcu_r5f0_1-hw-features-table"></a>

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
<td>ARM Cortex-R5F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_mcu_r5.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P012_arm_cortex-r5f.md#std-dtcompatible-arm-cortex-r5f"><code>arm,cortex-r5f</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_mcu_r5f0_1.dts?plain=1#L51">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>TI向量中断管理器（VIM）是TI专用外部中断控制器IP，兼容R5F的向量中断控制器（VIC）端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_mcu_r5.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P009_ti_vim.md#std-dtcompatible-ti-vim"><code>ti,vim</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP邮箱（MAILBOX）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_mcu_r5.dtsi?plain=1#L52">已启用：1</a>）</td>
<td><a href="../intercore_reference/P055_TIOMAP邮箱绑定.md#dtbinding-ti-omap-mailbox"><code>ti,omap-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_mcu.dtsi?plain=1#L15">已禁用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>RMPSG UART设备（拼写依原文保留）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_mcu_r5f0_1.dts?plain=1#L57">已启用：1</a>）</td>
<td><a href="../intercore_reference/P187_RPMsg串口设备树绑定.md#dtbinding-rpmsg-uart"><code>rpmsg-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beaglebone_ai64/beaglebone_ai64_j721e_mcu_r5f0_1.dts?plain=1#L28">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>TI双模式定时器（Dual-Mode Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_mcu.dtsi?plain=1#L35">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/j721e_mcu.dtsi?plain=1#L26">已禁用：1</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P012_ti_am654-timer.md#std-dtcompatible-ti-am654-timer"><code>ti,am654-timer</code></a></td>
</tr>
</table>

<a id="running-zephyr"></a>

## 运行Zephyr（Running Zephyr）

J721E没有供R5内核单独使用的闪存。因此需要由A72内核将R5程序加载到正确内存地址，设置程序计数器（PC）并启动处理器。可在A72上的Linux中通过远端处理器框架（remoteproc）完成。

默认R5内存保护单元（MPU）只允许从ATCM／BTCM执行指令。Linux还为每个R5预留了若干DRAM区域，可用于进程间／处理器间通信（IPC，DDR0）及数据（DDR1）。配置MPU后，DDR1也可用作可执行区域。

下表为A72视角到R5可用内存的映射。R5始终将本地ATCM视为`0x00000000`，BTCM视为`0x41010000`，参见TRM表2-5。remoteproc使用的ATCM／BTCM从端口列于下表，来自Linux的`k3-j721e-main.dtsi`。如果运行中的Linux设备树包含`k3-j721e-ti-ipc-firmware.dtsi`，DDR区域依该文件配置；可在板上执行`ls /proc/device-tree/reserved-memory/`确认。

主域（MAIN），Linux文件`k3-j721e-main.dtsi`：

<table>
<tr>
<th>区域（Region）</th>
<th>R5FSS0内核0（Core0）</th>
<th>R5FSS0内核1（Core1）</th>
<th>R5FSS1内核0（Core0）</th>
<th>R5FSS1内核1（Core1）</th>
<th>大小（Size）</th>
</tr>
<tr>
<td>A区紧耦合存储器（ATCM）</td>
<td>0x05c00000</td>
<td>0x05d00000</td>
<td>0x05e00000</td>
<td>0x05f00000</td>
<td>32KB</td>
</tr>
<tr>
<td>B区紧耦合存储器（BTCM）</td>
<td>0x05c10000</td>
<td>0x05d10000</td>
<td>0x05e10000</td>
<td>0x05f10000</td>
<td>32KB</td>
</tr>
<tr>
<td>DDR0，用于IPC</td>
<td>0xA2000000</td>
<td>0xA3000000</td>
<td>0xA4000000</td>
<td>0xA5000000</td>
<td>1MB</td>
</tr>
<tr>
<td>资源表（RSC Table）</td>
<td>0xA2100000</td>
<td>0xA3100000</td>
<td>0xA4100000</td>
<td>0xA5100000</td>
<td>1MB</td>
</tr>
<tr>
<td>DDR1，DRAM区域</td>
<td>0xA2200000</td>
<td>0xA3200000</td>
<td>0xA4200000</td>
<td>0xA5200000</td>
<td>14MB</td>
</tr>
</table>

MCU域，Linux文件`k3-j721e-mcu-wakeup.dtsi`：

<table>
<tr>
<th>区域（Region）</th>
<th>MCU R5FSS0内核0</th>
<th>MCU R5FSS0内核1</th>
<th>大小（Size）</th>
</tr>
<tr>
<td>A区紧耦合存储器（ATCM）</td>
<td>0x41000000</td>
<td>0x41400000</td>
<td>32KB</td>
</tr>
<tr>
<td>B区紧耦合存储器（BTCM）</td>
<td>0x41010000</td>
<td>0x41410000</td>
<td>32KB</td>
</tr>
<tr>
<td>DDR0，用于IPC</td>
<td>0xA0000000</td>
<td>0xA1000000</td>
<td>1MB</td>
</tr>
<tr>
<td>资源表（RSC Table）</td>
<td>0xA0100000</td>
<td>0xA1100000</td>
<td>1MB</td>
</tr>
<tr>
<td>DDR1，DRAM区域</td>
<td>0xA0200000</td>
<td>0xA1200000</td>
<td>14MB</td>
</tr>
</table>

U-Boot通常在Linux之前启动MCU R5FSS0 Core0，因此该内核在remoteproc中显示为仅IPC／已附接（IPC-Only / Attached）状态。要从Linux替换其固件，内核必须处于remoteproc模式，而非后期附接（Late-Attached）状态；或者由引导加载程序以`j7-mcu-r5f0_0-fw`加载Zephyr。BeagleBone AI-64默认Linux设备树将两个MCU内核配置为锁步模式（Lockstep，`ti,cluster-mode = 1`），只有将簇切换为分离模式（Split Mode）后，Core1才会成为独立remoteproc设备。

<a id="remoteproc-nodes"></a>

### remoteproc节点（Nodes）

每个MAIN R5内核都由Linux通过remoteproc启动。典型设备节点与固件名称如下，来自`k3-j721e-main.dtsi`：

<table>
<tr>
<th>Linux remoteproc节点</th>
<th><code>firmware-name</code></th>
<th>Zephyr开发板目标（Board Target）</th>
</tr>
<tr>
<td><code>/dev/remoteproc/j7-main-r5f0_0</code></td>
<td><code>j7-main-r5f0_0-fw</code></td>
<td><code>main_r5f0_0</code></td>
</tr>
<tr>
<td><code>/dev/remoteproc/j7-main-r5f0_1</code></td>
<td><code>j7-main-r5f0_1-fw</code></td>
<td><code>main_r5f0_1</code></td>
</tr>
<tr>
<td><code>/dev/remoteproc/j7-main-r5f1_0</code></td>
<td><code>j7-main-r5f1_0-fw</code></td>
<td><code>main_r5f1_0</code></td>
</tr>
<tr>
<td><code>/dev/remoteproc/j7-main-r5f1_1</code></td>
<td><code>j7-main-r5f1_1-fw</code></td>
<td><code>main_r5f1_1</code></td>
</tr>
<tr>
<td><code>41000000.r5f</code>，remoteproc12</td>
<td><code>j7-mcu-r5f0_0-fw</code></td>
<td><code>mcu_r5f0_0</code></td>
</tr>
<tr>
<td><code>41400000.r5f</code>，分离模式（Split Mode）</td>
<td><code>j7-mcu-r5f0_1-fw</code></td>
<td><code>mcu_r5f0_1</code></td>
</tr>
</table>

<a id="steps-to-build-and-run-an-image"></a>

### 构建并运行镜像的步骤（Steps to Build and Run）

以下以BeagleBone AI-64某个Cortex-R5F内核上的[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例：

```text
# From the root of the zephyr repository
west build -b beaglebone_ai64/j721e/main_r5f0_0 samples/hello_world
```

加载镜像，以R5FSS0 Core0为例：

将Zephyr镜像复制到目标Linux的`/lib/firmware/`目录。

`cp build/zephyr/zephyr.elf /lib/firmware/`



确保该内核未在运行。

`echo stop > /dev/remoteproc/j7-main-r5f0_0/state`



为remoteproc模块配置镜像名称。

`echo zephyr.elf > /dev/remoteproc/j7-main-r5f0_0/firmware`



配置镜像名称后，发送启动命令。

`echo start > /dev/remoteproc/j7-main-r5f0_0/state`

对`main_r5f0_1`、`main_r5f1_0`、`main_r5f1_1`及MCU目标，使用上表中对应的remoteproc路径。MCU Core0通常已经附接；`echo start`仅在内核离线（Offline）后有效。

<a id="console"></a>

### 控制台（Console）

`main_r5f0_0`使用UART2作为`zephyr,console`，RX位于P8.22，TX位于P8.34；TRM表2-1列出UART2地址为`0x02820000`，表9-47列出VIM中断号为160。

其他MAIN R5目标及两个MCU R5目标可通过设备树覆盖文件（Overlays）配置远端处理器消息（RPMsg）UART控制台。在Linux中启用RPMsg TTY驱动`rpmsg_tty`，查找`/dev/ttyRPMSG*`；绑定顺序取决于哪些内核正在运行。

<a id="references"></a>

## 参考资料（References）


- [BeagleBone AI-64主页（Homepage）](https://www.beagleboard.org/boards/beaglebone-ai-64)
- [J721E技术参考手册（TRM，SPRUIL1D）](https://www.ti.com/lit/zip/spruil1)：表2-1为MAIN内存映射，表2-5为R5 TCM／VIM，表9-47至9-50为R5F VIM中断编号，表7-2／7-4为NAVSS邮箱
- [PSDK RTOS J721E内存映射（Memory Map）](https://software-dl.ti.com/jacinto7/esd/processor-sdk-rtos-jacinto7/latest/exports/docs/psdk_rtos/docs/user_guide/developer_notes_memory_map.html)
- [PSDK Linux IPC J721E](https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-jacinto7/11_02_01_03/exports/docs/linux/Foundational_Components_IPC_J721E.html)
- Linux的`k3-j721e-main.dtsi`及`k3-j721e-ti-ipc-firmware.dtsi`

## 译注

原文自动生成绑定说明将RPMsg写为RMPSG；保留该拼写。remoteproc节点与DDR预留地址依运行中的Linux设备树而定；MCU Core0已附接和默认锁步模式的限制均按原文保留。

---

[上一章](P001_BeagleBadge.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_BeagleConnect_Freedom.md)
