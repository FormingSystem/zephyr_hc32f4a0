---
id: learning.zephyr-docs.boards-aesc-aithinker-alientek.page-1
title: ElemRV Flask-H
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/aesc/elemrv_flask_h/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="elemrv_flask_h"></a>

# 第1章\_ElemRV Flask-H

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/aesc/elemrv_flask_h/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`elemrv_flask_h`

厂商（Vendor）：

[Aesc Silicon](https://docs.zephyrproject.org/latest/boards/index.html#vendor=aesc)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[elemrv_h](https://docs.zephyrproject.org/latest/boards/index.html#soc=elemrv_h)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/aesc/elemrv_flask_h/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

ElemRV-H是ElemRV系列中尺寸最小、面积优化程度最高的设计，基于Hydrogen平台构建。它提供最小功能集（Minimal Feature Set），面向首要关注资源约束（Resource Constraints）的应用。

更多细节请参阅官方GitHub项目（[GitHub Project](https://github.com/aesc-silicon/elemrv)）。

<a id="supported-features"></a>

## 支持的功能（Supported Features）

`elemrv_flask_h`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="elemrv_flask_h-hw-features"></a>

<a id="elemrv_flask_h-elemrv_flask_h/elemrv_h-hw-features-section"></a>

### `elemrv_flask_h/elemrv_h`目标（Target）

<a id="elemrv_flask_h-elemrv_flask_h/elemrv_h-hw-features-panel"></a>

<a id="elemrv_flask_h-elemrv_flask_h/elemrv_h-hw-features-memory"></a>

该开发板目标的片上存储容量：8 KiB RAM、512 KiB Flash。

<a id="elemrv_flask_h-elemrv_flask_h/elemrv_h-hw-features-table"></a>

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
<td>VexiiRiscv RISC-V处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/hydrogen.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P045_spinalhdl_vexiiriscv.md#std-dtcompatible-spinalhdl-vexiiriscv"><code>spinalhdl,vexiiriscv</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Aesc Silicon时钟控制器（Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/hydrogen.dtsi?plain=1#L50">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P005_aesc_clock-controller.md#std-dtcompatible-aesc-clock-controller"><code>aesc,clock-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Aesc Silicon SPI闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/hydrogen.dtsi?plain=1#L65">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P003_aesc_spi-flash-controller.md#std-dtcompatible-aesc-spi-flash-controller"><code>aesc,spi-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Aesc Silicon通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/elemrv-h.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P013_aesc_gpio.md#std-dtcompatible-aesc-gpio"><code>aesc,gpio</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>RISC-V CPU中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/hydrogen.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P006_riscv_cpu-intc.md#std-dtcompatible-riscv-cpu-intc"><code>riscv,cpu-intc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive RISCV-V平台级中断控制器（PLIC / Platform-Local Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/hydrogen.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P009_sifive_plic-1.0.0.md#std-dtcompatible-sifive-plic-1.0.0"><code>sifive,plic-1.0.0</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/aesc/elemrv_flask_h/elemrv_flask_h.dts?plain=1#L31">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/aesc/elemrv_flask_h/elemrv_flask_h.dts?plain=1#L52">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Aesc引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/elemrv-h.dtsi?plain=1#L37">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P002_aesc_pinctrl.md#std-dtcompatible-aesc-pinctrl"><code>aesc,pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Aesc Silicon通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/elemrv-h.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P002_aesc_uart.md#std-dtcompatible-aesc-uart"><code>aesc,uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/aesc/elemrv_flask_h/elemrv_flask_h.dts?plain=1#L41">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>Aesc Silicon系统控制器（System Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/hydrogen.dtsi?plain=1#L58">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P006_aesc_syscon.md#std-dtcompatible-aesc-syscon"><code>aesc,syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>RISC-V机器模式定时器（Machine Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/hydrogen.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer"><code>riscv,machine-timer</code></a></td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

RISC-V内核的系统时钟设置为50 MHz。该值通过设备树`cpu0`节点的`clock-frequency`属性指定。

<a id="clock-controller"></a>

### 时钟控制器（Clock Controller）

时钟控制器管理Hydrogen平台的时钟域（Clock Domains）。每个时钟域提供一个含使能位的控制寄存器（Control Register），以及一个包含倍频因子和分频因子的比例寄存器（Ratio Register）。各时钟域的频率由系统控制器提供的参考时钟（Reference Clock）推导而来：

```text
rate = reference * multiplier / divider
```

外设通过`clocks`属性引用时钟域，而不是硬编码频率，例如`clocks = <&clkctrl HYDROGEN_CLK_SYSTEM>`。时钟域索引定义在[include/zephyr/dt-bindings/clock/aesc-clock-controller.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/clock/aesc-clock-controller.h)中。

<a id="system-controller"></a>

### 系统控制器（System Controller）

系统控制器是一个只读寄存器块（Read-Only Register Block），提供平台标识、芯片修订版本、构建日期、参考时钟频率及功能位图（Feature Bitmap）。时钟控制器从中读取参考时钟，因此系统控制器先初始化。

<a id="cpu"></a>

### 中央处理器（CPU）

ElemRV-H集成VexiiRiscv RISC-V内核，具有以下指令集架构（ISA）扩展：


- Zicsr：控制与状态寄存器操作（Control and Status Register Operations）
- Zifencei：指令获取屏障（Instruction-Fetch Fence）

该CPU的完整指令集架构（ISA）字符串为`RV32I_Zicsr_Zifencei`。

<a id="hart-level-interrupt-controller-hlic"></a>

### 硬件线程级中断控制器（HLIC / Hart-Level Interrupt Controller）

每个CPU内核都配有硬件线程级中断控制器（HLIC），可通过控制与状态寄存器（CSRs）配置。

<a id="machine-timer"></a>

### 机器模式定时器（Machine Timer）

默认启用符合RISC-V规范的机器模式定时器（Machine Timer）。

<a id="serial"></a>

### 串行接口（Serial）

通用异步收发器（UART / Universal Asynchronous Receiver-Transmitter）接口是可配置的串行通信外设，用于发送和接收数据。

默认情况下，`uart0`的波特率（Baud Rate）为115200，可通过ElemRV设备树调整。

要评估UART接口，构建并运行以下示例：

```text
# From the root of the zephyr repository
west build -b elemrv_flask_h samples/hello_world
```

<a id="pin-multiplexer"></a>

### 引脚复用器（Pin Multiplexer）

引脚复用器允许将每个引脚分配给多个外设功能之一。下表列出所有可用的引脚分配：

<table>
<tr>
<th>引脚（Pin）</th>
<th>选项0（Option 0）</th>
<th>选项1（Option 1）</th>
</tr>
<tr>
<td>0</td>
<td>gpio0_0</td>
<td>pwm0_out_0</td>
</tr>
<tr>
<td>1</td>
<td>gpio0_1</td>
<td>pio0_0</td>
</tr>
<tr>
<td>2</td>
<td>gpio0_2</td>
<td>pio0_1</td>
</tr>
<tr>
<td>3</td>
<td>gpio0_3</td>
<td>pio0_2</td>
</tr>
<tr>
<td>4</td>
<td>uart0_tx</td>
<td>gpio0_4</td>
</tr>
<tr>
<td>5</td>
<td>uart0_rx</td>
<td>gpio0_5</td>
</tr>
<tr>
<td>6</td>
<td>uart0_cts</td>
<td>gpio0_6</td>
</tr>
<tr>
<td>7</td>
<td>uart0_rts</td>
<td>gpio0_7</td>
</tr>
<tr>
<td>8</td>
<td>gpio0_8</td>
<td>pwm0_comp_0</td>
</tr>
<tr>
<td>9</td>
<td>gpio0_9</td>
<td>i2c0_scl</td>
</tr>
<tr>
<td>10</td>
<td>gpio0_10</td>
<td>i2c0_sda</td>
</tr>
<tr>
<td>11</td>
<td>gpio0_11</td>
<td>i2c0_interrupt_0</td>
</tr>
</table>

注意（Note）

Zephyr尚不支持PWM、PIO和I2C驱动。

<a id="gpio"></a>

### 通用输入输出（GPIO）

带三态引脚（Tri-State Pins）的通用输入输出接口（GPIO / General-Purpose Input/Output）是一种数字接口，允许将每个引脚配置为输入或输出，并通过额外控制设置数据流方向。

Blinky示例提供了一个简单方式，用于了解如何使用GPIO控制外部LED。

```text
# From the root of the zephyr repository
west build -b elemrv_flask_h samples/basic/blinky
```

---

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_ElemRV_Flask-N.md)
