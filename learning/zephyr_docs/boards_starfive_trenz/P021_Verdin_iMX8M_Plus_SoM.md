---
id: learning.zephyr-docs.boards-starfive-trenz.page-21
title: Verdin iMX8M Plus SoM
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/toradex/verdin_imx8mp/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="verdin_imx8mp"></a>

# 第21章\_Verdin iMX8M Plus系统模块（SoM）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/toradex/verdin_imx8mp/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/verdin_imx8mp_front.jpg](images/verdin_imx8mp_front.jpg)](images/verdin_imx8mp_front.jpg)

Verdin iMX8M Plus系统模块（SoM）

名称（Name）：

`verdin_imx8mp`

厂商（Vendor）：

[Toradex AG](https://docs.zephyrproject.org/latest/boards/index.html#vendor=toradex)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mimx8ml8](https://docs.zephyrproject.org/latest/boards/index.html#soc=mimx8ml8)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/toradex/verdin_imx8mp/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Verdin iMX8M Plus是Toradex开发的计算机模块（Computer on Module，CoM），基于NXP i.MX 8M Plus处理器／SoC系列。

Verdin iMX8M Plus系列包括：

<table>
<tr>
<th>计算模块（Computer on Module，CoM）</th>
<th>片上系统（SoC）</th>
</tr>
<tr>
<td>Verdin iMX8M Plus Quad 8GB Wi-Fi／Bluetooth IT</td>
<td>i.MX 8M Plus Quad</td>
</tr>
<tr>
<td>Verdin iMX8M Plus Quad 4GB Wi-Fi／Bluetooth IT</td>
<td>i.MX 8M Plus Quad</td>
</tr>
<tr>
<td>Verdin iMX8M Plus Quad 4GB IT</td>
<td>i.MX 8M Plus Quad</td>
</tr>
<tr>
<td>Verdin iMX8M Plus Quad 2GB Wi-Fi／Bluetooth IT</td>
<td>i.MX 8M Plus Quad</td>
</tr>
<tr>
<td>Verdin iMX8M Plus QuadLite 1GB IT</td>
<td>i.MX 8M Plus QuadLite</td>
</tr>
</table>

原文引用NXP介绍：

> i.MX 8M Plus系列面向机器学习与视觉、先进多媒体及高可靠工业自动化，满足智能家居、楼宇、城市及工业4.0应用需求。

Verdin iMX8M Plus集成四个1.6 GHz Arm Cortex-A53 CPU及一个800 MHz Arm Cortex-M7F微控制器。

Cortex-A53集群采用Armv8-A，定位于兼顾性能及能效的中端处理器。四个核各有独立L1存储系统，共享具备附加功能的统一L2缓存，原文称该缓存位于单个APR区域。处理器支持ETM实时跟踪及JTAG静态调试，并通过Arm CoreSight ETM实现实时跟踪，借助交叉触发接口（CTI）及交叉触发矩阵（CTM）协调触发。

Cortex-M7用于实时控制，兼顾高性能及低中断延迟，并兼容现有Cortex-M系列。它采用顺序执行的超标量流水线，借助多个存储接口支持加载／加载、加载／存储等指令对双发射。这些接口包括紧耦合存储器（TCM）、哈佛式缓存及AXI主机接口。平台提供32 KB L1指令缓存、32 KB L1数据缓存、支持FPv5的浮点单元（FPU）及内部跟踪（TRC），支持160个IRQ，并集成ETM及CTI等CoreSight调试与跟踪组件。

<a id="hardware"></a>

## 硬件（Hardware）


- SoC：NXP i.MX 8M Plus
- CPU：四个1.6 GHz Arm Cortex-A53
- 微控制器：一个800 MHz Arm Cortex-M7F
- 存储器（Memory）：


  - A53侧RAM：1、2、4或8 GB
  - M7侧RAM：TCML、TCMU、OCRAM_S各32 KB，OCRAM为128 KB，DDR区域为256 MB；容量按原文保留
  - A53侧闪存：最高32 GB eMMC
- 连接功能（Connectivity）：


  - USB 3.1 Gen 1：一路主机及一路OTG
  - USB 2.0：一路主机及一路OTG
  - 支持时间敏感网络（TSN）的千兆以太网，另有第二路RGMII
  - 双频Wi-Fi 802.11ac，2×2多用户多输入多输出（MU-MIMO）
  - 蓝牙5（Bluetooth 5）
  - 五路I2C
  - 3 个 SPI 接口。
  - 一路QSPI
  - 四路UART
  - 最多92个GPIO
  - 四路模拟输入
  - 两路CAN，FlexCAN
- 多媒体（Multimedia）：

  > - 神经网络处理单元（NPU）
  > - 图像信号处理器（ISP）
  > - 2D及3D加速
  > - HDMI、MIPI DSI及MIPI CSI接口

Verdin iMX8M Plus及i.MX 8M Plus SoC更多信息见：


- [i.MX 8M Plus应用处理器页面](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS)
- [Verdin iMX8M Plus主页](https://www.toradex.com/computer-on-modules/verdin-arm-family/nxp-imx-8m-plus)
- [Verdin iMX8M Plus开发者页面](https://developer.toradex.com/hardware/verdin-som-family/modules/verdin-imx8m-plus)
- [Verdin Development Board开发者页面](https://developer.toradex.com/hardware/verdin-som-family/carrier-boards/verdin-development-board/)
- [Verdin iMX8M Plus数据手册](https://docs.toradex.com/110977-verdin_imx8m_plus_v1.1_datasheet.pdf)
- [Verdin Development Board数据手册](https://docs.toradex.com/109463-verdin_development_board_datasheet_v1.1.pdf)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`verdin_imx8mp`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="verdin_imx8mp-hw-features"></a>

<a id="verdin_imx8mp-verdin_imx8mp/mimx8ml8/m7-hw-features-section"></a>

#### `verdin_imx8mp/mimx8ml8/m7`目标（Target）

<a id="verdin_imx8mp-verdin_imx8mp/mimx8ml8/m7-hw-features-panel"></a>

<a id="verdin_imx8mp-verdin_imx8mp/mimx8ml8/m7-hw-features-memory"></a>

该开发板目标的片上存储容量：128 KiB RAM、128 KiB Flash。

<a id="verdin_imx8mp-verdin_imx8mp/mimx8ml8/m7-hw-features-table"></a>

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
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="2">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>i.MX指令紧耦合存储器（ITCM / Instruction Tightly Coupled Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P014_nxp_imx-itcm.md#std-dtcompatible-nxp-imx-itcm"><code>nxp,imx-itcm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX数据紧耦合存储器（DTCM / Data Tightly Coupled Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L45">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P012_nxp_imx-dtcm.md#std-dtcompatible-nxp-imx-dtcm"><code>nxp,imx-dtcm</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>i.MX时钟控制模块（CCM / Clock Controller Module）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L84">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P021_nxp_imx-ccm.md#std-dtcompatible-nxp-imx-ccm"><code>nxp,imx-ccm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">数字音频接口（DAI）</td>
<td>片上（On-Chip）</td>
<td>NXP同步音频接口（SAI / Synchronous Audio Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L315">已禁用：1</a>）</td>
<td><a href="../dai_binding_reference/P008_nxp_dai-sai.md#std-dtcompatible-nxp-dai-sai"><code>nxp,dai-sai</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP智能直接存储器访问（SDMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L307">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P006_nxp_sdma.md#std-dtcompatible-nxp-sdma"><code>nxp,sdma</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L127">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L101">已禁用：4</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P030_nxp_imx-gpio.md#std-dtcompatible-nxp-imx-gpio"><code>nxp,imx-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP II2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L182">已禁用：6</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P001_nxp_ii2c.md#std-dtcompatible-nxp-ii2c"><code>nxp,ii2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">处理器间消息（IPM）</td>
<td>片上（On-Chip）</td>
<td>i.MX消息单元（Messaging Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L266">已启用：1</a>）</td>
<td><a href="../intercore_reference/P072_NXPiMX消息单元绑定.md#dtbinding-nxp-imx-mu"><code>nxp,imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>这个兼容性绑定（Compatible Binding）应应用于设备的<code>iomuxc</code>设备树源文件（DTS）节点。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L90">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P023_nxp_imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc"><code>nxp,imx-iomuxc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MCUX片上系统（SoC）的设备树（Devicetree）为该节点设置了<code>pinctrl</code>节点标签。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L95">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P002_nxp_imx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl"><code>nxp,imx8mp-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX脉宽调制（PWM）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L328">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L354">已禁用：2</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P006_nxp_ipwm.md#std-dtcompatible-nxp-ipwm"><code>nxp,ipwm</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>此绑定（Binding）提供NXP i.MX IUART的基本描述（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L174">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L166">已禁用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P010_nxp_imx-iuart.md#std-dtcompatible-nxp-imx-iuart"><code>nxp,imx-iuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX增强型可配置串行外设接口（ECSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L277">已禁用：3</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P020_nxp_imx-ecspi.md#std-dtcompatible-nxp-imx-ecspi"><code>nxp,imx-ecspi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
</table>

<a id="verdin_imx8mp-verdin_imx8mp/mimx8ml8/m7/ddr-hw-features-section"></a>

#### `verdin_imx8mp/mimx8ml8/m7/ddr`目标（Target）

<a id="verdin_imx8mp-verdin_imx8mp/mimx8ml8/m7/ddr-hw-features-panel"></a>

<a id="verdin_imx8mp-verdin_imx8mp/mimx8ml8/m7/ddr-hw-features-memory"></a>

该开发板目标的片上存储容量：2 MiB RAM、2 MiB Flash。

<a id="verdin_imx8mp-verdin_imx8mp/mimx8ml8/m7/ddr-hw-features-table"></a>

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
<td>ARM Cortex-M7处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P005_arm_cortex-m7.md#std-dtcompatible-arm-cortex-m7"><code>arm,cortex-m7</code></a></td>
</tr>
<tr>
<td rowspan="2">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>i.MX指令紧耦合存储器（ITCM / Instruction Tightly Coupled Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P014_nxp_imx-itcm.md#std-dtcompatible-nxp-imx-itcm"><code>nxp,imx-itcm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX数据紧耦合存储器（DTCM / Data Tightly Coupled Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L45">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P012_nxp_imx-dtcm.md#std-dtcompatible-nxp-imx-dtcm"><code>nxp,imx-dtcm</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>i.MX时钟控制模块（CCM / Clock Controller Module）IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L84">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P021_nxp_imx-ccm.md#std-dtcompatible-nxp-imx-ccm"><code>nxp,imx-ccm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">数字音频接口（DAI）</td>
<td>片上（On-Chip）</td>
<td>NXP同步音频接口（SAI / Synchronous Audio Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L315">已禁用：1</a>）</td>
<td><a href="../dai_binding_reference/P008_nxp_dai-sai.md#std-dtcompatible-nxp-dai-sai"><code>nxp,dai-sai</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP智能直接存储器访问（SDMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L307">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P006_nxp_sdma.md#std-dtcompatible-nxp-sdma"><code>nxp,sdma</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L127">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L101">已禁用：4</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P030_nxp_imx-gpio.md#std-dtcompatible-nxp-imx-gpio"><code>nxp,imx-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP II2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L182">已禁用：6</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P001_nxp_ii2c.md#std-dtcompatible-nxp-ii2c"><code>nxp,ii2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">处理器间消息（IPM）</td>
<td>片上（On-Chip）</td>
<td>i.MX消息单元（Messaging Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L266">已启用：1</a>）</td>
<td><a href="../intercore_reference/P072_NXPiMX消息单元绑定.md#dtbinding-nxp-imx-mu"><code>nxp,imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>这个兼容性绑定（Compatible Binding）应应用于设备的<code>iomuxc</code>设备树源文件（DTS）节点。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L90">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P023_nxp_imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc"><code>nxp,imx-iomuxc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MCUX片上系统（SoC）的设备树（Devicetree）为该节点设置了<code>pinctrl</code>节点标签。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L95">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P002_nxp_imx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl"><code>nxp,imx8mp-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX脉宽调制（PWM）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L328">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L354">已禁用：2</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P006_nxp_ipwm.md#std-dtcompatible-nxp-ipwm"><code>nxp,ipwm</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>此绑定（Binding）提供NXP i.MX IUART的基本描述（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L174">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L166">已禁用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P010_nxp_imx-iuart.md#std-dtcompatible-nxp-imx-iuart"><code>nxp,imx-iuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX增强型可配置串行外设接口（ECSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi?plain=1#L277">已禁用：3</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P020_nxp_imx-ecspi.md#std-dtcompatible-nxp-imx-ecspi"><code>nxp,imx-ecspi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
</table>

建议在Linux侧禁用由M7使用的外设。

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="uart"></a>

#### 通用异步收发器（UART）

Zephyr默认使用UART4，在多数Toradex载板上连接FTDI USB转换器。

带Wi-Fi／Bluetooth芯片的模块也将UART4连接到无线芯片，因此Zephyr占用UART4时无线功能将不能正常工作。

如需Wi-Fi／Bluetooth，应为Zephyr改用其他UART，例如UART1。可修改[boards/toradex/verdin_imx8mp/verdin_imx8mp_mimx8ml8_m7.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/toradex/verdin_imx8mp/verdin_imx8mp_mimx8ml8_m7.dts)或同目录verdin_imx8mp_mimx8ml8_m7_ddr.dts中的zephyr,console及zephyr,shell-uart。（[boards/toradex/verdin_imx8mp/verdin_imx8mp_mimx8ml8_m7_ddr.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/toradex/verdin_imx8mp/verdin_imx8mp_mimx8ml8_m7_ddr.dts)）

<table>
<tr>
<th>开发板名称（Board Name）</th>
<th>SoC名称（SoC Name）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>UART_1</td>
<td>UART1</td>
<td>通用UART</td>
</tr>
<tr>
<td>UART_4</td>
<td>UART4</td>
<td>Cortex-M4调试UART</td>
</tr>
</table>

<a id="gpio"></a>

#### 通用输入输出（GPIO）

[dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi)启用全部可用GPIO组。

<a id="pwm"></a>

#### 脉宽调制（PWM）

PWM_1及PWM_2已启用并路由至Verdin连接器。

<table>
<tr>
<th>开发板名称（Board Name）</th>
<th>SoC名称（SoC Name）</th>
<th>Verdin连接器</th>
</tr>
<tr>
<td>PWM_1</td>
<td>PWM1</td>
<td>SODIMM第15脚</td>
</tr>
<tr>
<td>PWM_2</td>
<td>PWM2</td>
<td>SODIMM第16脚</td>
</tr>
</table>

PWM3及PWM4在[dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx8ml_m7.dtsi)中定义，但本模块不启用，因为相应焊盘用于USB_2_EN及CSI_1_MCLK，改作PWM会破坏USB及CSI功能。不需要这些信号的载板可自行选择引脚并启用相应实例。

<a id="system-clock"></a>

### 系统时钟（System Clock）

M7核配置为以800 MHz运行。

<a id="serial-port"></a>

### 串口（Serial Port）

i.MX8M Plus有四路UART，UART4配置为控制台，其余未使用或测试。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`verdin_imx8mp`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>复位（reset）</th>
<th>调试服务器（debugserver）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-jlink">jlink</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

Verdin iMX8M Plus没有供M7使用的QSPI闪存，M7需由A53启动。A53负责将M7应用加载到RAM、复位M7、设置程序计数器及栈指针，再解除复位；可在引导加载器阶段或Linux启动后执行。

M7最多可使用3种RAM，目前仅支持指令紧耦合存储器（ITCM）及DDR两种配置。A53与M7的内存映射如下：

<table>
<tr>
<th>区域（Region）</th>
<th>Cortex-A53</th>
<th>Cortex-M7系统总线（System Bus）</th>
<th>Cortex-M7代码总线（Code Bus）</th>
<th>大小（Size）</th>
</tr>
<tr>
<td>片上RAM（OCRAM）</td>
<td>0x00900000-0x0098FFFF</td>
<td>0x20200000-0x2028FFFF</td>
<td>0x00900000-0x0098FFFF</td>
<td>576KB</td>
</tr>
<tr>
<td>数据紧耦合存储器（DTCM）</td>
<td>0x00800000-0x0081FFFF</td>
<td>0x20000000-0x2001FFFF</td>
<td></td>
<td>128KB</td>
</tr>
<tr>
<td>指令紧耦合存储器（ITCM）</td>
<td>0x007E0000-0x007FFFFF</td>
<td></td>
<td>0x00000000-0x0001FFFF</td>
<td>128KB</td>
</tr>
<tr>
<td>OCRAM_S</td>
<td>0x00180000-0x00188FFF</td>
<td>0x20180000-0x20188FFF</td>
<td>0x00180000-0x00188FFF</td>
<td>36KB</td>
</tr>
<tr>
<td>双倍数据率存储器（DDR）</td>
<td>0x80000000-0x803FFFFF</td>
<td>0x80200000-0x803FFFFF</td>
<td>0x80000000-0x801FFFFF</td>
<td>2MB</td>
</tr>
</table>

内存映射详情见《[i.MX 8M Plus应用处理器参考手册](https://www.nxp.com/webapp/Download?colCode=IMX8MPRM)》第2.1—2.3节。

编译时需选择使用的RAM，为便于配置提供两个目标：


- verdin_imx8mp/mimx8ml8/m7：采用指令紧耦合存储器（ITCM）配置
- verdin_imx8mp/mimx8ml8/m7/ddr：采用DDR配置

<a id="starting-the-cortex-m7-via-u-boot"></a>

### 通过U-Boot启动Cortex-M7

通过A53上的U-Boot加载并运行M7 Zephyr镜像：把编译得到的zephyr.bin复制到SD卡第一个FAT分区，插入开发板，上电后在提示符处停止U-Boot执行。

使用以下命令将M7二进制加载到所需存储器并启动：

<a id="itcm"></a>

### 指令紧耦合存储器（ITCM）

从EXT4分区加载二进制：

```text
ext4load mmc 2:2 ${loadaddr} /<path-to-binary>/zephyr.bin
cp.b ${loadaddr} 0x7e0000 <size_of_binary_in_bytes>
bootaux 0x7e0000
```

<a id="ddr"></a>

### 双倍数据率存储器（DDR）

从EXT4分区加载二进制：

```text
ext4load mmc 2:2 ${loadaddr} /<path-to-binary>/zephyr.bin
cp.b ${loadaddr} 0x80000000 <size_of_binary_in_bytes>
bootaux 0x80000000
```

<a id="debugging"></a>

### 调试（Debugging）

可将外部J-Link JTAG调试器连接X56调试连接器及电脑，也可直接用USB-C连接Verdin Development Board的X66，然后按常规方式调试应用。

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b verdin_imx8mp/mimx8ml8/m7/ddr samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
*** Booting Zephyr OS build zephyr-v3.4.0-2300-g03905f7e55d2  ***
Hello World! verdin_imx8mp
```

<a id="references"></a>

### 参考资料（References）


- [如何将编译后的二进制加载到Cortex-M](https://developer.toradex.com/software/real-time/cortex-m/how-to-load-binaries)
- [Cortex-M JTAG调试](https://developer.toradex.com/software/real-time/cortex-m/cortexm-jtag-debugging/)
- [NXP网站](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/evaluation-kit-for-the-i-mx-8m-plus-applications-processor:8MPLUSLPD4-EVK)

## 译注

Verdin iMX8M Plus的UART4与Wi-Fi／Bluetooth冲突，原文替代控制台为UART1；PWM3／4因引脚复用默认关闭。ITCM与DDR目标、Linux释放外设与A53加载M7的要求分别保留。官方verdin_imx8mp_front.jpg文件内容实际为PNG；重新下载后字节一致，PNG校验及解码通过，保留原始文件名与原始内容，并在图片清单记录实际格式。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [](https://developer.toradex.com/hardware/verdin-som-family/carrier-boards/verdin-development-board/)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1010)>。
- [verdin-imx8m-plus](https://developer.toradex.com/hardware/verdin-som-family/modules/verdin-imx8m-plus)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1010)>。
- [](https://developer.toradex.com/software/real-time/cortex-m/cortexm-jtag-debugging/)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1010)>。
- [how-to-load-binaries](https://developer.toradex.com/software/real-time/cortex-m/how-to-load-binaries)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1010)>。
- [109463-verdin_development_board_datasheet_v1.1.pdf](https://docs.toradex.com/109463-verdin_development_board_datasheet_v1.1.pdf)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1010)>。
- [110977-verdin_imx8m_plus_v1.1_datasheet.pdf](https://docs.toradex.com/110977-verdin_imx8m_plus_v1.1_datasheet.pdf)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1010)>。
- [evaluation-kit-for-the-i-mx-8m-plus-applications-processor:8MPLUSLPD4-EVK](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/evaluation-kit-for-the-i-mx-8m-plus-applications-processor:8MPLUSLPD4-EVK)：HTTP Error 404: Not Found。
- [i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS)：HTTP Error 404: Not Found。
- [Download?colCode=IMX8MPRM](https://www.nxp.com/webapp/Download?colCode=IMX8MPRM)：HTTP Error 404: Not Found。
- [nxp-imx-8m-plus](https://www.toradex.com/computer-on-modules/verdin-arm-family/nxp-imx-8m-plus)：HTTP Error 403: Forbidden。

---

[上一章](P020_Verdin_iMX8M_Mini.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P022_Trenz_Electronic.md)
