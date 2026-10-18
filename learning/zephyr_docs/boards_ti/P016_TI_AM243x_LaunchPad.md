---
id: learning.zephyr-docs.boards-ti.page-16
title: TI AM243x LaunchPad
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ti/lp_am243/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="lp_am243"></a>

# 第16章\_TI AM243x LaunchPad

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ti/lp_am243/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`lp_am243`

厂商（Vendor）：

[德州仪器（Texas Instruments）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=ti)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[am2434](https://docs.zephyrproject.org/latest/boards/index.html#soc=am2434)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/lp_am243/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

AM243x LaunchPad基于AM2434 SoC，具有两个运行于800 MHz的双核Cortex-R5F集群及一个运行于400 MHz的Cortex-M4F核。开发板还配有闪存芯片、用于选择启动模式的拨码开关及两个RJ45以太网端口。

<a id="id12"></a>

<a id="id14"></a>

更多信息见[AM243x LaunchPad产品页](https://www.ti.com/tool/LP-AM243)[注5](#id11)及[AM2434 SoC网站](https://www.ti.com/product/en-us/AM2434#tech-docs)[注6](#id13)。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="am64x-am243x-features"></a>

### AM64x／AM243x功能（Features）

AM64x／AM243x系列SoC最多支持两个通常运行于1 GHz的Cortex-A53核，仅AM64x提供；最多四个通常运行于800 MHz的Cortex-R5F核；以及一个通常运行于400 MHz的Cortex-M4F核。由于两系列的区别在于是否存在Cortex-A核，Zephyr代码将它们统称为AM64x。AM243x用户不适用涉及Cortex-A核的内容，但共享文档中有时仍会包含这些说明。

Arm核及外设划分到主域（MAIN Domain）及微控制器域（MCU Domain），其中只有Cortex-M4F核位于MCU域。默认情况下两个域可以交互，也可配置为相互隔离。

下面列出部分功能。目前Zephyr尚未支持所有外设：


- 最多两个Arm Cortex-A53核
- 最多两个双核Cortex-R5F集群（Cluster）
- 一个Cortex-M4F核
- 2 MiB内部SRAM
- 通用输入输出（GPIO）
- 模数转换器（ADC）
- 通用异步收发器（UART）
- 串行外设接口（SPI）
- 集成电路间总线（I2C）
- 多个定时器（Timer）
- 多个看门狗（Watchdog）
- CAN-FD
- 以太网（Ethernet）
- 通用串行总线（USB）
- 高速外围组件互连（PCIe）
- 外部(LP)DDR4 RAM接口
- DMSC，集中式电源及资源管理
- 密码运算加速（Crypto Acceleration）
- 安全启动（Secure Boot）

<a id="the-am243x-launchpad"></a>

### AM243x LaunchPad开发板

AM243x LaunchPad采用AM2434 SoC。原文在此将MAIN域中两个800 MHz双核集群写作Cortex-R4F，与本页前文Cortex-R5F不一致；MCU域包含一个400 MHz Cortex-M4F核。

开发板实际配有：


- 512 Mb，即64 MB的Infineon NOR闪存
- 用于切换启动模式的拨码开关
- 用于不同复位方式的按键
- 多个LED，部分用于电源指示，部分连接GPIO
- 两个物理以太网端口，含物理层收发器（PHY）
- XDS110调试探针，提供JTAG仿真

Cortex-R5F0_0默认使用连接XDS110调试探针的UART，无需另加UART转USB转换器。为避免冲突，Cortex-M4F默认使用MCU_UART0，可通过板上J17排针访问。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`lp_am243`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="lp_am243-hw-features"></a>

<a id="lp_am243-lp_am243/am2434/m4-hw-features-section"></a>

#### `lp_am243/am2434/m4`目标（Target）

<a id="lp_am243-lp_am243/am2434/m4-hw-features-panel"></a>

<a id="lp_am243-lp_am243/am2434/m4-hw-features-memory"></a>

该开发板目标的片上存储容量：192 KiB RAM、N/A Flash。

<a id="lp_am243-lp_am243/am2434/m4-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_m4.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>TI AM335X模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L421">已禁用：1</a>）</td>
<td><a href="../hardware/P904_TIAM335x模数转换器绑定.md#dtbinding-ti-am335x-adc"><code>ti,am335x-adc</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>TI系统控制接口（TI-SCI）时钟控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P024_ti_k2g-sci-clk.md#std-dtcompatible-ti-k2g-sci-clk"><code>ti,k2g-sci-clk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_m4.dtsi?plain=1#L37">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">固件（Firmware）</td>
<td>片上（On-Chip）</td>
<td>TISCI客户端驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L15">已禁用：1</a>）</td>
<td><a href="../hardware/P612_TI%20K2G系统控制接口绑定.md#dtbinding-ti-k2g-sci"><code>ti,k2g-sci</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Davinci及Keystone器件的GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L225">已启用：2</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P013_ti_davinci-gpio-nexus.md#std-dtcompatible-ti-davinci-gpio-nexus"><code>ti,davinci-gpio-nexus</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Davinci及Keystone器件的GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_mcu.dtsi?plain=1#L65">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L323">已禁用：6</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P014_ti_davinci-gpio.md#std-dtcompatible-ti-davinci-gpio"><code>ti,davinci-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L189">已禁用：6</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P013_ti_omap-i2c.md#std-dtcompatible-ti-omap-i2c"><code>ti,omap-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="2">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>TI安全代理邮箱（Secure Proxy Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L28">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P056_TI安全代理邮箱绑定.md#dtbinding-ti-secure-proxy"><code>ti,secure-proxy</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>TI OMAP邮箱（MAILBOX）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L479">已禁用：8</a>）</td>
<td><a href="../intercore_reference/P055_TIOMAP邮箱绑定.md#dtbinding-ti-omap-mailbox"><code>ti,omap-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">多位串行外设接口（Multi-Bit SPI）</td>
<td>片上（On-Chip）</td>
<td>带多线SPI接口（MSPI）的Cadence xSPI闪存控制器，支持双线、四线及八线SPI（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L702">已禁用：1</a>）</td>
<td><a href="../mspi_binding_reference/P003_cdns_xspi-nor.md#std-dtcompatible-cdns-xspi-nor"><code>cdns,xspi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>TI K3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_mcu.dtsi?plain=1#L22">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L44">已禁用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P013_ti_k3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl"><code>ti,k3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>由TISCI管理的电源域（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main_power_domains.dtsi?plain=1#L8">已启用：148</a>）</td>
<td><a href="../power_domain_binding_reference/P011_ti_sci-pm-domain.md#std-dtcompatible-ti-sci-pm-domain"><code>ti,sci-pm-domain</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>TI SoC基于增强型高分辨率PWM（EHRPWM）的PWM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L585">已禁用：9</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P014_ti_am3352-ehrpwm.md#std-dtcompatible-ti-am3352-ehrpwm"><code>ti,am3352-ehrpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>TI SoC基于增强型捕获模块（ECAP）的PWM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L675">已禁用：3</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P013_ti_am3352-ecap.md#std-dtcompatible-ti-am3352-ecap"><code>ti,am3352-ecap</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>TI SD／eMMC主机控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L542">已禁用：2</a>）</td>
<td><a href="../sdhc_binding_reference/P020_ti_am654-sdhci.md#std-dtcompatible-ti-am654-sdhci"><code>ti,am654-sdhci</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_mcu.dtsi?plain=1#L29">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L133">已禁用：8</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>用于OMAP及K3 SoC的TI多通道SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L371">已禁用：7</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P018_ti_omap-mcspi.md#std-dtcompatible-ti-omap-mcspi"><code>ti,omap-mcspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_m4.dtsi?plain=1#L27">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>TI K3器件级控制寄存器模块（Device Level Control Register Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L36">已启用：3</a>）</td>
<td><a href="../edac_syscon_binding_reference/P009_ti_control-module.md#std-dtcompatible-ti-control-module"><code>ti,control-module</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>TI双模式定时器（Dual-Mode Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L61">已禁用：12</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P012_ti_am654-timer.md#std-dtcompatible-ti-am654-timer"><code>ti,am654-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>K3代处理器的看门狗定时器，实时间隔（RTI）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L430">已禁用：7</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P006_ti_j7-rti-wdt.md#std-dtcompatible-ti-j7-rti-wdt"><code>ti,j7-rti-wdt</code></a></td>
</tr>
</table>

<a id="lp_am243-lp_am243/am2434/r5f0_0-hw-features-section"></a>

#### `lp_am243/am2434/r5f0_0`目标（Target）

<a id="lp_am243-lp_am243/am2434/r5f0_0-hw-features-panel"></a>

<a id="lp_am243-lp_am243/am2434/r5f0_0-hw-features-memory"></a>

该开发板目标的片上存储容量：256 KiB RAM、N/A Flash。

<a id="lp_am243-lp_am243/am2434/r5f0_0-hw-features-table"></a>

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
<td>ARM Cortex-R5F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_r5.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P012_arm_cortex-r5f.md#std-dtcompatible-arm-cortex-r5f"><code>arm,cortex-r5f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>TI AM335X模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L421">已禁用：1</a>）</td>
<td><a href="../hardware/P904_TIAM335x模数转换器绑定.md#dtbinding-ti-am335x-adc"><code>ti,am335x-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>TI系统控制接口（TI-SCI）时钟控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P024_ti_k2g-sci-clk.md#std-dtcompatible-ti-k2g-sci-clk"><code>ti,k2g-sci-clk</code></a></td>
</tr>
<tr>
<td rowspan="1">固件（Firmware）</td>
<td>片上（On-Chip）</td>
<td>TISCI客户端驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L15">已禁用：1</a>）</td>
<td><a href="../hardware/P612_TI%20K2G系统控制接口绑定.md#dtbinding-ti-k2g-sci"><code>ti,k2g-sci</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Davinci及Keystone器件的GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L225">已启用：2</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P013_ti_davinci-gpio-nexus.md#std-dtcompatible-ti-davinci-gpio-nexus"><code>ti,davinci-gpio-nexus</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Davinci及Keystone器件的GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L323">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L331">已禁用：5</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P014_ti_davinci-gpio.md#std-dtcompatible-ti-davinci-gpio"><code>ti,davinci-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>TI OMAP I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L189">已禁用：6</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P013_ti_omap-i2c.md#std-dtcompatible-ti-omap-i2c"><code>ti,omap-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>TI向量中断管理器（VIM）是TI专用外部中断控制器IP，兼容R5F的向量中断控制器（VIC）端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am64x_r5.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P009_ti_vim.md#std-dtcompatible-ti-vim"><code>ti,vim</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/lp_am243/lp_am243_r5f0_0.dts?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>TI安全代理邮箱（Secure Proxy Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L28">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P056_TI安全代理邮箱绑定.md#dtbinding-ti-secure-proxy"><code>ti,secure-proxy</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>TI OMAP邮箱（MAILBOX）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L495">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L479">已禁用：7</a>）</td>
<td><a href="../intercore_reference/P055_TIOMAP邮箱绑定.md#dtbinding-ti-omap-mailbox"><code>ti,omap-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">多位串行外设接口（Multi-Bit SPI）</td>
<td>片上（On-Chip）</td>
<td>带多线SPI接口（MSPI）的Cadence xSPI闪存控制器，支持双线、四线及八线SPI（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L702">已禁用：1</a>）</td>
<td><a href="../mspi_binding_reference/P003_cdns_xspi-nor.md#std-dtcompatible-cdns-xspi-nor"><code>cdns,xspi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>TI K3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L44">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_mcu.dtsi?plain=1#L22">已禁用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P013_ti_k3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl"><code>ti,k3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>由TISCI管理的电源域（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main_power_domains.dtsi?plain=1#L8">已启用：148</a>）</td>
<td><a href="../power_domain_binding_reference/P011_ti_sci-pm-domain.md#std-dtcompatible-ti-sci-pm-domain"><code>ti,sci-pm-domain</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>TI SoC基于增强型高分辨率PWM（EHRPWM）的PWM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L585">已禁用：9</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P014_ti_am3352-ehrpwm.md#std-dtcompatible-ti-am3352-ehrpwm"><code>ti,am3352-ehrpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>TI SoC基于增强型捕获模块（ECAP）的PWM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L675">已禁用：3</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P013_ti_am3352-ecap.md#std-dtcompatible-ti-am3352-ecap"><code>ti,am3352-ecap</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>TI SD／eMMC主机控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L542">已禁用：2</a>）</td>
<td><a href="../sdhc_binding_reference/P020_ti_am654-sdhci.md#std-dtcompatible-ti-am654-sdhci"><code>ti,am654-sdhci</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L133">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L141">已禁用：8</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>用于OMAP及K3 SoC的TI多通道SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L371">已禁用：7</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P018_ti_omap-mcspi.md#std-dtcompatible-ti-omap-mcspi"><code>ti,omap-mcspi</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>TI K3器件级控制寄存器模块（Device Level Control Register Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L36">已启用：3</a>）</td>
<td><a href="../edac_syscon_binding_reference/P009_ti_control-module.md#std-dtcompatible-ti-control-module"><code>ti,control-module</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>TI双模式定时器（Dual-Mode Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L109">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L61">已禁用：11</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P012_ti_am654-timer.md#std-dtcompatible-ti-am654-timer"><code>ti,am654-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>K3代处理器的看门狗定时器，实时间隔（RTI）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/ti/am64x_main.dtsi?plain=1#L430">已禁用：7</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P006_ti_j7-rti-wdt.md#std-dtcompatible-ti-j7-rti-wdt"><code>ti,j7-rti-wdt</code></a></td>
</tr>
</table>

<a id="booting-a-firmware"></a>

### 启动固件（Booting a Firmware）

<a id="the-am64x-am243x-bootflow"></a>

#### AM64x／AM243x启动流程（Bootflow）

AM64x／AM243x系列SoC因支持安全启动（Secure Boot）而具有专用启动流程。上电后首先在R5F0_0执行ROM内不可修改的引导加载器（RBL），随后应执行基于TI MCU+ SDK的第二阶段引导加载器（SBL），由其启动最终Zephyr固件。RBL可从外部闪存或UART传输等多种来源取得镜像。仅在AM64x上，也可使用TI SDK预制镜像充当SBL，在Cortex-A上启动Linux，再通过remoteproc将Zephyr固件加载到其他核。

此板可通过拨码开关选择SBL镜像读取位置。

<a id="id1"></a>

<table>
<tr>
<th>SW4 [1:7]</th>
</tr>
<tr>
<td>11100000</td>
</tr>
</table>

<a id="id2"></a>

<table>
<tr>
<th>SW4 [1:7]</th>
</tr>
<tr>
<td>01000100</td>
</tr>
</table>

<a id="flashing"></a>

## 烧录（Flashing）

AM2434启动流程要求镜像采用特定格式，并等待内部DMSC-L启动及配置内存防火墙（Memory Firewall）。Zephyr尚未提供这部分支持，因此必须使用TI MCU+ SDK的某个SBL引导加载器示例。

注意（Attention）

本页所有MCU+ SDK相关章节中的$Z_MCUPSDK_BOARD均需替换为am243x-lp；在文件外使用时，也可设置相应环境变量。

注意（Note）

虽然此板采用四线SPI（QSPI），而非八线SPI（OSPI），TI MCU+ SDK中该板的OSPI代码仍会正确使用QSPI。

<a id="mcu-sdk"></a>

### MCU+ SDK

<a id="setup"></a>

#### 设置（Setup）

以下步骤反映文档编写时的流程，未来可能变化。目标环境为Linux，并假定已安装python3及openssl等基础工具。

<a id="id10"></a>

构建前需安装TI MCU+ SDK。请按mcupsdk-core [GitHub仓库](https://github.com/TexasInstruments/mcupsdk-core)[注4](#id9)中的步骤操作，包括使用west克隆仓库。建议另建Python虚拟环境（venv），因为MCU+ SDK的Python依赖可能与Zephyr冲突。若想少克隆一些仓库，可将west init命令中的all/dev.yml替换为am243x/dev.yml。

还需执行“Downloading And Installing Dependencies”下载及安装依赖章节，但应将命令中的全部am263x替换为am243x。若不需要Doxygen或CCS，可向安装脚本传入--skip_doxygen=true及--skip_ccs=true。若提示某脚本无法执行，请用chmod +x <path>添加执行权限，然后重新运行download_components.sh。

注意（Attention）

请记录工具与mcu_plus_sdk的安装位置。后文以$TI_TOOLS表示download_components.sh使用的工具安装目录，以$MCUPSDK表示运行west init的mcu_plus_sdk目录。建议设置为环境变量，但文件内的占位符仍须按实际位置替换。

注意（Note）

安装MCU+ SDK通常需要执行以下命令或对应调整后的命令：

```text
python3 -m venv .venv
source .venv/bin/activate
pip3 install west
west init -m https://github.com/TexasInstruments/mcupsdk-manifests.git --mr mcupsdk_west --mf am243x/dev.yml
west update
./mcupsdk_setup/am243x/download_components.sh --skip_doxygen=true --skip_ccs=true
```

脚本成功后进入$MCUPSDK，编辑source/drivers/bootloader/bootloader.c，使Bootloader_runCpu中的entryPoint无条件设为0。这是由Zephyr当前镜像构建方式决定的。

随后使用以下命令构建内部库：

```text
make gen-buildfiles DEVICE=am243x PROFILE=release
make libs DEVICE=am243x PROFILE=release
```

若遇到编译错误，需要修复。可能涉及更改参数类型、从Makefile移除缺失的源文件，或从TI在线参考资料下载缺失的头文件。

<a id="building-mcu-sdk-sbls"></a>

#### 构建MCU+ SDK的SBL（Building MCU+ SDK SBLs）

SBL示例位于examples/drivers/boot/<example>/$Z_MCUPSDK_BOARD/r5fss0-0_nortos目录。

在$MCUPSDK目录运行make -C examples/drivers/boot/<example>/$Z_MCUPSDK_BOARD/r5fss0-0_nortos/ti-arm-clang/ DEVICE=am243x PROFILE=release即可构建示例。虽然存在sbl_prebuilt目录，但原文编写时该目录为空，只在构建SBL时才会填入内容。

建议根据用途按需构建以下SBL：

`sbl_null`

通过Code Composer Studio集成开发环境（CCS IDE）直接加载Zephyr .elf的引导加载器。易于使用，建议在开发期间从闪存启动它。

`sbl_uart`

通过UART启动RPRC格式固件文件的引导加载器。开发期间建议从UART启动，可避免反复切换UART及OSPI启动模式。

`sbl_ospi`

从闪存加载RPRC格式固件的引导加载器。需要断电后保留启动能力时推荐使用，在闪存偏移0x80000处寻找RPRC镜像。

`sbl_uart_uniflash`

可在RBL之后启动的应用，通常通过UART加载；它经UART接收数据并写入闪存。

<a id="id4"></a>

更多SBL见[TI MCU+ SDK启动流程文档](https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/latest/exports/docs/api_guide_am64x/BOOTFLOW_GUIDE.html)[注1](#id3)。

<a id="flashing-data-into-external-flash-with-the-mcu-sdk"></a>

#### 使用MCU+ SDK向外部闪存写入数据

向外部闪存写入数据时，先构建sbl_uart_uniflash示例，将生成的sbl_uart_uniflash.release.hs_fs.tiimage复制到工作目录，然后创建配置文件，将$FLASH_OFFSET及$FLASH_FILE分别替换为目标闪存偏移及待写入文件。

注意（Note）

$FLASH_OFFSET应采用0x80000这样的十六进制地址。

注意（Note）

可在不重启的情况下向不同位置写入多个文件，只需复制最后一行并调整文件及闪存偏移。

```text
--flash-writer=sbl_uart_uniflash.release.hs_fs.tiimage
--operation=flash-phy-tuning-data
--file=$FLASH_FILE --operation=flash --flash-offset=$FLASH_OFFSET
```

<a id="id6"></a>

随后运行python3 uart_uniflash.py -p /dev/ttyUSB0 --cfg=<path-to-the-config-file>。根据连接设备可能需要调整/dev/ttyUSB0。更多说明见[TI MCU+ SDK烧录文档](https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/latest/exports/docs/api_guide_am64x/TOOLS_FLASH.html)[注2](#id5)。

<a id="creating-a-sbl-bootable-rprc-image-from-a-zephyr-elf"></a>

#### 将Zephyr ELF转换为SBL可启动的RPRC镜像

将Zephyr ELF转换为sbl_uart、sbl_ospi等SBL可启动的RPRC文件需要执行多条命令。下面代码块假设zephyr.elf位于当前工作目录；根据固件目标核调整BOOTIMAGE_CORE_ID。

```text
export BOOTIMAGE_CORE_ID_r5fss0-0=4
export BOOTIMAGE_CORE_ID_m4=14
# set CORE_ID as per your target core
export BOOTIMAGE_CORE_ID=${BOOTIMAGE_CORE_ID_desired-core}
$TI_TOOLS/sysconfig_1.21.2/nodejs/node $MCUPSDK/tools/boot/out2rprc/elf2rprc.js ./zephyr.elf
$MCUPSDK/tools/boot/xipGen/xipGen.out -i ./zephyr.rprc -o ./zephyr.rprc_out -x ./zephyr.rprc_out_xip --flash-start-addr 0x60000000
$TI_TOOLS/sysconfig_1.21.2/nodejs/node $MCUPSDK/tools/boot/multicoreImageGen/multicoreImageGen.js --devID 55 --out ./zephyr.appimage ./zephyr.rprc_out@${BOOTIMAGE_CORE_ID}
$TI_TOOLS/sysconfig_1.21.2/nodejs/node $MCUPSDK/tools/boot/multicoreImageGen/multicoreImageGen.js --devID 55 --out ./zephyr.appimage_xip ./zephyr.rprc_out_xip@${BOOTIMAGE_CORE_ID}
python3 $MCUPSDK/source/security/security_common/tools/boot/signing/appimage_x509_cert_gen.py --bin ./zephyr.appimage --authtype 1 --key $MCUPSDK/source/security/security_common/tools/boot/signing/app_degenerateKey.pem --output ./zephyr.appimage.hs_fs
```

<a id="id8"></a>

结果文件为当前工作目录中的zephyr.appimage.hs_fs，采用SBL能够识别的TI RPRC格式。格式说明见[TI MCU+ SDK启动工具文档](https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/latest/exports/docs/api_guide_am64x/TOOLS_BOOT.html)[注3](#id7)。

<a id="full-bootflow-examples"></a>

#### 完整启动流程示例（Full Bootflow Examples）

下面归纳各启动方式所需步骤。

<a id="tab-0-0-0"></a>

<a id="tab-0-0-1"></a>

<a id="tab-0-0-2"></a>

<a id="panel-0-0-0"></a>

**通过调试器启动（Debugger Booting）**

通过调试器启动时，先按“构建MCU+ SDK的SBL”构建sbl_uart_uniflash及sbl_null，再将开发板切换到UART启动模式，按“[使用MCU+ SDK向外部闪存写入数据](#flashing-data-into-external-flash-with-the-mcu-sdk)”将sbl_null.release.hs_fs.tiimage写到0x0。（[构建MCU+ SDK的SBL（Building MCU+ SDK SBLs）](#building-mcu-sdk-sbls)）

随后切换到OSPI启动模式，通过Code Composer Studio调试器直接向所需核加载Zephyr ELF文件。

<a id="panel-0-0-1"></a>

**UART启动**

通过UART启动镜像时，先按“构建MCU+ SDK的SBL”构建sbl_uart，并将开发板切换到UART启动模式。（[构建MCU+ SDK的SBL（Building MCU+ SDK SBLs）](#building-mcu-sdk-sbls)）

随后按“[将Zephyr ELF转换为SBL可启动的RPRC镜像](#creating-a-sbl-bootable-rprc-image-from-a-zephyr-elf)”进行转换，并运行python3 $MCUPSDK/tools/boot/uart_bootloader.py -p /dev/ttyUSB0 --bootloader=sbl_uart.release.hs_fs.tiimage --file=zephyr.appimage.hs_fs。

<a id="panel-0-0-2"></a>

**OSPI启动**

通过OSPI启动镜像时，先按“构建MCU+ SDK的SBL”构建sbl_uart_uniflash及sbl_ospi，再将开发板切换到UART启动模式，按外部闪存烧录步骤将sbl_ospi.release.hs_fs.tiimage写到0x0；此操作只需执行一次。（[构建MCU+ SDK的SBL（Building MCU+ SDK SBLs）](#building-mcu-sdk-sbls)；[使用MCU+ SDK向外部闪存写入数据](#flashing-data-into-external-flash-with-the-mcu-sdk)）

此后每次新构建Zephyr固件，都需按RPRC转换步骤转换ELF，并按外部闪存烧录步骤写入0x80000。随后切换到OSPI启动模式即可运行。（[将Zephyr ELF转换为SBL可启动的RPRC镜像](#creating-a-sbl-bootable-rprc-image-from-a-zephyr-elf)；[使用MCU+ SDK向外部闪存写入数据](#flashing-data-into-external-flash-with-the-mcu-sdk)）

<a id="debugging"></a>

## 调试（Debugging）

<a id="openocd"></a>

### OpenOCD

此板配备XDS110 JTAG调试器，使用debug构建目标调试二进制：

```text
west build -b lp_am243/<soc>/<core> <my_app>
west debug
```

提示（Hint）

<a id="id16"></a>

使用此功能需要足够新的OpenOCD，可能需自行编译。方法见[从源码构建OpenOCD](https://docs.u-boot.org/en/latest/board/ti/k3.html#building-openocd-from-source)的说明[注7](#id15)。

<a id="references"></a>

## 参考资料（References）

<a id="id3"></a>

〔[1](#id4)〕 [https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/latest/exports/docs/api_guide_am64x/BOOTFLOW_GUIDE.html](https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/latest/exports/docs/api_guide_am64x/BOOTFLOW_GUIDE.html)

<a id="id5"></a>

〔[2](#id6)〕 [https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/latest/exports/docs/api_guide_am64x/TOOLS_FLASH.html](https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/latest/exports/docs/api_guide_am64x/TOOLS_FLASH.html)

<a id="id7"></a>

〔[3](#id8)〕 [https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/latest/exports/docs/api_guide_am64x/TOOLS_BOOT.html](https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/latest/exports/docs/api_guide_am64x/TOOLS_BOOT.html)

<a id="id9"></a>

〔[4](#id10)〕 [https://github.com/TexasInstruments/mcupsdk-core](https://github.com/TexasInstruments/mcupsdk-core)

<a id="id11"></a>

〔[5](#id12)〕 [https://www.ti.com/tool/LP-AM243](https://www.ti.com/tool/LP-AM243)

<a id="id13"></a>

〔[6](#id14)〕 [https://www.ti.com/product/en-us/AM2434#tech-docs](https://www.ti.com/product/en-us/AM2434#tech-docs)

<a id="id15"></a>

〔[7](#id16)〕 [https://docs.u-boot.org/en/latest/board/ti/k3.html#building-openocd-from-source](https://docs.u-boot.org/en/latest/board/ti/k3.html#building-openocd-from-source)

## 译注

AM243x LaunchPad硬件段将双核集群写成Cortex-R4F，与前文Cortex-R5F矛盾，按原文注明。此板使用QSPI，但TI SDK复用OSPI代码路径；MCU+ SDK板名为am243x-lp，不能沿用EVM的am243x-evm。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [AM2434](https://www.ti.com/product/en-us/AM2434#tech-docs)：页面可访问，但未确认目标片段。

---

[上一章](P015_AM13E230X_Launchpad.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P017_CC2340R5_LaunchPad.md)
