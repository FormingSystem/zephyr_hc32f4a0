---
id: learning.zephyr-docs.boards-alif-ambiq.page-8
title: Apollo2 EVB
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ambiq/apollo2_evb/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="apollo2_evb"></a>

# 第8章\_Apollo2评估板（EVB）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ambiq/apollo2_evb/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/apollo2-soc-eval-board.webp](images/apollo2-soc-eval-board.webp)](images/apollo2-soc-eval-board.webp)

Apollo2评估板（EVB）

名称（Name）：

`apollo2_evb`

厂商（Vendor）：

[Ambiq Micro, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=ambiq)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[apollo2](https://docs.zephyrproject.org/latest/boards/index.html#soc=apollo2)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ambiq/apollo2_evb/doc/index.rst/../..)Apollo2 EVB是Ambiq推出的开发板，采用其超低功耗Apollo2片上系统（SoC）。

<a id="hardware"></a>

## 硬件（Hardware）

Ambiq Apollo2片上系统（SoC）提供以下硬件功能：


- ARM® Cortex®-M4F内核，带浮点单元（Floating Point Unit）
- 最高工作频率48 MHz
- 16 kB两路组相联缓存（2-Way Associative Cache）
- 最多1 MB闪存（Flash），用于代码和数据
- 最多256 KB低漏电RAM（Low Leakage RAM），用于代码和数据

Apollo2片上系统及可选Apollo2评估板的更多信息：


- [Apollo2 SoC网站（Website）](https://ambiq.com/apollo2/)
- [Apollo2 SoC数据手册（Datasheet）](https://www.fujitsu.com/uk/imagesgig5/Apollo2_Blue_MCU_Data_Sheet_rev0p8.pdf)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`apollo2_evb`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="apollo2_evb-hw-features"></a>

<a id="apollo2_evb-apollo2_evb/apollo2-hw-features-section"></a>

#### `apollo2_evb/apollo2`目标（Target）

<a id="apollo2_evb-apollo2_evb/apollo2-hw-features-panel"></a>

<a id="apollo2_evb-apollo2_evb/apollo2-hw-features-memory"></a>

此开发板目标可用存储器：256 KiB RAM、1 MiB 闪存。

<a id="apollo2_evb-apollo2_evb/apollo2-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo2.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo2.dtsi?plain=1#L11">已启用：2</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">调试（Debug）</td>
<td>片上（On-Chip）</td>
<td>ARMv7仪器化跟踪宏单元（ITM / Instrumentation Trace Macrocell）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo2.dtsi?plain=1#L35">已启用：1</a>）</td>
<td><a href="../debug_binding_reference/P001_ARMv7M_ITM调试绑定.md#std-dtcompatible-arm-armv7m-itm"><code>arm,armv7m-itm</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Ambiq闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo2.dtsi?plain=1#L67">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P005_ambiq_flash-controller.md#std-dtcompatible-ambiq-flash-controller"><code>ambiq,flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo2.dtsi?plain=1#L76">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Ambiq Apollo2引脚控制器（Pin Controller）负责控制引脚功能选择和引脚属性，例如将UART0 TX路由到指定引脚，以及启用上拉电阻（Pull-Ups）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo2.dtsi?plain=1#L105">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P004_ambiq_apollo2-pinctrl.md#std-dtcompatible-ambiq-apollo2-pinctrl"><code>ambiq,apollo2-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Ambiq通用异步收发器控制器（UART Controller），兼容PL011（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo2.dtsi?plain=1#L87">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo2.dtsi?plain=1#L96">已禁用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P005_ambiq_pl011-uart.md#std-dtcompatible-ambiq-pl011-uart"><code>ambiq,pl011-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo2.dtsi?plain=1#L59">已启用：1</a>）</td>
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

### 烧录与调试（Programming and Debugging）

<a id="flashing-an-application"></a>

#### 烧录应用（Flashing an Application）

使用JLINK USB端口将设备连接到主机。以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例应用说明：构建Zephyr内核和应用，然后烧录到设备。

```text
# From the root of the zephyr repository
west build -b apollo2_evb samples/hello_world
west flash
```

注意（Note）

`west flash`要求主机上安装[SEGGER J-Link软件](https://www.segger.com/downloads/jlink)和[pylink](https://github.com/Square/pylink) Python模块。

打开串口终端（如minicom或PuTTY），设置如下：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

复位开发板后，应能在相应串口（Serial Port）看到以下消息：

```text
Hello World! apollo2_evb
```

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [Apollo2_Blue_MCU_Data_Sheet_rev0p8.pdf](https://www.fujitsu.com/uk/imagesgig5/Apollo2_Blue_MCU_Data_Sheet_rev0p8.pdf)：HTTP Error 429: Too Many Requests。

---

[上一章](P007_Alif_Semiconductor.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_Apollo3_Blue_EVB.md)
