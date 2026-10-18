---
id: learning.zephyr-docs.boards-realtek-ruiside-sifive.page-9
title: RTS5912 Evaluation Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/realtek/rts5912_evb/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rts5912_evb"></a>

# 第9章\_RTS5912评估板（Evaluation Board）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/realtek/rts5912_evb/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/rts5912evb.webp](images/rts5912evb.webp)](images/rts5912evb.webp)

RTS5912评估板（Evaluation Board）

名称（Name）：

`rts5912_evb`

厂商（Vendor）：

[Realtek Semiconductor Corp.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=realtek)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[rts5912](https://docs.zephyrproject.org/latest/boards/index.html#soc=rts5912)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/realtek/rts5912_evb/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

RTS5912 EVB是用于评估Realtek RTS5912嵌入式控制器（Embedded Controller）的开发平台。

<a id="hardware"></a>

## 硬件（Hardware）


- Realtek-M300处理器，兼容Cortex-M33
- 存储器（Memory）：

  > - 384 KB静态随机存储器（SRAM）
  > - 64 KB ROM
  > - 512 KB多芯片模块（MCM）闪存
  > - 256 B电池供电SRAM（Battery SRAM）
- 平台环境控制接口（PECI）3.1
- FAN、PWM及TACHO引脚
- 6个I2C实例
- eSPI排针
- 一个PS/2端口
- 键盘接口排针

<a id="id3"></a>

<a id="id5"></a>

更多板卡信息见[RTS5912_EVB_Schematics](https://github.com/JasonLin-RealTek/Realtek_EC/blob/main/RTS5912_EVB_Schematic_Ver%201.1_20240701_1407.pdf) [注1](#id2)及[RTS5912_DATASHEET](https://github.com/JasonLin-RealTek/Realtek_EC/blob/main/RTS5912_datasheet_brief.pdf) [注2](#id4)。

开发板通过+5 V USB Type-C连接器或电源适配器供电。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`rts5912_evb`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="rts5912_evb-hw-features"></a>

<a id="rts5912_evb-rts5912_evb/rts5912-hw-features-section"></a>

#### `rts5912_evb/rts5912`目标（Target）

<a id="rts5912_evb-rts5912_evb/rts5912-hw-features-panel"></a>

<a id="rts5912_evb-rts5912_evb/rts5912-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、256 KiB Flash。

<a id="rts5912_evb-rts5912_evb/rts5912-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L266">已启用：1</a>）</td>
<td><a href="../hardware/P897_RealtekRTS5912模数转换器绑定.md#dtbinding-realtek-rts5912-adc"><code>realtek,rts5912-adc</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912系统时钟控制器（SCCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L74">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P024_realtek_rts5912-sccon.md#std-dtcompatible-realtek-rts5912-sccon"><code>realtek,rts5912-sccon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L48">已启用：2</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912 32位定时器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L90">已禁用：6</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P013_realtek_rts5912-timer.md#std-dtcompatible-realtek-rts5912-timer"><code>realtek,rts5912-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912 32位慢速定时器（Slow Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L247">已禁用：1</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P012_realtek_rts5912-slwtimer.md#std-dtcompatible-realtek-rts5912-slwtimer"><code>realtek,rts5912-slwtimer</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912密码SHA加速器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L673">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P009_realtek_rts5912-sha.md#std-dtcompatible-realtek-rts5912-sha"><code>realtek,rts5912-sha</code></a></td>
</tr>
<tr>
<td rowspan="1">增强型串行外设接口（ESPI）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912增强SPI（eSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L168">已启用：1</a>）</td>
<td><a href="../espi_binding_reference/P016_realtek_rts5912-espi.md#std-dtcompatible-realtek-rts5912-espi"><code>realtek,rts5912-espi</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L547">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P024_realtek_rts5912-flash-controller.md#std-dtcompatible-realtek-rts5912-flash-controller"><code>realtek,rts5912-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L310">已启用：9</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P013_realtek_rts5912-gpio.md#std-dtcompatible-realtek-rts5912-gpio"><code>realtek,rts5912-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>串行线／JTAG连接器（Serial Wire–JTAG Connector）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L745">已启用：1</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P006_swj-connector.md#std-dtcompatible-swj-connector"><code>swj-connector</code></a></td>
</tr>
<tr>
<td rowspan="2">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Synopsys DesignWare I2C（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L561">已禁用：8</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P006_snps_designware-i2c.md#std-dtcompatible-snps-designware-i2c"><code>snps,designware-i2c</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912 I2C节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L681">已禁用：8</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P011_realtek_rts5912-i2c.md#std-dtcompatible-realtek-rts5912-i2c"><code>realtek,rts5912-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912键盘矩阵控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L438">已启用：1</a>）</td>
<td><a href="../input_keyboard_optical_ctsu_binding_reference/P017_realtek_rts5912-kbd.md#std-dtcompatible-realtek-rts5912-kbd"><code>realtek,rts5912-kbd</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912电池备份RAM（Battery Backed RAM）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L68">已启用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P004_realtek_rts5912-bbram.md#std-dtcompatible-realtek-rts5912-bbram"><code>realtek,rts5912-bbram</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L553">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L303">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P005_realtek_rts5912-pinctrl.md#std-dtcompatible-realtek-rts5912-pinctrl"><code>realtek,rts5912-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>RTS5912超低功耗模式（ULPM）电源控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L753">已禁用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P003_realtek_rts5912-ulpm.md#std-dtcompatible-realtek-rts5912-ulpm"><code>realtek,rts5912-ulpm</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L483">已禁用：8</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P017_realtek_rts5912-pwm.md#std-dtcompatible-realtek-rts5912-pwm"><code>realtek,rts5912-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912嵌入式控制器（EC）上的实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L82">已禁用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P005_realtek_rts5912-rtc.md#std-dtcompatible-realtek-rts5912-rtc"><code>realtek,rts5912-rtc</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L284">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L293">已启用：1</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P005_realtek_rts5912-uart.md#std-dtcompatible-realtek-rts5912-uart"><code>realtek,rts5912-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912串行外设接口（SPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L275">已启用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P014_realtek_rts5912-spi.md#std-dtcompatible-realtek-rts5912-spi"><code>realtek,rts5912-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">转速计（Tachometer）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912转速计（Tachometer）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L447">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L456">已禁用：3</a>）</td>
<td><a href="../auxdisplay_iio_tach_binding_reference/P019_realtek_rts5912-tach.md#std-dtcompatible-realtek-rts5912-tach"><code>realtek,rts5912-tach</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已禁用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912嵌入式控制器（EC）上的RTOS定时器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L259">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P012_realtek_rts5912-rtmr.md#std-dtcompatible-realtek-rts5912-rtmr"><code>realtek,rts5912-rtmr</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Realtek RTS5912看门狗定时器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L427">已禁用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P004_realtek_rts5912-watchdog.md#std-dtcompatible-realtek-rts5912-watchdog"><code>realtek,rts5912-watchdog</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`rts5912_evb`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

<a id="building"></a>

### 构建（Building）


1. 按通常方式构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用。
2. 构建成功后生成zephyr.rts5912.bin，二进制镜像位于build/zephyr/目录。

<a id="flashing"></a>

### 烧录（Flashing）


1. 将DediProg连接到J81及J82排针。
2. 使用DediProg SF600编程器，将二进制文件写入外部闪存U10的0x0地址。
3. 给开发板断电。
4. 将配置绑带引脚（Strap Pin）GPIO108置为高电平，再给开发板上电。

<a id="debugging"></a>

### 调试（Debugging）

配合ULINPRO使用SWD或JTAG。

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://github.com/JasonLin-RealTek/Realtek_EC/blob/main/RTS5912_EVB_Schematic_Ver%201.1_20240701_1407.pdf](https://github.com/JasonLin-RealTek/Realtek_EC/blob/main/RTS5912_EVB_Schematic_Ver%201.1_20240701_1407.pdf)

<a id="id4"></a>

〔[2](#id5)〕 [https://github.com/JasonLin-RealTek/Realtek_EC/blob/main/RTS5912_datasheet_brief.pdf](https://github.com/JasonLin-RealTek/Realtek_EC/blob/main/RTS5912_datasheet_brief.pdf)

## 译注

RTS5912输出zephyr.rts5912.bin，通过DediProg SF600在外部U10的0x0写入，GPIO108拉高后上电；调试采用ULINPRO的SWD或JTAG。

---

[上一章](P008_RTS5817_MAA_Evaluation_Board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_ART-Pi.md)
