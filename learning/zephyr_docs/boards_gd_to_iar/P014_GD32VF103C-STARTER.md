---
id: learning.zephyr-docs.boards-gd-to-iar.page-14
title: GD32VF103C-STARTER
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/gd/gd32vf103c_starter/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="gd32vf103c_starter"></a>

# 第14章\_GD32VF103C-STARTER

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/gd/gd32vf103c_starter/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/gd32vf103c_starter.jpg](images/gd32vf103c_starter.jpg)](images/gd32vf103c_starter.jpg)

GD32VF103C-STARTER

名称（Name）：

`gd32vf103c_starter`

厂商（Vendor）：

[兆易创新半导体（GigaDevice Semiconductor）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=gd)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[gd32vf103](https://docs.zephyrproject.org/latest/boards/index.html#soc=gd32vf103)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32vf103c_starter/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

GD32VF103C-STARTER是用于GD32VF103CB RISC-V微控制器原型开发（Prototyping）的硬件平台。

GD32VF103CB采用单核32位RISC-V MCU，最高108 MHz，支持闪存零等待状态访问，提供128 KiB Flash、32 KiB SRAM及37个GPIO。

<a id="hardware"></a>

## 硬件（Hardware）


- GD32VF103CBT6微控制器（MCU）
- 1个用户LED
- 1路USART，通过带CH340E的USB端口连接
- USB全速（FS）接口
- 板载GD-Link编程器（Programmer）
- J-Link／JTAG连接器

GD32VF103 SoC及GD32VF103C-STARTER开发板更多信息见：


- [兆易创新RISC-V主流SoC网站（Mainstream SoC Website）](https://www.gigadevice.com/products/microcontrollers/gd32/risc-v/mainstream-line/)
- [GD32VF103数据手册（Datasheet）](https://www.gigadevice.com/datasheet/gd32vf103xxxx-datasheet/)
- [GD32VF103用户手册（User Manual）](http://www.gd32mcu.com/download/down/document_id/222/path_type/1)
- [GD32VF103C-STARTER文档（Documents）](https://github.com/riscv-mcu/GD32VF103_Demo_Suites/tree/master/GD32VF103C_START_Demo_Suites/Docs)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`gd32vf103c_starter`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="gd32vf103c_starter-hw-features"></a>

<a id="gd32vf103c_starter-gd32vf103c_starter/gd32vf103-hw-features-section"></a>

#### `gd32vf103c_starter/gd32vf103`目标（Target）

<a id="gd32vf103c_starter-gd32vf103c_starter/gd32vf103-hw-features-panel"></a>

<a id="gd32vf103c_starter-gd32vf103c_starter/gd32vf103-hw-features-memory"></a>

该开发板目标的片上存储容量：32 KiB RAM、128 KiB Flash。

<a id="gd32vf103c_starter-gd32vf103c_starter/gd32vf103-hw-features-table"></a>

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
<td>芯来（Nuclei）Bumblebee RISC-V内核（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P023_nuclei_bumblebee.md#std-dtcompatible-nuclei-bumblebee"><code>nuclei,bumblebee</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L142">已禁用：2</a>）</td>
<td><a href="../hardware/P844_GD32模数转换器绑定.md#dtbinding-gd-gd32-adc"><code>gd,gd32-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>兆易创新复位与时钟单元（RCU）时钟控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L67">已启用：1</a>）</td>
<td><a href="../timer_reference/P184_GD32时钟控制绑定.md#dtbinding-gd-gd32-cctl"><code>gd,gd32-cctl</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L338">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L303">已禁用：6</a>）</td>
<td><a href="../counter_binding_reference/P018_gd_gd32-timer.md#std-dtcompatible-gd-gd32-timer"><code>gd,gd32-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32系列数模转换器（DAC）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L164">已禁用：1</a>）</td>
<td><a href="../hardware/P761_GD32数模转换器绑定.md#dtbinding-gd-gd32-dac"><code>gd,gd32-dac</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>GD32直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L411">已禁用：2</a>）</td>
<td><a href="../dma_binding_reference/P017_gd_gd32-dma.md#std-dtcompatible-gd-gd32-dma"><code>gd,gd32-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>GD32闪存控制器（FMC）有三种类型（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L80">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P013_gd_gd32-flash-controller.md#std-dtcompatible-gd-gd32-flash-controller"><code>gd,gd32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>GD32通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L252">已启用：4</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L282">已禁用：1</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P027_gd_gd32-gpio.md#std-dtcompatible-gd-gd32-gpio"><code>gd,gd32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32 I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L174">已禁用：1</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P020_gd_gd32-i2c.md#std-dtcompatible-gd-gd32-i2c"><code>gd,gd32-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32vf103c_starter/gd32vf103c_starter.dts?plain=1#L33">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>芯来增强型内核本地中断控制器（Nuclei ECLIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L54">已启用：1</a>）</td>
<td><a href="../riscv_interrupt_binding_reference/P005_nuclei_eclic.md#std-dtcompatible-nuclei-eclic"><code>nuclei,eclic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>兆易创新外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L216">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P007_gd_gd32-exti.md#std-dtcompatible-gd-gd32-exti"><code>gd,gd32-exti</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32vf103c_starter/gd32vf103c_starter.dts?plain=1#L24">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/gd/gd32vf103c_starter/gd32vf103c_starter.dts?plain=1#L43">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>兆易创新复位与时钟单元（RCU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L62">已启用：1</a>）</td>
<td><a href="../hardware/P705_GD32复位与时钟单元绑定.md#dtbinding-gd-gd32-rcu"><code>gd,gd32-rcu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>GD32 FMC v1的闪存绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L87">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P016_gd_gd32-nv-flash-v1.md#std-dtcompatible-gd-gd32-nv-flash-v1"><code>gd,gd32-nv-flash-v1</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>GD32复用功能输入输出（AFIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L209">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P023_gd_gd32-afio.md#std-dtcompatible-gd-gd32-afio"><code>gd,gd32-afio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>GD32引脚控制器，AFIO模型（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L245">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P025_gd_gd32-pinctrl-afio.md#std-dtcompatible-gd-gd32-pinctrl-afio"><code>gd,gd32-pinctrl-afio</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L348">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L314">已禁用：4</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P018_gd_gd32-pwm.md#std-dtcompatible-gd-gd32-pwm"><code>gd,gd32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>兆易创新RCU复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L73">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P003_gd_gd32-rctl.md#std-dtcompatible-gd-gd32-rctl"><code>gd,gd32-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>兆易创新通用同步异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L97">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L106">已禁用：4</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P006_gd_gd32-usart.md#std-dtcompatible-gd-gd32-usart"><code>gd,gd32-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>兆易创新GD32 SPI（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L187">已禁用：2</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P016_gd_gd32-spi.md#std-dtcompatible-gd-gd32-spi"><code>gd,gd32-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L35">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>芯来系统定时器（Nuclei System Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../system_timer_binding_reference/P012_nuclei_systimer.md#std-dtcompatible-nuclei-systimer"><code>nuclei,systimer</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>GD32独立看门狗定时器（Free Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L230">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P015_gd_gd32-fwdgt.md#std-dtcompatible-gd-gd32-fwdgt"><code>gd,gd32-fwdgt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>GD32窗口看门狗定时器（Window Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/gd/gd32vf103.dtsi?plain=1#L236">已禁用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P016_gd_gd32-wwdgt.md#std-dtcompatible-gd-gd32-wwdgt"><code>gd,gd32-wwdgt</code></a></td>
</tr>
</table>

<a id="serial-port"></a>

### 串口（Serial Port）

GD32VF103C-STARTER有一个串行通信端口，TX接PA9、RX接PA10。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`gd32vf103c_starter`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>调试服务器（debugserver）</th>
<th>复位（reset）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-jlink">jlink</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
</table>

编程前，按以下要求设置启动和串口跳线：


- JP2／3：均选择2–3位置，从用户存储器启动
- JP5／6：选择1–2位置，标为USART0

<a id="using-gd-link"></a>

### 使用GD-Link

GD32VF103C-STARTER带有板载GD-Link编程器／调试器，可通过USB烧录和调试。另有JTAG排针JP1，可配合Segger J-Link等工具使用。


1. 构建Zephyr内核和[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例应用：

  ```text
  west build -b gd32vf103c_starter samples/hello_world
  ```
2. 启动串口终端监听输出。在Linux下，设备名通常类似`/dev/ttyUSB0`。例如：

  ```text
  minicom -D /dev/ttyUSB0 -o
  ```

  `-o`选项让`minicom`不发送调制解调器初始化字符串（Modem Initialization String）。连接参数应配置如下：

  > - 速率（Speed）：115200波特率
  > - 数据位（Data）：8位
  > - 奇偶校验（Parity）：无（None）
  > - 停止位（Stop Bits）：1位
3. 烧录镜像：

  ```text
  west build -b gd32vf103c_starter samples/hello_world
  west flash
  ```

  终端应显示“Hello World! gd32vf103c_starter”。
4. 调试镜像的方法：

  ```text
  west build -b gd32vf103c_starter samples/hello_world
  west debug
  ```

---

[上一章](P013_GD32L233R-EVA.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P015_GD32VF103V-EVAL.md)
