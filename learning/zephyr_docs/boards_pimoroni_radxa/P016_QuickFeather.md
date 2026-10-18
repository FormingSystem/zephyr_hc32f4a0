---
id: learning.zephyr-docs.boards-pimoroni-radxa.page-16
title: QuickFeather
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/quicklogic/quick_feather/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="quick_feather"></a>

# 第16章\_QuickFeather

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/quicklogic/quick_feather/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/feather-board.jpg](images/feather-board.jpg)](images/feather-board.jpg)

QuickFeather

名称（Name）：

`quick_feather`

厂商（Vendor）：

[QuickLogic Corp.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=quicklogic)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[quicklogic_eos_s3](https://docs.zephyrproject.org/latest/boards/index.html#soc=quicklogic_eos_s3)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/quicklogic/quick_feather/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

QuickFeather开发板搭载QuickLogic EOS S3传感器处理平台（Sensor Processing Platform）。

<a id="hardware"></a>

## 硬件（Hardware）


- QuickLogic EOS S3 MCU平台
- mCube MC3635加速度传感器（Accelerometer）
- Infineon DPS310压力传感器（Pressure Sensor）
- Infineon IM69D130微机电系统（MEMS）麦克风
- 16 Mbit板载闪存
- 用户按键（User Button）
- RGB发光二极管（LED）
- 集成电池充电器

<a id="id3"></a>

详细板卡资料见[QuickFeather仓库](https://github.com/QuickLogic-Corp/quick-feather-dev-board)[注1](#id2)。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`quick_feather`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="quick_feather-hw-features"></a>

<a id="quick_feather-quick_feather/quicklogic_eos_s3-hw-features-section"></a>

#### `quick_feather/quicklogic_eos_s3`目标（Target）

<a id="quick_feather-quick_feather/quicklogic_eos_s3-hw-features-panel"></a>

<a id="quick_feather-quick_feather/quicklogic_eos_s3-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、N/A Flash。

<a id="quick_feather-quick_feather/quicklogic_eos_s3-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L37">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>EOS S3通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L58">已启用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P002_quicklogic_eos-s3-gpio.md#std-dtcompatible-quicklogic-eos-s3-gpio"><code>quicklogic,eos-s3-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/quicklogic/quick_feather/quick_feather.dts?plain=1#L49">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/quicklogic/quick_feather/quick_feather.dts?plain=1#L30">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>QuickLogic EOS S3输入输出复用（IO MUX）绑定覆盖46个IOMUX_PAD_x_CTRL寄存器，可用于设置焊盘方向及功能。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L69">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P024_quicklogic_eos-s3-pinctrl.md#std-dtcompatible-quicklogic-eos-s3-pinctrl"><code>quicklogic,eos-s3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L44">已启用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>QuickLogic USBserialport_S3B串行接口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L52">已禁用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P020_quicklogic_usbserialport-s3b.md#std-dtcompatible-quicklogic-usbserialport-s3b"><code>quicklogic,usbserialport-s3b</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/quicklogic/quicklogic_eos_s3.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
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

<a id="id5"></a>

详细引脚排列见原理图文档[注2](#id4)。（[原理图文档（Schematics）](https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/quickfeather-board.pdf)）

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`quick_feather`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

<a id="flashing"></a>

### 烧录（Flashing）

QuickFeather平台默认从闪存启动。目前Zephyr移植仅支持使用OpenOCD配合SWD编程器，或使用SEGGER J-Link，将程序直接加载至SRAM。

<a id="openocd"></a>

#### OpenOCD

连接目标需要OpenOCD支持的串行线调试（SWD）编程器。运行以下命令连接开发板：

```text
openocd -f /path/to/swd-programmer.cfg -f tcl/board/quicklogic_quickfeather.cfg -c "init" -c "reset halt"
```

<a id="id7"></a>

[QuickFeather的OpenOCD配置](https://sourceforge.net/p/openocd/code/ci/master/tree/tcl/board/quicklogic_quickfeather.cfg)[注3](#id6)位于OpenOCD主线仓库。

<a id="jlink"></a>

#### JLink

<a id="id9"></a>

通过J-Link连接QuickFeather时，请遵循[QuickFeather用户指南](https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/QuickFeather_UserGuide.pdf)[注4](#id8)中的说明。

<a id="debugging"></a>

### 调试（Debugging）

调试QuickFeather时，先通过OpenOCD或J-Link连接目标，再使用Zephyr SDK中arm-zephyr-eabi/bin目录下随附的GDB。

通过GDB加载基本示例：


- 按常规方式构建示例：

```text
# From the root of the zephyr repository
west build -b quick_feather samples/hello_world
```


- 使用OpenOCD或J-Link连接目标。
- 通过GDB连接并加载ELF文件：

```text
/path/to/zephyr-sdk/arm-zephyr-eabi/bin/arm-zephyr-eabi-gdb
target remote <port_number>
file </path/to/zephyr.elf>
load
continue
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://github.com/QuickLogic-Corp/quick-feather-dev-board](https://github.com/QuickLogic-Corp/quick-feather-dev-board)

<a id="id4"></a>

〔[2](#id5)〕 [https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/quickfeather-board.pdf](https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/quickfeather-board.pdf)

<a id="id6"></a>

〔[3](#id7)〕 [https://sourceforge.net/p/openocd/code/ci/master/tree/tcl/board/quicklogic_quickfeather.cfg](https://sourceforge.net/p/openocd/code/ci/master/tree/tcl/board/quicklogic_quickfeather.cfg)

<a id="id8"></a>

〔[4](#id9)〕 [https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/QuickFeather_UserGuide.pdf](https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/QuickFeather_UserGuide.pdf)

## 译注

QuickFeather硬件默认从闪存启动，但当前Zephyr移植仅支持由OpenOCD／SWD或J-Link直接加载至SRAM；保留这一限制及GDB加载顺序。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [quicklogic_quickfeather.cfg](https://sourceforge.net/p/openocd/code/ci/master/tree/tcl/board/quicklogic_quickfeather.cfg)：HTTP Error 403: Forbidden。

---

[上一章](P015_Qomu.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P017_Radxa.md)
