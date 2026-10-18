---
id: learning.zephyr-docs.boards-renesas-rx-rz.page-22
title: Renesas Starter Kit for RX140
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/renesas/rsk_rx140/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rsk_rx140"></a>

# 第22章\_瑞萨RX140入门套件

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/renesas/rsk_rx140/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/rsk_rx140.webp](images/rsk_rx140.webp)](images/rsk_rx140.webp)

瑞萨RX140入门套件

名称（Name）：

`rsk_rx140`

厂商（Vendor）：

[瑞萨电子（Renesas Electronics Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=renesas)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[rx](https://docs.zephyrproject.org/latest/boards/index.html#arch=rx)

片上系统（SoC）：

[r5f51406bdfn](https://docs.zephyrproject.org/latest/boards/index.html#soc=r5f51406bdfn)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rsk_rx140/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

瑞萨RX140入门套件面向初次使用RX140 MCU系列的开发者，兼具评估与入门用途。器件具有256 KB程序闪存、64 KB RAM及80针封装；套件包含LCD显示模块及片上调试仿真器。

直接访问MCU引脚（MCU Native Pin Access）

RSK-RX140包括：


- 48 MHz、32位RX140 MCU，R5F51406BDFN，80引脚LFQFP封装
- 通过标准排针直接访问MCU引脚，便于集成外设
- 板载8 MHz晶体、32.768 kHz子时钟及内部振荡器
- 多种低功耗模式

系统控制与调试


- USB Mini-B连接器用于串口通信，通过板载RL78/G1C USB转串口MCU实现
- 电源选项：


  - USB供电（USB-powered）
  - 外部直流电源，5 V输入插座
  - 由E2 Lite调试器供电
- 调试支持：


  - 通过E2 Lite调试器连接14针接口
- 用户LED及按键：


  - 四个用户LED，绿色、橙色及两个红色
  - 绿色电源LED
  - 一个复位按键、三个用户按键
  - 一个电位器，接到ADC输入
- 生态扩展接口：


  - 两个Digilent Pmod连接器，LCD及备用
  - 板载2 Kbit I2C EEPROM

专用功能接口（Special Feature Access）


- 电容触摸检测，一个滑条及两个按键
- CAN及LIN收发器
- 支持IEC 60730符合性
- 安全功能，内置可信安全IP（Trusted Secure IP）

<a id="hardware"></a>

## 硬件（Hardware）

详细硬件功能见：


- RX140 MCU：[RX140组用户手册硬件篇](https://www.renesas.com/en/document/mah/rx140-group-users-manual-hardware-rev120)
- RSK-RX140：[RSK_RX140用户手册](https://www.renesas.com/en/document/mat/renesas-starter-kit-rx140-users-manual)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`rsk_rx140`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="rsk_rx140-hw-features"></a>

<a id="rsk_rx140-rsk_rx140/r5f51406bdfn-hw-features-section"></a>

#### `rsk_rx140/r5f51406bdfn`目标（Target）

<a id="rsk_rx140-rsk_rx140/r5f51406bdfn-hw-features-panel"></a>

<a id="rsk_rx140-rsk_rx140/r5f51406bdfn-hw-features-memory"></a>

该开发板目标的片上存储容量：48 KiB RAM、256 KiB Flash。

<a id="rsk_rx140-rsk_rx140/r5f51406bdfn-hw-features-table"></a>

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
<td>瑞萨RXv2处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L24">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P031_renesas_rxv2.md#std-dtcompatible-renesas-rxv2"><code>renesas,rxv2</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L619">已禁用：1</a>）</td>
<td><a href="../hardware/P870_RenesasRX模数转换器绑定.md#dtbinding-renesas-rx-adc"><code>renesas,rx-adc</code></a></td>
</tr>
<tr>
<td rowspan="4">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX根时钟生成电路（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51406.dtsi?plain=1#L16">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51406.dtsi?plain=1#L47">已禁用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P010_renesas_rx-cgc-root-clock.md#std-dtcompatible-renesas-rx-cgc-root-clock"><code>renesas,rx-cgc-root-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX时钟生成电路的锁相环（PLL）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51406.dtsi?plain=1#L54">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P008_renesas_rx-cgc-pll.md#std-dtcompatible-renesas-rx-cgc-pll"><code>renesas,rx-cgc-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX时钟控制节点的pclk模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51406.dtsi?plain=1#L63">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P006_renesas_rx-cgc-pclk-block.md#std-dtcompatible-renesas-rx-cgc-pclk-block"><code>renesas,rx-cgc-pclk-block</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX时钟控制外设时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51406.dtsi?plain=1#L74">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51406.dtsi?plain=1#L103">已禁用：7</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P007_renesas_rx-cgc-pclk.md#std-dtcompatible-renesas-rx-cgc-pclk"><code>renesas,rx-cgc-pclk</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51406.dtsi?plain=1#L161">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P001_renesas_rx-flash.md#std-dtcompatible-renesas-rx-flash"><code>renesas,rx-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX系列通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L251">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L267">已禁用：11</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P019_renesas_rx-gpio.md#std-dtcompatible-renesas-rx-gpio"><code>renesas,rx-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX I2C主控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L631">已启用：1</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P016_renesas_rx-i2c.md#std-dtcompatible-renesas-rx-i2c"><code>renesas,rx-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rsk_rx140/rsk_rx140.dts?plain=1#L41">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>瑞萨中断控制单元（ICU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../renesas_interrupt_binding_reference/P002_renesas_rx-icu.md#std-dtcompatible-renesas-rx-icu"><code>renesas,rx-icu</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rsk_rx140/rsk_rx140.dts?plain=1#L27">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="4">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX数据传输控制器（Data Transfer Controller，DTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L60">已启用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P022_renesas_rx-dtc.md#std-dtcompatible-renesas-rx-dtc"><code>renesas,rx-dtc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX外部中断（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L181">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L171">已禁用：7</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P023_renesas_rx-external-interrupt.md#std-dtcompatible-renesas-rx-external-interrupt"><code>renesas,rx-external-interrupt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX串行通信接口（SCI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L523">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L539">已禁用：5</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P026_renesas_rx-sci.md#std-dtcompatible-renesas-rx-sci"><code>renesas,rx-sci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX多功能定时器脉冲单元（MTU）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L650">已启用：5</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P024_renesas_rx-mtu.md#std-dtcompatible-renesas-rx-mtu"><code>renesas,rx-mtu</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX系列闪存的设备树绑定（Binding）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51406.dtsi?plain=1#L169">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P011_renesas_rx-nv-flash.md#std-dtcompatible-renesas-rx-nv-flash"><code>renesas,rx-nv-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存或其他非易失性存储器的固定分区（Fixed Partitions）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rsk_rx140/rsk_rx140.dts?plain=1#L127">已启用：1</a>）</td>
<td><a href="../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions"><code>fixed-partitions</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L74">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P011_renesas_rx-pinctrl.md#std-dtcompatible-renesas-rx-pinctrl"><code>renesas,rx-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX引脚复用，多功能引脚控制器（Multi Function Pin Controller，MPC）；原文厂商名拼作Rensas（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L80">已启用：13</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P012_renesas_rx-pinmux.md#std-dtcompatible-renesas-rx-pinmux"><code>renesas,rx-pinmux</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX脉宽调制（PWM）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L694">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L668">已禁用：4</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P020_renesas_rx-mtu-pwm.md#std-dtcompatible-renesas-rx-mtu-pwm"><code>renesas,rx-mtu-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">瑞萨 RX（Renesas RX）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX软件中断（Software Interrupt，SWINT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L51">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P012_renesas_rx-swint.md#std-dtcompatible-renesas-rx-swint"><code>renesas,rx-swint</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX SCI UART控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L533">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L549">已禁用：5</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P013_renesas_rx-uart-sci.md#std-dtcompatible-renesas-rx-uart-sci"><code>renesas,rx-uart-sci</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX串行外设接口（RSPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L815">已启用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P019_renesas_rx-rspi.md#std-dtcompatible-renesas-rx-rspi"><code>renesas,rx-rspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51406.dtsi?plain=1#L155">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX定时器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L781">已启用：1</a>）</td>
<td><a href="../renesas_timer_binding_reference/P003_renesas_rx-timer-cmt-start-control.md#std-dtcompatible-renesas-rx-timer-cmt-start-control"><code>renesas,rx-timer-cmt-start-control</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX定时器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L790">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L803">已禁用：1</a>）</td>
<td><a href="../renesas_timer_binding_reference/P004_renesas_rx-timer-cmt.md#std-dtcompatible-renesas-rx-timer-cmt"><code>renesas,rx-timer-cmt</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX独立看门狗（Independent Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx140-common.dtsi?plain=1#L834">已启用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P006_renesas_rx-iwdt.md#std-dtcompatible-renesas-rx-iwdt"><code>renesas,rx-iwdt</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`rsk_rx140`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-rfp">rfp</a></td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

rsk_rx140可按常规方式构建、烧录及调试，详见“构建应用”与“运行应用”。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）

<a id="flashing"></a>

### 烧录（Flashing）

通过开发板14针调试连接器将E2 Lite调试器接至主机PC，可向RSK-RX140烧录。以下为构建并烧录[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用的示例。

```text
# From the root of the zephyr repository
west build -b rsk_rx140 samples/hello_world
west flash
```

<a id="debugging"></a>

### 调试（Debugging）

可使用Visual Studio Code的Renesas Debug扩展获得图形调试界面。launch.json配置如下。（[Renesas Debug调试扩展](https://marketplace.visualstudio.com/items?itemName=RenesasElectronicsCorporation.renesas-debug)）

```text
{
  "version": "0.2.0",
  "configurations": [
      {
          "type": "renesas-hardware",
          "request": "launch",
          "name": "RX140 Renesas Debugging E2lite",
          "target": {
              "deviceFamily": "RX",
              "device": "R5F51406",
              "debuggerType": "E2LITE"
              "serverParameters": [
                  "-uUseFine=", "1",
                  "-w=", "0",
              ],
          }
      }
  ]
}
```

<a id="references"></a>

## 参考资料（References）


- [RSK_RX140网站](https://www.renesas.com/en/design-resources/boards-kits/rsk-rx140)
- [RX140 MCU组网站](https://www.renesas.com/en/products/rx140)

## 译注

RSK-RX140的串口经RL78/G1C USB转换器，调试为14针E2 Lite；与FPB-RX140分别说明。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [renesas-starter-kit-rx140-users-manual](https://www.renesas.com/en/document/mat/renesas-starter-kit-rx140-users-manual)：HTTP Error 429: Too Many Requests。
- [rx140](https://www.renesas.com/en/products/rx140)：HTTP Error 429: Too Many Requests。

---

[上一章](P021_Renesas_Starter_Kit_for_RX130.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P023_Capacitive_Touch_Evaluation_System_for_RA2L1.md)
