---
id: learning.zephyr-docs.boards-renesas-rx-rz.page-4
title: RA0E1 Fast Prototype Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/renesas/fpb_ra0e1/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="fpb_ra0e1"></a>

# 第4章\_RA0E1快速原型板（Fast Prototype Board）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/renesas/fpb_ra0e1/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/fpb_ra0e1.webp](images/fpb_ra0e1.webp)](images/fpb_ra0e1.webp)

RA0E1快速原型板（Fast Prototype Board）

名称（Name）：

`fpb_ra0e1`

厂商（Vendor）：

[瑞萨电子（Renesas Electronics Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=renesas)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[r7fa0e1073cfj](https://docs.zephyrproject.org/latest/boards/index.html#soc=r7fa0e1073cfj)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/fpb_ra0e1/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

FPB-RA0E1采用与FPB系列其他板卡相似的架构。除RA MCU外，还包括板载编程器、引出RA MCU全部引脚的排针、电源稳压器、LED及开关，以及Pmod和Arduino等生态的输入输出连接器。

FPB-RA0E1主要功能按板卡架构分为以下两组：

MCU及其原生引脚访问


- R7FA0E1073CFJ MCU，下称RA MCU
- 32 MHz Arm Cortex-M23内核
- 64 KB代码闪存、12 KB SRAM、1 KB数据闪存
- 32引脚LQFP封装
- 两组16针公排针，直接访问MCU引脚，未安装
- MCU VCC电流测量点，用于精确测量电流消耗
- 多种时钟源：RA MCU内置高速、中速及低速振荡器。主时钟与子时钟也可分别使用20.000 MHz晶体振荡器（未安装）及32.768 kHz晶体振荡器的信号

系统控制与生态接口（System Control and Ecosystem Access）


- USB全速设备，USB 2.0 Type-C连接器
- 两种5 V输入源

  > - USB调试及全速端口
  > - 外部电源，使用两针排针，未安装
- 板载SWD调试器
- 用户LED及按键

  > - 2个绿色用户LED
  > - 绿色电源LED，指示稳压电源可用
  > - 黄色调试／电源LED，指示供电及调试连接
  > - 1个用户按键
  > - 1个复位按键
- 两种常见生态扩展接口

  > - 2个Digilent Pmod连接器，SPI、UART及I2C
  > - Arduino Uno R3连接器

<a id="hardware"></a>

## 硬件（Hardware）

详细硬件功能见：


- RA0E1 MCU：[RA0E1组用户手册硬件篇](https://www.renesas.com/en/document/mah/ra0e1-group-users-manual-hardware)
- FPB-RA0E1开发板：用户手册（[FPB-RA0E1用户手册](https://www.renesas.com/en/document/mat/fpb-ra0e1-users-manual)）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`fpb_ra0e1`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="fpb_ra0e1-hw-features"></a>

<a id="fpb_ra0e1-fpb_ra0e1/r7fa0e1073cfj-hw-features-section"></a>

#### `fpb_ra0e1/r7fa0e1073cfj`目标（Target）

<a id="fpb_ra0e1-fpb_ra0e1/r7fa0e1073cfj-hw-features-panel"></a>

<a id="fpb_ra0e1-fpb_ra0e1/r7fa0e1073cfj-hw-features-memory"></a>

该开发板目标的片上存储容量：12 KiB RAM、64 KiB Flash。

<a id="fpb_ra0e1-fpb_ra0e1/r7fa0e1073cfj-hw-features-table"></a>

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
<td>Arm Cortex-M23 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/ra0xx.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P020_arm_cortex-m23.md#std-dtcompatible-arm-cortex-m23"><code>arm,cortex-m23</code></a></td>
</tr>
<tr>
<td rowspan="6">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA时钟生成电路（Clock Generation Circuit）的外部时钟配置（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/r7fa0e10x.dtsi?plain=1#L61">已禁用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P029_renesas_ra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock"><code>renesas,ra-cgc-external-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/r7fa0e10x.dtsi?plain=1#L67">已启用：3</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA子时钟（Sub-Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/r7fa0e10x.dtsi?plain=1#L85">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P004_renesas_ra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk"><code>renesas,ra-cgc-subclk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定比例时钟提供器（Fixed Factor Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/r7fa0e10x.dtsi?plain=1#L92">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/r7fa0e10x.dtsi?plain=1#L113">已禁用：1</a>）</td>
<td><a href="../timer_reference/P110_固定比例时钟绑定.md#dtbinding-fixed-factor-clock"><code>fixed-factor-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA时钟控制节点的pclk模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/r7fa0e10x.dtsi?plain=1#L125">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P030_renesas_ra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block"><code>renesas,ra-cgc-pclk-block</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA时钟控制外设时钟（Peripheral Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/r7fa0e10x.dtsi?plain=1#L134">已启用：9</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/r7fa0e10x.dtsi?plain=1#L207">已禁用：5</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P001_renesas_ra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk"><code>renesas,ra-cgc-pclk</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/ra0xx.dtsi?plain=1#L114">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P008_renesas_ra-crc.md#std-dtcompatible-renesas-ra-crc"><code>renesas,ra-crc</code></a></td>
</tr>
<tr>
<td rowspan="2">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA闪存控制块（Flash Control Block）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/ra0xx.dtsi?plain=1#L106">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P026_renesas_ra-fcb.md#std-dtcompatible-renesas-ra-fcb"><code>renesas,ra-fcb</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA系列低功耗闪存控制器（Flash Low-Power Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/r7fa0e10x.dtsi?plain=1#L20">已启用：2</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P028_renesas_ra-flash-lp-controller.md#std-dtcompatible-renesas-ra-flash-lp-controller"><code>renesas,ra-flash-lp-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA通用输入输出端口（GPIO I/O Port）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/ra0xx.dtsi?plain=1#L40">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/ra0xx.dtsi?plain=1#L50">已禁用：4</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P014_renesas_ra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport"><code>renesas,ra-gpio-ioport</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/fpb_ra0e1/fpb_ra0e1.dts?plain=1#L39">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/fpb_ra0e1/fpb_ra0e1.dts?plain=1#L25">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="4">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>Renesas RA事件链接控制器（Event Link Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/ra0xx.dtsi?plain=1#L32">已禁用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P016_renesas_ra-elc.md#std-dtcompatible-renesas-ra-elc"><code>renesas,ra-elc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Renesas RA外部中断（External Interrupt）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/ra0xx.dtsi?plain=1#L121">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/ra0xx.dtsi?plain=1#L130">已禁用：5</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P017_renesas_ra-external-interrupt.md#std-dtcompatible-renesas-ra-external-interrupt"><code>renesas,ra-external-interrupt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RA串行阵列单元（Serial Array Unit，SAU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/ra0xx.dtsi?plain=1#L194">已启用：2</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P019_renesas_ra-sau.md#std-dtcompatible-renesas-ra-sau"><code>renesas,ra-sau</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RA串行阵列单元通道（SAU Channel）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/ra0xx.dtsi?plain=1#L201">已启用：6</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P018_renesas_ra-sau-channel.md#std-dtcompatible-renesas-ra-sau-channel"><code>renesas,ra-sau-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/r7fa0e10x.dtsi?plain=1#L28">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RA0引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/ra0xx.dtsi?plain=1#L100">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P007_renesas_ra0-pinctrl-pfs.md#std-dtcompatible-renesas-ra0-pinctrl-pfs"><code>renesas,ra0-pinctrl-pfs</code></a></td>
</tr>
<tr>
<td rowspan="1">保留内存（Reserved Memory）</td>
<td>片上（On-Chip）</td>
<td>Renesas选项设置存储器（Option-Setting Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/ra0xx.dtsi?plain=1#L175">已启用：2</a>）</td>
<td><a href="../memory_protection_binding_reference/P011_renesas_ofs-memory.md#std-dtcompatible-renesas-ofs-memory"><code>renesas,ofs-memory</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RA SAU UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/ra0xx.dtsi?plain=1#L237">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/ra0xx.dtsi?plain=1#L245">已禁用：2</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P007_renesas_ra-uart-sau.md#std-dtcompatible-renesas-ra-uart-sau"><code>renesas,ra-uart-sau</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra0/r7fa0e10x.dtsi?plain=1#L12">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`fpb_ra0e1`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-pyocd">pyocd</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

fpb_ra0e1可按常规方式构建、烧录及调试，详见“构建应用”与“运行应用”。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b fpb_ra0e1 samples/hello_world
west flash
```

打开串口终端，按复位开关S2复位开发板，终端应显示以下消息：

```text
***** Booting Zephyr OS v4.3.0-xxx-xxxxxxxxxxxxx *****
Hello World! fpb_ra0e1/r7fa0e1073cfj
```

<a id="flashing"></a>

### 烧录（Flashing）

FPB-RA0E1可通过板载SEGGER J-Link烧录，驱动见[https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)。

向开发板烧录程序：


1. 通过USB将J-Link OB连接主机；原文此处称OB，与前文外部调试器表述不同。
2. 确认J-Link OB跳线保持[FPB-RA0E1用户手册](https://www.renesas.com/en/document/mat/fpb-ra0e1-users-manual)中的默认配置。
3. 执行west命令。

  > ```text
  > west flash -r jlink
  > ```

<a id="references"></a>

## 参考资料（References）


- [FPB-RA0E1网站](https://www.renesas.com/en/design-resources/boards-kits/fpb-ra0e1)
- [RA0E1 MCU组网站](https://www.renesas.com/en/products/ra0e1)

## 译注

RA0E1的20 MHz主晶体未安装，32.768 kHz子晶体与内部高速／中速／低速时钟分别说明。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [fpb-ra0e1-users-manual](https://www.renesas.com/en/document/mat/fpb-ra0e1-users-manual)：HTTP Error 429: Too Many Requests。
- [ra0e1](https://www.renesas.com/en/products/ra0e1)：HTTP Error 429: Too Many Requests。

---

[上一章](P003_RX74N_Evaluation_Kit.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_RA4E1_Fast_Prototyping_Board.md)
