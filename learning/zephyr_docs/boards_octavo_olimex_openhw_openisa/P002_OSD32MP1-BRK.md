---
id: learning.zephyr-docs.boards-octavo-olimex-openhw-openisa.page-2
title: OSD32MP1-BRK
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/oct/osd32mp1_brk/doc/osd32mp1_brk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="osd32mp1_brk"></a>

# 第2章\_OSD32MP1-BRK

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/oct/osd32mp1_brk/doc/osd32mp1_brk.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/osd32mp1_brk.webp](images/osd32mp1_brk.webp)](images/osd32mp1_brk.webp)

OSD32MP1-BRK

名称（Name）：

`osd32mp1_brk`

厂商（Vendor）：

[Octavo Systems LLC](https://docs.zephyrproject.org/latest/boards/index.html#vendor=oct)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[osd32mp15x](https://docs.zephyrproject.org/latest/boards/index.html#soc=osd32mp15x)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/oct/osd32mp1_brk/doc/osd32mp1_brk.rst/../..)<a id="overview"></a>

## 概述（Overview）

Octavo Systems的OSD32MP1-BRK开发板集成OSD32MP15x系统级封装（SiP），其中包含多核STM32MP157F微处理器。Zephyr操作系统移植到STM32MP157F的Cortex-M4核运行。


- 通用功能（Common Features）：


  - OSD32MP15x系统级封装（SiP）：


    - STM32MP15x微处理器：


      - 双核32位Arm Cortex-A7，最高800 MHz
      - 32位Cortex-M4，最高209 MHz
      - 供Cortex-M4使用的448 KB嵌入式SRAM
    - 512 MB DDR3内存
    - STPMIC1A电源管理
    - 集成4 KB EEPROM
    - 微机电系统振荡器（MEMS Oscillator）
    - 超过100个无源元件
  - 小型外形（Small Form Factor）：


    - 尺寸：75 mm × 46 mm，约3英寸 × 1.8英寸
    - 兼容面包板，通过两个2×30、100 mil间距排针引出106个I/O
  - 内置功能（Built-in Features）：


    - Micro-USB
    - ST-Link排针
    - 通用异步收发器（UART）
    - MicroSD卡槽
    - 32 kHz晶体
    - 用户LED及复位按键
    - 4层PCB设计
    - 背面无元件

完整功能列表见[OSD32MP1-BRK产品页](https://octavosystems.com/octavo_products/osd32mp1-brk/)面。

<a id="hardware"></a>

## 硬件（Hardware）

OSD32MP15x SiP与STM32MP17 SoC集成后，提供以下硬件能力。此处SoC型号按原文保留。


- 处理器核（Core）：


  - 32 位双核 Arm Cortex-A7。


    - 每核一级缓存（L1）：32 KB 指令缓存（I）和 32 KB 数据缓存（D）。
    - 256 KB 统一二级缓存（Unified L2 Cache）。
    - Arm® NEON™及Arm® TrustZone®
  - 带浮点单元（FPU）与内存保护单元（MPU）的 32 位 Arm Cortex-M4。


    - 最高 209 MHz，最高 703 CoreMark。
- 存储器（Memories）：


  - SiP内集成512 MB DDR3L内存
  - 708 KB内部SRAM；总量按原文保留


    - 256 KB AXI SYSRAM
    - 384 KB AHB SRAM
    - 备份域（Backup Domain）内64 KB AHB SRAM
  - 双模式四线 SPI 存储器接口（Dual-Mode Quad-SPI）。
  - 灵活外部存储器控制器，数据总线最多 16 位。
  - SiP内集成4 KB EEPROM
- 信息安全／功能安全（Security/Safety）：


  - 安全启动（Secure Boot）、TrustZone外设及Cortex-M4资源隔离
- 时钟管理（Clock Management）：


  - 内部振荡器（Internal Oscillators）：


    - 64 MHz内部高速（HSI）振荡器
    - 4 MHz内部CSI振荡器
    - 32 kHz内部低速（LSI）振荡器
  - 外部振荡器（External Oscillators）：


    - 8—48 MHz高速外部振荡器（HSE）
    - 32.768 kHz低速外部振荡器（LSE）
  - 6 个支持小数模式（Fractional Mode）的 PLL。
  - SiP内集成MEMS振荡器
- 通用输入输出（GPIO）：


  - 最多 176 个支持中断的 I/O 端口。
  - 板上扩展排针引出106个I/O
- 互连矩阵（Interconnect Matrix）。
- 3 个 DMA 控制器。
- 通信外设（Communication Peripherals）：


  - 6 个 I2C FM+，速率 1 Mbit/s，支持 SMBus/PMBus。
  - 4 个 UART 和 4 个 USART，12.5 Mbit/s，支持 ISO7816 接口、LIN、IrDA 和 SPI 从机。
  - 6 个 SPI，50 Mbit/s，其中 3 个支持全双工 I2S 音频级精度。
  - 4 个串行音频接口（SAI），支持立体声音频 I2S、PDM、SPDIF 发送。
  - 带 4 路输入的 SPDIF 接收器（Rx）。
  - HDMI 消费电子控制接口（HDMI-CEC）。
  - 管理数据输入输出从接口（MDIO Slave Interface）。
  - 3 个 SDMMC，最多 8 位，支持 SD、eMMC、SDIO。
  - 2 个支持 CAN FD 协议和时间触发 CAN（TTCAN）的 CAN 控制器。
  - 2 个 USB 2.0 高速主机与 1 个 USB 2.0 全速 OTG 可同时工作。
  - 10/100 Mbit/s 或千兆以太网 GMAC，含 IEEE 1588v2 硬件，支持 MII/RMII/GMII/RGMI；最后一个接口名称沿用原文。
  - 8–14 位摄像头接口，最高 140 MB/s。
  - 6 个模拟外设（Analog Peripherals）。
  - 两个最高16位分辨率的ADC
  - 1 个温度传感器。
  - 2 个 12 位数模转换器（D/A Converters），1 MHz。
  - 1 个 Σ-Δ 调制器数字滤波器（DFSDM），含 8 个通道、6 个滤波器。
  - 内部或外部 ADC/DAC 参考电压 VREF+。
- 图形（Graphics）：


  - 三维图形处理器（3D GPU）：Vivante，支持 OpenGL ES 2.0。
  - LCD-TFT 控制器，最高 24 位并行 RGB888，最高 WXGA（1366×768）、60 fps。
  - MIPI DSI，2 条数据通道，每条最高 1 GHz。
- 定时器（Timers）：


  - 2 个 32 位定时器，最多 4 路输入捕获／输出比较／PWM（IC/OC/PWM），或脉冲计数及正交增量编码器输入。
  - 2 个 16 位高级电机控制定时器（Advanced Motor-Control Timers）。
  - 10 个 16 位通用定时器，其中 2 个为不支持 PWM 的基本定时器。
  - 5 个 16 位低功耗定时器（Low-Power Timers）。
  - 具有亚秒精度和硬件日历（Hardware Calendar）的 RTC。
  - 两组、每组 4 个 Cortex-A7 系统定时器：安全、非安全、虚拟和虚拟机监控器（Hypervisor）定时器。
  - 1 个 Cortex-M4 SysTick 定时器。
- 硬件加速（Hardware Acceleration）：


  - AES 128／192／256位及TDES
  - 散列（HASH）：MD5、SHA-1、SHA224、SHA256，以及 HMAC。
  - 2 个真随机数生成器（True Random Number Generators），各含 3 个振荡器。
  - 2 个 CRC 计算单元。
- 调试模式（Debug Mode）：


  - Arm CoreSight 跟踪与调试（Trace and Debug），支持 SWD 和 JTAG 接口。
  - 8 KB 嵌入式跟踪缓冲区（Embedded Trace Buffer）。
  - 3072 位熔丝（Fuses），包含 96 位唯一标识（Unique ID），最多 1184 位供用户使用。

硬件的更多信息见：


- [ST网站上的STM32MP157F](https://www.st.com/en/microcontrollers-microprocessors/stm32mp157f.html)
- [OSD32MP15x SiP文档](https://octavosystems.com/docs/osd32mp15x-datasheet/)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`osd32mp1_brk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="osd32mp1_brk-hw-features"></a>

<a id="osd32mp1_brk-osd32mp1_brk/osd32mp15x-hw-features-section"></a>

#### `osd32mp1_brk/osd32mp15x`目标（Target）

<a id="osd32mp1_brk-osd32mp1_brk/osd32mp15x-hw-features-panel"></a>

<a id="osd32mp1_brk-osd32mp1_brk/osd32mp15x-hw-features-memory"></a>

此开发板目标可用存储器：320 KiB RAM、64 KiB 闪存。

<a id="osd32mp1_brk-osd32mp1_brk/osd32mp15x-hw-features-table"></a>

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
<td>ARM Cortex-M4 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P024_arm_cortex-m4.md#std-dtcompatible-arm-cortex-m4"><code>arm,cortex-m4</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>STM32MP1 复位与时钟控制器（Reset and Clock Controller，RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../timer_reference/P181_STM32MP1复位与时钟控制绑定.md#dtbinding-st-stm32mp1-rcc"><code>st,stm32mp1-rcc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 外部高速时钟（HSE Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../timer_reference/P129_STM32高速外部时钟绑定.md#dtbinding-st-stm32-hse-clock"><code>st,stm32-hse-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>STM32 计数器（Counters）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L384">已禁用：2</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P007_st_stm32-counter.md#std-dtcompatible-st-stm32-counter"><code>st,stm32-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>STM32 CRC 计算单元（Calculation Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L431">已禁用：2</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P011_st_stm32-crc.md#std-dtcompatible-st-stm32-crc"><code>st,stm32-crc</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>STM32 LCD-TFT 显示控制器（Display Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L421">已禁用：1</a>）</td>
<td><a href="../display_st_ultrachip_zephyr_binding_reference/P004_st_stm32-ltdc.md#std-dtcompatible-st-stm32-ltdc"><code>st,stm32-ltdc</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>STM32 DMA 控制器（Controller，V1）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L194">已禁用：2</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P007_st_stm32-dma-v1.md#std-dtcompatible-st-stm32-dma-v1"><code>st,stm32-dma-v1</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 DMA 多路复用控制器（DMAMUX Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L216">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P011_st_stm32-dmamux.md#std-dtcompatible-st-stm32-dmamux"><code>st,stm32-dmamux</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用输入输出控制器（GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L97">已启用：11</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P029_st_stm32-gpio.md#std-dtcompatible-st-stm32-gpio"><code>st,stm32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>STM32 I2C V2 控制器（Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L356">已启用：1</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P008_st_stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2"><code>st,stm32-i2c-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/oct/osd32mp1_brk/osd32mp1_brk.dts?plain=1#L39">已启用：1</a>）</td>
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
<td>STM32G0 外部中断控制器（External Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L68">已启用：1</a>）</td>
<td><a href="../mcu_external_interrupt_binding_reference/P002_st_stm32g0-exti.md#std-dtcompatible-st-stm32g0-exti"><code>st,stm32g0-exti</code></a></td>
</tr>
<tr>
<td rowspan="1">处理器间消息（IPM）</td>
<td>片上（On-Chip）</td>
<td>STM32 处理器间通信控制器邮箱（IPCC Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L412">已启用：1</a>）</td>
<td><a href="../intercore_reference/P075_STM32处理器间通信控制器绑定.md#dtbinding-st-stm32-ipcc-mailbox"><code>st,stm32-ipcc-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/oct/osd32mp1_brk/osd32mp1_brk.dts?plain=1#L29">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>STM32 引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L90">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P004_st_stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl"><code>st,stm32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>STM32 脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L378">已禁用：2</a>）</td>
<td><a href="../pwm_stm32_ti_generic_binding_reference/P011_st_stm32-pwm.md#std-dtcompatible-st-stm32-pwm"><code>st,stm32-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 复位与时钟控制器（Reset and Clock Control，RCC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L61">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P017_st_stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl"><code>st,stm32-rcc-rctl</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>STM32 通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L293">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L302">已禁用：2</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P016_st_stm32-usart.md#std-dtcompatible-st-stm32-usart"><code>st,stm32-usart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L338">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L311">已禁用：3</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P015_st_stm32-uart.md#std-dtcompatible-st-stm32-uart"><code>st,stm32-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">系统管理总线（SMbus）</td>
<td>片上（On-Chip）</td>
<td>STM32 系统管理总线控制器（SMBus Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L448">已禁用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P013_st_stm32-smbus.md#std-dtcompatible-st-stm32-smbus"><code>st,stm32-smbus</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>STM32H7 串行外设接口控制器（SPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L267">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L228">已禁用：4</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P013_st_stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi"><code>st,stm32h7-spi</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>STM32 定时器（Timers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L368">已禁用：2</a>）</td>
<td><a href="../stm32_ti_silabs_timer_binding_reference/P008_st_stm32-timers.md#std-dtcompatible-st-stm32-timers"><code>st,stm32-timers</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>STM32 系统窗口看门狗（System Window Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp1/stm32mp157.dtsi?plain=1#L186">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P002_st_stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog"><code>st,stm32-window-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

OSD32MP1-BRK开发板原理图见：[OSD32MP1-BRK原理图](https://octavosystems.com/docs/osd32mp1-brk-schematics/)。

OSD32MP1-BRK开发板引脚映射见：[OSD32MP1-BRK默认引脚映射](https://octavosystems.com/octavosystems.com/wp-content/uploads/2020/05/Default-Pin-Mapping.pdf)。

<a id="default-zephyr-peripheral-mapping"></a>

#### Zephyr 默认外设映射（Peripheral Mapping）：


- UART7 TX／RX：PA15／PB3，默认控制台
- I2C5 SCL／SDA：PA11／PA12
- SPI4 SCK／MISO／MOSI：PE12／PE13／PE14

<a id="system-clock"></a>

#### 系统时钟（System Clock）

Cortex-M4 配置为 209 MHz，此值必须与配置的 `mlhclk_ck` 频率一致。

<a id="serial-port"></a>

#### 串口（Serial Port）

Zephyr默认将控制台输出写入RAM控制台，再由Cortex-A7上的Linux远程处理器框架（Remoteproc Framework）转储。若要启用USART2控制台，修改设备树及osd32mp1_brk_defconfig，或工程prj.conf。默认USART设置为115200、8N1。原文此处为USART2，上方引脚表为UART7。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`osd32mp1_brk`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd"><code>openocd</code></a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

原文说明STM32MP157F没有供Cortex-M4使用的QSPI闪存，M4必须由Cortex-A7启动。A7负责将M4应用二进制加载到RAM并解除M4复位，可在引导程序阶段或Linux启动后完成。

Cortex-M4可使用两种RAM。程序指针从0x00000000，即RETRAM开始，向量表应加载到此地址。下表给出Cortex-A7与Cortex-M4的内存映射：

<table>
<tr>
<th>区域（Region）</th>
<th>Cortex®-A7</th>
<th>Cortex®-M4</th>
<th>大小（Size）</th>
</tr>
<tr>
<td>保持RAM（RETRAM）</td>
<td>0x38000000-0x3800FFFF</td>
<td>0x00000000-0x0000FFFF</td>
<td>64KB</td>
</tr>
<tr>
<td>MCU静态随机存储器（MCUSRAM）</td>
<td>0x10000000-0x1005FFFF</td>
<td>0x10000000-0x1005FFFF</td>
<td>384KB</td>
</tr>
<tr>
<td>双倍数据率存储器（DDR）</td>
<td>0xC0000000-0x20000000</td>
<td></td>
<td>512MB</td>
</tr>
</table>

按以下步骤在Cortex-M4上启动Zephyr：


1. 下载并安装Octavo OpenSTLinux发行版：[OSD32MP1 OpenSTLinux](https://octavosystems.com/files/osd32mp1-brk-openstlinux-v3-0/)。

  过程详情见[OSD32MP1-BRK入门指南](https://octavosystems.com/app_notes/osd32mp1-brk-getting-started/)（Getting Started）。
2. 构建Zephyr应用：

  ```text
  # From the root of the zephyr repository
  west build -b osd32mp1_brk samples/hello_world
  ```
3. 通过USB远程网络驱动接口（RNDIS）将构建出的固件传输到开发板：

  ```text
  scp build/zephyr/zephyr.elf root@192.168.7.1:/lib/firmware
  ```
4. 在Cortex-M4上启动Zephyr：

  ```text
  ssh root@192.168.7.1
  echo stop > /sys/class/remoteproc/remoteproc0/state
  echo -n zephyr.elf > /sys/class/remoteproc/remoteproc0/firmware
  echo start > /sys/class/remoteproc/remoteproc0/state
  cat /sys/kernel/debug/remoteproc/remoteproc0/trace0
  ```

  控制台应显示：

  ```text
  *** Booting Zephyr OS build v4.0.0 ***
  Hello World! osd32mp1_brk/osd32mp15x
  ```

更详细说明见[OSD32MP1-BRK入门指南](https://octavosystems.com/app_notes/osd32mp1-brk-getting-started/)，以及STM32MP157启动Cortex-M4固件的Wiki页面。（[stm32mp157启动Cortex-M4固件（Boot Cortex-M4 Firmware）](https://wiki.st.com/stm32mpu/index.php/Linux_remoteproc_framework_overview#How_to_use_the_framework)）

<a id="debugging"></a>

### 调试（Debugging）

可使用OpenOCD及GDB调试应用。下述方法通过附加（Attach）到预加载固件进行调试，仅适用于Linux环境。必须先由Cortex-A7加载固件，再用OpenOCD将调试器附加到运行中的Zephyr。

基本方法是附加到Linux已经加载的固件。


- 构建示例：

  ```text
  # From the root of the zephyr repository
  west build -b osd32mp1_brk samples/hello_world
  ```
- 将固件复制到目标文件系统，加载并启动，参见STM32MP157启动Cortex-M4固件的说明。（[stm32mp157启动Cortex-M4固件（Boot Cortex-M4 Firmware）](https://wiki.st.com/stm32mpu/index.php/Linux_remoteproc_framework_overview#How_to_use_the_framework)）
- 附加到目标：

  ```text
  west attach
  ```

## 译注

OSD32MP1-BRK由A7加载并启动M4，调试流程附加到Linux已经加载的固件。原文STM32MP17名称、708 KB SRAM总量与256／384／64 KB分项之和、UART7引脚表与USART2控制台说明均分别保留；没有以其他型号资料替换。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [Linux_remoteproc_framework_overview](https://wiki.st.com/stm32mpu/index.php/Linux_remoteproc_framework_overview#How_to_use_the_framework)：The read operation timed out。
- [stm32mp157f.html](https://www.st.com/en/microcontrollers-microprocessors/stm32mp157f.html)：HTTP Error 567: Unknown Status。

---

[上一章](P001_Octavo.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_ESP32-P4-PC.md)
