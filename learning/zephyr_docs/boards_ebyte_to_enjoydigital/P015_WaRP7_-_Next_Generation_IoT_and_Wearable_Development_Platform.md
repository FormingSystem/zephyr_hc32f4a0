---
id: learning.zephyr-docs.boards-ebyte-to-enjoydigital.page-15
title: WaRP7 - Next Generation IoT and Wearable Development Platform
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/element14/warp7/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="warp7"></a>

# 第15章\_WaRP7——下一代物联网与可穿戴开发平台（Next Generation IoT and Wearable Development Platform）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/element14/warp7/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id2"></a>

[![官方原图：../../../../_images/warp7.jpg](images/warp7.jpg)](images/warp7.jpg)

WaRP7——下一代物联网与可穿戴开发平台（Next Generation IoT and Wearable Development Platform）

名称（Name）：

`warp7`

厂商（Vendor）：

[Element14，Premier Farnell旗下公司](https://docs.zephyrproject.org/latest/boards/index.html#vendor=element14)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mcimx7d](https://docs.zephyrproject.org/latest/boards/index.html#soc=mcimx7d)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/element14/warp7/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

i.MX7S SoC是一款异构多核处理器（Hybrid Multi-Core Processor），由一个Cortex-A7内核及一个Cortex-M4内核组成。Zephyr已移植到M4内核运行；原文表示后续版本还将通过RPMsg与运行Linux的A7内核通信。

<a id="hardware"></a>

## 硬件（Hardware）

WaRP7平台由CPU板及I/O板组成。

<a id="warp7-io-board"></a>

### WaRP7 I/O板（IO Board）


- 六轴加速度计与磁力计：NXP FXOS8700CQ，I2C4接口
- 三轴陀螺仪（Gyroscope）：NXP FXAS21002C，I2C4接口
- 高度计（Altimeter）：NXP MPL3115A2，I2C4接口
- NXP NTAG NT3H1101，I2C2接口
- 音频编解码器（Audio Codec）：NXP SGTL5000，I2C4及SAI1接口
- S1：复位按键，POR_B信号
- S2：用户定义按键，ENET1_RD1／GPIO7_IO1信号
- S3：开／关，MX7_ONOFF信号
- 板对板连接器，34个可配置引脚
- mikroBUS扩展连接器
- 10针探针式JTAG连接器（Needle JTAG Connector）
- 调试USB引出两个UART：UART1用于A7，UART2用于M4
- 单通道MIPI显示串行接口（DSI）连接器
- LCD触摸连接器，I2C2接口
- 音频插孔：麦克风及立体声耳机

<a id="warp7-cpu-board"></a>

### WaRP7 CPU板（CPU Board）


- i.MX7 Solo CPU，包含一个800 MHz Cortex-A7内核及一个200 MHz Cortex-M4内核
- 存储器（Memory）


  - A7 RAM：4 GB，Kingston 08EMCP04，数值与单位依原文保留
  - M4 RAM：三个32 KB区域TCML、TCMU及OCRAM_S，一个128 KB OCRAM区域，以及一个256 MB DDR区域
  - A7闪存：8 GB eMMC，Kingston 08EMCP04
- 多媒体（Multimedia）


  - 单通道MIPI摄像头串行接口（CSI）连接器，带500万像素OV5640摄像头模块，I2C2接口
- 连接能力（Connectivity）


  - 板对板连接器，34个可配置引脚
  - Micro USB 2.0 OTG连接器，USB_OTG1接口
  - 村田（Murata）Type 1DX模块，支持IEEE 802.11b/g/n Wi-Fi及Bluetooth 4.1加增强数据速率（EDR）；使用SD1、UART3和SAI2接口
- 锂离子／锂聚合物电池充电器：NXP BC3770，I2C1接口
- 电源管理芯片（PMIC）：NXP PF3000，I2C1接口

关于i.MX7 SoC与WaRP7的更多信息，见以下资料：


- [i.MX 7系列网站（Series Website）](https://www.nxp.com/products/processors-and-microcontrollers/applications-processors/i.mx-applications-processors/i.mx-7-processors:IMX7-SERIES?fsrch=1&sr=1&pageNum=1)
- [i.MX 7 Solo数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/IMX7SCEC.pdf)
- [i.MX 7 Solo参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=IMX7SRM)
- [WaRP7网站](https://www.element14.com/warp7)
- [WaRP7快速入门指南（Quick Start Guide）](https://www.nxp.com/docs/en/supporting-information/WARP7-LEAFLET-QSG.pdf)
- [WaRP7用户指南（User Guide）](https://github.com/WaRP7/WaRP7-User-Guide/releases/download/v1.3/User_Guide_Manual_v1-3.pdf)
- [WaRP7 GitHub仓库](https://github.com/WaRP7)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`warp7`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="warp7-hw-features"></a>

<a id="warp7-warp7/mcimx7d/m4-hw-features-section"></a>

#### `warp7/mcimx7d/m4`目标（Target）

<a id="warp7-warp7/mcimx7d/m4-hw-features-panel"></a>

<a id="warp7-warp7/mcimx7d/m4-hw-features-memory"></a>

该开发板目标的片上存储容量：32 KiB RAM、32 KiB Flash。

<a id="warp7-warp7/mcimx7d/m4-hw-features-table"></a>

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
<td>i.MX通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L150">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L72">已禁用：6</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P030_nxp_imx-gpio.md#std-dtcompatible-nxp-imx-gpio"><code>nxp,imx-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>i.MX I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L305">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L263">已禁用：3</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P019_fsl_imx21-i2c.md#std-dtcompatible-fsl-imx21-i2c"><code>fsl,imx21-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/element14/warp7/warp7_mcimx7d_m4.dts?plain=1#L30">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
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
<td rowspan="2">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>FXOS8700六轴加速度计／磁力计传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/element14/warp7/warp7_mcimx7d_m4.dts?plain=1#L81">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P052_nxp_fxos8700.md#std-dtcompatible-nxp-fxos8700"><code>nxp,fxos8700</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>FXAS21002三轴陀螺仪传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/element14/warp7/warp7_mcimx7d_m4.dts?plain=1#L87">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P050_nxp_fxas21002.md#std-dtcompatible-nxp-fxas21002"><code>nxp,fxas21002</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>iMX通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L177">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx7d_m4.dtsi?plain=1#L166">已禁用：5</a>）</td>
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

### 连接与输入输出（Connections and IOs）

原文说明，WaRP7开发板使用以下引脚复用（Pinmux）控制器配置进行了测试。

<table>
<tr>
<th>开发板名称（Board Name）</th>
<th>SoC名称（SoC Name）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>FT_TX2</td>
<td>UART2_TXD</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>FT_RX2</td>
<td>UART2_RXD</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>MKBUS_TX</td>
<td>UART6_TXD</td>
<td>通用异步收发器（UART）</td>
</tr>
<tr>
<td>MKBUS_RX</td>
<td>UART6_RXD</td>
<td>通用异步收发器（UART）</td>
</tr>
<tr>
<td>S2</td>
<td>ENET1_RD1/GPIO7_IO1</td>
<td>SW0</td>
</tr>
<tr>
<td>I2C4_SDA</td>
<td>I2C4_SDA</td>
<td><code>I2C / FXOS8700 / FXAS21002</code></td>
</tr>
<tr>
<td>I2C4_SCL</td>
<td>I2C4_SCL</td>
<td><code>I2C / FXOS8700 / FXAS21002</code></td>
</tr>
<tr>
<td>SENSOR_INT_B</td>
<td>ENET1_RD0/GPIO7_IO0</td>
<td><code>FXOS8700 INT1 / FXAS21002 INT1</code></td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

M4内核配置为以200 MHz时钟频率运行。

<a id="serial-port"></a>

### 串口（Serial Port）

i.MX7S SoC具有七路UART，其中UART2配置为控制台，UART6用于mikroBUS连接器。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`warp7`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

WaRP7没有供M4使用的QSPI闪存，M4必须由A7启动。A7负责将M4应用二进制程序加载到RAM，使M4保持复位，设置M4的程序计数器（PC）及栈指针（SP），再释放复位。A7可在引导加载程序阶段执行这些步骤，也可在Linux系统启动后执行。

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
<td>片上RAM（OCRAM）</td>
<td>0x00900000-0x0091FFFF</td>
<td>0x20200000-0x2021FFFF</td>
<td>0x00900000-0x0091FFFF</td>
<td>128KB</td>
</tr>
<tr>
<td>高地址紧耦合存储器（TCMU）</td>
<td>0x00800000-0x00807FFF</td>
<td>0x20000000-0x20007FFF</td>
<td></td>
<td>32KB</td>
</tr>
<tr>
<td>低地址紧耦合存储器（TCML）</td>
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

<a id="references"></a>

### 参考资料（References）


- i.MX 7 Solo参考手册第182页起，第2.1.2及2.1.3节（[i.MX 7 Solo参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=IMX7SRM)）
- [Toradex维基（Wiki）](https://developer.toradex.com/knowledge-base/freertos-on-the-cortex-m4-of-a-colibri-imx7#Memory_areas)

编译时必须选择使用哪一块RAM。在[boards/element14/warp7/warp7_mcimx7d_m4.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/element14/warp7/warp7_mcimx7d_m4.dts)中，通过`zephyr,flash`（`CONFIG_XIP=y`时）及`zephyr,sram`属性配置。可用配置如下：

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

将两个Micro USB接口都连接到计算机。其中一个USB接口提供两个USB串口：第一个是A7控制台，第二个是M4上的Zephyr控制台，两者均配置为115200 8N1。另一个USB接口给CPU板及I/O板供电，并连接i.MX7S的USB OTG接口。

平台上电后，中止A7内核上的U-Boot执行，在U-Boot提示符下运行`ums 0 mmc 0`，将eMMC呈现为大容量存储设备。将编译生成的`zephyr.bin`复制到第一个FAT分区，然后在U-Boot提示符下按`Ctrl+C`，移除计算机上挂载的设备。设置U-Boot环境变量，并从Zephyr编译配置所指定的相应存储器运行`zephyr.bin`：

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

### 调试（Debugging）

下载并安装[J-Link Tools](https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack)及[NXP iMX7D Connect CortexM4.JLinkScript](https://wiki.segger.com/images/8/86/NXP_iMX7D_Connect_CortexM4.JLinkScript)。

使用J-Link运行Zephyr二进制程序时，创建以下脚本，从`zephyr.bin`获取程序计数器（PC）及栈指针（SP）。

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
/usr/bin/JLinkExe -device Cortex-M4 -if JTAG \
   -speed 4000 -autoconnect 1 -jtagconf -1,-1 \
   -jlinkscriptfile iMX7D_Connect_CortexM4.JLinkScript
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

通过这些机制，可按通常方式构建及调试`warp7`配置的应用，详情见[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)及[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)。

<a id="id1"></a>

### 参考资料（References）


- [在i.MX 6SoloX和i.MX 7Dual/7Solo应用处理器上从Linux向Cortex-M4加载代码（Loading Code on Cortex-M4 from Linux）](https://www.nxp.com/docs/en/application-note/AN5317.pdf)
- [J-Link iMX7D操作说明（Instructions）](https://wiki.segger.com/IMX7D)

## 译注

原文写A7具有4GB RAM、板卡使用i.MX7S，而Zephyr目标名为warp7/mcimx7d/m4；均按各自位置保留。M4不能自行从独立QSPI启动，须由A7加载并设置PC／SP。RPMsg的后续支持表述是上游原文的时间语境。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [freertos-on-the-cortex-m4-of-a-colibri-imx7](https://developer.toradex.com/knowledge-base/freertos-on-the-cortex-m4-of-a-colibri-imx7#Memory_areas)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1010)>。
- [warp7](https://www.element14.com/warp7)：The read operation timed out。
- [AN5317.pdf](https://www.nxp.com/docs/en/application-note/AN5317.pdf)：HTTP Error 404: Not Found。
- [IMX7SCEC.pdf](https://www.nxp.com/docs/en/data-sheet/IMX7SCEC.pdf)：HTTP Error 404: Not Found。
- [WARP7-LEAFLET-QSG.pdf](https://www.nxp.com/docs/en/supporting-information/WARP7-LEAFLET-QSG.pdf)：HTTP Error 404: Not Found。
- [i.mx-7-processors:IMX7-SERIES?fsrch=1&sr=1&pageNum=1](https://www.nxp.com/products/processors-and-microcontrollers/applications-processors/i.mx-applications-processors/i.mx-7-processors:IMX7-SERIES?fsrch=1&sr=1&pageNum=1)：HTTP Error 404: Not Found。
- [Download?colCode=IMX7SRM](https://www.nxp.com/webapp/Download?colCode=IMX7SRM)：HTTP Error 404: Not Found。
- [](https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack)：页面可访问，但未确认目标片段。

---

[上一章](P014_Element_14.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P016_Guangdong_Embedsky_Technology_Co._Ltd.md)
