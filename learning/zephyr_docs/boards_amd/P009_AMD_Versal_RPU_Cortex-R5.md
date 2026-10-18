---
id: learning.zephyr-docs.boards-amd.page-9
title: AMD Versal RPU Cortex-R5
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/amd/versal_rpu/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="versal_rpu"></a>

# 第9章\_AMD Versal实时处理单元（RPU）Cortex-R5

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/amd/versal_rpu/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`versal_rpu`

厂商（Vendor）：

[Advanced Micro Devices（AMD）, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=amd)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[`versal_rpu`](https://docs.zephyrproject.org/latest/boards/index.html#soc=versal_rpu)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/amd/versal_rpu/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

此配置为AMD Versal器件上的实时处理单元（RPU / Real-Time Processing Unit）提供支持，可采用以下工作方式：


- 两个独立R5内核，各自具有紧耦合存储器（TCM / Tightly Coupled Memories）
- 或者组成带紧耦合存储器（TCM）的单个双核锁步单元（Dual Lock-Step Unit）

该处理单元基于ARM Cortex-R5F CPU，还启用以下设备：


- ARM GIC v2中断控制器（Interrupt Controller）
- Xilinx三通道定时计数器（TTC / Triple Timer Counter）
- 服务器基础系统架构通用异步收发器（SBSA UART）

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`versal_rpu`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="versal_rpu-hw-features"></a>

<a id="versal_rpu-versal_rpu/versal_rpu-hw-features-section"></a>

#### `versal_rpu/versal_rpu`目标（Target）

<a id="versal_rpu-versal_rpu/versal_rpu-hw-features-panel"></a>

<a id="versal_rpu-versal_rpu/versal_rpu-hw-features-memory"></a>

该开发板目标的片上存储容量：2096896 KiB RAM、N/A Flash。

<a id="versal_rpu-versal_rpu/versal_rpu-hw-features-table"></a>

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
<td>ARM Cortex-R5F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/versal_rpu.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P012_arm_cortex-r5f.md#std-dtcompatible-arm-cortex-r5f"><code>arm,cortex-r5f</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal.dtsi?plain=1#L10">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Xilinx Zynq-7000/ZynqMP MIO/EMIO通用输入输出控制器（GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal.dtsi?plain=1#L214">已禁用：2</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P030_xlnx_ps-gpio.md#std-dtcompatible-xlnx-ps-gpio"><code>xlnx,ps-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Xilinx Zynq-7000/ZynqMP MIO/EMIO GPIO控制器组（Bank）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal.dtsi?plain=1#L224">已禁用：6</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P029_xlnx_ps-gpio-bank.md#std-dtcompatible-xlnx-ps-gpio-bank"><code>xlnx,ps-gpio-bank</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v1（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/versal_rpu.dtsi?plain=1#L38">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P002_arm_gic-v1.md#std-dtcompatible-arm-gic-v1"><code>arm,gic-v1</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>AMD-Xilinx处理器间中断邮箱控制器（IPI / Inter Processor Interrupt Mailbox Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal.dtsi?plain=1#L24">已禁用：10</a>）</td>
<td><a href="../intercore_reference/P057_Versal核间中断邮箱绑定.md#dtbinding-xlnx-mbox-versal-ipi-mailbox"><code>xlnx,mbox-versal-ipi-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>Xilinx安全数字／嵌入式多媒体卡主机控制器（SD/EMMC Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal.dtsi?plain=1#L290">已禁用：2</a>）</td>
<td><a href="../sdhc_binding_reference/P021_xlnx_versal-8.9a.md#std-dtcompatible-xlnx-versal-8.9a"><code>xlnx,versal-8.9a</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM服务器基础系统架构通用异步收发器（SBSA UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal.dtsi?plain=1#L134">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal.dtsi?plain=1#L142">已禁用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P009_arm_sbsa-uart.md#std-dtcompatible-arm-sbsa-uart"><code>arm,sbsa-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Cadence串行外设接口控制器（SPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal.dtsi?plain=1#L150">已禁用：2</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P011_cdns_spi.md#std-dtcompatible-cdns-spi"><code>cdns,spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/amd/versal_rpu/versal_rpu.dts?plain=1#L22">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>Xilinx处理系统三通道定时计数器（PS Triple-Timer Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal.dtsi?plain=1#L174">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal.dtsi?plain=1#L184">已禁用：3</a>）</td>
<td><a href="../mcu_timer_binding_reference/P014_xlnx_ttcps.md#std-dtcompatible-xlnx-ttcps"><code>xlnx,ttcps</code></a></td>
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

虽然DTS文件定义了闪存、DDR和紧耦合存储器（TCM）区域，但应用的全部代码和数据都加载到指向DDR存储器的`sram0`区域。目前TCM区域可供使用，只是默认不在其中放置内容。

<a id="known-problems-or-limitations"></a>

### 已知问题或限制（Known Problems or Limitations）

不支持以下平台功能：


- 仅支持R5子系统的第一个内核。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`versal_rpu`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

在Versal实板上部署时，需要Xilinx系统调试器（XSDB）和可编程器件镜像（PDI）文件。PDI文件包含物理设备所需的硬件初始化和启动配置。

构建应用：

```text
# From the root of the zephyr repository
west build -b versal_rpu samples/hello_world
```

使用PDI文件烧录到实板：

```text
west flash --runner xsdb --pdi /path/to/your.pdi
```

控制台上应显示以下消息：

```text
Hello World! versal_rpu/versal_rpu
```

<a id="references"></a>

## 参考资料（References）


1. ARMv7-A和ARMv7-R架构参考手册（Architecture Reference Manual），ARM DDI 0406C ID051414
2. Cortex-R5和Cortex-R5F技术参考手册（Technical Reference Manual），ARM DDI 0460C ID021511
3. Versal自适应计算加速平台技术参考手册（ACAP Technical Reference Manual），AM011

---

[上一章](P008_AMD_Versal_APU_Development_Board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_Versal_Net_APU_Development_Board.md)
