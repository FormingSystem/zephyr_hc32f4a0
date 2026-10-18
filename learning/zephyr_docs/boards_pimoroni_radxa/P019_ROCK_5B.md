---
id: learning.zephyr-docs.boards-pimoroni-radxa.page-19
title: ROCK 5B
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/radxa/rock_5b_plus/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rock_5b_plus"></a>

# 第19章\_ROCK 5B+

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/radxa/rock_5b_plus/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`rock_5b_plus`

厂商（Vendor）：

[Radxa](https://docs.zephyrproject.org/latest/boards/index.html#vendor=radxa)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[rk3588](https://docs.zephyrproject.org/latest/boards/index.html#soc=rk3588)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/radxa/rock_5b_plus/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Radxa ROCK 5B+是一款基于Rockchip RK3588的单板计算机（Single-board Computer）。SoC组合了4个Cortex-A76及4个Cortex-A55 CPU核。开发板最高提供32 GB LPDDR5内存，并带有eMMC、microSD、PCIe、USB、以太网及40引脚扩展排针。

对称多处理（SMP）变体支持全部4个Cortex-A55及4个Cortex-A76核。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`rock_5b_plus`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="rock_5b_plus-hw-features"></a>

<a id="rock_5b_plus-rock_5b_plus/rk3588-hw-features-section"></a>

#### `rock_5b_plus/rk3588`目标（Target）

<a id="rock_5b_plus-rock_5b_plus/rk3588-hw-features-panel"></a>

<a id="rock_5b_plus-rock_5b_plus/rk3588-hw-features-memory"></a>

该开发板目标的片上存储容量：128 MiB RAM、N/A Flash。

<a id="rock_5b_plus-rock_5b_plus/rk3588-hw-features-table"></a>

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
<td rowspan="3">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Rockchip RK3588千兆以太网媒体访问控制器（GMAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L154">已禁用：2</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P018_rockchip_rk3588-gmac.md#std-dtcompatible-rockchip-rk3588-gmac"><code>rockchip,rk3588-gmac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 的管理数据输入输出控制器（MDIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L173">已禁用：2</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P010_snps_dwmac-mdio.md#std-dtcompatible-snps-dwmac-mdio"><code>snps,dwmac-mdio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 精确时间协议时钟（Precision Time Protocol，PTP Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L180">已禁用：2</a>）</td>
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
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/radxa/rock_5b_plus/rock_5b_plus.dts?plain=1#L21">已启用：1</a>）</td>
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

<a id="rock_5b_plus-rock_5b_plus/rk3588/smp-hw-features-section"></a>

#### `rock_5b_plus/rk3588/smp`目标（Target）

<a id="rock_5b_plus-rock_5b_plus/rk3588/smp-hw-features-panel"></a>

<a id="rock_5b_plus-rock_5b_plus/rk3588/smp-hw-features-memory"></a>

该开发板目标的片上存储容量：128 MiB RAM、N/A Flash。

<a id="rock_5b_plus-rock_5b_plus/rk3588/smp-hw-features-table"></a>

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
<td rowspan="3">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Rockchip RK3588千兆以太网媒体访问控制器（GMAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L154">已禁用：2</a>）</td>
<td><a href="../ethernet_phy_renesas_rockchip_binding_reference/P018_rockchip_rk3588-gmac.md#std-dtcompatible-rockchip-rk3588-gmac"><code>rockchip,rk3588-gmac</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 的管理数据输入输出控制器（MDIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L173">已禁用：2</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P010_snps_dwmac-mdio.md#std-dtcompatible-snps-dwmac-mdio"><code>snps,dwmac-mdio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare MAC 精确时间协议时钟（Precision Time Protocol，PTP Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588.dtsi?plain=1#L180">已禁用：2</a>）</td>
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
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/radxa/rock_5b_plus/rock_5b_plus.dts?plain=1#L21">已启用：1</a>）</td>
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

Zephyr目前尚不支持板载以太网接口。

<a id="serial-port"></a>

### 串口（Serial Port）

Zephyr使用UART2作为串行控制台，速率为1.5 Mbit/s。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`rock_5b_plus`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

应用使用标准配置构建，例如：

```text
# From the root of the zephyr repository
west build -b rock_5b_plus samples/hello_world
```

若需在全部8个CPU核上运行Zephyr，请构建SMP变体：

```text
# From the root of the zephyr repository
west build -b rock_5b_plus//smp samples/synchronization
```

创建传统格式U-Boot镜像（Legacy U-Boot Image），使其有效载荷加载并运行于0x10000000：

```text
mkimage -C none -A arm64 -O linux -a 0x10000000 -e 0x10000000 \
  -d build/zephyr/zephyr.bin build/zephyr/zephyr.img
```

Radxa U-Boot的AArch64 Linux启动流程需要设备树（Devicetree）。请从Radxa Linux发行版获取rk3588-rock-5b-plus.dtb，将其与zephyr.img一起复制到U-Boot可访问的FAT分区。

检查U-Boot提供的内核及设备树临时加载地址：

```text
printenv kernel_addr_r fdt_addr_r
```

将各文件载入其对应地址，再将设备树地址传给bootm。根据所选启动介质调整MMC设备号及分区号：

```text
fatload mmc 1:1 ${kernel_addr_r} zephyr.img
fatload mmc 1:1 ${fdt_addr_r} rk3588-rock-5b-plus.dtb
bootm ${kernel_addr_r} - ${fdt_addr_r}
```

传统镜像头（Legacy Image Header）指示U-Boot在跳转入口之前，将Zephyr有效载荷从kernel_addr_r搬移至0x10000000。分别保留临时镜像、设备树及Zephyr运行区域，可避免交接过程中覆盖其中任何一部分。

<a id="references"></a>

### 参考资料（References）

更多信息见[Radxa ROCK 5B+文档](https://docs.radxa.com/en/rock5/rock5b)。

## 译注

ROCK 5B+支持8核SMP，当前Zephyr不支持板载以太网，UART2控制台为1.5 Mbit/s。传统U-Boot镜像有效载荷在0x10000000运行，临时镜像、设备树及运行区需分开，设备树文件需从Radxa Linux发行版获取。

---

[上一章](P018_Radxa_ROCK_3B.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
