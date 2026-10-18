---
id: learning.zephyr-docs.boards-fanke-to-gardena.page-8
title: ROC-RK3588-PC Quad-core Cortex-A55
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/firefly/roc_rk3588_pc/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="roc_rk3588_pc"></a>

# 第8章\_ROC-RK3588-PC（四核Cortex-A55，标题按原文保留）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/firefly/roc_rk3588_pc/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`roc_rk3588_pc`

厂商（Vendor）：

[Firefly](https://docs.zephyrproject.org/latest/boards/index.html#vendor=firefly)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[rk3588](https://docs.zephyrproject.org/latest/boards/index.html#soc=rk3588)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/firefly/roc_rk3588_pc/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

ROC-RK3588-PC是一台采用Rockchip RK3588的八核64位微型计算机，支持最高32 GB RAM。它具备M.2 PCIe 3.0接口用于扩展NVMe SSD，以及HDMI 2.1、DP 1.4等丰富接口，支持Wi-Fi 6无线传输和千兆以太网，提供高速网络连接。

RK3588是8 nm工艺的八核64位处理器，包含4个Cortex-A76和4个Cortex-A55内核，最高频率2.4 GHz，集成Arm Mali-G610 MP4四核图形处理器（GPU）及内置人工智能加速器（NPU），提供6 TOPS算力。Zephyr OS已移植到该处理器运行。


- 开发板特性（Board Features）：


  - 内存：最高32 GB LPDDR4／LPDDR4x／LPDDR5
  - 存储（Storage）：


    - 最高128 GB eMMC
    - M.2 PCIe 3.0 NVMe SSD，支持2242／2260／2280规格
    - TF卡槽（TF-Card Slot）
  - 无线（Wireless）：


    - 支持Wi-Fi 6（802.11a/b/g/n/ac/ax）
    - 支持蓝牙5.0（BT 5.0）
  - Display:


    - HDMI 2.1，8K、60帧／秒
    - HDMI 2.0，4K、60帧／秒
    - DP 1.4，8K、30帧／秒
  - USB:


    - 2路USB 3.0
    - 1路USB 2.0
    - 1个USB-C接口，支持USB 3.0 OTG／DP 1.4
  - Network:


    - 1路1000 Mbps以太网，RJ45接口
  - Debug:


    - 开发板UART调试端口
  - Other:


    - 6 TOPS算力的神经网络处理器（NPU）
    - Arm Mali-G610 MP4四核GPU
    - 支持OpenGL ES 3.2、OpenCL 2.2、Vulkan 1.1

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`roc_rk3588_pc`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="roc_rk3588_pc-hw-features"></a>

<a id="roc_rk3588_pc-roc_rk3588_pc/rk3588-hw-features-section"></a>

#### `roc_rk3588_pc/rk3588`目标（Target）

<a id="roc_rk3588_pc-roc_rk3588_pc/rk3588-hw-features-panel"></a>

<a id="roc_rk3588_pc-roc_rk3588_pc/rk3588-hw-features-memory"></a>

该开发板目标的片上存储容量：1 MiB RAM、N/A Flash。

<a id="roc_rk3588_pc-roc_rk3588_pc/rk3588-hw-features-table"></a>

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
<td>Arm Cortex-A55 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L23">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P009_arm_cortex-a55.md#std-dtcompatible-arm-cortex-a55"><code>arm,cortex-a55</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Arm Cortex-A76 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L52">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P014_arm_cortex-a76.md#std-dtcompatible-arm-cortex-a76"><code>arm,cortex-a76</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Rockchip RK3588时钟复位单元（CRU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L118">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P023_rockchip_rk3588-cru.md#std-dtcompatible-rockchip-rk3588-cru"><code>rockchip,rk3588-cru</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Rockchip RK3588 CRU时钟控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L123">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P022_rockchip_rk3588-cru-clk.md#std-dtcompatible-rockchip-rk3588-cru-clk"><code>rockchip,rk3588-cru-clk</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Rockchip RK3588千兆以太网媒体访问控制器（GMAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L154">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L186">已禁用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P018_rockchip_rk3588-gmac.md#std-dtcompatible-rockchip-rk3588-gmac"><code>rockchip,rk3588-gmac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 的管理数据输入输出控制器（MDIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L173">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L204">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P010_snps_dwmac-mdio.md#std-dtcompatible-snps-dwmac-mdio"><code>snps,dwmac-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Realtek RTL8211F以太网物理层（PHY）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/firefly/roc_rk3588_pc/roc_rk3588_pc.dts?plain=1#L50">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P012_realtek_rtl8211f.md#std-dtcompatible-realtek-rtl8211f"><code>realtek,rtl8211f</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 精确时间协议时钟（Precision Time Protocol，PTP Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L180">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L211">已禁用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P006_snps_dwmac-ptp-clock.md#std-dtcompatible-snps-dwmac-ptp-clock"><code>snps,dwmac-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L81">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>片上（On-Chip）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L92">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>Rockchip RK3588 CRU复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L129">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P015_rockchip_rk3588-cru-rst.md#std-dtcompatible-rockchip-rk3588-cru-rst"><code>rockchip,rk3588-cru-rst</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L136">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L145">已禁用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/firefly/roc_rk3588_pc/roc_rk3588_pc.dts?plain=1#L21">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>系统控制器寄存器读写（System Controller Registers R/W）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L106">已启用：2</a>）</td>
<td><a href="../edac_syscon_binding_reference/P008_syscon.md#std-dtcompatible-syscon"><code>syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="roc_rk3588_pc-roc_rk3588_pc/rk3588/smp-hw-features-section"></a>

#### `roc_rk3588_pc/rk3588/smp`目标（Target）

<a id="roc_rk3588_pc-roc_rk3588_pc/rk3588/smp-hw-features-panel"></a>

<a id="roc_rk3588_pc-roc_rk3588_pc/rk3588/smp-hw-features-memory"></a>

该开发板目标的片上存储容量：1 MiB RAM、N/A Flash。

<a id="roc_rk3588_pc-roc_rk3588_pc/rk3588/smp-hw-features-table"></a>

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
<td>Arm Cortex-A55 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L23">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P009_arm_cortex-a55.md#std-dtcompatible-arm-cortex-a55"><code>arm,cortex-a55</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Arm Cortex-A76 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L52">已禁用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P014_arm_cortex-a76.md#std-dtcompatible-arm-cortex-a76"><code>arm,cortex-a76</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Rockchip RK3588时钟复位单元（CRU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L118">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P023_rockchip_rk3588-cru.md#std-dtcompatible-rockchip-rk3588-cru"><code>rockchip,rk3588-cru</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Rockchip RK3588 CRU时钟控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L123">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P022_rockchip_rk3588-cru-clk.md#std-dtcompatible-rockchip-rk3588-cru-clk"><code>rockchip,rk3588-cru-clk</code></a></td>
</tr>
<tr>
<td rowspan="4">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Rockchip RK3588千兆以太网媒体访问控制器（GMAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L154">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L186">已禁用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P018_rockchip_rk3588-gmac.md#std-dtcompatible-rockchip-rk3588-gmac"><code>rockchip,rk3588-gmac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 的管理数据输入输出控制器（MDIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L173">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L204">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P010_snps_dwmac-mdio.md#std-dtcompatible-snps-dwmac-mdio"><code>snps,dwmac-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Realtek RTL8211F以太网物理层（PHY）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/firefly/roc_rk3588_pc/roc_rk3588_pc.dts?plain=1#L50">已启用：1</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P012_realtek_rtl8211f.md#std-dtcompatible-realtek-rtl8211f"><code>realtek,rtl8211f</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 精确时间协议时钟（Precision Time Protocol，PTP Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L180">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L211">已禁用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P006_snps_dwmac-ptp-clock.md#std-dtcompatible-snps-dwmac-ptp-clock"><code>snps,dwmac-ptp-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L81">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>片上（On-Chip）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L92">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>Rockchip RK3588 CRU复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L129">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P015_rockchip_rk3588-cru-rst.md#std-dtcompatible-rockchip-rk3588-cru-rst"><code>rockchip,rk3588-cru-rst</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L136">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L145">已禁用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/firefly/roc_rk3588_pc/roc_rk3588_pc.dts?plain=1#L21">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>系统控制器寄存器读写（System Controller Registers R/W）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L106">已启用：2</a>）</td>
<td><a href="../edac_syscon_binding_reference/P008_syscon.md#std-dtcompatible-syscon"><code>syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="devices"></a>

### 设备（Devices）

<a id="system-clock"></a>

#### 系统时钟（System Clock）

此开发板配置使用24 MHz系统时钟。Cortex-A76内核最高运行于2.4 GHz，Cortex-A55内核最高运行于1.8 GHz。

<a id="serial-port"></a>

#### 串口（Serial Port）

此配置通过CPU的UART2使用一个串行通信通道。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`roc_rk3588_pc`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

使用U-Boot将`zephyr.bin`加载到内存并启动：

```text
tftp 0x50000000 zephyr.bin; dcache flush; icache flush; dcache off; icache off; go 0x50000000
```

此配置可运行基础Zephyr应用及内核测试，例如[基础同步（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)示例：

```text
# From the root of the zephyr repository
west build -b roc_rk3588_pc samples/synchronization
west build -t run
```

对于`roc_rk3588_pc//smp`支持，可使用此配置运行Zephyr SMP应用及子系统测试，例如基础同步示例：（[基础同步（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)）

```text
# From the root of the zephyr repository
west build -b roc_rk3588_pc//smp samples/synchronization
west build -t run
```

<a id="references"></a>

### 参考资料（References）

更多信息见Firefly官方网站（Firefly Website）。（[Firefly网站](https://en.t-firefly.com/product/industry/rocrk3588pc.html?theme=pc)）

## 译注

原文标题为Quad-core Cortex-A55，正文则说明RK3588包含4个Cortex-A76及4个Cortex-A55。译文保留标题，并明确正文八核组成。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [rocrk3588pc.html?theme=pc](https://en.t-firefly.com/product/industry/rocrk3588pc.html?theme=pc)：HTTP Error 404: Not Found。

---

[上一章](P007_ROC-RK3568-PC_Quad-core_Cortex-A55.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_FlySky_FS-i6S.md)
