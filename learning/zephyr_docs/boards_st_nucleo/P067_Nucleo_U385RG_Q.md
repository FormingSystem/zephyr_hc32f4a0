---
id: learning.zephyr-docs.boards-st-nucleo.page-67
title: Nucleo U385RG Q
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/st/nucleo_u385rg_q/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nucleo_u385rg_q"></a>

# 第67章\_Nucleo U385RG Q开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/st/nucleo_u385rg_q/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/nucleo_u385rg_q.webp](images/nucleo_u385rg_q.webp)](images/nucleo_u385rg_q.webp)

Nucleo U385RG Q开发板

名称（Name）：

`nucleo_u385rg_q`

厂商（Vendor）：

[意法半导体（STMicroelectronics）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=st)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[stm32u385xx](https://docs.zephyrproject.org/latest/boards/index.html#soc=stm32u385xx)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_u385rg_q/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Nucleo U385RG搭载基于Arm® Cortex®-M33且支持TrustZone®的STM32U385RG MCU，用户可选择不同性能与功耗组合，以经济、灵活的方式尝试新概念和构建原型。主要特点如下：


- LQFP64或LQFP48封装的STM32U385RG微控制器
- 两类扩展资源：


  - Arduino® Uno V3连接接口
  - ST morpho扩展排针，可访问全部STM32U3 I/O
- 板载STLINK-V2EC调试器／编程器支持USB重新枚举，提供大容量存储、虚拟COM端口及调试端口
- 灵活的开发板供电方式：


  - 通过USB VBUS或外部电源（3.3 V、5 V、7～12 V）供电
- 两个按键：USER及RESET
- 32.768 kHz晶体振荡器（Crystal Oscillator）
- 第二个用户LED与ARDUINO® Uno V3共用
- 通过外部或内部SMPS产生Vcore逻辑电源
- 24 MHz或48 MHz高速外部时钟（HSE）
- 用户USB全速设备，或USB全速受电端／上行端口（SNK/UFP）
- 密码功能（Cryptography）
- CAN FD收发器
- 开发板连接器（Board Connectors）：

> - 外部SMPS实验专用连接器
> - 用于ST-LINK的USB Type-C®、Micro-B或Mini-B连接器
> - 用户USB Type-C®连接器
> - MIPI®调试连接器
> - CAN FD排针

<a id="id3"></a>

更多信息见[NUCLEO_U385RG网站](https://www.st.com/en/evaluation-tools/nucleo-u385rg.html)[注1](#id2)。

<a id="hardware"></a>

## 硬件（Hardware）

STM32U385xx属于STM32U3超低功耗微控制器系列，基于Arm® Cortex®-M33 32位RISC内核，最高工作频率96 MHz。


- 采用ST先进专利技术
- 支持FlexPowerControl的超低功耗设计：


  - 供电电压1.71～3.6 V
  - 工作温度范围−40 °C至+105 °C
  - VBAT模式为RTC及32个32位备份寄存器供电
  - 保留8 Kbyte SRAM的Stop 3模式1.6 µA
  - 保留全部SRAM的Stop 3模式2.2 µA
  - 保留8 Kbyte SRAM的Stop 2模式3.8 µA
  - 保留全部SRAM的Stop 2模式4.5 µA
  - 3.3 V运行模式9.5 µA/MHz，执行While(1)，使用SMPS降压模式
  - 3.3 V、48 MHz运行模式13 µA/MHz，执行CoreMark®，使用SMPS降压模式
  - 3.3 V、96 MHz运行模式16 µA/MHz，执行CoreMark®，使用SMPS降压模式
  - 欠压复位（Brownout Reset）
- 处理器核（Core）：


  - 32位Arm® Cortex®-M33 CPU，支持TrustZone®及FPU
- 自适应实时加速器（ART Accelerator）：


  - 8 Kbyte指令缓存，支持从Flash及外部存储器零等待执行；最高96 MHz，带MPU，性能144 DMIPS，支持DSP指令
- 电源管理（Power Management）：


  - 内置LDO与SMPS降压转换器，支持运行中切换（Switch On-the-fly）及电压调节（Voltage Scaling）
- 基准测试（Benchmarks）：


  - 1.5 DMIPS/MHz，原文基准名称拼作Drystone 2.1
  - 387 CoreMark®，原文括注“4.09 CoreMark/MHz at 56 MHz”；数值及频率按来源保留。
  - ULPMark™-CP分数：500
  - ULPMark™-CM分数：117
  - SecureMark™-TLS分数：202000
- 存储器（Memories）：


  - 1 Mbyte Flash，支持ECC，双存储区，支持写入时读取
  - 256 Kbytes SRAM，其中64 Kbytes支持硬件奇偶校验
  - OCTOSPI外部存储器接口，支持SRAM、PSRAM、NOR、NAND及FRAM
- 通用输入输出（GPIO）：


  - 最多82个支持中断的高速I/O，多数耐受5 V；最多14个I/O具有独立供电，最低1.08 V
- 时钟管理（Clock Management）：


  - 4～50 MHz晶体振荡器
  - 用于RTC的32.768 kHz低速外部（LSE）晶体振荡器
  - 内部16 MHz出厂微调RC振荡器，精度±1%
  - 内部低功耗RC振荡器，频率32 kHz或250 Hz，精度±5%
  - 2个内部多速率振荡器，范围3～96 MHz
  - 内部48 MHz时钟，带时钟恢复（Clock Recovery）
  - 精密MSI支持PLL模式，以32.768 kHz、16 MHz或32 MHz晶体振荡器为基准，最高96 MHz
- 安全与密码功能（Security and Cryptography）：


  - Arm® TrustZone®，I/O、存储器及外设可配置安全属性
  - 灵活的生命周期方案，支持读出保护（RDP）及密码保护调试
  - 通过唯一启动入口及安全隐藏保护区域（HDP）建立信任根
  - 通过内置根安全服务（RSS）进行安全固件安装（SFI）
  - 利用硬件唯一密钥（Hardware Unique Key，HUK）进行安全数据存储
  - 安全固件升级（Secure Firmware Upgrade）
  - 支持Cortex-M可信固件（Trusted Firmware-M，TF-M）
  - 2个AES协处理器，其中1个为抵抗侧信道攻击（SCA）的SAES
  - 抵抗侧信道攻击的公钥加速器
  - 密钥硬件保护（Key Hardware Protection）
  - 证明密钥（Attestation Keys）
  - 哈希（HASH）硬件加速器
  - 符合NIST SP800-90B的真随机数发生器（TRNG）
  - 96位唯一标识（Unique ID）
  - 512字节一次性可编程存储器（OTP）
  - 防篡改保护（Antitamper Protection）
- 最多15个定时器及2个看门狗：


  - 一个16位高级电机控制定时器（Advanced Motor Control）
  - 3个32位及3个16位通用定时器
  - 两个16位基本定时器（Basic Timers）
  - 4个16位低功耗定时器，可在停止模式工作
  - 两个看门狗（Watchdogs）
  - 2个系统节拍（SysTick）定时器
  - 带硬件日历的RTC
  - 闹钟（Alarms）
  - 校准（Calibration）
- 最多19个通信外设：


  - 1个USB 2.0全速控制器
  - 1路串行音频接口（SAI）
  - 3路I2C FM+（1 Mbit/s），支持SMBus/PMBus™
  - 2路I3C单倍数据率（SDR）接口，支持I2C FM+模式
  - 2路USART及2路UART，支持SPI、ISO 7816、LIN、IrDA及调制解调器；另有1路LPUART
  - 3路SPI，计入1路OCTOSPI及2路USART可合计6路SPI
  - 1个CAN FD控制器
  - 1路SDMMC接口
  - 1个音频数字滤波器，带声音活动检测（Sound-activity Detection）
- 12通道通用DMA（GPDMA）控制器，可在睡眠模式（Sleep）及最深Stop 2的停止模式工作
- 最多21路电容感应通道：


  - 支持触摸按键、线性及旋转触摸传感器
- 丰富的模拟外设，具有独立供电：


  - 2个12位ADC，2.5 Msps，支持硬件过采样
  - 12位DAC模块，含2个D/A转换器，支持低功耗采样保持，可在Stop 1模式自主运行（Autonomous）
  - 2个运算放大器，内置PGA
  - 2个超低功耗比较器
- 循环冗余校验计算单元（CRC Calculation Unit）
- 调试（Debug）：


  - 开发支持：串行线调试（SWD）、JTAG及嵌入式跟踪宏单元（ETM）
- 符合ECOPACK2的封装

STM32U385RG的更多信息见：


- <a id="id8"></a>

  [STM32U385RG在ST官网的产品页](https://www.st.com/en/microcontrollers-microprocessors/stm32u385rg)[注3](#id7)
- <a id="id10"></a>

  [STM32U385RG参考手册](https://www.st.com/resource/en/reference_manual/rm0487-stm32u3-series-armbased-32bit-mcus-stmicroelectronics.pdf)（Reference Manual） [注4](#id9)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`nucleo_u385rg_q`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="nucleo_u385rg_q-hw-features"></a>

<a id="nucleo_u385rg_q-nucleo_u385rg_q@D/stm32u385xx-hw-features-section"></a>

#### `nucleo_u385rg_q@D/stm32u385xx`目标（Target）

<a id="nucleo_u385rg_q-nucleo_u385rg_q@D/stm32u385xx-hw-features-panel"></a>

<a id="nucleo_u385rg_q-nucleo_u385rg_q@D/stm32u385xx-hw-features-memory"></a>

此开发板目标可用存储器：256 KiB RAM、1 MiB 闪存。

<a id="nucleo_u385rg_q-nucleo_u385rg_q@D/stm32u385xx-hw-features-table"></a>

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
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>STM32N6模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L338">已启用：1</a>）</td>
<td><a href="../hardware/P842_STM32N6模数转换器绑定.md#dtbinding-st-stm32n6-adc"><code>st,stm32n6-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>STM32 FDCAN灵活数据速率CAN控制器（CAN FD Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L379">已启用：1</a>）</td>
<td><a href="../can_nxp_renesas_stm32_ti_binding_reference/P012_st_stm32-fdcan.md#std-dtcompatible-st-stm32-fdcan"><code>st,stm32-fdcan</code></a></td>
</tr>
<tr>
<td rowspan="5">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>STM32U5复位与时钟控制器（RCC / Reset and Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L195">已启用：1</a>）</td>
<td><a href="../timer_reference/P170_STM32U5复位与时钟控制绑定.md#dtbinding-st-stm32u5-rcc"><code>st,stm32u5-rcc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 外部高速时钟（HSE Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L88">已禁用：1</a>）</td>
<td><a href="../timer_reference/P129_STM32高速外部时钟绑定.md#dtbinding-st-stm32-hse-clock"><code>st,stm32-hse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L94">已启用：3</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32U3多速率内部时钟（MSI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L108">已启用：2</a>）</td>
<td><a href="../timer_reference/P159_STM32U3多速内部时钟绑定.md#dtbinding-st-stm32u3-msi-clock"><code>st,stm32u3-msi-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低速外部时钟（LSE Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L122">已启用：1</a>）</td>
<td><a href="../timer_reference/P130_STM32低速外部时钟绑定.md#dtbinding-st-stm32-lse-clock"><code>st,stm32-lse-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>STM32 计数器（Counters）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L610">已禁用：9</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P007_st_stm32-counter.md#std-dtcompatible-st-stm32-counter"><code>st,stm32-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>STM32 CRC 计算单元（Calculation Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L930">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P011_st_stm32-crc.md#std-dtcompatible-st-stm32-crc"><code>st,stm32-crc</code></a></td>
</tr>
<tr>
<td rowspan="2">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>STM32高级加密标准加速器（AES Accelerator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u385.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P015_st_stm32-aes.md#std-dtcompatible-st-stm32-aes"><code>st,stm32-aes</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32哈希处理器（HASH Processor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u385.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P017_st_stm32-hash.md#std-dtcompatible-st-stm32-hash"><code>st,stm32-hash</code></a></td>
</tr>
<tr>
<td rowspan="1">数模转换器（DAC）</td>
<td>片上（On-Chip）</td>
<td>STM32 系列数模转换器（DAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L371">已启用：1</a>）</td>
<td><a href="../hardware/P760_STM32数模转换器绑定.md#dtbinding-st-stm32-dac"><code>st,stm32-dac</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>STM32U5直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L463">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P012_st_stm32u5-dma.md#std-dtcompatible-st-stm32u5-dma"><code>st,stm32u5-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 系列闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L139">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P011_st_stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller"><code>st,stm32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用输入输出控制器（GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L236">已启用：7</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P029_st_stm32-gpio.md#std-dtcompatible-st-stm32-gpio"><code>st,stm32-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u385rg_q/arduino_r3_connector.dtsi?plain=1#L10">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>STM32 I2C V2 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L390">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L414">已禁用：1</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P008_st_stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2"><code>st,stm32-i2c-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>STM32 串行音频接口块控制器（SAI Block Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L553">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P017_st_stm32-sai.md#std-dtcompatible-st-stm32-sai"><code>st,stm32-sai</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>STM32H5 I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L426">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L439">已禁用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P010_st_stm32-i3c.md#std-dtcompatible-st-stm32-i3c"><code>st,stm32-i3c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u385rg_q/nucleo_u385rg_q.dts?plain=1#L36">已启用：1</a>）</td>
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
<td>STM32G0 外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L207">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P002_st_stm32g0-exti.md#std-dtcompatible-st-stm32g0-exti"><code>st,stm32g0-exti</code></a></td>
</tr>
<tr>
<td rowspan="2">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u385rg_q/nucleo_u385rg_q.dts?plain=1#L27">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组由脉宽调制（PWM）控制的LED（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u385rg_q/nucleo_u385rg_q.dts?plain=1#L46">已禁用：1</a>）</td>
<td><a href="../hardware/P565_PWM指示灯绑定.md#dtbinding-pwm-leds"><code>pwm-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L41">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">多位串行外设接口（Multi-Bit SPI）</td>
<td>片上（On-Chip）</td>
<td>STM32 XSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L514">已禁用：1</a>）</td>
<td><a href="../mspi_binding_reference/P014_st_stm32-xspi-controller.md#std-dtcompatible-st-stm32-xspi-controller"><code>st,stm32-xspi-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>STM32闪存（Flash Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L148">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P016_st_stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash"><code>st,stm32-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">非易失存储器（NVMEM）</td>
<td>片上（On-Chip）</td>
<td>非易失存储器固定布局（Fixed Layout for Non-Volatile Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L169">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P009_fixed-layout.md#std-dtcompatible-fixed-layout"><code>fixed-layout</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>STM32 嵌入式非易失一次性可编程存储器（NVM OTP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L165">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L158">已禁用：1</a>）</td>
<td><a href="../otp_binding_reference/P010_st_stm32-nvm-otp.md#std-dtcompatible-st-stm32-nvm-otp"><code>st,stm32-nvm-otp</code></a></td>
</tr>
<tr>
<td rowspan="1">物理层（PHY）</td>
<td>片上（On-Chip）</td>
<td>用于所有内置于 USB IP 的 USB 收发器（USB Transceivers）的绑定。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L939">已启用：1</a>）</td>
<td><a href="../phy_binding_reference/P008_usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv"><code>usb-nop-xceiv</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>STM32 引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L229">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P004_st_stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl"><code>st,stm32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>带LDO及SMPS双稳压器的STM32电源控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L852">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P007_st_stm32-dualreg-pwr.md#std-dtcompatible-st-stm32-dualreg-pwr"><code>st,stm32-dualreg-pwr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32唤醒线控制器（Wake-up Lines Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L863">已禁用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P009_st_stm32-pwr-wkupctrl.md#std-dtcompatible-st-stm32-pwr-wkupctrl"><code>st,stm32-pwr-wkupctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>STM32 脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L604">已禁用：7</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P011_st_stm32-pwm.md#std-dtcompatible-st-stm32-pwm"><code>st,stm32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 复位与时钟控制器（Reset and Clock Control，RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L201">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P017_st_stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl"><code>st,stm32-rcc-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>STM32 随机数生成器（Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L452">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P016_st_stm32-rng.md#std-dtcompatible-st-stm32-rng"><code>st,stm32-rng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>STM32 实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L543">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P014_st_stm32-rtc.md#std-dtcompatible-st-stm32-rtc"><code>st,stm32-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>STM32 正交解码器（Quadrature Decoder）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L615">已禁用：4</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P028_st_stm32-qdec.md#std-dtcompatible-st-stm32-qdec"><code>st,stm32-qdec</code></a></td>
</tr>
<tr>
<td rowspan="3">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L293">已启用：2</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P016_st_stm32-usart.md#std-dtcompatible-st-stm32-usart"><code>st,stm32-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L311">已禁用：2</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P015_st_stm32-uart.md#std-dtcompatible-st-stm32-uart"><code>st,stm32-uart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低功耗通用异步收发器（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L329">已启用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P014_st_stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart"><code>st,stm32-lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>STM32H7 串行外设接口控制器（SPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L475">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L488">已禁用：1</a>）</td>
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
<td>STM32 定时器（Timers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L622">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L594">已禁用：8</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P008_st_stm32-timers.md#std-dtcompatible-st-stm32-timers"><code>st,stm32-timers</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32U5低功耗定时器（LPTIM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L804">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L816">已禁用：3</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P009_st_stm32u5-lptim.md#std-dtcompatible-st-stm32u5-lptim"><code>st,stm32u5-lptim</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>STM32 USB控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L580">已启用：1</a>）</td>
<td><a href="../usb_stm32_audio_binding_reference/P006_st_stm32-usb.md#std-dtcompatible-st-stm32-usb"><code>st,stm32-usb</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>STM32 看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L528">已启用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P001_st_stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog"><code>st,stm32-watchdog</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系统窗口看门狗（System Window Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L535">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P002_st_stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog"><code>st,stm32-window-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

Nucleo U385RG有14个通用输入输出（GPIO）控制器，负责引脚复用（Pin Muxing）、输入输出、上拉等功能。

<a id="id5"></a>

更多细节见[STM32U385RG开发板用户手册](https://www.st.com/resource/en/user_manual/um3062-stm32u3u5-nucleo64-board-mb1841-stmicroelectronics.pdf)[注2](#id4)。

<a id="default-zephyr-peripheral-mapping"></a>

#### Zephyr 默认外设映射（Peripheral Mapping）：


- `DAC1_OUT1 : PA4`
- I2C1 SCL/SDA：PB6/PB7，修订版D的Arduino I2C，参见板卡修订版章节
- I2C2 SCL/SDA：PB13/PB14，修订版E的Arduino I2C，参见板卡修订版章节
- FDCAN1_TX : PA12
- FDCAN1_RX : PA11
- LD4 : PA5
- `LPUART_1_TX : PA2`
- `LPUART_1_RX : PA3`
- SPI3 NSS/SCK/MISO/MOSI : PA15/PB3/PB4/PB5（Arduino SPI接口）
- UART_1_TX：PA9
- UART_1_RX：PA10
- UART_3_TX : PC10
- UART_3_RX : PC11
- `USER_PB : PC13`
- I3C1 SCL/SDA : PB2/PC1

<a id="system-clock"></a>

#### 系统时钟（System Clock）

Nucleo U385RG系统时钟可来自内部振荡器、外部振荡器或主PLL。默认以4 MHz中速内部振荡器驱动PLL，产生48 MHz系统时钟。

<a id="serial-port"></a>

#### 串口（Serial Port）

Nucleo U385RG有4路U(S)ART及1路LPUART，Zephyr控制台分配给USART1，默认参数115200、8N1。

<a id="can"></a>

#### 控制器局域网（CAN）

STM32U385RG_Q没有板载CAN收发器。使用CAN总线时，须在PA11（FDCAN1_RX）及PA12（FDCAN1_TX）连接外部CAN收发器。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`nucleo_u385rg_q`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>复位（reset）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-pyocd">pyocd</a></td>
<td>✅</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-stm32cubeprogrammer"><code>stm32cubeprogrammer</code></a></td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

Nucleo U385RG内置ST-LINK/V3调试工具接口，可使用多种工具烧录开发板。

<a id="flashing"></a>

### 烧录（Flashing）

<a id="id12"></a>

开发板默认使用west的[STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html)运行器[注5](#id11)烧录，需要先安装该工具。（[installation](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#stm32cubeprog-flash-host-tools)）

也可以使用J-Link或pyOCD，通过--runner或-r选项烧录开发板：

```text
$ west flash --runner pyocd
$ west flash --runner jlink
```

pyOCD需要额外目标信息，可执行以下pyOCD命令安装：

```text
$ pyocd pack --update
$ pyocd pack --install stm32u3
```

<a id="flashing-an-application-to-nucleo-u385rg"></a>

#### 向Nucleo U385RG烧录应用（Flashing an Application）

通过USB将Nucleo U385RG连接主机，然后构建并烧录应用。以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例。

运行主机串口程序，连接Nucleo开发板：

```text
$ minicom -D /dev/ttyACM0
```

随后构建并烧录应用。

```text
# From the root of the zephyr repository
west build -b nucleo_u385rg_q samples/hello_world
west flash
```

控制台上应显示以下消息：

```text
Hello World! nucleo_u385rg_q
```

<a id="debugging"></a>

### 调试（Debugging）

可以按通常方式调试应用，以下以[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)为例。

```text
# From the root of the zephyr repository
west build -b nucleo_u385rg_q samples/basic/blinky
west debug
```

注意：检查build/tfm目录，确保系统提供脚本所需的命令，例如readlink；用于初始化的STM32_Programmer_CLI也必须在PATH中。

<a id="board-revisions"></a>

## 开发板修订版本（Board Revisions）

<a id="id6"></a>

[STM32U385RG开发板用户手册](https://www.st.com/resource/en/user_manual/um3062-stm32u3u5-nucleo64-board-mb1841-stmicroelectronics.pdf)[注2](#id4)列出两种板卡修订版：


- MB1841 D：Arduino D14/D15映射到PB7/PB6，即I2C1/I2C4
- MB1841 E：Arduino D14/D15可通过SB42/SB43/SB44/SB45焊桥配置；默认映射到PB14/PB13，即I2C2/I3C2；也可改为PB7/PB6，即I2C1/I2C4

默认使用修订版D。以下示例在修订版E上构建并烧录[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)：

```text
# From the root of the zephyr repository
west build -b nucleo_u385rg_q@E samples/basic/blinky
west flash
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.st.com/en/evaluation-tools/nucleo-u385rg.html](https://www.st.com/en/evaluation-tools/nucleo-u385rg.html)

<a id="id4"></a>

〔2〕 ([1](#id5),[2](#id6)) [https://www.st.com/resource/en/user_manual/um3062-stm32u3u5-nucleo64-board-mb1841-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um3062-stm32u3u5-nucleo64-board-mb1841-stmicroelectronics.pdf)

<a id="id7"></a>

〔[3](#id8)〕 [https://www.st.com/en/microcontrollers-microprocessors/stm32u385rg](https://www.st.com/en/microcontrollers-microprocessors/stm32u385rg)

<a id="id9"></a>

〔[4](#id10)〕 [https://www.st.com/resource/en/reference_manual/rm0487-stm32u3-series-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0487-stm32u3-series-armbased-32bit-mcus-stmicroelectronics.pdf)

<a id="id11"></a>

〔[5](#id12)〕 [https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)

## 译注

默认修订版D使用PB7/PB6，E默认使用PB14/PB13，可通过焊桥改回。CoreMark括注频率及数值不一致处照录。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)：HTTP Error 567: Unknown Status。
- [nucleo-u385rg.html](https://www.st.com/en/evaluation-tools/nucleo-u385rg.html)：HTTP Error 567: Unknown Status。
- [stm32u385rg](https://www.st.com/en/microcontrollers-microprocessors/stm32u385rg)：HTTP Error 567: Unknown Status。
- [rm0487-stm32u3-series-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0487-stm32u3-series-armbased-32bit-mcus-stmicroelectronics.pdf)：HTTP Error 567: Unknown Status。
- [um3062-stm32u3u5-nucleo64-board-mb1841-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um3062-stm32u3u5-nucleo64-board-mb1841-stmicroelectronics.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P066_Nucleo_U083RC.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P068_Nucleo_U3C5ZI_Q.md)
