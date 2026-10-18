---
id: learning.zephyr-docs.boards-cypress-to-dragino.page-2
title: PSOC 6 WiFi-BT Pioneer Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/cypress/cy8ckit_062_wifi_bt/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="cy8ckit_062_wifi_bt"></a>

# 第2章\_PSOC 6 WiFi-BT Pioneer开发套件（Kit）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/cypress/cy8ckit_062_wifi_bt/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/cy8ckit_062_wifi_bt_m0.jpg](images/cy8ckit_062_wifi_bt_m0.jpg)](images/cy8ckit_062_wifi_bt_m0.jpg)

PSOC 6 WiFi-BT Pioneer开发套件（Kit）

名称（Name）：

`cy8ckit_062_wifi_bt`

厂商（Vendor）：

[赛普拉斯半导体公司（Cypress Semiconductor Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=cypress)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[cy8c6247](https://docs.zephyrproject.org/latest/boards/index.html#soc=cy8c6247)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/cypress/cy8ckit_062_wifi_bt/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

PSOC 6 WiFi-BT Pioneer套件（CY8CKIT-062-WiFi-BT）是一款低成本硬件平台，用于设计及调试PSOC 62 MCU和村田（Murata）LBEE5KL1DX模块，即CYW4343W WiFi与蓝牙组合芯片。

PSOC 6 WiFi-BT Pioneer套件采用PSOC 62双核微控制器：150 MHz Arm Cortex-M4为主要应用处理器，100 MHz Arm Cortex-M0+支持低功耗操作；具有1 MB闪存、288 KB SRAM、104个GPIO、七个可编程模拟模块、56个可编程数字模块、全速USB、串行存储器接口、PDM-PCM数字麦克风接口，以及业界领先的CapSense电容感应功能。

PSOC 6 WiFi-BT Pioneer开发板兼容Arduino扩展板（Shields）。

Cortex-M0+是板载SoC的启动主核，它先启动，再启用CM4内核。


1. USB电力传输（PD）输出电压可用指示灯，LED7
2. 电池充电指示灯，LED6
3. KitProg2 USB Type-C连接器，J10
4. 带PD的Cypress EZ-PD™ CCG3 Type-C端口控制器，CYPD3125-40LQXI，U3
5. KitProg2编程模式选择按键，SW3
6. KitProg2 I/O排针，J6，标记1
7. KitProg2编程／自定义应用排针，J7，标记1
8. 外部电源连接器，J9
9. PSOC 6用户按键，SW2
10. KitProg2应用选择按键，SW4
11. 兼容Digilent® Pmod™的I/O排针，J14，标记1
12. 电源LED，LED4
13. KitProg2状态LED，LED1、LED2及LED3
14. PSOC 6复位按键，SW1
15. PSOC 6 I/O排针，J18、J19及J20
16. 兼容Arduino™ Uno R3的电源排针，J1
17. PSOC 6调试与跟踪（Debug and Trace）排针，J12
18. 兼容Arduino Uno R3的PSOC 6 I/O排针，J2、J3及J4
19. PSOC 6编程与调试排针，J11
20. CapSense接近感应排针，J13
21. CapSense电容感应滑条及按键
22. PSOC 6 VDD电源选择开关，SW5
23. Cypress 512 Mbit串行NOR闪存，S25-FL512S，U4
24. PSOC 6用户LED，LED8及LED9
25. RGB LED，LED5
26. WiFi／蓝牙模块，LBEE5KL 1DX，U6
27. Cypress串行铁电存储器（Ferroelectric RAM），U5，标记1
28. WiFi与蓝牙（BT）天线
29. VBACKUP与电源管理芯片（PMIC）控制选择开关，SW7，标记2
30. PSOC 6 USB设备Type-C连接器，J28
31. Cypress PSOC 6，CY8C6247BZI-D54，U1
32. PSOC 6 USB主机（Host）Type-A连接器，J27
33. 兼容Arduino Uno R3的在线串行编程（ICSP）排针，J5，标记1
34. PSOC 6功耗监测跳线，J8，标记2
35. KitProg2（PSOC 5LP）编程器与调试器，CY8C5868LTI-LP039，U2
36. 电池连接器，J15，标记1、2
37. USB PD输出电压9 V／12 V连接器，J16

<a id="hardware"></a>

## 硬件（Hardware）

PSOC 62 MCU SoC及CY8CKIT-062-WiFi-BT开发板的更多信息：


- <a id="id3"></a>

  PSOC 62 MCU SoC网站[注1](#id2)（[PSOC 62 MCUSoC网站](https://www.infineon.com/products/microcontroller/32-bit-psoc-arm-cortex/psoc-6-m4-mcu/psoc-62)）
- <a id="id5"></a>

  [PSOC 62 MCU数据手册（Datasheet）](https://www.infineon.com/assets/row/public/documents/30/49/infineon-cy8c62x6-cy8c62x7-psoc-62-mcu-arm-cortex--m4-datasheet-en.pdf)[注2](#id4)
- <a id="id7"></a>

  [PSOC 62 MCU架构参考手册（Architecture Reference Manual）](https://www.cypress.com/documentation/technical-reference-manuals/psoc-6-mcu-psoc-62-architecture-technical-reference-manual)[注3](#id6)
- <a id="id9"></a>

  [PSOC 62 MCU寄存器参考手册（Register Reference Manual）](https://www.cypress.com/documentation/technical-reference-manuals/psoc-6-mcu-psoc-62-register-technical-reference-manual-trm)[注4](#id8)
- <a id="id11"></a>

  [CY8CKIT-062-WiFi-BT网站](https://www.infineon.com/evaluation-board/CY8CKIT-062-WIFI-BT)[注5](#id10)
- <a id="id13"></a>

  [CY8CKIT-062-WiFi-BT用户指南（User Guide）](https://www.cypress.com/file/407731/download)[注6](#id12)
- <a id="id15"></a>

  [CY8CKIT-062-WiFi-BT原理图（Schematics）](https://www.cypress.com/file/420846/download)[注7](#id14)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`cy8ckit_062_wifi_bt`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="cy8ckit_062_wifi_bt-hw-features"></a>

<a id="cy8ckit_062_wifi_bt-cy8ckit_062_wifi_bt/cy8c6247/m0-hw-features-section"></a>

#### `cy8ckit_062_wifi_bt/cy8c6247/m0`目标（Target）

<a id="cy8ckit_062_wifi_bt-cy8ckit_062_wifi_bt/cy8c6247/m0-hw-features-panel"></a>

<a id="cy8ckit_062_wifi_bt-cy8ckit_062_wifi_bt/cy8c6247/m0-hw-features-memory"></a>

该开发板目标的片上存储容量：140 KiB RAM、384 KiB Flash。

<a id="cy8ckit_062_wifi_bt-cy8ckit_062_wifi_bt/cy8c6247/m0-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Cypress闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L31">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P011_cypress_psoc6-flash-controller.md#std-dtcompatible-cypress-psoc6-flash-controller"><code>cypress,psoc6-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Cypress高速I/O矩阵（High Speed I/O Matrix）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L76">已禁用：1</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P014_cypress_psoc6-hsiom.md#std-dtcompatible-cypress-psoc6-hsiom"><code>cypress,psoc6-hsiom</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Cypress GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L83">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L94">已禁用：13</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P013_cypress_psoc6-gpio.md#std-dtcompatible-cypress-psoc6-gpio"><code>cypress,psoc6-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>Cypress PSOC 6唯一88位序列号（Unique Serial Number）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L410">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P003_cypress_psoc6-uid.md#std-dtcompatible-cypress-psoc6-uid"><code>cypress,psoc6-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/cypress/cy8ckit_062_wifi_bt/cy8ckit_062_wifi_bt_cy8c6247_m0.dts?plain=1#L40">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Cypress中断复用器（Interrupt Multiplex）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6_cm0.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P009_cypress_psoc6-intmux.md#std-dtcompatible-cypress-psoc6-intmux"><code>cypress,psoc6-intmux</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Cypress中断复用通道（Interrupt Multiplex Channel）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6_cm0.dtsi?plain=1#L29">已启用：32</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P010_cypress_psoc6-intmux-ch.md#std-dtcompatible-cypress-psoc6-intmux-ch"><code>cypress,psoc6-intmux-ch</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/cypress/cy8ckit_062_wifi_bt/cy8ckit_062_wifi_bt_cy8c6247_m0.dts?plain=1#L31">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L38">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>英飞凌（Infineon）CAT1引脚控制容器（Pinctrl Container）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6-pinctrl.dtsi?plain=1#L12">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P001_infineon_pinctrl.md#std-dtcompatible-infineon-pinctrl"><code>infineon,pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Cypress串行通信模块（SCB）的UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L386">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L338">已禁用：8</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P016_cypress_psoc6-uart.md#std-dtcompatible-cypress-psoc6-uart"><code>cypress,psoc6-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Cypress串行通信模块（SCB）的SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L248">已禁用：9</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P012_cypress_psoc6-spi.md#std-dtcompatible-cypress-psoc6-spi"><code>cypress,psoc6-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L51">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
</table>

<a id="cy8ckit_062_wifi_bt-cy8ckit_062_wifi_bt/cy8c6247/m4-hw-features-section"></a>

#### `cy8ckit_062_wifi_bt/cy8c6247/m4`目标（Target）

<a id="cy8ckit_062_wifi_bt-cy8ckit_062_wifi_bt/cy8c6247/m4-hw-features-panel"></a>

<a id="cy8ckit_062_wifi_bt-cy8ckit_062_wifi_bt/cy8c6247/m4-hw-features-memory"></a>

该开发板目标的片上存储容量：112 KiB RAM、640 KiB Flash。

<a id="cy8ckit_062_wifi_bt-cy8ckit_062_wifi_bt/cy8c6247/m4-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L24">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Cypress闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L31">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P011_cypress_psoc6-flash-controller.md#std-dtcompatible-cypress-psoc6-flash-controller"><code>cypress,psoc6-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Cypress高速I/O矩阵（High Speed I/O Matrix）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L76">已禁用：1</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P014_cypress_psoc6-hsiom.md#std-dtcompatible-cypress-psoc6-hsiom"><code>cypress,psoc6-hsiom</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Cypress GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L83">已禁用：15</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P013_cypress_psoc6-gpio.md#std-dtcompatible-cypress-psoc6-gpio"><code>cypress,psoc6-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>Cypress PSOC 6唯一88位序列号（Unique Serial Number）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L410">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P003_cypress_psoc6-uid.md#std-dtcompatible-cypress-psoc6-uid"><code>cypress,psoc6-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L38">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>英飞凌（Infineon）CAT1引脚控制容器（Pinctrl Container）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6-pinctrl.dtsi?plain=1#L12">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P001_infineon_pinctrl.md#std-dtcompatible-infineon-pinctrl"><code>infineon,pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Cypress串行通信模块（SCB）的UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L378">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L338">已禁用：8</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P016_cypress_psoc6-uart.md#std-dtcompatible-cypress-psoc6-uart"><code>cypress,psoc6-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Cypress串行通信模块（SCB）的SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L248">已禁用：9</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P012_cypress_psoc6-spi.md#std-dtcompatible-cypress-psoc6-spi"><code>cypress,psoc6-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi?plain=1#L51">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

PSOC 62 MCU SoC配置为使用内部主振荡器与锁频环（IMO+FLL）作为系统时钟源；CM0+运行于50 MHz，CM4运行于100 MHz。SoC还提供其他系统时钟源，可根据系统需求选择。

<a id="serial-port"></a>

### 串口（Serial Port）

PSOC 62 MCU SoC具有九个SCB模块，其中八个可配置为UART串行通信接口。目前配置了SCB5上的UART5及SCB6上的UART6。SCB5连接板载KitProg2的USB-UART桥；SCB6连接兼容Arduino Uno R3的PSOC 6 I/O排针J3上的P12_0、P12_1。

<a id="openocd-installation"></a>

### 安装OpenOCD（OpenOCD Installation）

获取OpenOCD软件包需完成以下操作：


1. 下载ModusToolbox 3.1软件：[https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox)。
2. 下载后，将ModusToolbox提供的Scripts目录加入路径：`export PATH=$PATH:/path/to/ModusToolbox/tools_3.1/openocd/scripts`。
3. 在`west flash/debug`中指定OpenOCD可执行文件路径。
4. 烧录命令：`west flash –openocd path/to/infineon/openocd/bin/openocd`。
5. 调试命令：`west debug –openocd path/to/infineon/openocd/bin/openocd`。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`cy8ckit_062_wifi_bt`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

CY8CKIT-062-WiFi-BT包含板载编程器／调试器KitProg2，支持大容量存储编程（Mass Storage Programming），通过USB提供调试、闪存编程及串行通信。PSOC 6编程与调试排针J11、J12也可连接Segger J-Link。看门狗定时器默认启用；调用`Cy_WDT_Unlock()`及`Cy_WDT_Disable()`可将其禁用。

MCU复位后默认只启动CM0+内核。要使CM4工作，须将两个内核的固件都写入闪存。CM0+固件应在适当时刻调用`Cy_SysEnableCM4(CM4_START_ADDRESS);`启动CM4；当前配置中`CM4_START_ADDRESS`为`0x10060000`。CM0+／CM4的Flash和SRAM区域定义在[dts/arm/infineon/cat1a/legacy/psoc6.dtsi](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/legacy/psoc6.dtsi)中。

为CM0+构建工程

```text
west build -b cy8ckit_062_wifi_bt/cy8c6247/m0
```

通过SW3将开发套件切换到CMSIS-DAP模式，此时LED2应闪烁，然后烧录开发板：

```text
$<openocd_path>\bin\openocd -c "source [find interface/cmsis-dap.cfg]" \
   -c "transport select swd" -c "source [find target/psoc6.cfg]" \
   -c "if [catch {program {<zephyr_path>\samples\hello_world\build\zephyr\zephyr.elf}} ] \
      { echo {** Program operation failed **} } \
      else { echo {** Program operation completed successfully **} }" \
   -c "reset_config srst_only;reset run;psoc6.dap dpreg 0x04 0x00;shutdown"
```

通过SW3将开发套件切回原模式。打开串口终端，例如minicom或PuTTY，以以下设置连接开发板：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

复位开发板，相应串口将出现以下消息：

```text
***** Booting Zephyr OS zephyr-v1.13.0-1877-g9d14874db1 *****
Hello World! cy8ckit_062_wifi_bt
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.infineon.com/products/microcontroller/32-bit-psoc-arm-cortex/psoc-6-m4-mcu/psoc-62](https://www.infineon.com/products/microcontroller/32-bit-psoc-arm-cortex/psoc-6-m4-mcu/psoc-62)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.infineon.com/assets/row/public/documents/30/49/infineon-cy8c62x6-cy8c62x7-psoc-62-mcu-arm-cortex–m4-datasheet-en.pdf](https://www.infineon.com/assets/row/public/documents/30/49/infineon-cy8c62x6-cy8c62x7-psoc-62-mcu-arm-cortex--m4-datasheet-en.pdf)

<a id="id6"></a>

〔[3](#id7)〕 [https://www.cypress.com/documentation/technical-reference-manuals/psoc-6-mcu-psoc-62-architecture-technical-reference-manual](https://www.cypress.com/documentation/technical-reference-manuals/psoc-6-mcu-psoc-62-architecture-technical-reference-manual)

<a id="id8"></a>

〔[4](#id9)〕 [https://www.cypress.com/documentation/technical-reference-manuals/psoc-6-mcu-psoc-62-register-technical-reference-manual-trm](https://www.cypress.com/documentation/technical-reference-manuals/psoc-6-mcu-psoc-62-register-technical-reference-manual-trm)

<a id="id10"></a>

〔[5](#id11)〕 [https://www.infineon.com/evaluation-board/CY8CKIT-062-WIFI-BT](https://www.infineon.com/evaluation-board/CY8CKIT-062-WIFI-BT)

<a id="id12"></a>

〔[6](#id13)〕 [https://www.cypress.com/file/407731/download](https://www.cypress.com/file/407731/download)

<a id="id14"></a>

〔[7](#id15)〕 [https://www.cypress.com/file/420846/download](https://www.cypress.com/file/420846/download)

## 译注

两个内核的固件都须写入闪存，并由CM0+显式启动CM4；当前CM4起始地址0x10060000及Flash／SRAM划分路径按原文保留。封装引脚数、最高主频及当前默认时钟属于不同信息。

---

[上一章](P001_PSOC_63_BLE_Pioneer_Kit.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_Cypress.md)
