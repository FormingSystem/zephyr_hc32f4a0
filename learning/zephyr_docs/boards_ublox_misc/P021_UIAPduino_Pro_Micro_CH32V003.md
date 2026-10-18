---
id: learning.zephyr-docs.boards-ublox-misc.page-21
title: UIAPduino Pro Micro CH32V003
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/uiap/uiapduino_pro_micro_ch32v003/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="uiapduino_pro_micro_ch32v003"></a>

# 第21章\_UIAPduino Pro Micro CH32V003

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/uiap/uiapduino_pro_micro_ch32v003/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/uiapduino_pro_micro_ch32v003.webp](images/uiapduino_pro_micro_ch32v003.webp)](images/uiapduino_pro_micro_ch32v003.webp)

UIAPduino Pro Micro CH32V003

名称（Name）：

`uiapduino_pro_micro_ch32v003`

厂商（Vendor）：

[Umeta & Ikki Automotive Parts](https://docs.zephyrproject.org/latest/boards/index.html#vendor=uiap)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[ch32v003](https://docs.zephyrproject.org/latest/boards/index.html#soc=ch32v003)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/uiap/uiapduino_pro_micro_ch32v003/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id3"></a>

<a id="id5"></a>

[UIAPduino Pro Micro CH32V003 V1.4](https://www.uiap.jp/en/uiapduino/pro-micro/ch32v003/v1dot4)[注1](#id2)是基于WCH [CH32V003](https://www.wch-ic.com/products/CH32V003.html)[注2](#id4)的开源硬件开发板。USB Type-C用于供电和编程，也可作为USB 2.0低速设备实现人机接口设备（HID）应用。

此板当前Zephyr支持提供基本GPIO功能及板载用户LED。

<a id="hardware"></a>

## 硬件（Hardware）

板卡采用WCH CH32V003F4U6 SoC，含青稞（QingKe）V2A 32位RISC-V内核，16 KiB闪存、2 KiB SRAM，最高运行频率48 MHz。

主要板载硬件包括：


- USB Type-C连接器，用于供电及编程
- 板载复位按键
- 板载电源及用户LED
- 可选3.3 V或5 V微控制器电源
- USB主机保护保险丝
- 边缘通孔连接点
- 平整底面，便于类似表面贴装的安装方式

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`uiapduino_pro_micro_ch32v003`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="uiapduino_pro_micro_ch32v003-hw-features"></a>

<a id="uiapduino_pro_micro_ch32v003-uiapduino_pro_micro_ch32v003/ch32v003-hw-features-section"></a>

#### `uiapduino_pro_micro_ch32v003/ch32v003`目标（Target）

<a id="uiapduino_pro_micro_ch32v003-uiapduino_pro_micro_ch32v003/ch32v003-hw-features-panel"></a>

<a id="uiapduino_pro_micro_ch32v003-uiapduino_pro_micro_ch32v003/ch32v003-hw-features-memory"></a>

此目标可用存储：2 KiB RAM、16 KiB闪存。

<a id="uiapduino_pro_micro_ch32v003-uiapduino_pro_micro_ch32v003/ch32v003-hw-features-table"></a>

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
<td>WCH青稞V2 RISC-V微控制器（MCU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v2a.dtsi?plain=1#L15">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P048_wch_qingke-v2.md#std-dtcompatible-wch-qingke-v2"><code>wch,qingke-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>WCH CH32V00x模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L223">已禁用：1</a>）</td>
<td><a href="../hardware/P909_沁恒模数转换器绑定.md#dtbinding-wch-adc"><code>wch,adc</code></a></td>
</tr>
<tr>
<td rowspan="5">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>WCH CH32V00x复位及时钟控制（RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L152">已启用：1</a>）</td>
<td><a href="../timer_reference/P185_WCH复位与时钟控制绑定.md#dtbinding-wch-rcc"><code>wch,rcc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>WCH CH32V00x高速外部时钟（HSE）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L19">已禁用：1</a>）</td>
<td><a href="../timer_reference/P186_CH32V00x高速外部时钟绑定.md#dtbinding-wch-ch32v00x-hse-clock"><code>wch,ch32v00x-hse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>WCH CH32V00x高速内部时钟（HSI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L25">已禁用：1</a>）</td>
<td><a href="../timer_reference/P187_CH32V00x高速内部时钟绑定.md#dtbinding-wch-ch32v00x-hsi-clock"><code>wch,ch32v00x-hsi-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L32">已禁用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>WCH CH32V00x锁相环（PLL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../timer_reference/P188_CH32V00x锁相环时钟绑定.md#dtbinding-wch-ch32v00x-pll-clock"><code>wch,ch32v00x-pll-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>用于PWM的WCH高级控制定时器（ADTM / Advanced-control Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L174">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P012_wch_adtm.md#std-dtcompatible-wch-adtm"><code>wch,adtm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>WCH通用定时器（GPTM / General-purpose Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L193">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P013_wch_gptm.md#std-dtcompatible-wch-gptm"><code>wch,gptm</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>WCH DMA控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L164">已启用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P015_wch_wch-dma.md#std-dtcompatible-wch-wch-dma"><code>wch,wch-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>WCH CH32V系列闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L52">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P034_wch_ch32v-flash-controller.md#std-dtcompatible-wch-ch32v-flash-controller"><code>wch,ch32v-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>WCH CH32V00x通用输入／输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L103">已启用：3</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P024_wch_gpio.md#std-dtcompatible-wch-gpio"><code>wch,gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>WCH CH32V电子签名（ESIG / Electronic Signature）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L233">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P015_wch_esig.md#std-dtcompatible-wch-esig"><code>wch,esig</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>WCH I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L132">已禁用：1</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P017_wch_i2c.md#std-dtcompatible-wch-i2c"><code>wch,i2c</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>WCH CH32V00x可编程快速中断控制器（PFIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v2a.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P006_wch_pfic.md#std-dtcompatible-wch-pfic"><code>wch,pfic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>WCH CH32V003／20x／30x外部中断及事件控制器（EXTI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L82">已禁用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P005_wch_exti.md#std-dtcompatible-wch-exti"><code>wch,exti</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/uiap/uiapduino_pro_micro_ch32v003/uiapduino_pro_micro_ch32v003.dts?plain=1#L22">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L60">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>WCH CH32V00x复用功能I/O（AFIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L95">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P018_wch_afio.md#std-dtcompatible-wch-afio"><code>wch,afio</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>用于PWM的WCH高级控制定时器（ADTM / Advanced-control Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L185">已禁用：1</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P018_wch_adtm-pwm.md#std-dtcompatible-wch-adtm-pwm"><code>wch,adtm-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>用于PWM的WCH通用定时器（GPTM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L204">已禁用：1</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P019_wch_gptm-pwm.md#std-dtcompatible-wch-gptm-pwm"><code>wch,gptm-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>CH32复位及时钟控制（RCC）的复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L158">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P019_wch_ch32-rcc-rctl.md#std-dtcompatible-wch-ch32-rcc-rctl"><code>wch,ch32-rcc-rctl</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>WCH SDI控制台（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v2a.dtsi?plain=1#L47">已启用：1</a>）</td>
<td><a href="../uart_ti_wch_virtual_binding_reference/P006_wch_sdi-console.md#std-dtcompatible-wch-sdi-console"><code>wch,sdi-console</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>WCH CH32V00x UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L143">已启用：1</a>）</td>
<td><a href="../uart_ti_wch_virtual_binding_reference/P007_wch_usart.md#std-dtcompatible-wch-usart"><code>wch,usart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>WCH SPI（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L212">已禁用：1</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P019_wch_spi.md#std-dtcompatible-wch-spi"><code>wch,spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L47">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>WCH CH32V00x系统节拍（Systick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v2a.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../system_timer_binding_reference/P014_wch_systick.md#std-dtcompatible-wch-systick"><code>wch,systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>WCH独立看门狗（IWDG / Independent Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch32v0/ch32v003.dtsi?plain=1#L76">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P009_wch_iwdg.md#std-dtcompatible-wch-iwdg"><code>wch,iwdg</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="led"></a>

#### 发光二极管（LED）


- LED0 = PC0，高电平有效

<a id="programming"></a>

## 编程（Programming）

`uiapduino_pro_micro_ch32v003`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
<tr>
<td><code>minichlink</code></td>
<td>✅（默认 / default）</td>
<td></td>
</tr>
</table>

uiapduino_pro_micro_ch32v003目标可按常规方式构建和烧录，详见“构建应用”与“运行应用”。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）

<a id="id7"></a>

开发板出厂带有基于[rv003usb](https://github.com/cnlohr/rv003usb)[注3](#id6)的定制USB引导加载器。按住复位键连接USB，再松开复位键，即进入等待写入模式。

Zephyr板级配置默认使用minichlink运行工具，传入设备标识0x1209b803。

<a id="flashing"></a>

### 烧录（Flashing）

<a id="id9"></a>

从[ch32fun](https://github.com/cnlohr/ch32fun)[注4](#id8)安装minichlink，并确保主机可以访问开发板；Linux可能还需要安装相应udev规则。

以下以[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)应用为例。

```text
# From the root of the zephyr repository
west build -b uiapduino_pro_micro_ch32v003 samples/basic/blinky
west flash
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.uiap.jp/en/uiapduino/pro-micro/ch32v003/v1dot4](https://www.uiap.jp/en/uiapduino/pro-micro/ch32v003/v1dot4)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.wch-ic.com/products/CH32V003.html](https://www.wch-ic.com/products/CH32V003.html)

<a id="id6"></a>

〔[3](#id7)〕 [https://github.com/cnlohr/rv003usb](https://github.com/cnlohr/rv003usb)

<a id="id8"></a>

〔[4](#id9)〕 [https://github.com/cnlohr/ch32fun](https://github.com/cnlohr/ch32fun)

## 译注

UIAPduino出厂使用rv003usb定制引导加载器，minichlink设备标识0x1209b803。硬件具备USB能力不代表当前Zephyr板级支持已实现全部USB功能。

---

[上一章](P020_Umeta_Ikki_Automotive_Parts.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P022_UP_Bridge_the_Gap..md)
