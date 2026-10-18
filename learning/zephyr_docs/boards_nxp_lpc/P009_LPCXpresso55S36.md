---
id: learning.zephyr-docs.boards-nxp-lpc.page-9
title: LPCXpresso55S36
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso55s36/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="lpcxpresso55s36"></a>

# 第9章\_LPCXpresso55S36

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso55s36/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/lpcxpresso55S36.jpg](images/lpcxpresso55S36.jpg)](images/lpcxpresso55S36.jpg)

LPCXpresso55S36

名称（Name）：

`lpcxpresso55s36`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[lpc55s36](https://docs.zephyrproject.org/latest/boards/index.html#soc=lpc55s36)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/lpcxpresso55s36/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

LPCXpresso55S36是基于Arm Cortex-M33的LPC55S3x／LPC553x MCU系列评估平台。它提供兼容Arduino UNO的扩展板连接器，并在Arduino轮廓周围增加扩展端口，另有Pmod／主机接口及MikroElektronika Click模块位置。

<a id="hardware"></a>

## 硬件（Hardware）


- LPC55S36 Arm Cortex-M33微控制器，最高150 MHz
- 256 KB片上闪存及112 KB片上SRAM
- LPC-Link2高速USB调试探针，带虚拟COM端口（VCOM）
- 通过LPC-Link2探针，实现USB与LPC器件I2C及SPI接口的桥接
- MikroElektronika Click扩展选项
- 兼容Arduino UNO的LPCXpresso扩展连接器
- 兼容Pmod的扩展／主机连接器
- 复位、ISP、唤醒及用户按键，便于测试软件功能
- 三色LED
- USB全速设备／主机端口（Full-speed Device/Host Port）
- USB高速设备／主机端口（High-speed Device/Host Port）
- UART排针，用于连接外部串口转USB线缆
- CAN收发器（Transceiver）
- 带线路输入／输出的立体声音频编解码器（Stereo Audio Codec）

LPC55S36 SoC及LPCXPresso55S36开发板的更多信息见以下资料：


- [LPC55S36 SoC网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc553x-s3x-advanced-analog-armcortex-m33-based-mcu-family:LPC553x)
- [LPC55S36 数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/LPC553x.pdf)
- [LPC55S36 用户手册（User Manual）](https://www.nxp.com/docs/en/reference-manual/LPC553xRM.pdf)
- [LPCXpresso55S36 网站](https://www.nxp.com/design/development-boards/lpcxpresso-boards/development-board-for-the-lpc553x-family-of-mcus:LPCXpresso55S36)
- [LPCXpresso55S36 用户手册（User Manual）](https://www.nxp.com/docs/en/user-manual/LPCXpresso55S36UM.pdf)
- [LPCXpresso55S36 开发板设计文件（Design Files）](https://www.nxp.com/webapp/Download?colCode=LPCXPRESSO5536_EVK-DESIGN-FILES)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

NXP将LPCXpresso55S36视为LPC55(S)3x系列功能覆盖更广的开发板，并优先在此板落实Zephyr完整平台支持及新功能，以服务整个器件系列。另一块类似开发板[LPCXPRESSO55S69](P010_LPCXPRESSO55S69.md#lpcxpresso55s69)可能已有可复用于lpcxpresso55s36的其他功能。

`lpcxpresso55s36`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="lpcxpresso55s36-hw-features"></a>

<a id="lpcxpresso55s36-lpcxpresso55s36/lpc55s36-hw-features-section"></a>

#### `lpcxpresso55s36/lpc55s36`目标（Target）

<a id="lpcxpresso55s36-lpcxpresso55s36/lpc55s36-hw-features-panel"></a>

<a id="lpcxpresso55s36-lpcxpresso55s36/lpc55s36-hw-features-memory"></a>

该开发板目标的片上存储容量：112 KiB RAM、246 KiB Flash。

<a id="lpcxpresso55s36-lpcxpresso55s36/lpc55s36-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L393">已启用：1</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>LPC Flexcomm节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L303">已禁用：7</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P015_nxp_lpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm"><code>nxp,lpc-flexcomm</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC SoC系列MCAN CAN FD控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L499">已启用：1</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P001_nxp_lpc-mcan.md#std-dtcompatible-nxp-lpc-mcan"><code>nxp,lpc-mcan</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L89">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP高速比较器（HSCMP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L412">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L422">已禁用：2</a>）</td>
<td><a href="../hardware/P744_NXP高速比较器绑定.md#dtbinding-nxp-hscmp"><code>nxp,hscmp</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L232">已启用：5</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L652">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P006_nxp_crc.md#std-dtcompatible-nxp-crc"><code>nxp,crc</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX低功耗数模转换器（LPDAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L472">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L481">已禁用：2</a>）</td>
<td><a href="../hardware/P770_NXP低功耗数模转换器绑定.md#dtbinding-nxp-lpdac"><code>nxp,lpdac</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L172">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L184">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P003_nxp_lpc-dma.md#std-dtcompatible-nxp-lpc-dma"><code>nxp,lpc-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">数字信号处理（DSP）</td>
<td>片上（On-Chip）</td>
<td>NXP PowerQuad数字信号处理（DSP）协处理器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L668">已启用：1</a>）</td>
<td><a href="../sound_haptic_binding_reference/P004_nxp_powerquad.md#std-dtcompatible-nxp-powerquad"><code>nxp,powerquad</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>用于lpc553x系列的NXP在应用编程（IAP）闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L100">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P012_nxp_iap-fmc553.md#std-dtcompatible-nxp-iap-fmc553"><code>nxp,iap-fmc553</code></a></td>
</tr>
<tr>
<td rowspan="4">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>LPC通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L142">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P006_nxp_lpc-gpio.md#std-dtcompatible-nxp-lpc-gpio"><code>nxp,lpc-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>LPC GPIO端口设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L148">已启用：3</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P005_nxp_lpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port"><code>nxp,lpc-gpio-port</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通过Mikro BUS排针引出的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s36/lpcxpresso55s36.dts?plain=1#L76">已启用：1</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P006_mikro-bus.md#std-dtcompatible-mikro-bus"><code>mikro-bus</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s36/lpcxpresso55s36.dts?plain=1#L99">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC55xx电源管理控制器（PMC）的复位原因硬件信息（Hwinfo）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L84">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P008_nxp_lpc-pmc-hwinfo.md#std-dtcompatible-nxp-lpc-pmc-hwinfo"><code>nxp,lpc-pmc-hwinfo</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s36/lpcxpresso55s36.dts?plain=1#L60">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="3">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP分组GPIO输入中断（GINT / Grouped GPIO Input Interrupt）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L196">已启用：2</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P001_nxp_gint.md#std-dtcompatible-nxp-gint"><code>nxp,gint</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP引脚中断及模式匹配引擎（PINT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L212">已启用：1</a>）</td>
<td><a href="../nxp_interrupt_binding_reference/P004_nxp_pint.md#std-dtcompatible-nxp-pint"><code>nxp,pint</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s36/lpcxpresso55s36.dts?plain=1#L41">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L108">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L118">已禁用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">多路复用器（MUX）</td>
<td>片上（On-Chip）</td>
<td>NXP输入复用器（INPUTMUX）外设绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L224">已禁用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux"><code>nxp,inputmux</code></a></td>
</tr>
<tr>
<td rowspan="1">运算放大器（OPAMP）</td>
<td>片上（On-Chip）</td>
<td>NXP运算放大器（opamp）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L442">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L452">已禁用：2</a>）</td>
<td><a href="../hardware/P732_NXP运算放大器绑定.md#dtbinding-nxp-opamp"><code>nxp,opamp</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>LPC I/O引脚配置（IOCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L130">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P007_nxp_lpc-iocon.md#std-dtcompatible-nxp-lpc-iocon"><code>nxp,lpc-iocon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>LPC引脚控制（Pinctrl）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L137">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P005_nxp_lpc-iocon-pinctrl.md#std-dtcompatible-nxp-lpc-iocon-pinctrl"><code>nxp,lpc-iocon-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="3">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>包含mcux-pwm子模块的NXP eFLEX PWM模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L510">已启用：2</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P003_nxp_flexpwm.md#std-dtcompatible-nxp-flexpwm"><code>nxp,flexpwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L571">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L516">已禁用：7</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P005_nxp_imx-pwm.md#std-dtcompatible-nxp-imx-pwm"><code>nxp,imx-pwm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP状态可配置定时器（SCTimer）脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L629">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P012_nxp_sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm"><code>nxp,sctimer-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>NXP VREF SoC外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L639">已启用：1</a>）</td>
<td><a href="../hardware/P652_NXP参考电压绑定.md#dtbinding-nxp-vref"><code>nxp,vref</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L94">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P009_nxp_lpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset"><code>nxp,lpc-syscon-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC通用同步异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L292">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P014_nxp_lpc-usart.md#std-dtcompatible-nxp-lpc-usart"><code>nxp,lpc-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC串行外设接口（SPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L380">已禁用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P003_nxp_lpc-spi.md#std-dtcompatible-nxp-lpc-spi"><code>nxp,lpc-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L54">已启用：5</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP LPCIP3511 USB设备模式（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L620">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P008_nxp_lpcip3511.md#std-dtcompatible-nxp-lpcip3511"><code>nxp,lpcip3511</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>LPC窗口看门狗定时器（Windowed Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc55xxx/nxp_lpc55S3x_common.dtsi?plain=1#L659">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P011_nxp_lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt"><code>nxp,lpc-wwdt</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

LPC55S36 SoC具有IOCON寄存器，可用于配置引脚功能。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PIO0_17</td>
<td>通用输入输出（GPIO）</td>
<td>用户按键（USR）SW3</td>
</tr>
<tr>
<td>PIO0_22</td>
<td>通用输入输出（GPIO）</td>
<td>绿色LED（GREEN LED）</td>
</tr>
<tr>
<td>PIO0_28</td>
<td>通用输入输出（GPIO）</td>
<td>红色LED（RED LED）</td>
</tr>
<tr>
<td>PIO0_29</td>
<td>通用同步异步收发器（USART）</td>
<td>USART接收（RX）</td>
</tr>
<tr>
<td>PIO0_30</td>
<td>通用同步异步收发器（USART）</td>
<td>USART发送（TX）</td>
</tr>
<tr>
<td>PIO1_11</td>
<td>通用输入输出（GPIO）</td>
<td>BLUE_LED</td>
</tr>
<tr>
<td>PIO1_18</td>
<td>通用输入输出（GPIO）</td>
<td>唤醒按键（Wakeup）SW1</td>
</tr>
<tr>
<td>PIO1_20</td>
<td>FLEXPPWM0_PWM0_A</td>
<td>pwm</td>
</tr>
<tr>
<td>PIO1_17</td>
<td>FLEXPPWM0_PWM0_B</td>
<td>pwm</td>
</tr>
<tr>
<td>PIO1_6</td>
<td>FLEXPPWM0_PWM1_A</td>
<td>pwm</td>
</tr>
<tr>
<td>PIO1_22</td>
<td>FLEXPPWM0_PWM1_B</td>
<td>pwm</td>
</tr>
<tr>
<td>PIO1_8</td>
<td>FLEXPPWM0_PWM2_A</td>
<td>pwm</td>
</tr>
<tr>
<td>PIO1_4</td>
<td>FLEXPPWM0_PWM2_B</td>
<td>pwm</td>
</tr>
<tr>
<td>PIO1_21</td>
<td>FLEXPPWM1_PWM0_A</td>
<td>pwm</td>
</tr>
<tr>
<td>PIO0_3</td>
<td>FLEXPPWM1_PWM0_B</td>
<td>pwm</td>
</tr>
<tr>
<td>PIO1_23</td>
<td>FLEXPPWM1_PWM1_A</td>
<td>pwm</td>
</tr>
<tr>
<td>PIO0_21</td>
<td>FLEXPPWM1_PWM1_B</td>
<td>pwm</td>
</tr>
<tr>
<td>PIO1_25</td>
<td>FLEXPPWM1_PWM2_A</td>
<td>pwm</td>
</tr>
<tr>
<td>PIO0_31</td>
<td>FLEXPPWM1_PWM2_B</td>
<td>pwm</td>
</tr>
<tr>
<td>PIO1_2</td>
<td>CAN0_TXD</td>
<td>CAN发送（TX）</td>
</tr>
<tr>
<td>PIO1_3</td>
<td>CAN0_RXD</td>
<td>CAN接收（RX）</td>
</tr>
<tr>
<td>PIO0_22</td>
<td>USB0_VBUS</td>
<td>USB全速总线电源（USBFS VBUS）</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

LPC55S36 SoC使用外部24 MHz晶体驱动PLL1，产生144 MHz系统时钟。启用闪存控制器后，核心时钟降为96 MHz。SoC也提供其他系统时钟源，可按需求选择。

<a id="serial-port"></a>

### 串口（Serial Port）

LPC55S36 SoC有8路FLEXCOMM串行通信接口，一路配置为控制台USART，其余未使用。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`lpcxpresso55s36`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-jlink">jlink</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-linkserver">linkserver</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td></td>
<td></td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-pyocd">pyocd</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

按通常方式构建并烧录应用，详见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）与“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

<a id="configuring-a-debug-probe"></a>

### 配置调试探针（Configuring a Debug Probe）

默认运行工具（Runner）为LinkServer，烧录和调试均使用调试探针。原文此处将默认探针称为集成MCU-Link，并使用CMSIS-DAP模式。需安装LinkServer调试主机工具并加入搜索路径，才能用于Zephyr；更多信息见“应用调试”（[Application Debugging](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)）概述。（[MCU-Link板载调试探针](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#mcu-link-onboard-debug-probe)；[LinkServer调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#linkserver-debug-host-tools)）

原文说明，集成MCU-Link也可通过更新固件作为J-Link探针，方法见MCU-Link J-Link板载调试探针说明。此时需提供J-Link调试主机工具。（[MCU-Link J-Link板载调试探针（Onboard Debug Probe）](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#mcu-link-jlink-onboard-debug-probe)；[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)）

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

用USB线缆将PC连接J1（LINK2），在所选串口终端（如minicom、PuTTY）中使用以下设置：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

### 烧录（Flashing）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b lpcxpresso55s36 samples/hello_world
west flash
```

打开串口终端，复位开发板（按下RESET按键），应能在终端中看到以下消息：

```text
***** Booting Zephyr OS v2.2.0 *****
Hello World! lpcxpresso55s36
```

<a id="debugging"></a>

### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b lpcxpresso55s36 samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
***** Booting Zephyr OS zephyr-v2.2.0 *****
Hello World! lpcxpresso55s36
```

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)
- [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)
- [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- NXP Zephyr主页，包含培训资源（[NXP的Zephyr专题页面](https://nxp.com/zephyr)）
- [NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## 译注

当前配置使用24 MHz晶体及144 MHz PLL1，启用闪存控制器时降为96 MHz。板上LPC-Link2与后文MCU-Link称呼按原文分别保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [development-board-for-the-lpc553x-family-of-mcus:LPCXpresso55S36](https://www.nxp.com/design/development-boards/lpcxpresso-boards/development-board-for-the-lpc553x-family-of-mcus:LPCXpresso55S36)：HTTP Error 404: Not Found。
- [LPC553x.pdf](https://www.nxp.com/docs/en/data-sheet/LPC553x.pdf)：HTTP Error 404: Not Found。
- [LPC553xRM.pdf](https://www.nxp.com/docs/en/reference-manual/LPC553xRM.pdf)：HTTP Error 404: Not Found。
- [LPCXpresso55S36UM.pdf](https://www.nxp.com/docs/en/user-manual/LPCXpresso55S36UM.pdf)：HTTP Error 404: Not Found。
- [lpc553x-s3x-advanced-analog-armcortex-m33-based-mcu-family:LPC553x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc553x-s3x-advanced-analog-armcortex-m33-based-mcu-family:LPC553x)：HTTP Error 404: Not Found。
- [Download?colCode=LPCXPRESSO5536_EVK-DESIGN-FILES](https://www.nxp.com/webapp/Download?colCode=LPCXPRESSO5536_EVK-DESIGN-FILES)：HTTP Error 404: Not Found。

---

[上一章](P008_LPCXpresso55S28.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_LPCXPRESSO55S69.md)
