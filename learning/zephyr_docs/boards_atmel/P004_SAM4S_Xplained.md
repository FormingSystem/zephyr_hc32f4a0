---
id: learning.zephyr-docs.boards-atmel.page-4
title: SAM4S Xplained
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/atmel/sam/sam4s_xplained/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="sam4s_xplained"></a>

# 第4章\_SAM4S Xplained

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/atmel/sam/sam4s_xplained/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../../_images/sam4s_xplained.jpg](images/sam4s_xplained.jpg)](images/sam4s_xplained.jpg)

SAM4S Xplained

名称（Name）：

`sam4s_xplained`

厂商（Vendor）：

[Atmel公司（Atmel Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=atmel)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[sam4s16c](https://docs.zephyrproject.org/latest/boards/index.html#soc=sam4s16c)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/atmel/sam/sam4s_xplained/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

SAM4S Xplained评估套件是用于评估Atmel SAM4S系列微控制器的开发平台。

<a id="hardware"></a>

## 硬件（Hardware）


- ATSAM4S16C ARM Cortex-M4处理器
- 12 MHz晶体振荡器（Crystal Oscillator）
- 内部32.768 kHz晶体振荡器（类型依原文保留）
- IS66WV51216DALL 8 Mb SRAM
- Micro-AB USB设备接口（Device）
- Micro-AB USB调试接口，支持SEGGER OB、虚拟COM端口及数据（原文条目止于Data）
- 一个复位按键和一个用户按键
- 两个黄色用户LED
- 外部闪存芯片的集成电路焊盘（IC Pads）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`sam4s_xplained`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="sam4s_xplained-hw-features"></a>

<a id="sam4s_xplained-sam4s_xplained/sam4s16c-hw-features-section"></a>

#### `sam4s_xplained/sam4s16c`目标（Target）

<a id="sam4s_xplained-sam4s_xplained/sam4s16c-hw-features-panel"></a>

<a id="sam4s_xplained-sam4s_xplained/sam4s16c-hw-features-memory"></a>

该开发板目标的片上存储容量：128 KiB RAM、1 MiB Flash。

<a id="sam4s_xplained-sam4s_xplained/sam4s16c-hw-features-table"></a>

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
<td>ARM Cortex-M4 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P024_arm_cortex-m4.md#std-dtcompatible-arm-cortex-m4"><code>arm,cortex-m4</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L224">已启用：1</a>）</td>
<td><a href="../hardware/P856_AtmelSAM模数转换器绑定.md#dtbinding-atmel-sam-adc"><code>atmel,sam-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Atmel电源管理控制器（PMC / Power Management Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L43">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P009_atmel_sam-pmc.md#std-dtcompatible-atmel-sam-pmc"><code>atmel,sam-pmc</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM定时器／计数器（TC / Timer Counter）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L200">已禁用：2</a>）</td>
<td><a href="../counter_binding_reference/P010_atmel_sam-tc.md#std-dtcompatible-atmel-sam-tc"><code>atmel,sam-tc</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列数模转换器（DAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L235">已启用：1</a>）</td>
<td><a href="../hardware/P762_AtmelSAM数模转换器绑定.md#dtbinding-atmel-sam-dac"><code>atmel,sam-dac</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM增强型嵌入式闪存控制器（EEFC / Enhanced Embedded Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L62">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P006_atmel_sam-flash-controller.md#std-dtcompatible-atmel-sam-flash-controller"><code>atmel,sam-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>SAM通用输入输出端口（GPIO Port）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L169">已启用：3</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P029_atmel_sam-gpio.md#std-dtcompatible-atmel-sam-gpio"><code>atmel,sam-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Atmel Xplained排针引出的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4s_xplained/sam4s_xplained.dts?plain=1#L71">已启用：4</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P002_atmel-xplained-header.md#std-dtcompatible-atmel-xplained-header"><code>atmel-xplained-header</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>ATMEL SAM复位控制器（Reset Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L244">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P001_atmel_sam-rstc.md#std-dtcompatible-atmel-sam-rstc"><code>atmel,sam-rstc</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列I2C双线接口（TWI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L87">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L98">已禁用：1</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P008_atmel_sam-i2c-twi.md#std-dtcompatible-atmel-sam-i2c-twi"><code>atmel,sam-i2c-twi</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4s_xplained/sam4s_xplained.dts?plain=1#L61">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4s_xplained/sam4s_xplained.dts?plain=1#L47">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>Atmel静态存储器控制器（SMC / Static Memory Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L251">已启用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P003_atmel_sam-smc.md#std-dtcompatible-atmel-sam-smc"><code>atmel,sam-smc</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L35">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>此绑定（Binding）描述Atmel SAM闪存区域布局（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P009_atmel_sam-flash.md#std-dtcompatible-atmel-sam-flash"><code>atmel,sam-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM引脚控制容器（Pinctrl Container）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L162">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P013_atmel_sam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl"><code>atmel,sam-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM电源控制器（SUPC / Supply Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L51">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P001_atmel_sam-supc.md#std-dtcompatible-atmel-sam-supc"><code>atmel,sam-supc</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L135">已启用：1</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P007_atmel_sam-pwm.md#std-dtcompatible-atmel-sam-pwm"><code>atmel,sam-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列实时时钟（RTC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L260">已禁用：1</a>）</td>
<td><a href="../rtc_binding_reference/P004_atmel_sam-rtc.md#std-dtcompatible-atmel-sam-rtc"><code>atmel,sam-rtc</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>SAM系列通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L119">已启用：2</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P010_atmel_sam-uart.md#std-dtcompatible-atmel-sam-uart"><code>atmel,sam-uart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L146">已禁用：2</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P011_atmel_sam-usart.md#std-dtcompatible-atmel-sam-usart"><code>atmel,sam-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L109">已启用：1</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P008_atmel_sam-spi.md#std-dtcompatible-atmel-sam-spi"><code>atmel,sam-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L58">已启用：1</a>）</td>
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
<td>Atmel SAM USB设备端口控制器（UDP / USB Device Port）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L269">已启用：1</a>）</td>
<td><a href="../usb_controller_binding_reference/P003_atmel_sam-udp.md#std-dtcompatible-atmel-sam-udp"><code>atmel,sam-udp</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>ATMEL SAM0看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4s.dtsi?plain=1#L79">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P007_atmel_sam-watchdog.md#std-dtcompatible-atmel-sam-watchdog"><code>atmel,sam-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="id5"></a>

更多信息可下载[SAM4S Xplained设计文件](http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4S-XPLD__KitsFiles.zip)[注2](#id4)，其中包含完整原理图及Gerber文件。

<a id="system-clock"></a>

### 系统时钟（System Clock）

SAM4S MCU使用板上的12 MHz内部振荡器，经片上PLL生成84 MHz系统时钟（振荡器类型依原文保留）。

<a id="serial-port"></a>

### 串口（Serial Port）

ATSAM4S16C MCU有两路UART和两路USART。UART0连接SEGGER J-Link OB芯片，即烧录为J-Link OB的AT91SAM3U4。J-Link OB将该UART引出为虚拟COM端口；烧录一节使用此SEGGER USB调试连接上的UART。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`sam4s_xplained`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>✅</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-jlink"><code>jlink</code></a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

SAM4S Xplained自带SEGGER [J-Link OB](https://www.segger.com/jlink-ob.html)，为SAM4S16C提供调试接口。可使用Ozone或JLink与芯片通信。

<a id="flashing"></a>

### 烧录（Flashing）

Zephyr提供两种烧录路径：默认的JLink工具，以及SAM启动助手（SAM-BA）。（[SAM启动助手（SAM-BA / SAM Boot Assistant）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#atmel-sam-ba-bootloader)）

<a id="using-jlink"></a>

#### 使用JLink


1. <a id="id3"></a>

  从SEGGER [JLink下载页面](https://www.segger.com/downloads/jlink)[注1](#id2)获取JLink，在“J-Link Software and Documentation Pack”一节安装Linux版软件及文档包。应确保`JLinkExe`可通过`PATH`找到。
2. 通过USB调试端口将SAM4S Xplained连接到主机，然后构建并烧录[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用。

  ```text
  # From the root of the zephyr repository
  west build -b sam4s_xplained samples/hello_world
  west flash
  ```

<a id="using-sam-ba-bootloader"></a>

#### 使用SAM-BA引导加载程序（Bootloader）


1. 短接SAM4S Xplained的J25跳线，给开发板上电10秒。
2. 断开J25跳线。
3. 通过SoC USB端口将SAM4S Xplained连接到主机，然后构建并烧录[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用。

  ```text
  # From the root of the zephyr repository
  west build -b sam4s_xplained samples/hello_world
  ```

  ```text
  $ west flash -r bossac
  ```

<a id="visualizing-the-message"></a>

#### 查看输出消息（Visualizing the Message）


1. 运行你惯用的终端程序，监听输出。Linux下的终端设备应为`/dev/ttyACM0`，例如：

  ```text
  $ minicom -D /dev/ttyACM0 -o
  ```

  `-o`选项让`minicom`不发送调制解调器初始化字符串（Modem Initialization String）。连接参数应配置如下：


  - 速率（Speed）：115200波特率
  - 数据位（Data）：8位
  - 奇偶校验（Parity）：无（None）
  - 停止位（Stop Bits）：1位
2. 按下复位按键。

  终端应显示`Hello World! sam4s_xplained`。

<a id="debugging"></a>

### 调试（Debugging）

可以按常规方式调试应用。下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b sam4s_xplained samples/hello_world
west debug
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.segger.com/downloads/jlink](https://www.segger.com/downloads/jlink)

<a id="id4"></a>

〔[2](#id5)〕 [http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4S-XPLD__KitsFiles.zip](http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4S-XPLD__KitsFiles.zip)

## 译注

原文时钟段落将板上的12 MHz振荡器称为internal oscillator，部分硬件列表也将32.768 kHz晶体称为internal；这里保留原始表述，不自行按器件资料改写。

原文USB调试接口条目在Data处结束，译文未补造后续词句。J-Link OB和SAM-BA两种烧录路径、J25跳线步骤分别保留。

---

[上一章](P003_SAM4L-EK.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_SAM_E70_B_Xplained.md)
