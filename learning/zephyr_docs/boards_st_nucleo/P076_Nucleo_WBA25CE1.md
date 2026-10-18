---
id: learning.zephyr-docs.boards-st-nucleo.page-76
title: Nucleo WBA25CE1
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/st/nucleo_wba25ce1/doc/nucleo_wba25ce1.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nucleo_wba25ce1"></a>

# 第76章\_Nucleo WBA25CE1开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/st/nucleo_wba25ce1/doc/nucleo_wba25ce1.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/nucleo_wba25ce1.webp](images/nucleo_wba25ce1.webp)](images/nucleo_wba25ce1.webp)

Nucleo WBA25CE1开发板

名称（Name）：

`nucleo_wba25ce1`

厂商（Vendor）：

[意法半导体（STMicroelectronics）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=st)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[stm32wba25xx](https://docs.zephyrproject.org/latest/boards/index.html#soc=stm32wba25xx)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_wba25ce1/doc/nucleo_wba25ce1.rst/../..)<a id="overview"></a>

## 概述（Overview）

NUCLEO-WBA25CE1是一款低功耗蓝牙（Bluetooth® LE）超低功耗无线板，内置符合Bluetooth LE SIG 5.3规范的高性能超低功耗无线电。

ARDUINO® Uno V3连接接口及ST morpho排针支持众多专用扩展板（Shields），便于扩展STM32 Nucleo开放开发平台的功能。


- 基于Arm® Cortex®-M33内核的超低功耗无线STM32WBA25CE1微控制器，UFQFPN48封装，具有512 Kbytes Flash及96 Kbytes SRAM
- MCU射频板（RF Board）：MB1863


  - 2.4 GHz射频收发器，支持Bluetooth® 5.3规范
  - Arm® Cortex®-M33 CPU，带TrustZone®、MPU、DSP及FPU
  - 集成PCB天线
- 3个用户LED
- 3个用户按键及1个复位按键
- 8针SOP封装Quad-SPI NOR Flash焊盘
- 开发板连接器（Board Connectors）：


  - USB Type-C®接口
  - ARDUINO® Uno V3扩展连接器
  - ST morpho排针，可访问全部STM32 I/O
- 灵活供电方式：ST-LINK USB VBUS或外部电源
- 板载STLINK-V3MODS调试器／编程器支持USB重新枚举，提供大容量存储、虚拟COM端口及调试端口

<a id="hardware"></a>

## 硬件（Hardware）

STM32WBA2xxx多协议超低功耗无线器件内置符合Bluetooth® LE及IEEE 802.15.4-2015规范的高性能超低功耗2.4 GHz无线电，采用Arm® Cortex®-M33 32位RISC内核，最高工作频率64 MHz。


- 采用ST先进专利技术
- 超低功耗无线电（Ultra-low-power Radio）：


  - 2.4 GHz无线电
  - 射频收发器支持Bluetooth® LE及IEEE 802.15.4-2015的物理层（PHY）和媒体访问控制层（MAC），支持Matter及Zigbee®
  - 接收灵敏度：Bluetooth® LE 1 Mbps时−96 dBm，IEEE 802.15.4 250 kbps时−100 dBm
  - 输出功率可编程，最高+10 dBm，步进1 dB
  - 支持外部功率放大器（PA）
  - 数据包流量仲裁（Packet Traffic Arbitration）
  - 集成平衡不平衡转换器（Balun），减少物料清单（BOM）
  - 适用于需要符合ETSI EN 300 328、EN 300 440、FCC CFR47 Part 15及ARIB STD-T66无线电法规的系统
- 采用FlexPowerControl的超低功耗平台：


  - 供电电压1.71～3.6 V
  - 环境温度范围−40 °C至85／105 °C，原文将ambient拼作ambiant
  - 带DMA的自主外设，可在最深Stop 1模式工作
  - 待机模式110 nA，7个唤醒引脚
  - 保留64 KB SRAM的待机模式490 nA
  - 保留64 KB SRAM、2.4 GHz无线电及RTC的待机模式980 nA
  - 保留64 KB SRAM、2.4 GHz无线电及RTC的停止模式4.81 µA
  - 运行模式21 µA/MHz
  - 无线电电流：接收3.58 mA，0 dBm发送4.65 mA
- 内核：Arm® 32位Cortex®-M33 CPU，带TrustZone®、MPU、DSP及FPU
- ART Accelerator™：4 Kbyte指令缓存，支持从Flash零等待执行，最高64 MHz，性能96 DMIPS
- 电源管理：内置LDO及SMPS降压转换器，支持运行中切换与电压调节
- 基准测试（Benchmarks）：


  - 264 CoreMark®，4.12 CoreMark/MHz
- 时钟源（Clock Sources）：


  - 32 MHz晶体振荡器
  - 32 kHz低速外部（LSE）晶体振荡器
  - 内部低功耗32 kHz RC，精度±5%
  - 内部16 MHz出厂微调RC，精度±1%
  - 用于系统时钟、音频、USB及ADC的PLL
- 存储器（Memories）：


  - 512 Kbyte Flash，支持ECC，耐久度10 kcycles
  - 96 KB SRAM，其中32 KB支持奇偶校验
  - 512字节OTP，32行
  - 1路四线SPI（Quad-SPI）存储器接口
- 具有独立供电的模拟外设：


  - 12位ADC，2.5 Msps，通过硬件过采样可达16位
- 通信外设（Communication Peripherals）：


  - 1个可选择主机或设备模式的USB全速控制器
  - 1路串行音频接口（SAI）
  - 1路USART，支持ISO 7816、IrDA及调制解调器
  - 1路LPUART，支持ISO 7816及调制解调器
  - 1路SPI
  - 2路I2C Fm+（1 Mbit/s），支持SMBus/PMBus®
- 系统外设（System Peripherals）：


  - 2个16位定时器
  - 1个32位定时器
  - 2个16位低功耗定时器，可在停止模式工作
  - 2个SysTick定时器
  - RTC，带硬件日历及校准
  - 1个看门狗
  - 8通道DMA控制器，可在停止模式工作
- 安全与密码功能（Security and Cryptography）：


  - Arm® TrustZone®，I/O、存储器及外设可配置安全属性
  - 灵活的生命周期方案，支持读出保护（RDP）及密码保护调试
  - 通过唯一启动入口与安全隐藏保护区域（Hide Protection，HDP）建立信任根
  - 安全启动（Secure Boot）及安全固件更新（Secure Firmware Update）
  - AES加速器
  - 公钥加速器，支持ECC及RSA，抵抗侧信道攻击（SCA）
  - 哈希（HASH）硬件加速器
  - 符合NIST SP800-90B的真随机数发生器（TRNG）
  - 96位唯一标识（Unique ID）
  - 防篡改保护（Antitamper Protections）
- 开发支持（Development Support）：


  - 串行线调试（SWD）及JTAG
  - 嵌入式跟踪（ETM）
- 符合ECOPACK2的封装

STM32WBA系列更多信息见：


- [STM32WBA系列在ST官网的页面](https://www.st.com/en/microcontrollers-microprocessors/stm32wba-series.html)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`nucleo_wba25ce1`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="nucleo_wba25ce1-hw-features"></a>

<a id="nucleo_wba25ce1-nucleo_wba25ce1/stm32wba25xx-hw-features-section"></a>

#### `nucleo_wba25ce1/stm32wba25xx`目标（Target）

<a id="nucleo_wba25ce1-nucleo_wba25ce1/stm32wba25xx-hw-features-panel"></a>

<a id="nucleo_wba25ce1-nucleo_wba25ce1/stm32wba25xx-hw-features-memory"></a>

该开发板目标的片上存储容量：65504 B RAM、512 KiB Flash。

<a id="nucleo_wba25ce1-nucleo_wba25ce1/stm32wba25xx-hw-features-table"></a>

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
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>STM32模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L514">已启用：1</a>）</td>
<td><a href="../hardware/P839_STM32模数转换器绑定.md#dtbinding-st-stm32-adc"><code>st,stm32-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>ST STM32WBA蓝牙HCI驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L616">已启用：1</a>）</td>
<td><a href="../bluetooth_st_transport_binding_reference/P005_st_hci-stm32wba.md#std-dtcompatible-st-hci-stm32wba"><code>st,hci-stm32wba</code></a></td>
</tr>
<tr>
<td rowspan="6">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>STM32WBA复位与时钟控制器（RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L233">已启用：1</a>）</td>
<td><a href="../timer_reference/P174_STM32WBA复位与时钟控制绑定.md#dtbinding-st-stm32wba-rcc"><code>st,stm32wba-rcc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32WBA高速外部时钟（HSE）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L135">已启用：1</a>）</td>
<td><a href="../timer_reference/P163_STM32WBA高速外部时钟绑定.md#dtbinding-st-stm32wba-hse-clock"><code>st,stm32wba-hse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L143">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L158">已禁用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低速外部时钟（LSE Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L150">已启用：1</a>）</td>
<td><a href="../timer_reference/P130_STM32低速外部时钟绑定.md#dtbinding-st-stm32-lse-clock"><code>st,stm32-lse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32WBA锁相环（PLL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L165">已禁用：1</a>）</td>
<td><a href="../timer_reference/P152_STM32WBA锁相环时钟绑定.md#dtbinding-st-stm32wba-pll-clock"><code>st,stm32wba-pll-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 微控制器时钟输出（Microcontroller Clock Output，MCO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L173">已禁用：1</a>）</td>
<td><a href="../timer_reference/P134_STM32时钟输出绑定.md#dtbinding-st-stm32-clock-mco"><code>st,stm32-clock-mco</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>STM32 计数器（Counters）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L452">已禁用：3</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P007_st_stm32-counter.md#std-dtcompatible-st-stm32-counter"><code>st,stm32-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>STM32 CRC 计算单元（Calculation Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L602">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P011_st_stm32-crc.md#std-dtcompatible-st-stm32-crc"><code>st,stm32-crc</code></a></td>
</tr>
<tr>
<td rowspan="3">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>STM32高级加密标准加速器（AES Accelerator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L564">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P015_st_stm32-aes.md#std-dtcompatible-st-stm32-aes"><code>st,stm32-aes</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32哈希处理器（HASH Processor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L573">已禁用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P017_st_stm32-hash.md#std-dtcompatible-st-stm32-hash"><code>st,stm32-hash</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32WBA公钥加速器（PKA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L582">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P019_st_stm32wba-pka.md#std-dtcompatible-st-stm32wba-pka"><code>st,stm32wba-pka</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>STM32U5直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba23.dtsi?plain=1#L22">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P012_st_stm32u5-dma.md#std-dtcompatible-st-stm32u5-dma"><code>st,stm32u5-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 系列闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L181">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P011_st_stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller"><code>st,stm32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="3">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用输入输出控制器（GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L337">已启用：4</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P029_st_stm32-gpio.md#std-dtcompatible-st-stm32-gpio"><code>st,stm32-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>串行线／JTAG连接器（Serial Wire–JTAG Connector）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L639">已启用：1</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P006_swj-connector.md#std-dtcompatible-swj-connector"><code>swj-connector</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wba25ce1/arduino_r3_connector.dtsi?plain=1#L10">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>STM32 I2C V2 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L429">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L417">已禁用：1</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P008_st_stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2"><code>st,stm32-i2c-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">低速率无线个域网（IEEE 802.15.4）</td>
<td>片上（On-Chip）</td>
<td>ST STM32WBA IEEE 802.15.4无线接口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L621">已禁用：1</a>）</td>
<td><a href="../lora_ieee802154_binding_reference/P010_st_stm32wba-ieee802154.md#std-dtcompatible-st-stm32wba-ieee802154"><code>st,stm32wba-ieee802154</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wba25ce1/nucleo_wba25ce1.dts?plain=1#L65">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32G0 外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L308">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P002_st_stm32g0-exti.md#std-dtcompatible-st-stm32g0-exti"><code>st,stm32g0-exti</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wba25ce1/nucleo_wba25ce1.dts?plain=1#L38">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wba25ce1/nucleo_wba25ce1.dts?plain=1#L57">已启用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L85">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>STM32闪存（Flash Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L190">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P016_st_stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash"><code>st,stm32-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">网络（Networking）</td>
<td>片上（On-Chip）</td>
<td>STM32WBA 2.4 GHz无线电（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L610">已启用：1</a>）</td>
<td><a href="../network_radio_frontend_binding_reference/P016_st_stm32wba-radio.md#std-dtcompatible-st-stm32wba-radio"><code>st,stm32wba-radio</code></a></td>
</tr>
<tr>
<td rowspan="1">非易失存储器（NVMEM）</td>
<td>片上（On-Chip）</td>
<td>非易失存储器固定布局（Fixed Layout for Non-Volatile Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L207">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P009_fixed-layout.md#std-dtcompatible-fixed-layout"><code>fixed-layout</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>STM32 嵌入式非易失一次性可编程存储器（NVM OTP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L203">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L196">已禁用：1</a>）</td>
<td><a href="../otp_binding_reference/P010_st_stm32-nvm-otp.md#std-dtcompatible-st-stm32-nvm-otp"><code>st,stm32-nvm-otp</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>STM32 引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L330">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P004_st_stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl"><code>st,stm32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>STM32WBA电源控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L245">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P018_st_stm32wba-pwr.md#std-dtcompatible-st-stm32wba-pwr"><code>st,stm32wba-pwr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32唤醒线控制器（Wake-up Lines Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L249">已禁用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P009_st_stm32-pwr-wkupctrl.md#std-dtcompatible-st-stm32-pwr-wkupctrl"><code>st,stm32-pwr-wkupctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>STM32 脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L457">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L485">已禁用：2</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P011_st_stm32-pwm.md#std-dtcompatible-st-stm32-pwm"><code>st,stm32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 复位与时钟控制器（Reset and Clock Control，RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L239">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P017_st_stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl"><code>st,stm32-rcc-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>STM32 随机数生成器（Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L591">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P016_st_stm32-rng.md#std-dtcompatible-st-stm32-rng"><code>st,stm32-rng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>STM32 实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L370">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P014_st_stm32-rtc.md#std-dtcompatible-st-stm32-rtc"><code>st,stm32-rtc</code></a></td>
</tr>
<tr>
<td rowspan="2">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>STM32 正交解码器（Quadrature Decoder）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L463">已禁用：1</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P028_st_stm32-qdec.md#std-dtcompatible-st-stm32-qdec"><code>st,stm32-qdec</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系列温度节点（TEMP），用于以两个温度点完成生产校准的传感器。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L628">已启用：1</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P029_st_stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal"><code>st,stm32-temp-cal</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L386">已启用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P016_st_stm32-usart.md#std-dtcompatible-st-stm32-usart"><code>st,stm32-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低功耗通用异步收发器（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L395">已禁用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P014_st_stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart"><code>st,stm32-lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">系统管理总线（SMbus）</td>
<td>片上（On-Chip）</td>
<td>STM32 系统管理总线控制器（SMBus Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L649">已禁用：2</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P013_st_stm32-smbus.md#std-dtcompatible-st-stm32-smbus"><code>st,stm32-smbus</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>STM32H7 串行外设接口控制器（SPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L404">已禁用：1</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P013_st_stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi"><code>st,stm32h7-spi</code></a></td>
</tr>
<tr>
<td rowspan="3">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 定时器（Timers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L441">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L470">已禁用：2</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P008_st_stm32-timers.md#std-dtcompatible-st-stm32-timers"><code>st,stm32-timers</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32U5低功耗定时器（LPTIM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L540">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L552">已禁用：1</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P009_st_stm32u5-lptim.md#std-dtcompatible-st-stm32u5-lptim"><code>st,stm32u5-lptim</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>STM32 看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wba/stm32wba.dtsi?plain=1#L379">已启用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P001_st_stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog"><code>st,stm32-watchdog</code></a></td>
</tr>
</table>

<a id="secure-bootloader"></a>

### 安全引导加载程序（Secure Bootloader）

<a id="stm32-oemxrot-integration"></a>

#### STM32 OEMxROT集成（Integration）

STM32CubeWBA提供名为STM32 OEMiROT的外部安全启动加载器，利用STM32WBA25CE1的安全功能。详情见[STM32WBA的OEMiRoT/OEMuRoT Wiki文章](https://wiki.st.com/stm32mcu/wiki/Security:OEMiRoT_OEMuRoT_for_STM32WBA)。

外部[STM32 OEMxROT模块](https://github.com/stm32-hotspot/zephyr-stm32-oemxrot)提供该启动加载器与Zephyr构建环境的集成。

<a id="default-zephyr-bootloader"></a>

#### 默认Zephyr启动加载器（Default Zephyr Bootloader）

STM32器件可通过Zephyr默认的MCUboot流程实现安全启动。SMP服务器应用是MCUboot镜像管理流程的一个使用示例。（[SMP服务器（Server）](../firmware_update/P022_SMP服务器示例.md#smp-svr)）

使用支持MCUmgr的客户端工具或库，以下流程使用[newtmgr](https://mynewt.apache.org/latest/newtmgr/index.html)。（[工具和库（Tools and Libraries）](https://docs.zephyrproject.org/latest/services/device_mgmt/mcumgr.html#tools-libraries)）

视板卡能力而定，可使用smp_svr应用通过UART串口连接更新镜像。

启用MCUboot及串口MCUmgr传输，构建示例：

```text
west build -b nucleo_wba25ce1 --sysbuild samples/subsys/mgmt/mcumgr/smp_svr -- \
  -DEXTRA_CONF_FILE=serial.conf
```

UART MCUmgr要求设备树chosen节点zephyr,uart-mcumgr。如果板卡没有定义它，应在samples/subsys/mgmt/mcumgr/smp_svr/boards/下添加应用的板级覆盖文件，例如：

```text
/ {
  chosen {
    zephyr,uart-mcumgr = &usart1;
  };
};
```

将&usart1替换为连接板卡串口的UART。

烧录smp_svr后，即可通过串口使用newtmgr。以下示例假定串口设备为/dev/ttyACM0。

```text
# Create the serial connection for your board, here on /dev/ttyACM0
newtmgr conn add serial type=serial connstring="dev=/dev/ttyACM0,baud=115200"
# Upload a new signed image to the download slot
newtmgr -c serial image upload build/smp_svr/zephyr/zephyr.signed.bin
# List the images and retrieve the hash of the image the download slot
newtmgr -c serial image list
# Mark this image as a test image
newtmgr -c serial image test <new_image_hash>
# Reset the device for the bootloader to install the image into the primary slot
newtmgr -c serial reset
# Once the image is validated, confirm it to make it permanent (skip this step and reset to revert)
newtmgr -c serial image confirm <new_image_hash>
```

<a id="low-power"></a>

### 低功耗（Low Power）

Nucleo WBA25CE1支持Zephyr电源管理，在应用空闲时进入低功耗状态。

为尽量降低功耗，本平台的Zephyr挂起到RAM（Suspend-to-RAM）使用STM32待机模式（Standby）。

应用须启用CONFIG_PM以打开电源管理：

```text
CONFIG_PM=y
```

STM32WBA的Suspend-to-RAM参考实现是心率监测器外设示例（Heart-rate Monitor，Peripheral），配合[samples/bluetooth/peripheral_hr/boards/stm32wba_pwr_optim.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_hr/boards/stm32wba_pwr_optim.overlay)使用。（[心率监测器外设（Heart-Rate Monitor / Peripheral）](../bluetooth_samples/P007_心率服务外设.md#ble_peripheral_hr)）

该覆盖文件可将sram0缩减到最低可用大小以降低功耗，pm_s2ram仍应位于可用RAM末尾。

构建命令示例：

```text
west build -b nucleo_wba25ce1 samples/bluetooth/peripheral_hr -- \
  -DDTC_OVERLAY_FILE=boards/stm32wba_stdby.overlay \
  -DCONFIG_PM=y
```

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

Nucleo WBA25CE1有4个通用输入输出（GPIO）控制器，负责引脚复用（Pin Muxing）、输入输出、上拉等功能。

<a id="default-zephyr-peripheral-mapping"></a>

#### Zephyr 默认外设映射（Peripheral Mapping）：


- USART_1 TX/RX : PA6/PA12
- I2C_3_SCL : PB2
- I2C_3_SDA : PA11
- USER_PB_1 : PA1
- USER_PB_2 : PC13
- USER_PB_3 : PA2
- LD1 : PA7
- LD2 : PB12
- LD3 : PB15
- SPI_3_NSS：PA5（Arduino SPI，arduino_spi）
- SPI_3_SCK：PA8（Arduino SPI，arduino_spi）
- SPI_3_MISO：PA10（Arduino SPI，arduino_spi）
- SPI_3_MOSI：PA9（Arduino SPI，arduino_spi）

<a id="system-clock"></a>

#### 系统时钟（System Clock）

Nucleo WBA25CE1系统时钟可来自内部振荡器、外部振荡器或主PLL，默认由HSE及PLL产生64 MHz系统时钟。

<a id="serial-port"></a>

#### 串口（Serial Port）

Nucleo WBA25CE1有1路USART，Zephyr控制台分配给USART1，默认参数115200、8N1。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`nucleo_wba25ce1`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>调试服务器（debugserver）</th>
<th>实时传输（rtt）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-stlink-gdbserver">stlink_gdbserver</a></td>
<td></td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-stm32cubeprogrammer"><code>stm32cubeprogrammer</code></a></td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

Nucleo WBA25CE1内置ST-LINK/V3调试工具接口，可通过STM32Cube生态工具烧录和调试。

<a id="flashing"></a>

### 烧录（Flashing）

此板默认通过west的[STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html)运行器（Runner）烧录，因此需要安装该工具。（[installation](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#stm32cubeprog-flash-host-tools)）

<a id="flashing-an-application-to-nucleo-wba25ce1"></a>

#### 向Nucleo WBA25CE1烧录应用（Flashing an Application）

以下以[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)应用为例。

```text
# From the root of the zephyr repository
west build -b nucleo_wba25ce1 samples/basic/blinky
west flash
```

可以看到LED每秒闪烁一次。

<a id="debugging"></a>

### 调试（Debugging）

<a id="debugging-using-st-link-gdb-server"></a>

#### 使用ST-LINK GDB Server调试

可以使用ST-LINK GDB Server调试应用，须先安装[STM32CubeCLT](https://www.st.com/en/development-tools/stm32cubeclt.html)。更多细节见“[STM32CubeCLT烧录与调试主机工具](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#stm32cubeclt-host-tools)（Flash & Debug Host Tools）”。

```text
# From the root of the zephyr repository
west build -b nucleo_wba25ce1 samples/basic/blinky
west debug
```

<a id="debugging-using-stm32cubeide"></a>

#### 使用STM32CubeIDE调试

可以使用兼容STM32WBA的STM32CubeIDE版本调试应用。

操作步骤如下：


- 通过File → New → STM32 project创建空STM32WBA项目。
- 选择MCU，点击下一步（Next），选择空项目（Empty Project）。
- 右键项目名，选择Debug as → Debug configurations。
- 在新窗口的STM32 Cortex-M C/C++ Application下创建调试目标。
- 选择新目标，在C/C++ Application字段填写zephyr.elf文件路径。
- 勾选禁止自动构建（Disable Auto Build）。
- 运行调试（Debug）。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [Security:OEMiRoT_OEMuRoT_for_STM32WBA](https://wiki.st.com/stm32mcu/wiki/Security:OEMiRoT_OEMuRoT_for_STM32WBA)：The read operation timed out。
- [stm32cubeclt.html](https://www.st.com/en/development-tools/stm32cubeclt.html)：HTTP Error 567: Unknown Status。
- [stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)：HTTP Error 567: Unknown Status。
- [stm32wba-series.html](https://www.st.com/en/microcontrollers-microprocessors/stm32wba-series.html)：HTTP Error 567: Unknown Status。

---

[上一章](P075_Nucleo_WB55RG.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P077_Nucleo_WBA55CG.md)
