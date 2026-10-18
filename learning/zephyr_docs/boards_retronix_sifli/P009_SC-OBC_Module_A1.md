---
id: learning.zephyr-docs.boards-retronix-sifli.page-9
title: SC-OBC Module A1
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/sc/scobc_a1/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="scobc_a1"></a>

# 第9章\_SC-OBC Module A1

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/sc/scobc_a1/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/scobc.jpg](images/scobc.jpg)](images/scobc.jpg)

SC-OBC Module A1

名称（Name）：

`scobc_a1`

厂商（Vendor）：

[Space Cubics Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=sc)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[designstart_fpga_cortex_m3](https://docs.zephyrproject.org/latest/boards/index.html#soc=designstart_fpga_cortex_m3)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/sc/scobc_a1/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id3"></a>

[Space Cubics](https://spacecubics.com/) [注1](#id2) OBC Module A1（SC-OBC Module A1）是面向航天器，尤其3U立方星（CubeSat）的单板计算机。开发板基于Xilinx Artix-7 FPGA，以Arm Cortex-M3作为主CPU。

其设计面向极端温度、真空及空间辐射等严苛太空环境。

此板采用模块形式，需要通过CON1板对板连接器连接I/O底板。这种模块化设计使CubeSat设计者可按任务需求连接及扩展功能。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`scobc_a1`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="scobc_a1-hw-features"></a>

<a id="scobc_a1-scobc_a1@2.0.0/designstart_fpga_cortex_m3-hw-features-section"></a>

#### `scobc_a1@2.0.0/designstart_fpga_cortex_m3`目标（Target）

<a id="scobc_a1-scobc_a1@2.0.0/designstart_fpga_cortex_m3-hw-features-panel"></a>

<a id="scobc_a1-scobc_a1@2.0.0/designstart_fpga_cortex_m3-hw-features-memory"></a>

该开发板目标的片上存储容量：4 MiB RAM、N/A Flash。

<a id="scobc_a1-scobc_a1@2.0.0/designstart_fpga_cortex_m3-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>板载（On-Board）</td>
<td>ARM Cortex-M3处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sc/scobc_a1/scobc_a1.dts?plain=1#L26">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P021_arm_cortex-m3.md#std-dtcompatible-arm-cortex-m3"><code>arm,cortex-m3</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="3">其他绑定（Miscellaneous）</td>
<td>板载（On-Board）</td>
<td>Space Cubics高可靠性存储器（High-reliability Memory，HRMEM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sc/scobc_a1/scobc_a1.dts?plain=1#L41">已启用：1</a>）</td>
<td><code>sc,hrmem</code></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>SC-OBC Module A1系统寄存器（System Register）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sc/scobc_a1/scobc_a1.dts?plain=1#L52">已启用：1</a>）</td>
<td><code>sc,sysreg</code></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>SC-OBC Module A1系统监控器（System Monitor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sc/scobc_a1/scobc_a1.dts?plain=1#L57">已启用：1</a>）</td>
<td><code>sc,sysmon</code></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>板载（On-Board）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sc/scobc_a1/scobc_a1.dts?plain=1#L33">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>Xilinx UART Lite硬件IP（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sc/scobc_a1/scobc_a1.dts?plain=1#L46">已启用：1</a>）</td>
<td><a href="../uart_ti_wch_virtual_binding_reference/P010_xlnx_xps-uartlite-1.00.a.md#std-dtcompatible-xlnx-xps-uartlite-1.00.a"><code>xlnx,xps-uartlite-1.00.a</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
</table>

此移植目前不支持其他硬件功能。

<a id="system-clock"></a>

### 系统时钟（System Clock）

开发板为冗余设计配有两个连接FPGA的24 MHz外部振荡器，FPGA选择其中有效振荡器作为CPU系统时钟来源。选中的信号再送入FPGA时钟管理模块（CMT），默认驱动CPU运行于48 MHz。

<a id="serial-port"></a>

### 串口（Serial Port）

默认配置包含一个SC UART IP，其基本收发寄存器兼容Xilinx UART Lite。该UART为默认控制台，RX及TX分别通过CON1第43及45脚引出。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`scobc_a1`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

<a id="flashing"></a>

### 烧录（Flashing）

下面展示为此板构建并烧录hello_world应用的示例：

下面展示为默认设计构建并烧录[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用的示例：

```text
# From the root of the zephyr repository
west build -b scobc_a1 samples/hello_world
west flash
```

烧录后，终端中应出现类似以下消息：

```text
*** Booting Zephyr OS build v4.1.0-4619-gd571a59b0a43 ***
Hello World! scobc_a1/designstart_fpga_cortex_m3
```

但上述步骤并未将应用持久保存到闪存，只写入FPGA内部RAM。

可使用CMSIS-DAP、FT2232D或FT232R等外部调试适配器烧录。SC-OBC Module A1默认采用CMSIS-DAP接口，例如Raspberry Pi Pico Debug Probe。使用FT2232D或FT232R等适配器时，应在west flash之前通过OPENOCD_INTERFACE环境变量指定接口。

例如：

```text
$ export OPENOCD_INTERFACE=FT2232D
$ west flash

$ export OPENOCD_INTERFACE=FT232R
$ west flash
```

<a id="debugging"></a>

### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b scobc_a1 samples/hello_world
west debug
```

在调试器中单步执行应用，终端中应出现类似以下消息：

```text
*** Booting Zephyr OS build v4.1.0-4619-gd571a59b0a43 ***
Hello World! scobc_a1/designstart_fpga_cortex_m3
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://spacecubics.com/](https://spacecubics.com/)

## 译注

SC-OBC A1的Cortex-M3由Artix-7 FPGA实现，24 MHz振荡器冗余选择后默认生成48 MHz。示例west flash仅写内部RAM，不会持久写入闪存。

---

[上一章](P008_Space_Cubics.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_SC-OBC_Module_V1.md)
