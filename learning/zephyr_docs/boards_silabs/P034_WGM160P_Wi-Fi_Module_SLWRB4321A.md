---
id: learning.zephyr-docs.boards-silabs.page-34
title: WGM160P Wi-Fi Module SLWRB4321A
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/silabs/radio_boards/slwrb4321a/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="slwrb4321a"></a>

# 第34章\_WGM160P Wi-Fi模块，SLWRB4321A

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/silabs/radio_boards/slwrb4321a/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../../_images/wgm160p-starter-kit.jpg](images/wgm160p-starter-kit.jpg)](images/wgm160p-starter-kit.jpg)

WGM160P Wi-Fi模块，SLWRB4321A

名称（Name）：

`slwrb4321a`

厂商（Vendor）：

[芯科科技（Silicon Laboratories）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=silabs)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[efm32gg11b820f2048gm64](https://docs.zephyrproject.org/latest/boards/index.html#soc=efm32gg11b820f2048gm64)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/slwrb4321a/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

WGM160P入门套件SLWSTK6121A随附BRD4321A无线电板。板上WGM160P模块将WF200 Wi-Fi收发器与EFM32GG11微控制器组合。

<a id="hardware"></a>

## 硬件（Hardware）


- 高级能耗监视（AEM）提供应用或原型设计的实时能耗信息。
- 超低功耗128×128像素彩色存储型LCD
- 2个用户按键及2个LED
- Si7021湿度及温度传感器
- 板载SEGGER J-Link USB及以太网调试器
- 10/100BASE-TX以太网PHY及RJ45插座，位于随附扩展板
- MicroSD卡槽（Card Slot）
- USB Micro-AB连接器

WGM160P及SLWSTK6121A更多信息见：


- [WGM160P网站](https://www.silabs.com/wireless/wi-fi/wfm160-series-1-modules)
- [WGM160P数据手册](https://www.silabs.com/documents/public/data-sheets/wgm160p-datasheet.pdf)
- [SLWSTK6121A网站](https://www.silabs.com/development-tools/wireless/wi-fi/wgm160p-wifi-module-starter-kit)
- [SLWSTK6121A用户指南](https://www.silabs.com/documents/public/user-guides/ug351-brd4321a-user-guide.pdf)
- [EFM32GG11数据手册](https://www.silabs.com/documents/public/data-sheets/efm32gg11-datasheet.pdf)
- [EFM32GG11参考手册](https://www.silabs.com/documents/public/reference-manuals/efm32gg11-rm.pdf)
- [WF200数据手册](https://www.silabs.com/documents/public/data-sheets/wf200-datasheet.pdf)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`slwrb4321a`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="slwrb4321a-hw-features"></a>

<a id="slwrb4321a-slwrb4321a/efm32gg11b820f2048gm64-hw-features-section"></a>

#### `slwrb4321a/efm32gg11b820f2048gm64`目标（Target）

<a id="slwrb4321a-slwrb4321a/efm32gg11b820f2048gm64-hw-features-panel"></a>

<a id="slwrb4321a-slwrb4321a/efm32gg11b820f2048gm64-hw-features-memory"></a>

该开发板目标的片上存储容量：256 KiB RAM、2 MiB Flash。

<a id="slwrb4321a-slwrb4321a/efm32gg11b820f2048gm64-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="6">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Silabs Gecko时钟管理单元（Clock Management Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L96">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P030_silabs_series0-cmu.md#std-dtcompatible-silabs-series0-cmu"><code>silabs,series0-cmu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0低频晶体振荡器（LFXO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P003_silabs_series0-lfxo.md#std-dtcompatible-silabs-series0-lfxo"><code>silabs,series0-lfxo</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0低频RC振荡器（LFRCO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L41">已禁用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P002_silabs_series0-lfrco.md#std-dtcompatible-silabs-series0-lfrco"><code>silabs,series0-lfrco</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0高频晶体振荡器（HFXO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L48">已禁用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P001_silabs_series0-hfxo.md#std-dtcompatible-silabs-series0-hfxo"><code>silabs,series0-hfxo</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L54">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L81">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L60">已禁用：3</a>）</td>
<td><a href="../timer_reference/P110_固定比例时钟绑定.md#dtbinding-fixed-factor-clock"><code>fixed-factor-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Gecko以太网（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11b820f2048gl192.dtsi?plain=1#L16">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P001_silabs_gecko-ethernet.md#std-dtcompatible-silabs-gecko-ethernet"><code>silabs,gecko-ethernet</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Gecko闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L106">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P006_silabs_gecko-flash-controller.md#std-dtcompatible-silabs-gecko-flash-controller"><code>silabs,gecko-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0—2 GPIO外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L251">已启用：1</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P013_silabs_gecko-gpio.md#std-dtcompatible-silabs-gecko-gpio"><code>silabs,gecko-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0—2 GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L261">已启用：6</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L315">已禁用：3</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P012_silabs_gecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port"><code>silabs,gecko-gpio-port</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0—2 I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L221">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L241">已禁用：1</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P004_silabs_gecko-i2c.md#std-dtcompatible-silabs-gecko-i2c"><code>silabs,gecko-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4321a/slwrb4321a.dts?plain=1#L49">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4321a/slwrb4321a.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L115">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Silabs Gecko引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L366">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P025_silabs_gecko-pinctrl.md#std-dtcompatible-silabs-gecko-pinctrl"><code>silabs,gecko-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>GECKO真随机数发生器（TRNG / True Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L343">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P013_silabs_gecko-trng.md#std-dtcompatible-silabs-gecko-trng"><code>silabs,gecko-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Gecko实时计数器（Real-Time Counter，RTCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L124">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P009_silabs_gecko-rtcc.md#std-dtcompatible-silabs-gecko-rtcc"><code>silabs,gecko-rtcc</code></a></td>
</tr>
<tr>
<td rowspan="3">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Gecko UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L133">已禁用：2</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P007_silabs_gecko-uart.md#std-dtcompatible-silabs-gecko-uart"><code>silabs,gecko-uart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Gecko通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L151">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L160">已禁用：5</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P008_silabs_gecko-usart.md#std-dtcompatible-silabs-gecko-usart"><code>silabs,gecko-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Gecko低能耗UART（LEUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L205">已禁用：2</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P006_silabs_gecko-leuart.md#std-dtcompatible-silabs-gecko-leuart"><code>silabs,gecko-leuart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L29">已启用：1</a>）</td>
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
<td>Silicon Labs Series 0–2看门狗（WDOG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L350">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/gg11/efm32gg11.dtsi?plain=1#L358">已禁用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P011_silabs_gecko-wdog.md#std-dtcompatible-silabs-gecko-wdog"><code>silabs,gecko-wdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

WGM160P中的EFM32GG11 SoC具有六个GPIO控制器PORTA～PORTF，SLWSTK6121A当前全部启用。

下表Name列为引脚名称，例如PE1表示PORTE第1脚，与板卡数据手册及用户手册一致。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PA4</td>
<td>通用输入输出（GPIO）</td>
<td>LED0</td>
</tr>
<tr>
<td>PA5</td>
<td>通用输入输出（GPIO）</td>
<td>LED1</td>
</tr>
<tr>
<td>PD6</td>
<td>通用输入输出（GPIO）</td>
<td>按键PB0</td>
</tr>
<tr>
<td>PD8</td>
<td>通用输入输出（GPIO）</td>
<td>按键PB1</td>
</tr>
<tr>
<td>PE7</td>
<td>UART_TX</td>
<td>UART发送控制台：VCOM_TX，US0_TX，#1</td>
</tr>
<tr>
<td>PE6</td>
<td>UART_RX</td>
<td>UART接收控制台：VCOM_RX，US0_RX，#1</td>
</tr>
<tr>
<td>PB11</td>
<td>I2C_SDA</td>
<td>SENSOR_I2C_SDA，I2C1_SDA，#1</td>
</tr>
<tr>
<td>PB12</td>
<td>I2C_SCL</td>
<td>SENSOR_I2C_SCL，I2C1_SCL，#1</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

EFM32GG11 SoC配置为使用板载50 MHz外部振荡器。

<a id="serial-port"></a>

### 串口（Serial Port）

EFM32GG11 SoC具有四个USART、两个UART及两个低能耗UART（LEUART）。USART0连接板卡控制器，用作控制台。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`slwrb4321a`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td></td>
<td>✅</td>
</tr>
</table>

注意（Note）

原文要求首次使用套件前，在Simplicity Studio更新J-Link固件。

<a id="flashing"></a>

### 烧录（Flashing）

SLWSTK6121A内置[J-Link](https://www.segger.com/jlink-debug-probes.html)串口及调试适配器，提供：


- 与主机的USB连接
- 通过USB串口接口转发的物理UART连接。

<a id="flashing-an-application-to-slwstk6121a"></a>

#### 向SLWSTK6121A烧录应用

通过USB端口将SLWSTK6121A连接主机。

以下为构建并烧录[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用的示例。

```text
# From the root of the zephyr repository
west build -b slwrb4321a samples/hello_world
west flash
```

打开串口终端（如minicom或PuTTY），设置如下：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

复位开发板后，对应串口终端应显示以下消息：

```text
Hello World! slwrb4321a
```

## 译注

WGM160P页面列出4个USART；不要套用Giant Gecko 11入门套件的6个USART。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [wgm160p-wifi-module-starter-kit](https://www.silabs.com/development-tools/wireless/wi-fi/wgm160p-wifi-module-starter-kit)：HTTP Error 403: Forbidden。
- [efm32gg11-datasheet.pdf](https://www.silabs.com/documents/public/data-sheets/efm32gg11-datasheet.pdf)：HTTP Error 403: Forbidden。
- [wf200-datasheet.pdf](https://www.silabs.com/documents/public/data-sheets/wf200-datasheet.pdf)：HTTP Error 403: Forbidden。
- [wgm160p-datasheet.pdf](https://www.silabs.com/documents/public/data-sheets/wgm160p-datasheet.pdf)：HTTP Error 403: Forbidden。
- [efm32gg11-rm.pdf](https://www.silabs.com/documents/public/reference-manuals/efm32gg11-rm.pdf)：HTTP Error 403: Forbidden。
- [ug351-brd4321a-user-guide.pdf](https://www.silabs.com/documents/public/user-guides/ug351-brd4321a-user-guide.pdf)：HTTP Error 403: Forbidden。
- [wfm160-series-1-modules](https://www.silabs.com/wireless/wi-fi/wfm160-series-1-modules)：HTTP Error 403: Forbidden。

---

[上一章](P033_EFR32FG13_2400_915_MHz_19_dBm_Dual_Band_SLWRB4255A.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P035_EFR32xG21_2.4_GHz_20_dBm_SLWRB4180A.md)
