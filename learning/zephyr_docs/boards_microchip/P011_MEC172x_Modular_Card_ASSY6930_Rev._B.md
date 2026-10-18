---
id: learning.zephyr-docs.boards-microchip.page-11
title: MEC172x Modular Card ASSY6930 Rev. B
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/microchip/mec172xmodular_assy6930/doc/mec172xmodular_assy6930.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mec172xmodular_assy6930"></a>

# 第11章\_MEC172x模块卡ASSY6930，Rev. B（Modular Card）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/microchip/mec172xmodular_assy6930/doc/mec172xmodular_assy6930.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mec172xmodular_assy6930.jpg](images/mec172xmodular_assy6930.jpg)](images/mec172xmodular_assy6930.jpg)

MEC172x模块卡ASSY6930，Rev. B（Modular Card）

名称（Name）：

`mec172xmodular_assy6930`

厂商（Vendor）：

[微芯科技（Microchip Technology Inc.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=microchip)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mec172x_nsz](https://docs.zephyrproject.org/latest/boards/index.html#soc=mec172x_nsz)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/mec172xmodular_assy6930/doc/mec172xmodular_assy6930.rst/../..)<a id="overview"></a>

## 概述（Overview）

MEC172x Modular Card ASSY6930 Rev. B用于评估Microchip MEC172X系列微控制器，可独立运行，也可与符合MECC规范的平台配合。

<a id="hardware"></a>

## 硬件（Hardware）


- MEC172x系列MEC1723、MEC1727及MEC1728 Arm Cortex-M4处理器
- 416 KB RAM及128 KB启动ROM
- 通过Micro-USB连接的UART1
- PECI接口3.0
- FAN、PWM及TACHO引脚
- 5个SMBus实例
- eSPI排针
- VCI接口
- 1个硬件驱动PS/2端口
- 键盘接口排针

<a id="id3"></a>

SoC更多信息见MEC172x参考手册 [注1](#id2)。（[MEC172x参考手册（Reference Manual）](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC172x/MEC172x-Data-Sheet.pdf)）

与MEC172x评估板不同，MEC172x模块卡通过两种方式引出引脚：


1. 独立模式（Standalone Mode），通过排针连接


  - 通用输入输出（GPIOs）
  - JTAG端口
  - eSPI总线
  - I2C0、I2C1及I2C6
  - PWM1、PWM2及PWM3
  - 共享SPI（Shared SPI）
  - 键盘接口（Keyboard Interface）
2. 配合模式（Mated Mode），连接另一块带高密度MECC连接器的平台


  - FAN及PWM8
  - I2C3及I2C7
  - eSPI总线

通过+5 V USB Micro-A连接器或MECC连接器供电。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`mec172xmodular_assy6930`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mec172xmodular_assy6930-hw-features"></a>

<a id="mec172xmodular_assy6930-mec172xmodular_assy6930/mec172x_nsz-hw-features-section"></a>

#### `mec172xmodular_assy6930/mec172x_nsz`目标（Target）

<a id="mec172xmodular_assy6930-mec172xmodular_assy6930/mec172x_nsz-hw-features-panel"></a>

<a id="mec172xmodular_assy6930-mec172xmodular_assy6930/mec172x_nsz-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、352 KiB Flash。

<a id="mec172xmodular_assy6930-mec172xmodular_assy6930/mec172x_nsz-hw-features-table"></a>

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
<td>ARM Cortex-M4 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172xnsz.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P024_arm_cortex-m4.md#std-dtcompatible-arm-cortex-m4"><code>arm,cortex-m4</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L709">已启用：1</a>）</td>
<td><a href="../hardware/P860_MicrochipXEC模数转换器绑定.md#dtbinding-microchip-xec-adc"><code>microchip,xec-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC电源、时钟、复位及VBAT寄存器（PCR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L11">已启用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P021_microchip_xec-pcr.md#std-dtcompatible-microchip-xec-pcr"><code>microchip,xec-pcr</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC对称密码AES／哈希（Hash）加速器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L1084">已禁用：1</a>）</td>
<td><a href="../crypto_aes_sha_ccm_binding_reference/P019_microchip_xec-symcr.md#std-dtcompatible-microchip-xec-symcr"><code>microchip,xec-symcr</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC DMA控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L480">已禁用：1</a>）</td>
<td><a href="../intel_microchip_dma_binding_reference/P016_microchip_xec-dmac.md#std-dtcompatible-microchip-xec-dmac"><code>microchip,xec-dmac</code></a></td>
</tr>
<tr>
<td rowspan="4">增强型串行外设接口（ESPI）</td>
<td>片上（On-Chip）</td>
<td>Microchip eSPI V2控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L884">已启用：1</a>）</td>
<td><a href="../espi_binding_reference/P006_microchip_xec-espi-v2.md#std-dtcompatible-microchip-xec-espi-v2"><code>microchip,xec-espi-v2</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip eSPI TAF第2版控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L915">已禁用：1</a>）</td>
<td><a href="../espi_binding_reference/P004_microchip_xec-espi-saf-v2.md#std-dtcompatible-microchip-xec-espi-saf-v2"><code>microchip,xec-espi-saf-v2</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip XEC eSPI主机设备（Host Devices）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L938">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L928">已禁用：9</a>）</td>
<td><a href="../espi_binding_reference/P003_microchip_xec-espi-host-dev.md#std-dtcompatible-microchip-xec-espi-host-dev"><code>microchip,xec-espi-host-dev</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip XEC eSPI虚拟线（Virtual Wire）路由（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x/mec172x-vw-routing.dtsi?plain=1#L11">已启用：1</a>）</td>
<td><a href="../espi_binding_reference/P007_microchip_xec-espi-vw-routing.md#std-dtcompatible-microchip-xec-espi-vw-routing"><code>microchip,xec-espi-vw-routing</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Microchip CEC／MEC通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L244">已启用：6</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P004_microchip_xec-gpio.md#std-dtcompatible-microchip-xec-gpio"><code>microchip,xec-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Microchip I2C／SMBus V2控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L506">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L542">已禁用：2</a>）</td>
<td><a href="../i2c_infineon_ite_nordic_binding_reference/P013_microchip_xec-i2c-v2.md#std-dtcompatible-microchip-xec-i2c-v2"><code>microchip,xec-i2c-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC键盘矩阵控制器（Keyboard Matrix Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L722">已启用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P007_microchip_xec-kbd.md#std-dtcompatible-microchip-xec-kbd"><code>microchip,xec-kbd</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip XEC系列外部中断聚合控制器（External Interrupt Aggregator Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L31">已启用：1</a>）</td>
<td><a href="../infineon_microchip_interrupt_binding_reference/P010_microchip_xec-ecia.md#std-dtcompatible-microchip-xec-ecia"><code>microchip,xec-ecia</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip XEC系列外部中断聚合GIRQ（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L41">已禁用：19</a>）</td>
<td><a href="../infineon_microchip_interrupt_binding_reference/P009_microchip_xec-ecia-girq.md#std-dtcompatible-microchip-xec-ecia-girq"><code>microchip,xec-ecia-girq</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/mec172xmodular_assy6930/mec172xmodular_assy6930.dts?plain=1#L32">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC系列电池后备RAM（Battery Backed RAM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L466">已启用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P012_microchip_xec-bbram.md#std-dtcompatible-microchip-xec-bbram"><code>microchip,xec-bbram</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>Microchip片上EEPROM（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172xnsz.dtsi?plain=1#L60">已禁用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P005_microchip_xec-eeprom.md#std-dtcompatible-microchip-xec-eeprom"><code>microchip,xec-eeprom</code></a></td>
</tr>
<tr>
<td rowspan="1">平台环境控制接口（PECI）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC平台环境控制接口（PECI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L731">已启用：1</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P004_microchip_xec-peci.md#std-dtcompatible-microchip-xec-peci"><code>microchip,xec-peci</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L238">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P008_microchip_xec-pinctrl.md#std-dtcompatible-microchip-xec-pinctrl"><code>microchip,xec-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">PS/2 接口（PS/2）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC PS/2控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L566">已启用：1</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P012_microchip_xec-ps2.md#std-dtcompatible-microchip-xec-ps2"><code>microchip,xec-ps2</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L577">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L585">已禁用：8</a>）</td>
<td><a href="../pwm_intel_microchip_nxp_binding_reference/P012_microchip_xec-pwm.md#std-dtcompatible-microchip-xec-pwm"><code>microchip,xec-pwm</code></a></td>
</tr>
<tr>
<td rowspan="3">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC基础定时器（Basic Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L322">已禁用：6</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P004_microchip_xec-timer.md#std-dtcompatible-microchip-xec-timer"><code>microchip,xec-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip XEC休眠定时器（Hibernation Timer），位于32 kHz时钟域的16位递减计数定时器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L442">已禁用：2</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P002_microchip_xec-hibtimer.md#std-dtcompatible-microchip-xec-hibtimer"><code>microchip,xec-hibtimer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip XEC实时时钟定时器（RTC Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L1050">已禁用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P003_microchip_xec-rtc.md#std-dtcompatible-microchip-xec-rtc"><code>microchip,xec-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L872">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L860">已禁用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P001_microchip_xec-uart.md#std-dtcompatible-microchip-xec-uart"><code>microchip,xec-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>带本地DMA的Microchip XEC QMSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L741">已启用：1</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P010_microchip_xec-qmspi-ldma.md#std-dtcompatible-microchip-xec-qmspi-ldma"><code>microchip,xec-qmspi-ldma</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172xnsz.dtsi?plain=1#L52">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">转速计（Tachometer）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC转速计控制器（Tachometer Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L649">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L660">已禁用：3</a>）</td>
<td><a href="../auxdisplay_iio_tach_binding_reference/P017_microchip_xec-tach.md#std-dtcompatible-microchip-xec-tach"><code>microchip,xec-tach</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已禁用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip XEC实时操作系统定时器（RTOS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L313">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P004_microchip_xec-rtos-timer.md#std-dtcompatible-microchip-xec-rtos-timer"><code>microchip,xec-rtos-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC看门狗定时器（Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec172x_common.dtsi?plain=1#L305">已启用：1</a>）</td>
<td><a href="../soc_pmic_watchdog_binding_reference/P011_microchip_xec-watchdog.md#std-dtcompatible-microchip-xec-watchdog"><code>microchip,xec-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

此评估板套件由以下硬件模块组成：


- <a id="id5"></a>

  MEC172x Modular ASSY 6930 Rev B1，参见[MEC172x Modular EC Card - Assy_6930 Rev B1p1](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC172x/MEC172X-MECC_Assy_6930_B1p1-SCH.pdf) [注2](#id4)

<a id="system-clock"></a>

### 系统时钟（System Clock）

MEC172x MCU使用96 MHz内部振荡器及片上PLL，最终生成12 MHz EC时钟。详见文末数据手册第4章“4.0 POWER, CLOCKS, and RESETS”中的处理器时钟控制寄存器。

<a id="serial-port"></a>

### 串口（Serial Port）

UART1用于串行日志。

<a id="jumper-settings"></a>

## 跳线设置（Jumper Settings）

按以下跳线设置即可演示此板，高级用户可根据需要采用其他配置。

<a id="jumper-setting-for-mec172x-modular-assy-6930-rev-b1p1"></a>

### MEC172x Modular Assy 6930 Rev B1p1跳线设置

<a id="power-related-jumpers"></a>

#### 电源相关跳线（Power-Related Jumpers）

通过Type-A／B连接器P1供电时，短接JP22的1—2脚；独立模式必须使用此设置。若通过MECC连接器P2供电并连接外部平台，短接JP22的2—3脚。

注意：JP22只需安装一个跳线帽。

将VTR2设为3.3 V时，短接JP26的2—3脚，Windows应用要求此设置。设为1.8 V时，短接JP26的1—2脚，Chrome应用要求此设置。

<a id="boot-rom-straps"></a>

#### 启动ROM配置引脚（Boot-ROM Straps）

此跳线配置MEC172x启动ROM配置引脚。

<table>
<tr>
<th>JP23：UART_BSTRAP</th>
</tr>
<tr>
<td>1-2</td>
</tr>
</table>

JP23的1—2脚短接，将UART_BSTRAP拉到GND。MEC172x启动ROM采样该引脚，低电平时使用UART接口进行危机恢复（Crisis Recovery）。

<a id="boot-source-select"></a>

#### 启动源选择（Boot Source Select）

以下跳线将MEC172x配置为从共享SPI、从端附接闪存（SAF / Slave Attached Flash）或主端附接闪存（MAF / Master Attached Flash）启动。

<table>
<tr>
<th>启动源（Boot Source）</th>
<th>JP25</th>
</tr>
<tr>
<td>共享SPI或SAF</td>
<td>5-6</td>
</tr>
<tr>
<td>MAF</td>
<td>1-2, 4-6</td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`mec172xmodular_assy6930`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
<tr>
<td>dediprog</td>
<td>✅（默认 / default）</td>
<td></td>
</tr>
</table>

<a id="setup"></a>

### 设置（Setup）


1. 若使用Dediprog SF100编程器，先完成其设置。

  <a id="id11"></a>

  Windows版本见[SF100产品页面](https://www.dediprog.com/product/SF100) [注5](#id10)。

  <a id="id9"></a>

  <a id="id13"></a>

  Linux版本源码见[SF100 Linux GitHub](https://github.com/DediProgSW/SF100Linux) [注4](#id8)，按[SF100 Linux手册](https://www.dediprog.com/download/save/727.pdf) [注6](#id12) 完成设置。将SF100Linux目录的60-dediprog.rules复制到原文所列`/etc/udev/rules.s`或`rules.d`目录，然后执行以下命令重启服务：

  ```text
  $ udevadm control --reload
  ```

  将dpcmd所在目录加入PATH；Linux工具名为dpcmd，Windows为dpcmd.exe。
2. <a id="id7"></a>

  克隆[MEC172x SPI Image Gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC172x/SPI_image_gen) [注3](#id6) 仓库，或下载该目录中的文件。
3. 将镜像生成工具加入PATH，使Zephyr能够找到它，例如：

  ```text
  -DMEC172X_SPI_GEN=<path to spi_gen tool>/mec172x_spi_gen_lin_x86_64
  ```

  Linux和Windows工具文件名不同。
4. 默认MEC172X_SPI_CFG为`${BOARD_DIR}/support`中的spi_cfg.txt。同目录还提供4 Mbit的spi_cfg_4MBit.txt及128 Mbit的spi_cfg_128MBit.txt示例。必要时可指定自定义配置覆盖默认值。

  ```text
  -DMEC172X_SPI_CFG=<path to spi_cfg file>/spi_cfg.txt
  ```
5. 为hello_world生成128 Mbit SPI镜像的示例命令：

  ```text
  west build -p auto -b mec172xmodular_assy6930 samples/hello_world -- -DMEC172X_SPI_GEN=$HOME/CPGZephyrDocs/MEC172x/SPI_image_gen/mec172x_spi_gen_lin_x86_64 -DMEC172X_SPI_CFG=$HOME/zephyrproject/zephyr/boards/microchip/mec172xmodular_assy6930/support/spi_cfg_128MBit.txt
  ```

<a id="wiring"></a>

### 接线（Wiring）


1. 将编程器连接到ASSY6930的J2排针，以烧录SPI NOR芯片U2。确认偏移为0x0，可使用Dediprog SF100或类似SPI芯片编程工具。

  <table>
  <tr>
  <th>Dediprog连接器</th>
  <th><code>J2</code></th>
  </tr>
  <tr>
  <td>电源（VCC）</td>
  <td>1</td>
  </tr>
  <tr>
  <td>地（GND）</td>
  <td>2</td>
  </tr>
  <tr>
  <td>片选（CS）</td>
  <td>3</td>
  </tr>
  <tr>
  <td>时钟（CLK）</td>
  <td>4</td>
  </tr>
  <tr>
  <td>主机输入从机输出（MISO）</td>
  <td>6</td>
  </tr>
  <tr>
  <td>主机输出从机输入（MOSI）</td>
  <td>5</td>
  </tr>
  </table>
2. 通过RS232线缆，将mec172xmodular_assy6930 Rev. B的UART1连接主机。
3. 通过Micro-USB线缆供电，并短接JP22的1—2脚选择此供电方式。

<a id="building"></a>

### 构建（Building）


1. 按通常方式构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用。
2. 构建系统能找到镜像生成工具时，会生成spi_image.bin，可用它烧录SPI芯片。

<a id="flashing"></a>

### 烧录（Flashing）


1. 运行惯用的终端程序监听输出。Linux下串口应为`/dev/ttyUSB0`，保持终端打开。

  例如：

  ```text
  $ minicom -D /dev/ttyUSB0 -o
  ```

  `-o`选项让`minicom`不发送调制解调器初始化字符串（Modem Initialization String）。连接参数应配置如下：


  - 速率（Speed）：115200波特率
  - 数据位（Data）：8位
  - 奇偶校验（Parity）：无（None）
  - 停止位（Stop Bits）：1位
2. 在第二个终端中用west烧录开发板，同时并排显示两个终端。

  ```text
  $ west flash
  ```

  注意（Note）

  west进程启动时按住复位键S1，直至整个west过程成功结束后再松开。
3. 第一个终端应显示`Hello World! mec172xmodular_assy6930`。若未显示，可按复位键，随后应出现消息。

<a id="debugging"></a>

### 调试（Debugging）

板载J1排针提供JTAG调试连接。

<a id="troubleshooting"></a>

### 故障排查（Troubleshooting）


1. 若未看到应用运行，确认LED1已亮；若未亮，检查电源跳线。
2. 若Dediprog无法编程此板，可重新插拔P1连接线后重试。
3. 若Dediprog无法检测板载闪存，按住S1复位键后重试。

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC172x/MEC172x-Data-Sheet.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC172x/MEC172x-Data-Sheet.pdf)

<a id="id4"></a>

〔[2](#id5)〕 [https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC172x/MEC172X-MECC_Assy_6930_B1p1-SCH.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC172x/MEC172X-MECC_Assy_6930_B1p1-SCH.pdf)

<a id="id6"></a>

〔[3](#id7)〕 [https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC172x/SPI_image_gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC172x/SPI_image_gen)

<a id="id8"></a>

〔[4](#id9)〕 [https://github.com/DediProgSW/SF100Linux](https://github.com/DediProgSW/SF100Linux)

<a id="id10"></a>

〔[5](#id11)〕 [https://www.dediprog.com/product/SF100](https://www.dediprog.com/product/SF100)

<a id="id12"></a>

〔[6](#id13)〕 [https://www.dediprog.com/download/save/727.pdf](https://www.dediprog.com/download/save/727.pdf)

## 译注

保留Rev. B／B1p1的跳线条件、不同平台的VTR2电平、危机恢复模式（Crisis Recovery）及SPI镜像容量配置，不能直接套用其他MEC板的电源或启动跳线。

---

[上一章](P010_MEC172xEVB_ASSY6906.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P012_MEC17xxEVB_ASSY6941.md)
