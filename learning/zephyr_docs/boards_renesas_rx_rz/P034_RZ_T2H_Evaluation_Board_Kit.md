---
id: learning.zephyr-docs.boards-renesas-rx-rz.page-34
title: RZ T2H Evaluation Board Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/renesas/rzt2h_evb/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rzt2h_evb"></a>

# 第34章\_RZ/T2H评估板套件

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/renesas/rzt2h_evb/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/rzt2h_evb.webp](images/rzt2h_evb.webp)](images/rzt2h_evb.webp)

RZ/T2H评估板套件

名称（Name）：

`rzt2h_evb`

厂商（Vendor）：

[瑞萨电子（Renesas Electronics Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=renesas)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[r9a09g077m44gbg](https://docs.zephyrproject.org/latest/boards/index.html#soc=r9a09g077m44gbg)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rzt2h_evb/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

RZ/T2H评估板套件用于评估和开发RZ/T2H MPU。凭借板载仿真器，只需用随附线缆连接PC即可开始评估。板上包含千兆以太网PHY、非易失性存储器及LPDDR4等丰富功能IC，无需扩展板即可评估RZ/T2H多种功能。

还可扩展逆变器板，实现多轴电机控制。


- 板载729引脚RZ/T2H MPU，R9A09G077M44GBG
- 配备千兆以太网PHY、QSPI闪存／Octa Flash／eMMC等非易失性存储器及DDR等丰富功能IC，可全面评估目标MPU功能
- Micro SD卡槽、SD卡槽及PCIe连接器
- Pmod、Grove、Qwiic、mikroBUS等通用接口
- 排针支持与用户硬件系统自由组合，以评估RZ/T2H
- 配备仿真电路，连接USB线即可开始程序调试。随附三根USB线，分别用于15 V Type-C供电、Micro-B板载仿真器连接及Mini-B终端调试。


  - 请自行准备至少45 W、15 V／3 A的USB PD电源。
- 可使用瑞萨e² studio IDE及RZ/T2 FSP

<a id="hardware"></a>

## 硬件（Hardware）

<a id="id5"></a>

板卡详细硬件功能见[RZ/T2H-EVKIT网站](https://www.renesas.com/en/design-resources/boards-kits/rz-t2h-evkit)[注2](#id4)。


- <a id="id3"></a>

  [RZ/T2H组网站](https://www.renesas.com/en/products/rz-t2h)[注1](#id2)
- <a id="id6"></a>

  [RZ/T2H-EVKIT网站](https://www.renesas.com/en/design-resources/boards-kits/rz-t2h-evkit)[注2](#id4)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`rzt2h_evb`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="rzt2h_evb-hw-features"></a>

<a id="rzt2h_evb-rzt2h_evb/r9a09g077m44gbg/cr52_0-hw-features-section"></a>

#### `rzt2h_evb/r9a09g077m44gbg/cr52_0`目标（Target）

<a id="rzt2h_evb-rzt2h_evb/r9a09g077m44gbg/cr52_0-hw-features-panel"></a>

<a id="rzt2h_evb-rzt2h_evb/r9a09g077m44gbg/cr52_0-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、16 MiB Flash。

<a id="rzt2h_evb-rzt2h_evb/r9a09g077m44gbg/cr52_0-hw-features-table"></a>

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
<td>ARM Cortex-R52处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P011_arm_cortex-r52.md#std-dtcompatible-arm-cortex-r52"><code>arm,cortex-r52</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L38">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RZ GPIO公共部分v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L235">已启用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P021_renesas_rz-gpio-common-v3.md#std-dtcompatible-renesas-rz-gpio-common-v3"><code>renesas,rz-gpio-common-v3</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RZ GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L248">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L257">已禁用：31</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P025_renesas_rz-gpio.md#std-dtcompatible-renesas-rz-gpio"><code>renesas,rz-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzt2h_evb/rzt2h_evb_r9a09g077m44gbg_cr52_0.dts?plain=1#L54">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L52">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RZ中断控制单元（ICU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L98">已启用：1</a>）</td>
<td><a href="../renesas_interrupt_binding_reference/P005_renesas_rz-icu-v2.md#std-dtcompatible-renesas-rz-icu-v2"><code>renesas,rz-icu-v2</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RZ外部中断控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L122">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L106">已禁用：15</a>）</td>
<td><a href="../renesas_interrupt_binding_reference/P004_renesas_rz-ext-irq.md#std-dtcompatible-renesas-rz-ext-irq"><code>renesas,rz-ext-irq</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzt2h_evb/rzt2h_evb_r9a09g077m44gbg_cr52_0.dts?plain=1#L30">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RZ串行通信接口（SCI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L580">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L598">已禁用：5</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P029_renesas_rz-sci.md#std-dtcompatible-renesas-rz-sci"><code>renesas,rz-sci</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzt2h_evb/rzt2h_evb_r9a09g077m44gbg_cr52_0.dts?plain=1#L114">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RZ/T引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L45">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P017_renesas_rzt-pinctrl.md#std-dtcompatible-renesas-rzt-pinctrl"><code>renesas,rzt-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">四线串行外设接口（QSPI）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RZ扩展串行外设接口（XSPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L76">已禁用：2</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P010_renesas_rz-xspi.md#std-dtcompatible-renesas-rz-xspi"><code>renesas,rz-xspi</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RZ SCI UART控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L591">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L609">已禁用：5</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P015_renesas_rz-sci-uart.md#std-dtcompatible-renesas-rz-sci-uart"><code>renesas,rz-sci-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L61">已启用：3</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a09g077.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

开发板默认配置为：


- UART0连接到USB串口CN34；
- LED定义为led0、led1、led2及led3；

Zephyr控制台使用UART0。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`rzt2h_evb`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
</table>

rzt2h_evb可按常规方式构建、烧录及调试，详见“构建应用”与“运行应用”。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）

使用J-Link OB时：


1. 断开用于切换调试连接的跳线CN62。
2. 将Micro-USB Type-B连接到J-Link OB的USB连接器CN14，LED10随后亮起。

<a id="console"></a>

### 控制台（Console）

通过USB串口端口CN34访问UART。

<a id="debugging"></a>

### 调试（Debugging）

以下为构建并调试[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用的示例。

```text
# From the root of the zephyr repository
west build -b rzt2h_evb/r9a09g077m44gbg/cr52_0 samples/hello_world
west debug
```

<a id="flashing"></a>

### 烧录（Flashing）

使用flash命令前，必须将开发板设为xSPI启动模式。

```text
# From the root of the zephyr repository
west build -b rzt2h_evb/r9a09g077m44gbg/cr520 samples/hello_world
west flash
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.renesas.com/en/products/rz-t2h](https://www.renesas.com/en/products/rz-t2h)

<a id="id4"></a>

〔2〕 ([1](#id5),[2](#id6)) [https://www.renesas.com/en/design-resources/boards-kits/rz-t2h-evkit](https://www.renesas.com/en/design-resources/boards-kits/rz-t2h-evkit)

## 译注

RZ/T2H的J-Link OB为CN14、UART为CN34，切换调试连接需断开CN62。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [rz-t2h](https://www.renesas.com/en/products/rz-t2h)：HTTP Error 429: Too Many Requests。

---

[上一章](P033_Renesas_Starter_Kit_for_RZ_N2L.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P035_Renesas_Starter_Kit_for_RZ_T2L.md)
