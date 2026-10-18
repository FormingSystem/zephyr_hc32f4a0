---
id: learning.zephyr-docs.boards-retronix-sifli.page-11
title: FireCuda Gaming SSD FaZe board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/seagate/faze/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="faze"></a>

# 第11章\_FireCuda Gaming SSD的FaZe开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/seagate/faze/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/firecuda-gaming-ssd.jpg](images/firecuda-gaming-ssd.jpg)](images/firecuda-gaming-ssd.jpg)

FireCuda Gaming SSD的FaZe开发板

名称（Name）：

`faze`

厂商（Vendor）：

[Seagate Technology PLC](https://docs.zephyrproject.org/latest/boards/index.html#vendor=seagate)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[lpc11u67](https://docs.zephyrproject.org/latest/boards/index.html#soc=lpc11u67)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/seagate/faze/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

FaZe板位于Seagate FireCuda Gaming SSD设备内，集成NVMe SSD、ASMedia ASM2364 USB转PCIe桥接控制器及NXP LPC11U67微控制器。前者处理USB Type-C与SSD之间的I/O，后者专门控制LED效果，两芯片通过I2C及GPIO相连。

此Zephyr移植运行在NXP LPC11U67微控制器上。

<a id="hardware"></a>

## 硬件（Hardware）


- NXP LPC11U67微控制器，LQFP48封装：


  - Arm Cortex-M0+处理器
  - 20 KB SRAM：16 KB SRAM0、2 KB SRAM1及2 KB USB SRAM
  - 128 KB片上闪存
  - 4 KB片上EEPROM
- 连接到NXP LPC11U67微控制器的外部器件：


  - ASMedia ASM2364 USB转PCIe桥，作为端口0上的I2C主机；原文端口字符写作O
  - 六个RGB LED，连接TI LP5030 LED控制器，后者为I2C端口1上的设备
  - 一个白色LED，闪烁指示SSD活动

更多信息见以下资料：


- [LPC11UXX SoC网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-and-cortex-m0-cores:LPC11U00)
- [LPC11U6X 数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/LPC11U6X.pdf)
- [LPC11U6X 参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=UM10732)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`faze`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="faze-hw-features"></a>

<a id="faze-faze/lpc11u67-hw-features-section"></a>

#### `faze/lpc11u67`目标（Target）

<a id="faze-faze/lpc11u67-hw-features-panel"></a>

<a id="faze-faze/lpc11u67-hw-features-memory"></a>

该开发板目标的片上存储容量：16 KiB RAM、128 KiB Flash。

<a id="faze-faze/lpc11u67-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC11U6X时钟控制器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L136">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P008_nxp_lpc11u6x-syscon.md#std-dtcompatible-nxp-lpc11u6x-syscon"><code>nxp,lpc11u6x-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC11U6X通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L86">已启用：3</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P007_nxp_lpc11u6x-gpio.md#std-dtcompatible-nxp-lpc11u6x-gpio"><code>nxp,lpc11u6x-gpio</code></a></td>
</tr>
<tr>
<td rowspan="2">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>LPC11U6X I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L182">已启用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P004_nxp_lpc11u6x-i2c.md#std-dtcompatible-nxp-lpc11u6x-i2c"><code>nxp,lpc11u6x-i2c</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ASMedia ASM2364 USB转PCIe桥接控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seagate/faze/faze.dts?plain=1#L68">已启用：1</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P007_asmedia_asm2364.md#std-dtcompatible-asmedia-asm2364"><code>asmedia,asm2364</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seagate/faze/faze.dts?plain=1#L34">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>德州仪器LP5030 I2C LED控制器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seagate/faze/faze.dts?plain=1#L82">已启用：1</a>）</td>
<td><a href="../led_sct_ti_xpowers_binding_reference/P007_ti_lp5030.md#std-dtcompatible-ti-lp5030"><code>ti,lp5030</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seagate/faze/faze.dts?plain=1#L45">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP LPC11U6X片上EEPROM节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L45">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P001_nxp_lpc11u6x-eeprom.md#std-dtcompatible-nxp-lpc11u6x-eeprom"><code>nxp,lpc11u6x-eeprom</code></a></td>
</tr>
<tr>
<td rowspan="3">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>LPC I/O引脚配置（IOCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L55">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P007_nxp_lpc-iocon.md#std-dtcompatible-nxp-lpc-iocon"><code>nxp,lpc-iocon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>LPC引脚控制（Pinctrl）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L62">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P008_nxp_lpc11u6x-pinctrl.md#std-dtcompatible-nxp-lpc11u6x-pinctrl"><code>nxp,lpc11u6x-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>LPC输入输出引脚配置（IOCON）的端口输入输出（PIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L67">已启用：3</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P006_nxp_lpc-iocon-pio.md#std-dtcompatible-nxp-lpc-iocon-pio"><code>nxp,lpc-iocon-pio</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC11U6X通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L142">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L150">已禁用：4</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P015_nxp_lpc11u6x-uart.md#std-dtcompatible-nxp-lpc11u6x-uart"><code>nxp,lpc11u6x-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

可通过IOCON控制器配置LPC11U67引脚。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PIO0_2</td>
<td>通用输入输出（GPIO）</td>
<td>ASM2364中断（Interrupt）</td>
</tr>
<tr>
<td>PIO0_4</td>
<td>I2C0</td>
<td>I2C0串行时钟（SCL）</td>
</tr>
<tr>
<td>PIO0_5</td>
<td>I2C0</td>
<td>I2C0串行数据（SDA）</td>
</tr>
<tr>
<td>PIO0_7</td>
<td>I2C1</td>
<td>I2C1时钟（SCL）</td>
</tr>
<tr>
<td>PIO0_18</td>
<td>通用异步收发器（UART）</td>
<td>USART0接收（RX）</td>
</tr>
<tr>
<td>PIO0_19</td>
<td>通用异步收发器（UART）</td>
<td>USART0发送（TX）</td>
</tr>
<tr>
<td>PIO0_20</td>
<td>通用输入输出（GPIO）</td>
<td>USB睡眠（Sleep）</td>
</tr>
<tr>
<td>PIO1_23</td>
<td>通用输入输出（GPIO）</td>
<td>SSD活动白色LED</td>
</tr>
<tr>
<td>PIO1_24</td>
<td>I2C1</td>
<td>I2C1数据（SDA）</td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`faze`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>调试服务器（debugserver）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

<a id="flashing"></a>

### 烧录（Flashing）

通过板上4引脚J2排针将外部调试探针连接到SWD端口，即可烧录NXP LPC11U67。默认OpenOCD配置[boards/seagate/faze/support/openocd.cfg](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seagate/faze/support/openocd.cfg)选择ST-LINK接口，可能需要按所用探针更换接口。

调试探针连接FaZe板及主机后，运行west flash即可将已构建固件镜像写入闪存。

<a id="debugging"></a>

### 调试（Debugging）

请参考[烧录（Flashing）](#flashing)一节，并将`west flash`替换为`west debug`执行调试。

<a id="references"></a>

## 参考资料（References）


- [LPC11UXX SoC网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-and-cortex-m0-cores:LPC11U00)
- [LPC11U6X 数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/LPC11U6X.pdf)
- [LPC11U6X 参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=UM10732)

## 译注

FaZe的Zephyr运行于控制灯效的LPC11U67，不是SSD桥接控制器或存储固件。默认ST-LINK接口需按外部探针实际类型调整。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [LPC11U6X.pdf](https://www.nxp.com/docs/en/data-sheet/LPC11U6X.pdf)：HTTP Error 404: Not Found。
- [scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-and-cortex-m0-cores:LPC11U00](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-and-cortex-m0-cores:LPC11U00)：HTTP Error 404: Not Found。
- [Download?colCode=UM10732](https://www.nxp.com/webapp/Download?colCode=UM10732)：HTTP Error 404: Not Found。

---

[上一章](P010_SC-OBC_Module_V1.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P012_Seagate_Technology_PLC.md)
