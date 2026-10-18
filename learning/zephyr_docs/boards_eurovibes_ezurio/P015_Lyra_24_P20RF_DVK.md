---
id: learning.zephyr-docs.boards-eurovibes-ezurio.page-15
title: Lyra 24 P20RF DVK
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ezurio/lyra_24_dvk/doc/lyra_24_dvk_p20rf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="lyra_24_dvk_p20rf"></a>

# 第15章\_Lyra 24 P20RF开发套件（DVK）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ezurio/lyra_24_dvk/doc/lyra_24_dvk_p20rf.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/lyra_24_dvk_p20rf.webp](images/lyra_24_dvk_p20rf.webp)](images/lyra_24_dvk_p20rf.webp)

Lyra 24 P20RF开发套件（DVK）

名称（Name）：

`lyra_24_dvk_p20rf`

厂商（Vendor）：

[Ezurio](https://docs.zephyrproject.org/latest/boards/index.html#vendor=ezurio)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[bgm240pb32vnn](https://docs.zephyrproject.org/latest/boards/index.html#soc=bgm240pb32vnn)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ezurio/lyra_24_dvk/doc/lyra_24_dvk_p20rf.rst/../..)<a id="overview"></a>

## 概述（Overview）

Lyra 24 P20RF开发套件支持Ezurio Lyra 24 P20RF低功耗蓝牙（Bluetooth Low Energy）v5.4模块。

该模块基于Silicon Laboratories BGM240PB32VNN模块，包含EFR32BG24 Arm Cortex-M33 CPU。

Lyra 24 P20RF模块使用QFN封装的EFR32BG24，具有1024 kB Flash和256 kB RAM，最多26个可配置GPIO，低功耗蓝牙无线电发射功率最高20 dBm。

套件具备USB接口、板载SEGGER J-Link调试器、一个用户LED及一个按键，并通过[mikroBUS](https://www.mikroe.com/mikrobus)插座和[Qwiic](https://www.sparkfun.com/qwiic)连接器支持硬件扩展板（Add-On Boards）。

注意（Note）

Lyra 24系列模块的更多信息见[Lyra 24产品简介（Product Brief）](https://www.ezurio.com/documentation/product-brief-lyra-24-series)及[Lyra 24网站](https://www.ezurio.com/wireless-modules/bluetooth-modules/bluetooth-5-modules/lyra-24-series-bluetooth-5-modules)。

Lyra 24 P20RF模块更多信息见Lyra 24 P数据手册。（[Lyra 24 P数据手册（Datasheet）](https://www.ezurio.com/documentation/datasheet-lyra-24p)）

底层BGM240PB32VNN模块更多信息见BGM240P数据手册。（[BGM240P数据手册（Datasheet）](https://www.silabs.com/documents/public/data-sheets/bgm240p-datasheet.pdf)）

底层EFR32BG24 SoC更多信息见EFR32BG24数据手册及EFR32BG24参考手册。（[EFR32BG24数据手册（Datasheet）](https://www.silabs.com/documents/public/data-sheets/efr32bg24-datasheet.pdf)；[EFR32BG24参考手册（Reference Manual）](https://www.silabs.com/documents/public/reference-manuals/efr32xg24-rm.pdf)）

<a id="hardware"></a>

## 硬件（Hardware）

Lyra 24 P20RF DVK有两个晶体振荡器，如下所示。


- 39 MHz高频晶体振荡器（HFXO）
- 32.768 kHz低频晶体振荡器（LFXO）

高频晶体振荡器安装在Lyra 24 P20RF模块内部。

低频晶体振荡器安装在DVK上，位于Lyra 24 P20RF模块外部。

模块支持外部低功耗蓝牙天线（External Bluetooth Low Energy Antenna）。

DVK完整信息见Lyra 24 P DVK用户指南及Lyra 24 P20RF DVK原理图。（[Lyra 24 P DVK用户指南（User Guide）](https://www.ezurio.com/documentation/user-guide-lyra-24p-development-kit)；[Lyra 24 P20RF DVK原理图（Schematics）](https://www.ezurio.com/documentation/schematic-pcb-assembly-dvk-lyra-24p-devboard-rf-trace-pad-20dbm-453-00148-k1)）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`lyra_24_dvk_p20rf`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="lyra_24_dvk_p20rf-hw-features"></a>

<a id="lyra_24_dvk_p20rf-lyra_24_dvk_p20rf/bgm240pb32vnn-hw-features-section"></a>

#### `lyra_24_dvk_p20rf/bgm240pb32vnn`目标（Target）

<a id="lyra_24_dvk_p20rf-lyra_24_dvk_p20rf/bgm240pb32vnn-hw-features-panel"></a>

<a id="lyra_24_dvk_p20rf-lyra_24_dvk_p20rf/bgm240pb32vnn-hw-features-memory"></a>

该开发板目标的片上存储容量：256 KiB RAM、1536 KiB Flash。

<a id="lyra_24_dvk_p20rf-lyra_24_dvk_p20rf/bgm240pb32vnn-hw-features-table"></a>

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
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L169">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2增量式模数转换器（IADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L592">已启用：1</a>）</td>
<td><a href="../hardware/P900_SiliconLabsIADC绑定.md#dtbinding-silabs-iadc"><code>silabs,iadc</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2蓝牙主机控制器接口（Bluetooth HCI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/efr32xg24.dtsi?plain=1#L31">已启用：1</a>）</td>
<td><a href="../bluetooth_vendor_hci_binding_reference/P015_silabs_bt-hci-efr32.md#std-dtcompatible-silabs-bt-hci-efr32"><code>silabs,bt-hci-efr32</code></a></td>
</tr>
<tr>
<td rowspan="9">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2时钟管理单元（CMU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L217">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P029_silabs_series-clock.md#std-dtcompatible-silabs-series-clock"><code>silabs,series-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs CMU时钟输出（CLKOUT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L225">已禁用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P028_silabs_series-clock-output.md#std-dtcompatible-silabs-series-clock-output"><code>silabs,series-clock-output</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2高频RC振荡器数字锁相环（HFRCODPLL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L249">已启用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P004_silabs_series2-hfrcodpll.md#std-dtcompatible-silabs-series2-hfrcodpll"><code>silabs,series2-hfrcodpll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L258">已启用：3</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2低频外部晶体振荡器（LFXO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L266">已启用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P007_silabs_series2-lfxo.md#std-dtcompatible-silabs-series2-lfxo"><code>silabs,series2-lfxo</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2低频RC振荡器（LFRCO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L280">已启用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P006_silabs_series2-lfrco.md#std-dtcompatible-silabs-series2-lfrco"><code>silabs,series2-lfrco</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2 EM2／EM3模式高频RC振荡器（HFRCOEM23）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L660">已启用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P005_silabs_series2-hfrcoem23.md#std-dtcompatible-silabs-series2-hfrcoem23"><code>silabs,series2-hfrcoem23</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2高频外部晶体振荡器（HFXO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L670">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P027_silabs_hfxo.md#std-dtcompatible-silabs-hfxo"><code>silabs,hfxo</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L26">已启用：22</a>）</td>
<td><a href="../timer_reference/P110_固定比例时钟绑定.md#dtbinding-fixed-factor-clock"><code>fixed-factor-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2模拟比较器（ACMP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L602">已禁用：2</a>）</td>
<td><a href="../hardware/P757_SiliconLabs模拟比较器绑定.md#dtbinding-silabs-acmp"><code>silabs,acmp</code></a></td>
</tr>
<tr>
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs TIMER计数器（Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L404">已禁用：5</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P005_silabs_timer-counter.md#std-dtcompatible-silabs-timer-counter"><code>silabs,timer-counter</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2备份实时时钟（BURTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L513">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P003_silabs_burtc-counter.md#std-dtcompatible-silabs-burtc-counter"><code>silabs,burtc-counter</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs PROTIMER计数器（Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/efr32xg24.dtsi?plain=1#L36">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P004_silabs_protimer.md#std-dtcompatible-silabs-protimer"><code>silabs,protimer</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>Silabs通用循环冗余校验（CRC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L541">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P010_silabs_gpcrc.md#std-dtcompatible-silabs-gpcrc"><code>silabs,gpcrc</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2安全引擎邮箱（SE Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L724">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P012_silabs_gecko-semailbox.md#std-dtcompatible-silabs-gecko-semailbox"><code>silabs,gecko-semailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2电压数模转换器（VDAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L620">已启用：2</a>）</td>
<td><a href="../hardware/P774_SiliconLabs电压数模转换器绑定.md#dtbinding-silabs-vdac"><code>silabs,vdac</code></a></td>
</tr>
<tr>
<td rowspan="2">调试（Debug）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs数据包跟踪接口（Packet Trace Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/efr32xg24.dtsi?plain=1#L41">已禁用：1</a>）</td>
<td><a href="../debug_binding_reference/P006_Silicon_Labs数据包跟踪绑定.md#std-dtcompatible-silabs-pti"><code>silabs,pti</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARMv8仪器跟踪宏单元（Instrumentation Trace Macrocell）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L181">已启用：1</a>）</td>
<td><a href="../debug_binding_reference/P002_ARMv8M_ITM调试绑定.md#std-dtcompatible-arm-armv8m-itm"><code>arm,armv8m-itm</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2链式直接存储器访问（LDMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L381">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P001_silabs_ldma.md#std-dtcompatible-silabs-ldma"><code>silabs,ldma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2存储器系统控制器（MSC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L298">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P007_silabs_series2-flash-controller.md#std-dtcompatible-silabs-series2-flash-controller"><code>silabs,series2-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="4">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2通用输入输出外设（GPIO Peripheral）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L317">已启用：1</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P015_silabs_gpio.md#std-dtcompatible-silabs-gpio"><code>silabs,gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2 GPIO端口（Port）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L327">已启用：4</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P014_silabs_gpio-port.md#std-dtcompatible-silabs-gpio-port"><code>silabs,gpio-port</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通过Mikro BUS排针引出的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/lyra_24_dvk/lyra_24_dvk.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P006_mikro-bus.md#std-dtcompatible-mikro-bus"><code>mikro-bus</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>STEMMA QT是一种用于I2C设备的4针JST-SH接口。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/lyra_24_dvk/lyra_24_dvk.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P005_stemma-qt-connector.md#std-dtcompatible-stemma-qt-connector"><code>stemma-qt-connector</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2 I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L683">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L522">已禁用：1</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P005_silabs_i2c.md#std-dtcompatible-silabs-i2c"><code>silabs,i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/lyra_24_dvk/lyra_24_dvk.dtsi?plain=1#L47">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/lyra_24_dvk/lyra_24_dvk.dtsi?plain=1#L31">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ezurio/lyra_24_dvk/lyra_24_dvk.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L186">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L308">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">网络（Networking）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2无线电接口（Radio Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/efr32xg24.dtsi?plain=1#L11">已启用：1</a>）</td>
<td><a href="../network_radio_frontend_binding_reference/P014_silabs_series2-radio.md#std-dtcompatible-silabs-series2-radio"><code>silabs,series2-radio</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2 DBUS引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L368">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P024_silabs_dbus-pinctrl.md#std-dtcompatible-silabs-dbus-pinctrl"><code>silabs,dbus-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs TIMER脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L409">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L431">已禁用：4</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P010_silabs_timer-pwm.md#std-dtcompatible-silabs-timer-pwm"><code>silabs,timer-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs低能耗定时器脉宽调制（LETIMER PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L585">已禁用：1</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P008_silabs_letimer-pwm.md#std-dtcompatible-silabs-letimer-pwm"><code>silabs,letimer-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2直流电压转换器（DC-DC Converter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L548">已启用：1</a>）</td>
<td><a href="../hardware/P657_SiliconLabs_Series2直流转换器绑定.md#dtbinding-silabs-series2-dcdc"><code>silabs,series2-dcdc</code></a></td>
</tr>
<tr>
<td rowspan="1">保持存储器（Retained Memory）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2备份RAM（BURAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L534">已禁用：1</a>）</td>
<td><a href="../hardware/P629_SiliconLabs备份RAM绑定.md#dtbinding-silabs-buram"><code>silabs,buram</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2系统实时时钟（SYSRTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L566">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P013_silabs_sysrtc.md#std-dtcompatible-silabs-sysrtc"><code>silabs,sysrtc</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L504">已启用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P010_silabs_usart-uart.md#std-dtcompatible-silabs-usart-uart"><code>silabs,usart-uart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2增强型通用同步／异步收发器（EUSART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L715">已启用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P005_silabs_eusart-uart.md#std-dtcompatible-silabs-eusart-uart"><code>silabs,eusart-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 2增强型通用同步／异步收发器（EUSART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L557">已启用：1</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P005_silabs_eusart-spi.md#std-dtcompatible-silabs-eusart-spi"><code>silabs,eusart-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L733">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="3">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs定时器（TIMER）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L394">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L416">已禁用：4</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P006_silabs_series2-timer.md#std-dtcompatible-silabs-series2-timer"><code>silabs,series2-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs低能耗定时器（LETIMER）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L577">已禁用：1</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P005_silabs_series2-letimer.md#std-dtcompatible-silabs-series2-letimer"><code>silabs,series2-letimer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0–2看门狗（WDOG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L695">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg24/xg24.dtsi?plain=1#L705">已禁用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P011_silabs_gecko-wdog.md#std-dtcompatible-silabs-gecko-wdog"><code>silabs,gecko-wdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

下表的“名称”（Name）列列出引脚名称。例如，PA2表示PORTA的2号引脚，与开发板数据手册及手册中的命名一致。

方向（Direction）列以模块为参考描述引脚方向：I表示输入（Input），O表示输出（Output），I/O表示双向，不适用时为N/A。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
<th>方向（Direction）</th>
</tr>
<tr>
<td>PA0</td>
<td>USART0_TX</td>
<td>UART控制台VCOM_TX</td>
<td>输出（O）</td>
</tr>
<tr>
<td>PA1</td>
<td>SWD_SWCLK</td>
<td>J-Link SWCLK（SWD时钟）</td>
<td>输入（I）</td>
</tr>
<tr>
<td>PA2</td>
<td>SWD_SWDIO</td>
<td>J-Link SWDIO（SWD数据）</td>
<td>I/O</td>
</tr>
<tr>
<td>PA3</td>
<td>SWD_SWO</td>
<td>J-Link SWO（串行线输出）</td>
<td>输出（O）</td>
</tr>
<tr>
<td>PA4</td>
<td>USART0_RTS</td>
<td>UART控制台VCOM_RTS</td>
<td>输出（O）</td>
</tr>
<tr>
<td>PA5</td>
<td>USART0_CTS</td>
<td>UART控制台VCOM_CTS</td>
<td>输入（I）</td>
</tr>
<tr>
<td>PA6</td>
<td>通用输入输出（GPIO）</td>
<td>扩展连接器GPIO（Breakout Connector GPIO）</td>
<td>I/O</td>
</tr>
<tr>
<td>PA7</td>
<td>USART0_RX</td>
<td>UART控制台VCOM_RX</td>
<td>输入（I）</td>
</tr>
<tr>
<td>PA8</td>
<td>通用输入输出（GPIO）</td>
<td>LED 0</td>
<td>输出（O）</td>
</tr>
<tr>
<td>PB0</td>
<td>通用输入输出（GPIO）</td>
<td>mikroBUS模拟输入（AN）</td>
<td>输入（I）</td>
</tr>
<tr>
<td>PB1</td>
<td>EUSART0_TX</td>
<td>mikroBUS发送（TX）</td>
<td>输出（O）</td>
</tr>
<tr>
<td>PB2</td>
<td>EUSART0_RX</td>
<td>mikroBUS接收（RX）</td>
<td>输入（I）</td>
</tr>
<tr>
<td>PB3</td>
<td>通用输入输出（GPIO）</td>
<td>mikroBUS中断（INT）</td>
<td>输入（I）</td>
</tr>
<tr>
<td>PB4</td>
<td>通用输入输出（GPIO）</td>
<td>mikroBUS脉宽调制（PWM）</td>
<td>输出（O）</td>
</tr>
<tr>
<td>PC0</td>
<td>PTI_FRAME</td>
<td>数据包跟踪接口帧信号（Packet Trace Interface FRAME）</td>
<td>输出（O）</td>
</tr>
<tr>
<td>PC1</td>
<td>PTI_DATA</td>
<td>数据包跟踪接口数据信号（Packet Trace Interface DATA）</td>
<td>输出（O）</td>
</tr>
<tr>
<td>PC2</td>
<td>EUSART1_SCK</td>
<td>mikroBUS串行时钟（SCK）</td>
<td>输出（O）</td>
</tr>
<tr>
<td>PC3</td>
<td>通用输入输出（GPIO）</td>
<td>mikroBUS片选（CS）</td>
<td>输出（O）</td>
</tr>
<tr>
<td>PC4</td>
<td>EUSART1_TX</td>
<td>mikroBUS主机输出从机输入（MOSI）</td>
<td>输出（O）</td>
</tr>
<tr>
<td>PC5</td>
<td>EUSART1_RX</td>
<td>mikroBUS主机输入从机输出（MISO）</td>
<td>输入（I）</td>
</tr>
<tr>
<td>PC6</td>
<td>通用输入输出（GPIO）</td>
<td>mikroBUS复位（RST）</td>
<td>输出（O）</td>
</tr>
<tr>
<td>PC7</td>
<td>通用输入输出（GPIO）</td>
<td>按键0（Button 0）</td>
<td>输入（I）</td>
</tr>
<tr>
<td>PD0</td>
<td>低频晶体振荡器（LFXO）</td>
<td>低频晶体振荡器（LFXO）</td>
<td>N/A</td>
</tr>
<tr>
<td>PD1</td>
<td>低频晶体振荡器（LFXO）</td>
<td>低频晶体振荡器（LFXO）</td>
<td>N/A</td>
</tr>
<tr>
<td>PD2</td>
<td>I2C0_SCL</td>
<td>mikroBUS SCL／Qwiic SCL（I2C时钟）</td>
<td>I/O</td>
</tr>
<tr>
<td>PD3</td>
<td>I2C0_SDA</td>
<td>mikroBUS SDA／Qwiic SDA（I2C数据）</td>
<td>I/O</td>
</tr>
</table>

注意（Note）

Qwiic SCL与MikroBUS SCL复用同一I/O。短接焊桥SB5和SB6后，可同时使用MikroBUS I2C扩展板和Qwiic扩展板。

Qwiic SDA与MikroBUS SDA复用同一I/O。短接焊桥SB9和SB10后，可同时使用MikroBUS I2C扩展板和Qwiic扩展板。

更多细节见Lyra 24 P DVK用户指南及Lyra 24 P20RF DVK原理图。（[Lyra 24 P DVK用户指南（User Guide）](https://www.ezurio.com/documentation/user-guide-lyra-24p-development-kit)；[Lyra 24 P20RF DVK原理图（Schematics）](https://www.ezurio.com/documentation/schematic-pcb-assembly-dvk-lyra-24p-devboard-rf-trace-pad-20dbm-453-00148-k1)）

<a id="system-clock"></a>

### 系统时钟（System Clock）

Lyra 24 P20RF配置为使用板上的39 MHz外部振荡器，时钟频率最高可达78 MHz。

<a id="serial-port"></a>

### 串口（Serial Port）

Lyra 24 P20RF有两个增强型通用同步异步收发器（EUSART）和一个通用同步异步收发器（USART）。


- EUSART0默认用作mikroBUS UART。
- EUSART1默认用作mikroBUS SPI端口。
- USART0连接到开发板控制器，用于控制台。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`lyra_24_dvk_p20rf`开发板应用可按常规方式构建、烧录及调试，详见构建应用及运行应用。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）

注意（Note）

使用套件前，应在[Simplicity Studio](https://www.silabs.com/software-and-tools/simplicity-studio)中更新J-Link固件。

<a id="testing-the-led-and-button"></a>

### 测试LED和按键

[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)闪灯示例可测试DVK的LED。

[Button](../basic_samples/P003_按钮输入.md#button)按键示例可测试DVK的按键。

<a id="bluetooth-low-energy"></a>

### 低功耗蓝牙（Bluetooth Low Energy）

要使用低功耗蓝牙功能，运行以下命令，从Silicon Labs硬件抽象层（HAL）仓库取得必需的二进制固件（Binary Blobs）。

```text
west blobs fetch hal_silabs
```

随后用以下命令构建Zephyr内核和蓝牙示例。本例使用[Observer](../bluetooth_samples/P003_蓝牙观察者.md#bluetooth_observer)观察者示例应用。

```text
# From the root of the zephyr repository
west build -b lyra_24_dvk_p20rf samples/bluetooth/observer
```

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [mikrobus](https://www.mikroe.com/mikrobus)：HTTP Error 403: Forbidden。
- [bgm240p-datasheet.pdf](https://www.silabs.com/documents/public/data-sheets/bgm240p-datasheet.pdf)：HTTP Error 403: Forbidden。
- [efr32bg24-datasheet.pdf](https://www.silabs.com/documents/public/data-sheets/efr32bg24-datasheet.pdf)：HTTP Error 403: Forbidden。
- [efr32xg24-rm.pdf](https://www.silabs.com/documents/public/reference-manuals/efr32xg24-rm.pdf)：HTTP Error 403: Forbidden。
- [simplicity-studio](https://www.silabs.com/software-and-tools/simplicity-studio)：HTTP Error 403: Forbidden。

---

[上一章](P014_Lyra_24_P20_DVK.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P016_Lyra_24_S10_DVK.md)
