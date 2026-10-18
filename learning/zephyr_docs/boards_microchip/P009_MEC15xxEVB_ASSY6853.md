---
id: learning.zephyr-docs.boards-microchip.page-9
title: MEC15xxEVB ASSY6853
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/microchip/mec15xxevb_assy6853/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mec15xxevb_assy6853"></a>

# 第9章\_MEC15xxEVB ASSY6853

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/microchip/mec15xxevb_assy6853/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mec15xxevb_assy6853.jpg](images/mec15xxevb_assy6853.jpg)](images/mec15xxevb_assy6853.jpg)

MEC15xxEVB ASSY6853

名称（Name）：

`mec15xxevb_assy6853`

厂商（Vendor）：

[微芯科技（Microchip Technology Inc.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=microchip)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mec1501_hsz](https://docs.zephyrproject.org/latest/boards/index.html#soc=mec1501_hsz)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/mec15xxevb_assy6853/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

MEC15xxEVB_ASSY6853套件是用于评估Microchip MEC15XX系列微控制器的开发平台。原文说明，它需要配合MEC1501 144WFBA SOLDER DC ASSY 6860 CPU板运行。量产器件已由MEC152x取代MEC1501；MEC152x与MEC150x基本相同，区别是增强的启动ROM SPI加载器。SPI镜像格式已更新，必须使用新版镜像工具；MEC1501与MEC152x镜像格式互不兼容，但评估板和CPU板兼容。

<a id="hardware"></a>

## 硬件（Hardware）


- MEC1521HA0SZ Arm Cortex-M4处理器
- 256 KB RAM及64 KB启动ROM（Boot ROM）
- 键盘接口（Keyboard Interface）
- ADC与GPIO排针（Headers）
- UART0、UART1及UART2
- FAN0、FAN1及FAN2排针
- 风扇脉宽调制接口（FAN PWM）
- JTAG／SWD、ETM及MCHP Trace跟踪端口
- PECI接口3.0
- I2C电压转换器（Voltage Translator）
- 10组SMBus排针
- 4组串行GPIO（SGPIO）排针
- VCI接口
- 5个独立硬件驱动PS/2端口
- eSPI排针
- 3个呼吸／闪烁LED
- 2个SPI NOR芯片插座
- 复位及VCC_PWRDGD按键
- 一个外部PCA9555 I/O端口，I2C地址可通过跳线选择
- 一个外部LTC2489 ΔΣ模数转换器（Delta-Sigma ADC），I2C地址可通过跳线选择
- 通过跳线选择供电来源：+5 V、内径2.1 mm／外径5.5 mm圆形电源插座，或USB Micro-A连接器

<a id="id4"></a>

SoC更多信息见MEC152x参考手册 [注1](#id3)。（[MEC152x参考手册（Reference Manual）](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC152x/MEC152x_Datasheet.pdf)）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`mec15xxevb_assy6853`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mec15xxevb_assy6853-hw-features"></a>

<a id="mec15xxevb_assy6853-mec15xxevb_assy6853/mec1501_hsz-hw-features-section"></a>

#### `mec15xxevb_assy6853/mec1501_hsz`目标（Target）

<a id="mec15xxevb_assy6853-mec15xxevb_assy6853/mec1501_hsz-hw-features-panel"></a>

<a id="mec15xxevb_assy6853-mec15xxevb_assy6853/mec1501_hsz-hw-features-memory"></a>

该开发板目标的片上存储容量：32 KiB RAM、224 KiB Flash。

<a id="mec15xxevb_assy6853-mec15xxevb_assy6853/mec1501_hsz-hw-features-table"></a>

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
<td>ARM Cortex-M4 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P024_arm_cortex-m4.md#std-dtcompatible-arm-cortex-m4"><code>arm,cortex-m4</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L472">已启用：1</a>）</td>
<td><a href="../hardware/P860_MicrochipXEC模数转换器绑定.md#dtbinding-microchip-xec-adc"><code>microchip,xec-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC电源、时钟、复位及VBAT寄存器（PCR）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P021_microchip_xec-pcr.md#std-dtcompatible-microchip-xec-pcr"><code>microchip,xec-pcr</code></a></td>
</tr>
<tr>
<td rowspan="2">增强型串行外设接口（ESPI）</td>
<td>片上（On-Chip）</td>
<td>Microchip eSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L289">已启用：1</a>）</td>
<td><a href="../espi_binding_reference/P008_microchip_xec-espi.md#std-dtcompatible-microchip-xec-espi"><code>microchip,xec-espi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip eSPI从端附接闪存（SAF）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L298">已禁用：1</a>）</td>
<td><a href="../espi_binding_reference/P005_microchip_xec-espi-saf.md#std-dtcompatible-microchip-xec-espi-saf"><code>microchip,xec-espi-saf</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Microchip CEC／MEC通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L104">已启用：6</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P004_microchip_xec-gpio.md#std-dtcompatible-microchip-xec-gpio"><code>microchip,xec-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>PCA95xx系列I2C GPIO扩展器（Expander）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/mec15xxevb_assy6853/mec15xxevb_assy6853.dts?plain=1#L100">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P015_nxp_pca95xx.md#std-dtcompatible-nxp-pca95xx"><code>nxp,pca95xx</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>Microchip嵌入式控制器子系统（EC Subsystem）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L61">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P006_microchip_xec-ecs.md#std-dtcompatible-microchip-xec-ecs"><code>microchip,xec-ecs</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Microchip I2C／SMBus控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L224">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L263">已禁用：2</a>）</td>
<td><a href="../i2c_infineon_ite_nordic_binding_reference/P014_microchip_xec-i2c.md#std-dtcompatible-microchip-xec-i2c"><code>microchip,xec-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC键盘矩阵控制器（Keyboard Matrix Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L485">已启用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P007_microchip_xec-kbd.md#std-dtcompatible-microchip-xec-kbd"><code>microchip,xec-kbd</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/mec15xxevb_assy6853/mec15xxevb_assy6853.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC系列电池后备RAM（Battery Backed RAM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L174">已启用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P012_microchip_xec-bbram.md#std-dtcompatible-microchip-xec-bbram"><code>microchip,xec-bbram</code></a></td>
</tr>
<tr>
<td rowspan="1">平台环境控制接口（PECI）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC平台环境控制接口（PECI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L494">已启用：1</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P004_microchip_xec-peci.md#std-dtcompatible-microchip-xec-peci"><code>microchip,xec-peci</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L98">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P008_microchip_xec-pinctrl.md#std-dtcompatible-microchip-xec-pinctrl"><code>microchip,xec-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">PS/2 接口（PS/2）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC PS/2控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L378">已启用：2</a>）</td>
<td><a href="../lin_dali_mctp_sensor_bus_binding_reference/P012_microchip_xec-ps2.md#std-dtcompatible-microchip-xec-ps2"><code>microchip,xec-ps2</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L400">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L408">已禁用：8</a>）</td>
<td><a href="../pwm_intel_microchip_nxp_binding_reference/P012_microchip_xec-pwm.md#std-dtcompatible-microchip-xec-pwm"><code>microchip,xec-pwm</code></a></td>
</tr>
<tr>
<td rowspan="2">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC基础定时器（Basic Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L308">已禁用：4</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P004_microchip_xec-timer.md#std-dtcompatible-microchip-xec-timer"><code>microchip,xec-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip XEC休眠定时器（Hibernation Timer），位于32 kHz时钟域的16位递减计数定时器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L364">已启用：2</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P002_microchip_xec-hibtimer.md#std-dtcompatible-microchip-xec-hibtimer"><code>microchip,xec-hibtimer</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L212">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L188">已禁用：2</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P001_microchip_xec-uart.md#std-dtcompatible-microchip-xec-uart"><code>microchip,xec-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC QMSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L504">已启用：1</a>）</td>
<td><a href="../spi_microchip_nordic_nxp_binding_reference/P011_microchip_xec-qmspi.md#std-dtcompatible-microchip-xec-qmspi"><code>microchip,xec-qmspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L47">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">转速计（Tachometer）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC转速计控制器（Tachometer Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L522">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L533">已禁用：3</a>）</td>
<td><a href="../auxdisplay_iio_tach_binding_reference/P017_microchip_xec-tach.md#std-dtcompatible-microchip-xec-tach"><code>microchip,xec-tach</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已禁用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Microchip XEC实时操作系统定时器（RTOS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L165">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P004_microchip_xec-rtos-timer.md#std-dtcompatible-microchip-xec-rtos-timer"><code>microchip,xec-rtos-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC看门狗定时器（Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L180">已启用：1</a>）</td>
<td><a href="../soc_pmic_watchdog_binding_reference/P011_microchip_xec-watchdog.md#std-dtcompatible-microchip-xec-watchdog"><code>microchip,xec-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

此评估板套件由以下硬件模块组成：


- <a id="id6"></a>

  MEC15xx EVB ASSY 6853 Rev A，参见[MEC15xx EVB原理图](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/Everglades%20EVB%20-%20Assy_6853%20Rev%20A1p1%20-%20SCH.pdf) [注2](#id5)
- <a id="id8"></a>

  搭载MEC152x芯片的MEC1501 144WFBA SOLDER DC ASSY 6883，参见[MEC1501子卡原理图](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/MEC1501%20Socket%20DC%20for%20EVERGLADES%20EVB%20-%20Assy_6883%20Rev%20A0p1%20-%20SCH.pdf) [注3](#id7)
- <a id="id10"></a>

  SPI DONGLE ASSY 6791，参见SPI适配板原理图 [注4](#id9)（[SPI适配板原理图（Dongle Schematic）](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/SPI%20Dongles%20and%20Aardvark%20Interposer%20Assy%206791%20Rev%20A1p1%20-%20SCH.pdf)）

<a id="system-clock"></a>

### 系统时钟（System Clock）

MEC1521 MCU使用48 MHz内部振荡器及片上PLL，最终生成12 MHz EC时钟。详见文末数据手册第4章“4.0 POWER, CLOCKS, and RESETS”中的处理器时钟控制寄存器。

<a id="serial-port"></a>

### 串口（Serial Port）

UART2用于串行日志。

<a id="jumper-settings"></a>

## 跳线设置（Jumper Settings）

按以下跳线设置即可演示此板，高级用户可根据需要采用其他配置。

<a id="jumper-setting-for-mec15xx-evb-assy-6853-rev-a1p0"></a>

### MEC15xx EVB Assy 6853 Rev A1p0跳线设置

<a id="power-related-jumpers"></a>

#### 电源相关跳线（Power-Related Jumpers）

若通过+5 V电源适配器供电，将其连接到P11圆形电源插座，外径5.5 mm、内径2.1 mm，并短接JP88的5—6脚。

若通过Micro-USB Type-A／B连接器P12供电，短接JP88的7—8脚。

注意（Note）

JP88只需安装一个跳线帽。

<table>
<tr>
<th>JP22</th>
<th>JP32</th>
<th>JP33</th>
<th>JP37</th>
<th>JP43</th>
<th>JP47</th>
<th>JP54</th>
<th>JP56</th>
<th>JP58</th>
<th>JP64</th>
<th>JP65</th>
</tr>
<tr>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
</tr>
</table>

<table>
<tr>
<th>JP72</th>
<th>JP73</th>
<th>JP76</th>
<th>JP79</th>
<th>JP80</th>
<th>JP81</th>
<th>JP82</th>
<th>JP84</th>
<th>JP87</th>
<th>JP89</th>
</tr>
<tr>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
</tr>
</table>

<table>
<tr>
<th>JP90</th>
<th>JP91</th>
<th>JP100</th>
<th>JP101</th>
<th>JP118</th>
</tr>
<tr>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>2-3</td>
</tr>
</table>

这些跳线分别配置VCC电源良好信号（Power Good）、nRESETI及JTAG_STRAP。

<table>
<tr>
<th>JP5：VCC Power Good</th>
<th>JP4：nRESETI</th>
<th>JP45：JTAG_STRAP</th>
</tr>
<tr>
<td>1-2</td>
<td>1-2</td>
<td>2-3</td>
</tr>
</table>

<a id="boot-rom-straps"></a>

#### 启动ROM配置引脚（Boot-ROM Straps）

这些跳线配置MEC1501启动ROM采样的配置引脚。

<table>
<tr>
<th>JP93：CMP_STRAP</th>
<th>JP11：CR_STRAP</th>
<th>JP46：VTR2_STRAP</th>
<th>JP96：BSS_STRAP</th>
</tr>
<tr>
<td>2-3</td>
<td>1-2</td>
<td>2-3</td>
<td>1-2</td>
</tr>
</table>

JP96的1—2脚短接，将SHD SPI CS0#上拉到VTR2。MEC1501启动ROM采样此信号，高电平时从共享SPI加载代码。

<a id="peripheral-routing-jumpers"></a>

#### 外设连接跳线（Peripheral Routing Jumpers）

下表各列分别说明如何启用UART2、SWD、私有SPI（PVT SPI）、共享SPI（SHD SPI）及LED0—2。

<table>
<tr>
<th>JP48：UART2</th>
<th>JP9：UART2</th>
<th>JP9：SWD</th>
<th>JP38：私有SPI（PVT SPI）</th>
<th>JP98：共享SPI（SHD SPI）</th>
<th>JP41：LED0—2</th>
</tr>
<tr>
<td>1-2</td>
<td></td>
<td>2-3</td>
<td>2-3</td>
<td>2-3</td>
<td>1-2</td>
</tr>
<tr>
<td>4-5</td>
<td>4-5</td>
<td></td>
<td>5-6</td>
<td>5-6</td>
<td>3-4</td>
</tr>
<tr>
<td>7-8</td>
<td></td>
<td>8-9</td>
<td>8-9</td>
<td>8-9</td>
<td>5-6</td>
</tr>
<tr>
<td>10-11</td>
<td>10-11</td>
<td></td>
<td>11-12</td>
<td>11-12</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>14-15</td>
<td>14-15</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>17-18</td>
<td>20-21</td>
<td></td>
</tr>
</table>

注意（Note）

使用UART2时，确认JP39的1—2脚及3—4脚均已短接。

要接收UART2串行输出，请按下图确认JP9配置为UART2输出。

![官方原图：JP9 header Assy6853](images/mec15xxevb_assy6853_jp9_1.jpg)

<a id="jumper-settings-for-mec1501-144wfbga-socket-dc-assy-6883-rev-b1p0"></a>

### MEC1501 144WFBGA Socket DC Assy 6883 Rev B1p0跳线设置

上述跳线配置针对底板。ASSY 6883 MEC1501 CPU板支持可选的外部32 kHz时钟源，板载32 kHz晶体振荡器，也可配置为从XTAL2／32KHZ_IN引脚输入占空比50%的外部32 kHz时钟。固件必须设置MEC15xx时钟使能寄存器，选择与跳线匹配的外部时钟源。若使用芯片内部振荡器，32K跳线状态无关紧要。JP1仅用于示波器观察测试时钟输出。详见文末原理图。

<a id="parallel-32khz-crystal-configuration"></a>

#### 并联32 kHz晶体配置（Parallel Crystal Configuration）

<table>
<tr>
<th>JP2</th>
<th>JP3</th>
</tr>
<tr>
<td>1-2</td>
<td>2-3</td>
</tr>
</table>

<a id="external-32khz-50-duty-cycle-configuration"></a>

#### 外部32 kHz、50%占空比时钟配置

<table>
<tr>
<th>JP2</th>
<th>JP3</th>
</tr>
<tr>
<td>未连接（NC）</td>
<td>1-2</td>
</tr>
</table>

<a id="jumper-settings-for-mec1503-144wfbga-socket-dc-assy-6856-rev-b1p0"></a>

### MEC1503 144WFBGA Socket DC Assy 6856 Rev B1p0跳线设置

MEC1503 ASSY 6856 CPU卡不含板载外部32K晶体或振荡器。唯一跳线组JP1用于观察测试时钟输出，不用于配置。详见文末原理图。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`mec15xxevb_assy6853`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
<tr>
<td>dediprog</td>
<td>✅（默认 / default）</td>
<td></td>
</tr>
</table>

<a id="setup"></a>

### 设置（Setup）


1. 若使用Dediprog SF100编程器，先完成其设置。

  <a id="id18"></a>

  Windows版本见[SF100产品页面](https://www.dediprog.com/product/SF100) [注8](#id17)。

  <a id="id16"></a>

  <a id="id20"></a>

  Linux版本源码见[SF100 Linux GitHub](https://github.com/DediProgSW/SF100Linux) [注7](#id15)，按[SF100 Linux手册](https://www.dediprog.com/download/save/727.pdf) [注9](#id19) 完成设置。将SF100Linux目录的60-dediprog.rules复制到原文所列`/etc/udev/rules.s`或`rules.d`目录，然后执行以下命令重启服务：

  ```text
  $ udevadm control --reload
  ```

  将dpcmd所在目录加入PATH；Linux工具名为dpcmd，Windows为dpcmd.exe。
2. <a id="id12"></a>

  <a id="id14"></a>

  克隆[MEC152x SPI Image Gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC152x/SPI_image_gen) [注5](#id11) 仓库，或下载该目录中的文件。预生产版本MEC150x使用[MEC150x SPI Image Gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC1501/SPI_image_gen) [注6](#id13) 仓库。
3. 将镜像生成工具加入PATH，或设置EVERGLADES_SPI_GEN环境变量，使Zephyr能够找到它，例如：

  ```text
  export EVERGLADES_SPI_GEN=<path to tool>/everglades_spi_gen_RomE
  ```

  Linux和Windows工具文件名不同。预生产版本MEC1501 SoC使用everglades_spi_gen_lin64。
4. 必要时可指定自定义SPI镜像配置文件，覆盖默认配置。

  ```text
  export EVERGLADES_SPI_CFG=custom_spi_cfg.txt
  ```

<a id="wiring"></a>

### 接线（Wiring）


1. 将SPI Dongle ASSY 6791连接到EVB的J44。

  ![官方原图：SPI DONGLE ASSY 6791 Connected](images/spidongle_assy6791_view1.jpg)
2. 将编程器连接到Assy6791的J6排针，以烧录SPI NOR芯片U3。确认编程偏移为0x0，可使用Dediprog SF100或类似SPI芯片编程工具。

  <a id="id2"></a>

  <table>
  <tr>
  <td><img src="images/spidongle_assy6791.jpg" alt="官方原图：SPI DONGLE ASSY 6791"></td>
  <td><img src="images/spidongle_assy6791_view2.jpg" alt="官方原图：SPI DONGLE ASSY 6791 view 2"><br><br><br><br><img src="images/dediprog_connector_2.jpg" alt="官方原图：SPI DONGLE ASSY 6791 Connected"></td>
  </tr>
  </table>

  注意（Note）

  注意，Dediprog排针上的SPI MISO／MOSI信号相互交换。应使用独立导线连接Dediprog与Assy6791 SPI板，接线关系见下表。

  <table>
  <tr>
  <th>Dediprog连接器</th>
  <th>Assy6791 J6连接器</th>
  </tr>
  <tr>
  <td>电源（VCC）</td>
  <td>1</td>
  </tr>
  <tr>
  <td>地（GND）</td>
  <td>2</td>
  </tr>
  <tr>
  <td>片选（CS）</td>
  <td>3</td>
  </tr>
  <tr>
  <td>时钟（CLK）</td>
  <td>4</td>
  </tr>
  <tr>
  <td>主机输入从机输出（MISO）</td>
  <td>6</td>
  </tr>
  <tr>
  <td>主机输出从机输入（MOSI）</td>
  <td>5</td>
  </tr>
  </table>
3. 通过RS232线缆，将MEC15xxEVB_ASSY_6853的UART2连接主机。
4. 通过Micro-USB线缆供电，并短接JP88的7—8脚选择此供电方式。

  ![官方原图：SPI DONGLE ASSY 6791 Connected](images/jp88_power_options.jpg)
5. 最终接线应如下图所示：

  ![官方原图：SPI DONGLE ASSY 6791 Connected](images/mec_board_setup.jpg)

<a id="building"></a>

### 构建（Building）


1. 按通常方式构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用。
2. 构建系统能找到镜像生成工具时，会生成spi_image.bin，可用它烧录SPI芯片。

<a id="flashing"></a>

### 烧录（Flashing）


1. 运行惯用的终端程序监听输出。Linux下串口应为`/dev/ttyUSB0`，保持终端打开。

  例如：

  ```text
  $ minicom -D /dev/ttyUSB0 -o
  ```

  `-o`选项让`minicom`不发送调制解调器初始化字符串（Modem Initialization String）。连接参数应配置如下：


  - 速率（Speed）：115200波特率
  - 数据位（Data）：8位
  - 奇偶校验（Parity）：无（None）
  - 停止位（Stop Bits）：1位
2. 在第二个终端中用west烧录开发板，同时并排显示两个终端。

  ```text
  $ west flash
  ```

  注意（Note）

  west进程启动时按住复位键，直至整个west过程成功结束后再松开。

  ![官方原图：SPI DONGLE ASSY 6791 Connected](images/reset_button_1.jpg)

  注意（Note）

  若不想每次按住复位键，可在west flash编程期间断开SPI Dongle ASSY 6791与EVB的连接，完成后重新接到J44并给EVB供电，效果相同。
3. 第一个终端应显示`Hello World! mec15xxevb_assy6853`。若未显示，可按复位键，随后应出现消息。

<a id="debugging"></a>

### 调试（Debugging）

此板提供Cortex ETM端口，可通过单一物理连接进行跟踪及调试；另有仅供JTAG会话使用的插座。

<a id="troubleshooting"></a>

### 故障排查（Troubleshooting）


1. 若未看到应用运行，确认LED7、LED8及LED1均已亮；若任一未亮，重新检查电源跳线。
2. 若Dediprog无法编程此板，可断开Assy6791与Assy6853主板连接后重试。
3. 若Dediprog无法检测板载闪存，按住开发板复位键后重试。

<a id="notes"></a>

### 备注（Notes）


1. 要启用PCA9555PW并测试mec15xxevb_assy6853的I2C，需要额外设置：

  板载I2C目标器件NXP PCA95xx连接I2C00，但该端口与采集串行日志的UART2 RS232转TTL转换器共用，因此UART2及I2C00不能同时使用。应按下列跳线设置改用I2C01：

> - 短接JP99的1—2脚，将CPU的I2C01_SDA连接到J5
> - 短接JP99的13—14脚，将CPU的I2C01_SCL连接到J5
> - 短接JP25的21—22脚，启用I2C01_SDA外部上拉
> - 短接JP25的23—24脚，启用I2C01_SCL外部上拉
> - 连接JP44.1与J5.1，将NXP PCA95xx接到I2C01
> - 连接JP44.3与J5.3，将NXP PCA95xx接到I2C01

<a id="references"></a>

## 参考资料（References）

<a id="id3"></a>

〔[1](#id4)〕 [https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC152x/MEC152x_Datasheet.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC152x/MEC152x_Datasheet.pdf)

<a id="id5"></a>

〔[2](#id6)〕 [https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/Everglades%20EVB%20-%20Assy_6853%20Rev%20A1p1%20-%20SCH.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/Everglades%20EVB%20-%20Assy_6853%20Rev%20A1p1%20-%20SCH.pdf)

<a id="id7"></a>

〔[3](#id8)〕 [https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/MEC1501%20Socket%20DC%20for%20EVERGLADES%20EVB%20-%20Assy_6883%20Rev%20A0p1%20-%20SCH.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/MEC1501%20Socket%20DC%20for%20EVERGLADES%20EVB%20-%20Assy_6883%20Rev%20A0p1%20-%20SCH.pdf)

<a id="id9"></a>

〔[4](#id10)〕 [https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/SPI%20Dongles%20and%20Aardvark%20Interposer%20Assy%206791%20Rev%20A1p1%20-%20SCH.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/SPI%20Dongles%20and%20Aardvark%20Interposer%20Assy%206791%20Rev%20A1p1%20-%20SCH.pdf)

<a id="id11"></a>

〔[5](#id12)〕 [https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC152x/SPI_image_gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC152x/SPI_image_gen)

<a id="id13"></a>

〔[6](#id14)〕 [https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC1501/SPI_image_gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC1501/SPI_image_gen)

<a id="id15"></a>

〔[7](#id16)〕 [https://github.com/DediProgSW/SF100Linux](https://github.com/DediProgSW/SF100Linux)

<a id="id17"></a>

〔[8](#id18)〕 [https://www.dediprog.com/product/SF100](https://www.dediprog.com/product/SF100)

<a id="id19"></a>

〔[9](#id20)〕 [https://www.dediprog.com/download/save/727.pdf](https://www.dediprog.com/download/save/727.pdf)

## 译注

概述列CPU板ASSY 6860，硬件清单列ASSY 6883，均保留。MEC1501／MEC152x镜像格式互不兼容；MEC1503子卡不带外部32 kHz晶体。原文udev目录rules.s或rules.d及Dediprog信号交叉接线原样说明。

---

[上一章](P008_MEC1501_Modular_card_ASSY6885.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_MEC172xEVB_ASSY6906.md)
