---
id: learning.zephyr-docs.boards-renesas-rx-rz.page-20
title: R-Car Salvator-XS
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/renesas/rcar_salvator_xs/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rcar_salvator_xs"></a>

# 第20章\_R-Car Salvator-XS开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/renesas/rcar_salvator_xs/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/rcar_salvator_xs.jpg](images/rcar_salvator_xs.jpg)](images/rcar_salvator_xs.jpg)

R-Car Salvator-XS开发板

名称（Name）：

`rcar_salvator_xs`

厂商（Vendor）：

[瑞萨电子（Renesas Electronics Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=renesas)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[r8a77961](https://docs.zephyrproject.org/latest/boards/index.html#soc=r8a77961)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rcar_salvator_xs/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

R-Car M3-W是一款提供下一代汽车导航系统基本功能的片上系统（SoC）。

<a id="hardware"></a>

## 硬件（Hardware）

R-Car M3-W包括：


- 两个1.5 GHz Arm Cortex-A57 MPCore内核；
- 四个1.3 GHz Arm Cortex-A53 MPCore内核；
- LPDDR4-3200存储控制器，两个32位通道；
- 一个HDMI 1.4b输出通道、一个RGB888输出通道及一个LVDS通道；
- 两个MIPI-CSI2视频输入通道及两个数字视频输入通道；
- 一个USB 3.0及两个USB 2.0接口；
- 800 MHz Arm Cortex-R7内核；
- 二维及三维图形引擎；
- 视频处理单元；
- 音频处理单元；
- MediaLB接口；
- SD卡主机接口；
- USB 3.0及USB 2.0接口；
- PCI Express接口；
- CAN接口。
- 以太网音视频桥接（EtherAVB）

Salvator-XS硬件能力见[eLinux Salvator-XS页面](https://elinux.org/R-Car/Boards/Salvator-XS)。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`rcar_salvator_xs`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="rcar_salvator_xs-hw-features"></a>

<a id="rcar_salvator_xs-rcar_salvator_xs/r8a77961-hw-features-section"></a>

#### `rcar_salvator_xs/r8a77961`目标（Target）

<a id="rcar_salvator_xs-rcar_salvator_xs/r8a77961-hw-features-panel"></a>

<a id="rcar_salvator_xs-rcar_salvator_xs/r8a77961-hw-features-memory"></a>

该开发板目标的片上存储容量：512 MiB RAM、N/A Flash。

<a id="rcar_salvator_xs-rcar_salvator_xs/r8a77961-hw-features-table"></a>

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
<td>Arm Cortex-A57处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/r8a77961.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P010_arm_cortex-a57.md#std-dtcompatible-arm-cortex-a57"><code>arm,cortex-a57</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>瑞萨R8A7795 SoC时钟脉冲发生器（CPG）、模块待机及软件复位（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L69">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P025_renesas_r8a7795-cpg-mssr.md#std-dtcompatible-renesas-r8a7795-cpg-mssr"><code>renesas,r8a7795-cpg-mssr</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Renesas R-Car通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L76">已禁用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P017_renesas_rcar-gpio.md#std-dtcompatible-renesas-rcar-gpio"><code>renesas,rcar-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v2（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L51">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P003_arm_gic-v2.md#std-dtcompatible-arm-gic-v2"><code>arm,gic-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Renesas R-Car Gen3／Gen4引脚功能控制器（Pin Function Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L109">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P009_renesas_rcar-pfc.md#std-dtcompatible-renesas-rcar-pfc"><code>renesas,rcar-pfc</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>片上（On-Chip）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>固定电压稳压器（Fixed Voltage Regulators）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L31">已启用：2</a>）</td>
<td><a href="../hardware/P635_固定稳压器设备树绑定.md#dtbinding-regulator-fixed"><code>regulator-fixed</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>瑞萨R-Car嵌入式多媒体卡（eMMC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L87">已禁用：2</a>）</td>
<td><a href="../sdhc_binding_reference/P018_renesas_rcar-mmc.md#std-dtcompatible-renesas-rcar-mmc"><code>renesas,rcar-mmc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>瑞萨R-Car UART控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L114">已启用：1</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P010_renesas_rcar-scif.md#std-dtcompatible-renesas-rcar-scif"><code>renesas,rcar-scif</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rcar_gen3_ca57.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

按通常方式构建并烧录应用，详见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）与“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

<a id="references"></a>

## 参考资料（References）


- [瑞萨R-Car开发支持网站](https://www.renesas.com/us/en/support/partners/r-car-consortium/r-car-development-support)
- [eLinux Salvator-XS页面](https://elinux.org/R-Car/Boards/Salvator-XS)

## 译注

Salvator-XS的SoC为R-Car M3-W，勿套用Salvator-X的H3规格。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [r-car-development-support](https://www.renesas.com/us/en/support/partners/r-car-consortium/r-car-development-support)：HTTP Error 429: Too Many Requests。

---

[上一章](P019_R-Car_Salvator-X.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P021_Renesas_Starter_Kit_for_RX130.md)
