---
id: learning.zephyr-docs.boards-gd-to-iar.page-6
title: GD32F350R-EVAL
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/gd/gd32f350r_eval/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="gd32f350r_eval"></a>

# 第6章\_GD32F350R-EVAL

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/gd/gd32f350r_eval/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/gd32f350r_eval.webp](images/gd32f350r_eval.webp)](images/gd32f350r_eval.webp)

GD32F350R-EVAL

名称（Name）：

`gd32f350r_eval`

厂商（Vendor）：

[兆易创新半导体（GigaDevice Semiconductor）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=gd)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[gd32f350](https://docs.zephyrproject.org/latest/boards/index.html#soc=gd32f350)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32f350r_eval/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

GD32F350R-EVAL是用于设计和调试兆易创新F350 Cortex-M4F高性能微控制器（High Performance MCU）的硬件平台。

GD32F350RBT6采用单核Arm Cortex-M4F MCU，最高108 MHz，支持闪存零等待状态（Zero Wait States）访问，提供128kB Flash、16kB SRAM及55个GPIO。

<a id="hardware"></a>

## 硬件（Hardware）


- GD32F350RBT6微控制器（MCU）
- AT24C02C 2 Kb EEPROM
- 4个用户LED
- 4个用户按键
- 1路USART，J2连接器上的RS232接口
- 1个接到ADC输入的电位器（POT）
- 耳机接口（Headphone Interface）
- Micro SD卡接口
- 2.4英寸TFT LCD，36 × 48，分辨率按原文保留
- 板载GD-Link编程器（Programmer）
- J-Link／SWD连接器

GD32F350 SoC及GD32F350R-EVAL开发板更多信息见：


- [兆易创新Cortex-M4F拓展性能SoC网站（Stretch Performance SoC Website）](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m4/stretch-performance-line/)
- [GD32F350xx数据手册（Datasheet）](http://gd32mcu.com/download/down/document_id/133/path_type/1)
- [GD32F3x0用户手册（User Manual）](http://gd32mcu.com/download/down/document_id/136/path_type/1)
- [GD32F350R-EVAL用户手册（User Manual）](https://www.tme.com/Document/ff0a3609934053c07d78ef8662781da9/GD32350R-EVAL%20User%20Manual-V1.0.pdf)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`gd32f350r_eval`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="gd32f350r_eval-hw-features"></a>

<a id="gd32f350r_eval-gd32f350r_eval/gd32f350-hw-features-section"></a>

#### `gd32f350r_eval/gd32f350`目标（Target）

<a id="gd32f350r_eval-gd32f350r_eval/gd32f350-hw-features-panel"></a>

<a id="gd32f350r_eval-gd32f350r_eval/gd32f350-hw-features-memory"></a>

该开发板目标的片上存储容量：16 KiB RAM、128 KiB Flash。

<a id="gd32f350r_eval-gd32f350r_eval/gd32f350-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L92">已启用：1</a>）</td>
<td><a href="../hardware/P844_GD32模数转换器绑定.md#dtbinding-gd-gd32-adc"><code>gd,gd32-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>兆易创新复位与时钟单元（RCU）时钟控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L43">已启用：1</a>）</td>
<td><a href="../timer_reference/P184_GD32时钟控制绑定.md#dtbinding-gd-gd32-cctl"><code>gd,gd32-cctl</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32系列数模转换器（DAC）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f350.dtsi?plain=1#L12">已禁用：1</a>）</td>
<td><a href="../hardware/P761_GD32数模转换器绑定.md#dtbinding-gd-gd32-dac"><code>gd,gd32-dac</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>GD32直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L104">已禁用：1</a>）</td>
<td><a href="../dma_binding_reference/P017_gd_gd32-dma.md#std-dtcompatible-gd-gd32-dma"><code>gd,gd32-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>GD32闪存控制器（FMC）有三种类型（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P013_gd_gd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller"><code>gd,gd32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>GD32通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L136">已禁用：5</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P027_gd_gd32-gpio.md#std-dtcompatible-gd-gd32-gpio"><code>gd,gd32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>兆易创新复位与时钟单元（RCU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L38">已启用：1</a>）</td>
<td><a href="../hardware/P705_GD32复位与时钟单元绑定.md#dtbinding-gd-gd32-rcu"><code>gd,gd32-rcu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>GD32 FMC v1的闪存绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L64">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P016_gd_gd32-nv-flash-v1.md#std-dtcompatible-gd-gd32-nv-flash-v1"><code>gd,gd32-nv-flash-v1</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>GD32引脚控制器，复用功能模型（AF Model）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L129">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P024_gd_gd32-pinctrl-af.md#std-dtcompatible-gd-gd32-pinctrl-af"><code>gd,gd32-pinctrl-af</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>兆易创新RCU复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L49">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P003_gd_gd32-rctl.md#std-dtcompatible-gd-gd32-rctl"><code>gd,gd32-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>兆易创新通用同步异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L74">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L83">已禁用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P006_gd_gd32-usart.md#std-dtcompatible-gd-gd32-usart"><code>gd,gd32-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>GD32独立看门狗定时器（Free Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L114">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P015_gd_gd32-fwdgt.md#std-dtcompatible-gd-gd32-fwdgt"><code>gd,gd32-fwdgt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>GD32窗口看门狗定时器（Window Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f3x0/gd32f3x0.dtsi?plain=1#L120">已禁用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P016_gd_gd32-wwdgt.md#std-dtcompatible-gd-gd32-wwdgt"><code>gd,gd32-wwdgt</code></a></td>
</tr>
</table>

<a id="serial-port"></a>

### 串口（Serial Port）

GD32F350R-EVAL有一个串行通信端口，默认USART0的TX接PA9、RX接PA10。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`gd32f350r_eval`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

编程前，按以下要求设置启动和串口跳线：


- J4：均选择2–3位置，标为L
- J13：选择1–2位置，标为USART

<a id="using-gd-link"></a>

### 使用GD-Link

GD32F350R-EVAL带有板载GD-Link编程器／调试器，可通过USB烧录和调试。另有SWD排针J3，可配合Segger J-Link等工具使用。


1. 构建Zephyr内核和[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例应用：

  ```text
  west build -b gd32f350r_eval samples/hello_world
  ```
2. 启动串口终端监听输出。在Linux下，设备名通常类似`/dev/ttyUSB0`。例如：

  ```text
  minicom -D /dev/ttyUSB0 -o
  ```

  `-o`选项让`minicom`不发送调制解调器初始化字符串（Modem Initialization String）。连接参数应配置如下：

  > - 速率（Speed）：115200波特率
  > - 数据位（Data）：8位
  > - 奇偶校验（Parity）：无（None）
  > - 停止位（Stop Bits）：1位
3. 烧录镜像：

  ```text
  west build -b gd32f350r_eval samples/hello_world
  west flash
  ```

  终端应显示“Hello World! gd32f350r_eval”。
4. 调试镜像的方法：

  ```text
  west build -b gd32f350r_eval samples/hello_world
  west debug
  ```

## 译注

原文LCD分辨率写36x48，按原文保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [GD32350R-EVAL%20User%20Manual-V1.0.pdf](https://www.tme.com/Document/ff0a3609934053c07d78ef8662781da9/GD32350R-EVAL%20User%20Manual-V1.0.pdf)：HTTP Error 403: Forbidden。

---

[上一章](P005_GD32E507Z-EVAL.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_GD32F403Z-EVAL.md)
