---
id: learning.zephyr-docs.boards-silabs.page-62
title: EFM32 Wonder Gecko EFM32WG-STK3800
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/silabs/starter_kits/efm32wg_stk3800/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="efm32wg_stk3800"></a>

# 第62章\_EFM32 Wonder Gecko入门套件，EFM32WG-STK3800

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/silabs/starter_kits/efm32wg_stk3800/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../../_images/efm32wg_stk3800.jpg](images/efm32wg_stk3800.jpg)](images/efm32wg_stk3800.jpg)

EFM32 Wonder Gecko入门套件，EFM32WG-STK3800

名称（Name）：

`efm32wg_stk3800`

厂商（Vendor）：

[芯科科技（Silicon Laboratories）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=silabs)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[efm32wg990f256](https://docs.zephyrproject.org/latest/boards/index.html#soc=efm32wg990f256)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/starter_kits/efm32wg_stk3800/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

EFM32 Wonder Gecko入门套件EFM32WG-STK3800搭载基于Arm Cortex-M4F的EFM32WG系列MCU，具有优良低功耗能力。

<a id="hardware"></a>

## 硬件（Hardware）


- 高级能耗监视（AEM）提供应用或原型设计的实时能耗信息。
- 32 MB并行NAND闪存
- 160段Energy Micro LCD
- 2个用户按键、2个LED及1个触摸滑条
- 环境光传感器及电感电容式金属传感器
- 板载SEGGER J-Link USB调试器

EFM32WG SoC及EFM32WG-STK3800更多信息见：


- [EFM32WG网站](http://www.silabs.com/products/mcu/32-bit/efm32-wonder-gecko)
- [EFM32WG数据手册](http://www.silabs.com/documents/public/data-sheets/EFM32WG990.pdf)
- [EFM32WG参考手册](http://www.silabs.com/documents/public/reference-manuals/EFM32WG-RM.pdf)
- [EFM32WG-STK3800网站](http://www.silabs.com/products/development-tools/mcu/32-bit/efm32-wonder-gecko-starter-kit)
- [EFM32WG-STK3800用户指南](http://www.silabs.com/documents/public/user-guides/efm32wg-stk3800-ug.pdf)
- [EFM32WG-STK3800原理图](http://www.silabs.com/documents/public/schematic-files/BRD2400A_A00.pdf)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`efm32wg_stk3800`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="efm32wg_stk3800-hw-features"></a>

<a id="efm32wg_stk3800-efm32wg_stk3800/efm32wg990f256-hw-features-section"></a>

#### `efm32wg_stk3800/efm32wg990f256`目标（Target）

<a id="efm32wg_stk3800-efm32wg_stk3800/efm32wg990f256-hw-features-panel"></a>

<a id="efm32wg_stk3800-efm32wg_stk3800/efm32wg990f256-hw-features-memory"></a>

该开发板目标的片上存储容量：32 KiB RAM、256 KiB Flash。

<a id="efm32wg_stk3800-efm32wg_stk3800/efm32wg990f256-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="6">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Silabs Gecko时钟管理单元（Clock Management Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L76">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P030_silabs_series0-cmu.md#std-dtcompatible-silabs-series0-cmu"><code>silabs,series0-cmu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0低频晶体振荡器（LFXO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L28">已禁用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P003_silabs_series0-lfxo.md#std-dtcompatible-silabs-series0-lfxo"><code>silabs,series0-lfxo</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0低频RC振荡器（LFRCO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L35">已禁用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P002_silabs_series0-lfrco.md#std-dtcompatible-silabs-series0-lfrco"><code>silabs,series0-lfrco</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0高频晶体振荡器（HFXO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P001_silabs_series0-hfxo.md#std-dtcompatible-silabs-series0-hfxo"><code>silabs,series0-hfxo</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L48">已禁用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L68">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L54">已禁用：2</a>）</td>
<td><a href="../timer_reference/P110_固定比例时钟绑定.md#dtbinding-fixed-factor-clock"><code>fixed-factor-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Gecko闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L85">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P006_silabs_gecko-flash-controller.md#std-dtcompatible-silabs-gecko-flash-controller"><code>silabs,gecko-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0—2 GPIO外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L184">已启用：1</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P013_silabs_gecko-gpio.md#std-dtcompatible-silabs-gecko-gpio"><code>silabs,gecko-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0—2 GPIO端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L194">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L212">已禁用：2</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P012_silabs_gecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port"><code>silabs,gecko-gpio-port</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Silicon Labs Series 0—2 I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L164">已禁用：2</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P004_silabs_gecko-i2c.md#std-dtcompatible-silabs-gecko-i2c"><code>silabs,gecko-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/efm32wg_stk3800/efm32wg_stk3800.dts?plain=1#L49">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/efm32wg_stk3800/efm32wg_stk3800.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L94">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Silabs Gecko引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L249">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P025_silabs_gecko-pinctrl.md#std-dtcompatible-silabs-gecko-pinctrl"><code>silabs,gecko-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="3">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Gecko通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L103">已禁用：3</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P008_silabs_gecko-usart.md#std-dtcompatible-silabs-gecko-usart"><code>silabs,gecko-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Gecko UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L130">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L139">已禁用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P007_silabs_gecko-uart.md#std-dtcompatible-silabs-gecko-uart"><code>silabs,gecko-uart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Gecko低能耗UART（LEUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L148">已禁用：2</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P006_silabs_gecko-leuart.md#std-dtcompatible-silabs-gecko-leuart"><code>silabs,gecko-leuart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

EFM32WG SoC具有PORTA～PORTF六个GPIO控制器，但EFM32WG-STK3800目前仅启用PORTB、PORTE及PORTF三个。

下表Name列为引脚名称，例如PE2表示PORTE第2脚，与板卡数据手册及用户手册一致。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PE2</td>
<td>通用输入输出（GPIO）</td>
<td>LED0</td>
</tr>
<tr>
<td>PE3</td>
<td>通用输入输出（GPIO）</td>
<td>LED1</td>
</tr>
<tr>
<td>PB9</td>
<td>通用输入输出（GPIO）</td>
<td>按键PB0</td>
</tr>
<tr>
<td>PB10</td>
<td>通用输入输出（GPIO）</td>
<td>按键PB1</td>
</tr>
<tr>
<td>PF7</td>
<td>通用输入输出（GPIO）</td>
<td>板卡控制器使能：EFM_BC_EN</td>
</tr>
<tr>
<td>PE0</td>
<td>UART0_TX</td>
<td>UART控制台：EFM_BC_TX，U0_TX，#1</td>
</tr>
<tr>
<td>PE1</td>
<td>UART0_RX</td>
<td>UART控制台：EFM_BC_RX，U0_RX，#1</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

EFM32WG SoC配置为使用板载48 MHz外部振荡器。

<a id="serial-port"></a>

### 串口（Serial Port）

EFM32WG SoC具有三个USART、两个UART及两个低能耗UART（LEUART）。UART0连接板卡控制器，用作控制台。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`efm32wg_stk3800`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

注意（Note）

原文要求首次使用套件前，在Simplicity Studio更新J-Link固件。

<a id="flashing"></a>

### 烧录（Flashing）

EFM32WG-STK3800内置[J-Link](https://www.segger.com/jlink-debug-probes.html)串口及调试适配器，提供：


- 与主机的USB连接，同时呈现大容量存储（Mass Storage）及USB串口。
- 串行闪存设备（Serial Flash Device），实现USB闪存盘文件存储
- 通过接口USB串口转接的物理UART连接

<a id="flashing-an-application-to-efm32-stk3800"></a>

#### 向EFM32-STK3800烧录应用

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例，构建Zephyr内核及应用：

```text
# From the root of the zephyr repository
west build -b efm32wg_stk3800 samples/hello_world
```

通过USB将EFM32WG-STK3800连接主机，应能看到大容量存储设备STK3800及USB串口。将生成的zephyr.bin复制到STK3800驱动器。

打开串口终端（如minicom或PuTTY），设置如下：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

复位开发板后，应能在相应串口（Serial Port）看到以下消息：

```text
Hello World! efm32wg_stk3800
```

## 译注

Wonder Gecko使用48 MHz时钟和UART0，原文只启用GPIO B、E、F。其32 MByte并行NAND与Giant Gecko 11的32 Mbit Quad-SPI不同。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [EFM32WG990.pdf](http://www.silabs.com/documents/public/data-sheets/EFM32WG990.pdf)：HTTP Error 403: Forbidden。
- [EFM32WG-RM.pdf](http://www.silabs.com/documents/public/reference-manuals/EFM32WG-RM.pdf)：HTTP Error 403: Forbidden。
- [BRD2400A_A00.pdf](http://www.silabs.com/documents/public/schematic-files/BRD2400A_A00.pdf)：HTTP Error 403: Forbidden。
- [efm32wg-stk3800-ug.pdf](http://www.silabs.com/documents/public/user-guides/efm32wg-stk3800-ug.pdf)：HTTP Error 403: Forbidden。
- [efm32-wonder-gecko-starter-kit](http://www.silabs.com/products/development-tools/mcu/32-bit/efm32-wonder-gecko-starter-kit)：HTTP Error 403: Forbidden。
- [efm32-wonder-gecko](http://www.silabs.com/products/mcu/32-bit/efm32-wonder-gecko)：HTTP Error 403: Forbidden。

---

[上一章](P061_EFM32_Tiny_Gecko_EFM32TG-STK3300.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P063_Starter_Kits.md)
