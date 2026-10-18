---
id: learning.zephyr-docs.boards-infineon-innblue.page-13
title: PSOC Control C3M6 Evaluation Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/infineon/kit_psc3m6_evk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="kit_psc3m6_evk"></a>

# 第13章\_PSOC Control C3M6评估套件（Evaluation Kit）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/infineon/kit_psc3m6_evk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/kit_psc3m6_evk.webp](images/kit_psc3m6_evk.webp)](images/kit_psc3m6_evk.webp)

PSOC Control C3M6评估套件（Evaluation Kit）

名称（Name）：

`kit_psc3m6_evk`

厂商（Vendor）：

[英飞凌科技（Infineon Technologies）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=infineon)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[psc3m6ges3ahq1](https://docs.zephyrproject.org/latest/boards/index.html#soc=psc3m6ges3ahq1)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/infineon/kit_psc3m6_evk/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

PSOC Control C3M6评估套件[KIT_PSC3M6_EVK](https://www.infineon.com/evaluation-board/KIT-PSC3M6-EVAL)面向PSC3M6微控制器。PSC3M6是英飞凌CAT1B系列中基于Arm Cortex-M33的SoC，板载PSC3M6GES3AHQ1变体提供512 KB Flash、128 KB SRAM及TrustZone-M安全机制。

<a id="hardware"></a>

## 硬件（Hardware）


- 片上系统（SoC）：PSC3M6GES3AHQ1 (PG-E-LQFP-100)
- CPU：Arm Cortex-M33，最高180 MHz
- 闪存（Flash）：512 KB内部闪存
- 静态随机存储器（SRAM）：128 KB
- 连接：CAN FD、SCB（UART／SPI／I2C）
- 安全：TrustZone-M
- 调试：SEGGER J-Link，需要v9.68或更新版本
- 用户I/O：2个用户LED、2个用户按键

<a id="kit-contents"></a>

### 套件内容（Kit Contents）

KIT_PSC3M6_EVAL用户指南列出的套件内容如下：（[KIT_PSC3M6_EVAL用户指南（User Guide）](https://www.infineon.com/document-promo/infineon-kit-psc3m6-eval-user-guide-usermanual-en_3885ebcf-6410-484d-9f5c-0e3c645aec40)）


- PSOC Control C3M6 Evaluation Kit开发板
- USB Type-A转Type-C线缆
- 跳线，10根
- 快速入门指南，通过二维码访问网页信息

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`kit_psc3m6_evk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="kit_psc3m6_evk-hw-features"></a>

<a id="kit_psc3m6_evk-kit_psc3m6_evk/psc3m6ges3ahq1-hw-features-section"></a>

#### `kit_psc3m6_evk/psc3m6ges3ahq1`目标（Target）

<a id="kit_psc3m6_evk-kit_psc3m6_evk/psc3m6ges3ahq1-hw-features-panel"></a>

<a id="kit_psc3m6_evk-kit_psc3m6_evk/psc3m6ges3ahq1-hw-features-memory"></a>

该开发板目标的片上存储容量：128 KiB RAM、256 KiB Flash。

<a id="kit_psc3m6_evk-kit_psc3m6_evk/psc3m6ges3ahq1-hw-features-table"></a>

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
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/psc3m6.cm33.dtsi?plain=1#L16">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>英飞凌串行通信模块（SCB / Serial Communication Blocks）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/psc3m6_s.dtsi?plain=1#L163">已禁用：4</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P011_infineon_scb.md#std-dtcompatible-infineon-scb"><code>infineon,scb</code></a></td>
</tr>
<tr>
<td rowspan="2">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAN FD控制器封装层（Wrapper）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/psc3m6_s.dtsi?plain=1#L226">已启用：1</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P008_infineon_canfd-controller.md#std-dtcompatible-infineon-canfd-controller"><code>infineon,canfd-controller</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌MCAN驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/psc3m6_s.dtsi?plain=1#L247">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/psc3m6_s.dtsi?plain=1#L235">已禁用：1</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P007_infineon_can.md#std-dtcompatible-infineon-can"><code>infineon,can</code></a></td>
</tr>
<tr>
<td rowspan="3">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/system_clocks.dtsi?plain=1#L27">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/system_clocks.dtsi?plain=1#L54">已禁用：2</a>）</td>
<td><a href="../timer_reference/P112_Infineon固定时钟绑定.md#dtbinding-infineon-fixed-clock"><code>infineon,fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/system_clocks.dtsi?plain=1#L72">已禁用：14</a>）</td>
<td><a href="../timer_reference/P113_Infineon固定比例时钟绑定.md#dtbinding-infineon-fixed-factor-clock"><code>infineon,fixed-factor-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>英飞凌外设分频器（Peripheral Divider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/system_clocks.dtsi?plain=1#L307">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/system_clocks.dtsi?plain=1#L222">已禁用：15</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P009_infineon_peri-div.md#std-dtcompatible-infineon-peri-div"><code>infineon,peri-div</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/mpns/psc3m6ges3ahq1_s.dtsi?plain=1#L11">已禁用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P014_infineon_flash-controller.md#std-dtcompatible-infineon-flash-controller"><code>infineon,flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>英飞凌GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/psc3m6_s.dtsi?plain=1#L43">已启用：9</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/psc3m6_s.dtsi?plain=1#L23">已禁用：5</a>）</td>
<td><a href="../gpio_infineon_intel_ite_microchip_binding_reference/P001_infineon_gpio.md#std-dtcompatible-infineon-gpio"><code>infineon,gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/kit_psc3m6_evk/kit_psc3m6_evk-common.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/kit_psc3m6_evk/kit_psc3m6_evk-common.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/mpns/psc3m6ges3ahq1_s.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">物理层（PHY）</td>
<td>板载（On-Board）</td>
<td>由简单GPIO控制的CAN收发器（Transceiver）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/kit_psc3m6_evk/kit_psc3m6_evk-common.dtsi?plain=1#L60">已启用：1</a>）</td>
<td><a href="../phy_binding_reference/P001_can-transceiver-gpio.md#std-dtcompatible-can-transceiver-gpio"><code>can-transceiver-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>英飞凌（Infineon）CAT1引脚控制容器（Pinctrl Container）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/psc3m6_s.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P001_infineon_pinctrl.md#std-dtcompatible-infineon-pinctrl"><code>infineon,pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1B电源控制（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/system_clocks.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P003_infineon_cat1b-power.md#std-dtcompatible-infineon-cat1b-power"><code>infineon,cat1b-power</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1系列实时时钟（RTC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/psc3m6_s.dtsi?plain=1#L211">已禁用：1</a>）</td>
<td><a href="../rtc_binding_reference/P007_infineon_rtc.md#std-dtcompatible-infineon-rtc"><code>infineon,rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1 UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/psc3m6_s.dtsi?plain=1#L187">已启用：2</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P008_infineon_uart.md#std-dtcompatible-infineon-uart"><code>infineon,uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/psc3m6_s.dtsi?plain=1#L12">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>英飞凌CAT1看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1b/psc3/psc3m6/psc3m6_s.dtsi?plain=1#L219">已启用：1</a>）</td>
<td><a href="../soc_pmic_watchdog_binding_reference/P001_infineon_watchdog.md#std-dtcompatible-infineon-watchdog"><code>infineon,watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="leds"></a>

#### 发光二极管（LEDs）

<table>
<tr>
<th>名称（Name）</th>
<th>GPIO引脚（Pin）</th>
</tr>
<tr>
<td>LED0</td>
<td>P8.4（低电平有效 / active low）</td>
</tr>
<tr>
<td>LED1</td>
<td>P8.5（低电平有效 / active low）</td>
</tr>
</table>

<a id="push-buttons"></a>

#### 按键（Push Buttons）

<table>
<tr>
<th>名称（Name）</th>
<th>GPIO引脚（Pin）</th>
</tr>
<tr>
<td>SW4</td>
<td>P10.2（低电平有效 / active low）</td>
</tr>
<tr>
<td>SW3</td>
<td>P2.0（低电平有效 / active low）</td>
</tr>
</table>

<a id="default-zephyr-peripheral-mapping"></a>

#### Zephyr默认外设映射（Default Peripheral Mapping）

<table>
<tr>
<th>引脚（Pin）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>P6.3</td>
<td>SCB3 UART 发送（TX）</td>
<td>控制台发送（Console TX）</td>
</tr>
<tr>
<td>P6.2</td>
<td>SCB3 UART 接收（RX）</td>
<td>控制台接收（Console RX）</td>
</tr>
<tr>
<td>P3.3</td>
<td>SCB4 UART 发送（TX）</td>
<td>用户UART发送（TX）</td>
</tr>
<tr>
<td>P3.2</td>
<td>SCB4 UART 接收（RX）</td>
<td>用户UART接收（RX）</td>
</tr>
<tr>
<td>P5.3</td>
<td>CANFD0通道1发送（CH1 TX）</td>
<td>CAN FD发送（TX）</td>
</tr>
<tr>
<td>P5.2</td>
<td>CANFD0通道1接收（CH1 RX）</td>
<td>CAN FD接收（RX）</td>
</tr>
<tr>
<td>P9.0</td>
<td>SCB0 I2C串行时钟（SCL）</td>
<td>I2C时钟（Clock）</td>
</tr>
<tr>
<td>P9.2</td>
<td>SCB0 I2C串行数据（SDA）</td>
<td>I2C数据（Data）</td>
</tr>
<tr>
<td>P7.0</td>
<td>SCB2 SPI时钟（CLK）</td>
<td>SPI时钟（Clock）</td>
</tr>
<tr>
<td>P7.1</td>
<td>SCB2 SPI主机输出从机输入（MOSI）</td>
<td>SPI主机输出从机输入（MOSI）</td>
</tr>
<tr>
<td>P7.2</td>
<td>SCB2 SPI主机输入从机输出（MISO）</td>
<td>SPI主机输入从机输出（MISO）</td>
</tr>
<tr>
<td>P8.4</td>
<td>通用输入输出（GPIO）</td>
<td>LED0</td>
</tr>
<tr>
<td>P8.5</td>
<td>通用输入输出（GPIO）</td>
<td>LED1</td>
</tr>
<tr>
<td>P10.2</td>
<td>通用输入输出（GPIO）</td>
<td>按键SW4</td>
</tr>
<tr>
<td>P2.0</td>
<td>通用输入输出（GPIO）</td>
<td>按键SW3</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

PSOC Control C3M6及其评估板提供以下时钟源：


- 内部主振荡器（IMO）：8 MHz
- 内部高速振荡器（IHO / Internal High-Speed Oscillator）：48 MHz
- 外部晶体振荡器（ECO / External Crystal Oscillator）：16 MHz，连接P1.0及P1.1
- 钟表晶体振荡器（WCO / Watch Crystal Oscillator）：32.768 kHz，连接P0.0及P0.1

<a id="serial-port"></a>

### 串口（Serial Port）

Zephyr控制台分配到SCB3（uart3）的调试UART。

默认通信设置为115200、8N1。

<a id="building"></a>

## 构建（Building）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b kit_psc3m6_evk samples/hello_world
```

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`kit_psc3m6_evk`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

使用`west flash`及`west debug`，通过OpenOCD配合SEGGER J-Link探针操作，J-Link需要v9.68或更新版本。

<a id="infineon-openocd-installation"></a>

### 英飞凌OpenOCD安装（Installation）

ModusToolbox编程工具包（Programming Tools）包含[英飞凌OpenOCD](https://github.com/Infineon/openocd/releases/latest)。也可下载适用于当前系统的英飞凌OpenOCD发行版，解压到选定位置，独立安装。（[ModusToolbox编程工具（Programming Tools）](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools)）

<a id="flashing"></a>

### 烧录（Flashing）

构建并烧录应用：

```text
# From the root of the zephyr repository
west build -b kit_psc3m6_evk -p always samples/hello_world
west flash --openocd <path/to/openocd>
```

<a id="references"></a>

## 参考资料（References）

## 译注

SEGGER版本、OpenOCD与J-Link选择及180 MHz运行条件均按原文保留。

---

[上一章](P012_PSOC_Control_C3M5_Evaluation_Kit.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_PSOC_Edge_E84_AI_Evaluation_Kit.md)
