---
id: learning.zephyr-docs.boards-arduino.page-1
title: Arduino Due
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/arduino/due/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="arduino_due"></a>

# 第1章\_Arduino Due

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/arduino/due/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id2"></a>

[![官方原图：../../../../_images/arduino_due.jpg](images/arduino_due.jpg)](images/arduino_due.jpg)

Arduino Due

名称（Name）：

`arduino_due`

厂商（Vendor）：

[Arduino](https://docs.zephyrproject.org/latest/boards/index.html#vendor=arduino)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[sam3x8e](https://docs.zephyrproject.org/latest/boards/index.html#soc=sam3x8e)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arduino/due/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

`arduino_due`开发板配置用于运行在Arduino Due上的Zephyr应用，支持Atmel SAM3X8E ARM Cortex-M3 CPU及以下设备：


- 嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）
- 系统滴答系统时钟（SYSTICK / System Tick System Clock）
- 通过USB提供的串口（ATMEL_SAM3）

<a id="id4"></a>

<a id="id7"></a>

开发板的更多信息见[Arduino Due网站](https://www.arduino.cc/en/Main/ArduinoBoardDue)[注1](#id3)；处理器信息及数据手册见[Atmel SAM3X8E数据手册](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-11057-32-bit-Cortex-M3-Microcontroller-SAM3X-SAM3A_Datasheet.pdf)[注2](#id6)。

注意（Note）

此配置不受Arduino官方支持。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`arduino_due`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="arduino_due-hw-features"></a>

<a id="arduino_due-arduino_due/sam3x8e-hw-features-section"></a>

#### `arduino_due/sam3x8e`目标（Target）

<a id="arduino_due-arduino_due/sam3x8e-hw-features-panel"></a>

<a id="arduino_due-arduino_due/sam3x8e-hw-features-memory"></a>

该开发板目标的片上存储容量：96 KiB RAM、512 KiB Flash。

<a id="arduino_due-arduino_due/sam3x8e-hw-features-table"></a>

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
<td>ARM Cortex-M3处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P021_arm_cortex-m3.md#std-dtcompatible-arm-cortex-m3"><code>arm,cortex-m3</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L262">已禁用：1</a>）</td>
<td><a href="../hardware/P856_AtmelSAM模数转换器绑定.md#dtbinding-atmel-sam-adc"><code>atmel,sam-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Atmel电源管理控制器（PMC / Power Management Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P009_atmel_sam-pmc.md#std-dtcompatible-atmel-sam-pmc"><code>atmel,sam-pmc</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM定时器／计数器（TC / Timer Counter）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L226">已禁用：3</a>）</td>
<td><a href="../counter_binding_reference/P010_atmel_sam-tc.md#std-dtcompatible-atmel-sam-tc"><code>atmel,sam-tc</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列数模转换器（DAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L273">已启用：1</a>）</td>
<td><a href="../hardware/P762_AtmelSAM数模转换器绑定.md#dtbinding-atmel-sam-dac"><code>atmel,sam-dac</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM增强型嵌入式闪存控制器（EEFC / Enhanced Embedded Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L75">已禁用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P006_atmel_sam-flash-controller.md#std-dtcompatible-atmel-sam-flash-controller"><code>atmel,sam-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>SAM通用输入输出端口（GPIO Port）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L175">已启用：5</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P029_atmel_sam-gpio.md#std-dtcompatible-atmel-sam-gpio"><code>atmel,sam-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/due/arduino_r3_connector.dtsi?plain=1#L10">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>ATMEL SAM复位控制器（Reset Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L293">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P001_atmel_sam-rstc.md#std-dtcompatible-atmel-sam-rstc"><code>atmel,sam-rstc</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列I2C双线接口（TWI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L107">已启用：2</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P008_atmel_sam-i2c-twi.md#std-dtcompatible-atmel-sam-i2c-twi"><code>atmel,sam-i2c-twi</code></a></td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/due/arduino_due.dts?plain=1#L30">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L84">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM引脚控制容器（Pinctrl Container）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L169">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P013_atmel_sam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl"><code>atmel,sam-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM电源控制器（SUPC / Supply Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P001_atmel_sam-supc.md#std-dtcompatible-atmel-sam-supc"><code>atmel,sam-supc</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L282">已启用：1</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P007_atmel_sam-pwm.md#std-dtcompatible-atmel-sam-pwm"><code>atmel,sam-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列实时时钟（RTC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L300">已禁用：1</a>）</td>
<td><a href="../rtc_binding_reference/P004_atmel_sam-rtc.md#std-dtcompatible-atmel-sam-rtc"><code>atmel,sam-rtc</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>SAM系列通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L129">已启用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P010_atmel_sam-uart.md#std-dtcompatible-atmel-sam-uart"><code>atmel,sam-uart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L137">已禁用：4</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P011_atmel_sam-usart.md#std-dtcompatible-atmel-sam-usart"><code>atmel,sam-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L54">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L64">已禁用：1</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P008_atmel_sam-spi.md#std-dtcompatible-atmel-sam-spi"><code>atmel,sam-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L49">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>ATMEL SAM0看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam3x.dtsi?plain=1#L99">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P007_atmel_sam-watchdog.md#std-dtcompatible-atmel-sam-watchdog"><code>atmel,sam-watchdog</code></a></td>
</tr>
</table>

<a id="id5"></a>

<a id="id8"></a>

Arduino Due硬件功能的完整列表见[Arduino Due网站](https://www.arduino.cc/en/Main/ArduinoBoardDue)[注1](#id3)和[Atmel SAM3X8E数据手册](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-11057-32-bit-Cortex-M3-Microcontroller-SAM3X-SAM3A_Datasheet.pdf)[注2](#id6)。

注意（Note）

使用I2C的SCL1和SDA1引脚（位于IO13附近）时，需要上拉电阻（Pull-Up Resistors）。

<a id="interrupt-controller"></a>

### 中断控制器（Interrupt Controller）

共有15个固定异常（Exceptions），其中异常12（调试监控，Debug Monitor）和异常15（SYSTICK）的行为更接近中断。此外，还可有数量不定的中断请求（IRQ）。异常7–10及13为保留项，不需要处理程序（Handlers）。

基于Cortex-M3/4的开发板使用向量异常（Vectored Exceptions），每个异常都直接通过向量表（Vector Table）调用处理程序。

系统为异常1–6、11–12及14–15提供处理程序。下表列出各异常使用的处理程序。

<table>
<tr>
<th>异常编号（Exc#）</th>
<th>名称（Name）</th>
<th>备注（Remarks）</th>
<th>Zephyr内核中的用途（Used by Zephyr Kernel）</th>
</tr>
<tr>
<td>1</td>
<td>复位（Reset）</td>
<td></td>
<td>系统初始化（System Initialization）</td>
</tr>
<tr>
<td>2</td>
<td>不可屏蔽中断（NMI）</td>
<td></td>
<td>系统致命错误（System Fatal Error）</td>
</tr>
<tr>
<td>3</td>
<td>硬故障（Hard Fault）</td>
<td></td>
<td>系统致命错误（System Fatal Error）</td>
</tr>
<tr>
<td>4</td>
<td>存储器管理异常（MemManage）</td>
<td>内存保护单元故障（MPU Fault）</td>
<td>系统致命错误（System Fatal Error）</td>
</tr>
<tr>
<td>5</td>
<td>总线（Bus）</td>
<td></td>
<td>系统致命错误（System Fatal Error）</td>
</tr>
<tr>
<td>6</td>
<td>用法故障（Usage Fault）</td>
<td>未定义指令，或尝试切换到ARM模式</td>
<td>系统致命错误（System Fatal Error）</td>
</tr>
<tr>
<td>11</td>
<td>主管调用（SVC）</td>
<td></td>
<td>系统调用、内核运行时异常及中断卸载（IRQ Offloading）</td>
</tr>
<tr>
<td>12</td>
<td>调试监控（Debug Monitor）</td>
<td></td>
<td>系统致命错误（System Fatal Error）</td>
</tr>
<tr>
<td>14</td>
<td>可挂起系统调用（PendSV）</td>
<td></td>
<td>上下文切换（Context Switch）</td>
</tr>
<tr>
<td>15</td>
<td>系统节拍（SYSTICK）</td>
<td></td>
<td>系统时钟（System Clock）。</td>
</tr>
</table>

注意（Note）

复位后，所有异常的优先级均为0。为使中断锁定机制（Interrupt Locking）和异常处理正常工作，中断不能在优先级0运行。

<a id="system-clock"></a>

### 系统时钟（System Clock）

Arduino Due有两个外部振荡器／谐振器（Oscillators / Resonators）：慢速时钟为32.768 kHz，主时钟为12 MHz。处理器可配置锁相环（PLL）来驱动主控时钟（Master Clock），最高可设为84 MHz。

<a id="serial-port"></a>

### 串口（Serial Port）

Atmel SAM3X8E处理器有一个供SAM-BA引导加载程序（Bootloader）使用的UART。它只有RX/TX两根线，不提供CTS/RTS流量控制（Flow Control）或先进先出缓冲区（FIFO）。RX/TX引脚连接到ATmega16U2，由后者提供USB转TTL串口功能。Zephyr控制台默认使用此控制器输出。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`arduino_due`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-bossac">bossac</a></td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
</table>

<a id="flashing"></a>

### 烧录（Flashing）

<a id="bossa-tool"></a>

#### BOSSA工具（Tool）

<a id="id10"></a>

将Zephyr内核烧录到Arduino Due需要使用[bossa工具](https://github.com/shumatech/BOSSA)[注3](#id9)。

bossa工具提供图形界面（GUI）版和命令行版。下面介绍命令行版的构建步骤；GUI版的构建方法见bossa工具的README文件。

按以下步骤构建bossa工具：


1. 从仓库检出bossa工具的代码。

  ```text
  $ git clone https://github.com/shumatech/BOSSA.git
  $ cd BOSSA
  ```
2. 切换到`arduino`分支。`master`分支中的代码不适用于Arduino Due。

  ```text
  $ git switch arduino
  ```
3. 构建bossa工具的命令行版本。

  ```text
  $ make bin/bossac
  ```
4. 生成的二进制文件位于`bin/bossac`。

<a id="flashing-an-application-to-arduino-due"></a>

#### 向Arduino Due烧录应用（Flashing an Application）

`arduino_due`开发板配置的应用可按通常方式构建和烧录，详情见[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)及[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)。

以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。构建应用后，在执行烧录命令前按下Reset按键，使开发板进入SAM-BA引导加载程序并准备接收新程序。

```text
# From the root of the zephyr repository
west build -b arduino_due samples/hello_world
west flash
```

烧录应用后，运行常用终端程序查看输出。例如，在Linux上串口通常为`/dev/ttyACM0`，可执行：

```text
$ sudo minicom -D /dev/ttyACM0 -o
```

`-o`选项使minicom不发送调制解调器初始化字符串（Modem Initialization String）。

现在按下Reset按键，终端应显示`Hello World! arduino_due`。

注意（Note）

烧录二进制镜像前务必关闭终端程序，否则它会干扰烧录过程。

<a id="references"></a>

## 参考资料（References）

<a id="id3"></a>

〔1〕 ([1](#id4),[2](#id5)) [https://www.arduino.cc/en/Main/ArduinoBoardDue](https://www.arduino.cc/en/Main/ArduinoBoardDue)

<a id="id6"></a>

〔2〕 ([1](#id7),[2](#id8)) [http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-11057-32-bit-Cortex-M3-Microcontroller-SAM3X-SAM3A_Datasheet.pdf](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-11057-32-bit-Cortex-M3-Microcontroller-SAM3X-SAM3A_Datasheet.pdf)

<a id="id9"></a>

〔[3](#id10)〕 [https://github.com/shumatech/BOSSA](https://github.com/shumatech/BOSSA)

---

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_Arduino_GIGA_R1_WiFi.md)
