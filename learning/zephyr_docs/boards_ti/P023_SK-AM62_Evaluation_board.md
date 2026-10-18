---
id: learning.zephyr-docs.boards-ti.page-23
title: SK-AM62 Evaluation board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ti/sk_am62/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="sk_am62"></a>

# 第23章\_SK-AM62评估板（Evaluation Board）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ti/sk_am62/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/sk_am62_angled.webp](images/sk_am62_angled.webp)](images/sk_am62_angled.webp)

SK-AM62评估板（Evaluation Board）

名称（Name）：

`sk_am62`

厂商（Vendor）：

[德州仪器（Texas Instruments）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=ti)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)、[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[am6254](https://docs.zephyrproject.org/latest/boards/index.html#soc=am6254)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/sk_am62/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

SK-AM62板级配置用于在TI AM62x平台运行Zephyr应用，支持两种板卡变体：


- SK-AM62，基础版本
- SK-AM62B-P1，集成电源管理芯片（PMIC）的版本

两种版本均使用AM6254 SoC，板级配置支持：


- Arm Cortex-M4F微控制器核及以下功能：

  > - 嵌套向量中断控制器（NVIC）
  > - 系统滴答系统时钟（SYSTICK / System Tick System Clock）
- Arm Cortex-A53核及以下功能：

  > - 通用中断控制器（GIC）
  > - Arm通用定时器（arch_timer）
  > - 片上SRAM（oc_sram）
  > - UART接口，uart0至uart6
  > - 邮箱接口（Mailbox，mbox0）

此板配置也启用半主机（Semihosting）调试控制台。

详情见[TI AM62X产品页](https://www.ti.com/product/AM625)。

<a id="hardware"></a>

## 硬件（Hardware）

SK-AM62 EVM搭载AM6254 SoC，包含四核Cortex-A53集群及MCU域内一个Cortex-M4核。Zephyr已移植到M4F及A53核，使用以下硬件规格：


- 高性能Arm Cortex-A53
- 低功耗Arm Cortex-M4F
- 存储器（Memory）

  > - 256 KB SRAM
  > - 2 GB DDR4
- 调试（Debug）

  > - 基于XDS110的JTAG

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`sk_am62`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="sk_am62-hw-features"></a>

<a id="sk_am62-sk_am62/am6254/a53-hw-features-section"></a>

#### `sk_am62/am6254/a53`目标（Target）

<a id="sk_am62-sk_am62/am6254/a53-hw-features-panel"></a>

<a id="sk_am62-sk_am62/am6254/a53-hw-features-memory"></a>

此板级目标的存储：2016 MiB RAM；Flash不适用（N/A）。

<a id="sk_am62-sk_am62/am6254/a53-hw-features-table"></a>

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
<td>ARM Cortex-A53处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L24">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P008_arm_cortex-a53.md#std-dtcompatible-arm-cortex-a53"><code>arm,cortex-a53</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>TI K3代处理器中基于计数器的实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L302">已启用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P010_ti_k3-rtc-counter.md#std-dtcompatible-ti-k3-rtc-counter"><code>ti,k3-rtc-counter</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>TI TCA6424A，基于I2C的GPIO扩展器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/sk_am62/sk_am62_am6254_a53.dts?plain=1#L120">已启用：1</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P019_ti_tca6424a.md#std-dtcompatible-ti-tca6424a"><code>ti,tca6424a</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Davinci及Keystone器件的GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L230">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L161">已禁用：4</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P014_ti_davinci-gpio.md#std-dtcompatible-ti-davinci-gpio"><code>ti,davinci-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L73">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L91">已禁用：2</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P013_ti_omap-i2c.md#std-dtcompatible-ti-omap-i2c"><code>ti,omap-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L55">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/sk_am62/sk_am62_am6254_a53.dts?plain=1#L71">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP邮箱（MAILBOX）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L79">已启用：1</a>）</td>
<td><a href="../intercore_reference/P055_TIOMAP邮箱绑定.md#dtbinding-ti-omap-mailbox"><code>ti,omap-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>兼容Atmel AT24系列的I2C电可擦除可编程只读存储器（EEPROM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/sk_am62/sk_am62_am6254_a53.dts?plain=1#L105">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P004_atmel_at24.md#std-dtcompatible-atmel-at24"><code>atmel,at24</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>TI K3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P013_ti_k3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl"><code>ti,k3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>片上（On-Chip）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）1.1版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-1.1.html#std-dtcompatible-arm-psci-1.1"><code>arm,psci-1.1</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>TI SD／eMMC主机控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L315">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L352">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P020_ti_am654-sdhci.md#std-dtcompatible-ti-am654-sdhci"><code>ti,am654-sdhci</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L10">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L19">已禁用：6</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>用于OMAP及K3 SoC的TI多通道SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L274">已禁用：3</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P018_ti_omap-mcspi.md#std-dtcompatible-ti-omap-mcspi"><code>ti,omap-mcspi</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>TI K3器件级控制寄存器模块（Device Level Control Register Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L64">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P009_ti_control-module.md#std-dtcompatible-ti-control-module"><code>ti,control-module</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>K3代处理器的看门狗定时器，实时间隔（RTI）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L239">已禁用：5</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P006_ti_j7-rti-wdt.md#std-dtcompatible-ti-j7-rti-wdt"><code>ti,j7-rti-wdt</code></a></td>
</tr>
</table>

<a id="sk_am62-sk_am62/am6254/m4-hw-features-section"></a>

#### `sk_am62/am6254/m4`目标（Target）

<a id="sk_am62-sk_am62/am6254/m4-hw-features-panel"></a>

<a id="sk_am62-sk_am62/am6254/m4-hw-features-memory"></a>

该开发板目标的片上存储容量：256 KiB RAM、N/A Flash。

<a id="sk_am62-sk_am62/am6254/m4-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L54">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>TI K3代处理器中基于计数器的实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L302">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P010_ti_k3-rtc-counter.md#std-dtcompatible-ti-k3-rtc-counter"><code>ti,k3-rtc-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Davinci及Keystone器件的GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L161">已禁用：6</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P014_ti_davinci-gpio.md#std-dtcompatible-ti-davinci-gpio"><code>ti,davinci-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L73">已禁用：5</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P013_ti_omap-i2c.md#std-dtcompatible-ti-omap-i2c"><code>ti,omap-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP邮箱（MAILBOX）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L60">已启用：1</a>）</td>
<td><a href="../intercore_reference/P055_TIOMAP邮箱绑定.md#dtbinding-ti-omap-mailbox"><code>ti,omap-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>TI K3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L77">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P013_ti_k3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl"><code>ti,k3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>TI SD／eMMC主机控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L315">已禁用：3</a>）</td>
<td><a href="../sdhc_binding_reference/P020_ti_am654-sdhci.md#std-dtcompatible-ti-am654-sdhci"><code>ti,am654-sdhci</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L84">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L10">已禁用：7</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>用于OMAP及K3 SoC的TI多通道SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L274">已禁用：3</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P018_ti_omap-mcspi.md#std-dtcompatible-ti-omap-mcspi"><code>ti,omap-mcspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L35">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>TI K3器件级控制寄存器模块（Device Level Control Register Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L69">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P009_ti_control-module.md#std-dtcompatible-ti-control-module"><code>ti,control-module</code></a></td>
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
<td>K3代处理器的看门狗定时器，实时间隔（RTI）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/k3-am62-main.dtsi?plain=1#L239">已禁用：6</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P006_ti_j7-rti-wdt.md#std-dtcompatible-ti-j7-rti-wdt"><code>ti,j7-rti-wdt</code></a></td>
</tr>
</table>

<a id="devices"></a>

### 设备（Devices）

<a id="system-clock"></a>

#### 系统时钟（System Clock）

此开发板配置使用400 MHz系统时钟。

<a id="ddr-ram"></a>

#### DDR随机存取存储器（DDR RAM）

此板有2 GB DDR RAM。原文称为Zephyr分配4 KB RAM，仅用于资源表，并给出范围0x9CC00000至0x9CC00400；该范围实际跨度为1 KiB，容量与地址均按原文保留。

<a id="serial-port"></a>

#### 串口（Serial Port）

此配置使用MCU域UART，即MCU_UART0，作为唯一串行通信通道。

<a id="sd-card"></a>

## SD卡（SD Card）

下载TI官方[WIC](https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-PvdSyIiioq/10.01.10.04/tisdk-default-image-am62xx-evm-10.01.10.04.rootfs.wic.xz)镜像，用镜像写入软件写入SD卡，在评估板A53应用核上启动Linux。为M4编程时，由A53核通过remoteproc将Zephyr二进制加载到M4核。

<a id="programming-for-m4f-core"></a>

## 为M4F核编程（Programming for M4F Core）

开发板可通过OpenAMP资源表（Resource Table）使用remoteproc。

测试前需将二进制文件复制到SD卡，使A53内核在启动时通过remoteproc加载它。

测试M4F内核时，使用以下命令构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例。

```text
# From the root of the Zephyr repository
west build -p -b sk_am62/am6254/m4 samples/hello_world
```

构建生成的二进制文件名为`zephyr.elf`，位于`build/zephyr`目录。

将该文件复制到SD卡上的`/lib/firmware`系统目录，并命名为`am62-mcu-m4f0_0-fw`。

```text
# Mount the SD card at sdcard for example
sudo mount /dev/sdX sdcard
# copy the elf to the /lib/firmware directory
sudo cp --remove-destination zephyr.elf sdcard/lib/firmware/am62-mcu-m4f0_0-fw
```

随后可用SD卡启动系统，启动时二进制程序会被加载到M4F内核。

要从SD卡启动，请将启动引脚设为SD卡启动模式，参见评估板设置页面。（[评估板（EVM）设置页面](https://software-dl.ti.com/mcu-plus-sdk/esd/AM62X/08_06_00_18/exports/docs/api_guide_am62x/EVM_SETUP_PAGE.html)）

更改启动模式后，开发板上电时应执行启动流程，二进制程序运行并向MCU_UART0端口打印Hello world。

<a id="programming-for-a53-core"></a>

## 为A53核编程（Programming for A53 Core）

将编译的zephyr.bin复制到SD卡第一个FAT分区，插入开发板，上电后在提示符处停止U-Boot执行。

用U-Boot加载并启动zephyr.bin：

```text
fatload mmc 1:1 0x82000000 zephyr.bin; go 0x82000000
```

Zephyr应用应在A53核上开始运行。执行hello_world示例时，应看到类似以下输出：

```text
*** Booting Zephyr OS build v4.3.0-4646-g13fc152f3546 ***
Secondary CPU core 1 (MPID:0x1) is up
Secondary CPU core 2 (MPID:0x2) is up
Secondary CPU core 3 (MPID:0x3) is up
Hello World! sk_am62/am6254/a53
```

这表明四个A53核均已成功启动。

<a id="debugging"></a>

## 调试（Debugging）

此板配备XDS110 JTAG调试器，使用debug构建目标调试二进制：


- M4F内核（Core）

```text
west build -b sk_am62/am6254/m4 <my_app>
west debug
```


- A53内核（Core）

```text
west build -b sk_am62/am6254/a53 <my_app>
west debug
```

提示（Hint）

此功能需要OpenOCD 0.12或更新版本。软件源可能提供旧版，原文建议[从源码构建OpenOCD](https://docs.u-boot.org/en/latest/board/ti/k3.html#building-openocd-from-source)。

<a id="references"></a>

## 参考资料（References）

AM62x SK EVM技术参考手册（TRM）：

[https://www.ti.com/lit/ug/spruiv7/spruiv7.pdf](https://www.ti.com/lit/ug/spruiv7/spruiv7.pdf)

## 译注

SK-AM62包含基础板与带PMIC的SK-AM62B-P1。M4路径由A53 Linux通过remoteproc加载，A53直接运行Zephyr的流程另节说明；四核启动输出完整保留。

---

[上一章](P022_MSP-EXP432P401R_LaunchXL.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P024_SK-AM64.md)
