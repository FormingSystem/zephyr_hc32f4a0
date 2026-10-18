---
id: learning.zephyr-docs.boards-arm.page-5
title: V2M MPS2
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/arm/mps2/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mps2"></a>

# 第5章\_V2M MPS2

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/arm/mps2/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mps2.jpg](images/mps2.jpg)](images/mps2.jpg)

V2M MPS2

名称（Name）：

`mps2`

厂商（Vendor）：

[Arm公司（ARM Ltd.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=arm)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

`[an521](https://docs.zephyrproject.org/latest/boards/index.html#soc=an521), [an383](https://docs.zephyrproject.org/latest/boards/index.html#soc=an383), [an385](https://docs.zephyrproject.org/latest/boards/index.html#soc=an385), [an500](https://docs.zephyrproject.org/latest/boards/index.html#soc=an500), [an386](https://docs.zephyrproject.org/latest/boards/index.html#soc=an386)`

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arm/mps2/doc/index.rst/../..)MPS2开发板系列包含以下目标，点击链接查看各目标的详细信息。


- [ARM MPS2+ AN521](P006_ARM_MPS2_AN521.md#mps2-an521-board)
- [ARM V2M MPS2 Armv6-m（AN383）](P007_ARM_V2M_MPS2_Armv6-m_AN383.md#mps2-armv6m-board)
- [ARM V2M MPS2 Armv7-m（AN385/AN386/AN500）](P008_ARM_V2M_MPS2_Armv7-m_AN385_AN386_AN500.md#mps2-armv7m-board)

<a id="supported-features"></a>

## 支持的功能（Supported Features）

`mps2`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mps2-hw-features"></a>

<a id="mps2-mps2/an383-hw-features-section"></a>

### `mps2/an383`目标（Target）

<a id="mps2-mps2/an383-hw-features-panel"></a>

<a id="mps2-mps2/an383-hw-features-memory"></a>

该开发板目标的片上存储容量：4 MiB RAM、4 MiB Flash。

<a id="mps2-mps2/an383-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>板载（On-Board）</td>
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an383.dts?plain=1#L26">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>板载（On-Board）</td>
<td>ARM Cortex-M系统设计套件定时器（CMSDK Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L98">已启用：2</a>）</td>
<td><a href="../counter_binding_reference/P007_arm_cmsdk-timer.md#std-dtcompatible-arm-cmsdk-timer"><code>arm,cmsdk-timer</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM CMSDK双定时器（Dual Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L110">已启用：1</a>）</td>
<td><a href="../counter_binding_reference/P006_arm_cmsdk-dtimer.md#std-dtcompatible-arm-cmsdk-dtimer"><code>arm,cmsdk-dtimer</code></a></td>
</tr>
<tr>
<td rowspan="1">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN9220以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L203">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P003_smsc_lan9220.md#std-dtcompatible-smsc-lan9220"><code>smsc,lan9220</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L171">已启用：4</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P027_arm_cmsdk-gpio.md#std-dtcompatible-arm-cmsdk-gpio"><code>arm,cmsdk-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM 32位内存映射输入输出GPIO（MMIO32 GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L248">已启用：3</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P028_arm_mmio32-gpio.md#std-dtcompatible-arm-mmio32-gpio"><code>arm,mmio32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>板载（On-Board）</td>
<td>ARM SBCon双线串行总线接口（Two-Wire Serial Bus Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L212">已启用：4</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P006_arm_versatile-i2c.md#std-dtcompatible-arm-versatile-i2c"><code>arm,versatile-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L40">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L61">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存或其他非易失性存储器的固定分区（Fixed Partitions）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions"><code>fixed-partitions</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>板载（On-Board）</td>
<td>Arm MPS2引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L274">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P008_arm_mps2-pinctrl.md#std-dtcompatible-arm-mps2-pinctrl"><code>arm,mps2-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L116">已启用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P007_arm_cmsdk-uart.md#std-dtcompatible-arm-cmsdk-uart"><code>arm,cmsdk-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L154">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P005_arm_cmsdk-watchdog.md#std-dtcompatible-arm-cmsdk-watchdog"><code>arm,cmsdk-watchdog</code></a></td>
</tr>
</table>

<a id="mps2-mps2/an385-hw-features-section"></a>

### `mps2/an385`目标（Target）

<a id="mps2-mps2/an385-hw-features-panel"></a>

<a id="mps2-mps2/an385-hw-features-memory"></a>

该开发板目标的片上存储容量：4 MiB RAM、4 MiB Flash。

<a id="mps2-mps2/an385-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>板载（On-Board）</td>
<td>ARM Cortex-M3处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an385.dts?plain=1#L29">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P021_arm_cortex-m3.md#std-dtcompatible-arm-cortex-m3"><code>arm,cortex-m3</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>板载（On-Board）</td>
<td>ARM Cortex-M系统设计套件定时器（CMSDK Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L98">已启用：2</a>）</td>
<td><a href="../counter_binding_reference/P007_arm_cmsdk-timer.md#std-dtcompatible-arm-cmsdk-timer"><code>arm,cmsdk-timer</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM CMSDK双定时器（Dual Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L110">已启用：1</a>）</td>
<td><a href="../counter_binding_reference/P006_arm_cmsdk-dtimer.md#std-dtcompatible-arm-cmsdk-dtimer"><code>arm,cmsdk-dtimer</code></a></td>
</tr>
<tr>
<td rowspan="1">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN9220以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L203">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P003_smsc_lan9220.md#std-dtcompatible-smsc-lan9220"><code>smsc,lan9220</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L171">已启用：4</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P027_arm_cmsdk-gpio.md#std-dtcompatible-arm-cmsdk-gpio"><code>arm,cmsdk-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM 32位内存映射输入输出GPIO（MMIO32 GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L248">已启用：3</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P028_arm_mmio32-gpio.md#std-dtcompatible-arm-mmio32-gpio"><code>arm,mmio32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>板载（On-Board）</td>
<td>ARM SBCon双线串行总线接口（Two-Wire Serial Bus Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L212">已启用：4</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P006_arm_versatile-i2c.md#std-dtcompatible-arm-versatile-i2c"><code>arm,versatile-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L40">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L61">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存或其他非易失性存储器的固定分区（Fixed Partitions）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions"><code>fixed-partitions</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>板载（On-Board）</td>
<td>Arm MPS2引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L274">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P008_arm_mps2-pinctrl.md#std-dtcompatible-arm-mps2-pinctrl"><code>arm,mps2-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L116">已启用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P007_arm_cmsdk-uart.md#std-dtcompatible-arm-cmsdk-uart"><code>arm,cmsdk-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L154">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P005_arm_cmsdk-watchdog.md#std-dtcompatible-arm-cmsdk-watchdog"><code>arm,cmsdk-watchdog</code></a></td>
</tr>
</table>

<a id="mps2-mps2/an386-hw-features-section"></a>

### `mps2/an386`目标（Target）

<a id="mps2-mps2/an386-hw-features-panel"></a>

<a id="mps2-mps2/an386-hw-features-memory"></a>

该开发板目标的片上存储容量：4 MiB RAM、4 MiB Flash。

<a id="mps2-mps2/an386-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>板载（On-Board）</td>
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an386.dts?plain=1#L26">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>板载（On-Board）</td>
<td>ARM Cortex-M系统设计套件定时器（CMSDK Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L98">已启用：2</a>）</td>
<td><a href="../counter_binding_reference/P007_arm_cmsdk-timer.md#std-dtcompatible-arm-cmsdk-timer"><code>arm,cmsdk-timer</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM CMSDK双定时器（Dual Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L110">已启用：1</a>）</td>
<td><a href="../counter_binding_reference/P006_arm_cmsdk-dtimer.md#std-dtcompatible-arm-cmsdk-dtimer"><code>arm,cmsdk-dtimer</code></a></td>
</tr>
<tr>
<td rowspan="1">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN9220以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L203">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P003_smsc_lan9220.md#std-dtcompatible-smsc-lan9220"><code>smsc,lan9220</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L171">已启用：4</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P027_arm_cmsdk-gpio.md#std-dtcompatible-arm-cmsdk-gpio"><code>arm,cmsdk-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM 32位内存映射输入输出GPIO（MMIO32 GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L248">已启用：3</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P028_arm_mmio32-gpio.md#std-dtcompatible-arm-mmio32-gpio"><code>arm,mmio32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>板载（On-Board）</td>
<td>ARM SBCon双线串行总线接口（Two-Wire Serial Bus Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L212">已启用：4</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P006_arm_versatile-i2c.md#std-dtcompatible-arm-versatile-i2c"><code>arm,versatile-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L40">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L61">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存或其他非易失性存储器的固定分区（Fixed Partitions）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions"><code>fixed-partitions</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>板载（On-Board）</td>
<td>Arm MPS2引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L274">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P008_arm_mps2-pinctrl.md#std-dtcompatible-arm-mps2-pinctrl"><code>arm,mps2-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L116">已启用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P007_arm_cmsdk-uart.md#std-dtcompatible-arm-cmsdk-uart"><code>arm,cmsdk-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L154">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P005_arm_cmsdk-watchdog.md#std-dtcompatible-arm-cmsdk-watchdog"><code>arm,cmsdk-watchdog</code></a></td>
</tr>
</table>

<a id="mps2-mps2/an500-hw-features-section"></a>

### `mps2/an500`目标（Target）

<a id="mps2-mps2/an500-hw-features-panel"></a>

<a id="mps2-mps2/an500-hw-features-memory"></a>

该开发板目标的片上存储容量：4 MiB RAM、4 MiB Flash。

<a id="mps2-mps2/an500-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>板载（On-Board）</td>
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an500.dts?plain=1#L22">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>板载（On-Board）</td>
<td>ARM Cortex-M系统设计套件定时器（CMSDK Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L98">已启用：2</a>）</td>
<td><a href="../counter_binding_reference/P007_arm_cmsdk-timer.md#std-dtcompatible-arm-cmsdk-timer"><code>arm,cmsdk-timer</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM CMSDK双定时器（Dual Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L110">已启用：1</a>）</td>
<td><a href="../counter_binding_reference/P006_arm_cmsdk-dtimer.md#std-dtcompatible-arm-cmsdk-dtimer"><code>arm,cmsdk-dtimer</code></a></td>
</tr>
<tr>
<td rowspan="1">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN9220以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L203">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P003_smsc_lan9220.md#std-dtcompatible-smsc-lan9220"><code>smsc,lan9220</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L171">已启用：4</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P027_arm_cmsdk-gpio.md#std-dtcompatible-arm-cmsdk-gpio"><code>arm,cmsdk-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM 32位内存映射输入输出GPIO（MMIO32 GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L248">已启用：3</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P028_arm_mmio32-gpio.md#std-dtcompatible-arm-mmio32-gpio"><code>arm,mmio32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>板载（On-Board）</td>
<td>ARM SBCon双线串行总线接口（Two-Wire Serial Bus Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L212">已启用：4</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P006_arm_versatile-i2c.md#std-dtcompatible-arm-versatile-i2c"><code>arm,versatile-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L40">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L61">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存或其他非易失性存储器的固定分区（Fixed Partitions）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions"><code>fixed-partitions</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>板载（On-Board）</td>
<td>Arm MPS2引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L274">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P008_arm_mps2-pinctrl.md#std-dtcompatible-arm-mps2-pinctrl"><code>arm,mps2-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L116">已启用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P007_arm_cmsdk-uart.md#std-dtcompatible-arm-cmsdk-uart"><code>arm,cmsdk-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_base.dtsi?plain=1#L154">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P005_arm_cmsdk-watchdog.md#std-dtcompatible-arm-cmsdk-watchdog"><code>arm,cmsdk-watchdog</code></a></td>
</tr>
</table>

<a id="mps2-mps2/an521/cpu0-hw-features-section"></a>

### `mps2/an521/cpu0`目标（Target）

<a id="mps2-mps2/an521/cpu0-hw-features-panel"></a>

<a id="mps2-mps2/an521/cpu0-hw-features-memory"></a>

该开发板目标的片上存储容量：4 MiB RAM、4 MiB Flash。

<a id="mps2-mps2/an521/cpu0-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>板载（On-Board）</td>
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521_cpu0.dts?plain=1#L77">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521-common.dtsi?plain=1#L8">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>板载（On-Board）</td>
<td>ARM Cortex-M系统设计套件定时器（CMSDK Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521-common.dtsi?plain=1#L14">已启用：2</a>）</td>
<td><a href="../counter_binding_reference/P007_arm_cmsdk-timer.md#std-dtcompatible-arm-cmsdk-timer"><code>arm,cmsdk-timer</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM CMSDK双定时器（Dual Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521-common.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../counter_binding_reference/P006_arm_cmsdk-dtimer.md#std-dtcompatible-arm-cmsdk-dtimer"><code>arm,cmsdk-dtimer</code></a></td>
</tr>
<tr>
<td rowspan="1">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN9220以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521-common.dtsi?plain=1#L195">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P003_smsc_lan9220.md#std-dtcompatible-smsc-lan9220"><code>smsc,lan9220</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521-common.dtsi?plain=1#L44">已启用：4</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P027_arm_cmsdk-gpio.md#std-dtcompatible-arm-cmsdk-gpio"><code>arm,cmsdk-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM 32位内存映射输入输出GPIO（MMIO32 GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521-common.dtsi?plain=1#L167">已启用：3</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P028_arm_mmio32-gpio.md#std-dtcompatible-arm-mmio32-gpio"><code>arm,mmio32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>板载（On-Board）</td>
<td>ARM SBCon双线串行总线接口（Two-Wire Serial Bus Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521-common.dtsi?plain=1#L131">已启用：4</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P006_arm_versatile-i2c.md#std-dtcompatible-arm-versatile-i2c"><code>arm,versatile-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521_cpu0.dts?plain=1#L56">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521_cpu0.dts?plain=1#L42">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱处理单元（Mailbox Handling Unit）</td>
<td>板载（On-Board）</td>
<td>ARM消息处理单元（MHU / Message Handling Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521-common.dtsi?plain=1#L32">已启用：2</a>）</td>
<td><a href="../pcie_memory_virtualization_binding_reference/P001_arm_mhu.md#std-dtcompatible-arm-mhu"><code>arm,mhu</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>板载（On-Board）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521_cpu0.dts?plain=1#L84">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>板载（On-Board）</td>
<td>Arm MPS2引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521-common.dtsi?plain=1#L203">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P008_arm_mps2-pinctrl.md#std-dtcompatible-arm-mps2-pinctrl"><code>arm,mps2-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521-common.dtsi?plain=1#L82">已启用：5</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P007_arm_cmsdk-uart.md#std-dtcompatible-arm-cmsdk-uart"><code>arm,cmsdk-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521-common.dtsi?plain=1#L76">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P005_arm_cmsdk-watchdog.md#std-dtcompatible-arm-cmsdk-watchdog"><code>arm,cmsdk-watchdog</code></a></td>
</tr>
</table>

---

[上一章](P004_ARM_Ltd..md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_ARM_MPS2_AN521.md)
