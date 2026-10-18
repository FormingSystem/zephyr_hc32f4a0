---
id: learning.zephyr-docs.boards-cdac-to-cthings.page-1
title: ARIES v3.0 Development Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/cdac/aries_v3/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="aries_v3"></a>

# 第1章\_ARIES v3.0开发板（Development Board）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/cdac/aries_v3/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`aries_v3`

厂商（Vendor）：

[高级计算发展中心（C-DAC / Centre for Development of Advanced Computing）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=cdac)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[`riscv`](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[thejas32](https://docs.zephyrproject.org/latest/boards/index.html#soc=thejas32)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/cdac/aries_v3/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id2"></a>

C-DAC ARIES v3.0开发板基于高级计算发展中心（C-DAC）的[THEJAS32](https://vegaprocessors.in/thejas32-soc.php)片上系统（SoC）[注1](#id1)。THEJAS32采用VEGA ET1031处理器：这是印度数字印度RISC-V（DIR-V / Digital India RISC-V）计划开发的32位RV32IM单核、顺序执行（In-Order）、三级流水线（3-Stage Pipeline）RISC-V处理器。

<a id="hardware"></a>

## 硬件（Hardware）


- VEGA ET1031（RV32IM）内核，最高100 MHz
- 256 KB内部静态随机存储器（SRAM）；应用可用250 KB，启动ROM预留最高地址处的6 KB
- 2 MB外部SPI闪存
- 三路UART、四路SPI、三路I2C、八路PWM、32个GPIO及ADC
- 板载RGB LED
- JTAG调试接口

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`aries_v3`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="aries_v3-hw-features"></a>

<a id="aries_v3-aries_v3/thejas32-hw-features-section"></a>

#### `aries_v3/thejas32`目标（Target）

<a id="aries_v3-aries_v3/thejas32-hw-features-panel"></a>

<a id="aries_v3-aries_v3/thejas32-hw-features-memory"></a>

该开发板目标的片上存储容量：250 KiB RAM、N/A Flash。

<a id="aries_v3-aries_v3/thejas32-hw-features-table"></a>

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
<td>通用RISC-V处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/cdac/thejas32.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P034_riscv.md#std-dtcompatible-riscv"><code>riscv</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>C-DAC THEJAS32通用输入输出（GPIO）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/cdac/thejas32.dtsi?plain=1#L89">已启用：2</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P010_cdac_thejas32-gpio.md#std-dtcompatible-cdac-thejas32-gpio"><code>cdac,thejas32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>RISC-V CPU中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/cdac/thejas32.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P006_riscv_cpu-intc.md#std-dtcompatible-riscv-cpu-intc"><code>riscv,cpu-intc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>C-DAC THEJAS32中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/cdac/thejas32.dtsi?plain=1#L80">已启用：1</a>）</td>
<td><a href="../riscv_interrupt_binding_reference/P002_cdac_thejas32-intc.md#std-dtcompatible-cdac-thejas32-intc"><code>cdac,thejas32-intc</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/cdac/aries_v3/aries_v3.dts?plain=1#L22">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/cdac/thejas32.dtsi?plain=1#L107">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/cdac/thejas32.dtsi?plain=1#L116">已禁用：2</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/cdac/thejas32.dtsi?plain=1#L50">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>RISC-V机器模式定时器（Machine Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/cdac/thejas32.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer"><code>riscv,machine-timer</code></a></td>
</tr>
</table>

SoC具有SPI、I2C、PWM及ADC，但Zephyr尚不支持这些外设。

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

Zephyr控制台运行于`uart0`，波特率115200，通过USB转UART桥接到开发板的USB-C接口。

板载RGB LED的三个发光芯片分别由GPIO22（绿色，`led0`）、GPIO23（蓝色，`led1`）及GPIO24（红色，`led2`）驱动，均为低电平有效（Active Low）。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`aries_v3`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
<tr>
<td>vegadude</td>
<td>✅（默认 / default）</td>
<td></td>
</tr>
</table>

<a id="flashing"></a>

### 烧录（Flashing）

<a id="id4"></a>

<a id="index-0"></a>

开发板通过与控制台共用的USB-C串口烧录：启动ROM使用XMODEM协议经UART接收原始二进制程序，并从SRAM执行。`west flash`使用开源工具[vegadude](https://github.com/rnayabed/vegadude)[注2](#id3)，必须确保该工具可通过[`PATH`](../toolchains/P003_环境变量.md#envvar-PATH)找到。

保持BOOT SEL跳线断开并按下复位键，使开发板进入UART启动模式；随后构建并烧录应用。以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例。

```text
# From the root of the zephyr repository
west build -b aries_v3 samples/hello_world
west flash
```

然后连接串口终端，查看控制台输出：

```text
$ picocom /dev/ttyUSB0 -b 115200
```

也可使用C-DAC的`vegaxmodem`（UART启动）及`vegaflasher`（SPI闪存启动）工具手动上传`zephyr.bin`。

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://vegaprocessors.in/thejas32-soc.php](https://vegaprocessors.in/thejas32-soc.php)

<a id="id3"></a>

〔[2](#id4)〕 [https://github.com/rnayabed/vegadude](https://github.com/rnayabed/vegadude)

## 译注

本页的UART启动由ROM接收二进制程序后在SRAM执行，并不等同于写入外部SPI闪存。256 KB内部SRAM中启动ROM预留顶部6 KB；SPI、I2C、PWM、ADC虽存在于SoC中，官方页面明确尚未获得Zephyr支持。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [thejas32-soc.php](https://vegaprocessors.in/thejas32-soc.php)：HTTP Error 406: Not Acceptable。

---

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_C-DAC_Centre_for_Development_of_Advanced_Computing.md)
