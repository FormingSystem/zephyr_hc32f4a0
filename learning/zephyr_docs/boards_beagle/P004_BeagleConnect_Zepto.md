---
id: learning.zephyr-docs.boards-beagle.page-4
title: BeagleConnect Zepto
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/beagle/beagleconnect_zepto/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="beagleconnect_zepto"></a>

# 第4章\_BeagleConnect Zepto

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/beagle/beagleconnect_zepto/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/beagleconnect_zepto.webp](images/beagleconnect_zepto.webp)](images/beagleconnect_zepto.webp)

BeagleConnect Zepto

名称（Name）：

`beagleconnect_zepto`

厂商（Vendor）：

[BeagleBoard.org基金会（Foundation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=beagle)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mspm0l1117](https://docs.zephyrproject.org/latest/boards/index.html#soc=mspm0l1117)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/beagle/beagleconnect_zepto/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

BeagleConnect Zepto是BeagleBoard.org推出的低成本微控制器开发板，基于Texas Instruments MSPM0L1117。它面向使用Zephyr RTOS的嵌入式开发，提供紧凑平台，可通过兼容mikroBUS的扩展模块及QWIIC连接器扩展。

[MSPM0L1117](https://www.ti.com/product/MSPM0L1117)采用Arm Cortex-M0+ CPU，最高32 MHz，配有128 KB片上闪存及16 KB SRAM。

<a id="hardware"></a>

## 硬件（Hardware）

BeagleConnect Zepto提供以下硬件特性：


- Texas Instruments [MSPM0L1117](https://www.ti.com/product/MSPM0L1117) Arm Cortex-M0+ MCU
- 128 KB闪存
- 16 KB静态随机存储器（SRAM）
- 兼容mikroBUS的扩展连接器
- 12个非mikroBUS引脚，用于额外功能
- 两个QWIIC扩展连接器
- RGB发光二极管（LED）
- 蓝色用户LED
- 通过外部USB转UART适配器提供UART连接
- 兼容Raspberry Pi或[BeagleY-AI](https://www.beagleboard.org/boards/beagley-ai)附加硬件板（HAT）的连接器

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`beagleconnect_zepto`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="beagleconnect_zepto-hw-features"></a>

<a id="beagleconnect_zepto-beagleconnect_zepto/mspm0l1117-hw-features-section"></a>

#### `beagleconnect_zepto/mspm0l1117`目标（Target）

<a id="beagleconnect_zepto-beagleconnect_zepto/mspm0l1117-hw-features-panel"></a>

<a id="beagleconnect_zepto-beagleconnect_zepto/mspm0l1117-hw-features-memory"></a>

该开发板目标的片上存储容量：16 KiB RAM、128 KiB Flash。

<a id="beagleconnect_zepto-beagleconnect_zepto/mspm0l1117-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>TI MSPM0 12位模数转换器（ADC12）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/l/mspm0l.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../hardware/P908_TIMSPM0ADC12绑定.md#dtbinding-ti-mspm0-adc12"><code>ti,mspm0-adc12</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>TI MSPM0时钟（Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L79">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L85">已禁用：3</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P025_ti_mspm0-clk.md#std-dtcompatible-ti-mspm0-clk"><code>ti,mspm0-clk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>TI MSPM0振荡器（Oscillator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L141">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L127">已禁用：2</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P026_ti_mspm0-osc.md#std-dtcompatible-ti-mspm0-osc"><code>ti,mspm0-osc</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>TI MSPM0 SoC计数器节点（Counter Node）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/l/mspm0l111x.dtsi?plain=1#L34">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/l/mspm0l111x.dtsi?plain=1#L50">已禁用：2</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P011_ti_mspm0-timer-counter.md#std-dtcompatible-ti-mspm0-timer-counter"><code>ti,mspm0-timer-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>TI MSPM0直接存储器访问（DMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L242">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P014_ti_mspm0-dma.md#std-dtcompatible-ti-mspm0-dma"><code>ti,mspm0-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>TI MSPM0内部闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L159">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P032_ti_mspm0-flash-controller.md#std-dtcompatible-ti-mspm0-flash-controller"><code>ti,mspm0-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>TI MSPM0通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L208">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L217">已禁用：2</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P016_ti_mspm0-gpio.md#std-dtcompatible-ti-mspm0-gpio"><code>ti,mspm0-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beagleconnect_zepto/beagleconnect_zepto.dts?plain=1#L40">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/beagleconnect_zepto/beagleconnect_zepto.dts?plain=1#L49">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L166">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>TI MSPM0引脚控制节点（Pinctrl）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L203">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P014_ti_mspm0-pinctrl.md#std-dtcompatible-ti-mspm0-pinctrl"><code>ti,mspm0-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>Texas Instruments MSPM0参考电压（VREF）稳压器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L191">已禁用：1</a>）</td>
<td><a href="../hardware/P658_MSPM0参考电压绑定.md#dtbinding-ti-mspm0-vref"><code>ti,mspm0-vref</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Texas Instruments MSPM0系列真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/l/mspm0l111x.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P019_ti_mspm0-trng.md#std-dtcompatible-ti-mspm0-trng"><code>ti,mspm0-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Texas Instruments MSPM0实时时钟（RTC）驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L183">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P017_ti_mspm0-rtc.md#std-dtcompatible-ti-mspm0-rtc"><code>ti,mspm0-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>TI MSPM0通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L226">已启用：1</a>）</td>
<td><a href="../uart_ti_wch_virtual_binding_reference/P002_ti_mspm0-uart.md#std-dtcompatible-ti-mspm0-uart"><code>ti,mspm0-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Texas Instruments MSPM0串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L236">已禁用：1</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P017_ti_mspm0-spi.md#std-dtcompatible-ti-mspm0-spi"><code>ti,mspm0-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L155">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>TI MSPM0定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/l/mspm0l111x.dtsi?plain=1#L25">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/l/mspm0l111x.dtsi?plain=1#L41">已禁用：2</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P015_ti_mspm0-timer.md#std-dtcompatible-ti-mspm0-timer"><code>ti,mspm0-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>MSPM0窗口看门狗定时器（Windowed Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/mspm0/mspm0.dtsi?plain=1#L175">已启用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P007_ti_mspm0-watchdog.md#std-dtcompatible-ti-mspm0-watchdog"><code>ti,mspm0-watchdog</code></a></td>
</tr>
</table>

<a id="flashing"></a>

## 烧录（Flashing）

构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例：

```text
# From the root of the zephyr repository
west build -b beagleconnect_zepto/mspm0l1117 samples/hello_world
```

构建生成的二进制文件名为`zephyr.bin`，位于`build/zephyr`目录。

若BeagleConnect Zepto通过I2C或UART连接，可使用[BeagleBoard Imaging Utility](https://beagleboard.github.io/bb-imager-rs/)烧录二进制文件。兼容Raspberry Pi和[BeagleY-AI](https://www.beagleboard.org/boards/beagley-ai) HAT的连接器允许直接从这些板卡烧录，无需额外接线。

也可以将XDS110调试探针连接到SWD接口，直接用以下命令烧录应用：

```text
west build -b beagleconnect_zepto/mspm0l1117
west flash
```

<a id="debugging"></a>

## 调试（Debugging）

开发板支持通过SWD使用XDS110调试。

```text
west build -b beagleconnect_zepto/mspm0l1117
west debug
```

<a id="references"></a>

## 参考资料（References）

---

[上一章](P003_BeagleConnect_Freedom.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_BeaglePlay.md)
