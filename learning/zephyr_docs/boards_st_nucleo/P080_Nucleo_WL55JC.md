---
id: learning.zephyr-docs.boards-st-nucleo.page-80
title: Nucleo WL55JC
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/st/nucleo_wl55jc/doc/nucleo_wl55jc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nucleo_wl55jc"></a>

# 第80章\_Nucleo WL55JC开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/st/nucleo_wl55jc/doc/nucleo_wl55jc.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/nucleo_wl55jc.jpg](images/nucleo_wl55jc.jpg)](images/nucleo_wl55jc.jpg)

Nucleo WL55JC开发板

名称（Name）：

`nucleo_wl55jc`

厂商（Vendor）：

[意法半导体（STMicroelectronics）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=st)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[stm32wl55xx](https://docs.zephyrproject.org/latest/boards/index.html#soc=stm32wl55xx)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_wl55jc/doc/nucleo_wl55jc.rst/../..)<a id="overview"></a>

## 概述（Overview）

NUCLEO-WL55JC STM32WL Nucleo-64开发板提供经济、灵活的方式，用户可选择STM32WL系列的性能、功耗及功能组合，尝试新概念和构建原型。


- UFBGA73封装的STM32WL55JC多协议低功耗广域网（LPWAN）微控制器，32位双核Arm® Cortex®-M4/M0+，48 MHz，具有以下功能：


  - 超低功耗微控制器（MCU）
  - 射频收发器（RF Transceiver），频率范围150—960 MHz，支持LoRa、(G)FSK、(G)MSK及BPSK调制
  - 256 KB闪存及64 KB SRAM
- 三个用户LED
- 3个用户按键及1个复位按键
- 32.768 kHz LSE晶体振荡器
- 板载32 MHz高速外部（HSE）振荡器
- 开发板连接器（Board Connectors）：


  - USB Micro-B接口
  - MIPI调试连接器
  - ARDUINO Uno V3扩展连接器
  - ST morpho扩展排针，可访问全部STM32WL I/O
- 随附SMA天线
- 灵活供电方式：ST-LINK、USB VBUS或外部电源
- 板载STLINK-V3调试器／编程器支持USB重新枚举，提供大容量存储、虚拟COM端口及调试端口
- STM32CubeWL MCU软件包提供完整的免费软件库及示例
- 适合快速开发基于LoRaWAN、Sigfox、无线M-Bus（wM-Bus）及其他专有协议的终端节点（End Nodes）原型
- 完全开放的硬件平台

更多开发板信息见[Nucleo WL55JC网站](https://www.st.com/en/evaluation-tools/nucleo-wl55jc.html)。

<a id="hardware"></a>

## 硬件（Hardware）

STM32WL55JC长距离超低功耗无线器件内置符合LPWAN要求的无线电，支持LoRa®、(G)FSK、(G)MSK及BPSK调制，具有以下硬件能力：


- 无线电（Radio）


  - 频率范围：150～960 MHz
  - 调制方式：LoRa®、高斯／普通频移键控(G)FSK、高斯／普通最小频移键控(G)MSK及二进制相移键控BPSK
  - 接收灵敏度：2-FSK在1.2 Kbit/s时−123 dBm；LoRa®在10.4 kHz、扩频因子（Spreading Factor）12时−148 dBm
  - 高功率发射器，输出功率可编程，最高+22 dBm
  - 低功率发射器，输出功率可编程，最高+15 dBm
  - 原文列出的无线电法规包括ETSI EN 300 220、EN 300 113、EN 301 166，FCC CFR 47 Part 15、24、90、101，以及日本ARIB STD-T30、T-67、T-108
  - 兼容LoRaWAN®、Sigfox™、W-MBus等标准化或专有协议，属于完全开放的无线SoC
- 内核（Core）


  - 32位Arm® Cortex®-M4 CPU


    - 自适应实时加速器（ART Accelerator）支持从Flash零等待执行，最高48 MHz，带MPU及DSP指令
    - 1.25 DMIPS/MHz，Dhrystone 2.1基准
  - 32位Arm® Cortex®-M0+ CPU


    - 最高48 MHz，带MPU
    - 0.95 DMIPS/MHz，Dhrystone 2.1基准
- 安全与标识（Security and Identification）


  - AES 256位硬件加密
  - 真随机数发生器（RNG）
  - 扇区读写保护：PCROP、RDP及WRP
  - 循环冗余校验计算单元（CRC Calculation Unit）
  - 唯一器件标识符：符合IEEE 802-2001的64位UID
  - 96位唯一芯片标识符（Die Identifier）
  - 硬件公钥加速器（PKA）
  - 密钥管理服务（Key Management Services）
  - 安全sub-GHz媒体访问控制层（MAC Layer）
  - 安全固件更新（Secure Firmware Update，SFU）
  - 安全固件安装（Secure Firmware Install，SFI）
- 供电与复位管理（Supply and Reset Management）


  - 高效率内置SMPS降压转换器
  - SMPS与LDO智能切换
  - 高安全性低功耗欠压复位（BOR），5种可选阈值
  - 超低功耗上电／掉电复位（POR/PDR）
  - 可编程电压检测器（PVD）
  - VBAT模式提供RTC及备份寄存器；原文此处写20×32字节，后文写20×32位，两处单位均保留。
- 时钟源（Clock Sources）


  - 32 MHz晶体振荡器
  - 支持温度补偿晶体振荡器（TCXO），供电电压可编程
  - 用于RTC的32 kHz振荡器，支持校准
  - 高速内部16 MHz出厂微调RC振荡器，精度±1%
  - 内部低功耗32 kHz RC振荡器
  - 内部多速率低功耗RC振荡器，范围100 kHz～48 MHz
  - 用于CPU、ADC及音频时钟的PLL
- 存储器（Memories）


  - 256 Kbyte Flash
  - 64 Kbyte RAM
  - 20个32位备份寄存器
  - 启动加载器支持USART及SPI接口
  - 支持空中（Over-the-air，OTA）固件更新
  - 扇区读写操作保护
- 丰富的模拟外设，供电最低1.62 V


  - 12位ADC，2.5 Msps，通过硬件过采样可达16位，转换电压范围最高3.6 V
  - 12位DAC，支持低功耗采样保持
  - 两个超低功耗比较器（Comparators）
- 系统外设（System Peripherals）


  - 邮箱（Mailbox）及信号量（Semaphores），用于Cortex-M4与Cortex-M0+固件间通信
- 控制器（Controllers）


  - 2个DMA控制器，每个7通道，支持ADC、DAC、SPI、I2C、LPUART、USART、AES及定时器
  - 2路USART，支持ISO 7816、IrDA及SPI
  - 1路低功耗UART（LPUART）
  - 2路16 Mbit/s SPI，其中1路支持I2S
  - 3路I2C，支持SMBus/PMBus™
  - 2个16位单通道定时器
  - 1个16位四通道定时器，支持电机控制
  - 1个32位四通道定时器
  - 3个16位超低功耗定时器
  - 1个RTC，带32位亚秒唤醒计数器（Sub-second Wakeup Counter）
  - 1个独立SysTick
  - 1个独立看门狗
  - 1个窗口看门狗
- 最多43个I/O，多数耐受5 V
- 开发支持：SWD、JTAG及双CPU交叉触发（Cross Trigger）能力

STM32WL55JC的更多信息见：


- [STM32WL55JC在ST官网的产品页](https://www.st.com/en/microcontrollers-microprocessors/stm32wl55jc.html)
- [STM32WL55JC数据手册（Datasheet）](https://www.st.com/resource/en/datasheet/stm32wl55jc.pdf)
- [STM32WL55JC参考手册（Reference Manual）](https://www.st.com/resource/en/reference_manual/dm00451556-stm32wl5x-advanced-armbased-32bit-mcus-with-subghz-radio-solution-stmicroelectronics.pdf)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`nucleo_wl55jc`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="nucleo_wl55jc-hw-features"></a>

<a id="nucleo_wl55jc-nucleo_wl55jc/stm32wl55xx-hw-features-section"></a>

#### `nucleo_wl55jc/stm32wl55xx`目标（Target）

<a id="nucleo_wl55jc-nucleo_wl55jc/stm32wl55xx-hw-features-panel"></a>

<a id="nucleo_wl55jc-nucleo_wl55jc/stm32wl55xx-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、256 KiB Flash。

<a id="nucleo_wl55jc-nucleo_wl55jc/stm32wl55xx-hw-features-table"></a>

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
<td>ARM Cortex-M4 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P024_arm_cortex-m4.md#std-dtcompatible-arm-cortex-m4"><code>arm,cortex-m4</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>STM32模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L400">已启用：1</a>）</td>
<td><a href="../hardware/P839_STM32模数转换器绑定.md#dtbinding-st-stm32-adc"><code>st,stm32-adc</code></a></td>
</tr>
<tr>
<td rowspan="7">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>STM32WL复位与时钟控制器（RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L179">已启用：1</a>）</td>
<td><a href="../timer_reference/P173_STM32WL复位与时钟控制绑定.md#dtbinding-st-stm32wl-rcc"><code>st,stm32wl-rcc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32WL高速外部时钟（HSE）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L70">已禁用：1</a>）</td>
<td><a href="../timer_reference/P164_STM32WL高速外部时钟绑定.md#dtbinding-st-stm32wl-hse-clock"><code>st,stm32wl-hse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L78">已启用：2</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32多速内部时钟（MSI Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L85">已禁用：1</a>）</td>
<td><a href="../timer_reference/P132_STM32多速内部时钟绑定.md#dtbinding-st-stm32-msi-clock"><code>st,stm32-msi-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低速外部时钟（LSE Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L92">已启用：1</a>）</td>
<td><a href="../timer_reference/P130_STM32低速外部时钟绑定.md#dtbinding-st-stm32-lse-clock"><code>st,stm32-lse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32WB及STM32WL锁相环（PLL）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L107">已启用：1</a>）</td>
<td><a href="../timer_reference/P151_STM32WB锁相环时钟绑定.md#dtbinding-st-stm32wb-pll-clock"><code>st,stm32wb-pll-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 微控制器时钟输出（Microcontroller Clock Output，MCO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L115">已禁用：1</a>）</td>
<td><a href="../timer_reference/P134_STM32时钟输出绑定.md#dtbinding-st-stm32-clock-mco"><code>st,stm32-clock-mco</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>STM32 计数器（Counters）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L449">已禁用：4</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P007_st_stm32-counter.md#std-dtcompatible-st-stm32-counter"><code>st,stm32-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>STM32 CRC 计算单元（Calculation Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L620">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P011_st_stm32-crc.md#std-dtcompatible-st-stm32-crc"><code>st,stm32-crc</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>STM32高级加密标准加速器（AES Accelerator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L536">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P015_st_stm32-aes.md#std-dtcompatible-st-stm32-aes"><code>st,stm32-aes</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>STM32 系列数模转换器（DAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L424">已启用：1</a>）</td>
<td><a href="../hardware/P760_STM32数模转换器绑定.md#dtbinding-st-stm32-dac"><code>st,stm32-dac</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>STM32直接存储器访问控制器（DMA Controller，V2）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L556">已禁用：2</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P008_st_stm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2"><code>st,stm32-dma-v2</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 DMA 多路复用控制器（DMAMUX Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L578">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P011_st_stm32-dmamux.md#std-dtcompatible-st-stm32-dmamux"><code>st,stm32-dmamux</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 系列闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L123">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P011_st_stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller"><code>st,stm32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="3">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用输入输出控制器（GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L213">已启用：4</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P029_st_stm32-gpio.md#std-dtcompatible-st-stm32-gpio"><code>st,stm32-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wl55jc/arduino_r3_connector.dtsi?plain=1#L10">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到ST Morpho连接器的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wl55jc/st_morpho_connector.dtsi?plain=1#L10">已启用：1</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P003_st-morpho-header.md#std-dtcompatible-st-morpho-header"><code>st-morpho-header</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>STM32 I2C V2 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L335">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L323">已禁用：2</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P008_st_stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2"><code>st,stm32-i2c-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wl55jc/nucleo_wl55jc.dts?plain=1#L46">已启用：1</a>）</td>
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
<td>STM32 外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L190">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P001_st_stm32-exti.md#std-dtcompatible-st-stm32-exti"><code>st,stm32-exti</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wl55jc/nucleo_wl55jc.dts?plain=1#L27">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">远距离无线通信（LoRa）</td>
<td>片上（On-Chip）</td>
<td>STM32WL Sub-GHz无线电（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L391">已启用：1</a>）</td>
<td><a href="../lora_ieee802154_binding_reference/P026_st_stm32wl-subghz-radio.md#std-dtcompatible-st-stm32wl-subghz-radio"><code>st,stm32wl-subghz-radio</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 电池备份 RAM（Battery-Backed RAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L274">已禁用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P010_st_stm32-bbram.md#std-dtcompatible-st-stm32-bbram"><code>st,stm32-bbram</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>STM32闪存（Flash Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L132">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P016_st_stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash"><code>st,stm32-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">非易失存储器（NVMEM）</td>
<td>片上（On-Chip）</td>
<td>非易失存储器固定布局（Fixed Layout for Non-Volatile Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L153">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P009_fixed-layout.md#std-dtcompatible-fixed-layout"><code>fixed-layout</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>STM32 嵌入式非易失一次性可编程存储器（NVM OTP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L149">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L142">已禁用：1</a>）</td>
<td><a href="../otp_binding_reference/P010_st_stm32-nvm-otp.md#std-dtcompatible-st-stm32-nvm-otp"><code>st,stm32-nvm-otp</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>STM32 引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L206">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P004_st_stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl"><code>st,stm32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>STM32 电源控制器（Power Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L590">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P010_st_stm32-pwr.md#std-dtcompatible-st-stm32-pwr"><code>st,stm32-pwr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32唤醒线控制器（Wake-up Lines Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L594">已禁用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P009_st_stm32-pwr-wkupctrl.md#std-dtcompatible-st-stm32-pwr-wkupctrl"><code>st,stm32-pwr-wkupctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>STM32 脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L472">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L443">已禁用：3</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P011_st_stm32-pwm.md#std-dtcompatible-st-stm32-pwm"><code>st,stm32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 复位与时钟控制器（Reset and Clock Control，RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L184">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P017_st_stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl"><code>st,stm32-rcc-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>STM32 随机数生成器（Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L545">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P016_st_stm32-rng.md#std-dtcompatible-st-stm32-rng"><code>st,stm32-rng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>STM32 实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L258">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P014_st_stm32-rtc.md#std-dtcompatible-st-stm32-rtc"><code>st,stm32-rtc</code></a></td>
</tr>
<tr>
<td rowspan="4">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>STM32 正交解码器（Quadrature Decoder）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L454">已禁用：2</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P028_st_stm32-qdec.md#std-dtcompatible-st-stm32-qdec"><code>st,stm32-qdec</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系列温度节点（TEMP），用于以两个温度点完成生产校准的传感器。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L629">已启用：1</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P029_st_stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal"><code>st,stm32-temp-cal</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 参考电压（VREF+）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L640">已启用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P003_st_stm32-vref.md#std-dtcompatible-st-stm32-vref"><code>st,stm32-vref</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 电池电压（VBAT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L648">已启用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P001_st_stm32-vbat.md#std-dtcompatible-st-stm32-vbat"><code>st,stm32-vbat</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L295">已禁用：2</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P016_st_stm32-usart.md#std-dtcompatible-st-stm32-usart"><code>st,stm32-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低功耗通用异步收发器（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L313">已启用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P014_st_stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart"><code>st,stm32-lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">系统管理总线（SMbus）</td>
<td>片上（On-Chip）</td>
<td>STM32 系统管理总线控制器（SMBus Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L655">已禁用：3</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P013_st_stm32-smbus.md#std-dtcompatible-st-stm32-smbus"><code>st,stm32-smbus</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>带嵌入式接收和发送先进先出队列（Rx / Tx FIFOs）的STM32 SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L359">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L370">已禁用：1</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P009_st_stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo"><code>st,stm32-spi-fifo</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 SUBGHZ SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L381">已启用：1</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P011_st_stm32-spi-subghz.md#std-dtcompatible-st-stm32-spi-subghz"><code>st,stm32-spi-subghz</code></a></td>
</tr>
<tr>
<td rowspan="3">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低功耗定时器（LPTIM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L246">已启用：1</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P007_st_stm32-lptim.md#std-dtcompatible-st-stm32-lptim"><code>st,stm32-lptim</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 定时器（Timers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L461">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L432">已禁用：3</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P008_st_stm32-timers.md#std-dtcompatible-st-stm32-timers"><code>st,stm32-timers</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>STM32 看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L281">已启用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P001_st_stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog"><code>st,stm32-watchdog</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系统窗口看门狗（System Window Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L287">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P002_st_stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog"><code>st,stm32-window-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

Nucleo WL55JC有4个通用输入输出（GPIO）控制器，负责引脚复用（Pin Muxing）、输入输出、上拉等功能。

<a id="default-zephyr-peripheral-mapping"></a>

#### Zephyr 默认外设映射（Peripheral Mapping）：


- LPUART_1 TX/RX : PA3/PA2（ST-Link虚拟COM端口）
- I2C_2_SCL : PA12（Arduino I2C接口）
- I2C_2_SDA : PA11（Arduino I2C接口）
- SPI_1_NSS：PA4（Arduino SPI，arduino_spi）
- SPI_1_SCK：PA5（Arduino SPI，arduino_spi）
- SPI_1_MISO：PA6（Arduino SPI，arduino_spi）
- SPI_1_MOSI：PA7（Arduino SPI，arduino_spi）
- ADC1_IN5：PB1（Arduino A0引脚）
- DAC1_OUT1：PA10（Arduino A2引脚）

<a id="system-clock"></a>

#### 系统时钟（System Clock）

Nucleo WL55JC系统时钟可来自内部振荡器、外部振荡器或主PLL，默认由32 MHz HSE驱动。

<a id="serial-port"></a>

#### 串口（Serial Port）

Nucleo WL55JC有2路(LP)U(S)ART，Zephyr控制台分配给LPUART_1，默认参数115200、8N1。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`nucleo_wl55jc`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-stlink-gdbserver">stlink_gdbserver</a></td>
<td></td>
<td>✅</td>
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

Nucleo WL55JC内置STLINK-V3调试工具接口。

nucleo_wl55jc的应用可按常规方式构建，详见“[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)”。

<a id="flashing"></a>

### 烧录（Flashing）

此板默认通过west的[STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html)运行器（Runner）烧录，因此需要安装该工具。（[installation](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#stm32cubeprog-flash-host-tools)）

也可使用OpenOCD，通过--runner或-r选项烧录开发板：

```text
$ west flash --runner openocd
```

<a id="flashing-an-application-to-nucleo-wl55jc"></a>

#### 向Nucleo WL55JC烧录应用（Flashing an Application）

通过USB将Nucleo WL55JC连接主机，然后构建并烧录应用。以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例。

运行主机串口程序，连接Nucleo开发板：

```text
$ minicom -D /dev/ttyUSB0
```

随后构建并烧录应用。

```text
# From the root of the zephyr repository
west build -b nucleo_wl55jc samples/hello_world
west flash
```

控制台上应显示以下消息：

```text
Hello World! arm
```

<a id="debugging"></a>

### 调试（Debugging）

可以按通常方式调试应用，以下以[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)为例。

```text
# From the root of the zephyr repository
west build -b nucleo_wl55jc samples/basic/blinky
west debug
```

## 译注

备份寄存器原文一处写20×32字节、另一处写20×32位，差异保留。硬件无线能力与Zephyr功能状态分别阅读。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)：HTTP Error 567: Unknown Status。
- [nucleo-wl55jc.html](https://www.st.com/en/evaluation-tools/nucleo-wl55jc.html)：HTTP Error 567: Unknown Status。
- [stm32wl55jc.html](https://www.st.com/en/microcontrollers-microprocessors/stm32wl55jc.html)：HTTP Error 567: Unknown Status。
- [stm32wl55jc.pdf](https://www.st.com/resource/en/datasheet/stm32wl55jc.pdf)：HTTP Error 567: Unknown Status。
- [dm00451556-stm32wl5x-advanced-armbased-32bit-mcus-with-subghz-radio-solution-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/dm00451556-stm32wl5x-advanced-armbased-32bit-mcus-with-subghz-radio-solution-stmicroelectronics.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P079_Nucleo_WL33CC1.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
