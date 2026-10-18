---
id: learning.zephyr-docs.boards-arm.page-1
title: BASE RevC 2xAEM Architectural Envelope Model Fixed Virtual Platform
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/arm/fvp_base_revc_2xaem/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="fvp_base_revc_2xaem"></a>

# 第1章\_BASE RevC 2xAEM架构包络模型固定虚拟平台（Architectural Envelope Model / Fixed Virtual Platform）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/arm/fvp_base_revc_2xaem/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`fvp_base_revc_2xaem`

厂商（Vendor）：

[Arm公司（ARM Ltd.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=arm)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

`[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64), [arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)`

片上系统（SoC）：

`[v8a_aarch32](https://docs.zephyrproject.org/latest/boards/index.html#soc=v8a_aarch32), [v9a](https://docs.zephyrproject.org/latest/boards/index.html#soc=v9a), [a320](https://docs.zephyrproject.org/latest/boards/index.html#soc=a320), [v8a](https://docs.zephyrproject.org/latest/boards/index.html#soc=v8a)`

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arm/fvp_base_revc_2xaem/doc/index.rst/../..)<a id="arm-base-revc-2xaem-fixed-virtual-platforms"></a>

## Arm BASE RevC 2xAEM固定虚拟平台（FVP）

<a id="overview"></a>

### 概述（Overview）

此开发板配置使用Arm固定虚拟平台（FVP / Fixed Virtual Platforms）模拟通用架构包络模型（AEM / Architectural Envelope Model）硬件平台，同时支持ARMv8-A及ARMv9-A架构。

此配置支持通用AEM CPU及以下设备：


- 通用中断控制器v3（GICv3）
- ARM架构通用定时器（Architected Generic Timer）
- PL011 UART控制器

<a id="hardware"></a>

### 硬件（Hardware）

<a id="supported-features"></a>

#### 支持的功能（Supported Features）

`fvp_base_revc_2xaem`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="fvp_base_revc_2xaem-hw-features"></a>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/a320-hw-features-section"></a>

##### `fvp_base_revc_2xaem/a320`目标（Target）

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/a320-hw-features-panel"></a>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/a320-hw-features-memory"></a>

该开发板目标的片上存储容量：128 MiB RAM、64 KiB Flash。

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/a320-hw-features-table"></a>

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
<td>Arm Cortex-A320处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L32">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P006_arm_cortex-a320.md#std-dtcompatible-arm-cortex-a320"><code>arm,cortex-a320</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L142">已禁用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P002_smsc_lan91c111.md#std-dtcompatible-smsc-lan91c111"><code>smsc,lan91c111</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111管理数据输入输出（MDIO）驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L150">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P008_smsc_lan91c111-mdio.md#std-dtcompatible-smsc-lan91c111-mdio"><code>smsc,lan91c111-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L156">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>GIC v3中断转换服务（ITS / Interrupt Translation Service）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L85">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P005_arm_gic-v3-its.md#std-dtcompatible-arm-gic-v3-its"><code>arm,gic-v3-its</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L164">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>板载（On-Board）</td>
<td>Arm固定虚拟平台（FVP）电源控制器（PWRC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P003_arm_fvp-pwrc.md#std-dtcompatible-arm-fvp-pwrc"><code>arm,fvp-pwrc</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L103">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L112">已禁用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a-hw-features-section"></a>

##### `fvp_base_revc_2xaem/v8a`目标（Target）

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a-hw-features-panel"></a>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a-hw-features-memory"></a>

该开发板目标的片上存储容量：128 MiB RAM、64 KiB Flash。

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a-hw-features-table"></a>

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
<td>ARM Cortex-A53处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L32">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P008_arm_cortex-a53.md#std-dtcompatible-arm-cortex-a53"><code>arm,cortex-a53</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L142">已禁用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P002_smsc_lan91c111.md#std-dtcompatible-smsc-lan91c111"><code>smsc,lan91c111</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111管理数据输入输出（MDIO）驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L150">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P008_smsc_lan91c111-mdio.md#std-dtcompatible-smsc-lan91c111-mdio"><code>smsc,lan91c111-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L156">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>GIC v3中断转换服务（ITS / Interrupt Translation Service）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L85">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P005_arm_gic-v3-its.md#std-dtcompatible-arm-gic-v3-its"><code>arm,gic-v3-its</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L164">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>板载（On-Board）</td>
<td>Arm固定虚拟平台（FVP）电源控制器（PWRC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P003_arm_fvp-pwrc.md#std-dtcompatible-arm-fvp-pwrc"><code>arm,fvp-pwrc</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L103">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L112">已禁用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a/smp-hw-features-section"></a>

##### `fvp_base_revc_2xaem/v8a/smp`目标（Target）

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a/smp-hw-features-panel"></a>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a/smp-hw-features-memory"></a>

该开发板目标的片上存储容量：128 MiB RAM、64 KiB Flash。

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a/smp-hw-features-table"></a>

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
<td>ARM Cortex-A53处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L32">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P008_arm_cortex-a53.md#std-dtcompatible-arm-cortex-a53"><code>arm,cortex-a53</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L142">已禁用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P002_smsc_lan91c111.md#std-dtcompatible-smsc-lan91c111"><code>smsc,lan91c111</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111管理数据输入输出（MDIO）驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L150">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P008_smsc_lan91c111-mdio.md#std-dtcompatible-smsc-lan91c111-mdio"><code>smsc,lan91c111-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L156">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>GIC v3中断转换服务（ITS / Interrupt Translation Service）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L85">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P005_arm_gic-v3-its.md#std-dtcompatible-arm-gic-v3-its"><code>arm,gic-v3-its</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L164">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>板载（On-Board）</td>
<td>Arm固定虚拟平台（FVP）电源控制器（PWRC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P003_arm_fvp-pwrc.md#std-dtcompatible-arm-fvp-pwrc"><code>arm,fvp-pwrc</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L103">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L112">已禁用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a/smp/ns-hw-features-section"></a>

##### `fvp_base_revc_2xaem/v8a/smp/ns`目标（Target）

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a/smp/ns-hw-features-panel"></a>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a/smp/ns-hw-features-memory"></a>

该开发板目标的片上存储容量：128 MiB RAM、64 KiB Flash。

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a/smp/ns-hw-features-table"></a>

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
<td>ARM Cortex-A53处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L32">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P008_arm_cortex-a53.md#std-dtcompatible-arm-cortex-a53"><code>arm,cortex-a53</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L142">已禁用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P002_smsc_lan91c111.md#std-dtcompatible-smsc-lan91c111"><code>smsc,lan91c111</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111管理数据输入输出（MDIO）驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L150">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P008_smsc_lan91c111-mdio.md#std-dtcompatible-smsc-lan91c111-mdio"><code>smsc,lan91c111-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L156">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>GIC v3中断转换服务（ITS / Interrupt Translation Service）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L85">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P005_arm_gic-v3-its.md#std-dtcompatible-arm-gic-v3-its"><code>arm,gic-v3-its</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L164">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>板载（On-Board）</td>
<td>Arm固定虚拟平台（FVP）电源控制器（PWRC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P003_arm_fvp-pwrc.md#std-dtcompatible-arm-fvp-pwrc"><code>arm,fvp-pwrc</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L103">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L112">已禁用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a_aarch32-hw-features-section"></a>

##### `fvp_base_revc_2xaem/v8a_aarch32`目标（Target）

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a_aarch32-hw-features-panel"></a>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a_aarch32-hw-features-memory"></a>

该开发板目标的片上存储容量：128 MiB RAM、64 KiB Flash。

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a_aarch32-hw-features-table"></a>

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
<td>ARM Cortex-A32处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L32">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P005_arm_cortex-a32.md#std-dtcompatible-arm-cortex-a32"><code>arm,cortex-a32</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L142">已禁用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P002_smsc_lan91c111.md#std-dtcompatible-smsc-lan91c111"><code>smsc,lan91c111</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111管理数据输入输出（MDIO）驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L150">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P008_smsc_lan91c111-mdio.md#std-dtcompatible-smsc-lan91c111-mdio"><code>smsc,lan91c111-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L156">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>GIC v3中断转换服务（ITS / Interrupt Translation Service）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L85">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P005_arm_gic-v3-its.md#std-dtcompatible-arm-gic-v3-its"><code>arm,gic-v3-its</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L164">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>板载（On-Board）</td>
<td>Arm固定虚拟平台（FVP）电源控制器（PWRC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P003_arm_fvp-pwrc.md#std-dtcompatible-arm-fvp-pwrc"><code>arm,fvp-pwrc</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L103">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L112">已禁用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a_aarch32/smp-hw-features-section"></a>

##### `fvp_base_revc_2xaem/v8a_aarch32/smp`目标（Target）

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a_aarch32/smp-hw-features-panel"></a>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a_aarch32/smp-hw-features-memory"></a>

该开发板目标的片上存储容量：128 MiB RAM、64 KiB Flash。

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v8a_aarch32/smp-hw-features-table"></a>

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
<td>ARM Cortex-A32处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L32">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P005_arm_cortex-a32.md#std-dtcompatible-arm-cortex-a32"><code>arm,cortex-a32</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L142">已禁用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P002_smsc_lan91c111.md#std-dtcompatible-smsc-lan91c111"><code>smsc,lan91c111</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111管理数据输入输出（MDIO）驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L150">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P008_smsc_lan91c111-mdio.md#std-dtcompatible-smsc-lan91c111-mdio"><code>smsc,lan91c111-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L156">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>GIC v3中断转换服务（ITS / Interrupt Translation Service）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L85">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P005_arm_gic-v3-its.md#std-dtcompatible-arm-gic-v3-its"><code>arm,gic-v3-its</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L164">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>板载（On-Board）</td>
<td>Arm固定虚拟平台（FVP）电源控制器（PWRC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P003_arm_fvp-pwrc.md#std-dtcompatible-arm-fvp-pwrc"><code>arm,fvp-pwrc</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L103">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L112">已禁用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v9a-hw-features-section"></a>

##### `fvp_base_revc_2xaem/v9a`目标（Target）

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v9a-hw-features-panel"></a>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v9a-hw-features-memory"></a>

该开发板目标的片上存储容量：128 MiB RAM、64 KiB Flash。

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v9a-hw-features-table"></a>

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
<td>Arm Cortex-A510处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L32">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P007_arm_cortex-a510.md#std-dtcompatible-arm-cortex-a510"><code>arm,cortex-a510</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L142">已禁用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P002_smsc_lan91c111.md#std-dtcompatible-smsc-lan91c111"><code>smsc,lan91c111</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111管理数据输入输出（MDIO）驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L150">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P008_smsc_lan91c111-mdio.md#std-dtcompatible-smsc-lan91c111-mdio"><code>smsc,lan91c111-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L156">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>GIC v3中断转换服务（ITS / Interrupt Translation Service）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L85">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P005_arm_gic-v3-its.md#std-dtcompatible-arm-gic-v3-its"><code>arm,gic-v3-its</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L164">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>板载（On-Board）</td>
<td>Arm固定虚拟平台（FVP）电源控制器（PWRC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P003_arm_fvp-pwrc.md#std-dtcompatible-arm-fvp-pwrc"><code>arm,fvp-pwrc</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L103">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L112">已禁用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v9a/smp-hw-features-section"></a>

##### `fvp_base_revc_2xaem/v9a/smp`目标（Target）

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v9a/smp-hw-features-panel"></a>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v9a/smp-hw-features-memory"></a>

该开发板目标的片上存储容量：128 MiB RAM、64 KiB Flash。

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v9a/smp-hw-features-table"></a>

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
<td>Arm Cortex-A510处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L32">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P007_arm_cortex-a510.md#std-dtcompatible-arm-cortex-a510"><code>arm,cortex-a510</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L142">已禁用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P002_smsc_lan91c111.md#std-dtcompatible-smsc-lan91c111"><code>smsc,lan91c111</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111管理数据输入输出（MDIO）驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L150">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P008_smsc_lan91c111-mdio.md#std-dtcompatible-smsc-lan91c111-mdio"><code>smsc,lan91c111-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L156">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>GIC v3中断转换服务（ITS / Interrupt Translation Service）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L85">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P005_arm_gic-v3-its.md#std-dtcompatible-arm-gic-v3-its"><code>arm,gic-v3-its</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L164">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>板载（On-Board）</td>
<td>Arm固定虚拟平台（FVP）电源控制器（PWRC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P003_arm_fvp-pwrc.md#std-dtcompatible-arm-fvp-pwrc"><code>arm,fvp-pwrc</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L103">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L112">已禁用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v9a/smp/ns-hw-features-section"></a>

##### `fvp_base_revc_2xaem/v9a/smp/ns`目标（Target）

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v9a/smp/ns-hw-features-panel"></a>

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v9a/smp/ns-hw-features-memory"></a>

该开发板目标的片上存储容量：128 MiB RAM、64 KiB Flash。

<a id="fvp_base_revc_2xaem-fvp_base_revc_2xaem/v9a/smp/ns-hw-features-table"></a>

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
<td>Arm Cortex-A510处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L32">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P007_arm_cortex-a510.md#std-dtcompatible-arm-cortex-a510"><code>arm,cortex-a510</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L142">已禁用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P002_smsc_lan91c111.md#std-dtcompatible-smsc-lan91c111"><code>smsc,lan91c111</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN91C111管理数据输入输出（MDIO）驱动节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L150">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P008_smsc_lan91c111-mdio.md#std-dtcompatible-smsc-lan91c111-mdio"><code>smsc,lan91c111-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L156">已禁用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>GIC v3中断转换服务（ITS / Interrupt Translation Service）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L85">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P005_arm_gic-v3-its.md#std-dtcompatible-arm-gic-v3-its"><code>arm,gic-v3-its</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L164">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>板载（On-Board）</td>
<td>Arm固定虚拟平台（FVP）电源控制器（PWRC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P003_arm_fvp-pwrc.md#std-dtcompatible-arm-fvp-pwrc"><code>arm,fvp-pwrc</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L103">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L112">已禁用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_base_revc_2xaem/fvp_base_revc_2xaem.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="board-variants"></a>

#### 开发板变体（Board Variants）

可使用以下开发板目标：


- `fvp_base_revc_2xaem/v8a`：ARMv8-A（64位），使用Cortex-A53内核
- `fvp_base_revc_2xaem/v8a/smp`：ARMv8-A对称多处理（SMP），四核
- `fvp_base_revc_2xaem/v8a/smp/ns`：ARMv8-A SMP非安全态（Non-Secure）
- `fvp_base_revc_2xaem/v9a`：ARMv9-A（64位），使用Cortex-A510内核
- `fvp_base_revc_2xaem/v9a/smp`：ARMv9-A SMP，四核
- `fvp_base_revc_2xaem/v9a/smp/ns`：ARMv9-A SMP非安全态（Non-Secure）
- `fvp_base_revc_2xaem/a320`：ARMv9.2-A，使用Cortex-A320配置
- `fvp_base_revc_2xaem/v8a_aarch32`：ARMv8-A AArch32，使用Cortex-A32内核
- `fvp_base_revc_2xaem/v8a_aarch32/smp`：ARMv8-A AArch32 SMP，四核

Cortex-A320变体（Variant）：

`fvp_base_revc_2xaem/a320`变体提供面向Cortex-A320的FVP配置，包括：


- 符合ARMv9.2-A架构
- 增强密码扩展（Cryptographic Extensions），支持SHA3、SHA512、SM3及SM4
- 高级内存标记扩展（MTE Level 3 / Memory Tagging）
- QARMA3指针认证（Pointer Authentication）
- 针对Cortex-A320优化的缓存配置（Cache Configuration）
- 带可伸缩向量扩展专用事件（SVE-Specific Events）的性能监控单元（PMU）

<a id="devices"></a>

#### 设备（Devices）

<a id="system-clock"></a>

##### 系统时钟（System Clock）

此开发板配置的系统时钟频率为100 MHz。

<a id="serial-port"></a>

##### 串口（Serial Port）

此开发板配置使用UART0提供单路串行通信通道。

<a id="known-problems-or-limitations"></a>

#### 已知问题或限制（Known Problems or Limitations）

<a id="programming-and-debugging"></a>

### 烧录与调试（Programming and Debugging）

<a id="environment"></a>

#### 环境（Environment）

构建前先设置环境变量`ARMFVP_BIN_PATH`。还可选择设置`ARMFVP_EXTRA_FLAGS`，向FVP传递额外参数。

```text
export ARMFVP_BIN_PATH=/path/to/fvp/directory
```

<a id="programming"></a>

#### 编程（Programming）

此配置可在Arm FVP仿真环境中构建基本Zephyr应用及内核测试，例如[基础同步（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)示例：

```text
# From the root of the zephyr repository
west build -b fvp_base_revc_2xaem/v8a samples/synchronization
```

这会构建包含ARMv8-A同步示例应用的镜像，之后可通过`west build -t run`运行。

ARMv9-A变体：

```text
# From the root of the zephyr repository
west build -b fvp_base_revc_2xaem/v9a samples/synchronization
```

Cortex-A320变体：

```text
# From the root of the zephyr repository
west build -b fvp_base_revc_2xaem/a320 samples/hello_world
```

ARMv8-A AArch32变体：

```text
# From the root of the zephyr repository
west build -b fvp_base_revc_2xaem/v8a_aarch32 samples/hello_world
```

对称多处理（SMP）变体：

```text
# From the root of the zephyr repository
west build -b fvp_base_revc_2xaem/v8a/smp samples/synchronization
```

结合可信固件A（TF-A）的SMP非安全态变体：

```text
# From the root of the zephyr repository
west build -b fvp_base_revc_2xaem/v8a/smp/ns samples/synchronization
```

<a id="running-zephyr-at-el1ns"></a>

### 在EL1非安全态（EL1NS）运行Zephyr

若使用`CONFIG_ARMV8_A_NS`在EL1NS运行Zephyr，需要在FVP模型中加载合适的可信固件（Trusted Firmware）。

可使用面向FVP的Arm TF-A，将Zephyr作为预加载的BL33载荷（Payload）运行。

检出并构建TF-A：

```text
git clone https://git.trustedfirmware.org/TF-A/trusted-firmware-a.git --depth 1
cd trusted-firmware-a/
make PLAT=fvp PRELOADED_BL33_BASE="0x88000000" all fip
```

<a id="index-0"></a>

<a id="index-1"></a>

然后导出环境变量`ARMFVP_BL1_FILE`和`ARMFVP_FIP_FILE`：

```text
export ARMFVP_BL1_FILE=<path/to/tfa-a/build/fvp/release/bl1.bin>
export ARMFVP_FIP_FILE=<path/to/tfa-a/build/fvp/release/fip.bin>
```

<a id="migration-from-legacy-board-names"></a>

### 从旧开发板名称迁移（Migration from Legacy Board Names）

旧名称`fvp_base_revc_2xaemv8a`已由统一命名`fvp_base_revc_2xaem/v8a`替代。请更新构建命令：


- 旧命令：`west build -b fvp_base_revc_2xaemv8a`
- 新命令：`west build -b fvp_base_revc_2xaem/v8a`

为保持向后兼容，仍支持旧开发板名称。

<a id="debugging"></a>

#### 调试（Debugging）

详细概述见[应用调试（Application Debugging）](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

<a id="references"></a>

### 参考资料（References）


- [Arm架构参考手册——Armv8（Architecture Reference Manual）](https://developer.arm.com/documentation/ddi0487/latest)
- [固定虚拟平台（Fixed Virtual Platforms）](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms/Arm%20Architecture%20FVPs)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [Arm%20Architecture%20FVPs](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms/Arm%20Architecture%20FVPs)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [latest](https://developer.arm.com/documentation/ddi0487/latest)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。

---

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_FVP_BaseR_AEMv8-R.md)
