---
id: learning.zephyr-docs.boards-starfive-trenz.page-23
title: Trenz Electronic TE0950
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/trenz/te0950/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="te0950"></a>

# 第23章\_Trenz Electronic TE0950

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/trenz/te0950/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/te0950.webp](images/te0950.webp)](images/te0950.webp)

Trenz Electronic TE0950

名称（Name）：

`te0950`

厂商（Vendor）：

[Trenz Electronic](https://docs.zephyrproject.org/latest/boards/index.html#vendor=trenz)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[versal_rpu](https://docs.zephyrproject.org/latest/boards/index.html#soc=versal_rpu)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/trenz/te0950/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id3"></a>

[Trenz Electronic TE0950-02](http://trenz.org/te0950-info) [注1](#id2)是采用AMD Versal AI Edge器件的自适应SoC评估板，配有最高8 GB DDR4 SDRAM、128 MB SPI闪存及用于配置和数据存储的eMMC，并提供所需各路开关电源。输入输出通过可靠、灵活且兼顾成本的高速连接器引出。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`te0950`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="te0950-hw-features"></a>

<a id="te0950-te0950/versal_rpu-hw-features-section"></a>

#### `te0950/versal_rpu`目标（Target）

<a id="te0950-te0950/versal_rpu-hw-features-panel"></a>

<a id="te0950-te0950/versal_rpu-hw-features-memory"></a>

此板级目标的存储：128 KiB RAM；Flash不适用（N/A）。

<a id="te0950-te0950/versal_rpu-hw-features-table"></a>

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
<td>ARM服务器基础系统架构通用异步收发器（SBSA UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal.dtsi?plain=1#L142">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal.dtsi?plain=1#L134">已禁用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P009_arm_sbsa-uart.md#std-dtcompatible-arm-sbsa-uart"><code>arm,sbsa-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Cadence串行外设接口控制器（SPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal.dtsi?plain=1#L150">已禁用：2</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P011_cdns_spi.md#std-dtcompatible-cdns-spi"><code>cdns,spi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>Xilinx处理系统三通道定时计数器（PS Triple-Timer Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal.dtsi?plain=1#L174">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/amd/versal.dtsi?plain=1#L184">已禁用：3</a>）</td>
<td><a href="../mcu_timer_binding_reference/P014_xlnx_ttcps.md#std-dtcompatible-xlnx-ttcps"><code>xlnx,ttcps</code></a></td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

开发板提供33.333 MHz参考振荡器生成时钟，实时处理单元（RPU，Cortex-R5F）默认运行于600 MHz。

Zephyr中的“系统时钟”指内核节拍基准（Tick Base）：周期节拍构建默认为100 Hz，无节拍（Tickless）构建默认为10 kHz，即10000 Hz。详情见[CONFIG_SYS_CLOCK_TICKS_PER_SEC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_CLOCK_TICKS_PER_SEC)。

<a id="serial-port"></a>

### 串口（Serial Port）

TE0950-02通过FTDI FT2232H USB接口提供UART，同一USB接口也可用于JTAG。详情见板卡原理图。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`te0950`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

<a id="flashing"></a>

### 烧录（Flashing）

下面展示为此板构建并烧录[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用的示例：

```text
# From the root of the zephyr repository
west build -b te0950 samples/hello_world
west flash --pdi /path/to/your.pdi
```

烧录后，终端中应出现类似以下消息：

```text
*** Booting Zephyr OS build v4.2.0 ***
Hello World! te0950/versal_rpu
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [http://trenz.org/te0950-info](http://trenz.org/te0950-info)

## 译注

TE0950采用Versal AI Edge，原文RPU频率600 MHz、参考时钟33.333 MHz分别保留。FT2232H在同一USB接口提供UART与JTAG功能。

---

[上一章](P022_Trenz_Electronic.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
