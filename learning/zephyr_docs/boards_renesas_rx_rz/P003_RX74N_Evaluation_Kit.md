---
id: learning.zephyr-docs.boards-renesas-rx-rz.page-3
title: RX74N Evaluation Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/renesas/ek_rx74n/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="ek_rx74n"></a>

# 第3章\_RX74N评估套件

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/renesas/ek_rx74n/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/ek_rx74n.webp](images/ek_rx74n.webp)](images/ek_rx74n.webp)

RX74N评估套件

名称（Name）：

`ek_rx74n`

厂商（Vendor）：

[瑞萨电子（Renesas Electronics Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=renesas)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[rx](https://docs.zephyrproject.org/latest/boards/index.html#arch=rx)

片上系统（SoC）：

[r5k574ncb4ae](https://docs.zephyrproject.org/latest/boards/index.html#soc=r5k574ncb4ae)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/ek_rx74n/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

EK-RX74N是瑞萨RX700系列中的RX74N MCU组评估套件，支持评估RX74N功能及开发嵌入式系统应用。

该系列MCU采用最高600 MHz的RXv3e处理器内核，具有以下功能：


- 1 MB代码磁阻随机存取存储器（MRAM）
- 1.5 MB RAM
- 内置加密模块
- 灵活数据速率控制器局域网（Controller Area Network with Flexible Data Rate，CAN FD）
- 千兆以太网模块（Gigabit Ethernet Module，ETHM），RGMII接口
- 高速及全速USB，支持主机及设备功能（Host／Function）
- 扩展SPI（eXpanded SPI，XSPI）接口，用于外部OctaFlash及OctalRAM

直接访问MCU引脚（MCU Native Pin Access）


- 600 MHz RX74N MCU（R5K574NCB4AE），320引脚LFBGA封装
- 通过两组30×2针及一组20×2针扩展排针直接访问MCU引脚
- MCU及USB模块电流测量点，用于测量电流消耗
- 24.000 MHz晶体振荡器作为主时钟
- 32.768 kHz晶体振荡器作为子时钟
- 512 Mbit外部OctaFlash及256 Mbit外部OctalRAM，位于EK-RX74N的MCU原生引脚访问区

系统控制与生态接口（System Control and Ecosystem Access）


- 五种5 V输入源


  - USB调试、高速、全速及串口端口
  - 外部电源，经表贴夹持测试点及电源输入过孔
- 两种调试模式


  - 板载调试，E2 Emulator OB，FINE接口
  - 外部调试输入，JTAG、SWD及FINE接口
- 用户LED及开关


  - 三个用户LED，红、蓝、绿
  - 白色电源LED，指示稳压电源可用
  - 黄色调试LED，指示调试连接
  - 两个用户开关
  - 一个复位开关
- 五种常见生态扩展接口


  - 两个Seeed Grove接口，I2C／模拟，未安装
  - 一个SparkFun Qwiic连接器，未安装
  - 两个Digilent Pmod连接器，UART／SPI／I2C
  - Arduino Uno R3连接器
  - MikroElektronika mikroBUS连接器
- USB串口转换接口
- USB全速主机及设备功能，位于EK-RX74N专用功能访问区

专用功能接口（Special Feature Access）


- CAN FD收发器及接口连接器
- 以太网连接器，RGMII接口
- USB高速主机及设备功能

<a id="hardware"></a>

## 硬件（Hardware）

详细硬件功能见：


- RX74N MCU：[RX74N组用户手册硬件篇](https://www.renesas.com/en/document/mah/rx74n-group-hardware-manual)
- EK-RX74N开发板：用户手册（[EK-RX74N用户手册](https://www.renesas.com/en/document/mat/ek-rx74n-v1-evaluation-kit-manual)）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`ek_rx74n`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="ek_rx74n-hw-features"></a>

<a id="ek_rx74n-ek_rx74n/r5k574ncb4ae-hw-features-section"></a>

#### `ek_rx74n/r5k574ncb4ae`目标（Target）

<a id="ek_rx74n-ek_rx74n/r5k574ncb4ae-hw-features-panel"></a>

<a id="ek_rx74n-ek_rx74n/r5k574ncb4ae-hw-features-memory"></a>

此开发板目标的存储器：1536 KiB RAM、1 MiB闪存。

<a id="ek_rx74n-ek_rx74n/r5k574ncb4ae-hw-features-table"></a>

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
<td>瑞萨RX处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx74-common.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P033_renesas_rxv3e.md#std-dtcompatible-renesas-rxv3e"><code>renesas,rxv3e</code></a></td>
</tr>
<tr>
<td rowspan="6">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX根时钟生成电路（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5k574x.dtsi?plain=1#L15">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P010_renesas_rx-cgc-root-clock.md#std-dtcompatible-renesas-rx-cgc-root-clock"><code>renesas,rx-cgc-root-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5k574x.dtsi?plain=1#L22">已启用：3</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA子时钟（Sub-Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5k574x.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P004_renesas_ra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk"><code>renesas,ra-cgc-subclk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX时钟生成电路PLLCCR（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5k574x.dtsi?plain=1#L47">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5k574x.dtsi?plain=1#L66">已禁用：6</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P009_renesas_rx-cgc-pllccr-type.md#std-dtcompatible-renesas-rx-cgc-pllccr-type"><code>renesas,rx-cgc-pllccr-type</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX时钟控制节点的pclk模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5k574x.dtsi?plain=1#L112">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P006_renesas_rx-cgc-pclk-block.md#std-dtcompatible-renesas-rx-cgc-pclk-block"><code>renesas,rx-cgc-pclk-block</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX时钟控制外设时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5k574x.dtsi?plain=1#L122">已启用：11</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5k574x.dtsi?plain=1#L203">已禁用：13</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P007_renesas_rx-cgc-pclk.md#std-dtcompatible-renesas-rx-cgc-pclk"><code>renesas,rx-cgc-pclk</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX GPIO输入输出端口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx74-common.dtsi?plain=1#L121">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx74-common.dtsi?plain=1#L61">已禁用：14</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P018_renesas_rx-gpio-ioport.md#std-dtcompatible-renesas-rx-gpio-ioport"><code>renesas,rx-gpio-ioport</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>瑞萨ICUM中断控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx74-common.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../renesas_interrupt_binding_reference/P003_renesas_rx-icum.md#std-dtcompatible-renesas-rx-icum"><code>renesas,rx-icum</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_rx74n/ek_rx74n.dts?plain=1#L24">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX SCI B控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx74-common.dtsi?plain=1#L387">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx74-common.dtsi?plain=1#L231">已禁用：12</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P025_renesas_rx-sci-b.md#std-dtcompatible-renesas-rx-sci-b"><code>renesas,rx-sci-b</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5k574ncx.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx74-common.dtsi?plain=1#L434">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P010_renesas_rx-pinctrl-pfs.md#std-dtcompatible-renesas-rx-pinctrl-pfs"><code>renesas,rx-pinctrl-pfs</code></a></td>
</tr>
<tr>
<td rowspan="1">保留内存（Reserved Memory）</td>
<td>片上（On-Chip）</td>
<td>Renesas选项设置存储器（Option-Setting Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx74-common.dtsi?plain=1#L440">已禁用：2</a>）</td>
<td><a href="../memory_protection_binding_reference/P011_renesas_ofs-memory.md#std-dtcompatible-renesas-ofs-memory"><code>renesas,ofs-memory</code></a></td>
</tr>
<tr>
<td rowspan="1">瑞萨 RX（Renesas RX）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX软件中断（Software Interrupt，SWINT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx74-common.dtsi?plain=1#L45">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P012_renesas_rx-swint.md#std-dtcompatible-renesas-rx-swint"><code>renesas,rx-swint</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX SCI_B UART控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx74-common.dtsi?plain=1#L394">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx74-common.dtsi?plain=1#L238">已禁用：12</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P011_renesas_rx-uart-sci-b.md#std-dtcompatible-renesas-rx-uart-sci-b"><code>renesas,rx-uart-sci-b</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5k574x.dtsi?plain=1#L331">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX定时器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx74-common.dtsi?plain=1#L400">已启用：1</a>）</td>
<td><a href="../renesas_timer_binding_reference/P003_renesas_rx-timer-cmt-start-control.md#std-dtcompatible-renesas-rx-timer-cmt-start-control"><code>renesas,rx-timer-cmt-start-control</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX定时器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx74-common.dtsi?plain=1#L409">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx74-common.dtsi?plain=1#L422">已禁用：1</a>）</td>
<td><a href="../renesas_timer_binding_reference/P004_renesas_rx-timer-cmt.md#std-dtcompatible-renesas-rx-timer-cmt"><code>renesas,rx-timer-cmt</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`ek_rx74n`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-rfp">rfp</a></td>
<td>✅（默认 / default）</td>
<td></td>
</tr>
</table>

ek_rx74n可按常规方式构建、烧录及调试，详见“构建应用”与“运行应用”。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b ek_rx74n samples/hello_world
west flash
```

打开串口终端并复位开发板，应在终端中看到以下信息：

```text
***** Booting Zephyr OS v4.4.0-xxx-xxxxxxxxxxxxx *****
Hello World! ek_rx74n
```

<a id="flashing"></a>

### 烧录（Flashing）

EK-RX74N可通过板载E2仿真电路（E2 Emulator On Board，E2OB）及瑞萨闪存编程器（RFP）的命令行接口rfp-cli烧录。RFP下载地址：[https://www.renesas.com/en/software-tool/renesas-flash-programmer-programming-gui](https://www.renesas.com/en/software-tool/renesas-flash-programmer-programming-gui)。

向开发板烧录程序：


1. 将USB DEBUG1连接器接到主机PC，按[EK-RX74N用户手册](https://www.renesas.com/en/document/mat/ek-rx74n-v1-evaluation-kit-manual)将DIP开关SW6设为板载调试模式。
2. 执行west命令。

  ```text
  west flash -r rfp
  ```

<a id="references"></a>

## 参考资料（References）


- [EK-RX74N网站](https://www.renesas.com/en/design-resources/boards-kits/ek-rx74n)
- [RX74N MCU组网站](https://www.renesas.com/en/products/rx74n)

## 译注

RX74N的以太网为RGMII，与RX74M的ESWM／EtherCAT不同，硬件列表分别保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [ek-rx74n-v1-evaluation-kit-manual](https://www.renesas.com/en/document/mat/ek-rx74n-v1-evaluation-kit-manual)：HTTP Error 429: Too Many Requests。
- [rx74n](https://www.renesas.com/en/products/rx74n)：HTTP Error 429: Too Many Requests。
- [renesas-flash-programmer-programming-gui](https://www.renesas.com/en/software-tool/renesas-flash-programmer-programming-gui)：HTTP Error 429: Too Many Requests。

---

[上一章](P002_RX74M_Evaluation_Kit.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_RA0E1_Fast_Prototype_Board.md)
