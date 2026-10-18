---
id: learning.zephyr-docs.boards-infineon-innblue.page-18
title: Kit T2G-C2-D-6M Lite
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/infineon/kit_t2g_c2d6m_lite/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="kit_t2g_c2d6m_lite"></a>

# 第18章\_T2G-C2-D-6M Lite套件（Kit）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/infineon/kit_t2g_c2d6m_lite/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/kit_t2g_c2d6m_lite.webp](images/kit_t2g_c2d6m_lite.webp)](images/kit_t2g_c2d6m_lite.webp)

T2G-C2-D-6M Lite套件（Kit）

名称（Name）：

`kit_t2g_c2d6m_lite`

厂商（Vendor）：

[英飞凌科技（Infineon Technologies）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=infineon)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[cyt4dnjbzs](https://docs.zephyrproject.org/latest/boards/index.html#soc=cyt4dnjbzs)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/infineon/kit_t2g_c2d6m_lite/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

KIT_T2G-C-2D-6M_LITE套件用于评估TRAVEO T2G Cluster 2D系列CYT4DN器件及开发应用。TRAVEO T2G CYT4DN MCU专为汽车仪表盘（Instrument Cluster）及抬头显示（HUD / Head-Up Display）应用设计，是可编程的嵌入式片上系统，集成两个320 MHz Arm Cortex-M7 CPU作为主应用处理器，以及一个100 MHz Arm Cortex-M0+，支持以下功能：


- 低功耗运行，包括活动（Active）、睡眠（Sleep）、低功耗睡眠（Low-Power Sleep）、深度睡眠（Deep Sleep）及休眠（Hibernate）模式
- 6336 KB代码闪存（Code Flash）、额外128 KB工作闪存（Work Flash）及640 KB SRAM
- 可编程模拟和数字外设，可缩短产品上市时间

<a id="hardware"></a>

## 硬件（Hardware）

KIT_T2G-C-2D-6M_LITE更多信息见：


- <a id="id5"></a>

  [kit_t2g_c2d6m_lite开发板网站](https://www.infineon.com/evaluation-board/KIT-T2G-C-2D-6M-LITE) [注2](#id4)
- <a id="id3"></a>

  [T2G_C_2D SoC网站](https://www.infineon.com/products/microcontroller/32-bit-traveo-t2g-arm-cortex/for-cluster/t2g-cyt4dn) [注1](#id2)

<a id="kit-features"></a>

### 套件特性（Kit Features）


- 采用327-BGA封装CYT4DN MCU的评估板，包含两个320 MHz Arm Cortex-M7 CPU及一个100 MHz Arm Cortex-M0+ CPU
- 开发板提供完整系统配置，包括千兆以太网PHY和连接器、CAN FD收发器、用户LED、按键及电位器
- 兼容Arduino的排针，用于连接Arduino扩展板（Shields）
- 完全兼容ModusToolbox v3.0
- 板载KitProg3通过USB连接器提供SWD编程／调试、USB-UART及USB-I2C桥接功能
- 评估板支持CYT4DN在3.3 V至5.0 V电压范围运行

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`kit_t2g_c2d6m_lite`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="kit_t2g_c2d6m_lite-hw-features"></a>

<a id="kit_t2g_c2d6m_lite-kit_t2g_c2d6m_lite/cyt4dnjbzs/m0p-hw-features-section"></a>

#### `kit_t2g_c2d6m_lite/cyt4dnjbzs/m0p`目标（Target）

<a id="kit_t2g_c2d6m_lite-kit_t2g_c2d6m_lite/cyt4dnjbzs/m0p-hw-features-panel"></a>

<a id="kit_t2g_c2d6m_lite-kit_t2g_c2d6m_lite/cyt4dnjbzs/m0p-hw-features-memory"></a>

该开发板目标的片上存储容量：30 KiB RAM、6336 KiB Flash。

<a id="kit_t2g_c2d6m_lite-kit_t2g_c2d6m_lite/cyt4dnjbzs/m0p-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L26">已禁用：2</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>英飞凌串行通信模块（SCB / Serial Communication Blocks）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L469">已禁用：10</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P011_infineon_scb.md#std-dtcompatible-infineon-scb"><code>infineon,scb</code></a></td>
</tr>
<tr>
<td rowspan="6">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>英飞凌时钟振荡器（Clock Oscillators）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../timer_reference/P114_Infineon振荡器时钟绑定.md#dtbinding-infineon-clk-osc"><code>infineon,clk-osc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌锁相环（PLL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L41">已启用：7</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L120">已禁用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P007_infineon_clk-pll.md#std-dtcompatible-infineon-clk-pll"><code>infineon,clk-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌高频时钟（High Frequency Clock / clk_hf）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L136">已启用：13</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L253">已禁用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P006_infineon_cat1c-clk-hf.md#std-dtcompatible-infineon-cat1c-clk-hf"><code>infineon,cat1c-clk-hf</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L264">已启用：2</a>）</td>
<td><a href="../timer_reference/P110_固定比例时钟绑定.md#dtbinding-fixed-factor-clock"><code>fixed-factor-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌外设时钟组（Peripheral Clock Group）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L282">已启用：2</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P008_infineon_peri-clk.md#std-dtcompatible-infineon-peri-clk"><code>infineon,peri-clk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌外设分频器（Peripheral Divider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L574">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L287">已禁用：47</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P009_infineon_peri-div.md#std-dtcompatible-infineon-peri-div"><code>infineon,peri-div</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>英飞凌GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L227">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L150">已禁用：27</a>）</td>
<td><a href="../gpio_infineon_intel_ite_microchip_binding_reference/P001_infineon_gpio.md#std-dtcompatible-infineon-gpio"><code>infineon,gpio</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1 CPUSS系统中断多路复用器（System Interrupt Multiplexer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L59">已启用：1</a>）</td>
<td><a href="../infineon_microchip_interrupt_binding_reference/P003_infineon_sysintc.md#std-dtcompatible-infineon-sysintc"><code>infineon,sysintc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1 CPUSS中断多路复用器通道（Interrupt Multiplexer Channel）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L65">已启用：8</a>）</td>
<td><a href="../infineon_microchip_interrupt_binding_reference/P002_infineon_sysintc-mux.md#std-dtcompatible-infineon-sysintc-mux"><code>infineon,sysintc-mux</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/kit_t2g_c2d6m_lite/kit_t2g_c2d6m_lite_common.dtsi?plain=1#L15">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L136">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>英飞凌（Infineon）CAT1引脚控制容器（Pinctrl Container）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L145">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P001_infineon_pinctrl.md#std-dtcompatible-infineon-pinctrl"><code>infineon,pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1 UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L550">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L532">已禁用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P008_infineon_uart.md#std-dtcompatible-infineon-uart"><code>infineon,uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L43">已启用：3</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
</table>

<a id="kit_t2g_c2d6m_lite-kit_t2g_c2d6m_lite/cyt4dnjbzs/m7_0-hw-features-section"></a>

#### `kit_t2g_c2d6m_lite/cyt4dnjbzs/m7_0`目标（Target）

<a id="kit_t2g_c2d6m_lite-kit_t2g_c2d6m_lite/cyt4dnjbzs/m7_0-hw-features-panel"></a>

<a id="kit_t2g_c2d6m_lite-kit_t2g_c2d6m_lite/cyt4dnjbzs/m7_0-hw-features-memory"></a>

该开发板目标的片上存储容量：224 KiB RAM、6336 KiB Flash。

<a id="kit_t2g_c2d6m_lite-kit_t2g_c2d6m_lite/cyt4dnjbzs/m7_0-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L26">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L34">已禁用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>英飞凌串行通信模块（SCB / Serial Communication Blocks）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L469">已禁用：10</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P011_infineon_scb.md#std-dtcompatible-infineon-scb"><code>infineon,scb</code></a></td>
</tr>
<tr>
<td rowspan="6">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>英飞凌时钟振荡器（Clock Oscillators）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../timer_reference/P114_Infineon振荡器时钟绑定.md#dtbinding-infineon-clk-osc"><code>infineon,clk-osc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌锁相环（PLL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L41">已启用：7</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L120">已禁用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P007_infineon_clk-pll.md#std-dtcompatible-infineon-clk-pll"><code>infineon,clk-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌高频时钟（High Frequency Clock / clk_hf）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L136">已启用：13</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L253">已禁用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P006_infineon_cat1c-clk-hf.md#std-dtcompatible-infineon-cat1c-clk-hf"><code>infineon,cat1c-clk-hf</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L264">已启用：2</a>）</td>
<td><a href="../timer_reference/P110_固定比例时钟绑定.md#dtbinding-fixed-factor-clock"><code>fixed-factor-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌外设时钟组（Peripheral Clock Group）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L282">已启用：2</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P008_infineon_peri-clk.md#std-dtcompatible-infineon-peri-clk"><code>infineon,peri-clk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌外设分频器（Peripheral Divider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L574">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L287">已禁用：47</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P009_infineon_peri-div.md#std-dtcompatible-infineon-peri-div"><code>infineon,peri-div</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>英飞凌GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L150">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L161">已禁用：26</a>）</td>
<td><a href="../gpio_infineon_intel_ite_microchip_binding_reference/P001_infineon_gpio.md#std-dtcompatible-infineon-gpio"><code>infineon,gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/kit_t2g_c2d6m_lite/kit_t2g_c2d6m_lite_cyt4dnjbzs_m7_0.dts?plain=1#L30">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1 CPUSS系统中断多路复用器（System Interrupt Multiplexer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L59">已启用：1</a>）</td>
<td><a href="../infineon_microchip_interrupt_binding_reference/P003_infineon_sysintc.md#std-dtcompatible-infineon-sysintc"><code>infineon,sysintc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1 CPUSS中断多路复用器通道（Interrupt Multiplexer Channel）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L65">已启用：8</a>）</td>
<td><a href="../infineon_microchip_interrupt_binding_reference/P002_infineon_sysintc-mux.md#std-dtcompatible-infineon-sysintc-mux"><code>infineon,sysintc-mux</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/kit_t2g_c2d6m_lite/kit_t2g_c2d6m_lite_common.dtsi?plain=1#L15">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L136">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>英飞凌（Infineon）CAT1引脚控制容器（Pinctrl Container）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L145">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P001_infineon_pinctrl.md#std-dtcompatible-infineon-pinctrl"><code>infineon,pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1 UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L532">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L550">已禁用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P008_infineon_uart.md#std-dtcompatible-infineon-uart"><code>infineon,uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L43">已启用：3</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
</table>

<a id="kit_t2g_c2d6m_lite-kit_t2g_c2d6m_lite/cyt4dnjbzs/m7_1-hw-features-section"></a>

#### `kit_t2g_c2d6m_lite/cyt4dnjbzs/m7_1`目标（Target）

<a id="kit_t2g_c2d6m_lite-kit_t2g_c2d6m_lite/cyt4dnjbzs/m7_1-hw-features-panel"></a>

<a id="kit_t2g_c2d6m_lite-kit_t2g_c2d6m_lite/cyt4dnjbzs/m7_1-hw-features-memory"></a>

该开发板目标的片上存储容量：256 KiB RAM、6336 KiB Flash。

<a id="kit_t2g_c2d6m_lite-kit_t2g_c2d6m_lite/cyt4dnjbzs/m7_1-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L34">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L26">已禁用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>英飞凌串行通信模块（SCB / Serial Communication Blocks）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L469">已禁用：9</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P011_infineon_scb.md#std-dtcompatible-infineon-scb"><code>infineon,scb</code></a></td>
</tr>
<tr>
<td rowspan="6">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>英飞凌时钟振荡器（Clock Oscillators）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../timer_reference/P114_Infineon振荡器时钟绑定.md#dtbinding-infineon-clk-osc"><code>infineon,clk-osc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌锁相环（PLL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L41">已启用：7</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L120">已禁用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P007_infineon_clk-pll.md#std-dtcompatible-infineon-clk-pll"><code>infineon,clk-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌高频时钟（High Frequency Clock / clk_hf）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L136">已启用：13</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L253">已禁用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P006_infineon_cat1c-clk-hf.md#std-dtcompatible-infineon-cat1c-clk-hf"><code>infineon,cat1c-clk-hf</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L264">已启用：2</a>）</td>
<td><a href="../timer_reference/P110_固定比例时钟绑定.md#dtbinding-fixed-factor-clock"><code>fixed-factor-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌外设时钟组（Peripheral Clock Group）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L282">已启用：2</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P008_infineon_peri-clk.md#std-dtcompatible-infineon-peri-clk"><code>infineon,peri-clk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌外设分频器（Peripheral Divider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L574">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/system_clocks.dtsi?plain=1#L287">已禁用：46</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P009_infineon_peri-div.md#std-dtcompatible-infineon-peri-div"><code>infineon,peri-div</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>英飞凌GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L150">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L161">已禁用：27</a>）</td>
<td><a href="../gpio_infineon_intel_ite_microchip_binding_reference/P001_infineon_gpio.md#std-dtcompatible-infineon-gpio"><code>infineon,gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/kit_t2g_c2d6m_lite/kit_t2g_c2d6m_lite_cyt4dnjbzs_m7_1.dts?plain=1#L30">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1 CPUSS系统中断多路复用器（System Interrupt Multiplexer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L59">已启用：1</a>）</td>
<td><a href="../infineon_microchip_interrupt_binding_reference/P003_infineon_sysintc.md#std-dtcompatible-infineon-sysintc"><code>infineon,sysintc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1 CPUSS中断多路复用器通道（Interrupt Multiplexer Channel）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L65">已启用：8</a>）</td>
<td><a href="../infineon_microchip_interrupt_binding_reference/P002_infineon_sysintc-mux.md#std-dtcompatible-infineon-sysintc-mux"><code>infineon,sysintc-mux</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/kit_t2g_c2d6m_lite/kit_t2g_c2d6m_lite_common.dtsi?plain=1#L15">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L136">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>英飞凌（Infineon）CAT1引脚控制容器（Pinctrl Container）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L145">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P001_infineon_pinctrl.md#std-dtcompatible-infineon-pinctrl"><code>infineon,pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1 UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L478">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L532">已禁用：2</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P008_infineon_uart.md#std-dtcompatible-infineon-uart"><code>infineon,uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1c/traveo/cyt4dn/cyt4dn.dtsi?plain=1#L43">已启用：3</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`kit_t2g_c2d6m_lite`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

<a id="building"></a>

### 构建（Building）

为Cortex-M0+内核构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例应用：

```text
# From the root of the zephyr repository
west build -b kit_t2g_c2d6m_lite/cyt4dnjbzs/m0p samples/hello_world
```

要在启动期间由M0+释放Cortex-M7内核，应在构建时传入相应Kconfig选项。仅当该内核的闪存地址处存在有效固件时才启用它，否则内核会取到无效指令并发生故障（Fault）。

```text
# From the root of the zephyr repository
west build -b kit_t2g_c2d6m_lite/cyt4dnjbzs/m0p samples/hello_world -- -DCONFIG_SOC_SERIES_CYT4DN_START_M7_0=y -DCONFIG_SOC_SERIES_CYT4DN_START_M7_1=y
```

为Cortex-M7内核0构建：

```text
# From the root of the zephyr repository
west build -b kit_t2g_c2d6m_lite/cyt4dnjbzs/m7_0 samples/hello_world
```

为Cortex-M7内核1构建：

```text
# From the root of the zephyr repository
west build -b kit_t2g_c2d6m_lite/cyt4dnjbzs/m7_1 samples/hello_world
```

注意（Note）

根据CYT4DN启动顺序，ROM／闪存启动代码只将Cortex-M0+内核从复位状态释放。Cortex-M0+应用负责启用Cortex-M7内核：为CM7_0及CM7_1设置CLK_HF1，编程向量表基址寄存器，即地址`0x40200200`处的`CM7_0_VECTOR_TABLE_BASE`及地址`0x40200600`处的`CM7_1_VECTOR_TABLE_BASE`，为两个M7内核供电，清除`CPU_WAIT`，并释放其复位状态。

<a id="flashing"></a>

### 烧录（Flashing）

<a id="id13"></a>

KIT_T2G_C-2D-6M_LITE集成[KitProg3](https://github.com/Infineon/KitProg3) [注6](#id12) 编程器／调试器，通过USB提供调试、闪存编程及串行通信。烧录和调试命令使用OpenOCD，需要安装支持KitProg3的英飞凌定制OpenOCD版本。

<a id="id7"></a>

<a id="id9"></a>

<a id="id11"></a>

完整[ModusToolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox) [注3](#id6) 与[ModusToolbox Programming Tools](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools) [注4](#id8) 软件包都包含[英飞凌OpenOCD](https://github.com/Infineon/openocd/releases/latest)，安装任意一个即可同时安装OpenOCD。如果均未安装，可下载适用于当前系统的英飞凌OpenOCD [注5](#id10) 发行版，将文件手动解压到选定位置，完成最小安装。

注意（Note）

Linux需要为KitProg3设置设备访问权限。ModusToolbox及ModusToolbox Programming Tools安装过程会自动处理；最小安装时，可执行`openocd/udev_rules/install_rules.sh`脚本手动设置。

west工具命令必须能够找到所安装的英飞凌OpenOCD可执行文件。以下示例通过永久CMake参数设置`OPENOCD`变量。

一次性设置OpenOCD路径：

```text
west config build.cmake-args -- -DOPENOCD=path/to/infineon/openocd/bin/openocd
```

为Cortex-M0+内核构建并烧录：

```text
# From the root of the zephyr repository
west build -b kit_t2g_c2d6m_lite/cyt4dnjbzs/m0p -p always samples/hello_world
west flash
west debug
```

为Cortex-M0+内核构建并烧录，并在启动期间释放M7内核：

```text
# From the root of the zephyr repository
west build -b kit_t2g_c2d6m_lite/cyt4dnjbzs/m0p -p always samples/hello_world -- -DCONFIG_SOC_SERIES_CYT4DN_START_M7_0=y -DCONFIG_SOC_SERIES_CYT4DN_START_M7_1=y
west flash
west debug
```

为Cortex-M7内核0构建并烧录：

```text
# From the root of the zephyr repository
west build -b kit_t2g_c2d6m_lite/cyt4dnjbzs/m7_0 -p always samples/hello_world
west flash
west debug
```

为Cortex-M7内核1构建并烧录：

```text
# From the root of the zephyr repository
west build -b kit_t2g_c2d6m_lite/cyt4dnjbzs/m7_1 -p always samples/hello_world
west flash
west debug
```

执行`west debug`后，GDB控制台启动，即可设置断点并执行其他标准GDB调试操作。

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.infineon.com/products/microcontroller/32-bit-traveo-t2g-arm-cortex/for-cluster/t2g-cyt4dn](https://www.infineon.com/products/microcontroller/32-bit-traveo-t2g-arm-cortex/for-cluster/t2g-cyt4dn)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.infineon.com/evaluation-board/KIT-T2G-C-2D-6M-LITE](https://www.infineon.com/evaluation-board/KIT-T2G-C-2D-6M-LITE)

<a id="id6"></a>

〔[3](#id7)〕 [https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox)

<a id="id8"></a>

〔[4](#id9)〕 [https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools)

<a id="id10"></a>

〔[5](#id11)〕 [https://github.com/Infineon/openocd/releases/latest](https://github.com/Infineon/openocd/releases/latest)

<a id="id12"></a>

〔[6](#id13)〕 [https://github.com/Infineon/KitProg3](https://github.com/Infineon/KitProg3)

## 译注

仅M0+由启动代码释放，M7需存在有效镜像并通过相应Kconfig选项启用；设置时钟、向量表和释放复位的责任依原文保留。

---

[上一章](P017_T2G_Body_High_Lite_Evaluation_Kit.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P019_XMC7200_Evaluation_Kit.md)
