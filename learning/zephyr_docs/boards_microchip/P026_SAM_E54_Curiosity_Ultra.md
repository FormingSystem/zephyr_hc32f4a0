---
id: learning.zephyr-docs.boards-microchip.page-26
title: SAM E54 Curiosity Ultra
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/microchip/sam/sam_e54_cult/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="sam_e54_cult"></a>

# 第26章\_SAM E54 Curiosity Ultra

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/microchip/sam/sam_e54_cult/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../../_images/sam_e54_cult.webp](images/sam_e54_cult.webp)](images/sam_e54_cult.webp)

SAM E54 Curiosity Ultra

名称（Name）：

`sam_e54_cult`

厂商（Vendor）：

[微芯科技（Microchip Technology Inc.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=microchip)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[atsame54p20a](https://docs.zephyrproject.org/latest/boards/index.html#soc=atsame54p20a)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/sam/sam_e54_cult/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

SAM E54 Curiosity Ultra评估套件适合评估基于Cortex®-M4F处理器的SAM E54微控制器及进行原型开发。套件包含Microchip嵌入式调试器（EDBG），无需额外硬件即可提供完整调试接口。

<a id="hardware"></a>

## 硬件（Hardware）


- ATSAME54P20A，120 MHz，1 MB闪存，256 KB RAM
- 板载调试器（EDBG）
- 虚拟COM端口（VCOM）
- 数据网关接口（DGI / Data Gateway Interface）
- 一个mikroBUS接口
- 一个支持蓝牙及音频的X32音频接口
- 以太网接口（Ethernet Interface）
- 图形接口（Graphics Interface）
- 兼容Xplained Pro扩展的接口
- CAN接口
- 用户按键（User Buttons）
- 用户LED
- 8 MB QSPI存储器
- 兼容Arduino Uno R3的接口

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`sam_e54_cult`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="sam_e54_cult-hw-features"></a>

<a id="sam_e54_cult-sam_e54_cult/atsame54p20a-hw-features-section"></a>

#### `sam_e54_cult/atsame54p20a`目标（Target）

<a id="sam_e54_cult-sam_e54_cult/atsame54p20a-hw-features-panel"></a>

<a id="sam_e54_cult-sam_e54_cult/atsame54p20a-hw-features-memory"></a>

此开发板目标可用存储器：256 KiB RAM、1 MiB 闪存。

<a id="sam_e54_cult-sam_e54_cult/atsame54p20a-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Microchip ADC G1驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L395">已禁用：2</a>）</td>
<td><a href="../hardware/P859_MicrochipG1模数转换器绑定.md#dtbinding-microchip-adc-g1"><code>microchip,adc-g1</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>Microchip SERCOM模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L158">已禁用：7</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P013_microchip_sercom-g1.md#std-dtcompatible-microchip-sercom-g1"><code>microchip,sercom-g1</code></a></td>
</tr>
<tr>
<td rowspan="10">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Microchip SAM_D5x_E5x SoC系列时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L49">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_sam_binding_reference/P022_microchip_sam-d5x-e5x-clock.md#std-dtcompatible-microchip-sam-d5x-e5x-clock"><code>microchip,sam-d5x-e5x-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SAM_D5x_E5x晶体振荡器（XOSC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L60">已启用：1</a>）</td>
<td><a href="../clock_sam_nordic_binding_reference/P005_microchip_sam-d5x-e5x-xosc.md#std-dtcompatible-microchip-sam-d5x-e5x-xosc"><code>microchip,sam-d5x-e5x-xosc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SAM_D5x_E5x内部振荡器（OSC48M）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L64">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_sam_binding_reference/P023_microchip_sam-d5x-e5x-dfll.md#std-dtcompatible-microchip-sam-d5x-e5x-dfll"><code>microchip,sam-d5x-e5x-dfll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SAM_D5x_E5x FDPLL时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L68">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_sam_binding_reference/P024_microchip_sam-d5x-e5x-fdpll.md#std-dtcompatible-microchip-sam-d5x-e5x-fdpll"><code>microchip,sam-d5x-e5x-fdpll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SAM_D5x_E5x RTC时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../clock_sam_nordic_binding_reference/P004_microchip_sam-d5x-e5x-rtc.md#std-dtcompatible-microchip-sam-d5x-e5x-rtc"><code>microchip,sam-d5x-e5x-rtc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SAM_D5x_E5x外部晶体振荡器（XOSC32K）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L77">已启用：1</a>）</td>
<td><a href="../clock_sam_nordic_binding_reference/P006_microchip_sam-d5x-e5x-xosc32k.md#std-dtcompatible-microchip-sam-d5x-e5x-xosc32k"><code>microchip,sam-d5x-e5x-xosc32k</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SAM_D5x_E5x通用时钟发生器（Generic Clock Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L81">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_sam_binding_reference/P025_microchip_sam-d5x-e5x-gclkgen.md#std-dtcompatible-microchip-sam-d5x-e5x-gclkgen"><code>microchip,sam-d5x-e5x-gclkgen</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SAM_D5x_E5x通用时钟外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L85">已启用：1</a>）</td>
<td><a href="../clock_sam_nordic_binding_reference/P001_microchip_sam-d5x-e5x-gclkperiph.md#std-dtcompatible-microchip-sam-d5x-e5x-gclkperiph"><code>microchip,sam-d5x-e5x-gclkperiph</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SAM_D5x_E5x CPU主时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L90">已启用：1</a>）</td>
<td><a href="../clock_sam_nordic_binding_reference/P002_microchip_sam-d5x-e5x-mclkcpu.md#std-dtcompatible-microchip-sam-d5x-e5x-mclkcpu"><code>microchip,sam-d5x-e5x-mclkcpu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SAM_D5x_E5x MCLK外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L95">已启用：1</a>）</td>
<td><a href="../clock_sam_nordic_binding_reference/P003_microchip_sam-d5x-e5x-mclkperiph.md#std-dtcompatible-microchip-sam-d5x-e5x-mclkperiph"><code>microchip,sam-d5x-e5x-mclkperiph</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1模拟比较器（Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L356">已禁用：1</a>）</td>
<td><a href="../hardware/P756_Microchip模拟比较器通道绑定.md#dtbinding-microchip-ac-g1-comparator"><code>microchip,ac-g1-comparator</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Microchip TC G1外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L178">已禁用：8</a>）</td>
<td><a href="../microchip_soc_counter_binding_reference/P010_microchip_tc-g1.md#std-dtcompatible-microchip-tc-g1"><code>microchip,tc-g1</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip TCC G1定时器／计数器外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L295">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L306">已禁用：1</a>）</td>
<td><a href="../microchip_soc_counter_binding_reference/P013_microchip_tcc-g1.md#std-dtcompatible-microchip-tcc-g1"><code>microchip,tcc-g1</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1 DAC（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L431">已禁用：1</a>）</td>
<td><a href="../hardware/P776_MicrochipG1数模转换器绑定.md#dtbinding-microchip-dac-g1"><code>microchip,dac-g1</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1 DMA控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L264">已启用：1</a>）</td>
<td><a href="../intel_microchip_dma_binding_reference/P013_microchip_dmac-g1-dma.md#std-dtcompatible-microchip-dmac-g1-dma"><code>microchip,dmac-g1-dma</code></a></td>
</tr>
<tr>
<td rowspan="2">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1 GMAC以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/same54.dtsi?plain=1#L9">已禁用：1</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P016_microchip_gmac-g1-eth.md#std-dtcompatible-microchip-gmac-g1-eth"><code>microchip,gmac-g1-eth</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip G1 GMAC MDIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/same54.dtsi?plain=1#L20">已禁用：1</a>）</td>
<td><a href="../ethernet_mac_mdio_binding_reference/P020_microchip_gmac-g1-mdio.md#std-dtcompatible-microchip-gmac-g1-mdio"><code>microchip,gmac-g1-mdio</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip NVMCTRL（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x_20.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P022_microchip_nvmctrl-g1-flash.md#std-dtcompatible-microchip-nvmctrl-g1-flash"><code>microchip,nvmctrl-g1-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Microchip Port G1 GPIO（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L245">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L254">已禁用：1</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P001_microchip_port-g1-gpio.md#std-dtcompatible-microchip-port-g1-gpio"><code>microchip,port-g1-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1硬件信息（hwinfo）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L37">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P005_microchip_hwinfo-g1.md#std-dtcompatible-microchip-hwinfo-g1"><code>microchip,hwinfo-g1</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/sam/sam_e54_cult/sam_e54_cult.dts?plain=1#L44">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip EIC G1设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L133">已启用：1</a>）</td>
<td><a href="../infineon_microchip_interrupt_binding_reference/P007_microchip_eic-g1-intc.md#std-dtcompatible-microchip-eic-g1-intc"><code>microchip,eic-g1-intc</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/sam/sam_e54_cult/sam_e54_cult.dts?plain=1#L30">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x_20.dtsi?plain=1#L14">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Microchip PORT引脚控制（Pinctrl）容器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L238">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P006_microchip_port-g1-pinctrl.md#std-dtcompatible-microchip-port-g1-pinctrl"><code>microchip,port-g1-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip RSTC复位（Reset）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L101">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P006_microchip_rstc-g1-reset.md#std-dtcompatible-microchip-rstc-g1-reset"><code>microchip,rstc-g1-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Microchip TRNG G1熵（Entropy）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L366">已禁用：1</a>）</td>
<td><a href="../rng_binding_reference/P010_microchip_trng-g1-entropy.md#std-dtcompatible-microchip-trng-g1-entropy"><code>microchip,trng-g1-entropy</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1 RTC驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L120">已禁用：1</a>）</td>
<td><a href="../rtc_binding_reference/P015_microchip_rtc-g1.md#std-dtcompatible-microchip-rtc-g1"><code>microchip,rtc-g1</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>Microchip SDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L447">已禁用：2</a>）</td>
<td><a href="../sdhc_binding_reference/P012_microchip_sdhc-g1.md#std-dtcompatible-microchip-sdhc-g1"><code>microchip,sdhc-g1</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip SERCOM UART控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L168">已启用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P019_microchip_sercom-g1-uart.md#std-dtcompatible-microchip-sercom-g1-uart"><code>microchip,sercom-g1-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x_20.dtsi?plain=1#L9">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Microchip G1看门狗（Watchdog）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/sam/sam_d5x_e5x/common/samd5xe5x.dtsi?plain=1#L106">已禁用：1</a>）</td>
<td><a href="../soc_pmic_watchdog_binding_reference/P010_microchip_wdt-g1.md#std-dtcompatible-microchip-wdt-g1"><code>microchip,wdt-g1</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

SAM E54 Curiosity Ultra用户指南提供开发板连接详情。（[SAM E54 Curiosity Ultra用户指南（User Guide）](https://ww1.microchip.com/downloads/aemDocuments/documents/MCU32/ProductDocuments/UserGuides/SAM-E54-Curiosity-Ultra-User%E2%80%99s-Guide-DS70005405.pdf)）

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

SAM E54 Curiosity Ultra带Microchip板载嵌入式调试器（EDBG），同时提供标准调试接口和用作Zephyr控制台的虚拟串口。ATSAME54P20A MCU的SERCOM1配置为USART，用于控制台输出。


1. 通过调试USB端口将开发板连接主机。
2. 打开终端，在对应端口启动串行控制台。Linux下通常为/dev/ttyACM0，例如：

  ```text
  $ minicom -D /dev/ttyACM0 -o
  ```

  `-o`选项让`minicom`不发送调制解调器初始化字符串（Modem Initialization String）。连接参数应配置如下：


  - 速率（Speed）：115200波特率
  - 数据位（Data）：8位
  - 奇偶校验（Parity）：无（None）
  - 停止位（Stop Bits）：1位
3. 构建并烧录Zephyr hello_world示例应用：

  ```text
  west build -b sam_e54_cult samples/hello_world
  west flash
  ```
4. 观察终端输出。若设置正确，应看到：

  ```text
  Hello World! sam_e54_cult
  ```

<a id="references"></a>

## 参考资料（References）

SAM E54产品页面：

[https://www.microchip.com/en-us/product/ATSAME54P20A](https://www.microchip.com/en-us/product/ATSAME54P20A)

SAM E54 Curiosity Ultra评估套件页面：

[https://www.microchip.com/en-us/development-tool/EV66Z56A](https://www.microchip.com/en-us/development-tool/EV66Z56A)

## 译注

控制台使用SERCOM1；不要套用Xplained Pro页面的SERCOM2。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [EV66Z56A](https://www.microchip.com/en-us/development-tool/EV66Z56A)：HTTP Error 403: Forbidden。
- [ATSAME54P20A](https://www.microchip.com/en-us/product/ATSAME54P20A)：HTTP Error 403: Forbidden。

---

[上一章](P025_PIC64GX1000_Curiosity_kit.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P027_SAM_E54_Xplained_Pro.md)
