---
id: learning.zephyr-docs.boards-intel-ite.page-19
title: Agilex SoC Development Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/intel/socfpga/agilex_socdk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="intel_socfpga_agilex_socdk"></a>

# 第19章\_Agilex SoC开发套件（Development Kit）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/intel/socfpga/agilex_socdk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`intel_socfpga_agilex_socdk`

厂商（Vendor）：

[英特尔公司（Intel Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=intel)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[agilex](https://docs.zephyrproject.org/latest/boards/index.html#soc=agilex)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/intel/socfpga/agilex_socdk/doc/index.rst/../..)<a id="intel-agilex-soc-development-kit"></a>

## Intel Agilex SoC开发套件（Development Kit）

<a id="overview"></a>

### 概述（Overview）

Intel Agilex SoC开发套件提供完整的硬件及软件设计环境，用于开发Intel Agilex F系列FPGA设计。套件适合开发基于Arm处理器的定制SoC设计，以及评估收发器性能（Transceiver Performance）。

<a id="hardware"></a>

### 硬件（Hardware）

Intel Agilex SoC开发套件提供以下硬件特性：


- Intel Agilex F系列FPGA，1400 KLE、2486A封装，集成四核Arm Cortex-A53处理器
- 板载8 GB DDR4内存
- 板载JTAG Intel FPGA Download Cable II下载器
- QSPI闪存子卡（Daughtercard）
- 支持UART及SD卡的HPS OOBE子卡（Daughtercard）

<a id="supported-features"></a>

#### 支持的功能（Supported Features）

`intel_socfpga_agilex_socdk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="intel_socfpga_agilex_socdk-hw-features"></a>

<a id="intel_socfpga_agilex_socdk-intel_socfpga_agilex_socdk/agilex-hw-features-section"></a>

##### `intel_socfpga_agilex_socdk/agilex`目标（Target）

<a id="intel_socfpga_agilex_socdk-intel_socfpga_agilex_socdk/agilex-hw-features-panel"></a>

<a id="intel_socfpga_agilex_socdk-intel_socfpga_agilex_socdk/agilex-hw-features-memory"></a>

该开发板目标的片上存储容量：2 MiB RAM、N/A Flash。

<a id="intel_socfpga_agilex_socdk-intel_socfpga_agilex_socdk/agilex-hw-features-table"></a>

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
<td>ARM Cortex-A53处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex.dtsi?plain=1#L20">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P008_arm_cortex-a53.md#std-dtcompatible-arm-cortex-a53"><code>arm,cortex-a53</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Agilex时钟控制器（Clock Controller）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P011_intel_agilex-clock.md#std-dtcompatible-intel-agilex-clock"><code>intel,agilex-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare定时器驱动（Timer Driver）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex.dtsi?plain=1#L157">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex.dtsi?plain=1#L127">已禁用：3</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P006_snps_dw-timers.md#std-dtcompatible-snps-dw-timers"><code>snps,dw-timers</code></a></td>
</tr>
<tr>
<td rowspan="2">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Cadence Quad-SPI NOR闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex.dtsi?plain=1#L85">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P010_cdns_qspi-nor.md#std-dtcompatible-cdns-qspi-nor"><code>cdns,qspi-nor</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Micron QSPI闪存（Flash）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/intel/socfpga/agilex_socdk/intel_socfpga_agilex_socdk.dts?plain=1#L31">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P026_micron_mt25qu02g.md#std-dtcompatible-micron-mt25qu02g"><code>micron,mt25qu02g</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v2（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex.dtsi?plain=1#L45">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P003_arm_gic-v2.md#std-dtcompatible-arm-gic-v2"><code>arm,gic-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex.dtsi?plain=1#L108">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">平台内服务（Service in Platform）</td>
<td>片上（On-Chip）</td>
<td>Intel Agilex SoC FPGA上用于安全监控调用（SMC）的SiP服务（SVC）驱动实例（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex.dtsi?plain=1#L120">已禁用：1</a>）</td>
<td><a href="../pcie_memory_virtualization_binding_reference/P010_intel_socfpga-agilex-sip-smc.md#std-dtcompatible-intel-socfpga-agilex-sip-smc"><code>intel,socfpga-agilex-sip-smc</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>系统控制器寄存器读写（System Controller Registers R/W）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex.dtsi?plain=1#L67">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P008_syscon.md#std-dtcompatible-syscon"><code>syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex.dtsi?plain=1#L54">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex.dtsi?plain=1#L166">已禁用：4</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P014_snps_designware-watchdog.md#std-dtcompatible-snps-designware-watchdog"><code>snps,designware-watchdog</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

### 烧录与调试（Programming and Debugging）

<a id="boot-flow"></a>

#### 启动流程（Boot Flow）

Zephyr镜像需要由Intel Arm可信固件（ATF）加载。原文将ATF BL2称为第一级引导加载程序（FSBL），将ATF BL31称为第二级引导加载程序（SSBL）。

Zephyr启动流程：

> ATF BL2（EL3）→ ATF BL31（EL3）→ Zephyr（EL2→EL1）

Intel Arm可信固件（ATF）可从GitHub下载：

> [altera-opensource/arm-trusted-firmware](https://github.com/altera-opensource/arm-trusted-firmware.git)

<a id="flashing"></a>

#### 烧录（Flashing）

ATF BL2可从SD卡或QSPI闪存，将Zephyr镜像加载到DDR内存地址`0x10000000`。

<a id="debugging"></a>

#### 调试（Debugging）

Intel Agilex SoC开发套件提供一个板载JTAG连接器，连接Intel USB Blaster下载线即可用于调试。

运行在Cortex-A53内核上的Zephyr应用，可通过观察UART控制台输出进行测试。

<a id="references"></a>

#### 参考资料（References）

[Intel Agilex收发器SoC开发套件（Transceiver-SoC Development Kit）](https://www.intel.com/content/www/us/en/programmable/products/boards_and_kits/dev-kits/altera/kit-agf-si.html)

## 译注

原文将BL31称为第二级引导加载程序SSBL，与Agilex 5页面的描述不同，未静默统一。物理8 GB与构建目标2 MiB、EL2到EL1转换及0x10000000加载地址均按来源保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [kit-agf-si.html](https://www.intel.com/content/www/us/en/programmable/products/boards_and_kits/dev-kits/altera/kit-agf-si.html)：HTTP Error 403: Forbidden。

---

[上一章](P018_Agilex_5_SoC_FPGA_Development_Kit.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P020_Intel_Cyclone_V_SoC_Development_Kit.md)
