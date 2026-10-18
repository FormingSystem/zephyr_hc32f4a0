---
id: learning.zephyr-docs.boards-amd.page-10
title: Versal Net APU Development Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/amd/versalnet_apu/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="versalnet_apu"></a>

# 第10章\_Versal Net应用处理单元开发板（APU Development Board）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/amd/versalnet_apu/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`versalnet_apu`

厂商（Vendor）：

[Advanced Micro Devices（AMD）, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=amd)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[amd_versalnet_apu](https://docs.zephyrproject.org/latest/boards/index.html#soc=amd_versalnet_apu)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/amd/versalnet_apu/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

此配置为AMD Versal Net片上系统上的A78应用处理单元（APU）提供支持，可采用以下工作方式：


- 四个独立A78集群，每个集群包含四个A78内核

该处理单元基于ARM Cortex-A78 CPU，还启用以下设备：


- ARM GIC v3中断控制器（Interrupt Controller）
- 全局定时计数器（Global Timer Counter）
- 服务器基础系统架构通用异步收发器（SBSA UART）

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`versalnet_apu`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="versalnet_apu-hw-features"></a>

<a id="versalnet_apu-versalnet_apu/amd_versalnet_apu-hw-features-section"></a>

#### `versalnet_apu/amd_versalnet_apu`目标（Target）

<a id="versalnet_apu-versalnet_apu/amd_versalnet_apu-hw-features-panel"></a>

<a id="versalnet_apu-versalnet_apu/amd_versalnet_apu-hw-features-memory"></a>

该开发板目标的片上存储容量：2 GiB RAM、N/A Flash。

<a id="versalnet_apu-versalnet_apu/amd_versalnet_apu-hw-features-table"></a>

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
<td>ARM Cortex-A78处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/versalnet_a78.dtsi?plain=1#L23">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P015_arm_cortex-a78.md#std-dtcompatible-arm-cortex-a78"><code>arm,cortex-a78</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/amd/versalnet_apu/versalnet_apu.dts?plain=1#L17">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Xilinx ADMA直接存储器访问控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versalnet_apu.dtsi?plain=1#L40">已启用：8</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P018_xlnx_zynqmp-dma-1.0.md#std-dtcompatible-xlnx-zynqmp-dma-1.0"><code>xlnx,zynqmp-dma-1.0</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/versalnet_a78.dtsi?plain=1#L70">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>片上（On-Chip）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）1.1版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/versalnet_a78.dtsi?plain=1#L52">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-1.1.html#std-dtcompatible-arm-psci-1.1"><code>arm,psci-1.1</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM服务器基础系统架构通用异步收发器（SBSA UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versalnet_apu.dtsi?plain=1#L24">已启用：2</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P009_arm_sbsa-uart.md#std-dtcompatible-arm-sbsa-uart"><code>arm,sbsa-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/amd/versalnet_apu/versalnet_apu.dts?plain=1#L29">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/versalnet_a78.dtsi?plain=1#L57">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="versalnet_apu-versalnet_apu/amd_versalnet_apu/smp-hw-features-section"></a>

#### `versalnet_apu/amd_versalnet_apu/smp`目标（Target）

<a id="versalnet_apu-versalnet_apu/amd_versalnet_apu/smp-hw-features-panel"></a>

<a id="versalnet_apu-versalnet_apu/amd_versalnet_apu/smp-hw-features-memory"></a>

该开发板目标的片上存储容量：2 GiB RAM、N/A Flash。

<a id="versalnet_apu-versalnet_apu/amd_versalnet_apu/smp-hw-features-table"></a>

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
<td>ARM Cortex-A78处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/versalnet_a78.dtsi?plain=1#L23">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P015_arm_cortex-a78.md#std-dtcompatible-arm-cortex-a78"><code>arm,cortex-a78</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/amd/versalnet_apu/versalnet_apu.dts?plain=1#L17">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Xilinx ADMA直接存储器访问控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versalnet_apu.dtsi?plain=1#L40">已启用：8</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P018_xlnx_zynqmp-dma-1.0.md#std-dtcompatible-xlnx-zynqmp-dma-1.0"><code>xlnx,zynqmp-dma-1.0</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/versalnet_a78.dtsi?plain=1#L70">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>片上（On-Chip）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）1.1版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/versalnet_a78.dtsi?plain=1#L52">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-1.1.html#std-dtcompatible-arm-psci-1.1"><code>arm,psci-1.1</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM服务器基础系统架构通用异步收发器（SBSA UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versalnet_apu.dtsi?plain=1#L24">已启用：2</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P009_arm_sbsa-uart.md#std-dtcompatible-arm-sbsa-uart"><code>arm,sbsa-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/amd/versalnet_apu/versalnet_apu.dts?plain=1#L29">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/versalnet_a78.dtsi?plain=1#L57">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="devices"></a>

### 设备（Devices）

<a id="system-timer"></a>

#### 系统定时器（System Timer）

此开发板配置采用100 MHz的系统定时器节拍频率（Tick Frequency）。

<a id="serial-port"></a>

#### 串口（Serial Port）

此开发板配置使用片上UART0作为唯一的串行通信通道。

<a id="memories"></a>

#### 存储器（Memories）

虽然DTS文件定义了闪存（Flash）、DDR和片上存储器（OCM）区域，但应用的全部代码和数据都加载到指向DDR存储器的`sram0`区域。目前`ocm0`区域可供使用，只是默认不在其中放置内容。

<a id="known-problems-or-limitations"></a>

### 已知问题或限制（Known Problems or Limitations）

不支持以下平台功能：


- 仅支持A78子系统第一个集群中的第一个CPU。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`versalnet_apu`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>调试服务器（debugserver）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-xsdb">xsdb</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
</tr>
</table>

按通常方式构建和烧录。以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b versalnet_apu samples/hello_world
west flash
```

控制台上应显示以下消息：

```text
Hello World! versalnet_apu/amd_versalnet_apu
```

<a id="references"></a>

## 参考资料（References）


1. ARMv8-A架构参考手册（Architecture Reference Manual），ARM DDI 0487
2. Arm Cortex-A78内核技术参考手册（Core Technical Reference Manual），Doc ID 101430

## 译注

官方自动生成目标表含smp目标，而限制段落仍写仅支持首个CPU；译文同时保留，未据此补造多核支持结论。

---

[上一章](P009_AMD_Versal_RPU_Cortex-R5.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_Versal_NET_RPU_development_board.md)
