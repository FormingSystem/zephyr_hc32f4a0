---
id: learning.zephyr-docs.boards-nxp-lpc.page-5
title: LPCXpresso54628
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso54628/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="lpcxpresso54628"></a>

# 第5章\_LPCXpresso54628

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso54628/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/lpcxpresso54628.webp](images/lpcxpresso54628.webp)](images/lpcxpresso54628.webp)

LPCXpresso54628

名称（Name）：

`lpcxpresso54628`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[lpc54628](https://docs.zephyrproject.org/latest/boards/index.html#soc=lpc54628)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/lpcxpresso54628/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

LPCXpresso54628开发板OM13098采用基于Arm Cortex-M4F内核的NXP LPC54628 MCU。

<a id="hardware"></a>

## 硬件（Hardware）


- LPC54628 M4F，最高220 MHz
- 存储器（Memory）


  - 512 KB片上闪存
  - 200 KB片上SRAM，包含160 KB主SRAM、32 KB SRAMX及8 KB USB SRAM
- 板载高速USB调试探针LPC-Link2，支持CMSIS-DAP及J-Link协议
- 可选外部调试探针
- 3个用户LED及目标复位、ISP、中断／用户按键
- 基于Arduino UNO及Pmod的扩展选项，以及额外扩展端口引脚
- 8 MB串行闪存接口（SPIFI）闪存及128 Mbit同步动态RAM（SDRAM）
- 10/100 Mbit/s以太网、USB全速及高速接口、CAN

更多信息见以下资料：


- [LPC546xx SoC网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc-cortex-m4-mcus/lpc546xx-arm-cortex-m4-based-microcontroller-family:LPC546XX)
- [LPC546xx 数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/LPC546XX.pdf)
- [LPCXpresso54628 开发板网站](https://www.nxp.com/products/developer-resources/software-development-tools/developer-resources-/lpcxpresso-boards/lpcxpresso54628-development-board:OM13098)
- [LPCXpresso54628 开发板用户手册（Board User Manual）](https://www.nxp.com/webapp/Download?colCode=UM11035)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`lpcxpresso54628`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="lpcxpresso54628-hw-features"></a>

<a id="lpcxpresso54628-lpcxpresso54628/lpc54628-hw-features-section"></a>

#### `lpcxpresso54628/lpc54628`目标（Target）

<a id="lpcxpresso54628-lpcxpresso54628/lpc54628-hw-features-panel"></a>

<a id="lpcxpresso54628-lpcxpresso54628/lpc54628-hw-features-memory"></a>

该开发板目标的片上存储容量：160 KiB RAM、512 KiB Flash。

<a id="lpcxpresso54628-lpcxpresso54628/lpc54628-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>LPC Flexcomm节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L219">已禁用：8</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P015_nxp_lpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm"><code>nxp,lpc-flexcomm</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC SoC系列MCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L300">已禁用：2</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P001_nxp_lpc-mcan.md#std-dtcompatible-nxp-lpc-mcan"><code>nxp,lpc-mcan</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L41">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L347">已启用：5</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>用于lpc54xxx系列的NXP在应用编程（IAP）闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P010_nxp_iap-fmc54.md#std-dtcompatible-nxp-iap-fmc54"><code>nxp,iap-fmc54</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>LPC通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L127">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P006_nxp_lpc-gpio.md#std-dtcompatible-nxp-lpc-gpio"><code>nxp,lpc-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>LPC GPIO端口设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L133">已启用：6</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P005_nxp_lpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port"><code>nxp,lpc-gpio-port</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>LPC I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L228">已启用：1</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P003_nxp_lpc-i2c.md#std-dtcompatible-nxp-lpc-i2c"><code>nxp,lpc-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso54628/lpcxpresso54628.dts?plain=1#L40">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP分组GPIO输入中断（GINT / Grouped GPIO Input Interrupt）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L182">已禁用：2</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P001_nxp_gint.md#std-dtcompatible-nxp-gint"><code>nxp,gint</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP引脚中断及模式匹配引擎（PINT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L198">已启用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P004_nxp_pint.md#std-dtcompatible-nxp-pint"><code>nxp,pint</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso54628/lpcxpresso54628.dts?plain=1#L50">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L104">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>LPC I/O引脚配置（IOCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L115">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P007_nxp_lpc-iocon.md#std-dtcompatible-nxp-lpc-iocon"><code>nxp,lpc-iocon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>LPC引脚控制（Pinctrl）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L122">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P005_nxp_lpc-iocon-pinctrl.md#std-dtcompatible-nxp-lpc-iocon-pinctrl"><code>nxp,lpc-iocon-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P009_nxp_lpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset"><code>nxp,lpc-syscon-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC SD接口（SDIF）主控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L339">已启用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P015_nxp_lpc-sdif.md#std-dtcompatible-nxp-lpc-sdif"><code>nxp,lpc-sdif</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>FXOS8700六轴加速度计／磁力计传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso54628/lpcxpresso54628.dts?plain=1#L128">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P052_nxp_fxos8700.md#std-dtcompatible-nxp-fxos8700"><code>nxp,fxos8700</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC通用同步异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L210">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P014_nxp_lpc-usart.md#std-dtcompatible-nxp-lpc-usart"><code>nxp,lpc-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L61">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP LPCIP3511 USB设备模式（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L331">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/nxp_lpc546xx.dtsi?plain=1#L322">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P008_nxp_lpcip3511.md#std-dtcompatible-nxp-lpcip3511"><code>nxp,lpcip3511</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

可通过IOCON控制器配置LPC54628引脚。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PIO0_29</td>
<td>通用异步收发器（UART）</td>
<td>USART接收（RX），虚拟COM端口（VCOM）</td>
</tr>
<tr>
<td>PIO0_30</td>
<td>通用异步收发器（UART）</td>
<td>USART发送（TX），虚拟COM端口（VCOM）</td>
</tr>
<tr>
<td>PIO3_14</td>
<td>通用输入输出（GPIO）</td>
<td>用户LED1</td>
</tr>
<tr>
<td>PIO3_3</td>
<td>通用输入输出（GPIO）</td>
<td>用户LED2</td>
</tr>
<tr>
<td>PIO2_2</td>
<td>通用输入输出（GPIO）</td>
<td>用户LED3</td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`lpcxpresso54628`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>调试服务器（debugserver）</th>
<th>连接调试会话（attach）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-linkserver">linkserver</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

按通常方式构建并烧录应用，详见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）与“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

<a id="configuring-a-debug-probe"></a>

### 配置调试探针（Configuring a Debug Probe）

默认运行工具为LinkServer，烧录及调试都使用调试探针。此板默认使用CMSIS-DAP模式的板载LPC-Link2探针。需安装LinkServer调试主机工具并加入搜索路径，才能用于Zephyr；更多信息见“应用调试”（[Application Debugging](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)）概述。（[LPC-Link2 CMSIS-DAP板载调试探针](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#lpclink2-cmsis-onboard-debug-probe)；[LinkServer调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#linkserver-debug-host-tools)）

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

用USB线缆将PC连接到LPC-Link2 USB连接器，在所选串口终端（如minicom、PuTTY）中使用以下设置：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

### 烧录（Flashing）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b lpcxpresso54628 samples/hello_world
west flash
```

打开串口终端，复位开发板（按下RESET按键），应能在终端中看到以下消息：

```text
*** Booting Zephyr OS build v4.4.0 ***
Hello World! lpcxpresso54628/lpc54628
```

<a id="debugging"></a>

### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b lpcxpresso54628 samples/hello_world
west debug
```

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)
- [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)
- [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- NXP Zephyr主页，包含培训资源（[NXP的Zephyr专题页面](https://nxp.com/zephyr)）
- [NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [LPC546XX.pdf](https://www.nxp.com/docs/en/data-sheet/LPC546XX.pdf)：HTTP Error 404: Not Found。
- [lpcxpresso54628-development-board:OM13098](https://www.nxp.com/products/developer-resources/software-development-tools/developer-resources-/lpcxpresso-boards/lpcxpresso54628-development-board:OM13098)：HTTP Error 404: Not Found。
- [lpc546xx-arm-cortex-m4-based-microcontroller-family:LPC546XX](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc-cortex-m4-mcus/lpc546xx-arm-cortex-m4-based-microcontroller-family:LPC546XX)：HTTP Error 404: Not Found。
- [Download?colCode=UM11035](https://www.nxp.com/webapp/Download?colCode=UM11035)：HTTP Error 404: Not Found。

---

[上一章](P004_LPCXPRESSO54114.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_LPCXpresso55S06.md)
