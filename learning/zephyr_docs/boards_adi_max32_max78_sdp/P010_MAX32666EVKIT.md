---
id: learning.zephyr-docs.boards-adi-max32-max78-sdp.page-10
title: MAX32666EVKIT
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/adi/max32666evkit/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="max32666evkit"></a>

# 第10章\_MAX32666EVKIT

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/adi/max32666evkit/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/max32666evkit.webp](images/max32666evkit.webp)](images/max32666evkit.webp)

MAX32666EVKIT

名称（Name）：

`max32666evkit`

厂商（Vendor）：

[Analog Devices, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=adi)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[max32666](https://docs.zephyrproject.org/latest/boards/index.html#soc=max32666)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32666evkit/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

MAX32666EVKIT提供一个平台，用于评估面向可穿戴和耳戴设备应用的MAX32665及MAX32666高能效Arm®微控制器与音频数字信号处理器（Audio DSP）。

Zephyr移植版本运行在MAX32666微控制器（MCU）上。

<a id="hardware"></a>

## 硬件（Hardware）


- MAX32666微控制器（MCU）：


  - 面向可穿戴和耳戴设备的高能效微控制器与音频数字信号处理器（Audio DSP）


    - Arm Cortex-M4，带浮点单元（FPU），最高96 MHz
    - 可选第二个带FPU的Arm Cortex-M4内核，针对数据处理优化
    - 可选择7.3728 MHz低功耗系统时钟
    - 1 MB闪存，组织为两个512 KB存储区（Dual Banks）
    - 560 KB SRAM，启用ECC时为448 KB；三个16 KB缓存（Cache）
    - 缓存、SRAM和内部闪存可选启用纠错码（ECC-SEC-DED），支持单错纠正、双错检测
  - Bluetooth 5低功耗（LE）无线电


    - 数据吞吐率（Data Throughput）为1 Mbps和2 Mbps
    - 远距离（Long Range）模式，125 kbps和500 kbps
    - 广播扩展（Advertising Extension）
    - 接收灵敏度（Rx Sensitivity）：−95 dBm；最大发射功率（Tx Power）：+4.5 dBm
    - 片上匹配电路（On-Chip Matching），带单端天线端口（Single-Ended Antenna Port）
  - 通过电源管理（Power Management）尽可能延长电池供电应用的运行时间


    - 集成单电感多输出开关电源（SIMO SMPS），支持纽扣电池供电
    - 动态电压调节（Dynamic Voltage Scaling）尽可能降低内核运行功耗
    - 在3.3 V下从缓存执行时为27.3 μA/MHz
    - 启用实时时钟（RTC）的低功耗模式下，可选择保留SRAM内容
  - 多种系统控制外设（Peripherals for System Control）


    - 三路QSPI主机／从机，每路有三个片选（Chip Selects）
    - 三路四线UART
    - 三路I2C主机／从机
    - 最多50个GPIO
    - 四线SPI（QSPI / SPIXF），支持实时闪存解密（Real-Time Flash Decryption）
    - QSPI（SPIXR）RAM接口提供SRAM扩展
    - 8路输入、10位Δ-Σ模数转换器（Delta-Sigma ADC），7.8 ksps
    - USB 2.0高速引擎（HS Engine），带内部收发器（Transceiver）
    - 脉冲密度调制接口（PDM Interface）支持两个数字麦克风
    - 支持时分复用（TDM）的I2S
    - 六个32位定时器（Timers）
    - 两个高速定时器（High-Speed Timers）
    - 1-Wire单总线主机（Master）
    - 16个脉冲串（Pulse Trains / PWM）
    - 安全数字接口（Secure Digital Interface）支持SD3.0、SDIO3.0和eMMC4.51
  - 通过硬件安全（Hardware Security）保护重要知识产权／数据（IP/Data）


    - 信任保护单元（TPU）带模运算加速器（MAA），支持快速椭圆曲线数字签名算法（ECDSA）和模运算（Modular Arithmetic）
    - AES128/192/256、DES和3DES硬件加速器（Hardware Accelerator）
    - 真随机数（TRNG）种子发生器（Seed Generator）
    - SHA-2加速器（Accelerator）与安全引导加载程序（Secure Bootloader）
- MAX32666EVKIT的优势与功能（Benefits and Features）：


  - 蓝牙SMA接口，配2.4 GHz可折转鞭状天线（Hinged Whip Antenna）
  - 1.28英寸、128 × 128单色TFT显示屏
  - 64 MB就地执行闪存（XIP Flash）
  - 1 MB就地执行RAM（XIP RAM）
  - 立体声音频编解码器（Stereo Audio Codec），带3.5 mm线路输入（Line-In）和线路输出（Line-Out）插孔
  - 数字音频麦克风（Digital Audio Microphone）
  - USB 2.0 Micro-B接口
  - USB 2.0 Micro-B转串行UART
  - Micro SD卡接口
  - 通过0.1英寸间距排针访问部分GPIO
  - 通过0.1英寸间距排针访问8路模拟输入（Analog Inputs）
  - Arm®或SWD JTAG 20针排针（Header）
  - 1-Wire单总线RJ11端口
  - 可仅由纽扣电池（Coin Cell Battery）供电
  - 任一USB端口均可为开发板供电
  - 通过跳线分别测量所有芯片供电轨（IC Rails）的功耗
  - 板载1.8 V和3.3 V稳压器（Regulators）
  - 两个通用LED和两个通用按键开关（General-Purpose Pushbutton Switches）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`max32666evkit`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="max32666evkit-hw-features"></a>

<a id="max32666evkit-max32666evkit/max32666/cpu0-hw-features-section"></a>

#### `max32666evkit/max32666/cpu0`目标（Target）

<a id="max32666evkit-max32666evkit/max32666/cpu0-hw-features-panel"></a>

<a id="max32666evkit-max32666evkit/max32666/cpu0-hw-features-memory"></a>

该开发板目标的片上存储容量：128 KiB RAM、512 KiB Flash。

<a id="max32666evkit-max32666evkit/max32666/cpu0-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="2">中央处理器（CPU）</td>
<td>片上（On-Chip）</td>
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MAX32 ARM M4F CPU1内核（Core）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P001_adi_max32-m4f-cpu1.md#std-dtcompatible-adi-max32-m4f-cpu1"><code>adi,max32-m4f-cpu1</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32 10位模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L241">已禁用：1</a>）</td>
<td><a href="../hardware/P861_ADIMAX32十位ADC绑定.md#dtbinding-adi-max32-adc-10b"><code>adi,max32-adc-10b</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L64">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L71">已禁用：4</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MAX32全局控制（Global Control）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L130">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P004_adi_max32-gcr.md#std-dtcompatible-adi-max32-gcr"><code>adi,max32-gcr</code></a></td>
</tr>
<tr>
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32计数器（Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L260">已禁用：4</a>）</td>
<td><a href="../counter_binding_reference/P001_adi_max32-counter.md#std-dtcompatible-adi-max32-counter"><code>adi,max32-counter</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ADI MAX32兼容实时时钟计数器（Counter RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L332">已启用：1</a>）</td>
<td><a href="../counter_binding_reference/P002_adi_max32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter"><code>adi,max32-rtc-counter</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ADI MAX32唤醒定时器（Wake-Up Timer）是一个特殊的32位定时器实例，能够从睡眠（Sleep）、待机（Standby）和备份（Backup）模式唤醒设备。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L224">已禁用：1</a>）</td>
<td><a href="../counter_binding_reference/P003_adi_max32-wut.md#std-dtcompatible-adi-max32-wut"><code>adi,max32-wut</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>板载（On-Board）</td>
<td>Sharp LS0XX存储型显示控制器（Memory Display Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32666evkit/max32666evkit.dtsi?plain=1#L59">已启用：1</a>）</td>
<td><a href="../display_panel_renesas_sharp_binding_reference/P015_sharp_ls0xx.md#std-dtcompatible-sharp-ls0xx"><code>sharp,ls0xx</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32直接存储器访问（DMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L123">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L133">已禁用：1</a>）</td>
<td><a href="../dma_binding_reference/P002_adi_max32-dma.md#std-dtcompatible-adi-max32-dma"><code>adi,max32-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>MAX32XXX闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L111">已启用：2</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P001_adi_max32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller"><code>adi,max32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>MAX32通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L175">已启用：2</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P011_adi_max32-gpio.md#std-dtcompatible-adi-max32-gpio"><code>adi,max32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32 I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L149">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L139">已禁用：1</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P001_adi_max32-i2c.md#std-dtcompatible-adi-max32-i2c"><code>adi,max32-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32666evkit/max32666evkit.dtsi?plain=1#L32">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32666evkit/max32666evkit.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32 SEMA邮箱（Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L194">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P032_ADI硬件信号量邮箱绑定.md#dtbinding-adi-mbox-max32-sema"><code>adi,mbox-max32-sema</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L119">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L111">已禁用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>MAX32引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L169">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P001_adi_max32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl"><code>adi,max32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L265">已禁用：4</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P003_adi_max32-pwm.md#std-dtcompatible-adi-max32-pwm"><code>adi,max32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32XXX真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L226">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P001_adi_max32-trng.md#std-dtcompatible-adi-max32-trng"><code>adi,max32-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32安全数字主机控制器（SDHC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L201">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P001_adi_max32-sdhc.md#std-dtcompatible-adi-max32-sdhc"><code>adi,max32-sdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>MAX32通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L210">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L202">已禁用：2</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P001_adi_max32-uart.md#std-dtcompatible-adi-max32-uart"><code>adi,max32-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L143">已禁用：3</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P001_adi_max32-spi.md#std-dtcompatible-adi-max32-spi"><code>adi,max32-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L43">已启用：12</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L252">已禁用：7</a>）</td>
<td><a href="../system_timer_binding_reference/P002_adi_max32-timer.md#std-dtcompatible-adi-max32-timer"><code>adi,max32-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32高速USB（USBHS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L230">已启用：1</a>）</td>
<td><a href="../usb_controller_binding_reference/P001_adi_max32-usbhs.md#std-dtcompatible-adi-max32-usbhs"><code>adi,max32-usbhs</code></a></td>
</tr>
<tr>
<td rowspan="1">单线总线（1-Wire）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32xxx微控制器（MCU）的1-Wire单总线主机（Master）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L193">已禁用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P006_adi_max32-w1.md#std-dtcompatible-adi-max32-w1"><code>adi,max32-w1</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>MAX32XXX看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L233">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P001_adi_max32-watchdog.md#std-dtcompatible-adi-max32-watchdog"><code>adi,max32-watchdog</code></a></td>
</tr>
</table>

<a id="max32666evkit-max32666evkit/max32666/cpu1-hw-features-section"></a>

#### `max32666evkit/max32666/cpu1`目标（Target）

<a id="max32666evkit-max32666evkit/max32666/cpu1-hw-features-panel"></a>

<a id="max32666evkit-max32666evkit/max32666/cpu1-hw-features-memory"></a>

该开发板目标的片上存储容量：128 KiB RAM、512 KiB Flash。

<a id="max32666evkit-max32666evkit/max32666/cpu1-hw-features-table"></a>

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
<td>MAX32 ARM M4F CPU1内核（Core）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P001_adi_max32-m4f-cpu1.md#std-dtcompatible-adi-max32-m4f-cpu1"><code>adi,max32-m4f-cpu1</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32 10位模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L241">已禁用：1</a>）</td>
<td><a href="../hardware/P861_ADIMAX32十位ADC绑定.md#dtbinding-adi-max32-adc-10b"><code>adi,max32-adc-10b</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L64">已禁用：6</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>MAX32全局控制（Global Control）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L130">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P004_adi_max32-gcr.md#std-dtcompatible-adi-max32-gcr"><code>adi,max32-gcr</code></a></td>
</tr>
<tr>
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32计数器（Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L260">已禁用：4</a>）</td>
<td><a href="../counter_binding_reference/P001_adi_max32-counter.md#std-dtcompatible-adi-max32-counter"><code>adi,max32-counter</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ADI MAX32兼容实时时钟计数器（Counter RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L332">已禁用：1</a>）</td>
<td><a href="../counter_binding_reference/P002_adi_max32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter"><code>adi,max32-rtc-counter</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ADI MAX32唤醒定时器（Wake-Up Timer）是一个特殊的32位定时器实例，能够从睡眠（Sleep）、待机（Standby）和备份（Backup）模式唤醒设备。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L224">已禁用：1</a>）</td>
<td><a href="../counter_binding_reference/P003_adi_max32-wut.md#std-dtcompatible-adi-max32-wut"><code>adi,max32-wut</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>板载（On-Board）</td>
<td>Sharp LS0XX存储型显示控制器（Memory Display Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32666evkit/max32666evkit.dtsi?plain=1#L59">已禁用：1</a>）</td>
<td><a href="../display_panel_renesas_sharp_binding_reference/P015_sharp_ls0xx.md#std-dtcompatible-sharp-ls0xx"><code>sharp,ls0xx</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32直接存储器访问（DMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L123">已禁用：2</a>）</td>
<td><a href="../dma_binding_reference/P002_adi_max32-dma.md#std-dtcompatible-adi-max32-dma"><code>adi,max32-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>MAX32XXX闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L111">已启用：2</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P001_adi_max32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller"><code>adi,max32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>MAX32通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L175">已启用：2</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P011_adi_max32-gpio.md#std-dtcompatible-adi-max32-gpio"><code>adi,max32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32 I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L139">已禁用：3</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P001_adi_max32-i2c.md#std-dtcompatible-adi-max32-i2c"><code>adi,max32-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32666evkit/max32666evkit.dtsi?plain=1#L32">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32666evkit/max32666evkit.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32 SEMA邮箱（Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L194">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P032_ADI硬件信号量邮箱绑定.md#dtbinding-adi-mbox-max32-sema"><code>adi,mbox-max32-sema</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L111">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L119">已禁用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>MAX32引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L169">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P001_adi_max32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl"><code>adi,max32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L265">已禁用：4</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P003_adi_max32-pwm.md#std-dtcompatible-adi-max32-pwm"><code>adi,max32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32XXX真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L226">已禁用：1</a>）</td>
<td><a href="../rng_binding_reference/P001_adi_max32-trng.md#std-dtcompatible-adi-max32-trng"><code>adi,max32-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32安全数字主机控制器（SDHC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L201">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P001_adi_max32-sdhc.md#std-dtcompatible-adi-max32-sdhc"><code>adi,max32-sdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>MAX32通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L202">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L210">已禁用：2</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P001_adi_max32-uart.md#std-dtcompatible-adi-max32-uart"><code>adi,max32-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L143">已禁用：3</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P001_adi_max32-spi.md#std-dtcompatible-adi-max32-spi"><code>adi,max32-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L43">已启用：12</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L252">已禁用：7</a>）</td>
<td><a href="../system_timer_binding_reference/P002_adi_max32-timer.md#std-dtcompatible-adi-max32-timer"><code>adi,max32-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32高速USB（USBHS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L230">已禁用：1</a>）</td>
<td><a href="../usb_controller_binding_reference/P001_adi_max32-usbhs.md#std-dtcompatible-adi-max32-usbhs"><code>adi,max32-usbhs</code></a></td>
</tr>
<tr>
<td rowspan="1">单线总线（1-Wire）</td>
<td>片上（On-Chip）</td>
<td>ADI MAX32xxx微控制器（MCU）的1-Wire单总线主机（Master）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L193">已禁用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P006_adi_max32-w1.md#std-dtcompatible-adi-max32-w1"><code>adi,max32-w1</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>MAX32XXX看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/adi/max32/max32xxx.dtsi?plain=1#L233">已禁用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P001_adi_max32-watchdog.md#std-dtcompatible-adi-max32-watchdog"><code>adi,max32-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<table>
<tr>
<th>名称（Name）</th>
<th>名称（Name）</th>
<th>设置（Settings）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td>JP1</td>
<td>I2C0_SCL/SDA</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开I2C0 SCL和SDA的1.5 kΩ上拉电阻与VDDIOH。</td></tr><tr><td>将I2C0 SCL和SDA的1.5 kΩ上拉电阻连接到VDDIOH。</td></tr></table></td>
</tr>
<tr>
<td>JP2</td>
<td>I2C1_SCL/SDA</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开I2C1 SCL和SDA的1.5 kΩ上拉电阻与VDDIOH。</td></tr><tr><td>将I2C1 SCL和SDA的1.5 kΩ上拉电阻连接到VDDIOH。</td></tr></table></td>
</tr>
<tr>
<td>JP3</td>
<td>I2C2_SCL/SDA</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开I2C2 SCL和SDA的1.5 kΩ上拉电阻与VDDIOH。</td></tr><tr><td>将I2C2 SCL和SDA的1.5 kΩ上拉电阻连接到VDDIOH。</td></tr></table></td>
</tr>
<tr>
<td>JP4</td>
<td>P1_14</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开LED D2与P1_14。</td></tr><tr><td>将LED D2连接到P1_14。</td></tr></table></td>
</tr>
<tr>
<td>JP5</td>
<td>P1_15</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开LED D3与P1_15。</td></tr><tr><td>将LED D3连接到P1_15。</td></tr></table></td>
</tr>
<tr>
<td>JP6</td>
<td>VBUS</td>
<td><table><tr><td>2-1</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>将VBUS连接到USB接口CN1，为开发板供电。</td></tr><tr><td>将VBUS连接到USB接口CN2，为开发板供电。</td></tr></table></td>
</tr>
<tr>
<td>JP7</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr>
<td>JP8</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr>
<td>JP9</td>
<td><table><tr><td>P0_20</td></tr><tr><td>P0_28</td></tr></table></td>
<td><table><tr><td>2-1</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>将USB转串行UART连接到GPIO P0_20（RX1）。</td></tr><tr><td>将USB转串行UART连接到GPIO P0_28（RX2）。</td></tr></table></td>
</tr>
<tr>
<td>JP10</td>
<td><table><tr><td>P0_21</td></tr><tr><td>P0_29</td></tr></table></td>
<td><table><tr><td>2-1</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>将USB转串行UART连接到GPIO P0_21（TX1）。</td></tr><tr><td>将USB转串行UART连接到GPIO P0_29（TX2）。</td></tr></table></td>
</tr>
<tr>
<td>JP11</td>
<td><table><tr><td>P0_22</td></tr><tr><td>P0_30</td></tr></table></td>
<td><table><tr><td>2-1</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>将USB转串行UART连接到GPIO P0_22（CTS1_N）。</td></tr><tr><td>将USB转串行UART连接到GPIO P0_30（CTS2_N）。</td></tr></table></td>
</tr>
<tr>
<td>JP12</td>
<td><table><tr><td>P0_23</td></tr><tr><td>P0_31</td></tr></table></td>
<td><table><tr><td>2-1</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>将USB转串行UART连接到GPIO P0_23（RTS1_N）。</td></tr><tr><td>将USB转串行UART连接到GPIO P0_31（RTS2_N）。</td></tr></table></td>
</tr>
<tr>
<td>JP13</td>
<td>VREGI</td>
<td><table><tr><td>2-1</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>将VREGI连接到纽扣电池（Coin Cell Battery）。</td></tr><tr><td>将VREGI连接到3V3。</td></tr></table></td>
</tr>
<tr>
<td>JP14</td>
<td>VDDIOH</td>
<td><table><tr><td>1-2</td></tr><tr><td>3-4</td></tr><tr><td>5-6</td></tr></table></td>
<td><table><tr><td>将VDDIOH连接到VREGO_A。</td></tr><tr><td>将VDDIOH连接到1V8。</td></tr><tr><td>将VDDIOH连接到3V3。</td></tr></table></td>
</tr>
<tr>
<td>JP15</td>
<td>VDDIOH</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开VDDIOH的电源。</td></tr><tr><td>为VDDIOH接通电源。</td></tr></table></td>
</tr>
<tr>
<td>JP16</td>
<td>VDDB</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开VDDB的电源。</td></tr><tr><td>为VDDB接通电源。</td></tr></table></td>
</tr>
<tr>
<td>JP17</td>
<td>VDDIO</td>
<td><table><tr><td>2-1</td></tr><tr><td>2-3</td></tr></table></td>
<td><table><tr><td>将VDDIO连接到VREGO_A。</td></tr><tr><td>将VDDIO连接到1V8。</td></tr></table></td>
</tr>
<tr>
<td>JP18</td>
<td>VDDIO</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开VDDIO的电源。</td></tr><tr><td>为VDDIO接通电源。</td></tr></table></td>
</tr>
<tr>
<td>JP19</td>
<td>VDDA</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开VDDA的电源。</td></tr><tr><td>为VDDA接通电源。</td></tr></table></td>
</tr>
<tr>
<td>JP20</td>
<td>VCORE_A</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开VCORE_A的电源。</td></tr><tr><td>为VCORE_A接通电源。</td></tr></table></td>
</tr>
<tr>
<td>JP21</td>
<td>VCORE_B</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开VCORE_B的电源。</td></tr><tr><td>为VCORE_B接通电源。</td></tr></table></td>
</tr>
<tr>
<td>JP22</td>
<td>VTXIN</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开VTXIN的电源。</td></tr><tr><td>为VTXIN接通电源。</td></tr></table></td>
</tr>
<tr>
<td>JP23</td>
<td>VRXIN</td>
<td><table><tr><td>开路（Open）</td></tr><tr><td>闭合（Close）</td></tr></table></td>
<td><table><tr><td>断开VRXIN的电源。</td></tr><tr><td>为VRXIN接通电源。</td></tr></table></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`max32666evkit`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-jlink"><code>jlink</code></a></td>
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

<a id="flashing"></a>

### 烧录（Flashing）

将外部调试探针（Debug Probe）连接到SWD端口，即可烧录MAX32666微控制器（MCU）。SWD调试通过Cortex 10针接口J6接入，逻辑电平固定为VDDIOH，即1.8 V或3.3 V。

将调试探针连接到主机后，执行`west flash`即可将固件镜像写入闪存（Flash）。要执行整片擦除（Full Erase），在`west flash`命令中加入`--erase`选项。

注意（Note）

该开发板默认使用OpenOCD调试接口。也可覆盖运行工具（Runner），在west命令后添加`--runner jlink`，使用Segger J-Link及其原生工具。J-Link应连接到标准20针接口J7或Cortex® 10针接口J6。

<a id="debugging"></a>

### 调试（Debugging）

请参考[烧录（Flashing）](#flashing)一节，并将`west flash`替换为`west debug`执行调试。

<a id="references"></a>

## 参考资料（References）


- [MAX32666EVKIT网页（Web Page）](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/MAX32666EVKIT.html)

---

[上一章](P009_MAX32662EVKIT.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_MAX32666FTHR.md)
