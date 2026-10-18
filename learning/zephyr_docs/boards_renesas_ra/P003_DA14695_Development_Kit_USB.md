---
id: learning.zephyr-docs.boards-renesas-ra.page-3
title: DA14695 Development Kit USB
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/renesas/da14695_dk_usb/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="da14695_dk_usb"></a>

# 第3章\_DA14695 USB开发套件

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/renesas/da14695_dk_usb/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/da14695-00hqdevkt-u-usb-board.jpg](images/da14695-00hqdevkt-u-usb-board.jpg)](images/da14695-00hqdevkt-u-usb-board.jpg)

DA14695 USB开发套件

名称（Name）：

`da14695_dk_usb`

厂商（Vendor）：

[瑞萨电子（Renesas Electronics Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=renesas)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[da14695](https://docs.zephyrproject.org/latest/boards/index.html#soc=da14695)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/da14695_dk_usb/doc/index.rst/../..)<a id="da14695-development-kit-usb"></a>

## DA14695 USB开发套件

<a id="overview"></a>

### 概述（Overview）

DA14695 Development Kit USB是低成本DA14695开发板，集成调试器及USB集线器，通过一个端口同时连接片上USB及J-Link。

<a id="hardware"></a>

### 硬件（Hardware）

该套件有两个外部振荡器，休眠时钟32768 Hz，系统时钟32 MHz。

<a id="supported-features"></a>

#### 支持的功能（Supported Features）

`da14695_dk_usb`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="da14695_dk_usb-hw-features"></a>

<a id="da14695_dk_usb-da14695_dk_usb/da14695-hw-features-section"></a>

##### `da14695_dk_usb/da14695`目标（Target）

<a id="da14695_dk_usb-da14695_dk_usb/da14695-hw-features-panel"></a>

<a id="da14695_dk_usb-da14695_dk_usb/da14695-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、4 MiB Flash。

<a id="da14695_dk_usb-da14695_dk_usb/da14695-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="2">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond ADC节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L324">已禁用：1</a>）</td>
<td><a href="../hardware/P875_RenesasSmartBond模数转换器绑定.md#dtbinding-renesas-smartbond-adc"><code>renesas,smartbond-adc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond ADC节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L332">已禁用：1</a>）</td>
<td><a href="../hardware/P876_RenesasSmartBondSDADC绑定.md#dtbinding-renesas-smartbond-sdadc"><code>renesas,smartbond-sdadc</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>瑞萨DA1469x蓝牙主机控制器接口（Bluetooth HCI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L434">已启用：1</a>）</td>
<td><a href="../bluetooth_vendor_hci_binding_reference/P013_renesas_bt-hci-da1469x.md#std-dtcompatible-renesas-bt-hci-da1469x"><code>renesas,bt-hci-da1469x</code></a></td>
</tr>
<tr>
<td rowspan="4">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>SmartBond低功耗振荡器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L55">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L71">已禁用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P020_renesas_smartbond-lp-osc.md#std-dtcompatible-renesas-smartbond-lp-osc"><code>renesas,smartbond-lp-osc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L86">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L79">已禁用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SmartBond系统时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L108">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P021_renesas_smartbond-sys-clk.md#std-dtcompatible-renesas-smartbond-sys-clk"><code>renesas,smartbond-sys-clk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>SmartBond低功耗时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L114">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P019_renesas_smartbond-lp-clk.md#std-dtcompatible-renesas-smartbond-lp-clk"><code>renesas,smartbond-lp-clk</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond通用定时器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L262">已禁用：4</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P002_renesas_smartbond-timer.md#std-dtcompatible-renesas-smartbond-timer"><code>renesas,smartbond-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond加密模块（CRYPTO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L341">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P010_renesas_smartbond-crypto.md#std-dtcompatible-renesas-smartbond-crypto"><code>renesas,smartbond-crypto</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond显示控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L375">已禁用：1</a>）</td>
<td><a href="../display_panel_renesas_sharp_binding_reference/P013_renesas_smartbond-display.md#std-dtcompatible-renesas-smartbond-display"><code>renesas,smartbond-display</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond直接存储访问（DMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L417">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P016_renesas_smartbond-dma.md#std-dtcompatible-renesas-smartbond-dma"><code>renesas,smartbond-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond系列闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L193">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P005_renesas_smartbond-flash-controller.md#std-dtcompatible-renesas-smartbond-flash-controller"><code>renesas,smartbond-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond GPIO（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L219">已启用：2</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P030_renesas_smartbond-gpio.md#std-dtcompatible-renesas-smartbond-gpio"><code>renesas,smartbond-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通过Mikro BUS排针引出的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/da14695_dk_usb/da14695_dk_usb.dts?plain=1#L42">已启用：2</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P006_mikro-bus.md#std-dtcompatible-mikro-bus"><code>mikro-bus</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L355">已禁用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P020_renesas_smartbond-i2c.md#std-dtcompatible-renesas-smartbond-i2c"><code>renesas,smartbond-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/da14695_dk_usb/da14695_dk_usb.dts?plain=1#L32">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/da14695_dk_usb/da14695_dk_usb.dts?plain=1#L24">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond NOR／PSRAM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L427">已禁用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P006_renesas_smartbond-nor-psram.md#std-dtcompatible-renesas-smartbond-nor-psram"><code>renesas,smartbond-nor-psram</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L37">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L204">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L213">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P020_renesas_smartbond-pinctrl.md#std-dtcompatible-renesas-smartbond-pinctrl"><code>renesas,smartbond-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond低压差（LDO）及直流转换（DC-DC）稳压器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L120">已启用：1</a>）</td>
<td><a href="../hardware/P655_Renesas_SmartBond稳压器绑定.md#dtbinding-renesas-smartbond-regulator"><code>renesas,smartbond-regulator</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L348">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P010_renesas_smartbond-trng.md#std-dtcompatible-renesas-smartbond-trng"><code>renesas,smartbond-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L248">已禁用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P007_renesas_smartbond-rtc.md#std-dtcompatible-renesas-smartbond-rtc"><code>renesas,smartbond-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L298">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L306">已禁用：2</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P019_renesas_smartbond-uart.md#std-dtcompatible-renesas-smartbond-uart"><code>renesas,smartbond-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond SPI（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L382">已禁用：2</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P001_renesas_smartbond-spi.md#std-dtcompatible-renesas-smartbond-spi"><code>renesas,smartbond-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L175">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>瑞萨SmartBond USB设备控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L402">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P015_renesas_smartbond-usbd.md#std-dtcompatible-renesas-smartbond-usbd"><code>renesas,smartbond-usbd</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>SmartBond看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/smartbond/da1469x.dtsi?plain=1#L256">已启用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P008_renesas_smartbond-watchdog.md#std-dtcompatible-renesas-smartbond-watchdog"><code>renesas,smartbond-watchdog</code></a></td>
</tr>
</table>

DA14695开发套件更多信息：


- <a id="id3"></a>

  [DA14695 DK USB网站](https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14695-00hqdevkt-u-smartbond-da14695-bluetooth-low-energy-52-usb-development-kit)[注1](#id2)

<a id="system-clock"></a>

#### 系统时钟（System Clock）

DA14695 USB开发套件配置使用板上32 MHz外部振荡器。

<a id="connections-and-ios"></a>

#### 连接与输入输出（Connections and IOs）

该套件有一个应用LED和一个按键。UART连接板载串口转换器，经原文所称底板USB1端口提供。

引脚连接如下：


- 红色LED：P1.01
- 标为k1的按键：P0.06
- UART RX：P0.08，连接J-Link串口
- UART TX：P0.09，连接J-Link串口

<a id="system-requirements"></a>

### 系统要求（System Requirements）

<a id="prerequisites"></a>

#### 前置条件（Prerequisites）

瑞萨硬件抽象层（HAL）需要蓝牙控制器二进制固件（Binary Blobs），运行以下命令获取。

```text
west blobs fetch hal_renesas
```

注意（Note）

建议在 `west update` 之后运行上述命令。

<a id="programming-and-debugging"></a>

### 烧录与调试（Programming and Debugging）

`da14695_dk_usb`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>ezflashcli</td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-jlink">jlink</a></td>
<td>✅</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

da14695_dk_usb可按常规方式构建、烧录及调试，详见“构建应用”与“运行应用”。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）

<a id="flashing"></a>

#### 烧录（Flashing）

<a id="id7"></a>

<a id="id8"></a>

DA14695从QSPI外部闪存启动，写入的镜像必须带正确头部。专用[eZFlashCLI](https://github.com/ezflash/ezFlashCLI/)工具[注3](#id6)自动写入头部，并支持DA1469x连接的不同闪存。按eZFlashCLI[注3](#id6)说明安装后，即可常规烧录。（[ezFlashCLI](https://github.com/ezflash/ezFlashCLI/)）

```text
# From the root of the zephyr repository
west build -b da14695_dk_usb samples/basic/blinky
west flash
```

<a id="debugging"></a>

#### 调试（Debugging）

<a id="id5"></a>

DA14695 USB开发套件内置[J-Link](https://www.segger.com/jlink-debug-probes.html)适配器[注2](#id4)，同时提供调试接口及串口。通过USB连接PC后，可常规调试应用。

<a id="references"></a>

### 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14695-00hqdevkt-u-smartbond-da14695-bluetooth-low-energy-52-usb-development-kit](https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14695-00hqdevkt-u-smartbond-da14695-bluetooth-low-energy-52-usb-development-kit)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.segger.com/jlink-debug-probes.html](https://www.segger.com/jlink-debug-probes.html)

<a id="id6"></a>

〔3〕 ([1](#id7),[2](#id8)) [https://github.com/ezflash/ezFlashCLI/](https://github.com/ezflash/ezFlashCLI/)

## 译注

DA14695 USB套件集成USB集线器与调试器；必须下载蓝牙控制器二进制，QSPI启动镜像头由eZFlashCLI写入。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [da14695-00hqdevkt-u-smartbond-da14695-bluetooth-low-energy-52-usb-development-kit](https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14695-00hqdevkt-u-smartbond-da14695-bluetooth-low-energy-52-usb-development-kit)：HTTP Error 429: Too Many Requests。

---

[上一章](P002_CPKCOR_RA8D1B_board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_DA1469x_Development_Kit_Pro.md)
