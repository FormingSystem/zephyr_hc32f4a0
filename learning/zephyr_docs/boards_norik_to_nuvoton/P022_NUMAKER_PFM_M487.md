---
id: learning.zephyr-docs.boards-norik-to-nuvoton.page-22
title: NUMAKER PFM M487
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nuvoton/numaker_pfm_m487/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="numaker_pfm_m487"></a>

# 第22章\_NUMAKER PFM M487

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nuvoton/numaker_pfm_m487/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/pfm_m487.jpg](images/pfm_m487.jpg)](images/pfm_m487.jpg)

NUMAKER PFM M487

名称（Name）：

`numaker_pfm_m487`

厂商（Vendor）：

[新唐科技（Nuvoton Technology Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nuvoton)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[m487](https://docs.zephyrproject.org/latest/boards/index.html#soc=m487)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nuvoton/numaker_pfm_m487/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

NuMaker PFM M487是新唐专为物联网应用开发的平台，基于采用Arm Cortex-M4F内核的NuMicro® M487以太网系列MCU。

<a id="features"></a>

### 功能（Features）：


- 32位Arm Cortex®-M4 M487JIDAE MCU
- 内核时钟最高192 MHz
- 512 KB嵌入式双存储体闪存（Dual Bank Flash）及160 KB SRAM
- NAU88L25音频编解码器（Audio Codec），带麦克风输入及耳机输出
- 用于网络应用的IP101GR以太网接口
- USB 2.0高速（High-Speed）OTG／主机／设备
- USB 1.1全速（Full-Speed）OTG／主机／设备
- 外部SPI闪存Winbond W25Q20，可作为ROM模块
- 用于T-Flash的microSD卡插槽
- M487扩展接口，4个连接器各36引脚
- 兼容Arduino UNO的接口
- 三个按键，一个用于复位，另外两个可由用户自定义
- 四个LED，一个用于电源指示，另外三个可由用户自定义
- 板载NU-Link-Me ICE调试器／编程器，带SWD连接器

<a id="id3"></a>

更多开发板信息见PFM M487用户手册 [注1](#id2)。（[PFM M487用户手册（User Manual）](https://www.nuvoton.com/export/resource-files/UM_NuMaker-PFM-M487_User_Manual_EN_Rev1.01.pdf)）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`numaker_pfm_m487`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="numaker_pfm_m487-hw-features"></a>

<a id="numaker_pfm_m487-numaker_pfm_m487/m487-hw-features-section"></a>

#### `numaker_pfm_m487/m487`目标（Target）

<a id="numaker_pfm_m487-numaker_pfm_m487/m487-hw-features-panel"></a>

<a id="numaker_pfm_m487-numaker_pfm_m487/m487-hw-features-memory"></a>

该开发板目标的片上存储容量：160 KiB RAM、512 KiB Flash。

<a id="numaker_pfm_m487-numaker_pfm_m487/m487-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="7">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>新唐NuMicro系统时钟控制器（SCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L107">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P013_nuvoton_numicro-m4-scc.md#std-dtcompatible-nuvoton-numicro-m4-scc"><code>nuvoton,numicro-m4-scc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐NuMicro M4外设时钟控制器（PCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L113">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P012_nuvoton_numicro-m4-pcc.md#std-dtcompatible-nuvoton-numicro-m4-pcc"><code>nuvoton,numicro-m4-pcc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L37">已启用：3</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐M4高速外部晶体（HXT）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L54">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P005_nuvoton_m4-hxt-clock.md#std-dtcompatible-nuvoton-m4-hxt-clock"><code>nuvoton,m4-hxt-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐M4低速外部晶体（LXT）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L60">已禁用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P006_nuvoton_m4-lxt-clock.md#std-dtcompatible-nuvoton-m4-lxt-clock"><code>nuvoton,m4-lxt-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐M4锁相环（PLL）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L74">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P007_nuvoton_m4-pll-clock.md#std-dtcompatible-nuvoton-m4-pll-clock"><code>nuvoton,m4-pll-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>新唐M4 HCLK时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L81">已启用：1</a>）</td>
<td><a href="../clock_nordic_nuvoton_nxp_binding_reference/P004_nuvoton_m4-hclk-clock.md#std-dtcompatible-nuvoton-m4-hclk-clock"><code>nuvoton,m4-hclk-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>新唐NuMicro GPIO（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L129">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L119">已禁用：4</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P025_nuvoton_numicro-gpio.md#std-dtcompatible-nuvoton-numicro-gpio"><code>nuvoton,numicro-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/numaker_pfm_m487/numaker_pfm_m487.dts?plain=1#L55">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/numaker_pfm_m487/numaker_pfm_m487.dts?plain=1#L36">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>新唐NuMicro引脚控制（Pinctrl）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L92">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P018_nuvoton_numicro-pinctrl.md#std-dtcompatible-nuvoton-numicro-pinctrl"><code>nuvoton,numicro-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>新唐NuMaker复位（RESET）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L100">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P008_nuvoton_numaker-rst.md#std-dtcompatible-nuvoton-numaker-rst"><code>nuvoton,numaker-rst</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>新唐NuMicro系列UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L199">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L209">已禁用：7</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P009_nuvoton_numicro-uart.md#std-dtcompatible-nuvoton-numicro-uart"><code>nuvoton,numicro-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L27">已启用：1</a>）</td>
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
<td>新唐NuMaker看门狗定时器（Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L279">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P004_nuvoton_numaker-wdt.md#std-dtcompatible-nuvoton-numaker-wdt"><code>nuvoton,numaker-wdt</code></a></td>
</tr>
</table>

板载12 MHz晶体支持器件运行于最高192 MHz。

<a id="id5"></a>

受支持外设详情见[M480技术参考手册（TRM）](https://www.nuvoton.com/export/resource-files/TRM_M480_Series_EN_Rev2.02.pdf)[注2](#id4)。

<a id="building-and-flashing"></a>

## 构建与烧录（Building and Flashing）

<a id="flashing"></a>

### 烧录（Flashing）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

板载Nu-Link-Me调试器可通过USB将UART0模拟为虚拟COM端口。启用时，将ISW1拨码开关第1—3位TXD、RXD、VOM设为ON。通过USB将PFM M487 IoT连接主机，再运行串口终端程序，例如：

```text
$ minicom -D /dev/ttyACM0
```

```text
# From the root of the zephyr repository
west build -b numaker_pfm_m487 samples/hello_world
west flash
```

<a id="debugging"></a>

### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b numaker_pfm_m487 samples/hello_world
west debug
```

在调试器中单步执行应用。

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.nuvoton.com/export/resource-files/UM_NuMaker-PFM-M487_User_Manual_EN_Rev1.01.pdf](https://www.nuvoton.com/export/resource-files/UM_NuMaker-PFM-M487_User_Manual_EN_Rev1.01.pdf)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.nuvoton.com/export/resource-files/TRM_M480_Series_EN_Rev2.02.pdf](https://www.nuvoton.com/export/resource-files/TRM_M480_Series_EN_Rev2.02.pdf)

## 译注

板载调试器为NU-Link-Me，区别于其他页面的Nu-Link2；UART0虚拟串口仍按原文配置ISW1。

---

[上一章](P021_NUMAKER_PFM_M467.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
