---
id: learning.zephyr-docs.boards-intel-ite.page-10
title: Elkhart Lake CRB
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/intel/ehl/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="intel_ehl_crb"></a>

# 第10章\_Elkhart Lake客户参考板（CRB）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/intel/ehl/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`intel_ehl_crb`

厂商（Vendor）：

[英特尔公司（Intel Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=intel)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[x86](https://docs.zephyrproject.org/latest/boards/index.html#arch=x86)

片上系统（SoC）：

[elkhart_lake](https://docs.zephyrproject.org/latest/boards/index.html#soc=elkhart_lake)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/intel/ehl/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Elkhart Lake参考板（EHL CRB）是面向物联网边缘设备的高性能紧凑型单板计算机实现示例。

此开发板配置为[EHL](https://www.intel.com/content/www/us/en/products/docs/processors/embedded/enhanced-for-iot-platform-brief.html)开发板启用内核支持。

注意（Note）

该配置适用于包含Intel Atom SoC的[EHL](https://www.intel.com/content/www/us/en/products/docs/processors/embedded/enhanced-for-iot-platform-brief.html)开发板变体。

<a id="hardware"></a>

## 硬件（Hardware）

开发板一般信息见[EHL](https://www.intel.com/content/www/us/en/products/docs/processors/embedded/enhanced-for-iot-platform-brief.html)网站。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

除了HPET、本地及I/O APIC等标准架构设备，Zephyr还支持以下Elkhart Lake专用SoC设备：


- 集成电路间总线（I2C）
- 系统管理总线（SMBus）

<a id="uart-serial-port-support"></a>

#### UART串口支持（Serial Port Support）

Elkhart Lake UART兼容NS16550，支持115.2 kbps波特率。

`intel_ehl_crb`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="intel_ehl_crb-hw-features"></a>

<a id="intel_ehl_crb-intel_ehl_crb/elkhart_lake-hw-features-section"></a>

##### `intel_ehl_crb/elkhart_lake`目标（Target）

<a id="intel_ehl_crb-intel_ehl_crb/elkhart_lake-hw-features-panel"></a>

<a id="intel_ehl_crb-intel_ehl_crb/elkhart_lake-hw-features-memory"></a>

该开发板目标的片上存储容量：2 GiB RAM、N/A Flash。

<a id="intel_ehl_crb-intel_ehl_crb/elkhart_lake-hw-features-table"></a>

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
<td>Intel Elkhart Lake CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L17">已启用：2</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P007_intel_elkhart-lake.md#std-dtcompatible-intel-elkhart-lake"><code>intel,elkhart-lake</code></a></td>
</tr>
<tr>
<td rowspan="1">错误检测与纠正（EDAC）</td>
<td>片上（On-Chip）</td>
<td>错误检测与纠正（EDAC）：带内纠错码（IBECC / In-Band Error Correcting Code）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L41">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P001_intel_ibecc.md#std-dtcompatible-intel-ibecc"><code>intel,ibecc</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Intel通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L462">已启用：15</a>）</td>
<td><a href="../gpio_infineon_intel_ite_microchip_binding_reference/P005_intel_gpio.md#std-dtcompatible-intel-gpio"><code>intel,gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L224">已启用：15</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P006_snps_designware-i2c.md#std-dtcompatible-snps-designware-i2c"><code>snps,designware-i2c</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>Intel I/O高级可编程中断控制器（APIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P001_intel_ioapic.md#std-dtcompatible-intel-ioapic"><code>intel,ioapic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>本地高级可编程中断控制器（Local APIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L54">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P002_intel_loapic.md#std-dtcompatible-intel-loapic"><code>intel,loapic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Intel VT-D中断重映射控制器（Interrupt Remapping Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L426">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P003_intel_vt-d.md#std-dtcompatible-intel-vt-d"><code>intel,vt-d</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>兼容Motorola MC146818的实时时钟电池后备RAM（Battery Backed RAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L731">已启用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P013_motorola_mc146818-bbram.md#std-dtcompatible-motorola-mc146818-bbram"><code>motorola,mc146818-bbram</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>Motorola MC146818多功能器件（MFD）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L718">已启用：1</a>）</td>
<td><a href="../hardware/P713_MC146818多功能设备绑定.md#dtbinding-motorola-mc146818-mfd"><code>motorola,mc146818-mfd</code></a></td>
</tr>
<tr>
<td rowspan="1">高速外围组件互连（PCIe）</td>
<td>片上（On-Chip）</td>
<td>通用PCIe主机控制器（Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L62">已启用：1</a>）</td>
<td><a href="../pcie_memory_virtualization_binding_reference/P009_pcie-controller.md#std-dtcompatible-pcie-controller"><code>pcie-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>兼容Motorola MC146818的实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L722">已启用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P009_motorola_mc146818.md#std-dtcompatible-motorola-mc146818"><code>motorola,mc146818</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L78">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L122">已禁用：8</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">系统管理总线（SMbus）</td>
<td>片上（On-Chip）</td>
<td>Intel平台控制器集线器（PCH）SMBus（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L212">已启用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P011_intel_pch-smbus.md#std-dtcompatible-intel-pch-smbus"><code>intel,pch-smbus</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>高精度事件定时器（HPET / High-Precision Event Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L702">已启用：1</a>）</td>
<td><a href="../system_timer_binding_reference/P007_intel_hpet.md#std-dtcompatible-intel-hpet"><code>intel,hpet</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Intel TCO看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L711">已禁用：1</a>）</td>
<td><a href="../soc_pmic_watchdog_binding_reference/P004_intel_tco-wdt.md#std-dtcompatible-intel-tco-wdt"><code>intel,tco-wdt</code></a></td>
</tr>
</table>

<a id="intel_ehl_crb-intel_ehl_crb/elkhart_lake/sbl-hw-features-section"></a>

##### `intel_ehl_crb/elkhart_lake/sbl`目标（Target）

<a id="intel_ehl_crb-intel_ehl_crb/elkhart_lake/sbl-hw-features-panel"></a>

<a id="intel_ehl_crb-intel_ehl_crb/elkhart_lake/sbl-hw-features-memory"></a>

该开发板目标的片上存储容量：2 GiB RAM、N/A Flash。

<a id="intel_ehl_crb-intel_ehl_crb/elkhart_lake/sbl-hw-features-table"></a>

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
<td>Intel Elkhart Lake CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L17">已启用：2</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P007_intel_elkhart-lake.md#std-dtcompatible-intel-elkhart-lake"><code>intel,elkhart-lake</code></a></td>
</tr>
<tr>
<td rowspan="1">错误检测与纠正（EDAC）</td>
<td>片上（On-Chip）</td>
<td>错误检测与纠正（EDAC）：带内纠错码（IBECC / In-Band Error Correcting Code）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L41">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P001_intel_ibecc.md#std-dtcompatible-intel-ibecc"><code>intel,ibecc</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Intel通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L462">已启用：15</a>）</td>
<td><a href="../gpio_infineon_intel_ite_microchip_binding_reference/P005_intel_gpio.md#std-dtcompatible-intel-gpio"><code>intel,gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L224">已启用：15</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P006_snps_designware-i2c.md#std-dtcompatible-snps-designware-i2c"><code>snps,designware-i2c</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>Intel I/O高级可编程中断控制器（APIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P001_intel_ioapic.md#std-dtcompatible-intel-ioapic"><code>intel,ioapic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>本地高级可编程中断控制器（Local APIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L54">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P002_intel_loapic.md#std-dtcompatible-intel-loapic"><code>intel,loapic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Intel VT-D中断重映射控制器（Interrupt Remapping Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L426">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P003_intel_vt-d.md#std-dtcompatible-intel-vt-d"><code>intel,vt-d</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>兼容Motorola MC146818的实时时钟电池后备RAM（Battery Backed RAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L731">已启用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P013_motorola_mc146818-bbram.md#std-dtcompatible-motorola-mc146818-bbram"><code>motorola,mc146818-bbram</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>Motorola MC146818多功能器件（MFD）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L718">已启用：1</a>）</td>
<td><a href="../hardware/P713_MC146818多功能设备绑定.md#dtbinding-motorola-mc146818-mfd"><code>motorola,mc146818-mfd</code></a></td>
</tr>
<tr>
<td rowspan="1">高速外围组件互连（PCIe）</td>
<td>片上（On-Chip）</td>
<td>通用PCIe主机控制器（Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L62">已启用：1</a>）</td>
<td><a href="../pcie_memory_virtualization_binding_reference/P009_pcie-controller.md#std-dtcompatible-pcie-controller"><code>pcie-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>兼容Motorola MC146818的实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L722">已启用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P009_motorola_mc146818.md#std-dtcompatible-motorola-mc146818"><code>motorola,mc146818</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L78">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L107">已禁用：8</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">系统管理总线（SMbus）</td>
<td>片上（On-Chip）</td>
<td>Intel平台控制器集线器（PCH）SMBus（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L212">已启用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P011_intel_pch-smbus.md#std-dtcompatible-intel-pch-smbus"><code>intel,pch-smbus</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>高精度事件定时器（HPET / High-Precision Event Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L702">已启用：1</a>）</td>
<td><a href="../system_timer_binding_reference/P007_intel_hpet.md#std-dtcompatible-intel-hpet"><code>intel,hpet</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Intel TCO看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/elkhart_lake.dtsi?plain=1#L711">已禁用：1</a>）</td>
<td><a href="../soc_pmic_watchdog_binding_reference/P004_intel_tco-wdt.md#std-dtcompatible-intel-tco-wdt"><code>intel,tco-wdt</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

更多信息见[EHL](https://www.intel.com/content/www/us/en/products/docs/processors/embedded/enhanced-for-iot-platform-brief.html)网站。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`intel_ehl_crb`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
<tr>
<td>misc-flasher</td>
<td>✅（默认 / default）</td>
<td></td>
</tr>
</table>

按以下流程在EHL CRB上启动镜像。

<a id="contents"></a>


- <a id="id1"></a>

  [构建Zephyr应用（Build Zephyr Application）](#build-zephyr-application)
- <a id="id2"></a>

  [使用UEFI启动Elkhart Lake CRB开发板](#booting-the-elkhart-lake-crb-board-using-uefi)
- <a id="id3"></a>

  [通过网络启动Elkhart Lake CRB开发板](#booting-the-elkhart-lake-crb-board-over-network)

<a id="build-zephyr-application"></a>

### [构建Zephyr应用（Build Zephyr Application）](#contents)


1. 构建Zephyr应用。例如，在Elkhart Lake CRB上构建hello_world应用：

  ```text
  # From the root of the zephyr repository
  west build -b intel_ehl_crb samples/hello_world
  ```

  注意（Note）

  应用构建完成后，构建目录中会自动生成名为`zephyr.efi`的Zephyr EFI镜像文件。

<a id="booting-the-elkhart-lake-crb-board-using-uefi"></a>

### [使用UEFI启动Elkhart Lake CRB开发板](#contents)

<a id="preparing-the-boot-device"></a>

#### 准备启动设备（Preparing the Boot Device）

准备一个USB闪存盘，用于在开发板上启动Zephyr应用镜像。


1. 将USB闪存盘格式化为FAT32。

  在Windows中打开文件资源管理器，右键单击USB闪存盘并选择“格式化（Format...）”。确认“文件系统（File System）”选择FAT32，点击“格式化（Format）”按钮，等待完成。

  Linux下可使用gparted等图形工具，将USB闪存盘格式化为FAT32。也可在终端中找出对应设备节点，例如`/dev/sdd`，然后执行以下命令：

  ```text
  $ mkfs.vfat -F 32 <device-node>
  ```

  重要提示（Important）

  必须确认设备节点确实属于该USB闪存盘，否则可能擦除系统中的其他存储设备，导致系统无法使用。
2. 将Zephyr EFI镜像文件`zephyr/zephyr.efi`复制到USB闪存盘。

<a id="booting-zephyr-on-a-board"></a>

#### 在开发板上启动Zephyr（Booting Zephyr）

连接USB闪存盘，将开发板启动到EFI Shell。


1. 将准备好的启动设备，即USB闪存盘，插入开发板。
2. 通过串口线将开发板连接主机，并配置主机监听串口数据。更多信息见开发板网站。

  注意（Note）

  波特率使用115200。
3. 给开发板上电。
4. 出现以下输出时，按F7：

  ```text
  Press <DEL> or <ESC> to enter setup.
  ```
5. 在显示的菜单中选择对应EFI Shell的菜单项。
6. 在EFI Shell中选择要启动的Zephyr EFI镜像。

  ```text
  Shell> fs0:zephyr.efi
  ```
7. 启动过程结束后，Zephyr应用镜像即已启动。

<a id="booting-the-elkhart-lake-crb-board-over-network"></a>

### [通过网络启动Elkhart Lake CRB开发板](#contents)

<a id="prepare-linux-host"></a>

#### 准备Linux主机（Prepare Linux Host）


1. 安装DHCP及TFTP服务器，例如dnsmasq。

  ```text
  $ sudo apt-get install dnsmasq
  ```
2. 配置DHCP服务器，dnsmasq配置如下：

  ```text
  # Only listen to this interface
  interface=eno2
  dhcp-range=10.1.1.20,10.1.1.30,12h
  ```
3. 配置TFTP服务器。

  ```text
  # tftp
  enable-tftp
  tftp-root=/srv/tftp
  dhcp-boot=zephyr.efi
  ```

  `zephyr.efi`是前面生成的Zephyr EFI二进制文件。
4. 将Zephyr EFI镜像`zephyr/zephyr.efi`复制到`/srv/tftp`目录。

  > ```text
  > $ cp zephyr/zephyr.efi /srv/tftp
  > ```
5. TFTP根目录应如下所示：

  ```text
  $ tree /srv/tftp
  /srv/tftp
  └── zephyr.efi
  ```
6. 重启dnsmasq服务：

  ```text
  $ sudo systemctl restart dnsmasq.service
  ```

<a id="prepare-the-board-for-network-boot"></a>

#### 为开发板准备网络启动（Network Boot）


1. 在BIOS设置中启用PXE网络启动。
2. 将网络启动设为第一启动选项。

<a id="booting-the-board"></a>

#### 启动开发板（Booting the Board）


1. 通过串口线将开发板连接主机，并配置主机监听串口数据。更多信息见开发板网站。

  注意（Note）

  波特率使用115200。
2. 给开发板上电。
3. 确认开发板已获得IP地址。在Linux主机运行：

  ```text
  $ journalctl -f -u dnsmasq
  dnsmasq-dhcp[5386]: DHCPDISCOVER(eno2) 00:07:32:52:25:88
  dnsmasq-dhcp[5386]: DHCPOFFER(eno2) 10.1.1.28 00:07:32:52:25:88
  dnsmasq-dhcp[5386]: DHCPREQUEST(eno2) 10.1.1.28 00:07:32:52:25:88
  dnsmasq-dhcp[5386]: DHCPACK(eno2) 10.1.1.28 00:07:32:52:25:88
  ```
4. 确认网络启动已开始：

  ```text
  $ journalctl -f -u dnsmasq
  dnsmasq-tftp[5386]: sent /srv/tftp/zephyr.efi to 10.1.1.28
  ```
5. 启动过程结束后，Zephyr应用镜像即已启动。

注意（Note）

按以下步骤为Elkhart Lake CRB启用PXE启动：


1. 启用PXE启动。进入EFI Shell，确认第一启动选项为UEFI PXEv4。

  ```text
  Shell> bcfg boot dump
  Option: 00. Variable: Boot0007
    Desc    - UEFI PXEv4 (MAC:6805CABC1997)
    DevPath - PciRoot(0x0)/Pci(0x1C,0x0)/Pci(0x0,0x0)/MAC(6805CABC1997,0x0)/IPv4(0.0.0.0)
    Optional- Y
  ...
  ```
2. 若UEFI PXEv4不是第一启动选项，可用`bcfg boot mv`命令调整启动顺序。

  ```text
  Shell> bcfg boot mv 7 0
  ```

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [enhanced-for-iot-platform-brief.html](https://www.intel.com/content/www/us/en/products/docs/processors/embedded/enhanced-for-iot-platform-brief.html)：HTTP Error 403: Forbidden。

---

[上一章](P009_Prepare_Linux_host.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_Intel_Corporation.md)
