---
id: learning.zephyr-docs.boards-nxp-lpc.page-3
title: LPCXPRESSO51U68
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso51u68/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="lpcxpresso51u68"></a>

# 第3章\_LPCXPRESSO51U68

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso51u68/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/lpcxpresso51u68.jpg](images/lpcxpresso51u68.jpg)](images/lpcxpresso51u68.jpg)

LPCXPRESSO51U68

名称（Name）：

`lpcxpresso51u68`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[lpc51u68](https://docs.zephyrproject.org/latest/boards/index.html#soc=lpc51u68)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/lpcxpresso51u68/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

LPCXpresso51U68采用NXP LPC51U68 MCU，原文描述为基于Arm Cortex-M0+内核。

<a id="hardware"></a>

## 硬件（Hardware）


- LPC51U68 M0+，原文列出的最高频率为150 MHz
- 存储器（Memory）


  - 256 KB闪存
  - 96 KB SRAM
- 板载高速USB调试探针，支持CMSIS-DAP及J-Link协议，可调试板上LPC51U68或外部目标
- 可选外部调试探针
- 三色LED及目标复位、ISP、中断／用户按键，便于测试软件功能
- 基于Arduino UNO及Pmod的扩展选项，以及额外扩展端口引脚
- FTDI UART连接器

更多信息见以下资料：


- [LPC51U68 SoC网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/high-performance-power-efficient-and-cost-sensitive-arm-cortex-m0-plus-mcus:LPC51U68)
- [LPC51U68 数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/LPC51U68.pdf)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`lpcxpresso51u68`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="lpcxpresso51u68-hw-features"></a>

<a id="lpcxpresso51u68-lpcxpresso51u68/lpc51u68-hw-features-section"></a>

#### `lpcxpresso51u68/lpc51u68`目标（Target）

<a id="lpcxpresso51u68-lpcxpresso51u68/lpc51u68-hw-features-panel"></a>

<a id="lpcxpresso51u68-lpcxpresso51u68/lpc51u68-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、256 KiB Flash。

<a id="lpcxpresso51u68-lpcxpresso51u68/lpc51u68-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>LPC Flexcomm节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L125">已禁用：5</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P015_nxp_lpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm"><code>nxp,lpc-flexcomm</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L198">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P007_nxp_lpc-crc.md#std-dtcompatible-nxp-lpc-crc"><code>nxp,lpc-crc</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>LPC通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P006_nxp_lpc-gpio.md#std-dtcompatible-nxp-lpc-gpio"><code>nxp,lpc-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>LPC GPIO端口设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L72">已启用：2</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P005_nxp_lpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port"><code>nxp,lpc-gpio-port</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>LPC I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L152">已启用：1</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P003_nxp_lpc-i2c.md#std-dtcompatible-nxp-lpc-i2c"><code>nxp,lpc-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso51u68/lpcxpresso51u68.dts?plain=1#L55">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP分组GPIO输入中断（GINT / Grouped GPIO Input Interrupt）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L89">已启用：2</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P001_nxp_gint.md#std-dtcompatible-nxp-gint"><code>nxp,gint</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP引脚中断及模式匹配引擎（PINT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L105">已启用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P004_nxp_pint.md#std-dtcompatible-nxp-pint"><code>nxp,pint</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso51u68/lpcxpresso51u68.dts?plain=1#L36">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L49">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>LPC I/O引脚配置（IOCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L54">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P007_nxp_lpc-iocon.md#std-dtcompatible-nxp-lpc-iocon"><code>nxp,lpc-iocon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>LPC引脚控制（Pinctrl）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L61">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P005_nxp_lpc-iocon-pinctrl.md#std-dtcompatible-nxp-lpc-iocon-pinctrl"><code>nxp,lpc-iocon-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NXP状态可配置定时器（SCTimer）脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L188">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P012_nxp_sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm"><code>nxp,sctimer-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P009_nxp_lpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset"><code>nxp,lpc-syscon-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC通用同步异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L116">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P014_nxp_lpc-usart.md#std-dtcompatible-nxp-lpc-usart"><code>nxp,lpc-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC串行外设接口（SPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L161">已启用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P003_nxp_lpc-spi.md#std-dtcompatible-nxp-lpc-spi"><code>nxp,lpc-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc51u68/nxp_lpc51u68.dtsi?plain=1#L39">已启用：2</a>）</td>
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

可通过IOCON控制器配置LPC51U68引脚。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PIO0_0</td>
<td>通用异步收发器（UART）</td>
<td>USART接收（RX）</td>
</tr>
<tr>
<td>PIO0_1</td>
<td>通用异步收发器（UART）</td>
<td>USART发送（TX）</td>
</tr>
<tr>
<td>PIO1_10</td>
<td>通用输入输出（GPIO）</td>
<td>绿色LED（GREEN LED）</td>
</tr>
<tr>
<td>PIO0_29</td>
<td>通用输入输出（GPIO）</td>
<td>红色LED（RED LED）</td>
</tr>
<tr>
<td>PIO1_9</td>
<td>通用输入输出（GPIO）</td>
<td>BLUE_LED</td>
</tr>
<tr>
<td>PIO0_25</td>
<td>集成电路间总线（I2C）</td>
<td>I2C串行时钟（SCL）</td>
</tr>
<tr>
<td>PIO0_26</td>
<td>集成电路间总线（I2C）</td>
<td>I2C串行数据（SDA）</td>
</tr>
<tr>
<td>PIO0_18</td>
<td>串行外设接口（SPI）</td>
<td>SPI主机输入从机输出（MISO）</td>
</tr>
<tr>
<td>PIO0_19</td>
<td>串行外设接口（SPI）</td>
<td>SPI串行时钟（SCK）</td>
</tr>
<tr>
<td>PIO0_20</td>
<td>串行外设接口（SPI）</td>
<td>SPI主机输出从机输入（MOSI）</td>
</tr>
<tr>
<td>PIO1_1</td>
<td>串行外设接口（SPI）</td>
<td>SPI从设备选择2（SSEL2）</td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`lpcxpresso51u68`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

按通常方式构建并烧录应用，详见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）与“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

<a id="configuring-a-debug-probe"></a>

### 配置调试探针（Configuring a Debug Probe）

烧录及调试都使用调试探针。此板默认配置为使用LPC-Link2 CMSIS-DAP板载探针，但原文说明pyOCD调试主机工具不支持该探针，因此必须重新配置为以下调试探针之一。（[pyOCD调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#pyocd-debug-host-tools)）

<a id="lpclink2-jlink-onboard-debug-probe"></a>

#### [LPC-Link2 J-Link板载调试探针（Onboard Debug Probe）](../debugging/P003_调试探针.md#lpclink2-jlink-onboard-debug-probe)

安装J-Link调试主机工具（Debug Host Tools），并确保工具位于搜索路径中。（[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)）

按LPC-Link2 J-Link板载调试探针说明写入J-Link固件。（[LPC-Link2 J-Link板载调试探针（Onboard Debug Probe）](../debugging/P003_调试探针.md#lpclink2-jlink-onboard-debug-probe)）

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

将USB转FTDI串口适配器的RX、TX和GND接到P3连接器。

在串口终端中使用以下设置，例如minicom或PuTTY：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

### 烧录（Flashing）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b lpcxpresso51u68 samples/hello_world
west flash
```

```text
***** Booting Zephyr OS build zephyr-v2.6.0-934-g4c438c0c7d13 *****
Hello World! lpcxpresso51u68
```

<a id="debugging"></a>

### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b lpcxpresso51u68 samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
***** Booting Zephyr OS build zephyr-v2.6.0-934-g4c438c0c7d13 *****
Hello World! lpcxpresso51u68
```

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)
- [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)
- [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- NXP Zephyr主页，包含培训资源（[NXP的Zephyr专题页面](https://nxp.com/zephyr)）
- [NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## 译注

原文将LPC51U68写为Cortex-M0+、最高150 MHz，均按来源保留；pyOCD不支持该探针的描述也保留为来源条件。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [LPC51U68.pdf](https://www.nxp.com/docs/en/data-sheet/LPC51U68.pdf)：HTTP Error 404: Not Found。
- [high-performance-power-efficient-and-cost-sensitive-arm-cortex-m0-plus-mcus:LPC51U68](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/high-performance-power-efficient-and-cost-sensitive-arm-cortex-m0-plus-mcus:LPC51U68)：HTTP Error 404: Not Found。

---

[上一章](P002_LPCXpresso11U68.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_LPCXPRESSO54114.md)
