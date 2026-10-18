---
id: learning.zephyr-docs.boards-st-nucleo.page-75
title: Nucleo WB55RG
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/st/nucleo_wb55rg/doc/nucleo_wb55rg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nucleo_wb55rg"></a>

# 第75章\_Nucleo WB55RG开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/st/nucleo_wb55rg/doc/nucleo_wb55rg.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/nucleowb55rg.jpg](images/nucleowb55rg.jpg)](images/nucleowb55rg.jpg)

Nucleo WB55RG开发板

名称（Name）：

`nucleo_wb55rg`

厂商（Vendor）：

[意法半导体（STMicroelectronics）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=st)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[stm32wb55xx](https://docs.zephyrproject.org/latest/boards/index.html#soc=stm32wb55xx)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_wb55rg/doc/nucleo_wb55rg.rst/../..)<a id="overview"></a>

## 概述（Overview）

Nucleo WB55RG是一款多协议超低功耗无线设备，内置符合Bluetooth® LE SIG 5.0及IEEE 802.15.4-2011规范的高性能超低功耗无线电。


- VFQFPN68封装的STM32微控制器
- 2.4 GHz射频收发器，支持Bluetooth 5.0及IEEE 802.15.4-2011 PHY／MAC
- 专用于实时无线电层（Radio Layer）的Arm® 32位Cortex®-M0+ CPU
- 3个用户LED
- 板级连接器：用户USB Micro-B
- 两类扩展资源：


  - Arduino Uno V3连接接口
  - ST morpho扩展排针，可访问全部STM32 I/O
- 集成PCB天线或SMA连接器焊盘
- 带SWD连接器的板载ST-LINK/V2-1调试器／编程器
- 灵活供电方式：ST-LINK USB VBUS或外部电源
- 板载CR2032电池座
- 板载ST-LINK/V2-1调试器／编程器支持USB重新枚举，提供大容量存储、虚拟COM端口及调试端口

更多开发板信息见[Nucleo WB55RG网站](https://www.st.com/en/evaluation-tools/p-nucleo-wb55.html)。

<a id="hardware"></a>

## 硬件（Hardware）

STM32WB55RG是一款超低功耗双核SoC：64 MHz Arm Cortex-M4及32 MHz Cortex-M0，具备1 Mbyte Flash、Bluetooth® 5、802.15.4、USB、LCD及AES-256。原文此处写M0，上方核心说明为M0+；其硬件能力如下：


- 带FlexPowerControl的超低功耗设计，保留RTC及32 KB RAM的待机模式低至600 nA
- 32位ARM Cortex-M4内核，带FPU，最高64 MHz
- 无线电（Radio）：


  - 2.4GHz
  - 射频收发器支持Bluetooth 5、IEEE 802.15.4-2011 PHY／MAC、Thread及Zigbee 3.0
  - 接收灵敏度：Bluetooth LE 1 Mbit/s时−96 dBm，802.15.4时−100 dBm
  - 可编程输出功率最高+6 dBm，步进1 dB
  - 集成平衡不平衡转换器（Balun），减少物料清单（BOM）
  - 支持2 Mbit/s
  - 专用于实时无线电层（Radio Layer）的Arm® 32位Cortex®-M0+ CPU
  - 精确接收信号强度指示（RSSI），用于功率控制
  - 适用于需要符合ETSI EN 300 328、EN 300 440、FCC CFR47 Part 15及ARIB STD-T66无线电法规的系统
  - 支持外部功率放大器（PA）
- 时钟源（Clock Sources）：


  - 32 MHz晶体振荡器，带集成微调电容，用于无线电及CPU时钟
  - 用于实时时钟（RTC）的32 kHz低速外部晶体振荡器（LSE）
  - 2个内部低功耗32 kHz RC振荡器，精度分别为±5%及±500 ppm
  - 内部多速率100 kHz至48 MHz振荡器，由LSE自动校准，精度优于±0.25%
  - 2个PLL，用于系统时钟、USB、SAI及ADC
- 带硬件日历、闹钟及校准功能的实时时钟（RTC）
- LCD驱动8×40或4×44，带升压转换器（Step-up Converter）
- 最多24个电容感应通道，支持触摸键、线性及旋转触摸传感器
- 16个定时器（Timers）：


  - 两个16位高级电机控制定时器（Advanced Motor-Control）
  - 通用定时器：2个32位及5个16位
  - 两个16位基本定时器（Basic Timers）
  - 两个16位低功耗定时器，在停止模式（Stop Mode）下可用
  - 两个看门狗（Watchdogs）
  - 系统节拍定时器（SysTick Timer）
- 最多114个高速I/O，多数耐受5 V；最多14个I/O具有独立供电，最低1.08 V
- 存储器（Memories）


  - 最多1 MB闪存，双存储区支持读写并行（Read-While-Write），提供专有代码读出保护（Code Readout Protection）
  - 最多320 KB SRAM，其中64 KB支持硬件奇偶校验
  - 面向静态存储器的外部存储器接口（External Memory Interface），支持SRAM、PSRAM、NOR和NAND存储器
  - 四线SPI存储器接口（Quad SPI Memory Interface）
- 四个用于Σ-Δ调制器（Sigma Delta Modulator）的数字滤波器（Digital Filters）
- 丰富的模拟外设，供电最低1.62 V


  - 12位ADC，4.26 Msps，通过硬件过采样可达16位，功耗200 µA/Msps
  - 2个超低功耗比较器
  - 精密2.5 V或2.048 V参考电压缓冲输出
- 系统外设（System Peripherals）


  - 处理器间通信控制器（IPCC），用于与Bluetooth® LE及802.15.4通信
  - 用于CPU间资源共享的硬件信号量（Hardware Semaphores）
  - 2个DMA控制器，每个7通道，支持ADC、SPI、I2C、USART、QSPI、SAI、AES及定时器
  - 1路USART，支持ISO 7816、IrDA、SPI主机、Modbus及智能卡模式（Smartcard Mode）
  - 1路低功耗UART（LPUART）
  - 2路SPI，32 Mbit/s
  - 2路I2C，支持SMBus/PMBus
  - 1路SAI，支持双通道高品质音频
  - 1个无需晶体的USB 2.0全速设备接口，支持电池充电检测（BCD）及链路电源管理（LPM）
  - 触摸感应控制器，最多18个传感器
  - 8×40 LCD驱动，带升压转换器
  - 1个16位四通道高级定时器
  - 2个16位双通道定时器
  - 1个32位四通道定时器
  - 2个16位超低功耗定时器
  - 1个独立SysTick
  - 1个独立看门狗
  - 1个窗口看门狗
- 安全及标识（Security and ID）

> - 3个最高256位AES硬件加密单元，分别服务于应用、Bluetooth® LE及IEEE 802.15.4
> - 用户密钥存储及密钥管理服务
> - 公钥硬件单元（PKA）；原文将全称写为public key authority
> - 密码算法：RSA、Diffie-Hellman及GF(p)上的椭圆曲线密码（ECC）；原文将Diffie-Hellman拼作Diffie-Helman。
> - 真随机数发生器（RNG）
> - 扇区读写操作保护（PCROP）
> - 循环冗余校验计算单元（CRC Calculation Unit）
> - 96位唯一标识（Unique ID）
> - 64位唯一ID，可派生64位及Bluetooth® LE 48位扩展唯一标识（EUI）。原文前者协议写802.15.5，保留该编号差异。


- 最多72个高速I/O，其中70个耐受5 V
- 开发支持：串行线调试（SWD）、JTAG及嵌入式跟踪宏单元（Embedded Trace Macrocell™）

STM32WB55RG的更多信息见：


- [STM32WB55RG在ST官网的产品页](https://www.st.com/en/microcontrollers-microprocessors/stm32wb55rg.html)
- [STM32WB55RG数据手册（Datasheet）](https://www.st.com/resource/en/datasheet/stm32wb55rg.pdf)
- [STM32WB55RG参考手册（Reference Manual）](https://www.st.com/resource/en/reference_manual/dm00318631.pdf)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`nucleo_wb55rg`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="nucleo_wb55rg-hw-features"></a>

<a id="nucleo_wb55rg-nucleo_wb55rg/stm32wb55xx-hw-features-section"></a>

#### `nucleo_wb55rg/stm32wb55xx`目标（Target）

<a id="nucleo_wb55rg-nucleo_wb55rg/stm32wb55xx-hw-features-panel"></a>

<a id="nucleo_wb55rg-nucleo_wb55rg/stm32wb55xx-hw-features-memory"></a>

此目标可用存储：192 KiB RAM、876 KiB闪存。

<a id="nucleo_wb55rg-nucleo_wb55rg/stm32wb55xx-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L35">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>STM32模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L495">已启用：1</a>）</td>
<td><a href="../hardware/P839_STM32模数转换器绑定.md#dtbinding-st-stm32-adc"><code>st,stm32-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>STM32WB无线电设备（Radio Device）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L703">已启用：1</a>）</td>
<td><a href="../bluetooth_st_transport_binding_reference/P006_st_stm32wb-rf.md#std-dtcompatible-st-stm32wb-rf"><code>st,stm32wb-rf</code></a></td>
</tr>
<tr>
<td rowspan="6">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>STM32WB复位与时钟控制器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L218">已启用：1</a>）</td>
<td><a href="../timer_reference/P172_STM32WB复位与时钟控制绑定.md#dtbinding-st-stm32wb-rcc"><code>st,stm32wb-rcc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L84">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L92">已禁用：2</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32多速内部时钟（MSI Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L106">已禁用：1</a>）</td>
<td><a href="../timer_reference/P132_STM32多速内部时钟绑定.md#dtbinding-st-stm32-msi-clock"><code>st,stm32-msi-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低速外部时钟（LSE Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L113">已启用：1</a>）</td>
<td><a href="../timer_reference/P130_STM32低速外部时钟绑定.md#dtbinding-st-stm32-lse-clock"><code>st,stm32-lse-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32WB及STM32WL锁相环（PLL）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L135">已禁用：1</a>）</td>
<td><a href="../timer_reference/P151_STM32WB锁相环时钟绑定.md#dtbinding-st-stm32wb-pll-clock"><code>st,stm32wb-pll-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 时钟多路复用器（Clock Multiplexer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L141">已禁用：1</a>）</td>
<td><a href="../timer_reference/P133_STM32时钟多路复用绑定.md#dtbinding-st-stm32-clock-mux"><code>st,stm32-clock-mux</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>STM32 计数器（Counters）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L408">已禁用：4</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P007_st_stm32-counter.md#std-dtcompatible-st-stm32-counter"><code>st,stm32-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>STM32 CRC 计算单元（Calculation Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L663">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P011_st_stm32-crc.md#std-dtcompatible-st-stm32-crc"><code>st,stm32-crc</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>STM32高级加密标准加速器（AES Accelerator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L605">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P015_st_stm32-aes.md#std-dtcompatible-st-stm32-aes"><code>st,stm32-aes</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>STM32直接存储器访问控制器（DMA Controller，V2）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L539">已禁用：2</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P008_st_stm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2"><code>st,stm32-dma-v2</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 DMA 多路复用控制器（DMAMUX Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L561">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P011_st_stm32-dmamux.md#std-dtcompatible-st-stm32-dmamux"><code>st,stm32-dmamux</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 系列闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L149">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P011_st_stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller"><code>st,stm32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用输入输出控制器（GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L251">已启用：6</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P029_st_stm32-gpio.md#std-dtcompatible-st-stm32-gpio"><code>st,stm32-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wb55rg/arduino_r3_connector.dtsi?plain=1#L10">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>STM32 I2C V2 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L319">已启用：2</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P008_st_stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2"><code>st,stm32-i2c-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wb55rg/nucleo_wb55rg.dts?plain=1#L47">已启用：1</a>）</td>
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
<td>STM32 外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L229">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P001_st_stm32-exti.md#std-dtcompatible-st-stm32-exti"><code>st,stm32-exti</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wb55rg/nucleo_wb55rg.dts?plain=1#L28">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 电池备份 RAM（Battery-Backed RAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L353">已启用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P010_st_stm32-bbram.md#std-dtcompatible-st-stm32-bbram"><code>st,stm32-bbram</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>STM32闪存（Flash Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L159">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P016_st_stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash"><code>st,stm32-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">非易失存储器（NVMEM）</td>
<td>片上（On-Chip）</td>
<td>非易失存储器固定布局（Fixed Layout for Non-Volatile Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L180">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P009_fixed-layout.md#std-dtcompatible-fixed-layout"><code>fixed-layout</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>STM32 嵌入式非易失一次性可编程存储器（NVM OTP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L176">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L169">已禁用：1</a>）</td>
<td><a href="../otp_binding_reference/P010_st_stm32-nvm-otp.md#std-dtcompatible-st-stm32-nvm-otp"><code>st,stm32-nvm-otp</code></a></td>
</tr>
<tr>
<td rowspan="1">物理层（PHY）</td>
<td>片上（On-Chip）</td>
<td>用于所有内置于 USB IP 的 USB 收发器（USB Transceivers）的绑定。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L698">已启用：1</a>）</td>
<td><a href="../phy_binding_reference/P008_usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv"><code>usb-nop-xceiv</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>STM32 引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L244">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P004_st_stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl"><code>st,stm32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="2">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>STM32 电源控制器（Power Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L623">已启用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P010_st_stm32-pwr.md#std-dtcompatible-st-stm32-pwr"><code>st,stm32-pwr</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32唤醒线控制器（Wake-up Lines Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L627">已禁用：1</a>）</td>
<td><a href="../stm32_soc_power_binding_reference/P009_st_stm32-pwr-wkupctrl.md#std-dtcompatible-st-stm32-pwr-wkupctrl"><code>st,stm32-pwr-wkupctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>STM32 脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L402">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L460">已禁用：2</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P011_st_stm32-pwm.md#std-dtcompatible-st-stm32-pwm"><code>st,stm32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">四线串行外设接口（QSPI）</td>
<td>片上（On-Chip）</td>
<td>STM32 四线串行外设接口控制器（QSPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L587">已禁用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P011_st_stm32-qspi.md#std-dtcompatible-st-stm32-qspi"><code>st,stm32-qspi</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>STM32参考电压缓冲器稳压器（VREFBUF Regulator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L614">已禁用：1</a>）</td>
<td><a href="../hardware/P638_STM32参考电压缓冲器绑定.md#dtbinding-st-stm32-vrefbuf"><code>st,stm32-vrefbuf</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 复位与时钟控制器（Reset and Clock Control，RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L223">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P017_st_stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl"><code>st,stm32-rcc-rctl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>STM32 随机数生成器（Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L597">已启用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P016_st_stm32-rng.md#std-dtcompatible-st-stm32-rng"><code>st,stm32-rng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>STM32 实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L343">已启用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P014_st_stm32-rtc.md#std-dtcompatible-st-stm32-rtc"><code>st,stm32-rtc</code></a></td>
</tr>
<tr>
<td rowspan="4">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>STM32 正交解码器（Quadrature Decoder）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L413">已禁用：2</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P028_st_stm32-qdec.md#std-dtcompatible-st-stm32-qdec"><code>st,stm32-qdec</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 系列温度节点（TEMP），用于以两个温度点完成生产校准的传感器。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L672">已启用：1</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P029_st_stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal"><code>st,stm32-temp-cal</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 参考电压（VREF+）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L683">已启用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P003_st_stm32-vref.md#std-dtcompatible-st-stm32-vref"><code>st,stm32-vref</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 电池电压（VBAT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L691">已启用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P001_st_stm32-vbat.md#std-dtcompatible-st-stm32-vbat"><code>st,stm32-vbat</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L310">已启用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P016_st_stm32-usart.md#std-dtcompatible-st-stm32-usart"><code>st,stm32-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低功耗通用异步收发器（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L382">已启用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P014_st_stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart"><code>st,stm32-lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">系统管理总线（SMbus）</td>
<td>片上（On-Chip）</td>
<td>STM32 系统管理总线控制器（SMBus Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L712">已禁用：2</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P013_st_stm32-smbus.md#std-dtcompatible-st-stm32-smbus"><code>st,stm32-smbus</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>带嵌入式接收和发送先进先出队列（Rx / Tx FIFOs）的STM32 SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L360">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L371">已禁用：1</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P009_st_stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo"><code>st,stm32-spi-fifo</code></a></td>
</tr>
<tr>
<td rowspan="3">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 定时器（Timers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L391">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L449">已禁用：2</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P008_st_stm32-timers.md#std-dtcompatible-st-stm32-timers"><code>st,stm32-timers</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低功耗定时器（LPTIM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L527">已启用：1</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P007_st_stm32-lptim.md#std-dtcompatible-st-stm32-lptim"><code>st,stm32-lptim</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>STM32 USB控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L573">已启用：1</a>）</td>
<td><a href="../usb_stm32_audio_binding_reference/P006_st_stm32-usb.md#std-dtcompatible-st-stm32-usb"><code>st,stm32-usb</code></a></td>
</tr>
<tr>
<td rowspan="2">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>STM32 系统窗口看门狗（System Window Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L302">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P002_st_stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog"><code>st,stm32-window-watchdog</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L521">已启用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P001_st_stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog"><code>st,stm32-watchdog</code></a></td>
</tr>
</table>

<a id="bluetooth-and-compatibility-with-stm32wb-copro-wireless-binaries"></a>

### 蓝牙及STM32WB协处理器无线固件兼容性（Copro Wireless Binaries）

在Nucleo WB55RG上运行蓝牙，Cortex-M0内核须烧录有效的STM32WB协处理器固件，可为完整协议栈（Full Stack）或HCI层（HCI Layer）。这些二进制文件随STM32WB Cube软件包提供，位于Projects/STM32WB_Copro_Wireless_Binaries/STM32WB5x/。

各二进制版本兼容性见[hal_stm32:lib/stm32wb/README.rst](https://github.com/zephyrproject-rtos/hal_stm32/blob/c9550199186236d610092f4005f8c9bae2a6bfcf/lib/stm32wb/README.rst)。

注意：从STM32WB Cube V1.13.2开始，Full Stack二进制文件不再与Zephyr兼容，M0侧只能使用HCI Only版本。

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

Nucleo WB55RG有6个通用输入输出（GPIO）控制器，负责引脚复用（Pin Muxing）、输入输出、上拉等功能。

<a id="default-zephyr-peripheral-mapping"></a>

#### Zephyr 默认外设映射（Peripheral Mapping）：


- UART_1 TX/RX : PB7/PB6
- LPUART_1 TX/RX：PA3/PA2（Arduino串口，arduino_serial）
- `I2C_1_SCL : PB8`
- `I2C_1_SDA : PB9`
- `I2C_3_SCL : PC0`
- I2C_3_SDA : PC1
- USER_PB : PC4
- USER_PB1 : PD0
- USER_PB2 : PD1
- LD1 : PB5
- LD2 : PB0
- LD3 : PB1
- SPI_1_NSS：PA4（Arduino SPI，arduino_spi）
- SPI_1_SCK：PA5（Arduino SPI，arduino_spi）
- SPI_1_MISO：PA6（Arduino SPI，arduino_spi）
- SPI_1_MOSI：PA7（Arduino SPI，arduino_spi）
- PWM_2 CH 1 : PA0
- ADC_1_CH3 : PC2

<a id="system-clock"></a>

#### 系统时钟（System Clock）

Nucleo WB55RG系统时钟可来自内部振荡器、外部振荡器或主PLL，默认由32 MHz高速外部时钟（HSE）驱动。

<a id="serial-port"></a>

#### 串口（Serial Port）

Nucleo WB55RG有2路(LP)U(S)ART，Zephyr控制台分配给USART1，默认参数115200、8N1。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`nucleo_wb55rg`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td></td>
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

Nucleo WB55RG开发板内置ST-LINK/V2-1调试工具接口。

nucleo_wb55rg的应用可按常规方式构建，详见“[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)”。

<a id="flashing"></a>

### 烧录（Flashing）

此板默认通过west的[STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html)运行器（Runner）烧录，因此需要安装该工具。（[installation](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#stm32cubeprog-flash-host-tools)）

也可使用OpenOCD或pyOCD，通过--runner或-r选项烧录开发板：

```text
$ west flash --runner openocd
$ west flash --runner pyocd
```

也可以使用pyOCD，但需要先使用以下pyOCD命令启用软件包（Pack）支持：

```text
$ pyocd pack --update
$ pyocd pack --install stm32wb55rg
```

<a id="flashing-an-application-to-nucleo-wb55rg"></a>

#### 向Nucleo WB55RG烧录应用（Flashing an Application）

通过USB将Nucleo WB55RG连接主机，然后构建并烧录应用。以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例。

运行主机串口程序，连接Nucleo开发板：

```text
$ minicom -D /dev/ttyUSB0
```

随后构建并烧录应用。

```text
# From the root of the zephyr repository
west build -b nucleo_wb55rg samples/hello_world
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
west build -b nucleo_wb55rg samples/basic/blinky
west debug
```

## 译注

自STM32WB Cube V1.13.2起，Zephyr只使用M0侧HCI Only固件，不能沿用Full Stack。原文802.15.5及M0名称差异已注明。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)：HTTP Error 567: Unknown Status。
- [p-nucleo-wb55.html](https://www.st.com/en/evaluation-tools/p-nucleo-wb55.html)：HTTP Error 567: Unknown Status。
- [stm32wb55rg.html](https://www.st.com/en/microcontrollers-microprocessors/stm32wb55rg.html)：HTTP Error 567: Unknown Status。
- [stm32wb55rg.pdf](https://www.st.com/resource/en/datasheet/stm32wb55rg.pdf)：HTTP Error 567: Unknown Status。
- [dm00318631.pdf](https://www.st.com/resource/en/reference_manual/dm00318631.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P074_Nucleo_WB09KE.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P076_Nucleo_WBA25CE1.md)
