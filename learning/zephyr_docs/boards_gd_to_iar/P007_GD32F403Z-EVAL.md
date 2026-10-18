---
id: learning.zephyr-docs.boards-gd-to-iar.page-7
title: GD32F403Z-EVAL
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/gd/gd32f403z_eval/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="gd32f403z_eval"></a>

# 第7章\_GD32F403Z-EVAL

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/gd/gd32f403z_eval/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/gd32f403z_eval.jpg](images/gd32f403z_eval.jpg)](images/gd32f403z_eval.jpg)

GD32F403Z-EVAL

名称（Name）：

`gd32f403z_eval`

厂商（Vendor）：

[兆易创新半导体（GigaDevice Semiconductor）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=gd)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[gd32f403](https://docs.zephyrproject.org/latest/boards/index.html#soc=gd32f403)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32f403z_eval/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

GD32F403Z-EVAL是用于设计和调试兆易创新F403 Cortex-M4F高性能微控制器（High Performance MCU）的硬件平台。

GD32F403ZE采用单核Arm Cortex-M4F MCU，最高168 MHz，支持闪存零等待状态（Zero Wait States）访问，提供512kiB Flash、96kiB SRAM及112个GPIO。

<a id="hardware"></a>

## 硬件（Hardware）


- 带Mini-USB连接器的USB接口
- 4个用户LED
- 4个用户按键
- 复位按键（Reset Button）
- CAN端口
- 连接电位器（Potentiometer）的ADC
- 2个DAC通道
- GD25Q40 4 Mib SPI闪存
- HY27UF081G2A 1 GiB NAND闪存，容量按原文保留
- AT24C02C 2 KiB电可擦可编程只读存储器（EEPROM），容量按原文保留
- 3.2英寸TFT LCD，320 × 240
- PCM1770立体声DAC，带耳机放大器
- Micro-SDHC接口
- GD-Link接口


  - 通过USB人机接口设备（HID）提供CMSIS-DAP串行线调试（SWD）接口。

GD32F403 SoC及GD32F403Z-Eval开发板更多信息见：


- [兆易创新Cortex-M4F高性能SoC网站（High Performance SoC Website）](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m4/high-performance-line/gd32f403-series/)
- [GD32F403数据手册（Datasheet）](https://gd32mcu.com/data/documents/datasheet/GD32F403xx_Datasheet_Rev1.3.pdf)
- [GD32F403参考手册（Reference Manual）](https://gd32mcu.com/data/documents/userManual/GD32F403_User_Manual_Rev2.6.pdf)
- [GD32F403Z评估板原理图（Eval Schematics）](http://www.gd32mcu.com/download/down/document_id/270/path_type/1)
- [GD32 ISP控制台（Console）](http://www.gd32mcu.com/download/down/document_id/175/path_type/1)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`gd32f403z_eval`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="gd32f403z_eval-hw-features"></a>

<a id="gd32f403z_eval-gd32f403z_eval/gd32f403-hw-features-section"></a>

#### `gd32f403z_eval/gd32f403`目标（Target）

<a id="gd32f403z_eval-gd32f403z_eval/gd32f403-hw-features-panel"></a>

<a id="gd32f403z_eval-gd32f403z_eval/gd32f403-hw-features-memory"></a>

该开发板目标的片上存储容量：96 KiB RAM、512 KiB Flash。

<a id="gd32f403z_eval-gd32f403z_eval/gd32f403-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L160">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L171">已禁用：2</a>）</td>
<td><a href="../hardware/P844_GD32模数转换器绑定.md#dtbinding-gd-gd32-adc"><code>gd,gd32-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>兆易创新复位与时钟单元（RCU）时钟控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L51">已启用：1</a>）</td>
<td><a href="../timer_reference/P184_GD32时钟控制绑定.md#dtbinding-gd-gd32-cctl"><code>gd,gd32-cctl</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L307">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L325">已禁用：11</a>）</td>
<td><a href="../counter_binding_reference/P018_gd_gd32-timer.md#std-dtcompatible-gd-gd32-timer"><code>gd,gd32-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>GD32直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L501">已禁用：2</a>）</td>
<td><a href="../dma_binding_reference/P017_gd_gd32-dma.md#std-dtcompatible-gd-gd32-dma"><code>gd,gd32-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>GD32闪存控制器（FMC）有三种类型（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L64">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P013_gd_gd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller"><code>gd,gd32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>GD32通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L236">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L246">已禁用：4</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P027_gd_gd32-gpio.md#std-dtcompatible-gd-gd32-gpio"><code>gd,gd32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f403z_eval/gd32f403z_eval.dts?plain=1#L48">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>兆易创新外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L193">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P007_gd_gd32-exti.md#std-dtcompatible-gd-gd32-exti"><code>gd,gd32-exti</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f403z_eval/gd32f403z_eval.dts?plain=1#L24">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32f403z_eval/gd32f403z_eval.dts?plain=1#L76">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>兆易创新复位与时钟单元（RCU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../hardware/P705_GD32复位与时钟单元绑定.md#dtbinding-gd-gd32-rcu"><code>gd,gd32-rcu</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>GD32 FMC v2的闪存绑定（Flash Memory Binding）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L71">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P017_gd_gd32-nv-flash-v2.md#std-dtcompatible-gd-gd32-nv-flash-v2"><code>gd,gd32-nv-flash-v2</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>GD32复用功能输入输出（AFIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L207">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P023_gd_gd32-afio.md#std-dtcompatible-gd-gd32-afio"><code>gd,gd32-afio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>GD32引脚控制器，AFIO模型（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L229">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P025_gd_gd32-pinctrl-afio.md#std-dtcompatible-gd-gd32-pinctrl-afio"><code>gd,gd32-pinctrl-afio</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L318">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L335">已禁用：9</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P018_gd_gd32-pwm.md#std-dtcompatible-gd-gd32-pwm"><code>gd,gd32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>兆易创新RCU复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L57">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P003_gd_gd32-rctl.md#std-dtcompatible-gd-gd32-rctl"><code>gd,gd32-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>兆易创新通用同步异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L82">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L91">已禁用：4</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P006_gd_gd32-usart.md#std-dtcompatible-gd-gd32-usart"><code>gd,gd32-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32 SPI（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L127">已禁用：3</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P016_gd_gd32-spi.md#std-dtcompatible-gd-gd32-spi"><code>gd,gd32-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>GD32独立看门狗定时器（Free Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L214">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P015_gd_gd32-fwdgt.md#std-dtcompatible-gd-gd32-fwdgt"><code>gd,gd32-fwdgt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>GD32窗口看门狗定时器（Window Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32f403/gd32f403.dtsi?plain=1#L220">已禁用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P016_gd_gd32-wwdgt.md#std-dtcompatible-gd-gd32-wwdgt"><code>gd,gd32-wwdgt</code></a></td>
</tr>
</table>

<a id="serial-port"></a>

### 串口（Serial Port）

GD32F403Z-EVAL有5个串行通信端口，默认端口为UART0，位于PIN-9及PIN-10。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`gd32f403z_eval`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>调试服务器（debugserver）</th>
</tr>
<tr>
<td>gd32isp</td>
<td>✅</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

编程前，确认已配置启动设置及串口，默认串口为USART0。此端口通过JP-5／6排针在USB VBUS／ID与USART J2之间选择信号路由。

<table>
<tr>
<th>Boot-0</th>
<th>Boot-1</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>1-2</td>
<td>1-2</td>
<td>静态随机存储器（SRAM）</td>
</tr>
<tr>
<td>1-2</td>
<td>2-3</td>
<td>引导加载程序（Bootloader）</td>
</tr>
<tr>
<td>2-3</td>
<td>任意（Any）</td>
<td>闪存（Flash）</td>
</tr>
</table>

<table>
<tr>
<th>JP-5</th>
<th>JP-6</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>1-2</td>
<td>1-2</td>
<td>USART0／J2</td>
</tr>
<tr>
<td>2-3</td>
<td>2-3</td>
<td>USB VBUS／ID</td>
</tr>
<tr>
<td>断开（open）</td>
<td>断开（open）</td>
<td>空闲（Free）</td>
</tr>
</table>

<a id="using-gd-link"></a>

### 使用GD-Link

GD32F403Z-EVAL带有板载GD-Link编程器／调试器，可通过USB烧录和调试。还提供J1及J100编程调试排针，可配合任何兼容Arm的工具使用。


1. 构建Zephyr内核和[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例应用：

  ```text
  west build -b gd32f403z_eval samples/hello_world
  ```
2. 运行你惯用的终端程序，监听输出。Linux下的终端设备应为`/dev/ttyUSB0`，例如：

  ```text
  $ minicom -D /dev/ttyUSB0 -o
  ```

  `-o`选项让`minicom`不发送调制解调器初始化字符串（Modem Initialization String）。连接参数应配置如下：

  > - 速率（Speed）：115200波特率
  > - 数据位（Data）：8位
  > - 奇偶校验（Parity）：无（None）
  > - 停止位（Stop Bits）：1位
3. 烧录镜像：

  ```text
  west build -b gd32f403z_eval samples/hello_world
  west flash
  ```

  终端应显示“Hello World! gd32f403z_eval”。
4. 调试镜像的方法：

  ```text
  west build -b gd32f403z_eval samples/hello_world
  west debug
  ```

<a id="using-rom-bootloader"></a>

### 使用ROM引导程序（Bootloader）

GD32F403 MCU具有可烧录闪存的ROM引导程序（Bootloader）。应将[GD32 ISP Console](http://www.gd32mcu.com/download/down/document_id/175/path_type/1)软件安装到Linux目录中，推荐使用`$HOME/.local/bin`。


1. 构建Zephyr内核和[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例应用：

  ```text
  west build -b gd32f403z_eval samples/hello_world
  ```
2. 启用开发板引导程序：


  - 移除boot-0跳线
  - 按下复位键
3. 烧录镜像：

  ```text
  west build -b gd32f403z_eval samples/hello_world
  west flash -r gd32isp [--port=/dev/ttyUSB0]
  ```
4. 运行你惯用的终端程序，监听输出。Linux下的终端设备应为`/dev/ttyUSB0`，例如：

  ```text
  $ minicom -D /dev/ttyUSB0 -o
  ```

  `-o`选项让`minicom`不发送调制解调器初始化字符串（Modem Initialization String）。连接参数应配置如下：

  > - 速率（Speed）：115200波特率
  > - 数据位（Data）：8位
  > - 奇偶校验（Parity）：无（None）
  > - 停止位（Stop Bits）：1位

  按下复位按键。

  终端应显示“Hello World! gd32f403z_eval”。

## 译注

原文HY27UF081G2A容量写1GiB，按原文保留，未据其他芯片资料修改。

---

[上一章](P006_GD32F350R-EVAL.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P008_GD32F407V-START.md)
