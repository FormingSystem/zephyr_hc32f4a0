---
id: learning.zephyr-docs.boards-microchip.page-8
title: MEC1501 Modular card ASSY6885
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/microchip/mec1501modular_assy6885/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mec1501modular_assy6885"></a>

# 第8章\_MEC1501模块卡ASSY6885（Modular Card）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/microchip/mec1501modular_assy6885/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mec1501modular_assy6885.jpg](images/mec1501modular_assy6885.jpg)](images/mec1501modular_assy6885.jpg)

MEC1501模块卡ASSY6885（Modular Card）

名称（Name）：

`mec1501modular_assy6885`

厂商（Vendor）：

[微芯科技（Microchip Technology Inc.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=microchip)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mec1501_hsz](https://docs.zephyrproject.org/latest/boards/index.html#soc=mec1501_hsz)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/mec1501modular_assy6885/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

MEC1501 Modular Card ASSY6885用于评估Microchip MEC152X系列微控制器，可独立使用，也可与符合MECC规范的平台配合。

<a id="hardware"></a>

## 硬件（Hardware）


- MEC1521HA0SZ Arm Cortex-M4处理器
- 256 KB RAM及64 KB启动ROM（Boot ROM）
- GPIO排针
- 通过Micro-USB连接的UART1
- PECI接口3.0
- 10个SMBus实例
- FAN、PMW及TACHO引脚，PMW拼写沿用原文
- VCI接口
- 独立硬件驱动的PS/2端口

与MEC15xx评估板不同，MEC1521模块卡通过两种方式引出引脚：


1. 独立模式（Standalone Mode），通过排针连接


  - 通用输入输出（GPIOs）
  - PWM5
  - JTAG／SWD、ETM及MCHP Trace跟踪端口
  - eSPI总线
  - SMB0
2. 配合模式（Mated Mode），连接另一块带高密度MECC连接器的平台


  - FAN0、PWM0、SMB0、SMB1、SMB4及SMB5
  - eSPI总线
  - 呼吸／闪烁LED（Breathing / Blinking LEDs）

通过+5 V USB Micro-A连接器或MECC连接器供电。

<a id="id3"></a>

SoC更多信息见MEC152x参考手册 [注1](#id2)。（[MEC152x参考手册（Reference Manual）](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC152x/MEC152x_Datasheet.pdf)）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`mec1501modular_assy6885`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mec1501modular_assy6885-hw-features"></a>

<a id="mec1501modular_assy6885-mec1501modular_assy6885/mec1501_hsz-hw-features-section"></a>

#### `mec1501modular_assy6885/mec1501_hsz`目标（Target）

<a id="mec1501modular_assy6885-mec1501modular_assy6885/mec1501_hsz-hw-features-panel"></a>

<a id="mec1501modular_assy6885-mec1501modular_assy6885/mec1501_hsz-hw-features-memory"></a>

该开发板目标的片上存储容量：32 KiB RAM、224 KiB Flash。

<a id="mec1501modular_assy6885-mec1501modular_assy6885/mec1501_hsz-hw-features-table"></a>

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
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Microchip CEC／MEC通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L104">已启用：6</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P004_microchip_xec-gpio.md#std-dtcompatible-microchip-xec-gpio"><code>microchip,xec-gpio</code></a></td>
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
<td>Microchip I2C／SMBus控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L224">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L250">已禁用：3</a>）</td>
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
<td>Microchip XEC UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L200">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L188">已禁用：2</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P001_microchip_xec-uart.md#std-dtcompatible-microchip-xec-uart"><code>microchip,xec-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Microchip XEC QMSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/mec/mec1501hsz.dtsi?plain=1#L504">已禁用：1</a>）</td>
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


- <a id="id5"></a>

  MEC1501 Modular Card ASSY 6885 Rev A0，参见[MEC1501 Modular EC Card - Assy_6885 Rev A0p1](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/MEC1501%20Modular%20EC%20Card%20-%20Assy_6885%20Rev%20A0p1%20-%20SCH.pdf) [注2](#id4)

<a id="system-clock"></a>

### 系统时钟（System Clock）

MEC1501 MCU使用48 MHz内部振荡器及片上PLL，最终生成12 MHz EC时钟。详见文末数据手册第4章“4.0 POWER, CLOCKS, and RESETS”中的处理器时钟控制寄存器。

<a id="serial-port"></a>

### 串口（Serial Port）

UART1用于串行日志。

<a id="jumper-settings"></a>

## 跳线设置（Jumper Settings）

按以下跳线设置即可演示此板，高级用户可根据需要采用其他配置。

<a id="jumper-setting-for-mec1501-modular-assy-6885-rev-a1p0"></a>

### MEC1501 Modular Assy 6885 Rev A1p0跳线设置

<a id="power-related-jumpers"></a>

#### 电源相关跳线（Power-Related Jumpers）

若通过Type-A／B连接器P10供电，将JP35设为1—2脚短接。

若通过MECC连接器P1供电并连接外部平台，将JP35设为3—4脚短接。

注意（Note）

JP35只需安装一个跳线帽。

<table>
<tr>
<th>JP30：VTR3</th>
<th>JP31：VTR_PLL</th>
<th>JP32：VTR_REG</th>
<th>JP33：VTR1</th>
<th>JP34：VTR2</th>
<th>JP40：3.3 V</th>
<th>JP21：VREF_ADC</th>
</tr>
<tr>
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
<th>JP6：VBAT</th>
<th>JP36：VTR_ANALOG</th>
<th>JP27：PECI</th>
<th>JP4：VREF_VTT</th>
</tr>
<tr>
<td>2-3</td>
<td>1-2</td>
<td>2-3</td>
<td>断开（open）</td>
</tr>
</table>

这些跳线分别配置nRESETI及JTAG_STRAP。

<table>
<tr>
<th>JP22：nRESETI</th>
<th>JP29：JTAG_STRAP</th>
</tr>
<tr>
<td>11-12</td>
<td>1-2</td>
</tr>
</table>

<a id="boot-rom-straps"></a>

#### 启动ROM配置引脚（Boot-ROM Straps）

这些跳线配置MEC1501启动ROM采样的配置引脚。

<table>
<tr>
<th>JP37：CMP_STRAP</th>
<th>J6：CR_STRAP</th>
<th>JP41：VTR2_STRAP</th>
<th>JP23：BSS_STRAP</th>
</tr>
<tr>
<td>1-2</td>
<td>1-2</td>
<td>1-2</td>
<td>3-4</td>
</tr>
</table>

JP23的3—4脚短接，将SHD SPI CS0#上拉到VTR2。MEC1501启动ROM采样此信号，高电平时从共享SPI（SHD SPI）加载代码，这是推荐设置。

<table>
<tr>
<td>CR_STRAP</td>
<td>BSS_STRAP</td>
<td>来源（SOURCE）</td>
</tr>
<tr>
<td>0</td>
<td>X</td>
<td>使用3.3 V私有SPI（Private SPI）</td>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>使用eSPI闪存通道（Flash Channel）</td>
</tr>
<tr>
<td></td>
<td>1</td>
<td>使用3.3 V共享通道（Shared Channel），原文标记R</td>
</tr>
</table>

<a id="power-management"></a>

#### 电源管理（Power Management）

需要短接JP20的2—3脚，使VTR3电源轨供电的全部GPIO工作于1.8 V。

注意（Note）

需将外部1.8 V电源连接到JP13.1。

<table>
<tr>
<th>JP20：VTR3电源选择</th>
<th>JP13：1.8 V电源来源</th>
</tr>
<tr>
<td>2-3</td>
<td>1.8 V接第1脚</td>
</tr>
</table>

<a id="jumper-location-map"></a>

#### 跳线位置图（Jumper Location Map）

```text
+--------------------------------------------------------------------------------------+
|                  |------------|                     +----------+ J10              || |
|  [BT1]       +   +------------+ J50                                      ++   ++  || |
|              |                                           JP38 JP43       ++   ||  || |
|              +         +      +       +-+ JP4              +    +       JP26  ||  || |
|             JP6        +      +                  +      +  + +  + +           ||  || |
|    JP31 ++            JP32   JP36     +-+ JP27   +      +    +    +           J6  || |
|                                                 JP18  JP37 JP41 JP42              ++ |
|         ++                  +   +    +--------+                                  J48 |
|         ||  JP21            +   +    +--------+ JP22    +----------+                 |
|      J2 ||   +            JP34 JP30                         J11              ++      |
|         ++   +                                                  J44          ||      |
|                            ++                         +----------------+     ||      |
|       +---------------+    ||  +        JP24          |----------------|     ++      |
|       |---------------|    ++  +    +----------+      +----------------+    J47      |
| JP20  +---------------+  JP23  JP40 +----------+                                  ++ |
|                                                     +           ++ JP29           || |
|                             +  +    +----------+    +                             || |
|    J52+---------------+     +  +    +----------+   J5   +-------------+           ++ |
|    J45+---------------+  JP33 TP57      JP25            +-------------+ J4       J49 |
|                                                                                      |
| ++                                           TP4   +----------+   ++                 |
| ++     +    +      +    +    +       +  TP61         +----------+   ++               |
| JP28   +    +      +    +    +  TP65 +  TP60            J51        JP35              |
|      TP58 JP16   JP11 JP13 JP15     JP10                                             |
| TP5                                                                                  |
| TP6                                        TP1                                       |
+--------------------------------------------------------------------------------------+
```

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`mec1501modular_assy6885`开发板支持下表所列的运行工具（Runners）及相关west命令。

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


1. <a id="id7"></a>

  <a id="id10"></a>

  克隆[MEC152x SPI Image Gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC152x/SPI_image_gen) [注3](#id6) 仓库，或下载该目录中的文件。预生产版本MEC150x应使用[MEC150x SPI Image Gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC1501/SPI_image_gen) [注4](#id9) 仓库。
2. 将镜像生成工具加入PATH，或设置EVERGLADES_SPI_GEN环境变量，使Zephyr能够找到它，例如：

  ```text
  export EVERGLADES_SPI_GEN=<path to tool>/everglades_spi_gen_RomE
  ```

  Linux和Windows工具文件名不同。预生产版本MEC1501 SoC使用everglades_spi_gen_lin64。
3. 必要时可指定自定义SPI镜像配置文件，覆盖默认配置。

  ```text
  export EVERGLADES_SPI_CFG=custom_spi_cfg.txt
  ```

<a id="building"></a>

### 构建（Building）


1. 按通常方式构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用。
2. <a id="id8"></a>

  得到zephyr.bin后，使用Microchip [MEC152x SPI Image Gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC152x/SPI_image_gen) [注3](#id6) 工具生成最终二进制文件，再将其输出烧录到共享SPI存储器。

<a id="flashing"></a>

### 烧录（Flashing）


1. 将Dediprog连接到J2排针。
2. 使用Dediprog SF100或类似SPI芯片编程工具，在偏移0x0处烧录SPI NOR U3。
3. 运行你惯用的终端程序，监听输出。Linux下的终端设备应为`/dev/ttyACM0`，例如：

  ```text
  $ minicom -D /dev/ttyACM0 -o
  ```

  `-o`选项让`minicom`不发送调制解调器初始化字符串（Modem Initialization String）。连接参数应配置如下：


  - 速率（Speed）：115200波特率
  - 数据位（Data）：8位
  - 奇偶校验（Parity）：无（None）
  - 停止位（Stop Bits）：1位
4. 通过UART1将MEC1501MODULAR_ASSY6885连接到主机，然后供电。

  终端应显示`Hello World! mec1501modular_assy6885`。

<a id="debugging"></a>

### 调试（Debugging）

此板提供Cortex ETM端口，可通过单一物理连接进行跟踪及调试；另有仅供JTAG会话使用的插座。

<a id="hw-issues"></a>

### 硬件问题（HW Issues）

若未看到应用运行，确认LED1已亮；若未亮，重新检查电源跳线。

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC152x/MEC152x_Datasheet.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC152x/MEC152x_Datasheet.pdf)

<a id="id4"></a>

〔[2](#id5)〕 [https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/MEC1501%20Modular%20EC%20Card%20-%20Assy_6885%20Rev%20A0p1%20-%20SCH.pdf](https://github.com/MicrochipTech/CPGZephyrDocs/blob/master/MEC1501/MEC1501%20Modular%20EC%20Card%20-%20Assy_6885%20Rev%20A0p1%20-%20SCH.pdf)

<a id="id6"></a>

〔3〕 ([1](#id7),[2](#id8)) [https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC152x/SPI_image_gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC152x/SPI_image_gen)

<a id="id9"></a>

〔[4](#id10)〕 [https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC1501/SPI_image_gen](https://github.com/MicrochipTech/CPGZephyrDocs/tree/master/MEC1501/SPI_image_gen)

## 译注

原文标题MEC1501与量产MEC152x器件名称并存。预生产与量产芯片需使用不同SPI镜像工具；JP35供电来源只能选一个。VTR3的1.8 V配置及外部电源要求按原文保留。

---

[上一章](P007_Microchip_M2S_Hello_FPGA_Kit.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_MEC15xxEVB_ASSY6853.md)
