---
id: learning.zephyr-docs.boards-renesas-rx-rz.page-14
title: RX26T Motor Control Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/renesas/mcb_rx26t/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mcb_rx26t"></a>

# 第14章\_RX26T电机控制板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/renesas/mcb_rx26t/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mcb_rx26t.webp](images/mcb_rx26t.webp)](images/mcb_rx26t.webp)

RX26T电机控制板

名称（Name）：

`mcb_rx26t`

厂商（Vendor）：

[瑞萨电子（Renesas Electronics Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=renesas)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[rx](https://docs.zephyrproject.org/latest/boards/index.html#arch=rx)

片上系统（SoC）：

[r5f526tfddfp](https://docs.zephyrproject.org/latest/boards/index.html#soc=r5f526tfddfp)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/mcb_rx26t/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

MCB-RX26T Type B是用于电机控制评估的CPU板，与逆变器板配合即可方便地使用RX26T控制电机。

直接访问MCU引脚（MCU Native Pin Access）

MCB-RX26T Type B包括：


- CPU最高工作频率120 MHz，32位RXv3内核
- 封装／引脚数量：LFQFP／100针
- ROM／RAM：512 KB／64 KB
- MCU输入时钟：10 MHz，由外部晶体振荡器产生

系统控制与调试


- 电源：直流5 V、3.3 V，通过跳线开关选择；自动从以下输入方式选择一种


  - 通过USB调试端口供电
  - 经标准输入连接外部电源
- 调试支持：


  - 通过E2lite及E2OB板载调试电路，断开跳线J11
  - 通过JLink及JTAG连接器，短接跳线J11
- 连接器（Connector）：


  - 逆变器板连接器
  - E2 OB的USB连接器
  - 与Renesas Motor Workbench通信的SCI连接器
  - CAN通信通孔
  - SPI通信通孔
  - Pmod连接器
- 用户LED及按键：


  - 四个用户LED
  - 电源LED，指示稳压电源可用
  - 一个复位键

<a id="hardware"></a>

## 硬件（Hardware）

详细硬件功能见：


- RX26T MCU：[RX26T组用户手册硬件篇](https://www.renesas.com/en/document/mah/rx26t-group-users-manual-hardware)
- MCB-RX26T Type B：用户手册（[MCB-RX26T Type B用户手册](https://www.renesas.com/en/document/mat/mcb-rx26t-type-b-users-manual)）

注意：RX26T的CPU基于RXv3内核，但原文所述Zephyr内核版本仅支持RXv1。由于RXv3向后兼容RXv1，可以在该版本运行，但有以下限制：


- 不支持保存浮点运算单元（FPU）上下文，不要使用FPU。
- 不支持寄存器组保存（Register Bank Save）功能，不要使用相关指令。
- 不支持保存累加器寄存器（Accumulator Register），不要使用数字信号处理（DSP）指令或包含DSP指令的库。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`mcb_rx26t`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mcb_rx26t-hw-features"></a>

<a id="mcb_rx26t-mcb_rx26t@typeb/r5f526tfddfp-hw-features-section"></a>

#### `mcb_rx26t@typeb/r5f526tfddfp`目标（Target）

<a id="mcb_rx26t-mcb_rx26t@typeb/r5f526tfddfp-hw-features-panel"></a>

<a id="mcb_rx26t-mcb_rx26t@typeb/r5f526tfddfp-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、512 KiB Flash。

<a id="mcb_rx26t-mcb_rx26t@typeb/r5f526tfddfp-hw-features-table"></a>

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
<td>瑞萨RXv3处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P032_renesas_rxv3.md#std-dtcompatible-renesas-rxv3"><code>renesas,rxv3</code></a></td>
</tr>
<tr>
<td rowspan="4">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX根时钟生成电路（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f526tfddfp.dtsi?plain=1#L16">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f526tfddfp.dtsi?plain=1#L39">已禁用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P010_renesas_rx-cgc-root-clock.md#std-dtcompatible-renesas-rx-cgc-root-clock"><code>renesas,rx-cgc-root-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX时钟生成电路的锁相环（PLL）时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f526tfddfp.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P008_renesas_rx-cgc-pll.md#std-dtcompatible-renesas-rx-cgc-pll"><code>renesas,rx-cgc-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX时钟控制节点的pclk模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f526tfddfp.dtsi?plain=1#L62">已启用：1</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P006_renesas_rx-cgc-pclk-block.md#std-dtcompatible-renesas-rx-cgc-pclk-block"><code>renesas,rx-cgc-pclk-block</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX时钟控制外设时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f526tfddfp.dtsi?plain=1#L70">已启用：7</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f526tfddfp.dtsi?plain=1#L120">已禁用：5</a>）</td>
<td><a href="../clock_renesas_rockchip_sifli_silabs_binding_reference/P007_renesas_rx-cgc-pclk.md#std-dtcompatible-renesas-rx-cgc-pclk"><code>renesas,rx-cgc-pclk</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f526tfddfp.dtsi?plain=1#L163">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P001_renesas_rx-flash.md#std-dtcompatible-renesas-rx-flash"><code>renesas,rx-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX系列通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L223">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L187">已禁用：13</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P019_renesas_rx-gpio.md#std-dtcompatible-renesas-rx-gpio"><code>renesas,rx-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX I2C主控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L544">已启用：1</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P016_renesas_rx-i2c.md#std-dtcompatible-renesas-rx-i2c"><code>renesas,rx-i2c</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>瑞萨中断控制单元（ICU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../renesas_interrupt_binding_reference/P002_renesas_rx-icu.md#std-dtcompatible-renesas-rx-icu"><code>renesas,rx-icu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨分组中断（Group Interrupt）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L611">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L599">已禁用：4</a>）</td>
<td><a href="../renesas_interrupt_binding_reference/P001_renesas_rx-grp-intc.md#std-dtcompatible-renesas-rx-grp-intc"><code>renesas,rx-grp-intc</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/mcb_rx26t/mcb_rx26t.dts?plain=1#L24">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX数据传输控制器（Data Transfer Controller，DTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L62">已启用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P022_renesas_rx-dtc.md#std-dtcompatible-renesas-rx-dtc"><code>renesas,rx-dtc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX串行通信接口（SCI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L527">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L476">已禁用：3</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P026_renesas_rx-sci.md#std-dtcompatible-renesas-rx-sci"><code>renesas,rx-sci</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX系列闪存的设备树绑定（Binding）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f526tfddfp.dtsi?plain=1#L169">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P011_renesas_rx-nv-flash.md#std-dtcompatible-renesas-rx-nv-flash"><code>renesas,rx-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L76">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P011_renesas_rx-pinctrl.md#std-dtcompatible-renesas-rx-pinctrl"><code>renesas,rx-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX引脚复用，多功能引脚控制器（Multi Function Pin Controller，MPC）；原文厂商名拼作Rensas（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L82">已启用：15</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P012_renesas_rx-pinmux.md#std-dtcompatible-renesas-rx-pinmux"><code>renesas,rx-pinmux</code></a></td>
</tr>
<tr>
<td rowspan="1">瑞萨 RX（Renesas RX）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX软件中断（Software Interrupt，SWINT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P012_renesas_rx-swint.md#std-dtcompatible-renesas-rx-swint"><code>renesas,rx-swint</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX SCI UART控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L538">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L487">已禁用：3</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P013_renesas_rx-uart-sci.md#std-dtcompatible-renesas-rx-uart-sci"><code>renesas,rx-uart-sci</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f526tfddfp.dtsi?plain=1#L157">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>瑞萨RX定时器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L558">已启用：1</a>）</td>
<td><a href="../renesas_timer_binding_reference/P003_renesas_rx-timer-cmt-start-control.md#std-dtcompatible-renesas-rx-timer-cmt-start-control"><code>renesas,rx-timer-cmt-start-control</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>瑞萨RX定时器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx26t-common.dtsi?plain=1#L567">已启用：2</a>）</td>
<td><a href="../renesas_timer_binding_reference/P004_renesas_rx-timer-cmt.md#std-dtcompatible-renesas-rx-timer-cmt"><code>renesas,rx-timer-cmt</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`mcb_rx26t`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>✅</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-rfp">rfp</a></td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

mcb_rx26t可按常规方式构建、烧录及调试，详见“构建应用”与“运行应用”。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）

<a id="flashing"></a>

### 烧录（Flashing）

MCB-RX26T可通过e2lite E2OB板载调试电路烧录。

向开发板烧录程序：

> 1. 使用E2 OB的USB连接器，将板上调试连接端口接到主机PC。
> 2. 执行west命令。
>
> > ```text
> > west flash
> > ```

<a id="debugging"></a>

### 调试（Debugging）

可使用Visual Studio Code的Renesas Debug扩展获得图形调试界面，launch.json配置如下。（[Renesas Debug调试扩展](https://marketplace.visualstudio.com/items?itemName=RenesasElectronicsCorporation.renesas-debug)）

```text
{
  "version": "0.2.0",
  "configurations": [
      {
          "type": "renesas-hardware",
          "request": "launch",
          "name": "Renesas GDB Hardware Debugging",
          "target": {
              "deviceFamily": "RX",
              "device": "R5F526TF",
              "debuggerType": "E2LITE",
              "serverParameters": [
                  "-uUseFine=", "1",
                  "-w=", "1",
              ],
          }
      }
  ]
}
```

<a id="references"></a>

## 参考资料（References）


- [MCB-RX26T Type B网站](https://www.renesas.com/en/design-resources/boards-kits/mcb-rx26t-type-b)
- [RX26T MCU组网站](https://www.renesas.com/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/rx26t-32-bit-microcontroller-optimized-dual-motor-and-pfc-control)

## 译注

MCB-RX26T原文记载当时Zephyr仅支持RXv1，利用RXv3向后兼容运行；FPU、寄存器组保存及DSP累加器上下文的限制保留。该记录不代表本次重新验证了当前内核支持。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [mcb-rx26t-type-b-users-manual](https://www.renesas.com/en/document/mat/mcb-rx26t-type-b-users-manual)：HTTP Error 429: Too Many Requests。
- [rx26t-32-bit-microcontroller-optimized-dual-motor-and-pfc-control](https://www.renesas.com/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/rx26t-32-bit-microcontroller-optimized-dual-motor-and-pfc-control)：HTTP Error 429: Too Many Requests。

---

[上一章](P013_RX14T_Motor_Control_Board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P015_RA4T1_Motor_Control_Kit.md)
