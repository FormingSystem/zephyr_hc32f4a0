---
id: learning.zephyr-docs.boards-gd-to-iar.page-2
title: GD32C231C-EVAL
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/gd/gd32c231c_eval/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="gd32c231c_eval"></a>

# 第2章\_GD32C231C-EVAL

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/gd/gd32c231c_eval/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/gd32c231c_eval.webp](images/gd32c231c_eval.webp)](images/gd32c231c_eval.webp)

GD32C231C-EVAL

名称（Name）：

`gd32c231c_eval`

厂商（Vendor）：

[兆易创新半导体（GigaDevice Semiconductor）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=gd)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[gd32c231](https://docs.zephyrproject.org/latest/boards/index.html#soc=gd32c231)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32c231c_eval/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

GD32C231C-EVAL是一块低成本开发平台，支持基于Arm Cortex-M23内核的兆易创新GD32C231C微控制器系列。

GD32C231C8具备以下特性：


- Arm Cortex-M23处理器，最高48 MHz
- 64 KB闪存（Flash）
- 12 KB静态随机存储器（SRAM）
- 低功耗运行（Low Power Operation）
- 多种通信接口：UART、SPI、I2C
- GPIO端口
- 定时器模块（Timer Modules）
- ADC与比较器（Comparator）

<a id="hardware"></a>

## 硬件（Hardware）


- 微控制器（MCU）：GD32C231C8T6
- 晶体：用于高速外部晶体时钟（HXTAL）的8 MHz外部晶体
- LED：4个用户LED，LED1至LED4
- 调试：SWD接口

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`gd32c231c_eval`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="gd32c231c_eval-hw-features"></a>

<a id="gd32c231c_eval-gd32c231c_eval/gd32c231-hw-features-section"></a>

#### `gd32c231c_eval/gd32c231`目标（Target）

<a id="gd32c231c_eval-gd32c231c_eval/gd32c231-hw-features-panel"></a>

<a id="gd32c231c_eval-gd32c231c_eval/gd32c231-hw-features-memory"></a>

该开发板目标的片上存储容量：12 KiB RAM、64 KiB Flash。

<a id="gd32c231c_eval-gd32c231c_eval/gd32c231-hw-features-table"></a>

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
<td>Arm Cortex-M23 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32c2x1/gd32c2x1.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P020_arm_cortex-m23.md#std-dtcompatible-arm-cortex-m23"><code>arm,cortex-m23</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>兆易创新复位与时钟单元（RCU）时钟控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32c2x1/gd32c2x1.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../timer_reference/P184_GD32时钟控制绑定.md#dtbinding-gd-gd32-cctl"><code>gd,gd32-cctl</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>GD32闪存控制器（FMC）有三种类型（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32c2x1/gd32c2x1.dtsi?plain=1#L55">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P013_gd_gd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller"><code>gd,gd32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>GD32通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32c2x1/gd32c2x1.dtsi?plain=1#L127">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32c2x1/gd32c2x1.dtsi?plain=1#L137">已禁用：3</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P027_gd_gd32-gpio.md#std-dtcompatible-gd-gd32-gpio"><code>gd,gd32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>兆易创新外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32c2x1/gd32c2x1.dtsi?plain=1#L106">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P007_gd_gd32-exti.md#std-dtcompatible-gd-gd32-exti"><code>gd,gd32-exti</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32c231c_eval/gd32c231c_eval.dts?plain=1#L22">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>兆易创新复位与时钟单元（RCU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32c2x1/gd32c2x1.dtsi?plain=1#L37">已启用：1</a>）</td>
<td><a href="../hardware/P705_GD32复位与时钟单元绑定.md#dtbinding-gd-gd32-rcu"><code>gd,gd32-rcu</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32系统配置寄存器（System Configuration Registers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32c2x1/gd32c2x1.dtsi?plain=1#L100">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P009_gd_gd32-syscfg.md#std-dtcompatible-gd-gd32-syscfg"><code>gd,gd32-syscfg</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>GD32 FMC v1的闪存绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32c2x1/gd32c2x1.dtsi?plain=1#L63">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P016_gd_gd32-nv-flash-v1.md#std-dtcompatible-gd-gd32-nv-flash-v1"><code>gd,gd32-nv-flash-v1</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>GD32引脚控制器，复用功能模型（AF Model）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32c2x1/gd32c2x1.dtsi?plain=1#L120">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P024_gd_gd32-pinctrl-af.md#std-dtcompatible-gd-gd32-pinctrl-af"><code>gd,gd32-pinctrl-af</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>兆易创新RCU复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32c2x1/gd32c2x1.dtsi?plain=1#L48">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P003_gd_gd32-rctl.md#std-dtcompatible-gd-gd32-rctl"><code>gd,gd32-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>兆易创新通用同步异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32c2x1/gd32c2x1.dtsi?plain=1#L73">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32c2x1/gd32c2x1.dtsi?plain=1#L82">已禁用：2</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P006_gd_gd32-usart.md#std-dtcompatible-gd-gd32-usart"><code>gd,gd32-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32c2x1/gd32c2x1.dtsi?plain=1#L31">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="led"></a>

#### 发光二极管（LED）


- `LED1 = PA15`
- `LED2 = PD1`
- `LED3 = PD3`
- `LED4 = PB4`

<a id="uart"></a>

#### 通用异步收发器（UART）


- `USART0_TX = PA9`
- `USART0_RX = PA10`

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`gd32c231c_eval`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>调试服务器（debugserver）</th>
<th>复位（reset）</th>
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

GD32C231C-EVAL内置GD-Link编程器／调试器，通过USB提供CMSIS-DAP SWD接口。推荐使用兆易创新官方GD-Link Utility Programmer烧录工具，也支持OpenOCD及J-Link。

<a id="flashing"></a>

### 烧录（Flashing）

<a id="using-gd-link-utility-programmer"></a>

#### 使用GD-Link Utility Programmer

<a id="id3"></a>

[GD-Link Utility Programmer](https://www.gd32mcu.com/en/download/7?kw=GD32C2)[注1](#id2)是兆易创新面向GD-Link硬件的官方下载工具，支持SWD编程和在线系统编程下载（ISP）。


1. <a id="id5"></a>

  从[兆易创新下载中心](https://www.gigadevice.com/en/download/)（Download Center）[注2](#id4)下载并安装GD-Link Utility Programmer。
2. 构建示例应用：

  ```text
  west build -b gd32c231c_eval samples/hello_world
  ```
3. 通过GD-Link接口对应的USB端口，将开发板连接到计算机。
4. 打开GD-Link Utility Programmer，选择目标器件GD32C231C8T6，加载`build/zephyr/zephyr.hex`，再点击Download（下载）。

<a id="using-openocd"></a>

#### 使用OpenOCD

OpenOCD可通过板载GD-Link CMSIS-DAP接口或外部SWD探针使用：

```text
west build -b gd32c231c_eval samples/hello_world
west flash
```

<a id="using-j-link"></a>

#### 使用J-Link

```text
west build -b gd32c231c_eval samples/hello_world
west flash --runner jlink
```

<a id="debugging"></a>

### 调试（Debugging）

使用板载GD-Link接口或外部SWD探针：

```text
west build -b gd32c231c_eval samples/hello_world
west debug
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.gd32mcu.com/en/download/7?kw=GD32C2](https://www.gd32mcu.com/en/download/7?kw=GD32C2)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.gigadevice.com/en/download/](https://www.gigadevice.com/en/download/)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [](https://www.gigadevice.com/en/download/)：HTTP Error 404: Not Found。

---

[上一章](P001_GD32A503V-EVAL.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_GD32E103V-EVAL.md)
