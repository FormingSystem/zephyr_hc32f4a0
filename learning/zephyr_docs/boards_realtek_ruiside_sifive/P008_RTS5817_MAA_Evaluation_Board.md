---
id: learning.zephyr-docs.boards-realtek-ruiside-sifive.page-8
title: RTS5817 MAA Evaluation Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/realtek/rts5817_maa_evb/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rts5817_maa_evb"></a>

# 第8章\_RTS5817 MAA评估板（Evaluation Board）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/realtek/rts5817_maa_evb/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/rts5817_maa_evb.webp](images/rts5817_maa_evb.webp)](images/rts5817_maa_evb.webp)

RTS5817 MAA评估板（Evaluation Board）

名称（Name）：

`rts5817_maa_evb`

厂商（Vendor）：

[Realtek Semiconductor Corp.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=realtek)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[rts5817](https://docs.zephyrproject.org/latest/boards/index.html#soc=rts5817)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/realtek/rts5817_maa_evb/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

RTS5817 MAA EVB是用于评估Realtek RTS5817 MAA指纹芯片的开发平台，该芯片包含高性能MCU及指纹传感器。

[![官方原图：rts5817_maa_evb](images/rts5817_maa_evb1.webp)](images/rts5817_maa_evb1.webp)

<a id="hardware"></a>

## 硬件（Hardware）


- 240 MHz单核32位CPU，带32 KB指令缓存（I-Cache）及16 KB数据缓存（D-Cache）
- 48 KB启动ROM（Boot ROM）
- 256 KB片上SRAM
- 1 KB PUFrt一次性可编程存储器（OTP）
- 2 MB闪存
- USB 2.0全速／高速设备
- 最多11个GPIO
- 2路UART
- 2个定时器
- 2路SPI，其中一路支持从机模式（Slave Mode）
- 看门狗（Watchdog）
- 直接存储器访问（DMA）
- 温度传感器（Temperature Sensor）。
- 密码运算硬件加速：随机数（RNG）、SHA及AES
- 指纹匹配硬件加速，包括乘累加（MAC）、置位计数（Popcount）、卷积（Convolution）等
- SWD调试接口

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`rts5817_maa_evb`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="rts5817_maa_evb-hw-features"></a>

<a id="rts5817_maa_evb-rts5817_maa_evb/rts5817-hw-features-section"></a>

#### `rts5817_maa_evb/rts5817`目标（Target）

<a id="rts5817_maa_evb-rts5817_maa_evb/rts5817-hw-features-panel"></a>

<a id="rts5817_maa_evb-rts5817_maa_evb/rts5817-hw-features-memory"></a>

该开发板目标的片上存储容量：256 KiB RAM、2 MiB Flash。

<a id="rts5817_maa_evb-rts5817_maa_evb/rts5817-hw-features-table"></a>

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
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817_base.dtsi?plain=1#L24">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5817时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817_base.dtsi?plain=1#L58">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P023_realtek_rts5817-clock.md#std-dtcompatible-realtek-rts5817-clock"><code>realtek,rts5817-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>RTS5817 GPIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817_base.dtsi?plain=1#L83">已禁用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P012_realtek_rts5817-gpio.md#std-dtcompatible-realtek-rts5817-gpio"><code>realtek,rts5817-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">非易失存储器（NVMEM）</td>
<td>片上（On-Chip）</td>
<td>非易失存储器固定布局（Fixed Layout for Non-Volatile Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817_base.dtsi?plain=1#L161">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P009_fixed-layout.md#std-dtcompatible-fixed-layout"><code>fixed-layout</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>RTS5817片上一次性可编程存储器（OTP）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817_base.dtsi?plain=1#L152">已禁用：1</a>）</td>
<td><a href="../otp_binding_reference/P007_realtek_rts5817-ocotp.md#std-dtcompatible-realtek-rts5817-ocotp"><code>realtek,rts5817-ocotp</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5817系列引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817_base.dtsi?plain=1#L74">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P004_realtek_rts5817-pinctrl.md#std-dtcompatible-realtek-rts5817-pinctrl"><code>realtek,rts5817-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5817内核及指纹传感器电源稳压器（Regulator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817_base.dtsi?plain=1#L125">已禁用：1</a>）</td>
<td><a href="../hardware/P678_RTS5817稳压器绑定.md#dtbinding-realtek-rts5817-regulator"><code>realtek,rts5817-regulator</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5817外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817_base.dtsi?plain=1#L67">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P013_realtek_rts5817-reset.md#std-dtcompatible-realtek-rts5817-reset"><code>realtek,rts5817-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817_base.dtsi?plain=1#L103">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817_base.dtsi?plain=1#L114">已禁用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817_base.dtsi?plain=1#L214">已禁用：2</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P008_snps_designware-spi.md#std-dtcompatible-snps-designware-spi"><code>snps,designware-spi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek RTS5817 SPI封装节点（Wrapper Node）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817_base.dtsi?plain=1#L242">已禁用：2</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P013_realtek_rts5817-spi.md#std-dtcompatible-realtek-rts5817-spi"><code>realtek,rts5817-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817_base.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>系统控制器寄存器读写（System Controller Registers R/W）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817_base.dtsi?plain=1#L44">已启用：2</a>）</td>
<td><a href="../edac_syscon_binding_reference/P008_syscon.md#std-dtcompatible-syscon"><code>syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5817看门狗驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/fingerprint/rts5817/rts5817_base.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P003_realtek_rts5817-watchdog.md#std-dtcompatible-realtek-rts5817-watchdog"><code>realtek,rts5817-watchdog</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`rts5817_maa_evb`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
<tr>
<td>rtsflash</td>
<td>✅（默认 / default）</td>
<td></td>
</tr>
</table>

<a id="building"></a>

### 构建（Building）


1. 按通常方式构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用。

```text
# From the root of the zephyr repository
west build -b rts5817_maa_evb samples/hello_world
```


1. 构建成功后生成zephyr.rts5817.bin，二进制镜像位于build/zephyr/目录。

<a id="flashing"></a>

### 烧录（Flashing）


1. <a id="id3"></a>

  短接J6的两个引脚以进入强制ROM模式（Force ROM Mode），见[RTS5817MAA_EVB_User_Guide](https://github.com/RtkFP/Doc/blob/main/RTS5817MAA_EVB%20User%20Guide_V1.0.pdf) [注1](#id2)。
2. 通过USB将开发板连接主机。
3. 使用west flash命令烧录镜像。
4. 断开J6两个引脚并重启，[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用开始运行。

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://github.com/RtkFP/Doc/blob/main/RTS5817MAA_EVB%20User%20Guide_V1.0.pdf](https://github.com/RtkFP/Doc/blob/main/RTS5817MAA_EVB%20User%20Guide_V1.0.pdf)

## 译注

RTS5817 MAA输出zephyr.rts5817.bin；J6短接进入强制ROM模式，写入后断开J6再重启。

---

[上一章](P007_RTL87x2G_Model_A_Evaluation_Board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_RTS5912_Evaluation_Board.md)
