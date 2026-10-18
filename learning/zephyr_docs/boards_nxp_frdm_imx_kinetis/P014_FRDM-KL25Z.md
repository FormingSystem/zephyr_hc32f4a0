---
id: learning.zephyr-docs.boards-nxp-frdm-imx-kinetis.page-14
title: FRDM-KL25Z
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/frdm_kl25z/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="frdm_kl25z"></a>

# 第14章\_FRDM-KL25Z

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/frdm_kl25z/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/frdm_kl25z.jpg](images/frdm_kl25z.jpg)](images/frdm_kl25z.jpg)

FRDM-KL25Z

名称（Name）：

`frdm_kl25z`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mkl25z4](https://docs.zephyrproject.org/latest/boards/index.html#soc=mkl25z4)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_kl25z/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Freedom KL25Z是用于基于ARM® Cortex®-M0+的Kinetis® L系列KL1x（KL14／15）及KL2x（KL24／25）MCU的超低成本开发平台。

FRDM-KL25Z便于访问MCU I/O，支持电池供电及低功耗运行，采用标准化外形并可连接扩展板，内置用于闪存编程和运行控制的调试接口。

<a id="hardware"></a>

## 硬件（Hardware）


- MKL25Z128VLK4 MCU，48 MHz，128 KB闪存，16 KB SRAM，全速USB OTG，80引脚LQFP封装
- 板载电容触摸滑条（Slider）、MMA8451Q加速度计及三色LED
- OpenSDA调试接口

KL25Z SoC及FRDM-KL25Z更多信息：


- [KL25Z网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/l-seriesultra-low-powerm0-plus/kinetis-kl2x-72-96mhz-usb-ultra-low-power-microcontrollers-mcus-based-on-arm-cortex-m0-plus-core:KL2x?&l)
- [KL25Z数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/KL25P80M48SF0.pdf)
- [KL25Z参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=KL25P80M48SF0RM)
- [FRDM-KL25Z网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/l-seriesultra-low-powerm0-plus/freedom-development-platform-for-kinetis-kl14-kl15-kl24-kl25-mcus:FRDM-KL25Z)
- [FRDM-KL25Z用户指南（User Guide）](https://www.nxp.com/webapp/Download?colCode=FRDMKL25ZUM)
- [FRDM-KL25Z原理图（Schematics）](https://www.nxp.com/downloads/en/schematics/FRDM-KL25Z_SCH_REV_E.pdf)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`frdm_kl25z`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="frdm_kl25z-hw-features"></a>

<a id="frdm_kl25z-frdm_kl25z/mkl25z4-hw-features-section"></a>

#### `frdm_kl25z/mkl25z4`目标（Target）

<a id="frdm_kl25z-frdm_kl25z/mkl25z4-hw-features-panel"></a>

<a id="frdm_kl25z-frdm_kl25z/mkl25z4-hw-features-memory"></a>

该开发板目标的片上存储容量：16 KiB RAM、128 KiB Flash。

<a id="frdm_kl25z-frdm_kl25z/mkl25z4-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Kinetis 16位模数转换器（ADC16）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L162">已启用：1</a>）</td>
<td><a href="../hardware/P850_NXPKinetisADC16绑定.md#dtbinding-nxp-kinetis-adc16"><code>nxp,kinetis-adc16</code></a></td>
</tr>
<tr>
<td rowspan="3">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis多用途时钟发生器（MCG）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L61">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P003_nxp_kinetis-mcg.md#std-dtcompatible-nxp-kinetis-mcg"><code>nxp,kinetis-mcg</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Kinetis系统集成模块（SIM）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L94">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P006_nxp_kinetis-sim.md#std-dtcompatible-nxp-kinetis-sim"><code>nxp,kinetis-sim</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L99">已启用：2</a>）</td>
<td><a href="../timer_reference/P110_固定比例时钟绑定.md#dtbinding-fixed-factor-clock"><code>fixed-factor-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis闪存模块A（FTFA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L44">已禁用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P014_nxp_kinetis-ftfa.md#std-dtcompatible-nxp-kinetis-ftfa"><code>nxp,kinetis-ftfa</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Kinetis通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L220">已启用：5</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P002_nxp_kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio"><code>nxp,kinetis-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kl25z/frdm_kl25z.dts?plain=1#L69">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP RCM获取复位原因标志（Reset Cause Flags）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L89">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P012_nxp_rcm-hwinfo.md#std-dtcompatible-nxp-rcm-hwinfo"><code>nxp,rcm-hwinfo</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Kinetis I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L67">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L78">已禁用：1</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P002_nxp_kinetis-i2c.md#std-dtcompatible-nxp-kinetis-i2c"><code>nxp,kinetis-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kl25z/frdm_kl25z.dts?plain=1#L53">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kl25z/frdm_kl25z.dts?plain=1#L34">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L190">已启用：5</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P017_nxp_port-pinmux.md#std-dtcompatible-nxp-port-pinmux"><code>nxp,port-pinmux</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L38">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P016_nxp_port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl"><code>nxp,port-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L123">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L136">已禁用：2</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P008_nxp_kinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm"><code>nxp,kinetis-tpm</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>FXOS8700六轴加速度计／磁力计传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kl25z/frdm_kl25z.dts?plain=1#L123">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P052_nxp_fxos8700.md#std-dtcompatible-nxp-fxos8700"><code>nxp,fxos8700</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Kinetis低功耗串行通信接口（LPSCI）UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L114">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P012_nxp_kinetis-lpsci.md#std-dtcompatible-nxp-kinetis-lpsci"><code>nxp,kinetis-lpsci</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>面向KL25Z的自定义NXP Kinetis L系列SPI驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L170">已启用：2</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P002_nxp_kinetis-l-spi.md#std-dtcompatible-nxp-kinetis-l-spi"><code>nxp,kinetis-l-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>设备模式下的NPX Kinetis USBFSOTG控制器，厂商缩写NPX按原文保留（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/kinetis/kl2x/nxp_kl25z.dtsi?plain=1#L267">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P007_nxp_kinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd"><code>nxp,kinetis-usbd</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

KL25Z有5对引脚复用／GPIO控制器，FRDM-KL25Z当前全部启用：PORTA／GPIOA、PORTB／GPIOB、PORTC／GPIOC、PORTD／GPIOD及PORTE／GPIOE。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PTB2</td>
<td>模数转换器（ADC）</td>
<td>ADC0通道12</td>
</tr>
<tr>
<td><code>PTB18</code></td>
<td>通用输入输出（GPIO）</td>
<td>红色LED（Red LED）</td>
</tr>
<tr>
<td><code>PTB19</code></td>
<td>通用输入输出（GPIO）</td>
<td>绿色LED（Green LED）</td>
</tr>
<tr>
<td>PTD1</td>
<td>通用输入输出（GPIO）</td>
<td>蓝色LED（Blue LED）</td>
</tr>
<tr>
<td>PTA1</td>
<td>UART0_RX</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>PTA2</td>
<td>UART0_TX</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>PTE24</td>
<td>I2C0_SCL</td>
<td>集成电路间总线（I2C）</td>
</tr>
<tr>
<td>PTE25</td>
<td>I2C0_SDA</td>
<td>集成电路间总线（I2C）</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

KL25Z使用板载8 MHz外部振荡器及片上FLL，生成48 MHz系统时钟。

<a id="serial-port"></a>

### 串口（Serial Port）

KL25Z UART0用于控制台。

<a id="usb"></a>

### 通用串行总线（USB）

KL25Z USB OTG控制器支持通过原文所称Mini-USB连接器USB KL25Z提供设备及主机功能，但Zephyr当前仅支持设备功能。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`frdm_kl25z`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-jlink">jlink</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-linkserver">linkserver</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td></td>
<td></td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-pyocd">pyocd</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

按通常方式构建并烧录应用，详见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）与“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

<a id="configuring-a-debug-probe"></a>

### 配置调试探针（Configuring a Debug Probe）

烧录及调试均使用调试探针，默认配置为OpenSDA DAPLink板载调试探针。（[OpenSDA DAPLink板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#opensda-daplink-onboard-debug-probe)）

早期开发板的OpenSDA引导加载程序版本过旧，需要更新。按DAPLink引导加载程序更新（Bootloader Update）页面说明，从CMSIS-DAP引导加载程序升级到DAPLink。（[更新DAPLink引导加载程序（Bootloader）](https://os.mbed.com/blog/entry/DAPLink-bootloader-update/)）

<a id="option-1-linkserver-opensda-daplink-onboard-debug-probe-recommended"></a>

#### 选项1：LinkServer及OpenSDA DAPLink板载调试探针，推荐（[OpenSDA DAPLink板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#opensda-daplink-onboard-debug-probe)）

> 安装LinkServer调试主机工具并加入搜索路径。它兼容CMSIS-DAP调试固件；按OpenSDA DAPLink板载调试探针说明选择最新固件镜像版本。（[LinkServer调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#linkserver-debug-host-tools)；[OpenSDA DAPLink板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#opensda-daplink-onboard-debug-probe)）
>
> 此板默认使用LinkServer，west flash及west debug将调用linkserver运行工具。
>
> ```text
> west flash
> west debug
> ```

<a id="option-2-opensda-jlink-onboard-debug-probe"></a>

#### 选项2：OpenSDA J-Link板载调试探针（[OpenSDA J-Link板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#opensda-jlink-onboard-debug-probe)）

安装J-Link调试主机工具（Debug Host Tools），并确保工具位于搜索路径中。（[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)）

按OpenSDA J-Link板载调试探针说明，写入[OpenSDA J-Link FRDM-KL25Z固件](https://www.segger.com/downloads/jlink/OpenSDA_FRDM-KL25Z)。（[OpenSDA J-Link板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#opensda-jlink-onboard-debug-probe)）

调用west build时添加-DBOARD_FLASH_RUNNER=jlink及-DBOARD_DEBUG_RUNNER=jlink，将运行工具改为J-Link。原文此处称默认工具为pyOCD，与前文默认LinkServer的说明不同：

```text
# From the root of the zephyr repository
west build -b frdm_kl25z samples/hello_world -- -DBOARD_FLASH_RUNNER=jlink -DBOARD_DEBUG_RUNNER=jlink
```

<a id="note"></a>

#### 注意（Note）：

NXP支持的运行工具为LinkServer及J-Link。pyOCD也是可能的选择，但NXP不对它测试或提供支持。

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

无论选择哪种调试探针，串行控制台都使用OpenSDA微控制器作为USB转串口适配器。

用USB线缆将PC连接J7。

在串口终端中使用以下设置，例如minicom或PuTTY：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

### 烧录（Flashing）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b frdm_kl25z samples/hello_world
west flash
```

打开串口终端，按SW1复位开发板，应显示以下消息：

```text
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! frdm_kl25z
```

<a id="debugging"></a>

### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b frdm_kl25z samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! frdm_kl25z
```

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)
- [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)
- [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- NXP Zephyr主页，包含培训资源（[NXP的Zephyr专题页面](https://nxp.com/zephyr)）
- [NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## 译注

USB连接器的mini USB表述按原文保留，USB硬件能力与Zephyr当前仅设备模式的支持范围分别说明。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [KL25P80M48SF0.pdf](https://www.nxp.com/docs/en/data-sheet/KL25P80M48SF0.pdf)：HTTP Error 404: Not Found。
- [FRDM-KL25Z_SCH_REV_E.pdf](https://www.nxp.com/downloads/en/schematics/FRDM-KL25Z_SCH_REV_E.pdf)：HTTP Error 404: Not Found。
- [freedom-development-platform-for-kinetis-kl14-kl15-kl24-kl25-mcus:FRDM-KL25Z](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/l-seriesultra-low-powerm0-plus/freedom-development-platform-for-kinetis-kl14-kl15-kl24-kl25-mcus:FRDM-KL25Z)：HTTP Error 404: Not Found。
- [kinetis-kl2x-72-96mhz-usb-ultra-low-power-microcontrollers-mcus-based-on-arm-cortex-m0-plus-core:KL2x?&l](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/l-seriesultra-low-powerm0-plus/kinetis-kl2x-72-96mhz-usb-ultra-low-power-microcontrollers-mcus-based-on-arm-cortex-m0-plus-core:KL2x?&l)：HTTP Error 404: Not Found。
- [Download?colCode=FRDMKL25ZUM](https://www.nxp.com/webapp/Download?colCode=FRDMKL25ZUM)：HTTP Error 404: Not Found。
- [Download?colCode=KL25P80M48SF0RM](https://www.nxp.com/webapp/Download?colCode=KL25P80M48SF0RM)：HTTP Error 404: Not Found。

---

[上一章](P013_FRDM-KE17Z512.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P015_FRDM-KW41Z.md)
