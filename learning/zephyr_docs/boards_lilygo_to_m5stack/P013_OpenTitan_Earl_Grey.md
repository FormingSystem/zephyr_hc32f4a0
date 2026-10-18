---
id: learning.zephyr-docs.boards-lilygo-to-m5stack.page-13
title: OpenTitan Earl Grey
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/lowrisc/opentitan_earlgrey/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="opentitan_earlgrey"></a>

# 第13章\_OpenTitan Earl Grey

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/lowrisc/opentitan_earlgrey/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`opentitan_earlgrey`

厂商（Vendor）：

[lowRISC社区利益公司（Community Interest Company）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=lowrisc)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[opentitan](https://docs.zephyrproject.org/latest/boards/index.html#soc=opentitan)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/lowrisc/opentitan_earlgrey/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id4"></a>

OpenTitan Earl Grey是一款低功耗安全微控制器，面向多种需要硬件安全的场景。OpenTitan GitHub [注2](#id3) 页面提供相关硬件描述语言（HDL）代码、工具和文档。（[OpenTitan GitHub仓库](https://github.com/lowRISC/opentitan)）

<a id="hardware"></a>

## 硬件（Hardware）


- RV32IMCB RISC-V Ibex内核
- 128 kB主SRAM
- 固定频率定时器及常开定时器（AON Timers）
- 32个GPIO
- 4路UART
- 3路I2C
- 2个SPI主机（Host）
- 1个SPI设备端（Device）
- 多种安全外设（Security Peripherals）

<a id="id2"></a>

详细规格见OpenTitan Earl Grey芯片数据手册 [注1](#id1)。（[OpenTitan Earl Grey芯片数据手册（Chip Datasheet）](https://opentitan.org/book/hw/top_earlgrey/doc/specification.html)）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`opentitan_earlgrey`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="opentitan_earlgrey-hw-features"></a>

<a id="opentitan_earlgrey-opentitan_earlgrey/opentitan-hw-features-section"></a>

#### `opentitan_earlgrey/opentitan`目标（Target）

<a id="opentitan_earlgrey-opentitan_earlgrey/opentitan-hw-features-panel"></a>

<a id="opentitan_earlgrey-opentitan_earlgrey/opentitan-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、1 MiB Flash。

<a id="opentitan_earlgrey-opentitan_earlgrey/opentitan-hw-features-table"></a>

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
<td>LowRISC Ibex RISC-V内核（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/lowrisc/opentitan_earlgrey.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P020_lowrisc_ibex.md#std-dtcompatible-lowrisc-ibex"><code>lowrisc,ibex</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>RISC-V CPU中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/lowrisc/opentitan_earlgrey.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P006_riscv_cpu-intc.md#std-dtcompatible-riscv-cpu-intc"><code>riscv,cpu-intc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SiFive RISCV-V平台级中断控制器（PLIC / Platform-Local Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/lowrisc/opentitan_earlgrey.dtsi?plain=1#L76">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P009_sifive_plic-1.0.0.md#std-dtcompatible-sifive-plic-1.0.0"><code>sifive,plic-1.0.0</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/lowrisc/opentitan_earlgrey.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>OpenTitan电源管理（Power Management）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/lowrisc/opentitan_earlgrey.dtsi?plain=1#L70">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P006_lowrisc_opentitan-pwrmgr.md#std-dtcompatible-lowrisc-opentitan-pwrmgr"><code>lowrisc,opentitan-pwrmgr</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>OpenTitan UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/lowrisc/opentitan_earlgrey.dtsi?plain=1#L88">已启用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P015_lowrisc_opentitan-uart.md#std-dtcompatible-lowrisc-opentitan-uart"><code>lowrisc,opentitan-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>OpenTitan SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/lowrisc/opentitan_earlgrey.dtsi?plain=1#L94">已启用：2</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P005_lowrisc_opentitan-spi.md#std-dtcompatible-lowrisc-opentitan-spi"><code>lowrisc,opentitan-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>RISC-V机器模式定时器（Machine Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/lowrisc/opentitan_earlgrey.dtsi?plain=1#L52">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer"><code>riscv,machine-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>OpenTitan常开定时器（Always-On Timer）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/lowrisc/opentitan_earlgrey.dtsi?plain=1#L60">已禁用：1</a>）</td>
<td><a href="../soc_pmic_watchdog_binding_reference/P008_lowrisc_opentitan-aontimer.md#std-dtcompatible-lowrisc-opentitan-aontimer"><code>lowrisc,opentitan-aontimer</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`opentitan_earlgrey`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

<a id="id6"></a>

首先按OpenTitan Verilator安装指南 [注3](#id5) 构建并安装Verilator。（[OpenTitan Verilator安装指南（Setup）](https://opentitan.org/book/doc/getting_started/setup_verilator.html)）

<a id="building-and-flashing"></a>

### 构建与烧录（Building and Flashing）

以下为构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用的示例。原文步骤曾在OpenTitan master分支提交6a3c2e98上测试。

```text
# From the root of the zephyr repository
west build -b opentitan_earlgrey samples/hello_world
```

OpenTitan的Vchip_sim_tb工具可接收Zephyr .elf文件，将其放入仿真闪存。OpenTitan测试ROM随后在仿真中运行，从仿真闪存读取清单头部（Manifest Header），并从入口点开始执行Zephyr。

```text
$OT_HOME/bazel-bin/hw/build.verilator_real/sim-verilator/Vchip_sim_tb --verbose-mem-load \
-r $OT_HOME/bazel-out/k8-fastbuild-ST-2cc462681f62/bin/sw/device/lib/testing/test_rom/test_rom_sim_verilator.39.scr.vmem \
--meminit=otp,$OT_HOME/bazel-out/k8-fastbuild/bin/hw/ip/otp_ctrl/data/img_rma.24.vmem \
--meminit=flash,$ZEPHYR_PATH/build/zephyr/zephyr.elf
```

UART输出：

```text
I00000 test_rom.c:135] Version: earlgrey_silver_release_v5-9599-g6a3c2e988, Build Date: 2023-01-17 16:02:09
I00001 test_rom.c:237] Test ROM complete, jumping to flash (addr: 20000384)!
*** Booting Zephyr OS build zephyr-v3.2.0-3494-gf0729b494b98 ***
Hello World! opentitan_earlgrey
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://opentitan.org/book/hw/top_earlgrey/doc/specification.html](https://opentitan.org/book/hw/top_earlgrey/doc/specification.html)

<a id="id3"></a>

〔[2](#id4)〕 [https://github.com/lowRISC/opentitan](https://github.com/lowRISC/opentitan)

<a id="id5"></a>

〔[3](#id6)〕 [https://opentitan.org/book/doc/getting_started/setup_verilator.html](https://opentitan.org/book/doc/getting_started/setup_verilator.html)

## 译注

原文验证基于OpenTitan master提交6a3c2e98；Vchip_sim_tb加载ELF及测试ROM读取清单头部为仿真流程，不是对实体芯片执行烧录。

---

[上一章](P012_lowRISC.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_ESP32C3_LUATOS_CORE.md)
