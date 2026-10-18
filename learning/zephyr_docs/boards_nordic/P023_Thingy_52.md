---
id: learning.zephyr-docs.boards-nordic.page-23
title: Thingy 52
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nordic/thingy52/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="thingy52"></a>

# 第23章\_Thingy:52

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nordic/thingy52/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/thingy52.jpg](images/thingy52.jpg)](images/thingy52.jpg)

Thingy:52

名称（Name）：

`thingy52`

厂商（Vendor）：

[Nordic Semiconductor](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nordic)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[nrf52832](https://docs.zephyrproject.org/latest/boards/index.html#soc=nrf52832)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nordic/thingy52/doc/index.rst/../..)警告（Warning）

Nordic Semiconductor已停止为此板提供支持，因此不建议用于新的原型。

<a id="overview"></a>

## 概述（Overview）

Zephyr使用thingy52/nrf52832（PCA20020）开发板配置为Thingy:52构建应用。开发板带nRF52832 ARM Cortex-M4F MCU、一组环境传感器、一个按键及两个RGB LED。

<a id="id3"></a>

<a id="id5"></a>

原文将更多开发板信息指向[nRF52 DK网站](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/Nordic-Thingy-52) [注1](#id2)；[Nordic Thingy:52指南](https://docs.nordicsemi.com/bundle/ug_thingy52/page/UG/thingy52/intro/frontpage.html) [注2](#id4) 提供处理器信息及数据手册。

<a id="hardware"></a>

## 硬件（Hardware）

Thingy:52具有以下功能：


- 两个RGB LED
- 二氧化碳（CO2）及总挥发性有机物（TVOC）传感器
- 温湿度传感器
- 颜色传感器（Color Sensor）
- I2C GPIO扩展器（Expander）
- 预留排针、I2C及串行连接器位置
- 蓝牙无线电（Bluetooth Radio）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`thingy52`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="thingy52-hw-features"></a>

<a id="thingy52-thingy52/nrf52832-hw-features-section"></a>

#### `thingy52/nrf52832`目标（Target）

<a id="thingy52-thingy52/nrf52832-hw-features-panel"></a>

<a id="thingy52-thingy52/nrf52832-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、512 KiB Flash。

<a id="thingy52-thingy52/nrf52832-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Nordic Semiconductor nRF系列逐次逼近模数转换器（SAADC）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L239">已启用：1</a>）</td>
<td><a href="../hardware/P846_NordicNRF逐次逼近ADC绑定.md#dtbinding-nordic-nrf-saadc"><code>nordic,nrf-saadc</code></a></td>
</tr>
<tr>
<td rowspan="4">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>Nordic用户信息配置寄存器（UICR / User Information Configuration Registers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L57">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P007_nordic_nrf-uicr.md#std-dtcompatible-nordic-nrf-uicr"><code>nordic,nrf-uicr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Nordic nRF系列块保护（BPROT / Block Protection）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L121">已启用：1</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P015_nordic_nrf-bprot.md#std-dtcompatible-nordic-nrf-bprot"><code>nordic,nrf-bprot</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Nordic事件发生器单元（EGU / Event Generator Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L352">已启用：6</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P018_nordic_nrf-egu.md#std-dtcompatible-nordic-nrf-egu"><code>nordic,nrf-egu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Nordic nRF系列存储器监视单元（MWU / Memory Watch Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L452">已启用：1</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P022_nordic_nrf-mwu.md#std-dtcompatible-nordic-nrf-mwu"><code>nordic,nrf-mwu</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>片上（On-Chip）</td>
<td>Nordic脉冲密度调制接口（PDM / Pulse Density Modulation Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L422">已禁用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P012_nordic_nrf-pdm.md#std-dtcompatible-nordic-nrf-pdm"><code>nordic,nrf-pdm</code></a></td>
</tr>
<tr>
<td rowspan="4">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Nordic nRF时钟控制（Clock Control）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../clock_sam_nordic_binding_reference/P015_nordic_nrf-clock.md#std-dtcompatible-nordic-nrf-clock"><code>nordic,nrf-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Nordic nRF高频时钟（HFCLK）控制节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../clock_sam_nordic_binding_reference/P009_nordic_nrf-clock-hfclk.md#std-dtcompatible-nordic-nrf-clock-hfclk"><code>nordic,nrf-clock-hfclk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Nordic nRF低频时钟（LFCLK）控制节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L83">已启用：1</a>）</td>
<td><a href="../clock_sam_nordic_binding_reference/P012_nordic_nrf-clock-lfclk.md#std-dtcompatible-nordic-nrf-clock-lfclk"><code>nordic,nrf-clock-lfclk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Nordic nRF高频晶体振荡器（High-frequency Crystal Oscillator，nRF52系列）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../clock_sam_nordic_binding_reference/P022_nordic_nrf52-hfxo.md#std-dtcompatible-nordic-nrf52-hfxo"><code>nordic,nrf52-hfxo</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>Nordic nRF模拟比较器（COMP / Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L341">已禁用：1</a>）</td>
<td><a href="../hardware/P752_NordicnRF比较器绑定.md#dtbinding-nordic-nrf-comp"><code>nordic,nrf-comp</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Nordic nRF定时器（Timer）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L248">已禁用：5</a>）</td>
<td><a href="../microchip_soc_counter_binding_reference/P017_nordic_nrf-timer.md#std-dtcompatible-nordic-nrf-timer"><code>nordic,nrf-timer</code></a></td>
</tr>
<tr>
<td rowspan="2">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>Nordic ECB（AES电子密码本模式加密 / Electronic Codebook Mode Encryption）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L302">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P001_nordic_nrf-ecb.md#std-dtcompatible-nordic-nrf-ecb"><code>nordic,nrf-ecb</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Nordic nRF系列CCM（AES CCM模式加密 / CCM Mode Encryption）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L309">已启用：1</a>）</td>
<td><a href="../crypto_aes_sha_ccm_binding_reference/P020_nordic_nrf-ccm.md#std-dtcompatible-nordic-nrf-ccm"><code>nordic,nrf-ccm</code></a></td>
</tr>
<tr>
<td rowspan="1">调试（Debug）</td>
<td>片上（On-Chip）</td>
<td>ARMv7仪器化跟踪宏单元（ITM / Instrumentation Trace Macrocell）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../debug_binding_reference/P001_ARMv7M_ITM调试绑定.md#std-dtcompatible-arm-armv7m-itm"><code>arm,armv7m-itm</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Nordic非易失性存储器控制器（NVMC / Non-Volatile Memory Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L429">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P030_nordic_nrf52-flash-controller.md#std-dtcompatible-nordic-nrf52-flash-controller"><code>nordic,nrf52-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="3">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>SX1509B GPIO（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L146">已启用：1</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P006_semtech_sx1509b.md#std-dtcompatible-semtech-sx1509b"><code>semtech,sx1509b</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NRF5 GPIO任务与事件（GPIOTE）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L231">已启用：1</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P017_nordic_nrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote"><code>nordic,nrf-gpiote</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NRF5通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L511">已启用：1</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P016_nordic_nrf-gpio.md#std-dtcompatible-nordic-nrf-gpio"><code>nordic,nrf-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Nordic nRF系列TWIM（带EasyDMA的TWI主机）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L152">已启用：2</a>）</td>
<td><a href="../i2c_infineon_ite_nordic_binding_reference/P016_nordic_nrf-twim.md#std-dtcompatible-nordic-nrf-twim"><code>nordic,nrf-twim</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>Nordic芯片间音频接口（I2S / Inter-IC Sound Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L502">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P010_nordic_nrf-i2s.md#std-dtcompatible-nordic-nrf-i2s"><code>nordic,nrf-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">工业输入输出（IIO）</td>
<td>板载（On-Board）</td>
<td>分压器（Voltage Divider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L69">已启用：1</a>）</td>
<td><a href="../auxdisplay_iio_tach_binding_reference/P012_voltage-divider.md#std-dtcompatible-voltage-divider"><code>voltage-divider</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L58">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L38">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>Nordic工厂信息配置寄存器（FICR / Factory Information Configuration Registers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L50">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P018_nordic_nrf-ficr.md#std-dtcompatible-nordic-nrf-ficr"><code>nordic,nrf-ficr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Nordic nRF系列可编程外设互连（PPI / Programmable Peripheral Interconnect）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L446">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P020_nordic_nrf-ppi.md#std-dtcompatible-nordic-nrf-ppi"><code>nordic,nrf-ppi</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L436">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">网络（Networking）</td>
<td>片上（On-Chip）</td>
<td>Nordic nRF系列无线电（RADIO）外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L127">已启用：1</a>）</td>
<td><a href="../network_radio_frontend_binding_reference/P009_nordic_nrf-radio.md#std-dtcompatible-nordic-nrf-radio"><code>nordic,nrf-radio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Nordic nRF系列近场通信标签（NFCT / Near Field Communication Tag）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L224">已启用：1</a>）</td>
<td><a href="../network_radio_frontend_binding_reference/P008_nordic_nrf-nfct.md#std-dtcompatible-nordic-nrf-nfct"><code>nordic,nrf-nfct</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Nordic nRF系列引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P009_nordic_nrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl"><code>nordic,nrf-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>Nordic nRF电源控制（Power Control）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L89">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P008_nordic_nrf-power.md#std-dtcompatible-nordic-nrf-power"><code>nordic,nrf-power</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>nRF脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L414">已禁用：3</a>）</td>
<td><a href="../pwm_intel_microchip_nxp_binding_reference/P015_nordic_nrf-pwm.md#std-dtcompatible-nordic-nrf-pwm"><code>nordic,nrf-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>nRFx软件脉宽调制（S/W PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L39">已禁用：1</a>）</td>
<td><a href="../pwm_intel_microchip_nxp_binding_reference/P016_nordic_nrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm"><code>nordic,nrf-sw-pwm</code></a></td>
</tr>
<tr>
<td rowspan="2">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>Nordic nRF5X稳压器（Regulator，内核供电的固定级）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L113">已启用：1</a>）</td>
<td><a href="../hardware/P643_nRF5X稳压器绑定.md#dtbinding-nordic-nrf5x-regulator"><code>nordic,nrf5x-regulator</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>固定电压稳压器（Fixed Voltage Regulators）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L77">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L91">已禁用：3</a>）</td>
<td><a href="../hardware/P635_固定稳压器设备树绑定.md#dtbinding-regulator-fixed"><code>regulator-fixed</code></a></td>
</tr>
<tr>
<td rowspan="1">保持存储器（Retained Memory）</td>
<td>片上（On-Chip）</td>
<td>Nordic通用保持寄存器（GPREGRET / General Purpose Register Retention）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L97">已启用：2</a>）</td>
<td><a href="../hardware/P627_Nordic通用保留寄存器绑定.md#dtbinding-nordic-nrf-gpregret"><code>nordic,nrf-gpregret</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Nordic nRF系列随机数发生器（RNG / Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L295">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P014_nordic_nrf-rng.md#std-dtcompatible-nordic-nrf-rng"><code>nordic,nrf-rng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Nordic nRF实时时间计数器（RTC / Real-Time Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L278">已禁用：3</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P010_nordic_nrf-rtc.md#std-dtcompatible-nordic-nrf-rtc"><code>nordic,nrf-rtc</code></a></td>
</tr>
<tr>
<td rowspan="6">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>STMicroelectronics LPS22HB 压力传感器（Pressure Sensor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L158">已启用：1</a>）</td>
<td><a href="../sensor_st_lis_lps_binding_reference/P021_st_lps22hb-press.md#std-dtcompatible-st-lps22hb-press"><code>st,lps22hb-press</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>I2C 总线上的 STMicroelectronics HTS221 温湿度传感器（Humidity and Temperature Sensor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L164">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P069_st_hts221.md#std-dtcompatible-st-hts221"><code>st,hts221</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>CCS811数字空气质量传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L171">已启用：1</a>）</td>
<td><a href="../sensor_ams_aosong_bosch_binding_reference/P001_ams_ccs811.md#std-dtcompatible-ams-ccs811"><code>ams,ccs811</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>意法半导体（STMicroelectronics）LIS2DH12三轴加速度计（3-axis Accelerometer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/thingy52/thingy52_nrf52832.dts?plain=1#L189">已启用：1</a>）</td>
<td><a href="../sensor_st_lis_lps_binding_reference/P003_st_lis2dh12-i2c.md#std-dtcompatible-st-lis2dh12"><code>st,lis2dh12</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Nordic nRF系列温度（TEMP）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L288">已启用：1</a>）</td>
<td><a href="../sensor_microchip_nordic_nxp_binding_reference/P023_nordic_nrf-temp.md#std-dtcompatible-nordic-nrf-temp"><code>nordic,nrf-temp</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Nordic nRF正交解码器（QDEC / Quadrature Decoder）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L334">已禁用：1</a>）</td>
<td><a href="../sensor_microchip_nordic_nxp_binding_reference/P021_nordic_nrf-qdec.md#std-dtcompatible-nordic-nrf-qdec"><code>nordic,nrf-qdec</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Nordic nRF系列UARTE（带EasyDMA的UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L143">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P004_nordic_nrf-uarte.md#std-dtcompatible-nordic-nrf-uarte"><code>nordic,nrf-uarte</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Nordic nRF系列串行外设接口（SPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L170">已禁用：3</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P012_nordic_nrf-spi.md#std-dtcompatible-nordic-nrf-spi"><code>nordic,nrf-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已禁用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Nordic nRF系列看门狗定时器（WDT / Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf52832.dtsi?plain=1#L317">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P002_nordic_nrf-wdt.md#std-dtcompatible-nordic-nrf-wdt"><code>nordic,nrf-wdt</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="lightwell-rgb-led"></a>

#### 导光结构RGB LED（Lightwell RGB LED）

LED由SX1509B GPIO扩展器芯片驱动，设备名称为GPIO_P0。

<table>
<tr>
<th>GPIO扩展器引脚（Pin）</th>
<th>LED通道（Channel）</th>
</tr>
<tr>
<td>5</td>
<td>绿色（Green）</td>
</tr>
<tr>
<td>6</td>
<td>蓝色（Blue）</td>
</tr>
<tr>
<td>7</td>
<td>红色（Red）</td>
</tr>
</table>

<a id="button"></a>

#### 按键（Button）

Thingy:52的按键连接到SoC的P0.11 GPIO。

<a id="serial"></a>

#### 串行接口（Serial）

系统UART默认引脚配置如下：

<table>
<tr>
<th>SoC引脚（Pin）</th>
<th>信号（Signal）</th>
</tr>
<tr>
<td>P0.02</td>
<td>发送（TX）</td>
</tr>
<tr>
<td>P0.03</td>
<td>接收（RX）</td>
</tr>
</table>

这些引脚位于P4及P6连接器上，系统UART控制台默认使用它们。

<a id="internal-i2c-bus"></a>

#### 内部I2C总线（Internal I2C Bus）

内部I2C总线I2C_0没有引出到外部连接器，但大多数板载器件通过它访问。总线分配了以下引脚：

<table>
<tr>
<th>SoC引脚（Pin）</th>
<th>信号（Signal）</th>
</tr>
<tr>
<td>P0.07</td>
<td>串行数据线（SDA）</td>
</tr>
<tr>
<td>P0.08</td>
<td>串行时钟线（SCL）</td>
</tr>
</table>

总线连接以下器件。

<table>
<tr>
<th>器件（Device）</th>
<th>地址（Address）</th>
</tr>
<tr>
<td>SX1509B</td>
<td>0x3e</td>
</tr>
<tr>
<td>LPS22HB</td>
<td>0x5c</td>
</tr>
<tr>
<td>HTS221</td>
<td>0x5f</td>
</tr>
<tr>
<td>CCS811</td>
<td>0x5a</td>
</tr>
</table>

<a id="external-i2c-bus"></a>

#### 外部I2C总线（External I2C Bus）

外部I2C总线I2C_1位于P4排针及P5、P7连接器。

<table>
<tr>
<th>SoC引脚（Pin）</th>
<th>信号（Signal）</th>
</tr>
<tr>
<td>P0.14</td>
<td>SDA_EXT</td>
</tr>
<tr>
<td>P0.15</td>
<td>SCL_EXT</td>
</tr>
</table>

<a id="pin-header"></a>

#### 引脚排针（Pin Header）

以下为P4排针的引脚分配。它引出部分SoC GPIO及I2C GPIO扩展器引脚，还允许外部设备连接板上的4个N沟道MOSFET。

<table>
<tr>
<th>引脚（Pin）</th>
<th>器件（Device）</th>
<th>信号／器件引脚（Signal / Device Pin）</th>
</tr>
<tr>
<td>1</td>
<td>片上系统（SoC）</td>
<td>SCL_EXT／P0.15</td>
</tr>
<tr>
<td>2</td>
<td>片上系统（SoC）</td>
<td>SDA_EXT／P0.14</td>
</tr>
<tr>
<td>3</td>
<td>片上系统（SoC）</td>
<td>ANA/DIG0／P0.02</td>
</tr>
<tr>
<td>4</td>
<td>片上系统（SoC）</td>
<td>ANA/DIG1／P0.03</td>
</tr>
<tr>
<td>5</td>
<td>片上系统（SoC）</td>
<td>ANA/DIG2／P0.04</td>
</tr>
<tr>
<td>6</td>
<td></td>
<td>地（GND）</td>
</tr>
<tr>
<td>7</td>
<td>GPIO扩展器（Expander）</td>
<td>引脚0（Pin 0）</td>
</tr>
<tr>
<td>8</td>
<td>GPIO扩展器（Expander）</td>
<td>引脚1（Pin 1）</td>
</tr>
<tr>
<td>9</td>
<td>GPIO扩展器（Expander）</td>
<td>引脚2（Pin 2）</td>
</tr>
<tr>
<td>10</td>
<td>GPIO扩展器（Expander）</td>
<td>引脚3（Pin 3）</td>
</tr>
<tr>
<td>11</td>
<td>MOSFET 1</td>
<td>漏极（Drain）</td>
</tr>
<tr>
<td>12</td>
<td>MOSFET 1</td>
<td>源极（Source）</td>
</tr>
<tr>
<td>13</td>
<td>MOSFET 2</td>
<td>漏极（Drain）</td>
</tr>
<tr>
<td>14</td>
<td>MOSFET 2</td>
<td>源极（Source）</td>
</tr>
<tr>
<td>15</td>
<td>MOSFET 3</td>
<td>漏极（Drain）</td>
</tr>
<tr>
<td>16</td>
<td>MOSFET 3</td>
<td>源极（Source）</td>
</tr>
<tr>
<td>17</td>
<td>MOSFET 4</td>
<td>漏极（Drain）</td>
</tr>
<tr>
<td>18</td>
<td>MOSFET 4</td>
<td>源极（Source）</td>
</tr>
<tr>
<td>19</td>
<td></td>
<td>电源（VDD）</td>
</tr>
<tr>
<td>20</td>
<td></td>
<td>地（GND）</td>
</tr>
</table>

<a id="mosfets"></a>

##### 金属氧化物半导体场效应晶体管（MOSFETs）

MOSFET连接以下SoC GPIO引脚：

<table>
<tr>
<th>器件（Device）</th>
<th>栅极引脚（Gate Pin）</th>
</tr>
<tr>
<td>MOSFET 1</td>
<td>P0.18</td>
</tr>
<tr>
<td>MOSFET 2</td>
<td>P0.19</td>
</tr>
<tr>
<td>MOSFET 3</td>
<td>P0.20</td>
</tr>
<tr>
<td>MOSFET 4</td>
<td>P0.21</td>
</tr>
</table>

<a id="power-rails"></a>

#### 电源轨（Power Rails）

Thingy:52具有多路电源轨，此处列出当前受支持器件所需的电源轨。原文将产品名写为Thing:52。

<table>
<tr>
<th>名称（Name）</th>
<th>派生来源（Derived From）</th>
<th>控制来源（Controlled By）</th>
</tr>
<tr>
<td>VREG</td>
<td>电池（Battery）</td>
<td>始终开启（Always On）</td>
</tr>
<tr>
<td>VDD_nRF</td>
<td>VREG</td>
<td>始终开启（Always On）</td>
</tr>
<tr>
<td>电源（VDD）</td>
<td>VREG</td>
<td>SoC引脚P0.30</td>
</tr>
<tr>
<td>VDD_CCS</td>
<td>电源（VDD）</td>
<td>GPIO扩展器引脚10</td>
</tr>
</table>

电源轨存在依赖关系，开启某个器件可能需要同时开启多路电源；上电顺序应沿依赖链依次进行。例如，为CCS811气体传感器供电时，先开启VDD，再开启VDD_CCS。器件及其电源轨列表如下：

<table>
<tr>
<th>器件（Device）</th>
<th>电源轨（Rail）</th>
</tr>
<tr>
<td>nRF52832</td>
<td>VDD_nRF</td>
</tr>
<tr>
<td>SX1509B</td>
<td>电源（VDD）</td>
</tr>
<tr>
<td>LPS22HB</td>
<td>电源（VDD）</td>
</tr>
<tr>
<td>HTS221</td>
<td>电源（VDD）</td>
</tr>
<tr>
<td>CCS811</td>
<td>VDD_CCS</td>
</tr>
</table>

<a id="sensors"></a>

#### 传感器（Sensors）

<table>
<tr>
<th>器件（Device）</th>
<th>功能（Function）</th>
<th>总线（Bus）</th>
<th>I2C地址（Address）</th>
<th>电源轨（Power Rail）</th>
</tr>
<tr>
<td>LPS22HB</td>
<td>压力及温度传感器</td>
<td>I2C_0</td>
<td>0x5c</td>
<td>电源（VDD）</td>
</tr>
<tr>
<td>HTS221</td>
<td>湿度及温度传感器</td>
<td>I2C_0</td>
<td>0x5f</td>
<td>电源（VDD）</td>
</tr>
<tr>
<td>CCS811</td>
<td>气体传感器（Gas Sensor）</td>
<td>I2C_0</td>
<td>0x5a</td>
<td>VDD_CCS</td>
</tr>
</table>

<a id="misc-device-pins"></a>

#### 其他器件引脚（Misc. Device Pins）

<a id="sx1509b"></a>

##### SX1509B

<table>
<tr>
<th>器件信号（Device Signal）</th>
<th>SoC引脚（Pin）</th>
</tr>
<tr>
<td>SX_OSCIO</td>
<td>P0.05</td>
</tr>
<tr>
<td>SX_RESET</td>
<td>P0.16</td>
</tr>
</table>

<a id="lps22hb"></a>

##### LPS22HB

<table>
<tr>
<th>传感器信号（Sensor Signal）</th>
<th>SoC引脚（Pin）</th>
</tr>
<tr>
<td>LPS_INT</td>
<td>P0.23</td>
</tr>
</table>

<a id="hts221"></a>

##### HTS221

<table>
<tr>
<th>传感器信号（Sensor Signal）</th>
<th>SoC引脚（Pin）</th>
</tr>
<tr>
<td>HTS_INT</td>
<td>P0.24</td>
</tr>
</table>

<a id="ccs811"></a>

##### CCS811

<table>
<tr>
<th>传感器信号（Sensor Signal）</th>
<th>GPIO扩展器引脚（Pin）</th>
</tr>
<tr>
<td>CCS_RESET</td>
<td>11</td>
</tr>
<tr>
<td>CCS_WAKE</td>
<td>12</td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`thingy52`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>nrfjprog</td>
<td>✅</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><code>nrfutil</code></td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
</table>

<a id="flashing"></a>

### 烧录（Flashing）

向Thingy:52烧录Zephyr需要外部J-Link编程器，连接P9编程排针。

<a id="debugging"></a>

### 调试（Debugging）

Thingy:52不像部分nRF5开发板那样带板载J-Link调试芯片，但[Nordic nRF5x Segger J-Link](../debugging/P005_Nordic_Segger_JLink.md#nordic-segger)页面说明仍适用，只需额外连接外部调试器。[nRF52 DK](P008_nRF52_DK.md#nrf52dk)等带Debug Out连接器的开发板可用作Thingy:52调试器。

<a id="testing-board-features"></a>

## 测试开发板功能（Board Features）

可用[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)示例测试绿色导光LED（Lightwell LED）。

```text
# From the root of the zephyr repository
west build -b thingy52/nrf52832 samples/basic/blinky
west flash
```

也可用[HTS221温湿度监测（Temperature and Humidity Monitor）](../sensors/P029_HTS221温湿度传感器示例.md#hts221)示例测试温湿度传感器。

```text
# From the root of the zephyr repository
west build -b thingy52/nrf52832 samples/sensor/hts221
west flash
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.nordicsemi.com/Software-and-Tools/Development-Kits/Nordic-Thingy-52](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/Nordic-Thingy-52)

<a id="id4"></a>

〔[2](#id5)〕 [https://docs.nordicsemi.com/bundle/ug_thingy52/page/UG/thingy52/intro/frontpage.html](https://docs.nordicsemi.com/bundle/ug_thingy52/page/UG/thingy52/intro/frontpage.html)

## 译注

原文明确Nordic已停止支持Thingy:52，不建议用于新原型。原文更多信息链接指向nRF52 DK，产品名一处写Thing:52，均保留说明。多路电源需按依赖顺序开启；烧录需要外部J-Link。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [frontpage.html](https://docs.nordicsemi.com/bundle/ug_thingy52/page/UG/thingy52/intro/frontpage.html)：HTTP Error 403: Forbidden。
- [Nordic-Thingy-52](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/Nordic-Thingy-52)：HTTP Error 403: Forbidden。

---

[上一章](P022_nRF93M1_DK.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P024_Thingy_53.md)
