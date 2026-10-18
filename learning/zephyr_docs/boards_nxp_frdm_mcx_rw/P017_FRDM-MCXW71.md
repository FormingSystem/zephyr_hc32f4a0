---
id: learning.zephyr-docs.boards-nxp-frdm-mcx-rw.page-17
title: FRDM-MCXW71
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxw71/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="frdm_mcxw71"></a>

# 第17章\_`FRDM-MCXW71`

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxw71/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/frdm_mcxw71.webp](images/frdm_mcxw71.webp)](images/frdm_mcxw71.webp)

`FRDM-MCXW71`

名称（Name）：

`frdm_mcxw71`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mcxw716c](https://docs.zephyrproject.org/latest/boards/index.html#soc=mcxw716c)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_mcxw71/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

FRDM-MCXW71是紧凑、可扩展的开发板，用于MCX W71无线MCU的快速原型开发，可便捷评估Bluetooth LE、Zigbee、Thread和Matter多协议无线支持。板载MCU-Link调试器、便于访问MCU I/O的工业标准排针、加速度计、光传感器及外部SPI闪存。

MCX W71x系列采用96 MHz Arm Cortex-M33内核，配合支持Matter、Thread、Zigbee及Bluetooth LE的多协议无线子系统。无线子系统具有独立内核及存储器，可分担主CPU的工作，让主CPU服务于主要应用，并通过固件更新支持未来无线标准。

<a id="hardware"></a>

## 硬件（Hardware）


- MCXW71 Arm Cortex-M33微控制器，最高96 MHz
- 1 MB片上闪存单元
- 128 KB TCM RAM
- 支持CMSIS-DAP的板载MCU-Link调试器

MCXW71 SoC及FRDM-MCXW71开发板的更多信息见以下资料：


- <a id="id17"></a>

  [MCXW71 SoC网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w71x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W71X) [注8](#id16)
- <a id="id19"></a>

  [FRDM-MCXW71网站](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-w71x-wireless-mcus:FRDM-MCXW71) [注9](#id18)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`frdm_mcxw71`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="frdm_mcxw71-hw-features"></a>

<a id="frdm_mcxw71-frdm_mcxw71/mcxw716c-hw-features-section"></a>

#### `frdm_mcxw71/mcxw716c`目标（Target）

<a id="frdm_mcxw71-frdm_mcxw71/mcxw716c-hw-features-panel"></a>

<a id="frdm_mcxw71-frdm_mcxw71/mcxw716c-hw-features-memory"></a>

该开发板目标的片上存储容量：112 KiB RAM、1 MiB Flash。

<a id="frdm_mcxw71-frdm_mcxw71/mcxw716c-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L497">已启用：1</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>NXP NBU中断信息（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L460">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P017_nxp_nbu.md#std-dtcompatible-nxp-nbu"><code>nxp,nbu</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗蓝牙主机控制器接口（BLE HCI）信息（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L471">已启用：1</a>）</td>
<td><a href="../bluetooth_vendor_hci_binding_reference/P009_nxp_hci-ble.md#std-dtcompatible-nxp-hci-ble"><code>nxp,hci-ble</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L483">已启用：1</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd"><code>nxp,flexcan-fd</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP MCXW7X系列时钟控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L211">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P012_nxp_mcxw7x-clock.md#std-dtcompatible-nxp-mcxw7x-clock"><code>nxp,mcxw7x-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L62">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗周期中断定时器（LPIT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L256">已禁用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P012_nxp_lpit.md#std-dtcompatible-nxp-lpit"><code>nxp,lpit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>低功耗周期中断定时器节点的子节点，表示一个独立定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L268">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P011_nxp_lpit-channel.md#std-dtcompatible-nxp-lpit-channel"><code>nxp,lpit-channel</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP低功耗定时器（LPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L429">已启用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr"><code>nxp,lptmr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP时间戳定时器（TSTMR / Time Stamp Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L453">已启用：1</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P004_nxp_tstmr.md#std-dtcompatible-nxp-tstmr"><code>nxp,tstmr</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L592">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P006_nxp_crc.md#std-dtcompatible-nxp-crc"><code>nxp,crc</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L548">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP MSF1闪存模块（FMU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L70">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P018_nxp_msf1.md#std-dtcompatible-nxp-msf1"><code>nxp,msf1</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Kinetis通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L625">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L371">已禁用：2</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P002_nxp_kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio"><code>nxp,kinetis-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxw71/frdm_mcxw71.dts?plain=1#L74">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC 128位唯一标识符（Unique Identifier）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L192">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P009_nxp_lpc-uid.md#std-dtcompatible-nxp-lpc-uid"><code>nxp,lpc-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件自旋锁（Hardware Spinlock）</td>
<td>片上（On-Chip）</td>
<td>NXP SEMA42硬件信号量（Hardware Semaphore）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L601">已启用：1</a>）</td>
<td><a href="../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42"><code>nxp,sema42</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L330">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L317">已禁用：1</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">低速率无线个域网（IEEE 802.15.4）</td>
<td>片上（On-Chip）</td>
<td>NXP MCXW71 IEEE 802.15.4节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L475">已启用：1</a>）</td>
<td><a href="../lora_ieee802154_binding_reference/P008_nxp_mcxw-ieee802154.md#std-dtcompatible-nxp-mcxw-ieee802154"><code>nxp,mcxw-ieee802154</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxw71/frdm_mcxw71.dts?plain=1#L63">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxw71/frdm_mcxw71.dts?plain=1#L39">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxw71/frdm_mcxw71.dts?plain=1#L47">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L576">已禁用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCXW7x硬件参数（HW_PARAMS）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L171">已启用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P002_nxp_mcxw-hw-params.md#std-dtcompatible-nxp-mcxw-hw-params"><code>nxp,mcxw-hw-params</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="3">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L83">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCXW闪存信息行（IFR）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P002_nxp_mcxw-ifr.md#std-dtcompatible-nxp-mcxw-ifr"><code>nxp,mcxw-ifr</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>这些属性用于支持Zephyr的<code>spi-nor</code>闪存驱动通过Zephyr SPI API，使用基于M25P80的标准命令集控制串行闪存（Serial Flash Memory）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxw71/frdm_mcxw71.dts?plain=1#L152">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor"><code>jedec,spi-nor</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L228">已启用：4</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P017_nxp_port-pinmux.md#std-dtcompatible-nxp-port-pinmux"><code>nxp,port-pinmux</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP PORT引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L167">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P016_nxp_port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl"><code>nxp,port-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="3">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>NXP内核模式控制器（CMC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L186">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P014_nxp_cmc.md#std-dtcompatible-nxp-cmc"><code>nxp,cmc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP系统电源控制器（SPC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L197">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P001_nxp_spc.md#std-dtcompatible-nxp-spc"><code>nxp,spc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP智能电源开关（VBAT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L381">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P002_nxp_vbat.md#std-dtcompatible-nxp-vbat"><code>nxp,vbat</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>MCUX定时器／PWM模块（TPM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L387">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L399">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P008_nxp_kinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm"><code>nxp,kinetis-tpm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP FlexIO脉宽调制（PWM）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L585">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P002_nxp_flexio-pwm.md#std-dtcompatible-nxp-flexio-pwm"><code>nxp,flexio-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>NXP VREF SoC外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L515">已启用：1</a>）</td>
<td><a href="../hardware/P652_NXP参考电压绑定.md#dtbinding-nxp-vref"><code>nxp,vref</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>NXP EdgeLock安全隔离区（ELE / EdgeLock Secure Enclave）的真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L479">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P016_nxp_ele-trng.md#std-dtcompatible-nxp-ele-trng"><code>nxp,ele-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>NXP实时时钟（RTC / Real Time Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L533">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P002_nxp_rtc.md#std-dtcompatible-nxp-rtc"><code>nxp,rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>FXLS8974三轴加速度传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxw71/frdm_mcxw71.dts?plain=1#L138">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P051_nxp_fxls8974.md#std-dtcompatible-nxp-fxls8974"><code>nxp,fxls8974</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L293">已启用：2</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L357">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L343">已禁用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L128">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>NXP看门狗（WDOG32）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L411">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L420">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P014_nxp_wdog32.md#std-dtcompatible-nxp-wdog32"><code>nxp,wdog32</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP外部看门狗监测器（External Watchdog Monitor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L565">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P007_nxp_ewm.md#std-dtcompatible-nxp-ewm"><code>nxp,ewm</code></a></td>
</tr>
<tr>
<td rowspan="1">唤醒控制器（Wakeup Controller）</td>
<td>片上（On-Chip）</td>
<td>作为唤醒控制器（WUC）的NXP唤醒单元（WUU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/mcx/mcxw/nxp_mcxw7x_common.dtsi?plain=1#L204">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P008_nxp_wuc-wuu.md#std-dtcompatible-nxp-wuc-wuu"><code>nxp,wuc-wuu</code></a></td>
</tr>
</table>

<a id="fetch-binary-blobs"></a>

## 获取二进制文件（Fetch Binary Blobs）

为支持蓝牙，frdm_mcxw71需要下载二进制组件（Binary Blobs），可执行以下命令：

```text
west blobs fetch hal_nxp -l "mcxw71"
```

注意（Note）

-l选项接收Python正则表达式，与每个二进制组件的路径匹配。传入“mcxw71”只下载此板需要的组件；省略该选项，即执行west blobs fetch hal_nxp，则下载全部NXP二进制组件。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`frdm_mcxw71`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
</table>

按通常方式构建并烧录应用，详见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）与“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

<a id="configuring-a-debug-probe"></a>

### 配置调试探针（Configuring a Debug Probe）

烧录和调试均使用调试探针，默认配置为MCU-Link CMSIS-DAP板载调试探针。

<a id="using-linkserver"></a>

#### 使用LinkServer

默认运行工具为LinkServer，支持出厂MCU-Link固件。只有板载调试电路固件被更换时，才需按MCU-Link CMSIS-DAP板载调试探针说明重新写入默认固件；写入前短接J5，进入DFU模式。原文此处为J5，后面的J-Link步骤为JP5。（[板载MCU-Link CMSIS-DAP调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#mcu-link-cmsis-onboard-debug-probe)）

<a id="using-j-link"></a>

#### 使用J-Link

有两种方案。第一种按MCU-Link J-Link板载调试探针说明，将板载调试电路更新为Segger J-Link固件；写入前短接JP5，进入DFU模式。第二种将外部J-Link调试探针连接到10引脚SWD连接器J12。两种方案都需给west传入-r jlink，选择J-Link运行工具。（[MCU-Link J-Link板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#mcu-link-jlink-onboard-debug-probe)；[J-Link外部调试探针（External Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#jlink-external-debug-probe)）

```text
west flash -r jlink
```

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

用USB线缆将PC连接到J10，在所选串口终端（如minicom、PuTTY）中使用以下设置：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="application-building"></a>

### 构建应用（Application Building）

<a id="openthread-applications"></a>

#### OpenThread应用

```text
# From the root of the zephyr repository
west build -b frdm_mcxw71 samples/net/sockets/echo_server -- -DEXTRA_CONF_FILE=overlay-ot.conf
```

```text
# From the root of the zephyr repository
west build -b frdm_mcxw71 samples/net/sockets/echo_client -- -DEXTRA_CONF_FILE=overlay-ot.conf
```

<a id="application-flashing"></a>

### `Application Flashing`

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b frdm_mcxw71/mcxw716c samples/hello_world
west flash
```

打开串口终端，复位开发板（按下RESET按键），应能在终端中看到以下消息：

```text
*** Booting Zephyr OS build v3.7.0-xxx-xxxx ***
Hello World! frdm_mcxw71/mcxw716c
```

<a id="debugging"></a>

### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b frdm_mcxw71/mcxw716c samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
*** Booting Zephyr OS build v3.7.0-xxx-xxxx ***
Hello World! frdm_mcxw71/mcxw716c
```

<a id="entering-isp-mode"></a>

### `Entering ISP Mode`

按以下步骤使MCU以ISP模式启动：

> - 断开FRDM-MCXW71的全部电源。
> - 按住板上的SW3，同时将开发板连接到主机USB端口。
> - 松开SW3，MCU即以ISP模式启动。原文此处写MCXW72，虽然当前页面介绍MCXW71。
> - 如有需要，重新连接外部电源。

<a id="flashing-with-low-power-mode"></a>

### 低功耗模式下的烧录（Flashing with Low Power Mode）

运行启用低功耗模式的应用（CONFIG_PM=y）时，通过常规MCU-Link或J-Link调试探针烧录可能失败，因为MCU进入某些低功耗状态后，SWD调试接口会停止响应。

为运行低功耗镜像的开发板重新烧录时，应先进入ISP模式，步骤见“进入ISP模式”（Entering ISP Mode）。

<a id="nbu-flashing"></a>

### `NBU Flashing`

BLE功能依赖二进制组件，请先完成“获取二进制组件”（Fetch Binary Blobs）一节。

需要向开发板写入两个镜像：主机核CM33的镜像及NBU无线子系统CM3的镜像。


- CM33应用的烧录方法见前面的“应用烧录”（Application Flashing）一节。
- 按以下步骤烧录NBU：

  > - 从NXP网站安装blhost，用于烧录NBU。
  > - 进入ISP模式，步骤见“进入ISP模式”（Entering ISP Mode）。
  > - 从此板的二进制组件目录`<zephyr workspace>/modules/hal/nxp/zephyr/blobs/mcxw71/`中选择所需协议的NBU镜像，例如仅BLE镜像或动态BLE + 802.15.4镜像，然后烧录：

<a id="tab-0-V2luZG93cw=="></a>

<a id="tab-0-TGludXg="></a>

<a id="panel-0-V2luZG93cw=="></a>

**Windows**

```text
blhost.exe -p COMxx -- receive-sb-file <nbu-image>
```

<a id="panel-0-TGludXg="></a>

**Linux**

```text
./blhost -p /dev/ttyxx -- receive-sb-file <nbu-image>
```

将COMxx／ttyxx替换为开发板实际串口，将`<nbu-image>`替换为blobs/mcxw71/目录中选定的文件。

更多细节参见：

<a id="troubleshooting"></a>

### 故障排查（Troubleshooting）

<a id="using-segger-systemview-and-rtt"></a>

#### 使用Segger SystemView及RTT

此SoC使用SEGGER SystemView或实时传输（RTT）时，必须在SystemView或RTT Viewer中手动设置RTT控制块地址。该地址为_SEGGER_RTT符号的位置，可通过调试器或链接器输出的zephyr.map文件查找。

必须手动指定控制块地址，是因为此SoC支持带纠错码（ECC）的RAM。当ECC已启用、待搜索RAM区域尚未初始化为已知值时，SEGGER工具若在ECC RAM中搜索控制块，将引发故障（Fault）。

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- <a id="id3"></a>

  [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)[注1](#id2)
- <a id="id5"></a>

  [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)[注2](#id4)
- <a id="id7"></a>

  <a id="id9"></a>

  [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode) [注3](#id6)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html) [注4](#id8)
- <a id="id11"></a>

  [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)[注5](#id10)
- <a id="id13"></a>

  [NXP的Zephyr专题页面](https://nxp.com/zephyr) [注6](#id12)，含培训资源
- <a id="id15"></a>

  NXP Zephyr支持社区论坛 [注7](#id14)（[NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)）

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)

<a id="id4"></a>

〔[2](#id5)〕 [https://github.com/nxp-zephyr/nxp-zsdk](https://github.com/nxp-zephyr/nxp-zsdk)

<a id="id6"></a>

〔[3](#id7)〕 [https://mcuxpresso.nxp.com/mcux-vscode](https://mcuxpresso.nxp.com/mcux-vscode)

<a id="id8"></a>

〔[4](#id9)〕 [https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)

<a id="id10"></a>

〔[5](#id11)〕 [https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)

<a id="id12"></a>

〔[6](#id13)〕 [https://nxp.com/zephyr](https://nxp.com/zephyr)

<a id="id14"></a>

〔[7](#id15)〕 [https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

<a id="id16"></a>

〔[8](#id17)〕 [https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w71x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W71X](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w71x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W71X)

<a id="id18"></a>

〔[9](#id19)〕 [https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-w71x-wireless-mcus:FRDM-MCXW71](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-w71x-wireless-mcus:FRDM-MCXW71)

## 译注

原文LinkServer步骤为J5，J-Link步骤为JP5；ISP退出描述又写MCXW72，均标注保留。低功耗状态可能使SWD无响应，重新烧录需先进入ISP。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [frdm-development-board-for-mcx-w71x-wireless-mcus:FRDM-MCXW71](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-w71x-wireless-mcus:FRDM-MCXW71)：HTTP Error 404: Not Found。
- [mcx-w71x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W71X](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w71x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W71X)：HTTP Error 404: Not Found。

---

[上一章](P016_FRDM-MCXW70.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P018_FRDM-MCXW72.md)
