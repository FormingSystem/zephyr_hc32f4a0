---
id: learning.zephyr-docs.boards-mikroe-to-mxchip.page-10
title: MuseLab nanoCH57x
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/muselab/nano_ch57x/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nano_ch57x"></a>

# 第10章\_MuseLab nanoCH57x

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/muselab/nano_ch57x/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/nano_ch57x.webp](images/nano_ch57x.webp)](images/nano_ch57x.webp)

MuseLab nanoCH57x

名称（Name）：

`nano_ch57x`

厂商（Vendor）：

[MuseLab Electronics](https://docs.zephyrproject.org/latest/boards/index.html#vendor=muselab)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[ch570](https://docs.zephyrproject.org/latest/boards/index.html#soc=ch570)、[ch572](https://docs.zephyrproject.org/latest/boards/index.html#soc=ch572)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/muselab/nano_ch57x/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id3"></a>

MuseLab [nanoCH57x](https://github.com/wuxx/nanoCH57x) [注1](#id2) 是用于基于RISC-V的CH570／CH572 SoC的评估板。

开发板带电源LED、复位按键、USB端口及一个用户LED，还配有2.4G PCB天线，支持BLE／2.4 GHz射频收发器（RF Transceiver）。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="id5"></a>

nanoCH57x的[青稞（QingKe）V3C 32位RISC-V处理器](https://www.wch-ic.com/downloads/QingKeV3_Processor_Manual_PDF.html) [注2](#id4) 使用32 MHz外部晶体，最高运行频率100 MHz。

<a id="id7"></a>

<a id="id9"></a>

[WCH的CH572网页](https://www.wch-ic.com/products/CH572.html) [注3](#id6) 提供处理器信息及数据手册；nanoCH57x开发板原理图见其Git仓库 [注4](#id8)。（[nanoCH57x Git仓库](https://github.com/wuxx/nanoCH57x/blob/main/hardware/nanoCH57x-v1.0.pdf)）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`nano_ch57x`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="nano_ch57x-hw-features"></a>

<a id="nano_ch57x-nano_ch57x/ch570-hw-features-section"></a>

#### `nano_ch57x/ch570`目标（Target）

<a id="nano_ch57x-nano_ch57x/ch570-hw-features-panel"></a>

<a id="nano_ch57x-nano_ch57x/ch570-hw-features-memory"></a>

该开发板目标的片上存储容量：12 KiB RAM、256 KiB Flash。

<a id="nano_ch57x-nano_ch57x/ch570-hw-features-table"></a>

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
<td>WCH青稞（QingKe）V3C RISC-V MCU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v3c.dtsi?plain=1#L15">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P049_wch_qingke-v3c.md#std-dtcompatible-wch-qingke-v3c"><code>wch,qingke-v3c</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>CH5xx比较器（Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch57/ch570.dtsi?plain=1#L62">已禁用：1</a>）</td>
<td><a href="../hardware/P759_WCHCH5xx比较器绑定.md#dtbinding-wch-ch5xx-comparator"><code>wch,ch5xx-comparator</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>WCH CH5xx通用输入／输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch57/ch570.dtsi?plain=1#L50">已启用：1</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P023_wch_ch5xx-gpio.md#std-dtcompatible-wch-ch5xx-gpio"><code>wch,ch5xx-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>WCH CH32V00x可编程快速中断控制器（PFIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v3c.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P006_wch_pfic.md#std-dtcompatible-wch-pfic"><code>wch,pfic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/muselab/nano_ch57x/nano_ch57x_common.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch57/ch570.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>WCH CH570／CH572复用功能（Alternate Function）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch57/ch570.dtsi?plain=1#L44">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P019_wch_ch570-pinctrl.md#std-dtcompatible-wch-ch570-pinctrl"><code>wch,ch570-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>WCH CH5xx UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch57/ch570.dtsi?plain=1#L36">已启用：1</a>）</td>
<td><a href="../uart_ti_wch_virtual_binding_reference/P005_wch_ch5xx-uart.md#std-dtcompatible-wch-ch5xx-uart"><code>wch,ch5xx-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch57/ch570.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>WCH CH32V00x系统节拍（Systick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v3c.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../system_timer_binding_reference/P014_wch_systick.md#std-dtcompatible-wch-systick"><code>wch,systick</code></a></td>
</tr>
</table>

<a id="nano_ch57x-nano_ch57x/ch572-hw-features-section"></a>

#### `nano_ch57x/ch572`目标（Target）

<a id="nano_ch57x-nano_ch57x/ch572-hw-features-panel"></a>

<a id="nano_ch57x-nano_ch57x/ch572-hw-features-memory"></a>

该开发板目标的片上存储容量：12 KiB RAM、256 KiB Flash。

<a id="nano_ch57x-nano_ch57x/ch572-hw-features-table"></a>

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
<td>WCH青稞（QingKe）V3C RISC-V MCU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v3c.dtsi?plain=1#L15">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P049_wch_qingke-v3c.md#std-dtcompatible-wch-qingke-v3c"><code>wch,qingke-v3c</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>CH5xx比较器（Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch57/ch570.dtsi?plain=1#L62">已禁用：1</a>）</td>
<td><a href="../hardware/P759_WCHCH5xx比较器绑定.md#dtbinding-wch-ch5xx-comparator"><code>wch,ch5xx-comparator</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>WCH CH5xx通用输入／输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch57/ch570.dtsi?plain=1#L50">已启用：1</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P023_wch_ch5xx-gpio.md#std-dtcompatible-wch-ch5xx-gpio"><code>wch,ch5xx-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>WCH CH32V00x可编程快速中断控制器（PFIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v3c.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P006_wch_pfic.md#std-dtcompatible-wch-pfic"><code>wch,pfic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/muselab/nano_ch57x/nano_ch57x_common.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch57/ch570.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>WCH CH570／CH572复用功能（Alternate Function）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch57/ch570.dtsi?plain=1#L44">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P019_wch_ch570-pinctrl.md#std-dtcompatible-wch-ch570-pinctrl"><code>wch,ch570-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>WCH CH5xx UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch57/ch570.dtsi?plain=1#L36">已启用：1</a>）</td>
<td><a href="../uart_ti_wch_virtual_binding_reference/P005_wch_ch5xx-uart.md#std-dtcompatible-wch-ch5xx-uart"><code>wch,ch5xx-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/ch57/ch570.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>WCH CH32V00x系统节拍（Systick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/wch/qingke-v3c.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../system_timer_binding_reference/P014_wch_systick.md#std-dtcompatible-wch-systick"><code>wch,systick</code></a></td>
</tr>
</table>

<a id="pin-mapping"></a>

### 引脚映射（Pin Mapping）

CH570／CH572 SoC外设可连接到开发板上的不同引脚，通过DTS配置映射。下表列出各外设可用的引脚连接。

<table>
<tr>
<th>外设（Peripheral）</th>
<th>可选引脚（Possible Pins）</th>
<th>默认引脚（Default Pin）</th>
</tr>
<tr>
<td>UART0 RXD</td>
<td>PA2、PA3、PA0、PA1、PA6、PA9、PA10、PA11</td>
<td>PA2</td>
</tr>
<tr>
<td>UART0 TXD</td>
<td>PA3、PA2、PA1、PA0、PA7、PA8、PA11、PA10</td>
<td>PA3</td>
</tr>
<tr>
<td>IC20 SCL，名称按原文保留</td>
<td>PA8、PA0、PA3、PA5</td>
<td>PA8</td>
</tr>
<tr>
<td>IC20 SDA，名称按原文保留</td>
<td>PA9、PA1、PA2、PA6</td>
<td>PA9</td>
</tr>
<tr>
<td>SPI0主出从入（MOSI）</td>
<td>PA7</td>
<td>PA7</td>
</tr>
<tr>
<td>SPI0主入从出（MISO）</td>
<td>PA6</td>
<td>PA6</td>
</tr>
<tr>
<td>SPI0串行时钟（SCK）</td>
<td>PA5、PA3</td>
<td>PA5</td>
</tr>
<tr>
<td>SPI0 SCS</td>
<td>PA4、PA2</td>
<td>PA4</td>
</tr>
<tr>
<td>TMR0 — PWM0</td>
<td>PA7、PA2、PA4、PA9</td>
<td>PA7</td>
</tr>
<tr>
<td>TMR0 — CAPIN1</td>
<td>PA7、PA2、PA4、PA9</td>
<td>PA7</td>
</tr>
<tr>
<td>TMR0 — CAPIN2</td>
<td>PA2、PA7、PA9、PA4</td>
<td>PA2</td>
</tr>
<tr>
<td>PWM（1—5）</td>
<td>PA7、PA2、PA3、PA4、PA8</td>
<td>PA7、PA2、PA3、PA4、PA8</td>
</tr>
<tr>
<td>KEYSCAN（0—4）</td>
<td>PA2、PA3、PA8、PA10、PA11</td>
<td>PA2、PA3、PA8、PA10、PA11</td>
</tr>
<tr>
<td>CMP0 — N</td>
<td>PA2</td>
<td>PA2</td>
</tr>
<tr>
<td>CMP0 — P</td>
<td>PA3、PA7</td>
<td>PA3</td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

<a id="id11"></a>

nanoCH57x开发板目标可按通常方式构建及烧录应用，详情见构建应用及运行应用；不过，为方便烧录和调试，建议使用[WCH LinkE](https://www.wch-ic.com/products/WCH-Link.html) [注5](#id10) 等外部编程器。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）

此时外部编程器引脚必须按以下方式连接：

<table>
<tr>
<td>WCH LinkE</td>
<td>3V3</td>
<td>地（GND）</td>
<td>串行线调试数据（SWDIO）</td>
<td>串行线时钟（SWCLK）</td>
<td>发送（TX）</td>
<td>接收（RX）</td>
</tr>
<tr>
<td><code>nanoCH57x</code></td>
<td>3V3</td>
<td>G</td>
<td>PA0</td>
<td>PA1</td>
<td>PA2</td>
<td>PA3</td>
</tr>
</table>

注意（Note）

必须启用开发板调试接口，并关闭代码保护（Code Protection）。

`nano_ch57x`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd"><code>openocd</code></a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

使用OpenOCD运行工具（Runner）时，需要WCH版OpenOCD，例如位于[https://github.com/jnk0le/openocd-wch](https://github.com/jnk0le/openocd-wch)的WCH OpenOCD liberated分支。

注意（Note）

可通过以下方式更改Zephyr默认使用的OpenOCD可执行文件：


1. 每次烧录或调试时，在west flash或west debug命令后添加--openocd path/to/wch-openocd/bin/openocd参数指定路径。
2. 将WCH OpenOCD可执行文件设置为构建配置参数：

  ```text
  west config build.cmake-args -- "-DOPENOCD=path/to/wch-openocd/bin/openocd"
  ```

  与第一种方式不同，这种方式只需设置一次。

<a id="flashing"></a>

### 烧录（Flashing）

以下以[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)应用为例。LED定义位于[boards/muselab/nano_ch57x/nano_ch57x_common.dtsi](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/muselab/nano_ch57x/nano_ch57x_common.dtsi)。

```text
# From the root of the zephyr repository
west build -b nano_ch57x/ch570 samples/basic/blinky
west flash
```

<a id="debugging"></a>

### 调试（Debugging）

此板可通过OpenOCD调试：

```text
# From the root of the zephyr repository
west build -b nano_ch57x/ch570 samples/basic/blinky
west debug
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://github.com/wuxx/nanoCH57x](https://github.com/wuxx/nanoCH57x)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.wch-ic.com/downloads/QingKeV3_Processor_Manual_PDF.html](https://www.wch-ic.com/downloads/QingKeV3_Processor_Manual_PDF.html)

<a id="id6"></a>

〔[3](#id7)〕 [https://www.wch-ic.com/products/CH572.html](https://www.wch-ic.com/products/CH572.html)

<a id="id8"></a>

〔[4](#id9)〕 [https://github.com/wuxx/nanoCH57x/blob/main/hardware/nanoCH57x-v1.0.pdf](https://github.com/wuxx/nanoCH57x/blob/main/hardware/nanoCH57x-v1.0.pdf)

<a id="id10"></a>

〔[5](#id11)〕 [https://www.wch-ic.com/products/WCH-Link.html](https://www.wch-ic.com/products/WCH-Link.html)

## 译注

引脚表中的IC20按原文保留，未擅自改名。外部编程器需要启用调试接口并禁用代码保护；OpenOCD需使用原文指定的WCH版本，可通过每次命令参数或构建配置选择。

---

[上一章](P009_MuseLab_nanoCH32V317.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_AZ3166_MXChip_IoT_DevKit.md)
