---
id: learning.zephyr-docs.boards-intel-ite.page-13
title: INTEL FPGA niosv g
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/intel/niosv_g/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="niosv_g"></a>

# 第13章\_Intel FPGA niosv_g

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/intel/niosv_g/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`niosv_g`

厂商（Vendor）：

[英特尔公司（Intel Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=intel)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[`niosv_g`](https://docs.zephyrproject.org/latest/boards/index.html#soc=niosv_g)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/intel/niosv_g/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

niosv_g开发板基于Intel FPGA Design Store中的Nios V/g Hello World示例设计系统，完整系统由以下IP模块组成：

```text
Nios® V/g Processor Intel® FPGA IP
JTAG UART Intel® FPGA IP
On-Chip Memory Intel® FPGA IP
```

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`niosv_g`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="niosv_g-hw-features"></a>

<a id="niosv_g-niosv_g/niosv_g-hw-features-section"></a>

#### `niosv_g/niosv_g`目标（Target）

<a id="niosv_g-niosv_g/niosv_g-hw-features-panel"></a>

<a id="niosv_g-niosv_g/niosv_g-hw-features-memory"></a>

该开发板目标的片上存储容量：256 KiB RAM、N/A Flash。

<a id="niosv_g-niosv_g/niosv_g-hw-features-table"></a>

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
<td>Intel FPGA NIOSV软核处理器（Softcore Processor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/niosv/niosv-g.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P010_intel_niosv.md#std-dtcompatible-intel-niosv"><code>intel,niosv</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>RISC-V CPU中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/niosv/niosv-g.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P006_riscv_cpu-intc.md#std-dtcompatible-riscv-cpu-intc"><code>riscv,cpu-intc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Altera JTAG UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/niosv/niosv-g.dtsi?plain=1#L55">已启用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P003_altr_jtag-uart.md#std-dtcompatible-altr-jtag-uart"><code>altr,jtag-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/niosv/niosv-g.dtsi?plain=1#L44">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>RISC-V机器模式定时器（Machine Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/niosv/niosv-g.dtsi?plain=1#L48">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer"><code>riscv,machine-timer</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`niosv_g`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

<a id="nios-v-g-hello-world-example-design-system"></a>

### Nios V/g Hello World示例设计系统（Example Design System）

Intel FPGA Design Store提供预构建的Nios V/g Hello World示例设计系统：[https://www.intel.com/content/www/us/en/support/programmable/support-resources/design-examples/design-store.html?s=Newest](https://www.intel.com/content/www/us/en/support/programmable/support-resources/design-examples/design-store.html?s=Newest)

例如，Arria10 Nios V/g处理器示例设计系统的预构建文件可从以下地址下载：[https://www.intel.com/content/www/us/en/design-example/776196/intel-arria-10-fpga-hello-world-design-on-nios-v-g-processor.html](https://www.intel.com/content/www/us/en/design-example/776196/intel-arria-10-fpga-hello-world-design-on-nios-v-g-processor.html)

成功解压所下载的PAR文件后，`ready_to_test/top.sof`即为Hello World示例设计系统的预构建SRAM目标文件（SRAM Object File）。

<a id="create-nios-v-g-processor-example-design-system-in-fpga"></a>

### 在FPGA中创建Nios V/g处理器示例设计系统

使用Intel Quartus Programmer工具，将基于Nios V/g处理器的系统编程到FPGA，并执行应用。

要在FPGA器件内创建Nios V/g处理器，请用以下命令将生成的`.sof`文件下载到开发板。

```text
quartus_pgm -c 1 -m JTAG -o "p;top.sof@1"
```

```text
Note:
-c 1 is referring to JTAG cable number connected to the Host Computer.
@1 is referring to device index on the JTAG Chain and may differ for your board.
top.sof is referring to Nios® V/m processor based system SRAM Object File.
```

<a id="download-zephyr-elf-file-and-run-application"></a>

### 下载Zephyr ELF文件并运行应用

要下载Zephyr可执行与可链接格式（ELF / Executable and Linkable Format）的`.elf`文件，请在Nios V Command Shell环境中使用`niosv-download`命令。

```text
niosv-download -g <elf file>
```

使用JTAG UART终端显示Nios V/g处理器系统的标准输出（stdout）及标准错误（stderr）。

```text
juart-terminal
```

运行Hello World示例时，JTAG UART终端应显示类似以下消息：

```text
*** Booting Zephyr OS build zephyr-vn.n.nn  ***
Hello World! niosv_g
```

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [intel-arria-10-fpga-hello-world-design-on-nios-v-g-processor.html](https://www.intel.com/content/www/us/en/design-example/776196/intel-arria-10-fpga-hello-world-design-on-nios-v-g-processor.html)：HTTP Error 403: Forbidden。
- [design-store.html?s=Newest](https://www.intel.com/content/www/us/en/support/programmable/support-resources/design-examples/design-store.html?s=Newest)：HTTP Error 403: Forbidden。

---

[上一章](P012_Intel_Integrated_Sensor_Hub_ISH.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_INTEL_FPGA_niosv_m.md)
