---
id: learning.zephyr-docs.boards-gd-to-iar.page-1
title: GD32A503V-EVAL
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/gd/gd32a503v_eval/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="gd32a503v_eval"></a>

# 第1章\_GD32A503V-EVAL

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/gd/gd32a503v_eval/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/gd32a503v_eval.jpg](images/gd32a503v_eval.jpg)](images/gd32a503v_eval.jpg)

GD32A503V-EVAL

名称（Name）：

`gd32a503v_eval`

厂商（Vendor）：

[兆易创新半导体（GigaDevice Semiconductor）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=gd)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[gd32a503](https://docs.zephyrproject.org/latest/boards/index.html#soc=gd32a503)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32a503v_eval/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

GD32A503V-EVAL是用于设计和调试兆易创新A503 Cortex-M4F高性能微控制器（High Performance MCU）的硬件平台。

GD32A503VD采用单核Arm Cortex-M4F MCU，最高120 MHz，支持闪存零等待状态（Zero Wait States）访问，提供384kiB Flash、48kiB SRAM及88个GPIO。

<a id="hardware"></a>

## 硬件（Hardware）


- 2个用户LED
- 两个用户按键
- 复位按键（Reset Button）
- 连接电位器（Potentiometer）的ADC
- 1个数模转换器（DAC）通道
- GD25Q16 2 Mib SPI闪存，单位按原文保留
- AT24C02C 2 KiB电可擦可编程只读存储器（EEPROM），容量按原文保留
- CS4344立体声数模转换器（Stereo DAC），带耳机放大器（Headphone Amplifier）
- GD-Link接口


  - 通过USB人机接口设备（HID）提供CMSIS-DAP串行线调试（SWD）接口。
- 2路CAN FD端口

GD32A503 SoC及GD32A503V-EVAL开发板更多信息见：


- [兆易创新Cortex-M33高性能SoC网站（High Performance SoC Website）](https://www.gigadevice.com.cn/product/mcu/arm-cortex-m33/gd32a503vdt3)
- [GD32A503数据手册（Datasheet）](https://www.gd32mcu.com/download/down/document_id/401/path_type/1)
- [GD32A503参考手册（Reference Manual）](https://www.gd32mcu.com/download/down/document_id/402/path_type/1)
- [GD32A503V评估板原理图（Eval Schematics）](https://www.gd32mcu.com/download/down/document_id/404/path_type/1)
- [GD32 ISP控制台（Console）](http://www.gd32mcu.com/download/down/document_id/175/path_type/1)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`gd32a503v_eval`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="gd32a503v_eval-hw-features"></a>

<a id="gd32a503v_eval-gd32a503v_eval/gd32a503-hw-features-section"></a>

#### `gd32a503v_eval/gd32a503`目标（Target）

<a id="gd32a503v_eval-gd32a503v_eval/gd32a503-hw-features-panel"></a>

<a id="gd32a503v_eval-gd32a503v_eval/gd32a503-hw-features-memory"></a>

该开发板目标的片上存储容量：48 KiB RAM、384 KiB Flash。

<a id="gd32a503v_eval-gd32a503v_eval/gd32a503-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L179">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L190">已禁用：1</a>）</td>
<td><a href="../hardware/P844_GD32模数转换器绑定.md#dtbinding-gd-gd32-adc"><code>gd,gd32-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>兆易创新复位与时钟单元（RCU）时钟控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L62">已启用：1</a>）</td>
<td><a href="../timer_reference/P184_GD32时钟控制绑定.md#dtbinding-gd-gd32-cctl"><code>gd,gd32-cctl</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L303">已禁用：7</a>）</td>
<td><a href="../counter_binding_reference/P018_gd_gd32-timer.md#std-dtcompatible-gd-gd32-timer"><code>gd,gd32-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32系列数模转换器（DAC）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L121">已启用：1</a>）</td>
<td><a href="../hardware/P761_GD32数模转换器绑定.md#dtbinding-gd-gd32-dac"><code>gd,gd32-dac</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>GD32直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L413">已禁用：2</a>）</td>
<td><a href="../dma_binding_reference/P017_gd_gd32-dma.md#std-dtcompatible-gd-gd32-dma"><code>gd,gd32-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>GD32闪存控制器（FMC）有三种类型（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P013_gd_gd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller"><code>gd,gd32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>GD32通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L242">已启用：6</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P027_gd_gd32-gpio.md#std-dtcompatible-gd-gd32-gpio"><code>gd,gd32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32 I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L131">已禁用：2</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P020_gd_gd32-i2c.md#std-dtcompatible-gd-gd32-i2c"><code>gd,gd32-i2c</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>兆易创新外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L207">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P007_gd_gd32-exti.md#std-dtcompatible-gd-gd32-exti"><code>gd,gd32-exti</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32a503v_eval/gd32a503v_eval.dts?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>兆易创新复位与时钟单元（RCU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L57">已启用：1</a>）</td>
<td><a href="../hardware/P705_GD32复位与时钟单元绑定.md#dtbinding-gd-gd32-rcu"><code>gd,gd32-rcu</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32系统配置寄存器（System Configuration Registers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L201">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P009_gd_gd32-syscfg.md#std-dtcompatible-gd-gd32-syscfg"><code>gd,gd32-syscfg</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L30">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>GD32 FMC v2的闪存绑定（Flash Memory Binding）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L83">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P017_gd_gd32-nv-flash-v2.md#std-dtcompatible-gd-gd32-nv-flash-v2"><code>gd,gd32-nv-flash-v2</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>这些属性用于支持Zephyr的<code>spi-nor</code>闪存驱动通过Zephyr SPI API，使用基于M25P80的标准命令集控制串行闪存（Serial Flash Memory）。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32a503v_eval/gd32a503v_eval.dts?plain=1#L96">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor"><code>jedec,spi-nor</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>GD32引脚控制器，复用功能模型（AF Model）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L235">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P024_gd_gd32-pinctrl-af.md#std-dtcompatible-gd-gd32-pinctrl-af"><code>gd,gd32-pinctrl-af</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L314">已禁用：5</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P018_gd_gd32-pwm.md#std-dtcompatible-gd-gd32-pwm"><code>gd,gd32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>兆易创新RCU复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L68">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P003_gd_gd32-rctl.md#std-dtcompatible-gd-gd32-rctl"><code>gd,gd32-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>兆易创新通用同步异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L94">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L103">已禁用：2</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P006_gd_gd32-usart.md#std-dtcompatible-gd-gd32-usart"><code>gd,gd32-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32 SPI（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L157">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L168">已禁用：1</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P016_gd_gd32-spi.md#std-dtcompatible-gd-gd32-spi"><code>gd,gd32-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>GD32独立看门狗定时器（Free Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L220">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P015_gd_gd32-fwdgt.md#std-dtcompatible-gd-gd32-fwdgt"><code>gd,gd32-fwdgt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>GD32窗口看门狗定时器（Window Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/gd/gd32a50x/gd32a50x.dtsi?plain=1#L226">已禁用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P016_gd_gd32-wwdgt.md#std-dtcompatible-gd-gd32-wwdgt"><code>gd,gd32-wwdgt</code></a></td>
</tr>
</table>

<a id="serial-port"></a>

### 串口（Serial Port）

GD32A503V-EVAL有3个串行通信端口，默认端口为UART0，位于PIN-72及PIN-73。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`gd32a503v_eval`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>gd32isp</td>
<td>✅</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-pyocd">pyocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

编程前，确认已配置启动设置及串口，默认串口为USART0。

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

<a id="using-gd-link"></a>

### 使用GD-Link

GD32A503V-EVAL带有板载GD-Link编程器／调试器，可通过USB烧录和调试。还提供J2及J100编程调试排针，可配合任何兼容Arm的工具使用。


1. 构建Zephyr内核和[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例应用：

  ```text
  west build -b gd32a503v_eval samples/hello_world
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
  west build -b gd32a503v_eval samples/hello_world
  west flash
  ```

  终端应显示“Hello World! gd32a503v_eval”。
4. 调试镜像的方法：

  ```text
  west build -b gd32a503v_eval samples/hello_world
  west debug
  ```

<a id="using-rom-bootloader"></a>

### 使用ROM引导程序（Bootloader）

GD32A503 MCU具有可烧录闪存的ROM引导程序（Bootloader）。应将[GD32 ISP Console](http://www.gd32mcu.com/download/down/document_id/175/path_type/1)软件安装到Linux目录中，推荐使用`$HOME/.local/bin`。


1. 构建Zephyr内核和[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例应用：

  ```text
  west build -b gd32a503v_eval samples/hello_world
  ```
2. 启用开发板引导程序：


  - 移除boot-0跳线
  - 按下复位键
3. 烧录镜像：

  ```text
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

  终端应显示“Hello World! gd32a503v_eval”。

## 译注

GD32A503正文内核为Cortex-M4F，而参考链接标签写Cortex-M33；按原文分别保留。GD25Q16的2Mib及AT24C02C的2KiB也沿用原文单位，不推算替换。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [1](https://www.gd32mcu.com/download/down/document_id/404/path_type/1)：HTTP Error 302: The HTTP server returned a redirect error that would lead to an infinite loop. The last 30x error message was: Moved Temporarily。

---

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_GD32C231C-EVAL.md)
