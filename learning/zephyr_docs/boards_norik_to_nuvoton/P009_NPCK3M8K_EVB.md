---
id: learning.zephyr-docs.boards-norik-to-nuvoton.page-9
title: NPCK3M8K EVB
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nuvoton/npck3m8k_evb/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="npck3m8k_evb"></a>

# 第9章\_NPCK3M8K_EVB

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nuvoton/npck3m8k_evb/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/npck3m8k_evb.webp](images/npck3m8k_evb.webp)](images/npck3m8k_evb.webp)

NPCK3M8K_EVB

名称（Name）：

`npck3m8k_evb`

厂商（Vendor）：

[新唐科技（Nuvoton Technology Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nuvoton)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[npck3m8k](https://docs.zephyrproject.org/latest/boards/index.html#soc=npck3m8k)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nuvoton/npck3m8k_evb/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

NPCK3M8K_EVB套件是用于评估新唐（Nuvoton）NPCK3系列微控制器的开发平台，提供多种外设及接口，供开发和测试使用，需要配套NPCK3M8K器件。

<a id="hardware"></a>

## 硬件（Hardware）


- ARM Cortex-M4F处理器
- 352 KB RAM及64 KB启动ROM
- GPIO排针
- UART0及UART1
- JTAG接口

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`npck3m8k_evb`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="npck3m8k_evb-hw-features"></a>

<a id="npck3m8k_evb-npck3m8k_evb/npck3m8k-hw-features-section"></a>

#### `npck3m8k_evb/npck3m8k`目标（Target）

<a id="npck3m8k_evb-npck3m8k_evb/npck3m8k-hw-features-panel"></a>

<a id="npck3m8k_evb-npck3m8k_evb/npck3m8k-hw-features-memory"></a>

该开发板目标的片上存储容量：62 KiB RAM、416 KiB Flash。

<a id="npck3m8k_evb-npck3m8k_evb/npck3m8k-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX ADC节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L389">已禁用：1</a>）</td>
<td><a href="../hardware/P892_NuvotonNPCX模数转换器绑定.md#dtbinding-nuvoton-npcx-adc"><code>nuvoton,npcx-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX电源及时钟控制器（PCC）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L80">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P009_nuvoton_npcx-pcc.md#std-dtcompatible-nuvoton-npcx-pcc"><code>nuvoton,npcx-pcc</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCK变体的NPCK-LCT节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck3.dtsi?plain=1#L269">已禁用：1</a>）</td>
<td><a href="../microchip_soc_counter_binding_reference/P018_nuvoton_npck-lct.md#std-dtcompatible-nuvoton-npck-lct"><code>nuvoton,npck-lct</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX GDMA节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L613">已禁用：1</a>）</td>
<td><a href="../intel_microchip_dma_binding_reference/P017_nuvoton_npcx-gdma.md#std-dtcompatible-nuvoton-npcx-gdma"><code>nuvoton,npcx-gdma</code></a></td>
</tr>
<tr>
<td rowspan="5">增强型串行外设接口（ESPI）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX eSPI虚拟线（VW / Virtual Wire）映射子节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck-espi-vws-map.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../espi_binding_reference/P010_nuvoton_npcx-espi-vw-conf.md#std-dtcompatible-nuvoton-npcx-espi-vw-conf"><code>nuvoton,npcx-espi-vw-conf</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐NPCX eSPI节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L407">已启用：1</a>）</td>
<td><a href="../espi_binding_reference/P011_nuvoton_npcx-espi.md#std-dtcompatible-nuvoton-npcx-espi"><code>nuvoton,npcx-espi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐eSPI TAF控制器访问的目标闪存设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck3.dtsi?plain=1#L260">已禁用：1</a>）</td>
<td><a href="../espi_binding_reference/P009_nuvoton_npcx-espi-taf.md#std-dtcompatible-nuvoton-npcx-espi-taf"><code>nuvoton,npcx-espi-taf</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐NPCX主机子模块（Host Sub-Modules）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L425">已启用：1</a>）</td>
<td><a href="../espi_binding_reference/P012_nuvoton_npcx-host-sub.md#std-dtcompatible-nuvoton-npcx-host-sub"><code>nuvoton,npcx-host-sub</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐NPCX主机UART I/O节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L636">已禁用：1</a>）</td>
<td><a href="../espi_binding_reference/P013_nuvoton_npcx-host-uart.md#std-dtcompatible-nuvoton-npcx-host-uart"><code>nuvoton,npcx-host-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>定义闪存接口单元（FIU）中NPCX四线SPI外设的属性（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L584">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P005_nuvoton_npcx-fiu-qspi.md#std-dtcompatible-nuvoton-npcx-fiu-qspi"><code>nuvoton,npcx-fiu-qspi</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX GPIO（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L137">已启用：20</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P023_nuvoton_npcx-gpio.md#std-dtcompatible-nuvoton-npcx-gpio"><code>nuvoton,npcx-gpio</code></a></td>
</tr>
<tr>
<td rowspan="2">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L461">已禁用：6</a>）</td>
<td><a href="../i2c_infineon_ite_nordic_binding_reference/P018_nuvoton_npcx-i2c-ctrl.md#std-dtcompatible-nuvoton-npcx-i2c-ctrl"><code>nuvoton,npcx-i2c-ctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐NPCX I2C端口焊盘（Port Pads）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L641">已禁用：10</a>）</td>
<td><a href="../i2c_infineon_ite_nordic_binding_reference/P019_nuvoton_npcx-i2c-port.md#std-dtcompatible-nuvoton-npcx-i2c-port"><code>nuvoton,npcx-i2c-port</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX键盘扫描控制器（Keyboard Scan Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L603">已启用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P009_nuvoton_npcx-kbd.md#std-dtcompatible-nuvoton-npcx-kbd"><code>nuvoton,npcx-kbd</code></a></td>
</tr>
<tr>
<td rowspan="4">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>NPCX MIWU唤醒单元输入（WUI）映射子节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck-miwus-wui-map.dtsi?plain=1#L9">已启用：1</a>）</td>
<td><a href="../wakeup_interrupt_binding_reference/P009_nuvoton_npcx-miwu-wui-map.md#std-dtcompatible-nuvoton-npcx-miwu-wui-map"><code>nuvoton,npcx-miwu-wui-map</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐NPCX多输入唤醒单元（MIWU）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L116">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck-miwus-wui-map.dtsi?plain=1#L602">已禁用：1</a>）</td>
<td><a href="../wakeup_interrupt_binding_reference/P010_nuvoton_npcx-miwu.md#std-dtcompatible-nuvoton-npcx-miwu"><code>nuvoton,npcx-miwu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NPCX MIWU分组中断（Group-interrupt）映射子节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck-miwus-int-map.dtsi?plain=1#L10">已启用：3</a>）</td>
<td><a href="../wakeup_interrupt_binding_reference/P008_nuvoton_npcx-miwu-int-map.md#std-dtcompatible-nuvoton-npcx-miwu-int-map"><code>nuvoton,npcx-miwu-int-map</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/npck3m8k_evb/npck3m8k_evb.dts?plain=1#L42">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/npck3m8k_evb/npck3m8k_evb.dts?plain=1#L51">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX电池后备RAM（Battery Backed RAM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P014_nuvoton_npcx-bbram.md#std-dtcompatible-nuvoton-npcx-bbram"><code>nuvoton,npcx-bbram</code></a></td>
</tr>
<tr>
<td rowspan="2">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX SoC标识（ID）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L737">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P023_nuvoton_npcx-soc-id.md#std-dtcompatible-nuvoton-npcx-soc-id"><code>nuvoton,npcx-soc-id</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐NPCX引导程序（Booter）变体选项（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L742">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P022_nuvoton_npcx-booter-variant.md#std-dtcompatible-nuvoton-npcx-booter-variant"><code>nuvoton,npcx-booter-variant</code></a></td>
</tr>
<tr>
<td rowspan="1">平台环境控制接口（PECI）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX PECI节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L593">已启用：1</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P005_nuvoton_npcx-peci.md#std-dtcompatible-nuvoton-npcx-peci"><code>nuvoton,npcx-peci</code></a></td>
</tr>
<tr>
<td rowspan="6">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX7引脚复用（Pin-Mux）配置：从NPCX GPIO到引脚复用控制器SCFG驱动实例的配置映射（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck-alts-map.dtsi?plain=1#L8">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P012_nuvoton_npcx-pinctrl-conf.md#std-dtcompatible-nuvoton-npcx-pinctrl-conf"><code>nuvoton,npcx-pinctrl-conf</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐NPCX7低电压电平检测配置：NPCX GPIO与低电压控制器LV_GPIO_CTL驱动实例之间的配置映射（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck-lvol-ctrl-map.dtsi?plain=1#L8">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P011_nuvoton_npcx-lvolctrl-conf.md#std-dtcompatible-nuvoton-npcx-lvolctrl-conf"><code>nuvoton,npcx-lvolctrl-conf</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐NPCX系统配置，包括引脚复用及1.8 V支持等（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P016_nuvoton_npcx-scfg.md#std-dtcompatible-nuvoton-npcx-scfg"><code>nuvoton,npcx-scfg</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐NPCX默认引脚配置（Default Pins Configurations）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L49">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P013_nuvoton_npcx-pinctrl-def.md#std-dtcompatible-nuvoton-npcx-pinctrl-def"><code>nuvoton,npcx-pinctrl-def</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐引脚控制器是单例节点（Singleton Node），负责控制引脚功能选择及引脚属性（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L58">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P015_nuvoton_npcx-pinctrl.md#std-dtcompatible-nuvoton-npcx-pinctrl"><code>nuvoton,npcx-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐NPCX漏电I/O（Power Leakage IOs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P010_nuvoton_npcx-leakage-io.md#std-dtcompatible-nuvoton-npcx-leakage-io"><code>nuvoton,npcx-leakage-io</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX电源开关逻辑（PSL / Power Switch Logic）控制节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L731">已禁用：1</a>）</td>
<td><a href="../power_control_binding_reference/P011_nuvoton_npcx-power-psl.md#std-dtcompatible-nuvoton-npcx-power-psl"><code>nuvoton,npcx-power-psl</code></a></td>
</tr>
<tr>
<td rowspan="2">PS/2 接口（PS/2）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX PS/2控制器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L563">已启用：1</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P014_nuvoton_npcx-ps2-ctrl.md#std-dtcompatible-nuvoton-npcx-ps2-ctrl"><code>nuvoton,npcx-ps2-ctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐NPCX PS/2通道焊盘节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L570">已禁用：2</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P013_nuvoton_npcx-ps2-channel.md#std-dtcompatible-nuvoton-npcx-ps2-channel"><code>nuvoton,npcx-ps2-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX脉宽调制器（PWM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L326">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L317">已禁用：7</a>）</td>
<td><a href="../pwm_intel_microchip_nxp_binding_reference/P017_nuvoton_npcx-pwm.md#std-dtcompatible-nuvoton-npcx-pwm"><code>nuvoton,npcx-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>执行电压转温度（V2T）测量（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L556">已禁用：1</a>）</td>
<td><a href="../sensor_microchip_nordic_nxp_binding_reference/P027_nuvoton_npcx-adc-v2t.md#std-dtcompatible-nuvoton-npcx-adc-v2t"><code>nuvoton,npcx-adc-v2t</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX UART节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck3.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P007_nuvoton_npcx-uart.md#std-dtcompatible-nuvoton-npcx-uart"><code>nuvoton,npcx-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck3m8k.dtsi?plain=1#L19">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>系统控制器寄存器读写（System Controller Registers R/W）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L104">已启用：2</a>）</td>
<td><a href="../edac_syscon_binding_reference/P008_syscon.md#std-dtcompatible-syscon"><code>syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">转速计（Tachometer）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX转速计（Tachometer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L521">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L528">已禁用：4</a>）</td>
<td><a href="../auxdisplay_iio_tach_binding_reference/P018_nuvoton_npcx-tach.md#std-dtcompatible-nuvoton-npcx-tach"><code>nuvoton,npcx-tach</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐NPCX内部定时器（ITIM / Internal Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck3.dtsi?plain=1#L45">已启用：1</a>）</td>
<td><a href="../mcu_timer_binding_reference/P012_nuvoton_npcx-itim-timer.md#std-dtcompatible-nuvoton-npcx-itim-timer"><code>nuvoton,npcx-itim-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>新唐NPCX TWD（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L400">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P003_nuvoton_npcx-watchdog.md#std-dtcompatible-nuvoton-npcx-watchdog"><code>nuvoton,npcx-watchdog</code></a></td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

NPCK3M8K MCU使用90 MHz内部振荡器及片上PLL，最终生成15 MHz嵌入式控制器（EC）时钟。详见用户手册第4章的处理器时钟控制寄存器。

<a id="serial-port"></a>

### 串口（Serial Port）

UART1用于串行日志。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`npck3m8k_evb`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

此板提供Cortex ETM端口，可通过单一物理连接进行跟踪及调试；另有仅供JTAG会话使用的插座。

<a id="flashing"></a>

### 烧录（Flashing）

按通常方式为npck3m8k_evb构建应用。

<a id="debugging"></a>

### 调试（Debugging）

使用J-Link通过JTAG／SWD连接。

<a id="references"></a>

## 参考资料（References）

## 译注

原文90 MHz振荡器和15 MHz EC时钟分别保留。

---

[上一章](P008_Nuvoton_Technology_Corporation.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_NPCM400_EVB.md)
