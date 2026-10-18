---
id: learning.zephyr-docs.boards-nxp-imx-rt-multicore.page-8
title: MIMXRT700-EVK
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/mimxrt700_evk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mimxrt700_evk"></a>

# 第8章\_MIMXRT700-EVK

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/mimxrt700_evk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`mimxrt700_evk`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)、[xtensa](https://docs.zephyrproject.org/latest/boards/index.html#arch=xtensa)

片上系统（SoC）：

[mimxrt798s](https://docs.zephyrproject.org/latest/boards/index.html#soc=mimxrt798s)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt700_evk/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

i.MX RT700 CPU架构由高性能主计算子系统、次级常开感知计算子系统及专用协处理器组成。

主计算子系统包含325 MHz主Arm Cortex-M33及集成Cadence Tensilica HiFi 4 DSP，处理要求较高的DSP及音频任务。感知计算子系统包含第二个Cortex-M33及集成HiFi 1 DSP，从而无需外部传感器集线器，降低系统设计复杂度、占板面积及物料清单（BOM）成本。

HiFi 4是基于超长指令字（VLIW）架构的高性能DSP，每个指令周期最多执行8次32×16位乘加（MAC）。它可分担音频及图像处理等高性能数值任务，支持定点与浮点运算。

i.MX RT700还具有NXP eIQ Neutron神经网络处理单元（NPU），由eIQ机器学习软件开发环境支持。

<a id="hardware"></a>

## 硬件（Hardware）


- 主计算子系统（Main Compute Subsystem）：


  - Arm Cortex-M33，最高325 MHz
  - HiFi 4 DSP，最高325 MHz
  - eIQ Neutron NPU，最高325 MHz
- 感知计算子系统（Sense Compute Subsystem）


  - Arm Cortex-M33，最高250 MHz
  - HiFi 1 DSP，最高250 MHz
- 7.5 MB片上SRAM
- 3个xSPI接口用于片外存储器扩展，支持最高16位宽、250 MHz双倍数据速率（DDR）外部存储器
- 支持带集成PHY的嵌入式USB（eUSB）
- 两个SD／eMMC存储卡接口，其中一个支持eMMC 5.0的HS400／DDR运行
- 带片上PHY的USB高速主机／设备控制器
- 最多支持8通道的数字麦克风接口
- 串行外设：UART、I2C、I3C、SPI、HSPI及SAI
- 2.5D图形处理器（GPU），支持矢量图形加速及帧缓冲压缩
- 采用RISC-V核的EZH-V，具有额外SIMD及DSP指令
- 完整支持OpenVG 1.1
- 使用片上SRAM时最高支持720p、60帧／秒（FPS）
- LCD接口及MIPI DSI
- 集成JPEG及PNG支持
- 通过FlexIO提供8／10／16位并行摄像头接口（CSI）

MIMXRT798 SoC及MIMXRT700-EVK开发板的更多信息见以下资料：


- [i.MX RT700网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt700-crossover-mcu-with-arm-cortex-m33-npu-dsp-and-gpu-cores:i.MX-RT700)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

NXP将MIMXRT700-EVK视为i.MX RT7xx系列功能覆盖更广的开发板，并优先在此板落实Zephyr完整平台支持及新功能，以服务整个RT7xx系列。

`mimxrt700_evk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mimxrt700_evk-hw-features"></a>

<a id="mimxrt700_evk-mimxrt700_evk@mx25um51345g/mimxrt798s/cm33_cpu0-hw-features-section"></a>

#### `mimxrt700_evk@mx25um51345g/mimxrt798s/cm33_cpu0`目标（Target）

<a id="mimxrt700_evk-mimxrt700_evk@mx25um51345g/mimxrt798s/cm33_cpu0-hw-features-panel"></a>

<a id="mimxrt700_evk-mimxrt700_evk@mx25um51345g/mimxrt798s/cm33_cpu0-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、64 MiB Flash。

<a id="mimxrt700_evk-mimxrt700_evk@mx25um51345g/mimxrt798s/cm33_cpu0-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L107">已启用：1</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="2">音频（Audio）</td>
<td>板载（On-Board）</td>
<td>WM8962音频编解码器（Audio Codec）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L314">已启用：1</a>）</td>
<td><a href="../audio_stm32_ti_wolfson_binding_reference/P013_wolfson_wm8962.md#std-dtcompatible-wolfson-wm8962"><code>wolfson,wm8962</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP脉冲密度调制麦克风接口（PDM / MICFIL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1088">已启用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P014_nxp_micfil.md#std-dtcompatible-nxp-micfil"><code>nxp,micfil</code></a></td>
</tr>
<tr>
<td rowspan="1">充电器（Charger）</td>
<td>板载（On-Board）</td>
<td>NXP PCA9422电池充电器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L214">已启用：1</a>）</td>
<td><a href="../charger_binding_reference/P004_nxp_pca9422-charger.md#std-dtcompatible-nxp-pca9422-charger"><code>nxp,pca9422-charger</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L151">已启用：8</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟监测（Clock Monitor）</td>
<td>片上（On-Chip）</td>
<td>NXP频率测量（FREQME）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L174">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P004_nxp_freqme.md#std-dtcompatible-nxp-freqme"><code>nxp,freqme</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis模拟比较器（ACMP / Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1392">已启用：1</a>）</td>
<td><a href="../hardware/P745_NXPKinetis模拟比较器绑定.md#dtbinding-nxp-kinetis-acmp"><code>nxp,kinetis-acmp</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>通过计数器API提供的NXP IRTC唤醒定时器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L137">已禁用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P008_nxp_irtc-wake-timer.md#std-dtcompatible-nxp-irtc-wake-timer"><code>nxp,irtc-wake-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L257">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L269">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器（Multirate Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1233">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P015_nxp_mrt.md#std-dtcompatible-nxp-mrt"><code>nxp,mrt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1244">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1250">已禁用：3</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P014_nxp_mrt-channel.md#std-dtcompatible-nxp-mrt-channel"><code>nxp,mrt-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1441">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P006_nxp_crc.md#std-dtcompatible-nxp-crc"><code>nxp,crc</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L317">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L334">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>板载（On-Board）</td>
<td>NXP XSPI闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L401">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P019_nxp_xspi-nor.md#std-dtcompatible-nxp-xspi-nor"><code>nxp,xspi-nor</code></a></td>
</tr>
<tr>
<td rowspan="3">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Kinetis通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L366">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L418">已禁用：3</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P002_nxp_kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio"><code>nxp,kinetis-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ArduCam 20引脚排针式摄像头连接器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L110">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P021_arducam_dvp-20pin-connector.md#std-dtcompatible-arducam-dvp-20pin-connector"><code>arducam,dvp-20pin-connector</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP LCD 8080接口上引出的GPIO引脚，例如LCD-PAR-035面板使用的引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L144">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P003_nxp_lcd-8080.md#std-dtcompatible-nxp-lcd-8080"><code>nxp,lcd-8080</code></a></td>
</tr>
<tr>
<td rowspan="2">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP RSTCTL复位原因标志读取（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L138">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P013_nxp_rstctl-hwinfo.md#std-dtcompatible-nxp-rstctl-hwinfo"><code>nxp,rstctl-hwinfo</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP LPC 128位唯一标识符（Unique Identifier）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1426">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P009_nxp_lpc-uid.md#std-dtcompatible-nxp-lpc-uid"><code>nxp,lpc-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件自旋锁（Hardware Spinlock）</td>
<td>片上（On-Chip）</td>
<td>NXP SEMA42硬件信号量（Hardware Semaphore）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L203">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1431">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42"><code>nxp,sema42</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L586">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L502">已禁用：13</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1303">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1321">已禁用：2</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L60">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L46">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>用作Zephyr邮箱（MBOX）的NXP i.MX消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1069">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1059">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P047_NXPiMX消息单元邮箱绑定.md#dtbinding-nxp-mbox-imx-mu"><code>nxp,mbox-imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>板载（On-Board）</td>
<td>NXP XSPI PSRAM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L489">已启用：2</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P003_nxp_xspi-psram.md#std-dtcompatible-nxp-xspi-psram"><code>nxp,xspi-psram</code></a></td>
</tr>
<tr>
<td rowspan="2">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>低功耗Flexcomm（Low Power Flexcomm）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L470">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L512">已禁用：11</a>）</td>
<td><a href="../hardware/P702_NXP低功耗灵活通信接口绑定.md#dtbinding-nxp-lp-flexcomm"><code>nxp,lp-flexcomm</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP PCA9422电源管理芯片（PMIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L209">已启用：1</a>）</td>
<td><a href="../hardware/P689_PCA9422多功能设备绑定.md#dtbinding-nxp-pca9422"><code>nxp,pca9422</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示总线接口（MIPI-DBI）</td>
<td>片上（On-Chip）</td>
<td>NXP DCnano LCD控制器的显示总线接口（DBI）设置（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1367">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P004_nxp_mipi-dbi-dcnano-lcdif.md#std-dtcompatible-nxp-mipi-dbi-dcnano-lcdif"><code>nxp,mipi-dbi-dcnano-lcdif</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示串行接口（MIPI-DSI）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX MIPI DSI双通道显示串行接口（2L）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1378">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P014_nxp_mipi-dsi-2l.md#std-dtcompatible-nxp-mipi-dsi-2l"><code>nxp,mipi-dsi-2l</code></a></td>
</tr>
<tr>
<td rowspan="2">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1269">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX RTxxx DSP控制驱动，适用于i.MX RT700 HiFi 4 DSP（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P005_nxp_rt700-dsp-ctrl-hifi4.md#std-dtcompatible-nxp-rt700-dsp-ctrl-hifi4"><code>nxp,rt700-dsp-ctrl-hifi4</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>Macronix MX25UM51345G八线SPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L412">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P008_mxicy_mx25um51345g.md#std-dtcompatible-mxicy-mx25um51345g"><code>mxicy,mx25um51345g</code></a></td>
</tr>
<tr>
<td rowspan="1">多路复用器（MUX）</td>
<td>片上（On-Chip）</td>
<td>NXP输入复用器（INPUTMUX）外设绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L166">已启用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux"><code>nxp,inputmux</code></a></td>
</tr>
<tr>
<td rowspan="1">非易失存储器（NVMEM）</td>
<td>片上（On-Chip）</td>
<td>非易失存储器固定布局（Fixed Layout for Non-Volatile Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1406">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P009_fixed-layout.md#std-dtcompatible-fixed-layout"><code>fixed-layout</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>NXP RT7xx片上一次性可编程存储器（OCOTP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1401">已禁用：1</a>）</td>
<td><a href="../otp_binding_reference/P006_nxp_rt7xx-ocotp.md#std-dtcompatible-nxp-rt7xx-ocotp"><code>nxp,rt7xx-ocotp</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>LPC I/O引脚配置（IOCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L187">已启用：3</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P007_nxp_lpc-iocon.md#std-dtcompatible-nxp-lpc-iocon"><code>nxp,lpc-iocon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>RT600／RT500引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P018_nxp_rt-iocon-pinctrl.md#std-dtcompatible-nxp-rt-iocon-pinctrl"><code>nxp,rt-iocon-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>此电源域在进入及退出指定电源状态（Power State）时开启或关闭设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../power_domain_binding_reference/P007_power-domain-soc-state-change.md#std-dtcompatible-power-domain-soc-state-change"><code>power-domain-soc-state-change</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NXP状态可配置定时器（SCTimer）脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1357">已启用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P012_nxp_sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm"><code>nxp,sctimer-pwm</code></a></td>
</tr>
<tr>
<td rowspan="2">稳压器（Regulator）</td>
<td>板载（On-Board）</td>
<td>NXP PCA9422电源管理芯片（PMIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L225">已启用：1</a>）</td>
<td><a href="../hardware/P669_PCA9422稳压器绑定.md#dtbinding-nxp-pca9422-regulator"><code>nxp,pca9422-regulator</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>固定电压稳压器（Fixed Voltage Regulators）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L98">已启用：1</a>）</td>
<td><a href="../hardware/P635_固定稳压器设备树绑定.md#dtbinding-regulator-fixed"><code>regulator-fixed</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP RSTCTL外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L123">已启用：4</a>）</td>
<td><a href="../reset_controller_binding_reference/P011_nxp_rstctl.md#std-dtcompatible-nxp-rstctl"><code>nxp,rstctl</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>独立实时时钟（IRTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L128">已启用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P012_nxp_irtc.md#std-dtcompatible-nxp-irtc"><code>nxp,irtc</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1220">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1207">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P014_nxp_imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc"><code>nxp,imx-usdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>NXP PMC温度传感器（PMC-TMPSNS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1419">已禁用：1</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P011_nxp_pmc-tmpsns.md#std-dtcompatible-nxp-pmc-tmpsns"><code>nxp,pmc-tmpsns</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L483">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L525">已禁用：13</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1120">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L491">已禁用：15</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L58">已启用：6</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已禁用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX RT5xx／6xx上的NXP操作系统定时器（OS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1277">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P008_nxp_os-timer.md#std-dtcompatible-nxp-os-timer"><code>nxp,os-timer</code></a></td>
</tr>
<tr>
<td rowspan="3">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1159">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1180">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB主机控制器（Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1170">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1191">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P009_nxp_uhc-ehci.md#std-dtcompatible-nxp-uhc-ehci"><code>nxp,uhc-ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1201">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td rowspan="3">视频（Video）</td>
<td>板载（On-Board）</td>
<td>NXP FlexIO并行摄像头接口（DVP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L590">已禁用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P007_nxp_flexio-camera.md#std-dtcompatible-nxp-flexio-camera"><code>nxp,flexio-camera</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP JPEG解码器可解码JPEG／mJPEG压缩帧（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1449">已启用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P009_nxp_jpegdec.md#std-dtcompatible-nxp-jpegdec"><code>nxp,jpegdec</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP PNG解码器可解码PNG压缩帧（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1457">已启用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P011_nxp_pngdec.md#std-dtcompatible-nxp-pngdec"><code>nxp,pngdec</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>LPC窗口看门狗定时器（Windowed Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1285">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1294">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P011_nxp_lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt"><code>nxp,lpc-wwdt</code></a></td>
</tr>
<tr>
<td rowspan="1">唤醒控制器（Wakeup Controller）</td>
<td>片上（On-Chip）</td>
<td>用作唤醒控制器（WUC）的NXP睡眠控制器（SLEEPCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L158">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P007_nxp_sleepcon-wuc.md#std-dtcompatible-nxp-sleepcon-wuc"><code>nxp,sleepcon-wuc</code></a></td>
</tr>
<tr>
<td rowspan="1">扩展串行外设接口（xSPI）</td>
<td>片上（On-Chip）</td>
<td>NXP XSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L27">已启用：3</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P015_nxp_xspi.md#std-dtcompatible-nxp-xspi"><code>nxp,xspi</code></a></td>
</tr>
</table>

<a id="mimxrt700_evk-mimxrt700_evk@mx25um51345g/mimxrt798s/cm33_cpu1-hw-features-section"></a>

#### `mimxrt700_evk@mx25um51345g/mimxrt798s/cm33_cpu1`目标（Target）

<a id="mimxrt700_evk-mimxrt700_evk@mx25um51345g/mimxrt798s/cm33_cpu1-hw-features-panel"></a>

<a id="mimxrt700_evk-mimxrt700_evk@mx25um51345g/mimxrt798s/cm33_cpu1-hw-features-memory"></a>

该开发板目标的片上存储容量：256 KiB RAM、512 KiB Flash。

<a id="mimxrt700_evk-mimxrt700_evk@mx25um51345g/mimxrt798s/cm33_cpu1-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L14">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L107">已启用：1</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L151">已启用：8</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis模拟比较器（ACMP / Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L404">已启用：1</a>）</td>
<td><a href="../hardware/P745_NXPKinetis模拟比较器绑定.md#dtbinding-nxp-kinetis-acmp"><code>nxp,kinetis-acmp</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L88">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L100">已禁用：2</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Kinetis通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L156">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L169">已禁用：2</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P002_nxp_kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio"><code>nxp,kinetis-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP RSTCTL复位原因标志读取（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L138">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P013_nxp_rstctl-hwinfo.md#std-dtcompatible-nxp-rstctl-hwinfo"><code>nxp,rstctl-hwinfo</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件自旋锁（Hardware Spinlock）</td>
<td>片上（On-Chip）</td>
<td>NXP SEMA42硬件信号量（Hardware Semaphore）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L203">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L413">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42"><code>nxp,sema42</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L225">已禁用：5</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L143">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L130">已禁用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu1.dts?plain=1#L48">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu1.dts?plain=1#L38">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>用作Zephyr邮箱（MBOX）的NXP i.MX消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L356">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L366">已禁用：2</a>）</td>
<td><a href="../intercore_reference/P047_NXPiMX消息单元邮箱绑定.md#dtbinding-nxp-mbox-imx-mu"><code>nxp,mbox-imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>板载（On-Board）</td>
<td>NXP XSPI PSRAM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu1.dts?plain=1#L133">已启用：1</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P003_nxp_xspi-psram.md#std-dtcompatible-nxp-xspi-psram"><code>nxp,xspi-psram</code></a></td>
</tr>
<tr>
<td rowspan="1">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>低功耗Flexcomm（Low Power Flexcomm）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L275">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L195">已禁用：3</a>）</td>
<td><a href="../hardware/P702_NXP低功耗灵活通信接口绑定.md#dtbinding-nxp-lp-flexcomm"><code>nxp,lp-flexcomm</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>LPC I/O引脚配置（IOCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L187">已启用：2</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P007_nxp_lpc-iocon.md#std-dtcompatible-nxp-lpc-iocon"><code>nxp,lpc-iocon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>RT600／RT500引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P018_nxp_rt-iocon-pinctrl.md#std-dtcompatible-nxp-rt-iocon-pinctrl"><code>nxp,rt-iocon-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP RSTCTL外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L123">已启用：4</a>）</td>
<td><a href="../reset_controller_binding_reference/P011_nxp_rstctl.md#std-dtcompatible-nxp-rstctl"><code>nxp,rstctl</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>独立实时时钟（IRTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L62">已启用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P012_nxp_irtc.md#std-dtcompatible-nxp-irtc"><code>nxp,irtc</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>连接I3C总线的NXP P3T1755数字温度传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu1.dts?plain=1#L103">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P053_nxp_p3t1755.md#std-dtcompatible-nxp-p3t1755"><code>nxp,p3t1755</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L287">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L207">已禁用：3</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L214">已禁用：4</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L58">已启用：6</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已禁用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX RT5xx／6xx上的NXP操作系统定时器（OS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L397">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P008_nxp_os-timer.md#std-dtcompatible-nxp-os-timer"><code>nxp,os-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">唤醒控制器（Wakeup Controller）</td>
<td>片上（On-Chip）</td>
<td>用作唤醒控制器（WUC）的NXP睡眠控制器（SLEEPCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L80">已禁用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P007_nxp_sleepcon-wuc.md#std-dtcompatible-nxp-sleepcon-wuc"><code>nxp,sleepcon-wuc</code></a></td>
</tr>
<tr>
<td rowspan="1">扩展串行外设接口（xSPI）</td>
<td>片上（On-Chip）</td>
<td>NXP XSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P015_nxp_xspi.md#std-dtcompatible-nxp-xspi"><code>nxp,xspi</code></a></td>
</tr>
</table>

<a id="mimxrt700_evk-mimxrt700_evk@w25q512nw/mimxrt798s/cm33_cpu0-hw-features-section"></a>

#### `mimxrt700_evk@w25q512nw/mimxrt798s/cm33_cpu0`目标（Target）

<a id="mimxrt700_evk-mimxrt700_evk@w25q512nw/mimxrt798s/cm33_cpu0-hw-features-panel"></a>

<a id="mimxrt700_evk-mimxrt700_evk@w25q512nw/mimxrt798s/cm33_cpu0-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、64 MiB Flash。

<a id="mimxrt700_evk-mimxrt700_evk@w25q512nw/mimxrt798s/cm33_cpu0-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L107">已启用：1</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="2">音频（Audio）</td>
<td>板载（On-Board）</td>
<td>WM8962音频编解码器（Audio Codec）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L314">已启用：1</a>）</td>
<td><a href="../audio_stm32_ti_wolfson_binding_reference/P013_wolfson_wm8962.md#std-dtcompatible-wolfson-wm8962"><code>wolfson,wm8962</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP脉冲密度调制麦克风接口（PDM / MICFIL）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1088">已启用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P014_nxp_micfil.md#std-dtcompatible-nxp-micfil"><code>nxp,micfil</code></a></td>
</tr>
<tr>
<td rowspan="1">充电器（Charger）</td>
<td>板载（On-Board）</td>
<td>NXP PCA9422电池充电器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L214">已启用：1</a>）</td>
<td><a href="../charger_binding_reference/P004_nxp_pca9422-charger.md#std-dtcompatible-nxp-pca9422-charger"><code>nxp,pca9422-charger</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L151">已启用：8</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟监测（Clock Monitor）</td>
<td>片上（On-Chip）</td>
<td>NXP频率测量（FREQME）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L174">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P004_nxp_freqme.md#std-dtcompatible-nxp-freqme"><code>nxp,freqme</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis模拟比较器（ACMP / Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1392">已启用：1</a>）</td>
<td><a href="../hardware/P745_NXPKinetis模拟比较器绑定.md#dtbinding-nxp-kinetis-acmp"><code>nxp,kinetis-acmp</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>通过计数器API提供的NXP IRTC唤醒定时器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L137">已禁用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P008_nxp_irtc-wake-timer.md#std-dtcompatible-nxp-irtc-wake-timer"><code>nxp,irtc-wake-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L257">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L269">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器（Multirate Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1233">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P015_nxp_mrt.md#std-dtcompatible-nxp-mrt"><code>nxp,mrt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1244">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1250">已禁用：3</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P014_nxp_mrt-channel.md#std-dtcompatible-nxp-mrt-channel"><code>nxp,mrt-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1441">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P006_nxp_crc.md#std-dtcompatible-nxp-crc"><code>nxp,crc</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX增强型DMA（EDMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L317">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L334">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P004_nxp_mcux-edma.md#std-dtcompatible-nxp-mcux-edma"><code>nxp,mcux-edma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>板载（On-Board）</td>
<td>NXP XSPI闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L401">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P019_nxp_xspi-nor.md#std-dtcompatible-nxp-xspi-nor"><code>nxp,xspi-nor</code></a></td>
</tr>
<tr>
<td rowspan="3">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Kinetis通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L366">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L418">已禁用：3</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P002_nxp_kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio"><code>nxp,kinetis-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ArduCam 20引脚排针式摄像头连接器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L110">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P021_arducam_dvp-20pin-connector.md#std-dtcompatible-arducam-dvp-20pin-connector"><code>arducam,dvp-20pin-connector</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP LCD 8080接口上引出的GPIO引脚，例如LCD-PAR-035面板使用的引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L144">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P003_nxp_lcd-8080.md#std-dtcompatible-nxp-lcd-8080"><code>nxp,lcd-8080</code></a></td>
</tr>
<tr>
<td rowspan="2">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP RSTCTL复位原因标志读取（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L138">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P013_nxp_rstctl-hwinfo.md#std-dtcompatible-nxp-rstctl-hwinfo"><code>nxp,rstctl-hwinfo</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP LPC 128位唯一标识符（Unique Identifier）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1426">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P009_nxp_lpc-uid.md#std-dtcompatible-nxp-lpc-uid"><code>nxp,lpc-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件自旋锁（Hardware Spinlock）</td>
<td>片上（On-Chip）</td>
<td>NXP SEMA42硬件信号量（Hardware Semaphore）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L203">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1431">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42"><code>nxp,sema42</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗I2C（LPI2C）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L586">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L502">已禁用：13</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P005_nxp_lpi2c.md#std-dtcompatible-nxp-lpi2c"><code>nxp,lpi2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX串行音频接口（SAI）I2S控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1303">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1321">已禁用：2</a>）</td>
<td><a href="../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s"><code>nxp,mcux-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L60">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L46">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>用作Zephyr邮箱（MBOX）的NXP i.MX消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1069">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1059">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P047_NXPiMX消息单元邮箱绑定.md#dtbinding-nxp-mbox-imx-mu"><code>nxp,mbox-imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储器控制器（Memory Controller）</td>
<td>板载（On-Board）</td>
<td>NXP XSPI PSRAM控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L489">已启用：2</a>）</td>
<td><a href="../memory_controller_sdram_psram_binding_reference/P003_nxp_xspi-psram.md#std-dtcompatible-nxp-xspi-psram"><code>nxp,xspi-psram</code></a></td>
</tr>
<tr>
<td rowspan="2">多功能设备（Multi-Function Device）</td>
<td>片上（On-Chip）</td>
<td>低功耗Flexcomm（Low Power Flexcomm）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L470">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L512">已禁用：11</a>）</td>
<td><a href="../hardware/P702_NXP低功耗灵活通信接口绑定.md#dtbinding-nxp-lp-flexcomm"><code>nxp,lp-flexcomm</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>NXP PCA9422电源管理芯片（PMIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L209">已启用：1</a>）</td>
<td><a href="../hardware/P689_PCA9422多功能设备绑定.md#dtbinding-nxp-pca9422"><code>nxp,pca9422</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示总线接口（MIPI-DBI）</td>
<td>片上（On-Chip）</td>
<td>NXP DCnano LCD控制器的显示总线接口（DBI）设置（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1367">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P004_nxp_mipi-dbi-dcnano-lcdif.md#std-dtcompatible-nxp-mipi-dbi-dcnano-lcdif"><code>nxp,mipi-dbi-dcnano-lcdif</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示串行接口（MIPI-DSI）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX MIPI DSI双通道显示串行接口（2L）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1378">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P014_nxp_mipi-dsi-2l.md#std-dtcompatible-nxp-mipi-dsi-2l"><code>nxp,mipi-dsi-2l</code></a></td>
</tr>
<tr>
<td rowspan="2">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexIO控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1269">已启用：1</a>）</td>
<td><a href="../misc_adi_nordic_binding_reference/P024_nxp_flexio.md#std-dtcompatible-nxp-flexio"><code>nxp,flexio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP i.MX RTxxx DSP控制驱动，适用于i.MX RT700 HiFi 4 DSP（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P005_nxp_rt700-dsp-ctrl-hifi4.md#std-dtcompatible-nxp-rt700-dsp-ctrl-hifi4"><code>nxp,rt700-dsp-ctrl-hifi4</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>Winbond W25Q512NW四线SPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L412">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P021_winbond_w25q512nw.md#std-dtcompatible-winbond-w25q512nw"><code>winbond,w25q512nw</code></a></td>
</tr>
<tr>
<td rowspan="1">多路复用器（MUX）</td>
<td>片上（On-Chip）</td>
<td>NXP输入复用器（INPUTMUX）外设绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L166">已启用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux"><code>nxp,inputmux</code></a></td>
</tr>
<tr>
<td rowspan="1">非易失存储器（NVMEM）</td>
<td>片上（On-Chip）</td>
<td>非易失存储器固定布局（Fixed Layout for Non-Volatile Memory）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1406">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P009_fixed-layout.md#std-dtcompatible-fixed-layout"><code>fixed-layout</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>NXP RT7xx片上一次性可编程存储器（OCOTP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1401">已禁用：1</a>）</td>
<td><a href="../otp_binding_reference/P006_nxp_rt7xx-ocotp.md#std-dtcompatible-nxp-rt7xx-ocotp"><code>nxp,rt7xx-ocotp</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>LPC I/O引脚配置（IOCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L187">已启用：3</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P007_nxp_lpc-iocon.md#std-dtcompatible-nxp-lpc-iocon"><code>nxp,lpc-iocon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>RT600／RT500引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P018_nxp_rt-iocon-pinctrl.md#std-dtcompatible-nxp-rt-iocon-pinctrl"><code>nxp,rt-iocon-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>片上（On-Chip）</td>
<td>此电源域在进入及退出指定电源状态（Power State）时开启或关闭设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../power_domain_binding_reference/P007_power-domain-soc-state-change.md#std-dtcompatible-power-domain-soc-state-change"><code>power-domain-soc-state-change</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NXP状态可配置定时器（SCTimer）脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1357">已启用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P012_nxp_sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm"><code>nxp,sctimer-pwm</code></a></td>
</tr>
<tr>
<td rowspan="2">稳压器（Regulator）</td>
<td>板载（On-Board）</td>
<td>NXP PCA9422电源管理芯片（PMIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L225">已启用：1</a>）</td>
<td><a href="../hardware/P669_PCA9422稳压器绑定.md#dtbinding-nxp-pca9422-regulator"><code>nxp,pca9422-regulator</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>固定电压稳压器（Fixed Voltage Regulators）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L98">已启用：1</a>）</td>
<td><a href="../hardware/P635_固定稳压器设备树绑定.md#dtbinding-regulator-fixed"><code>regulator-fixed</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP RSTCTL外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L123">已启用：4</a>）</td>
<td><a href="../reset_controller_binding_reference/P011_nxp_rstctl.md#std-dtcompatible-nxp-rstctl"><code>nxp,rstctl</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>独立实时时钟（IRTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L128">已启用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P012_nxp_irtc.md#std-dtcompatible-nxp-irtc"><code>nxp,irtc</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1220">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1207">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P014_nxp_imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc"><code>nxp,imx-usdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>NXP PMC温度传感器（PMC-TMPSNS）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1419">已禁用：1</a>）</td>
<td><a href="../sensor_nxp_qdec_optical_binding_reference/P011_nxp_pmc-tmpsns.md#std-dtcompatible-nxp-pmc-tmpsns"><code>nxp,pmc-tmpsns</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗UART（LPUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L483">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L525">已禁用：13</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P017_nxp_lpuart.md#std-dtcompatible-nxp-lpuart"><code>nxp,lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP低功耗SPI（LPSPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1120">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L491">已禁用：15</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P004_nxp_lpspi.md#std-dtcompatible-nxp-lpspi"><code>nxp,lpspi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L58">已启用：6</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已禁用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>i.MX RT5xx／6xx上的NXP操作系统定时器（OS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1277">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P008_nxp_os-timer.md#std-dtcompatible-nxp-os-timer"><code>nxp,os-timer</code></a></td>
</tr>
<tr>
<td rowspan="3">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB设备模式（Device Mode）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1159">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1180">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P006_nxp_ehci.md#std-dtcompatible-nxp-ehci"><code>nxp,ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP EHCI USB主机控制器（Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1170">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1191">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P009_nxp_uhc-ehci.md#std-dtcompatible-nxp-uhc-ehci"><code>nxp,uhc-ehci</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1201">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td rowspan="3">视频（Video）</td>
<td>板载（On-Board）</td>
<td>NXP FlexIO并行摄像头接口（DVP）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L590">已禁用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P007_nxp_flexio-camera.md#std-dtcompatible-nxp-flexio-camera"><code>nxp,flexio-camera</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP JPEG解码器可解码JPEG／mJPEG压缩帧（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1449">已启用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P009_nxp_jpegdec.md#std-dtcompatible-nxp-jpegdec"><code>nxp,jpegdec</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP PNG解码器可解码PNG压缩帧（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1457">已启用：1</a>）</td>
<td><a href="../video_camera_endpoint_binding_reference/P011_nxp_pngdec.md#std-dtcompatible-nxp-pngdec"><code>nxp,pngdec</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>LPC窗口看门狗定时器（Windowed Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1285">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1294">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P011_nxp_lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt"><code>nxp,lpc-wwdt</code></a></td>
</tr>
<tr>
<td rowspan="1">唤醒控制器（Wakeup Controller）</td>
<td>片上（On-Chip）</td>
<td>用作唤醒控制器（WUC）的NXP睡眠控制器（SLEEPCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L158">已启用：1</a>）</td>
<td><a href="../power_state_wakeup_binding_reference/P007_nxp_sleepcon-wuc.md#std-dtcompatible-nxp-sleepcon-wuc"><code>nxp,sleepcon-wuc</code></a></td>
</tr>
<tr>
<td rowspan="1">扩展串行外设接口（xSPI）</td>
<td>片上（On-Chip）</td>
<td>NXP XSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt7xx/nxp_rt7xx_common.dtsi?plain=1#L27">已启用：3</a>）</td>
<td><a href="../qspi_ospi_xspi_binding_reference/P015_nxp_xspi.md#std-dtcompatible-nxp-xspi"><code>nxp,xspi</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

MIMXRT798 SoC提供IOCON寄存器，用于配置引脚功能。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PIO0_6</td>
<td>集成电路间总线（I2C）</td>
<td>I2C串行数据（SDA）</td>
</tr>
<tr>
<td>PIO0_7</td>
<td>集成电路间总线（I2C）</td>
<td>I2C串行时钟（SCL）</td>
</tr>
<tr>
<td>PIO0_31</td>
<td>UART0</td>
<td>UART接收（RX）</td>
</tr>
<tr>
<td>PIO1_0</td>
<td>UART0</td>
<td>UART发送（TX）</td>
</tr>
<tr>
<td>PIO0_18</td>
<td>通用输入输出（GPIO）</td>
<td>绿色LED（GREEN LED）</td>
</tr>
<tr>
<td>PIO0_9</td>
<td>通用输入输出（GPIO）</td>
<td>SW5</td>
</tr>
<tr>
<td>PIO8_14</td>
<td>UART19</td>
<td>UART发送（TX）</td>
</tr>
<tr>
<td>PIO8_15</td>
<td>UART19</td>
<td>UART接收（RX）</td>
</tr>
<tr>
<td>PIO3_0</td>
<td>串行外设接口（SPI）</td>
<td>SPI主机输出从机输入（MOSI）</td>
</tr>
<tr>
<td>PIO3_1</td>
<td>串行外设接口（SPI）</td>
<td>SPI串行时钟（SCK）</td>
</tr>
<tr>
<td>PIO3_2</td>
<td>串行外设接口（SPI）</td>
<td>SPI主机输入从机输出（MISO）</td>
</tr>
<tr>
<td>PIO3_3</td>
<td>串行外设接口（SPI）</td>
<td>SPI从设备选择（SSEL）</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

MIMXRT700 EVK配置为使用SysTick作为系统时钟源。

<a id="hifi1-dsp-core"></a>

### HiFi 1 DSP核

以HiFi 1 SoC为目标可为i.MX RT700 HiFi 1 DSP构建Zephyr应用。Zephyr SDK包含支持RT700 DSP核的Xtensa工具链。

为i.MX RT700 HiFi 1 DSP构建Hello World示例：

```text
# From the root of the zephyr repository
west build -b mimxrt700_evk/mimxrt798s/hifi1 samples/hello_world
```

<a id="hifi4-dsp-core"></a>

### HiFi 4 DSP核

以HiFi 4 SoC为目标可为i.MX RT700 HiFi 4 DSP构建Zephyr应用。Zephyr SDK包含支持RT700 DSP核的Xtensa工具链。

为i.MX RT700 HiFi 4 DSP构建Hello World示例：

```text
# From the root of the zephyr repository
west build -b mimxrt700_evk/mimxrt798s/hifi4 samples/hello_world
```

<a id="multicore-core-operation"></a>

## 多核运行（Multicore Operation）

MIMXRT700-EVK支持Cortex-M33 CPU0、Cortex-M33 CPU1、HiFi 1及HiFi 4全部内核参与多核运行。CM33 CPU0默认是启动核，负责初始化系统并启动CM33 CPU1和／或HiFi 4；CM33 CPU1负责启动HiFi 1。

通常由负责引导次级核的内核，将次级核固件／镜像复制到指定存储位置，再解除其复位。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`mimxrt700_evk`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
</table>

按通常方式构建并烧录应用，详见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）与“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

<a id="configuring-a-debug-probe"></a>

### 配置调试探针（Configuring a Debug Probe）

烧录和调试均使用调试探针，默认配置为MCU-Link CMSIS-DAP板载调试探针。

<a id="tab-0-TGlua1NlcnZlcg=="></a>

<a id="tab-0-SkxpbmsgRXh0ZXJuYWw="></a>

<a id="panel-0-TGlua1NlcnZlcg=="></a>

**LinkServer**


1. 安装LinkServer调试主机工具，并确保位于搜索路径中。（[LinkServer调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#linkserver-debug-host-tools)）
2. 短接J20使开发板进入DFU模式，以写入固件。
3. 调试固件更新步骤见“MIMXRT700-EVK调试固件”。

<a id="panel-0-SkxpbmsgRXh0ZXJuYWw="></a>

**外部J-Link**


1. 安装J-Link调试主机工具（Debug Host Tools），并确保工具位于搜索路径中。（[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)）
2. 短接JP18，从板载调试电路断开SWD信号。
3. 将J-Link探针连接到J18的20引脚排针。

更多信息见“外部J-Link调试探针”（[J-Link External Debug Probe](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#jlink-external-debug-probe)）。

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

用USB线缆将PC连接J54，在所选串口终端（如minicom、PuTTY）中使用以下设置：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

### 烧录（Flashing）

SW10拨码选择启动方式。设为Off-On，即01，从XSPI0上的默认外部闪存启动。

以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例，默认使用[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)。

```text
# From the root of the zephyr repository
west build -b mimxrt700_evk/mimxrt798s/cm33_cpu0 samples/hello_world
west flash
```

打开串口终端，复位开发板（按下RESET按键），应能在终端中看到以下消息：

```text
*** Booting Zephyr OS v3.7.0 ***
Hello World! mimxrt700_evk/mimxrt798s/cm33_cpu0
```

<a id="debugging"></a>

### 调试（Debugging）

以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例，默认使用[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)。

```text
# From the root of the zephyr repository
west build -b mimxrt700_evk/mimxrt798s/cm33_cpu0 samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
*** Booting Zephyr OS v3.7.0 ***
Hello World! mimxrt700_evk/mimxrt798s/cm33_cpu0
```

<a id="segger-rtt-logging"></a>

### SEGGER实时传输日志（RTT Logging）

CM33 CPU0默认对SRAM启用数据缓存（D-Cache）。若把RTT缓冲区直接放在普通.bss中，CPU写入可能只停留在缓存，未到达J-Link读取的物理SRAM，使调试器看不到数据。启用[CONFIG_USE_SEGGER_RTT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_SEGGER_RTT)时，SoC层会自动将SEGGER RTT控制块及缓冲区放入Zephyr非缓存（nocache）区域，无需另设缓冲区放置Kconfig或DTS覆盖文件。

通过RTT输出日志只需启用相应日志后端：

```text
CONFIG_USE_SEGGER_RTT=y
CONFIG_LOG_BACKEND_RTT=y
```

使用JLinkRTTViewer或JLinkRTTLogger连接时，把RTT Control Block选项设为Address，不能使用Auto Detection，并输入构建生成的链接器映射文件中_SEGGER_RTT的地址：

```text
$ grep " _SEGGER_RTT$" build/zephyr/zephyr.map
                0x30180260                _SEGGER_RTT
```

板卡defconfig启用了[CONFIG_TRUSTED_EXECUTION_SECURE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRUSTED_EXECUTION_SECURE)，因此该地址位于安全SRAM别名范围0x30xxxxxx。J-Link默认RTT自动搜索仅覆盖非安全别名0x20xxxxxx，无法找到控制块。

<a id="sd-card-support"></a>

## SD卡支持

MIMXRT700-EVK的USDHC1通过TMUX136电子开关，在SD卡槽J47与M.2连接器J44之间共享。JP65用于选择有效接口：


- JP65短接1—2：将SDIO信号路由到SD卡槽J47，使用SD卡时采用此位置。
- JP65短接2—3，默认：将SDIO信号路由到M.2连接器J44。

使用SD卡时，确保JP65设为1—2。

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)
- [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)
- [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- NXP Zephyr主页，包含培训资源（[NXP的Zephyr专题页面](https://nxp.com/zephyr)）
- [NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

<a id="display-support"></a>

## 显示支持（Display Support）

mimxrt700_evk支持以下源码树内显示模块，各模块的设置如下。注意，板上显示控制器不能在启用数据缓存时工作。

<a id="nxp-g1120b0mipi-mipi-display"></a>

### NXP G1120B0MIPI MIPI显示屏

NXP G1120B0MIPI直接连接板上MIPI连接器J52，但需要一些修改，列表见[boards/shields/g1120b0mipi/boards/mimxrt700_evk_mimxrt798s_cm33_cpu0.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/g1120b0mipi/boards/mimxrt700_evk_mimxrt798s_cm33_cpu0.overlay)。可按以下方式构建显示示例：（[NXP G1120B0MIPI MIPI显示屏](https://docs.zephyrproject.org/latest/boards/shields/g1120b0mipi/doc/index.html#g1120b0mipi)）

```text
west build -b mimxrt700_evk/mimxrt798s/cm33_cpu0 --shield g1120b0mipi samples/drivers/display
```

<a id="nxp-rk055hdmipi4ma0-720p-mipi-display"></a>

### NXP RK055HDMIPI4MA0 720p MIPI显示屏

NXP RK055HDMIPI4MA0直接连接MIPI连接器J52，但需要一些修改，列表见[boards/shields/rk055hdmipi4ma0/boards/mimxrt700_evk_mimxrt798s_cm33_cpu0.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4ma0/boards/mimxrt700_evk_mimxrt798s_cm33_cpu0.overlay)。此720p面板需要较大的帧缓冲区，因此必须使用PSRAM存储区，并连接JP45的1—2脚。可按以下方式构建显示示例：（[NXP RK055HDMIPI4MA0 MIPI显示屏](https://docs.zephyrproject.org/latest/boards/shields/rk055hdmipi4ma0/doc/index.html#rk055hdmipi4ma0)）

```text
west build -b mimxrt700_evk/mimxrt798s/cm33_cpu0 --shield rk055hdmipi4ma0 samples/drivers/display
```

<a id="nxp-zc143ac72mipi-mipi-display"></a>

### NXP ZC143AC72MIPI MIPI显示屏

NXP ZC143AC72MIPI直接连接MIPI连接器J26，但需要一些修改，列表见[boards/shields/zc143ac72mipi/boards/mimxrt700_evk_mimxrt798s_cm33_cpu0.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/zc143ac72mipi/boards/mimxrt700_evk_mimxrt798s_cm33_cpu0.overlay)。可按以下方式构建显示示例：（[NXP ZC143AC72MIPI MIPI显示屏](https://docs.zephyrproject.org/latest/boards/shields/zc143ac72mipi/doc/index.html#zc143ac72mipi)）

```text
west build -b mimxrt700_evk/mimxrt798s/cm33_cpu0 --shield zc143ac72mipi samples/drivers/display
```

<a id="nxp-lcd-par-s035"></a>

### NXP LCD_PAR_S035

[NXP LCD_PAR_S035 TFT LCD模块](https://docs.zephyrproject.org/latest/boards/shields/lcd_par_s035/doc/index.html#lcd-par-s035)直接连接LCD插座J4的1—28脚，但需要一些修改，列表见[boards/shields/lcd_par_s035/boards/mimxrt700_evk_mimxrt798s_cm33_cpu0.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/lcd_par_s035/boards/mimxrt700_evk_mimxrt798s_cm33_cpu0.overlay)。连接JP7的2—3脚使用3.3 V接口，移除R60启用触摸功能。可按以下方式构建显示示例：

```text
west build -b mimxrt700_evk/mimxrt798s/cm33_cpu0 --shield lcd_par_s035_8080 samples/drivers/display
```

<a id="flash-memory-configuration"></a>

### 闪存配置（Flash Memory Configuration）

默认从XSPI0上的板载MX25UM51345G八线SPI NOR闪存启动并就地执行（XIP）。

若通过硬件返工改为在XSPI0安装Winbond W25Q512NW四线SPI NOR，则使用w25q512nw修订版本；该版本选择四线闪存器件、匹配ROM启动及XIP的闪存配置块（FCB），以及对应XSPI0时钟设置。可按以下方式构建SPI闪存示例：

```text
west build -b mimxrt700_evk@w25q512nw/mimxrt798s/cm33_cpu0 -p always samples/drivers/spi_flash
```

通过以下电阻改装，将XSPI0路由到W25Q512NW四线SPI NOR：


- 移除R396、R397、R400及R402。
- 安装R386、R694、R695、R701、R707及R708。

构建时不指定修订版本，将选择默认mx25um51345g，对应出厂八线闪存。

注意（Note）

w25q512nw版本通过LinkServer烧录，即west flash --runner linkserver；默认J-Link运行工具不支持此器件。LinkServer通过MIMXRT700_XSPI0_Quad_S.cfx算法访问安全XSPI0区域；该算法由NXP单独提供，需复制到`<LinkServer>/binaries/Flash/`。

```text
west flash --runner linkserver -- \
  --override=/board/memory/1/flash-driver=MIMXRT700_XSPI0_Quad_S.cfx
# west flash --runner linkserver -- \
#   --override=/device/memory/5/flash-driver=MIMXRT700_XSPI0_Quad_S.cfx
```

<a id="id1"></a>

### Zephyr支持资源（Support Resources）


- [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)
- [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)
- [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- NXP Zephyr主页，包含培训资源（[NXP的Zephyr专题页面](https://nxp.com/zephyr)）
- [NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## 译注

CPU0启动CPU1及HiFi 4，CPU1启动HiFi 1。RTT需非缓存区域及0x30xxxxxx安全别名地址；SD卡需JP65的1—2脚。显示控制器不支持启用数据缓存；720p帧缓冲使用PSRAM并连接JP45。四线闪存w25q512nw变体需硬件返工、LinkServer及NXP单独提供的安全XSPI0算法，默认J-Link不支持。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [i-mx-rt700-crossover-mcu-with-arm-cortex-m33-npu-dsp-and-gpu-cores:i.MX-RT700](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt700-crossover-mcu-with-arm-cortex-m33-npu-dsp-and-gpu-cores:i.MX-RT700)：HTTP Error 404: Not Found。

---

[上一章](P007_MIMXRT685-EVK.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
