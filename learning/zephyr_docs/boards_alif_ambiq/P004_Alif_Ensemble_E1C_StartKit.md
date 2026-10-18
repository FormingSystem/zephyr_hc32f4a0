---
id: learning.zephyr-docs.boards-alif-ambiq.page-4
title: Alif Ensemble E1C StartKit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/alif/ensemble_e1c_sk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="ensemble_e1c_sk"></a>

# 第4章\_Alif Ensemble E1C入门套件（StartKit）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/alif/ensemble_e1c_sk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/ensemble_e1c_sk.webp](images/ensemble_e1c_sk.webp)](images/ensemble_e1c_sk.webp)

Alif Ensemble E1C入门套件（StartKit）

名称（Name）：

`ensemble_e1c_sk`

厂商（Vendor）：

[Alif Semiconductor](https://docs.zephyrproject.org/latest/boards/index.html#vendor=alif)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[ae1c1f4051920ph0](https://docs.zephyrproject.org/latest/boards/index.html#soc=ae1c1f4051920ph0)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/alif/ensemble_e1c_sk/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Alif Ensemble E1C入门套件是一个低成本单板开发平台，面向Alif Ensemble系列中低功耗、支持人工智能（AI）的E1C微控制器。

E1C系列包含一个CPU集群（Cluster）：


- 高能效实时子系统（RTSS-HE / High Efficiency）：Cortex-M55，最高160 MHz

开发板支持AE1C1F4051920PH0片上系统（SoC）变体，开发板标识为`ensemble_e1c_sk/ae1c1f4051920ph0/rtss_he`。

<a id="id3"></a>

更多开发板信息见[Ensemble E1C StartKit产品页（Product Page）](https://alifsemi.com/support/kits/ensemble-e1cstartkit/)[注1](#id2)。

<a id="hardware"></a>

## 硬件（Hardware）

Ensemble E1C入门套件提供以下硬件组件：


- 板载J-Link调试器（On-Board Debugger），带USB转UART桥
- 高速USB设备接口（High-Speed USB Device Interface）
- mikroBUS Click扩展板插座（Expansion Socket）
- Arducam摄像头排针（Camera Header）
- 两个脉冲密度调制（PDM）数字麦克风
- 多色用户LED
- 用户按键和复位按键
- 用于I/O扩展的GPIO排针

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`ensemble_e1c_sk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="ensemble_e1c_sk-hw-features"></a>

<a id="ensemble_e1c_sk-ensemble_e1c_sk/ae1c1f4051920ph0/rtss_he-hw-features-section"></a>

#### `ensemble_e1c_sk/ae1c1f4051920ph0/rtss_he`目标（Target）

<a id="ensemble_e1c_sk-ensemble_e1c_sk/ae1c1f4051920ph0/rtss_he-hw-features-panel"></a>

<a id="ensemble_e1c_sk-ensemble_e1c_sk/ae1c1f4051920ph0/rtss_he-hw-features-memory"></a>

该开发板目标的片上存储容量：1536 KiB RAM、1945 KiB Flash。

<a id="ensemble_e1c_sk-ensemble_e1c_sk/ae1c1f4051920ph0/rtss_he-hw-features-table"></a>

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
<td>ARM Cortex-M55处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/alif/ensemble/common/ensemble_rtss_he.dtsi?plain=1#L15">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P003_arm_cortex-m55.md#std-dtcompatible-arm-cortex-m55"><code>arm,cortex-m55</code></a></td>
</tr>
<tr>
<td rowspan="4">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/alif/ensemble/common/ensemble_common.dtsi?plain=1#L22">已启用：5</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Alif时钟源多路选择器（Clock Source Multiplexer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/alif/ensemble/common/ensemble_common.dtsi?plain=1#L68">已启用：1</a>）</td>
<td><a href="../timer_reference/P115_Alif时钟多路复用绑定.md#dtbinding-alif-clock-mux"><code>alif,clock-mux</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/alif/ensemble/common/ensemble_common.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../timer_reference/P110_固定比例时钟绑定.md#dtbinding-fixed-factor-clock"><code>fixed-factor-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Alif Semiconductor时钟控制器（Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/alif/ensemble/common/ensemble_common.dtsi?plain=1#L95">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P006_alif_clockctrl.md#std-dtcompatible-alif-clockctrl"><code>alif,clockctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare定时器驱动（Timer Driver）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/alif/ensemble/common/ensemble_common.dtsi?plain=1#L309">已禁用：2</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P006_snps_dw-timers.md#std-dtcompatible-snps-dw-timers"><code>snps,dw-timers</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/alif/ensemble/common/ensemble_common.dtsi?plain=1#L174">已禁用：10</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P021_snps_designware-gpio.md#std-dtcompatible-snps-designware-gpio"><code>snps,designware-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/alif/ensemble/common/ensemble_common.dtsi?plain=1#L275">已禁用：2</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P006_snps_designware-i2c.md#std-dtcompatible-snps-designware-i2c"><code>snps,designware-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P004_ARMv8_1_M_NVIC.md#std-dtcompatible-arm-v8.1m-nvic"><code>arm,v8.1m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/alif/ensemble/common/ensemble_rtss_he.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P006_arm_armv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu"><code>arm,armv8.1m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Alif Semiconductor引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/alif/ensemble/common/ensemble_common.dtsi?plain=1#L114">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P003_alif_pinctrl.md#std-dtcompatible-alif-pinctrl"><code>alif,pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/alif/ensemble/common/ensemble_common.dtsi?plain=1#L138">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/alif/ensemble/common/ensemble_common.dtsi?plain=1#L120">已禁用：5</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P008_ARMv8_1_M_SysTick.md#std-dtcompatible-arm-armv8.1m-systick"><code>arm,armv8.1m-systick</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

板载USB转UART桥由安全隔离区（Secure Enclave）的UART和UART2用户串口共用，通过JP5跳线选择。将JP5移到UART2位置，即短接JP5-3-5和JP5-4-6，即可访问Zephyr控制台。

使用USB线缆将PC连接到PRG USB接口，然后选用串口终端（如minicom或PuTTY），设置如下：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

若希望无需把JP5切回即可使用SETOOLS，可保持JP5在UART2位置，并将1.8 V USB转串口线连接到SEUART排针J10：引脚1为GND，引脚2为SEUART发送线，接线缆RXD；引脚3为SEUART接收线，接线缆TXD。这样可同时访问Zephyr控制台与安全隔离区（Secure Enclave）的UART。

<a id="flashing"></a>

### 烧录（Flashing）

<a id="id4"></a>

Alif Ensemble E1C入门套件使用Alif安全工具包（SETOOLS / Security Toolkit）编程。安装和使用SETOOLS为开发板编程的详细说明见[Ensemble E1C StartKit产品页（Product Page）](https://alifsemi.com/support/kits/ensemble-e1cstartkit/)[注1](#id2)。

为RTSS-HE内核构建应用：

```text
# From the root of the zephyr repository
west build -b ensemble_e1c_sk/ae1c1f4051920ph0/rtss_he samples/hello_world
```

构建后，使用SETOOLS将`build/zephyr/zephyr.bin`二进制文件烧录到开发板。

烧录并复位开发板后，应能在串口控制台看到以下消息：

```text
Hello World! ensemble_e1c_sk/ae1c1f4051920ph0/rtss_he
```

<a id="debugging"></a>

### 调试（Debugging）

开发板支持使用标准SEGGER J-Link工具，通过板载J-Link调试器进行调试。

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔1〕 ([1](#id3),[2](#id4)) [https://alifsemi.com/support/kits/ensemble-e1cstartkit/](https://alifsemi.com/support/kits/ensemble-e1cstartkit/)

---

[上一章](P003_Alif_Ensemble_E1C_Development_Kit.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_Alif_Ensemble_E8_AI_ML_AppKit.md)
