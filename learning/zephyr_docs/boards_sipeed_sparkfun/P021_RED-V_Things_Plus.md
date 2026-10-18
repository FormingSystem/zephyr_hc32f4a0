---
id: learning.zephyr-docs.boards-sipeed-sparkfun.page-21
title: RED-V Things Plus
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/sparkfun/red_v_things_plus/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="sparkfun_red_v_things_plus"></a>

# 第21章\_RED-V Things Plus

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/sparkfun/red_v_things_plus/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/sparkfun_red_v_things_plus.jpg](images/sparkfun_red_v_things_plus.jpg)](images/sparkfun_red_v_things_plus.jpg)

RED-V Things Plus

名称（Name）：

`sparkfun_red_v_things_plus`

厂商（Vendor）：

[SparkFun Electronics](https://docs.zephyrproject.org/latest/boards/index.html#vendor=sparkfun)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[fe310_g002](https://docs.zephyrproject.org/latest/boards/index.html#soc=fe310_g002)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/sparkfun/red_v_things_plus/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

SparkFun RED-V Things Plus是一块采用SiFive FE310-G002 RISC-V SoC的开发板。

SparkFun RED-V Things Plus及SiFive FE310-G002更多信息见：


- [SparkFun RED-V Things Plus网站](https://www.sparkfun.com/products/15799)
- [SiFive FE310-G002数据手册](https://sifive.cdn.prismic.io/sifive/4999db8a-432f-45e4-bab2-57007eed0a43_fe310-g002-datasheet-v1p2.pdf)
- [SiFive FE310-G002用户手册](https://sifive.cdn.prismic.io/sifive/034760b5-ac6a-4b1c-911c-f4148bb2c4a5_fe310-g002-v1p5.pdf)

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`sparkfun_red_v_things_plus`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="sparkfun_red_v_things_plus-hw-features"></a>

<a id="sparkfun_red_v_things_plus-sparkfun_red_v_things_plus/fe310_g002-hw-features-section"></a>

#### `sparkfun_red_v_things_plus/fe310_g002`目标（Target）

<a id="sparkfun_red_v_things_plus-sparkfun_red_v_things_plus/fe310_g002-hw-features-panel"></a>

<a id="sparkfun_red_v_things_plus-sparkfun_red_v_things_plus/fe310_g002-hw-features-memory"></a>

此板级目标的片上存储：16 KiB RAM；Flash不适用（N/A）。

<a id="sparkfun_red_v_things_plus-sparkfun_red_v_things_plus/fe310_g002-hw-features-table"></a>

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
<td>SiFive E31标准处理器核（Standard Core CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P038_sifive_e31.md#std-dtcompatible-sifive-e31"><code>sifive,e31</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L14">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../timer_reference/P110_固定比例时钟绑定.md#dtbinding-fixed-factor-clock"><code>fixed-factor-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>SiFive GPIO（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L104">已启用：1</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P008_sifive_gpio0.md#std-dtcompatible-sifive-gpio0"><code>sifive,gpio0</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>SiFive Freedom I2C接口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L131">已启用：1</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P002_sifive_i2c0.md#std-dtcompatible-sifive-i2c0"><code>sifive,i2c0</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>RISC-V CPU中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P006_riscv_cpu-intc.md#std-dtcompatible-riscv-cpu-intc"><code>riscv,cpu-intc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive RISC-V内核本地中断器（Core-Local Interruptor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P010_sifive_clint0.md#std-dtcompatible-sifive-clint0"><code>sifive,clint0</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive RISCV-V平台级中断控制器（PLIC / Platform-Local Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L142">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P009_sifive_plic-1.0.0.md#std-dtcompatible-sifive-plic-1.0.0"><code>sifive,plic-1.0.0</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sparkfun/red_v_things_plus/sparkfun_red_v_things_plus.dts?plain=1#L26">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>这些属性用于支持Zephyr的<code>spi-nor</code>闪存驱动通过Zephyr SPI API，使用基于M25P80的标准命令集控制串行闪存（Serial Flash Memory）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sparkfun/red_v_things_plus/sparkfun_red_v_things_plus.dts?plain=1#L51">已禁用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor"><code>jedec,spi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>SiFive FE310 I/O功能（IOF）绑定涵盖GPIO控制器中的IOF_EN及IOF_SEL寄存器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L125">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P022_sifive_pinctrl.md#std-dtcompatible-sifive-pinctrl"><code>sifive,pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>SiFive脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L171">已禁用：3</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P004_sifive_pwm0.md#std-dtcompatible-sifive-pwm0"><code>sifive,pwm0</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>SiFive UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L216">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L225">已禁用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P003_sifive_uart0.md#std-dtcompatible-sifive-uart0"><code>sifive,uart0</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>SiFive SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L245">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L234">已禁用：2</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P003_sifive_spi0.md#std-dtcompatible-sifive-spi0"><code>sifive,spi0</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>SiFive数据紧密集成存储器（Data Tightly-Integrated Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L92">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P012_sifive_dtim0.md#std-dtcompatible-sifive-dtim0"><code>sifive,dtim0</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>RISC-V机器模式定时器（Machine Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer"><code>riscv,machine-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>SiFive FE310看门狗驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sifive/riscv32-fe310.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P009_sifive_wdt.md#std-dtcompatible-sifive-wdt"><code>sifive,wdt</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 编程与调试（Programming and Debugging）

`sparkfun_red_v_things_plus`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

<a id="building"></a>

### 构建（Building）

sparkfun_red_v_things_plus板级配置的应用可按常规方式构建，见“构建应用”，使用相应板名：（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)）

```text
west build -b sparkfun_red_v_things_plus
```

<a id="flashing"></a>

### 烧录（Flashing）

此板通过SEGGER J-Link OB烧录及调试，需要安装[SEGGER J-Link软件及文档包](https://www.segger.com/downloads/jlink#J-LinkSoftwareAndDocumentationPack)。原文要求V6.46a或更新版本，提供Windows、Linux及macOS下载。

安装SEGGER J-Link软件后，可按常规方式烧录，详情见“构建应用”及“运行应用”：（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）

```text
west build -b sparkfun_red_v_things_plus
west flash
```

<a id="debugging"></a>

### 调试（Debugging）

详细概述见[应用调试（Application Debugging）](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

## 译注

RED-V Things Plus采用FE310-G002，J-Link OB版本要求按原文V6.46a及更新保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [jlink](https://www.segger.com/downloads/jlink#J-LinkSoftwareAndDocumentationPack)：页面可访问，但未确认目标片段。

---

[上一章](P020_Pro_Micro_RP2040.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P022_Sparkfun_RP2040_mikroBUS_Development_Board.md)
