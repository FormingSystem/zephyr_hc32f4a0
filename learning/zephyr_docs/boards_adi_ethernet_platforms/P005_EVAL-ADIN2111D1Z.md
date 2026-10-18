---
id: learning.zephyr-docs.boards-adi-ethernet-platforms.page-5
title: EVAL-ADIN2111D1Z
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/adi/eval_adin2111d1z/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adi_eval_adin2111d1z"></a>

# 第5章\_EVAL-ADIN2111D1Z

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/adi/eval_adin2111d1z/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/adi_eval_adin2111d1z.webp](images/adi_eval_adin2111d1z.webp)](images/adi_eval_adin2111d1z.webp)

EVAL-ADIN2111D1Z

名称（Name）：

`adi_eval_adin2111d1z`

厂商（Vendor）：

[Analog Devices, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=adi)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[max32690](https://docs.zephyrproject.org/latest/boards/index.html#soc=max32690)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/eval_adin2111d1z/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

EVAL-ADIN2111D1Z是一块4.5 × 6.5 cm的小型开发板，配有ADIN2111和MAX32690微控制器。它提供两个10BASE-T1L端口，可作为电源与数据菊花链配置（Daisy-chain Configuration）中的评估节点（Evaluation Node）。开发板可以连接模拟或数字传感器。掉电时，数据会转发到链中的另一个节点／开发板。该设计的目的并非构建供电节点（Power Node），而是展示菊花链连接，以及通过板载继电器（Relay）旁路传输数据（Bypassing Data）。

<a id="use-cases"></a>

## 使用场景（Use-Cases）


- 在房间或建筑物内，使用10BASE-T1L以菊花链方式连接温度、压力、光照、接近等传感器
- 通过若干块（原文数量为“?”）开发板以菊花链方式传递电源
- 通过若干块（原文数量为“?”）开发板以菊花链方式传递数据
- 读取板载ADT75温度传感器的数据
- 展示经过多个节点的10BASE-T1L通信
- 使用MAX32690通过SPI接口控制ADIN2111

<a id="hardware"></a>

## 硬件（Hardware）

<table>
<tr>
<th>组件（Component）</th>
<th>功能（Function）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td>ADIN2111</td>
<td>双端口10BASE-T1L交换机（Switch）</td>
<td>集成10BASE-T1L PHY的双端口工业以太网交换机（Industrial Ethernet Switch）。超低功耗，支持多种路由配置（Routing Configurations），通过SPI与微控制器（uC）通信。</td>
</tr>
<tr>
<td>MAX32690（68引脚TQFN-EP封装）</td>
<td>ARM M4微控制器（uC / Microcontroller）</td>
<td>广泛用于ADI产品；时钟频率120 MHz，3 MB闪存（Flash）、1 MB SRAM、12位ADC、Bluetooth LE 5.2；提供安全选项（Security Options）和引导加载程序（Bootloader）。接口包括：2路I2C、I2S、SPI、2路UART、单总线主机（OWM）和USB。</td>
</tr>
<tr>
<td>MAX17640</td>
<td>转换为3.3 V的直流转换器（DC/DC Converter）</td>
<td>输入+4.5 V至+70 V；输出400 mA @3.3 V。温度范围−40 °C至+150 °C。</td>
</tr>
<tr>
<td>MAX77324</td>
<td>转换为1.8 V的直流转换器（DC/DC Converter）</td>
<td>输入来自MAX17640，输出1500 mA @1.8 V。提供ADIN2111和微控制器的VDDIO，并为其他器件供电。</td>
</tr>
<tr>
<td>MAX77324</td>
<td>转换为1.1 V的直流转换器（DC/DC Converter）</td>
<td>输入来自MAX17640，输出1500 mA @1.1 V。为微控制器和ADIN2111供电。</td>
</tr>
<tr>
<td>Microchip AT24C64D电可擦除可编程只读存储器（EEPROM）</td>
<td>通过I2C连接微控制器的EEPROM存储器</td>
<td>64 Kbit（8192 × 8），400 kHz快速模式（Fast Mode）</td>
</tr>
<tr>
<td>极性校正（Polarity Correction），Bourns CD-HD201</td>
<td>桥式整流器（Bridge Rectifier）</td>
<td>VRRM 100 V，IFSM 50 A；IF(AV) 2 A；VF(MAX) 0.85 A（单位依原文保留）。</td>
</tr>
<tr>
<td>继电器（Relay），TE IM21GR</td>
<td>掉电时旁路传输数据（Bypasses Data）</td>
<td>VCOIL 3 VDC，RCOIL 180 Ω；PCOIL 50 mW；超高灵敏度（Ultra Highly Sensitive）。VSWITCH(MAX) 220 VDC，ASWITCH(MAX) 2 A。</td>
</tr>
<tr>
<td>变压器（Transformers），TDK ICI70CGI</td>
<td>确保掉电时呈高阻抗（High Impedance）</td>
<td>LR 2.2 mH。数据和信号线路扼流圈（Chokes），无中心抽头（Central Tap）。</td>
</tr>
<tr>
<td>功率电感（Power Inductors），Coilcraft MSD7342</td>
<td>电源菊花链（Power Daisy-chain）</td>
<td>L 47 μH；DCR(MAX) 0.42 Ω；SRF 9.5 MHz；ISAT（下降20% / 20% Drop）1.3 A；IRMS（双路／单路 / Both/One）= 0.61 / 0.86 A。</td>
</tr>
<tr>
<td>USB-C / JTAG</td>
<td>用户／开发者接口（User / Developer Interfaces）</td>
<td></td>
</tr>
<tr>
<td>FTDI芯片（FT230XQ-R）</td>
<td>允许终端（Terminal）连接到微控制器</td>
<td>USB到串行UART接口（USB to Serial UART Interface）。</td>
</tr>
<tr>
<td>ADT75温度传感器（Temperature Sensor）</td>
<td>温度传感器（Temperature Sensor）。</td>
<td>范围−25 °C至+100 °C，精度±2 °C。功耗79 μW @3.3 V。</td>
</tr>
<tr>
<td>Pmod扩展接口（PMOD）</td>
<td>供外部传感器使用的UART/SPI/I2C连接、单总线主机（OWM / 1-Wire）和一路ADC输入</td>
<td>12针母座（Female Connector）。与ADC_0和ADC_TRIG共用引脚；提供OWM（1-Wire）连接。</td>
</tr>
<tr>
<td>6针排针（Header）</td>
<td>ADIN2111的SPI引脚</td>
<td>仅用于测试（Testing）</td>
</tr>
<tr>
<td>低功耗蓝牙天线（BLE Antenna），Kyocera M310220</td>
<td>2.4 GHz板载天线（On-board Antenna）</td>
<td>频率范围2400–2485 MHz；G(PEAK) 1.7 dBi；线性极化（Linearly Polarized）。</td>
</tr>
<tr>
<td>端口1/2（Port 1/2）</td>
<td>10BASE-T1L端口与直流电源（DC Power）</td>
<td>两个3针Phoenix插拔式螺钉接线端子（Plug-in Screw-terminal Connectors）</td>
</tr>
<tr>
<td>外部电源（Ext. Power）</td>
<td>外部电源，不注入T1L线路（External Power）</td>
<td>2针Phoenix插拔式螺钉接线端子（Plug-in Screw-terminal Connector）</td>
</tr>
</table>

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`adi_eval_adin2111d1z`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="adi_eval_adin2111d1z-hw-features"></a>

<a id="adi_eval_adin2111d1z-adi_eval_adin2111d1z/max32690/m4-hw-features-section"></a>

#### `adi_eval_adin2111d1z/max32690/m4`目标（Target）

<a id="adi_eval_adin2111d1z-adi_eval_adin2111d1z/max32690/m4-hw-features-panel"></a>

<a id="adi_eval_adin2111d1z-adi_eval_adin2111d1z/max32690/m4-hw-features-memory"></a>

该开发板目标的片上存储容量：128 KiB RAM、3 MiB Flash。

<a id="adi_eval_adin2111d1z-adi_eval_adin2111d1z/max32690/m4-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MAX32 RV32内核（Core）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P002_adi_max32-rv32.md#std-dtcompatible-adi-max32-rv32"><code>adi,max32-rv32</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32逐次逼近模数转换器（SAR ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L241">已禁用：1</a>）</td>
<td><a href="../hardware/P863_ADIMAX32逐次逼近ADC绑定.md#dtbinding-adi-max32-adc-sar"><code>adi,max32-adc-sar</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32控制器局域网（CAN）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32690.dtsi?plain=1#L203">已禁用：2</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P001_adi_max32-can.md#std-dtcompatible-adi-max32-can"><code>adi,max32-can</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L64">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L71">已禁用：6</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MAX32全局控制（Global Control）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L130">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P004_adi_max32-gcr.md#std-dtcompatible-adi-max32-gcr"><code>adi,max32-gcr</code></a></td>
</tr>
<tr>
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32计数器（Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L260">已禁用：6</a>）</td>
<td><a href="../counter_binding_reference/P001_adi_max32-counter.md#std-dtcompatible-adi-max32-counter"><code>adi,max32-counter</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ADI MAX32兼容实时时钟计数器（Counter RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L332">已禁用：1</a>）</td>
<td><a href="../counter_binding_reference/P002_adi_max32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter"><code>adi,max32-rtc-counter</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ADI MAX32唤醒定时器（Wake-Up Timer）是一个特殊的32位定时器实例，能够从睡眠（Sleep）、待机（Standby）和备份（Backup）模式唤醒设备。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32690.dtsi?plain=1#L234">已禁用：2</a>）</td>
<td><a href="../counter_binding_reference/P003_adi_max32-wut.md#std-dtcompatible-adi-max32-wut"><code>adi,max32-wut</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32直接存储器访问（DMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32690.dtsi?plain=1#L150">已禁用：1</a>）</td>
<td><a href="../dma_binding_reference/P002_adi_max32-dma.md#std-dtcompatible-adi-max32-dma"><code>adi,max32-dma</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>带SPI接口的ADIN2111独立10BASE-T1L以太网控制器（Ethernet Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin2111d1z/adi_eval_adin2111d1z_max32690_m4.dts?plain=1#L137">已启用：1</a>）</td>
<td><a href="../ethernet_mac_mdio_binding_reference/P003_adi_adin2111.md#std-dtcompatible-adi-adin2111"><code>adi,adin2111</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ADIN2111管理数据输入输出（MDIO）驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin2111d1z/adi_eval_adin2111d1z_max32690_m4.dts?plain=1#L156">已启用：1</a>）</td>
<td><a href="../ethernet_mac_mdio_binding_reference/P015_adi_adin2111-mdio.md#std-dtcompatible-adi-adin2111-mdio"><code>adi,adin2111-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ADIN2111物理层（PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin2111d1z/adi_eval_adin2111d1z_max32690_m4.dts?plain=1#L162">已启用：2</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P016_adi_adin2111-phy.md#std-dtcompatible-adi-adin2111-phy"><code>adi,adin2111-phy</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>MAX32XXX闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L111">已启用：2</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P001_adi_max32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller"><code>adi,max32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>MAX32通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L175">已启用：5</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P011_adi_max32-gpio.md#std-dtcompatible-adi-max32-gpio"><code>adi,max32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32 I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L139">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L149">已禁用：2</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P001_adi_max32-i2c.md#std-dtcompatible-adi-max32-i2c"><code>adi,max32-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>Analog Devices MAX32系列I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32690.dtsi?plain=1#L217">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P001_adi_max32-i2s.md#std-dtcompatible-adi-max32-i2s"><code>adi,max32-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin2111d1z/adi_eval_adin2111d1z_max32690_m4.dts?plain=1#L52">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin2111d1z/adi_eval_adin2111d1z_max32690_m4.dts?plain=1#L33">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32 SEMA邮箱（Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L194">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P032_ADI硬件信号量邮箱绑定.md#dtbinding-adi-mbox-max32-sema"><code>adi,mbox-max32-sema</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>MAX32 HyperBus存储器控制器接口（HPB / HyperBus Memory Controller Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32690-m4.dtsi?plain=1#L66">已禁用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P002_adi_max32-hpb.md#std-dtcompatible-adi-max32-hpb"><code>adi,max32-hpb</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L119">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>MAX32引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L169">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P001_adi_max32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl"><code>adi,max32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L265">已禁用：4</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P003_adi_max32-pwm.md#std-dtcompatible-adi-max32-pwm"><code>adi,max32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">四线串行外设接口（QSPI）</td>
<td>片上（On-Chip）</td>
<td>MAX32 SPIXF设备表示（Device Representation）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32690-m4.dtsi?plain=1#L53">已禁用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P003_adi_max32-spixf.md#std-dtcompatible-adi-max32-spixf"><code>adi,max32-spixf</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>板载（On-Board）</td>
<td>固定电压稳压器（Fixed Voltage Regulators）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/eval_adin2111d1z/adi_eval_adin2111d1z_max32690_m4.dts?plain=1#L26">已启用：1</a>）</td>
<td><a href="../hardware/P635_固定稳压器设备树绑定.md#dtbinding-regulator-fixed"><code>regulator-fixed</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32XXX真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L226">已禁用：1</a>）</td>
<td><a href="../rng_binding_reference/P001_adi_max32-trng.md#std-dtcompatible-adi-max32-trng"><code>adi,max32-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>MAX32通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L202">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L210">已禁用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P001_adi_max32-uart.md#std-dtcompatible-adi-max32-uart"><code>adi,max32-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32690.dtsi?plain=1#L115">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32690.dtsi?plain=1#L124">已禁用：4</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P001_adi_max32-spi.md#std-dtcompatible-adi-max32-spi"><code>adi,max32-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32690.dtsi?plain=1#L110">已启用：9</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L252">已禁用：8</a>）</td>
<td><a href="../system_timer_binding_reference/P002_adi_max32-timer.md#std-dtcompatible-adi-max32-timer"><code>adi,max32-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32高速USB（USBHS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32690-m4.dtsi?plain=1#L95">已禁用：1</a>）</td>
<td><a href="../usb_controller_binding_reference/P001_adi_max32-usbhs.md#std-dtcompatible-adi-max32-usbhs"><code>adi,max32-usbhs</code></a></td>
</tr>
<tr>
<td rowspan="1">单线总线（1-Wire）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32xxx微控制器（MCU）的1-Wire单总线主机（Master）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32690.dtsi?plain=1#L196">已禁用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P006_adi_max32-w1.md#std-dtcompatible-adi-max32-w1"><code>adi,max32-w1</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>MAX32XXX看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L233">已禁用：2</a>）</td>
<td><a href="../watchdog_binding_reference/P001_adi_max32-watchdog.md#std-dtcompatible-adi-max32-watchdog"><code>adi,max32-watchdog</code></a></td>
</tr>
</table>

<a id="why-max32690"></a>

### 为什么选择MAX32690？（Why MAX32690?）

ADI MAX32690微控制器是一款ARM Cortex-M4器件，能效高、功耗低，适合电池供电设备。目前这款微控制器（uC）广泛用于ADI产品。它有3 MB内部闪存（Flash Memory），这是承载网页以及存储MAC地址和IP地址所必需且足够的容量。326xx系列的其他微控制器闪存明显更少：32670/1为384 KB，32672为1 MB，并且不支持外部闪存。选择MAX32690的其他原因包括：更多GPIO引脚、可以通过USB接口和USB串口烧录固件（当前尚未实现，属于计划功能）、更多安全选项，以及对蓝牙（Bluetooth）的支持。

此外，这块评估板还具有展示价值：将微控制器、ADIN2111 PHY、ADT75温度传感器，以及MAX17640和MAX77324直流转换器（DC/DC Converters）集中连接在一块板上。

<a id="connectivity"></a>

### 连接能力（Connectivity）


- 两个3针Phoenix接口P1、P2（+、−、EARTH地）：通信幅度支持1 V和2.4 V。
- USB-C接口P4通过FTDI芯片与微控制器通信。可以打开终端应用，通过UART读写微控制器。也可能通过UCB-C端口（原文拼写）和引导加载程序（Bootloader）为微控制器烧录新固件。
- JTAG/SWD接口P5将微控制器的串行线调试接口（SWD）引出到接插件。固件开发期间，可使用MAX32625PICO开发板进行下载和调试。
- 蓝牙（Bluetooth）：由MAX32690微控制器及板载集成芯片天线提供蓝牙连接。

<a id="sensors"></a>

### 传感器（Sensors）

<table>
<tr>
<th>模拟（Analog）</th>
<th>类型（Type）</th>
<th>连接器（Connector）</th>
<th>注意（Note）</th>
</tr>
<tr>
<td>数字（Digital）</td>
<td>集成电路间总线（I2C）</td>
<td>PMOD接口P6</td>
<td rowspan="3">全部共用一个PMOD接口，同一时间只能使用一种协议（Protocol）</td>
</tr>
<tr>
<td></td>
<td>串行外设接口（SPI）</td>
<td>PMOD接口P6</td>
</tr>
<tr>
<td></td>
<td>通用异步收发器（UART）</td>
<td>PMOD接口P6</td>
</tr>
<tr>
<td></td>
<td>ADT75</td>
<td>板载（On-board），U5</td>
<td></td>
</tr>
<tr>
<td></td>
<td>单总线主机（OWM / 1-Wire Master）</td>
<td>PMOD接口P6</td>
<td></td>
</tr>
<tr>
<td>模拟（Analog）</td>
<td rowspan="2">模数转换器（ADC）</td>
<td>PMOD接口P6</td>
<td>12位逐次逼近型（SAR）。PMOD仅提供ADC触发（ADC Trigger）和ADC_0输入。</td>
</tr>
<tr>
<td></td>
<td>ADC_1 / ADC_4</td>
<td>板上提供这些引脚的焊接点（Solder Pins），供将来使用</td>
</tr>
</table>

<a id="power"></a>

### 电源（Power）

有三种方式为开发板供电：USB-C、外部2针接口，以及10BASE-T1L 3针接口。

该开发板的目标并非充当供电节点（Power Node），因此通过不同接口提供电源时，行为有所不同。


- USB-C接口P4

  > - 仅供开发板使用，不注入PORT1/2
  > - 为直流转换器（DC/DC）供电，继而以3V3、1V8和1V1为全部电路供电
- 外部2针接口P3（Ext. 2 Pin Connector）

  > - 5V-58VDC
  > - 仅供开发板使用，不注入PORT1/2
  > - 为直流转换器（DC/DC）供电，继而以3V3、1V8和1V1为全部电路供电
- 端口1（PORT 1）

  > - 输入／输出电源（IN/OUT Power）
  > - 7–58 VDC，桥式整流器（Bridge Rectifier）会产生压降
  > - 为开发板供电
  > - 为直流转换器（DC/DC）供电，继而以3V3、1V8和1V1为全部电路供电
  > - 转发到PORT 2，实现电源菊花链（Daisy-chain Power）
- 端口2（PORT 2）

  > - 输入／输出电源（IN/OUT Power）
  > - 7–58 VDC，桥式整流器（Bridge Rectifier）会产生压降
  > - 为开发板供电
  > - 为直流转换器（DC/DC）供电，继而以3V3、1V8和1V1为全部电路供电
  > - 转发到PORT 1，实现电源菊花链（Daisy-chain Power）

<a id="data-power-bypass"></a>

### 数据／电源旁路（Data/Power Bypass）


- 向PORT 1供电

  > - 开发板有电源
  > - 继电器将PORT 1和PORT 2连接到ADIN2111
  > - 电源也会转发到PORT 2
- PORT 1的电源丢失

  > - 开发板没有电源
  > - 继电器断开PORT 1、PORT 2与ADIN2111的连接
  > - 继电器将PORT 1与PORT 2连在一起，以支持菊花链连接，数据由此传到链中的另一个节点
  > - 电源不会转发到PORT 2
- 数据到达PORT 1

  > - 开发板没有电源，除非外部接口或USB-C提供电源
  > - 继电器将PORT 1和PORT 2连接到ADIN2111，两个端口的数据都进入ADIN2111
  > - 变压器确保ADIN2111与线路断开，连接到变压器的线路电阻趋于无穷大。
- 数据到达PORT 1且电源丢失

  > - 继电器将PORT 1与PORT 2连在一起，以菊花链方式传递数据
  > - 继电器将PORT 1和PORT 2连接到ADIN2111
  > - 电源不会以菊花链方式传递
  > - 数据由ADIN2111处理
  > - 开发板没有电源，且外部接口或USB-C也不提供电源
  > - 开发板没有电源，但外部接口或USB-C提供了电源

<a id="relay-functionality"></a>

### 继电器功能（Relay Functionality）


- 继电器由微控制器的GPIO引脚控制，该引脚（引脚13 / P0.23）连接到N沟道场效应晶体管（N-FET）

  > - 配置正确时：
  > - 微控制器有电源 → 继电器有电源 → PORT 1和PORT 2连接到ADIN2111
  > - 微控制器没有电源 → 继电器没有电源 → PORT 1和PORT 2不连接到ADIN2111，而是彼此相连，从而以菊花链方式传递数据
- 装入R41后，将旁路微控制器对继电器的控制：开发板有电源 → 继电器有电源 → PORT 1和PORT 2连接到ADIN2111

  > - 此选项用于硬件（HW）测试和开发板软件（SW）开发的初始阶段。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`adi_eval_adin2111d1z`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>rtt</th>
<th>debugserver</th>
<th>reset</th>
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

## 译注

原文没有确定可级联开发板的数量，使用“number (?)”；桥式整流器的VF(MAX)单位写作A，继电器表中也有“开发板没有电源，但外部接口或USB-C提供电源”等表述。译文逐项保留，不据此推断可承受数量、额定参数或实际继电器状态。原图文件adi_eval_adin2111d1z.webp的官网扩展名和响应类型为WebP，但实际字节为JPEG；两次下载一致，已保留原始文件名和字节，未转换或替换图片。

---

[上一章](P004_EVAL-ADIN1140D1Z.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_EVAL-ADIN2111EVB_Evaluation_board.md)
