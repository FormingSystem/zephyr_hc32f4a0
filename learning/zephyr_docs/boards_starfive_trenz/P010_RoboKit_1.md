---
id: learning.zephyr-docs.boards-starfive-trenz.page-10
title: RoboKit 1
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/tdk/robokit1/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="robokit1"></a>

# 第10章\_RoboKit 1

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/tdk/robokit1/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/tdk_robokit1.jpg](images/tdk_robokit1.jpg)](images/tdk_robokit1.jpg)

RoboKit 1

名称（Name）：

`robokit1`

厂商（Vendor）：

[TDK Corporation.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=tdk)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[same70q21b](https://docs.zephyrproject.org/latest/boards/index.html#soc=same70q21b)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/tdk/robokit1/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

TDK RoboKit1主要面向ROS 2开发，配有多种适用于小型地面机器人的传感器，包括用于飞行时间（Time of Flight，ToF）测量的Chirp传感器，例如超声避障。

开发板将300 MHz Cortex-M7 ATSAME70Q21与多种TDK传感器及机器人接口排针组合。

<a id="hardware"></a>

## 硬件（Hardware）


- ATSAME70Q21 Arm Cortex-M7处理器
- 12 MHz晶体振荡器，原文括注Pres
- 32.768 kHz晶体振荡器（Crystal Oscillator）
- Micro-AB USB设备接口（Device）
- Micro-AB USB调试接口，采用Microchip EDBG，支持CMSIS-DAP、虚拟COM端口及数据传输
- JTAG接口连接器
- 一个复位按键
- 一个红色用户LED
- TDK ICM-42688-P六轴惯性测量单元（IMU），32 kHz
- TDK ICP-10111压力传感器
- TDK负温度系数（NTC）热敏电阻，用于温度测量
- AKM AK09918C磁力计
- 两个TDK HVCi-4223 Cortex-M3专用电机控制器
- 三个TDK ICS-43434立体声麦克风
- 工业双IMU连接器，TDK IIM-46230
- TDK CH101超声测距传感器阵列，9个连接器，随附3个传感器

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`robokit1`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="robokit1-hw-features"></a>

<a id="robokit1-robokit1/same70q21b-hw-features-section"></a>

#### `robokit1/same70q21b`目标（Target）

<a id="robokit1-robokit1/same70q21b-hw-features-panel"></a>

<a id="robokit1-robokit1/same70q21b-hw-features-memory"></a>

该开发板目标的片上存储容量：384 KiB RAM、2 MiB Flash。

<a id="robokit1-robokit1/same70q21b-hw-features-table"></a>

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
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="2">模数转换器（ADC）</td>
<td>板载（On-Board）</td>
<td>德州仪器单通道SPI模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/tdk/robokit1/robokit1-common.dtsi?plain=1#L121">已启用：1</a>）</td>
<td><a href="../hardware/P965_ADS7052模数转换器绑定.md#dtbinding-ti-ads7052"><code>ti,ads7052</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列模拟前端控制器（AFEC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L222">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L311">已禁用：1</a>）</td>
<td><a href="../hardware/P857_AtmelSAM模拟前端ADC绑定.md#dtbinding-atmel-sam-afec"><code>atmel,sam-afec</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM同步串行控制器（SSC / Synchronous Serial Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L58">已禁用：1</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P007_atmel_sam-ssc.md#std-dtcompatible-atmel-sam-ssc"><code>atmel,sam-ssc</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>针对Atmel SAM定制的Bosch m_can CAN灵活数据速率控制器（CAN FD）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L184">已禁用：2</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P002_atmel_sam-can.md#std-dtcompatible-atmel-sam-can"><code>atmel,sam-can</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Atmel电源管理控制器（PMC / Power Management Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L337">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P009_atmel_sam-pmc.md#std-dtcompatible-atmel-sam-pmc"><code>atmel,sam-pmc</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM定时器／计数器（TC / Timer Counter）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L76">已禁用：4</a>）</td>
<td><a href="../counter_binding_reference/P010_atmel_sam-tc.md#std-dtcompatible-atmel-sam-tc"><code>atmel,sam-tc</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列数模转换器（DAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L231">已启用：1</a>）</td>
<td><a href="../hardware/P762_AtmelSAM数模转换器绑定.md#dtbinding-atmel-sam-dac"><code>atmel,sam-dac</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM扩展DMA控制器（XDMAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L328">已启用：1</a>）</td>
<td><a href="../dma_binding_reference/P010_atmel_sam-xdmac.md#std-dtcompatible-atmel-sam-xdmac"><code>atmel,sam-xdmac</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Microchip SAM以太网控制器（Ethernet Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L240">已启用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P019_microchip_sam-ethernet-controller.md#std-dtcompatible-microchip-sam-ethernet-controller"><code>microchip,sam-ethernet-controller</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列千兆媒体访问控制器以太网（GMAC Ethernet）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L245">已禁用：1</a>）</td>
<td><a href="../ethernet_mac_mdio_binding_reference/P004_atmel_sam-gmac.md#std-dtcompatible-atmel-sam-gmac"><code>atmel,sam-gmac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列管理数据输入输出（MDIO）驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L254">已启用：1</a>）</td>
<td><a href="../ethernet_mac_mdio_binding_reference/P016_atmel_sam-mdio.md#std-dtcompatible-atmel-sam-mdio"><code>atmel,sam-mdio</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM增强型嵌入式闪存控制器（EEFC / Enhanced Embedded Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L361">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P006_atmel_sam-flash-controller.md#std-dtcompatible-atmel-sam-flash-controller"><code>atmel,sam-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>SAM通用输入输出端口（GPIO Port）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L387">已启用：5</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P029_atmel_sam-gpio.md#std-dtcompatible-atmel-sam-gpio"><code>atmel,sam-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>ATMEL SAM复位控制器（Reset Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L438">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P001_atmel_sam-rstc.md#std-dtcompatible-atmel-sam-rstc"><code>atmel,sam-rstc</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列高速双线接口（TWIHS / I2C）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L127">已启用：3</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P009_atmel_sam-i2c-twihs.md#std-dtcompatible-atmel-sam-i2c-twihs"><code>atmel,sam-i2c-twihs</code></a></td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/tdk/robokit1/robokit1-common.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>此绑定（Binding）描述Atmel SAM闪存区域布局（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L372">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P009_atmel_sam-flash.md#std-dtcompatible-atmel-sam-flash"><code>atmel,sam-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM引脚控制容器（Pinctrl Container）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L381">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P013_atmel_sam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl"><code>atmel,sam-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM电源控制器（SUPC / Supply Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L445">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P001_atmel_sam-supc.md#std-dtcompatible-atmel-sam-supc"><code>atmel,sam-supc</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L149">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L289">已禁用：1</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P007_atmel_sam-pwm.md#std-dtcompatible-atmel-sam-pwm"><code>atmel,sam-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM随机数发生器（RNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L320">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P004_atmel_sam-trng.md#std-dtcompatible-atmel-sam-trng"><code>atmel,sam-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列实时时钟（RTC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L460">已禁用：1</a>）</td>
<td><a href="../rtc_binding_reference/P004_atmel_sam-rtc.md#std-dtcompatible-atmel-sam-rtc"><code>atmel,sam-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>ATMEL（Microchip）SAM高速多媒体卡接口SD主机控制器（HSMCI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L51">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P003_atmel_sam-hsmci.md#std-dtcompatible-atmel-sam-hsmci"><code>atmel,sam-hsmci</code></a></td>
</tr>
<tr>
<td rowspan="4">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>ICM-42688运动跟踪器件（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/tdk/robokit1/robokit1-common.dtsi?plain=1#L108">已启用：1</a>）</td>
<td><a href="../sensor_espressif_honeywell_invensense_binding_reference/P028_invensense_icm42688.md#std-dtcompatible-invensense-icm42688"><code>invensense,icm42688</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAM定时器／计数器（TC）的正交解码模式（QDEC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L87">已禁用：4</a>）</td>
<td><a href="../sensor_ams_aosong_bosch_binding_reference/P018_atmel_sam-tc-qdec.md#std-dtcompatible-atmel-sam-tc-qdec"><code>atmel,sam-tc-qdec</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>旭化成AKM09918C磁力计；绑定名称按原文保留（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/tdk/robokit1/robokit1-common.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../sensor_ams_aosong_bosch_binding_reference/P017_asahi-kasei_akm09918c.md#std-dtcompatible-asahi-kasei-akm09918c"><code>asahi-kasei,akm09918c</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>EPCOS B57861S0103A039热敏电阻（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/tdk/robokit1/robokit1-common.dtsi?plain=1#L50">已启用：1</a>）</td>
<td><a href="../sensor_bosch_broadcom_espressif_binding_reference/P029_epcos_b57861s0103a039.md#std-dtcompatible-epcos-b57861s0103a039"><code>epcos,b57861s0103a039</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L176">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L160">已禁用：2</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P011_atmel_sam-usart.md#std-dtcompatible-atmel-sam-usart"><code>atmel,sam-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SAM系列通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L345">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L477">已禁用：2</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P010_atmel_sam-uart.md#std-dtcompatible-atmel-sam-uart"><code>atmel,sam-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L66">已启用：2</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P008_atmel_sam-spi.md#std-dtcompatible-atmel-sam-spi"><code>atmel,sam-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列高速USB（USBHS），设备模式（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L208">已启用：1</a>）</td>
<td><a href="../usb_controller_binding_reference/P005_atmel_sam-usbhs.md#std-dtcompatible-atmel-sam-usbhs"><code>atmel,sam-usbhs</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>ATMEL SAM0看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L452">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P007_atmel_sam-watchdog.md#std-dtcompatible-atmel-sam-watchdog"><code>atmel,sam-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

连接详情见TDK RoboKit硬件指南。

<a id="system-clock"></a>

### 系统时钟（System Clock）

SAM E70 MCU使用板上的12 MHz外部振荡器，经片上PLL生成300 MHz系统时钟。

<a id="serial-port"></a>

### 串口（Serial Port）

ATSAME70Q21具有五路UART及三路USART，其中一路UART配置为控制台，通过USB2连接器以虚拟COM端口提供。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`robokit1`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td></td>
<td>✅</td>
</tr>
</table>

向SAM E70烧录Zephyr需要OpenOCD。原文说明USB0及USB1均连接且板卡已供电时，west flash及west debug应可正常工作。（[OpenOCD工具](http://openocd.org/)）

<a id="flashing"></a>

### 烧录（Flashing）


1. 运行你惯用的终端程序，监听输出。Linux下的终端设备应为`/dev/ttyACM0`，例如：

  ```text
  $ minicom -D /dev/ttyUSB0 -o
  ```

  `-o`选项让`minicom`不发送调制解调器初始化字符串（Modem Initialization String）。连接参数应配置如下：


  - 速率（Speed）：115200波特率
  - 数据位（Data）：8位
  - 奇偶校验（Parity）：无（None）
  - 停止位（Stop Bits）：1位
2. 使用USB1调试端口连接主机、USB2连接串口控制台，剩余Micro-USB用于供电，然后构建并烧录[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)。

  ```text
  # From the root of the zephyr repository
  west build -b robokit1 samples/hello_world
  west flash
  ```

  终端应显示“Hello World! robokit1”。

<a id="debugging"></a>

### 调试（Debugging）

可以按常规方式调试应用。下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b robokit1 samples/hello_world
west debug
```

<a id="references"></a>

## 参考资料（References）

TDK RoboKit1产品页：

[https://invensense.tdk.com/products/robokit1-dk/](https://invensense.tdk.com/products/robokit1-dk/)

## 译注

RoboKit 1搭载SAME70Q21 Cortex-M7。AK09918C与设备绑定中AKM09918C的名称按各自来源保留；原文USB0／USB1供电段与USB1调试／USB2控制台段的端口编号存在差异，不据此假定它们完全等同。

---

[上一章](P009_TDK.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_TECHNEXION.md)
