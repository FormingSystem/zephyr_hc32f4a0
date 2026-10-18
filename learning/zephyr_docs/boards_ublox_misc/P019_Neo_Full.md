---
id: learning.zephyr-docs.boards-ublox-misc.page-19
title: Neo Full
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/udoo/udoo_neo_full/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="udoo_neo_full"></a>

# 第19章\_Neo Full

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/udoo/udoo_neo_full/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id2"></a>

[![官方原图：../../../../_images/udoo_neo_full_mcimx6x_m4.jpg](images/udoo_neo_full_mcimx6x_m4.jpg)](images/udoo_neo_full_mcimx6x_m4.jpg)

Neo Full

名称（Name）：

`udoo_neo_full`

厂商（Vendor）：

[Udoo](https://docs.zephyrproject.org/latest/boards/index.html#vendor=udoo)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mcimx6x](https://docs.zephyrproject.org/latest/boards/index.html#soc=mcimx6x)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/udoo/udoo_neo_full/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

UDOO Neo Full是开源、兼容Arduino Uno的单板计算机，采用NXP i.MX 6SoloX异构多核处理器，包括最高1 GHz的ARM Cortex-A9及最高227 MHz的Cortex-M4，兼顾性能与实时响应。此Zephyr移植仅运行于M4，原文计划未来通过OpenAMP与运行Linux的A9通信。

<a id="hardware"></a>

## 硬件（Hardware）


- MCIMX6X MCU：单个1 GHz Cortex-A9及单个227 MHz Cortex-M4内核
- 存储器（Memory）


  - 1 GB随机存取存储器（RAM）
  - 128 KB片上RAM（OCRAM）
  - 256 KB二级缓存（L2 Cache），可改为OCRAM
  - 16 KB OCRAM_S
  - 32 KB TCML
  - 32 KB TCMU
  - 32 KB CAAM安全RAM
- A9启动设备（Boot Devices）


  - NOR闪存
  - NAND闪存
  - OneNAND闪存
  - SD/MMC
  - 串行I2C／SPI NOR闪存及EEPROM
  - 四线SPI（QuadSPI，QSPI）闪存
- 显示（Display）


  - Micro HDMI连接器
  - 低压差分信号（LVDS）显示接口
  - 触摸接口，I2C信号
- 多媒体（Multimedia）


  - 集成二维／三维图形控制器
  - 8位并行模拟摄像头接口，支持NTSC及PAL
  - HDMI音频发送器
  - S/PDIF
  - 集成电路间音频总线（I2S）
- 连接能力（Connectivity）


  - USB 2.0 Type-A端口
  - USB OTG，Micro-AB连接器
  - 10/100 Mbit/s以太网物理层收发器（Ethernet PHY）
  - Wi-Fi 802.11 b/g/n
  - 蓝牙4.0低功耗（Bluetooth 4.0 Low Energy）
  - 3路UART端口
  - 2路控制器局域网（CAN Bus）接口
  - 8路脉宽调制（PWM）信号
  - 3路I2C接口
  - 1路SPI接口
  - 6路可复用信号
  - 32路GPIO，A9侧
  - 22路GPIO，M4侧
- 其他（Other）


  - MicroSD卡槽，8位SDIO接口
  - 绿色电源状态LED
  - 2个用户LED，红色和橙色
- 电源（Power）


  - 5 V直流Micro USB供电
  - 6—15 V直流电源插孔
  - 实时时钟（RTC）电池连接器
- 调试（Debug）


  - 14引脚JTAG连接器焊盘
- 传感器（Sensor）


  - 三轴加速度计（3-Axis Accelerometer）
  - 三轴磁力计（Magnetometer）
  - 三轴数字陀螺仪（Digital Gyroscope）
  - 1个卡扣式传感器I2C连接器（Sensor Snap-In）
- 扩展端口（Expansion Port）


  - Arduino接口（Interface）

MCIMX6X SoC及UDOO Neo Full的更多信息见：


- <a id="id18"></a>

  [NXP i.MX 6SoloX网站](https://www.nxp.com/products/processors-and-microcontrollers/applications-processors/i.mx-applications-processors/i.mx-6-processors/i.mx-6solox-processors-heterogeneous-processing-with-arm-cortex-a9-and-cortex-m4-cores:i.MX6SX)[注8](#id17)
- <a id="id20"></a>

  [NXP i.MX 6SoloX数据手册](https://www.nxp.com/docs/en/data-sheet/IMX6SXCEC.pdf)[注9](#id19)
- <a id="id22"></a>

  [NXP i.MX 6SoloX参考手册](https://www.nxp.com/docs/en/reference-manual/IMX6SXRM.pdf)[注10](#id21)
- <a id="id4"></a>

  [UDOO Neo网站](https://www.udoo.org/udoo-neo/)[注1](#id3)
- <a id="id6"></a>

  [UDOO Neo入门指南](https://www.udoo.org/get-started-neo/)[注2](#id5)
- <a id="id8"></a>

  [UDOO Neo文档](https://www.udoo.org/docs-neo)[注3](#id7)
- <a id="id10"></a>

  [UDOO Neo数据手册](https://www.udoo.org/download/files/datasheets/datasheet_udoo_neo.pdf)[注4](#id9)
- <a id="id12"></a>

  [UDOO Neo原理图](https://www.udoo.org/download/files/schematics/UDOO_NEO_schematics.pdf)[注5](#id11)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`udoo_neo_full`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="udoo_neo_full-hw-features"></a>

<a id="udoo_neo_full-udoo_neo_full/mcimx6x/m4-hw-features-section"></a>

#### `udoo_neo_full/mcimx6x/m4`目标（Target）

<a id="udoo_neo_full-udoo_neo_full/mcimx6x/m4-hw-features-panel"></a>

<a id="udoo_neo_full-udoo_neo_full/mcimx6x/m4-hw-features-memory"></a>

该开发板目标的片上存储容量：32 KiB RAM、512 KiB Flash。

<a id="udoo_neo_full-udoo_neo_full/mcimx6x/m4-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="2">中央处理器（CPU）</td>
<td>片上（On-Chip）</td>
<td>ARM Cortex-A9处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L19">已禁用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P016_arm_cortex-a9.md#std-dtcompatible-arm-cortex-a9"><code>arm,cortex-a9</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>VF610模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L436">已禁用：2</a>）</td>
<td><a href="../hardware/P855_NXPVF610模数转换器绑定.md#dtbinding-nxp-vf610-adc"><code>nxp,vf610-adc</code></a></td>
</tr>
<tr>
<td rowspan="3">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>i.MX增强型周期中断定时器（Enhanced Periodic Interrupt Timer，EPIT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L240">已启用：2</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P013_nxp_imx-epit.md#std-dtcompatible-nxp-imx-epit"><code>nxp,imx-epit</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX指令紧耦合存储器（ITCM / Instruction Tightly Coupled Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P014_nxp_imx-itcm.md#std-dtcompatible-nxp-imx-itcm"><code>nxp,imx-itcm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX数据紧耦合存储器（DTCM / Data Tightly Coupled Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P012_nxp_imx-dtcm.md#std-dtcompatible-nxp-imx-dtcm"><code>nxp,imx-dtcm</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>i.MX通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L177">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L138">已禁用：4</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P030_nxp_imx-gpio.md#std-dtcompatible-nxp-imx-gpio"><code>nxp,imx-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>i.MX I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L276">已禁用：4</a>）</td>
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
<td>i.MX消息单元（Messaging Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L229">已启用：1</a>）</td>
<td><a href="../intercore_reference/P072_NXPiMX消息单元绑定.md#dtbinding-nxp-imx-mu"><code>nxp,imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/udoo/udoo_neo_full/udoo_neo_full_mcimx6x_m4.dts?plain=1#L45">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L62">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>这个兼容性绑定（Compatible Binding）应应用于设备的<code>iomuxc</code>设备树源文件（DTS）节点。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L252">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P023_nxp_imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc"><code>nxp,imx-iomuxc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>该节点在MCUX RT SoC设备树中设置了pinctrl节点标签（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L257">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P012_nxp_mcux-rt-pinctrl.md#std-dtcompatible-nxp-mcux-rt-pinctrl"><code>nxp,mcux-rt-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>该驱动支持i.MX6SX和i.MX7D的脉宽调制（PWM）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L332">已禁用：8</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P017_fsl_imx27-pwm.md#std-dtcompatible-fsl-imx27-pwm"><code>fsl,imx27-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>iMX通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L116">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imx/nxp_imx6sx_m4.dtsi?plain=1#L72">已禁用：5</a>）</td>
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

UDOO Neo Full已按原文所列的以下引脚复用控制器配置测试。

<table>
<tr>
<th>开发板名称（Board Name）</th>
<th>SoC名称（SoC Name）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>J4接收（RX）</td>
<td>UART5_RX_DATA</td>
<td>UART控制台（UART Console）</td>
</tr>
<tr>
<td>J4发送（TX）</td>
<td>UART5_TX_DATA</td>
<td>UART控制台（UART Console）</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

MCIMX6X使用板上24 MHz外部振荡器及片上锁相环（PLL）生成内核时钟。M4的PLL设置由A9上运行的代码完成。

<a id="serial-port"></a>

### 串口（Serial Port）

MCIMX6X具有六路UART。UART5配置给M4，其余由A9使用或未启用。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`udoo_neo_full`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

M4没有闪存，上电复位时也未提供时钟，必须由A9启动。A9负责将M4应用二进制加载到RAM，使M4处于复位状态，设置程序计数器（Program Counter）及栈指针（Stack Pointer），再解除复位。这些步骤可由引导加载器执行，也可在Linux启动后执行。

M4可使用最多五种RAM；安全RAM等其他存储尚未在Zephyr中实现。A9和M4的存储映射如下：

<table>
<tr>
<th>区域（Region）</th>
<th>Cortex-A9</th>
<th>Cortex-M4</th>
<th>大小（Size）</th>
</tr>
<tr>
<td>低地址紧耦合存储器（TCML）</td>
<td>0x007F8000-0x007FFFFF</td>
<td>0x1FFF8000-0x1FFFFFFF</td>
<td>32 KB</td>
</tr>
<tr>
<td>高地址紧耦合存储器（TCMU）</td>
<td>0x00800000-0x00807FFF</td>
<td>0x20000000-0x20007FFF</td>
<td>32 KB</td>
</tr>
<tr>
<td>OCRAM_S</td>
<td>0x008F8000-0x008FBFFF</td>
<td>0x208F8000-0x208FBFFF</td>
<td>16 KB</td>
</tr>
<tr>
<td>片上RAM（OCRAM）</td>
<td>0x00900000-0x0091FFFF</td>
<td>0x20900000-0x2091FFFF</td>
<td>128 KB</td>
</tr>
<tr>
<td>双倍数据率存储器（DDR）</td>
<td>0x80000000-0xFFFFFFFF</td>
<td>0x80000000-0xDFFFFFFF</td>
<td>2048 MB，其中M4可用1536 MB</td>
</tr>
</table>

<a id="references"></a>

### 参考资料（References）


- <a id="id23"></a>

  [NXP i.MX 6SoloX参考手册](https://www.nxp.com/docs/en/reference-manual/IMX6SXRM.pdf)[注10](#id21)第2章：存储器映射（Memory Maps）

编译时须选择使用哪种RAM，配置文件为[boards/udoo/udoo_neo_full/udoo_neo_full_mcimx6x_m4.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/udoo/udoo_neo_full/udoo_neo_full_mcimx6x_m4.dts)。

若要将代码放入某存储区域的子区域，常见于DDR场景，选择zephyr,flash=&flash，并用DT_FLASH_SIZE设置区域大小、DT_FLASH_ADDR设置起始地址。

若要将数据放入某存储区域的子区域，常见于DDR场景，选择zephyr,sram = &sram。

否则，将zephyr,flash及／或zephyr,sram设为以下预定义区域之一：

```text
"zephyr,flash"
- &tcml
- &ocram_s
- &ocram
- &ddr

"zephyr,sram"
- &tcmu
- &ocram_s
- &ocram
- &ddr
```

下面介绍如何使用A9上的Linux用户态应用加载并运行M4上的Zephyr。

<a id="id14"></a>

UDOOBuntu Linux提供[udooneo-m4uploader](https://github.com/ektor5/udooneo-m4uploader)工具[注6](#id13)，但其用途是加载UDOO Neo的类Arduino程序（Sketch），通常不能直接用于Zephyr。原因是该工具与M4程序通过硬编码共享内存地址交换状态：工具写入标志，M4程序读到后安全退出并回写状态；工具随后加载新应用，再读取共享状态确认启动。这套特定机制未在Zephyr中实现，但需要配合A9上的UDOOBuntu使用时，Zephyr应用可以自行实现。udooneo-uploader还会调用mqx_upload_on_m4SoloX，可直接用后者加载Zephyr。将Zephyr二进制复制到Linux文件系统，然后以root用户执行：

```text
mqx_upload_on_m4SoloX zephyr.bin
```

若出现以下输出，表示mqx_upload_on_m4SoloX无法读取已停止应用的状态。先前应用不是UDOO Neo类Arduino程序、未参与共享内存通信时，这是预期情况：

```text
UDOONeo - mqx_upload_on_m4SoloX 1.1.0
UDOONeo - Waiting M4 Stop, m4TraceFlags: 00000000
UDOONeo - Waiting M4 Stop, m4TraceFlags: 00000000
UDOONeo - Waiting M4 Stop, m4TraceFlags: 00000000
UDOONeo - Waiting M4 Stop, m4TraceFlags: 00000000
UDOONeo - Failed to Stop M4 sketch: reboot system !
```

此时mqx_upload_on_m4SoloX已经复位跟踪标志，再次调用应能成功，可能出现以下输出：

```text
UDOONeo - mqx_upload_on_m4SoloX 1.1.0
UDOONeo - FILENAME = zephyr.bin; loadaddr = 0x84000000
UDOONeo - start - end (0x84000000 - 0x84080000)
UDOONeo - Waiting M4 Run, m4TraceFlags: 000001E0
UDOONeo - M4 sketch is running
```

若工具无法读取M4应用已启动的状态标志，也可能出现以下输出。原文说明可忽略，因为应用应已运行，只是工具未能获知：

```text
UDOONeo - mqx_upload_on_m4SoloX 1.1.0
UDOONeo - FILENAME = zephyr.bin; loadaddr = 0x84000000
UDOONeo - start - end (0x84000000 - 0x84080000)
UDOONeo - Waiting M4 Run, m4TraceFlags: 00000000
UDOONeo - Waiting M4 Run, m4TraceFlags: 00000000
UDOONeo - Waiting M4 Run, m4TraceFlags: 00000000
UDOONeo - Waiting M4 Run, m4TraceFlags: 00000000
UDOONeo - Failed to Start M4 sketch: reboot system !
```

栈指针与程序计数器的值从二进制中读取。二进制加载地址由程序计数器向下对齐到64 KB计算，也可作为第二个命令行参数显式提供：

```text
mqx_upload_on_m4SoloX zephyr.bin 0x84000000
```

如果目标存储在A9与M4上的映射不同，必须显式提供地址。原文此处称从二进制栈指针计算的地址会出错，与前文按程序计数器计算的说法不同，保留此差异。

也可修改mqx_upload_on_m4SoloX源代码，取消与M4应用的共享内存通信。

<a id="id16"></a>

还可使用[imx-m4fwloader](https://github.com/codeauroraforum/imx-m4fwloader)工具[注7](#id15)加载M4应用。

UDOOBuntu中的一种方式是将二进制复制为Linux文件系统中的/var/opt/m4/m4last.fw，下次启动时Das U-Boot会从此处加载。

另一种方式是直接使用Das U-Boot加载代码。

<a id="debugging"></a>

### 调试（Debugging）

UDOO Neo Full提供14引脚JTAG连接器焊盘。原文说明M4上的Zephyr应用仅通过观察UART控制台输出测试。

<a id="id1"></a>

### 参考资料（References）

<a id="id3"></a>

〔[1](#id4)〕 [https://www.udoo.org/udoo-neo/](https://www.udoo.org/udoo-neo/)

<a id="id5"></a>

〔[2](#id6)〕 [https://www.udoo.org/get-started-neo/](https://www.udoo.org/get-started-neo/)

<a id="id7"></a>

〔[3](#id8)〕 [https://www.udoo.org/docs-neo](https://www.udoo.org/docs-neo)

<a id="id9"></a>

〔[4](#id10)〕 [https://www.udoo.org/download/files/datasheets/datasheet_udoo_neo.pdf](https://www.udoo.org/download/files/datasheets/datasheet_udoo_neo.pdf)

<a id="id11"></a>

〔[5](#id12)〕 [https://www.udoo.org/download/files/schematics/UDOO_NEO_schematics.pdf](https://www.udoo.org/download/files/schematics/UDOO_NEO_schematics.pdf)

<a id="id13"></a>

〔[6](#id14)〕 [https://github.com/ektor5/udooneo-m4uploader](https://github.com/ektor5/udooneo-m4uploader)

<a id="id15"></a>

〔[7](#id16)〕 [https://github.com/codeauroraforum/imx-m4fwloader](https://github.com/codeauroraforum/imx-m4fwloader)

<a id="id17"></a>

〔[8](#id18)〕 [https://www.nxp.com/products/processors-and-microcontrollers/applications-processors/i.mx-applications-processors/i.mx-6-processors/i.mx-6solox-processors-heterogeneous-processing-with-arm-cortex-a9-and-cortex-m4-cores:i.MX6SX](https://www.nxp.com/products/processors-and-microcontrollers/applications-processors/i.mx-applications-processors/i.mx-6-processors/i.mx-6solox-processors-heterogeneous-processing-with-arm-cortex-a9-and-cortex-m4-cores:i.MX6SX)

<a id="id19"></a>

〔[9](#id20)〕 [https://www.nxp.com/docs/en/data-sheet/IMX6SXCEC.pdf](https://www.nxp.com/docs/en/data-sheet/IMX6SXCEC.pdf)

<a id="id21"></a>

〔10〕 ([1](#id22),[2](#id23)) [https://www.nxp.com/docs/en/reference-manual/IMX6SXRM.pdf](https://www.nxp.com/docs/en/reference-manual/IMX6SXRM.pdf)

## 译注

Neo Full仅在M4上运行此Zephyr移植，由A9设置时钟并加载镜像。原文PC与SP推导加载地址的说法不同，已注明。UDOOBuntu上传器的共享内存握手机制未由Zephyr自动实现；实板测试范围按原文限于UART输出观察。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [IMX6SXCEC.pdf](https://www.nxp.com/docs/en/data-sheet/IMX6SXCEC.pdf)：HTTP Error 404: Not Found。
- [IMX6SXRM.pdf](https://www.nxp.com/docs/en/reference-manual/IMX6SXRM.pdf)：HTTP Error 404: Not Found。
- [i.mx-6solox-processors-heterogeneous-processing-with-arm-cortex-a9-and-cortex-m4-cores:i.MX6SX](https://www.nxp.com/products/processors-and-microcontrollers/applications-processors/i.mx-applications-processors/i.mx-6-processors/i.mx-6solox-processors-heterogeneous-processing-with-arm-cortex-a9-and-cortex-m4-cores:i.MX6SX)：HTTP Error 404: Not Found。

---

[上一章](P018_UDOO_KEY.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P020_Umeta_Ikki_Automotive_Parts.md)
