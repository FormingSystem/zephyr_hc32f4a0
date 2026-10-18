---
id: learning.zephyr-docs.boards-intel-ite.page-16
title: Panther Lake H CRB
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/intel/ptl/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="intel_ptl_h_crb"></a>

# 第16章\_Panther Lake H客户参考板（CRB）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/intel/ptl/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`intel_ptl_h_crb`

厂商（Vendor）：

[英特尔公司（Intel Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=intel)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[x86](https://docs.zephyrproject.org/latest/boards/index.html#arch=x86)

片上系统（SoC）：

[panther_lake](https://docs.zephyrproject.org/latest/boards/index.html#soc=panther_lake)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/intel/ptl/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Panther Lake H处理器是64位多核处理器，原文将其工艺写为Intel 18A（1.8 nm）。它采用混合架构（Hybrid Architecture），以P核提供性能、E核提高能效。

Panther Lake处理器系列、P核及E核的更多信息见[INTEL_PTL](https://edc.intel.com/content/www/us/en/secure/design/confidential/products/platforms/details/panther-lake/panther-lake-u-h-processor-external-design-specification-volume-1-of-2/)。

此开发板配置为Panther Lake H开发板启用内核支持。

<a id="hardware"></a>

## 硬件（Hardware）

`intel_ptl_h_crb`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="intel_ptl_h_crb-hw-features"></a>

<a id="intel_ptl_h_crb-intel_ptl_h_crb/panther_lake-hw-features-section"></a>

### `intel_ptl_h_crb/panther_lake`目标（Target）

<a id="intel_ptl_h_crb-intel_ptl_h_crb/panther_lake-hw-features-panel"></a>

<a id="intel_ptl_h_crb-intel_ptl_h_crb/panther_lake-hw-features-memory"></a>

该开发板目标的片上存储容量：2 GiB RAM、N/A Flash。

<a id="intel_ptl_h_crb-intel_ptl_h_crb/panther_lake-hw-features-table"></a>

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
<td>Intel Panther Lake CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L18">已启用：2</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P012_intel_panther-lake.md#std-dtcompatible-intel-panther-lake"><code>intel,panther-lake</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>低功耗子系统（LPSS）DMA控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L164">已禁用：6</a>）</td>
<td><a href="../intel_microchip_dma_binding_reference/P011_intel_lpss.md#std-dtcompatible-intel-lpss"><code>intel,lpss</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Intel通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/gpio_common.dtsi?plain=1#L13">已禁用：17</a>）</td>
<td><a href="../gpio_infineon_intel_ite_microchip_binding_reference/P005_intel_gpio.md#std-dtcompatible-intel-gpio"><code>intel,gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L170">已禁用：6</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P006_snps_designware-i2c.md#std-dtcompatible-snps-designware-i2c"><code>snps,designware-i2c</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>Intel I/O高级可编程中断控制器（APIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L38">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P001_intel_ioapic.md#std-dtcompatible-intel-ioapic"><code>intel,ioapic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>本地高级可编程中断控制器（Local APIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P002_intel_loapic.md#std-dtcompatible-intel-loapic"><code>intel,loapic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Intel VT-D中断重映射控制器（Interrupt Remapping Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L371">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P003_intel_vt-d.md#std-dtcompatible-intel-vt-d"><code>intel,vt-d</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>兼容Motorola MC146818的实时时钟电池后备RAM（Battery Backed RAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L412">已禁用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P013_motorola_mc146818-bbram.md#std-dtcompatible-motorola-mc146818-bbram"><code>motorola,mc146818-bbram</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>Motorola MC146818多功能器件（MFD）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L399">已启用：1</a>）</td>
<td><a href="../hardware/P713_MC146818多功能设备绑定.md#dtbinding-motorola-mc146818-mfd"><code>motorola,mc146818-mfd</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>Intel定时GPIO（TGPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L421">已禁用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P011_intel_timeaware-gpio.md#std-dtcompatible-intel-timeaware-gpio"><code>intel,timeaware-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">高速外围组件互连（PCIe）</td>
<td>片上（On-Chip）</td>
<td>通用PCIe主机控制器（Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L146">已启用：1</a>）</td>
<td><a href="../pcie_memory_virtualization_binding_reference/P009_pcie-controller.md#std-dtcompatible-pcie-controller"><code>pcie-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Intel Blinky脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L388">已启用：1</a>）</td>
<td><a href="../pwm_intel_microchip_nxp_binding_reference/P002_intel_blinky-pwm.md#std-dtcompatible-intel-blinky-pwm"><code>intel,blinky-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>兼容Motorola MC146818的实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L403">已启用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P009_motorola_mc146818.md#std-dtcompatible-motorola-mc146818"><code>motorola,mc146818</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L377">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L318">已禁用：3</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">系统管理总线（SMbus）</td>
<td>片上（On-Chip）</td>
<td>Intel平台控制器集线器（PCH）SMBus（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L153">已启用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P011_intel_pch-smbus.md#std-dtcompatible-intel-pch-smbus"><code>intel,pch-smbus</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Intel Penwell串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L264">已禁用：3</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P019_intel_penwell-spi.md#std-dtcompatible-intel-penwell-spi"><code>intel,penwell-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>高精度事件定时器（HPET / High-Precision Event Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L430">已禁用：1</a>）</td>
<td><a href="../system_timer_binding_reference/P007_intel_hpet.md#std-dtcompatible-intel-hpet"><code>intel,hpet</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Intel TCO看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/panther_lake_h.dtsi?plain=1#L438">已启用：1</a>）</td>
<td><a href="../soc_pmic_watchdog_binding_reference/P004_intel_tco-wdt.md#std-dtcompatible-intel-tco-wdt"><code>intel,tco-wdt</code></a></td>
</tr>
</table>

开发板一般信息见[INTEL_PTL](https://edc.intel.com/content/www/us/en/secure/design/confidential/products/platforms/details/panther-lake/panther-lake-u-h-processor-external-design-specification-volume-1-of-2/)网站。

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

更多信息见[INTEL_PTL](https://edc.intel.com/content/www/us/en/secure/design/confidential/products/platforms/details/panther-lake/panther-lake-u-h-processor-external-design-specification-volume-1-of-2/)网站。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

按以下流程在Panther Lake H CRB上启动镜像。

<a id="contents"></a>


- <a id="id1"></a>

  [构建Zephyr应用（Build Zephyr Application）](#build-zephyr-application)

<a id="build-zephyr-application"></a>

### [构建Zephyr应用（Build Zephyr Application）](#contents)


1. 构建Zephyr应用。例如，为Panther Lake H CRB构建hello_world应用：

  ```text
  # From the root of the zephyr repository
  west build -b intel_ptl_h_crb samples/hello_world
  ```

  注意（Note）

  应用构建完成后，构建目录中会自动生成名为`zephyr.efi`的Zephyr EFI镜像文件。

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

## 译注

Intel 18A（1.8 nm）为本页原文工艺表述，未据其他资料改写或扩展。

---

[上一章](P015_Nova_Lake_RVP.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P017_Raptor_Lake_CRB.md)
