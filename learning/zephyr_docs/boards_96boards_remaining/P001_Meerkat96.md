---
id: learning.zephyr-docs.boards-96boards-remaining.page-1
title: Meerkat96
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/96boards/meerkat96/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="96b_meerkat96"></a>

# 第1章\_Meerkat96

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/96boards/meerkat96/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/96b_meerkat96.jpg](images/96b_meerkat96.jpg)](images/96b_meerkat96.jpg)

Meerkat96

名称（Name）：

`96b_meerkat96`

厂商（Vendor）：

[96Boards](https://docs.zephyrproject.org/latest/boards/index.html#vendor=96boards)

状态（Status）：

未处于积极维护状态（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mcimx7d](https://docs.zephyrproject.org/latest/boards/index.html#soc=mcimx7d)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/96boards/meerkat96/doc/index.rst/../..)<a id="boards-meerkat96"></a>

## 96Boards Meerkat96

<a id="overview"></a>

### 概述（Overview）

96Boards Meerkat96开发板采用NXP i.MX7异构多核处理器（Hybrid Multi-core Processor），由两个Cortex®-A7内核和一个Cortex®-M4内核组成。Zephyr操作系统移植到Cortex®-M4内核运行。


- 开发板特性（Board Features）：


  - 随机存储器（RAM）：512 Mbyte
  - 存储（Storage）：


    - microSD卡插槽（Socket）
  - 无线（Wireless）：


    - 无线局域网（Wi-Fi）：2.4 GHz IEEE 802.11b/g/n
    - 蓝牙（Bluetooth）：v4.1，基本速率／增强数据速率（BR/EDR）
  - USB:


    - 主机（Host）：2个Type-A接口
    - USB OTG：1个Micro-B接口
  - HDMI
  - 接插件（Connectors）：


    - 40 引脚低速排针（Low-Speed Header）。
    - 60 引脚高速排针（High-Speed Header）。
  - 发光二极管（LED）：


    - 4 个绿色用户 LED。
    - 1 个蓝色蓝牙 LED。
    - 1 个黄色 Wi-Fi LED。

开发板更多信息见 96Boards 网站。（[96Boards网站](https://www.96boards.org/product/imx7-96/)）

<a id="hardware"></a>

### 硬件（Hardware）

i.MX7片上系统（SoC）提供以下硬件能力：


- 两个Cortex-A7内核（800 MHz / 1.0 GHz）和一个Cortex-M4内核（200 MHz）
- 存储器（Memory）


  - 外部双倍数据率存储器（DDR）容量最高1 Gbyte
  - 内部RAM → A7：256 KB静态随机存储器（SRAM）
  - 内部RAM → M4：3 × 32 KB（TCML、TCMU、OCRAM_S）、1 × 128 KB（OCRAM）和1 × 256 MB（DDR）
- 显示（Display）


  - RGB显示：1920 × 1080，每像素24位（24 bpp）
  - 四线电阻式触摸（4-wire Resistive Touch）
- 多媒体（Multimedia）


  - 1路摄像头并行接口（Camera Parallel Interface）
  - 1路模拟音频线路输入（Line In，立体声）
  - 1路模拟音频麦克风输入（Mic In，单声道）
  - 1路模拟音频耳机输出（Headphone Out，立体声）
- 连接能力（Connectivity）


  - USB 2.0 OTG（高速 / High Speed）
  - USB 2.0主机（Host，高速 / High Speed）
  - 10/100 Mbit/s以太网物理层收发器（Ethernet PHY）
  - 4路I2C总线
  - 4路串行外设接口（SPI）
  - 7路通用异步收发器（UART）
  - 1路红外数据接口（IrDA）
  - 20路脉宽调制（PWM）
  - 最多125个通用输入输出（GPIO）
  - 4路模拟输入（Analog Input），12位
  - 2路SDIO / SD / MMC接口，8位
  - 2路控制器局域网（CAN）

有关i.MX7片上系统（SoC）的更多信息，请参阅：


- [i.MX 7系列网站（Series Website）](https://www.nxp.com/products/processors-and-microcontrollers/applications-processors/i.mx-applications-processors/i.mx-7-processors:IMX7-SERIES?fsrch=1&sr=1&pageNum=1)
- [i.MX 7 Dual数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/IMX7DCEC.pdf)
- [i.MX 7 Dual参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=IMX7DRM)

<a id="supported-features"></a>

#### 支持的功能（Supported Features）

`96b_meerkat96`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="96b_meerkat96-hw-features"></a>

<a id="96b_meerkat96-96b_meerkat96/mcimx7d/m4-hw-features-section"></a>

##### `96b_meerkat96/mcimx7d/m4`目标（Target）

<a id="96b_meerkat96-96b_meerkat96/mcimx7d/m4-hw-features-panel"></a>

<a id="96b_meerkat96-96b_meerkat96/mcimx7d/m4-hw-features-memory"></a>

该开发板目标的片上存储容量：32 KiB RAM、32 KiB Flash。

<a id="96b_meerkat96-96b_meerkat96/mcimx7d/m4-hw-features-table"></a>

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
<td>ARM Cortex-M4 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P024_arm_cortex-m4.md#std-dtcompatible-arm-cortex-m4"><code>arm,cortex-m4</code></a></td>
</tr>
<tr>
<td rowspan="2">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>i.MX指令紧耦合存储器（ITCM / Instruction Tightly Coupled Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P014_nxp_imx-itcm.md#std-dtcompatible-nxp-imx-itcm"><code>nxp,imx-itcm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX数据紧耦合存储器（DTCM / Data Tightly Coupled Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L44">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P012_nxp_imx-dtcm.md#std-dtcompatible-nxp-imx-dtcm"><code>nxp,imx-dtcm</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L72">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L85">已禁用：6</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P030_nxp_imx-gpio.md#std-dtcompatible-nxp-imx-gpio"><code>nxp,imx-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>i.MX I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L263">已禁用：4</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P019_fsl_imx21-i2c.md#std-dtcompatible-fsl-imx21-i2c"><code>fsl,imx21-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">处理器间消息（IPM）</td>
<td>片上（On-Chip）</td>
<td>i.MX消息单元（Messaging Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L243">已启用：1</a>）</td>
<td><a href="../intercore_reference/P072_NXPiMX消息单元绑定.md#dtbinding-nxp-imx-mu"><code>nxp,imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/96boards/meerkat96/96b_meerkat96_mcimx7d_m4.dts?plain=1#L22">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>这个兼容性绑定（Compatible Binding）应应用于设备的<code>iomuxc</code>设备树源文件（DTS）节点。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L252">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P023_nxp_imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc"><code>nxp,imx-iomuxc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MCUX片上系统（SoC）的设备树（Devicetree）为该节点设置了<code>pinctrl</code>节点标签。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L257">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P024_nxp_imx7d-pinctrl.md#std-dtcompatible-nxp-imx7d-pinctrl"><code>nxp,imx7d-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>该驱动支持i.MX6SX和i.MX7D的脉宽调制（PWM）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L319">已禁用：4</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P017_fsl_imx27-pwm.md#std-dtcompatible-fsl-imx27-pwm"><code>fsl,imx27-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>iMX通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L166">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L177">已禁用：6</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P011_nxp_imx-uart.md#std-dtcompatible-nxp-imx-uart"><code>nxp,imx-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

#### 连接与输入输出（Connections and IOs）

96Boards Meerkat96开发板使用以下引脚复用控制器（Pinmux Controller）配置进行了测试。

<table>
<tr>
<th>开发板名称（Board Name）</th>
<th>SoC名称（SoC Name）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>UART_1接收数据（RXD）</td>
<td>UART1_TXD</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>UART_1发送数据（TXD）</td>
<td>UART1_RXD</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>LED_R1</td>
<td>GPIO1_IO04</td>
<td>LED0</td>
</tr>
<tr>
<td>LED_R2</td>
<td>GPIO1_IO05</td>
<td>LED1</td>
</tr>
<tr>
<td>LED_R3</td>
<td>GPIO1_IO06</td>
<td>LED2</td>
</tr>
<tr>
<td>LED_R4</td>
<td>GPIO1_IO07</td>
<td>LED3</td>
</tr>
</table>

<a id="system-clock"></a>

#### 系统时钟（System Clock）

M4内核配置为以200 MHz时钟频率运行。

<a id="serial-port"></a>

#### 串口（Serial Port）

iMX7D片上系统（SoC）提供7路UART。UART_1配置为控制台（Console），其余UART尚未使用或测试。

<a id="programming-and-debugging"></a>

### 烧录与调试（Programming and Debugging）

96Boards Meerkat96开发板没有供M4使用的四线SPI闪存（QSPI Flash），M4需要由A7内核启动。A7负责将M4应用的二进制文件加载到RAM，使M4进入复位状态，设置M4的程序计数器（Program Counter）和栈指针（Stack Pointer），再解除M4复位。A7可以在引导加载程序（Bootloader）阶段完成这些步骤，也可以在Linux系统启动后执行。

M4最多可以使用5种不同的RAM。A7和M4的存储器映射（Memory Mapping）如下：

<table>
<tr>
<th>区域（Region）</th>
<th>Cortex-A7</th>
<th>Cortex-M4（系统总线 / System Bus）</th>
<th>Cortex-M4（代码总线 / Code Bus）</th>
<th>大小（Size）</th>
</tr>
<tr>
<td>双倍数据率存储器（DDR）</td>
<td>0x80000000-0xFFFFFFFF</td>
<td>0x80000000-0xDFFFFFFF</td>
<td>0x10000000-0x1FFEFFFF</td>
<td>2048 MB（M4可用容量较少）</td>
</tr>
<tr>
<td>OCRAM</td>
<td>0x00900000-0x0091FFFF</td>
<td>0x20200000-0x2021FFFF</td>
<td>0x00900000-0x0091FFFF</td>
<td>128KB</td>
</tr>
<tr>
<td>TCMU</td>
<td>0x00800000-0x00807FFF</td>
<td>0x20000000-0x20007FFF</td>
<td></td>
<td>32KB</td>
</tr>
<tr>
<td>TCML</td>
<td>0x007F8000-0x007FFFFF</td>
<td></td>
<td>0x1FFF8000-0x1FFFFFFF</td>
<td>32KB</td>
</tr>
<tr>
<td>OCRAM_S</td>
<td>0x00180000-0x00187FFF</td>
<td>0x20180000-0x20187FFF</td>
<td>0x00000000-0x00007FFF</td>
<td>32KB</td>
</tr>
<tr>
<td>四线SPI闪存（QSPI Flash）</td>
<td></td>
<td></td>
<td>0x08000000-0x0BFFFFFF</td>
<td>64MB</td>
</tr>
</table>

有关存储器映射（Memory Mapping）的更多信息，请参阅[i.MX 7 Dual参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=IMX7DRM)的2.1.2和2.1.3节，以及[Toradex Wiki](https://developer.toradex.com/knowledge-base/freertos-on-the-cortex-m4-of-a-colibri-imx7#Memory_areas)。

编译时必须选择要使用的RAM。在[boards/96boards/meerkat96/96b_meerkat96_mcimx7d_m4.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/96boards/meerkat96/96b_meerkat96_mcimx7d_m4.dts)文件中，通过`zephyr,flash`属性（当`CONFIG_XIP=y`时）和`zephyr,sram`属性进行配置。可用配置如下：

```text
"zephyr,flash"
- &ddr_code
- &tcml_code
- &ocram_code
- &ocram_s_code
- &ocram_pxp_code
- &ocram_epdc_code

"zephyr,sram"
- &ddr_sys
- &tcmu_sys
- &ocram_sys
- &ocram_s_sys
- &ocram_pxp_sys
- &ocram_epdc_sys
```

下面说明如何从A7使用U-Boot将Zephyr加载到M4并运行。

将编译得到的`zephyr.bin`复制到SD卡的第一个FAT分区，然后将卡插入开发板。上电并中止U-Boot自动执行。设置U-Boot环境变量，从Zephyr编译时配置的相应存储器运行`zephyr.bin`：

```text
setenv bootm4 'fatload mmc 0:1 $m4addr $m4fw && dcache flush && bootaux $m4addr'
# TCML
setenv m4tcml 'setenv m4fw zephyr.bin; setenv m4addr 0x007F8000'
setenv bootm4tcml 'run m4tcml && run bootm4'
run bootm4tcml
# TCMU
setenv m4tcmu 'setenv m4fw zephyr.bin; setenv m4addr 0x00800000'
setenv bootm4tcmu 'run m4tcmu && run bootm4'
run bootm4tcmu
# OCRAM
setenv m4ocram 'setenv m4fw zephyr.bin; setenv m4addr 0x00900000'
setenv bootm4ocram 'run m4ocram && run bootm4'
run bootm4ocram
# OCRAM_S
setenv m4ocrams 'setenv m4fw zephyr.bin; setenv m4addr 0x00180000'
setenv bootm4ocrams 'run m4ocrams && run bootm4'
run bootm4ocrams
# DDR
setenv m4ddr 'setenv m4fw zephyr.bin; setenv m4addr 0x80000000'
setenv bootm4ddr 'run m4ddr && run bootm4'
run bootm4ddr
```

<a id="debugging"></a>

#### 调试（Debugging）

将外部J-Link JTAG调试器连接到J4调试接口，即可调试96Boards Meerkat96开发板。随后下载并安装[J-Link工具（Tools）](https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack)和NXP的`iMX7D_Connect_CortexM4.JLinkScript`脚本。（[NXP iMX7D Connect CortexM4.JLinkScript脚本](https://wiki.segger.com/images/8/86/NXP_iMX7D_Connect_CortexM4.JLinkScript)）

要使用J-Link运行Zephyr二进制程序，请创建以下脚本，从`zephyr.bin`获取程序计数器（Program Counter）和栈指针（Stack Pointer）。

`get-pc-sp.sh`：原文此处显示为`.. code-block:: console`。

> `#!/bin/sh`
>
> `firmware=$1`
>
> `pc=$(od -An -N 8 -t x4 $firmware | awk ‘{print $2;}’)`
>
> `sp=$(od -An -N 8 -t x4 $firmware | awk ‘{print $1;}’)`
>
> `echo pc=$pc`
>
> `echo sp=$sp`

从固件二进制文件获取栈指针（SP）和程序计数器（PC）：`./get-pc-sp.sh zephyr.bin`。原文此处显示为`.. code-block:: console`。

> `pc=00900f01`
>
> `sp=00905020`

将J-Link连接到开发板和PC，然后运行J-Link命令行工具：

```text
/usr/bin/JLinkExe -device Cortex-M4 -if JTAG -speed 4000 -autoconnect 1 -jtagconf -1,-1 -jlinkscriptfile iMX7D_Connect_CortexM4.JLinkScript
```

运行`zephyr.bin`需要执行以下步骤：


1. 使M4内核进入复位状态。
2. 将二进制文件加载到相应地址（TMCL、TCMU、OCRAM、OCRAM_S或DDR）。
3. 设置程序计数器（PC / Program Counter）。
4. 设置栈指针（SP / Stack Pointer）。
5. 解除M4内核的复位状态。

在J-Link Commander中执行以下命令：

```text
w4 0x3039000C 0xAC
loadfile zephyr.bin,0x00900000
w4 0x00180000 00900f01
w4 0x00180004 00905020
w4 0x3039000C 0xAA
```

通过这些机制，可以按常规方式为`96b_meerkat96`开发板配置构建和调试应用；详见[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)和[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)。

<a id="references"></a>

#### 参考资料（References）


- [在i.MX 6SoloX和i.MX 7Dual/7Solo应用处理器上从Linux向Cortex-M4加载代码（Loading Code on Cortex-M4 from Linux）](https://www.nxp.com/docs/en/application-note/AN5317.pdf)
- [J-Link iMX7D操作说明（Instructions）](https://wiki.segger.com/IMX7D)

## 译注

原文将部分存储器归入“Internal RAM”，并在步骤中将TCML写作TMCL；此处保留原始分类、名称和容量。原文的get-pc-sp.sh示例存在reStructuredText代码指令未生效、awk使用弯引号等排版问题，译文保留这些原字符并恢复可辨认的行分隔，不将其冒充已验证可直接执行的脚本。原例中的/usr/bin/JLinkExe是Linux程序路径，不是作者的仓库绝对位置。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [freertos-on-the-cortex-m4-of-a-colibri-imx7](https://developer.toradex.com/knowledge-base/freertos-on-the-cortex-m4-of-a-colibri-imx7#Memory_areas)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1010)>。
- [AN5317.pdf](https://www.nxp.com/docs/en/application-note/AN5317.pdf)：HTTP Error 404: Not Found。
- [IMX7DCEC.pdf](https://www.nxp.com/docs/en/data-sheet/IMX7DCEC.pdf)：HTTP Error 404: Not Found。
- [i.mx-7-processors:IMX7-SERIES?fsrch=1&sr=1&pageNum=1](https://www.nxp.com/products/processors-and-microcontrollers/applications-processors/i.mx-applications-processors/i.mx-7-processors:IMX7-SERIES?fsrch=1&sr=1&pageNum=1)：HTTP Error 404: Not Found。
- [Download?colCode=IMX7DRM](https://www.nxp.com/webapp/Download?colCode=IMX7DRM)：HTTP Error 404: Not Found。
- [](https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack)：页面可访问，但未确认目标片段。

---

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_Neonkey.md)
