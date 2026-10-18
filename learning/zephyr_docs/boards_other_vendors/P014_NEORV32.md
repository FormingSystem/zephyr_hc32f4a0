---
id: learning.zephyr-docs.boards-other-vendors.page-14
title: NEORV32
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/others/neorv32/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="neorv32"></a>

# 第14章\_NEORV32

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/others/neorv32/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/neorv32.png](images/neorv32.png)](images/neorv32.png)

NEORV32

名称（Name）：

`neorv32`

厂商（Vendor）：

[其他／未知厂商（Other/Unknown）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=others)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[`neorv32`](https://docs.zephyrproject.org/latest/boards/index.html#soc=neorv32)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/others/neorv32/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

NEORV32是兼容RISC-V的开源处理器系统，可作为更大SoC中的现成辅助处理器，或独立可定制微控制器。

NEORV32的更多信息见以下网站：


- [NEORV32 RISC-V处理器GitHub仓库](https://github.com/stnolting/neorv32)
- [NEORV32 RISC-V处理器数据手册](https://stnolting.github.io/neorv32/)
- [NEORV32 RISC-V处理器用户指南](https://stnolting.github.io/neorv32/ug/)

当前页面所支持的版本为NEORV32 v1.11.6。

<a id="supported-board-targets"></a>

### 支持的开发板目标（Supported Board Targets）

Zephyr支持以下NEORV32开发板目标：


- `neorv32/neorv32/minimalboot`
- `neorv32/neorv32/up5kdemo`

每个目标对应NEORV32 RTL附带的一个处理器模板。可使用[开发板扩展（Board Extensions）](https://docs.zephyrproject.org/latest/hardware/porting/board_porting.html#extend-board)或设备树覆盖文件，在源码树外定制这些目标，以适配自定义NEORV32实现。（[设备树覆盖文件（Devicetree Overlays）](https://docs.zephyrproject.org/latest/build/dts/howtos.html#use-dt-overlays)）

`neorv32`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="neorv32-hw-features"></a>

<a id="neorv32-neorv32/neorv32/minimalboot-hw-features-section"></a>

#### `neorv32/neorv32/minimalboot`目标（Target）

<a id="neorv32-neorv32/neorv32/minimalboot-hw-features-panel"></a>

<a id="neorv32-neorv32/neorv32/minimalboot-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、64 KiB Flash。

<a id="neorv32-neorv32/neorv32/minimalboot-hw-features-table"></a>

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
<td>NEORV32 RISC-V CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P021_neorv32_cpu.md#std-dtcompatible-neorv32-cpu"><code>neorv32,cpu</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NEORV32通用定时器（GPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L89">已禁用：1</a>）</td>
<td><a href="../microchip_soc_counter_binding_reference/P016_neorv32_gptmr.md#std-dtcompatible-neorv32-gptmr"><code>neorv32,gptmr</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>NEORV32通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L137">已启用：1</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P008_neorv32_gpio.md#std-dtcompatible-neorv32-gpio"><code>neorv32,gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/neorv32/neorv32_neorv32_minimalboot.dts?plain=1#L63">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>RISC-V CPU中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P006_riscv_cpu-intc.md#std-dtcompatible-riscv-cpu-intc"><code>riscv,cpu-intc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive RISC-V内核本地中断器（Core-Local Interruptor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P010_sifive_clint0.md#std-dtcompatible-sifive-clint0"><code>sifive,clint0</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/neorv32/neorv32_neorv32_minimalboot.dts?plain=1#L39">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/neorv32/neorv32_neorv32_minimalboot.dts?plain=1#L91">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L65">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NEORV32脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L81">已启用：1</a>）</td>
<td><a href="../pwm_intel_microchip_nxp_binding_reference/P014_neorv32_pwm.md#std-dtcompatible-neorv32-pwm"><code>neorv32,pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>NEORV32真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L130">已禁用：1</a>）</td>
<td><a href="../rng_binding_reference/P012_neorv32_trng.md#std-dtcompatible-neorv32-trng"><code>neorv32,trng</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NEORV32通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L112">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L121">已禁用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P002_neorv32_uart.md#std-dtcompatible-neorv32-uart"><code>neorv32,uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L70">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>系统控制器寄存器读写（System Controller Registers R/W）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L148">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P008_syscon.md#std-dtcompatible-syscon"><code>syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>RISC-V机器模式定时器（Machine Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L104">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer"><code>riscv,machine-timer</code></a></td>
</tr>
</table>

<a id="neorv32-neorv32/neorv32/up5kdemo-hw-features-section"></a>

#### `neorv32/neorv32/up5kdemo`目标（Target）

<a id="neorv32-neorv32/neorv32/up5kdemo-hw-features-panel"></a>

<a id="neorv32-neorv32/neorv32/up5kdemo-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、64 KiB Flash。

<a id="neorv32-neorv32/neorv32/up5kdemo-hw-features-table"></a>

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
<td>NEORV32 RISC-V CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P021_neorv32_cpu.md#std-dtcompatible-neorv32-cpu"><code>neorv32,cpu</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NEORV32通用定时器（GPTMR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L89">已禁用：1</a>）</td>
<td><a href="../microchip_soc_counter_binding_reference/P016_neorv32_gptmr.md#std-dtcompatible-neorv32-gptmr"><code>neorv32,gptmr</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>NEORV32通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L137">已启用：1</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P008_neorv32_gpio.md#std-dtcompatible-neorv32-gpio"><code>neorv32,gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/neorv32/neorv32_neorv32_up5kdemo.dts?plain=1#L63">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>RISC-V CPU中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P006_riscv_cpu-intc.md#std-dtcompatible-riscv-cpu-intc"><code>riscv,cpu-intc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive RISC-V内核本地中断器（Core-Local Interruptor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P010_sifive_clint0.md#std-dtcompatible-sifive-clint0"><code>sifive,clint0</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/neorv32/neorv32_neorv32_up5kdemo.dts?plain=1#L39">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/neorv32/neorv32_neorv32_up5kdemo.dts?plain=1#L91">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L65">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NEORV32脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L81">已启用：1</a>）</td>
<td><a href="../pwm_intel_microchip_nxp_binding_reference/P014_neorv32_pwm.md#std-dtcompatible-neorv32-pwm"><code>neorv32,pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>NEORV32真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L130">已禁用：1</a>）</td>
<td><a href="../rng_binding_reference/P012_neorv32_trng.md#std-dtcompatible-neorv32-trng"><code>neorv32,trng</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NEORV32通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L112">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L121">已禁用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P002_neorv32_uart.md#std-dtcompatible-neorv32-uart"><code>neorv32,uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L70">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>系统控制器寄存器读写（System Controller Registers R/W）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L148">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P008_syscon.md#std-dtcompatible-syscon"><code>syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>RISC-V机器模式定时器（Machine Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/neorv32.dtsi?plain=1#L104">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer"><code>riscv,machine-timer</code></a></td>
</tr>
</table>

<a id="supported-features"></a>

## 支持的功能（Supported Features）

Zephyr支持以下NEORV32功能，受支持的开发板目标已预配置这些功能，也可按自定义NEORV32实现修改。

<a id="system-clock"></a>

### 系统时钟（System Clock）

默认配置从NEORV32 SYSINFO模块读取系统时钟频率，产生少量运行时开销。若构建时已知频率，可通过cpu0设备树节点的clock-frequency属性覆盖此行为。

<a id="cpu"></a>

### 中央处理器（CPU）

SoC配置假定NEORV32 CPU启用了以下RISC-V指令集（ISA）扩展：


- Zicntr，基本计数器与定时器扩展
- Zicsr，控制与状态寄存器（CSR）指令扩展，始终启用
- Zifencei，指令获取栅栏（Instruction-fetch Fence）扩展，始终启用

可修改cpu0节点的riscv,isa-extensions属性，启用其他受支持的RISC-V ISA扩展。

<a id="core-local-interruptor"></a>

### 核本地中断器（Core Local Interruptor）

支持NEORV32核本地中断器CLINT及其机器定时器MTIMER，但默认禁用。若SoC实现包含这些功能，可将clint及mtimer节点的status设为okay以启用。

<a id="internal-instruction-memory"></a>

### 内部指令存储器（Internal Instruction Memory）

支持用于代码执行的内部指令存储器IMEM，但默认禁用。若SoC实现包含IMEM，可通过imem节点reg属性设置容量，并将status设为okay以启用。

<a id="internal-data-memory"></a>

### 内部数据存储器（Internal Data Memory）

支持内部数据存储器DMEM，但默认禁用。若SoC实现包含DMEM，可通过dmem节点reg属性设置容量，并将status设为okay以启用。

<a id="serial-port"></a>

### 串口（Serial Port）

支持UART0及UART1，但默认禁用。若SoC实现包含其中任一串口，可将uart0和／或uart1节点的status设为okay以启用。

注意（Note）

开发板目标在UART0提供19200波特率控制台，与标准NEORV32引导加载程序一致。可通过uart0节点current-speed属性修改波特率。

<a id="general-purpose-input-output"></a>

### 通用输入输出（GPIO / General Purpose Input/Output）

支持NEORV32 GPIO端口，但默认禁用。若SoC实现包含GPIO，可将gpio节点status设为okay以启用，并通过ngpios属性设置GPIO数量。

<a id="pulse-width-modulation"></a>

### 脉宽调制（PWM / Pulse-Width Modulation）

支持NEORV32 PWM控制器，但默认禁用。若SoC实现包含PWM，可将pwm节点status设为okay以启用。

<a id="true-random-number-generator"></a>

### 真随机数发生器（TRNG / True Random-Number Generator）

支持NEORV32 TRNG，但默认禁用。若SoC实现包含TRNG，可将trng节点status设为okay以启用。

<a id="general-purpose-timer"></a>

### 通用定时器（GPTMR / General Purpose Timer）

支持NEORV32 GPTMR，但默认禁用。若SoC实现包含GPTMR，可将gptmr节点status设为okay以启用，并通过prescaler属性选择所需时钟预分频器。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`neorv32`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>调试服务器（debugserver）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

首先按NEORV32用户指南，将NEORV32位流加载到FPGA。

接着按通常方式构建和烧录应用，详情见[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)及[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)。

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

在串口终端中使用以下设置，例如minicom或PuTTY：


- 波特率：19200
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing-via-jtag"></a>

### 通过JTAG烧录

以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例，通过JTAG构建并烧录NEORV32应用。JTAG烧录要求SoC实现同时启用片上调试器（OCD）及引导加载程序。

注意（Note）

若未启用引导加载程序，内部指令存储器IMEM将配置为ROM，无法通过JTAG修改。

```text
# From the root of the zephyr repository
west build -b neorv32/neorv32/<variant> samples/hello_world
west flash
```

默认OpenOCD配置与NEORV32项目提供的示例类似。烧录时传入额外参数也可使用其他JTAG探针，例如以2 kHz使用Flyswatter JTAG：（[OpenOCD调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#openocd-debug-host-tools)）

```text
# From the root of the zephyr repository
west build -b neorv32/neorv32/<variant> samples/hello_world
west flash --config interface/ftdi/flyswatter.cfg --config neorv32.cfg --cmd-pre-init 'adapter speed 2000'
```

烧录后，终端中应出现类似以下消息：

```text
*** Booting Zephyr OS build zephyr-vn.n.nn  ***
Hello World! neorv32/neorv32/<variant>
```

但上述步骤不会将应用持久化到闪存，只会将其写入FPGA内部块RAM（Block RAM）。下次配置FPGA时，会恢复为FPGA位流所包含的块RAM初始应用。

将应用固化到FPGA位流的步骤见NEORV32用户指南。启用[CONFIG_BUILD_OUTPUT_BIN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_OUTPUT_BIN)且NEORV32 image_gen可执行文件可用时，构建系统自动生成zephyr.vhd，用于初始化NEORV32内部指令存储器。

<a id="index-0"></a>

自动检测image_gen要求其位于[PATH](../toolchains/P003_环境变量.md#envvar-PATH)环境变量中，也可在构建时显式传入路径：

```text
# From the root of the zephyr repository
west build -b neorv32/neorv32/<variant> samples/hello_world -- -DCMAKE_PROGRAM_PATH=<path/to/neorv32/sw/image_gen/>
```

<a id="uploading-via-uart"></a>

### 通过UART上传

启用[CONFIG_BUILD_OUTPUT_BIN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_OUTPUT_BIN)且NEORV32 image_gen可执行文件可用时，构建系统自动生成zephyr_exe.bin，供内置引导加载程序上传，步骤见NEORV32用户指南。

<a id="debugging-via-jtag"></a>

### 通过JTAG调试

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b neorv32/neorv32/<variant> samples/hello_world
west debug
```

在调试器中单步执行应用，终端中应出现类似以下消息：

```text
*** Booting Zephyr OS build zephyr-vn.n.nn  ***
Hello World! neorv32/neorv32/<variant>
```

## 译注

原文支持版本为NEORV32 v1.11.6。各外设默认禁用与具体目标预配置分开描述；IMEM／DMEM容量、ISA扩展和时钟可通过设备树设置。JTAG烧录需OCD及引导程序，否则IMEM作为ROM不可修改；保留固化VHDL与UART上传两种产物。

---

[上一章](P013_JZ-F407VET6_Industrial_Control_Board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P015_Pro_Micro_nRF52840.md)
