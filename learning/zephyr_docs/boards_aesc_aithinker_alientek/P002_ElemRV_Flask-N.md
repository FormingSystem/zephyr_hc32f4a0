---
id: learning.zephyr-docs.boards-aesc-aithinker-alientek.page-2
title: ElemRV Flask-N
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/aesc/elemrv_flask_n/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="elemrv_flask_n"></a>

# 第2章\_ElemRV Flask-N

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/aesc/elemrv_flask_n/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`elemrv_flask_n`

厂商（Vendor）：

[Aesc Silicon](https://docs.zephyrproject.org/latest/boards/index.html#vendor=aesc)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[elemrv_n](https://docs.zephyrproject.org/latest/boards/index.html#soc=elemrv_n)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/aesc/elemrv_flask_n/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

ElemRV-N是一款使用SpinalHDL设计、从端到端均开源（End-to-End Open-Source）的RISC-V微控制器。

在[FMD-QNC](https://www.elektronikforschung.de/projekte/fmd-qnc)支持下，ElemRV-N 0.2版本使用[IHP开放工艺设计套件（Open PDK）](https://github.com/IHP-GmbH/IHP-Open-PDK)成功制造；该套件对应130 nm开放半导体工艺。

更多细节请参阅官方GitHub项目（[GitHub Project](https://github.com/aesc-silicon/elemrv)）。

注意（Note）

当前支持的芯片版本为ElemRV-N 0.2。

<a id="supported-features"></a>

## 支持的功能（Supported Features）

`elemrv_flask_n`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="elemrv_flask_n-hw-features"></a>

<a id="elemrv_flask_n-elemrv_flask_n/elemrv_n-hw-features-section"></a>

### `elemrv_flask_n/elemrv_n`目标（Target）

<a id="elemrv_flask_n-elemrv_flask_n/elemrv_n-hw-features-panel"></a>

<a id="elemrv_flask_n-elemrv_flask_n/elemrv_n-hw-features-memory"></a>

该开发板目标的片上存储容量：32 KiB RAM、32 KiB Flash。

<a id="elemrv_flask_n-elemrv_flask_n/elemrv_n-hw-features-table"></a>

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
<td>采用LiteX所用标准配置（Standard Configuration）的VexRiscv内核（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/nitrogen.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P019_litex_vexriscv-standard.md#std-dtcompatible-litex-vexriscv-standard"><code>litex,vexriscv-standard</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Aesc Silicon通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/elemrv-n.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P013_aesc_gpio.md#std-dtcompatible-aesc-gpio"><code>aesc,gpio</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>RISC-V CPU中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/nitrogen.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P006_riscv_cpu-intc.md#std-dtcompatible-riscv-cpu-intc"><code>riscv,cpu-intc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive RISCV-V平台级中断控制器（PLIC / Platform-Local Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/nitrogen.dtsi?plain=1#L51">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P009_sifive_plic-1.0.0.md#std-dtcompatible-sifive-plic-1.0.0"><code>sifive,plic-1.0.0</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/aesc/elemrv_flask_n/elemrv_flask_n.dts?plain=1#L27">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/aesc/elemrv_flask_n/elemrv_flask_n.dts?plain=1#L49">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Aesc引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/elemrv-n.dtsi?plain=1#L38">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P002_aesc_pinctrl.md#std-dtcompatible-aesc-pinctrl"><code>aesc,pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Aesc Silicon通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/elemrv-n.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P002_aesc_uart.md#std-dtcompatible-aesc-uart"><code>aesc,uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/aesc/elemrv_flask_n/elemrv_flask_n.dts?plain=1#L37">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>RISC-V机器模式定时器（Machine Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/nitrogen.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer"><code>riscv,machine-timer</code></a></td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

RISC-V内核的系统时钟设置为20 MHz。该值通过设备树`cpu0`节点的`clock-frequency`属性指定。

<a id="cpu"></a>

### 中央处理器（CPU）

ElemRV-N集成VexRiscv RISC-V内核，采用五级流水线（5-Stage Pipeline），并具有以下指令集架构（ISA）扩展：


- M：整数乘法／除法（Integer Multiply/Divide）
- C：压缩指令（Compressed Instructions）

还包含以下通用Z扩展（General-Purpose Z Extensions）：


- Zicntr：基本计数器与定时器扩展（Base Counter and Timer Extensions）
- Zicsr：控制与状态寄存器操作（Control and Status Register Operations）
- Zifencei：指令获取屏障（Instruction-Fetch Fence）

该CPU的完整指令集架构（ISA）字符串为`RV32IMC_Zicntr_Zicsr_Zifencei`。

<a id="hart-level-interrupt-controller-hlic"></a>

### 硬件线程级中断控制器（HLIC / Hart-Level Interrupt Controller）

每个CPU内核都配有硬件线程级中断控制器（HLIC），可通过控制与状态寄存器（CSRs）配置。

<a id="machine-timer"></a>

### 机器模式定时器（Machine Timer）

默认启用符合RISC-V规范的机器模式定时器（Machine Timer）。

<a id="serial"></a>

### 串行接口（Serial）

通用异步收发器（UART / Universal Asynchronous Receiver-Transmitter）接口是可配置的串行通信外设，用于发送和接收数据。

默认情况下，`uart0`的波特率（Baud Rate）为115200，可通过elemrv设备树调整。

要评估UART接口，构建并运行以下示例：

```text
# From the root of the zephyr repository
west build -b elemrv_flask_n samples/hello_world
```

<a id="gpio"></a>

### 通用输入输出（GPIO）

带三态引脚（Tri-State Pins）的通用输入输出接口（GPIO / General-Purpose Input/Output）是一种数字接口，允许将每个引脚配置为输入或输出，并通过额外控制设置数据流方向。

`gpio`共包含12个独立引脚。

Blinky示例提供了一个简单方式，用于了解如何使用GPIO控制外部LED。

```text
# From the root of the zephyr repository
west build -b elemrv_flask_n samples/basic/blinky
```

---

[上一章](P001_ElemRV_Flask-H.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_Aesc_Silicon.md)
