---
id: learning.zephyr-docs.boards-st-discovery-eval.page-59
title: STM32WB5MMG
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/st/stm32wb5mmg/doc/stm32wb5mmg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="stm32wb5mmg"></a>

# 第59章\_STM32WB5MMG

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/st/stm32wb5mmg/doc/stm32wb5mmg.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/STM32WB5MMG.jpg](images/STM32WB5MMG.jpg)](images/STM32WB5MMG.jpg)

STM32WB5MMG

名称（Name）：

`stm32wb5mmg`

厂商（Vendor）：

[意法半导体（STMicroelectronics）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=st)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[stm32wb55xx](https://docs.zephyrproject.org/latest/boards/index.html#soc=stm32wb55xx)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32wb5mmg/doc/stm32wb5mmg.rst/../..)<a id="overview"></a>

## 概述（Overview）

STM32WB5MMG是超低功耗、小尺寸、经过认证的2.4 GHz无线模块，支持Bluetooth LE 5.4、Zigbee 3.0、OpenThread、动态及静态并发模式，以及802.15.4专有协议。添加此开发板支持，是为了让模块可在其他板上充当HCI层，特别是B-U585I-IOT02A开发板。

STM32WB5MMG支持以下功能：


- SiP-LGA86封装Bluetooth模块
- 集成芯片天线
- 通过Bluetooth LE 5.4、Zigbee 3.0及OpenThread认证，支持动态及静态并发模式
- IEEE 802.15.4-2011 MAC／PHY；原文同时写支持2 Mbit/s，照录
- 频段2402～2480 MHz
- 扩展广播（Advertising Extension）
- 发射输出功率最高+6 dBm
- 接收灵敏度：BLE 1 Mbit/s时−96 dBm，802.15.4时−100 dBm
- 传输距离最高75米
- 专用Arm Cortex-M0+ CPU，处理射频及安全任务
- 专用Arm Cortex-M4 CPU，带FPU及自适应实时加速器ART，最高64 MHz
- 1 Mbyte Flash及256 Kbyte SRAM
- 完整集成物料清单BOM，包括32 MHz射频晶体及32 kHz RTC晶体
- 集成开关电源SMPS
- 超低功耗模式有助于延长电池寿命
- 68个GPIO
- SWD及JTAG

更多信息见[STM32WB5MMG网站](https://www.st.com/en/microcontrollers-microprocessors/stm32wb5mmg.html)。

<a id="hardware"></a>

## 硬件（Hardware）

STM32WB5MMG是超低功耗、小尺寸、经过认证的2.4 GHz无线模块，支持Bluetooth LE 5.4、Zigbee 3.0、OpenThread、动态及静态并发模式，以及802.15.4专有协议。它基于STM32WB55VGY，凭借高接收灵敏度及发射功率提供出色射频性能，低功耗特性有利于延长电池寿命，适用于小型纽扣电池及能量采集。模块Y版基于STM32WB55VGY cut 2.1，X版基于cut 2.2。


- 带FlexPowerControl的超低功耗设计，保留RTC及32 KB RAM的待机模式低至600 nA
- 32位ARM Cortex-M4内核，带FPU，最高64 MHz
- 无线电（Radio）：


  - 2.4GHz
  - 射频收发器支持Bluetooth 5.4、IEEE 802.15.4-2011 PHY及MAC、Thread 1.3以及后续条目；原句在and处断开
  - Zigbee 3.0
  - 接收灵敏度：BLE 1 Mbit/s时−96 dBm，802.15.4时−100 dBm
  - 可编程输出功率最高+6 dBm，步进1 dB
  - 集成平衡不平衡转换器（Balun），减少物料清单（BOM）
  - 支持2 Mbit/s
  - 支持GATT缓存
  - 支持增强ATT（EATT）
  - 支持扩展广播（Advertising Extension）
  - 专用32位Arm Cortex-M0+，处理实时无线电层
  - 精确接收信号强度指示（RSSI），用于功率控制
  - 适用于需要符合ETSI EN 300 328、EN 300 440、FCC CFR47 Part 15及ARIB STD-T66无线电法规的系统
- 时钟源（Clock Sources）：


  - 32 MHz晶体振荡器，带集成微调电容，用于无线电及CPU时钟
  - 用于实时时钟（RTC）的32 kHz低速外部晶体振荡器（LSE）
  - 内部低功耗32 kHz RC振荡器LSI1，精度±5%
  - 内部低功耗32 kHz RC振荡器LSI2，稳定度±500 ppm
  - 内部多速率振荡器，100 kHz～48 MHz，由LSE自动校准，精度优于±0.25%
  - 内部高速16 MHz RC振荡器，出厂校准，精度±1%
  - 2个PLL，用于系统时钟、USB、SAI及ADC
- 2个DMA控制器，各7通道，支持ADC、SPI、I2C、USART、QSPI、SAI、AES及定时器
- 1路USART，支持ISO7816、IrDA、SPI主机、Modbus及智能卡模式
- 1路低功耗UART（LPUART）
- 2路SPI，最高32 Mbit/s
- 2路I2C，支持SMBus/PMBus
- 1路SAI，支持双通道高品质音频
- 1个无需晶体的USB 2.0全速设备接口，支持电池充电检测（BCD）及链路电源管理（LPM）
- 1个触摸感应控制器，最多18个传感器
- 1个8×40段LCD控制器，带升压转换器
- 1个16位四通道高级定时器
- 2个16位双通道定时器
- 1个32位四通道定时器
- 2个16位超低功耗定时器
- 1个独立SysTick
- 1个独立看门狗
- 1个窗口看门狗
- 最多72个高速I/O，其中70个耐受5 V
- 存储器（Memories）


  - 最多1 MB Flash，扇区具有防读写保护PCROP，可用于无线协议栈及应用
  - 最多256 KB SRAM，其中64 KB支持硬件奇偶校验
  - 20个32位备份寄存器
  - 启动加载器支持USART、SPI、I2C及USB接口
  - Bluetooth LE及802.15.4无线升级（OTA）
  - 支持就地执行XIP的Quad-SPI存储器接口
  - 1 Kbyte一次性可编程存储器OTP，即128个双字
- 四个用于Σ-Δ调制器（Sigma Delta Modulator）的数字滤波器（Digital Filters）
- 丰富的模拟外设，供电最低1.62 V
- 12位ADC，4.26 Msps，硬件过采样可达16位，功耗200 µA/Msps
- 2个超低功耗比较器
- 精密2.5 V或2.048 V参考电压缓冲输出
- 安全及标识（Security and ID）

> - Bluetooth LE及802.15.4软件协议栈的安全固件安装（SFI）
> - 3个最高256位AES硬件加密单元，用于应用及Bluetooth；原文句子在此分行
> - 低功耗Bluetooth LE及IEEE 802.15.4，承接上一条
> - 客户密钥存储／管理服务
> - 公钥硬件单元（PKA）；原文将全称写为public key authority
> - 密码算法：RSA、Diffie-Hellman及GF(p)上的椭圆曲线密码（ECC）；原文将Diffie-Hellman拼作Diffie-Helman。
> - 真随机数发生器（RNG）
> - 扇区读写操作保护（PCROP）
> - 循环冗余校验计算单元（CRC Calculation Unit）
> - 芯片信息：96位唯一标识ID
> - IEEE 64位唯一ID，可派生802.15.4的64位标识及Bluetooth LE的
> - 48位扩展唯一标识EUI，承接上一条

更多STM32WB5MMG信息见：


- [STM32WB5MMG网站](https://www.st.com/en/microcontrollers-microprocessors/stm32wb5mmg.html)
- [STM32WB5MMG数据手册](https://www.st.com/resource/en/datasheet/stm32wb5mmg.pdf)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`stm32wb5mmg`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="stm32wb5mmg-hw-features"></a>

<a id="stm32wb5mmg-stm32wb5mmg/stm32wb55xx-hw-features-section"></a>

#### `stm32wb5mmg/stm32wb55xx`目标（Target）

<a id="stm32wb5mmg-stm32wb5mmg/stm32wb55xx-hw-features-panel"></a>

<a id="stm32wb5mmg-stm32wb5mmg/stm32wb55xx-hw-features-memory"></a>

此目标可用存储：192 KiB RAM、876 KiB闪存。

<a id="stm32wb5mmg-stm32wb5mmg/stm32wb55xx-hw-features-table"></a>

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
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L84">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L92">已禁用：3</a>）</td>
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
<td>STM32 CRC 计算单元（Calculation Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L663">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P011_st_stm32-crc.md#std-dtcompatible-st-stm32-crc"><code>st,stm32-crc</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>STM32高级加密标准加速器（AES Accelerator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L605">已禁用：1</a>）</td>
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
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用输入输出控制器（GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L251">已启用：6</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P029_st_stm32-gpio.md#std-dtcompatible-st-stm32-gpio"><code>st,stm32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>STM32 I2C V2 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L319">已禁用：2</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P008_st_stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2"><code>st,stm32-i2c-v2</code></a></td>
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
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 电池备份 RAM（Battery-Backed RAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L353">已禁用：1</a>）</td>
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
<td>STM32 脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L402">已禁用：4</a>）</td>
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
<td>STM32 随机数生成器（Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L597">已禁用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P016_st_stm32-rng.md#std-dtcompatible-st-stm32-rng"><code>st,stm32-rng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>STM32 实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L343">已禁用：1</a>）</td>
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
<td>STM32 系列温度节点（TEMP），用于以两个温度点完成生产校准的传感器。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L672">已禁用：1</a>）</td>
<td><a href="../sensor_st_lsm_stm32_binding_reference/P029_st_stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal"><code>st,stm32-temp-cal</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 参考电压（VREF+）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L683">已禁用：1</a>）</td>
<td><a href="../sensor_st_ti_power_capacitance_binding_reference/P003_st_stm32-vref.md#std-dtcompatible-st-stm32-vref"><code>st,stm32-vref</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 电池电压（VBAT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L691">已禁用：1</a>）</td>
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
<td>带嵌入式接收和发送先进先出队列（Rx / Tx FIFOs）的STM32 SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L360">已禁用：2</a>）</td>
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
<td>STM32 定时器（Timers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L391">已禁用：4</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P008_st_stm32-timers.md#std-dtcompatible-st-stm32-timers"><code>st,stm32-timers</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32低功耗定时器（LPTIM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L527">已禁用：1</a>）</td>
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
<td>STM32 看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L521">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P001_st_stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog"><code>st,stm32-watchdog</code></a></td>
</tr>
</table>

<a id="bluetooth-and-compatibility-with-stm32wb-copro-wireless-binaries"></a>

### 蓝牙及STM32WB协处理器无线固件兼容性（Copro Wireless Binaries）

在STM32WB5MMG上使用Bluetooth时，应为Cortex-M0内核烧录有效的STM32WB协处理器二进制，可选择完整协议栈Full Stack或HCI层。文件位于STM32WB Cube软件包的Projects/STM32WB_Copro_Wireless_Binaries/STM32WB5x/。

各二进制版本兼容性见[hal_stm32:lib/stm32wb/README.rst](https://github.com/zephyrproject-rtos/hal_stm32/blob/c9550199186236d610092f4005f8c9bae2a6bfcf/lib/stm32wb/README.rst)。

注意：从STM32WB Cube V1.13.2开始，Full Stack二进制文件不再与Zephyr兼容，M0侧只能使用HCI Only版本。

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="default-zephyr-peripheral-mapping"></a>

#### Zephyr 默认外设映射（Peripheral Mapping）：


- UART_1 TX/RX : PB7/PB6
- LPUART_1 TX/RX : PA3/PA2
- USB : PA11/PA12
- SWD : PA13/PA14

<a id="system-clock"></a>

#### 系统时钟（System Clock）

STM32WB5MMG系统时钟可来自内部振荡器、外部振荡器或主PLL，默认使用32 MHz HSE时钟。

<a id="serial-port"></a>

#### 串口（Serial Port）

STM32WB5MMG有2路(LP)U(S)ART。LPUART1连接主U585I微控制器，用作HCI控制器端口；USART1未引出到外部引脚，不能据此直接调试模块。可在USB CN12上运行虚拟COM端口VCP USB协议栈，用于调试。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`stm32wb5mmg`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-stm32cubeprogrammer">stm32cubeprogrammer</a></td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

stm32wb5mmg应用可按常规方式构建，详见“构建应用”。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)）

<a id="flashing-the-module"></a>

### 烧录模块（Flashing the Module）

可使用b_u585i_iot02a板载ST-Link烧录STM32WB5MMG。将SW4置OFF、SW5置ON，此时固件会写入无线模块。

模块配置为使用west的[STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html)运行工具烧录，因此必须安装该程序。（[installation](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#stm32cubeprog-flash-host-tools)）

也可使用OpenOCD，通过--runner或-r选项烧录开发板：

```text
$ west flash --runner openocd
```

<a id="flashing-hci-uart-application-to-stm32wb5mmg"></a>

#### 向STM32WB5MMG烧录hci_uart应用

通过USB将B-U585I-IOT02A连接主机，将SW4 MCU SWD置OFF、SW5 SWD BLE置ON，再构建并烧录应用，下面以[HCI UART](../bluetooth_samples/P016_HCI_UART传输.md#bluetooth_hci_uart)为例。

运行主机串口程序连接B-U585I-IOT02A：

```text
$ minicom -D /dev/ttyACM0
```

然后为STM32WB5MMG模块构建并烧录应用。

```text
# From the root of the zephyr repository
west build -b stm32wb5mmg samples/bluetooth/hci_uart
west flash
```

接着将开关恢复默认：SW4置ON、SW5置OFF，使蓝牙示例写入主微控制器。随后为B-U585I-IOT02A构建[samples/bluetooth/observer](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/observer)蓝牙观察者示例：

```text
# From the root of the zephyr repository
west build -b b_u585i_iot02a samples/bluetooth/observer
west flash
```

复位开发板后，控制台应显示以下消息；原文Rest按上下文译为复位。

```text
Starting Observer Demo
Started scanning...
Exiting main thread.
Device found: R:2C:98:F3:64:58:06 (RSSI -82), type 3, AD data len 31
Device found: R:CE:5B:9A:87:69:4F (RSSI -80), type 3, AD data len 8
Device found: R:7B:1E:DD:38:23:E1 (RSSI -85), type 0, AD data len 17
```

<a id="debugging"></a>

### 调试（Debugging）

可按常规方式调试应用，下面以[HCI UART](../bluetooth_samples/P016_HCI_UART传输.md#bluetooth_hci_uart)为例。

```text
# From the root of the zephyr repository
west build -b b_u585i_iot02a samples/bluetooth/observer
west debug
```

## 译注

模块Y/X版分别基于芯片cut 2.1/2.2。B-U585I-IOT02A的SW4/SW5决定烧录主MCU还是无线模块；UART与USB调试条件分别保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)：HTTP Error 567: Unknown Status。
- [stm32wb5mmg.html](https://www.st.com/en/microcontrollers-microprocessors/stm32wb5mmg.html)：HTTP Error 567: Unknown Status。
- [stm32wb5mmg.pdf](https://www.st.com/resource/en/datasheet/stm32wb5mmg.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P058_STM32WB5MM-DK.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P060_STM32WBA65I_Discovery_kit.md)
