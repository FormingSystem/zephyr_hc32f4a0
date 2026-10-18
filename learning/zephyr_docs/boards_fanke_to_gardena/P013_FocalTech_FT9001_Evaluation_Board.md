---
id: learning.zephyr-docs.boards-fanke-to-gardena.page-13
title: FocalTech FT9001 Evaluation Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/focaltech/ft9001_eval/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="ft9001_eval"></a>

# 第13章\_FocalTech FT9001评估板（Evaluation Board）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/focaltech/ft9001_eval/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/ft9001_eval.webp](images/ft9001_eval.webp)](images/ft9001_eval.webp)

FocalTech FT9001评估板（Evaluation Board）

名称（Name）：

`ft9001_eval`

厂商（Vendor）：

[FocalTech Systems Co., Ltd.（敦泰电子）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=focaltech)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[ft9001](https://docs.zephyrproject.org/latest/boards/index.html#soc=ft9001)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/focaltech/ft9001_eval/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

FT9001-EVAL是FocalTech FT9001 MCU的评估平台，该MCU采用Arm Cortex-M4F，最高160 MHz。

<a id="hardware"></a>

## 硬件（Hardware）


- FocalTech FT9001 SoC，兼容Arm Cortex-M4F
- 32 KB启动只读存储器（Boot ROM）
- 256 KB片上SRAM：


  - 224 KB标准SRAM
  - 32 KB连接DBUS的SRAM
- 2 MB外部闪存，SPI接口
- 2路UART接口
- 2路SPI接口
- 支持中断的外部GPIO引脚

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`ft9001_eval`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="ft9001_eval-hw-features"></a>

<a id="ft9001_eval-ft9001_eval/ft9001-hw-features-section"></a>

#### `ft9001_eval/ft9001`目标（Target）

<a id="ft9001_eval-ft9001_eval/ft9001-hw-features-panel"></a>

<a id="ft9001_eval-ft9001_eval/ft9001-hw-features-memory"></a>

该开发板目标的片上存储容量：224 KiB RAM、2 MiB Flash。

<a id="ft9001_eval-ft9001_eval/ft9001-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/focaltech/ft9001/ft9001.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>FocalTech FT9001时钟与电源管理器（CPM / Clock &amp; Power Manager）说明符使用<code>include/zephyr/dt-bindings/clock/focaltech_ft9001_clock.h</code>中定义的打包ID（Packed IDs）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/focaltech/ft9001/ft9001.dtsi?plain=1#L59">已启用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P005_focaltech_ft9001-cpm.md#std-dtcompatible-focaltech-ft9001-cpm"><code>focaltech,ft9001-cpm</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/focaltech/ft9001/ft9001.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/focaltech/ft9001/ft9001.dtsi?plain=1#L80">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>FocalTech FT9001复位控制器，CPM子节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/focaltech/ft9001/ft9001.dtsi?plain=1#L65">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P002_focaltech_ft9001-cpm-rctl.md#std-dtcompatible-focaltech-ft9001-cpm-rctl"><code>focaltech,ft9001-cpm-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>FocalTech FT9001 USART控制器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/focaltech/ft9001/ft9001.dtsi?plain=1#L90">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/focaltech/ft9001/ft9001.dtsi?plain=1#L99">已禁用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P004_focaltech_ft9001-usart.md#std-dtcompatible-focaltech-ft9001-usart"><code>focaltech,ft9001-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/focaltech/ft9001/ft9001.dtsi?plain=1#L35">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`ft9001_eval`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

<a id="flashing"></a>

### 烧录（Flashing）

构建并烧录[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例应用：

```text
west build -b ft9001_eval samples/hello_world
west flash
```

---

[上一章](P012_Quill_nRF52840_Mesh.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_Framework_LED_Matrix.md)
