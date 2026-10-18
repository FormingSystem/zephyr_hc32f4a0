---
id: learning.zephyr-docs.boards-retronix-sifli.page-10
title: SC-OBC Module V1
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/sc/scobc_v1/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="scobc_v1"></a>

# 第10章\_SC-OBC Module V1

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/sc/scobc_v1/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/scobc_v1.webp](images/scobc_v1.webp)](images/scobc_v1.webp)

SC-OBC Module V1

名称（Name）：

`scobc_v1`

厂商（Vendor）：

[Space Cubics Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=sc)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)、[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[miv](https://docs.zephyrproject.org/latest/boards/index.html#soc=miv)、[versal_rpu](https://docs.zephyrproject.org/latest/boards/index.html#soc=versal_rpu)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/sc/scobc_v1/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id3"></a>

[Space Cubics](https://spacecubics.com/) [注1](#id2) OBC Module V1（SC-OBC Module V1）是用于可靠实时控制及边缘处理的航天器机载计算机（Onboard Computer），基于AMD Versal自适应SoC及Microchip IGLOO2 FPGA，面向地球轨道及月球任务等严苛环境。

Versal侧结合通用处理器、可编程逻辑及向量处理器构成的异构架构，运行目标检测、图像压缩／分割及高速信号处理等在轨任务，同时让飞行关键任务遵循Zephyr RTOS可预测的调度模型。

IGLOO2侧作为安全处理器（Safety Processor），监督主系统，提供独立看门狗及故障管理路径，并协调安全模式切换，以提高容错能力。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`scobc_v1`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="scobc_v1-hw-features"></a>

<a id="scobc_v1-scobc_v1/miv-hw-features-section"></a>

#### `scobc_v1/miv`目标（Target）

<a id="scobc_v1-scobc_v1/miv-hw-features-panel"></a>

<a id="scobc_v1-scobc_v1/miv-hw-features-memory"></a>

该开发板目标的片上存储容量：128 KiB RAM、512 KiB Flash。

<a id="scobc_v1-scobc_v1/miv-hw-features-table"></a>

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
<td>通用RISC-V处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sc/scobc_v1/scobc_v1_miv.dts?plain=1#L27">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P034_riscv.md#std-dtcompatible-riscv"><code>riscv</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>板载（On-Board）</td>
<td>Microchip IGLOO2嵌入式非易失性存储器（eNVM）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sc/scobc_v1/scobc_v1_miv.dts?plain=1#L83">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P021_microchip_igloo2-envm-controller.md#std-dtcompatible-microchip-igloo2-envm-controller"><code>microchip,igloo2-envm-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>RISC-V CPU中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sc/scobc_v1/scobc_v1_miv.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P006_riscv_cpu-intc.md#std-dtcompatible-riscv-cpu-intc"><code>riscv,cpu-intc</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>SiFive RISCV-V平台级中断控制器（PLIC / Platform-Local Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sc/scobc_v1/scobc_v1_miv.dts?plain=1#L50">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P009_sifive_plic-1.0.0.md#std-dtcompatible-sifive-plic-1.0.0"><code>sifive,plic-1.0.0</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sc/scobc_v1/scobc_v1_miv.dts?plain=1#L95">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>SiFive UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sc/scobc_v1/scobc_v1_miv.dts?plain=1#L61">已启用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P017_microchip_coreuart.md#std-dtcompatible-microchip-coreuart"><code>microchip,coreuart</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Xilinx UART Lite硬件IP（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sc/scobc_v1/scobc_v1_miv.dts?plain=1#L109">已禁用：1</a>）</td>
<td><a href="../uart_ti_wch_virtual_binding_reference/P010_xlnx_xps-uartlite-1.00.a.md#std-dtcompatible-xlnx-xps-uartlite-1.00.a"><code>xlnx,xps-uartlite-1.00.a</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sc/scobc_v1/scobc_v1_miv.dts?plain=1#L77">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>RISC-V机器模式定时器（Machine Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sc/scobc_v1/scobc_v1_miv.dts?plain=1#L69">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer"><code>riscv,machine-timer</code></a></td>
</tr>
</table>

<a id="scobc_v1-scobc_v1/versal_rpu-hw-features-section"></a>

#### `scobc_v1/versal_rpu`目标（Target）

<a id="scobc_v1-scobc_v1/versal_rpu-hw-features-panel"></a>

<a id="scobc_v1-scobc_v1/versal_rpu-hw-features-memory"></a>

该开发板目标的片上存储容量：128 KiB RAM、128 KiB Flash。

<a id="scobc_v1-scobc_v1/versal_rpu-hw-features-table"></a>

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

开发板提供50 MHz参考振荡器用于生成时钟，实时处理单元（RPU，Cortex-R5F）默认运行于600 MHz。

Zephyr中的“系统时钟”指内核节拍基准（Tick Base）：周期节拍构建默认为100 Hz，无节拍（Tickless）构建默认为10 kHz，即10000 Hz。详情见[CONFIG_SYS_CLOCK_TICKS_PER_SEC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_CLOCK_TICKS_PER_SEC)。

<a id="serial-port"></a>

### 串口（Serial Port）

SC-OBC Module V1具有多个UART端口，主要端口连接评估板上的FT4232H，因此通过USB Type-C连接电脑时，主机会枚举这些端口。


- 端口A用于JTAG。
- 端口B通过Bank 502的LPD MIO第0脚RXD及第1脚TXD连接UART0。
- 端口C通过Bank 502的LPD MIO第4脚TXD及第5脚RXD连接UART1。Versal RPU上的Zephyr在scobc_v1_versal_rpu.dts中选择UART1作为默认控制台；Linux主机上通常类似/dev/ttyUSB2，实际设备编号可能不同。
- 端口D连接IGLOO2。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`scobc_v1`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
west build -b scobc_v1/versal_rpu samples/hello_world
west flash --pdi /path/to/your.pdi
```

烧录后，终端中应出现类似以下消息：

```text
*** Booting Zephyr OS build v4.2.0 ***
Hello World! scobc_v1/versal_rpu
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://spacecubics.com/](https://spacecubics.com/)

## 译注

SC-OBC V1分别列IGLOO2侧Mi-V及Versal RPU目标。600 MHz为RPU处理器时钟，100 Hz／10 kHz是内核节拍频率，不能混为一谈；默认RPU控制台经FT4232H端口C的UART1。

---

[上一章](P009_SC-OBC_Module_A1.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_FireCuda_Gaming_SSD_FaZe_board.md)
