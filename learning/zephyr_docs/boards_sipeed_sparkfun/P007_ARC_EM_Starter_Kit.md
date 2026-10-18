---
id: learning.zephyr-docs.boards-sipeed-sparkfun.page-7
title: ARC EM Starter Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/snps/em_starterkit/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="em_starterkit"></a>

# 第7章\_ARC EM入门套件（Starter Kit）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/snps/em_starterkit/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/em_starterkit.jpg](images/em_starterkit.jpg)](images/em_starterkit.jpg)

ARC EM入门套件（Starter Kit）

名称（Name）：

`em_starterkit`

厂商（Vendor）：

[Synopsys, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=snps)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arc](https://docs.zephyrproject.org/latest/boards/index.html#arch=arc)

片上系统（SoC）：

[emsk_em7d](https://docs.zephyrproject.org/latest/boards/index.html#soc=emsk_em7d)、[emsk_em11d](https://docs.zephyrproject.org/latest/boards/index.html#soc=emsk_em11d)、[emsk_em9d](https://docs.zephyrproject.org/latest/boards/index.html#soc=emsk_em9d)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/snps/em_starterkit/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

DesignWare ARC EM Starter Kit是一款低成本、多用途方案，用于快速开发、调试及性能分析（Profiling）ARC EM系列处理器软件。EM系列包括EM4、EM6、EM5D、EM7D、EM9D及EM11D核，套件可运行Zephyr RTOS。

<a id="id3"></a>

ARC EM Starter Kit硬件平台预装多种包含外设的ARC EM处理器配置FPGA镜像，板卡文档见[embARC网站](https://www.embarc.org)[注1](#id2)。

<a id="id7"></a>

板卡详情另见[DesignWare ARC EM Starter Kit网站](https://www.synopsys.com/dw/ipdir.php?ds=arc_em_starter_kit)[注2](#id6)。

原文编写时EM Starter Kit最新版本为2.3，可使用相应新固件从2.0／2.1／2.2升级到2.3。Zephyr默认配置位于[boards/snps/em_starterkit/](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/)。

Zephyr对此板默认支持的SoC为EM9D，采用指令总线与数据总线分离的哈佛架构（Harvard Architecture）。指令存储器称为ICCM，数据存储器称为DCCM。EM9D配置文件位于[soc/snps/emsk/Kconfig.defconfig.em9d](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsk/Kconfig.defconfig.em9d)。

较大程序可选择EM7D或EM11D，以访问带指令及数据缓存的128 KB DRAM。对应配置分别位于[soc/snps/emsk/Kconfig.defconfig.em7d](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsk/Kconfig.defconfig.em7d)及[soc/snps/emsk/Kconfig.defconfig.em11d](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsk/Kconfig.defconfig.em11d)。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="board-layout"></a>

### 开发板布局（Board Layout）

ARC EM Starter Kit主板具有6个Pmod连接器，可配置为连接GPIO、I2C、UART或SPI设备。

板上另有16 MB SPI闪存及SD卡用于存储，9个LED、3个按键及4个拨码开关可通过GPIO使用。

Xilinx Spartan-6 LX150 FPGA可自动加载三个SoC比特流文件之一，分别提供EM7D、EM9D或EM11D。

<a id="id4"></a>

板卡文档、一般信息及部分免费示例软件见[embARC网站](https://www.embarc.org)[注1](#id2)。

<a id="supported-firmware-versions"></a>

### 受支持的固件版本（Supported Firmware Versions）

EM Starter Kit具有1.0、1.1、2.0、2.1、2.2及2.3等版本，Zephyr仅支持2.2及2.3固件。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`em_starterkit`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="em_starterkit-hw-features"></a>

<a id="em_starterkit-em_starterkit@2.2.0/emsk_em7d-hw-features-section"></a>

#### `em_starterkit@2.2.0/emsk_em7d`目标（Target）

<a id="em_starterkit-em_starterkit@2.2.0/emsk_em7d-hw-features-panel"></a>

<a id="em_starterkit-em_starterkit@2.2.0/emsk_em7d-hw-features-memory"></a>

此板级目标的存储：128 KiB RAM；Flash不适用（N/A）。

<a id="em_starterkit-em_starterkit@2.2.0/emsk_em7d-hw-features-table"></a>

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
<td>Synopsys ARC EM处理器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P042_snps_arcem.md#std-dtcompatible-snps-arcem"><code>snps,arcem</code></a></td>
</tr>
<tr>
<td rowspan="2">ARC 架构（ARC Architecture）</td>
<td>板载（On-Board）</td>
<td>ARC指令紧耦合存储器（ICCM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_emsk_em7d_2_2_0.overlay?plain=1#L30">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P002_arc_iccm.md#std-dtcompatible-arc-iccm"><code>arc,iccm</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARC数据紧耦合存储器（DCCM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_emsk_em7d_2_2_0.overlay?plain=1#L35">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P001_arc_dccm.md#std-dtcompatible-arc-dccm"><code>arc,dccm</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L43">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L102">已启用：4</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P021_snps_designware-gpio.md#std-dtcompatible-snps-designware-gpio"><code>snps,designware-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L60">已启用：2</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P006_snps_designware-i2c.md#std-dtcompatible-snps-designware-i2c"><code>snps,designware-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/board.dtsi?plain=1#L71">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARCv2中断控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P004_snps_arcv2-intc.md#std-dtcompatible-snps-arcv2-intc"><code>snps,arcv2-intc</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/board.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L78">已启用：3</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L144">已启用：2</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P008_snps_designware-spi.md#std-dtcompatible-snps-designware-spi"><code>snps,designware-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>Synopsys ARC本地定时器，支持中断（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L31">已启用：2</a>）</td>
<td><a href="../system_timer_binding_reference/P006_snps_arc-timer.md#std-dtcompatible-snps-arc-timer"><code>snps,arc-timer</code></a></td>
</tr>
</table>

<a id="em_starterkit-em_starterkit@2.3.0/emsk_em11d-hw-features-section"></a>

#### `em_starterkit@2.3.0/emsk_em11d`目标（Target）

<a id="em_starterkit-em_starterkit@2.3.0/emsk_em11d-hw-features-panel"></a>

<a id="em_starterkit-em_starterkit@2.3.0/emsk_em11d-hw-features-memory"></a>

该开发板目标的片上存储容量：128 MiB RAM、N/A Flash。

<a id="em_starterkit-em_starterkit@2.3.0/emsk_em11d-hw-features-table"></a>

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
<td>Synopsys ARC EM处理器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P042_snps_arcem.md#std-dtcompatible-snps-arcem"><code>snps,arcem</code></a></td>
</tr>
<tr>
<td rowspan="4">ARC 架构（ARC Architecture）</td>
<td>板载（On-Board）</td>
<td>ARC指令紧耦合存储器（ICCM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_emsk_em11d.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P002_arc_iccm.md#std-dtcompatible-arc-iccm"><code>arc,iccm</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARC数据紧耦合存储器（DCCM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_emsk_em11d.dts?plain=1#L40">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P001_arc_dccm.md#std-dtcompatible-arc-dccm"><code>arc,dccm</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARC X紧耦合存储器（XCCM）；XY存储器用于提高数字信号处理（DSP）性能（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_emsk_em11d.dts?plain=1#L45">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P003_arc_xccm.md#std-dtcompatible-arc-xccm"><code>arc,xccm</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARC Y紧耦合存储器（YCCM）；XY存储器用于提高数字信号处理（DSP）性能（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_emsk_em11d.dts?plain=1#L50">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P004_arc_yccm.md#std-dtcompatible-arc-yccm"><code>arc,yccm</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L43">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L102">已启用：4</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P021_snps_designware-gpio.md#std-dtcompatible-snps-designware-gpio"><code>snps,designware-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Synopsys配置寄存器GPIO（CREG GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_r23.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P020_snps_creg-gpio.md#std-dtcompatible-snps-creg-gpio"><code>snps,creg-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L60">已启用：2</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P006_snps_designware-i2c.md#std-dtcompatible-snps-designware-i2c"><code>snps,designware-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/board.dtsi?plain=1#L71">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARCv2中断控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P004_snps_arcv2-intc.md#std-dtcompatible-snps-arcv2-intc"><code>snps,arcv2-intc</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/board.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>这些属性用于支持Zephyr的<code>spi-nor</code>闪存驱动通过Zephyr SPI API，使用基于M25P80的标准命令集控制串行闪存（Serial Flash Memory）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_r23.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor"><code>jedec,spi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L78">已启用：3</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L144">已启用：2</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P008_snps_designware-spi.md#std-dtcompatible-snps-designware-spi"><code>snps,designware-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>Synopsys ARC本地定时器，支持中断（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L31">已启用：2</a>）</td>
<td><a href="../system_timer_binding_reference/P006_snps_arc-timer.md#std-dtcompatible-snps-arc-timer"><code>snps,arc-timer</code></a></td>
</tr>
</table>

<a id="em_starterkit-em_starterkit@2.3.0/emsk_em7d-hw-features-section"></a>

#### `em_starterkit@2.3.0/emsk_em7d`目标（Target）

<a id="em_starterkit-em_starterkit@2.3.0/emsk_em7d-hw-features-panel"></a>

<a id="em_starterkit-em_starterkit@2.3.0/emsk_em7d-hw-features-memory"></a>

此板级目标的存储：128 KiB RAM；Flash不适用（N/A）。

<a id="em_starterkit-em_starterkit@2.3.0/emsk_em7d-hw-features-table"></a>

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
<td>Synopsys ARC EM处理器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P042_snps_arcem.md#std-dtcompatible-snps-arcem"><code>snps,arcem</code></a></td>
</tr>
<tr>
<td rowspan="2">ARC 架构（ARC Architecture）</td>
<td>板载（On-Board）</td>
<td>ARC指令紧耦合存储器（ICCM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_emsk_em7d_2_3_0.overlay?plain=1#L30">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P002_arc_iccm.md#std-dtcompatible-arc-iccm"><code>arc,iccm</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARC数据紧耦合存储器（DCCM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_emsk_em7d_2_3_0.overlay?plain=1#L35">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P001_arc_dccm.md#std-dtcompatible-arc-dccm"><code>arc,dccm</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L43">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L102">已启用：4</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P021_snps_designware-gpio.md#std-dtcompatible-snps-designware-gpio"><code>snps,designware-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Synopsys配置寄存器GPIO（CREG GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_r23.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P020_snps_creg-gpio.md#std-dtcompatible-snps-creg-gpio"><code>snps,creg-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L60">已启用：2</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P006_snps_designware-i2c.md#std-dtcompatible-snps-designware-i2c"><code>snps,designware-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/board.dtsi?plain=1#L71">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARCv2中断控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P004_snps_arcv2-intc.md#std-dtcompatible-snps-arcv2-intc"><code>snps,arcv2-intc</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/board.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>这些属性用于支持Zephyr的<code>spi-nor</code>闪存驱动通过Zephyr SPI API，使用基于M25P80的标准命令集控制串行闪存（Serial Flash Memory）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_r23.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor"><code>jedec,spi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L78">已启用：3</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L144">已启用：2</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P008_snps_designware-spi.md#std-dtcompatible-snps-designware-spi"><code>snps,designware-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>Synopsys ARC本地定时器，支持中断（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L31">已启用：3</a>）</td>
<td><a href="../system_timer_binding_reference/P006_snps_arc-timer.md#std-dtcompatible-snps-arc-timer"><code>snps,arc-timer</code></a></td>
</tr>
</table>

<a id="em_starterkit-em_starterkit@2.3.0/emsk_em9d-hw-features-section"></a>

#### `em_starterkit@2.3.0/emsk_em9d`目标（Target）

<a id="em_starterkit-em_starterkit@2.3.0/emsk_em9d-hw-features-panel"></a>

<a id="em_starterkit-em_starterkit@2.3.0/emsk_em9d-hw-features-memory"></a>

此板级目标的存储：128 KiB RAM；Flash不适用（N/A）。

<a id="em_starterkit-em_starterkit@2.3.0/emsk_em9d-hw-features-table"></a>

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
<td>Synopsys ARC EM处理器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P042_snps_arcem.md#std-dtcompatible-snps-arcem"><code>snps,arcem</code></a></td>
</tr>
<tr>
<td rowspan="4">ARC 架构（ARC Architecture）</td>
<td>板载（On-Board）</td>
<td>ARC指令紧耦合存储器（ICCM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_emsk_em9d.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P002_arc_iccm.md#std-dtcompatible-arc-iccm"><code>arc,iccm</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARC数据紧耦合存储器（DCCM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_emsk_em9d.dts?plain=1#L40">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P001_arc_dccm.md#std-dtcompatible-arc-dccm"><code>arc,dccm</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARC X紧耦合存储器（XCCM）；XY存储器用于提高数字信号处理（DSP）性能（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_emsk_em9d.dts?plain=1#L45">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P003_arc_xccm.md#std-dtcompatible-arc-xccm"><code>arc,xccm</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARC Y紧耦合存储器（YCCM）；XY存储器用于提高数字信号处理（DSP）性能（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_emsk_em9d.dts?plain=1#L50">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P004_arc_yccm.md#std-dtcompatible-arc-yccm"><code>arc,yccm</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L43">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L102">已启用：4</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P021_snps_designware-gpio.md#std-dtcompatible-snps-designware-gpio"><code>snps,designware-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Synopsys配置寄存器GPIO（CREG GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_r23.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P020_snps_creg-gpio.md#std-dtcompatible-snps-creg-gpio"><code>snps,creg-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L60">已启用：2</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P006_snps_designware-i2c.md#std-dtcompatible-snps-designware-i2c"><code>snps,designware-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/board.dtsi?plain=1#L71">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARCv2中断控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../multiarch_interrupt_binding_reference/P004_snps_arcv2-intc.md#std-dtcompatible-snps-arcv2-intc"><code>snps,arcv2-intc</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/board.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>这些属性用于支持Zephyr的<code>spi-nor</code>闪存驱动通过Zephyr SPI API，使用基于M25P80的标准命令集控制串行闪存（Serial Flash Memory）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/em_starterkit/em_starterkit_r23.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor"><code>jedec,spi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L78">已启用：3</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L144">已启用：2</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P008_snps_designware-spi.md#std-dtcompatible-snps-designware-spi"><code>snps,designware-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>Synopsys ARC本地定时器，支持中断（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arc/synopsys/emsk.dtsi?plain=1#L31">已启用：2</a>）</td>
<td><a href="../system_timer_binding_reference/P006_snps_arc-timer.md#std-dtcompatible-snps-arc-timer"><code>snps,arc-timer</code></a></td>
</tr>
</table>

支持SPI闪存驱动，示例位于samples/drivers/spi_flash。

SPI闪存还保存三个或四个独立FPGA CPU比特流文件，可通过拨码开关选择。

SPI闪存内还写有引导加载器，可将程序镜像从SPI闪存复制到可执行存储器。若使用CONFIG_XIP，Zephyr初始化会将已初始化数据段复制到数据存储器。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`em_starterkit`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>调试服务器（debugserver）</th>
</tr>
<tr>
<td>mdb-hw</td>
<td>✅</td>
<td>✅</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

<a id="required-hardware-and-software"></a>

### 所需硬件及软件（Required Hardware and Software）

在EM Starter Kit运行Zephyr RTOS应用还需要以下硬件及软件。


- USB线，随ARC EM Starter Kit提供
- USB线可为板卡供电；独立运行时，也可使用套件随附的通用开关电源适配器，将110—240 V交流转换为5 V直流。
- [Zephyr软件开发套件（SDK）](../toolchains/P002_ZephyrSDK.md#toolchain-zephyr-sdk)
- <a id="id11"></a>

  用于USB转UART的终端仿真软件，原文建议[PuTTY网站](https://www.putty.software)[注4](#id10)所提供的软件。
- <a id="id9"></a>

  可选Pmod模块，见[Digilent Pmod Modules](http://store.digilentinc.com/pmod-modules) [注3](#id8)；也可自行开发连接Pmod的接口。

<a id="set-up-the-arc-em-starter-kit"></a>

### 设置ARC EM Starter Kit

要在EM Starter Kit正确的ARC核上运行Zephyr，需正确设置开发板。


- 通过Digilent USB线将主机连接开发板。
- 将5 V直流电源连接开发板。
- 通过SW1拨码开关选择正确的处理器核配置，再按板上ARC标志字母C上方的FPGA配置按键。
- 开发板会按所选处理器核配置重新配置，之后即可下载及调试Zephyr应用。
- <a id="id12"></a>

  更多使用说明见[ARC EM Starter Kit用户指南](https://www.synopsys.com/dw/ipdir.php?ds=arc_em_starter_kit)[注2](#id6)。

<a id="set-up-zephyr-software"></a>

### 设置Zephyr软件

EM Starter Kit有不同固件版本，需选择Zephyr支持的相应版本。

此板有三种配置：


- EM7D：em_starterkit_em7d_defconfig
- EM9D：em_starterkit_defconfig
- EM11D：em_starterkit_em11d_defconfig

<a id="building-sample-applications"></a>

### 构建示例应用（Building Sample Applications）

可尝试多种示例或测试，这里以[samples/hello_world](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/hello_world)中的[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例。

<a id="configuring"></a>

#### 配置（Configuring）

若示例没有prj_arc.conf，可能需自行编写。随后可通过menuconfig配置目标；选择em_starterkit板级配置即可启用对应Zephyr支持。

```text
# From the root of the zephyr repository
west build -b em_starterkit samples/hello_world
west build -t menuconfig
```

此板还需在“ARC SoC Selection”中选择EM9D或EM11D。启动EM9D时，除1号开关外全部拨码向上；启动EM11D时，除2号开关外全部拨码向上。其他选项按常规配置，随后按板上ARC丝印字母C上方的按键。

<a id="building"></a>

#### 构建（Building）

应用可按常规方式构建，详情见“构建应用”。下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)）

```text
# From the root of the zephyr repository
west build -b em_starterkit samples/hello_world
```

<a id="connecting-serial-output"></a>

### 连接串口输出（Connecting Serial Output）

默认Zephyr EM Starter Kit镜像通过板上UART1输出串口日志，启用方法如下：

开发环境中需要：


- 打开串口终端，例如Linux中的minicom、PuTTY或screen。
- 指定tty设备名，例如Linux中的/dev/ttyUSB1。
- 通信参数设为：

<table>
<tr>
<th>参数（Parameter）</th>
<th>值（Value）</th>
</tr>
<tr>
<td>波特率（Baud）：</td>
<td>115200</td>
</tr>
<tr>
<td>数据位（Data）：</td>
<td>8位数据位</td>
</tr>
<tr>
<td>奇偶校验（Parity）：</td>
<td>无（None）</td>
</tr>
<tr>
<td>停止位（Stop Bits）：</td>
<td>1</td>
</tr>
</table>

<a id="debugging"></a>

### 调试（Debugging）

原文说明Zephyr SDK 0.9及更新版本可直接调试并加载EM Starter Kit；这里保留原文版本门槛。

一种方式是通过常规Zephyr构建命令构建并调试应用。

```text
west build -b em_starterkit <my app>
west debug
```

随后可按常规调试，设置断点，再输入c继续执行。

另一种方式是启动调试服务器：

```text
west build -b em_starterkit <my app>
west debugserver
```

再打开第二个终端，在包含输出zephyr.elf的构建目录连接EM Starter Kit调试服务器。

```text
$ cd <my app>
$ $ZEPHYR_SDK_INSTALL_DIR/arc-zephyr-elf/bin/arc-zephyr-elf-gdb zephyr.elf
(gdb) target remote localhost:3333
(gdb) load
(gdb) b main
(gdb) c
```

<a id="flashing"></a>

### 烧录（Flashing）

若只需将应用下载到EM Starter Kit的紧耦合存储器（CCM）或DDR并运行，也可按常规方式操作。

```text
west build -b em_starterkit
west flash
```

此命令仍使用OpenOCD及GDB加载应用ELF，但加载后立即运行；由于未持久保存，掉电后应用会丢失。

开发期间通常通过OpenOCD及GDB调试，程序经USB下载到代码及数据存储器，而非每次写入闪存。

需要在复位或上电后自动启动时，可按步骤将程序放入SPI闪存。

<a id="id5"></a>

SPI闪存写入方法见[embARC网站](https://www.embarc.org)[注1](#id2)上的ARC EM Starter Kit文档，其中说明如何将可执行镜像写成引导加载器可识别的格式。

<a id="release-notes"></a>

## 发布说明（Release Notes）

原文列出的待办事项（TODO）：


- GH-2647：Zephyr需要指令缓存API，涉及全部目标
- GH-2230：Zephyr的ARC移植尚不支持常规中断嵌套；此为原文待办状态
- 引脚复用驱动（Pinmux Driver）：可能还可用于配置Pmod

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔1〕 ([1](#id3),[2](#id4),[3](#id5)) [https://www.embarc.org](https://www.embarc.org)

<a id="id6"></a>

〔2〕 ([1](#id7),[2](#id12)) [https://www.synopsys.com/dw/ipdir.php?ds=arc_em_starter_kit](https://www.synopsys.com/dw/ipdir.php?ds=arc_em_starter_kit)

<a id="id8"></a>

〔[3](#id9)〕 [http://store.digilentinc.com/pmod-modules](http://store.digilentinc.com/pmod-modules)

<a id="id10"></a>

〔[4](#id11)〕 [https://www.putty.software](https://www.putty.software)

## 译注

EM Starter Kit仅支持原文列出的2.2／2.3固件。原文称最新2.3及SDK 0.9门槛、旧GH待办是该页历史叙述，不作为本翻译集的当前通用版本结论。加载到CCM／DDR的应用断电丢失。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [pmod-modules](http://store.digilentinc.com/pmod-modules)：HTTP Error 403: Forbidden。
- [www.embarc.org](https://www.embarc.org)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。

---

[上一章](P006_Tang_Mega_138K_Pro_Dock.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P008_ARC_EM_Software_Development_Platform.md)
