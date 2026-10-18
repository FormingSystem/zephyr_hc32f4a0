---
id: learning.zephyr-docs.boards-intel-ite.page-18
title: Agilex 5 SoC FPGA Development Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/intel/socfpga/agilex5_socdk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="intel_socfpga_agilex5_socdk"></a>

# 第18章\_Agilex 5 SoC FPGA开发套件（Development Kit）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/intel/socfpga/agilex5_socdk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`intel_socfpga_agilex5_socdk`

厂商（Vendor）：

[英特尔公司（Intel Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=intel)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[agilex5](https://docs.zephyrproject.org/latest/boards/index.html#soc=agilex5)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/intel/socfpga/agilex5_socdk/doc/index.rst/../..)<a id="intel-agilex-5-soc-fpga-development-kit"></a>

## Intel Agilex 5 SoC FPGA开发套件（Development Kit）

<a id="overview"></a>

### 概述（Overview）

Intel Agilex 5 SoC FPGA开发套件提供完整的硬件及软件设计环境，用于开发基于Intel Agilex 5 E系列的FPGA设计。套件适合开发基于Arm处理器的定制SoC设计，以及边缘智能、嵌入式等应用。

<a id="hardware"></a>

### 硬件（Hardware）

Intel Agilex 5开发套件提供以下硬件特性：


- Intel Agilex 5 E系列FPGA，50K至656K逻辑单元（LE），集成双核Arm A55及双核Arm A76处理器
- 板载8 GB DDR5内存
- 板载JTAG Intel FPGA Download Cable II下载器
- QSPI闪存子卡（Daughtercard）

<a id="supported-features"></a>

#### 支持的功能（Supported Features）

`intel_socfpga_agilex5_socdk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="intel_socfpga_agilex5_socdk-hw-features"></a>

<a id="intel_socfpga_agilex5_socdk-intel_socfpga_agilex5_socdk/agilex5-hw-features-section"></a>

##### `intel_socfpga_agilex5_socdk/agilex5`目标（Target）

<a id="intel_socfpga_agilex5_socdk-intel_socfpga_agilex5_socdk/agilex5-hw-features-panel"></a>

<a id="intel_socfpga_agilex5_socdk-intel_socfpga_agilex5_socdk/agilex5-hw-features-memory"></a>

该开发板目标的片上存储容量：8 MiB RAM、N/A Flash。

<a id="intel_socfpga_agilex5_socdk-intel_socfpga_agilex5_socdk/agilex5-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="2">中央处理器（CPU）</td>
<td>片上（On-Chip）</td>
<td>Arm Cortex-A55 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L23">已启用：2</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P009_arm_cortex-a55.md#std-dtcompatible-arm-cortex-a55"><code>arm,cortex-a55</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Arm Cortex-A76 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L37">已启用：2</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P014_arm_cortex-a76.md#std-dtcompatible-arm-cortex-a76"><code>arm,cortex-a76</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Agilex5时钟控制器（Clock Controller）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L83">已启用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P012_intel_agilex5-clock.md#std-dtcompatible-intel-agilex5-clock"><code>intel,agilex5-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare定时器驱动（Timer Driver）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L199">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L166">已禁用：3</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P006_snps_dw-timers.md#std-dtcompatible-snps-dw-timers"><code>snps,dw-timers</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare AXI DMA控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L354">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L336">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P004_snps_designware-dma-axi.md#std-dtcompatible-snps-designware-dma-axi"><code>snps,designware-dma-axi</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWareCore XGMAC（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L371">已禁用：3</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P005_snps_dwcxgmac.md#std-dtcompatible-snps-dwcxgmac"><code>snps,dwcxgmac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DWC XGMAC MDIO SMA驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L386">已禁用：3</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P009_snps_dwcxgmac-mdio.md#std-dtcompatible-snps-dwcxgmac-mdio"><code>snps,dwcxgmac-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/intel/socfpga/agilex5_socdk/intel_socfpga_agilex5_socdk.dts?plain=1#L76">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Cadence NAND闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L257">已禁用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P009_cdns_nand.md#std-dtcompatible-cdns-nand"><code>cdns,nand</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L109">已启用：2</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P021_snps_designware-gpio.md#std-dtcompatible-snps-designware-gpio"><code>snps,designware-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L271">已禁用：5</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P006_snps_designware-i2c.md#std-dtcompatible-snps-designware-i2c"><code>snps,designware-i2c</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L52">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>GIC v3中断转换服务（ITS / Interrupt Translation Service）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L62">已禁用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P005_arm_gic-v3-its.md#std-dtcompatible-arm-gic-v3-its"><code>arm,gic-v3-its</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/intel/socfpga/agilex5_socdk/intel_socfpga_agilex5_socdk.dts?plain=1#L25">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>片上（On-Chip）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）1.1版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L89">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-1.1.html#std-dtcompatible-arm-psci-1.1"><code>arm,psci-1.1</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>Intel SoC FPGA复位控制器（Reset Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L145">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P004_intel_socfpga-reset.md#std-dtcompatible-intel-socfpga-reset"><code>intel,socfpga-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>Cadence SDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L153">已启用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P005_cdns_sdhc.md#std-dtcompatible-cdns-sdhc"><code>cdns,sdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L133">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">平台内服务（Service in Platform）</td>
<td>片上（On-Chip）</td>
<td>Intel Agilex SoC FPGA上用于安全监控调用（SMC）的SiP服务（SVC）驱动实例（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L249">已禁用：1</a>）</td>
<td><a href="../pcie_memory_virtualization_binding_reference/P010_intel_socfpga-agilex-sip-smc.md#std-dtcompatible-intel-socfpga-agilex-sip-smc"><code>intel,socfpga-agilex-sip-smc</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>系统控制器寄存器读写（System Controller Registers R/W）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L78">已启用：2</a>）</td>
<td><a href="../edac_syscon_binding_reference/P008_syscon.md#std-dtcompatible-syscon"><code>syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L69">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/intel/intel_socfpga_agilex5.dtsi?plain=1#L209">已禁用：5</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P014_snps_designware-watchdog.md#std-dtcompatible-snps-designware-watchdog"><code>snps,designware-watchdog</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

### 烧录与调试（Programming and Debugging）

<a id="zephyr-boot-flow"></a>

### Zephyr启动流程（Boot Flow）

Zephyr镜像需要由Intel Arm可信固件（ATF / Arm Trusted Firmware）加载。ATF BL2是第一级引导加载程序（FSBL），ATF BL31是运行时驻留固件，提供安全监控调用（SMC / Secure Monitor Calls）及电源状态协调接口（PSCI / Power State Coordination Interface）等服务。

启动流程（Boot Flow）：

ATF BL2（EL3）→ ATF BL31（EL3）→ Zephyr（EL1）

Intel Arm可信固件（ATF）可从GitHub下载：

[altera-opensource/arm-trusted-firmware](https://github.com/altera-opensource/arm-trusted-firmware.git)

<a id="flashing"></a>

#### 烧录（Flashing）

ATF BL2可从SD卡、QSPI闪存或NAND，将Zephyr镜像加载到DDR内存地址`0x80000000`。

<a id="debugging"></a>

#### 调试（Debugging）

Intel Agilex 5 SoC开发套件提供一个板载JTAG连接器，连接Intel USB Blaster下载线即可用于调试。

运行在Cortex-A55／A76内核上的Zephyr应用，可通过观察UART控制台输出进行测试。

<a id="references"></a>

#### 参考资料（References）

[Intel Agilex 5 FPGA及SoC FPGA](https://www.intel.in/content/www/in/en/products/details/fpga/agilex/5.html)

## 译注

物理内存8 GB与构建目标可用8 MiB分别保留；此页将BL31定义为运行时驻留固件，加载地址为0x80000000。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [5.html](https://www.intel.in/content/www/in/en/products/details/fpga/agilex/5.html)：HTTP Error 403: Forbidden。

---

[上一章](P017_Raptor_Lake_CRB.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P019_Agilex_SoC_Development_Kit.md)
